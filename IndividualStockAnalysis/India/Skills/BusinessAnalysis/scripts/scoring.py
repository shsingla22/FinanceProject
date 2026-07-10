"""
scoring.py — pure, testable scoring + aggregation for the Business Analysis skill.

Combines QUANTITATIVE signals (from quant_signals.py) and QUALITATIVE judgements
(produced by an LLM following reference/qualitative_playbook.md) into:
  - a per-parameter score on a fixed scale
  - per-module scores (weighted)
  - an overall business-quality score + rank input
  - an explainability trace (every score carries its evidence + source)

Scoring scale (per parameter): integers -2 .. +2
  +2 strong positive  |  +1 positive  |  0 neutral/mixed
  -1 negative         |  -2 strong negative  |  None = not assessed (no data)

`direction` from the framework tells us how to read a raw quantitative value; the
LLM supplies qualitative scores directly on the -2..+2 scale with a rationale.

Nothing here does I/O or calls a model — it is deterministic and unit-tested.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict

SCALE_MIN, SCALE_MAX = -2, 2

# Default module weights (sum need not be 1; normalised at aggregation).
# Rationale: quality-investing weights durable economics (ROC, MOAT, IND) and
# capital discipline (CAP) highest; growth and the softer human factors slightly
# lower because they are more judgemental. Tune per mandate.
DEFAULT_MODULE_WEIGHTS = {
    "CAP": 1.0,
    "ROC": 1.25,
    "GRW": 1.0,
    "MGT": 1.0,
    "IND": 1.25,
    "CUS": 1.0,
    "MOAT": 1.25,
}


@dataclass
class ParamScore:
    id: str
    module: str
    nature: str
    score: int | None          # -2..+2 or None (not assessed)
    rationale: str             # why this score
    evidence: dict = field(default_factory=dict)   # raw numbers / quotes used
    sources: list = field(default_factory=list)    # provenance pointers
    quant_available: bool = False


def clamp(x: int) -> int:
    return max(SCALE_MIN, min(SCALE_MAX, int(x)))


def score_module(param_scores: list) -> dict:
    """Average of assessed parameter scores in a module (ignoring None)."""
    assessed = [p.score for p in param_scores if p.score is not None]
    coverage = len(assessed) / len(param_scores) if param_scores else 0.0
    module_score = (sum(assessed) / len(assessed)) if assessed else None
    return {
        "module_score": module_score,
        "coverage": coverage,
        "n_assessed": len(assessed),
        "n_total": len(param_scores),
    }


def aggregate(param_scores: list, module_ids: list,
              weights: dict | None = None) -> dict:
    """Aggregate parameter scores -> module scores -> overall.

    Returns a full explainability record (a decision tree): overall -> modules ->
    parameters, each with score, rationale, evidence, sources.
    """
    weights = weights or DEFAULT_MODULE_WEIGHTS
    by_module = {m: [] for m in module_ids}
    for p in param_scores:
        by_module.setdefault(p.module, []).append(p)

    module_records = {}
    weighted_sum = 0.0
    weight_used = 0.0
    for m in module_ids:
        ms = score_module(by_module.get(m, []))
        module_records[m] = {
            **ms,
            "parameters": [asdict(p) for p in by_module.get(m, [])],
        }
        if ms["module_score"] is not None:
            w = weights.get(m, 1.0)
            weighted_sum += ms["module_score"] * w
            weight_used += w

    overall = (weighted_sum / weight_used) if weight_used > 0 else None
    total_params = len(param_scores)
    assessed = sum(1 for p in param_scores if p.score is not None)

    return {
        "overall_score": overall,                 # -2..+2
        "overall_coverage": assessed / total_params if total_params else 0.0,
        "n_parameters_assessed": assessed,
        "n_parameters_total": total_params,
        "weights": weights,
        "modules": module_records,
    }


def rank(company_records: dict) -> list:
    """Given {symbol: aggregate_record}, return symbols sorted best-first.

    Ranking key = (overall_score, coverage) so a well-evidenced company outranks
    a thinly-evidenced one at the same score. Companies with no score sort last.
    """
    def key(item):
        _sym, rec = item
        s = rec.get("overall_score")
        return (s if s is not None else -99, rec.get("overall_coverage", 0.0))
    return [sym for sym, _ in sorted(company_records.items(), key=key, reverse=True)]


def quant_to_score(value, direction: str, thresholds: dict) -> int | None:
    """Map a raw quantitative value to a -2..+2 score using per-signal thresholds.

    thresholds: {"strong": x2, "good": x1, "bad": y1, "weak": y2} interpreted
    per direction. Kept explicit and injectable so it is fully unit-testable and
    tunable without touching logic.
    """
    if value is None:
        return None
    if direction == "maximize":
        if value >= thresholds["strong"]:
            return 2
        if value >= thresholds["good"]:
            return 1
        if value <= thresholds["weak"]:
            return -2
        if value <= thresholds["bad"]:
            return -1
        return 0
    if direction == "minimize":
        if value <= thresholds["strong"]:
            return 2
        if value <= thresholds["good"]:
            return 1
        if value >= thresholds["weak"]:
            return -2
        if value >= thresholds["bad"]:
            return -1
        return 0
    # 'stable' and 'context' are decided qualitatively; no auto-map here.
    return None
