"""
refresh_constituents.py — the live universe, kept honest MONTHLY.

    python3 refresh_constituents.py            # respects the 30-day stamp
    python3 refresh_constituents.py --force    # pull now regardless

The stored NiftyTotalMarket constituents file goes stale as the index
rebalances. This module pulls the OFFICIAL current list from NSE
Indices, and only when the membership actually differs from the
stored file does it rewrite it — every added and removed symbol is
printed, never silent. A stamp file remembers the last check so the
live screen re-pulls at most once a month; a network failure warns
and falls back to the stored list, never blocking a run.

The live screen (analyze.py run) calls refresh() automatically.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
STORED = INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"
STAMP = INDIA / "NiftyTotalMarket" / "_constituents_refreshed.txt"
URL = ("https://niftyindices.com/IndexConstituent/"
       "ind_niftytotalmarket_list.csv")
MAX_AGE_DAYS = 30
FIELDS = ["nse_symbol", "company_name", "industry", "series", "isin"]


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


def refresh(force: bool = False) -> dict:
    """Pull-if-due; update the stored file only on a real change."""
    if not force and not _stale():
        return {"checked": False, "changed": False,
                "note": "constituents checked within the last month"}
    try:
        req = urllib.request.Request(URL, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
            "Referer": "https://niftyindices.com/"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            text = resp.read().decode("utf-8", "replace")
        official = parse_official(text)
        if len(official) < 600:
            raise ValueError(f"only {len(official)} rows — refusing to "
                             f"replace the stored list with a stub")
    except Exception as e:                # noqa: BLE001 — never block
        return {"checked": False, "changed": False,
                "note": f"official pull failed ({e}); the stored list "
                        f"stands"}
    with open(STORED) as fh:
        stored = list(csv.DictReader(fh))
    d = diff_membership(stored, official)
    if d["changed"]:
        with open(STORED, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            w.writeheader()
            w.writerows(official)
    STAMP.write_text(dt.date.today().isoformat() + "\n")
    return {"checked": True, "changed": d["changed"],
            "added": d["added"], "removed": d["removed"],
            "count": len(official)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    r = refresh(force=args.force)
    if not r["checked"]:
        print(r["note"])
        return
    if r["changed"]:
        print(f"constituents UPDATED — {r['count']} members now; "
              f"added: {', '.join(r['added']) or '—'}; "
              f"removed: {', '.join(r['removed']) or '—'}")
    else:
        print(f"constituents unchanged ({r['count']} members)")


if __name__ == "__main__":
    main()
