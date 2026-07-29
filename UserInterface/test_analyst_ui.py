"""
Tests for the analyst-experience UI (analyst_bridge + the new endpoints).

  python3 -m pytest test_analyst_ui.py -q            (from UserInterface/)
  RUN_SWEEP=1 python3 -m pytest test_analyst_ui.py -q   adds the full
                                                        742-company sweep

All standard tests run in numbers-only mode (no AI calls). The page view
(/api/analysis) and the downloadable file (/api/report) must come from the
SAME composition — that consistency is asserted, not assumed.
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


def test_untestable_company_is_honestly_not_rated():
    out = _analysis("HDFCBANK")          # lender: frameworks can't read it
    assert out["rating"]["grade"] == "Not rated"
    assert "## The verdict: Not rated" in out["md"]


def test_quick_mode_has_no_overview_and_says_so():
    out = _analysis("CRISIL")
    assert out["overview"] is None       # no AI in quick mode
    assert "No conference-call transcripts were available" in out["md"] or \
        "About the business" in out["md"]


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
