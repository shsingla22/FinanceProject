"""
QualityRisks skill tests.

  python3 -m pytest tests/ -q     (from Skills/QualityRisks/)

Covers: taxonomy completeness (no risk missed), the severity ladder,
risk fingerprints on synthetic profiles shaped like the document's examples
(a steel-like pure cyclical, a Nobel-Biocare-like premium collapse, a
stable-compounder counterexample), the explainability contract (every
verdict carries evidence), and a real-data integration pass.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

import risk_engine as RE      # noqa: E402
import risk_evidence as QE    # noqa: E402


# ------------------------------------------------------------ completeness
def test_taxonomy_valid_and_complete():
    problems = RE.validate()
    assert problems == [], "taxonomy problems:\n" + "\n".join(problems)


def test_all_eight_risks_present():
    tax = RE.load_taxonomy()
    assert len(tax["risks"]) == 8
    ids = {r["id"] for r in tax["risks"]}
    assert ids == {"CYCLICALITY", "TECH_DISRUPTION", "GOVT_DEPENDENCY",
                   "CONCENTRATION", "NEW_ENTRANTS", "PREFERENCE_SHIFT",
                   "FASHION", "GOOD_ENOUGH"}


def test_every_declared_check_is_implemented():
    import yaml
    chk = yaml.safe_load((HERE.parent / "reference" / "checklist.yaml").read_text())
    produced = _checks_for_profile(_stable_compounder())
    for cid in chk["expected_quant_checks"] + chk["expected_fragility_checks"]:
        assert cid in produced, f"risk check not implemented: {cid}"


# ------------------------------------------------------------ synthetic profiles
def _checks_for_profile(g):
    orig = QE.gather
    QE.gather = lambda sym, base=None, universe=None: g
    try:
        return QE.compute_checks("TEST")
    finally:
        QE.gather = orig


def _stable_compounder():
    """Steady franchise: no risk fingerprints anywhere."""
    return {
        "sales": [800, 880, 960, 1050, 1160, 1280, 1400, 1550, 1700, 1870],
        "opm": [22, 22, 23, 23, 24, 24, 24, 25, 25, 25],
        "gm": [55, 55, 56, 56, 57, 57, 57, 58, 58, 58],
        "op": [176, 194, 221, 242, 278, 307, 336, 388, 425, 468],
        "cfo": [180, 200, 225, 250, 285, 315, 345, 395, 430, 475],
        "capex": [-20, -22, -24, -26, -28, -31, -34, -37, -41, -45],
        "debtor_days": [35, 34, 35, 36, 35, 34, 35, 36, 35, 34],
        "roce": [35, 36, 36, 37, 38, 38, 39, 40, 40, 41],
        "borrowing": [50, 48, 45, 42, 40, 38, 35, 30, 25, 20],
        "equity": [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
        "reserves": [400, 460, 530, 610, 700, 800, 910, 1040, 1180, 1340],
    }


def _steel_like():
    """Pure cycle: commodity boom-bust in sales AND margins, capex binge."""
    g = _stable_compounder()
    g["sales"] = [900, 1400, 1900, 1100, 800, 1300, 2100, 1500, 1000, 1700]
    g["opm"] = [8, 22, 28, 10, 4, 18, 30, 15, 6, 20]
    g["capex"] = [-90, -300, -600, -500, -100, -80, -400, -700, -200, -100]
    return g


def _nobel_like():
    """Good-enough attack: 34% OPM and 80% GM competed down to 13% / 68%."""
    g = _stable_compounder()
    g["opm"] = [34, 33, 31, 28, 24, 21, 18, 16, 14, 13]
    g["gm"] = [80, 79, 78, 76, 74, 73, 71, 70, 69, 68]
    g["sales"] = [1000, 1220, 1480, 1750, 1900, 1980, 2020, 2060, 2080, 2100]
    return g


def _stressed_bs():
    """Fragile: leverage climbing, cash conversion slipping, returns sliding."""
    g = _stable_compounder()
    g["borrowing"] = [100, 200, 350, 550, 800, 1100, 1500, 1900, 2400, 3000]
    g["equity"] = [50] * 10
    g["reserves"] = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]
    g["cfo"] = [160, 150, 140, 120, 100, 90, 130, 60, 50, 40]
    g["op"] = [180, 190, 200, 210, 220, 230, 240, 250, 260, 270]
    g["roce"] = [24, 22, 20, 18, 16, 14, 13, 12, 11, 10]
    return g


def test_stable_compounder_has_no_flags():
    checks = _checks_for_profile(_stable_compounder())
    flagged = [k for k, c in checks.items() if c["flagged"] is True]
    assert flagged == [], f"stable compounder wrongly flagged: {flagged}"
    rec = RE.analyse("STEADYCO", checks)
    assert rec["material_risks"] == []
    assert rec["fragility"]["status"] == "SOUND"


def test_steel_like_cyclical_flagged():
    checks = _checks_for_profile(_steel_like())
    assert checks["sales_swings"]["flagged"] is True
    assert checks["margin_swings"]["flagged"] is True
    assert "fluctuate" in checks["margin_swings"]["explanation"]
    rec = RE.analyse("STEELCO", checks)
    cyc = next(v for v in rec["verdicts"] if v["risk"] == "CYCLICALITY")
    assert cyc["verdict"] == "QUANT FLAG"      # numbers alone cap here
    assert "CYCLICALITY" in rec["material_risks"]


def test_nobel_like_collapse_flagged():
    checks = _checks_for_profile(_nobel_like())
    assert checks["margin_collapse"]["flagged"] is True
    assert checks["gross_margin_erosion"]["flagged"] is True
    assert checks["pricing_pressure"]["flagged"] is True
    assert "collapsed" in checks["margin_collapse"]["explanation"]
    rec = RE.analyse("NOBELCO", checks)
    ge = next(v for v in rec["verdicts"] if v["risk"] == "GOOD_ENOUGH")
    assert ge["verdict"] == "QUANT FLAG"


def test_stressed_balance_sheet_detected():
    checks = _checks_for_profile(_stressed_bs())
    rec = RE.analyse("FRAGILECO", checks)
    assert rec["fragility"]["status"] == "STRESSED"
    assert rec["fragility"]["flagged"] >= 2


# ------------------------------------------------------------ severity ladder
def _risk(rid="GOOD_ENOUGH"):
    tax = RE.load_taxonomy()
    return next(r for r in tax["risks"] if r["id"] == rid)


def test_ladder_high_plus_quant_is_high_risk():
    checks = _checks_for_profile(_nobel_like())
    v = RE.combine(_risk(), checks, {"exposure": "high", "rationale": "r",
                                     "quote": "q"})
    assert v["verdict"] == "HIGH RISK"


def test_ladder_high_without_quant_dimension_is_high_risk():
    checks = _checks_for_profile(_stable_compounder())
    v = RE.combine(_risk("GOVT_DEPENDENCY"), checks,
                   {"exposure": "high", "rationale": "tariff-set business"})
    assert v["verdict"] == "HIGH RISK"       # GOVT has no quant fingerprint


def test_ladder_high_with_clean_numbers_is_elevated():
    checks = _checks_for_profile(_stable_compounder())
    v = RE.combine(_risk(), checks, {"exposure": "high", "rationale": "r"})
    assert v["verdict"] == "ELEVATED"


def test_ladder_low_overrides_quant_flags():
    checks = _checks_for_profile(_nobel_like())
    v = RE.combine(_risk(), checks, {"exposure": "low",
                                     "rationale": "niche protected",
                                     "mitigant": "niche/scale protection"})
    assert v["verdict"] == "LOW"


def test_ladder_numbers_alone_cap_at_quant_flag():
    checks = _checks_for_profile(_nobel_like())
    v = RE.combine(_risk(), checks, None)
    assert v["verdict"] == "QUANT FLAG"


def test_ladder_not_assessed_when_no_evidence():
    empty = {k: {"flagged": None, "value": None, "explanation": "no data"}
             for k in _checks_for_profile(_stable_compounder())}
    v = RE.combine(_risk(), empty, None)
    assert v["verdict"] == "NOT ASSESSED"


def test_no_transcript_never_claims_no_signal():
    """Clean numbers WITHOUT a judge must stay NOT ASSESSED — silence that
    was never examined is not safety (the ITC-with-no-concalls case)."""
    checks = _checks_for_profile(_stable_compounder())
    rec = RE.analyse("NOCALLSCO", checks, qual_by_risk=None)
    assert rec["judged"] is False
    assert all(v["verdict"] in ("NOT ASSESSED", "QUANT FLAG")
               for v in rec["verdicts"])
    # ...while the same numbers WITH a silent judge honestly say NO SIGNAL
    rec2 = RE.analyse("CALLSCO", checks, qual_by_risk={})
    assert any(v["verdict"] == "NO SIGNAL" for v in rec2["verdicts"])


# ------------------------------------------------------------ explainability
def test_every_verdict_carries_evidence():
    checks = _checks_for_profile(_nobel_like())
    rec = RE.analyse("NOBELCO", checks,
                     {"GOOD_ENOUGH": {"exposure": "high",
                                      "rationale": "challengers sell cheaper",
                                      "quote": "price competition intensified"}})
    for v in rec["verdicts"]:
        assert "quant" in v and "evidence" in v["quant"]
        assert "qual" in v and "rationale" in v["qual"]
    ge = next(v for v in rec["verdicts"] if v["risk"] == "GOOD_ENOUGH")
    assert ge["verdict"] == "HIGH RISK"
    assert ge["qual"]["quote"] == "price competition intensified"
    assert any(e["status"] == "flags the risk" for e in ge["quant"]["evidence"])


def test_report_renders_human_readably():
    sys.path.insert(0, str(HERE.parent / "scripts"))
    import analyze as AZ
    checks = _checks_for_profile(_nobel_like())
    rec = RE.analyse("NOBELCO", checks)
    md = AZ.render_report(rec, "Nobel-like Test Co")
    assert md.startswith("# Nobel-like Test Co")
    assert "Financial resilience" in md
    assert "not investment advice" in md
    import re
    body = re.sub(r"^> .*$", "", md, flags=re.M)
    for banned in ["opm", "gm ", "cfo", "roce", "_erosion", "_swings",
                   "QUANT FLAG_", "1 days", "yoy", "std"]:
        assert banned not in body, f"jargon leaked into report: {banned}"


# ------------------------------------------------------------ real data
def test_real_data_integration():
    data = QE.INDIA / "ProfitStatement" / "NiftyTotalMarket" / "_all_profit_loss_long.csv"
    if not data.exists():
        import pytest
        pytest.skip("dataset not present")
    checks = QE.compute_checks("TATASTEEL")
    assert checks["margin_swings"]["flagged"] is not None
    rec = RE.analyse("TATASTEEL", checks)
    assert len(rec["verdicts"]) == 8
    assert rec["fragility"]["tested"] >= 2
