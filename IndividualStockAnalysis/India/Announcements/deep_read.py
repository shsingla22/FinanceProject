"""
deep_read.py — read the first pages of EVERY material filing, not just the
headline, and classify from both.

A headline ("Outcome of Board Meeting", "Updates", "General Updates") often
says nothing; the attachment's first pages say what was approved. This
module keeps a store of every universe filing for the year
(`_all_filings.csv.gz`), streams each eligible attachment once, keeps the
text of its first DEEP_PAGES pages under `text/first/`, discards the PDF,
and records the result so a re-run only reads what is new.

Eligible = any category that could carry a corporate action (everything
except the routine-compliance categories in NOISE_FOR_DEEP), with a PDF
attachment of at most DEEP_MB megabytes. Larger files keep their
headline-only classification and are marked `skipped:size`.

Classification is MULTI-LABEL: `classify_all(category, headline, text)`
returns every kind the headline or the first pages support, so one filing
(and one company) can sit in several categories — a composite scheme that
demerges one business and merges another carries both tags.
"""

from __future__ import annotations

import concurrent.futures as cf
import csv
import gzip
import io
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import fetch_announcements as FA        # noqa: E402  (patterns, http, paths)

ALL_FILINGS = FA.OUT_DIR / "_all_filings.csv.gz"
FIRST_DIR = FA.TEXT_DIR / "first"
DEEP_PAGES = 6
DEEP_MB = 8
WORKERS = 6
SAVE_EVERY = 500

NOISE_FOR_DEEP = {
    "Analysts/Institutional Investor Meet/Con. Call Updates", "Copy of Newspaper Publication",
    "Trading Window", "Certificate under SEBI (Depositories and Participants) Regulations, 2018",
    "ESOP/ESOS/ESPS", "Disclosure under SEBI Takeover Regulations", "Appointment",
    "Change in Management", "Credit Rating", "Dividend", "Change in Director(s)",
    "Bagging/Receiving of orders/contracts", "Action(s) taken or orders passed",
    "Monitoring Agency Report", "Resignation", "Resignation of Director/KMP/SMP",
    "Spurt in Volume", "Cessation", "Action(s) initiated or orders passed", "Change in Auditors",
    "Pendency of Litigation(s)/dispute(s) or the outcome impacting the Company",
    "Statement of deviation(s) or variation(s) under Reg. 32", "Options to purchase securities",
    "Credit Rating- Revision", "Credit Rating- New", "Credit Rating- Others",
    "Commencement of commercial production/operations", "Capacity addition",
    "Monthly Business Updates", "Amendment to AOA/MOA", "Retirement",
    "Giving guarantees/indemnity/ becoming a surety for third party",
    "Reply to Clarification- Financial results", "Clarification - Financial results",
    "Structural Digital Database", "Price movement", "Investor Presentation",
    "Issue of Duplicate Share Certificate(s)", "Loss of Share Certificate",
}

ALL_FIELDS = ["date", "symbol", "company", "category", "headline", "attachment", "ann_id",
              "file_size", "read_status", "first_text", "tags"]

# ------------------------------------------------------- text classification
# Text is boilerplate-heavy, so a kind from the BODY needs either a strong
# phrase or repeated mention. Each entry: (pattern, minimum hits).
TEXT_RULES = {
    "demerger": (re.compile(r"\bde-?merg|spin[\s-]?off|hiv(e|ing)[\s-]?off|carve[\s-]?out|"
                            r"resulting compan|demerged (undertaking|compan)", re.I), 2),
    "subsidiary_listing": (re.compile(
        r"(ipo|initial public offer\w*|draft red herring|drhp|listing of (the |its )?(equity )?shares)"
        r".{0,120}(subsidiar|arm\b)|subsidiar.{0,120}(ipo|initial public offer|draft red herring|drhp|"
        r"listing of (the |its )?(equity )?shares)", re.I | re.S), 1),
    "slump_sale": (re.compile(r"slump sale|business transfer agreement", re.I), 1),
    "merger": (re.compile(r"amalgamat|scheme of amalgamation|\bmerger\b", re.I), 2),
    "capital_reduction": (re.compile(r"reduction of (share )?capital|capital reduction|buy[\s-]?back of", re.I), 1),
    "rights_issue": (re.compile(r"rights? issue|rights entitlement|letter of offer", re.I), 1),
    "preferential_issue": (re.compile(r"preferential (issue|allotment|basis|offer)|convertible warrants?|"
                                      r"allotment of .{0,40}warrants|conversion of warrants", re.I), 1),
    "scheme_other": (re.compile(r"scheme of arrangement|composite scheme", re.I), 1),
}
# a notice that merely restates earlier approvals in passing
BOILERPLATE_RX = re.compile(r"pursuant to (the )?scheme of arrangement.{0,60}(approved|sanctioned) (by|in) \d{4}", re.I)


def classify_text(text: str) -> list[str]:
    """Kinds the first pages support, in KIND_ORDER."""
    t = (text or "")[:40_000]
    if not t.strip():
        return []
    tags = []
    for kind in FA.KIND_ORDER:
        rx, need = TEXT_RULES[kind]
        if len(rx.findall(t)) >= need:
            tags.append(kind)
    return tags


def classify_all(category: str, headline: str, text: str = "") -> tuple[str, list[str]]:
    """Every kind the headline OR the first pages support; `kind` is the
    first in KIND_ORDER for callers that want one. Noise categories still
    classify from their TEXT (a 'General Updates' can be anything), but the
    pure-compliance categories are never read at all (see NOISE_FOR_DEEP)."""
    _, head_tags = FA.classify(category, headline)
    tags = sorted(set(head_tags) | set(classify_text(text)), key=FA.KIND_ORDER.index)
    return (tags[0] if tags else ""), tags


# ------------------------------------------------------------------ store

def load_all() -> dict[str, dict]:
    if not ALL_FILINGS.exists():
        return {}
    with gzip.open(ALL_FILINGS, "rt", newline="") as fh:
        return {r["ann_id"]: r for r in csv.DictReader(fh)}


def save_all(rows: dict[str, dict]) -> None:
    ALL_FILINGS.parent.mkdir(parents=True, exist_ok=True)
    tmp = ALL_FILINGS.with_suffix(".tmp.gz")
    with gzip.open(tmp, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=ALL_FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows.values(), key=lambda r: (r["date"], r["symbol"], r["ann_id"])):
            w.writerow({k: r.get(k, "") for k in ALL_FIELDS})
    tmp.replace(ALL_FILINGS)


def feed_to_all(feed: list[dict], members: dict[str, str]) -> list[dict]:
    """Every universe row of one monthly feed, in the store's schema."""
    out = []
    for r in feed:
        sym = (r.get("symbol") or "").strip()
        if sym not in members:
            continue
        out.append({"date": FA._nse_date(r.get("an_dt") or ""), "symbol": sym,
                    "company": members[sym], "category": r.get("desc") or "",
                    "headline": re.sub(r"\s+", " ", r.get("attchmntText") or "").strip(),
                    "attachment": r.get("attchmntFile") or "",
                    "ann_id": str(r.get("seq_id") or r.get("dt") or ""),
                    "file_size": r.get("attFileSize") or "", "read_status": "", "first_text": "",
                    "tags": ""})
    return out


# -------------------------------------------------------------- the read

def first_pages(data: bytes, n: int = DEEP_PAGES) -> str:
    """Text of the first n pages; '' for anything PyPDF2 cannot open
    (encrypted with an unsupported cipher, damaged, not a PDF)."""
    import PyPDF2                                   # noqa: PLC0415
    parts = []
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(data), strict=False)
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception:                       # noqa: BLE001
                return ""
        for i in range(min(n, len(reader.pages))):
            try:
                parts.append(reader.pages[i].extract_text() or "")
            except Exception:                       # noqa: BLE001
                parts.append("")
    except Exception:                               # noqa: BLE001
        return clean_text("\n".join(parts))[:60_000]
    return clean_text("\n".join(parts))[:60_000]


def clean_text(s: str) -> str:
    """Control characters out, and lone surrogates (which some PDFs' fonts
    produce) dropped — they cannot be written as UTF-8."""
    s = s.encode("utf-8", "ignore").decode("utf-8", "ignore")
    return re.sub(r"[\x00-\x08\x0b-\x1f]", "", s)


def eligible(r: dict) -> str:
    """'' when the row should be read, else the reason it is not."""
    if r["category"] in NOISE_FOR_DEEP:
        return "noise-category"
    if not r["attachment"].lower().endswith(".pdf"):
        return "no-pdf"
    if FA._size_mb(r.get("file_size", "")) > DEEP_MB:
        return f"skipped:size>{DEEP_MB}MB"
    return ""


def read_one(r: dict) -> dict:
    """Stream one attachment, keep its first pages, drop the bytes. Never
    raises: a worker's failure is recorded on its row, not on the run."""
    try:
        return _read_one(r)
    except Exception as e:                          # noqa: BLE001
        return {**r, "read_status": f"failed:{type(e).__name__}"}


def _read_one(r: dict) -> dict:
    code, body = FA._get(r["attachment"], timeout=90, headers={
        "Referer": "https://www.nseindia.com/", "Accept": "application/pdf,*/*"})
    if code != 200 or body[:4] != b"%PDF":
        return {**r, "read_status": f"failed:http{code}"}
    if len(body) > DEEP_MB * 1024 * 1024 * 1.5:
        return {**r, "read_status": "skipped:size"}
    text = first_pages(body)
    FIRST_DIR.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", r["ann_id"])[:40]
    path = FIRST_DIR / f"{r['symbol']}_{safe}.txt"
    try:
        path.write_text(text if text.strip() else "(no extractable text)", encoding="utf-8")
    except (OSError, UnicodeEncodeError) as e:
        return {**r, "read_status": f"failed:write:{type(e).__name__}"}
    _, tags = classify_all(r["category"], r["headline"], text)
    return {**r, "read_status": "read", "first_text": str(path.relative_to(FA.OUT_DIR)),
            "tags": "|".join(tags)}


def run_deep(feeds: list[list[dict]], members: dict[str, str], workers: int = WORKERS,
             note=print) -> dict[str, dict]:
    """Merge the feeds into the all-filings store, read every eligible
    filing not yet read, classify headline + first pages, save as it goes.
    Returns the store."""
    store = load_all()
    fresh = 0
    for feed in feeds:
        for r in feed_to_all(feed, members):
            if r["ann_id"] not in store:
                store[r["ann_id"]] = r
                fresh += 1
    for r in store.values():
        if not r.get("read_status"):
            why = eligible(r)
            if why:
                r["read_status"] = why
                _, tags = classify_all(r["category"], r["headline"], "")
                r["tags"] = "|".join(tags)
    todo = [r for r in store.values() if not r.get("read_status")]
    note("deep", f"store {len(store)} filings ({fresh} new); {len(todo)} to read "
                 f"(first {DEEP_PAGES} pages, ≤{DEEP_MB} MB)")
    save_all(store)
    done, t0 = 0, time.time()
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(read_one, todo):
            store[res["ann_id"]] = res
            done += 1
            if done % SAVE_EVERY == 0:
                save_all(store)
                note("deep", f"{done}/{len(todo)} read ({time.time() - t0:.0f}s)")
    save_all(store)
    tagged = sum(1 for r in store.values() if r.get("tags"))
    read = sum(1 for r in store.values() if r.get("read_status") == "read")
    note("deep", f"done: {read} filings read, {tagged} carry a restructuring tag")
    return store


def restructuring_rows(store: dict[str, dict]) -> list[dict]:
    """The tagged filings in the matches schema (source NSE, tags multi)."""
    out = []
    for r in store.values():
        if not r.get("tags"):
            continue
        tags = r["tags"].split("|")
        out.append({"date": r["date"], "symbol": r["symbol"], "company": r["company"],
                    "source": "NSE", "category": r["category"], "kind": tags[0],
                    "tags": r["tags"], "headline": r["headline"],
                    "attachment": r["attachment"], "ann_id": r["ann_id"],
                    "file_size": r["file_size"], "text_file": ""})
    return out


if __name__ == "__main__":
    import datetime as dt
    members = FA.universe()
    feeds = []
    for a, b in FA.month_windows(dt.date.today(), 370):
        feeds.append(FA.nse_fetch(a, b))
        time.sleep(1)
    run_deep(feeds, members, note=lambda s, m: print(f"[{s}] {m}", file=sys.stderr))
