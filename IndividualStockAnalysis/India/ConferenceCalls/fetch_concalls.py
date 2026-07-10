"""
Fetch quarterly conference-call transcripts (last 3 fiscal years) for
every NIFTY Total Market constituent, extract text from each PDF, and
emit one consolidated PDF per company with sections sorted oldest-first
to newest-last.

Source chain:
  1. screener.in's company page exposes a "Concalls" section listing
     each quarter's transcript URL (mostly hosted on bseindia.com).
  2. We download each transcript PDF, extract text with PyPDF2, and
     render the combined text into a single PDF using reportlab,
     prefixed by a quarter header.

Inputs:
  ../NiftyTotalMarket/niftytotalmarket_constituents.csv (742 cos)

Outputs (in NiftyTotalMarket/):
  {NSE_SYMBOL}.pdf     consolidated text-only PDF, sections in
                        chronological order; one quarter header per call
  _fetch_log.csv       per-co status with counts

Usage:
  python3 fetch_concalls.py                       # NiftyTotalMarket
  python3 fetch_concalls.py --skip-existing       # incremental
  python3 fetch_concalls.py --only RELIANCE,TCS   # spot check
  python3 fetch_concalls.py --years 3             # default lookback
"""

from __future__ import annotations

import argparse
import concurrent.futures
import io
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

HERE = Path(__file__).parent
DEFAULT_OUT = HERE / "NiftyTotalMarket"
CONST_CSV = HERE.parent / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
DELAY = 0.4
PDF_TIMEOUT = 45
SCREENER_TIMEOUT = 25

MONTH_ORDER = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
               "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}


def _http_get(url: str, timeout: int = SCREENER_TIMEOUT,
              accept: str = "text/html") -> tuple[int, bytes | None]:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": accept,
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.screener.in/",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:
        return 0, None


CONCALLS_BLOCK_RE = re.compile(
    r'class="documents concalls flex-column".*?<ul class="list-links">(.*?)</ul>',
    re.DOTALL,
)
LI_RE = re.compile(r'<li[^>]*>(.*?)</li>', re.DOTALL)
DATE_RE = re.compile(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})')
TRANSCRIPT_RE = re.compile(
    r'<a[^>]+class="concall-link"[^>]+href="([^"]+)"[^>]+title="Raw Transcript"',
)


def parse_concalls(html: str) -> list[tuple[str, str]]:
    """Returns a list of (date_label, transcript_pdf_url).
    Date label is screener's "MMM YYYY" string."""
    m = CONCALLS_BLOCK_RE.search(html)
    if not m:
        return []
    block = m.group(1)
    out = []
    for li_html in LI_RE.findall(block):
        # First date label in this li
        d = DATE_RE.search(li_html)
        if not d:
            continue
        date_label = f"{d.group(1)} {d.group(2)}"
        # Transcript URL (must be a Raw Transcript link, not PPT/AI Summary)
        t = TRANSCRIPT_RE.search(li_html)
        if not t:
            continue
        url = t.group(1).replace("&amp;", "&")
        out.append((date_label, url))
    return out


def date_key(label: str) -> tuple[int, int]:
    """Convert 'Jan 2026' to (2026, 1) for sorting."""
    m = re.match(r"(\w{3})\s+(\d{4})", label)
    if not m:
        return (0, 0)
    return (int(m.group(2)), MONTH_ORDER.get(m.group(1), 0))


def filter_recent(concalls: list[tuple[str, str]], years: int) -> list[tuple[str, str]]:
    """Keep only concalls dated within the last `years` years from today."""
    cutoff = datetime.utcnow() - timedelta(days=years * 365 + 30)
    cutoff_key = (cutoff.year, cutoff.month)
    return [(d, u) for d, u in concalls if date_key(d) >= cutoff_key]


def download_pdf(url: str) -> bytes | None:
    for attempt in range(3):
        code, body = _http_get(url, timeout=PDF_TIMEOUT, accept="application/pdf,*/*")
        if code == 200 and body and body[:4] == b"%PDF":
            return body
        if code == 429:
            time.sleep(2 ** attempt)
            continue
        if code in (403, 404):
            return None
        time.sleep(1)
    return None


def extract_text(pdf_bytes: bytes) -> str:
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes), strict=False)
    except Exception:
        return ""
    parts = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        parts.append(text)
    return "\n".join(parts)


def clean_text_for_pdf(text: str) -> str:
    # Strip unusual whitespace + control chars, normalize line breaks
    text = text.replace("\r", "\n")
    text = re.sub(r"[\x00-\x08\x0b-\x1f]", "", text)
    # collapse runs of blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_pdf(out_path: Path, company_symbol: str,
              company_name: str, sections: list[tuple[str, str]]) -> None:
    """sections: list of (date_label, text) already sorted oldest-first."""
    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=A4,
        leftMargin=1.5 * cm, rightMargin=1.5 * cm,
        topMargin=1.5 * cm, bottomMargin=1.5 * cm,
        title=f"{company_symbol} concalls",
    )
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("title", parent=styles["Title"], fontSize=18)
    head_style = ParagraphStyle("head", parent=styles["Heading2"], fontSize=14,
                                spaceBefore=12, spaceAfter=6)
    body_style = ParagraphStyle("body", parent=styles["BodyText"],
                                fontSize=9, leading=11, alignment=0)
    flow = [
        Paragraph(f"{company_name} ({company_symbol})", title_style),
        Paragraph(
            f"Conference call transcripts, oldest-first. {len(sections)} call(s). "
            f"Generated {datetime.utcnow().strftime('%Y-%m-%d')}.",
            styles["Italic"]
        ),
        Spacer(1, 0.4 * cm),
    ]
    for date_label, text in sections:
        flow.append(PageBreak())
        flow.append(Paragraph(f"Call: {date_label}", head_style))
        if not text:
            flow.append(Paragraph(
                "<i>(no extractable text — likely a scanned image PDF)</i>",
                body_style,
            ))
            continue
        # Split into paragraphs by blank line; escape XML chars for reportlab
        for para in text.split("\n\n"):
            para = para.strip()
            if not para:
                continue
            safe = (para.replace("&", "&amp;")
                        .replace("<", "&lt;").replace(">", "&gt;"))
            # reportlab paragraphs don't break across pages if huge — split long ones
            for chunk in [safe[i:i + 4000] for i in range(0, len(safe), 4000)]:
                flow.append(Paragraph(chunk.replace("\n", "<br/>"), body_style))
    doc.build(flow)


def process_company(sym: str, name: str, out_dir: Path, years: int) -> str:
    out_path = out_dir / f"{sym.replace('&','_AND_')}.pdf"
    encoded = urllib.parse.quote(sym, safe="")
    html_bytes = None
    for attempt in range(3):
        for variant in ("consolidated/", ""):
            code, body = _http_get(
                f"https://www.screener.in/company/{encoded}/{variant}")
            if code == 200 and body:
                html_bytes = body
                break
        if html_bytes is not None:
            break
        time.sleep(1 + attempt)
    if html_bytes is None:
        return "no_screener_page"
    html = html_bytes.decode("utf-8", errors="ignore")
    concalls = parse_concalls(html)
    if not concalls:
        return "no_concalls_listed"

    # Keep last N years, sort oldest-first
    recent = filter_recent(concalls, years)
    recent.sort(key=lambda x: date_key(x[0]))
    if not recent:
        return "no_recent_concalls"

    # Download PDFs concurrently (4 workers) to keep total runtime sane.
    # Order is preserved by indexing into `recent`.
    def fetch_one(idx_url):
        idx, (date_label, url) = idx_url
        pdf_bytes = download_pdf(url)
        if pdf_bytes is None:
            return idx, date_label, ""
        text = clean_text_for_pdf(extract_text(pdf_bytes))
        return idx, date_label, text

    sections_idx: dict[int, tuple[str, str]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for idx, date_label, text in ex.map(
                fetch_one, list(enumerate(recent))):
            sections_idx[idx] = (date_label, text)
    sections: list[tuple[str, str]] = [sections_idx[i]
                                       for i in range(len(recent))]
    n_downloaded = sum(1 for _, t in sections if t or t == "")  # we count all attempts; refine below
    n_text_ok = sum(1 for _, t in sections if t)
    n_downloaded = sum(1 for _, t in sections if t)  # treat empty as not-downloaded

    try:
        build_pdf(out_path, sym, name, sections)
    except Exception as e:
        return f"pdf_build_error:{type(e).__name__}:{str(e)[:60]}"

    return f"ok:calls_listed={len(recent)}:downloaded={n_downloaded}:text_ok={n_text_ok}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--only", default=None,
                    help="Comma-separated list of NSE symbols to fetch")
    ap.add_argument("--skip-existing", action="store_true")
    ap.add_argument("--years", type=int, default=3,
                    help="Lookback window in years (default: 3)")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    log_csv = out_dir / "_fetch_log.csv"

    constituents = pd.read_csv(CONST_CSV)
    if args.only:
        wanted = {s.strip() for s in args.only.split(",")}
        constituents = constituents[constituents["nse_symbol"].isin(wanted)]
    symbols = list(zip(
        constituents["nse_symbol"].astype(str),
        constituents["company_name"].astype(str),
    ))

    if args.skip_existing:
        existing_stems = {p.stem for p in out_dir.glob("*.pdf")}
        before = len(symbols)
        symbols = [(s, n) for s, n in symbols
                   if s.replace("&", "_AND_") not in existing_stems]
        print(f"Skipping {before - len(symbols)} cos already present in {out_dir}")

    print(f"To process: {len(symbols)} cos  (lookback: last {args.years} yrs)")
    print("-" * 70)

    log_rows = []
    for i, (sym, name) in enumerate(symbols, 1):
        try:
            status = process_company(sym, name, out_dir, args.years)
        except Exception as e:
            status = f"exception:{type(e).__name__}:{str(e)[:60]}"
        log_rows.append({"nse_symbol": sym, "status": status})

        if i % 10 == 0 or i == len(symbols):
            ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
            print(f"  [{i:4d}/{len(symbols)}] last={sym:<14s} ok={ok}/{i} "
                  f"last_status={status[:75]}")

    # Merge with any existing log
    if log_csv.exists():
        existing = pd.read_csv(log_csv)
        existing = existing[~existing["nse_symbol"].isin(
            {r["nse_symbol"] for r in log_rows})]
        out_log = pd.concat([existing, pd.DataFrame(log_rows)], ignore_index=True)
    else:
        out_log = pd.DataFrame(log_rows)
    out_log.to_csv(log_csv, index=False)

    ok = sum(1 for r in log_rows if r["status"].startswith("ok"))
    print("-" * 70)
    print(f"DONE. ok={ok}/{len(symbols)}")
    print(f"Log: {log_csv}")


if __name__ == "__main__":
    main()
