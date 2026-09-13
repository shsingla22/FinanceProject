"""
longrun.py — the finalised skill, run as a portfolio for SIX YEARS.

    python3 longrun.py                      # fetch (if needed) + replay
    python3 longrun.py --no-fetch           # reuse the stored archive

June 2020 → the present, ₹100 to start, all in cash. Every Friday after
the close the FULL three-gate screen (weekly volume trigger,
month-vs-year volume, rising box ladder) re-runs over the whole
NiftyTotalMarket universe; fresh BUY/ACCUMULATE signals are funded from
cash — equal slices of one tenth of equity, best volume reaction first,
entries at the next trading day's open, falling earnings power refused,
nothing below half a slice, no borrowed money. Stops are checked daily
and ratcheted up weekly; a stopped symbol returns only by passing the
full screen again. When nothing qualifies, the money simply STAYS IN
CASH (uninvested, earning nothing — stated, not hidden).

Point-in-time discipline:
  * one continuous price archive is fetched for the whole window
    (June 2019 onward, so the very first screen already has its year
    of volume baseline) — no seams, no stitching;
  * every Friday screen sees only bars up to that Friday;
  * the earnings gate reads only fiscal years ENDED on or before the
    last 31 March at each screen date — the cut ROLLS forward year by
    year, and non-March fiscal-year ends are compared by actual date;
  * the conference-call read is excluded (the transcript archive
    postdates most of the window — excluded beats contaminated).

Honest limits that CANNOT be engineered away and are printed in the
report: today's constituent list is used throughout (survivorship
bias — stocks that later died or left the index are underrepresented),
and Yahoo prices are split-adjusted history as served today.

Outputs: a detailed report with the complete trade blotter, monthly
equity curve, calendar-year returns, drawdown, trade statistics, CAGR
and the Nifty 50 comparison — plus the full event ledger as a CSV.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import statistics
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import backtest as BT        # noqa: E402
import earnings as EP        # noqa: E402
import fetch_data as FD      # noqa: E402
import rolling as RL         # noqa: E402
import walkforward as WF     # noqa: E402

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "DarvasAnalysis"

FETCH_START = dt.date(2019, 6, 1)     # one year of runway before screening
SCREEN_START = "2020-06-01"           # first Friday screen: 2020-06-05
SLOTS = 10                            # equal slices: one tenth of equity

_MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}


# ------------------------------------------------------------------ data

def ensure_archive(end: dt.date) -> Path:
    """The continuous window archive, fetched once and reused."""
    adir = BT.window_dir(FETCH_START, end)
    if (adir / "_all_daily_long.csv").exists():
        print(f"archive reused: {adir}", file=sys.stderr)
        return adir
    print(f"fetching {FETCH_START} → {end} for the whole universe "
          f"into {adir} …", file=sys.stderr)
    old_dir, old_url = FD.OUT_DIR, FD._yahoo_url
    FD.OUT_DIR = adir
    FD._yahoo_url = lambda sym: BT.window_url(sym, FETCH_START, end)
    try:
        summary = FD.fetch_universe()
        print(json.dumps(summary), file=sys.stderr)
    finally:
        FD.OUT_DIR, FD._yahoo_url = old_dir, old_url
    return adir


def load_bars(archive: Path) -> dict[str, list[dict]]:
    by_date = WF._load_daily_csv(archive / "_all_daily_long.csv")
    return {sym: [rows[d] for d in sorted(rows)]
            for sym, rows in by_date.items()}


def fetch_nifty(start: dt.date, end: dt.date) -> list[tuple[str, float]]:
    """Daily closes for the Nifty 50 (^NSEI) over the window."""
    p1 = int(dt.datetime(start.year, start.month, start.day).timestamp())
    p2 = int(dt.datetime(end.year, end.month, end.day, 23, 59).timestamp())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI"
           f"?period1={p1}&period2={p2}&interval=1d")
    req = urllib.request.Request(url, headers={"User-Agent": FD.UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    result = data["chart"]["result"][0]
    ts = result["timestamp"]
    closes = result["indicators"]["quote"][0]["close"]
    return [(dt.date.fromtimestamp(t).isoformat(), round(c, 2))
            for t, c in zip(ts, closes) if c is not None]


# ------------------------------------------- the rolling statement cut

def fy_end_date(label: str) -> dt.date | None:
    """'Mar 2020' -> 2020-03-31; None when the label doesn't parse."""
    m = re.match(r"([A-Z][a-z]{2})\s+(\d{4})", str(label).strip())
    if not m or m.group(1) not in _MONTHS:
        return None
    month, year = _MONTHS[m.group(1)], int(m.group(2))
    nxt = dt.date(year + (month == 12), (month % 12) + 1, 1)
    return nxt - dt.timedelta(days=1)


def make_earnings_ok():
    """earnings_ok(sym, day): the P&L frame is cut at the last 31 March
    on or before `day` — the same convention as the parent backtests,
    rolled forward as the replay advances — and non-March fiscal-year
    ends are compared by their real end date, so a 'Jun 2020' year can
    never leak into a June-2020 screen."""
    import pandas as pd
    full = pd.read_csv(EP.PL_LONG)
    ends = {y: fy_end_date(y) for y in full.year.unique()}
    frames: dict = {}
    memo: dict = {}

    def earnings_ok(sym: str, day: dt.date) -> bool:
        fy = BT.asof_fiscal_year(day)                    # e.g. "Mar 2020"
        if (sym, fy) in memo:
            return memo[(sym, fy)]
        if fy not in frames:
            cut = fy_end_date(fy)
            keep = [y for y, e in ends.items() if e and e <= cut]
            frames[fy] = full[full.year.isin(keep)]
        EP._PL_CACHE["df"] = frames[fy]
        memo[(sym, fy)] = EP.earnings_power(sym)["verdict"] != "FALLING"
        return memo[(sym, fy)]

    return earnings_ok


# ---------------------------------------------------------------- report

def _yearly(curve: list[dict]) -> list[dict]:
    """Calendar-year rows from the weekly equity curve."""
    rows, prev_eq = [], curve[0]["equity"]
    by_year: dict[int, dict] = {}
    for w in curve:
        by_year[int(w["date"][:4])] = w
    start_label = curve[0]["date"]
    for y in sorted(by_year):
        w = by_year[y]
        rows.append({"year": y, "through": w["date"], "equity": w["equity"],
                     "ret_pct": (w["equity"] - prev_eq) / prev_eq * 100,
                     "since": start_label})
        prev_eq = w["equity"]
        start_label = w["date"]
    return rows


def _max_drawdown(curve: list[dict]) -> dict:
    peak, peak_d, worst, worst_row = -1.0, "", 0.0, None
    for w in curve:
        if w["equity"] > peak:
            peak, peak_d = w["equity"], w["date"]
        dd = (w["equity"] - peak) / peak * 100
        if dd < worst:
            worst = dd
            worst_row = {"from": peak_d, "to": w["date"], "dd_pct": dd}
    return worst_row or {"from": "—", "to": "—", "dd_pct": 0.0}


def _cagr(final: float, initial: float, days: int) -> float:
    return ((final / initial) ** (365.25 / days) - 1) * 100


def write_report(res: dict, args, through: str, nifty: list, archive: Path,
                 n_syms: int) -> Path:
    tag = f"{SCREEN_START}_to_{through}"
    report = OUT_DIR / f"DARVAS_BACKTEST_LONGRUN_{tag}.md"
    ledger_csv = OUT_DIR / f"_longrun_events_{tag}.csv"

    with open(ledger_csv, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "symbol", "event"])
        for d, sym, what in sorted(res["blotter"]):
            w.writerow([d, sym, what])

    curve = res["equity_curve"]
    days = (dt.date.fromisoformat(through)
            - dt.date.fromisoformat(curve[0]["date"])).days
    cagr = _cagr(res["final_equity"], args.capital, days)

    n0 = next((c for d0, c in nifty if d0 >= curve[0]["date"]), None)
    n1 = nifty[-1][1] if nifty else None
    nifty_100 = 100 * n1 / n0 if n0 else None
    nifty_cagr = _cagr(n1, n0, days) if n0 else None
    nifty_by_date = dict(nifty)

    closed = res["closed"]
    wins = [c for c in closed if c["ret_pct"] > 0]
    hold_days = [(dt.date.fromisoformat(c["exit_date"])
                  - dt.date.fromisoformat(c["entry_date"])).days
                 for c in closed]
    cash_share = [w["cash"] / w["equity"] * 100 for w in curve]
    all_cash_weeks = sum(1 for w in curve if w["positions"] == 0)

    trades = [b for b in sorted(res["blotter"])
              if "BUY ₹" in b[2] or "SELL ₹" in b[2]]

    A = [f"# The Darvas screen, run for six years — {SCREEN_START} → "
         f"{through}", "",
         f"> **LONG-RUN BACKTEST.** One continuous price archive "
         f"({FETCH_START} → {through}, {n_syms} symbols, fetched once "
         f"into `{archive.name}/`) so every Friday screen has its full "
         f"year of volume baseline and six months of boxes. Every screen "
         f"sees only bars up to its own Friday. The earnings gate reads "
         f"only fiscal years ended on or before the last 31 March at "
         f"each screen date — the cut rolls forward with the replay — "
         f"and the conference-call read is excluded. **Two limits that "
         f"cannot be engineered away:** the universe is TODAY'S "
         f"NiftyTotalMarket constituents (survivorship bias — companies "
         f"that later failed or left the index are missing from the "
         f"early years, which flatters results), and Yahoo serves "
         f"split-adjusted history as it stands today. No costs, no "
         f"slippage, stop exits at the stop price, fractional shares.",
         "",
         "## The rules, exactly as the live skill prescribes", "",
         f"₹{args.capital:,.0f} starts ALL IN CASH. Every Friday after "
         f"the close, the full three-gate screen (weekly volume ≥1.5× "
         f"the 12-week average WITH a rising price; last month's volume "
         f"≥1.5× the year's norm; at least 3 boxes with the last 3 "
         f"midpoints rising) runs over the whole universe. Fresh "
         f"BUY/ACCUMULATE signals are funded from cash — equal slices "
         f"of one tenth of equity, best volume reaction first, entries "
         f"at the next trading day's open, falling earnings power "
         f"refused, nothing below half a slice. Stops (box bottom − "
         f"max(0.3×height, 5% of bottom)) are checked daily and "
         f"ratcheted up weekly; the stabilisation grace applies — only "
         f"the stop itself exits. A stopped symbol returns only by "
         f"passing the full screen again. **When nothing qualifies, "
         f"the cash stays cash.**", "",
         "## The headline", "",
         f"| | ₹100 became | CAGR |",
         f"|---|---:|---:|",
         f"| **This system** | **₹{res['final_equity']:,.2f}** | "
         f"**{cagr:+.2f}% a year** |"]
    if nifty_100:
        A.append(f"| Nifty 50 (same window) | ₹{nifty_100:,.2f} | "
                 f"{nifty_cagr:+.2f}% a year |")
    A += ["",
          f"{(dt.date.fromisoformat(through) - dt.date.fromisoformat(curve[0]['date'])).days / 365.25:.2f} "
          f"years, {len(curve)} weekly screens, {len(trades)} trades "
          f"printed in the blotter below.", ""]

    A += ["## Calendar-year equity", "",
          "| Year (through) | Equity (₹) | Return |"
          + (" Nifty 50 |" if nifty else ""),
          "|---|---:|---:|" + ("---:|" if nifty else "")]
    prev_n = n0
    for r in _yearly(curve):
        line = (f"| {r['year']} ({r['through']}) | {r['equity']:,.2f} | "
                f"{r['ret_pct']:+.1f}% |")
        if nifty:
            n_now = nifty_by_date.get(r["through"]) or next(
                (c for d0, c in reversed(nifty) if d0 <= r["through"]), None)
            if n_now and prev_n:
                line += f" {(n_now - prev_n) / prev_n * 100:+.1f}% |"
                prev_n = n_now
            else:
                line += " — |"
        A.append(line)
    A.append("")

    dd = _max_drawdown(curve)
    A += ["## What it took to earn it", "",
          f"- **Maximum drawdown: {dd['dd_pct']:.1f}%** (peak "
          f"{dd['from']} → trough {dd['to']}, on weekly closes).",
          f"- **{len(closed)} closed trades**: {len(wins)} winners "
          f"({len(wins) / len(closed) * 100:.0f}%), average winner "
          f"{statistics.mean([c['ret_pct'] for c in wins]):+.1f}%, "
          f"average loser "
          f"{statistics.mean([c['ret_pct'] for c in closed if c['ret_pct'] <= 0]):+.1f}%."
          if closed and wins and len(wins) < len(closed) else
          f"- **{len(closed)} closed trades.**",
          f"- Best closed trade "
          f"{max(closed, key=lambda c: c['ret_pct'])['symbol']} "
          f"{max(c['ret_pct'] for c in closed):+.1f}%; worst "
          f"{min(closed, key=lambda c: c['ret_pct'])['symbol']} "
          f"{min(c['ret_pct'] for c in closed):+.1f}%."
          if closed else "- No closed trades.",
          f"- Median holding period {statistics.median(hold_days):.0f} "
          f"days." if hold_days else "",
          f"- Cash share of equity averaged "
          f"{statistics.mean(cash_share):.0f}% across all weeks "
          f"(median {statistics.median(cash_share):.0f}%); the "
          f"portfolio sat FULLY in cash for {all_cash_weeks} of "
          f"{len(curve)} weeks — rule 3: when nothing qualifies, "
          f"the money waits.", ""]

    A += ["## Monthly equity curve", "",
          "| Month-end screen | Equity (₹) | Cash (₹) | Positions |",
          "|---|---:|---:|---:|"]
    last_in_month: dict[str, dict] = {}
    for w in curve:
        last_in_month[w["date"][:7]] = w
    for _, w in sorted(last_in_month.items()):
        A.append(f"| {w['date']} | {w['equity']:,.2f} | {w['cash']:,.2f} | "
                 f"{w['positions']} |")
    A.append("")

    if res["book"]:
        A += ["## Still held at the end", "",
              "| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |",
              "|---|---|---:|---:|---:|---:|"]
        for b in res["book"]:
            A.append(f"| {b['symbol']} | {b['entry_date']} | "
                     f"{b['entry_px']:,.2f} | {b['mark_px']:,.2f} | "
                     f"{b['stop']:,.2f} | {b['ret_pct']:+.1f}% |")
        A.append("")

    if closed:
        A += ["## Every closed trade", "",
              "| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |",
              "|---|---|---:|---|---:|---:|"]
        for c in closed:
            A.append(f"| {c['symbol']} | {c['entry_date']} | "
                     f"{c['entry_px']:,.2f} | {c['exit_date']} | "
                     f"{c['exit_px']:,.2f} | {c['ret_pct']:+.1f}% |")
        A.append("")

    A += ["## The complete trade blotter", "",
          "*Buys and sells only; every stop raise, refused signal and "
          f"unfunded signal is in `{ledger_csv.name}` beside this "
          f"report ({len(res['blotter'])} events in all).*", "", "```"]
    for d, sym, what in trades:
        A.append(f"{d}  {sym:11s} {what}")
    A += ["```", ""]

    report.write_text("\n".join(A))
    return report


# ------------------------------------------------------------------ main

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--capital", type=float, default=100.0)
    ap.add_argument("--no-fetch", action="store_true",
                    help="reuse the stored archive, never fetch")
    ap.add_argument("--end", default=None,
                    help="archive end date (default: today)")
    args = ap.parse_args()

    end = (dt.date.fromisoformat(args.end) if args.end else dt.date.today())
    archive = (BT.window_dir(FETCH_START, end) if args.no_fetch
               else ensure_archive(end))
    if args.no_fetch and not (archive / "_all_daily_long.csv").exists():
        cands = sorted((INDIA / "VolumeAndPricingBacktest").glob(
            f"{FETCH_START}_to_*"))
        if not cands:
            sys.exit("no archive found and --no-fetch given")
        archive = cands[-1]
        print(f"archive reused: {archive}", file=sys.stderr)

    bars_by = load_bars(archive)
    print(f"{len(bars_by)} symbols loaded", file=sys.stderr)
    through = max(b[-1]["date"] for b in bars_by.values())

    res = RL.run_rolling(bars_by, [], SCREEN_START, through, args.capital,
                         make_earnings_ok(), slots=SLOTS)
    try:
        nifty = fetch_nifty(dt.date.fromisoformat(SCREEN_START), end)
    except Exception as e:                # noqa: BLE001 — benchmark only
        print(f"nifty fetch failed ({e}); report goes out without the "
              f"benchmark", file=sys.stderr)
        nifty = []

    report = write_report(res, args, through, nifty, archive, len(bars_by))
    print(f"report: {report}")
    print(f"final equity: ₹{res['final_equity']:,.2f} "
          f"(cash ₹{res['cash']:,.2f} + {len(res['book'])} open positions)")


if __name__ == "__main__":
    main()
