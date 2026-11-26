"""
fetch_management_change.py — the data the ManagementChangeSkill reads.

Five exchange sources, all NSE, for every NiftyTotalMarket constituent:

1. FILINGS, READ IN FULL. The all-filings store (`Announcements/NiftyTotalMarket/
   _all_filings.csv.gz`) already holds every announcement of the universe and
   the first pages of the material ones — but it deliberately skipped the
   management and takeover categories as noise for restructuring. This module
   reads THOSE: every filing in MGMT_CATEGORIES in the window is downloaded
   (a .zip is opened and each PDF inside read), up to READ_PAGES pages of text
   kept under `NiftyTotalMarket/text/`, the bytes dropped, the result recorded
   in `_filings.csv.gz` so a re-run only reads what is new. A headline says
   "change in Management" for a new head of internal audit and for a new CEO
   alike; only the text tells them apart.
2. REG 29 TAKEOVER DISCLOSURES (`_sast_reg29.csv`): NSE's structured feed of
   every acquisition / sale disclosed under SEBI SAST Regulation 29 — who,
   promoter or not, how many shares, the holding after.
3. BULK AND BLOCK DEALS (`_deals.csv`): every large trade, with the client.
4. SHAREHOLDING PATTERN (`_shareholding.csv`): promoter-and-group and public
   holding, quarter by quarter, from the exchange's shareholding master — the
   independent register a change of ownership must show up in.
5. The all-filings store itself is refreshed to today first, so the text scan
   of board outcomes, press releases and updates covers the same window.

Nothing here classifies; `Skills/ManagementChangeSkill/scripts/` does that.

Usage:
  python3 fetch_management_change.py                # 365 days, everything
  python3 fetch_management_change.py --days 400 --no-refresh
  python3 fetch_management_change.py --only filings|sast|deals|shareholding
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import contextlib
import shutil
import signal
import subprocess
import tempfile
import xml.etree.ElementTree as ET
import csv
import datetime as dt
import gzip
import io
import json
import re
import sys
import time
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent
sys.path.insert(0, str(INDIA / "Announcements"))

import fetch_announcements as FA        # noqa: E402  (http, universe)
import deep_read as DR                  # noqa: E402  (pdf first pages, the all-filings store)

OUT_DIR = HERE / "NiftyTotalMarket"
TEXT_DIR = OUT_DIR / "text"
FILINGS = OUT_DIR / "_filings.csv.gz"
SAST = OUT_DIR / "_sast_reg29.csv"
DEALS = OUT_DIR / "_deals.csv"
SHP = OUT_DIR / "_shareholding.csv"
LOG = OUT_DIR / "_fetch_log.csv"

READ_PAGES = 15
READ_CHARS = 90_000
READ_MB = 60
OCR_PAGES = 4               # a scanned letter says what happened on its first pages
MIN_TEXT = 120              # fewer non-space characters than this is a scan, not text
WORKERS = 6
EXTRACT_SECONDS = 30        # a PDF whose text will not come out in this long is recorded as slow, not waited on
PAGE_SECONDS = 12           # past this, the pages already read are kept and the rest left
SAVE_EVERY = 400

# the categories the restructuring store never read: management, board and takeover filings
MGMT_CATEGORIES = {
    "Change in Management", "Appointment", "Change in Director(s)", "Resignation",
    "Resignation of Director/KMP/SMP", "Cessation", "Retirement", "Resignation of Independent director",
    "Disclosure under SEBI Takeover Regulations",
}
# categories the store read only when small or with a PDF: read again here when it has no text for them
ALSO_READ = {"Public Announcement-Open Offer", "Open Offer", "Demise", "Offer for sale",
             "Change in Company Secretary/Compliance Officer"}

# the all-filings store skips attachments over 8 MB — and a board outcome that carries the results is often
# larger. A new CEO or CFO announced only there would be missed, so the big ones of these categories are read here
BIG_CATEGORIES = {"Outcome of Board Meeting", "Press Release", "Updates", "General Updates"}

FILING_FIELDS = ["date", "symbol", "company", "category", "headline", "attachment", "ann_id",
                 "file_size", "read_status", "text_file", "pages", "chars", "method"]
# scans in these categories are not put through OCR: the same disclosures arrive structured in the Reg 29 feed
NO_OCR_CATEGORIES = {"Disclosure under SEBI Takeover Regulations"}
SAST_FIELDS = ["date", "symbol", "company", "reg", "acquirer", "promoter", "kind", "mode", "period",
               "shares_acquired", "shares_sold", "pct_acquired", "pct_sold", "shares_after", "pct_after",
               "attachment", "application_no"]
DEAL_FIELDS = ["date", "symbol", "company", "deal", "client", "side", "quantity", "price", "remarks"]
SHP_FIELDS = ["symbol", "as_of", "promoter_pct", "public_pct", "employee_trust_pct", "submitted", "xbrl", "notes"]

JSON_HEADERS = {"Accept": "application/json", "Referer": "https://www.nseindia.com/"}
_MON = {m: i + 1 for i, m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split())}


def log(stage: str, msg: str) -> None:
    print(f"[{stage}] {msg}", file=sys.stderr, flush=True)


def iso(s: str) -> str:
    """'12-NOV-2026', '26-Nov-2026 12:48', '02-NOV-2026' → '2026-11-12'; '' when unreadable."""
    m = re.search(r"(\d{1,2})[-\s]([A-Za-z]{3})[-\s](\d{4})", s or "")
    if not m or m.group(2).upper() not in _MON:
        return ""
    return f"{int(m.group(3)):04d}-{_MON[m.group(2).upper()]:02d}-{int(m.group(1)):02d}"


def get_json(url: str, timeout: int = 120):
    code, body = FA._get(url, timeout=timeout, headers=JSON_HEADERS)
    if code != 200 or not body:
        raise RuntimeError(f"HTTP {code} for {url[:110]}")
    return json.loads(body)


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(tmp, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})
    tmp.replace(path)


# ------------------------------------------------------------- 1. filings

def refresh_store(today: dt.date, days: int = 25) -> int:
    """Bring the all-filings store up to today (the last `days` days of the
    NSE feed; rows already there are kept). Returns the store's size."""
    members = FA.universe()
    feeds = []
    for a, b in FA.month_windows(today, days):
        feeds.append(FA.nse_fetch(a, b))
        time.sleep(1)
    store = DR.run_deep(feeds, members, note=log)
    return len(store)


def xml_text(data: bytes) -> str:
    """The facts of an exchange XBRL filing as readable text. NSE files a
    resignation or a change in management as a .zip: a structured XML
    ('TypeOfChange = Cessation', 'DesignationOfDesignatedPerson = Chief
    Financial Officer', 'NameOfDesignatedPerson = …') beside a scanned
    letter. The tags are split into words and the facts joined on one line,
    so the seat, the person and the event sit together."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return ""
    facts, seen = [], set()
    for el in root.iter():
        ns, _, tag = el.tag.rpartition("}")
        val = re.sub(r"\s+", " ", el.text or "").strip()
        if not val or "xbrl.org/2003/instance" in ns or "xbrl.org/2006/xbrldi" in ns or "linkbase" in ns:
            continue
        if tag.endswith("Domain") or val.lower() in ("true", "false") and len(tag) > 60:
            continue
        name = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", tag)
        name = re.sub(r"Director Or Key Managerial Personnel Or Senior Management Personnel Or Compliance Officer", "Person", name)
        key = (name, val)
        if key in seen:
            continue
        seen.add(key)
        facts.append(f"{name}: {val}")
    return " ; ".join(facts)


def text_of(data: bytes, pages: int = READ_PAGES) -> tuple[str, int]:
    """(text, pages read) of a PDF, or of everything inside a .zip: the
    structured XML first (it is the disclosure itself), then each PDF."""
    if data[:4] == b"%PDF":
        return _pdf(data, pages)
    if data[:2] == b"PK":
        parts, n = [], 0
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                names = sorted(z.namelist(), key=lambda x: (not x.lower().endswith(".xml"), x))
                for name in names:
                    low = name.lower()
                    if low.endswith(".xml"):
                        t = xml_text(z.read(name))
                        if t:
                            parts.append(f"--- {name} (the exchange's structured disclosure) ---\n{t}")
                    elif low.endswith(".pdf"):
                        t, k = _pdf(z.read(name), pages)
                        if t.strip():
                            parts.append(f"--- {name} ---\n{t}")
                            n += k
        except (zipfile.BadZipFile, OSError, RuntimeError):
            return "", 0
        return "\n\n".join(parts)[:READ_CHARS], n
    if data.lstrip()[:5] == b"<?xml":
        return xml_text(data)[:READ_CHARS], 0
    return "", 0


LOW_SPACE = 0.08            # normal prose is 13–18% spaces; under this the words have run together


def space_ratio(text: str) -> float:
    t = text or ""
    return len(re.findall(r"\s", t)) / len(t) if t else 0.0


def _pdftotext(data: bytes, pages: int) -> tuple[str, int]:
    """Poppler's pdftotext — fast, and it reads many PDFs PyPDF2 cannot.
    ('', 0) when it is not installed or gives nothing."""
    exe = shutil.which("pdftotext")
    if not exe:
        return "", 0
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        fh.write(data)
        fh.flush()
        try:
            out = subprocess.run([exe, "-l", str(pages), "-q", fh.name, "-"], capture_output=True, timeout=40).stdout
        except (subprocess.TimeoutExpired, OSError):
            return "", 0
        text = out.decode("utf-8", "replace")
        if len(re.sub(r"\s+", "", text)) >= 40 and space_ratio(text) < LOW_SPACE:
            # some PDFs place every glyph separately and the words run together: the layout mode keeps the gaps
            try:
                alt = subprocess.run([exe, "-l", str(pages), "-q", "-layout", fh.name, "-"],
                                     capture_output=True, timeout=40).stdout.decode("utf-8", "replace")
            except (subprocess.TimeoutExpired, OSError):
                alt = ""
            if space_ratio(alt) > space_ratio(text):
                text = alt
    if len(re.sub(r"\s+", "", text)) < 40:
        return "", 0
    return DR.clean_text(text.replace("\f", "\n"))[:READ_CHARS], min(pages, text.count("\f") or 1)


_OCR = None


def ocr_available() -> bool:
    try:
        import rapidocr_onnxruntime                 # noqa: F401, PLC0415
    except Exception:                               # noqa: BLE001
        return False
    return shutil.which("pdftoppm") is not None


def ocr_text(data: bytes, pages: int = OCR_PAGES) -> tuple[str, int]:
    """Text of a SCANNED PDF: its first pages rendered (pdftoppm) and read
    by RapidOCR (optional: `python3 -m pip install rapidocr-onnxruntime`).
    OCR runs words together ('ChiefFinancialOfficer'), so a space is put
    back at every lower-to-upper boundary. ('', 0) when OCR is not
    installed or finds nothing."""
    global _OCR
    if not ocr_available() or data[:4] != b"%PDF":
        return "", 0
    if _OCR is None:
        from rapidocr_onnxruntime import RapidOCR   # noqa: PLC0415
        _OCR = RapidOCR()
    out = []
    with tempfile.TemporaryDirectory() as d:
        pdf = Path(d) / "a.pdf"
        pdf.write_bytes(data)
        try:
            subprocess.run(["pdftoppm", "-r", "110", "-l", str(pages), "-png", str(pdf), str(Path(d) / "p")],
                           capture_output=True, timeout=120, check=True)
        except (subprocess.SubprocessError, OSError):
            return "", 0
        pngs = sorted(Path(d).glob("p*.png"))
        for png in pngs:
            try:
                res, _ = _OCR(str(png))
            except Exception:                       # noqa: BLE001
                res = None
            out.append(" ".join(x[1] for x in (res or [])))
    text = "\n".join(out)
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    text = re.sub(r"(?<=[A-Za-z])(?=\d{1,2}(?:st|nd|rd|th)?\s*(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))", " ", text)
    return DR.clean_text(text)[:READ_CHARS], len(out)


class SlowPdf(BaseException):
    """Raised by the alarm; a BaseException so the tolerant PDF handlers do not swallow it."""


def _alarm(signum, frame):
    raise SlowPdf()


def _pdf(data: bytes, pages: int) -> tuple[str, int]:
    fast = _pdftotext(data, pages)
    if fast[0]:
        return fast
    import PyPDF2                                   # noqa: PLC0415
    parts = []
    t0 = time.time()
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(data), strict=False)
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception:                       # noqa: BLE001
                return "", 0
        total = len(reader.pages)
        for i in range(min(pages, total)):
            if time.time() - t0 > PAGE_SECONDS and parts:
                break
            try:
                parts.append(reader.pages[i].extract_text() or "")
            except Exception:                       # noqa: BLE001
                parts.append("")
    except Exception:                               # noqa: BLE001
        return DR.clean_text("\n".join(parts))[:READ_CHARS], len(parts)
    return DR.clean_text("\n".join(parts))[:READ_CHARS], len(parts)


def read_one(r: dict) -> dict:
    """Download one attachment, keep its text, drop the bytes. Never raises."""
    try:
        if not r.get("attachment"):
            return {**r, "read_status": "no-attachment"}
        if FA._size_mb(r.get("file_size", "")) > READ_MB:
            return {**r, "read_status": f"skipped:size>{READ_MB}MB"}
        code, body = FA._get(r["attachment"], timeout=120, headers={
            "Referer": "https://www.nseindia.com/", "Accept": "application/pdf,*/*"})
        if code != 200 or not body:
            return {**r, "read_status": f"failed:http{code}"}
        old = signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(EXTRACT_SECONDS)
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                text, pages = text_of(body)
        except SlowPdf:
            return {**r, "read_status": "skipped:slow-pdf"}
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old)
        method = "text"
        if len(re.sub(r"\s+", "", text)) < MIN_TEXT and r.get("category") not in NO_OCR_CATEGORIES:
            scan = body
            if body[:2] == b"PK":                    # the scanned letter inside a zip with no XML facts
                try:
                    with zipfile.ZipFile(io.BytesIO(body)) as z:
                        scan = next((z.read(n) for n in sorted(z.namelist()) if n.lower().endswith(".pdf")), b"")
                except (zipfile.BadZipFile, OSError):
                    scan = b""
            ot, op = ocr_text(scan)
            if len(re.sub(r"\s+", "", ot)) >= MIN_TEXT:
                text, pages, method = (text + "\n" + ot).strip(), op, "ocr"
        if len(re.sub(r"\s+", "", text)) < MIN_TEXT:
            kind = "pdf" if body[:4] == b"%PDF" else ("zip" if body[:2] == b"PK" else "other")
            return {**r, "read_status": f"no-text:{kind}", "pages": pages, "chars": 0, "method": ""}
        TEXT_DIR.mkdir(parents=True, exist_ok=True)
        safe = re.sub(r"[^A-Za-z0-9_-]", "_", r["ann_id"])[:40]
        path = TEXT_DIR / f"{r['symbol'].replace('&', '_')}_{safe}.txt"
        path.write_text(text, encoding="utf-8")
        return {**r, "read_status": "read", "text_file": str(path.relative_to(OUT_DIR)),
                "pages": pages, "chars": len(text), "method": method}
    except Exception as e:                          # noqa: BLE001
        return {**r, "read_status": f"failed:{type(e).__name__}"}


def read_filings(today: dt.date, days: int = 365, workers: int = WORKERS, retry_failed: bool = True,
                 retry: tuple[str, ...] = ()) -> dict:
    """Every management / takeover filing of the window, read in full."""
    start = (today - dt.timedelta(days=days)).isoformat()
    store = DR.load_all()
    mine = {r["ann_id"]: r for r in read_csv(FILINGS)}
    added = 0
    for r in store.values():
        if r["date"] < start or r["date"] > today.isoformat() or r["ann_id"] in mine:
            continue
        want = (r["category"] in MGMT_CATEGORIES or (r["category"] in ALSO_READ and r.get("read_status") != "read")
                or (r["category"] in BIG_CATEGORIES and (r.get("read_status") or "").startswith(("skipped", "failed"))))
        if want:
            mine[r["ann_id"]] = {k: r.get(k, "") for k in FILING_FIELDS[:8]} | {
                "read_status": "", "text_file": "", "pages": "", "chars": ""}
            added += 1
    if "nospace" in retry:
        # first pages the all-filings store extracted with the words run together: read them again here
        for r in store.values():
            if r["date"] < start or r["date"] > today.isoformat() or r["ann_id"] in mine or r.get("read_status") != "read":
                continue
            p = FA.OUT_DIR / (r.get("first_text") or "_")
            try:
                t = p.read_text(errors="replace") if p.is_file() else ""
            except OSError:
                t = ""
            if len(t) > 400 and space_ratio(t) < LOW_SPACE:
                mine[r["ann_id"]] = {k: r.get(k, "") for k in FILING_FIELDS[:8]} | {
                    "read_status": "", "text_file": "", "pages": "", "chars": "", "method": ""}
                added += 1

    def low_space(r: dict) -> bool:
        if r.get("read_status") != "read" or not r.get("text_file"):
            return False
        try:
            t = (OUT_DIR / r["text_file"]).read_text(errors="replace")
        except OSError:
            return False
        return len(t) > 400 and space_ratio(t) < LOW_SPACE
    todo = [r for r in mine.values()
            if not r.get("read_status") or (retry_failed and r["read_status"].startswith("failed"))
            or ("nospace" in retry and low_space(r))
            or any(r["read_status"].startswith(k) for k in retry)
            or ("zip" in retry and r.get("attachment", "").lower().endswith(".zip"))
            or ("short" in retry and r["read_status"] == "read" and int(r.get("chars") or 0) < 300)]
    log("filings", f"index {len(mine)} ({added} new); {len(todo)} to read")
    done, t0 = 0, time.time()
    order = lambda rows: sorted(rows, key=lambda r: (r["date"], r["symbol"], r["ann_id"]))   # noqa: E731
    # text extraction is CPU-bound: processes, not threads
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(read_one, todo, chunksize=2):
            mine[res["ann_id"]] = res
            done += 1
            if done % SAVE_EVERY == 0:
                write_csv(FILINGS, order(mine.values()), FILING_FIELDS)
                log("filings", f"{done}/{len(todo)} read ({time.time() - t0:.0f}s)")
    write_csv(FILINGS, order(mine.values()), FILING_FIELDS)
    by = {}
    for r in mine.values():
        k = (r.get("read_status") or "").split(":")[0]
        by[k] = by.get(k, 0) + 1
    log("filings", f"done: {by}")
    return by


# ------------------------------------------------------- 2. Reg 29 feed

def fetch_sast(today: dt.date, days: int, members: dict[str, str]) -> int:
    old = {(r["application_no"], r["symbol"], r["acquirer"], r["period"]): r for r in read_csv(SAST)}
    for a, b in FA.month_windows(today, days):
        url = ("https://www.nseindia.com/api/corporate-sast-reg29?index=equities"
               f"&from_date={a.strftime('%d-%m-%Y')}&to_date={b.strftime('%d-%m-%Y')}")
        try:
            data = get_json(url).get("data") or []
        except Exception as e:                      # noqa: BLE001
            log("sast", f"{a}→{b}: {e}")
            continue
        for d in data:
            sym = (d.get("symbol") or "").strip()
            if sym not in members:
                continue
            row = {"date": iso(d.get("timestamp") or d.get("time") or ""), "symbol": sym, "company": members[sym],
                   "reg": d.get("regType") or "", "acquirer": re.sub(r"\s+", " ", d.get("acquirerName") or "").strip(),
                   "promoter": d.get("promoterType") or "", "kind": d.get("acqSaleType") or "",
                   "mode": d.get("acquisitionMode") or "", "period": d.get("acquirerDate") or "",
                   "shares_acquired": d.get("noOfShareAcq") or "", "shares_sold": d.get("noOfShareSale") or "",
                   "pct_acquired": d.get("totAcqShare") or "", "pct_sold": d.get("totSaleShare") or "",
                   "shares_after": d.get("noOfShareAft") or "", "pct_after": d.get("totAftShare") or "",
                   "attachment": d.get("attachement") or "", "application_no": str(d.get("application_no") or "")}
            old[(row["application_no"], sym, row["acquirer"], row["period"])] = row
        time.sleep(1)
    rows = sorted(old.values(), key=lambda r: (r["date"], r["symbol"], r["acquirer"]))
    write_csv(SAST, rows, SAST_FIELDS)
    log("sast", f"{len(rows)} Reg 29 disclosures for universe companies")
    return len(rows)


# ------------------------------------------------ 3. bulk and block deals

def fetch_deals(today: dt.date, days: int, members: dict[str, str]) -> int:
    old = {(r["date"], r["symbol"], r["deal"], r["client"], r["side"], r["quantity"], r["price"]): r
           for r in read_csv(DEALS)}
    for kind in ("bulk_deals", "block_deals"):
        for a, b in FA.month_windows(today, days):
            url = ("https://www.nseindia.com/api/historicalOR/bulk-block-short-deals"
                   f"?optionType={kind}&from={a.strftime('%d-%m-%Y')}&to={b.strftime('%d-%m-%Y')}")
            try:
                data = get_json(url).get("data") or []
            except Exception as e:                  # noqa: BLE001
                log("deals", f"{kind} {a}→{b}: {e}")
                continue
            for d in data:
                sym = (d.get("BD_SYMBOL") or "").strip()
                if sym not in members:
                    continue
                row = {"date": iso(d.get("BD_DT_DATE") or ""), "symbol": sym, "company": members[sym],
                       "deal": kind.split("_")[0], "client": re.sub(r"\s+", " ", d.get("BD_CLIENT_NAME") or "").strip(),
                       "side": (d.get("BD_BUY_SELL") or "").upper(), "quantity": str(d.get("BD_QTY_TRD") or ""),
                       "price": str(d.get("BD_TP_WATP") or ""), "remarks": (d.get("BD_REMARKS") or "").strip("- ")}
                old[(row["date"], sym, row["deal"], row["client"], row["side"], row["quantity"], row["price"])] = row
            time.sleep(0.8)
    rows = sorted(old.values(), key=lambda r: (r["date"], r["symbol"], r["client"]))
    write_csv(DEALS, rows, DEAL_FIELDS)
    log("deals", f"{len(rows)} bulk / block deals for universe companies")
    return len(rows)


# --------------------------------------------------- 4. shareholding

def shareholding_of(symbol: str) -> list[dict]:
    url = ("https://www.nseindia.com/api/corporate-share-holdings-master?index=equities&symbol="
           + symbol.replace("&", "%26"))
    data = get_json(url, timeout=60)
    out = {}
    for d in data if isinstance(data, list) else []:
        as_of = iso(d.get("date") or "")
        if not as_of:
            continue
        row = {"symbol": symbol, "as_of": as_of, "promoter_pct": d.get("pr_and_prgrp") or "",
               "public_pct": d.get("public_val") or "", "employee_trust_pct": d.get("employeeTrusts") or "",
               "submitted": iso(d.get("submissionDate") or d.get("broadcastDate") or ""),
               "xbrl": d.get("xbrl") or "",
               "notes": re.sub(r"\s+", " ", DR.clean_text(d.get("remarksWeb") or "")).strip()[:700]}
        if as_of not in out or row["submitted"] >= out[as_of]["submitted"]:     # a revised filing replaces the first
            out[as_of] = row
    return list(out.values())


def fetch_shareholding(members: dict[str, str], workers: int = 4, max_age_days: int = 20) -> int:
    """Quarterly promoter / public holding for every member (a symbol whose
    rows were fetched within `max_age_days` of its newest quarter end + 21
    days is left alone only when nothing newer can exist)."""
    old: dict[str, list[dict]] = {}
    for r in read_csv(SHP):
        old.setdefault(r["symbol"], []).append(r)
    todo = sorted(members)
    def one(sym):
        for attempt in range(3):
            try:
                return sym, shareholding_of(sym)
            except Exception:                       # noqa: BLE001
                time.sleep(2 * (attempt + 1))
        return sym, None
    done = failed = 0
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        for sym, rows in ex.map(one, todo):
            done += 1
            if rows is None:
                failed += 1
            elif rows:
                old[sym] = rows
            if done % 100 == 0:
                log("shareholding", f"{done}/{len(todo)} ({failed} failed)")
    rows = sorted((r for rs in old.values() for r in rs), key=lambda r: (r["symbol"], r["as_of"]))
    write_csv(SHP, rows, SHP_FIELDS)
    log("shareholding", f"{len(old)} companies, {len(rows)} quarters; {failed} failed")
    return len(old)


# -------------------------------------------------------------------- run

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=365)
    ap.add_argument("--no-refresh", action="store_true", help="do not refresh the all-filings store first")
    ap.add_argument("--only", default="", help="filings | sast | deals | shareholding")
    ap.add_argument("--workers", type=int, default=WORKERS)
    ap.add_argument("--ocr-all", action="store_true", help="also OCR scanned takeover disclosures (slow; the Reg 29 feed carries the same facts)")
    ap.add_argument("--retry", default="", help="re-read filings whose status starts with these (comma-separated), "
                                                "e.g. no-text,skipped — and 'zip' for every .zip attachment")
    args = ap.parse_args()
    today = dt.date.today()
    members = FA.universe()
    if args.ocr_all:
        NO_OCR_CATEGORIES.clear()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    only = set(filter(None, args.only.split(",")))
    out = {"date": today.isoformat(), "days": args.days}
    if not only or "filings" in only:
        if not args.no_refresh:
            out["store"] = refresh_store(today)
        out["filings"] = json.dumps(read_filings(today, args.days, args.workers,
                                                 retry=tuple(filter(None, args.retry.split(",")))))
    if not only or "sast" in only:
        out["sast"] = fetch_sast(today, args.days, members)
    if not only or "deals" in only:
        out["deals"] = fetch_deals(today, args.days, members)
    if not only or "shareholding" in only:
        out["shareholding"] = fetch_shareholding(members)
    rows = read_csv(LOG) + [out]
    write_csv(LOG, rows, ["date", "days", "store", "filings", "sast", "deals", "shareholding"])
    print(json.dumps(out))


if __name__ == "__main__":
    main()
