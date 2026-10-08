"""
analyze.py — run the SpinOffSkill end to end and write the report.

    python3 analyze.py run                   # analyse the stored filings
    python3 analyze.py run --refresh         # re-pull the last year first
    python3 analyze.py run --quick           # no AI reading of the schemes
    python3 analyze.py run --only TMPV,SIEMENS
    python3 analyze.py company TMPV          # one company, JSON to stdout

THE PIPELINE
  1. Announcements/fetch_announcements.py has pulled the last year of
     NSE (and BSE) filings for every NiftyTotalMarket company and kept
     the ones that classify as restructuring (spin-off / demerger,
     subsidiary listing, scheme, merger, slump sale, rights, capital
     reduction), with their attachments reduced to text.
  2. spinoff.py groups those into SITUATIONS, walks each one's stages
     (announced → NOC → meetings → NCLT → effective → record date →
     listed), extracts the stated facts (entitlement ratio, resulting
     company, dates, pro-forma, option pricing, insider continuity,
     size), scans the last twelve months of the company's conference
     calls for management's own words, pulls leverage / earnings /
     comparable P/E from the stored statements and market data, and
     answers the notes' checklist item by item.
  3. The judge (claude, `ANALYST_MODEL` / `SPINOFF_JUDGE_MODEL`, default
     claude-opus-5) READS each spin-off's scheme text and call excerpts
     and fills the parts a regex cannot: the real reason, who gains,
     what is being hidden or revealed, and what to read next — strictly
     from the documents, with quotes, cached per document hash. --quick
     skips it; the mechanical read stands on its own.

OUTPUT (Analysis/NiftyTotalMarketAnalysis/SpinOffAnalysis/)
  SPINOFF_REPORT.md        the report
  spinoff_latest.json      the run, machine-readable
  _situations.csv          one row per situation
  _concall_mentions.csv    every call mention with its quote
  history/<run_date>/      snapshot of the three above
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import spinoff as SO                       # noqa: E402
import fetch_announcements as FA           # noqa: E402  (via spinoff's path)

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "SpinOffAnalysis"
REPORT = OUT_DIR / "SPINOFF_REPORT.md"
LATEST = OUT_DIR / "spinoff_latest.json"
SITUATIONS = OUT_DIR / "_situations.csv"
MENTIONS = OUT_DIR / "_concall_mentions.csv"
HISTORY = OUT_DIR / "history"
CACHE = HERE.parent / ".judge_cache.json"
MODEL = os.environ.get("SPINOFF_JUDGE_MODEL",
                       os.environ.get("ANALYST_MODEL", "claude-opus-5"))
JUDGE_CHARS = 45_000


# ------------------------------------------------------------- the judge

def _ai_available() -> bool:
    return shutil.which("claude") is not None


def judge_prompt(sit: dict, scheme_text: str, mentions: list[dict]) -> str:
    quotes = "\n".join(f"- [{m['call']}] {m['quote']}" for m in mentions[:10])
    return (
        f"You are reading the filings of {sit['company']} ({sit['symbol']}) for a "
        f"special-situation investor following Greenblatt's spin-off checklist. "
        f"The situation on file: kind={sit['kind']}, stage={sit['stage']}, "
        f"first filing {sit['first_filing']}, facts={json.dumps(sit['facts'])[:800]}.\n"
        "Answer STRICT JSON only, every field from the documents below — never "
        "from memory, never invented; when the documents do not say, write "
        "\"not stated\":\n"
        '{"what_is_spun": "<the business being separated, <=20 words>", '
        '"reason": "<management\'s stated reason, <=40 words>", '
        '"reason_class": "unrelated"|"bad_business"|"unsellable"|"regulatory_strategic"|"value_unlocking"|"not stated", '
        '"insiders": "<promoter / management stake and incentives in the new entity, <=40 words>", '
        '"hidden_value": "<what the separation reveals — a great business, a cheap one, leverage; <=50 words>", '
        '"selling_pressure": "likely"|"unlikely"|"unclear", '
        '"selling_pressure_why": "<size, index exclusion, different industry; <=30 words>", '
        '"parent_or_spin": "parent"|"spin"|"both"|"neither"|"unclear", '
        '"option_pricing_date": "<date or not stated>", '
        '"read_next": "<the one document or number to check next, <=25 words>", '
        '"quote": "<one verbatim sentence from the documents>"}\n\n'
        f"CONFERENCE-CALL MENTIONS (last 12 months):\n{quotes or '(none)'}\n\n"
        f"FILING TEXT (scheme / disclosures, truncated):\n{scheme_text[:JUDGE_CHARS]}"
    )


def judge(sit: dict, scheme_text: str, mentions: list[dict],
          allow_ai: bool = True, runner=None) -> dict:
    """The judge's read, cached by (documents, model). `runner` lets tests
    stand in for the CLI."""
    stamp = hashlib.md5((scheme_text[:JUDGE_CHARS] + json.dumps(mentions[:10])
                         + MODEL).encode()).hexdigest()
    cache: dict = {}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text())
        except json.JSONDecodeError:
            cache = {}
    hit = cache.get(sit["symbol"])
    if hit and hit.get("stamp") == stamp:
        return {"status": "cached", **hit["verdict"]}
    if not allow_ai or (runner is None and not _ai_available()):
        return {"status": "not assessed",
                "note": "judge not run — mechanical read only"}
    if len(scheme_text) < 500 and not mentions:
        return {"status": "no documents", "note": "nothing on file to read"}
    prompt = judge_prompt(sit, scheme_text, mentions)
    try:
        if runner is not None:
            out = runner(prompt)
        else:
            proc = subprocess.run(["claude", "-p", "--model", MODEL], input=prompt,
                                  capture_output=True, text=True, timeout=600)
            if proc.returncode != 0:
                return {"status": f"judge failed: {(proc.stderr or '')[-120:]}"}
            out = proc.stdout
    except Exception as e:                                 # noqa: BLE001
        return {"status": f"judge failed: {e}"}
    m = re.search(r"\{.*\}", out or "", re.DOTALL)
    if not m:
        return {"status": "judge failed: unparseable"}
    try:
        verdict = json.loads(m.group(0))
    except json.JSONDecodeError:
        return {"status": "judge failed: bad json"}
    cache[sit["symbol"]] = {"stamp": stamp, "verdict": verdict}
    CACHE.write_text(json.dumps(cache, indent=1))
    return {"status": "judged", **verdict}


def scheme_text_for(sit: dict, rows: list[dict]) -> str:
    """The longest attachment texts of the situation's filings, demerger
    documents first, joined for the judge."""
    mine = [r for r in rows if r["symbol"] == sit["symbol"]]
    texts = []
    for r in mine:
        t = SO.load_text(r)
        if t:
            texts.append((r["kind"] in ("demerger", "subsidiary_listing"), len(t), r["date"], t))
    texts.sort(key=lambda x: (not x[0], -x[1]))
    return "\n\n=====\n\n".join(t for _, _, _, t in texts[:4])


# ------------------------------------------------------------- rendering

def _inr(x) -> str:
    return f"₹{x:,.0f} cr" if isinstance(x, (int, float)) else "—"


def render_report(record: dict) -> str:
    m = record["meta"]
    sits = record["situations"]
    spins = [s for s in sits if s["kind"] in SO.SPIN_KINDS]
    others = [s for s in sits if s["kind"] not in SO.SPIN_KINDS]
    A = ["# Spin-offs and demergers — NiftyTotalMarket", "",
         f"*Run {m['run_date']} · filings window {m['window_from']} → {m['window_to']} · "
         f"{m['filings']} restructuring filings across {m['companies']} companies · "
         f"{len(spins)} spin-off situations, {len(others)} other restructurings · "
         f"judge: {m['judge']}.*", "",
         "**The method, in one paragraph.** Spin-offs are where the notes say the "
         "bargains hide: the new stock is sold by holders who never chose it "
         "(index funds, size and mandate limits, no coverage) for about a year, "
         "the parent is often the better buy before the split, insiders tell you "
         "what they think through the stock and options they take in the new "
         "entity, and a pro-forma statement plus the peer P/E prices what the "
         "market is ignoring. This report lists every spin-off, demerger and "
         "subsidiary listing announced or indicated in the last year — from the "
         "exchange filings and from what management said on the calls — walks "
         "each one's stage, and answers the checklist from the documents on file.",
         ""]
    # ---- summary table
    A += ["## The situations", "",
          "| Company | What | Stage | First filing | Listed on | Score | Verdict |",
          "|---|---|---|---|---|---:|---|"]
    for s in sorted(spins, key=lambda s: -s["verdict"]["score"]):
        A.append(f"| **{s['symbol']}** | {s['family']} | {s['stage']} | {s['first_filing']} | "
                 f"{s.get('listed_on') or '—'} | {s['verdict']['score']} | {s['verdict']['label']} |")
    if not spins:
        A.append("| — | no spin-off situation on file | | | | | |")
    A.append("")
    if others:
        A += ["<details><summary>Other restructurings on file (mergers, slump sales, "
              f"rights, capital actions) — {len(others)}</summary>", "",
              "| Company | What | Stage | First filing | Filings |", "|---|---|---|---|---:|"]
        A += [f"| {s['symbol']} | {s['family']} | {s['stage']} | {s['first_filing']} | {s['n_filings']} |"
              for s in others]
        A += ["", "</details>", ""]
    # ---- each spin-off
    for s in spins:
        A += [f"## {s['symbol']} — {s['company']}", "",
              f"**{s['verdict']['label']}** · score {s['verdict']['score']}/10 · {s['family']} · "
              f"{s['n_filings']} filing(s) from {', '.join(s['sources'])} · "
              f"first {s['first_filing']}, latest {s['latest_filing']}", ""]
        if s["stage_dates"]:
            A += ["**The stages, as filed:** " + " → ".join(
                f"{k} ({v})" for k, v in s["stage_dates"].items()), ""]
        f = s["facts"]
        facts = [x for x in (
            f"resulting company **{f['resulting_company']}**" if f.get("resulting_company") else "",
            f"demerged undertaking: {f['demerged_undertaking']}" if f.get("demerged_undertaking") else "",
            f"entitlement **{f['entitlement_ratio']}**" if f.get("entitlement_ratio") else "",
            f"record date {f['record_date']}" if f.get("record_date") else "",
            f"appointed date {f['appointed_date']}" if f.get("appointed_date") else "",
            "pro-forma statements referenced" if f.get("pro_forma") else "",
            f"size hint: {f['small_share']}" if f.get("small_share") else "") if x]
        if facts:
            A += ["**Stated in the filings:** " + "; ".join(facts) + ".", ""]
        j = s.get("judge") or {}
        if j.get("status") in ("judged", "cached"):
            A += ["**The judge's read of the documents:**", "",
                  f"- *What is spun:* {j.get('what_is_spun', '—')}",
                  f"- *Why (as stated):* {j.get('reason', '—')} — class `{j.get('reason_class', '—')}`",
                  f"- *Insiders:* {j.get('insiders', '—')}",
                  f"- *What it reveals:* {j.get('hidden_value', '—')}",
                  f"- *Selling pressure:* {j.get('selling_pressure', '—')} — {j.get('selling_pressure_why', '')}",
                  f"- *Parent or spin:* {j.get('parent_or_spin', '—')} · *option pricing date:* {j.get('option_pricing_date', '—')}",
                  f"- *Read next:* {j.get('read_next', '—')}"]
            if j.get("quote"):
                A.append(f"- *In their words:* “{j['quote']}”")
            A.append("")
        A += ["**The checklist:**", "", "| Item | Status | Evidence |", "|---|---|---|"]
        for it in s["checklist"]:
            ev = it["evidence"]
            if it.get("quote"):
                ev += f" — “{it['quote'][:220]}”"
            if it.get("next") and it["status"] in ("unknown", "partly"):
                ev += f" *(next: {it['next']})*"
            A.append(f"| {it['item']} | {it['status']} | {ev} |")
        A.append("")
        fin = s["financials"]
        nums = [x for x in (
            f"market cap {_inr(fin.get('market_cap_cr'))} at ₹{fin['price']:,.0f} ({fin.get('market_data_at', '')[:10]})"
            if fin.get("market_cap_cr") else "no live market data on file (Nifty 500 only)",
            f"borrowings {_inr(fin.get('borrowings_cr'))} ({fin.get('borrowings_year')})" if fin.get("borrowings_cr") is not None else "",
            f"debt / market cap {fin['debt_to_market_cap']}" if fin.get("debt_to_market_cap") is not None else "",
            f"net profit {_inr(fin.get('net_profit_cr'))} ({fin.get('net_profit_cr_year')})" if fin.get("net_profit_cr") is not None else "",
            f"P/E {fin['pe_on_latest_profit']} vs {fin['industry']} median {fin['industry_median_pe']} ({fin['industry_peers']} peers)"
            if fin.get("pe_on_latest_profit") and fin.get("industry_median_pe") else "") if x]
        A += ["**The numbers on file (parent, consolidated):** " + "; ".join(nums) + ".", ""]
        if s["concall_mentions"]:
            A += [f"**On the calls (last {SO.CONCALL_MONTHS} months):**", ""]
            A += [f"- *{mm['call']}* — “{mm['quote']}”" for mm in s["concall_mentions"][:5]] + [""]
        A += ["<details><summary>The filings</summary>", "", "| Date | Category | Headline | Attachment |", "|---|---|---|---|"]
        for h in s["headlines"]:
            link = f"[pdf]({h['attachment']})" if h["attachment"] else ""
            A.append(f"| {h['date']} | {h['category'][:40]} | {h['headline'][:160]} | {link} |")
        A += ["", "</details>", ""]
    # ---- the calls alone
    only_calls = record.get("call_only", [])
    A += ["## Indicated on the calls, not yet filed", "",
          "Companies whose management used spin-off / demerger / listing language "
          f"in the last {SO.CONCALL_MONTHS} months of calls but have no restructuring "
          "filing on file — the earliest signal the notes describe.", ""]
    if only_calls:
        A += ["| Company | Forward-looking / all mentions | Latest forward call | Example |", "|---|---:|---|---|"]
        for c in only_calls:
            A.append(f"| **{c['symbol']}** | {c['forward']} / {c['n']} | {c['latest']} | “{c['example'][:200]}” |")
    else:
        A.append("- (none)")
    A.append("")
    # ---- method
    A += ["---", "", "## How this was built", "",
          f"- **Filings:** NSE's corporate-announcements feed read month by month for the "
          f"{m['window_from']} → {m['window_to']} window and filtered to the {m['universe']} "
          f"official NiftyTotalMarket constituents; BSE via its daily RSS (accumulating) and "
          f"the BSE-sourced per-company lists on screener.in (BSE's own API refuses this "
          f"environment). Each filing is classified by category and headline; its attachment "
          f"is reduced to text and re-classified from the text, so a bare 'Scheme of Arrangement' "
          f"becomes a demerger or a merger once the scheme is read. Stored in "
          f"`IndividualStockAnalysis/India/Announcements/NiftyTotalMarket/`.",
          "- **Situations:** one per company per kind family; stages from the filings' words; "
          "facts (entitlement ratio, resulting company, dates, pro-forma, option pricing, insider "
          "continuity, size) by pattern from the texts; reasons classified into the notes' five.",
          f"- **Calls:** the stored consolidated transcripts, last {SO.CONCALL_MONTHS} months of "
          "calls, scanned for demerger / spin-off / listing language with verbatim snippets.",
          "- **Numbers:** borrowings from the stored balance sheets, net profit from the stored "
          "P&L, market cap / P/E from the live Nifty 500 market file (stated date), the industry "
          "median P/E from the same file. `stub_value()` and `leverage_doubling()` carry the "
          "notes' partial-spin-off and Host Marriott arithmetic for when the pieces trade.",
          f"- **Judge:** {m['judge']}. The judge reads only the documents shown to it and must "
          "quote; its read is cached per document hash and model.",
          "- **Score:** share of checklist items answered yes (1) or partly (½), on 10. It measures "
          "how much of the notes' pattern is VISIBLE in the documents, not how good the stock is.",
          ""]
    return "\n".join(A)


# ----------------------------------------------------------------- run

def situation_rows(sits: list[dict]) -> list[dict]:
    out = []
    for s in sits:
        f = s["facts"]
        out.append({"symbol": s["symbol"], "company": s["company"], "kind": s["kind"],
                    "family": s["family"], "stage": s["stage"], "first_filing": s["first_filing"],
                    "latest_filing": s["latest_filing"], "listed_on": s.get("listed_on") or "",
                    "n_filings": s["n_filings"], "score": s["verdict"]["score"],
                    "verdict": s["verdict"]["label"],
                    "resulting_company": f.get("resulting_company", ""),
                    "entitlement_ratio": f.get("entitlement_ratio", ""),
                    "record_date": f.get("record_date", ""),
                    "reasons": "; ".join(r["reason"] for r in s["reasons"]),
                    "concall_mentions": len(s["concall_mentions"]),
                    "judge_status": (s.get("judge") or {}).get("status", "")})
    return out


def call_only_scan(symbols: list[str], exclude: set[str], today: dt.date) -> list[dict]:
    """Companies whose calls indicate a spin-off with no filing on file."""
    out = []
    for sym in symbols:
        if sym in exclude:
            continue
        ms = SO.concall_mentions(SO.concall_text(sym), today)
        fwd = [m for m in ms if m["tone"] == "forward"]
        # an indication needs at least one FORWARD-looking mention; a company
        # merely describing a past demerger, or denying one, is not a signal
        if fwd and len(ms) >= 2:
            out.append({"symbol": sym, "n": len(ms), "forward": len(fwd),
                        "latest": fwd[-1]["call"], "example": fwd[-1]["quote"],
                        "mentions": ms})
    out.sort(key=lambda c: (-c["forward"], -c["n"]))
    return out


def cmd_run(args) -> None:
    today = dt.date.today()
    if args.refresh:
        print("refreshing the last year of filings…", file=sys.stderr)
        FA.run(days=args.days, bse=not args.no_bse, pdf=True,
               only={s.strip().upper() for s in args.only.split(",") if s.strip()} or None)
    rows = SO.load_filings()
    if args.only:
        keep = {s.strip().upper() for s in args.only.split(",") if s.strip()}
        rows = [r for r in rows if r["symbol"] in keep]
    members = FA.universe()
    sits = SO.analyse(rows, today=today, with_calls=not args.no_calls)
    ai = _ai_available() and not args.quick
    for s in sits:
        if s["kind"] in SO.SPIN_KINDS:
            s["judge"] = judge(s, scheme_text_for(s, rows), s["concall_mentions"], allow_ai=ai)
            print(f"  {s['symbol']}: {s['kind']} / {s['stage']} — {s['verdict']['label']}"
                  f" [{s['judge'].get('status')}]", file=sys.stderr)
    call_only = [] if args.no_calls else call_only_scan(
        sorted(members if not args.only else {s["symbol"] for s in sits}),
        {s["symbol"] for s in sits}, today)
    dates = [r["date"] for r in rows] or [today.isoformat()]
    meta = {"run_date": today.isoformat(), "window_from": min(dates), "window_to": max(dates),
            "filings": len(rows), "companies": len({r["symbol"] for r in rows}),
            "universe": len(members),
            "judge": (f"{MODEL} read the schemes and calls" if ai else
                      "not run (--quick or no CLI); mechanical read only")}
    record = {"meta": meta, "situations": sits, "call_only": call_only}
    md = render_report(record)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(md)
    LATEST.write_text(json.dumps(record, indent=1, default=str))
    FA.write_csv(SITUATIONS, situation_rows(sits), list(situation_rows(sits)[0].keys())
                 if sits else ["symbol"])
    mrows = [{"symbol": s["symbol"], **mm} for s in sits for mm in s["concall_mentions"]]
    mrows += [{"symbol": c["symbol"], **mm} for c in call_only for mm in c["mentions"]]
    FA.write_csv(MENTIONS, mrows, ["symbol", "call", "term", "tone", "quote"])
    snap = HISTORY / today.isoformat()
    snap.mkdir(parents=True, exist_ok=True)
    for p in (REPORT, SITUATIONS, MENTIONS):
        shutil.copy(p, snap / p.name)
    (snap / "run.json").write_text(json.dumps(record, indent=1, default=str))
    print(f"wrote {REPORT} ({len(md.splitlines())} lines); {len(sits)} situations, "
          f"{sum(1 for s in sits if s['kind'] in SO.SPIN_KINDS)} spin-offs, "
          f"{len(call_only)} call-only indications", file=sys.stderr)


def cmd_company(args) -> None:
    rows = [r for r in SO.load_filings() if r["symbol"] == args.symbol.upper()]
    sits = SO.analyse(rows, with_calls=True)
    for s in sits:
        if s["kind"] in SO.SPIN_KINDS:
            s["judge"] = judge(s, scheme_text_for(s, rows), s["concall_mentions"],
                               allow_ai=not args.quick)
    if not sits:
        ms = SO.concall_mentions(SO.concall_text(args.symbol.upper()))
        sits = [{"symbol": args.symbol.upper(), "note": "no restructuring filing on file",
                 "concall_mentions": ms}]
    print(json.dumps(sits, indent=1, default=str))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--refresh", action="store_true", help="re-pull the filings first")
    r.add_argument("--days", type=int, default=365)
    r.add_argument("--no-bse", action="store_true")
    r.add_argument("--quick", action="store_true", help="no AI judge")
    r.add_argument("--no-calls", action="store_true", help="skip the conference-call scan")
    r.add_argument("--only", default="")
    c = sub.add_parser("company")
    c.add_argument("symbol")
    c.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    {"run": cmd_run, "company": cmd_company}[args.cmd](args)


if __name__ == "__main__":
    main()
