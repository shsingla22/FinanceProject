"""
analyze_batch.py — batch quality analysis over NiftyTotalMarket companies.

For each company in a batch (default: 100 at a time, in constituents-file
order) this runs the full skill family and stores TWO reports here:

  {SYMBOL}_analysis.md     the AnalystSkill's complete company analysis
                           (BusinessAnalysis + MultibaggerPattern +
                           QualityRisks, orchestrated, with the combined
                           rating and full explainability)
  {SYMBOL}_comparison.md   the ComparisonSkill's then-vs-now report — the
                           long view vs the RecentAnalystSkill's one-year
                           view, movement called out verdict-by-verdict

The one-year (RecentAnalystSkill) view is computed as the comparison's
recent side, so all three skills run for every company.

Usage (from this folder):
  python3 analyze_batch.py run                    first 100 companies
  python3 analyze_batch.py run --start 100        companies 101–200
  python3 analyze_batch.py run --count 25         smaller batch
  python3 analyze_batch.py run --symbols A,B,C    explicit list
  python3 analyze_batch.py run --quick            numbers-only (no AI)
  python3 analyze_batch.py validate               test every stored MD

Design points:
  - RESUMABLE: a company whose two MD files already exist is skipped, so
    an interrupted batch continues where it stopped (delete a company's
    files to force a re-run).
  - Each skill runs through its own CLI in a subprocess (the one-year
    skill windows its engines in-process, so sides must never share an
    interpreter). AI judge verdicts are cached on disk by the skills —
    the AnalystSkill run warms the caches the comparison's full side
    then reuses.
  - RETRIES: transient failures (Claude CLI usage limits, network) are
    retried with exponential backoff before a company is marked failed.
  - Every outcome lands in _batch_log.csv (status, seconds, attempts).
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent          # .../IndividualStockAnalysis/India
SKILLS = INDIA / "Skills"
CONST = INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"

RETRIES = 3                                # attempts per skill run
BACKOFF = 60                               # s; doubles per retry


def universe() -> list[str]:
    with open(CONST) as f:
        return [row["nse_symbol"] for row in csv.DictReader(f)]


def run_skill(skill: str, sym: str, out_md: Path, quick: bool) -> tuple[bool, str]:
    """One skill's `report` CLI with retries. Returns (ok, note)."""
    cmd = [sys.executable, str(SKILLS / skill / "scripts" / "analyze.py"),
           "report", sym, str(out_md)]
    if quick:
        cmd.append("--quick")
    last = ""
    for attempt in range(1, RETRIES + 1):
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              timeout=None)
        if proc.returncode == 0 and out_md.exists():
            return True, f"attempt {attempt}"
        last = (proc.stderr or proc.stdout or "")[-300:].replace("\n", " ")
        if attempt < RETRIES:
            wait = BACKOFF * (2 ** (attempt - 1))
            print(f"      {skill} attempt {attempt} failed — retrying in "
                  f"{wait}s: {last[:120]}", flush=True)
            time.sleep(wait)
    return False, last


def process(sym: str, quick: bool) -> dict:
    """Both reports for one company; the AnalystSkill runs first so its
    judge caches are warm when the comparison's full side re-runs it."""
    t0 = time.time()
    a_md = HERE / f"{sym}_analysis.md"
    c_md = HERE / f"{sym}_comparison.md"
    if a_md.exists() and c_md.exists():
        return {"symbol": sym, "status": "skip:already_done", "seconds": 0}
    ok_a, note_a = run_skill("AnalystSkill", sym, a_md, quick)
    if not ok_a:
        return {"symbol": sym, "status": f"fail:analysis:{note_a[:160]}",
                "seconds": round(time.time() - t0, 1)}
    ok_c, note_c = run_skill("ComparisonSkill", sym, c_md, quick)
    if not ok_c:
        return {"symbol": sym, "status": f"fail:comparison:{note_c[:160]}",
                "seconds": round(time.time() - t0, 1)}
    return {"symbol": sym, "status": "ok", "seconds": round(time.time() - t0, 1)}


def cmd_run(args) -> None:
    if args.symbols:
        syms = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    else:
        syms = universe()[args.start:args.start + args.count]
    mode = "QUICK (numbers only)" if args.quick else "FULL (Opus judges)"
    print(f"Batch of {len(syms)} companies "
          f"({syms[0]}…{syms[-1]}) — {mode}", flush=True)
    log_path = HERE / "_batch_log.csv"
    rows, done, failed = [], 0, 0
    t0 = time.time()
    for i, sym in enumerate(syms, 1):
        # user-requested pause: stop cleanly between companies
        if (HERE / "_paused").exists():
            print(f"PAUSED after {i - 1} companies — _paused flag present, "
                  "stopping (remove the flag to resume)", flush=True)
            break
        r = process(sym, args.quick)
        rows.append(r)
        done += r["status"].startswith(("ok", "skip"))
        failed += r["status"].startswith("fail")
        el = (time.time() - t0) / 60
        print(f"[{i:3d}/{len(syms)}] {sym:<14s} {r['status'][:60]:<60s} "
              f"{r['seconds']:7.1f}s  total {el:6.1f} min", flush=True)
        with open(log_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["symbol", "status", "seconds"])
            w.writeheader()
            w.writerows(rows)
    print(f"\nDONE: {done} ok/skipped, {failed} failed, "
          f"{(time.time() - t0) / 60:.1f} min. Log: {log_path}", flush=True)
    if failed:
        print("Failed companies (re-run the same command — completed ones "
              "are skipped):", flush=True)
        for r in rows:
            if r["status"].startswith("fail"):
                print(f"  {r['symbol']}: {r['status']}", flush=True)


def cmd_validate(args) -> None:
    import validate_reports as V
    problems = V.validate_all(HERE)
    if problems:
        print(f"{len(problems)} problems:")
        for p in problems[:40]:
            print("  ", *p)
        sys.exit(1)
    print("all stored reports validated clean")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--start", type=int, default=0,
                   help="0-based index into the constituents file")
    r.add_argument("--count", type=int, default=100,
                   help="companies per batch (default 100)")
    r.add_argument("--symbols", default=None,
                   help="explicit comma-separated symbols instead")
    r.add_argument("--quick", action="store_true",
                   help="numbers-only, no AI judges")
    v = sub.add_parser("validate")
    args = ap.parse_args()
    {"run": cmd_run, "validate": cmd_validate}[args.cmd](args)


if __name__ == "__main__":
    main()
