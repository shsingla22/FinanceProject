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
    assert "Investment Company" in r.text and "app.js" in r.text


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


# ---------------------------------------------------- AI request routing
def test_interpret_off_without_ai():
    r = client.post("/api/jobs/interpret", json={"query": "best pharma bets"})
    assert r.status_code == 503                    # UI_DISABLE_AI=1
    assert client.post("/api/jobs/interpret", json={}).status_code in (422, 503)


def _run_interpret(monkeypatch, canned, query):
    import time
    monkeypatch.setattr(S, "_ai_backend", lambda: "test")
    monkeypatch.setattr(S, "_ai_text", lambda *a, **k: canned)
    r = client.post("/api/jobs/interpret", json={"query": query})
    assert r.status_code == 200
    job_id = r.json()["job"].split(":")[1]
    for _ in range(50):
        j = client.get(f"/api/jobs/interpret/{job_id}").json()
        if j["state"] != "running":
            break
        time.sleep(0.1)
    assert j["state"] == "done", j.get("error")
    return j["result"]


def test_interpret_routes_and_validates(monkeypatch):
    out = _run_interpret(monkeypatch,
        'Sure! {"intent": "rank", "symbols": [], "n": 500, "order": "worst", '
        '"industry": "pharma", "question": null}', "weakest drug makers")
    assert out["intent"] == "rank" and out["order"] == "worst"
    assert out["n"] == 200                          # clamped
    # made-up tickers are dropped; question intent needs a real symbol
    out = _run_interpret(monkeypatch,
        '{"intent": "question", "symbols": ["NOTREAL"], "question": "x"}', "?")
    assert out["intent"] == "unknown"
    out = _run_interpret(monkeypatch,
        f'{{"intent": "question", "symbols": ["{SOME}"], '
        '"question": "why is it rated so high?"}', "why rated high")
    assert out["intent"] == "question" and out["symbols"] == [SOME]
    # compare with one symbol degrades to company; garbage -> unknown
    out = _run_interpret(monkeypatch,
        f'{{"intent": "compare", "symbols": ["{SOME}"]}}', "compare")
    assert out["intent"] == "company"
    out = _run_interpret(monkeypatch, "no json here at all", "gibberish")
    assert out["intent"] == "unknown"


def test_interpret_candidates_ground_the_model():
    cands = S._candidates_for("analyse colgate palmolive")
    assert "COLPAL" in cands
    assert all(c in S._const_map for c in cands)


# ------------------------- the index comparison (v2) -------------------------
# Everything here must be PARSED OUT OF the stored reports, never recomputed:
# if the page and the downloadable file could disagree, the guarantee is void.

import re                                        # noqa: E402
import relative_index as RI                      # noqa: E402


def _rel(sym):
    r = client.get(f"/api/relative/{sym}")
    assert r.status_code == 200, r.text[:300]
    return r.json()


def test_relative_endpoint_shape():
    d = _rel("PIDILITIND")
    assert d["index"] == "Nifty 50"
    s = d["section"]
    assert s["scored"] and 0 <= s["points"] <= 100
    assert "index" in s["verdict"].lower()
    assert s["measures"] == ["Price ratio", "PAT ratio",
                             "Operating-profit ratio"]
    assert [r["window"] for r in s["windows"]] == [10, 5, 3, 1]
    assert d["workup"]["raw"]["rows"], "raw yearly values missing"


def test_every_number_shown_is_in_the_stored_report():
    """The parsed windows must appear verbatim in the analysis Markdown."""
    sym = "PIDILITIND"
    md = client.get(f"/api/analysis/{sym}").json()["md"]
    for row in _rel(sym)["section"]["windows"]:
        for measure, c in row["cells"].items():
            if c["pct"] is None:
                continue
            assert f"{c['pct']:+d}% · {c['word']}" in md, (measure, c)


def test_relative_matches_the_headline_pillar_bullet():
    """The pillar bullet in the report and the parsed points must agree."""
    for sym in ("PIDILITIND", "COLPAL", "APOLLOHOSP", "CRISIL"):
        md = client.get(f"/api/analysis/{sym}").json()["md"]
        m = re.search(r"\*\*Relative to the index \((\d+)/100\):\*\*", md)
        d = _rel(sym)
        if m:
            assert d["section"]["points"] == int(m.group(1)), sym
        arith = re.search(r"10% × (\d+) \(relative to the index\)", md)
        if arith:
            assert d["section"]["points"] == int(arith.group(1)), sym


def test_comparison_side_is_parsed_and_consistent():
    d = _rel("PIDILITIND")
    c = d["comparison"]
    assert c["long_points"] == d["section"]["points"]
    if c["delta"] is not None:
        assert c["delta"] == c["recent_points"] - c["long_points"]


def test_workup_download_is_the_exact_stored_bytes():
    sym = "PIDILITIND"
    stored = RI.workup_path(S.QA, sym).read_text()
    r = client.get(f"/api/relative_report/{sym}")
    assert r.status_code == 200
    assert "text/markdown" in r.headers["content-type"]
    assert "attachment" in r.headers.get("content-disposition", "")
    assert r.text == stored, "download must be the stored file, byte for byte"


def test_company_without_index_history_is_honest_not_broken():
    """4 companies cannot be compared at any window. They must return a
    parsed, unscored section rather than a 500 or an invented number."""
    for sym in ("DBREALTY", "ENRIN", "SPARC", "TMCV"):
        if sym not in SYMS:
            continue
        d = _rel(sym)
        assert d["section"] is not None, sym
        assert d["section"]["scored"] is False, sym
        assert d["section"]["points"] is None, sym


def test_unknown_symbol_is_a_clean_404():
    assert client.get("/api/relative/NOTACOMPANY").status_code == 404
    assert client.get("/api/relative_report/NOTACOMPANY").status_code == 404


@pytest.mark.parametrize("chunk", range(10))
def test_relative_sweep_every_company(chunk):
    """Every analysed company must parse cleanly — no exceptions, no
    half-parsed tables, and a scored company always has its windows."""
    bad = []
    for sym in SYMS[chunk::10]:
        try:
            d = _rel(sym)
        except Exception as e:
            bad.append((sym, str(e)[:90]))
            continue
        s = d["section"]
        if s is None:
            bad.append((sym, "no section 4"))
        elif s["scored"]:
            if not s["windows"]:
                bad.append((sym, "scored but no window table"))
            elif not (0 <= s["points"] <= 100):
                bad.append((sym, f"points out of range: {s['points']}"))
            for row in s["windows"]:
                for measure, c in row["cells"].items():
                    if c["pct"] is not None and not isinstance(c["pct"], int):
                        bad.append((sym, f"bad pct {c}"))
    assert not bad, f"{len(bad)} companies failed: {bad[:5]}"


def test_all_three_measures_are_always_listed_never_silently_dropped():
    """A measure the stored data cannot span still appears, carrying the
    report's own words. Dropping it would hide that it was considered."""
    d = _rel("COLPAL")
    labels = [r["label"] for r in d["workup"]["ratios"]]
    assert labels == ["Price ratio", "PAT ratio", "Operating-profit ratio"]
    unavailable = [r for r in d["workup"]["ratios"] if r["unavailable"]]
    assert unavailable, "COLPAL has no PAT/OP overlap; that must be stated"
    for r in unavailable:
        assert "too little" in r["unavailable"]
        assert not r["levels"]
    # and the window table marks them not-comparable rather than 0%
    cells = d["section"]["windows"][0]["cells"]
    assert cells["PAT ratio"]["pct"] is None


def test_every_company_lists_exactly_the_three_measures():
    bad = []
    for sym in SYMS[::17]:
        d = _rel(sym)
        labels = [r["label"] for r in (d["workup"] or {}).get("ratios", [])]
        if labels != ["Price ratio", "PAT ratio", "Operating-profit ratio"]:
            bad.append((sym, labels))
    assert not bad, f"measures missing or renamed: {bad[:5]}"


# ---------------- the static (GitHub Pages) export of the Darvas screen

def test_static_export_serves_the_darvas_screen_from_files(tmp_path):
    sys.path.insert(0, str(Path(__file__).resolve().parent / "StaticWebsite"))
    import build_static as BS
    if S.DB.latest() is None:
        pytest.skip("no stored Darvas run")
    info = BS.export_darvas(tmp_path)
    d = tmp_path / "api" / "darvas"
    import json as _json
    assert _json.loads((d / "latest").read_text()) == \
        _json.loads(_json.dumps(S.DB.latest(), default=str))
    assert (d / "report").read_text() == S.DB.report_md()
    tr = _json.loads((d / "trace").read_text())
    assert tr["days"] == 31 and tr["runs"]
    st = _json.loads((d / "run" / "status").read_text())
    assert st["state"] == "idle" and st["static"] is True
    assert info["run_date"] == S.DB.latest()["run_date"]
