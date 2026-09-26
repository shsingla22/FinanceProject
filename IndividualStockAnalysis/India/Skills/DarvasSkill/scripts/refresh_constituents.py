"""
refresh_constituents.py — the live universe, kept honest MONTHLY.

    python3 refresh_constituents.py            # respects the 30-day stamp
    python3 refresh_constituents.py --force    # pull now regardless

The live universe is the UNION of two lists, each pulled monthly:

  1. the OFFICIAL NiftyTotalMarket constituents from NSE Indices;
  2. the MCAP_TOP (1,250) largest listed companies by market
     capitalisation, from
     the market-cap file inside NSE's daily PR bundle (the same
     official source the point-in-time backtests ranked on) — EQ/BE
     series, listed (not merely permitted), ETFs and funds excluded.

A company outside the index but inside the top 1,250 by size (the
index rebalances only twice a year, and its microcap slice stops well
above the 1,250th company) is therefore screened, and every stored row
says which list(s) it came from (`source`: official, mcap<N>, both). Only when the membership actually differs from the
stored file is it rewritten — every added and removed symbol is
printed, never silent. A stamp file remembers the last check so the
live screen re-pulls at most once a month; a failure of either pull
warns and keeps that list's stored rows, never blocking a run.

The live screen (analyze.py run) calls refresh() automatically.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
STORED = INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"
STAMP = INDIA / "NiftyTotalMarket" / "_constituents_refreshed.txt"
URL = ("https://niftyindices.com/IndexConstituent/"
       "ind_niftytotalmarket_list.csv")
PR_URL = ("https://nsearchives.nseindia.com/archives/equities/bhavcopy/"
          "pr/PR{ddmmyy}.zip")
MAX_AGE_DAYS = 30
MCAP_TOP = 1250
MCAP_TAG = f"mcap{MCAP_TOP}"      # the source tag on size-list rows
PR_LOOKBACK_DAYS = 10
FIELDS = ["nse_symbol", "company_name", "industry", "series", "isin",
          "source"]
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
           "Referer": "https://www.nseindia.com/"}


def parse_official(text: str) -> list[dict]:
    """NSE Indices CSV -> rows in the stored schema, symbol-sorted."""
    rows = []
    for r in csv.DictReader(io.StringIO(text)):
        sym = (r.get("Symbol") or "").strip()
        if not sym or sym.upper().startswith("DUMMY"):
            continue          # NSE's placeholder rows are not stocks
        rows.append({"nse_symbol": sym,
                     "company_name": (r.get("Company Name") or "").strip(),
                     "industry": (r.get("Industry") or "").strip(),
                     "series": (r.get("Series") or "").strip(),
                     "isin": (r.get("ISIN Code") or "").strip()})
    rows.sort(key=lambda x: x["nse_symbol"])
    return rows


def parse_mcap(text: str) -> list[dict]:
    """NSE PR-bundle mcapDDMMYYYY.csv -> [{symbol, name, series,
    category, mcap}] for every row that is a tradeable listed company
    (EQ/BE series, category Listed, not an ETF/fund)."""
    sys.path.insert(0, str(HERE))
    from pit_universe import is_etf          # the backtest's own filter
    out = []
    for r in csv.DictReader(io.StringIO(text)):
        r = {(k or "").strip(): (v or "").strip() for k, v in r.items()}
        sym, series = r.get("Symbol", ""), r.get("Series", "")
        if not sym or series not in ("EQ", "BE") \
                or r.get("Category", "") != "Listed" or is_etf(sym):
            continue
        try:
            mcap = float(r.get("Market Cap(Rs.)", "") or 0)
        except ValueError:
            continue
        if mcap <= 0:
            continue
        out.append({"symbol": sym, "name": r.get("Security Name", ""),
                    "series": series, "mcap": mcap})
    return out


def top_by_mcap(rows: list[dict], n: int = MCAP_TOP) -> list[dict]:
    """The n largest, in the stored schema."""
    best = sorted(rows, key=lambda r: -r["mcap"])[:n]
    return [{"nse_symbol": r["symbol"], "company_name": r["name"],
             "industry": "", "series": r["series"], "isin": ""}
            for r in best]


def _fetch(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def latest_mcap(today: dt.date | None = None,
                fetch=_fetch) -> tuple[str, list[dict]]:
    """The most recent PR bundle's market-cap file, walking back from
    yesterday over weekends and holidays. Returns (date, rows)."""
    today = today or dt.date.today()
    last_err = "no bundle found"
    for back in range(1, PR_LOOKBACK_DAYS + 1):
        d = today - dt.timedelta(days=back)
        if d.weekday() >= 5:
            continue
        try:
            blob = fetch(PR_URL.format(ddmmyy=d.strftime("%d%m%y")))
            with zipfile.ZipFile(io.BytesIO(blob)) as z:
                name = next(n for n in z.namelist()
                            if n.lower().startswith("mcap"))
                rows = parse_mcap(z.read(name).decode("utf-8", "replace"))
            if len(rows) < 1500:
                raise ValueError(f"only {len(rows)} companies in {name}")
            return d.isoformat(), rows
        except Exception as e:            # noqa: BLE001 — try the day before
            last_err = f"{d}: {e}"
    raise RuntimeError(f"no PR bundle in the last {PR_LOOKBACK_DAYS} days "
                       f"({last_err})")


def union_universe(official: list[dict], mcap_top: list[dict]) -> list[dict]:
    """Official ∪ top-by-mcap, one row per symbol, tagged by source.
    The official row's richer fields (industry, ISIN) win."""
    rows = {}
    for r in official:
        rows[r["nse_symbol"]] = {**r, "source": "official"}
    for r in mcap_top:
        s = r["nse_symbol"]
        if s in rows:
            rows[s]["source"] = "both"
        else:
            rows[s] = {**r, "source": MCAP_TAG}
    return sorted(rows.values(), key=lambda x: x["nse_symbol"])


def diff_membership(stored_rows: list[dict],
                    official_rows: list[dict]) -> dict:
    old = {r["nse_symbol"] for r in stored_rows}
    new = {r["nse_symbol"] for r in official_rows}
    return {"added": sorted(new - old), "removed": sorted(old - new),
            "changed": old != new}


def _stale() -> bool:
    if not STAMP.exists():
        return True
    try:
        last = dt.date.fromisoformat(STAMP.read_text().strip()[:10])
    except ValueError:
        return True
    return (dt.date.today() - last).days >= MAX_AGE_DAYS


def refresh(force: bool = False, fetch=_fetch,
            today: dt.date | None = None) -> dict:
    """Pull-if-due; update the stored file only on a real change."""
    if not force and not _stale():
        return {"checked": False, "changed": False,
                "note": "constituents checked within the last month"}
    with open(STORED) as fh:
        rd = csv.DictReader(fh)
        stored = list(rd)
        had_source = "source" in (rd.fieldnames or [])
    for r in stored:                        # files written before `source`
        r.setdefault("source", "official")
    notes = []
    try:
        official = parse_official(fetch(URL).decode("utf-8", "replace"))
        if len(official) < 600:
            raise ValueError(f"only {len(official)} rows — refusing to "
                             f"replace the stored list with a stub")
    except Exception as e:                # noqa: BLE001 — never block
        notes.append(f"official pull failed ({e}); the stored official "
                     f"rows stand")
        official = [r for r in stored if r["source"] in ("official", "both")]
    try:
        mcap_date, mcap_rows = latest_mcap(today, fetch)
        mcap_top = top_by_mcap(mcap_rows, MCAP_TOP)
        notes.append(f"top {MCAP_TOP} by market cap as of {mcap_date}")
    except Exception as e:                # noqa: BLE001 — never block
        notes.append(f"market-cap pull failed ({e}); the stored size-list "
                     f"rows stand")
        mcap_top = [r for r in stored
                    if r["source"] == "both" or r["source"].startswith("mcap")]
    union = union_universe(official, mcap_top)
    d = diff_membership(stored, union)
    if d["changed"] or not had_source:
        with open(STORED, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            w.writeheader()
            w.writerows(union)
    STAMP.write_text((today or dt.date.today()).isoformat() + "\n")
    src = {}
    for r in union:
        src[r["source"]] = src.get(r["source"], 0) + 1
    return {"checked": True, "changed": d["changed"],
            "added": d["added"], "removed": d["removed"],
            "count": len(union), "sources": src, "note": "; ".join(notes)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    r = refresh(force=args.force)
    if not r["checked"]:
        print(r["note"])
        return
    if r.get("note"):
        print(r["note"])
    if r["changed"]:
        print(f"constituents UPDATED — {r['count']} members now "
              f"{r['sources']}; "
              f"added: {', '.join(r['added']) or '—'}; "
              f"removed: {', '.join(r['removed']) or '—'}")
    else:
        print(f"constituents unchanged ({r['count']} members)")


if __name__ == "__main__":
    main()
