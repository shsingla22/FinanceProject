"""
Automated tests for the Markdown report generator.

Run from UserInterface/:  python3 -m pytest test_report.py -q

Covers:
  - structural completeness (all 7 areas, verdict, coverage, footer)
  - every assessed parameter appears with its rationale
  - quotes from the record survive into the report
  - the BANNED-JARGON scan: no internal ids, stat shorthand, or
    developer vocabulary may reach the reader
  - honest handling when qualitative evidence is unavailable
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import server as S  # noqa: E402

# NAUKRI has a fully-cached qualitative record (30/30) from the Opus run;
# quick=True elsewhere avoids triggering live AI inside tests.
FULL_SYM = "NAUKRI"
QUICK_SYM = "DIXON"

BANNED_JARGON = [
    r"\bCROCI\b", r"\bopm_std\b", r"\byoy_std\b", r"\bCCC\b",
    r"pricing_mix_volume", r"working_capital_cost", r"\bproxy\b",
    r"\b(CAP|ROC|GRW|MGT|IND|CUS|MOAT)\.[a-z_]+",   # internal param ids
    r"\bquant\b", r"\bqual\b(?!ity)", r"\bstd\b", r"\bYoY\b",
    r"\bdata_available\b", r"\bn/a\b",
    r"From concall:", r"\| Concall:", r"\b1 days\b",
]


def _report(sym, quick):
    return S.render_report_md(sym, quick=quick)


def test_structure_full():
    md = _report(FULL_SYM, quick=False)
    assert md.startswith("# ")
    assert "Business Quality Report" in md
    assert "**Verdict:" in md
    assert "The verdict at a glance" in md
    for area in ["Capital Allocation", "Return on Capital", "Growth",
                 "Management", "Industry Structure", "Customer Benefits",
                 "Competitive Advantage"]:
        assert f"## {area}" in md, f"missing area section: {area}"
    assert "How to read this report" in md
    assert "not investment advice" in md


def test_every_assessed_param_present():
    qual, _ = S._qual_scores_cached(FULL_SYM)
    rec = S.build_record(FULL_SYM, S._live_map(), S._cc_counts(), qual_scores=qual)
    md = _report(FULL_SYM, quick=False)
    fw_by_id = {p["id"]: p for p in S._fw_json["parameters"]}
    for pid in rec["params"]:
        name = fw_by_id[pid]["name"]
        assert name in md, f"assessed parameter missing from report: {name}"


def test_quotes_survive():
    qual, _ = S._qual_scores_cached(FULL_SYM)
    rec = S.build_record(FULL_SYM, S._live_map(), S._cc_counts(), qual_scores=qual)
    quoted = [p["quote"] for p in rec["params"].values()
              if p.get("quote") and len(p["quote"]) > 30]
    md = _report(FULL_SYM, quick=False)
    survived = sum(1 for q in quoted if q[:40] in md)
    assert survived >= max(1, len(quoted) // 2), \
        f"only {survived}/{len(quoted)} long quotes made it into the report"


def test_no_banned_jargon():
    for sym, quick in [(FULL_SYM, False), (QUICK_SYM, True)]:
        md = _report(sym, quick)
        # quotes are management's verbatim words — exempt from the scan
        md_no_quotes = re.sub(r'^> .*$', '', md, flags=re.M)
        for pat in BANNED_JARGON:
            hits = re.findall(pat, md_no_quotes)
            assert not hits, f"{sym}: banned jargon {pat!r} in report: {hits[:3]}"


def test_verdict_words_not_raw_scores_only():
    md = _report(FULL_SYM, quick=False)
    for w in ["Excellent", "Good", "Neutral", "Weak", "Poor"]:
        if w in md:
            break
    else:
        raise AssertionError("no verdict words found in report")


def test_quick_mode_is_honest_about_missing_qualitative():
    md = _report(QUICK_SYM, quick=True)
    assert "never guess" in md
    # quick mode must not silently pretend full coverage
    m = re.search(r"assessed \*\*(\d+)% ", md) or re.search(r"\*\*(\d+)% of the framework", md)
    assert m, "coverage line missing"
    assert int(m.group(1)) < 50, "quick mode should show partial coverage"


def test_coverage_full_for_cached_company():
    md = _report(FULL_SYM, quick=False)
    m = re.search(r"\*\*(\d+)% of the framework", md)
    assert m and int(m.group(1)) >= 90, "NAUKRI cached record should be ~100%"


def test_management_table_present():
    md = _report(FULL_SYM, quick=False)
    assert "Who has been running the company" in md
    assert "| Role | Name |" in md


def test_trend_lines_present():
    md = _report(FULL_SYM, quick=False)
    assert "trend lines" in md.lower()
    assert "Sales (₹ crore)" in md
