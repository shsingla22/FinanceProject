"""
fetch_presentations.py — annual reports and quarterly investor
presentations for named NiftyTotalMarket companies, saved in the same
hierarchy as BalanceSheet/ and ConferenceCalls/.

    python3 fetch_presentations.py --only THOMASCOOK,HINDUNILVR
    python3 fetch_presentations.py --only TMPV --years 3 --ppt-quarters 6

SOURCE
  screener.in's company page lists every annual report (BSE-hosted PDF)
  and, per quarterly call, the raw transcript and the investor
  presentation ("PPT", BSE-hosted). Those links are followed; the PDFs
  are downloaded from bseindia.com and reduced to text WITH PAGE MARKERS
  (`=== page N ===`) so any number lifted from them can be cited to a
  page.

OUTPUTS
  InvestorPresentations/NiftyTotalMarket/{SYMBOL}/
      {YYYY-MM}_presentation.pdf / .txt     the quarterly presentations
      _index.csv                             label, url, file, pages, status
  AnnualReports/NiftyTotalMarket/{SYMBOL}/
      Annual_Report_{YYYY}.pdf / .txt        the last `--years` reports
      _index.csv
  InvestorPresentations/NiftyTotalMarket/_concall_links.csv
      symbol, call label, transcript url, presentation url — the source
      links for every quarterly call on file
  InvestorPresentations/NiftyTotalMarket/_fetch_log.csv

The PDFs stay on disk beside their text (they are large and are listed
in .gitignore); the text files and indexes are what the repository
keeps, and this script re-fetches any PDF on demand.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent
PPT_DIR = HERE / "NiftyTotalMarket"
AR_DIR = INDIA / "AnnualReports" / "NiftyTotalMarket"
LINKS = PPT_DIR / "_concall_links.csv"
LOG = PPT_DIR / "_fetch_log.csv"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
SCREENER = "https://www.screener.in"
DELAY = 0.5
MAX_PAGES = 600
MAX_MB = 60
_MONTHS = {m: i + 1 for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


# ----------------------------------------------------------------- http

def _get(url: str, timeout: int = 120, referer: str = "") -> tuple[int, bytes]:
    h = {"User-Agent": UA, "Accept": "*/*"}
    if referer:
        h["Referer"] = referer
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h),
                                        timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return e.code, b""
            time.sleep(1.5 * (attempt + 1))
            last = e.code
        except Exception:                      # noqa: BLE001
            time.sleep(1.5 * (attempt + 1))
            last = 0
    return last, b""


def bse_direct(url: str) -> str:
    """AnnPdfOpen.aspx?Pname=<file> -> the file under AttachLive."""
    m = re.search(r"Pname=([^&]+)", url)
    return ("https://www.bseindia.com/xml-data/corpfiling/AttachLive/" + m.group(1)
            if m else url)


# -------------------------------------------------------------- parsing

def parse_company_page(html: str) -> dict:
    """{annual_reports: [(year, url)], calls: [(label, transcript, ppt)]}."""
    out = {"annual_reports": [], "calls": []}
    m = re.search(r'class="documents annual-reports flex-column".*?<ul class="list-links">(.*?)</ul>',
                  html, re.S)
    if m:
        for li in re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.S):
            a = re.search(r'href="(https?://[^"]+)"[^>]*>\s*(?:Annual Report|Financial Year)\s*(\d{4})', li, re.S)
            if a:
                out["annual_reports"].append((int(a.group(2)), a.group(1).replace("&amp;", "&")))
    m = re.search(r'class="documents concalls flex-column".*?<ul class="list-links">(.*?)</ul>',
                  html, re.S)
    if m:
        for li in re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.S):
            d = re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})\b", li)
            if not d:
                continue
            label = f"{d.group(1)} {d.group(2)}"
            tr = re.search(r'href="([^"]+)"[^>]*title="Raw Transcript"', li)
            ppt = re.search(r'href="([^"]+)"[^>]*>\s*PPT\s*<', li)
            out["calls"].append((label,
                                 tr.group(1).replace("&amp;", "&") if tr else "",
                                 ppt.group(1).replace("&amp;", "&") if ppt else ""))
    return out


def label_date(label: str) -> dt.date:
    mon, yr = label.split()
    return dt.date(int(yr), _MONTHS[mon], 1)


# ----------------------------------------------------------------- text

def pdf_text_pages(data: bytes) -> tuple[str, int]:
    """Text with `=== page N ===` markers, and the page count."""
    import PyPDF2                                  # noqa: PLC0415
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(data), strict=False)
    except Exception:                              # noqa: BLE001
        return "", 0
    parts = []
    n = len(reader.pages)
    for i, page in enumerate(reader.pages[:MAX_PAGES], 1):
        try:
            t = page.extract_text() or ""
        except Exception:                          # noqa: BLE001
            t = ""
        parts.append(f"\n=== page {i} ===\n{t}")
    text = re.sub(r"[\x00-\x08\x0b-\x1f]", "", "".join(parts))
    return text, n


def download_doc(url: str, pdf_path: Path, txt_path: Path) -> dict:
    """Fetch (once) and reduce to text; returns a status record."""
    if txt_path.exists() and txt_path.stat().st_size > 50:
        return {"status": "cached", "pages": "", "file": pdf_path.name, "text_file": txt_path.name}
    # AnnPdfOpen.aspx redirects to the file (AttachLive for recent filings,
    # AttachHis for older ones); urllib follows it. Fall back to both paths.
    code, body = _get(url, referer="https://www.bseindia.com/")
    if code != 200 or body[:4] != b"%PDF":
        for base in ("AttachLive", "AttachHis"):
            alt = bse_direct(url).replace("AttachLive", base)
            code, body = _get(alt, referer="https://www.bseindia.com/")
            if code == 200 and body[:4] == b"%PDF":
                break
    if code != 200 or body[:4] != b"%PDF":
        return {"status": f"failed:http{code}", "pages": "", "file": "", "text_file": ""}
    if len(body) > MAX_MB * 1024 * 1024:
        return {"status": "skipped:oversize", "pages": "", "file": "", "text_file": ""}
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path.write_bytes(body)
    text, n = pdf_text_pages(body)
    txt_path.write_text(text if text.strip() else "(no extractable text)")
    return {"status": "ok", "pages": n, "file": pdf_path.name, "text_file": txt_path.name}


# ----------------------------------------------------------------- store

def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path) as fh:
        return list(csv.DictReader(fh))


def _write(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


INDEX_FIELDS = ["symbol", "kind", "label", "url", "file", "text_file", "pages", "status", "fetched"]


def fetch_company(symbol: str, years: int = 3, ppt_quarters: int = 12,
                  today: dt.date | None = None) -> dict:
    today = today or dt.date.today()
    code, body = _get(f"{SCREENER}/company/{symbol}/consolidated/", timeout=40,
                      referer=f"{SCREENER}/")
    if code != 200:
        code, body = _get(f"{SCREENER}/company/{symbol}/", timeout=40, referer=f"{SCREENER}/")
    if code != 200 or not body:
        return {"symbol": symbol, "status": f"screener:http{code}", "annual": 0, "ppt": 0}
    page = parse_company_page(body.decode("utf-8", "replace"))
    stamp = today.isoformat()

    # annual reports: the last `years` fiscal years on offer
    ar_rows = {r["label"]: r for r in _read(AR_DIR / symbol / "_index.csv")}
    for yr, url in sorted(page["annual_reports"], reverse=True)[:years]:
        label = f"Annual Report {yr}"
        rec = download_doc(url, AR_DIR / symbol / f"Annual_Report_{yr}.pdf",
                           AR_DIR / symbol / f"Annual_Report_{yr}.txt")
        ar_rows[label] = {"symbol": symbol, "kind": "annual_report", "label": label,
                          "url": url, **rec, "fetched": stamp}
        time.sleep(DELAY)
    if ar_rows:
        _write(AR_DIR / symbol / "_index.csv",
               sorted(ar_rows.values(), key=lambda r: r["label"], reverse=True), INDEX_FIELDS)

    # presentations: the last `ppt_quarters` calls that have one
    ppt_rows = {r["label"]: r for r in _read(PPT_DIR / symbol / "_index.csv")}
    calls = sorted(page["calls"], key=lambda c: label_date(c[0]), reverse=True)
    n = 0
    for label, _tr, ppt in calls:
        if not ppt or n >= ppt_quarters:
            continue
        d = label_date(label)
        rec = download_doc(ppt, PPT_DIR / symbol / f"{d:%Y-%m}_presentation.pdf",
                           PPT_DIR / symbol / f"{d:%Y-%m}_presentation.txt")
        ppt_rows[label] = {"symbol": symbol, "kind": "presentation", "label": label,
                           "url": ppt, **rec, "fetched": stamp}
        n += 1
        time.sleep(DELAY)
    if ppt_rows:
        _write(PPT_DIR / symbol / "_index.csv",
               sorted(ppt_rows.values(), key=lambda r: label_date(r["label"]), reverse=True),
               INDEX_FIELDS)

    # the call links, for citations
    links = {(r["symbol"], r["label"]): r for r in _read(LINKS)}
    for label, tr, ppt in calls:
        links[(symbol, label)] = {"symbol": symbol, "label": label,
                                 "transcript_url": tr, "presentation_url": ppt}
    _write(LINKS, sorted(links.values(), key=lambda r: (r["symbol"], label_date(r["label"]))),
           ["symbol", "label", "transcript_url", "presentation_url"])
    return {"symbol": symbol, "status": "ok",
            "annual": sum(1 for r in ar_rows.values() if r["status"] in ("ok", "cached")),
            "ppt": sum(1 for r in ppt_rows.values() if r["status"] in ("ok", "cached")),
            "calls": len(calls)}


def run(symbols: list[str], years: int = 3, ppt_quarters: int = 12) -> list[dict]:
    log = {r["symbol"]: r for r in _read(LOG)}
    out = []
    for s in symbols:
        r = fetch_company(s, years, ppt_quarters)
        r["at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        print(f"[{s}] {r}", file=sys.stderr)
        log[s] = r
        out.append(r)
        _write(LOG, sorted(log.values(), key=lambda r: r["symbol"]),
               ["symbol", "status", "annual", "ppt", "calls", "at"])
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", required=True, help="comma-separated NSE symbols")
    ap.add_argument("--years", type=int, default=3)
    ap.add_argument("--ppt-quarters", type=int, default=12)
    a = ap.parse_args()
    run([s.strip().upper() for s in a.only.split(",") if s.strip()], a.years, a.ppt_quarters)


if __name__ == "__main__":
    main()
