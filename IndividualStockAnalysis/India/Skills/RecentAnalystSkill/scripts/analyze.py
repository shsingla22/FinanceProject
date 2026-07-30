"""
analyze.py — run the RecentAnalystSkill (the AnalystSkill, last one year).

Modes (identical to the AnalystSkill):
  python3 analyze.py report SYMBOL out.md          full (AI judges + summary)
  python3 analyze.py report SYMBOL out.md --quick  numbers only, no AI
  python3 analyze.py company SYMBOL [--quick]      the combined record (JSON)
  python3 analyze.py batch SYM... --out-dir DIR [--quick]

The one-year window is applied by importing `window` (which loads the
AnalystSkill and restricts every data read); everything downstream is the
AnalystSkill unchanged. Judge model: ANALYST_MODEL (default claude-opus-5).
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import window as W          # noqa: E402  (applies the one-year lens)

AR, AC = W.AR, W.AC


def _ai_available() -> bool:
    return shutil.which("claude") is not None


def run_all(sym: str, ai: bool) -> dict:
    ba, s1 = AR.run_business(sym, ai=ai)
    mb, s2 = AR.run_patterns(sym, ai=ai)
    qr, s3 = AR.run_risks(sym, ai=ai)
    exts = AR.run_extensions(sym, ai=ai)
    rt = AC.compute_rating(ba, mb, qr, extensions=exts)
    return {"symbol": sym, "window": "last_one_year",
            "business": ba, "patterns": mb, "risks": qr,
            "extensions": exts, "rating": rt,
            "statuses": {"business": s1, "patterns": s2, "risks": s3}}


def compose_md(sym: str, out: dict, ai: bool) -> str:
    meta = AR.company_meta(sym)
    name = meta["name"]
    synth = overview = None
    if ai:
        print("Composing the business overview and analyst's summary "
              "(one-year lens)…", file=sys.stderr)
        overview = AC.business_overview(sym, name)
        synth = AC.synthesize(sym, name, out["business"], out["patterns"],
                              out["risks"], out["rating"],
                              extensions=out.get("extensions"))
        if synth is None:
            print("(summary could not be grounded — omitted honestly)",
                  file=sys.stderr)
    trends = AR.trend_series(sym)
    return AC.render(sym, name, out["business"], out["patterns"],
                     out["risks"], out["rating"], synth, out["statuses"],
                     extensions=out.get("extensions"), overview=overview,
                     trends=trends, industry=meta["industry"])


def cmd_company(args):
    ai = _ai_available() and not args.quick
    print(json.dumps(run_all(args.symbol, ai), indent=2, default=str))


def cmd_report(args):
    ai = _ai_available() and not args.quick
    if ai:
        print(f"Running all three skills over {args.symbol}'s LAST ONE YEAR "
              f"({AR.MODEL}, no timeout)…", file=sys.stderr)
    out = run_all(args.symbol, ai)
    md = compose_md(args.symbol, out, ai)
    Path(args.out).write_text(md)
    print(f"wrote {args.out} ({len(md.splitlines())} lines)")


def cmd_batch(args):
    ai = _ai_available() and not args.quick
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    done = failed = 0
    for sym in [s.upper() for s in args.symbols]:
        try:
            out = run_all(sym, ai)
            md = compose_md(sym, out, ai)
            (outdir / f"{sym}_last_year_analysis.md").write_text(md)
            done += 1
            print(f"[{done + failed}/{len(args.symbols)}] {sym}: "
                  f"{out['rating']['grade']} {out['rating']['score']}",
                  file=sys.stderr)
        except Exception as e:
            failed += 1
            print(f"[{done + failed}/{len(args.symbols)}] {sym}: "
                  f"FAILED {str(e)[:100]}", file=sys.stderr)
    print(f"wrote {done} reports to {outdir} ({failed} failed)")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("company")
    c.add_argument("symbol")
    c.add_argument("--quick", action="store_true")
    r = sub.add_parser("report")
    r.add_argument("symbol")
    r.add_argument("out")
    r.add_argument("--quick", action="store_true")
    b = sub.add_parser("batch")
    b.add_argument("symbols", nargs="+")
    b.add_argument("--out-dir", required=True)
    b.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    if hasattr(args, "symbol"):
        args.symbol = args.symbol.upper()
    {"company": cmd_company, "report": cmd_report,
     "batch": cmd_batch}[args.cmd](args)


if __name__ == "__main__":
    main()
