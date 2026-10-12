"""
analyze.py — run the SpinOffSkill end to end and write the report.

    python3 analyze.py run                   # analyse the stored filings
    python3 analyze.py run --refresh         # re-pull the last year first
    python3 analyze.py run --quick           # no AI reading of the documents
    python3 analyze.py run --only TMPV,SIEMENS
    python3 analyze.py run --fetch-docs      # pull annual reports + presentations first
    python3 analyze.py company TMPV          # one company, JSON to stdout

THE PIPELINE
  1. Announcements/fetch_announcements.py has pulled the last year of
     NSE (and BSE) filings for every NiftyTotalMarket company and kept
     the ones that classify as restructuring, with their attachments
     reduced to text.
  2. spinoff.py groups those into SITUATIONS, walks each one's stages,
     extracts the stated facts, scans the calls, and answers the notes'
     checklist. Each situation gets a CONFIDENCE — confirmed (a demerger
     scheme is on the exchange record), probable, indicated — and a
     LISTING STATUS: whether the demerged entity trades, from when, or
     what must still happen before it can.
  3. For every confirmed or probable spin-off, financials.py brings the
     parent's last three fiscal years (sales, operating profit, PAT,
     growth, margins, P/E, cash flows) from the stored statements, and
     the documents behind the piece being separated: the last three
     annual reports and twelve quarterly presentations
     (InvestorPresentations/fetch_presentations.py), page-marked.
  4. The judge (claude; SPINOFF_JUDGE_MODEL / ANALYST_MODEL / claude-opus-5)
     READS: (a) the scheme and call excerpts for the checklist items a
     pattern cannot answer, including the listing timeline; (b) three
     years of call passages for the detailed RATIONALE, point by point
     with the transcript each came from; (c) the segment-reporting pages
     for the piece's OWN sales, operating profit and PAT, year by year,
     each number with its document and page — growth and margins are
     then computed here, never by the model. Every read is cached per
     document hash; --quick skips the judge and the report says so.

OUTPUT (Analysis/NiftyTotalMarketAnalysis/SpinOffAnalysis/)
  SPINOFF_REPORT.md, spinoff_latest.json, _situations.csv,
  _concall_mentions.csv, _coverage.csv (what was found for whom),
  history/<run_date>/
"""

from __future__ import annotations

import argparse
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
import financials as FN                    # noqa: E402
import fetch_announcements as FA           # noqa: E402  (via spinoff's path)

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "SpinOffAnalysis"
REPORT = OUT_DIR / "SPINOFF_REPORT.md"
LATEST = OUT_DIR / "spinoff_latest.json"
SITUATIONS = OUT_DIR / "_situations.csv"
MENTIONS = OUT_DIR / "_concall_mentions.csv"
COVERAGE = OUT_DIR / "_coverage.csv"
HISTORY = OUT_DIR / "history"
CACHE = HERE.parent / ".judge_cache.json"
MODEL = os.environ.get("SPINOFF_JUDGE_MODEL",
                       os.environ.get("ANALYST_MODEL", "claude-opus-5"))
JUDGE_CHARS = 45_000
SEGMENT_CHARS = 115_000       # segment pages are tables; they must arrive whole
PROMPT_VERSION = "v2"


# ------------------------------------------------------------- the judge

def _ai_available() -> bool:
    return shutil.which("claude") is not None


def _cache() -> dict:
    if CACHE.exists():
        try:
            return json.loads(CACHE.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def _ask(key: str, stamp: str, prompt: str, allow_ai: bool, runner=None) -> dict:
    """One cached, strict-JSON question to the judge."""
    cache = _cache()
    hit = cache.get(key)
    if hit and hit.get("stamp") == stamp:
        return {"status": "cached", **hit["verdict"]}
    if not allow_ai or (runner is None and not _ai_available()):
        return {"status": "not assessed", "note": "judge not run — mechanical read only"}
    try:
        if runner is not None:
            out = runner(prompt)
        else:
            proc = subprocess.run(["claude", "-p", "--model", MODEL], input=prompt,
                                  capture_output=True, text=True, timeout=900)
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
    cache = _cache()
    cache[key] = {"stamp": stamp, "verdict": verdict}
    CACHE.write_text(json.dumps(cache, indent=1))
    return {"status": "judged", **verdict}


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
        '"demerged_business_names": ["<every name the documents use for the business or '
        'resulting company, e.g. a brand, a segment name, the new company>"], '
        '"reason": "<management\'s stated reason, <=40 words>", '
        '"reason_class": "unrelated"|"bad_business"|"unsellable"|"regulatory_strategic"|"value_unlocking"|"not stated", '
        '"insiders": "<promoter / management stake and incentives in the new entity, <=40 words>", '
        '"hidden_value": "<what the separation reveals — a great business, a cheap one, leverage; <=50 words>", '
        '"selling_pressure": "likely"|"unlikely"|"unclear", '
        '"selling_pressure_why": "<size, index exclusion, different industry; <=30 words>", '
        '"parent_or_spin": "parent"|"spin"|"both"|"neither"|"unclear", '
        '"option_pricing_date": "<date or not stated>", '
        '"listing_timeline": "<when the demerged entity is expected to list or was listed, '
        'in the documents\' own words with the date they were said; or not stated>", '
        '"read_next": "<the one document or number to check next, <=25 words>", '
        '"quote": "<one verbatim sentence from the documents>"}\n\n'
        f"CONFERENCE-CALL MENTIONS (last 12 months):\n{quotes or '(none)'}\n\n"
        f"FILING TEXT (scheme / disclosures, truncated):\n{scheme_text[:JUDGE_CHARS]}"
    )


def judge(sit: dict, scheme_text: str, mentions: list[dict],
          allow_ai: bool = True, runner=None) -> dict:
    stamp = hashlib.md5((scheme_text[:JUDGE_CHARS] + json.dumps(mentions[:10])
                         + MODEL + PROMPT_VERSION).encode()).hexdigest()
    if len(scheme_text) < 500 and not mentions:
        return {"status": "no documents", "note": "nothing on file to read"}
    return _ask(sit["symbol"], stamp, judge_prompt(sit, scheme_text, mentions), allow_ai, runner)


def rationale_prompt(sit: dict, excerpts: list[dict], scheme_text: str) -> str:
    body = "\n\n".join(f"[{e['call']}] {e['quote']}" for e in excerpts)
    return (
        f"You are reconstructing WHY {sit['company']} ({sit['symbol']}) is separating a "
        f"business, for a special-situation investor. Below are passages from three "
        f"years of the company's earnings calls (each tagged with its call) and the "
        f"rationale section of the scheme filing. Answer STRICT JSON only, from these "
        f"texts alone — never from memory. Be specific and detailed: name the "
        f"businesses, the numbers management cited, the problems they said the "
        f"separation solves, who asked for it (investors, lenders, partners), and how "
        f"the plan changed over time.\n"
        '{"rationale": "<4-8 sentences: the full reasoning as management explained it, '
        'with the specifics they gave>", '
        '"evolution": "<2-4 sentences: how the idea surfaced and evolved call by call, '
        'with the call dates>", '
        '"points": [{"call": "<call label exactly as tagged, or Scheme>", '
        '"point": "<what was said, 1-2 sentences, specific>", '
        '"quote": "<verbatim sentence>"}], '
        '"what_management_expects": "<what they said the separation will do for each '
        'entity — margins, capital, valuation, focus; <=60 words>", '
        '"gaps": "<what the calls did NOT explain, <=30 words>"}\n\n'
        f"CALL PASSAGES:\n{body[:JUDGE_CHARS]}\n\n"
        f"SCHEME RATIONALE (filing text, truncated):\n{scheme_text[:12_000]}"
    )


def judge_rationale(sit: dict, excerpts: list[dict], scheme_text: str,
                    allow_ai: bool = True, runner=None) -> dict:
    if not excerpts and len(scheme_text) < 500:
        return {"status": "no documents", "note": "no call passages or scheme text on file"}
    stamp = hashlib.md5((json.dumps(excerpts)[:JUDGE_CHARS] + scheme_text[:12_000]
                         + MODEL + PROMPT_VERSION).encode()).hexdigest()
    return _ask(f"{sit['symbol']}::rationale", stamp,
                rationale_prompt(sit, excerpts, scheme_text), allow_ai, runner)


def segments_prompt(sit: dict, excerpts: list[dict], names: list[str]) -> str:
    body = "\n\n".join(f"[{e['doc']} — page {e['page']}] {e['text']}" for e in excerpts)
    return (
        f"You are extracting the OWN financials of the business {sit['company']} "
        f"({sit['symbol']}) is separating — known in the documents as: {', '.join(names)}. "
        f"Below are pages from the company's annual reports (segment reporting) and "
        f"quarterly presentations, each tagged with document and page. Answer STRICT JSON "
        f"only. Take every number from the tagged pages — never estimate, never recall. "
        f"Report fiscal-year figures (FY2024 = year ended March 2024, etc.); if only "
        f"quarterly or half-year numbers exist, say so in notes and leave the year null. "
        f"Keep the unit the document uses.\n"
        '{"segment_name": "<the segment / business as the documents label it>", '
        '"unit": "<₹ crore | ₹ million | ₹ lakh | as in the document>", '
        '"measure_notes": "<what the profit line is: segment result / EBIT / EBITDA / PBT; '
        'whether revenue is external or includes inter-segment>", '
        '"years": [{"fy": "FY2024", "revenue": <number or null>, '
        '"operating_profit": <number or null>, "pat": <number or null>, '
        '"source": "<document — page N>"}, '
        '{"fy": "FY2025", ...}, {"fy": "FY2026", ...}], '
        '"latest_quarter": {"period": "<e.g. Q1 FY27 or null>", "revenue": <number or null>, '
        '"operating_profit": <number or null>, "source": "<document — page N>"}, '
        '"not_found": "<which figures the pages do not carry, <=40 words>"}\n\n'
        f"PAGES:\n{body[:SEGMENT_CHARS]}"
    )


def judge_segments(sit: dict, excerpts: list[dict], names: list[str],
                   allow_ai: bool = True, runner=None) -> dict:
    if not excerpts:
        return {"status": "no documents", "note": "no segment pages found in the stored reports"}
    stamp = hashlib.md5((json.dumps(excerpts)[:SEGMENT_CHARS] + "|".join(names)
                         + MODEL + PROMPT_VERSION).encode()).hexdigest()
    return _ask(f"{sit['symbol']}::segments", stamp,
                segments_prompt(sit, excerpts, names), allow_ai, runner)


def segment_table(seg: dict) -> dict:
    """Growth and margins computed from the judge's extracted numbers;
    nothing is filled in."""
    years = [y for y in (seg.get("years") or []) if isinstance(y, dict)]
    if not years:
        return {"available": False}
    labels = [y.get("fy", "") for y in years]
    def col(k):
        out = []
        for y in years:
            v = y.get(k)
            out.append(float(v) if isinstance(v, (int, float)) else None)
        return out
    rev, op, pat = col("revenue"), col("operating_profit"), col("pat")
    def growth(vals):
        return [None] + [FN._growth(vals[i], vals[i - 1]) for i in range(1, len(vals))]
    rows = [
        {"metric": f"Revenue ({seg.get('unit', '')})", "values": rev},
        {"metric": "Revenue growth (%)", "values": growth(rev)},
        {"metric": f"Operating profit ({seg.get('unit', '')})", "values": op},
        {"metric": "Operating profit growth (%)", "values": growth(op)},
        {"metric": "Operating margin (%)", "values": [FN._margin(o, r) for o, r in zip(op, rev)]},
        {"metric": f"PAT ({seg.get('unit', '')})", "values": pat},
        {"metric": "PAT growth (%)", "values": growth(pat)},
    ]
    found = sum(1 for v in rev + op + pat if v is not None)
    return {"available": found > 0, "years": labels, "rows": rows,
            "sources": [y.get("source", "") for y in years], "found_numbers": found}


def scheme_text_for(sit: dict, rows: list[dict]) -> str:
    mine = [r for r in rows if r["symbol"] == sit["symbol"]]
    texts = []
    for r in mine:
        t = SO.load_text(r)
        if t:
            texts.append((r["kind"] in ("demerger", "subsidiary_listing"), len(t), r["date"], t))
    texts.sort(key=lambda x: (not x[0], -x[1]))
    return "\n\n=====\n\n".join(t for _, _, _, t in texts[:4])


def rationale_section_of(scheme_text: str) -> str:
    """The part of the scheme that explains itself, if it has one."""
    m = re.search(r"rationale", scheme_text, re.I)
    return scheme_text[max(0, m.start() - 500): m.start() + 12_000] if m else scheme_text[:12_000]


# ------------------------------------------------------------- rendering

def _inr(x) -> str:
    return f"₹{x:,.0f} cr" if isinstance(x, (int, float)) else "—"


def _v(x, pct=False) -> str:
    if x is None:
        return "—"
    return f"{x:+.1f}%" if pct else (f"{x:,.1f}" if abs(x) < 100 else f"{x:,.0f}")


def table_md(fin: dict, pct_rows: tuple[str, ...] = ("growth", "margin")) -> list[str]:
    A = ["| | " + " | ".join(fin["years"]) + " |", "|---|" + "---:|" * len(fin["years"])]
    for r in fin["rows"]:
        pct = any(k in r["metric"].lower() for k in pct_rows)
        A.append(f"| {r['metric']} | " + " | ".join(_v(v, pct and 'growth' in r['metric'].lower())
                                                  if pct else _v(v) for v in r["values"]) + " |")
    return A


def render_company(s: dict, heavy: bool) -> list[str]:
    conf, why = s["confidence"]
    L = s["listing"]
    A = [f"## {s['symbol']} — {s['company']}", "",
         f"**{conf.upper()}** ({why}) · **{s['verdict']['label']}** · score {s['verdict']['score']}/10 · "
         f"{s['family']} · {s['n_filings']} filing(s) from {', '.join(s['sources'])} · "
         f"first {s['first_filing']}, latest {s['latest_filing']}", "",
         f"> **Listing:** {L['text']}", ""]
    if s["stage_dates"]:
        A += ["**The stages, as filed:** " + " → ".join(f"{k} ({v})" for k, v in s["stage_dates"].items()), ""]
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
        A += ["**What is being separated, as the documents put it:** "
              f"{j.get('what_is_spun', '—')} — class `{j.get('reason_class', '—')}`.", "",
              f"- *Insiders:* {j.get('insiders', '—')}",
              f"- *What it reveals:* {j.get('hidden_value', '—')}",
              f"- *Selling pressure:* {j.get('selling_pressure', '—')} — {j.get('selling_pressure_why', '')}",
              f"- *Parent or spin:* {j.get('parent_or_spin', '—')} · *option pricing date:* {j.get('option_pricing_date', '—')}",
              f"- *Read next:* {j.get('read_next', '—')}"]
        if j.get("quote"):
            A.append(f"- *In their words:* “{j['quote']}”")
        A.append("")
    # ---- the rationale, from three years of calls
    r = s.get("rationale") or {}
    A += ["### Why the demerger — three years of calls and the scheme", ""]
    if r.get("status") in ("judged", "cached"):
        A += [r.get("rationale", ""), ""]
        if r.get("evolution"):
            A += [f"**How it evolved:** {r['evolution']}", ""]
        if r.get("what_management_expects"):
            A += [f"**What management expects from it:** {r['what_management_expects']}", ""]
        pts = [p for p in (r.get("points") or []) if isinstance(p, dict)]
        if pts:
            A += ["**Point by point, with the source:**", ""]
            for p in pts[:12]:
                url = s.get("call_links", {}).get(p.get("call", ""), "")
                src = f"[{p.get('call', '')}]({url})" if url else p.get("call", "")
                A.append(f"- *{src}* — {p.get('point', '')}" + (f" “{p['quote']}”" if p.get("quote") else ""))
            A.append("")
        if r.get("gaps"):
            A += [f"*Not explained on the calls:* {r['gaps']}", ""]
    elif s["reasons"]:
        A += ["Mechanical read only (judge not run). Stated reasons: " +
              "; ".join(f"{x['reason']} — “{x['quote']}”" for x in s["reasons"]), ""]
    else:
        A += ["No rationale on file: " + (r.get("note") or "no call passages and no scheme rationale text."), ""]
    if s.get("rationale_excerpts"):
        calls = sorted({e["call"] for e in s["rationale_excerpts"]}, key=lambda c: c)
        links = s.get("call_links", {})
        A += ["*Calls read (36 months):* " + ", ".join(
            f"[{c}]({links[c]})" if links.get(c) else c for c in calls), ""]
    if not heavy:
        return A + render_light_tail(s)
    # ---- the parent's numbers
    fin = s["parent_financials"]
    A += ["### The parent, last three fiscal years (consolidated)", ""]
    if fin.get("available"):
        A += table_md(fin) + ["", f"*Source: {fin['source']}; growth and margins computed here.*", ""]
        A += [c + "\n" for c in FN.charts_for(fin)]
    else:
        A += ["No stored P&L for this symbol.", ""]
    pe = s["pe"]
    A += [f"**P/E:** {pe['pe'] if pe.get('pe') is not None else '—'} — {pe['method']}"
          + (f" (price ₹{pe['price']:,.2f} as of {pe.get('as_of', '')})" if pe.get("price") else "") + ".", ""]
    cf = s["cash_flows"]
    if cf.get("available"):
        A += ["**Cash flows (₹ cr):**", ""] + table_md(cf, pct_rows=()) + ["", f"*Source: {cf['source']}.*", ""]
    else:
        A += ["No stored cash-flow statement for this symbol.", ""]
    # ---- the piece's own numbers
    seg, st = s.get("segments") or {}, s.get("segment_table") or {}
    A += ["### The business being separated — its own numbers", ""]
    docs = s.get("docs", {})
    searched = (f"{len(docs.get('annual_reports', []))} annual report(s) and "
                f"{len(docs.get('presentations', []))} presentation(s) on file")
    if st.get("available"):
        A += [f"**{seg.get('segment_name', '')}** · unit {seg.get('unit', '')} · {seg.get('measure_notes', '')}", ""]
        A += table_md(st) + [""]
        srcs = [x for x in st.get("sources", []) if x]
        if srcs:
            A += ["*Sources:* " + "; ".join(dict.fromkeys(srcs)), ""]
        lq = seg.get("latest_quarter") or {}
        if isinstance(lq, dict) and lq.get("period"):
            A += [f"*Latest quarter ({lq['period']}):* revenue {lq.get('revenue', '—')}, "
                  f"operating profit {lq.get('operating_profit', '—')} — {lq.get('source', '')}", ""]
        if seg.get("not_found"):
            A += [f"*Not in the pages read:* {seg['not_found']}", ""]
    elif seg.get("status") in ("judged", "cached"):
        A += [f"The segment pages read ({searched}) do not carry this business's own "
              f"revenue or profit: {seg.get('not_found', '')}", ""]
    else:
        A += [f"Not extracted — {seg.get('note') or seg.get('status') or 'judge not run'} ({searched}).", ""]
    if docs.get("annual_reports") or docs.get("presentations"):
        A += ["*Documents on file:* " + "; ".join(
            [f"[{l}]({u})" for l, u, _ in docs.get("annual_reports", [])] +
            [f"[Presentation {l}]({u})" for l, u, _ in docs.get("presentations", [])[:6]]), ""]
    return A + render_light_tail(s)


def render_light_tail(s: dict) -> list[str]:
    A = ["**The checklist:**", "", "| Item | Status | Evidence |", "|---|---|---|"]
    for it in s["checklist"]:
        ev = it["evidence"]
        if it.get("quote"):
            ev += f" — “{it['quote'][:220]}”"
        if it.get("next") and it["status"] in ("unknown", "partly"):
            ev += f" *(next: {it['next']})*"
        A.append(f"| {it['item']} | {it['status']} | {ev} |")
    A.append("")
    if s["concall_mentions"]:
        A += [f"**On the calls (last {SO.CONCALL_MONTHS} months):**", ""]
        A += [f"- *{mm['call']}* ({mm.get('tone', '')}) — “{mm['quote']}”" for mm in s["concall_mentions"][:5]] + [""]
    A += ["<details><summary>The filings</summary>", "", "| Date | Category | Headline | Attachment |", "|---|---|---|---|"]
    for h in s["headlines"]:
        link = f"[pdf]({h['attachment']})" if h["attachment"] else ""
        A.append(f"| {h['date']} | {h['category'][:40]} | {h['headline'][:160]} | {link} |")
    A += ["", "</details>", ""]
    return A


def render_report(record: dict) -> str:
    m = record["meta"]
    sits = record["situations"]
    spins = [s for s in sits if s["kind"] in SO.SPIN_KINDS]
    others = [s for s in sits if s["kind"] not in SO.SPIN_KINDS]
    conf = {s["symbol"]: s["confidence"][0] for s in spins}
    confirmed = [s for s in spins if conf[s["symbol"]] == "confirmed"]
    probable = [s for s in spins if conf[s["symbol"]] == "probable"]
    indicated = [s for s in spins if conf[s["symbol"]] == "indicated"]
    A = ["# Spin-offs and demergers — NiftyTotalMarket", "",
         f"*Run {m['run_date']} · filings window {m['window_from']} → {m['window_to']} · "
         f"{m['filings']} restructuring filings across {m['companies']} companies · "
         f"{len(confirmed)} confirmed demergers, {len(probable)} probable, {len(indicated)} indicated, "
         f"{len(others)} other restructurings · judge: {m['judge']}.*", "",
         "**The method, in one paragraph.** Spin-offs are where the notes say the bargains hide: "
         "the new stock is sold by holders who never chose it for about a year, the parent is "
         "often the better buy before the split, insiders tell you what they think through the "
         "stock and options they take in the new entity, and a pro-forma statement plus the "
         "peer P/E prices what the market is ignoring. This report puts the CONFIRMED demergers "
         "first — a demerger scheme on the exchange record — each with when the new entity lists, "
         "why management is doing it (three years of calls, with the transcript each point came "
         "from), the parent's last three years with charts, P/E and cash flows, and the separated "
         "business's own numbers from the annual reports and presentations, page-cited. Probable "
         "and indicated cases follow, then every other restructuring on file.", ""]
    A += ["## Confirmed demergers", "",
          "| Company | Resulting entity | Stage | Listing | Score | Verdict |", "|---|---|---|---|---:|---|"]
    for s in confirmed:
        A.append(f"| **{s['symbol']}** | {s['facts'].get('resulting_company') or (s.get('judge') or {}).get('what_is_spun', '—')[:60]} | "
                 f"{s['stage']} | {s['listing']['text'][:110]} | {s['verdict']['score']} | {s['verdict']['label'].split(' — ')[0]} |")
    if not confirmed:
        A.append("| — | | | | | |")
    A += ["", "## Probable and indicated", "",
          "| Company | What | Confidence | Stage | Listing | Score |", "|---|---|---|---|---|---:|"]
    for s in probable + indicated:
        A.append(f"| **{s['symbol']}** | {s['family']} | {s['confidence'][0]} — {s['confidence'][1][:60]} | "
                 f"{s['stage']} | {s['listing']['text'][:90]} | {s['verdict']['score']} |")
    if not probable and not indicated:
        A.append("| — | | | | | |")
    A.append("")
    if others:
        A += ["<details><summary>Other restructurings on file (mergers, slump sales, rights, "
              f"capital actions) — {len(others)}</summary>", "",
              "| Company | What | Stage | First filing | Filings |", "|---|---|---|---|---:|"]
        A += [f"| {s['symbol']} | {s['family']} | {s['stage']} | {s['first_filing']} | {s['n_filings']} |"
              for s in others]
        A += ["", "</details>", ""]
    A += ["---", "", "# Confirmed demergers — in full", ""]
    for s in confirmed:
        A += render_company(s, heavy=True)
    A += ["---", "", "# Probable spin-offs and listings", ""]
    for s in probable:
        A += render_company(s, heavy=True)
    A += ["---", "", "# Indicated only", ""]
    for s in indicated:
        A += render_company(s, heavy=False)
    only_calls = record.get("call_only", [])
    A += ["## Indicated on the calls, not yet filed", "",
          "Companies whose management used forward-looking spin-off / demerger / listing language "
          f"in the last {SO.CONCALL_MONTHS} months of calls but have no restructuring filing on file.", ""]
    if only_calls:
        A += ["| Company | Forward-looking / all mentions | Latest forward call | Example |", "|---|---:|---|---|"]
        for c in only_calls:
            A.append(f"| **{c['symbol']}** | {c['forward']} / {c['n']} | {c['latest']} | “{c['example'][:200]}” |")
    else:
        A.append("- (none)")
    A.append("")
    A += ["---", "", "## How this was built", "",
          f"- **Filings:** NSE's corporate-announcements feed read month by month for the "
          f"{m['window_from']} → {m['window_to']} window and filtered to the {m['universe']} official "
          f"NiftyTotalMarket constituents; BSE via its daily RSS (accumulating) and the BSE-sourced "
          f"per-company lists on screener.in. Each filing is classified by category and headline, its "
          f"attachment reduced to text and re-classified from the text. Stored in "
          f"`IndividualStockAnalysis/India/Announcements/NiftyTotalMarket/`.",
          "- **Confidence:** confirmed = a Demerger / Scheme filing or a scheme text that demerges is on "
          "the exchange record; probable = a subsidiary listing in motion or a scheme whose nature the "
          "documents do not settle; indicated = news verification, denial or calls alone.",
          "- **Listing:** from the record date and listing filings; where neither exists, what the "
          "filings and calls say about timing, or that nothing is stated. The 4–10 week note is the "
          "typical gap between record date and listing seen in these filings, not a forecast.",
          "- **Rationale:** every passage in the last 36 months of the stored calls where the "
          "separation was discussed, plus the scheme's rationale section, read by the judge; each "
          "point links to its transcript. Transcripts and presentations are indexed in "
          "`InvestorPresentations/NiftyTotalMarket/_concall_links.csv`.",
          "- **Parent numbers:** the stored consolidated P&L and cash-flow statements (screener.in); "
          "growth and margins computed here. P/E from the live Nifty 500 market file, else latest "
          "stored close ÷ latest fiscal-year EPS. Charts are Mermaid xychart blocks (render on GitHub).",
          "- **Segment numbers:** the last three annual reports and twelve quarterly presentations "
          "(`AnnualReports/`, `InvestorPresentations/`, page-marked text), their segment-reporting "
          "pages read by the judge with document and page per number; growth and margins computed "
          "here. Where the pages do not carry the figures, the report says so.",
          f"- **Judge:** {m['judge']}; reads only the documents shown to it, must quote, cached per "
          "document hash and model.",
          "- **Score:** share of checklist items answered yes (1) or partly (½), on 10 — visibility of "
          "the pattern in the documents, not stock quality.",
          "- **Coverage:** `_coverage.csv` lists, per highlighted company, which of the above was "
          "found and which was not.", ""]
    return "\n".join(A)


# ----------------------------------------------------------------- run

def situation_rows(sits: list[dict]) -> list[dict]:
    out = []
    for s in sits:
        f = s["facts"]
        out.append({"symbol": s["symbol"], "company": s["company"], "kind": s["kind"],
                    "family": s["family"], "confidence": s["confidence"][0],
                    "stage": s["stage"], "listing": s["listing"]["state"],
                    "listing_text": s["listing"]["text"],
                    "first_filing": s["first_filing"], "latest_filing": s["latest_filing"],
                    "listed_on": s.get("listed_on") or "", "n_filings": s["n_filings"],
                    "score": s["verdict"]["score"], "verdict": s["verdict"]["label"],
                    "resulting_company": f.get("resulting_company", ""),
                    "entitlement_ratio": f.get("entitlement_ratio", ""),
                    "record_date": f.get("record_date", ""),
                    "reasons": "; ".join(r["reason"] for r in s["reasons"]),
                    "concall_mentions": len(s["concall_mentions"]),
                    "judge_status": (s.get("judge") or {}).get("status", "")})
    return out


def coverage_rows(sits: list[dict]) -> list[dict]:
    out = []
    for s in sits:
        if s["confidence"][0] not in ("confirmed", "probable"):
            continue
        st = s.get("segment_table") or {}
        docs = s.get("docs", {})
        out.append({"symbol": s["symbol"], "confidence": s["confidence"][0],
                    "listing": s["listing"]["state"],
                    "parent_pnl": "yes" if s["parent_financials"].get("available") else "no",
                    "cash_flow": "yes" if s["cash_flows"].get("available") else "no",
                    "pe": "yes" if s["pe"].get("pe") is not None else "no",
                    "annual_reports": len(docs.get("annual_reports", [])),
                    "presentations": len(docs.get("presentations", [])),
                    "segment_numbers_found": st.get("found_numbers", 0),
                    "segment_status": (s.get("segments") or {}).get("status", ""),
                    "rationale_points": len((s.get("rationale") or {}).get("points") or []),
                    "rationale_status": (s.get("rationale") or {}).get("status", ""),
                    "calls_read_36m": len({e["call"] for e in s.get("rationale_excerpts", [])})})
    return out


def call_only_scan(symbols: list[str], exclude: set[str], today: dt.date) -> list[dict]:
    out = []
    for sym in symbols:
        if sym in exclude:
            continue
        ms = SO.concall_mentions(SO.concall_text(sym), today)
        fwd = [m for m in ms if m["tone"] == "forward"]
        if fwd and len(ms) >= 2:
            out.append({"symbol": sym, "n": len(ms), "forward": len(fwd),
                        "latest": fwd[-1]["call"], "example": fwd[-1]["quote"], "mentions": ms})
    out.sort(key=lambda c: (-c["forward"], -c["n"]))
    return out


def enrich(s: dict, rows: list[dict], ai: bool, today: dt.date, live: dict,
           fetch_docs: bool = False, runner=None) -> None:
    """Everything beyond the mechanical situation: confidence, judge,
    listing status, and — for confirmed / probable — rationale, parent
    numbers, documents and segment numbers."""
    s["confidence"] = SO.confidence(s)
    scheme = scheme_text_for(s, rows)
    s["judge"] = judge(s, scheme, s["concall_mentions"], allow_ai=ai, runner=runner) \
        if s["kind"] in SO.SPIN_KINDS else {}
    s["listing"] = SO.listing_status(s, s["judge"], today)
    if s["confidence"][0] not in ("confirmed", "probable"):
        return
    sym = s["symbol"]
    if fetch_docs:
        import fetch_presentations as FP                      # noqa: PLC0415
        FP.fetch_company(sym)
    s["docs"] = FN.doc_links(sym)
    s["call_links"] = s["docs"]["calls"]
    s["rationale_excerpts"] = FN.rationale_excerpts(sym, today=today)
    s["rationale"] = judge_rationale(s, s["rationale_excerpts"], rationale_section_of(scheme),
                                     allow_ai=ai, runner=runner)
    s["parent_financials"] = FN.parent_financials(sym)
    s["cash_flows"] = FN.cash_flows(sym)
    s["pe"] = FN.pe_ratio(sym, live)
    names = [s["facts"].get("resulting_company", ""), s["facts"].get("demerged_undertaking", "")]
    j = s["judge"] or {}
    for n in (j.get("demerged_business_names") or []):
        if isinstance(n, str):
            names.append(n)
    if isinstance(j.get("what_is_spun"), str):
        names.append(j["what_is_spun"])
    names = [n for n in dict.fromkeys(x.strip() for x in names if x) if len(n) > 3][:8]
    # long descriptions make poor search keys: keep the short names, plus
    # the first two words of a long one
    keys = []
    for n in names:
        keys.append(n if len(n) <= 40 else " ".join(n.split()[:3]))
    s["segment_names"] = keys
    s["segment_excerpts_n"] = 0
    ex = FN.segment_excerpts(sym, keys)
    s["segment_excerpts_n"] = len(ex)
    s["segments"] = judge_segments(s, ex, keys, allow_ai=ai, runner=runner)
    s["segment_table"] = segment_table(s["segments"]) if s["segments"].get("status") in ("judged", "cached") else {}


def cmd_run(args, runner=None) -> dict:
    today = dt.date.today()
    only = {s.strip().upper() for s in args.only.split(",") if s.strip()} or None
    if args.refresh:
        print("refreshing the last year of filings…", file=sys.stderr)
        FA.run(days=args.days, bse=not args.no_bse, pdf=True, only=only)
    rows = SO.load_filings()
    if only:
        rows = [r for r in rows if r["symbol"] in only]
    members = FA.universe()
    live = SO.live_market()
    sits = SO.analyse(rows, today=today, with_calls=not args.no_calls, live=live)
    ai = (runner is not None) or (_ai_available() and not args.quick)
    for s in sits:
        enrich(s, rows, ai, today, live, fetch_docs=args.fetch_docs, runner=runner)
        if s["kind"] in SO.SPIN_KINDS:
            print(f"  {s['symbol']}: {s['confidence'][0]} / {s['stage']} — {s['listing']['state']}"
                  f" [{(s.get('judge') or {}).get('status')} / {(s.get('rationale') or {}).get('status', '-')}"
                  f" / {(s.get('segments') or {}).get('status', '-')}]", file=sys.stderr)
    sits.sort(key=lambda s: (s["kind"] not in SO.SPIN_KINDS,
                             SO.CONFIDENCE_ORDER.get(s["confidence"][0], 9),
                             -s["verdict"]["score"], s["symbol"]))
    call_only = [] if args.no_calls else call_only_scan(
        sorted(members if not only else {s["symbol"] for s in sits}), {s["symbol"] for s in sits}, today)
    dates = [r["date"] for r in rows] or [today.isoformat()]
    meta = {"run_date": today.isoformat(), "window_from": min(dates), "window_to": max(dates),
            "filings": len(rows), "companies": len({r["symbol"] for r in rows}), "universe": len(members),
            "judge": (f"{MODEL} read the schemes, three years of calls and the segment pages" if ai else
                      "not run (--quick or no CLI); mechanical read only")}
    record = {"meta": meta, "situations": sits, "call_only": call_only}
    md = render_report(record)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(md)
    LATEST.write_text(json.dumps(record, indent=1, default=str))
    srows = situation_rows(sits)
    FA.write_csv(SITUATIONS, srows, list(srows[0].keys()) if srows else ["symbol"])
    crows = coverage_rows(sits)
    FA.write_csv(COVERAGE, crows, list(crows[0].keys()) if crows else ["symbol"])
    mrows = [{"symbol": s["symbol"], **mm} for s in sits for mm in s["concall_mentions"]]
    mrows += [{"symbol": c["symbol"], **mm} for c in call_only for mm in c["mentions"]]
    FA.write_csv(MENTIONS, mrows, ["symbol", "call", "term", "tone", "quote"])
    snap = HISTORY / today.isoformat()
    snap.mkdir(parents=True, exist_ok=True)
    for p in (REPORT, SITUATIONS, MENTIONS, COVERAGE):
        if p.exists():
            shutil.copy(p, snap / p.name)
    (snap / "run.json").write_text(json.dumps(record, indent=1, default=str))
    n_conf = sum(1 for s in sits if s.get("confidence", ("",))[0] == "confirmed")
    print(f"wrote {REPORT} ({len(md.splitlines())} lines); {len(sits)} situations, "
          f"{n_conf} confirmed demergers, {len(call_only)} call-only indications", file=sys.stderr)
    return record


def cmd_company(args) -> None:
    rows = [r for r in SO.load_filings() if r["symbol"] == args.symbol.upper()]
    live = SO.live_market()
    sits = SO.analyse(rows, with_calls=True, live=live)
    for s in sits:
        enrich(s, rows, not args.quick, dt.date.today(), live)
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
    r.add_argument("--fetch-docs", action="store_true",
                   help="pull annual reports and presentations for the highlighted companies")
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
