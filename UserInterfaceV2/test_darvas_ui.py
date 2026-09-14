"""
test_darvas_ui.py — the Darvas weekly screen through THIS UI's server.

The contract, asserted not assumed: the page payload IS the stored run
record; that record agrees with the downloadable Markdown report (same
symbols, actions and stops in the recommendations table, same buys in
the closing section); the report downloads as exact bytes; the trace
covers the latest run; and the run trigger reaches the skill's bridge
with this UI's own mode (no real engine run is ever started here).
"""

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("UI_DISABLE_AI", "1")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import pytest
from fastapi.testclient import TestClient

import server as S
import darvas_history as DH
import ui_bridge as DB

client = TestClient(S.app)
STORED = DB.LATEST.exists() and DB.REPORT.exists()
skip_no_run = pytest.mark.skipif(not STORED, reason="no stored Darvas run")


@skip_no_run
def test_latest_is_exactly_the_stored_record():
    r = client.get("/api/darvas/latest")
    assert r.status_code == 200
    assert r.json() == json.loads(DB.LATEST.read_text())


@skip_no_run
def test_page_payload_agrees_with_the_downloadable_report():
    rec = client.get("/api/darvas/latest").json()
    md = client.get("/api/darvas/report").text
    parsed = DH.parse_report(md)
    assert parsed["run_date"] == rec["run_date"]
    assert [(r["symbol"], r["action"]) for r in parsed["recommendations"]] \
        == [(r["symbol"], r["action"]) for r in rec["recommendations"]]
    for m, j in zip(parsed["recommendations"], rec["recommendations"]):
        if j["action"] != "SELL":
            assert m["stop_loss"] == pytest.approx(j["stop_loss"], abs=0.01)
    for b in rec["actions"]["buys"]:
        assert f"| **{b['symbol']}** | buy at next open |" in md
    for s in rec["actions"]["sells"]:
        assert f"- {s['symbol']}" in md.split("## Today's actions")[1]


@skip_no_run
def test_report_downloads_as_exact_bytes():
    r = client.get("/api/darvas/report")
    assert r.status_code == 200
    assert r.text == DB.REPORT.read_text()
    assert "attachment" in r.headers.get("content-disposition", "")


@skip_no_run
def test_trace_covers_the_latest_run_and_its_buys():
    rec = client.get("/api/darvas/latest").json()
    tr = client.get("/api/darvas/trace?days=31").json()
    assert tr["days"] == 31 and tr["runs"] and tr["timeline"]
    assert rec["run_date"] in [x["run_date"] for x in tr["runs"]]
    today = {(e["symbol"], e["event"]) for e in tr["timeline"]
             if e["date"] == rec["run_date"]}
    for b in rec["actions"]["buys"]:
        assert (b["symbol"], "BUY") in today
    for s in rec["actions"]["sells"]:
        assert (s["symbol"], "SELL") in today
    # bounds are clamped, never trusted
    assert client.get("/api/darvas/trace?days=99999").json()["days"] == 400


def test_run_trigger_reaches_the_bridge_in_this_uis_mode(monkeypatch):
    calls = []
    monkeypatch.setattr(DB, "start_run",
                        lambda quick=False, runner=None:
                        calls.append(quick) or {"started": True,
                                                "state": "running",
                                                "quick": quick})
    r = client.post("/api/darvas/run")
    assert r.status_code == 200 and r.json()["started"]
    assert calls == [bool(S.DARVAS_QUICK_DEFAULT)]
    client.post("/api/darvas/run?quick=1")
    assert calls[-1] is True


def test_run_status_is_always_answerable():
    r = client.get("/api/darvas/run/status")
    assert r.status_code == 200
    assert r.json()["state"] in ("idle", "running", "done", "error")


def test_the_front_end_offers_the_section():
    html = (HERE / "index.html").read_text()
    js = (HERE / "app.js").read_text()
    assert 'data-q="darvas weekly screen"' in html
    assert "renderDarvas" in js and "api/darvas/latest" in js
    assert f"const DARVAS_QUICK = {S.DARVAS_QUICK_DEFAULT};" in js
