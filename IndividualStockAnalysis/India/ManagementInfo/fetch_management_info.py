"""
Fetch annual reports (last 5 fiscal years) for every NIFTY Total Market
constituent, extract Chairman / Managing Director / CEO / CFO names plus
best-effort qualification + experience snippets via regex, and emit one
CSV per company summarizing 5-year management history.

Pipeline per company:
  1. screener.in -> AR PDF URLs for last 5 FYs
  2. For each AR PDF:
     - Download to /tmp (cached); 4-way concurrent across the 5 ARs
     - Extract text from first 80 pages (board profiles live in first 50-70)
     - Regex-extract (name, role) pairs for Chairman/MD/CEO/CFO/Chairperson
     - For each found person, search +/- 1500 chars for qualification keywords
       (B.Tech / IIT / IIM / MBA / CA / etc.) and experience phrases
       ("X years of experience", "previously associated with").
  3. Across the 5 ARs, dedupe by (person, role); compute years_present
     (e.g. FY22-FY26 if seen in every year, FY24-FY26 if joined later);
     status = 'current' if seen in FY26, else 'exited'.

Output (per co):
  {NSE_SYMBOL}.csv   columns: role, name, qualification, experience,
                              years_present, status, source_ars
  _fetch_log.csv     per-co status

Caveats:
  - Annual reports are 200-500 pages of varied formats; regex extraction
    of qualification + experience is best-effort. Names + designations
    are reliable; qualification/experience fields are often empty.
  - PDFs are downloaded to /tmp/mgmt_ar_cache/ (NOT stored in git).
    ~90 GB of cached downloads; the cache is purged at end of run by
    default unless --keep-cache is passed.

Usage:
  python3 fetch_management_info.py                       # all 742 cos
  python3 fetch_management_info.py --only RELIANCE,TCS   # spot check
  python3 fetch_management_info.py --skip-existing       # resume
  python3 fetch_management_info.py --keep-cache          # retain PDFs
"""

from __future__ import annotations

import argparse
import concurrent.futures
import io
import os
import re
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from html import unescape
from pathlib import Path

import pandas as pd
import PyPDF2

HERE = Path(__file__).parent
DEFAULT_OUT = HERE / "NiftyTotalMarket"
CONST_CSV = HERE.parent / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"
CACHE_DIR = Path("/tmp/mgmt_ar_cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
DELAY = 0.4
PDF_TIMEOUT = 90
HTML_TIMEOUT = 25
MAX_PAGES_TO_PARSE = 80   # board profile pages are nearly always in first 80
N_AR_YEARS = 5            # how many recent FYs to look at

ROLE_PATTERNS = {
    # Each pattern must reject "Chairman of <Committee>" / "of the Audit Committee" etc.
    # by checking that the next ~25 chars are NOT "of the ... Committee".
    "Chairman": [
        r"(?:Executive\s+|Non-?Executive\s+)?(?:Chairman|Chairperson)(?!\s+(?:of\s+the|of))",
    ],
    "Managing Director": [
        r"Managing\s+Director(?!\s+of\s)",
        r"MD\s*&\s*CEO",
        r"Joint\s+Managing\s+Director",
        r"Deputy\s+Managing\s+Director",
        r"Whole[- ]?time\s+Director",
    ],
    "CEO": [
        r"Chief\s+Executive\s+Officer",
    ],
    "CFO": [
        r"Chief\s+Financial\s+Officer",
    ],
}

# Restrict to two-to-four capitalised words, optionally one middle initial,
# no embedded punctuation (commas/parens/digits/newlines).
# Names: 2-4 capitalized tokens, allow single-letter middle initial ("D."),
# but reject digits or unusual punctuation.
NAME_TOKEN = r"[A-Z][a-zA-Z'\-]{1,20}"
NAME_MIDDLE = r"(?:[A-Z]\.?\s+)?"  # optional middle initial
NAME_RE_STRICT = (
    rf"({NAME_TOKEN}\s+{NAME_MIDDLE}{NAME_TOKEN}(?:\s+{NAME_TOKEN})?)"
)
NAME_WITH_PREFIX = (
    rf"(?:Shri|Sri|Smt\.?|Mr\.?|Ms\.?|Mrs\.?|Dr\.?)\s+{NAME_RE_STRICT}"
)

NAME_BAD_TOKEN = re.compile(
    r"\b(?:President|Chief|Officer|Director|Independent|Executive|Group|"
    r"Member|Committee|Board|Audit|Risk|Nomination|Remuneration|"
    r"Stakeholders|Counsel|Legal|Vice|Senior|Founder|Whole|Joint|"
    r"Limited|Ltd|Company|Age|Date|Shri|Sri|Mr|Ms|Mrs|Dr)\b",
    re.IGNORECASE,
)

QUAL_KEYWORDS = [
    r"B\.?\s*Tech\.?\b", r"B\.?\s*E\.?\b", r"B\.?\s*Sc\.?\b", r"B\.?\s*Com\.?\b",
    r"B\.?\s*A\.?\b", r"M\.?\s*Tech\.?\b", r"M\.?\s*Sc\.?\b", r"M\.?\s*Com\.?\b",
    r"M\.?\s*B\.?\s*A\.?\b", r"PGDM\b", r"PGDBM\b", r"MBBS\b", r"LL\.?\s*B\.?\b",
    r"LL\.?\s*M\.?\b", r"Ph\.?\s*D\.?\b", r"D\.\s*Phil\b",
    r"\bIIT[\s,]", r"\bIIM[\s,]", r"\bICAI\b", r"\bICSI\b",
    r"\bFCA\b", r"\bACA\b", r"\bCA\b", r"\bCS\b", r"\bCMA\b",
    r"Harvard\b", r"Stanford\b", r"Wharton\b", r"MIT\b", r"INSEAD\b",
    r"London\s+School\s+of\s+Economics\b", r"University\s+of\s+\w+",
]
QUAL_RE = re.compile("|".join(QUAL_KEYWORDS), re.IGNORECASE)

EXP_PATTERNS = [
    re.compile(r"over\s+(\d{1,2})\s+years?\s+of\s+(?:experience|industry experience)",
               re.IGNORECASE),
    re.compile(r"(\d{1,2})\+?\s+years?\s+of\s+(?:experience|industry experience)",
               re.IGNORECASE),
    re.compile(r"more than\s+(\d{1,2})\s+years?\s+of\s+(?:experience|industry experience)",
               re.IGNORECASE),
]


def _http_get(url: str, timeout: int = HTML_TIMEOUT) -> bytes | None:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.screener.in/",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception:
        return None


def list_annual_reports(sym: str) -> list[tuple[int, str]]:
    """Return list of (fy_year, pdf_url) for the last N_AR_YEARS years."""
    encoded = urllib.parse.quote(sym, safe="")
    for variant in ("consolidated/", ""):
        body = _http_get(f"https://www.screener.in/company/{encoded}/{variant}")
        if body:
            break
    if not body:
        return []
    html = body.decode("utf-8", errors="ignore")
    i = html.find('class="documents annual-reports')
    if i < 0:
        return []
    snippet = html[i:i + 6000]
    items = re.findall(r'<li[^>]*>(.*?)</li>', snippet, re.DOTALL)
    out = []
    for it in items:
        y = re.search(r"Financial\s+Year\s+(\d{4})", it)
        pdfs = re.findall(r'href="([^"]+\.pdf[^"]*)"', it)
        if y and pdfs:
            out.append((int(y.group(1)), pdfs[0].replace("&amp;", "&")))
    # Keep the most recent N_AR_YEARS by year desc, then return ascending
    out.sort(key=lambda x: x[0], reverse=True)
    out = out[:N_AR_YEARS]
    out.sort()
    return out


def download_ar(url: str, cache_path: Path) -> bool:
    if cache_path.exists() and cache_path.stat().st_size > 10_000:
        return True
    for attempt in range(3):
        body = _http_get(url, timeout=PDF_TIMEOUT)
        if body and body[:4] == b"%PDF":
            cache_path.write_bytes(body)
            return True
        time.sleep(2 ** attempt)
    return False


def extract_text_first_n_pages(pdf_path: Path, n: int = MAX_PAGES_TO_PARSE) -> str:
    try:
        reader = PyPDF2.PdfReader(str(pdf_path), strict=False)
    except Exception:
        return ""
    parts = []
    for i in range(min(n, len(reader.pages))):
        try:
            parts.append(reader.pages[i].extract_text() or "")
        except Exception:
            parts.append("")
    return "\n".join(parts)


def is_valid_name(s: str) -> bool:
    s = s.strip()
    parts = s.split()
    if not (2 <= len(parts) <= 4):
        return False
    if NAME_BAD_TOKEN.search(s):
        return False
    # Each token must start with an uppercase, no digits/odd punctuation
    for p in parts:
        if not re.match(r"^[A-Z][a-zA-Z'\-]{1,}\.?$", p):
            return False
    return True


def find_role_people(text: str) -> list[tuple[str, str, int]]:
    """Look for tight "<Name>, <Role>" or "<Role>: <Name>" patterns."""
    out: list[tuple[str, str, int]] = []
    role_alt = "|".join(
        "(?:" + "|".join(pats) + ")"
        for pats in ROLE_PATTERNS.values()
    )
    # Tight pattern 1: "<Prefix> <Name>, <Role>"   (very common in board profile pages)
    for m in re.finditer(NAME_WITH_PREFIX + r"\s*[,\-–]\s*(" + role_alt + r")", text):
        name = m.group(1)
        if not is_valid_name(name):
            continue
        role = _classify_role(m.group(2))
        if role:
            out.append((role, name, m.start()))
    # Tight pattern 2: "<Role>: <Name>" or "<Role> - <Name>"
    for m in re.finditer(r"(" + role_alt + r")\s*[:\-–]\s*" + NAME_WITH_PREFIX, text):
        role = _classify_role(m.group(1))
        name = m.group(2)
        if role and is_valid_name(name):
            out.append((role, name, m.start()))
    # Tight pattern 3: "Mr. NAME, ROLE of the Company" (slight variant)
    for m in re.finditer(NAME_WITH_PREFIX + r"\s+(?:is\s+)?(?:the\s+)?(" + role_alt + r")", text):
        name = m.group(1)
        if not is_valid_name(name):
            continue
        role = _classify_role(m.group(2))
        if role:
            out.append((role, name, m.start()))
    return out


def _classify_role(matched: str) -> str | None:
    s = matched.lower()
    if "managing" in s or "whole" in s or "md" in s:
        return "Managing Director"
    if "executive officer" in s:
        return "CEO"
    if "financial officer" in s:
        return "CFO"
    if "chairman" in s or "chairperson" in s:
        return "Chairman"
    return None


QUAL_VERB_RE = re.compile(
    r"\b(?:holds?|has|is|did|received|earned|completed|graduated|"
    r"alumnus|alumna)\b", re.IGNORECASE,
)


def find_qual_near(text: str, offset: int, name: str, radius: int = 800) -> str:
    """Only return a qualification snippet if it's clearly a degree statement
    near the person's name (e.g. 'holds a B.Tech from IIT Bombay')."""
    snippet = text[max(0, offset - radius): offset + radius]
    qm = QUAL_RE.search(snippet)
    if not qm:
        return ""
    # Require a degree-statement verb within 80 chars of the qualification keyword.
    win = snippet[max(0, qm.start() - 80): qm.end() + 80]
    if not QUAL_VERB_RE.search(win):
        return ""
    # Clean and return a tight 140-char window around the match.
    s = max(0, qm.start() - 50)
    e = min(len(snippet), qm.end() + 70)
    out = re.sub(r"\s+", " ", snippet[s:e].replace("\n", " ").strip())
    return out[:140]


def find_exp_near(text: str, offset: int, radius: int = 800) -> str:
    """Only return experience snippet if the pattern matches the canonical
    'X years of experience' phrasing — those are reliable."""
    snippet = text[max(0, offset - radius): offset + radius]
    for pat in EXP_PATTERNS:
        m = pat.search(snippet)
        if m:
            s = max(0, m.start() - 30)
            e = min(len(snippet), m.end() + 50)
            out = re.sub(r"\s+", " ",
                         snippet[s:e].replace("\n", " ").strip())
            return out[:140]
    return ""


def process_year(fy: int, pdf_path: Path) -> list[dict]:
    text = extract_text_first_n_pages(pdf_path)
    if not text:
        return []
    findings: dict[tuple[str, str], dict] = {}
    for role, name, offset in find_role_people(text):
        key = (role, name)
        if key in findings:
            continue
        findings[key] = {
            "fy": fy,
            "role": role,
            "name": name,
            "qualification": find_qual_near(text, offset, name),
            "experience": find_exp_near(text, offset),
        }
    return list(findings.values())


def process_company(sym: str, out_dir: Path, keep_cache: bool = False) -> str:
    ars = list_annual_reports(sym)
    if not ars:
        return "no_annual_reports"

    per_year: dict[int, list[dict]] = {}
    sym_cache = CACHE_DIR / sym.replace("&", "_AND_")
    sym_cache.mkdir(exist_ok=True)

    # Concurrent download of AR PDFs
    def dl(fy_url):
        fy, url = fy_url
        path = sym_cache / f"FY{fy}.pdf"
        ok = download_ar(url, path)
        return fy, path, ok, url

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        results = list(ex.map(dl, ars))

    n_dl = 0
    for fy, path, ok, url in results:
        if not ok:
            per_year[fy] = []
            continue
        n_dl += 1
        per_year[fy] = process_year(fy, path)
        per_year[fy] = [{**r, "source_ar_url": url} for r in per_year[fy]]

    if not any(per_year.values()):
        return f"no_extractable_people:dl={n_dl}"

    # Deduplicate across years: normalize names aggressively
    # (drop middle initials, lowercase, collapse whitespace).
    def norm(n: str) -> str:
        n = re.sub(r"\s+", " ", n.lower().strip())
        # Drop single-letter middle tokens (e.g. "A. Ambani" matches "Ambani")
        toks = [t for t in n.replace(".", "").split() if len(t) > 1]
        return " ".join(toks)

    aggregated: dict[tuple[str, str], dict] = {}
    fys_seen: dict[tuple[str, str], set[int]] = {}
    for fy, people in sorted(per_year.items()):
        for p in people:
            k = (p["role"], norm(p["name"]))
            fys_seen.setdefault(k, set()).add(fy)
            if k not in aggregated:
                aggregated[k] = {
                    "role": p["role"],
                    "name": p["name"],
                    "qualification": p["qualification"],
                    "experience": p["experience"],
                    "first_ar_url": p["source_ar_url"],
                }
            else:
                # Prefer non-empty qualification / experience from any year
                if not aggregated[k]["qualification"] and p["qualification"]:
                    aggregated[k]["qualification"] = p["qualification"]
                if not aggregated[k]["experience"] and p["experience"]:
                    aggregated[k]["experience"] = p["experience"]

    # An AR whose parse found nobody must not define "current" — an
    # unparseable latest AR is absence of evidence, not evidence of exit.
    fys_with_people = [fy for fy, people in per_year.items() if people]
    latest_fy = max(fys_with_people) if fys_with_people else max(per_year.keys())
    rows = []
    for k, v in aggregated.items():
        fys = sorted(fys_seen[k])
        years_present = f"FY{fys[0]}" if len(fys) == 1 else f"FY{fys[0]}–FY{fys[-1]}"
        if len(fys) > 1 and (fys[-1] - fys[0] + 1) != len(fys):
            years_present = ",".join(f"FY{y}" for y in fys)
        status = "current" if latest_fy in fys else "exited"
        rows.append({
            "role": v["role"],
            "name": v["name"],
            "qualification": v["qualification"],
            "experience": v["experience"],
            "years_present": years_present,
            "status": status,
            "first_seen_in_ar": v["first_ar_url"],
        })

    # Sort: current first, then by role
    role_order = {"Chairman": 0, "Managing Director": 1, "CEO": 2, "CFO": 3}
    rows.sort(key=lambda r: (r["status"] != "current",
                             role_order.get(r["role"], 99),
                             r["name"]))

    out_path = out_dir / f"{sym.replace('&', '_AND_')}.csv"
    pd.DataFrame(rows).to_csv(out_path, index=False)

    if not keep_cache:
        shutil.rmtree(sym_cache, ignore_errors=True)

    return f"ok:ars_listed={len(ars)}:downloaded={n_dl}:people_unique={len(rows)}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--only", default=None)
    ap.add_argument("--skip-existing", action="store_true")
    ap.add_argument("--keep-cache", action="store_true",
                    help="Keep downloaded AR PDFs in /tmp (default: purge)")
    ap.add_argument("--only-new", action="store_true",
                    help="Re-process ONLY companies whose latest listed "
                         "annual report is newer than the stored CSV "
                         "reflects (1 cheap listing request per company; "
                         "full AR downloads only where something changed)")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    log_csv = out_dir / "_fetch_log.csv"

    constituents = pd.read_csv(CONST_CSV)
    if args.only:
        wanted = {s.strip() for s in args.only.split(",")}
        constituents = constituents[constituents["nse_symbol"].isin(wanted)]
    symbols = constituents["nse_symbol"].astype(str).tolist()

    if args.skip_existing:
        existing = {p.stem.replace("_AND_", "&") for p in out_dir.glob("*.csv")
                    if not p.stem.startswith("_")}
        symbols = [s for s in symbols if s not in existing]

    print(f"To process: {len(symbols)} cos  "
          f"(downloads cached to {CACHE_DIR})")
    print("-" * 70)

    def stored_max_fy(sym: str) -> int:
        f = out_dir / f"{sym.replace('&', '_AND_')}.csv"
        if not f.exists():
            return 0
        try:
            import re as _re
            fys = _re.findall(r"FY(\d+)", f.read_text())
            return max(int(x) for x in fys) if fys else 0
        except Exception:
            return 0

    log_rows = []
    for i, sym in enumerate(symbols, 1):
        try:
            if args.only_new:
                ars = list_annual_reports(sym)
                latest_listed = max((fy for fy, _ in ars), default=0)
                if latest_listed and latest_listed <= stored_max_fy(sym):
                    status = f"skip:current_through_FY{latest_listed}"
                    log_rows.append({"nse_symbol": sym, "status": status})
                    if i % 25 == 0 or i == len(symbols):
                        ok = sum(1 for r in log_rows
                                 if r["status"].startswith(("ok", "skip")))
                        print(f"  [{i:4d}/{len(symbols)}] last={sym:<14s} "
                              f"ok/skip={ok}/{i} {status[:60]}")
                    time.sleep(DELAY)
                    continue
            # Hard per-company timeout: PyPDF2 can spin forever on a
            # malformed AR (observed: a 20-hour stall). A hung parse is
            # logged and skipped, never allowed to block the whole run.
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as _ex:
                fut = _ex.submit(process_company, sym, out_dir,
                                 keep_cache=args.keep_cache)
                try:
                    status = fut.result(timeout=600)
                except concurrent.futures.TimeoutError:
                    status = "timeout:600s (hung AR parse — skipped)"
                    fut.cancel()
        except Exception as e:
            status = f"exception:{type(e).__name__}:{str(e)[:60]}"
        log_rows.append({"nse_symbol": sym, "status": status})

        if i % 5 == 0 or i == len(symbols):
            ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
            print(f"  [{i:4d}/{len(symbols)}] last={sym:<14s} ok={ok}/{i} "
                  f"last_status={status[:75]}")
        time.sleep(DELAY)

    # Merge with any existing log
    if log_csv.exists():
        existing = pd.read_csv(log_csv)
        existing = existing[~existing["nse_symbol"].isin(
            {r["nse_symbol"] for r in log_rows})]
        out_log = pd.concat([existing, pd.DataFrame(log_rows)], ignore_index=True)
    else:
        out_log = pd.DataFrame(log_rows)
    out_log.to_csv(log_csv, index=False)

    if not args.keep_cache:
        print(f"\nPurging cache {CACHE_DIR} ...")
        shutil.rmtree(CACHE_DIR, ignore_errors=True)

    print("-" * 70)
    ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
    print(f"DONE. ok={ok}/{len(symbols)}")
    print(f"Log: {log_csv}")


if __name__ == "__main__":
    main()
