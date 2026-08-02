"""
analyze.py — run the ComparisonSkill: AnalystSkill vs RecentAnalystSkill.

Modes:
  python3 analyze.py report SYMBOL out.md          full (AI on both sides)
  python3 analyze.py report SYMBOL out.md --quick  numbers only, no AI
  python3 analyze.py company SYMBOL [--quick]      the comparison record (JSON)
  python3 analyze.py batch SYM... --out-dir DIR [--quick]

Each side runs through its own skill's CLI in a subprocess; AI judge
verdicts are served from each skill's cache, so a company already
analysed by both skills compares in seconds.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import compare_engine as CE     # noqa: E402


def _ai_available() -> bool:
    return shutil.which("claude") is not None


def _fmt(v, signed=False):
    if v is None:
        return "—"
    return f"{v:+d}" if signed else str(v)


def _company_name(sym: str) -> str:
    import pandas as pd
    const = pd.read_csv(CE.SKILLS.parent / "NiftyTotalMarket"
                        / "niftytotalmarket_constituents.csv")
    row = const[const.nse_symbol == sym]
    return str(row.iloc[0].company_name) if len(row) else sym


def render(sym: str, name: str, rec: dict) -> str:
    L: list[str] = []
    A = L.append
    A(f"# {name} ({sym}) — Then vs Now: The One-Year Comparison")
    A("")
    A("**What this compares:** the full-history AnalystSkill view (\"what "
      "has this business been over the long run?\") against the "
      "RecentAnalystSkill's one-year view (\"what does it look like RIGHT "
      "NOW?\") — same three analysis engines, same rules, different "
      "evidence windows. Only items assessed on BOTH views are compared; "
      "checks the one-year lens silences by design are listed separately "
      "and never counted as regressions.")
    A("")

    # ---- step 1: the overall rating
    rd = rec["rating"]
    head = {"improved": "IMPROVED in the last year 📈",
            "declined": "DECLINED in the last year 📉",
            "held steady": "HELD STEADY in the last year ➡️",
            "not comparable": "could not be compared"}[rd["direction"]]
    A(f"## Step 1 — The overall rating: {head}")
    A("")
    A(rd["derivation"])
    A("")
    if rd["delta"] is not None:
        A("| Pillar | Long view | Last one year | Change |")
        A("|---|---|---|---|")
        for p in rec["pillars"]:
            A(f"| {p['pillar']} | {_fmt(p['full'])} | {_fmt(p['recent'])} | "
              f"{_fmt(p['delta'], signed=True)} |")
        A("")
        A("*A pillar move can be partly lens-driven — the one-year view "
          "cannot test multi-year fingerprints (foundation gate, trend "
          "checks), which lowers its multibagger pillar mechanically. "
          "Step 2 separates genuine movement from window effects.*")
        A("")
        A("**How each side built its number:**")
        A("")
        for p in rec["pillars"]:
            A(f"- **{p['pillar']}, long view:** {p['full_why']}")
            A(f"- **{p['pillar']}, last one year:** {p['recent_why']}")
        A("")

    # ---- the raw numbers behind both views
    if rec.get("numbers"):
        A("## The numbers behind the comparison")
        A("")
        A("*The same yearly figures both analyses judged, from the "
          "comparison viewpoint: what the business has averaged over the "
          "long run, the year the one-year window uses as its baseline, "
          "the latest year, and the change between the two.*")
        A("")
        A("| Measure | Long-view average | Year before last | Latest year "
          "| Change |")
        A("|---|---|---|---|---|")
        for n in rec["numbers"]:
            A(f"| {n['measure']} | {n['long_avg']} *(avg of "
              f"{n['n_years']} years)* | {n['prior']} | {n['latest']} | "
              f"{n['change']} |")
        A("")

    # ---- step 2: the three buckets
    A("## Step 2 — Where it improved and where it regressed")
    A("")

    # bucket 1: business quality
    b = rec["business"]
    A("### Bucket 1 — Business quality (34-check framework)")
    A("")
    A(b["overall"])
    A("")
    A("| Area | Long view | Last one year | Change |")
    A("|---|---|---|---|")
    for a in b["areas"]:
        A(f"| {a['area']} | {a['full_word']}"
          + (f" ({a['full']:+.2f})" if a["full"] is not None else "")
          + f" | {a['recent_word']}"
          + (f" ({a['recent']:+.2f})" if a["recent"] is not None else "")
          + " | "
          + ("—" if a["delta"] is None else f"{a['delta']:+.2f}") + " |")
    A("")
    if b["improved"]:
        A("**Checks that improved:**")
        A("")
        for c in b["improved"]:
            A(f"- **{c['check']}** ({c['area']}): {c['full_word']} → "
              f"{c['recent_word']}. {c['explanation']}")
        A("")
    if b["regressed"]:
        A("**Checks that regressed:**")
        A("")
        for c in b["regressed"]:
            A(f"- **{c['check']}** ({c['area']}): {c['full_word']} → "
              f"{c['recent_word']}. {c['explanation']}")
        A("")
    if b["unchanged"]:
        A("*Unchanged: " + "; ".join(c["check"] for c in b["unchanged"])
          + ".*")
        A("")
    if b.get("carried"):
        A("*Carried forward from the long view unchanged (the window could "
          "not re-test these — identical by construction): "
          + "; ".join(f"{c['check']} ({c['word']})"
                      for c in b["carried"]) + ".*")
        A("")
    if b["window_excluded"]:
        A("*Needs longer history than the one-year lens allows (not "
          "counted as regressions): "
          + "; ".join(f"{c['check']} (long view: {c['full_word']})"
                      for c in b["window_excluded"]) + ".*")
        A("")
    if b["newly_visible"]:
        A("**Newly assessable in the recent view:**")
        A("")
        for c in b["newly_visible"]:
            A(f"- **{c['check']}** — {c['recent_word']}: {c['explanation']}")
        A("")

    # buckets 2 and 3 share a shape
    for title, key, verb in (
            ("Bucket 2 — Multibagger patterns (11 patterns)", "patterns",
             ("strengthened", "weakened")),
            ("Bucket 3 — Risks (8 channels)", "risks",
             ("eased", "worsened"))):
        t = rec[key]
        A(f"### {title}")
        A("")
        A(t["overall"])
        A("")
        if key == "patterns":
            A(f"*Foundation test: {t['gate_full']} on the long view, "
              f"{t['gate_recent']} on the one-year view.*")
            A("")
        for label, items in ((f"That {verb[0]}", t["improved"]),
                             (f"That {verb[1]}", t["regressed"])):
            if items:
                A(f"**{label}:**")
                A("")
                for i in items:
                    A(f"- **{i['name']}**: {i['from']} → {i['to']}. "
                      f"Why now: {i['now'] or i['why_now']}"
                      + (f" (The long view had said: {i['then']})"
                         if i.get("then") and i["then"] != i["now"] else ""))
                A("")
        if t.get("carried"):
            A("*Carried forward from the long view unchanged (the window "
              "could not re-test these): "
              + "; ".join(f"{c['name']} ({c['verdict']})"
                          for c in t["carried"]) + ".*")
            A("")
        if t["unchanged"]:
            A("*Unchanged: "
              + "; ".join(f"{i['name']} ({i['from']})"
                          for i in t["unchanged"]) + ".*")
            A("")
        if t["not_comparable"]:
            A("*Not comparable: "
              + "; ".join(f"{i['name']} ({i['from']} → {i['to']} — "
                          f"{i.get('note', '')})"
                          for i in t["not_comparable"]) + ".*")
            A("")
        if key == "risks":
            fr = t["fragility"]
            A(f"**Financial resilience:** {fr['full'].title()} on the long "
              f"view ({fr['full_why']}) vs {fr['recent'].title()} on the "
              f"one-year view ({fr['recent_why']})")
            A("")

    # ---- methodology
    A("## How this comparison was built")
    A("")
    st = rec["statuses"]
    A("Both sides ran the same three analysis engines (BusinessAnalysis, "
      "MultibaggerPattern, QualityRisks) through their respective "
      "orchestrators:")
    A("")
    A(f"- **Long view (full AnalystSkill):** statements over ~a decade, the "
      f"whole call timeline — engines ran "
      f"{', '.join(sorted(set(st['full'].values())))}.")
    A(f"- **Last one year (RecentAnalystSkill):** latest fiscal year (prior "
      f"year as baseline only), last 12 months of calls — engines ran "
      f"{', '.join(sorted(set(st['recent'].values())))}.")
    A("")
    A("Comparison rules: only verdicts assessed on both views are counted; "
      "one-year-lens silences are listed but never scored as regressions; "
      "every movement line carries both sides' evidence so the WHY of the "
      "change is visible, not just the direction. Research tooling; not "
      "investment advice.")
    return "\n".join(L)


def run(sym: str, ai: bool) -> dict:
    full = CE.run_analysis(sym, "full", ai=ai)
    recent = CE.run_analysis(sym, "recent", ai=ai)
    return CE.compare(sym, full, recent)


def cmd_company(args):
    ai = _ai_available() and not args.quick
    print(json.dumps(run(args.symbol, ai), indent=2, default=str))


def cmd_report(args):
    ai = _ai_available() and not args.quick
    if ai:
        print(f"Running BOTH views of {args.symbol} (cached judges are "
              f"reused; first-ever runs take several minutes per side)…",
              file=sys.stderr)
    rec = run(args.symbol, ai)
    md = render(args.symbol, _company_name(args.symbol), rec)
    Path(args.out).write_text(md)
    print(f"wrote {args.out} ({len(md.splitlines())} lines)")


def cmd_batch(args):
    ai = _ai_available() and not args.quick
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    done = failed = 0
    for sym in [s.upper() for s in args.symbols]:
        try:
            rec = run(sym, ai)
            md = render(sym, _company_name(sym), rec)
            (outdir / f"{sym}_comparison.md").write_text(md)
            done += 1
            print(f"[{done + failed}/{len(args.symbols)}] {sym}: "
                  f"{rec['rating']['direction']}", file=sys.stderr)
        except Exception as e:
            failed += 1
            print(f"[{done + failed}/{len(args.symbols)}] {sym}: FAILED "
                  f"{str(e)[:100]}", file=sys.stderr)
    print(f"wrote {done} comparisons to {outdir} ({failed} failed)")


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
