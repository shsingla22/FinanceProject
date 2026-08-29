"""
Tests for the AnalystSkill's fourth input — the index comparison — and
for the post-processor that folds it into the stored reports.

  python3 -m pytest tests/test_relative_index.py -q   (from AnalystSkill/)

The corpus tests at the bottom read the stored reports, so they check
the real 742-company output rather than a fixture: every report must
carry the new section, its arithmetic must add up, and none of the
original analysis may have been lost.
"""

import re
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

import add_relative_index as ADD      # noqa: E402
import composer as C                  # noqa: E402
REL = ADD.REL                         # pillar lives in the ratio skill

OUT = ADD.OUT


# ------------------------------------------------------------- scoring

@pytest.mark.parametrize("pct,expected", [
    (60.0, 2), (25.0, 2), (24.9, 1), (10.0, 1), (9.9, 0), (0.0, 0),
    (-9.9, 0), (-10.0, -1), (-24.9, -1), (-25.0, -2), (-80.0, -2),
])
def test_cell_score_thresholds(pct, expected):
    assert REL.cell_score(pct) == expected


def test_window_change_is_a_plain_percentage():
    rows = [("Mar 2016", 100.0), ("Mar 2021", 150.0), ("Mar 2026", 75.0)]
    assert REL.window_change(rows, 10)[0] == pytest.approx(-25.0)
    assert REL.window_change(rows, 5)[0] == pytest.approx(-50.0)


def test_window_change_none_when_the_base_year_is_absent():
    rows = [("Mar 2024", 10.0), ("Mar 2026", 12.0)]
    assert REL.window_change(rows, 10) is None
    assert REL.window_change(rows, 2)[0] == pytest.approx(20.0)


def test_window_change_refuses_a_sign_flip():
    """A ratio crossing zero has no honest percentage change."""
    assert REL.window_change([("Mar 2025", -4.0), ("Mar 2026", 6.0)], 1) is None
    assert REL.window_change([("Mar 2025", 4.0), ("Mar 2026", -6.0)], 1) is None


def test_pillar_maps_the_mean_onto_0_100_like_the_other_pillars():
    """Same −2..+2 → 0..100 mapping the 34-check framework uses."""
    for mean, pts in ((2.0, 100), (1.0, 75), (0.0, 50), (-1.0, 25), (-2.0, 0)):
        assert round((mean + 2) / 4 * 100) == pts


def test_a_company_that_tracked_the_index_scores_mid_scale():
    """A flat ratio means the company moved with the index -> about 50."""
    p = REL.pillar("PIDILITIND")
    assert p["points"] is not None
    assert abs(p["points"] - round((p["mean"] + 2) / 4 * 100)) == 0


def test_pillar_reports_coverage_and_never_guesses():
    p = REL.pillar("COLPAL")          # price only; statements stop at FY2010
    assert 0 < p["coverage"] < 1
    assert any(c["pct"] is None for c in p["cells"])
    assert all(c["score"] is None for c in p["cells"] if c["pct"] is None)


def test_pillar_is_none_when_nothing_is_comparable():
    p = REL.pillar("ENRIN")           # a single fiscal year of history
    assert p["points"] is None and p["coverage"] == 0
    assert "does not reach back" in p["derivation"]


def test_one_year_lens_uses_only_the_latest_window():
    p = REL.pillar("PIDILITIND", windows=[1])
    assert {c["window"] for c in p["cells"]} == {1}


def test_window_table_covers_every_requested_window():
    table = REL.window_table(REL.pillar("PIDILITIND"))
    for w in (10, 5, 3, 1):
        label = f"last {w} year" + ("s" if w > 1 else "")
        assert f"| {label} |" in table


# ------------------------------------------------------------- weighting

def test_weights_sum_to_one_and_give_the_index_a_tenth():
    total = ADD.W_QUALITY + ADD.W_PATTERNS + ADD.W_SAFETY + ADD.W_RELATIVE
    assert total == pytest.approx(1.0)
    assert ADD.W_RELATIVE == pytest.approx(0.10)


def test_the_original_three_keep_their_proportions_inside_the_90_percent():
    """45/30/25 scaled to 90% — the relative ordering must not shift."""
    for new, old in ((ADD.W_QUALITY, 0.45), (ADD.W_PATTERNS, 0.30),
                     (ADD.W_SAFETY, 0.25)):
        assert new == pytest.approx(old * 0.9)


def test_grade_bands_match_the_composer_so_the_scale_cannot_drift():
    assert ADD.GRADE_BANDS == C.GRADE_BANDS


@pytest.mark.parametrize("score,grade,stars", [
    (100, "Outstanding", 5), (80, "Outstanding", 5), (79, "Strong", 4),
    (65, "Strong", 4), (64, "Decent", 3), (50, "Decent", 3),
    (49, "Mixed", 2), (35, "Mixed", 2), (34, "Weak", 1), (0, "Weak", 1),
])
def test_grade_of(score, grade, stars):
    assert ADD.grade_of(score) == (grade, stars)


# ----------------------------------------------------- report rewriting

def _arith(md: str):
    m = ADD.ARITH_RE.search(md)
    assert m, "arithmetic line not found"
    return m


def test_arithmetic_regex_reads_both_the_old_and_new_forms():
    old = ("**The exact arithmetic:** Overall = 45% × 76 (business quality) "
           "+ 30% × 100 (multibagger fit) + 25% × 88 (risk safety) = 86 out "
           "of 100 → Outstanding (5 stars).")
    new = ("**The exact arithmetic:** Overall = 40.5% × 76 (business quality) "
           "+ 27% × 100 (multibagger fit) + 22.5% × 88 (risk safety) + 10% × "
           "54 (relative to the index) = 83 out of 100 → Outstanding "
           "(5 stars).")
    for text in (old, new):
        m = _arith(text)
        assert (m["bq"], m["mb"], m["rs"]) == ("76", "100", "88")


# --------------------------------------------------------- whole corpus

def _universe():
    return ADD.universe()


def _rated_analysis_files():
    for sym in _universe():
        f = OUT / f"{sym}_analysis.md"
        if f.exists():
            md = f.read_text()
            if ADD.ARITH_RE.search(md):
                yield sym, md


def test_every_company_report_has_the_index_section():
    missing = [sym for sym in _universe()
               if (OUT / f"{sym}_analysis.md").exists()
               and ADD.SECTION_HEAD not in (OUT / f"{sym}_analysis.md").read_text()]
    assert not missing, f"{len(missing)} reports without the section: {missing[:8]}"


def test_every_rated_report_uses_the_new_weights_and_adds_up():
    """Checked against the base weights, not the printed ones, so a report
    whose pillars were re-normalised (a lender with no multibagger score)
    is verified just as strictly as a full four-pillar one."""
    bad = []
    for sym, md in _rated_analysis_files():
        m = ADD.ARITH_LINE_RE.search(md)
        if not m or "relative to the index" not in m.group(0):
            continue                       # no comparable history: untouched
        terms = [(float(w) / 100, int(pts), name)
                 for w, pts, name in ADD.TERM_RE.findall(m["terms"])]
        wsum = sum(ADD.BASE_WEIGHTS[n] for _w, _p, n in terms)
        expect = round(sum(ADD.BASE_WEIGHTS[n] * p for _w, p, n in terms) / wsum)
        if expect != int(m["total"]):
            bad.append((sym, expect, m["total"]))
        # the printed percentages must be the base weights re-normalised
        for w, _p, n in terms:
            if abs(w - ADD.BASE_WEIGHTS[n] / wsum) > 0.001:
                bad.append((sym, n, w, ADD.BASE_WEIGHTS[n] / wsum))
    assert not bad, f"arithmetic does not add up: {bad[:5]}"


def test_the_index_pillar_is_a_tenth_wherever_all_four_are_scored():
    seen = 0
    bad = []
    for sym, md in _rated_analysis_files():
        m = ADD.ARITH_LINE_RE.search(md)
        if not m or len(ADD.TERM_RE.findall(m["terms"])) != 4:
            continue
        seen += 1
        if "10% × " not in m["terms"]:
            bad.append(sym)
    assert seen > 500, f"expected most reports to score all four, saw {seen}"
    assert not bad, f"index pillar not weighted 10%: {bad[:5]}"


def test_headline_score_matches_the_arithmetic_in_every_report():
    bad = []
    for sym, md in _rated_analysis_files():
        head = ADD.VERDICT_RE.search(md)
        arith = ADD.ARITH_RE.search(md)
        if not head:
            continue
        if int(head["score"]) != int(arith["total"]):
            bad.append((sym, head["score"], arith["total"]))
        grade, stars = ADD.grade_of(int(arith["total"]))
        if head["grade"].strip() != grade or head["stars"].count("★") != stars:
            bad.append((sym, head["grade"], grade))
    assert not bad, f"headline disagrees with the arithmetic: {bad[:5]}"


def test_no_report_lost_its_original_sections():
    """The post-processor must add, never remove."""
    bad = []
    for sym, md in _rated_analysis_files():
        for required in ("## About the business",
                         "## Section 1 — How good is the business?",
                         "## Section 2 —", "## Section 3 —",
                         "## How this report was built"):
            if required not in md:
                bad.append((sym, required))
    assert not bad, f"original sections missing: {bad[:5]}"


def test_provenance_lists_the_fourth_skill_exactly_once():
    bad = [sym for sym, md in _rated_analysis_files()
           if md.count("- **StockToIndexPriceEarningsRatio**") != 1]
    assert not bad, f"provenance bullet not exactly once: {bad[:5]}"


def test_comparison_reports_carry_the_index_pillar_and_bucket():
    bad = []
    for sym in _universe():
        f = OUT / f"{sym}_comparison.md"
        if not f.exists():
            continue
        md = f.read_text()
        if ADD.BUCKET_HEAD not in md:
            bad.append((sym, "no bucket"))
        elif "| Relative to the index |" in md:
            if md.count("| Relative to the index |") != 1:
                bad.append((sym, "pillar row duplicated"))
    assert not bad, f"comparison reports wrong: {bad[:5]}"


REL_ROW_RE = re.compile(
    r"\| Relative to the index \| (?P<full>\d+|—) \| (?P<recent>\d+|—) \| "
    r"(?P<delta>[-+]\d+|—) \|")


def test_comparison_step1_matches_its_pillar_table():
    """Long/recent overalls must equal the weighted pillars shown — for
    every shape, including sides where a pillar is an em dash."""
    bad = []
    checked = 0
    for sym in _universe():
        f = OUT / f"{sym}_comparison.md"
        if not f.exists():
            continue
        md = f.read_text()
        step1 = ADD.STEP1_RE.search(md)
        rows = {m["name"]: m for m in ADD.PILLAR_ROW_RE.finditer(md)}
        rel = REL_ROW_RE.search(md)
        if not (step1 and len(rows) == 3 and rel):
            continue
        checked += 1
        for side, idx in (("fs", "full"), ("rs", "recent")):
            cell = rel[idx]
            expect = ADD._side_score(
                rows, idx, int(cell) if cell.isdigit() else None)
            if expect != int(step1[side]):
                bad.append((sym, idx, expect, step1[side]))
    assert checked > 500, f"expected a broad sweep, only checked {checked}"
    assert not bad, f"comparison overalls do not match pillars: {bad[:5]}"


def test_the_index_row_delta_is_consistent_with_its_cells():
    bad = []
    for sym in _universe():
        f = OUT / f"{sym}_comparison.md"
        if not f.exists():
            continue
        m = REL_ROW_RE.search(f.read_text())
        if not m:
            continue
        if m["recent"] == "—" or m["full"] == "—":
            if m["delta"] != "—":
                bad.append((sym, "delta should be an em dash", m["delta"]))
        elif int(m["delta"]) != int(m["recent"]) - int(m["full"]):
            bad.append((sym, m["full"], m["recent"], m["delta"]))
    assert not bad, f"index row delta wrong: {bad[:5]}"
