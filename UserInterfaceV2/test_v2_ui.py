"""
test_v2_ui.py — automated tests for the precomputed (v2) UI server.

Run from this folder:  UI_DISABLE_AI=1 python3 -m pytest test_v2_ui.py -q

Covers the whole contract:
  health / companies inventory
  analysis + comparison endpoints serve the EXACT stored bytes
  downloads byte-identical to the page payload
  best/worst ranking with drill-down fields, industry filter, bounds
  charts: series aligned to years, only chartable metrics offered
  Q&A: extractive fallback (no AI) is grounded in the reports; job twin
  full sweep: every analysed company loads analysis+comparison cleanly
  honest 404s: unknown symbol vs not-yet-analysed symbol
"""

import os
import sys
from pathlib import Path

os.environ.setdefault("UI_DISABLE_AI", "1")   # tests never call the AI

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pytest
from fastapi.testclient import TestClient

import server as S

client = TestClient(S.app)

SYMS = S.analysed_symbols()
SOME = SYMS[0] if SYMS else None


def test_reports_exist():
    assert len(SYMS) >= 400, f"expected the batch's stored reports, found {len(SYMS)}"


def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    h = r.json()
    assert h["mode"] == "precomputed"
    assert h["n_analysed"] == len(SYMS)
    assert h["n_universe"] == len(S._const_map)
    assert h["ai_qa"] is False          # UI_DISABLE_AI=1


def test_companies_inventory():
    r = client.get("/api/companies")
    assert r.status_code == 200
    d = r.json()
    assert d["n"] == len(S._const_map)
    assert d["n_analysed"] == len(SYMS)
    co = d["companies"][SOME]
    assert co["analysed"] is True
    assert co["grade"] in {"Outstanding", "Strong", "Decent", "Mixed",
                           "Weak", "Not rated"}
    # an unanalysed constituent is listed and flagged, not hidden
    missing = [s for s in S._const_map if s not in set(SYMS)]
    if missing:
        assert d["companies"][missing[0]]["analysed"] is False


def test_analysis_serves_exact_stored_bytes():
    r = client.get(f"/api/analysis/{SOME}")
    assert r.status_code == 200
    d = r.json()
    stored = (S.QA / f"{SOME}_analysis.md").read_text()
    assert d["md"] == stored
    assert d["score"] is None or 0 <= d["score"] <= 100
    assert d["sections"], "section map must not be empty"
    assert any("verdict" in s["title"].lower() for s in d["sections"])


def test_comparison_serves_exact_stored_bytes():
    r = client.get(f"/api/comparison/{SOME}")
    assert r.status_code == 200
    d = r.json()
    stored = (S.QA / f"{SOME}_comparison.md").read_text()
    assert d["md"] == stored
    assert d["direction"] in {"improved", "declined", "held steady",
                              "not comparable", None}


def test_downloads_byte_identical():
    for kind, fname in (("report", "_analysis.md"),
                        ("comparison_report", "_comparison.md")):
        r = client.get(f"/api/{kind}/{SOME}")
        assert r.status_code == 200
        assert r.content == (S.QA / f"{SOME}{fname}").read_bytes()
        assert "attachment" in r.headers["content-disposition"]


def test_ranking_best_and_worst():
    best = client.get("/api/ranking?n=20&order=best").json()
    worst = client.get("/api/ranking?n=20&order=worst").json()
    assert best["n"] == 20 and worst["n"] == 20
    scores_b = [r["score"] for r in best["rows"]]
    scores_w = [r["score"] for r in worst["rows"]]
    assert scores_b == sorted(scores_b, reverse=True)
    assert scores_w == sorted(scores_w)
    assert best["rows"][0]["rank"] == 1
    # drill-down contract: every row names an analysed company with reports
    for r in best["rows"] + worst["rows"]:
        assert r["symbol"] in set(SYMS)
        assert r["grade"] and r["name"]
        assert client.get(f"/api/analysis/{r['symbol']}").status_code == 200


def test_ranking_bounds_and_industry():
    assert client.get("/api/ranking?n=100000").json()["n"] <= 200
    assert client.get("/api/ranking?n=0").json()["n"] == 1
    ind = S._const_map[SOME]["industry"]
    if ind:
        rows = client.get(f"/api/ranking?n=50&industry={ind}").json()["rows"]
        assert all(r["industry"].lower() == ind.lower() for r in rows)


def test_charts_shape():
    r = client.get(f"/api/charts/{SOME}")
    assert r.status_code == 200
    d = r.json()
    assert d["years"], "chart years must not be empty"
    for key, vals in d["series"].items():
        assert len(vals) == len(d["years"]), f"{key} misaligned with years"
    offered = {c["key"] for c in d["charts"]}
    for c in d["charts"]:
        pts = [v for v in d["series"][c["key"]] if v is not None]
        assert len(pts) >= 3, f"{c['key']} offered with <3 points"
    assert "sales" in offered or "cfo" in offered


def test_ask_extractive_fallback_grounded():
    r = client.post(f"/api/ask/{SOME}",
                    json={"question": "What are the biggest risks?"})
    assert r.status_code == 200
    d = r.json()
    assert d["ai"] is False and d["grounded_on"] == "stored_reports"
    # the verbatim passages must actually come from the stored files
    a_md = (S.QA / f"{SOME}_analysis.md").read_text()
    c_md = (S.QA / f"{SOME}_comparison.md").read_text()
    quoted = [seg for seg in d["answer"].split("\n\n")[1:] if seg]
    assert quoted, "fallback answered without quoting any section"
    for seg in quoted:
        body = seg.split("]\n", 1)[-1]
        probe = body[:200]
        assert probe in a_md or probe in c_md, "quoted text not from reports"


def test_ask_validation():
    assert client.post(f"/api/ask/{SOME}", json={}).status_code == 422
    assert client.post("/api/ask/NOSUCH", json={"question": "x"}).status_code == 404


def test_ask_job_roundtrip():
    r = client.post(f"/api/jobs/ask/{SOME}", json={"question": "Why this rating?"})
    assert r.status_code == 200
    job = r.json()["job"]
    job_id = job.split(":")[1]
    import time
    for _ in range(80):
        j = client.get(f"/api/jobs/ask/{job_id}").json()
        if j["state"] != "running":
            break
        time.sleep(0.1)
    assert j["state"] == "done", j.get("error")
    assert "answer" in j["result"]
    assert client.get("/api/jobs/ask/DEADBEEF").status_code == 404


def test_honest_404s():
    assert client.get("/api/analysis/NOSUCHCO").status_code == 404
    missing = [s for s in S._const_map if s not in set(SYMS)]
    if missing:
        r = client.get(f"/api/analysis/{missing[0]}")
        assert r.status_code == 404
        assert "not been analysed" in r.json()["detail"]


def test_static_frontend_served():
    r = client.get("/")
    assert r.status_code == 200
    assert "Company Analyst" in r.text and "app.js" in r.text


@pytest.mark.parametrize("chunk", range(10))
def test_sweep_all_stored_reports_load(chunk):
    """EVERY analysed company must load: analysis, comparison, charts."""
    for sym in SYMS[chunk::10]:
        a = client.get(f"/api/analysis/{sym}")
        assert a.status_code == 200, f"{sym} analysis failed"
        d = a.json()
        assert d["md"].startswith("#"), f"{sym} analysis not a report"
        assert d["sections"], f"{sym} has no sections"
        c = client.get(f"/api/comparison/{sym}")
        assert c.status_code == 200, f"{sym} comparison failed"
        assert "Then vs Now" in c.json()["md"], f"{sym} comparison malformed"
        ch = client.get(f"/api/charts/{sym}")
        assert ch.status_code == 200, f"{sym} charts failed"
