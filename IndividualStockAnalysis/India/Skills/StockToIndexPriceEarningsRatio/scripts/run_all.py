"""
run_all.py — build the stock-vs-index reports for the whole universe.

For every company in the NiftyTotalMarket constituents file this writes
three files, next to that company's other stored analysis:

  {SYMBOL}_stock_to_index.md    the report (self-contained; text charts)
  {SYMBOL}_stock_to_index.svg   the same line graph as a vector chart
  {SYMBOL}_stock_to_index.mmd   the same line graph as Mermaid source

The skill reads only stored data, so this is pure computation — no AI
calls, no network. The whole universe takes about a minute.

RESUMABLE: a company whose three files already exist is skipped, so an
interrupted run continues where it stopped (--force rebuilds anyway).

Every outcome lands in _stock_to_index_log.csv: ok / skipped / no-chart
(the company has no plottable series) / failed, with the reason.

Usage (from this folder):
  python3 run_all.py                 build everything still missing
  python3 run_all.py --force         rebuild every company
  python3 run_all.py --limit 20      first 20 only (a smoke run)
"""

from __future__ import annotations

import argparse
import csv
import sys
import time
import traceback
from pathlib import Path

import analyze
import mermaidchart
import svgchart

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
CONST = INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"
# the reports live beside each company's other stored analysis
OUT = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "QualityAnalysis"

SERIES_LABELS = [("price", "Price ratio"), ("pat", "PAT ratio"),
                 ("op", "Operating-profit ratio")]


def universe() -> list[str]:
    with open(CONST) as f:
        return [r["nse_symbol"] for r in csv.DictReader(f)]


def _yoy(rows) -> dict[int, float]:
    return analyze.yoy_series(rows)


def build_one(sym: str, force: bool) -> tuple[str, str]:
    """Returns (status, note)."""
    md_p = OUT / f"{sym}_stock_to_index.md"
    svg_p = OUT / f"{sym}_stock_to_index.svg"
    mmd_p = OUT / f"{sym}_stock_to_index.mmd"
    if not force and md_p.exists() and svg_p.exists() and mmd_p.exists():
        return "skipped", "already built"

    md = analyze.build_report(sym)
    md_p.write_text(md)

    s = analyze._LAST_SERIES.get(sym, {})
    name = s.get("name", sym)
    series = [(label, _yoy(s.get(key, [])))
              for key, label in SERIES_LABELS]
    series = [(n, v) for n, v in series if v]
    if not series:
        # nothing to plot: say so rather than writing an empty chart
        for stale in (svg_p, mmd_p):
            if stale.exists():
                stale.unlink()
        return "no-chart", "no year-on-year series to plot"

    title = f"{name} ({sym}) vs Nifty 50 — yearly change in each ratio"
    svg = svgchart.render(
        series, title,
        subtitle="Above 0 the company gained on the index that year; "
                 "below 0 it lagged")
    if svg:
        svg_p.write_text(svg)
    mmd = mermaidchart.render(series, title)
    if mmd:
        mmd_p.write_text(mmd)
    made = ("svg" if svg else "") + ("+mmd" if mmd else "")
    return "ok", f"{len(series)} series, {made}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true",
                    help="rebuild even where the files already exist")
    ap.add_argument("--limit", type=int, default=0,
                    help="only the first N companies (smoke run)")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    syms = universe()
    if args.limit:
        syms = syms[:args.limit]

    log_path = OUT / "_stock_to_index_log.csv"
    rows, counts = [], {"ok": 0, "skipped": 0, "no-chart": 0, "failed": 0}
    t0 = time.time()
    for i, sym in enumerate(syms, 1):
        try:
            status, note = build_one(sym, args.force)
        except Exception as exc:                    # never abort the batch
            status, note = "failed", f"{type(exc).__name__}: {exc}"[:200]
            traceback.print_exc(limit=2)
        counts[status] += 1
        rows.append({"symbol": sym, "status": status, "note": note})
        if i % 50 == 0 or i == len(syms):
            print(f"[{i:4d}/{len(syms)}] {sym:<14s} {status:<9s} "
                  f"ok={counts['ok']} skip={counts['skipped']} "
                  f"nochart={counts['no-chart']} fail={counts['failed']} "
                  f"({time.time()-t0:.0f}s)", flush=True)

    with open(log_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["symbol", "status", "note"])
        w.writeheader()
        w.writerows(rows)

    print(f"\nDONE in {time.time()-t0:.0f}s — "
          f"{counts['ok']} built, {counts['skipped']} already present, "
          f"{counts['no-chart']} without a plottable series, "
          f"{counts['failed']} failed. Log: {log_path.name}")
    if counts["failed"]:
        print("Failed companies:")
        for r in rows:
            if r["status"] == "failed":
                print(f"  {r['symbol']}: {r['note']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
