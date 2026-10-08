"""
fetch_announcements.py — the last year of exchange filings that bear on
spin-offs, demergers and related special situations, for every
NiftyTotalMarket company.

    python3 fetch_announcements.py                 # NSE + BSE, 365 days
    python3 fetch_announcements.py --days 400      # a longer lookback
    python3 fetch_announcements.py --no-bse        # NSE only (fast)
    python3 fetch_announcements.py --no-pdf        # skip attachment text
    python3 fetch_announcements.py --only SUNPHARMA,TATAMOTORS

WHAT IS PULLED
  NSE  — the corporate-announcements feed (`/api/corporate-announcements`),
         month by month over the lookback window, for the whole exchange;
         the rows for NiftyTotalMarket companies are kept and each one is
         CLASSIFIED (see `classify`): demerger / spin-off, merger,
         slump sale, subsidiary listing, rights issue, scheme (other),
         capital reduction, or none. Rows with a restructuring kind are
         stored, and their attachment PDFs are downloaded from
         nsearchives and reduced to text.
  BSE  — BSE's announcement API sits behind a WAF that refuses this
         environment, so two honest routes are used instead: (1) BSE's
         own RSS feed of the day's announcements, snapshotted on every
         run and accumulated (it grows forward from the first run), and
         (2) the BSE-sourced "recent" and "important" announcement lists
         screener.in publishes per company. BSE attachment PDFs
         (bseindia.com/xml-data/corpfiling) download normally. Every
         NiftyTotalMarket company is NSE-listed, and Regulation 30
         disclosures are filed with both exchanges, so the NSE feed is
         the complete one-year record; the BSE routes are the mirror.
  Codes — each company's BSE scrip code and screener id are resolved
         once from its screener page and kept in `_bse_codes.csv`.

OUTPUTS (NiftyTotalMarket/)
  _announcements_restructuring.csv   one row per matched filing, NSE+BSE
  text/{SYMBOL}_{id}.txt             the attachment's text (PyPDF2)
  _bse_codes.csv                     symbol → bse_code, screener_id
  _bse_rss_snapshots.csv             every BSE RSS item ever seen, deduped
  _fetch_log.csv, _README.md
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import datetime as dt
import html as html_mod
import io
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent
OUT_DIR = HERE / "NiftyTotalMarket"
TEXT_DIR = OUT_DIR / "text"
CONSTITUENTS = INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"
MATCHES = OUT_DIR / "_announcements_restructuring.csv"
CODES = OUT_DIR / "_bse_codes.csv"
RSS_STORE = OUT_DIR / "_bse_rss_snapshots.csv"
LOG = OUT_DIR / "_fetch_log.csv"
README = OUT_DIR / "_README.md"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
NSE_API = ("https://www.nseindia.com/api/corporate-announcements"
           "?index=equities&from_date={frm}&to_date={to}")
BSE_RSS = "https://www.bseindia.com/data/xml/announcements.xml"
SCREENER = "https://www.screener.in"
MAX_PDF_MB = 25
MAX_TEXT_CHARS = 400_000
MAX_PAGES = 300
DELAY = 0.4

FIELDS = ["date", "symbol", "company", "source", "category", "kind", "tags",
          "headline", "attachment", "ann_id", "file_size", "text_file"]


# ------------------------------------------------------------ classifying

# Patterns are applied to the category + headline (lower-cased). A row may
# carry several tags; `kind` is the first tag in KIND_ORDER that matched.
PATTERNS = {
    "demerger": re.compile(
        r"\bde-?merg|spin[\s-]?off|hiv(e|ing)[\s-]?off|carve[\s-]?out|"
        r"separat(e|ion) (of )?(the |its )?\w* ?business|"
        r"scheme of arrangement.*demerg|demerg.*scheme of arrangement|"
        r"value[\s-]?unlock"),
    "subsidiary_listing": re.compile(
        r"(ipo|initial public offer|public (issue|offer)|offer for sale|"
        r"listing) (of|for) (its |the |a |our )?(material |wholly[- ]owned |"
        r"step[- ]down )?(subsidiar|arm|unit)|"
        r"(subsidiar|arm)\w*.{0,60}\b(ipo|initial public offer|draft red "
        r"herring|drhp|listing of (its|the) (equity )?shares)|"
        r"\bdrhp\b"),
    "slump_sale": re.compile(r"slump sale|business transfer agreement|\bbta\b"),
    "merger": re.compile(
        r"amalgamat|\bmerger\b|merge[sd]? (with|into)|scheme of amalgamation"),
    "capital_reduction": re.compile(
        r"reduction of (share )?capital|capital reduction|buy[\s-]?back"),
    "rights_issue": re.compile(r"rights? (issue|offering|entitlement)|letter of offer"),
    "scheme_other": re.compile(r"scheme of arrangement|composite scheme|"
                               r"\bnclt\b|national company law tribunal"),
}
KIND_ORDER = ["demerger", "subsidiary_listing", "slump_sale", "merger",
              "capital_reduction", "rights_issue", "scheme_other"]
# NSE categories that are restructuring by definition even without words
CATEGORY_KINDS = {"Scheme of Arrangement": "scheme_other",
                  "Demerger": "demerger",
                  "Amalgamation/Merger": "merger",
                  "Rights Issue": "rights_issue"}
# Noise: these categories never hold a restructuring signal, whatever the
# headline says (a DP certificate mentioning "demerged shares", say)
NOISE_CATEGORIES = {
    "Certificate under SEBI (Depositories and Participants) Regulations, 2018",
    "Trading Window", "Structural Digital Database", "Spurt in Volume",
    "Price movement", "Copy of Newspaper Publication",
}
NOISE_PREFIXES = ("Issue of Duplicate Share Cer", "Loss of Share Certificate",
                  "Certificate under SEBI")


def classify(category: str, headline: str) -> tuple[str, list[str]]:
    """(kind, tags) for one filing; kind == "" when it is not a
    restructuring filing. Newspaper copies and the like are noise."""
    if category in NOISE_CATEGORIES or category.startswith(NOISE_PREFIXES):
        return "", []
    text = f"{category or ''} {headline or ''}".lower()
    tags = [k for k in KIND_ORDER if PATTERNS[k].search(text)]
    cat_kind = CATEGORY_KINDS.get(category)
    if cat_kind and cat_kind not in tags:
        tags.append(cat_kind)
    if not tags:
        return "", []
    # a scheme that only amalgamates is a merger, not a spin-off; a
    # scheme that demerges is a demerger even if it also merges parts
    tags = sorted(set(tags), key=KIND_ORDER.index)
    return tags[0], tags


# --------------------------------------------------------------- universe

def universe() -> dict[str, str]:
    """{symbol: company_name} for the official NiftyTotalMarket members
    (the index list, not the wider size list the Darvas screen adds)."""
    out = {}
    with open(CONSTITUENTS) as fh:
        for r in csv.DictReader(fh):
            src = r.get("source") or "official"
            if src in ("official", "both"):
                out[r["nse_symbol"]] = r.get("company_name") or r["nse_symbol"]
    return out


# ----------------------------------------------------------------- http

def _get(url: str, timeout: int = 60, headers: dict | None = None,
         retries: int = 3) -> tuple[int, bytes]:
    h = {"User-Agent": UA, "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9"}
    h.update(headers or {})
    last = 0
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=h)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            last = e.code
            if e.code in (404, 410):
                return e.code, b""
            time.sleep(1.5 * (attempt + 1))
        except Exception:                  # noqa: BLE001 — retried
            last = 0
            time.sleep(1.5 * (attempt + 1))
    return last, b""


# ------------------------------------------------------------------- NSE

def month_windows(end: dt.date, days: int) -> list[tuple[dt.date, dt.date]]:
    """Consecutive windows of at most one month covering [end-days, end]
    — the NSE feed is happiest with short ranges."""
    start = end - dt.timedelta(days=days)
    out, a = [], start
    while a <= end:
        nxt = (a.replace(day=1) + dt.timedelta(days=32)).replace(day=1)
        b = min(nxt - dt.timedelta(days=1), end)
        out.append((a, b))
        a = b + dt.timedelta(days=1)
    return out


def nse_fetch(frm: dt.date, to: dt.date) -> list[dict]:
    url = NSE_API.format(frm=frm.strftime("%d-%m-%Y"), to=to.strftime("%d-%m-%Y"))
    code, body = _get(url, timeout=180, headers={
        "Accept": "application/json",
        "Referer": "https://www.nseindia.com/companies-listing/"
                   "corporate-filings-announcements"})
    if code != 200 or not body:
        raise RuntimeError(f"NSE feed {frm}→{to}: HTTP {code}")
    data = json.loads(body)
    if not isinstance(data, list):
        raise RuntimeError(f"NSE feed {frm}→{to}: unexpected payload")
    return data


def _nse_date(s: str) -> str:
    """'08-Oct-2025 23:59:43' -> '2025-10-08'."""
    try:
        return dt.datetime.strptime(s[:11], "%d-%b-%Y").date().isoformat()
    except ValueError:
        return s[:10]


def nse_rows(feed: list[dict], members: dict[str, str]) -> list[dict]:
    """Keep the NiftyTotalMarket rows that classify as restructuring, in
    the stored schema."""
    out = []
    for r in feed:
        sym = (r.get("symbol") or "").strip()
        if sym not in members:
            continue
        kind, tags = classify(r.get("desc") or "", r.get("attchmntText") or "")
        if not kind:
            continue
        out.append({
            "date": _nse_date(r.get("an_dt") or ""), "symbol": sym,
            "company": members[sym], "source": "NSE",
            "category": r.get("desc") or "", "kind": kind,
            "tags": "|".join(tags),
            "headline": re.sub(r"\s+", " ", r.get("attchmntText") or "").strip(),
            "attachment": r.get("attchmntFile") or "",
            "ann_id": str(r.get("seq_id") or r.get("dt") or ""),
            "file_size": r.get("attFileSize") or "", "text_file": ""})
    return out


# ------------------------------------------------------------------- BSE

def parse_bse_rss(xml: str) -> list[dict]:
    """BSE's announcements RSS -> [{bse_code, company, headline, link,
    date}] — today's filings, every run."""
    out = []
    for item in re.findall(r"<item>(.*?)</item>", xml, re.S):
        def tag(name):
            m = re.search(rf"<{name}>(.*?)</{name}>", item, re.S)
            return (m.group(1) if m else "").strip()
        title = tag("title")
        m = re.match(r"(.*?)\s*\((\d{5,6})\)\s*$", title)
        company, code = (m.group(1), m.group(2)) if m else (title, tag("scripcode"))
        pub = tag("pubDate")
        try:
            date = dt.datetime.strptime(pub[:11], "%d-%b-%Y").date().isoformat()
        except ValueError:
            date = pub[:10]
        out.append({"bse_code": code, "company": company,
                    "headline": re.sub(r"\s+", " ", tag("description")),
                    "link": tag("link"), "date": date})
    return out


def parse_screener_company(html: str) -> dict:
    """screener id and BSE code from a company page."""
    cid = re.search(r'data-company-id="(\d+)"', html)
    bse = re.search(r"bseindia\.com/stock-share-price/[^\"']*?/(\d{6})/", html)
    if not bse:
        bse = re.search(r"BSE:\s*</span>\s*(\d{6})|BSE:\s*(\d{6})", html)
    code = (bse.group(1) or bse.group(2)) if bse and bse.lastindex and \
        bse.lastindex >= 2 else (bse.group(1) if bse else "")
    return {"screener_id": cid.group(1) if cid else "", "bse_code": code or ""}


def parse_screener_announcements(html: str, year_hint: int) -> list[dict]:
    """The BSE-sourced announcement list screener renders per company:
    [{date, headline, link, note}]. Dates come as '7 Oct' (this year) or
    '12 Oct 2025'; the ISO form in the <time> tag is preferred."""
    out = []
    for li in re.findall(r"<li[^>]*>(.*?)</li>", html, re.S):
        href = re.search(r'href="(https?://[^"]+)"', li)
        if not href:
            continue
        iso = re.search(r'datetime="(\d{4}-\d{2}-\d{2})', li)
        if iso:
            date = iso.group(1)
        else:
            d = re.search(r">\s*(\d{1,2})\s+(\w{3})(?:\s+(\d{4}))?\s*<", li)
            if not d:
                continue
            y = int(d.group(3) or year_hint)
            try:
                date = dt.datetime.strptime(
                    f"{d.group(1)} {d.group(2)} {y}", "%d %b %Y").date().isoformat()
            except ValueError:
                continue
        text = html_mod.unescape(re.sub(r"<[^>]+>", " ", li))
        text = re.sub(r"\s+", " ", text).strip()
        # the headline is the text before the date; the note follows it
        parts = re.split(r"\b\d{1,2} \w{3}(?: \d{4})?\b", text, maxsplit=1)
        headline = parts[0].strip(" -")
        note = parts[1].strip(" -") if len(parts) > 1 else ""
        out.append({"date": date, "headline": headline, "link": href.group(1),
                    "note": note})
    return out


def screener_codes(symbol: str) -> dict:
    code, body = _get(f"{SCREENER}/company/{symbol}/consolidated/", timeout=30,
                      headers={"Referer": f"{SCREENER}/"})
    if code != 200:
        code, body = _get(f"{SCREENER}/company/{symbol}/", timeout=30,
                          headers={"Referer": f"{SCREENER}/"})
    if code != 200 or not body:
        return {"screener_id": "", "bse_code": ""}
    return parse_screener_company(body.decode("utf-8", "replace"))


def screener_announcements(screener_id: str) -> list[dict]:
    rows = []
    for kind in ("recent", "important"):
        code, body = _get(f"{SCREENER}/announcements/{kind}/{screener_id}/",
                          timeout=30, headers={"Referer": f"{SCREENER}/",
                                               "X-Requested-With": "XMLHttpRequest"})
        if code == 200 and body:
            rows += parse_screener_announcements(body.decode("utf-8", "replace"),
                                                 dt.date.today().year)
    seen, out = set(), []
    for r in rows:
        if r["link"] in seen:
            continue
        seen.add(r["link"])
        out.append(r)
    return out


def bse_pdf_url(link: str) -> str:
    """screener links go through AnnPdfOpen.aspx?Pname=<file>; the file
    itself lives under xml-data/corpfiling/AttachLive."""
    m = re.search(r"Pname=([^&]+)", link)
    if m:
        return ("https://www.bseindia.com/xml-data/corpfiling/AttachLive/"
                + m.group(1))
    return link


# ----------------------------------------------------------------- text

def pdf_text(data: bytes) -> str:
    import PyPDF2                                   # noqa: PLC0415
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(data), strict=False)
    except Exception:                               # noqa: BLE001
        return ""
    parts, n = [], 0
    for page in reader.pages[:MAX_PAGES]:
        try:
            t = page.extract_text() or ""
        except Exception:                           # noqa: BLE001
            t = ""
        parts.append(t)
        n += len(t)
        if n > MAX_TEXT_CHARS:
            break
    text = "\n".join(parts)
    text = re.sub(r"[\x00-\x08\x0b-\x1f]", "", text)
    return text[:MAX_TEXT_CHARS]


def _size_mb(s: str) -> float:
    m = re.match(r"([\d.]+)\s*(KB|MB|GB)", s or "", re.I)
    if not m:
        return 0.0
    v, u = float(m.group(1)), m.group(2).upper()
    return v / 1024 if u == "KB" else v * 1024 if u == "GB" else v


def fetch_text(row: dict) -> str:
    """Download the attachment, store its text, return the text path (or
    a reason it was skipped)."""
    url = row["attachment"]
    if not url or not url.lower().endswith(".pdf"):
        return ""
    if _size_mb(row.get("file_size", "")) > MAX_PDF_MB:
        return f"skipped:{row['file_size']}"
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", row["ann_id"])[:40]
    path = TEXT_DIR / f"{row['symbol']}_{safe}.txt"
    if path.exists() and path.stat().st_size > 0:
        return str(path.relative_to(OUT_DIR))
    referer = ("https://www.bseindia.com/" if "bseindia" in url
               else "https://www.nseindia.com/")
    code, body = _get(url, timeout=120, headers={"Referer": referer,
                                                  "Accept": "application/pdf,*/*"})
    if code != 200 or not body[:4] == b"%PDF":
        return f"failed:http{code}"
    if len(body) > MAX_PDF_MB * 1024 * 1024:
        return "skipped:oversize"
    text = pdf_text(body)
    path.write_text(text if text else "(no extractable text)")
    return str(path.relative_to(OUT_DIR))


# ----------------------------------------------------------------- store

def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path) as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def merge_rows(old: list[dict], new: list[dict]) -> list[dict]:
    """Union by (source, ann_id) — a re-run adds, never duplicates;
    a row that gained a text file keeps it."""
    by = {(r["source"], r["ann_id"]): r for r in old}
    for r in new:
        k = (r["source"], r["ann_id"])
        if k in by and by[k].get("text_file") and not r.get("text_file"):
            r = {**r, "text_file": by[k]["text_file"]}
        by[k] = r
    return sorted(by.values(), key=lambda r: (r["date"], r["symbol"], r["ann_id"]))


# ------------------------------------------------------------------ main

def run(days: int = 365, bse: bool = True, pdf: bool = True,
        only: set[str] | None = None, workers: int = 4,
        today: dt.date | None = None) -> dict:
    today = today or dt.date.today()
    members = universe()
    if only:
        members = {s: n for s, n in members.items() if s in only}
    log: list[dict] = []
    cutoff = (today - dt.timedelta(days=days)).isoformat()

    def note(stage, detail):
        log.append({"stage": stage, "detail": detail,
                    "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")})
        print(f"[{stage}] {detail}", file=sys.stderr)

    # ---- NSE, month by month
    rows: list[dict] = []
    total = 0
    for a, b in month_windows(today, days):
        try:
            feed = nse_fetch(a, b)
        except RuntimeError as e:
            note("nse", f"{a}→{b} FAILED: {e}")
            continue
        got = nse_rows(feed, members)
        total += len(feed)
        rows += got
        note("nse", f"{a}→{b}: {len(feed)} filings, {len(got)} restructuring "
                    f"rows for the universe")
        time.sleep(DELAY)
    note("nse", f"total {total} filings read, {len(rows)} kept")

    # ---- BSE: codes, RSS snapshot, screener lists
    if bse:
        codes = {r["symbol"]: r for r in read_csv(CODES)}
        missing = [s for s in members if not codes.get(s, {}).get("screener_id")]
        if missing:
            note("bse", f"resolving BSE codes for {len(missing)} companies")
            with cf.ThreadPoolExecutor(max_workers=workers) as ex:
                for sym, got in zip(missing, ex.map(screener_codes, missing)):
                    codes[sym] = {"symbol": sym, **got}
                    time.sleep(DELAY / workers)
            write_csv(CODES, sorted(codes.values(), key=lambda r: r["symbol"]),
                      ["symbol", "bse_code", "screener_id"])
        by_code = {c["bse_code"]: s for s, c in codes.items() if c.get("bse_code")}
        try:
            code, body = _get(BSE_RSS, timeout=60,
                              headers={"Referer": "https://www.bseindia.com/"})
            rss = parse_bse_rss(body.decode("utf-8", "replace")) if code == 200 else []
            store = read_csv(RSS_STORE)
            seen = {r["link"] for r in store}
            fresh = [r for r in rss if r["link"] not in seen]
            store += fresh
            write_csv(RSS_STORE, store, ["date", "bse_code", "company", "headline", "link"])
            note("bse", f"RSS snapshot: {len(rss)} items today, {len(fresh)} new "
                        f"(store {len(store)})")
            for r in store:
                sym = by_code.get(r["bse_code"])
                if not sym or sym not in members or r["date"] < cutoff:
                    continue
                kind, tags = classify("", r["headline"])
                if kind:
                    rows.append({"date": r["date"], "symbol": sym,
                                 "company": members[sym], "source": "BSE-RSS",
                                 "category": "", "kind": kind, "tags": "|".join(tags),
                                 "headline": r["headline"], "attachment": r["link"],
                                 "ann_id": Path(r["link"]).stem, "file_size": "",
                                 "text_file": ""})
        except Exception as e:                        # noqa: BLE001
            note("bse", f"RSS FAILED: {e}")
        ids = [(s, codes[s]["screener_id"]) for s in members
               if codes.get(s, {}).get("screener_id")]
        note("bse", f"screener BSE-sourced lists for {len(ids)} companies")
        with cf.ThreadPoolExecutor(max_workers=workers) as ex:
            for (sym, _), anns in zip(ids, ex.map(lambda p: screener_announcements(p[1]), ids)):
                for a in anns:
                    if a["date"] < cutoff:
                        continue
                    kind, tags = classify("", f"{a['headline']} {a['note']}")
                    if not kind:
                        continue
                    rows.append({"date": a["date"], "symbol": sym,
                                 "company": members[sym], "source": "BSE-screener",
                                 "category": a["headline"][:80], "kind": kind,
                                 "tags": "|".join(tags),
                                 "headline": (a["note"] or a["headline"]),
                                 "attachment": bse_pdf_url(a["link"]),
                                 "ann_id": Path(bse_pdf_url(a["link"])).stem,
                                 "file_size": "", "text_file": ""})
                time.sleep(DELAY / workers)

    merged = merge_rows(read_csv(MATCHES) if not only else
                        [r for r in read_csv(MATCHES) if r["symbol"] not in members],
                        rows)
    merged = [r for r in merged if r["date"] >= cutoff or r["symbol"] not in members]

    # ---- attachment text
    if pdf:
        todo = [r for r in merged if r["symbol"] in members
                and (not r.get("text_file") or r["text_file"].startswith("failed"))
                and r["attachment"]]
        note("text", f"fetching text for {len(todo)} attachments")
        with cf.ThreadPoolExecutor(max_workers=workers) as ex:
            for r, res in zip(todo, ex.map(fetch_text, todo)):
                r["text_file"] = res
        ok = sum(1 for r in merged if r.get("text_file", "").startswith("text/"))
        note("text", f"{ok} attachments with text on file")

    write_csv(MATCHES, merged, FIELDS)
    write_csv(LOG, log, ["stage", "detail", "at"])
    kinds: dict[str, int] = {}
    for r in merged:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    README.write_text(_readme(today, days, len(members), len(merged), kinds,
                              len({r["symbol"] for r in merged})))
    note("done", f"{len(merged)} rows, {len({r['symbol'] for r in merged})} "
                 f"companies, kinds {kinds}")
    return {"rows": len(merged), "kinds": kinds, "log": log}


def _readme(today, days, n_members, n_rows, kinds, n_cos) -> str:
    k = "\n".join(f"- `{a}`: {b}" for a, b in sorted(kinds.items(), key=lambda x: -x[1]))
    return f"""# NiftyTotalMarket — restructuring filings (spin-offs, demergers, schemes)

**Generated:** {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}
**Window:** the {days} days to {today} · **Universe:** {n_members} official
NiftyTotalMarket constituents · **Rows:** {n_rows} filings across {n_cos} companies

## What is here
- `_announcements_restructuring.csv` — one row per exchange filing that
  classifies as a restructuring event: `date, symbol, company, source
  (NSE | BSE-RSS | BSE-screener), category, kind, tags, headline,
  attachment, ann_id, file_size, text_file`.
- `text/` — the attachment's extracted text, `{{SYMBOL}}_{{ann_id}}.txt`.
- `_bse_codes.csv` — symbol → BSE scrip code and screener id.
- `_bse_rss_snapshots.csv` — BSE's daily RSS, accumulated run over run.
- `_fetch_log.csv` — what each run did.

## Kinds (first matching tag wins; all tags kept in `tags`)
{k}

## Sources, honestly
NSE's corporate-announcements API is read month by month for the whole
exchange and filtered to the universe — this is the complete one-year
record, since every member is NSE-listed and Regulation 30 disclosures
go to both exchanges. BSE's announcement API refuses this environment
(Akamai), so BSE is covered by its daily RSS feed (accumulating forward
from the first run) and by the BSE-sourced per-company lists on
screener.in; BSE attachment PDFs download normally.

Re-run: `python3 ../fetch_announcements.py` (adds, never duplicates).
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=365)
    ap.add_argument("--no-bse", action="store_true")
    ap.add_argument("--no-pdf", action="store_true")
    ap.add_argument("--only", default="")
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    only = {s.strip().upper() for s in a.only.split(",") if s.strip()} or None
    run(days=a.days, bse=not a.no_bse, pdf=not a.no_pdf, only=only,
        workers=a.workers)


if __name__ == "__main__":
    main()
