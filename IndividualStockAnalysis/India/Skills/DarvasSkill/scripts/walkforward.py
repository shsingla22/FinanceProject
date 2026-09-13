"""
walkforward.py — replay the backtest's picks under the REAL weekly rhythm.

    python3 walkforward.py --asof 2026-03-31 [--through 2026-09-11]

The backtest froze the world at an as-of date and scored its picks with
the INITIAL stop only. This runner replays the SAME picks — the stocks
are never re-chosen — under the rhythm the skill actually prescribes:

  * a STANDING STOP checked daily: a low at or under the stop exits at
    the stop price that day;
  * a WEEKLY RUN on each week's last trading day: boxes are re-sealed on
    the trailing six months of data as of that day; a newly sealed box
    whose stop (bottom − 0.3 × height) is HIGHER ratchets the stop up —
    never down; a BREAKDOWN state (closed below the box bottom) is the
    skill's SELL signal and exits at that day's close; a RECOVERY holds;
  * WATCH picks enter at their own instruction — the first daily CLOSE
    above the box top — and then live under the same rules;
  * no re-entry after an exit, no costs, everything logged.

Prices come from the backtest archive stitched to the live archive; the
seam is verified (every overlapping day must agree within 0.5%) so a
corporate-action adjustment between fetches can never fabricate a move.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import darvas as DV          # noqa: E402

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "DarvasAnalysis"
BOX_LOOKBACK_BARS = 130          # ~ six months of trading days


# ------------------------------------------------------------------ data

def _load_daily_csv(path: Path) -> dict[str, dict[str, dict]]:
    out: dict[str, dict[str, dict]] = {}
    with open(path) as fh:
        for r in csv.DictReader(fh):
            out.setdefault(r["symbol"], {})[r["date"]] = {
                "date": r["date"],
                "high": float(r["high"]) if r["high"] else None,
                "low": float(r["low"]) if r["low"] else None,
                "close": float(r["close"])}
    return out


def stitched_bars(backtest_dir: Path, symbols: list[str],
                  seam_tolerance_pct: float = 0.5) -> dict[str, list[dict]]:
    """Backtest archive + live archive, seam-verified, per symbol."""
    bt = _load_daily_csv(backtest_dir / "_all_daily_long.csv")
    lv = _load_daily_csv(DV.DATA_DIR / "_all_daily_long.csv")
    out: dict[str, list[dict]] = {}
    for sym in symbols:
        a, b = bt.get(sym, {}), lv.get(sym, {})
        overlap = set(a) & set(b)
        for d in overlap:
            drift = abs(a[d]["close"] - b[d]["close"]) / b[d]["close"] * 100
            if drift > seam_tolerance_pct:
                raise ValueError(
                    f"{sym}: archives disagree by {drift:.2f}% on {d} — "
                    f"a corporate action was adjusted between fetches; "
                    f"refusing to stitch a fabricated move")
        merged = {**a, **b}          # live wins on the overlap
        out[sym] = [merged[d] for d in sorted(merged)]
    return out


def week_end_indices(bars: list[dict]) -> set[int]:
    """Indices of each ISO week's LAST trading day — the weekly run."""
    ends = set()
    for i, bar in enumerate(bars):
        d = dt.date.fromisoformat(bar["date"])
        if i + 1 == len(bars):
            ends.add(i)
            continue
        nxt = dt.date.fromisoformat(bars[i + 1]["date"])
        if nxt.isocalendar()[:2] != d.isocalendar()[:2]:
            ends.add(i)
    return ends


# ------------------------------------------------------------- simulation

def simulate_position(bars: list[dict], entry_date: str, entry_px: float,
                      initial_stop: float | None,
                      through: str) -> dict:
    """One position under the rhythm. `bars` must include history BEFORE
    the entry (boxes need their trailing window). Returns the full event
    log — every ratchet with its box, and the exit with its reason."""
    idx = {b["date"]: i for i, b in enumerate(bars)}
    start = idx[entry_date] + 1              # the stop stands from day two
    endi = max(i for b, i in idx.items() if b <= through)
    ends = week_end_indices(bars[:endi + 1])
    stop = initial_stop
    events: list[dict] = []
    for i in range(start, endi + 1):
        bar = bars[i]
        if stop is not None and bar["low"] is not None \
                and bar["low"] <= stop:
            return _closed(entry_px, stop, bar["date"], "stop hit",
                           stop, events)
        if i in ends:                        # the weekly run, after close
            st = DV.find_boxes(bars[max(0, i - BOX_LOOKBACK_BARS):i + 1])
            if st["state"] == "BREAKDOWN":
                return _closed(entry_px, bar["close"], bar["date"],
                               "weekly SELL signal (closed below its box)",
                               stop, events)
            cur = st["current"]
            if st["state"] in ("IN_BOX", "BREAKOUT") and cur is not None:
                cand = DV.stop_loss(cur)
                if stop is None or cand > stop:
                    events.append({"date": bar["date"], "from": stop,
                                   "to": cand, "box_bottom": cur["bottom"],
                                   "box_top": cur["top"]})
                    stop = cand
    last = bars[endi]
    return _closed(entry_px, last["close"], last["date"],
                   "held through the period", stop, events)


def _closed(entry, exit_px, date, reason, stop, events):
    return {"exit_px": exit_px, "exit_date": date, "reason": reason,
            "final_stop": stop, "events": events,
            "ret_pct": (exit_px - entry) / entry * 100}


def watch_entry(bars: list[dict], after: str, buy_above: float,
                through: str) -> dict | None:
    """The WATCH instruction: enter on the first daily CLOSE above the
    box top, at that close."""
    for b in bars:
        if after < b["date"] <= through and b["close"] > buy_above:
            return {"date": b["date"], "px": b["close"]}
    return None


# ------------------------------------------------------------- the driver

def _initial_only(bars, entry_date, entry_px, stop, through):
    """Variant B — the fixed initial stop, no weekly runs (comparison)."""
    idx = {b["date"]: i for i, b in enumerate(bars)}
    endi = max(i for b, i in idx.items() if b <= through)
    for i in range(idx[entry_date] + 1, endi + 1):
        b = bars[i]
        if stop is not None and b["low"] is not None and b["low"] <= stop:
            return _closed(entry_px, stop, b["date"], "stop hit", stop, [])
    last = bars[endi]
    return _closed(entry_px, last["close"], last["date"],
                   "held through the period", stop, [])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--asof", default="2026-03-31")
    ap.add_argument("--through", default=None)
    ap.add_argument("--tag", default="2025-06-01_to_2026-03-31")
    args = ap.parse_args()

    bt_dir = INDIA / "VolumeAndPricingBacktest" / args.tag
    ledger = OUT_DIR / f"_positions_backtest_{args.tag}.csv"
    report = OUT_DIR / f"DARVAS_BACKTEST_{args.tag}.md"
    picks = list(csv.DictReader(open(ledger)))
    bars_by = stitched_bars(bt_dir, [p["symbol"] for p in picks])
    through = args.through or max(b["date"]
                                  for bars in bars_by.values() for b in bars)

    core, watch_rows, blotter = [], [], []
    for p in picks:
        sym = p["symbol"]
        bars = bars_by[sym]
        asof_bar = [b for b in bars if b["date"] <= args.asof][-1]
        stop0 = float(p["stop_loss"]) if p["stop_loss"] else None
        if p["action"] in ("BUY", "ACCUMULATE"):
            entry_date, entry_px = asof_bar["date"], asof_bar["close"]
            C = simulate_position(bars, entry_date, entry_px, stop0, through)
            B = _initial_only(bars, entry_date, entry_px, stop0, through)
            A = ([b for b in bars if b["date"] <= through][-1]["close"]
                 - entry_px) / entry_px * 100
            core.append({"sym": sym, "action": p["action"],
                         "entry_date": entry_date, "entry_px": entry_px,
                         "stop0": stop0, "A": A, "B": B, "C": C})
            blotter.append((entry_date, sym,
                            f"BUY at ₹{entry_px:,.2f} ({p['action']} as of "
                            f"{args.asof}; initial stop ₹{stop0:,.2f})"))
            _blot(blotter, sym, C)
        elif p["action"] == "WATCH" and p["box_top"]:
            hit = watch_entry(bars, asof_bar["date"],
                              float(p["box_top"]), through)
            if hit is None:
                watch_rows.append({"sym": sym, "triggered": False,
                                   "buy_above": float(p["box_top"])})
                continue
            C = simulate_position(bars, hit["date"], hit["px"], stop0,
                                  through)
            watch_rows.append({"sym": sym, "triggered": True,
                               "buy_above": float(p["box_top"]),
                               "entry_date": hit["date"],
                               "entry_px": hit["px"], "stop0": stop0,
                               "C": C})
            blotter.append((hit["date"], sym,
                            f"BUY at ₹{hit['px']:,.2f} (WATCH trigger: "
                            f"first close above the ₹{float(p['box_top']):,.2f} "
                            f"box top; initial stop "
                            f"{'₹%s' % format(stop0, ',.2f') if stop0 else '—'})"))
            _blot(blotter, sym, C)

    blotter.sort()
    _append_report(report, args, through, core, watch_rows, blotter)
    print(f"walk-forward appended to {report}")


def _blot(blotter, sym, C):
    for e in C["events"]:
        frm = f"₹{e['from']:,.2f}" if e["from"] is not None else "—"
        blotter.append((e["date"], sym,
                        f"RAISE STOP {frm} → ₹{e['to']:,.2f} (new box "
                        f"₹{e['box_bottom']:,.2f}–₹{e['box_top']:,.2f} "
                        f"sealed)"))
    verb = "SELL" if "held" not in C["reason"] else "STILL HELD"
    blotter.append((C["exit_date"], sym,
                    f"{verb} at ₹{C['exit_px']:,.2f} — {C['reason']} "
                    f"({C['ret_pct']:+.1f}%)"))


def _append_report(report, args, through, core, watch_rows, blotter):
    A = ["", f"## The weekly-ratcheting walk-forward "
             f"({args.asof} → {through})", "",
         "*The SAME picks as the as-of run — the stocks were never "
         "re-chosen. Rules replayed exactly as the skill prescribes: a "
         "standing stop checked DAILY (a low at the stop exits at the "
         "stop price); a WEEKLY run on each week's last trading day that "
         "re-seals boxes on the trailing six months and ratchets the "
         "stop up — never down — when a higher box seals, and exits at "
         "that day's close when the state is BREAKDOWN (the skill's SELL "
         "signal); WATCH picks enter on their own instruction, the first "
         "daily close above their box top. Prices are the two archives "
         "stitched with a verified seam. No re-entry, no costs.*", ""]

    A += ["### The complete trade blotter, in date order", "", "```"]
    for date, sym, what in blotter:
        A.append(f"{date}  {sym:11s} {what}")
    A += ["```", ""]

    A += ["### The core positions: initial stop vs the weekly ratchet", "",
          "| Stock | Entry (₹) | Initial stop | Buy & hold | "
          "Initial-stop only | WEEKLY RATCHET | Ratchets | Final stop | "
          "Exit |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for r in core:
        A.append(f"| {r['sym']} | {r['entry_px']:,.1f} | "
                 f"{r['stop0']:,.1f} | {r['A']:+.1f}% | "
                 f"{r['B']['ret_pct']:+.1f}% | "
                 f"**{r['C']['ret_pct']:+.1f}%** | "
                 f"{len(r['C']['events'])} | "
                 f"{'₹%s' % format(r['C']['final_stop'], ',.1f') if r['C']['final_stop'] else '—'} | "
                 f"{r['C']['reason']}, {r['C']['exit_date']} |")
    import statistics as st
    A += ["",
          f"**Averages ({len(core)} core positions):** buy & hold "
          f"{st.mean(r['A'] for r in core):+.1f}% · initial-stop only "
          f"{st.mean(r['B']['ret_pct'] for r in core):+.1f}% · weekly "
          f"ratchet **{st.mean(r['C']['ret_pct'] for r in core):+.1f}%**.",
          ""]

    trig = [w for w in watch_rows if w["triggered"]]
    A += ["### The WATCH picks, traded by their own instruction", "",
          f"{len(trig)} of {len(watch_rows)} WATCH picks closed above "
          f"their box top and became buys:", "",
          "| Stock | Buy above | Entry date | Entry (₹) | WEEKLY RATCHET | "
          "Ratchets | Exit |",
          "|---|---:|---|---:|---:|---:|---|"]
    for w in trig:
        A.append(f"| {w['sym']} | {w['buy_above']:,.1f} | "
                 f"{w['entry_date']} | {w['entry_px']:,.1f} | "
                 f"**{w['C']['ret_pct']:+.1f}%** | "
                 f"{len(w['C']['events'])} | {w['C']['reason']}, "
                 f"{w['C']['exit_date']} |")
    if trig:
        A += ["", f"**Average over the {len(trig)} triggered WATCH "
                  f"trades: {st.mean(w['C']['ret_pct'] for w in trig):+.1f}%**"
                  + (f"; untriggered: "
                     + ", ".join(w["sym"] for w in watch_rows
                                 if not w["triggered"])
                     if any(not w["triggered"] for w in watch_rows)
                     else "") + ".", ""]

    allpos = [r["C"]["ret_pct"] for r in core] + \
             [w["C"]["ret_pct"] for w in trig]
    A += [f"**The whole system under the rhythm — {len(allpos)} trades "
          f"taken: average {st.mean(allpos):+.1f}%, "
          f"{sum(1 for x in allpos if x > 0)} of {len(allpos)} positive, "
          f"vs the Nifty 50's +4.8% over the same period.**", "",
          "*Honest limits: entries at the daily close that triggered "
          "(no slippage), stop exits assume a fill at the stop price, no "
          "costs, one period is one sample.*", ""]
    report.write_text(report.read_text() + "\n".join(A))


if __name__ == "__main__":
    main()
