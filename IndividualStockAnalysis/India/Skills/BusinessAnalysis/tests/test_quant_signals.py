"""End-to-end test of the quantitative engine against a bundled fixture universe.

Uses tests/fixtures/universe as the data base so it runs anywhere, with or
without the full repo dataset present.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))
import quant_signals as Q  # noqa: E402

FIXTURE_BASE = HERE / "fixtures" / "universe"


def _compute():
    return Q.compute("TESTCO", base=FIXTURE_BASE, universe="TestUniverse")


def test_returns_all_expected_quant_params():
    res = _compute()
    # every quantitative-touching parameter id must be present in the output
    for pid in ["ROC.headline", "ROC.asset_turn", "ROC.profit_margin",
                "CAP.working_capital_cost", "CAP.growth_capex",
                "CAP.shareholder_distribution", "GRW.persistence",
                "GRW.pricing_mix_volume", "IND.barriers_entry_rationality",
                "CUS.intangible_benefits"]:
        assert pid in res, f"{pid} missing from quant output"


def test_asset_turn_value():
    res = _compute()
    # Sales 1150 / Total Assets 1300 = 0.8846
    assert abs(res["ROC.asset_turn"]["value"] - 1150 / 1300) < 1e-6
    assert res["ROC.asset_turn"]["data_available"]


def test_croci_proxy():
    res = _compute()
    # CFO 240 / (100+700+200)=1000 -> 0.24
    croci = res["ROC.headline"]["value"]["croci_proxy"]
    assert abs(croci - 0.24) < 1e-6


def test_profit_margin_stability():
    res = _compute()
    v = res["ROC.profit_margin"]["value"]
    assert v["opm_latest"] == 23
    assert v["gross_margin_proxy_latest"] == 60  # 100 - 40
    assert v["opm_std"] is not None and v["opm_std"] < 2  # very stable margins


def test_working_capital_negative_ccc():
    res = _compute()
    v = res["CAP.working_capital_cost"]["value"]
    assert v["ccc_latest"] == -8
    # 3y change = FY26 (-8) minus 3-years-back FY23 (10) = -18 (a big improvement)
    assert v["ccc_3y_change"] == -8 - 10


def test_persistence_band():
    res = _compute()
    v = res["GRW.persistence"]["value"]
    # sales 800->1150 over 3 yrs -> ~12.8% CAGR, inside 10-15% band
    assert v["in_10_15_band"] is True


def test_buyback_detected():
    res = _compute()
    v = res["CAP.shareholder_distribution"]["value"]
    assert v["buyback_indicated"] is True   # Proceeds from shares = -20


def test_unavailable_params_flagged():
    res = _compute()
    for pid in ["CAP.advertising_promotion", "CAP.research_development",
                "MOAT.technology", "GRW.market_share_gain"]:
        assert res[pid]["data_available"] is False


def test_missing_company_is_graceful():
    res = Q.compute("NOSUCHCO", base=FIXTURE_BASE, universe="TestUniverse")
    # should not raise; signals simply unavailable
    assert res["ROC.asset_turn"]["data_available"] is False
