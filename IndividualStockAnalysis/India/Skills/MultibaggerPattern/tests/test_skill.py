"""
MultibaggerPattern skill tests.

  python3 -m pytest tests/ -q     (from Skills/MultibaggerPattern/)

Covers: taxonomy completeness (no pattern missed), the verdict combiner's
ladder, quant checks on synthetic profiles shaped like the document's
examples (a KONE-like recurring business, a Hermès-like pricing-power
business, a Costco-like low-price business, a deteriorating counterexample),
explainability contract (every verdict carries evidence), and a real-data
integration pass when the repository dataset is present.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

import pattern_engine as PE   # noqa: E402
import quant_evidence as QE   # noqa: E402


# ------------------------------------------------------------ completeness
def test_taxonomy_valid_and_complete():
    problems = PE.validate()
    assert problems == [], "taxonomy problems:\n" + "\n".join(problems)


def test_all_eleven_patterns_present():
    tax = PE.load_taxonomy()
    assert len(tax["patterns"]) == 11
    ids = {p["id"] for p in tax["patterns"]}
    assert ids == {"RECURRING", "MIDDLEMAN", "TOLLROAD", "LOWPRICE", "PRICING",
                   "BRAND", "INNOVATION", "FORWARD", "SHAREGAIN", "CULTURE",
                   "MOATTEST"}


def test_every_quant_check_id_is_implemented():
    """Every check declared in the checklist must be produced by the engine."""
    import yaml
    chk = yaml.safe_load((HERE.parent / "reference" / "checklist.yaml").read_text())
    produced = _checks_for_profile(_kone_like())
    for cid in chk["expected_core_checks"] + chk["expected_quant_checks"]:
        assert cid in produced, f"quant check not implemented: {cid}"


# ------------------------------------------------------------ synthetic profiles
def _profile_to_checks(g):
    """Run compute_checks against a synthetic gather() dict by monkeypatching."""
    orig = QE.gather
    QE.gather = lambda sym, base=None, universe=None: g
    try:
        return QE.compute_checks("TEST")
    finally:
        QE.gather = orig


def _checks_for_profile(g):
    return _profile_to_checks(g)


def _kone_like():
    """Recurring-revenue elevator-services profile: negative working capital,
    tiny capex, rock-steady cash, high stable margins."""
    return {
        "sales": [800, 880, 960, 1050, 1160, 1280, 1400, 1550, 1700, 1870],
        "opm": [22, 22, 23, 23, 24, 24, 24, 25, 25, 25],
        "gm": [55, 55, 56, 56, 57, 57, 57, 58, 58, 58],
        "op": [176, 194, 221, 242, 278, 307, 336, 388, 425, 468],
        "cfo": [180, 200, 225, 250, 285, 315, 345, 395, 430, 475],
        "capex": [-20, -22, -24, -26, -28, -31, -34, -37, -41, -45],
        "wcd": [-30, -32, -33, -35, -36, -38, -39, -40, -42, -43],
        "ccc": [-25, -26, -28, -29, -30, -32, -33, -35, -36, -38],
        "roce": [35, 36, 36, 37, 38, 38, 39, 40, 40, 41],
        "advances": [100, 115, 130, 150, 170, 195, 220, 250, 285, 320],
        "total_assets": [900, 980, 1060, 1150, 1260, 1380, 1500, 1650, 1800, 1980],
    }


def _hermes_like():
    """Pricing power: very high & rising gross margin, rising operating margin."""
    g = _kone_like()
    g["gm"] = [62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    g["opm"] = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    return g


def _costco_like():
    """Low Price Plus: thin gross margin, huge asset turns, decent returns."""
    g = _kone_like()
    g["gm"] = [14, 14, 14, 15, 15, 15, 15, 15, 15, 15]
    g["opm"] = [4, 4, 4, 4, 4, 4, 5, 5, 5, 5]
    g["sales"] = [5000, 5600, 6300, 7100, 8000, 9000, 10100, 11300, 12700, 14200]
    g["total_assets"] = [3000, 3300, 3600, 4000, 4400, 4800, 5300, 5800, 6400, 7000]
    g["roce"] = [16, 16, 17, 17, 18, 18, 18, 19, 19, 20]
    return g


def _deteriorating():
    """Counterexample: growth bought with collapsing margins, weak cash."""
    return {
        "sales": [500, 600, 720, 870, 1050, 1260, 1520, 1830, 2200, 2650],
        "opm": [18, 17, 15, 13, 12, 10, 9, 8, 7, 6],
        "gm": [30, 29, 28, 26, 25, 24, 23, 22, 21, 20],
        "op": [90, 100, 108, 113, 126, 126, 137, 146, 154, 159],
        "cfo": [40, -10, 55, -20, 60, 30, -15, 70, 20, -5],
        "capex": [-80, -100, -130, -160, -200, -250, -310, -380, -460, -560],
        "wcd": [60, 65, 70, 75, 80, 88, 95, 105, 115, 125],
        "ccc": [70, 75, 82, 90, 98, 108, 118, 130, 142, 155],
        "roce": [12, 11, 10, 9, 9, 8, 8, 7, 7, 6],
        "advances": [],
        "total_assets": [600, 750, 940, 1170, 1460, 1820, 2270, 2830, 3530, 4400],
    }


def test_recurring_profile_detected():
    checks = _checks_for_profile(_kone_like())
    assert checks["negative_working_capital"]["passed"] is True
    assert checks["low_capex_intensity"]["passed"] is True
    assert checks["cash_conversion_strength"]["passed"] is True
    assert checks["core_cash_generation"]["passed"] is True
    rec = PE.analyse("KONELIKE", checks)
    assert rec["core_gate"]["status"] == "PASS"
    assert "RECURRING" in rec["matched_patterns"]   # QUANT SIGNAL


def test_pricing_power_profile_detected():
    checks = _checks_for_profile(_hermes_like())
    assert checks["high_gross_margin"]["passed"] is True
    assert checks["rising_margins"]["passed"] is True
    rec = PE.analyse("HERMESLIKE", checks)
    assert "PRICING" in rec["matched_patterns"]


def test_lowprice_profile_detected():
    checks = _checks_for_profile(_costco_like())
    assert checks["lowprice_economics"]["passed"] is True, \
        checks["lowprice_economics"]["explanation"]
    rec = PE.analyse("COSTCOLIKE", checks)
    assert "LOWPRICE" in rec["matched_patterns"]


def test_deteriorating_profile_rejected():
    checks = _checks_for_profile(_deteriorating())
    rec = PE.analyse("BADCO", checks)
    assert rec["core_gate"]["status"] in ("FAIL", "PARTIAL")
    assert rec["matched_patterns"] == [], \
        f"deteriorating company matched: {rec['matched_patterns']}"
    # margin erosion must be called out in the evidence
    assert "ERODING" in checks["rising_margins"]["explanation"]


# ------------------------------------------------------------ verdict ladder
def _pat(pid="PRICING"):
    tax = PE.load_taxonomy()
    return next(p for p in tax["patterns"] if p["id"] == pid)


def test_combiner_strong_fit():
    checks = _checks_for_profile(_hermes_like())
    v = PE.combine(_pat(), checks, {"fit": "strong", "rationale": "r", "quote": "q"})
    assert v["verdict"] == "STRONG FIT"


def test_combiner_quant_signal_without_qual():
    checks = _checks_for_profile(_hermes_like())
    v = PE.combine(_pat(), checks, None)
    assert v["verdict"] == "QUANT SIGNAL"


def test_combiner_qual_none_wins_over_quant():
    checks = _checks_for_profile(_hermes_like())
    v = PE.combine(_pat(), checks, {"fit": "none", "rationale": "contradicts"})
    assert v["verdict"] == "NO FIT"


def test_combiner_not_assessed():
    empty = {k: {"passed": None, "value": None, "explanation": "no data"}
             for k in _checks_for_profile(_kone_like())}
    v = PE.combine(_pat(), empty, None)
    assert v["verdict"] == "NOT ASSESSED"


# ------------------------------------------------------------ explainability
def test_every_verdict_explains_its_own_ladder_position():
    """Every combiner outcome must state WHY the ladder landed there."""
    strong_checks = _checks_for_profile(_hermes_like())
    weak = {k: {"passed": None, "value": None, "explanation": "no data"}
            for k in strong_checks}
    cases = [
        (strong_checks, {"fit": "strong", "rationale": "r"}, "STRONG FIT"),
        (strong_checks, {"fit": "partial", "rationale": "r"}, "LIKELY FIT"),
        (strong_checks, {"fit": "none", "rationale": "r"}, "NO FIT"),
        (strong_checks, None, "QUANT SIGNAL"),
        (weak, None, "NOT ASSESSED"),
    ]
    for checks, qual, expected in cases:
        v = PE.combine(_pat(), checks, qual)
        assert v["verdict"] == expected, (expected, v["verdict"])
        assert len(v.get("derivation", "")) > 20, f"no derivation: {expected}"


def test_every_verdict_carries_evidence():
    checks = _checks_for_profile(_kone_like())
    rec = PE.analyse("KONELIKE", checks,
                     {"RECURRING": {"fit": "strong",
                                    "rationale": "90% attach rate discussed",
                                    "quote": "attach rate is around 90%"}})
    for v in rec["verdicts"]:
        assert "quant" in v and "evidence" in v["quant"]
        assert "qual" in v and "rationale" in v["qual"]
    rc = next(v for v in rec["verdicts"] if v["pattern"] == "RECURRING")
    assert rc["verdict"] == "STRONG FIT"
    assert rc["qual"]["quote"] == "attach rate is around 90%"
    assert any(e["status"] == "supports" for e in rc["quant"]["evidence"])


def test_report_renders_human_readably():
    sys.path.insert(0, str(HERE.parent / "scripts"))
    import analyze as AZ
    checks = _checks_for_profile(_kone_like())
    rec = PE.analyse("KONELIKE", checks)
    md = AZ.render_report(rec, "Kone-like Test Co")
    assert md.startswith("# Kone-like Test Co")
    assert "Foundation test" in md
    assert "not investment advice" in md
    import re
    body = re.sub(r"^> .*$", "", md, flags=re.M)
    for banned in ["QUANT SIGNAL_", "core_cash", "wcd", "ccc", "opm",
                   "_economics", "capex_to_sales"]:
        assert banned not in body, f"jargon leaked into report: {banned}"


# ------------------------------------------------------------ real data
def test_real_data_integration():
    """Runs only when the repository dataset is present (it is on main)."""
    data = QE.INDIA / "ProfitStatement" / "NiftyTotalMarket" / "_all_profit_loss_long.csv"
    if not data.exists():
        import pytest
        pytest.skip("dataset not present")
    checks = QE.compute_checks("NAUKRI")
    assert checks["core_cash_generation"]["passed"] is not None
    rec = PE.analyse("NAUKRI", checks)
    assert rec["core_gate"]["of"] >= 2
    assert len(rec["verdicts"]) == 11
