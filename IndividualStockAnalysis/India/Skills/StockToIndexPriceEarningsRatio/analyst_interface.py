"""
analyst_interface.py — how this skill plugs into the AnalystSkill.

The AnalystSkill discovers any sibling skill that ships this file (see
the extensibility contract in AnalystSkill/scripts/registry.py) and
folds it into the combined report. This one contributes:

  pillar      "Relative to the index", weighted 10% of the overall
              rating. The three built-in pillars are weighted 40.5 / 27
              / 22.5 so the four sum to exactly 100%; when this pillar
              cannot be scored the analyst re-normalises and the
              original 45 / 30 / 25 split returns untouched.
  section_md  a full report section — the verdict, the 10 / 5 / 3 /
              1-year window table and the line graph of all three ratios
  facts       compact facts for the analyst's written summary

Everything is computed from stored data, so this adds no AI call and no
network round-trip to an analyst run.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE / "scripts"

PILLAR_WEIGHT = 0.10
SECTION_ORDER = 40          # after quality (10), patterns (20), risks (30)


def _load(name: str, filename: str):
    if name in sys.modules:
        return sys.modules[name]
    if str(SCRIPTS) not in sys.path:
        sys.path.append(str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def run(symbol: str, ai: bool = True) -> dict:
    """The analyst's extension entry point. `ai` is ignored: this skill
    reads stored data and never calls a model."""
    P = _load("stock_to_index_pillar", "index_pillar.py")
    linechart = _load("stock_to_index_linechart", "linechart.py")

    p = P.pillar(symbol)
    recent = P.pillar(symbol, windows=[1])
    series = P.series_for(symbol)

    md = [f"## Section 4 — How has it done against the index? "
          f"(price and earnings vs the Nifty 50)", ""]
    if p["points"] is None:
        md += [f"**Verdict: {p['verdict']}.**", "", p["derivation"], ""]
    else:
        md += [f"**Verdict: the company has {p['verdict']} — "
               f"{p['points']} out of 100.**", "",
               "The other three sections judge the business on its own "
               "terms. This one asks a different question: measured against "
               "the Nifty 50, has the company been pulling ahead or falling "
               "behind? Each ratio below is the company divided by the "
               "index, so a rise means the company outgrew the index and a "
               "fall means it lagged.", "",
               p["derivation"], "",
               "### The verdict over each window", "",
               P.window_table(p), ""]
        plotted = [(label, P.RATIO.yoy_series(series[key]))
                   for key, label in P.MEASURES]
        plotted = [(n, s, i) for i, (n, s) in enumerate(plotted) if s]
        if plotted:
            md += ["### How the three ratios moved, year by year", "",
                   linechart.render(
                       plotted,
                       "Yearly change of each ratio against the Nifty 50 (%)"),
                   ""]
        md += [f"The full index comparison — the level of each ratio year by "
               f"year and the raw numbers behind it — is in "
               f"[`{symbol}_stock_to_index.md`]({symbol}_stock_to_index.md), "
               f"with the same graph as "
               f"[`{symbol}_stock_to_index.svg`]({symbol}_stock_to_index.svg) "
               f"and [`{symbol}_stock_to_index.mmd`]"
               f"({symbol}_stock_to_index.mmd).", ""]

    windows = {}
    for c in p["cells"]:
        if c["pct"] is not None:
            windows.setdefault(f"last_{c['window']}y", {})[c["measure"]] = \
                f"{c['pct']:+.0f}% ({c['word']})"

    return {
        "name": "Relative to the index",
        "skill": "StockToIndexPriceEarningsRatio",
        "status": "ok" if p["points"] is not None else "no comparable history",
        "order": SECTION_ORDER,
        "record": {"pillar": p, "one_year": recent},
        "pillar": {"name": "Relative to the index", "points": p["points"],
                   "derivation": p["derivation"], "weight": PILLAR_WEIGHT},
        "section_md": "\n".join(md),
        "facts": {
            "relative_to_index": {
                "verdict": p["verdict"], "points": p["points"],
                "one_year_verdict": recent["verdict"],
                "one_year_points": recent["points"],
                "by_window": windows,
            },
            "names": ["Nifty 50"],
        },
    }
