"""
demerger_ground_truth.py — the demergers NSE's own bhavcopy bundles record,
as an independent check on the skill's list.

    python3 demerger_ground_truth.py --days 400        # pull and build
    python3 demerger_ground_truth.py --no-fetch        # rebuild from stored bundles

Every trading day NSE publishes a PR bundle (PR<ddmmyy>.zip) beside the
bhavcopy. Two files in it see a demerger without anyone writing a headline:

  bc<ddmmyyyy>.csv   the corporate-actions / book-closure file: one row per
                     record date with its PURPOSE — "Demerger", "Scheme of
                     Arrangement", "Spin off" — for the PARENT symbol;
  pd<ddmmyyyy>.csv   the day's price file for every series: a RESULTING
                     company lists as a symbol never seen before.

The bundle is small (about 0.6 MB), so the year's bundles are kept under
`_bhav_bundles/` and parsed into:

  NiftyTotalMarket/_demerger_ground_truth.csv
      date (record / ex date), symbol, company, purpose, source
      (bc = corporate-actions file, api = NSE corporate-actions API,
      newlist = first appearance in the price file)

The skill's own list is then checked against this file by
Skills/SpinOffSkill/scripts/validate_demergers.py.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import re
import sys
import time
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fetch_announcements as FA        # noqa: E402

BUNDLES = HERE / "_bhav_bundles"
GROUND_TRUTH = FA.OUT_DIR / "_demerger_ground_truth.csv"
PR_URL = "https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR{ddmmyy}.zip"
CA_API = ("https://www.nseindia.com/api/corporates-corporateActions"
          "?index=equities&from_date={frm}&to_date={to}")
PURPOSE_RX = re.compile(r"de-?merg|scheme of arrangement|spin[\s-]?off|hiv(e|ing)[\s-]?off|arrangement", re.I)
FIELDS = ["date", "symbol", "company", "purpose", "source", "detail", "isin", "register_symbol"]


# ------------------------------------------------------------- bundles

def trading_days(end: dt.date, days: int) -> list[dt.date]:
    d, out = end - dt.timedelta(days=days), []
    while d <= end:
        if d.weekday() < 5:
            out.append(d)
        d += dt.timedelta(days=1)
    return out


def fetch_bundle(day: dt.date) -> Path | None:
    """The day's PR bundle on disk (cached); None on a holiday (404)."""
    BUNDLES.mkdir(parents=True, exist_ok=True)
    path = BUNDLES / f"PR{day:%d%m%y}.zip"
    miss = BUNDLES / f"PR{day:%d%m%y}.none"
    if path.exists():
        return path
    if miss.exists():
        return None
    code, body = FA._get(PR_URL.format(ddmmyy=day.strftime("%d%m%y")), timeout=60,
                         headers={"Referer": "https://www.nseindia.com/"})
    if code == 200 and body[:2] == b"PK":
        path.write_bytes(body)
        return path
    if code == 404:
        miss.write_text("holiday or not published")
    return None


def parse_bc(zpath: Path) -> list[dict]:
    """Corporate-action rows whose purpose names a demerger or scheme."""
    out = []
    with zipfile.ZipFile(zpath) as z:
        names = [n for n in z.namelist() if n.lower().startswith("bc")]
        for n in names:
            text = z.read(n).decode("utf-8", "replace")
            rd = csv.DictReader(io.StringIO(text))
            for r in rd:
                r = {(k or "").strip().upper(): (v or "").strip() for k, v in r.items()}
                purpose = r.get("PURPOSE") or ""
                if not PURPOSE_RX.search(purpose):
                    continue
                def col(*needles):
                    for k, v in r.items():
                        if v and any(nd in k for nd in needles):
                            return v
                    return ""
                date = col("RECORD") or col("EX DT", "EX-DT", "EX DATE", "EXDATE") or col("BC ST", "BC_ST") or ""
                if not date:                       # the file is dated; fall back to its day
                    date = zpath.stem[2:4] + "-" + zpath.stem[4:6] + "-20" + zpath.stem[6:8]
                    date = "20" + zpath.stem[6:8] + "-" + zpath.stem[4:6] + "-" + zpath.stem[2:4]
                out.append({"date": _iso(date), "symbol": r.get("SYMBOL", ""),
                            "company": r.get("SECURITY", ""), "purpose": purpose,
                            "source": "bc", "detail": f"ex {_iso(col('EX DT', 'EX-DT', 'EX DATE'))}; series {r.get('SERIES', '')}; file {zpath.name}"})
    return out


def parse_pd_symbols(zpath: Path) -> set[str]:
    """Every EQ/BE symbol in the day's price file."""
    syms = set()
    with zipfile.ZipFile(zpath) as z:
        for n in z.namelist():
            if not n.lower().startswith("pd"):
                continue
            text = z.read(n).decode("utf-8", "replace")
            for r in csv.DictReader(io.StringIO(text)):
                r = {(k or "").strip().upper(): (v or "").strip() for k, v in r.items()}
                if r.get("SERIES") in ("EQ", "BE") and r.get("SYMBOL"):
                    syms.add(r["SYMBOL"])
    return syms


def _iso(s: str) -> str:
    s = (s or "").strip()
    for fmt in ("%d-%b-%Y", "%d-%m-%Y", "%d/%m/%Y", "%d %b %Y"):
        try:
            return dt.datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    return s


def api_rows(frm: dt.date, to: dt.date) -> list[dict]:
    """The same record dates from NSE's corporate-actions API, as a
    second reading of the same register."""
    import json                                   # noqa: PLC0415
    code, body = FA._get(CA_API.format(frm=frm.strftime("%d-%m-%Y"), to=to.strftime("%d-%m-%Y")),
                         timeout=120, headers={"Accept": "application/json",
                                               "Referer": "https://www.nseindia.com/companies-listing/corporate-filings-actions"})
    if code != 200 or not body:
        return []
    out = []
    for a in json.loads(body):
        if PURPOSE_RX.search(a.get("subject") or ""):
            out.append({"date": _iso(a.get("recDate") or a.get("exDate") or ""),
                        "symbol": a.get("symbol", ""), "company": a.get("comp", ""),
                        "purpose": a.get("subject", ""), "source": "api",
                        "detail": f"ex {_iso(a.get('exDate', ''))}", "isin": a.get("isin", "")})
    return out


# ----------------------------------------------------------- the universe

def universe_isins(path: Path = FA.CONSTITUENTS) -> dict[str, str]:
    """{ISIN: universe symbol} from the constituents file — the stable key
    across a rename (Tata Motors → TMPV, HEG → HEGAM)."""
    out = {}
    if path.exists():
        with open(path) as fh:
            for r in csv.DictReader(fh):
                if r.get("isin") and r.get("nse_symbol"):
                    out[r["isin"].strip()] = r["nse_symbol"].strip()
    return out


def _first_token(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (name or "").lower().split()[0]) if (name or "").split() else ""


def canonicalise(rows: list[dict], members: dict, isin_map: dict[str, str]) -> list[dict]:
    """Dedupe, and put every register row under its UNIVERSE symbol:
      - an API row carries the ISIN, so a renamed company is recognised
        whatever symbol the register used;
      - a bc row (no ISIN) under a symbol that is not a member is matched to
        an API row of the same date and purpose family whose company name
        starts with the same word (bc 'TATAMOTORS / Tata Motors Limited'
        14-Oct-2025 ↔ api TMPV 'Tata Motors …' 14-Oct-2025);
    `register_symbol` keeps what the register printed. in_universe is then
    by canonical symbol."""
    seen, out = set(), []
    api_by_date: dict[tuple[str, bool], list[dict]] = {}
    for r in rows:
        r.setdefault("isin", "")
        r["register_symbol"] = r["symbol"]
        if r["source"] == "api" and r["isin"] in isin_map:
            r["symbol"] = isin_map[r["isin"]]
        if r["source"] == "api":
            api_by_date.setdefault((r["date"], bool(re.search(r"de-?merg", r["purpose"], re.I))), []).append(r)
    for r in rows:
        if r["source"] == "bc" and r["symbol"] not in members:
            fam = bool(re.search(r"de-?merg", r["purpose"], re.I))
            for a in api_by_date.get((r["date"], fam), []):
                if a["symbol"] in members and _first_token(a["company"]) == _first_token(r["company"]):
                    r["symbol"], r["isin"] = a["symbol"], a.get("isin", "")
                    break
    for r in rows:
        k = (r["source"], r["symbol"], r["date"], r["purpose"][:40])
        if k in seen:
            continue
        seen.add(k)
        r["in_universe"] = "yes" if r["symbol"] in members else ""
        out.append(r)
    return out


# ----------------------------------------------------------- equity list

EQUITY_L = "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv"
EQUITY_LIST = FA.OUT_DIR / "_nse_equity_list.csv"


def fetch_equity_list(path: Path = EQUITY_LIST) -> list[dict]:
    """NSE's list of every listed equity with its DATE OF LISTING — the
    exchange's word on when a company (a resulting company among them)
    began trading. Written to NiftyTotalMarket/_nse_equity_list.csv as
    symbol, name, listing_date (ISO), series, isin."""
    code, body = FA._get(EQUITY_L, timeout=60, headers={"Referer": "https://www.nseindia.com/"})
    if code != 200 or not body:
        return []
    out = []
    for r in csv.DictReader(io.StringIO(body.decode("utf-8", "replace"))):
        r = {(k or "").strip().upper(): (v or "").strip() for k, v in r.items()}
        if not r.get("SYMBOL"):
            continue
        out.append({"symbol": r["SYMBOL"], "name": r.get("NAME OF COMPANY", ""),
                    "listing_date": _iso(r.get("DATE OF LISTING", "")), "series": r.get("SERIES", ""),
                    "isin": r.get("ISIN NUMBER", "")})
    if out:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["symbol", "name", "listing_date", "series", "isin"])
            w.writeheader()
            w.writerows(sorted(out, key=lambda r: r["symbol"]))
    return out


# ----------------------------------------------------------------- build

def build(days: int = 400, fetch: bool = True, today: dt.date | None = None,
          note=print) -> list[dict]:
    today = today or dt.date.today()
    members = FA.universe()
    rows: list[dict] = []
    seen_syms: set[str] = set()
    first_seen: dict[str, str] = {}
    n_bundles = 0
    for day in trading_days(today, days):
        z = fetch_bundle(day) if fetch else (BUNDLES / f"PR{day:%d%m%y}.zip")
        if not z or not z.exists():
            continue
        n_bundles += 1
        try:
            rows += parse_bc(z)
            syms = parse_pd_symbols(z)
        except zipfile.BadZipFile:
            continue
        if seen_syms:
            for s in syms - seen_syms:
                first_seen.setdefault(s, day.isoformat())
        seen_syms |= syms
        if fetch:
            time.sleep(0.2)
    note("gt", f"{n_bundles} bundles read; {len(rows)} corporate-action rows name a demerger / scheme")
    if fetch:
        try:
            note("gt", f"{len(fetch_equity_list())} listed equities with listing dates (EQUITY_L)")
        except Exception as e:                        # noqa: BLE001
            note("gt", f"equity list failed: {e}")
    # new listings: a symbol first seen after the window's first month is a
    # new listing — IPOs included; the validator uses them only to confirm
    # a resulting company's arrival, never as a demerger on its own
    cutoff = (today - dt.timedelta(days=days - 35)).isoformat()
    for s, d in first_seen.items():
        if d >= cutoff:
            rows.append({"date": d, "symbol": s, "company": "", "purpose": "first appearance in the price file",
                         "source": "newlist", "detail": ""})
    try:
        rows += api_rows(today - dt.timedelta(days=days), today)
    except Exception as e:                        # noqa: BLE001
        note("gt", f"corporate-actions API failed: {e}")
    out = canonicalise(rows, members, universe_isins())
    out.sort(key=lambda r: (r["date"], r["symbol"]))
    GROUND_TRUTH.parent.mkdir(parents=True, exist_ok=True)
    with open(GROUND_TRUTH, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS + ["in_universe"])
        w.writeheader()
        w.writerows(out)
    note("gt", f"{len(out)} rows written; universe demerger record dates: "
               f"{len({r['symbol'] for r in out if r['source'] in ('bc', 'api') and r['in_universe'] and re.search(r'de-?merg', r['purpose'], re.I)})}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=400)
    ap.add_argument("--no-fetch", action="store_true")
    a = ap.parse_args()
    build(a.days, fetch=not a.no_fetch, note=lambda s, m: print(f"[{s}] {m}", file=sys.stderr))


if __name__ == "__main__":
    main()
