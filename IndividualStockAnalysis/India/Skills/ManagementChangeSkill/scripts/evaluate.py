"""
evaluate.py — does the skill miss anything, and is what it reports right?

Eight checks on a finished run, each against something the skill's own
detector did not decide:

  E1 coverage      every management / takeover filing of the window: read,
                   or why not — nothing dropped silently
  E2 ownership     NSE's shareholding register: every company whose promoter
                   holding moved five points or crossed 50% / 25% / nil must
                   carry a verdict; the ones read as "no change" are listed
  E3 open offers   every company with an open-offer filing must be read as a
                   change of control (completed or in progress)
  E4 rosters       the call transcripts' own list of management: a seat whose
                   holder differs between the first and last call of the
                   window must be a reported change
  E5 headlines     filings whose HEADLINE names a CEO / MD / CFO coming or
                   going (the exchange's label, independent of the text read):
                   the company must have a reported change or a recorded
                   reason why not
  E6 unreadable    management filings whose PDF gave no text (scans): listed,
                   with what their headlines say
  E7 labelled set  a hand-labelled sample of filings (`evals/labelled_filings.csv`):
                   precision and recall of the mechanical flag and of the
                   final list
  E8 quotes        every reported change: names and quote found in the documents

Writes MANAGEMENT_CHANGE_EVAL.md and _eval.json beside the report. Exit code
is non-zero when a hard check fails (E2/E3 without a verdict, E8 below 90%).

Usage:  python3 evaluate.py [--out DIR]
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mgmt as M            # noqa: E402
import analyze as AZ        # noqa: E402

LABELS = HERE.parent / "evals" / "labelled_filings.csv"
REVIEWED = HERE.parent / "evals" / "reviewed_exceptions.csv"

HEAD_ROLE_RX = re.compile(r"chief\s+executive|\bc\.?e\.?o\b|managing\s+director|\bm\.?d\.?\s*(?:&|and)\s*c\.?e\.?o|\bcmd\b|chief\s+financ|\bc\.?f\.?o\b|director\s*\(?finance", re.I)
HEAD_EVENT_RX = re.compile(r"(?<!re-)(?<!re)appoint|resign|cessation|retire|superannuat|demise|step\w*\s+down|elevat|relinquish|takes?\s+(?:over|charge)|assum", re.I)
HEAD_NOT_RX = re.compile(r"re-?\s?appoint|independent\s+director|company\s+secretary|subsidiar|auditor", re.I)


def seat_of_headline(h: str) -> str:
    if not (HEAD_ROLE_RX.search(h) and HEAD_EVENT_RX.search(h)) or HEAD_NOT_RX.search(h):
        return ""
    return "CFO" if re.search(r"chief\s+financ|\bc\.?f\.?o\b|director\s*\(?finance", h, re.I) and not re.search(
        r"chief\s+executive|\bc\.?e\.?o\b|managing\s+director", h, re.I) else "CEO/MD"


def reviewed() -> dict[tuple[str, str], str]:
    """Exceptions a person has read and explained: {(check, symbol): note}."""
    out = {}
    if REVIEWED.exists():
        with open(REVIEWED, newline="") as fh:
            for r in csv.DictReader(fh):
                out[(r["check"], r["symbol"])] = r.get("note", "")
    return out


def evaluate(record: dict) -> dict:
    meta = record["meta"]
    today = dt.date.fromisoformat(meta["run_date"])
    start, end = meta["window_from"], meta["window_to"]
    days = (today - dt.date.fromisoformat(start)).days
    cos = {c["symbol"]: c for c in record["companies"]}
    seat_groups = {s: {ch["group"] for ch in c.get("seat_changes", []) if not ch.get("dropped")} for s, c in cos.items()}
    seat_any = {s: [ch for ch in c.get("seat_changes", [])] for s, c in cos.items()}
    rev = reviewed()
    out: dict = {"run_date": meta["run_date"], "window": [start, end]}

    # ---- E1 coverage
    idx = [r for r in M.MF.read_csv(M.MF.FILINGS) if start <= r["date"] <= end and r["symbol"] in cos]
    by = Counter((r.get("read_status") or "unread").split(":")[0] for r in idx)
    cat = defaultdict(Counter)
    for r in idx:
        cat[r["category"]][(r.get("read_status") or "unread").split(":")[0]] += 1
    out["E1"] = {"filings": len(idx), "by_status": dict(by), "read_pct": round(100 * by.get("read", 0) / max(1, len(idx)), 1),
                 "by_category": {k: dict(v) for k, v in sorted(cat.items())},
                 "unread": [r for r in idx if not r.get("read_status")][:20]}

    # ---- E2 ownership vs the shareholding register
    moves = M.shareholding_moves(M.MF.read_csv(M.MF.SHP), today, days)
    major = {s: v for s, v in moves.items() if v["level"] == "major" and s in cos}
    rows, no_verdict, read_none = [], [], []
    for s, v in sorted(major.items(), key=lambda kv: -abs(kv[1]["change"])):
        o = cos[s].get("ownership") or {}
        row = {"symbol": s, "base": v["base"], "latest": v["latest"], "change": v["change"], "crossed": v["crossed"],
               "verdict": o.get("verdict", ""), "what": o.get("what_happened", ""), "reviewed": rev.get(("E2", s), "")}
        rows.append(row)
        if not o.get("verdict"):
            no_verdict.append(s)
        elif o["verdict"] == "none":
            read_none.append(s)
    out["E2"] = {"major_moves": len(major), "with_verdict": len(major) - len(no_verdict), "no_verdict": no_verdict,
                 "by_verdict": dict(Counter(r["verdict"] or "no verdict" for r in rows)),
                 "read_as_none": read_none, "read_as_none_unreviewed": [s for s in read_none if ("E2", s) not in rev], "rows": rows}

    # ---- E3 open offers
    store = M.load_filings(today, days)
    oo = defaultdict(list)
    for r in store:
        if r["category"] in AZ.OPEN_OFFER_CATEGORIES and r["symbol"] in cos:
            oo[r["symbol"]].append(r["date"])
    bad = []
    for s in sorted(oo):
        v = (cos[s].get("ownership") or {}).get("verdict", "")
        if v not in ("change_of_control", "control_change_in_progress"):
            bad.append({"symbol": s, "verdict": v or "no verdict", "what": (cos[s].get("ownership") or {}).get("what_happened", ""),
                        "reviewed": rev.get(("E3", s), "")})
    out["E3"] = {"companies_with_open_offer_filing": len(oo), "read_as_control_change": len(oo) - len(bad), "others": bad,
                 "unreviewed": [b["symbol"] for b in bad if not b["reviewed"]]}

    # ---- E4 rosters
    miss, n_rost, n_changed = [], 0, 0
    for s, c in cos.items():
        text = M.call_text(s)
        if not text:
            continue
        n_rost += 1
        for rc in M.roster_changes(s, today, text=text, company=c.get("company", "")):
            n_changed += 1
            group = "CFO" if rc["seat"] == "CFO" else "CEO/MD"
            if group in seat_groups.get(s, set()):
                continue
            dropped = [ch for ch in seat_any.get(s, []) if ch.get("dropped") and ch["group"] == group]
            miss.append({"symbol": s, "seat": rc["seat"], "before": rc["before"], "after": rc["after"],
                         "from_call": rc["from_call"], "to_call": rc["to_call"],
                         "skill": ("dropped: " + dropped[0]["dropped"]) if dropped else (
                             "judge read, no change" if AZ.J.ok(c.get("seat_judge")) else "not a candidate"),
                         "reviewed": rev.get(("E4", s), "")})
    out["E4"] = {"companies_with_transcripts": n_rost, "seats_whose_roster_changed": n_changed,
                 "reported_by_skill": n_changed - len(miss), "not_reported": miss,
                 "unreviewed": [m["symbol"] for m in miss if not m["reviewed"]]}

    # ---- E5 headlines
    heads = defaultdict(lambda: defaultdict(list))
    for r in store:
        g = seat_of_headline(r["headline"])
        if g and r["symbol"] in cos:
            heads[r["symbol"]][g].append(r)
    for r in idx:                                   # also the filings that gave no text
        if r.get("read_status") != "read":
            g = seat_of_headline(r["headline"])
            if g:
                heads[r["symbol"]][g].append(r)
    hmiss, n_head = [], 0
    for s, gs in heads.items():
        for g, rs in gs.items():
            n_head += 1
            if g in seat_groups.get(s, set()):
                continue
            dropped = [ch for ch in seat_any.get(s, []) if ch.get("dropped")]
            hmiss.append({"symbol": s, "group": g, "headline": rs[0]["headline"][:200], "date": rs[0]["date"],
                          "attachment": rs[0].get("attachment", ""),
                          "skill": ("; ".join(sorted({f"{ch['seat']}: {ch['dropped']}" for ch in dropped}))[:260] if dropped else (
                              "judge read, no change" if AZ.J.ok(cos[s].get("seat_judge")) else "not a candidate")),
                          "reviewed": rev.get(("E5", s), "")})
    out["E5"] = {"company_seats_named_in_headlines": n_head, "reported_by_skill": n_head - len(hmiss), "not_reported": hmiss,
                 "unreviewed": [m["symbol"] for m in hmiss if not m["reviewed"]]}

    # ---- E6 unreadable
    blind = [r for r in idx if (r.get("read_status") or "").startswith(("no-text", "failed", "skipped", "no-attachment"))
             and r["category"] != "Disclosure under SEBI Takeover Regulations"]
    out["E6"] = {"management_filings_without_text": len(blind), "companies": len({r["symbol"] for r in blind}),
                 "with_a_seat_in_the_headline": sum(1 for r in blind if seat_of_headline(r["headline"])),
                 "rows": [{k: r[k] for k in ("date", "symbol", "category", "headline", "read_status", "attachment")} for r in blind][:400]}

    # ---- E7 labelled set
    if LABELS.exists():
        with open(LABELS, newline="") as fh:
            labels = list(csv.DictReader(fh))
        by_id = {r["ann_id"]: r for r in store}
        tp = fp = fn = tn = 0
        ctp = cfp = cfn = ctn = 0
        wrong = []
        for lab in labels:
            want = lab["is_seat_change"].strip().lower() in ("1", "yes", "true", "y")
            r = by_id.get(lab["ann_id"])
            got = bool(r and M.scan_filing(r)["kmp_flags"])
            tp += want and got
            fp += (not want) and got
            fn += want and not got
            tn += (not want) and not got
            if want and not got:
                wrong.append({"ann_id": lab["ann_id"], "symbol": lab["symbol"], "kind": "mechanical miss", "note": lab.get("note", "")})
            g = lab.get("group", "").strip()
            final = g in seat_groups.get(lab["symbol"], set()) if g else bool(seat_groups.get(lab["symbol"]))
            ctp += want and final
            cfn += want and not final
            if want and not final:
                wrong.append({"ann_id": lab["ann_id"], "symbol": lab["symbol"], "kind": "final miss", "note": lab.get("note", "")})
        pr = lambda a, b: round(100 * a / (a + b), 1) if (a + b) else None          # noqa: E731
        out["E7"] = {"labelled": len(labels), "mechanical": {"tp": tp, "fp": fp, "fn": fn, "tn": tn, "recall": pr(tp, fn), "precision": pr(tp, fp)},
                     "final_list": {"changes_labelled": ctp + cfn, "found": ctp, "missed": cfn, "recall": pr(ctp, cfn)}, "wrong": wrong}
    else:
        out["E7"] = {"labelled": 0}

    # ---- E8 quotes
    seat_kept = [(s, ch) for s, c in cos.items() for ch in c.get("seat_changes", []) if not ch.get("dropped")]
    own_kept = [(s, c["ownership"]) for s, c in cos.items() if (c.get("ownership") or {}).get("keep")]
    sv = sum(1 for _, ch in seat_kept if ch.get("verified"))
    ov = sum(1 for _, o in own_kept if o.get("verified"))
    out["E8"] = {"seat_changes": len(seat_kept), "seat_verified": sv, "ownership": len(own_kept), "ownership_verified": ov,
                 "verified_pct": round(100 * (sv + ov) / max(1, len(seat_kept) + len(own_kept)), 1),
                 "unverified": [{"symbol": s, "seat": ch["seat"], "checks": ch.get("checks"), "quote": ch.get("quote", "")[:160]}
                                for s, ch in seat_kept if not ch.get("verified")][:60]
                               + [{"symbol": s, "seat": "ownership", "checks": o.get("checks"), "quote": o.get("quote", "")[:160]}
                                  for s, o in own_kept if not o.get("verified")][:40],
                 "judge_failures": sorted(s for s, c in cos.items()
                                          if str((c.get("seat_judge") or {}).get("status", "")).startswith("judge failed")
                                          or str((c.get("own_judge") or {}).get("status", "")).startswith("judge failed"))}
    out["hard_failures"] = ([f"E2: {len(no_verdict)} major promoter moves without a verdict"] if no_verdict else []) \
        + ([f"E8: only {out['E8']['verified_pct']}% of reported changes verified"] if out["E8"]["verified_pct"] < 90 else []) \
        + ([f"E8: {len(out['E8']['judge_failures'])} judge failures"] if out["E8"]["judge_failures"] else []) \
        + ([f"E1: {len(out['E1']['unread'])}+ filings never attempted"] if out["E1"]["unread"] else [])
    return out


def render(ev: dict) -> str:
    A = ["# Management change — evaluation", "",
         f"*Run {ev['run_date']} · window {ev['window'][0]} → {ev['window'][1]}.* Each check compares the skill's list with something "
         f"its own detector did not decide. An exception a person has read and explained (`evals/reviewed_exceptions.csv`) is shown with the note.", "",
         "| Check | Result |", "|---|---|"]
    e = ev
    A += [f"| E1 Coverage — management / takeover filings read | {e['E1']['by_status'].get('read', 0):,} of {e['E1']['filings']:,} ({e['E1']['read_pct']}%) |",
          f"| E2 Ownership vs NSE shareholding register | {e['E2']['major_moves']} major promoter moves; {e['E2']['with_verdict']} carry a verdict; "
          f"{len(e['E2']['read_as_none'])} read as no change ({len(e['E2']['read_as_none_unreviewed'])} not yet reviewed) |",
          f"| E3 Open-offer filings | {e['E3']['companies_with_open_offer_filing']} companies; {e['E3']['read_as_control_change']} read as a change of control; "
          f"{len(e['E3']['unreviewed'])} others not yet reviewed |",
          f"| E4 Call rosters | {e['E4']['seats_whose_roster_changed']} seats whose listed holder changed; {e['E4']['reported_by_skill']} reported; "
          f"{len(e['E4']['not_reported'])} not ({len(e['E4']['unreviewed'])} not yet reviewed) |",
          f"| E5 Headlines naming a CEO / MD / CFO | {e['E5']['company_seats_named_in_headlines']} company-seats; {e['E5']['reported_by_skill']} reported; "
          f"{len(e['E5']['not_reported'])} not ({len(e['E5']['unreviewed'])} not yet reviewed) |",
          f"| E6 Management filings whose PDF gave no text | {e['E6']['management_filings_without_text']} at {e['E6']['companies']} companies; "
          f"{e['E6']['with_a_seat_in_the_headline']} name a seat in the headline (covered by E5) |"]
    if e["E7"].get("labelled"):
        m, f = e["E7"]["mechanical"], e["E7"]["final_list"]
        A += [f"| E7 Hand-labelled filings ({e['E7']['labelled']}) | mechanical flag: recall {m['recall']}%, precision {m['precision']}% "
              f"(tp {m['tp']}, fp {m['fp']}, fn {m['fn']}, tn {m['tn']}); final list: {f['found']} of {f['changes_labelled']} labelled changes found |"]
    A += [f"| E8 Names and quotes found in the documents | {e['E8']['seat_verified']} of {e['E8']['seat_changes']} seat changes, "
          f"{e['E8']['ownership_verified']} of {e['E8']['ownership']} ownership changes ({e['E8']['verified_pct']}%); "
          f"{len(e['E8']['judge_failures'])} judge failures |", ""]
    A += ["**Hard failures:** " + ("; ".join(e["hard_failures"]) if e["hard_failures"] else "none."), ""]

    A += ["## E1 — coverage by category", "", "| Category | Read | No text | Failed | Skipped (size) | Other |", "|---|---:|---:|---:|---:|---:|"]
    for c, v in e["E1"]["by_category"].items():
        other = sum(n for k, n in v.items() if k not in ("read", "no-text", "failed", "skipped"))
        A.append(f"| {c} | {v.get('read', 0)} | {v.get('no-text', 0)} | {v.get('failed', 0)} | {v.get('skipped', 0)} | {other} |")

    A += ["", "## E2 — every major move in the promoter holding", "",
          "| Company | Promoter holding | Change | Crossed | Verdict | What the skill read | Reviewed |", "|---|---|---:|---|---|---|---|"]
    for r in e["E2"]["rows"]:
        A.append(f"| **{r['symbol']}** | {r['base'][1]}% ({r['base'][0]}) → {r['latest'][1]}% ({r['latest'][0]}) | {r['change']:+.2f} | "
                 f"{', '.join(r['crossed']) or '—'} | {r['verdict'] or '**NO VERDICT**'} | {AZ._short(r['what'], 170)} | {r['reviewed'] or '—'} |")

    A += ["", "## E3 — open-offer filings not read as a change of control", ""]
    if e["E3"]["others"]:
        A += ["| Company | Verdict | What the skill read | Reviewed |", "|---|---|---|---|"]
        A += [f"| **{b['symbol']}** | {b['verdict']} | {AZ._short(b['what'], 200)} | {b['reviewed'] or '—'} |" for b in e["E3"]["others"]]
    else:
        A += ["None."]

    A += ["", "## E4 — a seat whose holder differs between the calls, not reported", ""]
    if e["E4"]["not_reported"]:
        A += ["| Company | Seat | Earlier call lists | Later call lists | Calls | The skill | Reviewed |", "|---|---|---|---|---|---|---|"]
        A += [f"| **{m['symbol']}** | {m['seat']} | {', '.join(m['before'])} | {', '.join(m['after'])} | {m['from_call']} → {m['to_call']} | {m['skill']} | {m['reviewed'] or '—'} |"
              for m in e["E4"]["not_reported"]]
    else:
        A += ["None."]

    A += ["", "## E5 — a headline names a seat, no change reported", ""]
    if e["E5"]["not_reported"]:
        A += ["| Company | Seat | Date | Headline | The skill | Reviewed |", "|---|---|---|---|---|---|"]
        A += [f"| **{m['symbol']}** | {m['group']} | {m['date']} | [{AZ._short(m['headline'], 120)}]({m['attachment']}) | {AZ._short(m['skill'], 150)} | {m['reviewed'] or '—'} |"
              for m in e["E5"]["not_reported"]]
    else:
        A += ["None."]

    A += ["", "## E8 — reported changes whose name or quote was not matched", ""]
    if e["E8"]["unverified"]:
        A += ["| Company | Seat | Names in documents | Quote in documents | Quote |", "|---|---|---|---|---|"]
        for u in e["E8"]["unverified"]:
            ck = u.get("checks") or {}
            A.append(f"| **{u['symbol']}** | {u['seat']} | {ck.get('names_in_documents', ck.get('names_in_record'))} | {ck.get('quote_in_documents')} | {AZ._short(u['quote'], 140)} |")
    else:
        A += ["None."]
    if e["E7"].get("wrong"):
        A += ["", "## E7 — labelled changes missed", "", "| Filing | Company | Kind | Note |", "|---|---|---|---|"]
        A += [f"| {w['ann_id']} | {w['symbol']} | {w['kind']} | {w['note']} |" for w in e["E7"]["wrong"]]
    return "\n".join(A) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.out:
        AZ.set_out_dir(Path(args.out))
    record = json.loads(AZ.LATEST.read_text())
    ev = evaluate(record)
    (AZ.OUT_DIR / "MANAGEMENT_CHANGE_EVAL.md").write_text(render(ev))
    (AZ.OUT_DIR / "_eval.json").write_text(json.dumps(ev, indent=1, default=str))
    print(json.dumps({k: (v if k in ("hard_failures",) else None) for k, v in ev.items() if k == "hard_failures"}
                     | {"E1_read_pct": ev["E1"]["read_pct"], "E2_no_verdict": len(ev["E2"]["no_verdict"]),
                        "E2_read_as_none": len(ev["E2"]["read_as_none"]), "E3_others": len(ev["E3"]["others"]),
                        "E4_not_reported": len(ev["E4"]["not_reported"]), "E5_not_reported": len(ev["E5"]["not_reported"]),
                        "E6_no_text": ev["E6"]["management_filings_without_text"], "E8_verified_pct": ev["E8"]["verified_pct"]}))
    sys.exit(1 if ev["hard_failures"] else 0)


if __name__ == "__main__":
    main()
