"""
rating.py — the unified company rating built from all three skills.

Three pillars, one score out of 100, one grade in plain words:

  1. Business quality  (45%)  — the BusinessAnalysis skill's 34-check
                                framework: how good is this business today?
  2. Multibagger fit   (30%)  — the MultibaggerPattern skill: does it match
                                the patterns long-term winners share?
  3. Risk safety       (25%)  — the QualityRisks skill: how exposed is it to
                                the ways quality companies fail? (higher =
                                safer)

Deterministic and explainable by construction: every pillar carries a
points breakdown listing exactly what earned or cost points, and the
composite states its arithmetic in one sentence. Nothing is narrated after
the fact — the derivations are built from the same variables that decided
the numbers.
"""

from __future__ import annotations

import importlib.util
import os
import re
import sys
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent / "IndividualStockAnalysis" / "India"

# The quality judge for ALL skills. Opus 5 by default (per user preference);
# ANALYSIS_MODEL overrides everything at once.
JUDGE_MODEL = os.environ.get("ANALYSIS_MODEL", "claude-opus-5")
os.environ.setdefault("MB_JUDGE_MODEL", JUDGE_MODEL)
os.environ.setdefault("RISK_JUDGE_MODEL", JUDGE_MODEL)


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# Load each skill's analyze module under a unique name (both are called
# analyze.py); their own engine/evidence imports register under their
# unique real names.
MB_AZ = _load("mb_analyze",
              INDIA / "Skills" / "MultibaggerPattern" / "scripts" / "analyze.py")
QR_AZ = _load("qr_analyze",
              INDIA / "Skills" / "QualityRisks" / "scripts" / "analyze.py")
MB_PE = sys.modules["pattern_engine"]
MB_QE = sys.modules["quant_evidence"]
QR_RE = sys.modules["risk_engine"]
QR_QE = sys.modules["risk_evidence"]

# One judge subprocess per skill at a time (their disk caches are per-skill).
_mb_lock = threading.Lock()
_qr_lock = threading.Lock()

# The judges write analyst shorthand; readers shouldn't need to know it.
# Applied to AI rationales and mitigants ONLY — verbatim call quotes are
# management's own words and are never rewritten.
_PLAIN_TERMS = [
    (re.compile(r"\bYoY\b"), "year-on-year"),
    (re.compile(r"\by-o-y\b", re.I), "year-on-year"),
    (re.compile(r"\bQoQ\b"), "quarter-on-quarter"),
    (re.compile(r"\bFCF\b"), "free cash flow"),
    (re.compile(r"\bCAGR\b"), "compound annual growth"),
    (re.compile(r"\bcapex\b"), "capital spending"),
    (re.compile(r"\bopex\b"), "operating costs"),
    (re.compile(r"(\d)\s?bps\b"), r"\1 hundredths of a percentage point"),
]


def _plain(text: str) -> str:
    for pat, repl in _PLAIN_TERMS:
        text = pat.sub(repl, text)
    return text


def _plain_qual(rec: dict) -> dict:
    """Rewrite analyst shorthand in the judge's rationales to everyday
    language, in place. Quotes are left untouched."""
    for v in rec.get("verdicts", []):
        q = v.get("qual") or {}
        for field in ("rationale", "mitigant"):
            if q.get(field):
                q[field] = _plain(q[field])
    return rec


def patterns_analysis(sym: str, ai: bool = True) -> tuple[dict, str]:
    """MultibaggerPattern record for one company. status explains what ran."""
    checks = MB_QE.compute_checks(sym)
    qual, status = None, "numbers_only"
    if ai:
        try:
            with _mb_lock:
                qual = MB_AZ.qual_judge(sym, MB_PE.load_taxonomy())
            status = "with_calls" if qual else "no_concalls"
        except Exception as e:
            status = f"judge_failed: {str(e)[:120]}"
    return _plain_qual(MB_PE.analyse(sym, checks, qual)), status


def risks_analysis(sym: str, ai: bool = True) -> tuple[dict, str]:
    """QualityRisks record for one company. status explains what ran."""
    checks = QR_QE.compute_checks(sym)
    qual, status = None, "numbers_only"
    if ai:
        try:
            with _qr_lock:
                qual = QR_AZ.qual_judge(sym, QR_RE.load_taxonomy())
            status = "with_calls" if qual else "no_concalls"
        except Exception as e:
            status = f"judge_failed: {str(e)[:120]}"
    return _plain_qual(QR_RE.analyse(sym, checks, qual)), status


# ------------------------------------------------------------------ pillars
GRADE_BANDS = [(80, "Outstanding", 5), (65, "Strong", 4), (50, "Decent", 3),
               (35, "Mixed", 2), (0, "Weak", 1)]
WEIGHTS = {"quality": 0.45, "patterns": 0.30, "safety": 0.25}


def _grade(score: float) -> tuple[str, int]:
    for cut, word, stars in GRADE_BANDS:
        if score >= cut:
            return word, stars
    return "Weak", 1


def quality_pillar(rec: dict) -> dict:
    """Business quality 0–100 from the 34-check framework's −2…+2 overall."""
    overall = rec.get("overall")
    cov = rec.get("coverage") or 0
    if overall is None:
        return {"name": "Business quality", "points": None,
                "derivation": "The 34-check quality framework could not "
                              "score this business — not enough evidence."}
    pts = round((overall + 2) / 4 * 100)
    caution = ("" if cov >= 0.5 else
               f" Caution: only {cov:.0%} of the 34 checks could be "
               f"answered from this evidence — a thin base; the full "
               f"analysis (with the conference calls) firms this up.")
    return {
        "name": "Business quality",
        "points": pts,
        "derivation": (
            f"The 34-check quality framework scored the business "
            f"{overall:+.2f} on its −2 (poor) to +2 (excellent) scale, with "
            f"{cov:.0%} of checks backed by evidence; mapped onto 0–100 "
            f"that is {pts} points.") + caution,
        "detail": {"overall": overall, "coverage": cov,
                   "qualitative_included": rec.get("qualitative_included",
                                                   False)},
    }


def patterns_pillar(mb_rec: dict) -> dict:
    """Multibagger fit 0–100: foundation gate + how many patterns fit."""
    vs = mb_rec["verdicts"]
    strong = [v["name"] for v in vs if v["verdict"] == "STRONG FIT"]
    likely = [v["name"] for v in vs if v["verdict"] == "LIKELY FIT"]
    signal = [v["name"] for v in vs if v["verdict"] == "QUANT SIGNAL"]
    gate = mb_rec["core_gate"]["status"]
    gate_pts = {"PASS": 25, "PARTIAL": 10}.get(gate, 0)
    pts = min(100, gate_pts + 15 * len(strong) + 8 * len(likely)
              + 3 * len(signal))
    parts = []
    if gate == "PASS":
        parts.append("the foundation test (steady cash + high returns on "
                     "capital + growth) passed in full (+25)")
    elif gate == "PARTIAL":
        parts.append("the foundation test partly passed (+10)")
    else:
        parts.append("the foundation test did not pass (+0)")
    if strong:
        parts.append(f"{len(strong)} pattern{'s' if len(strong) > 1 else ''} "
                     f"fit strongly ({', '.join(strong[:4])}"
                     f"{'…' if len(strong) > 4 else ''}) "
                     f"(+{15 * len(strong)})")
    if likely:
        parts.append(f"{len(likely)} likely fit{'s' if len(likely) > 1 else ''} "
                     f"(+{8 * len(likely)})")
    if signal:
        parts.append(f"{len(signal)} numbers-only hint"
                     f"{'s' if len(signal) > 1 else ''} (+{3 * len(signal)})")
    if not (strong or likely or signal):
        parts.append("no pattern found meaningful support (+0)")
    return {
        "name": "Multibagger fit",
        "points": pts,
        "derivation": "; ".join(parts) + f" → {pts} of 100."
                      + (" (Capped at 100.)" if gate_pts + 15 * len(strong)
                         + 8 * len(likely) + 3 * len(signal) > 100 else ""),
        "detail": {"gate": gate, "strong": strong, "likely": likely,
                   "signal": signal},
    }


def safety_pillar(qr_rec: dict) -> dict:
    """Risk safety 0–100: start at 100, each found risk costs points."""
    vs = qr_rec["verdicts"]
    high = [v["name"] for v in vs if v["verdict"] == "HIGH RISK"]
    elev = [v["name"] for v in vs if v["verdict"] == "ELEVATED"]
    watch = [v["name"] for v in vs if v["verdict"] == "WATCH"]
    flags = [v["name"] for v in vs if v["verdict"] == "QUANT FLAG"]
    frag = qr_rec["fragility"]["status"]
    frag_pts = {"STRESSED": 20, "STRAINED": 8}.get(frag, 0)
    raw = (100 - 20 * len(high) - 10 * len(elev) - 4 * len(watch)
           - 4 * len(flags) - frag_pts)
    pts = max(0, raw)
    parts = ["started from a clean 100"]
    if high:
        parts.append(f"{len(high)} high risk{'s' if len(high) > 1 else ''} "
                     f"({', '.join(high[:3])}{'…' if len(high) > 3 else ''}) "
                     f"(−{20 * len(high)})")
    if elev:
        parts.append(f"{len(elev)} elevated (−{10 * len(elev)})")
    if watch:
        parts.append(f"{len(watch)} worth watching (−{4 * len(watch)})")
    if flags:
        parts.append(f"{len(flags)} numbers-only flag"
                     f"{'s' if len(flags) > 1 else ''} (−{4 * len(flags)})")
    if frag_pts:
        parts.append(f"the balance sheet shows "
                     f"{'multiple stress signals' if frag == 'STRESSED' else 'one stress signal'} "
                     f"(−{frag_pts})")
    if len(parts) == 1:
        parts.append("no risk channel cost any points")
    return {
        "name": "Risk safety",
        "points": pts,
        "derivation": "; ".join(parts)
                      + f" → {pts} of 100."
                      + (" (Floored at 0.)" if raw < 0 else ""),
        "detail": {"high": high, "elevated": elev, "watch": watch,
                   "flags": flags, "fragility": frag},
    }


def compute_rating(sym: str, business_rec: dict, mb_rec: dict,
                   qr_rec: dict) -> dict:
    """Combine the three pillars into one rating, with full arithmetic."""
    pillars = {
        "quality": quality_pillar(business_rec),
        "patterns": patterns_pillar(mb_rec),
        "safety": safety_pillar(qr_rec),
    }
    avail = {k: p for k, p in pillars.items() if p["points"] is not None}
    if not avail:
        return {"symbol": sym, "score": None, "grade": "Not rated",
                "stars": 0, "pillars": pillars,
                "derivation": "None of the three pillars could be scored — "
                              "not enough evidence to rate this company."}
    wsum = sum(WEIGHTS[k] for k in avail)
    score = round(sum(pillars[k]["points"] * WEIGHTS[k] for k in avail)
                  / wsum)
    grade, stars = _grade(score)
    terms = " + ".join(
        f"{WEIGHTS[k] / wsum:.0%} × {pillars[k]['points']} "
        f"({pillars[k]['name'].lower()})" for k in ("quality", "patterns",
                                                    "safety") if k in avail)
    note = ("" if len(avail) == 3 else
            " (One or more pillars had no evidence, so the weights were "
            "re-spread over the pillars that could be scored.)")
    return {
        "symbol": sym,
        "score": score,
        "grade": grade,
        "stars": stars,
        "pillars": pillars,
        "derivation": f"Overall rating = {terms} = {score} out of 100 → "
                      f"{grade} ({stars} star{'s' if stars > 1 else ''})."
                      + note,
        "judge_model": JUDGE_MODEL,
    }
