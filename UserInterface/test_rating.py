"""
Tests for the unified 3-pillar rating (rating.py) and the extended report.

  python3 -m pytest test_rating.py -q          (from UserInterface/)

Everything here runs in numbers-only mode (no AI calls) so the suite is
fast and deterministic; the judge paths are exercised by the skills' own
test suites and by live verification.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "IndividualStockAnalysis" / "India"
                       / "Skills" / "BusinessAnalysis" / "scripts"))

import rating as R                    # noqa: E402


def _full_stack(sym: str):
    import server as SV
    rec = SV.build_record(sym, SV._live_map(), SV._cc_counts())
    mb, _ = R.patterns_analysis(sym, ai=False)
    qr, _ = R.risks_analysis(sym, ai=False)
    return rec, mb, qr, R.compute_rating(sym, rec, mb, qr)


def test_rating_structure_and_bounds():
    rec, mb, qr, rt = _full_stack("CRISIL")
    assert rt["score"] is not None and 0 <= rt["score"] <= 100
    assert rt["grade"] in {"Outstanding", "Strong", "Decent", "Mixed", "Weak"}
    assert 1 <= rt["stars"] <= 5
    for key in ("quality", "patterns", "safety"):
        p = rt["pillars"][key]
        assert p["points"] is None or 0 <= p["points"] <= 100
        assert len(p["derivation"]) > 30, f"pillar {key} lacks a derivation"
    assert "out of 100" in rt["derivation"]


def test_rating_arithmetic_is_what_it_claims():
    _, _, _, rt = _full_stack("CRISIL")
    avail = {k: p for k, p in rt["pillars"].items() if p["points"] is not None}
    wsum = sum(R.WEIGHTS[k] for k in avail)
    expect = round(sum(p["points"] * R.WEIGHTS[k] for k, p in avail.items())
                   / wsum)
    assert rt["score"] == expect


def test_riskier_company_scores_lower_on_safety():
    _, _, qr_safe, rt_safe = _full_stack("PIDILITIND")
    _, _, qr_risky, rt_risky = _full_stack("RTNPOWER")
    assert rt_safe["pillars"]["safety"]["points"] >= \
        rt_risky["pillars"]["safety"]["points"]


def test_pillar_derivations_use_plain_language():
    for sym in ("CRISIL", "TATASTEEL", "DIXON"):
        _, _, _, rt = _full_stack(sym)
        text = rt["derivation"] + " ".join(
            p["derivation"] for p in rt["pillars"].values())
        for banned in ["QUANT FLAG", "QUANT SIGNAL", "opm", "roce", "cfo",
                       "gate_pts", "frag", "None", "nan"]:
            assert banned not in text, f"{sym}: jargon leaked: {banned}"


def test_report_covers_all_three_skills_and_rating():
    import server as SV
    md = SV.render_report_md("CRISIL", quick=True)
    assert "Complete Company Analysis" in md
    assert "## The rating:" in md
    assert "How it was built:" in md
    assert "Which winning patterns does it fit?" in md
    assert "What could go wrong? (the risk check)" in md
    assert "not investment advice" in md
    # skill sub-reports must be demoted below the top-level sections
    assert "\n# CRISIL" not in md.split("\n", 1)[1]
    # every pattern/risk section carries its "why"
    assert md.count("Why this verdict:") >= 5 or "numbers only" in md.lower()


def test_patterns_and_risks_records_carry_derivations():
    _, mb, qr, _ = _full_stack("TATASTEEL")
    for v in mb["verdicts"]:
        assert len(v.get("derivation", "")) > 15
    for v in qr["verdicts"]:
        assert len(v.get("derivation", "")) > 15
    assert len(qr["fragility"].get("derivation", "")) > 15
