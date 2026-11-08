"""
validate_demergers.py — test the skill's demerger list against NSE's own
record (Announcements/demerger_ground_truth.py).

    python3 validate_demergers.py            # writes the check and exits 1 on a miss

RECALL   every universe company whose corporate-action register carries a
         demerger record date in the window must be in the skill's list as
         a demerger (confirmed or probable). A company the register names
         and the skill lacks, or holds only as a merger / other, is a MISS.
PRECISION  every demerger the skill marks LISTED or at RECORD DATE must
         have a matching register row; a confirmed demerger with no record
         date yet cannot be checked against the register and is listed as
         "pending — not yet verifiable". A confirmed demerger whose judge
         read says nothing is separated is a FALSE POSITIVE.
ARRIVAL  for each register demerger, whether a resulting company appeared
         in the price file after the record date (newlist rows).

Output: Analysis/NiftyTotalMarketAnalysis/SpinOffAnalysis/SPINOFF_GROUND_TRUTH_CHECK.md
and _ground_truth_check.csv; exit code 1 when any miss or false positive.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
GT = INDIA / "Announcements" / "NiftyTotalMarket" / "_demerger_ground_truth.csv"
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "SpinOffAnalysis"
LATEST = OUT_DIR / "spinoff_latest.json"
CHECK_MD = OUT_DIR / "SPINOFF_GROUND_TRUTH_CHECK.md"
CHECK_CSV = OUT_DIR / "_ground_truth_check.csv"
SPIN = ("demerger", "subsidiary_listing", "scheme_other")
DEMERGER_RX = re.compile(r"de-?merg|spin[\s-]?off|hiv(e|ing)[\s-]?off", re.I)


def load_ground_truth(path: Path = GT) -> list[dict]:
    with open(path) as fh:
        return list(csv.DictReader(fh))


def register_demergers(gt: list[dict]) -> dict[str, dict]:
    """{parent symbol: {dates, purposes}} for universe demerger record
    dates — the 'bc' file and the API read the same register."""
    out: dict[str, dict] = {}
    for r in gt:
        if r["source"] not in ("bc", "api") or r.get("in_universe") != "yes":
            continue
        if not DEMERGER_RX.search(r["purpose"]):
            continue
        d = out.setdefault(r["symbol"], {"dates": set(), "purposes": set(), "company": r["company"]})
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["date"] or ""):
            d["dates"].add(r["date"])
        d["purposes"].add(r["purpose"])
    return out


def new_listings(gt: list[dict]) -> dict[str, str]:
    return {r["symbol"]: r["date"] for r in gt if r["source"] == "newlist" and re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["date"] or "")}


def check(situations: list[dict], gt: list[dict], today: dt.date | None = None) -> dict:
    today = today or dt.date.today()
    reg = register_demergers(gt)
    arrivals = new_listings(gt)
    by_sym: dict[str, list[dict]] = {}
    for s in situations:
        by_sym.setdefault(s["symbol"], []).append(s)

    recall_rows, misses = [], []
    for sym, d in sorted(reg.items()):
        sits = by_sym.get(sym, [])
        spin = [s for s in sits if s["kind"] in SPIN]
        dem = [s for s in spin if s["kind"] == "demerger" and s["confidence"][0] in ("confirmed", "probable")]
        verdict = ("captured" if dem else "captured as scheme/listing only" if spin
                   else "held as other restructuring only" if sits else "MISSING")
        arrived = sorted(a for a, when in arrivals.items()
                         if any(when >= rd for rd in d["dates"]) and
                         any(abs((dt.date.fromisoformat(when) - dt.date.fromisoformat(rd)).days) <= 75 for rd in d["dates"]))
        resulting = next((s["facts"].get("resulting_company", "") for s in dem if s["facts"].get("resulting_company")), "")
        row = {"symbol": sym, "company": d["company"], "record_dates": "; ".join(sorted(d["dates"])),
               "purpose": "; ".join(sorted(d["purposes"]))[:120], "skill_kind": "/".join(sorted({s["kind"] for s in sits})) or "—",
               "skill_confidence": "/".join(sorted({s["confidence"][0] for s in spin})) or "—",
               "skill_stage": "/".join(sorted({s["stage"] for s in dem})) or "—",
               "resulting_company_read": resulting,
               "new_symbols_near_record_date": ", ".join(arrived[:4]), "verdict": verdict}
        recall_rows.append(row)
        if verdict != "captured":
            misses.append(row)

    precision_rows, false_pos, pending = [], [], []
    for sym, sits in sorted(by_sym.items()):
        for s in sits:
            if s["kind"] != "demerger" or s["confidence"][0] != "confirmed":
                continue
            j = s.get("judge") or {}
            said_nothing = bool(re.search(r"nothing (is )?(separated|spun|demerged)|not a demerger|only (an? )?(amalgamation|merger)",
                                          f"{j.get('what_is_spun', '')} {j.get('reason', '')}", re.I))
            at_record = s["stage"] in ("record_date", "listed") or s.get("listed_on")
            in_reg = sym in reg
            is_spin = s.get("facts", {}).get("is_the_spin")
            if said_nothing:
                v = "FALSE POSITIVE (judge: nothing separated)"
            elif is_spin and s.get("listed_on"):
                # the company IS the resulting company: the register holds the
                # PARENT's record date; the company's own listing date (NSE's
                # equity list) is the verification
                v = f"verified by NSE's equity list — this company is the listed resulting company (listed {s['listed_on']})"
            elif at_record and not in_reg:
                v = "FALSE POSITIVE (record date claimed, register has none)"
            elif at_record and in_reg:
                v = "verified by the register"
            else:
                v = "pending — not yet verifiable (no record date yet)"
            row = {"symbol": sym, "company": s["company"], "skill_stage": s["stage"],
                   "listed_on": s.get("listed_on") or "", "register_dates": "; ".join(sorted(reg[sym]["dates"])) if in_reg else "",
                   "what_is_spun": (j.get("what_is_spun") or "")[:100], "verdict": v}
            precision_rows.append(row)
            (false_pos if v.startswith("FALSE") else pending if v.startswith("pending") else []).append(row)
    return {"register": reg, "recall": recall_rows, "misses": misses, "precision": precision_rows,
            "false_positives": false_pos, "pending": pending,
            "summary": {"register_demergers": len(reg), "captured": len(reg) - len(misses), "missed": len(misses),
                        "confirmed_in_skill": len(precision_rows),
                        "verified": sum(1 for r in precision_rows if r["verdict"].startswith("verified")),
                        "pending": len(pending), "false_positives": len(false_pos)}}


def render(res: dict, run_date: str) -> str:
    s = res["summary"]
    A = ["# Demerger list checked against NSE's register", "",
         f"*Skill run {run_date} · register from the daily bhavcopy bundles' corporate-actions file and "
         f"NSE's corporate-actions API · {s['register_demergers']} universe demerger record dates in the window.*", "",
         "| | Count |", "|---|---:|",
         f"| Demergers in NSE's register (universe) | {s['register_demergers']} |",
         f"| …captured by the skill as demergers | {s['captured']} |",
         f"| …MISSED | {s['missed']} |",
         f"| Confirmed demergers in the skill | {s['confirmed_in_skill']} |",
         f"| …verified by a register record date | {s['verified']} |",
         f"| …pending (no record date yet, not verifiable) | {s['pending']} |",
         f"| …FALSE POSITIVES | {s['false_positives']} |", ""]
    A += ["## Recall — every register demerger, and what the skill holds", "",
          "| Parent | Record date(s) | Purpose | Skill kind | Confidence | Stage | Resulting company read | New symbols near the record date | Verdict |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in res["recall"]:
        A.append(f"| **{r['symbol']}** | {r['record_dates']} | {r['purpose'][:60]} | {r['skill_kind']} | {r['skill_confidence']} | "
                 f"{r['skill_stage']} | {r['resulting_company_read'][:40]} | {r['new_symbols_near_record_date']} | {r['verdict']} |")
    A += ["", "## Precision — every confirmed demerger in the skill", "",
          "| Company | Stage | Listed on | Register date(s) | What is spun (judge) | Verdict |", "|---|---|---|---|---|---|"]
    for r in res["precision"]:
        A.append(f"| **{r['symbol']}** | {r['skill_stage']} | {r['listed_on']} | {r['register_dates']} | {r['what_is_spun'][:80]} | {r['verdict']} |")
    A += ["", "## Reading the result", "",
          "- A register demerger the skill lacks is a miss in CAPTURE; one held as merger or other is a miss in CLASSIFICATION.",
          "- A confirmed demerger with a record date the register does not know is a false positive; one the judge reads as an amalgamation is too.",
          "- Confirmed demergers still before their record date cannot be verified against the register; they are listed as pending, and the register will settle them as it fills.",
          "- New symbols within 75 days after a record date show the resulting company arriving in the price file.", ""]
    return "\n".join(A)


def main() -> int:
    if not GT.exists() or not LATEST.exists():
        print("ground truth or skill run missing", file=sys.stderr)
        return 2
    gt = load_ground_truth()
    rec = json.loads(LATEST.read_text())
    res = check(rec["situations"], gt)
    CHECK_MD.write_text(render(res, rec["meta"]["run_date"]))
    with open(CHECK_CSV, "w", newline="") as fh:
        rows = [{"check": "recall", **r} for r in res["recall"]] + [{"check": "precision", **r} for r in res["precision"]]
        keys = sorted({k for r in rows for k in r})
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    s = res["summary"]
    print(json.dumps(s))
    return 1 if (s["missed"] or s["false_positives"]) else 0


if __name__ == "__main__":
    sys.exit(main())
