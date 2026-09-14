"""
ui_bridge.py — the one door both user interfaces use to reach this skill.

Both UIs render the Darvas section from the SAME machine-readable run
record the report was written from (`darvas_latest.json`), so page and
file can never disagree; the report itself is served as exact bytes for
download; the trace comes from the archived runs; and "run this week's
screen" starts the real engine (`analyze.py run`) in the background,
with a status file the page polls — a long fetch can never time out a
request.

    latest()            the current run record (dict) or None
    report_md()         the current report, exact bytes
    trace(days)         per-run four verbs + per-symbol timeline
    start_run(quick)    launch analyze.py run [--quick]; refuses a
                        second concurrent run
    run_status()        {"state": idle|running|done|error, ...}
"""

from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import darvas_history as DH      # noqa: E402

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "DarvasAnalysis"
LATEST = OUT_DIR / "darvas_latest.json"
REPORT = OUT_DIR / "DARVAS_REPORT.md"
STATUS = OUT_DIR / "_run_status.json"
RUN_LOG = OUT_DIR / "_run.log"

_lock = threading.Lock()


def latest() -> dict | None:
    if not LATEST.exists():
        return None
    try:
        return json.loads(LATEST.read_text())
    except json.JSONDecodeError:
        return None


def report_md() -> str | None:
    return REPORT.read_text() if REPORT.exists() else None


def trace(days: int = 31) -> dict:
    return DH.trace(days)


def run_status() -> dict:
    if not STATUS.exists():
        return {"state": "idle"}
    try:
        st = json.loads(STATUS.read_text())
    except json.JSONDecodeError:
        return {"state": "idle"}
    if st.get("state") == "running" and st.get("pid"):
        try:                       # a crashed runner must not look alive
            os.kill(int(st["pid"]), 0)
        except OSError:
            st["state"] = "error"
            st["error"] = "the runner process is gone"
            _write_status(st)
    tail = ""
    if RUN_LOG.exists():
        tail = "\n".join(RUN_LOG.read_text().splitlines()[-8:])
    st["log_tail"] = tail
    return st


def _write_status(st: dict) -> None:
    STATUS.write_text(json.dumps(st))


def start_run(quick: bool = False, runner=None) -> dict:
    """Launch the weekly engine. `runner` (tests) replaces the real
    subprocess with a callable that returns an exit code."""
    with _lock:
        st = run_status()
        if st.get("state") == "running":
            return {"started": False, "state": "running",
                    "note": "a run is already in progress"}
        now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        st = {"state": "running", "started": now, "quick": quick,
              "pid": None}
        _write_status(st)

    def work():
        code = None
        try:
            if runner is not None:
                code = runner()
            else:
                cmd = [sys.executable, str(HERE / "analyze.py"), "run"]
                if quick:
                    cmd.append("--quick")
                with open(RUN_LOG, "w") as log:
                    proc = subprocess.Popen(cmd, cwd=str(HERE), stdout=log,
                                            stderr=subprocess.STDOUT)
                    st["pid"] = proc.pid
                    _write_status(st)
                    code = proc.wait()
        except Exception as e:                # noqa: BLE001
            _write_status({**st, "state": "error", "error": str(e)[:300],
                           "pid": None})
            return
        done = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        _write_status({**st, "state": "done" if code == 0 else "error",
                       "finished": done, "exit_code": code, "pid": None,
                       "error": None if code == 0 else
                       f"analyze.py exited with {code}"})

    threading.Thread(target=work, daemon=True).start()
    return {"started": True, "state": "running", "quick": quick}
