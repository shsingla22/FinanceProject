"""
analyze.py — the ManagementChangeSkill run.

  candidates  the mechanical read (mgmt.py) over every filing's TEXT, the
              exchange's shareholding register, Reg 29 disclosures, bulk and
              block deals and the stored calls → the companies worth reading
  judge       one forced-choice question per candidate company and kind,
              over its COMPLETE documents: did the chief executive or the CFO
              change? did the ownership change? who, when, why, from where
  check       every name and quote the judge gives must be in the documents
  analysis    for each company with a change: three years of financials,
              the track record of the outgoing and the incoming management,
              what was said on the calls, the share price since
  report      MANAGEMENT_CHANGE_REPORT.md (the lists, then each company),
              companies/<SYMBOL>.md, CSVs, the run's JSON

Usage:
  python3 analyze.py run                       # last 365 days, judge on
  python3 analyze.py run --quick               # mechanical only
  python3 analyze.py run --only RBLBANK,TCS --workers 6
  python3 analyze.py render                    # re-render the saved run
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import datetime as dt
import gzip
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mgmt as M            # noqa: E402
import judge as J           # noqa: E402
import track as T           # noqa: E402

INDIA = M.INDIA
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "ManagementChangeAnalysis"
REPORT = OUT_DIR / "MANAGEMENT_CHANGE_REPORT.md"
LATEST = OUT_DIR / "management_change_latest.json"
CHANGES_CSV = OUT_DIR / "_seat_changes.csv"
OWNERSHIP_CSV = OUT_DIR / "_ownership_changes.csv"
CANDIDATES_CSV = OUT_DIR / "_candidates.csv"
SCAN_CACHE = M.DATA / "_scan_cache.json.gz"

KMP_PROMPT_VERSION = "seat-v2"
OWN_PROMPT_VERSION = "own-v2"
DOC_CHARS = 240_000
DOC_HEAD = 5_000
FUTURE_DAYS = 200           # an announced change may take effect after the run date


def set_out_dir(path: Path) -> None:
    global OUT_DIR, REPORT, LATEST, CHANGES_CSV, OWNERSHIP_CSV, CANDIDATES_CSV
    OUT_DIR = Path(path)
    REPORT, LATEST = OUT_DIR / "MANAGEMENT_CHANGE_REPORT.md", OUT_DIR / "management_change_latest.json"
    CHANGES_CSV, OWNERSHIP_CSV = OUT_DIR / "_seat_changes.csv", OUT_DIR / "_ownership_changes.csv"
    CANDIDATES_CSV = OUT_DIR / "_candidates.csv"


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


# ------------------------------------------------------------ candidates

def _scan_job(row: dict) -> tuple[str, dict]:
    s = M.scan_filing(row)
    # keep only what the run needs: the flags and a few evidence lines
    return row["ann_id"], {"kmp_flags": s["kmp_flags"], "own_flags": s["own_flags"], "chars": s["chars"],
                           "kmp": [{k: h[k] for k in ("seat", "event", "person", "lower", "unit", "snippet")} for h in s["kmp"][:6]],
                           "own": [{k: h[k] for k in ("rule", "snippet")} for h in s["own"][:6]]}


def scan_all(filings: list[dict], workers: int = 6) -> dict[str, dict]:
    """The mechanical read of every filing, cached by filing id (the text of
    a filing never changes once read)."""
    cache = {}
    if SCAN_CACHE.exists():
        try:
            with gzip.open(SCAN_CACHE, "rt") as fh:
                cache = json.load(fh)
        except (OSError, json.JSONDecodeError):
            cache = {}
    version = f"{M.ROLE_RX.pattern}{M.APPOINT_RX.pattern}{M.CEASE_RX.pattern}{sorted(M.OWN_RULES)}{M.KMP_OPENING_CHARS}"
    vkey = J.stamp_of(version, *[r.pattern for r in M.OWN_RULES.values()], M.BOILER_RX.pattern, M.TARGET_RX.pattern)
    if cache.get("_version") != vkey:
        cache = {"_version": vkey}
    todo = [r for r in filings if r["ann_id"] not in cache]
    if todo:
        log(f"[scan] {len(todo)} filings to read mechanically ({len(filings) - len(todo)} cached)")
        with cf.ProcessPoolExecutor(max_workers=workers) as ex:
            for i, (aid, res) in enumerate(ex.map(_scan_job, todo, chunksize=64), 1):
                cache[aid] = res
                if i % 5000 == 0:
                    log(f"[scan] {i}/{len(todo)}")
        SCAN_CACHE.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(SCAN_CACHE, "wt") as fh:
            json.dump(cache, fh)
    return cache


def _warm_call(sym: str) -> int:
    return len(M.call_text(sym))


def warm_calls(symbols: list[str], workers: int = 6) -> None:
    todo = [s for s in symbols if (M.CONCALLS / f"{s}.pdf").exists()
            and not ((M.CALL_CACHE / f"{s.replace('&', '_')}.txt").exists()
                     and (M.CALL_CACHE / f"{s.replace('&', '_')}.txt").stat().st_mtime >= (M.CONCALLS / f"{s}.pdf").stat().st_mtime)]
    if not todo:
        return
    log(f"[calls] extracting the text of {len(todo)} transcripts")
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        list(ex.map(_warm_call, todo, chunksize=4))


OPEN_OFFER_CATEGORIES = {"Public Announcement-Open Offer", "Open Offer"}
ROSTER_SKIP = {"Press Release", "Disclosure under SEBI Takeover Regulations", "Shareholders meeting", "Copy of Newspaper Publication"}
STRONG_CALL_RX = re.compile(r"new\s+(?:c\.?e\.?o|c\.?f\.?o|m\.?d\b|managing|chief)|as\s+(?:the\s+|our\s+)?(?:new\s+|group\s+)?(?:c\.?e\.?o|c\.?f\.?o|m\.?d\b|managing|chief)|"
                            r"designate|elect\b|stepp\w+\s+down|step\s+down|last\s+|final\s+|first\s+", re.I)


def build_candidates(today: dt.date, days: int = M.WINDOW_DAYS, only: set[str] | None = None,
                     workers: int = 6) -> dict[str, dict]:
    """{symbol: {'company', 'seat': {...}, 'own': {...}}} — everything the
    mechanical read found, per company, with why it is (or is not) a
    candidate for the judge."""
    members = M.FA.universe()
    filings = [r for r in M.load_filings(today, days) if r["symbol"] in members and (not only or r["symbol"] in only)]
    scans = scan_all(filings, workers)
    symbols = sorted(only & set(members)) if only else sorted(members)
    warm_calls(symbols, workers)
    shp_rows = M.MF.read_csv(M.MF.SHP)
    moves = M.shareholding_moves(shp_rows, today, days)
    sast = M.sast_summary(M.MF.read_csv(M.MF.SAST), today, days)
    deals = M.deals_summary(M.MF.read_csv(M.MF.DEALS), today, M.shares_outstanding(today), days)
    notes = defaultdict(list)
    start, end = M.window(today, days)
    for r in shp_rows:
        if r.get("notes") and start <= r["as_of"] <= end:
            notes[r["symbol"]].append((r["as_of"], r["notes"]))
    by_sym: dict[str, list[dict]] = defaultdict(list)
    for r in filings:
        by_sym[r["symbol"]].append(r)
    out = {}
    for sym in symbols:
        rows = by_sym.get(sym, [])
        seat_rows, own_rows = [], []
        for r in rows:
            s = scans.get(r["ann_id"]) or {}
            if s.get("kmp_flags"):
                seat_rows.append({**r, "flags": s["kmp_flags"], "hits": s.get("kmp", [])})
            if s.get("own_flags") or r["category"] in OPEN_OFFER_CATEGORIES:
                own_rows.append({**r, "flags": s.get("own_flags", []) + (["open_offer_filing"] if r["category"] in OPEN_OFFER_CATEGORIES else []),
                                 "hits": s.get("own", [])})
        ctext = M.call_text(sym)
        chits = M.call_hits(sym, today, text=ctext) if ctext else []
        rost = M.roster_changes(sym, today, text=ctext, company=members[sym]) if ctext else []
        if rost:
            # the calls list a new holder: any filing that names that person is read too, flagged or not
            have = {r["ann_id"] for r in seat_rows}
            names = [n for x in rost for n in x["after"] if len(n.split()) >= 2]
            extra = []
            for r in sorted(rows, key=lambda r: r["date"], reverse=True):
                if r["ann_id"] in have or r["category"] in ROSTER_SKIP:
                    continue
                flat = _flat(M.text_of(r)[:40_000])
                if any(name_in(n, flat) for n in names) and re.search(r"appoint|resign|retir|cessat|ceas|charge|designat|elevat|succe", flat):
                    extra.append({**r, "flags": ["named in a call roster"], "hits": []})
                    if len(extra) >= 5:
                        break
            seat_rows += extra
        seat_calls = [h for h in chits if h["kind"] == "kmp"]
        own_calls = [h for h in chits if h["kind"] == "ownership"]
        strong_calls = [h for h in seat_calls if STRONG_CALL_RX.search(h["term"])]
        seat_why = []
        if seat_rows:
            seat_why.append(f"{len(seat_rows)} filing(s) whose text has an appointment or cessation beside a CEO / MD / CFO seat")
        if rost:
            seat_why.append("the calls list a different " + ", ".join(r["seat"] for r in rost))
        if len(strong_calls) >= 1 and not seat_rows:
            seat_why.append(f"{len(strong_calls)} mention(s) of a new or departing CEO / CFO on the calls")
        mv, ss, dd = moves.get(sym, {}), sast.get(sym, {}), deals.get(sym, {})
        strong_text = [r for r in own_rows if set(r["flags"]) & (set(M.OWN_STRONG) | {"open_offer_filing"})]
        own_why = []
        if mv.get("level") == "major":
            own_why.append(f"promoter holding {mv['base'][1]}% ({mv['base'][0]}) → {mv['latest'][1]}% ({mv['latest'][0]})"
                           + (f"; crossed {', '.join(mv['crossed'])}" if mv.get("crossed") else ""))
        if ss.get("level") == "major":
            own_why.append(f"Reg 29: promoters sold {ss['promoter_sold']}%"
                           + (f"; outsider at {max(o['pct_after'] for o in ss['outsiders'])}%" if ss.get("outsiders") else ""))
        if dd.get("level") == "major":
            own_why.append(f"bulk / block deals: one client sold {dd['top_seller_pct']}% net")
        if any(r["category"] in OPEN_OFFER_CATEGORIES for r in own_rows):
            own_why.append("an open-offer filing")
        if len(strong_text) >= 2 or any("open_offer" in r["flags"] and "change_of_control" in r["flags"] for r in own_rows):
            own_why.append(f"{len(strong_text)} filing(s) whose text speaks of control, an open offer or a promoter reclassification")
        minor = [k for k, v in (("shareholding", mv), ("Reg 29", ss), ("deals", dd)) if v.get("level") == "minor"]
        if not own_why and (len(minor) >= 2 or (minor and (strong_text or len(own_calls) >= 2))):
            own_why.append("smaller moves in " + ", ".join(minor) + (" with ownership language in the filings or calls" if strong_text or own_calls else ""))
        if not own_why and len(own_calls) >= 2 and strong_text:
            own_why.append("ownership language on the calls and in the filings")
        out[sym] = {"symbol": sym, "company": members[sym],
                    "seat": {"candidate": bool(seat_why), "why": seat_why, "filings": seat_rows, "calls": seat_calls, "roster": rost},
                    "own": {"candidate": bool(own_why), "why": own_why, "filings": own_rows, "calls": own_calls,
                            "shareholding": mv, "sast": {k: v for k, v in ss.items() if k != "rows"},
                            "sast_rows": (ss.get("rows") or [])[-25:], "deals": dd, "notes": notes.get(sym, [])[-3:],
                            "minor": minor}}
    return out


# ---------------------------------------------------------- the documents

def docs_text(rows: list[dict], budget: int = DOC_CHARS, head: int = DOC_HEAD) -> str:
    """The filings a judge must read, newest first. Complete when they fit;
    otherwise every filing gives its opening pages first, then whole
    filings shortest first, so no filing is crowded out by a long one."""
    docs, seen = [], set()
    for r in sorted(rows, key=lambda r: r["date"], reverse=True):
        t = M.text_of(r)
        key = J.stamp_of(t[:3000])
        if not t.strip() or key in seen:
            continue
        seen.add(key)
        docs.append((r, t))
    if not docs:
        return ""
    heads = [f"### FILING {r['date']} · {r['category']} · {re.sub(chr(10), ' ', r['headline'])[:150]}\n" for r, _ in docs]
    room = budget - sum(len(h) for h in heads)
    sizes = [len(t) for _, t in docs]
    if sum(sizes) <= room:
        take = sizes[:]
    else:
        h = max(1200, min(head, int(room * 0.6 / len(docs))))
        take = [min(n, h) for n in sizes]
        left = room - sum(take)
        for i in sorted(range(len(docs)), key=lambda i: sizes[i]):
            need = sizes[i] - take[i]
            if 0 < need <= left:
                take[i], left = sizes[i], left - need
        cut = [i for i in range(len(docs)) if take[i] < sizes[i]]
        for i in cut:
            take[i] += min(sizes[i] - take[i], max(0, left) // len(cut))
    parts = []
    for (r, t), hd, n in zip(docs, heads, take):
        parts.append(hd + (t if n >= len(t) else f"[the first {n:,} of {len(t):,} characters]\n" + t[:max(n, 0)]))
    return "\n\n".join(parts)


def calls_block(hits: list[dict], cap: int = 14_000) -> str:
    out, used = [], 0
    for h in hits:
        line = f"[call of {h['call']}] …{h['snippet']}…"
        if used + len(line) > cap:
            break
        out.append(line)
        used += len(line)
    return "\n".join(out)


# ------------------------------------------------------------ the judge

def seat_prompt(c: dict, docs: str, calls: str, start: str, end: str) -> str:
    rost = "; ".join(f"{r['seat']}: {', '.join(r['before'])} (call of {r['from_call']}) → {', '.join(r['after'])} (call of {r['to_call']})"
                     for r in c["seat"].get("roster") or [])
    return (
        f"You are reading the stock-exchange filings of {c['company']} ({c['symbol']}) for an investor who tracks "
        f"MANAGEMENT CHANGE. From the complete documents below and nothing else — never from memory — decide whether "
        f"the company's own CHIEF EXECUTIVE or its CHIEF FINANCIAL OFFICER changed, or was announced to change, "
        f"between {start} and {end}.\n"
        f"The chief executive seat: CEO, Managing Director, MD & CEO, Chairman & Managing Director, or an Executive "
        f"Chairman / Whole-time Director / 'Manager' who IS the company's chief executive. The finance seat: CFO, or "
        f"Director (Finance) of a public-sector company.\n"
        f"A CHANGE is: a new person appointed to the seat; the holder resigning, retiring, dying, being removed, or "
        f"completing a term that is not renewed; an interim or additional-charge holder taking the seat; the seat "
        f"falling vacant; a person RE-DESIGNATED INTO the seat from another post (Executive Director made Managing "
        f"Director, Deputy CFO made CFO, a Whole-time Director made CEO) — the seat has a new holder even though the "
        f"person was already in the company.\n"
        f"NOT a change (report it with is_change false and the reason, so the reader sees it was read): the same "
        f"person re-appointed or extended in the seat they already hold; a title added to a person who ALREADY holds "
        f"the seat (MD made MD & CEO, CFO made Executive Director & CFO); the head of a division, business, region, "
        f"plant or subsidiary; a deputy, joint or assistant seat; one of several Managing Directors who serve under a "
        f"Chairman or CEO who is the chief executive (State Bank of India, LIC); any other senior management; a "
        f"director who is not the chief executive; a company secretary; an auditor; a person's PAST jobs in a "
        f"profile; a letter merely addressed to or signed by the MD or CFO.\n"
        f"Answer STRICT JSON only. Every field from the documents; \"not stated\" when they do not say; quotes verbatim.\n"
        '{"changes": [{'
        '"seat": "CEO" | "MD" | "MD & CEO" | "CMD" | "Executive Chairman" | "CFO", '
        '"designation_as_written": "<the seat in the document\'s words>", '
        '"is_change": true | false, '
        '"not_a_change_because": "<empty when is_change; else: re-appointment | same person, new title | division or subsidiary seat | deputy or joint seat | not the chief executive | other senior management | not this company | other: …>", '
        '"outgoing": {"name": "<full name, no title; empty when a newly created seat>", "last_day": "<YYYY-MM-DD or not stated>", '
        '"reason": "resignation" | "retirement" | "end of term" | "death" | "removal" | "moved to another role in the company or group" | "interim holder replaced" | "not stated", '
        '"reason_in_their_words": "<verbatim, <=40 words; or not stated>", '
        '"in_seat_since": "<YYYY-MM or YYYY when the documents say when this person took the seat; else not stated>", '
        '"stays_on_as": "<another role they keep or move to; or empty>"}, '
        '"incoming": {"name": "<full name, no title; empty when no successor is named>", "effective": "<YYYY-MM-DD or not stated>", '
        '"interim": true | false, '
        '"from_where": "internal" | "external" | "promoter family" | "group company" | "government appointee" | "not stated", '
        '"age": "<years or not stated>", "qualifications": "<as written or not stated>", '
        '"experience_years": "<as written or not stated>", '
        '"previous_roles": [{"company": "<employer>", "role": "<role there>", "from": "<year or not stated>", "to": "<year or not stated>"}], '
        '"profile": "<the documents\' own profile of this person, verbatim, <=120 words; or not stated>"}, '
        '"status": "effective" | "announced, not yet effective" | "seat vacant — no successor named", '
        '"announced_on": "<YYYY-MM-DD of the filing that first says it; when only a call speaks of it, the first day of that call\'s month>", '
        '"quote": "<one verbatim sentence from the documents that STATES the appointment or the departure — never a signature line or a list of names>"}], '
        '"read": "<one sentence: what these documents are about, when there is no change>"}\n'
        "One entry per seat that changed. When one person leaves and another takes the same seat, that is ONE entry "
        "with both. A person who holds two seats (MD & CEO) is one entry. Give every date the documents give: the "
        "outgoing person's last day and the day the incoming person takes the seat decide whether it falls in the period.\n\n"
        + (f"WHAT THE CALL TRANSCRIPTS LIST AS MANAGEMENT (a cross-check, not proof): {rost}\n\n" if rost else "")
        + f"THE FILINGS (newest first):\n{docs or '(no filing text)'}\n\n"
        + (f"PASSAGES FROM THE COMPANY'S EARNINGS CALLS:\n{calls}\n" if calls else "")
    )


def own_prompt(c: dict, docs: str, calls: str, start: str, end: str) -> str:
    o = c["own"]
    mv = o.get("shareholding") or {}
    facts = []
    if mv.get("series"):
        facts.append("Promoter-and-group holding by quarter (exchange shareholding register): "
                     + ", ".join(f"{d}: {v}%" for d, v in mv["series"]))
    for d, n in o.get("notes") or []:
        facts.append(f"Company's note to the {d} shareholding pattern: {n}")
    s = o.get("sast") or {}
    if s:
        facts.append(f"Reg 29 disclosures in the window: promoters sold {s.get('promoter_sold', 0)}% and bought "
                     f"{s.get('promoter_bought', 0)}% of the capital.")
    for r in (o.get("sast_rows") or [])[-18:]:
        facts.append(f"Reg 29 · {r['date']} · {r['acquirer']} ({'promoter' if (r.get('promoter') or '').upper().startswith('Y') else 'not a promoter'}) · "
                     f"{r.get('kind', '')} via {r.get('mode', '')} · acquired {r.get('pct_acquired') or 0}% / sold {r.get('pct_sold') or 0}% · holds {r.get('pct_after') or '?'}% after")
    for cl in (o.get("deals") or {}).get("clients", [])[:6]:
        if abs(cl.get("net_sold_pct") or 0) >= 0.5:
            facts.append(f"Bulk / block deals · {cl['client']} · sold {cl.get('sold_pct')}% and bought {cl.get('bought_pct')}% of the shares outstanding")
    return (
        f"You are reading the record of {c['company']} ({c['symbol']}) for an investor who tracks MANAGEMENT CHANGE "
        f"of the first kind: the PROMOTERS / OWNERS of the company changing. From the exchange facts and the complete "
        f"documents below and nothing else — never from memory — decide what happened to the ownership of THIS "
        f"company between {start} and {end}.\n"
        f"Choose ONE:\n"
        f"- \"change_of_control\": a new promoter or controlling owner has taken over, or the old one has exited "
        f"(share purchase agreement completed, open offer, promoter sold out, government disinvestment, insolvency "
        f"resolution, the parent itself was acquired).\n"
        f"- \"control_change_in_progress\": agreed or announced, not yet completed (agreement signed, open offer "
        f"announced or under way, approvals awaited).\n"
        f"- \"stake_change_no_control_change\": the promoters or a sponsor sold or bought a large block but the same "
        f"people still control the company — or a financial sponsor classified as promoter sold down without a new "
        f"controller arriving.\n"
        f"- \"within_promoter_family\": control passed INSIDE the same promoter family or group — a family "
        f"settlement or separation, a generation handing over, a holding company restructured — and either 5% or "
        f"more of the capital moved or a different person or branch now leads. Say who now leads. A small gift, "
        f"the transmission of a deceased relative's few shares, or a minor member reclassified is \"none\".\n"
        f"- \"dilution_only\": the promoter percentage moved only because the company issued shares (QIP, "
        f"preferential issue, merger, ESOPs, IPO) or bought shares back; nobody sold or bought control.\n"
        f"- \"none\": the documents show no change in ownership (a company buying ANOTHER company is not its own "
        f"ownership changing; a routine pledge or a reclassification of a minor family member is not either).\n"
        f"Answer STRICT JSON only. Every field from the documents and facts; \"not stated\" when they do not say.\n"
        '{"verdict": "change_of_control" | "control_change_in_progress" | "stake_change_no_control_change" | "within_promoter_family" | "dilution_only" | "none", '
        '"what_happened": "<<=60 words, plain>", '
        '"outgoing_owner": {"name": "<who is selling / leaving / diluted; or empty>", "kind": "founder family" | "corporate parent" | "private-equity sponsor" | "government" | "other" | "not stated", '
        '"stake_before": "<% or not stated>", "stake_after": "<% or not stated>", "why": "<their stated reason, verbatim <=40 words; or not stated>"}, '
        '"incoming_owner": {"name": "<who is buying / arriving; or empty>", "kind": "strategic buyer" | "private-equity fund" | "founder family member" | "government" | "public — no single owner" | "other" | "not stated", '
        '"stake_after": "<% or not stated>", "price_per_share": "<₹ or not stated>", "deal_value": "<as written or not stated>", '
        '"who_they_are": "<what the documents say about the buyer: business, size, other holdings, record — verbatim where possible, <=120 words; or not stated>"}, '
        '"mode": "share purchase agreement" | "open offer" | "block or bulk deal" | "offer for sale" | "preferential issue" | "scheme of arrangement" | "insolvency resolution" | "gift or inheritance" | "share issue (dilution)" | "other" | "not stated", '
        '"open_offer": {"made": true | false, "price": "<₹ or not stated>", "size": "<% of capital or not stated>", "status": "<announced | tendering | completed | not stated>"}, '
        '"control_changes": true | false, '
        '"board_or_management_change_with_it": "<what the documents say about directors / CEO changing with the ownership; or not stated>", '
        '"dates": [{"event": "<agreement | public announcement | approval | open offer opens | completion | block deal | other>", "date": "<YYYY-MM-DD>"}], '
        '"announced_on": "<YYYY-MM-DD of the first filing or disclosure that shows it>", '
        '"quote": "<one verbatim sentence from the documents that states it; empty when only the exchange facts show it>"}\n\n'
        f"EXCHANGE FACTS:\n" + ("\n".join(f"- {x}" for x in facts) or "- (none)") + "\n\n"
        f"THE FILINGS (newest first):\n{docs or '(no filing text carries ownership language)'}\n\n"
        + (f"PASSAGES FROM THE COMPANY'S EARNINGS CALLS:\n{calls}\n" if calls else "")
    )


def judge_seat(c: dict, start: str, end: str, allow_ai: bool = True, runner=None) -> dict:
    docs = docs_text(c["seat"]["filings"])
    calls = calls_block(c["seat"]["calls"])
    if not docs and not calls and not c["seat"].get("roster"):
        return {"status": "no documents"}
    prompt = seat_prompt(c, docs, calls, start, end)
    return J.ask(f"{c['symbol']}::seat", J.stamp_of(prompt, KMP_PROMPT_VERSION), prompt, allow_ai, runner, require=("changes",))


def judge_own(c: dict, start: str, end: str, allow_ai: bool = True, runner=None) -> dict:
    docs = docs_text(c["own"]["filings"])
    calls = calls_block(c["own"]["calls"])
    prompt = own_prompt(c, docs, calls, start, end)
    return J.ask(f"{c['symbol']}::own", J.stamp_of(prompt, OWN_PROMPT_VERSION), prompt, allow_ai, runner, require=("verdict",))


# -------------------------------------------------------------- checking

def _flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def name_in(name: str, haystack_flat: str) -> bool:
    """A person's name is in the documents: its surname and first name (or
    initial) both appear, within a short span of each other."""
    words = [w for w in M.norm_name(name).split() if w]
    if not words:
        return False
    if len(words) >= 2 and len(words[0] + words[-1]) >= 7:
        # a PDF whose words run together ('Mr.MonuRatra,whowas…'): the name is there without its spaces
        dense = haystack_flat.replace(" ", "")
        if "".join(words) in dense or (words[0] + words[-1]) in dense:
            return True
    if len(words) == 1:
        return f" {words[0]} " in f" {haystack_flat} "
    first, last = words[0], words[-1]
    for m in re.finditer(r"\b" + re.escape(last) + r"\b", haystack_flat):
        span = haystack_flat[max(0, m.start() - 60):m.end() + 60]
        if re.search(r"\b" + re.escape(first) + (r"\b" if len(first) > 1 else ""), span):
            return True
    return False


def quote_in(quote: str, haystack_flat: str) -> bool:
    """The quote is verbatim: a run of its words appears in the documents
    (PDF text breaks lines and drops punctuation, so 8 consecutive words
    are asked for, not the whole string)."""
    q = _flat(quote).split()
    if len(q) < 4:
        return False
    n = min(8, len(q))
    if any(" ".join(q[i:i + n]) in haystack_flat for i in range(0, len(q) - n + 1)):
        return True
    # the same run with the spaces out: line breaks inside words, or a PDF with no spaces at all
    dense, qd = haystack_flat.replace(" ", ""), "".join(q)
    return len(qd) >= 30 and any(qd[i:i + 36] in dense for i in range(0, max(1, len(qd) - 36 + 1), 6))


CHIEF_SEATS = ("CEO", "MD", "CMD", "EXECUTIVE CHAIRMAN", "MANAGING", "CHIEF EXECUTIVE", "MANAGER")


def seat_group(seat: str, written: str = "") -> str:
    s = f"{seat} {written}".upper()
    if "CFO" in s or "FINANC" in s:
        if not any(k in (seat or "").upper() for k in ("CEO", "MD", "CMD", "CHAIRMAN")):
            return "CFO"
    return "CEO/MD"


def _date(s: str) -> dt.date | None:
    """'2026-01-05' → that day; '2026-01' → the first of the month (a model
    often has only the month); anything else → None."""
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", str(s or ""))
    try:
        if m:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        m = re.fullmatch(r"\s*(\d{4})-(\d{2})\s*", str(s or ""))
        if m:
            return dt.date(int(m.group(1)), int(m.group(2)), 1)
    except ValueError:
        return None
    return None


def settle_seat(c: dict, res: dict, start: str, end: str) -> list[dict]:
    """The judge's seat changes, checked: kept when it is a change, falls in
    the window, and its people and quote are in the documents. Each carries
    `verified` and, when it failed a check, `dropped` with the reason."""
    if not J.ok(res):
        return []
    hay = _flat(" ".join(M.text_of(r) for r in c["seat"]["filings"]) + " " + " ".join(h["snippet"] for h in c["seat"]["calls"]))
    lo, hi = dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    out, seen = [], set()
    for ch in res.get("changes") or []:
        if not isinstance(ch, dict):
            continue
        o = ch.get("outgoing") if isinstance(ch.get("outgoing"), dict) else {}
        i = ch.get("incoming") if isinstance(ch.get("incoming"), dict) else {}
        oname, iname = _clean(o.get("name")), _clean(i.get("name"))
        row = {"seat": str(ch.get("seat") or ""), "designation": _clean(ch.get("designation_as_written")),
               "group": seat_group(str(ch.get("seat") or ""), str(ch.get("designation_as_written") or "")),
               "is_change": bool(ch.get("is_change")), "not_a_change_because": _clean(ch.get("not_a_change_because")),
               "outgoing": {**o, "name": oname}, "incoming": {**i, "name": iname},
               "status": _clean(ch.get("status")), "announced_on": _clean(ch.get("announced_on")), "quote": _clean(ch.get("quote"))}
        if not row["is_change"]:
            row["dropped"] = "not a change: " + (row["not_a_change_because"] or "judge")
            out.append(row)
            continue
        if not oname and not iname:
            row["dropped"] = "no person named"
            out.append(row)
            continue
        dates = [d for d in (_date(row["announced_on"]), _date(o.get("last_day")), _date(i.get("effective"))) if d]
        when = _date(row["announced_on"]) or (min(dates) if dates else None)
        src = sources_for([oname, iname], c["seat"]["filings"], when.isoformat() if when else "")
        if not dates and src:
            # the judge gave no date: the earliest filing that names these people stands in, and says so
            when = min(_date(s["date"]) for s in src)
            dates = [when]
            row["date_basis"] = "the date of the filing that names them"
        if not dates:
            # only the calls speak of it: the first call that names them stands in
            said = sorted(h["date"] for h in c["seat"]["calls"] if h.get("date")
                          and any(name_in(n, _flat(h["snippet"])) for n in (oname, iname) if n))
            if said:
                when = _date(said[0])
                dates = [when]
                row["date_basis"] = f"first mentioned on the call of {said[0][:7]}; the documents give no date"
        row["when"] = when.isoformat() if when else ""
        # the event itself — the day the new person took the seat, or the old one left — decides the window;
        # a shareholders' vote months later on an appointment already in effect does not bring it back in
        event = [d for d in (_date(o.get("last_day")), _date(i.get("effective"))) if d]
        latest = max(event) if event else (max(dates) if dates else None)
        if not dates:
            row["dropped"] = "no date in the documents (the change may predate the window)"
        elif latest and latest < lo:
            row["dropped"] = f"before the window ({latest.isoformat()})"
        elif when and when > hi:
            row["dropped"] = f"dated after the run ({when.isoformat()})"
        names_ok = all(name_in(n, hay) for n in (oname, iname) if n)
        q_ok = quote_in(row["quote"], hay)
        says = bool(M.APPOINT_RX.search(row["quote"]) or M.CEASE_RX.search(row["quote"])
                    or re.search(r"\bnew\b|\bfirst\b|\bwelcome\b|\bcharge\b|\bvice\b|\bin place of\b", row["quote"], re.I))
        row["verified"] = bool(names_ok and q_ok and says)
        row["checks"] = {"names_in_documents": names_ok, "quote_in_documents": q_ok, "quote_states_a_change": says}
        if not names_ok and "dropped" not in row:
            row["dropped"] = "a name the judge gave is not in the documents"
        key = (row["group"], M.norm_name(oname), M.norm_name(iname))
        if key in seen:
            continue
        seen.add(key)
        row["sources"] = src
        out.append(row)
    return out


def sources_for(names: list[str], filings: list[dict], near: str = "", n: int = 4) -> list[dict]:
    """The filings that name these people, the ones nearest the announcement
    first — the documents a reader should open for this change."""
    hits = []
    for r in filings:
        flat = _flat(M.text_of(r))
        if any(name_in(x, flat) for x in names if x):
            gap = abs((_date(r["date"]) - _date(near)).days) if _date(near) and _date(r["date"]) else 9999
            hits.append((gap, r["date"], r))
    hits.sort(key=lambda x: (x[0], x[1]))
    return [{k: r.get(k, "") for k in ("date", "category", "headline", "attachment", "ann_id")} for _, _, r in hits[:n]]


def _clean(x) -> str:
    s = re.sub(r"\s+", " ", str(x or "")).strip()
    return "" if s.lower() in ("not stated", "none", "n/a", "na", "null", "-", "—", "empty") else s


STAKE_MIN = 2.0             # a stake change under the same controller is listed from two points of the capital

OWN_KEEP = ("change_of_control", "control_change_in_progress", "stake_change_no_control_change", "within_promoter_family")
OWN_LABEL = {"change_of_control": "Change of control — completed", "control_change_in_progress": "Change of control — in progress",
             "stake_change_no_control_change": "Large stake change, same controller", "within_promoter_family": "Within the promoter family / group",
             "dilution_only": "Dilution only (shares issued)", "none": "No ownership change"}


def settle_own(c: dict, res: dict) -> dict:
    if not J.ok(res):
        return {}
    v = str(res.get("verdict") or "none")
    hay = _flat(" ".join(M.text_of(r) for r in c["own"]["filings"]) + " " + " ".join(h["snippet"] for h in c["own"]["calls"])
                + " " + " ".join(n for _, n in c["own"].get("notes") or [])
                + " " + " ".join(f"{r.get('acquirer', '')}" for r in c["own"].get("sast_rows") or [])
                + " " + " ".join(cl["client"] for cl in (c["own"].get("deals") or {}).get("clients", [])))
    o = res.get("outgoing_owner") if isinstance(res.get("outgoing_owner"), dict) else {}
    i = res.get("incoming_owner") if isinstance(res.get("incoming_owner"), dict) else {}
    out = {"verdict": v, "label": OWN_LABEL.get(v, v), "keep": v in OWN_KEEP,
           "what_happened": _clean(res.get("what_happened")), "outgoing_owner": {k: _clean(x) for k, x in o.items()},
           "incoming_owner": {k: _clean(x) for k, x in i.items()}, "mode": _clean(res.get("mode")),
           "open_offer": res.get("open_offer") if isinstance(res.get("open_offer"), dict) else {},
           "control_changes": bool(res.get("control_changes")),
           "board_or_management_change_with_it": _clean(res.get("board_or_management_change_with_it")),
           "dates": [d for d in (res.get("dates") or []) if isinstance(d, dict) and _date(d.get("date"))],
           "announced_on": _clean(res.get("announced_on")), "quote": _clean(res.get("quote"))}
    q_ok = quote_in(out["quote"], hay) if out["quote"] else None
    names = [n for n in (out["outgoing_owner"].get("name"), out["incoming_owner"].get("name")) if n]
    # an owner's name is a company or a person: its first distinctive word must be in the record
    def owner_in(n: str) -> bool:
        ws = [w for w in _flat(n).split() if len(w) > 3 and w not in ("limited", "private", "group", "family", "promoter", "promoters", "public", "holdings")]
        return not ws or any(f" {w} " in f" {hay} " for w in ws[:3])
    n_ok = all(owner_in(n) for n in names)
    out["checks"] = {"names_in_record": n_ok, "quote_in_documents": q_ok}
    out["verified"] = bool(n_ok and q_ok is not False)
    # how much of the capital the exchange's own registers show moving
    mv, ss, dd = c["own"].get("shareholding") or {}, c["own"].get("sast") or {}, c["own"].get("deals") or {}
    moved = max(abs(mv.get("change") or 0), abs(mv.get("max_step") or 0), ss.get("promoter_sold") or 0, ss.get("promoter_bought") or 0,
                dd.get("top_seller_pct") or 0, dd.get("top_buyer_pct") or 0)
    out["moved_pct"] = round(moved, 2)
    if v == "stake_change_no_control_change" and moved < STAKE_MIN:
        out["keep"] = False
        out["label"] = f"Stake change under {STAKE_MIN:g} points, same controller"
    return out


# -------------------------------------------------------------- analysis

def _company_symbol(name: str, members: dict[str, str]) -> str:
    """A universe company named in a profile ('ex-CFO of Tata Steel Limited') → its symbol."""
    want = M.FA.__dict__.get("_norm") or None
    def norm(n):
        n = re.sub(r"\b(limited|ltd\.?|private|pvt\.?|india|the|company|corporation|corp\.?)\b", " ", n or "", flags=re.I)
        return re.sub(r"[^a-z0-9]", "", n.lower())
    key = norm(name)
    if len(key) < 4:
        return ""
    for sym, co in members.items():
        if norm(co) == key:
            return sym
    return ""


TOP_ROLE_RX = re.compile(r"chief\s+executive|\bc\.?e\.?o\b|managing\s+director|\bm\.?d\b|chief\s+financ|\bc\.?f\.?o\b|"
                         r"whole[\s-]?time\s+director|executive\s+director|director\s*\(?finance|\bpresident\b|country\s+(?:head|manager)|chairman", re.I)
LOWER_ROLE_RX = re.compile(r"\b(?:deputy|dy\.?|vice|assistant|asst\.?|associate|trainee|regional|zonal|joint)\b", re.I)
CONTEXT_YEARS = 5


def outgoing_record(sym: str, ch: dict) -> dict:
    """The company's results while the outgoing person held the seat."""
    o = ch["outgoing"]
    if not o.get("name"):
        return {"available": False, "why": "no outgoing person (a new seat, or not named)"}
    since, basis = T.fy_of(o.get("in_seat_since")), "the filing"
    at_floor = False
    if not since:
        floor = T.seat_since(sym, o["name"], ch["group"].split("/")[0])
        at_floor = bool(floor and floor == T.reports_floor(sym))
        since, basis = floor, ("the earliest annual report on file — they held the seat at least since then, possibly for years before"
                               if at_floor else "the annual reports on file")
    last = _date(o.get("last_day")) or _date(ch.get("announced_on"))
    end_fy = None
    if last:
        fy = T.fy_of(last.isoformat())
        end_fy = fy if (last.month == 3 and last.day >= 25) else fy - 1
    rec = T.tenure_record(sym, since, end_fy)
    if not since:
        # the date they took the seat is not on file: the company's last few years, as context only
        s = T.series(sym)
        fys = [fy for fy, v in zip(s.get("fy") or [], s.get("revenue") or []) if fy and v is not None]
        if fys:
            last = min(end_fy or max(fys), max(fys))
            rec = T.tenure_record(sym, last - CONTEXT_YEARS + 1, last)
            rec["context_only"] = True
    rec.update({"name": o["name"], "since_fy": since, "since_basis": basis if since else "", "at_floor": at_floor,
                "elsewhere": T.seats_held(o["name"], exclude_symbol=sym)})
    return rec


def incoming_record(sym: str, ch: dict, members: dict[str, str]) -> dict:
    """What is on file about the incoming person: the documents' profile,
    earlier seats the annual reports on file show them in, and — where an
    earlier employer is a universe company — its results in those years."""
    i = ch["incoming"]
    if not i.get("name"):
        return {"available": False, "why": "no successor named"}
    out = {"available": True, "name": i["name"], "from_where": _clean(i.get("from_where")), "age": _clean(i.get("age")),
           "qualifications": _clean(i.get("qualifications")), "experience_years": _clean(i.get("experience_years")),
           "profile": _clean(i.get("profile")), "previous_roles": [], "seats_on_file": [], "records": []}
    for p in i.get("previous_roles") or []:
        if not isinstance(p, dict) or not _clean(p.get("company")):
            continue
        row = {"company": _clean(p.get("company")), "role": _clean(p.get("role")), "from": _clean(p.get("from")), "to": _clean(p.get("to"))}
        psym = _company_symbol(row["company"], members)
        row["symbol"] = psym
        out["previous_roles"].append(row)
        a, b = T.fy_of(row["from"]), T.fy_of(row["to"])
        if psym and psym != sym and a and TOP_ROLE_RX.search(row["role"]) and not LOWER_ROLE_RX.search(row["role"]):
            rec = T.tenure_record(psym, a, (b - 1) if b else None)
            if rec.get("available"):
                out["records"].append({**rec, "company": row["company"], "role": row["role"], "basis": "the filing's profile"})
    # seats at OTHER companies only: an insider's earlier years here are in the company's own numbers above,
    # and the annual-report read of names is too loose to draw a record from a single year
    for s in T.seats_held(i["name"], exclude_symbol=sym):
        out["seats_on_file"].append(s)
        if any(r.get("symbol") == s["symbol"] for r in out["records"]) or s["last_fy"] - s["first_fy"] < 1:
            continue
        if not TOP_ROLE_RX.search(s["role"]):
            continue
        rec = T.tenure_record(s["symbol"], s["first_fy"], s["last_fy"])
        if rec.get("available"):
            out["records"].append({**rec, "company": members.get(s["symbol"], s["symbol"]), "role": s["role"],
                                   "basis": f"annual reports on file show the seat FY{s['first_fy']}–FY{s['last_fy']}"})
    return out


def owner_record(owner: dict, members: dict[str, str]) -> dict:
    """An incoming or outgoing owner that is itself a universe company: its
    last three years."""
    sym = _company_symbol(owner.get("name", ""), members)
    if not sym:
        return {"available": False}
    return {"available": True, "symbol": sym, "company": members[sym], "financials": T.financials(sym)}


def call_exchanges(sym: str, names: list[str], kind_rx: re.Pattern, today: dt.date, months: int = 13) -> list[dict]:
    """Every exchange on the calls of the window about the change — the
    question and every answer to it, uncut; complete sentences from the
    prepared remarks. Reuses the speaker-turn reader of the SpinOffSkill."""
    text = M.call_text(sym)
    if not text:
        return []
    try:
        sys.path.insert(0, str(INDIA / "Skills" / "SpinOffSkill" / "scripts"))
        import deal as DL                                # noqa: PLC0415
    except Exception:                                    # noqa: BLE001
        return []
    surnames = [w for n in names for w in [M.norm_name(n).split()[-1:] or [""]][0:1] for w in w if len(w) >= 4]
    extra = "|".join(r"\b" + re.escape(M.norm_name(n)).replace(r"\ ", r"\s+") + r"\b" for n in names if len(M.norm_name(n).split()) >= 2)
    rx = re.compile(kind_rx.pattern + ("|" + extra if extra else ""), re.I | re.S)
    cutoff = dt.date(today.year, today.month, 1) - dt.timedelta(days=months * 31)
    out = []
    for label, d, body in M.call_sections(text):
        if d < cutoff or d > today:
            continue
        try:
            ex = DL.exchanges_in(body, rx)
        except Exception:                                # noqa: BLE001
            ex = []
        if ex:
            out.append({"call": label, "date": d.isoformat(), "exchanges": ex[:12]})
    return out


def corporate_actions(today: dt.date, days: int) -> dict[str, list[tuple[str, str]]]:
    """{symbol: [(ex-date, purpose)]} for splits, bonuses, demergers and
    rights in the window — a price across one of these is not comparable."""
    out: dict[str, list[tuple[str, str]]] = defaultdict(list)
    path = INDIA / "Announcements" / "NiftyTotalMarket" / "_demerger_ground_truth.csv"
    for r in M.MF.read_csv(path):
        d = r.get("record_date") or r.get("date") or ""
        if d:
            out[r.get("symbol", "")].append((d, r.get("purpose") or "demerger"))
    return out


_ACTIONS_RX = re.compile(r"split|sub-?division|bonus|demerger|rights|consolidation|capital reduction", re.I)


def price_block(sym: str, announced: str, today: dt.date, actions: dict) -> dict:
    p = T.price_since(sym, announced, today)
    if not p.get("available"):
        return p
    between = [(d, why) for d, why in actions.get(sym, []) if p["before"][0] < d <= p["latest"][0] and _ACTIONS_RX.search(why)]
    ratio = p["latest"][1] / p["before"][1] if p["before"][1] else 1
    if between or ratio < 0.45 or ratio > 2.6:
        p["not_comparable"] = (f"{between[0][1]} on {between[0][0]}" if between
                               else "the price moved by more than a split or demerger would explain away — check for a corporate action")
    return p


def enrich(c: dict, today: dt.date, members: dict[str, str], actions: dict) -> None:
    """Everything a reader needs for a company with a change."""
    sym = c["symbol"]
    seat = [ch for ch in c.get("seat_changes", []) if not ch.get("dropped")]
    own = c.get("ownership") if (c.get("ownership") or {}).get("keep") else None
    c["financials"] = T.financials(sym)
    announced = sorted([ch.get("when") or ch.get("announced_on") for ch in seat if ch.get("when") or ch.get("announced_on")]
                       + ([own["announced_on"]] if own and own.get("announced_on") else []))
    c["first_announced"] = announced[0] if announced else ""
    c["price"] = price_block(sym, c["first_announced"], today, actions) if c["first_announced"] else {"available": False}
    for ch in seat:
        ch["outgoing_record"] = outgoing_record(sym, ch)
        ch["incoming_record"] = incoming_record(sym, ch, members)
    names = [n for ch in seat for n in (ch["outgoing"].get("name"), ch["incoming"].get("name")) if n]
    c["call_exchanges"] = []
    if seat:
        c["call_exchanges"] += [{**x, "about": "the seat"} for x in call_exchanges(sym, names, M.CALL_KMP_RX, today)]
    if own:
        c["call_exchanges"] += [{**x, "about": "the ownership"} for x in call_exchanges(sym, [], M.CALL_OWN_RX, today)]
        own["incoming_record"] = owner_record(own.get("incoming_owner") or {}, members)
        own["outgoing_record"] = owner_record(own.get("outgoing_owner") or {}, members)


# ------------------------------------------------------------- rendering

def _v(x) -> str:
    if x is None:
        return "—"
    if isinstance(x, (int, float)):
        return f"{x:,.1f}" if abs(x) < 100 else f"{x:,.0f}"
    return str(x)


def _rupee(x) -> str:
    s = str(x or "").strip()
    return s if re.match(r"(?:₹|rs\.?|inr|`)", s, re.I) else f"₹{s}"


def _short(x, n: int = 70) -> str:
    s = re.sub(r"\s+", " ", str(x or "")).replace("|", "/").strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def _cell(x) -> str:
    return re.sub(r"\s+", " ", str(x or "—")).replace("|", "/").strip() or "—"


def table_md(fin: dict) -> list[str]:
    A = ["| | " + " | ".join(fin["years"]) + " |", "|---|" + "---:|" * len(fin["years"])]
    for r in fin["rows"]:
        A.append(f"| {r['metric']} | " + " | ".join(_v(v) for v in r["values"]) + " |")
    return A


def record_md(rec: dict) -> list[str]:
    A = [f"| {rec['from']} → {rec['to']} | At the start | At the end | Change |", "|---|---:|---:|---|"]
    for r in rec["rows"]:
        A.append(f"| {r['metric']} | {_v(r['start'])} | {_v(r['end'])} | {r['change']} |")
    return A


def source_links(rows: list[dict], n: int = 6) -> str:
    out = []
    for r in sorted(rows, key=lambda r: r["date"], reverse=True)[:n]:
        label = f"{r['date']} {_short(r['category'], 34)}"
        out.append(f"[{label}]({r['attachment']})" if r.get("attachment") else label)
    more = f" · +{len(rows) - n} more" if len(rows) > n else ""
    return " · ".join(out) + more


def seat_line(ch: dict) -> tuple[str, str, str, str]:
    o, i = ch["outgoing"], ch["incoming"]
    out = o.get("name") or "— (new seat)"
    if o.get("name"):
        bits = [x for x in (_clean(o.get("reason")), f"last day {o['last_day']}" if _date(o.get("last_day")) else "") if x]
        out += f" ({'; '.join(bits)})" if bits else ""
    inc = i.get("name") or "— not named"
    if i.get("name"):
        bits = [x for x in ("interim" if i.get("interim") else "", _clean(i.get("from_where")),
                            f"from {i['effective']}" if _date(i.get("effective")) else "") if x]
        inc += f" ({'; '.join(bits)})" if bits else ""
    return ch.get("designation") or ch["seat"], out, inc, ch.get("status") or "—"


def render_company(c: dict, verbatim: bool = True) -> list[str]:
    sym = c["symbol"]
    seat = [ch for ch in c.get("seat_changes", []) if not ch.get("dropped")]
    own = c.get("ownership") if (c.get("ownership") or {}).get("keep") else None
    kinds = ([own["label"]] if own else []) + sorted({("CEO / MD change" if ch["group"] == "CEO/MD" else "CFO change") for ch in seat})
    A = [f"## {sym} — {c['company']}", "", f"**{' · '.join(kinds)}**", ""]

    # 1 — what is changing
    A += ["### 1. What is changing", ""]
    if own:
        o, i = own["outgoing_owner"], own["incoming_owner"]
        A += [f"**Ownership — {own['label']}.** {own['what_happened']}", "",
              "| | Who | Kind | Stake before | Stake after |", "|---|---|---|---|---|",
              f"| Outgoing | {_cell(o.get('name'))} | {_cell(o.get('kind'))} | {_cell(o.get('stake_before'))} | {_cell(o.get('stake_after'))} |",
              f"| Incoming | {_cell(i.get('name'))} | {_cell(i.get('kind'))} | — | {_cell(i.get('stake_after'))} |", ""]
        bits = [f"mode: {own['mode']}" if own.get("mode") else "",
                f"price {_rupee(i['price_per_share'])}" if i.get("price_per_share") else "",
                f"deal value {i['deal_value']}" if i.get("deal_value") else "",
                "control changes" if own.get("control_changes") else "control does not change"]
        A += ["- " + " · ".join(b for b in bits if b)]
        oo = own.get("open_offer") or {}
        if oo.get("made"):
            A += [f"- Open offer: price {_cell(oo.get('price'))}, size {_cell(oo.get('size'))}, status {_cell(oo.get('status'))}"]
        if o.get("why"):
            A += [f"- Why the seller is selling, in their words: “{o['why']}”"]
        if own.get("board_or_management_change_with_it"):
            A += [f"- Management changing with it: {own['board_or_management_change_with_it']}"]
        if own.get("dates"):
            A += ["- Dates: " + "; ".join(f"{d.get('event', 'event')} {d['date']}" for d in sorted(own["dates"], key=lambda d: d["date"]))]
        if own.get("quote"):
            A += [f"- In the documents: “{own['quote']}”"]
        mv = c["own"].get("shareholding") or {}
        if mv.get("series"):
            A += ["", "**Promoter-and-group holding, quarter by quarter (NSE shareholding register):** "
                  + " → ".join(f"{v}% ({d})" for d, v in mv["series"])]
        s = c["own"].get("sast") or {}
        if s.get("promoter_sold") or s.get("promoter_bought") or s.get("outsiders"):
            A += [f"**Reg 29 disclosures in the window:** promoters sold {s.get('promoter_sold', 0)}% and bought {s.get('promoter_bought', 0)}%"
                  + ("; outside acquirers at 10% or more: " + "; ".join(f"{x['acquirer']} {x['pct_after']}% ({x['date']})" for x in s["outsiders"][:4])
                     if s.get("outsiders") else "") + "."]
        dl = [cl for cl in (c["own"].get("deals") or {}).get("clients", []) if abs(cl.get("net_sold_pct") or 0) >= 1]
        if dl:
            A += ["**Bulk / block deals (net, % of shares outstanding):** "
                  + "; ".join(f"{cl['client'].title()} {'sold' if cl['net_sold_pct'] > 0 else 'bought'} {abs(cl['net_sold_pct'])}%" for cl in dl[:6]) + "."]
        if c["own"]["filings"]:
            A += ["", "*Filings read for the ownership:* " + source_links(c["own"]["filings"])]
        if not own.get("verified"):
            A += ["", "> ⚠ A name or the quote above could not be matched to the documents mechanically — read the filing before relying on it."]
        A += [""]
    if seat:
        A += ["| Seat | Outgoing | Incoming | Status | First said on |", "|---|---|---|---|---|"]
        for ch in seat:
            d, o_, i_, st = seat_line(ch)
            A.append(f"| **{_cell(d)}** | {_cell(o_)} | {_cell(i_)} | {_cell(st)} | {_cell(ch.get('announced_on'))} |")
        A += [""]
        for ch in seat:
            o = ch["outgoing"]
            if o.get("reason_in_their_words"):
                A += [f"- **Why {o.get('name') or 'the holder'} is leaving, in the filing's words:** “{o['reason_in_their_words']}”"
                      + (f" Stays on as: {o['stays_on_as']}." if o.get("stays_on_as") else "")]
            elif o.get("stays_on_as"):
                A += [f"- {o.get('name')} stays on as: {o['stays_on_as']}."]
            if ch.get("quote"):
                A += [f"- In the documents: “{ch['quote']}”"
                      + (" — " + source_links(ch["sources"], 3) if ch.get("sources") else "")]
            if not ch.get("verified"):
                ck = ch.get("checks") or {}
                why = ("the quote is in the documents but does not itself state an appointment or a departure"
                       if ck.get("quote_in_documents") and not ck.get("quote_states_a_change")
                       else "the quote could not be matched word for word to the documents")
                A += [f"  > ⚠ Not fully verified — {why}. Read the filing before relying on it."]
            if ch.get("date_basis"):
                A += [f"  > Date: {ch['date_basis']}."]
        A += ["", f"*All {len(c['seat']['filings'])} filing(s) read for the seats:* " + source_links(c["seat"]["filings"]), ""]

    # 2 — financials
    A += ["### 2. Financials — the last three years", ""]
    fin = c.get("financials") or {}
    if fin.get("available"):
        A += table_md(fin) + ["", f"*Source: {fin['source']}.*", ""]
    else:
        A += ["No statements on file for this company.", ""]
    p = c.get("price") or {}
    if p.get("available"):
        if p.get("not_comparable"):
            A += [f"**Share price since the announcement:** ₹{p['before'][1]:,.2f} ({p['before'][0]}) and ₹{p['latest'][1]:,.2f} "
                  f"({p['latest'][0]}) — not comparable: {p['not_comparable']}.", ""]
        else:
            idx = f"; Nifty 500 {p['index_change_pct']:+.1f}% over the same days" if p.get("index_change_pct") is not None else ""
            A += [f"**Share price since the announcement:** ₹{p['before'][1]:,.2f} on {p['before'][0]} (the close before) → "
                  f"₹{p['latest'][1]:,.2f} on {p['latest'][0]}: **{p['change_pct']:+.1f}%**{idx}. Unadjusted closes from the NSE bhavcopy.", ""]

    # 3 — outgoing
    A += ["### 3. Track record — the outgoing management", ""]
    any3 = False
    if own:
        o = own["outgoing_owner"]
        if o.get("name"):
            any3 = True
            A += [f"**{o['name']}** ({o.get('kind') or 'owner'}) — the outgoing owner. The record of the company under this ownership is the "
                  f"financials above; the promoter holding moved {_cell(o.get('stake_before'))} → {_cell(o.get('stake_after'))}.", ""]
            rec = own.get("outgoing_record") or {}
            if rec.get("available") and rec["financials"].get("available"):
                A += [f"The seller is itself in the universe ({rec['symbol']}); its own last three years:", ""] + table_md(rec["financials"]) + [""]
    for ch in seat:
        rec = ch.get("outgoing_record") or {}
        o = ch["outgoing"]
        if not o.get("name"):
            continue
        any3 = True
        A += [f"**{o['name']}** — {ch.get('designation') or ch['seat']}"
              + ((f", in the seat since at least FY{rec['since_fy']} ({rec['since_basis']})" if rec.get("at_floor")
                  else f", in the seat since FY{rec['since_fy']} per {rec['since_basis']}") if rec.get("since_fy")
                 else ", date of taking the seat not on file") + ".", ""]
        if rec.get("available") and rec.get("context_only"):
            A += [f"When they took the seat is not in the documents or annual reports on file, so no tenure can be drawn. For context "
                  f"only, the company's results over the last {rec['years']} fiscal years:", ""]
            A += record_md(rec) + [""]
        elif rec.get("available"):
            A += [("The company's results over the part of the tenure the reports on file cover" if rec.get("at_floor")
                   else "The company's results while they held the seat (the year before they took it, to the last full year they held it")
                  + ("; the statements on file start later than the tenure" if rec.get("clipped") else "")
                  + (":" if rec.get("at_floor") else "):"), ""]
            A += record_md(rec) + [""]
        else:
            A += [f"*No tenure record: {rec.get('why', 'not determinable')}.*", ""]
        for s in rec.get("elsewhere") or []:
            A += [f"- Also on file: {s['role']} at {s['symbol']} (FY{s['first_fy']}–FY{s['last_fy']}, annual reports)."]
        if rec.get("elsewhere"):
            A += [""]
    if not any3:
        A += ["No outgoing person or owner is named (a new seat, or the documents do not say).", ""]

    # 4 — incoming
    A += ["### 4. Track record — the incoming management", ""]
    any4 = False
    if own:
        i = own["incoming_owner"]
        if i.get("name"):
            any4 = True
            A += [f"**{i['name']}** ({i.get('kind') or 'owner'}) — the incoming owner."
                  + (f" Holding after: {i['stake_after']}." if i.get("stake_after") else ""), ""]
            if i.get("who_they_are"):
                A += [f"What the documents say about them: “{i['who_they_are']}”", ""]
            rec = own.get("incoming_record") or {}
            if rec.get("available") and rec["financials"].get("available"):
                A += [f"The buyer is itself in the universe ({rec['symbol']}); its own last three years:", ""] + table_md(rec["financials"]) + [""]
            elif not i.get("who_they_are"):
                A += ["*The documents on file say nothing about the buyer's own record, and it is not a company in the universe.*", ""]
    for ch in seat:
        rec = ch.get("incoming_record") or {}
        if not rec.get("available"):
            continue
        any4 = True
        facts = [x for x in (f"from: {rec['from_where']}" if rec.get("from_where") else "",
                             f"age {rec['age']}" if rec.get("age") else "",
                             f"experience: {rec['experience_years']}" if rec.get("experience_years") else "",
                             f"qualifications: {rec['qualifications']}" if rec.get("qualifications") else "") if x]
        A += [f"**{rec['name']}** — {ch.get('designation') or ch['seat']}" + (" (interim)" if ch["incoming"].get("interim") else "")
              + (". " + "; ".join(facts) if facts else "") + ".", ""]
        if rec.get("profile"):
            A += [f"The filing's own profile: “{rec['profile']}”", ""]
        if rec.get("previous_roles"):
            A += ["| Earlier role | Company | From | To |", "|---|---|---|---|"]
            for pr in rec["previous_roles"][:10]:
                A.append(f"| {_cell(pr['role'])} | {_cell(pr['company'])}{' (' + pr['symbol'] + ')' if pr.get('symbol') else ''} | {_cell(pr['from'])} | {_cell(pr['to'])} |")
            A += [""]
        for r in rec.get("records") or []:
            A += [f"Results of **{r['company']}** while they were {r['role']} there ({r['basis']}):", ""] + record_md(r) + [""]
        if not rec.get("profile") and not rec.get("previous_roles") and not rec.get("records"):
            A += ["*The filings on file give no profile of this person, and the annual reports on file do not show them in an earlier seat.*", ""]
    if not any4:
        A += ["No successor or new owner is named yet.", ""]

    # 5 — calls
    A += ["### 5. On the calls", ""]
    ex = c.get("call_exchanges") or []
    if ex:
        n = sum(len(x["exchanges"]) for x in ex)
        A += [f"{n} passage(s) from {len(ex)} call(s) in the window, oldest first — each question with every answer to it, as the transcript prints it.", ""]
        if verbatim:
            for x in ex:
                A += [f"#### {x['call']} — about {x['about']}", ""]
                for e in x["exchanges"]:
                    A += ["**" + ("Question and answer" if e.get("kind") == "qa" else "From the prepared remarks") + "**", ""]
                    for who, said in e["turns"]:
                        A += [f"> **{who}:** {said}", ">"]
                    A[-1] = ""
        else:
            A += ["| Call | About | Passages |", "|---|---|---:|"] + [f"| {x['call']} | {x['about']} | {len(x['exchanges'])} |" for x in ex]
            A += ["", f"*Every passage in full: [companies/{sym.replace('&', '_')}.md](companies/{sym.replace('&', '_')}.md).*", ""]
    else:
        A += ["Nothing about the change in the calls on file for the window" + ("" if M.call_text(sym) else " (no transcripts on file)") + ".", ""]
    return A


def summary_tables(record: dict) -> list[str]:
    cos = record["companies"]
    A = []
    own = sorted([c for c in cos if (c.get("ownership") or {}).get("keep")],
                 key=lambda c: (list(OWN_KEEP).index(c["ownership"]["verdict"]), c["symbol"]))
    A += ["## List 1 — the promoters / owners changing", "",
          f"{len(own)} companies, in three groups. Every row was read from the documents and the exchange's own registers.", ""]
    groups = (("1a. Change of control", ("change_of_control", "control_change_in_progress"),
               "A new promoter or controlling owner has arrived, or the old one has left — completed, or agreed and in progress."),
              ("1b. Large stake change, same controller", ("stake_change_no_control_change",),
               f"The promoters or a sponsor sold or bought {STAKE_MIN:g} points or more of the capital; the same people still control the company. "
               "Promoter selling first, largest fall first; then promoter buying."),
              ("1c. Inside the promoter family or group", ("within_promoter_family",),
               "Control passed within the same family or group — a settlement, a generation handing over, a holding company restructured."))
    for title, verdicts, note in groups:
        rows = [c for c in own if c["ownership"]["verdict"] in verdicts]
        if verdicts == ("stake_change_no_control_change",):
            rows.sort(key=lambda c: ((c["own"].get("shareholding") or {}).get("change") or 0, c["symbol"]))
        A += [f"### {title}", "", f"{len(rows)} companies. {note}", "",
              "| Company | What | Outgoing / selling | Incoming / buying | Promoter holding (register) | Mode | First shown | Sources |",
              "|---|---|---|---|---|---|---|---|"]
        for c in rows:
            o = c["ownership"]
            mv = c["own"].get("shareholding") or {}
            hold = f"{mv['base'][1]}% → {mv['latest'][1]}%" if mv.get("base") else "—"
            lead = "**In progress.** " if o["verdict"] == "control_change_in_progress" else ""
            A.append(f"| **{c['symbol']}** — {_short(c['company'], 34)} | {lead}{_short(o['what_happened'], 190)} | "
                     f"{_short(o['outgoing_owner'].get('name') or '—', 44)} | {_short(o['incoming_owner'].get('name') or '—', 44)} | {hold} | "
                     f"{_cell(o.get('mode'))} | {_cell(o.get('announced_on'))} | {source_links(c['own']['filings'], 2) or 'exchange registers'} |")
        A += [""]
    for group, title in (("CEO/MD", "List 2 — the chief executive changing (CEO / MD / CMD / Executive Chairman)"), ("CFO", "List 3 — the CFO changing")):
        rows = [(c, ch) for c in cos for ch in c.get("seat_changes", []) if not ch.get("dropped") and ch["group"] == group]
        rows.sort(key=lambda x: (x[1].get("when") or x[1].get("announced_on") or "", x[0]["symbol"]), reverse=True)
        A += [f"## {title}", "", f"{len(rows)} changes at {len({c['symbol'] for c, _ in rows})} companies, newest first.", "",
              "| Company | Seat | Outgoing | Incoming | Status | First said on | Sources |", "|---|---|---|---|---|---|---|"]
        for c, ch in rows:
            d, o_, i_, st = seat_line(ch)
            A.append(f"| **{c['symbol']}** — {_short(c['company'], 34)} | {_short(d, 46)} | {_short(o_, 90)} | {_short(i_, 90)} | "
                     f"{_short(st, 34)} | {_cell(ch.get('announced_on'))} | {source_links(ch.get('sources') or c['seat']['filings'], 2)} |")
        A += [""]
    return A


def render_report(record: dict) -> str:
    m = record["meta"]
    cos = record["companies"]
    changed = [c for c in cos if c.get("has_change")]
    A = ["# Management change — NiftyTotalMarket", "",
         f"*Run {m['run_date']} · window {m['window_from']} → {m['window_to']} · {m['universe']} companies · judge: {m['judge']}.*", "",
         "Two kinds of management change: the **promoters / owners** of the company changing, and the **CEO / MD or CFO** changing. "
         "Nothing here rests on a filing's headline: the text of every filing in the management, board and takeover categories was read, "
         "along with board outcomes, press releases and updates, NSE's quarterly shareholding register, its Regulation 29 takeover "
         "disclosures, bulk and block deals, and the stored conference calls. A reading model then read each candidate company's complete "
         "documents and decided; every name and quote it gave was checked against the documents.", "",
         "| | Count |", "|---|---:|",
         f"| Companies with a management change | **{len(changed)}** |",
         f"| …ownership: change of control, completed | {m['counts'].get('change_of_control', 0)} |",
         f"| …ownership: change of control, in progress | {m['counts'].get('control_change_in_progress', 0)} |",
         f"| …ownership: large stake change, same controller | {m['counts'].get('stake_change_no_control_change', 0)} |",
         f"| …ownership: within the promoter family / group | {m['counts'].get('within_promoter_family', 0)} |",
         f"| …chief executive changes (CEO / MD) | {m['counts'].get('ceo_md_changes', 0)} at {m['counts'].get('ceo_md_companies', 0)} companies |",
         f"| …CFO changes | {m['counts'].get('cfo_changes', 0)} at {m['counts'].get('cfo_companies', 0)} companies |",
         f"| Filings whose text was read | {m['filings_read']:,} |",
         f"| Companies the mechanical read put to the judge | {m['judged_seat']} for the seats, {m['judged_own']} for the ownership |",
         ""]
    A += summary_tables(record)

    # what was read and set aside
    A += ["", "## Read and set aside", "",
          "Candidates the judge read and found were not a change, by reason — the full list is in `_candidates.csv`.", "",
          "| Reason | Companies |", "|---|---:|"]
    for why, n in sorted(m.get("set_aside", {}).items(), key=lambda kv: -kv[1]):
        A.append(f"| {why} | {n} |")
    minor = [c for c in cos if not (c.get("ownership") or {}).get("keep") and (c["own"].get("shareholding") or {}).get("level") in ("major", "minor")]
    if minor:
        A += ["", "### Promoter holding moved by two points or more, not an ownership change", "",
              "| Company | Promoter holding | Change | Read as |", "|---|---|---:|---|"]
        for c in sorted(minor, key=lambda c: -abs(c["own"]["shareholding"]["change"])):
            mv = c["own"]["shareholding"]
            o = c.get("ownership") or {}
            A.append(f"| **{c['symbol']}** | {mv['base'][1]}% ({mv['base'][0]}) → {mv['latest'][1]}% ({mv['latest'][0]}) | {mv['change']:+.2f} | "
                     f"{(o.get('label') + ' — ' + _short(o.get('what_happened'), 150)) if o else 'not put to the judge (a move under five points with no other sign)'} |")
    A += ["", "---", "", "# Company by company", "",
          "Each company with a change, in five parts: (1) what is changing, with the documents' words; (2) the last three years of "
          "financials; (3) the track record of the outgoing management — the company's results while they held the seat; (4) the track "
          "record of the incoming management — the filing's profile, earlier roles, and the results of an earlier company where it is on "
          "file; (5) what was said on the calls. The call passages are in full in each company's own file under `companies/`.", ""]
    for c in sorted(changed, key=lambda c: c["symbol"]):
        A += render_company(c, verbatim=False) + ["---", ""]
    return "\n".join(A) + "\n"


def write_company_files(record: dict) -> int:
    folder = OUT_DIR / "companies"
    folder.mkdir(parents=True, exist_ok=True)
    keep = set()
    for c in record["companies"]:
        if not c.get("has_change"):
            continue
        name = f"{c['symbol'].replace('&', '_')}.md"
        keep.add(name)
        body = [f"*Run {record['meta']['run_date']} · part of [MANAGEMENT_CHANGE_REPORT.md](../MANAGEMENT_CHANGE_REPORT.md).*", ""]
        (folder / name).write_text("\n".join(body + render_company(c, verbatim=True)) + "\n")
    for p in folder.glob("*.md"):
        if p.name not in keep:
            p.unlink()
    return len(keep)


# ------------------------------------------------------------------- run

def slim(c: dict) -> dict:
    """A company's record without the bulky evidence (the hits' snippets
    stay; the text stays on disk)."""
    d = dict(c)
    for kind in ("seat", "own"):
        k = dict(d[kind])
        k["filings"] = [{x: r[x] for x in ("date", "symbol", "category", "headline", "attachment", "ann_id", "text_path", "origin", "flags")
                         } | {"hits": r.get("hits", [])[:3]} for r in k["filings"]]
        k["calls"] = k["calls"][:8]
        d[kind] = k
    return d


def count(record_cos: list[dict]) -> dict:
    n = defaultdict(int)
    for c in record_cos:
        o = c.get("ownership") or {}
        if o.get("keep"):
            n[o["verdict"]] += 1
        groups = {ch["group"] for ch in c.get("seat_changes", []) if not ch.get("dropped")}
        for ch in c.get("seat_changes", []):
            if not ch.get("dropped"):
                n["ceo_md_changes" if ch["group"] == "CEO/MD" else "cfo_changes"] += 1
        if "CEO/MD" in groups:
            n["ceo_md_companies"] += 1
        if "CFO" in groups:
            n["cfo_companies"] += 1
    return dict(n)


def set_aside(cos: list[dict]) -> dict:
    n = defaultdict(int)
    for c in cos:
        if c["seat"]["candidate"] and not any(not ch.get("dropped") for ch in c.get("seat_changes", [])):
            reasons = {re.sub(r"[:(].*", "", ch["dropped"]).strip() for ch in c.get("seat_changes", []) if ch.get("dropped")}
            n["seat — " + (sorted(reasons)[0] if reasons else ("judge not run" if not J.ok(c.get("seat_judge")) else "no change in the documents"))] += 1
        if c["own"]["candidate"] and not (c.get("ownership") or {}).get("keep"):
            o = c.get("ownership") or {}
            n["ownership — " + (o.get("label") or "judge not run")] += 1
    return dict(n)


def candidate_rows(cos: list[dict]) -> list[dict]:
    out = []
    for c in cos:
        if not (c["seat"]["candidate"] or c["own"]["candidate"]):
            continue
        seat = [ch for ch in c.get("seat_changes", [])]
        o = c.get("ownership") or {}
        out.append({"symbol": c["symbol"], "company": c["company"],
                    "seat_candidate": c["seat"]["candidate"], "seat_why": "; ".join(c["seat"]["why"]),
                    "seat_filings": len(c["seat"]["filings"]),
                    "seat_kept": sum(1 for ch in seat if not ch.get("dropped")),
                    "seat_dropped": "; ".join(sorted({f"{ch['seat']}: {ch['dropped']}" for ch in seat if ch.get("dropped")}))[:400],
                    "seat_judge": (c.get("seat_judge") or {}).get("status", ""),
                    "seat_read": _short((c.get("seat_judge") or {}).get("read"), 200),
                    "own_candidate": c["own"]["candidate"], "own_why": "; ".join(c["own"]["why"]),
                    "own_verdict": o.get("verdict", ""), "own_what": _short(o.get("what_happened"), 240),
                    "own_judge": (c.get("own_judge") or {}).get("status", "")})
    return out


def seat_rows(cos: list[dict]) -> list[dict]:
    out = []
    for c in cos:
        for ch in c.get("seat_changes", []):
            if ch.get("dropped"):
                continue
            o, i = ch["outgoing"], ch["incoming"]
            out.append({"symbol": c["symbol"], "company": c["company"], "group": ch["group"], "seat": ch["seat"],
                        "designation": ch.get("designation", ""), "outgoing": o.get("name", ""), "outgoing_reason": _clean(o.get("reason")),
                        "outgoing_last_day": _clean(o.get("last_day")), "outgoing_in_seat_since": _clean(o.get("in_seat_since")),
                        "incoming": i.get("name", ""), "incoming_effective": _clean(i.get("effective")),
                        "incoming_from": _clean(i.get("from_where")), "interim": bool(i.get("interim")),
                        "status": ch.get("status", ""), "announced_on": ch.get("announced_on", ""), "verified": ch.get("verified"),
                        "quote": ch.get("quote", "")})
    return out


def own_rows(cos: list[dict]) -> list[dict]:
    out = []
    for c in cos:
        o = c.get("ownership") or {}
        if not o:
            continue
        mv = c["own"].get("shareholding") or {}
        out.append({"symbol": c["symbol"], "company": c["company"], "verdict": o["verdict"], "kept": o["keep"],
                    "what_happened": o["what_happened"], "outgoing_owner": o["outgoing_owner"].get("name", ""),
                    "incoming_owner": o["incoming_owner"].get("name", ""), "mode": o.get("mode", ""),
                    "promoter_base": mv.get("base", ["", ""])[1] if mv.get("base") else "", "promoter_latest": mv.get("latest", ["", ""])[1] if mv.get("latest") else "",
                    "control_changes": o.get("control_changes"), "announced_on": o.get("announced_on", ""), "verified": o.get("verified"),
                    "quote": o.get("quote", "")})
    return out


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as fh:
        if not rows:
            fh.write("symbol\n")
            return
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def finish(record: dict) -> str:
    cos = record["companies"]
    for c in cos:
        c["has_change"] = bool((c.get("ownership") or {}).get("keep") or any(not ch.get("dropped") for ch in c.get("seat_changes", [])))
    record["meta"]["counts"] = count(cos)
    record["meta"]["set_aside"] = set_aside(cos)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LATEST.write_text(json.dumps(record, indent=1, default=str, ensure_ascii=False))
    md = render_report(record)
    REPORT.write_text(md)
    write_company_files(record)
    write_csv(CHANGES_CSV, seat_rows(cos))
    write_csv(OWNERSHIP_CSV, own_rows(cos))
    write_csv(CANDIDATES_CSV, candidate_rows(cos))
    return md


def cmd_run(args, runner=None) -> dict:
    today = dt.date.fromisoformat(args.as_of) if getattr(args, "as_of", None) else dt.date.today()
    days = args.days
    start, end = M.window(today, days)
    if getattr(args, "out", None):
        set_out_dir(Path(args.out))
    only = {s.strip().upper() for s in (args.only or "").split(",") if s.strip()} or None
    ai = not args.quick
    cands = build_candidates(today, days, only, workers=max(2, min(8, args.workers)))
    members = M.FA.universe()
    seat_c = [c for c in cands.values() if c["seat"]["candidate"]]
    own_c = [c for c in cands.values() if c["own"]["candidate"]]
    log(f"[candidates] {len(seat_c)} companies for the seats, {len(own_c)} for the ownership (of {len(cands)})")
    jobs = [("seat", c) for c in seat_c] + [("own", c) for c in own_c]

    def one(job):
        kind, c = job
        if kind == "seat":
            c["seat_judge"] = judge_seat(c, start, end, ai, runner)
            c["seat_changes"] = settle_seat(c, c["seat_judge"], start, end)
        else:
            c["own_judge"] = judge_own(c, start, end, ai, runner)
            c["ownership"] = settle_own(c, c["own_judge"])
        return kind, c["symbol"], (c.get("seat_judge") if kind == "seat" else c.get("own_judge") or {}).get("status", "")
    done = 0
    with cf.ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        for kind, sym, status in ex.map(one, jobs):
            done += 1
            if status.startswith("judge failed"):
                log(f"  {sym} {kind}: {status}")
            if done % 25 == 0:
                log(f"[judge] {done}/{len(jobs)}")
    actions = corporate_actions(today, days)
    cos = list(cands.values())
    for c in cos:
        if (c.get("ownership") or {}).get("keep") or any(not ch.get("dropped") for ch in c.get("seat_changes", [])):
            enrich(c, today, members, actions)
    n_read = sum(1 for r in M.load_filings(today, days) if not only or r["symbol"] in only)
    meta = {"run_date": today.isoformat(), "window_from": start, "window_to": end, "universe": len(cands),
            "filings_read": n_read, "judged_seat": len(seat_c), "judged_own": len(own_c),
            "judge": (f"{J.MODEL} read each candidate company's complete documents" if ai else "not run (--quick): mechanical read only")}
    record = {"meta": meta, "companies": [slim(c) for c in cos]}
    md = finish(record)
    k = record["meta"]["counts"]
    print(f"wrote {REPORT} ({len(md.splitlines())} lines); {sum(1 for c in record['companies'] if c['has_change'])} companies with a change; "
          f"{k.get('change_of_control', 0)} control changes, {k.get('control_change_in_progress', 0)} in progress, "
          f"{k.get('ceo_md_changes', 0)} CEO/MD changes, {k.get('cfo_changes', 0)} CFO changes")
    return record


def cmd_render(args) -> None:
    if getattr(args, "out", None):
        set_out_dir(Path(args.out))
    record = json.loads(LATEST.read_text())
    md = finish(record)
    print(f"re-rendered {REPORT} ({len(md.splitlines())} lines) from the run of {record['meta']['run_date']}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--days", type=int, default=M.WINDOW_DAYS)
    r.add_argument("--as-of", dest="as_of", default=None)
    r.add_argument("--only", default="")
    r.add_argument("--quick", action="store_true", help="no judge: the mechanical candidates only")
    r.add_argument("--workers", type=int, default=6)
    r.add_argument("--out", default=None)
    x = sub.add_parser("render")
    x.add_argument("--out", default=None)
    args = ap.parse_args()
    {"run": cmd_run, "render": cmd_render}[args.cmd](args)


if __name__ == "__main__":
    main()
