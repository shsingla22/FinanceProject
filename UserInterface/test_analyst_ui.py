"""
Tests for the analyst-experience UI (analyst_bridge + the new endpoints).

  python3 -m pytest test_analyst_ui.py -q            (from UserInterface/)
  RUN_SWEEP=1 python3 -m pytest test_analyst_ui.py -q   adds the full
                                                        742-company sweep

All standard tests run in numbers-only mode (no AI calls). The page view
(/api/analysis) and the downloadable file (/api/report) must come from the
SAME composition — that consistency is asserted, not assumed.
"""

import json
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
import analyst_bridge as AB             # noqa: E402

client = TestClient(SV.app)

SECTIONS = ["## About the business", "## The verdict:",
            "## Section 1 — How good is the business?",
            "## Section 2 — Does it look like a long-term winner?",
            "## Section 3 — What could break it?",
            "## What to watch", "## How this report was built"]
JARGON = [r"\b(CAP|ROC|GRW|MGT|IND|CUS|MOAT)\.[a-z_]+", r"\bopm\b",
          r"\byoy\b", r"\b1 days\b", r"\bNone\b(?! of)", r"\bnan\b",
          r"1 checks\b", r"1 fingerprints\b", r"1 high risks\b"]


def _analysis(sym, quick=1):
    r = client.get(f"/api/analysis/{sym}?quick={quick}")
    assert r.status_code == 200, r.text[:200]
    return r.json()


# ------------------------------------------------------------ the endpoint
def test_analysis_payload_matches_the_analyst_experience():
    out = _analysis("CRISIL")
    # everything the page needs, in the analyst's order
    for key in ("name", "industry", "overview", "rating", "verdict_plain",
                "summary", "business", "patterns", "risks", "trends",
                "statuses", "md", "market"):
        assert key in out, f"payload missing {key}"
    assert out["rating"]["grade"] in {"Outstanding", "Strong", "Decent",
                                      "Mixed", "Weak", "Not rated"}
    assert len(out["patterns"]["verdicts"]) == 11
    assert len(out["risks"]["verdicts"]) == 8
    assert set(out["trends"]) == {"sales", "opm", "roce", "ccc"}
    # module weights included so the page can show the exact arithmetic
    assert all("weight" in d for d in out["business"]["modules"].values())


def test_every_verdict_in_payload_carries_its_why():
    out = _analysis("TATASTEEL")
    for v in out["patterns"]["verdicts"] + out["risks"]["verdicts"]:
        assert len(v.get("derivation", "")) > 15, v["name"]
    for p in out["rating"]["pillars"].values():
        assert len(p["derivation"]) > 30
    assert len(out["verdict_plain"]) > 30


def test_md_is_generated_with_the_page_and_matches_download():
    out = _analysis("CRISIL")
    md = out["md"]
    idx = [md.find(s) for s in SECTIONS]
    assert all(i >= 0 for i in idx) and idx == sorted(idx), \
        f"md sections wrong: {list(zip(SECTIONS, idx))}"
    r = client.get("/api/report/CRISIL?quick=1")
    assert r.status_code == 200
    assert "text/markdown" in r.headers["content-type"]
    assert "attachment" in r.headers.get("content-disposition", "")
    assert r.text == md, "page md and downloaded md must be IDENTICAL"


def test_md_has_charts_and_no_jargon():
    out = _analysis("DIXON")
    md = out["md"]
    assert "### The numbers over time" in md and "█" in md
    assert "vs prior year" in md
    body = re.sub(r"^> .*$", "", md, flags=re.M)
    for pat in JARGON:
        assert not re.search(pat, body), f"jargon leaked: {pat}"


def test_unknown_symbol_is_a_clean_404():
    assert client.get("/api/analysis/NOTACOMPANY").status_code == 404


def test_live_no_ai_run_agrees_with_the_stored_verdict():
    """A lender the NUMBERS alone cannot rate (HDFCBANK) is still rated in
    no-AI mode because the committed judge caches carry the qualitative
    verdicts — and the grade must be the STORED report's grade, so the live
    pipeline and the stored corpus can never disagree about a company."""
    out = _analysis("HDFCBANK")
    st = SV.stored_ratings().get("HDFCBANK")
    assert st is not None
    if st["score"] is None:
        assert out["rating"]["grade"] == "Not rated"
    else:
        assert out["rating"]["grade"] == st["grade"]
        assert out["rating"]["score"] == st["score"]


def test_quick_mode_overview_comes_from_the_cache_never_a_live_call():
    """With AI off, the About-the-business overview is served from the
    committed cache when one exists — and is honestly absent otherwise.
    Either way no model is invoked (UI_DISABLE_AI guarantees that)."""
    out = _analysis("CRISIL")
    cached = json.loads((AB.AR.HERE.parent / ".overview_cache.json")
                        .read_text()).get("CRISIL")
    if cached is None:
        assert out["overview"] is None
    else:
        assert out["overview"] == cached["overview"]
        assert "About the business" in out["md"]


# ------------------------------------------------------- optional big sweep
@pytest.mark.skipif(not os.environ.get("RUN_SWEEP"),
                    reason="set RUN_SWEEP=1 for the 742-company sweep")
def test_full_universe_sweep_through_the_server_path():
    """High dataset coverage: EVERY company in the universe must compose a
    structurally-sound page+md through the same code path the UI uses."""
    import pandas as pd
    const = pd.read_csv(SV.INDIA / "NiftyTotalMarket"
                        / "niftytotalmarket_constituents.csv")
    failures = []
    for i, sym in enumerate(sorted(const.nse_symbol.astype(str)), 1):
        try:
            out = AB.full_analysis(sym, ai=False)
            md = out["md"]
            idx = [md.find(s) for s in SECTIONS]
            if any(x < 0 for x in idx) or idx != sorted(idx):
                failures.append((sym, "sections"))
                continue
            body = re.sub(r"^> .*$", "", md, flags=re.M)
            for pat in JARGON:
                if re.search(pat, body):
                    failures.append((sym, f"jargon {pat}"))
                    break
        except Exception as e:
            failures.append((sym, f"EXC {str(e)[:80]}"))
    assert not failures, f"{len(failures)} failures: {failures[:10]}"


# --------------------- the index comparison as a fourth pillar ---------------

def test_analysis_payload_carries_the_index_pillar_and_its_numbers():
    """The UI renders this pillar structurally, so the payload must carry
    the window cells and the yearly series — not just a Markdown blob."""
    out = client.get("/api/analysis/PIDILITIND?quick=1").json()
    ext = next(e for e in out["extensions"]
               if "index" in e["pillar"]["name"].lower())
    assert ext["status"] == "ok"
    p = ext["record"]["pillar"]
    assert 0 <= p["points"] <= 100
    assert p["verdict"] and "index" in p["verdict"].lower()
    assert {c["window"] for c in p["cells"]} == {10, 5, 3, 1}
    for c in p["cells"]:
        if c["pct"] is not None:
            assert c["score"] in (-2, -1, 0, 1, 2)
            assert c["word"]
    chart = ext["record"]["chart"]
    assert set(chart) == {"price", "pat", "op"}
    assert any(chart[k]["yoy"] for k in chart), "no yearly series to plot"


def test_the_rating_uses_four_pillars_and_the_arithmetic_adds_up():
    rt = client.get("/api/analysis/PIDILITIND?quick=1").json()["rating"]
    assert rt["pillar_order"][:3] == ["quality", "patterns", "safety"]
    ext_keys = [k for k in rt["pillar_order"] if k.startswith("ext:")]
    assert ext_keys, "no extension pillar in the rating"
    scored = {k: rt["pillars"][k] for k in rt["pillar_order"]
              if rt["pillars"][k]["points"] is not None}
    weights = {"quality": 0.405, "patterns": 0.27, "safety": 0.225}
    for k in ext_keys:
        weights[k] = 0.10
    wsum = sum(weights[k] for k in scored)
    expect = round(sum(weights[k] * p["points"] for k, p in scored.items())
                   / wsum)
    assert rt["score"] == expect, rt["derivation"]
    assert "relative to the index" in rt["derivation"]


def test_api_rating_and_api_analysis_never_quote_different_numbers():
    """Two endpoints, one truth: both must fold in the same pillars."""
    a = client.get("/api/analysis/PIDILITIND?quick=1").json()["rating"]
    r = client.get("/api/rating/PIDILITIND?quick=1").json()["rating"]
    a_rel = next(p for k, p in a["pillars"].items() if k.startswith("ext:"))
    r_rel = next(p for k, p in r["pillars"].items() if k.startswith("ext:"))
    assert a_rel["points"] == r_rel["points"]
    assert "relative to the index" in r["derivation"]


def test_the_report_markdown_explains_the_index_pillar():
    md = client.get("/api/analysis/PIDILITIND?quick=1").json()["md"]
    assert "## Section 4 — How has it done against the index?" in md
    assert "Against the Nifty 50 it has" in md, "one-breath line missing it"
    assert "- **Relative to the index (" in md, "pillar bullet missing"


# ---------------- the list view runs on the STORED analyst ratings -----------
# The numbers alone answer 7 of the 34 checks (~21% coverage); ranking the
# universe on them would be wrong. Every list/rank/compare surface therefore
# reads the full stored verdict — qualitative pillars included — parsed from
# the same report files the download buttons serve.

def test_companies_payload_carries_the_stored_rating():
    out = client.get("/api/companies").json()
    assert out["n_rated"] >= 700, "expected the batch's stored verdicts"
    covered = [c for c in out["companies"].values() if c.get("stored")]
    assert len(covered) >= 700
    rated = [c for c in covered if c["stored"]["score"] is not None]
    for c in rated[:20]:
        st = c["stored"]
        assert 0 <= st["score"] <= 100
        assert st["grade"] in {"Outstanding", "Strong", "Decent",
                               "Mixed", "Weak"}
        assert st["direction"] in {"improved", "declined", "held steady",
                                   None}


def test_stored_rating_matches_the_report_the_ui_offers_for_download():
    """List row and downloaded report must be the same verdict."""
    import re as _re
    for sym in ("PIDILITIND", "COLPAL", "APOLLOHOSP", "CRISIL"):
        st = SV.stored_ratings()[sym]
        md = (SV.QA_REPORTS / f"{sym}_analysis.md").read_text()
        m = _re.search(r"^## The verdict: (.+?) — (\d+) out of 100",
                       md, _re.M)
        assert st["grade"] == m.group(1).strip()
        assert st["score"] == int(m.group(2))


def test_not_rated_companies_come_back_honest_not_scored():
    st = SV.stored_ratings()
    unrated = [s for s, v in st.items() if v["score"] is None]
    for s in unrated:
        assert st[s]["grade"] == "Not rated"
        md = (SV.QA_REPORTS / f"{s}_analysis.md").read_text()
        assert "## The verdict: Not rated" in md


def test_stored_ratings_agree_with_the_generated_ranking_csv():
    """Two derivations of the same reports must agree on every company."""
    import csv as _csv
    st = SV.stored_ratings()
    path = SV.QA_REPORTS / "_ranking.csv"
    if not path.exists():
        pytest.skip("no _ranking.csv in this checkout")
    bad = []
    with open(path) as fh:
        for row in _csv.DictReader(fh):
            sym = row["symbol"]
            if sym not in st:
                continue
            want = int(float(row["score"])) if row["score"] else None
            if st[sym]["score"] != want:
                bad.append((sym, st[sym]["score"], want))
    assert not bad, f"stored parse disagrees with ranking csv: {bad[:5]}"


# -------- the stored-first company view + clone-stable judge caches ----------

def test_stored_endpoint_serves_the_complete_report():
    r = client.get("/api/stored/IXIGO")
    assert r.status_code == 200
    d = r.json()
    assert d["source"] == "stored"
    assert d["score"] is not None and d["grade"]
    assert "## The verdict:" in d["analysis_md"]
    assert "## Section 4 — How has it done against the index?" in d["analysis_md"]
    assert d["comparison_md"] and "### Bucket" in d["comparison_md"]
    # the payload verdict and the report's verdict are the same line
    assert f"{d['grade']} — {d['score']} out of 100" in d["analysis_md"]


def test_stored_downloads_are_the_exact_stored_bytes():
    for suffix, ep in (("_analysis.md", "stored_report"),
                       ("_comparison.md", "stored_comparison_report")):
        stored = (SV.QA_REPORTS / f"IXIGO{suffix}").read_text()
        r = client.get(f"/api/{ep}/IXIGO")
        assert r.status_code == 200
        assert r.text == stored, f"{ep} must serve the stored file byte-for-byte"


def test_stored_endpoint_404s_honestly():
    assert client.get("/api/stored/NOTACOMPANY").status_code == 404
    assert client.get("/api/stored_report/NOTACOMPANY").status_code == 404


def test_judge_caches_survive_a_fresh_clone():
    """The cache stamp must derive from the transcript's CONTENT: touching
    the file (what a git clone effectively does to every mtime) must not
    invalidate a single committed verdict."""
    import json as _json, os as _os, time as _time
    pdf = (SV.INDIA / "ConferenceCalls" / "NiftyTotalMarket" / "IXIGO.pdf")
    stamp_before = AB.AR.pdf_content_stamp(pdf)
    old = pdf.stat().st_mtime
    _os.utime(pdf, (old + 1000, old + 1000))     # simulate a re-clone
    try:
        AB.AR._PDF_HASH_MEMO.clear()
        assert AB.AR.pdf_content_stamp(pdf) == stamp_before
        cached = _json.loads((AB.AR.HERE.parent / ".qual_cache.json")
                             .read_text())["IXIGO"]["stamp"]
        assert cached.startswith(stamp_before), \
            "committed cache entry must match the content-derived stamp"
    finally:
        _os.utime(pdf, (old, old))
        AB.AR._PDF_HASH_MEMO.clear()


def test_live_rerun_without_ai_reuses_the_batch_judgement():
    """The regression the user reported: with AI OFF, the live pipeline
    must still produce the COMPLETE analysis by reading the committed
    judge caches — never 'not assessed' walls at ~20% coverage."""
    md = client.get("/api/analysis/IXIGO").json()["md"]
    m = re.search(r"(\d+)% of the 34 checks had evidence", md)
    assert m and int(m.group(1)) >= 90, f"coverage collapsed: {m}"
    assert "NOT ASSESSED" not in md
    stored_v = re.search(r"^## The verdict: (.+?) — (\d+) out of 100",
                         (SV.QA_REPORTS / "IXIGO_analysis.md").read_text(),
                         re.M)
    live_v = re.search(r"^## The verdict: (.+?) — (\d+) out of 100", md, re.M)
    assert live_v.group(2) == stored_v.group(2), \
        "live no-AI re-run must reproduce the stored score from the caches"


def test_run_business_status_says_with_calls_when_cache_hits():
    ba, status = AB.AR.run_business("IXIGO", ai=False)
    assert status == "with_calls", status
    assert ba["coverage"] >= 0.9
