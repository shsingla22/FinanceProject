"""
add_relative_index.py — fold the index comparison into the stored reports.

The AnalystSkill now weighs a fourth input: how the company has done
AGAINST the Nifty 50 (relative_index.py). Re-running the whole analysis
would mean thousands of fresh judge calls for verdicts that have not
changed, so this script edits the reports that already exist:

  {SYM}_analysis.md    the long view — rescored with the index pillar at
                       10%, plus a new section carrying the charts and
                       the 10 / 5 / 3 / 1-year verdicts
  {SYM}_comparison.md  the then-vs-now view — the index pillar added to
                       the pillar table (long run vs the latest year) and
                       a matching bucket in Step 2

Nothing else in either file is touched: every existing verdict, chart,
quote and derivation is preserved exactly.

Weighting. The three original pillars keep their relative proportions
and are scaled to 90%, so the new pillar takes 10%:

    business quality  45% → 40.5%
    multibagger fit   30% → 27%
    risk safety       25% → 22.5%
    relative to index        10%

A company the index comparison cannot reach (too little stored history)
keeps its original three-pillar score, and the report says so rather
than inventing a fourth number.

IDEMPOTENT: running twice produces the same file as running once — the
script recognises its own output, strips it, and rebuilds from the
untouched original values.

Usage (from this folder):
  python3 add_relative_index.py                 every company
  python3 add_relative_index.py --limit 5       a smoke run
  python3 add_relative_index.py --symbols A,B   named companies
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import time
import traceback
from pathlib import Path

import importlib.util

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent   # .../IndividualStockAnalysis/India
CONST = INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"
OUT = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "QualityAnalysis"


def _load_pillar_module():
    """The pillar logic lives with the data, in the ratio skill."""
    scripts = (HERE.parent.parent / "StockToIndexPriceEarningsRatio"
               / "scripts")
    if str(scripts) not in sys.path:
        sys.path.append(str(scripts))
    spec = importlib.util.spec_from_file_location(
        "stock_to_index_pillar", scripts / "index_pillar.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["stock_to_index_pillar"] = mod
    spec.loader.exec_module(mod)
    return mod


REL = _load_pillar_module()

# the three original pillars, scaled to 90% so the index pillar takes 10%
W_QUALITY, W_PATTERNS, W_SAFETY, W_RELATIVE = 0.405, 0.27, 0.225, 0.10
GRADE_BANDS = [(80, "Outstanding", 5), (65, "Strong", 4), (50, "Decent", 3),
               (35, "Mixed", 2), (0, "Weak", 1)]

SECTION_HEAD = "## Section 4 — How has it done against the index?"
BUCKET_HEAD = "### Bucket 4 — Against the index (price and earnings vs the Nifty 50)"

# The arithmetic line lists ONE term per pillar that could be scored, so
# a company whose multibagger pillar was unscorable shows two terms at
# re-normalised weights (64%/36%), not three. Parse the terms generically
# and rebuild the same way composer.compute_rating does.
ARITH_LINE_RE = re.compile(
    r"\*\*The exact arithmetic:\*\* Overall = (?P<terms>[^=]+?) = "
    r"(?P<total>\d+) out of 100 → (?P<grade>[^(]+) \((?P<stars>\d+) stars?\)\.")
TERM_RE = re.compile(r"([\d.]+)% × (\d+) \(([a-z ]+?)\)")
BASE_WEIGHTS = {"business quality": 0.405, "multibagger fit": 0.27,
                "risk safety": 0.225, "relative to the index": 0.10}
# kept for the three-pillar case the tests pin down
ARITH_RE = re.compile(
    r"\*\*The exact arithmetic:\*\* Overall = [\d.]+% × (?P<bq>\d+) "
    r"\(business quality\) \+ [\d.]+% × (?P<mb>\d+) \(multibagger fit\) "
    r"\+ [\d.]+% × (?P<rs>\d+) \(risk safety\)"
    r"(?: \+ [\d.]+% × \d+ \(relative to the index\))?"
    r" = (?P<total>\d+) out of 100 → (?P<grade>[^(]+) \((?P<stars>\d+) stars?\)\.")


def _pct(w: float) -> str:
    """0.405 -> "40.5%", 0.27 -> "27%" — matches composer._pct."""
    return f"{f'{w * 100:.1f}'.rstrip('0').rstrip('.')}%"


def rebuild_arithmetic(line_match, rel_points):
    """Recompute the overall from the terms shown, with the index pillar
    folded in at 10% and every weight re-normalised over what is
    actually scored — exactly what composer.compute_rating does."""
    pts = {name: int(v) for _w, v, name in TERM_RE.findall(line_match["terms"])}
    if not pts:
        return None
    if rel_points is not None:
        pts["relative to the index"] = rel_points
    order = ["business quality", "multibagger fit", "risk safety",
             "relative to the index"]
    present = [n for n in order if n in pts]
    wsum = sum(BASE_WEIGHTS[n] for n in present)
    score = round(sum(pts[n] * BASE_WEIGHTS[n] for n in present) / wsum)
    terms = " + ".join(f"{_pct(BASE_WEIGHTS[n] / wsum)} × {pts[n]} ({n})"
                       for n in present)
    grade, stars = grade_of(score)
    return {"score": score, "grade": grade, "stars": stars,
            "line": (f"**The exact arithmetic:** Overall = {terms} = {score} "
                     f"out of 100 → {grade} "
                     f"({stars} star{'s' if stars > 1 else ''})."),
            "rel": pts.get("relative to the index")}
VERDICT_RE = re.compile(
    r"^## The verdict: (?P<grade>.+?) — (?P<score>\d+) out of 100 "
    r"(?P<stars>[★☆]+)[ \t]*$", re.M)   # never eat the blank line after
BREATH_RE = re.compile(
    r"(?:Against the Nifty 50 [^.]*\.\s*)?Weighing those together gives "
    r"\d+ out of 100 — [\w ]+\.")


def grade_of(score: float) -> tuple[str, int]:
    for cut, word, stars in GRADE_BANDS:
        if score >= cut:
            return word, stars
    return "Weak", 1


def universe() -> list[str]:
    with open(CONST) as f:
        return [r["nse_symbol"] for r in csv.DictReader(f)]


# --------------------------------------------------------------- section

def _chart_block(sym: str, p: dict) -> str:
    """The line graph of the three ratios, drawn by the ratio skill."""
    sys.path.append(str(REL.RATIO_SCRIPTS))
    import linechart                                   # noqa: E402
    series = [(label, REL.RATIO.yoy_series(REL.series_for(sym)[key]))
              for key, label in REL.MEASURES]
    series = [(n, s, i) for i, (n, s) in enumerate(series) if s]
    if not series:
        return ""
    return linechart.render(
        series, "Yearly change of each ratio against the Nifty 50 (%)")


def build_section(sym: str, p: dict) -> str:
    """Section 4 of the long report."""
    out = [SECTION_HEAD + " (price and earnings vs the Nifty 50)", ""]
    if p["points"] is None:
        out += [f"**Verdict: {p['verdict']}.**", "", p["derivation"], ""]
        return "\n".join(out)

    out += [f"**Verdict: the company has {p['verdict']} — "
            f"{p['points']} out of 100.**", "",
            "The other three sections judge the business on its own terms. "
            "This one asks a different question: measured against the Nifty "
            "50, has the company been pulling ahead or falling behind? Each "
            "ratio below is the company divided by the index, so a rise "
            "means the company outgrew the index and a fall means it "
            "lagged.", "",
            p["derivation"], "",
            "### The verdict over each window", "",
            REL.window_table(p), ""]
    chart = _chart_block(sym, p)
    if chart:
        out += ["### How the three ratios moved, year by year", "", chart, ""]
    out += [f"The full index comparison for this company — including the "
            f"level of each ratio year by year and the raw numbers behind "
            f"it — is in [`{sym}_stock_to_index.md`]({sym}_stock_to_index.md), "
            f"with the same graph as "
            f"[`{sym}_stock_to_index.svg`]({sym}_stock_to_index.svg) and "
            f"[`{sym}_stock_to_index.mmd`]({sym}_stock_to_index.mmd).", ""]
    return "\n".join(out)


# ------------------------------------------------------- analysis report

def _strip_previous(md: str, head: str, next_heads: tuple[str, ...]) -> str:
    """Remove a section this script added before, so it can be rebuilt."""
    if head not in md:
        return md
    start = md.index(head)
    ends = [md.index(h, start) for h in next_heads if h in md[start:]]
    end = min(ends) if ends else len(md)
    return md[:start] + md[end:]


def update_analysis(sym: str, p: dict) -> tuple[bool, str]:
    path = OUT / f"{sym}_analysis.md"
    if not path.exists():
        return False, "no analysis report"
    md = path.read_text()
    original = md

    md = _strip_previous(md, SECTION_HEAD,
                         ("## What to watch", "## How this report was built"))

    m = ARITH_LINE_RE.search(md)
    rescored = "not rated — kept as is"
    rebuilt = rebuild_arithmetic(m, p["points"]) if m else None
    if m and rebuilt and p["points"] is not None:
        total, grade, stars = (rebuilt["score"], rebuilt["grade"],
                               rebuilt["stars"])
        rel = p["points"]
        md = md.replace(m.group(0), rebuilt["line"])
        vm = VERDICT_RE.search(md)
        if vm:
            md = md.replace(
                vm.group(0),
                f"## The verdict: {grade} — {total} out of 100 "
                f"{'★' * stars}{'☆' * (5 - stars)}")
        md = BREATH_RE.sub(
            f"Against the Nifty 50 it has {p['verdict'].lower()} "
            f"({rel}/100). Weighing those together gives {total} out of 100 "
            f"— {grade.lower()}.", md, count=1)
        # the pillar bullet list gains a fourth entry
        md = re.sub(r"\n- \*\*Relative to the index \([^)]*\):\*\*[^\n]*", "", md)
        bullet = (f"\n- **Relative to the index ({rel}/100):** "
                  f"{p['derivation']}")
        rs_bullet = re.search(r"\n- \*\*Risk safety \([^\n]*", md)
        if rs_bullet:
            md = md[:rs_bullet.end()] + bullet + md[rs_bullet.end():]
        rescored = f"{m['total']} → {total}"
    elif p["points"] is not None:
        rescored = "arithmetic line not found — score left alone"

    # insert the new section before "What to watch"
    section = build_section(sym, p) + "\n"
    for anchor in ("## What to watch", "## How this report was built"):
        if anchor in md:
            md = md.replace(anchor, section + anchor, 1)
            break
    else:
        md = md.rstrip() + "\n\n" + section

    # the closing provenance list gains the fourth skill (strip any copy
    # left by an earlier run first, so re-running never stacks them up)
    md = re.sub(r"\n- \*\*StockToIndexPriceEarningsRatio\*\*[^\n]*", "", md)
    # the QualityRisks bullet reads "(with_calls)" or "(no_concalls)"
    # depending on what evidence that company had, so match either
    md = re.sub(
        r"(- \*\*QualityRisks\*\* \([a-z_]+\): the 8 channels through "
        r"which quality companies fail\.)",
        r"\1\n- **StockToIndexPriceEarningsRatio** (stored data): price, "
        r"profit after tax and operating profit measured against the "
        r"Nifty 50.", md, count=1)

    if md != original:
        path.write_text(md)
        return True, rescored
    return False, "unchanged"


# ----------------------------------------------------- comparison report

# a pillar the one-year lens could not score shows an em dash, not a number
PILLAR_ROW_RE = re.compile(
    r"\| (?P<name>Business quality|Multibagger fit|Risk safety) \| "
    r"(?P<full>\d+|—) \| (?P<recent>\d+|—) \| (?P<delta>[-+\d]+|—) \|")
ROW_KEY = {"Business quality": "business quality",
           "Multibagger fit": "multibagger fit", "Risk safety": "risk safety"}


def _side_score(rows: dict, side: str, rel: int | None):
    """One side of the comparison, re-normalised over what is scored."""
    pts = {ROW_KEY[name]: int(m[side]) for name, m in rows.items()
           if m[side].isdigit()}
    if rel is not None:
        pts["relative to the index"] = rel
    if not pts:
        return None
    wsum = sum(BASE_WEIGHTS[n] for n in pts)
    return round(sum(v * BASE_WEIGHTS[n] for n, v in pts.items()) / wsum)
STEP1_RE = re.compile(
    r"Long-term view: (?P<fg>[\w ]+) \((?P<fs>\d+)/100\)\. Last one year: "
    r"(?P<rg>[\w ]+) \((?P<rs>\d+)/100\)\. The last year looks "
    r"(?P<verb>STRONGER than|WEAKER than|in line with) the long-term "
    r"picture \((?P<delta>[-+]\d+) points\)[^.]*\.")
HEAD_RE = re.compile(
    r"## Step 1 — The overall rating: (?P<dir>IMPROVED|DECLINED|HELD STEADY) "
    r"in the last year (?P<emoji>📈|📉|➡️)")


def update_comparison(sym: str, p_long: dict, p_recent: dict) -> tuple[bool, str]:
    path = OUT / f"{sym}_comparison.md"
    if not path.exists():
        return False, "no comparison report"
    md = path.read_text()
    original = md

    md = _strip_previous(md, BUCKET_HEAD, ("## How this comparison was built",))
    md = re.sub(r"\n\| Relative to the index \|[^\n]*\|", "", md)

    note = "pillar row added"
    new_full = new_rec = None
    rows = {m["name"]: m for m in PILLAR_ROW_RE.finditer(md)}
    step1 = STEP1_RE.search(md)
    # The one-year lens may not reach a company's latest year. That is the
    # same situation the other three pillars are already in when the window
    # cannot re-test them, so it is shown the same way: an em dash on the
    # recent side, and a recent overall re-normalised over what IS scored.
    f_rel = p_long["points"]
    r_rel = p_recent["points"]
    if rows and step1 and f_rel is not None:
        new_full = _side_score(rows, "full", f_rel)
        new_rec = _side_score(rows, "recent", r_rel)
        if new_full is None or new_rec is None:
            new_full = new_rec = None
    if new_full is not None and new_rec is not None:
        delta = new_rec - new_full
        direction = ("improved" if delta > 2 else
                     "declined" if delta < -2 else "held steady")
        verb = {"improved": "STRONGER than", "declined": "WEAKER than",
                "held steady": "in line with"}[direction]
        tail = {"improved": "the company has improved in the recent period",
                "declined": "the company has declined in the recent period",
                "held steady": "the company has held steady"}[direction]
        head_word, emoji = {"improved": ("IMPROVED", "📈"),
                            "declined": ("DECLINED", "📉"),
                            "held steady": ("HELD STEADY", "➡️")}[direction]
        fg, _ = grade_of(new_full)
        rg, _ = grade_of(new_rec)

        hm = HEAD_RE.search(md)
        if hm:
            md = md.replace(
                hm.group(0),
                f"## Step 1 — The overall rating: {head_word} in the last "
                f"year {emoji}")
        md = md.replace(
            step1.group(0),
            f"Long-term view: {fg} ({new_full}/100). Last one year: {rg} "
            f"({new_rec}/100). The last year looks {verb} the long-term "
            f"picture ({delta:+d} points) — {tail}.")
        # add the pillar row under Risk safety
        rs_row = rows["Risk safety"].group(0)
        rec_cell = "—" if r_rel is None else str(r_rel)
        delta_cell = "—" if r_rel is None else f"{r_rel - f_rel:+d}"
        md = md.replace(
            rs_row,
            f"{rs_row}\n| Relative to the index | {f_rel} | {rec_cell} | "
            f"{delta_cell} |")
        note = f"{step1['fs']}/{step1['rs']} → {new_full}/{new_rec}"

    # a bucket in Step 2, mirroring the other buckets
    bucket = [BUCKET_HEAD, ""]
    if p_long["points"] is None:
        bucket += ["The stored history is too short to compare this company "
                   "with the index over any window.", ""]
    else:
        bucket += [
            f"Over the long run the company has **{p_long['verdict']}** "
            f"({p_long['points']}/100). Looking only at the latest year, it "
            f"has **{p_recent['verdict'] if p_recent['points'] is not None else 'no comparable year'}**"
            + (f" ({p_recent['points']}/100)."
               if p_recent["points"] is not None else "."), "",
            "Each cell is the change in the company-to-index ratio across "
            "that window — a rise means the company outgrew the index.", "",
            REL.window_table(p_long), ""]
    md = md.replace("## How this comparison was built",
                    "\n".join(bucket) + "\n## How this comparison was built", 1)

    if md != original:
        path.write_text(md)
        return True, note
    return False, "unchanged"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--symbols", default="")
    args = ap.parse_args()

    syms = ([s.strip().upper() for s in args.symbols.split(",") if s.strip()]
            or universe())
    if args.limit:
        syms = syms[:args.limit]

    rows, counts = [], {"updated": 0, "no-relative": 0, "skipped": 0,
                        "failed": 0}
    t0 = time.time()
    for i, sym in enumerate(syms, 1):
        try:
            p_long = REL.pillar(sym)
            p_recent = REL.pillar(sym, windows=[1])
            a_ok, a_note = update_analysis(sym, p_long)
            c_ok, c_note = update_comparison(sym, p_long, p_recent)
            if p_long["points"] is None:
                status = "no-relative"
            elif a_ok or c_ok:
                status = "updated"
            else:
                status = "skipped"
            note = f"analysis: {a_note}; comparison: {c_note}"
        except Exception as exc:
            status, note = "failed", f"{type(exc).__name__}: {exc}"[:200]
            traceback.print_exc(limit=2)
        counts[status] += 1
        rows.append({"symbol": sym, "status": status,
                     "relative_points": (p_long.get("points")
                                         if "p_long" in dir() else ""),
                     "note": note})
        if i % 50 == 0 or i == len(syms):
            print(f"[{i:4d}/{len(syms)}] {sym:<14s} {status:<11s} "
                  f"upd={counts['updated']} norel={counts['no-relative']} "
                  f"fail={counts['failed']} ({time.time()-t0:.0f}s)",
                  flush=True)

    log = OUT / "_relative_index_log.csv"
    with open(log, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["symbol", "status",
                                          "relative_points", "note"])
        w.writeheader()
        w.writerows(rows)
    print(f"\nDONE in {time.time()-t0:.0f}s — {counts['updated']} updated, "
          f"{counts['no-relative']} without a comparable history, "
          f"{counts['skipped']} unchanged, {counts['failed']} failed. "
          f"Log: {log.name}")
    if counts["failed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
