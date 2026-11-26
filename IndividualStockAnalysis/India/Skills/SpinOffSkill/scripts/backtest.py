"""
backtest.py — run the demerger skill AS OF a past date over a past
window, check its list against NSE's register for that window, and keep
everything in its own folder.

    python3 backtest.py --from 2024-04-01 --to 2025-03-31 --label FY2024-25
    python3 backtest.py --from 2024-04-01 --label 2024-04_to_today

What a backtest sees: the filings dated inside the window (the store must
already reach back that far: Announcements/fetch_announcements.py --days N),
the calls up to the as-of month, NSE's register record dates up to the
as-of date (Announcements/demerger_ground_truth.py --days N), the equity
list. What it does not see: anything dated after the as-of date. The run
is list-only (judge classification and listing status; no rationale,
numbers, documents or offerings), so what is measured is the LIST.

Outputs, under Analysis/NiftyTotalMarketAnalysis/SpinOffBacktest/<label>/:
  SPINOFF_REPORT.md, spinoff_latest.json, _situations.csv …   the run as of --to
  SPINOFF_GROUND_TRUTH_CHECK.md, _ground_truth_check.csv       the register check
  BACKTEST_SUMMARY.md                                          both, side by side
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze as AZ                      # noqa: E402
import validate_demergers as VD           # noqa: E402

INDIA = HERE.parent.parent.parent
BACKTESTS = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "SpinOffBacktest"
GT = INDIA / "Announcements" / "NiftyTotalMarket" / "_demerger_ground_truth.csv"


def run_backtest(frm: dt.date, to: dt.date, label: str, workers: int = 4, quick: bool = False,
                 runner=None) -> dict:
    out = BACKTESTS / label
    out.mkdir(parents=True, exist_ok=True)
    days = (to - frm).days
    args = SimpleNamespace(as_of=to.isoformat(), only="", refresh=False, days=days, no_bse=True,
                           quick=quick, no_calls=False, fetch_docs=False, workers=workers,
                           out=str(out), register=str(GT), list_only=True)
    record = AZ.cmd_run(args, runner=runner)
    gt = VD.load_ground_truth(GT)
    res = VD.check(record["situations"], gt, to, days=days)
    (out / VD.CHECK_MD.name).write_text(VD.render(res, to.isoformat()))
    rows = [{"check": "recall", **r} for r in res["recall"]] + [{"check": "precision", **r} for r in res["precision"]]
    if rows:
        with open(out / VD.CHECK_CSV.name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=sorted({k for r in rows for k in r}))
            w.writeheader()
            w.writerows(rows)
    (out / "BACKTEST_SUMMARY.md").write_text(summary(frm, to, label, record, res))
    (out / "backtest_check.json").write_text(json.dumps(
        {"from": frm.isoformat(), "to": to.isoformat(), "summary": res["summary"],
         "misses": res["misses"], "false_positives": res["false_positives"]}, indent=1, default=str))
    return {"record": record, "check": res, "folder": str(out)}


def summary(frm: dt.date, to: dt.date, label: str, record: dict, res: dict) -> str:
    sits = record["situations"]
    conf = [s for s in sits if s["kind"] == "demerger" and s["confidence"][0] == "confirmed"]
    prob = [s for s in sits if s["kind"] == "demerger" and s["confidence"][0] == "probable"]
    ind = [s for s in sits if s["kind"] == "demerger" and s["confidence"][0] == "indicated"]
    done = [s for s in sits if s["kind"] == "demerger" and (s["confidence"][0] == "completed" or s["facts"].get("mature"))]
    disc = [s for s in sits if s["facts"].get("resolution") in AZ.SO.RESOLUTION_DISCARD and s["confidence"][0] == "other"]
    part = [s for s in sits if s["kind"] == "subsidiary_listing" and s["confidence"][0] == "confirmed"]
    part += [s["also_partial"] for s in sits if s.get("also_partial")]
    not_listing = [s for s in sits if s["kind"] == "subsidiary_listing" and s["confidence"][0] == "other"]
    s = res["summary"]
    A = [f"# Backtest {label} — the demerger skill as of {to}, filings {frm} → {to}", "",
         f"*List-only run: the judge classified each situation from the complete filings and calls up to {to}; "
         f"no rationale, numbers or offerings. Register: NSE's corporate-actions record dates between {frm} and {to}.*", "",
         "## Ground truth vs the skill", "",
         "| | Count |", "|---|---:|",
         f"| Universe demergers with a record date in the window (NSE register) | {s['register_demergers']} |",
         f"| …captured by the skill as confirmed / probable demergers | {s['captured']} |",
         f"| …MISSED (absent, or held as merger / other) | {s['missed']} |",
         f"| Confirmed demergers in the skill as of {to} | {s['confirmed_in_skill']} |",
         f"| …verified by a register record date or the company's own listing | {s['verified'] - s.get('verified_later', 0)} |",
         f"| …verified by a record date that came AFTER {to} (the register up to today) | {s.get('verified_later', 0)} |",
         f"| …pending (no record date to date) | {s['pending']} |",
         f"| …FALSE POSITIVES | {s['false_positives']} |",
         f"| Partial spin-offs (subsidiary IPOs, announced or listed) | {len(part)} |",
         f"| …flagged as a subsidiary listing and found not to be one (excluded) | {len(not_listing)} |",
         f"| …of the confirmed, read as in progress from the filings' text | {sum(1 for c in conf if c['facts'].get('resolved_from_text'))} |",
         f"| Completed demergers (dated) | {len(done)} |",
         f"| Probable / indicated rows discarded on reading | {len(disc)} |",
         f"| Probable rows left (no judge answer) | {len(prob)} |", f"| Indicated demergers | {len(ind)} |",
         f"| Situations in all | {len(sits)} |", ""]
    A += ["## Every register demerger in the window", "",
          "| Parent | Record date(s) | Skill kind | Confidence | Stage as of the run | Resulting company listed | Verdict |",
          "|---|---|---|---|---|---|---|"]
    for r in res["recall"]:
        A.append(f"| **{r['symbol']}** | {r['record_dates']} | {r['skill_kind']} | {r['skill_confidence']} | {r['skill_stage']} | "
                 f"{r['resulting_company_listed']} | {r['verdict']} |")
    A += ["", "## The skill's confirmed demergers as of the run", "",
          "| Company | Stage | Listing | Register verdict |", "|---|---|---|---|"]
    pv = {r["symbol"]: r["verdict"] for r in res["precision"]}
    for c in conf:
        A.append(f"| **{c['symbol']}** | {c['stage']} | {c['listing']['short']} | {pv.get(c['symbol'], '')} |")
    A += ["", "## Partial spin-offs as of the run", "",
          "| Company | Subsidiary | IPO stage | Listed on | Source of the date |", "|---|---|---|---|---|"]
    for p in sorted(part, key=lambda s: (s["stage"] != "listed", s["symbol"])):
        f = p["facts"]
        A.append(f"| **{p['symbol']}** | {f.get('subsidiary', '')[:60]} | {f.get('ipo_stage', '')} | "
                 f"{p.get('listed_on') or ''} | {f.get('subsidiary_listing_source', '')} |")
    A += ["", "## Completed demergers as of the run", "",
          "| Company | Role | Completed | Source of the date |", "|---|---|---|---|"]
    for d in sorted(done, key=lambda s: AZ.completed_date_of(s), reverse=True):
        f = d["facts"]
        A.append(f"| **{d['symbol']}** | {f.get('completed_role', 'demerged company')} | "
                 f"{f.get('completed_date') or f.get('record_date', '')} | "
                 f"{f.get('completed_date_source') or 'NSE register (record date)'} |")
    A += ["", "## Misses, with what the skill held", ""]
    if res["misses"]:
        for m in res["misses"]:
            A.append(f"- **{m['symbol']}** ({m['company']}): register {m['record_dates']} · skill holds "
                     f"{m['skill_kind']} / {m['skill_confidence']} / {m['skill_stage']} → {m['verdict']}")
    else:
        A.append("- none")
    A += ["", "## False positives, with the judge's read", ""]
    if res["false_positives"]:
        for f in res["false_positives"]:
            A.append(f"- **{f['symbol']}**: {f['verdict']} — stage {f['skill_stage']}, listed_on {f['listed_on'] or '—'}; "
                     f"judge: “{f['what_is_spun']}”")
    else:
        A.append("- none")
    A.append("")
    return "\n".join(A)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="frm", required=True)
    ap.add_argument("--to", default=dt.date.today().isoformat())
    ap.add_argument("--label", required=True)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--quick", action="store_true", help="no judge")
    a = ap.parse_args()
    r = run_backtest(dt.date.fromisoformat(a.frm), dt.date.fromisoformat(a.to), a.label, a.workers, a.quick)
    print(json.dumps(r["check"]["summary"]), file=sys.stderr)
    print(f"backtest written to {r['folder']}", file=sys.stderr)


if __name__ == "__main__":
    main()
