"""
analyze.py — run the AnalystSkill.

Modes:
  python3 analyze.py report SYMBOL out.md          the coherent full report
                                                   (all three skills + AI
                                                   judges + synthesis)
  python3 analyze.py report SYMBOL out.md --quick  numbers only, no AI
  python3 analyze.py company SYMBOL [--quick]      the combined record (JSON)

The judge/synthesis model is ANALYST_MODEL (default claude-opus-5); it is
propagated to the sibling skills' judges so one variable steers everything.
First run of a company makes three deep concall reads plus one synthesis
call — several minutes; every step is cached (per transcript + model, and
the synthesis per record content).
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import registry as REG      # noqa: E402
import composer as C        # noqa: E402


def _ai_available() -> bool:
    return shutil.which("claude") is not None


def run_all(sym: str, ai: bool) -> dict:
    ba, s1 = REG.run_business(sym, ai=ai)
    mb, s2 = REG.run_patterns(sym, ai=ai)
    qr, s3 = REG.run_risks(sym, ai=ai)
    rt = C.compute_rating(ba, mb, qr)
    return {"symbol": sym, "business": ba, "patterns": mb, "risks": qr,
            "rating": rt,
            "statuses": {"business": s1, "patterns": s2, "risks": s3}}


def cmd_company(args):
    ai = _ai_available() and not args.quick
    out = run_all(args.symbol, ai)
    print(json.dumps(out, indent=2, default=str))


def cmd_report(args):
    ai = _ai_available() and not args.quick
    if ai:
        print(f"Running all three skills over {args.symbol} "
              f"({REG.MODEL}, no timeout — first run can take several "
              f"minutes)…", file=sys.stderr)
    out = run_all(args.symbol, ai)
    name = REG.company_name(args.symbol)
    synth = None
    if ai:
        print("Composing the analyst's summary…", file=sys.stderr)
        synth = C.synthesize(args.symbol, name, out["business"],
                             out["patterns"], out["risks"], out["rating"])
        if synth is None:
            print("(summary could not be grounded — omitted honestly)",
                  file=sys.stderr)
    md = C.render(args.symbol, name, out["business"], out["patterns"],
                  out["risks"], out["rating"], synth, out["statuses"])
    Path(args.out).write_text(md)
    print(f"wrote {args.out} ({len(md.splitlines())} lines)")


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
    args = ap.parse_args()
    args.symbol = args.symbol.upper()
    {"company": cmd_company, "report": cmd_report}[args.cmd](args)


if __name__ == "__main__":
    main()
