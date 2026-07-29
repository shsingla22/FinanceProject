"""
analyst_bridge.py — the UI's gateway to the AnalystSkill.

The company view and the downloadable report are now the SAME analysis:
this module runs the AnalystSkill's registry (all three sibling skills +
extensions) and composer (overview, rating, grounded summary, Markdown)
once, and hands both the structured records (for the interactive UI) and
the composed Markdown (for download) back to the server. Nothing is
computed twice, so the page and the file can never disagree.
"""

from __future__ import annotations

import importlib.util
import sys
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = (HERE.parent / "IndividualStockAnalysis" / "India" / "Skills"
         / "AnalystSkill" / "scripts")


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


AR = _load("ui_analyst_registry", SKILL / "registry.py")
# composer does `import registry` at load time — alias it FIRST so both
# modules share one registry instance (and one set of judge caches)
sys.modules.setdefault("registry", AR)
AC = _load("ui_analyst_composer", SKILL / "composer.py")
AC.REG = AR

_locks: dict = {}
_locks_guard = threading.Lock()


def _lock_for(sym: str) -> threading.Lock:
    with _locks_guard:
        return _locks.setdefault(sym, threading.Lock())


def full_analysis(sym: str, ai: bool = True) -> dict:
    """Run everything once; return records + rating + overview + summary +
    the composed Markdown. Judges and AI steps are cached by the skills."""
    with _lock_for(sym):
        ba, s1 = AR.run_business(sym, ai=ai)
        mb, s2 = AR.run_patterns(sym, ai=ai)
        qr, s3 = AR.run_risks(sym, ai=ai)
        exts = AR.run_extensions(sym, ai=ai)
        rt = AC.compute_rating(ba, mb, qr, extensions=exts)
        meta = AR.company_meta(sym)
        overview = AC.business_overview(sym, meta["name"]) if ai else None
        synth = (AC.synthesize(sym, meta["name"], ba, mb, qr, rt,
                               extensions=exts) if ai else None)
        trends = AR.trend_series(sym)
        statuses = {"business": s1, "patterns": s2, "risks": s3}
        md = AC.render(sym, meta["name"], ba, mb, qr, rt, synth, statuses,
                       extensions=exts, overview=overview, trends=trends,
                       industry=meta["industry"])
        return {
            "symbol": sym, "name": meta["name"],
            "industry": meta["industry"],
            "overview": overview,
            "rating": rt,
            "verdict_plain": AC._verdict_plain(rt),
            "summary": synth,
            "business": ba, "patterns": mb, "risks": qr,
            "extensions": [{k: e.get(k) for k in
                            ("skill", "name", "status", "order",
                             "pillar", "section_md")}
                           for e in exts],
            "trends": trends,
            "statuses": statuses,
            "md": md,
        }
