"""
RecentAnalystSkill tests.

  python3 -m pytest tests/ -q       (from Skills/RecentAnalystSkill/)

The skill IS the AnalystSkill behind a one-year lens, so the tests focus
on the lens itself: the window is really applied to every data source,
the caches are really separate, the explanations really say when the
window (not the data) is the reason a check is silent, and the composed
report carries the lens banner while keeping the full analyst structure.
All tests run numbers-only (no AI calls).
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

import window as W      # noqa: E402  (applies the lens at import)

AR, AC = W.AR, W.AC


# --------------------------------------------------------------- the window
def test_statement_frames_are_windowed_to_two_years():
    g = AR.MB_QE.gather("DIXON")
    assert 0 < len(g["sales"]) <= W.WINDOW_YEARS, g["sales"]
    assert 0 < len(g["opm"]) <= W.WINDOW_YEARS
    gq = AR.QR_QE.gather("DIXON")
    assert 0 < len(gq["roce"]) <= W.WINDOW_YEARS
    tr = AR.trend_series("DIXON")
    assert all(len(v["values"]) <= W.WINDOW_YEARS for v in tr.values())


def test_business_framework_sees_only_the_window():
    sig = AR.Q.compute("DIXON", base=AR.INDIA, universe="NiftyTotalMarket")
    gp = sig.get("GRW.persistence", {})
    series = (gp.get("evidence") or {}).get("sales_series") or []
    assert len(series) <= W.WINDOW_YEARS, \
        f"BusinessAnalysis saw {len(series)} years through the lens"


def test_concall_timeline_is_last_twelve_months_only():
    ex, n, rng = AR.MB_AZ._timeline_excerpt("DIXON")
    assert 0 < n <= W.WINDOW_CALLS
    assert "last 12 months" in rng or "recent" in rng
    assert AR.QR_AZ._timeline_excerpt is AR.MB_AZ._timeline_excerpt


def test_judge_prompts_carry_the_lens_instruction():
    tax = AR.MB_PE.load_taxonomy()
    p = AR.MB_AZ._qual_prompt("DIXON", tax)
    assert p is not None and p.startswith("IMPORTANT — ONE-YEAR LENS")
    p2 = AR.QR_AZ._qual_prompt("DIXON", AR.QR_RE.load_taxonomy())
    assert p2 is not None and p2.startswith("IMPORTANT — ONE-YEAR LENS")
    p3 = AR._ba_qual_prompt("DIXON")
    assert p3 is not None and p3.startswith("IMPORTANT — ONE-YEAR LENS")


def test_caches_are_separate_from_the_full_history_skill():
    recent = HERE.parent
    for p in (AR.BA_CACHE, AR.MB_AZ.CACHE, AR.QR_AZ.CACHE,
              AC.SYNTH_CACHE, AC.OVERVIEW_CACHE):
        assert Path(p).parent == recent, \
            f"cache would collide with the full-history skill: {p}"


# --------------------------------------------------- honest explanations
def test_unassessable_trend_checks_blame_the_lens_not_the_data():
    checks = AR.MB_QE.compute_checks("DIXON")
    silent = [c for c in checks.values() if c["passed"] is None]
    assert silent, "expected some trend checks to be unassessable in-window"
    assert any("One-year lens" in c["explanation"] for c in silent)
    rchecks = AR.QR_QE.compute_checks("DIXON")
    rsilent = [c for c in rchecks.values() if c["flagged"] is None]
    assert any("One-year lens" in c["explanation"] for c in rsilent)


def test_level_checks_still_work_inside_the_window():
    checks = AR.MB_QE.compute_checks("DIXON")
    # level-based checks need only the latest year — must still assess
    assert checks["low_capex_intensity"]["passed"] is not None
    assert checks["negative_working_capital"]["passed"] is not None


# --------------------------------------------------------------- the record
def _stack(sym):
    ba, _ = AR.run_business(sym, ai=False)
    mb, _ = AR.run_patterns(sym, ai=False)
    qr, _ = AR.run_risks(sym, ai=False)
    return ba, mb, qr, AC.compute_rating(ba, mb, qr)


def test_record_shape_is_identical_to_the_analyst_skill():
    ba, mb, qr, rt = _stack("DIXON")
    assert len(mb["verdicts"]) == 11
    assert len(qr["verdicts"]) == 8
    assert rt["grade"] in {"Outstanding", "Strong", "Decent", "Mixed",
                           "Weak", "Not rated"}
    for v in mb["verdicts"] + qr["verdicts"]:
        assert len(v.get("derivation", "")) > 15      # explainability intact


def test_report_carries_the_lens_and_the_full_structure():
    ba, mb, qr, rt = _stack("DIXON")
    meta = AR.company_meta("DIXON")
    md = AC.render("DIXON", meta["name"], ba, mb, qr, rt, synth=None,
                   statuses={"business": "numbers_only",
                             "patterns": "numbers_only",
                             "risks": "numbers_only"},
                   trends=AR.trend_series("DIXON"),
                   industry=meta["industry"])
    assert "The Analyst's Report · Last One Year" in md.splitlines()[0]
    assert "The one-year lens:" in md
    assert "RESTRICTED TO THE LAST ONE YEAR" in md
    for s in ["## About the business", "## The verdict:",
              "## Section 1 — How good is the business?",
              "## Section 2 — Does it look like a long-term winner?",
              "## Section 3 — What could break it?",
              "## What to watch", "## How this report was built"]:
        assert s in md, f"missing section: {s}"
    body = re.sub(r"^> .*$", "", md, flags=re.M)
    for banned in [r"\b(CAP|ROC|GRW|MGT|IND|CUS|MOAT)\.[a-z_]+",
                   r"\b1 days\b", r"\bnan\b"]:
        assert not re.search(banned, body), banned


def test_windowed_verdicts_differ_from_what_full_history_would_say():
    """The lens must actually change the picture: Dixon's full-history
    sales CAGR check passes easily, but a two-point window cannot compute
    a multi-year CAGR at all — the foundation gate must reflect that."""
    checks = AR.MB_QE.compute_checks("DIXON")
    assert checks["core_growth"]["passed"] is None, \
        "a one-year window must not claim a multi-year growth verdict"
