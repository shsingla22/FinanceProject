"""
rolling.py — the rhythm as an OPERATING PORTFOLIO: cash never sleeps.

    python3 rolling.py --asof 2026-05-31 --through 2026-09-11 \
                       --tag 2025-06-01_to_2026-05-31 [--capital 100]

The frozen walk-forward proved the picks but parked every rupee an exit
freed — 25% of all capital-time sat idle in the May replay. This runner
operates the skill the way its own step 5 prescribes the rhythm:

  * it starts with the SAME book as the frozen replay — the as-of
    ledger's BUY/ACCUMULATE picks, entered on the same day at the same
    price, equal slices of the starting capital — so the two runs
    differ in ONE thing only: what happens to freed cash;
  * EVERY FRIDAY (each week's last trading day, after the close) the
    FULL three-gate screen re-runs over the whole universe as of that
    day — weekly trigger, month-vs-year volume, rising ladder — plus
    the earnings-power check from the as-of statements (FALLING blocks
    the buy, exactly as the live skill downgrades it);
  * fresh buy signals (recommend() says BUY or ACCUMULATE through all
    three gates) are funded from CASH, best volume reaction first, each
    sized at one slice (equity ÷ the seed-book count) and capped by the
    cash on hand — no entry below half a slice, no borrowed money;
  * entries from a Friday screen execute at the NEXT trading day's OPEN
    — a decision made after the close cannot buy at that close;
  * positions live under the unchanged rules: a standing stop checked
    daily (a low at the stop exits at the stop price), weekly ratchets
    up only, the 5% stabilisation grace (only the stop itself exits),
    one position per symbol; a stopped symbol may return ONLY by
    passing the full screen again on a later Friday.

No lookahead anywhere: every screen sees only bars up to its own
Friday, statements are cut at the as-of fiscal year, and the
conference-call read is excluded exactly as in the parent backtest.
Every action lands in the dated blotter; the weekly equity curve and
the final accounting are appended to the window's backtest report.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import backtest as BT        # noqa: E402
import darvas as DV          # noqa: E402
import earnings as EP        # noqa: E402
import fetch_data as FD      # noqa: E402
import walkforward as WF     # noqa: E402

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "DarvasAnalysis"

MIN_DEPLOY_FRACTION = 0.5    # never open a position below half a slice
LOOKBACK = WF.BOX_LOOKBACK_BARS


# ------------------------------------------------------------------ data

def stitch_universe(backtest_dir: Path,
                    symbols: list[str]) -> tuple[dict, list[str]]:
    """Both archives loaded ONCE, then stitched per symbol with the same
    seam check as walkforward.stitched_bars — but a symbol whose seam
    disagrees is SKIPPED (and reported), not fatal: one adjusted
    corporate action must not abort a universe-wide replay."""
    bt = WF._load_daily_csv(backtest_dir / "_all_daily_long.csv")
    lv = WF._load_daily_csv(DV.DATA_DIR / "_all_daily_long.csv")
    out, refused = {}, []
    for sym in symbols:
        a, b = bt.get(sym, {}), lv.get(sym, {})
        if not a and not b:
            continue
        bad = False
        for d in set(a) & set(b):
            if abs(a[d]["close"] - b[d]["close"]) / b[d]["close"] * 100 > 0.5:
                bad = True
                break
        if bad:
            refused.append(sym)
            continue
        merged = {**a, **b}                  # live wins on the overlap
        out[sym] = [merged[d] for d in sorted(merged)]
    return out, refused


# ------------------------------------------------------------- screening

def screen_day(bars_upto: list[dict], day: dt.date) -> dict | None:
    """The full three-gate screen + recommend() for ONE symbol as of
    `day` (bars_upto must end on or before day, the day's close known).
    Returns the buy signal when every gate passes AND the action is BUY
    or ACCUMULATE — the skill's direct buy instructions. WATCH is not
    an entry; a genuine in-box WATCH becomes a BREAKOUT buy on a later
    Friday if the break comes on volume."""
    if len(bars_upto) < DV.MONTH_DAYS + DV.MIN_BASELINE_DAYS:
        return None
    weeks = FD.aggregate_weeks(bars_upto[-LOOKBACK:],
                               today=day + dt.timedelta(days=1))
    sig = DV.volume_signal(weeks)
    if not sig or not sig["qualifies"]:
        return None
    mv = DV.month_vs_year(bars_upto)
    if not mv or not mv["qualifies"]:
        return None
    st = DV.find_boxes(bars_upto[-LOOKBACK:])
    up = DV.box_uptrend(st["boxes"])
    if not up["qualifies"]:
        return None
    rec = DV.recommend(st, sig)
    if rec["action"] not in ("BUY", "ACCUMULATE") or "stop_loss" not in rec:
        return None
    return {"action": rec["action"], "stop": rec["stop_loss"],
            "volume_multiple": sig["volume_multiple"],
            "month_multiple": mv["month_vs_year_multiple"]}


def plan_deployment(cash: float, slice_size: float,
                    n_signals: int) -> list[float]:
    """How much cash goes to each of n_signals fresh entries, in signal
    order: one slice each while the cash lasts, the remainder only if it
    still clears MIN_DEPLOY_FRACTION of a slice. Never negative, never
    more than the cash."""
    amounts, left = [], cash
    for _ in range(n_signals):
        amt = min(slice_size, left)
        if amt < slice_size * MIN_DEPLOY_FRACTION or amt <= 0:
            break
        amounts.append(amt)
        left -= amt
    return amounts


# ------------------------------------------------------------ simulation

def run_rolling(bars_by: dict[str, list[dict]], seed: list[dict],
                start: str, through: str, capital: float,
                earnings_ok, screen=None) -> dict:
    """The portfolio day loop.

    seed rows: {"symbol", "stop"} — entered at `start`'s close, one
    equal slice of `capital` each (the frozen replay's exact book).
    earnings_ok(sym) -> bool blocks FALLING earnings power on NEW buys.
    `screen` defaults to screen_day (tests may inject one).
    Returns the blotter, the weekly equity curve and the final book."""
    probe = screen or screen_day
    all_dates = sorted({b["date"] for bars in bars_by.values()
                        for b in bars if start <= b["date"] <= through})
    idx_by = {sym: {b["date"]: i for i, b in enumerate(bars)}
              for sym, bars in bars_by.items()}
    week_ends = set()
    for i, d in enumerate(all_dates):
        if i + 1 == len(all_dates):
            week_ends.add(d)
        else:
            a = dt.date.fromisoformat(d).isocalendar()[:2]
            b = dt.date.fromisoformat(all_dates[i + 1]).isocalendar()[:2]
            if a != b:
                week_ends.add(d)

    slice_size = capital / len(seed)
    cash = capital
    positions: dict[str, dict] = {}
    pending: list[dict] = []
    blotter: list[tuple] = []
    equity_curve: list[dict] = []
    closed: list[dict] = []

    def bar_of(sym, d):
        i = idx_by[sym].get(d)
        return bars_by[sym][i] if i is not None else None

    def equity(d):
        total = cash
        for sym, p in positions.items():
            bar = bar_of(sym, d)
            px = bar["close"] if bar else p["last_px"]
            total += p["shares"] * px
        return total

    def open_position(sym, d, px, amt, stop, why):
        nonlocal cash
        cash -= amt
        positions[sym] = {"entry_date": d, "entry_px": px,
                          "shares": amt / px, "stop": stop,
                          "cost": amt, "last_px": px, "ratchets": 0}
        blotter.append((d, sym, f"BUY ₹{amt:,.2f} at ₹{px:,.2f} "
                                f"({why}; stop ₹{stop:,.2f})"))

    # ---- the seed book: same day, same prices as the frozen replay
    for row in seed:
        sym = row["symbol"]
        bar = bar_of(sym, start)
        if bar is None:
            continue
        open_position(sym, start, bar["close"], min(slice_size, cash),
                      row["stop"], "seed — the as-of book, one slice")

    for d in all_dates:
        # 1. pending Friday signals execute at TODAY'S OPEN
        still_pending = []
        for sig in pending:
            sym = sig["symbol"]
            bar = bar_of(sym, d)
            if bar is None:                  # symbol didn't trade today
                still_pending.append(sig)
                continue
            if sym in positions:
                continue
            eq = equity(d)
            cur_slice = slice_size * (eq / capital)
            plan = plan_deployment(cash, cur_slice, 1)
            if not plan:
                blotter.append((d, sym, "signal SKIPPED — cash below half "
                                        "a slice"))
                continue
            px = bar["open"] or bar["close"]
            open_position(sym, d, px, plan[0], sig["stop"],
                          f"fresh Friday signal — {sig['note']}")
        pending = still_pending

        # 2. the standing stop, checked daily
        for sym in list(positions):
            p = positions[sym]
            bar = bar_of(sym, d)
            if bar is None:
                continue
            p["last_px"] = bar["close"]
            if p["entry_date"] != d and bar["low"] is not None \
                    and bar["low"] <= p["stop"]:
                proceeds = p["shares"] * p["stop"]
                ret = (p["stop"] - p["entry_px"]) / p["entry_px"] * 100
                cash += proceeds
                closed.append({"symbol": sym, **p, "exit_date": d,
                               "exit_px": p["stop"], "proceeds": proceeds,
                               "ret_pct": ret})
                blotter.append((d, sym,
                                f"SELL ₹{proceeds:,.2f} at stop "
                                f"₹{p['stop']:,.2f} ({ret:+.1f}%) — the "
                                f"cash goes back to work at the next "
                                f"Friday screen"))
                del positions[sym]

        if d not in week_ends:
            continue

        # 3. the Friday run: ratchet held stops, then re-screen the world
        day = dt.date.fromisoformat(d)
        for sym, p in positions.items():
            i = idx_by[sym].get(d)
            if i is None:
                continue
            st = DV.find_boxes(bars_by[sym][max(0, i - LOOKBACK):i + 1])
            if st["state"] in ("IN_BOX", "BREAKOUT") and st["current"]:
                cand = DV.stop_loss(st["current"])
                if cand > p["stop"]:
                    blotter.append((d, sym,
                                    f"RAISE STOP ₹{p['stop']:,.2f} → "
                                    f"₹{cand:,.2f} (new box "
                                    f"₹{st['current']['bottom']:,.2f}–"
                                    f"₹{st['current']['top']:,.2f} sealed)"))
                    p["stop"] = cand
                    p["ratchets"] += 1

        eq = equity(d)
        cur_slice = slice_size * (eq / capital)
        signals = []
        if cash >= cur_slice * MIN_DEPLOY_FRACTION and d != through:
            for sym, bars in bars_by.items():
                if sym in positions:
                    continue
                i = idx_by[sym].get(d)
                if i is None:
                    continue
                hit = probe(bars[:i + 1], day)
                if hit is None:
                    continue
                if not earnings_ok(sym):
                    blotter.append((d, sym, "fresh signal REFUSED — "
                                            "falling earnings power"))
                    continue
                signals.append({
                    "symbol": sym, "stop": hit["stop"],
                    "mult": hit["volume_multiple"],
                    "note": f"{hit['action']}: {hit['volume_multiple']:.2f}× "
                            f"weekly, month {hit['month_multiple']:.2f}×, "
                            f"ladder rising"})
            signals.sort(key=lambda s: -s["mult"])
            n_fundable = len(plan_deployment(cash, cur_slice, len(signals)))
            pending = signals[:n_fundable]
            for s in signals[n_fundable:]:
                blotter.append((d, s["symbol"],
                                f"fresh signal NOT FUNDED — cash exhausted "
                                f"({s['note']})"))
        equity_curve.append({"date": d, "equity": round(eq, 2),
                             "cash": round(cash, 2),
                             "positions": len(positions),
                             "queued": len(pending)})

    last = all_dates[-1]
    book = []
    for sym, p in sorted(positions.items()):
        bar = bar_of(sym, last)
        px = bar["close"] if bar else p["last_px"]
        book.append({"symbol": sym, **p, "mark_px": px,
                     "value": p["shares"] * px,
                     "ret_pct": (px - p["entry_px"]) / p["entry_px"] * 100})
    return {"blotter": blotter, "equity_curve": equity_curve,
            "cash": cash, "book": book, "closed": closed,
            "final_equity": cash + sum(b["value"] for b in book)}


# ------------------------------------------------------------------ main

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--asof", default="2026-05-31")
    ap.add_argument("--through", default="2026-09-11")
    ap.add_argument("--tag", default="2025-06-01_to_2026-05-31")
    ap.add_argument("--capital", type=float, default=100.0)
    args = ap.parse_args()

    bt_dir = INDIA / "VolumeAndPricingBacktest" / args.tag
    syms = FD.universe_symbols()
    print(f"stitching {len(syms)} symbols…", file=sys.stderr)
    bars_by, refused = stitch_universe(bt_dir, syms)
    print(f"{len(bars_by)} stitched clean, {len(refused)} refused on the "
          f"seam: {', '.join(refused) or '—'}", file=sys.stderr)

    ledger = OUT_DIR / f"_positions_backtest_{args.tag}.csv"
    picks = list(csv.DictReader(open(ledger)))
    seed = [{"symbol": p["symbol"], "stop": float(p["stop_loss"])}
            for p in picks
            if p["action"] in ("BUY", "ACCUMULATE") and p["stop_loss"]
            and p["symbol"] in bars_by]
    seed_date = max(b["date"] for b in bars_by[seed[0]["symbol"]]
                    if b["date"] <= args.asof)
    print(f"seed book: {len(seed)} positions on {seed_date}",
          file=sys.stderr)

    # statements cut at the as-of fiscal year — no future annuals
    fy = BT.asof_fiscal_year(dt.date.fromisoformat(args.asof))
    import pandas as pd
    df = pd.read_csv(EP.PL_LONG)
    keep = [y for y in df.year.unique()
            if EP._year_key(y) <= EP._year_key(fy)]
    EP._PL_CACHE["df"] = df[df.year.isin(keep)]
    _memo: dict = {}

    def earnings_ok(sym: str) -> bool:
        if sym not in _memo:
            _memo[sym] = EP.earnings_power(sym)["verdict"] != "FALLING"
        return _memo[sym]

    res = run_rolling(bars_by, seed, seed_date, args.through,
                      args.capital, earnings_ok)
    _append_report(args, res, seed_date, len(seed))
    print(f"final equity: ₹{res['final_equity']:,.2f} "
          f"(cash ₹{res['cash']:,.2f} + {len(res['book'])} open positions)")


def _append_report(args, res, seed_date, n_seed) -> None:
    report = OUT_DIR / f"DARVAS_BACKTEST_{args.tag}.md"
    slice_rs = args.capital / n_seed
    A = ["", f"## The rolling rhythm — freed cash redeployed every Friday "
             f"({seed_date} → {args.through})", "",
         f"*Same starting book as the frozen replay above — the {n_seed} "
         f"as-of buys, entered {seed_date} at the same closes, "
         f"₹{slice_rs:.2f} each — but from then on the FULL three-gate "
         f"screen re-runs over the whole universe every Friday after the "
         f"close, and cash freed by a stop is deployed into that week's "
         f"fresh BUY/ACCUMULATE signals (best volume reaction first, one "
         f"slice per position, entries at the next day's open, falling "
         f"earnings power refused, nothing below half a slice). Stops "
         f"are checked daily and ratcheted weekly exactly as before; a "
         f"stopped symbol returns only by passing the full screen again. "
         f"The 25% idle-capital drag of the frozen replay is gone by "
         f"construction.*", ""]

    A += ["### The complete rolling blotter", "", "```"]
    for d, sym, what in sorted(res["blotter"]):
        A.append(f"{d}  {sym:11s} {what}")
    A += ["```", ""]

    A += ["### The weekly equity curve", "",
          "| Friday | Equity (₹) | Cash (₹) | Open positions | "
          "Fresh entries queued |", "|---|---:|---:|---:|---:|"]
    for w in res["equity_curve"]:
        A.append(f"| {w['date']} | {w['equity']:,.2f} | {w['cash']:,.2f} | "
                 f"{w['positions']} | {w['queued']} |")
    A.append("")

    if res["closed"]:
        A += ["### Closed trades", "",
              "| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |",
              "|---|---|---:|---|---:|---:|"]
        for c in res["closed"]:
            A.append(f"| {c['symbol']} | {c['entry_date']} | "
                     f"{c['entry_px']:,.2f} | {c['exit_date']} | "
                     f"{c['exit_px']:,.2f} | {c['ret_pct']:+.1f}% |")
        A.append("")

    if res["book"]:
        A += ["### Still held at the end", "",
              "| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |",
              "|---|---|---:|---:|---:|---:|"]
        for b in res["book"]:
            A.append(f"| {b['symbol']} | {b['entry_date']} | "
                     f"{b['entry_px']:,.2f} | {b['mark_px']:,.2f} | "
                     f"{b['stop']:,.2f} | {b['ret_pct']:+.1f}% |")
        A.append("")

    A += [f"**₹{args.capital:,.0f} became ₹{res['final_equity']:,.2f} "
          f"({res['final_equity'] / args.capital * 100 - 100:+.2f}%)** — "
          f"the frozen-picks replay of this same window made ₹113.34, "
          f"and the Nifty 50 ₹104.80.", "",
          "*Honest limits: next-open entries for fresh signals, seed "
          "entries at the as-of closes (matching the frozen replay), "
          "stop exits at the stop price, no costs or slippage, "
          "fractional shares, one period. The screen is the live "
          "skill's, unchanged — no parameter was tuned on this window; "
          "the conference-call read is excluded and statements are cut "
          "at the as-of fiscal year, as in the parent backtest.*", ""]
    report.write_text(report.read_text() + "\n".join(A))
    print(f"appended to {report}")


if __name__ == "__main__":
    main()
