"""
darvas_history.py — the trace: what the skill said, run by run.

Every `analyze.py run` archives itself under
`DarvasAnalysis/history/<run_date>/` (report, ledger, run.json). This
module turns that archive into the complete trace a user needs to
follow the rhythm — for every run in the window, the four verbs it
issued; and for every symbol, its BUY / RAISE STOP / SELL / WATCH
events in date order. Nothing here recomputes anything: the trace is
read straight off what each run wrote.

    python3 darvas_history.py trace [--days 31]
    python3 darvas_history.py backfill      # older runs from git history

`backfill` reconstructs run.json for the runs that predate the
structured record: it reads each committed DARVAS_REPORT.md and
_positions.csv from git, parses the recommendations table and the
ledger, and derives the four verbs the same way the live run does
(BUY/ACCUMULATE rows; SELL rows in the ledger; a RAISE where a held
stop rose against the previous run; WATCH rows as the radar). The
reconstruction is marked `"source": "backfill"` so nobody mistakes it
for a native record.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
REPO = INDIA.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "DarvasAnalysis"
HISTORY = OUT_DIR / "history"
REL_REPORT = ("IndividualStockAnalysis/India/Analysis/"
              "NiftyTotalMarketAnalysis/DarvasAnalysis/DARVAS_REPORT.md")
REL_LEDGER = ("IndividualStockAnalysis/India/Analysis/"
              "NiftyTotalMarketAnalysis/DarvasAnalysis/_positions.csv")


# ------------------------------------------------------------- reading

def load_runs(days: int | None = 31,
              history: Path = HISTORY) -> list[dict]:
    """Every archived run inside the window, oldest first."""
    if not history.exists():
        return []
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat() \
        if days else "0000-00-00"
    runs = []
    for d in sorted(p for p in history.iterdir() if p.is_dir()):
        if d.name < cutoff:
            continue
        rj = d / "run.json"
        if rj.exists():
            try:
                runs.append(json.loads(rj.read_text()))
            except json.JSONDecodeError:
                continue
    return runs


def timeline(runs: list[dict]) -> list[dict]:
    """Per-symbol events in date order, derived from each run's own
    four verbs: BUY (with stop), RAISE STOP (old → new), SELL, and the
    first time a symbol appears on the radar (WATCH, with the price it
    turns into a BUY above)."""
    events = []
    seen_radar: set = set()
    for r in runs:
        d = r["run_date"]
        a = r.get("actions", {})
        for b in a.get("buys", []):
            events.append({"date": d, "symbol": b["symbol"], "event": "BUY",
                           "detail": f"{b.get('action', 'BUY')} at next "
                                     f"open; stop ₹{b['stop_loss']:,.2f}"
                                     if b.get("stop_loss") else "BUY",
                           "stop_loss": b.get("stop_loss")})
        for x in a.get("raises", []):
            events.append({"date": d, "symbol": x["symbol"],
                           "event": "RAISE STOP",
                           "detail": f"₹{x['old']:,.2f} → ₹{x['new']:,.2f}",
                           "stop_loss": x["new"]})
        for s in a.get("sells", []):
            events.append({"date": d, "symbol": s["symbol"],
                           "event": "SELL",
                           "detail": "closed below its box bottom — exit",
                           "stop_loss": None})
        for w in a.get("radar", []):
            key = (w["symbol"], w.get("buy_above"))
            if key in seen_radar:
                continue
            seen_radar.add(key)
            events.append({"date": d, "symbol": w["symbol"],
                           "event": "WATCH",
                           "detail": (f"on the radar — becomes BUY on a "
                                      f"daily close above "
                                      f"₹{w['buy_above']:,.2f}"
                                      if w.get("buy_above")
                                      else "on the radar"),
                           "stop_loss": None})
    order = {"BUY": 0, "RAISE STOP": 1, "SELL": 2, "WATCH": 3}
    events.sort(key=lambda e: (e["date"], order[e["event"]], e["symbol"]))
    return events


def journal(events: list[dict]) -> list[dict]:
    """The trace as a TRADER keeps it, from the raw per-run events: a
    SELL is recorded once — the runs after it (which still carry the
    row) do not sell the stock again; a BUY re-flagged while the
    position is open stays a BUY (the UIs and tests read it so) but is
    marked `repeat` and points back to the first entry. Everything else
    passes through in date order."""
    out, open_since, last = [], {}, {}
    for e in events:
        sym, kind = e["symbol"], e["event"]
        if kind == "SELL":
            if last.get(sym) == "SELL":
                continue
            open_since.pop(sym, None)
        elif kind == "BUY":
            if sym in open_since:
                e = {**e, "repeat": True,
                     "detail": (f"still a BUY — re-flagged by the screen; "
                                f"first entry {open_since[sym]}"
                                + (f"; stop now ₹{e['stop_loss']:,.2f}"
                                   if e.get("stop_loss") else ""))}
            else:
                open_since[sym] = e["date"]
        out.append(e)
        last[sym] = kind
    return out


def full_journal(history: Path = HISTORY,
                 current: dict | None = None) -> list[dict]:
    """Every run ever archived (plus `current`, the run in progress,
    replacing an archived run of the same date) → the cleaned trace."""
    runs = load_runs(None, history)
    if current is not None:
        runs = [r for r in runs if r["run_date"] != current["run_date"]]
        runs.append(current)
        runs.sort(key=lambda r: r["run_date"])
    return journal(timeline(runs))


EVENTS = OUT_DIR / "_events.csv"
EVENT_FIELDS = ["date", "symbol", "event", "stop_loss", "repeat", "detail"]


def save_events(events: list[dict], path: Path = EVENTS) -> None:
    """The trace preserved beside the report, one row per event, exactly
    as the backtests keep theirs."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=EVENT_FIELDS)
        w.writeheader()
        for e in events:
            w.writerow({"date": e["date"], "symbol": e["symbol"],
                        "event": e["event"],
                        "stop_loss": "" if e.get("stop_loss") is None
                        else e["stop_loss"],
                        "repeat": "yes" if e.get("repeat") else "",
                        "detail": e.get("detail", "")})


def _inr(x) -> str:
    return f"₹{float(x):,.2f}"


def render_trace_md(events: list[dict], ledger: list[dict]) -> str:
    """The trade trace section of the report: one line per stock (bought
    when, at what stop, every raise, sold when, where it stands), then
    the complete dated journal. Symbols never bought but carried on the
    ledger (WATCH rows with a stop) are shown too — a raise on them
    applies only to someone who holds them."""
    by: dict[str, list] = {}
    for e in events:
        by.setdefault(e["symbol"], []).append(e)
    status = {r["symbol"]: r for r in ledger}
    A = ["", "---", "", "## The trade trace", "",
         "Every recommendation this screen has ever made, carried run to "
         "run: when a stock was first flagged BUY and at what stop, each "
         "time its stop was raised, and when it was sold. The journal "
         "is preserved beside this report in `_events.csv` and in the "
         "dated `history/` snapshots; a re-flagged BUY on an open "
         "position is noted, not counted as a second entry.", "",
         "| Stock | Bought | Stop at entry | Stop raises | Stop now "
         "| Sold | Status |", "|---|---|---:|---|---:|---|---|"]
    for sym in sorted(by):
        ev = by[sym]
        buys = [e for e in ev if e["event"] == "BUY" and not e.get("repeat")]
        raises = [e for e in ev if e["event"] == "RAISE STOP"]
        sells = [e for e in ev if e["event"] == "SELL"]
        row = status.get(sym, {})
        act = row.get("action", "")
        bought = buys[0]["date"] if buys else "—"
        entry_stop = (_inr(buys[0]["stop_loss"])
                      if buys and buys[0].get("stop_loss") else "—")
        rs = "<br>".join(f"{e['date']}: {e['detail']}" for e in raises) or "—"
        now = _inr(row["stop_loss"]) if row.get("stop_loss") not in \
            (None, "", "None") else "—"
        sold = sells[-1]["date"] if sells and (
            not buys or sells[-1]["date"] >= buys[-1]["date"]) else "—"
        if act == "SELL":
            st = "sold"
        elif act in ("BUY", "ACCUMULATE"):
            st = "held"
        elif act == "WATCH":
            st = "on watch (never a buy)"
        else:
            st = "expired"
        A.append(f"| {sym} | {bought} | {entry_stop} | {rs} | {now} | "
                 f"{sold} | {st} |")
    A += ["", "### The journal", "",
          "*Every event in date order — the same trace the interfaces "
          "show.*", "", "```"]
    for e in events:
        A.append(f"{e['date']}  {e['symbol']:11s} {e['event']:10s} "
                 f"{e.get('detail', '')}")
    A += ["```", ""]
    return "\n".join(A)


def trace(days: int | None = 31, history: Path = HISTORY) -> dict:
    runs = load_runs(days, history)
    cutoff = runs[0]["run_date"] if runs else "9999-99-99"
    ev = [e for e in journal(timeline(load_runs(None, history)))
          if e["date"] >= cutoff]
    by_symbol: dict[str, list] = {}
    for e in ev:
        by_symbol.setdefault(e["symbol"], []).append(e)
    return {"days": days, "runs": [
        {"run_date": r["run_date"], "fetched_at": r.get("fetched_at"),
         "source": r.get("source", "native"),
         "weekly_qualifiers": r.get("weekly_qualifiers"),
         "fully_qualified": r.get("fully_qualified"),
         "actions": r.get("actions", {})} for r in runs],
        "timeline": ev, "by_symbol": by_symbol}


# ------------------------------------------------------------ backfill

def parse_report(md: str) -> dict:
    """The run date and the recommendations table out of a report."""
    m = re.search(r"\*Run (\d{4}-\d\d-\d\d) on data fetched (\S+) ·", md)
    run_date = m.group(1) if m else None
    fetched = m.group(2) if m else None
    rows = []
    sec = md.split("## The recommendations", 1)
    if len(sec) == 2:
        for line in sec[1].split("\n## ", 1)[0].splitlines():
            if not line.startswith("| ") or line.startswith("| Stock") \
                    or line.startswith("|---"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            action = cells[1].replace("*", "")
            bm = re.match(r"([\d,.]+)–([\d,.]+)", cells[2])
            sm = re.search(r"([\d,.]+)", cells[4])
            rows.append({
                "symbol": cells[0], "action": action,
                "downgraded": "DOWNGRAD" in line.upper(),
                "box_bottom": float(bm.group(1).replace(",", "")) if bm else None,
                "box_top": float(bm.group(2).replace(",", "")) if bm else None,
                "stop_loss": (float(sm.group(1).replace(",", ""))
                              if sm and cells[4] != "exit" else None),
                "buy_above": (float(bm.group(2).replace(",", ""))
                              if bm and action == "WATCH" else None),
                "earnings_power": cells[-2], "new_age": cells[-1]})
    return {"run_date": run_date, "fetched_at": fetched,
            "recommendations": rows}


def derive_actions(recs: list[dict], ledger: list[dict],
                   prev_stops: dict) -> dict:
    buys = [{"symbol": r["symbol"], "action": r["action"],
             "entry": "buy at next open", "stop_loss": r["stop_loss"],
             "last_close": None, "risk_pct": None, "wide": False}
            for r in recs if r["action"] in ("BUY", "ACCUMULATE")]
    radar = [{"symbol": r["symbol"], "buy_above": r.get("buy_above")}
             for r in recs if r["action"] == "WATCH"
             and not r.get("downgraded")]
    downs = [{"symbol": r["symbol"],
              "why": "downgraded (falling earnings power): never a buy"}
             for r in recs if r.get("downgraded")]
    sells = [{"symbol": row["symbol"]} for row in ledger
             if row.get("action") == "SELL"]
    raises = []
    for row in ledger:
        old, new = prev_stops.get(row["symbol"]), row.get("stop_loss")
        try:
            if old and new and float(new) > float(old) + 1e-9:
                raises.append({"symbol": row["symbol"], "old": float(old),
                               "new": float(new)})
        except ValueError:
            continue
    return {"buys": buys, "raises": raises, "sells": sells,
            "radar": radar, "downgraded": downs}


def _git_show(rev: str, path: str) -> str | None:
    p = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=REPO,
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None


def backfill(history: Path = HISTORY) -> list[str]:
    """Reconstruct run.json for every report commit whose run date has
    no native record yet. Returns the run dates written."""
    log = subprocess.run(
        ["git", "log", "--format=%H", "--reverse", "--", REL_REPORT],
        cwd=REPO, capture_output=True, text=True).stdout.split()
    written, prev_stops, last_by_date = [], {}, {}
    for rev in log:
        md = _git_show(rev, REL_REPORT)
        if not md:
            continue
        parsed = parse_report(md)
        if not parsed["run_date"]:
            continue
        led_txt = _git_show(rev, REL_LEDGER) or ""
        ledger = list(csv.DictReader(io.StringIO(led_txt)))
        last_by_date[parsed["run_date"]] = (parsed, ledger, md)
    for run_date in sorted(last_by_date):
        parsed, ledger, md = last_by_date[run_date]
        target = history / run_date
        if (target / "run.json").exists():
            rec = json.loads((target / "run.json").read_text())
            if rec.get("source", "native") == "native":
                prev_stops = {r["symbol"]: r.get("stop_loss")
                              for r in rec.get("ledger", [])}
                continue
        actions = derive_actions(parsed["recommendations"], ledger,
                                 prev_stops)
        record = {"run_date": run_date, "fetched_at": parsed["fetched_at"],
                  "source": "backfill",
                  "recommendations": parsed["recommendations"],
                  "actions": actions, "ledger": ledger}
        target.mkdir(parents=True, exist_ok=True)
        (target / "run.json").write_text(json.dumps(record, indent=1))
        (target / "DARVAS_REPORT.md").write_text(md)
        with open(target / "_positions.csv", "w", newline="") as fh:
            if ledger:
                w = csv.DictWriter(fh, fieldnames=list(ledger[0].keys()))
                w.writeheader()
                w.writerows(ledger)
        prev_stops = {r["symbol"]: r.get("stop_loss") for r in ledger}
        written.append(run_date)
    return written


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("trace")
    t.add_argument("--days", type=int, default=31)
    sub.add_parser("backfill")
    args = ap.parse_args()
    if args.cmd == "backfill":
        print("backfilled:", ", ".join(backfill()) or "nothing to do")
    else:
        tr = trace(args.days)
        print(f"{len(tr['runs'])} runs in the last {args.days} days, "
              f"{len(tr['timeline'])} events")
        for e in tr["timeline"]:
            print(f"  {e['date']}  {e['symbol']:11s} {e['event']:10s} "
                  f"{e['detail']}")


if __name__ == "__main__":
    main()
