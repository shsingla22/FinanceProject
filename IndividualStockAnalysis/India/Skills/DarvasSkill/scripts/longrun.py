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
import frictions as FR       # noqa: E402
import rolling as RL         # noqa: E402
import walkforward as WF     # noqa: E402

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "DarvasAnalysis"

FETCH_START = dt.date(2019, 6, 1)     # one year of runway before screening
SCREEN_START = "2020-06-01"           # first Friday screen: 2020-06-05
SLOTS = 10                            # equal slices: one tenth of equity

inr = RL.inr                          # Indian-system money formatting

_MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}


# ------------------------------------------------------------------ data

def ensure_archive(start: dt.date, end: dt.date) -> Path:
    """The continuous window archive, fetched once and reused."""
    adir = BT.window_dir(start, end)
    if (adir / "_all_daily_long.csv").exists():
        print(f"archive reused: {adir}", file=sys.stderr)
        return adir
    print(f"fetching {start} → {end} for the whole universe "
          f"into {adir} …", file=sys.stderr)
    old_dir, old_url = FD.OUT_DIR, FD._yahoo_url
    FD.OUT_DIR = adir
    FD._yahoo_url = lambda sym: BT.window_url(sym, start, end)
    try:
        summary = FD.fetch_universe()
        print(json.dumps(summary), file=sys.stderr)
    finally:
        FD.OUT_DIR, FD._yahoo_url = old_dir, old_url
    return adir


def _daily_file(archive: Path) -> Path | None:
    for name in ("_all_daily_long.csv", "_all_daily_long.csv.gz"):
        if (archive / name).exists():
            return archive / name
    return None


def load_bars(archive: Path) -> dict[str, list[dict]]:
    import gzip
    path = _daily_file(archive)
    fh = (gzip.open(path, "rt") if path.suffix == ".gz" else open(path))
    by: dict[str, dict[str, dict]] = {}
    with fh:
        for r in csv.DictReader(fh):
            by.setdefault(r["symbol"], {})[r["date"]] = {
                "symbol": r["symbol"], "date": r["date"],
                "open": float(r["open"]) if r["open"] else None,
                "high": float(r["high"]) if r["high"] else None,
                "low": float(r["low"]) if r["low"] else None,
                "close": float(r["close"]),
                "volume": int(r["volume"]) if r.get("volume") else 0}
    return {sym: [rows[d] for d in sorted(rows)]
            for sym, rows in by.items()}


def load_membership(archive: Path) -> dict | None:
    """The rolling radar, when the archive carries one:
    {"YYYY-MM": set of that month's members}."""
    p = archive / "_membership_long.csv"
    if not p.exists():
        return None
    memb: dict[str, set] = {}
    with open(p) as fh:
        for r in csv.DictReader(fh):
            memb.setdefault(r["month"], set()).add(r["symbol"])
    return memb


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


def xirr(flows: list[tuple[str, float]]) -> float:
    """Money-weighted annual return in % — the rate at which the NPV of
    every dated flow (negative = money in, positive = money out/final
    value) is zero. Bisection: robust and derivative-free. With a
    single inflow this IS the CAGR."""
    t0 = dt.date.fromisoformat(min(d for d, _ in flows))

    def npv(rate: float) -> float:
        return sum(cf / (1.0 + rate) **
                   ((dt.date.fromisoformat(d) - t0).days / 365.25)
                   for d, cf in flows)

    lo, hi = -0.9999, 100.0
    f_lo = npv(lo)
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = npv(mid)
        if f_lo * f_mid <= 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return ((lo + hi) / 2) * 100


def dietz_yearly(curve: list[dict], injections: list[tuple[str, float]],
                 ) -> list[dict]:
    """Calendar-year MONEY-WEIGHTED returns (Modified Dietz) for a
    portfolio that receives external injections: a year's growth is
    judged against starting equity PLUS the injected money weighted by
    how long it was in — a plain (end-start)/start would book the new
    money itself as 'return'. With no injections this reduces exactly
    to the simple yearly return."""
    by_year: dict[int, dict] = {}
    for w in curve:
        by_year[int(w["date"][:4])] = w
    rows, prev = [], curve[0]
    for y in sorted(by_year):
        w = by_year[y]
        d0 = dt.date.fromisoformat(prev["date"])
        d1 = dt.date.fromisoformat(w["date"])
        span = max((d1 - d0).days, 1)
        flows = [(d, a) for d, a in injections
                 if prev["date"] < d <= w["date"]]
        F = sum(a for _, a in flows)
        weighted = sum(a * (d1 - dt.date.fromisoformat(d)).days / span
                       for d, a in flows)
        base = prev["equity"] + weighted
        rows.append({"year": y, "through": w["date"],
                     "equity": w["equity"], "injected": F,
                     "ret_pct": (w["equity"] - prev["equity"] - F)
                     / base * 100 if base > 0 else 0.0})
        prev = w
    return rows


def _write_events_csv(path: Path, res: dict) -> None:
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "symbol", "event"])
        for d, sym, what in sorted(res["blotter"]):
            w.writerow([d, sym, what])


def write_report(runs: dict, fr, args, through: str, nifty: list,
                 archive: Path, n_syms: int) -> Path:
    tag = f"{args.screen_start}_to_{through}"
    report = OUT_DIR / f"DARVAS_BACKTEST_LONGRUN_{tag}.md"
    res, gross = runs["net"], runs["gross"]
    _write_events_csv(OUT_DIR / f"_longrun_events_{tag}.csv", res)

    curve = res["equity_curve"]
    start_d = curve[0]["date"]
    days = (dt.date.fromisoformat(through)
            - dt.date.fromisoformat(start_d)).days
    def irr_of(r):
        flows = ([(start_d, -args.capital)]
                 + [(dd, -a) for dd, a in r["injections"]]
                 + [(through, r["final_equity"])])
        return xirr(sorted(flows))

    irr = irr_of(res)
    gross_irr = irr_of(gross)
    accrued = fr.accrued()
    truly_net = res["final_equity"] - accrued["tax"]

    n0 = next((c for d0, c in nifty if d0 >= start_d), None)
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
              if "BUY ₹" in b[2] or "SELL ₹" in b[2]
              or "RAISE STOP" in b[2]
              or b[1] == "TAX" or b[2].startswith("TRIM")]

    runway_days = (dt.date.fromisoformat(args.screen_start)
                   - dt.date.fromisoformat(args.fetch_start)).days
    runway_note = ("" if runway_days >= 360 else
                   f" The earliest screens run on ~{runway_days // 30} "
                   f"months of history instead of a full year — every "
                   f"gate's own minimum (6 completed weeks, 120 baseline "
                   f"days) is still enforced.")

    A = [f"# The Darvas screen — {args.screen_start} → {through}", "",
         f"> **LONG-RUN BACKTEST.** One continuous price archive "
         f"({args.fetch_start} → {through}, {n_syms} symbols, in "
         f"`{archive.name}/`); every Friday screen sees only bars up to "
         f"its own Friday; the earnings gate reads only fiscal years "
         f"ended on or before the last 31 March at each screen date; "
         f"the conference-call read is excluded. The net run pays Angel "
         f"One charges on every order and settles capital-gains tax "
         f"every 1 April. "
         + (f"**The universe is POINT-IN-TIME with a ROLLING radar:** "
            f"membership is recomputed EVERY MONTH as the top symbols "
            f"by the TRAILING month's traded value from NSE's official "
            f"bhavcopies, with hysteresis (leave only past rank 900) — "
            f"casualties are IN while they traded, new listings enter "
            f"the month they earn their place; membership gates fresh "
            f"entries only (`_membership_long.csv`); split/bonus "
            f"adjustments are heuristic, all listed in "
            f"`_adjustments.csv`. "
            if (archive / "_membership_long.csv").exists() else "")
         + f"No slippage, stop exits at the stop price, fractional "
           f"shares.{runway_note}"
         + (f" Stored fiscal statements exist for "
            f"{args.stmt_coverage:.0f}% of this universe — a stock "
            f"without statements cannot be blocked by the earnings "
            f"gate."
            if getattr(args, "stmt_coverage", 100) < 90 else ""), "",
         "## The rules — the skill, kept simple", "",
         f"₹{args.capital:,.0f} starts the book, and **no qualified "
         f"signal is EVER starved**: entries are funded from the "
         f"portfolio's cash first, with fresh capital topping up any "
         f"shortfall (every top-up dated and logged — the yardstick "
         f"is the money-weighted IRR). There is **NO ceiling on the "
         f"number of positions**: ten is only the sizing denominator "
         f"— each fresh entry is one tenth of the book at entry. "
         f"**Stocks only:** ETFs and funds are excluded from the "
         f"universe outright ({getattr(args, 'etf_excluded', 0)} "
         f"instruments filtered from this archive). Every Friday "
         f"after the close, the full three-gate screen (weekly volume "
         f"≥1.5× the 12-week average WITH a rising price; last "
         f"month's volume ≥1.5× the year's norm; ≥3 boxes with the "
         f"last 3 midpoints rising) runs over the whole universe; "
         f"entries at the next trading day's open; falling earnings "
         f"power refused; a box whose stop sits more than 25% below "
         f"the price refused. Stops (box bottom − max(0.3×height, 5% "
         f"of bottom)) are checked daily and ratcheted up weekly. "
         f"**Two exits, never more:** the stop itself, and the "
         f"DEAD-MONEY rule — a stock that seals no higher box for six "
         f"months is sold at that Friday's close, freeing capital and "
         f"attention. A sold symbol returns only by passing the full "
         f"screen again. NO pyramiding — doubling was built, measured "
         f"and retired: the add-on structurally bought the newest box "
         f"top with the stop a whole box lower.", "",
         "## The headline — IRR, since capital is added when signals call",
         "",
         f"| | Money put in | Final value | IRR (money-weighted, "
         f"per year) |",
         f"|---|---:|---:|---:|",
         f"| **This system, NET of charges and capital-gains tax** | "
         f"{inr(args.capital + res['total_injected'])} "
         f"(₹{args.capital:,.0f} + {inr(res['total_injected'])} added "
         f"across {len(res['injections'])} top-ups) | "
         f"**{inr(res['final_equity'])}** | **{irr:+.2f}%** |",
         f"| Before charges and taxes | "
         f"{inr(args.capital + gross['total_injected'])} | "
         f"{inr(gross['final_equity'])} | {gross_irr:+.2f}% |"]
    if nifty_100:
        A.append(f"| Nifty 50 (same window, pre-cost, pre-tax) | "
                 f"₹100.00 | {inr(nifty_100)} | {nifty_cagr:+.2f}% |")
    A += ["",
          f"*{inr(accrued['tax'])} of tax has accrued on the final "
          f"part-year's realised gains (due next April) — settling it "
          f"today would leave {inr(truly_net)}; "
          f"unrealised gains in the end book carry a further deferred "
          f"liability. {days / 365.25:.2f} years, {len(curve)} weekly "
          f"screens.*", ""]

    A += ["## What the frictions took (net run)", "",
          f"- **Transaction charges: {inr(fr.total_costs)}** (Angel One "
          f"equity delivery: STT 0.10% both sides, exchange and SEBI "
          f"levies, 18% GST, stamp duty 0.015% on buys, delivery "
          f"brokerage ₹0 until 31 Oct 2024 then 0.1%).",
          f"- **Capital-gains tax paid: {inr(fr.total_tax)}** — 20% "
          f"short-term (≤365 days), 12.5% long-term, settled each "
          f"1 April with lawful set-off and loss carry-forward.", "",
          "| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | "
          "Tax paid | Losses c/f (ST / LT) |",
          "|---|---|---:|---:|---:|---:|"]
    for t in fr.tax_rows:
        A.append(f"| {t['fy']} | {t['paid_on']} | "
                 f"{inr(t['st_taxable'])} | {inr(t['lt_taxable'])} | "
                 f"{inr(t['tax'])} | {inr(t['cf_st'])} / "
                 f"{inr(t['cf_lt'])} |")
    A += [f"| Final part-year (accrued) | — | "
          f"{inr(accrued['st_taxable'])} | {inr(accrued['lt_taxable'])} "
          f"| {inr(accrued['tax'])} | {inr(accrued['cf_st'])} / "
          f"{inr(accrued['cf_lt'])} |", ""]

    gross_yearly = {r["year"]: r for r in dietz_yearly(
        gross["equity_curve"], gross["injections"])}
    A += ["## Calendar-year returns (Modified Dietz — money-weighted "
          "for the top-ups, so added capital is never booked as "
          "return)", "",
          "| Year (through) | Net equity | Added in year | Net return |"
          " Gross return |" + (" Nifty 50 |" if nifty else ""),
          "|---|---:|---:|---:|---:|" + ("---:|" if nifty else "")]
    prev_n = n0
    for r in dietz_yearly(curve, res["injections"]):
        g = gross_yearly.get(r["year"])
        line = (f"| {r['year']} ({r['through']}) | {inr(r['equity'])} | "
                f"{inr(r['injected'])} | "
                f"{r['ret_pct']:+.1f}% | "
                + (f"{g['ret_pct']:+.1f}% |" if g else "— |"))
        if nifty:
            n_now = nifty_by_date.get(r["through"]) or next(
                (c for d0, c in reversed(nifty) if d0 <= r["through"]),
                None)
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
          f"{dd['from']} → trough {dd['to']}, weekly closes).",
          (f"- **{len(closed)} closed trades**: {len(wins)} winners "
           f"({len(wins) / len(closed) * 100:.0f}%), average winner "
           f"{statistics.mean([c['ret_pct'] for c in wins]):+.1f}%, "
           f"average loser "
           f"{statistics.mean([c['ret_pct'] for c in closed if c['ret_pct'] <= 0]):+.1f}%."
           if closed and wins and len(wins) < len(closed) else
           f"- **{len(closed)} closed trades.**"),
          (f"- Best closed trade "
           f"{max(closed, key=lambda c: c['ret_pct'])['symbol']} "
           f"{max(c['ret_pct'] for c in closed):+.1f}%; worst "
           f"{min(closed, key=lambda c: c['ret_pct'])['symbol']} "
           f"{min(c['ret_pct'] for c in closed):+.1f}%."
           if closed else "- No closed trades."),
          (f"- Median holding period "
           f"{statistics.median(hold_days):.0f} days."
           if hold_days else ""),
          f"- Cash share of equity averaged "
          f"{statistics.mean(cash_share):.0f}% (median "
          f"{statistics.median(cash_share):.0f}%); fully in cash "
          f"{all_cash_weeks} of {len(curve)} weeks — when nothing "
          f"qualifies, the money waits.", ""]

    A += ["## Monthly equity curve (net run)", "",
          "| Month-end screen | Equity | Cash | Positions |",
          "|---|---:|---:|---:|"]
    last_in_month: dict[str, dict] = {}
    for w in curve:
        last_in_month[w["date"][:7]] = w
    for _, w in sorted(last_in_month.items()):
        A.append(f"| {w['date']} | {inr(w['equity'])} | "
                 f"{inr(w['cash'])} | {w['positions']} |")
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
          f"*Buys, sells and tax settlements; every stop raise, "
          f"starved signal and refused signal is in "
          f"`_longrun_events_{tag}.csv` ({len(res['blotter'])} events "
          f"in all).*", "", "```"]
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
    ap.add_argument("--screen-start", default=SCREEN_START,
                    help="first screen date (default: 2020-06-01)")
    ap.add_argument("--screen-end", default=None,
                    help="last screen date (default: the archive's end)")
    ap.add_argument("--fetch-start", default=FETCH_START.isoformat(),
                    help="archive start date (default: 2019-06-01)")
    ap.add_argument("--archive", default=None,
                    help="explicit archive directory (overrides the "
                         "date-derived path; implies no fetch)")
    args = ap.parse_args()

    fetch_start = dt.date.fromisoformat(args.fetch_start)
    end = (dt.date.fromisoformat(args.end) if args.end else dt.date.today())
    if args.archive:
        archive = Path(args.archive)
    else:
        archive = (BT.window_dir(fetch_start, end) if args.no_fetch
                   else ensure_archive(fetch_start, end))
    if args.no_fetch and not args.archive and _daily_file(archive) is None:
        cands = sorted((INDIA / "VolumeAndPricingBacktest").glob(
            f"{fetch_start}_to_*"))
        if not cands:
            sys.exit("no archive found and --no-fetch given")
        archive = cands[-1]
        print(f"archive reused: {archive}", file=sys.stderr)

    bars_by = load_bars(archive)
    print(f"{len(bars_by)} symbols loaded", file=sys.stderr)
    import pandas as pd
    pl_syms = set(pd.read_csv(EP.PL_LONG).nse_symbol.unique())
    args.stmt_coverage = (100 * len(set(bars_by) & pl_syms)
                          / max(len(bars_by), 1))
    dates = sorted({b["date"] for bars in bars_by.values() for b in bars})
    through = dates[-1]
    if args.screen_end:
        through = max(d for d in dates if d <= args.screen_end)
    print(f"screens {args.screen_start} → {through}", file=sys.stderr)

    import pit_universe as PIT
    etfs = {s for s in bars_by if PIT.is_etf(s)}
    bars_by = {s: b for s, b in bars_by.items() if s not in etfs}
    args.etf_excluded = len(etfs)
    print(f"{len(etfs)} ETF/fund instruments excluded — stocks only",
          file=sys.stderr)
    membership = load_membership(archive)
    if membership:
        membership = {m: {s for s in ss if s not in etfs}
                      for m, ss in membership.items()}
        print(f"rolling membership loaded: {len(membership)} months",
              file=sys.stderr)
    earnings_ok = make_earnings_ok()
    fr = FR.AngelOneFrictions()
    runs = {}
    for key, f in (("gross", None), ("net", fr)):
        print(f"{key} replay…", file=sys.stderr)
        runs[key] = RL.run_rolling(bars_by, [], args.screen_start, through,
                                   args.capital, earnings_ok, slots=SLOTS,
                                   frictions=f, membership=membership,
                                   funded=True)
        print(f"{key}: final ₹{runs[key]['final_equity']:,.2f}, "
              f"added ₹{runs[key]['total_injected']:,.2f}",
              file=sys.stderr)

    try:
        nifty = fetch_nifty(dt.date.fromisoformat(args.screen_start),
                            dt.date.fromisoformat(through))
    except Exception as e:                # noqa: BLE001 — benchmark only
        print(f"nifty fetch failed ({e}); report goes out without the "
              f"benchmark", file=sys.stderr)
        nifty = []

    report = write_report(runs, fr, args, through, nifty, archive,
                          len(bars_by))
    print(f"report: {report}")


if __name__ == "__main__":
    main()
