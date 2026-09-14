"""
backtest.py — run the SAME Darvas skill as of a date in the past.

    python3 backtest.py --start 2025-06-01 --end 2026-03-31 [--top 25]

Nothing in the method changes: the runner re-points the skill at a frozen
window and lets it run exactly as it would have on the as-of date.

  * PRICE/VOLUME: fetched for [start, end] only (Yahoo period1/period2)
    into a SEPARATE archive beside the live one —
    India/VolumeAndPricingBacktest/<start>_to_<end>/ — so backtest data
    never mixes with the live folder. Week completeness is judged as of
    `end`: an unfinished final week is tested pro-rated, exactly as a
    live run on that day would have.
  * PROFIT AND LOSS: the stored statements are filtered to fiscal years
    ENDING ON OR BEFORE the as-of fiscal year — nothing later leaks in.
  * CONFERENCE CALLS: excluded entirely. The transcript archive contains
    calls AFTER the window, and sampling "only the old part" cannot be
    verified page by page — so the new-age read is honestly reported as
    excluded rather than quietly contaminated.
  * LEDGER: the backtest writes its own positions file; the live
    _positions.csv is never touched.

The report lands beside the live one, named for the window.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import analyze as AZ         # noqa: E402
import darvas as DV          # noqa: E402
import earnings as EP        # noqa: E402
import fetch_data as FD      # noqa: E402

INDIA = HERE.parent.parent.parent


def window_dir(start: dt.date, end: dt.date) -> Path:
    return (INDIA / "VolumeAndPricingBacktest"
            / f"{start.isoformat()}_to_{end.isoformat()}")


def window_url(sym: str, start: dt.date, end: dt.date) -> str:
    import urllib.parse
    p1 = int(dt.datetime(start.year, start.month, start.day).timestamp())
    p2 = int(dt.datetime(end.year, end.month, end.day, 23, 59).timestamp())
    return (f"https://query1.finance.yahoo.com/v8/finance/chart/"
            f"{urllib.parse.quote(sym, safe='')}.NS"
            f"?period1={p1}&period2={p2}&interval=1d")


def asof_fiscal_year(end: dt.date) -> str:
    """The last fiscal year whose statements the window may use: the FY
    ending in the March ON OR BEFORE `end` (Indian FYs end 31 March)."""
    year = end.year if (end.month, end.day) >= (3, 31) else end.year - 1
    return f"Mar {year}"


def banner(start: dt.date, end: dt.date, fy: str) -> str:
    return (
        f"> **BACKTEST — as of {end.isoformat()}.** Price and volume data "
        f"cover {start.isoformat()} to {end.isoformat()} ONLY, stored "
        f"separately in `VolumeAndPricingBacktest/`. Statements are cut "
        f"at fiscal year {fy}; note that in reality {fy} annual results "
        f"would not all have been published by {end.isoformat()} — they "
        f"are included because the backtest's rule is 'no data after "
        f"{fy}', stated here so the optimism is visible. The conference-"
        f"call read is EXCLUDED (the transcript archive contains calls "
        f"after the window), so every 'new-age' verdict below is "
        f"'not assessed' by design, and the live ledger is untouched.\n")


def activate(start: dt.date, end: dt.date, top: int) -> None:
    out_dir = window_dir(start, end)
    tag = f"{start.isoformat()}_to_{end.isoformat()}"

    # 1. the frozen price/volume window, in its own archive
    FD.OUT_DIR = out_dir
    FD._yahoo_url = lambda sym: window_url(sym, start, end)
    _orig_agg = FD.aggregate_weeks
    FD.aggregate_weeks = lambda daily, today=None: _orig_agg(
        daily, today=end)                     # completeness as of `end`
    DV.DATA_DIR = out_dir
    AZ.FD = FD

    # 2. statements cut at the as-of fiscal year
    fy = asof_fiscal_year(end)
    import pandas as pd
    df = pd.read_csv(EP.PL_LONG)
    years = sorted(df.year.unique(), key=EP._year_key)
    keep = [y for y in years if EP._year_key(y) <= EP._year_key(fy)]
    EP._PL_CACHE["df"] = df[df.year.isin(keep)]

    # 3. no conference-call read: the archive post-dates the window
    EP.new_age_verdict = lambda sym, allow_ai=True: {
        "status": "excluded_from_backtest", "new_age": "not assessed",
        "rationale": "the transcript archive contains calls after the "
                     "backtest window — excluded rather than contaminated"}

    # 4. the backtest's own report and ledger — the live ones untouched
    AZ.REPORT = AZ.OUT_DIR / f"DARVAS_BACKTEST_{tag}.md"
    AZ.LEDGER = AZ.OUT_DIR / f"_positions_backtest_{tag}.csv"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, type=dt.date.fromisoformat)
    ap.add_argument("--end", required=True, type=dt.date.fromisoformat)
    ap.add_argument("--top", type=int, default=AZ.DEFAULT_TOP)
    ap.add_argument("--no-fetch", action="store_true")
    args = ap.parse_args()
    if args.end <= args.start:
        ap.error("--end must be after --start")

    activate(args.start, args.end, args.top)
    run_args = argparse.Namespace(top=args.top, no_fetch=args.no_fetch,
                                  quick=True)   # no AI inside a backtest
    AZ.cmd_run(run_args)

    fy = asof_fiscal_year(args.end)
    md = AZ.REPORT.read_text()
    head, rest = md.split("\n", 1)
    AZ.REPORT.write_text(head + "\n\n" + banner(args.start, args.end, fy)
                         + rest)
    print(f"backtest report: {AZ.REPORT}")


if __name__ == "__main__":
    main()
