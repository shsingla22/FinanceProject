"""
ComparisonSkill tests.

  python3 -m pytest tests/ -q          (from Skills/ComparisonSkill/)
  RUN_SWEEP=1 ... adds a multi-company real-data coverage sweep

Unit tests drive the comparer with synthetic record pairs so every rule
is pinned: rating direction, pillar deltas, per-check improvement and
regression, the one-year-lens silences NEVER counted as regressions,
pattern/risk verdict transitions in the right direction, and the report
order (rating first, then the three buckets). Real-data tests run both
sides quick via the actual CLIs.
"""

import json
import os
import re
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

import compare_engine as CE     # noqa: E402
import analyze as AZ            # noqa: E402


# ------------------------------------------------------- synthetic fixtures
def _side(score, grade, params, mb_verdicts, qr_verdicts, gate="PASS",
          frag="SOUND"):
    return {
        "rating": {"score": score, "grade": grade,
                   "derivation": f"= {score} of 100",
                   "pillars": {
                       "quality": {"name": "Business quality", "points": 60,
                                   "derivation": "q"},
                       "patterns": {"name": "Multibagger fit", "points": 40,
                                    "derivation": "p"},
                       "safety": {"name": "Risk safety", "points": 80,
                                  "derivation": "s"}}},
        "business": {
            "overall": 0.5, "coverage": 0.5,
            "modules": {m: {"score": 1.0, "assessed": 1, "total": 3}
                        for m in CE.MODULE_IDS},
            "params": params},
        "patterns": {"verdicts": mb_verdicts,
                     "matched_patterns": [v["pattern"] for v in mb_verdicts
                                          if v["verdict"] == "STRONG FIT"],
                     "core_gate": {"status": gate, "passed": 3, "of": 3}},
        "risks": {"verdicts": qr_verdicts,
                  "fragility": {"status": frag, "derivation": "fine"}},
        "statuses": {"business": "numbers_only", "patterns": "numbers_only",
                     "risks": "numbers_only"},
    }


def _mbv(pid, verdict):
    return {"pattern": pid, "name": pid.title(), "verdict": verdict,
            "derivation": f"why {verdict}", "qual": {"rationale": f"r-{pid}"}}


def _qrv(rid, verdict):
    return {"risk": rid, "name": rid.title(), "verdict": verdict,
            "derivation": f"why {verdict}", "qual": {"rationale": f"r-{rid}"}}


PID = "ROC.profit_margin"     # a real framework id so names resolve


def test_rating_direction_improved_declined_held():
    base = _side(60, "Decent", {}, [], [])
    up = _side(70, "Strong", {}, [], [])
    down = _side(50, "Decent", {}, [], [])
    flat = _side(61, "Decent", {}, [], [])
    assert CE._rating_delta(base, up)["direction"] == "improved"
    assert CE._rating_delta(base, down)["direction"] == "declined"
    assert CE._rating_delta(base, flat)["direction"] == "held steady"
    d = CE._rating_delta(base, down)
    assert d["delta"] == -10 and "WEAKER" in d["derivation"]


def test_rating_not_comparable_when_a_side_is_unrated():
    base = _side(60, "Decent", {}, [], [])
    unrated = _side(None, "Not rated", {}, [], [])
    d = CE._rating_delta(base, unrated)
    assert d["direction"] == "not comparable" and d["delta"] is None
    assert "could not be rated" in d["derivation"]


def test_business_checks_classified_with_both_sides_evidence():
    f = _side(60, "Decent",
              {PID: {"score": 0, "rationale": "was neutral", "module": "ROC"},
               "CAP.working_capital_cost": {"score": 2, "rationale": "was great",
                                            "module": "CAP"}}, [], [])
    r = _side(60, "Decent",
              {PID: {"score": 2, "rationale": "now excellent", "module": "ROC"},
               "CAP.working_capital_cost": {"score": -1, "rationale": "now weak",
                                            "module": "CAP"}}, [], [])
    b = CE._compare_business(f, r)
    assert len(b["improved"]) == 1 and len(b["regressed"]) == 1
    imp = b["improved"][0]
    assert imp["check"] == "Profit margin" and imp["delta"] == 2
    assert "now excellent" in imp["explanation"]
    assert "was neutral" in imp["explanation"]       # both sides' evidence


def test_lens_silence_is_never_a_regression():
    """A check the one-year window cannot see must land in
    window_excluded — NOT in regressed — with the lens named."""
    f = _side(60, "Decent",
              {PID: {"score": 2, "rationale": "long-trend check",
                     "module": "ROC"}}, [], [])
    r = _side(60, "Decent", {}, [], [])          # silent in the window
    b = CE._compare_business(f, r)
    assert b["regressed"] == []
    assert len(b["window_excluded"]) == 1
    assert "not a regression" in b["window_excluded"][0]["note"]
    assert "not counted" in b["overall"]


def test_pattern_transitions_direction():
    f = _side(60, "Decent", {}, [_mbv("TOLL", "STRONG FIT"),
                                 _mbv("BRAND", "PARTIAL"),
                                 _mbv("CULT", "STRONG FIT"),
                                 _mbv("INNO", "NOT ASSESSED")], [])
    r = _side(60, "Decent", {}, [_mbv("TOLL", "PARTIAL"),      # weakened
                                 _mbv("BRAND", "STRONG FIT"),  # strengthened
                                 _mbv("CULT", "STRONG FIT"),   # unchanged
                                 _mbv("INNO", "STRONG FIT")], [])  # n/c
    t = CE._compare_patterns(f, r)
    assert [i["name"] for i in t["regressed"]] == ["Toll"]
    assert [i["name"] for i in t["improved"]] == ["Brand"]
    assert [i["name"] for i in t["unchanged"]] == ["Cult"]
    assert [i["name"] for i in t["not_comparable"]] == ["Inno"]
    assert "1 strengthened, 1 weakened" in t["overall"]


def test_risk_transitions_direction_is_inverted():
    """For risks, moving TOWARD severity is a regression."""
    f = _side(60, "Decent", {}, [], [_qrv("GOVT", "WATCH"),
                                     _qrv("CYCL", "HIGH RISK")])
    r = _side(60, "Decent", {}, [], [_qrv("GOVT", "HIGH RISK"),   # worsened
                                     _qrv("CYCL", "LOW")])        # eased
    t = CE._compare_risks(f, r)
    assert [i["name"] for i in t["regressed"]] == ["Govt"]
    assert [i["name"] for i in t["improved"]] == ["Cycl"]
    assert t["fragility"]["full"] == "SOUND"


def test_report_order_rating_first_then_three_buckets():
    f = _side(60, "Decent",
              {PID: {"score": 0, "rationale": "x", "module": "ROC"}},
              [_mbv("TOLL", "STRONG FIT")], [_qrv("GOVT", "WATCH")])
    r = _side(52, "Decent",
              {PID: {"score": -1, "rationale": "y", "module": "ROC"}},
              [_mbv("TOLL", "PARTIAL")], [_qrv("GOVT", "ELEVATED")])
    rec = CE.compare("TESTCO", f, r)
    md = AZ.render("TESTCO", "Test Co", rec)
    order = ["## Step 1 — The overall rating: DECLINED",
             "## Step 2 — Where it improved and where it regressed",
             "### Bucket 1 — Business quality",
             "### Bucket 2 — Multibagger patterns",
             "### Bucket 3 — Risks",
             "## How this comparison was built"]
    idx = [md.find(s) for s in order]
    assert all(i >= 0 for i in idx), list(zip(order, idx))
    assert idx == sorted(idx)
    assert "not investment advice" in md
    # explainability: movements carry both sides' evidence
    assert "Why now:" in md and "The long view had said:" in md


# --------------------------------------------------------------- real data
def test_real_end_to_end_quick():
    rec = AZ.run("DIXON", ai=False)
    assert rec["rating"]["direction"] in {"improved", "declined",
                                          "held steady", "not comparable"}
    md = AZ.render("DIXON", "Dixon", rec)
    assert "## Step 1" in md and "### Bucket 3" in md
    body = re.sub(r"^> .*$", "", md, flags=re.M)
    for banned in [r"\b(CAP|ROC|GRW|MGT|IND|CUS|MOAT)\.[a-z_]+",
                   r"\b1 days\b", r"\bnan\b", r"1 checks need\b"]:
        assert not re.search(banned, body), banned


@pytest.mark.skipif(not os.environ.get("RUN_SWEEP"),
                    reason="set RUN_SWEEP=1 for the multi-company sweep")
def test_coverage_sweep_across_diverse_companies():
    """High coverage: a stratified set spanning compounders, cyclicals,
    PSUs, lenders (not-rated path), and recent listings must all compose
    a structurally-sound comparison."""
    SYMS = ["CRISIL", "DIXON", "TATASTEEL", "PIDILITIND", "NAUKRI",
            "HINDUNILVR", "COALINDIA", "IRCTC", "HDFCBANK", "IFCI",
            "ETHOSLTD", "URBANCO", "BLUESTONE", "KAYNES", "ASIANPAINT",
            "PHOENIXLTD", "CAMS", "COLPAL", "ITC", "TRENT"]
    failures = []
    for sym in SYMS:
        try:
            rec = AZ.run(sym, ai=False)
            md = AZ.render(sym, sym, rec)
            for s in ("## Step 1", "### Bucket 1", "### Bucket 2",
                      "### Bucket 3", "## How this comparison was built"):
                if s not in md:
                    failures.append((sym, f"missing {s}"))
                    break
        except Exception as e:
            failures.append((sym, str(e)[:100]))
    assert not failures, failures


def test_carried_items_get_their_own_bucket_never_regressions():
    """A carried-forward item must classify as carried — not improved,
    not regressed, not not-comparable — in all three buckets."""
    f = _side(60, "Decent",
              {PID: {"score": 1, "rationale": "long-trend verdict",
                     "module": "ROC"}},
              [_mbv("TOLL", "STRONG FIT")], [_qrv("GOVT", "WATCH")])
    r = _side(60, "Decent",
              {PID: {"score": 1, "rationale": "Carried forward...",
                     "module": "ROC", "source": "carried"}},
              [dict(_mbv("TOLL", "STRONG FIT"), carried_forward=True)],
              [dict(_qrv("GOVT", "WATCH"), carried_forward=True)])
    b = CE._compare_business(f, r)
    assert [c["check"] for c in b["carried"]] == ["Profit margin"]
    assert b["improved"] == b["regressed"] == b["unchanged"] == []
    t = CE._compare_patterns(f, r)
    assert [c["name"] for c in t["carried"]] == ["Toll"]
    assert t["improved"] == t["regressed"] == t["not_comparable"] == []
    tq = CE._compare_risks(f, r)
    assert [c["name"] for c in tq["carried"]] == ["Govt"]
    rec = CE.compare("TESTCO", f, r)
    md = AZ.render("TESTCO", "Test Co", rec)
    assert "Carried forward from the long view unchanged" in md
