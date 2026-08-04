"""
comparison_bridge.py — the UI's gateway to the ComparisonSkill.

When the user analyses a company, the page shows the full AnalystSkill
workup on the left and, on the right, the ComparisonSkill's answer to
"how have things moved in the last one year?" — the full-history view
vs the RecentAnalystSkill's one-year view.

Same page==file guarantee as analyst_bridge: the comparison record the
panel renders and the downloadable comparison Markdown come from ONE
run of the skill, cached together, so they can never disagree.

Each side runs through its own skill's CLI in a subprocess (the
one-year skill windows its engines in-process, so the two sides must
never share an interpreter) — exactly how the ComparisonSkill's own
CLI does it. Results are cached in memory per (symbol, ai-mode); the
skills' own judge caches make recomputation after a server restart
cheap for already-analysed companies.
"""

from __future__ import annotations

import importlib.util
import sys
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = (HERE.parent / "IndividualStockAnalysis" / "India" / "Skills"
         / "ComparisonSkill" / "scripts")


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# by explicit path — every skill has an analyze.py, so sys.path would
# resolve the wrong one
CE = _load("ui_compare_engine", SKILL / "compare_engine.py")
CA = _load("ui_compare_analyze", SKILL / "analyze.py")

_results: dict = {}
_locks: dict = {}
_locks_guard = threading.Lock()


def _lock_for(sym: str) -> threading.Lock:
    with _locks_guard:
        return _locks.setdefault(sym, threading.Lock())


def full_comparison(sym: str, ai: bool = True) -> dict:
    """Run the ComparisonSkill once for a symbol; return the structured
    comparison record AND the composed Markdown, cached together."""
    key = (sym, bool(ai))
    with _lock_for(sym):
        if key in _results:
            return _results[key]
        full = CE.run_analysis(sym, "full", ai=ai)
        recent = CE.run_analysis(sym, "recent", ai=ai)
        rec = CE.compare(sym, full, recent)
        name = CA._company_name(sym)
        md = CA.render(sym, name, rec)
        out = {"symbol": sym, "name": name, "record": rec, "md": md}
        _results[key] = out
        return out


def cached(sym: str) -> dict | None:
    """The comparison for a symbol IF it has already been computed this
    session (either ai mode) — used to ground Q&A without triggering an
    expensive recompute."""
    for ai in (True, False):
        if (sym, ai) in _results:
            return _results[(sym, ai)]
    return None


def drop_caches() -> None:
    _results.clear()
