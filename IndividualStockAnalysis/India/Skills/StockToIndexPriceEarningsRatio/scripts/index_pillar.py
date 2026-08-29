"""
index_pillar.py — this skill's verdict, scored as an analyst pillar.

The AnalystSkill folds this in as its fourth input (see
../analyst_interface.py): how the company has done AGAINST the index,
not just on its own.

The first three inputs judge the company in isolation (is the business
good, does it look like a long-term winner, what could break it). This
one asks a different question: over the last ten, five, three and one
fiscal years, did the company GAIN on the Nifty 50 or LAG it — on price,
on profit after tax, and on operating profit?

It reuses the StockToIndexPriceEarningsRatio skill's stored ratio series,
so nothing is recomputed and no AI call is made.

Scoring, on the same −2..+2 scale the 34-check framework uses:

    a ratio up  25% or more over the window   +2  gained strongly
    up 10% to 25%                             +1  gained
    within ±10%                                0  moved with the index
    down 10% to 25%                           −1  lagged
    down 25% or more                          −2  lagged badly

Every measure × window pair that the stored data can answer becomes one
cell; the pillar is the mean of those cells mapped onto 0–100. Pairs the
data cannot reach are left out, never guessed, and the coverage is
reported alongside the score.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RATIO_SCRIPTS = HERE                      # analyze.py is a sibling


def _load_ratio_module():
    """Load the ratio skill's analyze.py under its own module name.

    A plain `import analyze` would collide with this skill's own
    analyze.py, so the module is loaded by path and registered as
    `stock_to_index_analyze` instead. Its own folder goes on sys.path
    (appended, never prepended) because it imports sibling helpers.
    """
    if "stock_to_index_analyze" in sys.modules:
        return sys.modules["stock_to_index_analyze"]
    if str(RATIO_SCRIPTS) not in sys.path:
        sys.path.append(str(RATIO_SCRIPTS))
    spec = importlib.util.spec_from_file_location(
        "stock_to_index_analyze", RATIO_SCRIPTS / "analyze.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["stock_to_index_analyze"] = mod
    spec.loader.exec_module(mod)
    return mod


RATIO = _load_ratio_module()

WINDOWS = [10, 5, 3, 1]
MEASURES = [("price", "Price ratio"),
            ("pat", "PAT ratio"),
            ("op", "Operating-profit ratio")]

CELL_WORD = {2: "gained strongly", 1: "gained", 0: "moved with",
             -1: "lagged", -2: "lagged badly"}


def _by_year(rows: list[tuple[str, float]]) -> dict[int, float]:
    return {int(fy.split()[1]): v for fy, v in rows}


def window_change(rows: list[tuple[str, float]], window: int):
    """Percentage change of the ratio across `window` fiscal years.

    Returns (pct, from_year, to_year) or None when the stored data does
    not reach back that far.
    """
    by_year = _by_year(rows)
    if len(by_year) < 2:
        return None
    latest = max(by_year)
    base = latest - window
    if base not in by_year or by_year[base] == 0:
        return None
    a, b = by_year[base], by_year[latest]
    if a < 0 <= b or b < 0 <= a:      # a sign flip has no honest percentage
        return None
    return (b - a) / abs(a) * 100, base, latest


def cell_score(pct: float) -> int:
    if pct >= 25:
        return 2
    if pct >= 10:
        return 1
    if pct > -10:
        return 0
    if pct > -25:
        return -1
    return -2


def _verdict_word(mean: float) -> str:
    if mean >= 1:
        return "GAINED STRONGLY on the index"
    if mean >= 0.25:
        return "GAINED on the index"
    if mean > -0.25:
        return "MOVED WITH the index"
    if mean > -1:
        return "LAGGED the index"
    return "LAGGED the index badly"


def series_for(sym: str) -> dict[str, list[tuple[str, float]]]:
    """The company's three ratio series, from the ratio skill."""
    RATIO.build_report(sym)                     # fills its series cache
    s = RATIO._LAST_SERIES.get(sym, {})
    return {"price": s.get("price", []), "pat": s.get("pat", []),
            "op": s.get("op", [])}


def pillar(sym: str, windows: list[int] | None = None) -> dict:
    """The relative-to-index pillar.

    windows=None uses 10/5/3/1 (the long view). Pass [1] for the
    one-year lens, which may only look at the latest year.
    """
    windows = windows or WINDOWS
    series = series_for(sym)
    cells: list[dict] = []
    for key, label in MEASURES:
        rows = series.get(key) or []
        for w in windows:
            got = window_change(rows, w)
            if got is None:
                cells.append({"measure": label, "window": w, "pct": None,
                              "score": None, "word": "not in the stored data"})
                continue
            pct, base, latest = got
            sc = cell_score(pct)
            cells.append({"measure": label, "window": w, "pct": pct,
                          "score": sc, "word": CELL_WORD[sc],
                          "from": base, "to": latest})

    scored = [c for c in cells if c["score"] is not None]
    if not scored:
        return {"name": "Relative to the index", "points": None,
                "cells": cells, "coverage": 0.0, "mean": None,
                "verdict": "no comparable years in the stored data",
                "derivation": "The stored price and profit history does not "
                              "reach back far enough to compare this company "
                              "with the index over any window."}

    mean = sum(c["score"] for c in scored) / len(scored)
    points = round((mean + 2) / 4 * 100)
    coverage = len(scored) / len(cells)
    return {
        "name": "Relative to the index", "points": points, "cells": cells,
        "coverage": coverage, "mean": mean, "verdict": _verdict_word(mean),
        "derivation": (
            f"Across {len(scored)} of {len(cells)} measure-and-window pairs "
            f"the stored data could answer, the company scored {mean:+.2f} on "
            f"the −2 (lagged badly) to +2 (gained strongly) scale against the "
            f"Nifty 50; mapped onto 0–100 that is {points} points."),
    }


def window_table(p: dict) -> str:
    """Markdown table: one row per window, one column per measure."""
    windows = sorted({c["window"] for c in p["cells"]}, reverse=True)
    measures = [label for _k, label in MEASURES]
    head = "| Window | " + " | ".join(measures) + " |"
    rows = [head, "|---" * (len(measures) + 1) + "|"]
    for w in windows:
        cells = []
        for m in measures:
            c = next((c for c in p["cells"]
                      if c["window"] == w and c["measure"] == m), None)
            if c is None or c["pct"] is None:
                cells.append("—")
            else:
                cells.append(f"{c['pct']:+.0f}% · {c['word']}")
        label = f"last {w} year" + ("s" if w > 1 else "")
        rows.append(f"| {label} | " + " | ".join(cells) + " |")
    return "\n".join(rows) + "\n"
