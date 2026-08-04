"""
pytest wrapper: every stored report pair must validate clean.

  python3 -m pytest test_reports.py -q      (from this folder)
"""

from pathlib import Path

import validate_reports as V

HERE = Path(__file__).resolve().parent


def test_all_stored_reports_are_clean():
    problems = V.validate_all(HERE)
    assert not problems, f"{len(problems)} problems: {problems[:10]}"


def test_batch_log_has_no_unresolved_failures():
    """A company may fail transiently mid-batch, but the FINAL state must
    be clean: every company in the log either succeeded or was later
    completed (its two MD files exist)."""
    import csv
    log = HERE / "_batch_log.csv"
    if not log.exists():
        return                       # nothing run yet — nothing to assert
    with open(log) as f:
        rows = list(csv.DictReader(f))
    unresolved = [
        r["symbol"] for r in rows
        if r["status"].startswith("fail")
        and not ((HERE / f"{r['symbol']}_analysis.md").exists()
                 and (HERE / f"{r['symbol']}_comparison.md").exists())
    ]
    assert not unresolved, f"companies still failed: {unresolved}"
