"""Unit tests for the pure scoring / aggregation logic."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import scoring as S  # noqa: E402


def test_quant_to_score_maximize():
    th = {"strong": 0.25, "good": 0.15, "bad": 0.08, "weak": 0.04}
    assert S.quant_to_score(0.30, "maximize", th) == 2
    assert S.quant_to_score(0.18, "maximize", th) == 1
    assert S.quant_to_score(0.10, "maximize", th) == 0
    assert S.quant_to_score(0.06, "maximize", th) == -1
    assert S.quant_to_score(0.02, "maximize", th) == -2
    assert S.quant_to_score(None, "maximize", th) is None


def test_quant_to_score_minimize():
    th = {"strong": 0, "good": 30, "bad": 90, "weak": 150}
    assert S.quant_to_score(-10, "minimize", th) == 2   # negative CCC = best
    assert S.quant_to_score(20, "minimize", th) == 1
    assert S.quant_to_score(60, "minimize", th) == 0
    assert S.quant_to_score(100, "minimize", th) == -1
    assert S.quant_to_score(200, "minimize", th) == -2


def test_context_and_stable_not_auto_mapped():
    assert S.quant_to_score(5, "context", {}) is None
    assert S.quant_to_score(5, "stable", {}) is None


def _ps(pid, module, score, nature="quantitative"):
    return S.ParamScore(id=pid, module=module, nature=nature, score=score,
                        rationale="test", evidence={}, sources=[])


def test_score_module_ignores_none():
    ps = [_ps("ROC.headline", "ROC", 2), _ps("ROC.asset_turn", "ROC", None),
          _ps("ROC.profit_margin", "ROC", 1)]
    m = S.score_module(ps)
    assert m["module_score"] == 1.5           # (2+1)/2, None ignored
    assert m["n_assessed"] == 2
    assert m["n_total"] == 3
    assert abs(m["coverage"] - 2 / 3) < 1e-9


def test_score_module_all_none():
    ps = [_ps("X.a", "X", None), _ps("X.b", "X", None)]
    m = S.score_module(ps)
    assert m["module_score"] is None
    assert m["coverage"] == 0.0


def test_aggregate_weighted_overall():
    ps = [
        _ps("ROC.headline", "ROC", 2),
        _ps("CAP.working_capital_cost", "CAP", 0),
    ]
    weights = {"ROC": 2.0, "CAP": 1.0}
    agg = S.aggregate(ps, ["ROC", "CAP"], weights)
    # module scores: ROC=2, CAP=0 ; overall = (2*2 + 0*1)/(2+1) = 1.333
    assert abs(agg["overall_score"] - 4 / 3) < 1e-9
    assert agg["n_parameters_assessed"] == 2
    assert agg["modules"]["ROC"]["module_score"] == 2


def test_aggregate_all_unassessed_gives_none():
    ps = [_ps("ROC.headline", "ROC", None)]
    agg = S.aggregate(ps, ["ROC"], {"ROC": 1.0})
    assert agg["overall_score"] is None
    assert agg["overall_coverage"] == 0.0


def test_rank_orders_by_score_then_coverage():
    a = S.aggregate([_ps("ROC.headline", "ROC", 2), _ps("ROC.asset_turn", "ROC", 2)],
                    ["ROC"], {"ROC": 1.0})            # score 2, coverage 1.0
    b = S.aggregate([_ps("ROC.headline", "ROC", 2), _ps("ROC.asset_turn", "ROC", None)],
                    ["ROC"], {"ROC": 1.0})            # score 2, coverage 0.5
    c = S.aggregate([_ps("ROC.headline", "ROC", -1)], ["ROC"], {"ROC": 1.0})  # score -1
    order = S.rank({"A": a, "B": b, "C": c})
    assert order == ["A", "B", "C"]  # A>B on coverage tie-break, C last on score


def test_clamp():
    assert S.clamp(5) == 2
    assert S.clamp(-9) == -2
    assert S.clamp(1) == 1
