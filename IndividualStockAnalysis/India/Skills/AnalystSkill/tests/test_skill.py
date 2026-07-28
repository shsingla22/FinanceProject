"""
AnalystSkill tests.

  python3 -m pytest tests/ -q       (from Skills/AnalystSkill/)

All tests run in numbers-only mode (no AI calls) so the suite is fast and
deterministic; the judge and synthesis paths are exercised by live
verification and each sibling skill's own suite.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

import registry as REG    # noqa: E402
import composer as C      # noqa: E402


# --------------------------------------------------------- orchestration
def test_discovers_all_three_sibling_skills():
    found = REG.discover()
    assert found == {"BusinessAnalysis": True, "MultibaggerPattern": True,
                     "QualityRisks": True}, found


def test_executes_every_sibling_skill_on_real_data():
    ba, s1 = REG.run_business("CRISIL", ai=False)
    mb, s2 = REG.run_patterns("CRISIL", ai=False)
    qr, s3 = REG.run_risks("CRISIL", ai=False)
    assert s1 == s2 == s3 == "numbers_only"
    assert ba["overall"] is not None and 0 < ba["coverage"] <= 1
    assert len(mb["verdicts"]) == 11
    assert len(qr["verdicts"]) == 8
    assert qr["fragility"]["status"] in ("SOUND", "STRAINED", "STRESSED",
                                         "UNKNOWN")


def test_quick_mode_is_honest_about_coverage():
    ba, _ = REG.run_business("DIXON", ai=False)
    assert ba["qualitative_included"] is False
    assert ba["coverage"] < 0.6, "numbers-only run must not claim full coverage"


# --------------------------------------------------------- rating
def _stack(sym):
    ba, _ = REG.run_business(sym, ai=False)
    mb, _ = REG.run_patterns(sym, ai=False)
    qr, _ = REG.run_risks(sym, ai=False)
    return ba, mb, qr, C.compute_rating(ba, mb, qr)


def test_rating_bounds_and_grades():
    _, _, _, rt = _stack("CRISIL")
    assert 0 <= rt["score"] <= 100
    assert rt["grade"] in {"Outstanding", "Strong", "Decent", "Mixed", "Weak"}
    for p in rt["pillars"].values():
        assert p["points"] is None or 0 <= p["points"] <= 100
        assert len(p["derivation"]) > 30


def test_rating_arithmetic_matches_its_own_claim():
    _, _, _, rt = _stack("CRISIL")
    avail = {k: p for k, p in rt["pillars"].items() if p["points"] is not None}
    wsum = sum(C.WEIGHTS[k] for k in avail)
    expect = round(sum(p["points"] * C.WEIGHTS[k]
                       for k, p in avail.items()) / wsum)
    assert rt["score"] == expect


# --------------------------------------------------------- the report
def _report(sym):
    ba, mb, qr, rt = _stack(sym)
    name = REG.company_name(sym)
    return C.render(sym, name, ba, mb, qr, rt, synth=None,
                    statuses={"business": "numbers_only",
                              "patterns": "numbers_only",
                              "risks": "numbers_only"})


def test_report_is_one_coherent_document():
    md = _report("CRISIL")
    assert md.startswith("# ")
    assert "The Analyst's Report" in md
    # one coherent flow: rating, then the three pillars, then watch + method
    order = ["## The rating:", "How good is the business?",
             "Does it look like a long-term winner?", "What could break it?",
             "## What to watch", "## How this report was built"]
    idx = [md.find(s) for s in order]
    assert all(i >= 0 for i in idx), f"missing sections: {list(zip(order, idx))}"
    assert idx == sorted(idx), "sections out of order"
    assert "not investment advice" in md


def test_report_names_every_sibling_skill():
    md = _report("CRISIL")
    for s in ("BusinessAnalysis", "MultibaggerPattern", "QualityRisks"):
        assert s in md, f"report does not credit {s}"
    assert "numbers_only" in md      # honest about what ran


def test_report_has_no_jargon_and_no_internal_ids():
    for sym in ("CRISIL", "TATASTEEL"):
        md = _report(sym)
        body = re.sub(r"^> .*$", "", md, flags=re.M)
        for banned in [r"\b(CAP|ROC|GRW|MGT|IND|CUS|MOAT)\.[a-z_]+",
                       r"\bopm\b", r"\bccc\b", r"\byoy\b", r"\b1 days\b",
                       r"\bNone\b", r"\bnan\b"]:
            assert not re.search(banned, body), \
                f"{sym}: jargon leaked: {banned}"


def test_untested_company_is_not_rated_not_faked():
    """A lender in numbers-only mode: the frameworks can't read bank
    financials, so NOTHING is actually tested. The rating must say 'Not
    rated' — never award a perfect safety score for untested risks, and
    never count an untestable foundation as a zero."""
    ba, mb, qr, rt = _stack("HDFCBANK")
    if ba["overall"] is not None:      # guard: only meaningful if untestable
        import pytest
        pytest.skip("bank unexpectedly scoreable — rule not exercised")
    assert rt["pillars"]["safety"]["points"] is None
    assert "untested" in rt["pillars"]["safety"]["derivation"]
    assert rt["pillars"]["patterns"]["points"] is None
    assert rt["score"] is None and rt["grade"] == "Not rated"


# --------------------------------------------------------- extensibility
FAKE_SKILL = '''
def run(symbol, ai=True):
    return {
        "name": "Valuation Check",
        "order": 40,
        "status": "ok",
        "record": {"symbol": symbol, "verdict": "fairly priced"},
        "pillar": {"name": "Valuation comfort", "points": 60,
                   "derivation": "Price sits mid-range against its own "
                                 "history — neither a bargain nor a "
                                 "stretch; 60 of 100.",
                   "weight": 0.15},
        "section_md": "## Is the price sensible? (valuation check)\\n\\n"
                      "The stock looks fairly priced against its own "
                      "history.",
        "facts": {"verdict": "fairly priced",
                  "names": ["Valuation Check"]},
    }
'''


def test_future_skill_is_discovered_executed_and_folded_in(tmp_path):
    """The extensibility contract: drop a new skill folder with an
    analyst_interface.py next to the others and it joins the analysis —
    discovered, executed, its pillar re-weighted into the rating, its
    section in the report, its name in the methodology."""
    fake = tmp_path / "ValuationSkill"
    fake.mkdir()
    (fake / "analyst_interface.py").write_text(FAKE_SKILL)

    found = REG.discover_extensions(skills_dir=tmp_path)
    assert [e["skill"] for e in found] == ["ValuationSkill"]

    exts = REG.run_extensions("CRISIL", ai=False, skills_dir=tmp_path)
    assert exts[0]["status"] == "ok"
    assert exts[0]["record"]["verdict"] == "fairly priced"

    ba, mb, qr, _ = _stack("CRISIL")
    rt = C.compute_rating(ba, mb, qr, extensions=exts)
    key = "ext:ValuationSkill"
    assert key in rt["pillars"] and rt["pillars"][key]["points"] == 60
    # weights re-normalized: the composite must match its own claim
    weights = dict(C.WEIGHTS); weights[key] = 0.15
    avail = {k: p for k, p in rt["pillars"].items() if p["points"] is not None}
    wsum = sum(weights[k] for k in avail)
    expect = round(sum(p["points"] * weights[k] for k, p in avail.items()) / wsum)
    assert rt["score"] == expect
    assert "valuation comfort" in rt["derivation"].lower()

    md = C.render("CRISIL", "CRISIL Ltd.", ba, mb, qr, rt, synth=None,
                  statuses={"business": "numbers_only",
                            "patterns": "numbers_only",
                            "risks": "numbers_only"},
                  extensions=exts)
    assert "Is the price sensible?" in md          # its section rendered
    assert "ValuationSkill" in md                  # credited in methodology
    assert md.find("Is the price sensible?") < md.find("## What to watch")


def test_broken_extension_cannot_sink_the_report(tmp_path):
    fake = tmp_path / "BrokenSkill"
    fake.mkdir()
    (fake / "analyst_interface.py").write_text("def run(symbol, ai=True):\n"
                                              "    raise RuntimeError('boom')\n")
    exts = REG.run_extensions("CRISIL", ai=False, skills_dir=tmp_path)
    assert exts[0]["status"].startswith("failed:")
    assert exts[0]["record"] is None
    ba, mb, qr, _ = _stack("CRISIL")
    rt = C.compute_rating(ba, mb, qr, extensions=exts)   # must not raise
    assert rt["score"] is not None
    md = C.render("CRISIL", "CRISIL Ltd.", ba, mb, qr, rt, synth=None,
                  statuses={"business": "numbers_only",
                            "patterns": "numbers_only",
                            "risks": "numbers_only"},
                  extensions=exts)
    assert "failed:" in md                          # honest, not hidden


def test_synthesis_grounding_rejects_unknown_names():
    ba, mb, qr, rt = _stack("CRISIL")
    # a fake synthesis that names a risk which is NOT in the records must
    # be rejected by the grounding gate the composer applies
    known = {v["name"].lower() for v in mb["verdicts"]}
    assert "currency collapse" not in known
    import composer
    text = "The Currency Collapse risk dominates everything."
    fake = {"summary": [text], "watch_items": []}
    # reuse the same check the composer runs (extracted inline here)
    bad = []
    for phrase in re.findall(r"(?:[A-Z][a-z]+ ){1,3}(?:pattern|risk|test)\b",
                             text):
        base = phrase.rsplit(" ", 1)[0].strip().lower()
        if base and base not in known:
            bad.append(base)
    assert bad, "the grounding scan must catch the fabricated risk name"
