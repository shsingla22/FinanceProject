"""
Tests for the then-vs-now UI panel (comparison_bridge + the new endpoints).

  python3 -m pytest test_comparison_ui.py -q            (from UserInterface/)
  RUN_SWEEP=1 python3 -m pytest test_comparison_ui.py -q   adds a stratified
                                                           multi-company sweep

All standard tests run in numbers-only mode (no AI calls). The panel view
(/api/comparison) and the downloadable file (/api/comparison_report) must
come from the SAME composition — that consistency is asserted, not assumed.
"""

import os
import re
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "IndividualStockAnalysis" / "India"
                       / "Skills" / "BusinessAnalysis" / "scripts"))

import server as SV                     # noqa: E402
import comparison_bridge as CB          # noqa: E402

client = TestClient(SV.app)

MD_SECTIONS = ["— Then vs Now: The One-Year Comparison",
               "## Step 1 — The overall rating",
               "## Step 2 — Where it improved and where it regressed",
               "### Bucket 1 — Business quality (34-check framework)",
               "### Bucket 2 — Multibagger patterns (11 patterns)",
               "### Bucket 3 — Risks (8 channels)",
               "## How this comparison was built"]
JARGON = [r"\b(CAP|ROC|GRW|MGT|IND|CUS|MOAT)\.[a-z_]+", r"\bopm\b",
          r"\byoy\b", r"\b1 days\b", r"\bnan\b",
          r"1 checks\b", r"1 fingerprints\b"]


def _comparison(sym, quick=1):
    r = client.get(f"/api/comparison/{sym}?quick={quick}")
    assert r.status_code == 200, r.text[:300]
    return r.json()


# ------------------------------------------------------------ the endpoint
def test_comparison_payload_shape():
    out = _comparison("CRISIL")
    for key in ("symbol", "name", "record", "md"):
        assert key in out, f"payload missing {key}"
    rec = out["record"]
    for key in ("rating", "numbers", "pillars", "business", "patterns",
                "risks", "statuses"):
        assert key in rec, f"record missing {key}"
    assert rec["rating"]["direction"] in {"improved", "declined",
                                          "held steady", "not comparable"}
    assert len(rec["pillars"]) == 3
    # both sides' engine statuses disclosed — the methodology is inspectable
    assert set(rec["statuses"]) == {"full", "recent"}


def test_delta_arithmetic_is_what_it_claims():
    rec = _comparison("CRISIL")["record"]
    rd = rec["rating"]
    if rd["delta"] is not None:
        assert rd["delta"] == rd["recent"]["score"] - rd["full"]["score"]
        expect = ("improved" if rd["delta"] > 2 else
                  "declined" if rd["delta"] < -2 else "held steady")
        assert rd["direction"] == expect
    for p in rec["pillars"]:
        if p["delta"] is not None:
            assert p["delta"] == p["recent"] - p["full"]
            assert len(p["full_why"]) > 20 and len(p["recent_why"]) > 20


def test_md_structure_and_matches_download():
    out = _comparison("CRISIL")
    md = out["md"]
    idx = [md.find(s) for s in MD_SECTIONS]
    assert all(i >= 0 for i in idx) and idx == sorted(idx), \
        f"md sections wrong: {list(zip(MD_SECTIONS, idx))}"
    r = client.get("/api/comparison_report/CRISIL?quick=1")
    assert r.status_code == 200
    assert "text/markdown" in r.headers["content-type"]
    assert "attachment" in r.headers.get("content-disposition", "")
    assert r.text == md, "panel md and downloaded md must be IDENTICAL"


def test_md_has_numbers_table_and_no_jargon():
    out = _comparison("CRISIL")
    md = out["md"]
    if out["record"]["numbers"]:
        assert "## The numbers behind the comparison" in md
        assert "| Measure | Long-view average |" in md
    body = re.sub(r"^> .*$", "", md, flags=re.M)
    for pat in JARGON:
        assert not re.search(pat, body), f"jargon leaked: {pat}"


def test_carried_items_are_never_regressions():
    rec = _comparison("DIXON")["record"]
    carried = {c["check"] for c in rec["business"]["carried"]} \
        | {c["name"] for c in rec["patterns"]["carried"]} \
        | {c["name"] for c in rec["risks"]["carried"]}
    regressed = {c["check"] for c in rec["business"]["regressed"]} \
        | {c["name"] for c in rec["patterns"]["regressed"]} \
        | {c["name"] for c in rec["risks"]["regressed"]}
    assert not carried & regressed, \
        f"carried items counted as regressions: {carried & regressed}"


def test_every_movement_line_carries_its_why():
    rec = _comparison("DIXON")["record"]
    for c in rec["business"]["improved"] + rec["business"]["regressed"]:
        assert len(c["explanation"]) > 10, c["check"]
    for key in ("patterns", "risks"):
        for i in rec[key]["improved"] + rec[key]["regressed"]:
            assert (i["now"] or i["why_now"]), i["name"]


def test_unknown_symbol_is_a_clean_404():
    assert client.get("/api/comparison/NOTACOMPANY").status_code == 404
    assert client.get("/api/comparison_report/NOTACOMPANY").status_code == 404


def test_ask_grounding_uses_cached_comparison_only():
    # a symbol never compared this session -> no grounding, no compute
    CB.drop_caches()
    assert SV._comparison_grounding("CRISIL") is None
    _comparison("CRISIL")                      # computes + caches
    g = SV._comparison_grounding("CRISIL")
    assert g is not None
    assert '"direction"' in g and '"business_quality"' in g
    # grounding text uses display language, not internal codes
    for pat in JARGON[:1]:
        assert not re.search(pat, g)


def test_refresh_drops_the_comparison_cache():
    _comparison("CRISIL")
    assert CB.cached("CRISIL") is not None
    r = client.post("/api/refresh")
    assert r.status_code == 200
    assert CB.cached("CRISIL") is None


# ------------------------------------------------------- optional big sweep
@pytest.mark.skipif(not os.environ.get("RUN_SWEEP"),
                    reason="set RUN_SWEEP=1 for the stratified sweep")
def test_stratified_sweep_through_the_server_path():
    """High dataset coverage: companies of every stripe — strong, weak,
    lender (Not rated), thin-history recent listing — must all compose a
    structurally sound panel+md through the same code path the UI uses."""
    SYMS = ["CRISIL", "DIXON", "TATASTEEL", "PIDILITIND", "RTNPOWER",
            "HDFCBANK", "IFCI", "KAYNES", "ASIANPAINT", "INFY",
            "URBANCO", "ETHOSLTD"]
    failures = []
    for sym in SYMS:
        try:
            out = _comparison(sym)
            md = out["md"]
            idx = [md.find(s) for s in MD_SECTIONS]
            if any(x < 0 for x in idx) or idx != sorted(idx):
                failures.append((sym, "sections"))
                continue
            body = re.sub(r"^> .*$", "", md, flags=re.M)
            for pat in JARGON:
                if re.search(pat, body):
                    failures.append((sym, f"jargon {pat}"))
                    break
        except Exception as e:
            failures.append((sym, f"EXC {str(e)[:120]}"))
    assert not failures, f"{len(failures)} failures: {failures}"
