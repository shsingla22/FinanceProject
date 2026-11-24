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
import concurrent.futures as cf
import shutil
import subprocess
import sys
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import spinoff as SO                       # noqa: E402
import financials as FN                    # noqa: E402
import fetch_announcements as FA           # noqa: E402  (via spinoff's path)
import deal as DL                          # noqa: E402

INDIA = HERE.parent.parent.parent
OUT_DIR = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "SpinOffAnalysis"
REPORT = OUT_DIR / "SPINOFF_REPORT.md"
LATEST = OUT_DIR / "spinoff_latest.json"
SITUATIONS = OUT_DIR / "_situations.csv"
MENTIONS = OUT_DIR / "_concall_mentions.csv"
COVERAGE = OUT_DIR / "_coverage.csv"
OFFERINGS = OUT_DIR / "_offerings.csv"
HISTORY = OUT_DIR / "history"
CACHE = HERE.parent / ".judge_cache.json"


def set_out_dir(path: Path) -> None:
    """Write this run's outputs under `path` instead of the production
    folder (a backtest keeps its own folder)."""
    global OUT_DIR, REPORT, LATEST, SITUATIONS, MENTIONS, COVERAGE, OFFERINGS, HISTORY
    OUT_DIR = Path(path)
    REPORT = OUT_DIR / "SPINOFF_REPORT.md"
    LATEST = OUT_DIR / "spinoff_latest.json"
    SITUATIONS = OUT_DIR / "_situations.csv"
    MENTIONS = OUT_DIR / "_concall_mentions.csv"
    COVERAGE = OUT_DIR / "_coverage.csv"
    OFFERINGS = OUT_DIR / "_offerings.csv"
    HISTORY = OUT_DIR / "history"
MODEL = os.environ.get("SPINOFF_JUDGE_MODEL",
                       os.environ.get("ANALYST_MODEL", "claude-opus-5"))
JUDGE_CHARS = 45_000          # offerings: one filing is enough
SEGMENT_CHARS = 115_000       # segment pages are tables; they must arrive whole
# the demerger reads get the COMPLETE documents: every filing's full text and
# every call section in the window, whole — snippets lose the reasoning.
# Budgets keep the prompt inside the model's context; when a company's
# record is larger, the newest documents and calls are kept whole and the
# oldest dropped, and the prompt says how many were dropped.
FILINGS_CHARS = 320_000
CALLS_CHARS = 360_000
PROMPT_VERSION = "v2"
LISTING_PROMPT_VERSION = "listing-v2"      # the subsidiary-listing resolution question
RESOLUTION_PROMPT_VERSION = "resolution-v1"  # the probable / indicated demerger resolution question
DEAL_PROMPT_VERSION = "deal-v3"              # the deal sheet: every entity, size, swap, holdings, incentives, dates
SEGMENT_PROMPT_VERSION = "segments-v3"       # one table per separated business, with segment assets and liabilities


# ------------------------------------------------------------- the judge

def _ai_available() -> bool:
    return shutil.which("claude") is not None


_CACHE_LOCK = threading.Lock()     # several judge calls run at once; one writer


def _cache() -> dict:
    if CACHE.exists():
        try:
            return json.loads(CACHE.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def _parse_json(out: str) -> dict | None:
    """The first complete JSON object in the judge's answer, tolerant of
    code fences, prose around it and trailing commas; None when there is
    none."""
    text = re.sub(r"```(?:json)?", "", out or "")
    dec = json.JSONDecoder()
    for m in re.finditer(r"\{", text):
        chunk = text[m.start():]
        try:
            obj, _ = dec.raw_decode(chunk)
        except json.JSONDecodeError:
            try:                                           # trailing commas
                obj, _ = dec.raw_decode(re.sub(r",\s*([}\]])", r"\1", chunk))
            except json.JSONDecodeError:
                continue
        if isinstance(obj, dict) and obj:
            return obj
    return None


def _ask(key: str, stamp: str, prompt: str, allow_ai: bool, runner=None) -> dict:
    """One cached, strict-JSON question to the judge; a malformed answer
    is asked once more."""
    cache = _cache()
    hit = cache.get(key) or {}
    # several readings of one key may be live at once (a backtest's as-of
    # window beside today's): the cache keeps the last few stamps per key
    stamps = hit.get("stamps") or ({hit["stamp"]: hit["verdict"]} if hit.get("stamp") else {})
    if stamp in stamps:
        return {"status": "cached", **stamps[stamp]}
    if not allow_ai or (runner is None and not _ai_available()):
        return {"status": "not assessed", "note": "judge not run — mechanical read only"}
    verdict, failure = None, "unparseable"
    for attempt in range(2):
        ask = prompt if attempt == 0 else (
            prompt + "\n\nYour previous answer was not valid JSON. Reply with ONE JSON "
                     "object only — no prose before or after it, no code fence, every "
                     "string value properly escaped.")
        try:
            if runner is not None:
                out = runner(ask)
            else:
                proc = subprocess.run(["claude", "-p", "--model", MODEL], input=ask,
                                      capture_output=True, text=True, timeout=900)
                if proc.returncode != 0:
                    return {"status": f"judge failed: {(proc.stderr or '')[-120:]}"}
                out = proc.stdout
        except Exception as e:                             # noqa: BLE001
            return {"status": f"judge failed: {e}"}
        verdict = _parse_json(out)
        if verdict is not None:
            break
        failure = "bad json" if "{" in (out or "") else "unparseable"
    if verdict is None:
        return {"status": f"judge failed: {failure}"}
    with _CACHE_LOCK:
        cache = _cache()
        old = cache.get(key) or {}
        kept = old.get("stamps") or ({old["stamp"]: old["verdict"]} if old.get("stamp") else {})
        kept = dict(list(kept.items())[-3:])             # at most four readings per key
        kept[stamp] = verdict
        cache[key] = {"stamps": kept}
        tmp = CACHE.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(cache, indent=1))
        tmp.replace(CACHE)
    return {"status": "judged", **verdict}


def judge_prompt(sit: dict, scheme_text: str, calls_text: str) -> str:
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
        f"THE COMPANY'S FILINGS, COMPLETE (newest first):\n{scheme_text}\n\n"
        f"THE COMPANY'S EARNINGS CALLS, COMPLETE (last 12 months, newest first):\n"
        f"{calls_text or '(no transcripts on file)'}"
    )


def judge(sit: dict, scheme_text: str, calls_text: str,
          allow_ai: bool = True, runner=None) -> dict:
    stamp = hashlib.md5((scheme_text + calls_text + MODEL + PROMPT_VERSION).encode()).hexdigest()
    if len(scheme_text) < 500 and len(calls_text) < 500:
        return {"status": "no documents", "note": "nothing on file to read"}
    return _ask(sit["symbol"], stamp, judge_prompt(sit, scheme_text, calls_text), allow_ai, runner)


def rationale_prompt(sit: dict, calls_text: str, scheme_text: str) -> str:
    return (
        f"You are reconstructing WHY {sit['company']} ({sit['symbol']}) is separating a "
        f"business, for a special-situation investor. Below are the COMPLETE transcripts "
        f"of three years of the company's earnings calls (each headed by its call and "
        f"transcript link) and the company's filings in full. Answer STRICT JSON only, "
        f"from these texts alone — never from memory. Be specific and detailed: name the "
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
        f"THE EARNINGS CALLS, COMPLETE (last 36 months, newest first):\n{calls_text or '(no transcripts on file)'}\n\n"
        f"THE FILINGS, COMPLETE (newest first):\n{scheme_text}"
    )


def judge_rationale(sit: dict, calls_text: str, scheme_text: str,
                    allow_ai: bool = True, runner=None) -> dict:
    if len(calls_text) < 500 and len(scheme_text) < 500:
        return {"status": "no documents", "note": "no transcripts or filing text on file"}
    stamp = hashlib.md5((calls_text + scheme_text + MODEL + PROMPT_VERSION).encode()).hexdigest()
    return _ask(f"{sit['symbol']}::rationale", stamp,
                rationale_prompt(sit, calls_text, scheme_text), allow_ai, runner)


def segments_prompt(sit: dict, excerpts: list[dict], names: list[str]) -> str:
    body = "\n\n".join(f"[{e['doc']} — page {e['page']}] {e['text']}" for e in excerpts)
    return (
        f"You are extracting the OWN financials of EACH business {sit['company']} "
        f"({sit['symbol']}) is separating — the entities and businesses are known in the documents as: "
        f"{'; '.join(names)}. There may be SEVERAL separated businesses; give one entry for each that the "
        f"pages carry numbers for. Below are pages from the company's annual reports (segment reporting) and "
        f"quarterly presentations, each tagged with document and page. Answer STRICT JSON "
        f"only. Take every number from the tagged pages — never estimate, never recall. "
        f"Report fiscal-year figures (FY2024 = year ended March 2024, etc.); if only "
        f"quarterly or half-year numbers exist, say so in notes and leave the year null. "
        f"Keep the unit the document uses, and give ONE unit per business — the unit of its annual figures. "
        f"Give the SEPARATED businesses first and in full; look in the OLDER annual reports too, where a business "
        f"that has since left was still a reported segment. Add the segments that REMAIN with the parent after them.\n"
        '{"businesses": [{"side": "separated" (the business leaves the company — it goes to a resulting company or is the '
        'subsidiary being listed) | "remaining" (it stays with the parent), '
        '"entity": "<for a separated business: which of the named entities it goes to, as named above; for a remaining one: the parent>", '
        '"segment_name": "<the segment / business as the documents label it>", '
        '"unit": "<₹ crore | ₹ million | ₹ lakh | as in the document>", '
        '"measure_notes": "<what the profit line is: segment result / EBIT / EBITDA / PBT; '
        'whether revenue is external or includes inter-segment>", '
        '"years": [{"fy": "FY2024", "revenue": <number or null>, '
        '"operating_profit": <number or null>, "pat": <number or null>, '
        '"segment_assets": <number or null>, "segment_liabilities": <number or null>, '
        '"capex": <number or null>, "depreciation": <number or null>, '
        '"source": "<document — page N>"}, '
        '{"fy": "FY2025", ...}, {"fy": "FY2026", ...}], '
        '"latest_quarter": {"period": "<e.g. Q1 FY27 or null>", "revenue": <number or null>, '
        '"operating_profit": <number or null>, "source": "<document — page N>"}, '
        '"not_found": "<which figures the pages do not carry for this business, <=40 words>"}], '
        '"not_found": "<businesses named above for which the pages carry no numbers at all, <=40 words>"}\n\n'
        f"PAGES:\n{body[:SEGMENT_CHARS]}"
    )


def judge_segments(sit: dict, excerpts: list[dict], names: list[str],
                   allow_ai: bool = True, runner=None) -> dict:
    if not excerpts:
        return {"status": "no documents", "note": "no segment pages found in the stored reports"}
    stamp = hashlib.md5((json.dumps(excerpts)[:SEGMENT_CHARS] + "|".join(names)
                         + MODEL + PROMPT_VERSION + SEGMENT_PROMPT_VERSION).encode()).hexdigest()
    return _ask(f"{sit['symbol']}::segments", stamp,
                segments_prompt(sit, excerpts, names), allow_ai, runner)


def deal_prompt(sit: dict, scheme_text: str, calls_text: str, arrivals: list[dict] | None = None) -> str:
    kind = ("a subsidiary's IPO / listing (a partial spin-off)" if sit["kind"] == "subsidiary_listing"
            else "a demerger / spin-off")
    hint = ""
    if arrivals:
        rd = sit["facts"].get("record_date", "")
        hint = (f"NSE'S EQUITY LIST (the exchange's own record) shows these companies began trading after this "
                f"company's demerger record date of {rd}: "
                + "; ".join(f"{a['name']} ({a['symbol']}, listed {a['listed_on']})" for a in arrivals)
                + ". Include EACH of them in `entities`: with role \"resulting\" and its nse_symbol when the documents "
                  "show the scheme created or separated it (a resulting company is often renamed before it lists), "
                  "else with role \"unrelated\".\n")
    return (
        f"You are preparing the DEAL SHEET for {kind} at {sit['company']} ({sit['symbol']}), for an investor "
        f"following Greenblatt's spin-off checklist. Read the complete documents below. Answer STRICT JSON only; "
        f"every field from the documents — never from memory, never estimated; write \"not stated\" when they "
        f"do not say; quotes must be verbatim.\n"
        f"A company can have MORE THAN ONE scheme or transaction on file — an earlier demerger already completed and "
        f"a newer one in progress, or one scheme that separates several businesses into several companies. The "
        f"documents span the whole period; cover EVERY scheme and EVERY entity in them, not only the newest.\n"
        f"{hint}"
        '{"entities": [{"name": "<CURRENT full legal name of EACH resulting company, each subsidiary being listed, '
        'the parent itself, and every other party to the scheme — ALL of them, one entry each; the name only: no '
        'bracketed abbreviations, no \'formerly\', no CIN, no role>", '
        '"former_names": ["<any earlier name of this entity in the documents>"], '
        '"role": "resulting" | "listed_subsidiary" | "parent" | "former_parent" | "merged_in" | "unrelated" | "other" '
        '— resulting = receives a separated business and its shares go to the parent\'s shareholders; '
        'listed_subsidiary = a subsidiary / associate / JV listed by IPO in the period of these documents, or being '
        'listed — NOT one that has been listed for years (that is \"other\"); parent = this company '
        'itself, what remains; former_parent = the company THIS company was spun out of; merged_in = amalgamated '
        'into another entity and dissolved, or a transfer inside the group with no shares to the parent\'s holders, '
        '"scheme": "<which scheme or transaction this entity belongs to, with its year, e.g. \'2023 demerger into five companies\'>", '
        '"status": "<listed | effective, awaiting listing | in progress | withdrawn / dropped | not stated>", '
        '"nse_symbol": "<its NSE symbol when the documents or the exchange list above give it, else empty>", '
        '"business": "<what goes into it, <=30 words>", '
        '"swap_ratio": "<shares of this entity for shares of the parent, in the documents\' words; for an IPO the '
        'offer structure (fresh issue / offer for sale, size); or not stated>", '
        '"listing": "<listed on <date> | to be listed | not to be listed | not stated>", '
        '"turnover": "<turnover / revenue of this undertaking with its year and unit, as stated; or not stated>", '
        '"turnover_pct_of_parent": "<its share of the listed company\'s total turnover, as stated, e.g. 23.4%; or not stated>", '
        '"net_worth_or_assets": "<net worth / assets of this undertaking and its share of the parent\'s, as stated; or not stated>", '
        '"who_runs_it": "<the named CEO / MD / chair of this entity, or not stated>", '
        '"quote": "<one verbatim sentence about this entity>"}], '
        '"size_statement": "<the documents\' own statement of how large the separated business(es) are beside the '
        'company — verbatim, with the numbers; or not stated>", '
        '"promoter_holding_parent": "<promoter and promoter group holding in the parent, % with its date; or not stated>", '
        '"promoter_holding_after": "<what the promoters will hold in each resulting / listed entity — e.g. mirror '
        'shareholding, or the % after the IPO; verbatim; for EVERY scheme; or not stated>", '
        '"public_shareholders_get": "<what a public shareholder of the parent receives under EACH scheme, in the documents\' words; or not stated>", '
        '"management_incentives": "<stock options / RSUs / SARs: how existing grants are treated in the scheme, any '
        'new plan in the new entity, exercise price or pricing date, management or insider shareholding; verbatim; or not stated>", '
        '"insider_actions": "<any promoter or management buying, selling, pledging or stated intent around the '
        'separation; or not stated>", '
        '"dates": [{"event": "<ONLY events of THIS separation, not of earlier schemes or unrelated record dates: board approval | filed with exchanges | exchange no-objection | SEBI approval | '
        'shareholders / creditors meeting | NCLT order | appointed date | effective date | record date | allotment | '
        'listing and trading | DRHP filed | SEBI observations | IPO opened | other>", '
        '"date": "<YYYY-MM-DD, or YYYY-MM when only the month is given>", "entity": "<which entity, when it differs>", '
        '"source": "<the filing or call that gives it, with its date>"}], '
        '"other_differences": [{"metric": "<working capital | operating margin | growth | debt and leverage | cash | '
        'capex and capital intensity | return on capital | tax | other>", '
        '"parent_or_remaining": "<what the documents say about the parent / remaining business>", '
        '"separated_business": "<what they say about the separated business>", '
        '"quote": "<verbatim sentence with the numbers>"}]}\n\n'
        f"THE COMPANY'S FILINGS ABOUT ITS SEPARATIONS, THE WHOLE PERIOD ON FILE (newest first):\n{scheme_text}\n\n"
        f"THE COMPANY'S EARNINGS CALLS, COMPLETE (last 12 months, newest first):\n"
        f"{calls_text or '(no transcripts on file)'}"
    )


def judge_deal(sit: dict, scheme_text: str, calls_text: str, allow_ai: bool = True, runner=None,
               arrivals: list[dict] | None = None) -> dict:
    """The deal sheet: EVERY resulting or listed entity (Quess: Digitide and
    Bluspring; Vedanta: each of its demerged companies), the size of each
    beside the parent, the share swap, promoter holding, management
    incentives, every dated event, and the documents' own statements of
    how the businesses differ."""
    if len(scheme_text) < 300 and len(calls_text) < 300:
        return {"status": "no documents", "note": "nothing on file to read"}
    hint = json.dumps(arrivals or [], sort_keys=True)
    stamp = hashlib.md5((scheme_text + calls_text + hint + MODEL + PROMPT_VERSION + DEAL_PROMPT_VERSION).encode()).hexdigest()
    return _ask(f"{sit['symbol']}::deal", stamp, deal_prompt(sit, scheme_text, calls_text, arrivals), allow_ai, runner)


def offering_prompt(sit: dict, text: str) -> str:
    return (
        f"You are reading the filings of {sit['company']} ({sit['symbol']}) about a "
        f"{sit['family']} for an investor who wants to know WHO IS BUYING. Facts the "
        f"pattern read: {json.dumps(sit['facts'])[:600]}. Answer STRICT JSON only, from the "
        f"filing text below — never from memory; \"not stated\" when it does not say:\n"
        '{"instrument": "warrants"|"equity shares"|"rights equity shares"|"CCPS"|"other", '
        '"securities": "<number of securities, as written>", "issue_price": "<per security, ₹>", '
        '"total_amount": "<aggregate, as written>", "pricing_basis": "<SEBI ICDR floor / discount or premium to market, if stated>", '
        '"allottees": [{"name": "<person or entity>", "category": "promoter"|"promoter group"|"non-promoter"|"institution"|"public", '
        '"securities": "<count or not stated>", "amount": "<₹ or not stated>"}], '
        '"promoter_share_of_issue": "<% of the issue going to promoters, or not stated>", '
        '"promoter_intent": "<for rights: whether promoters will subscribe fully / renounce / oversubscribe, in their words>", '
        '"upfront_paid": "<for warrants: % paid upfront, tenure to convert>", '
        '"purpose": "<stated use of proceeds, <=30 words>", '
        '"stage": "board approved"|"shareholders approved"|"in-principle approval"|"allotted"|"converted"|"completed"|"not stated", '
        '"quote": "<one verbatim sentence naming the buyers>"}\n\n'
        f"FILING TEXT (truncated):\n{text[:JUDGE_CHARS]}"
    )


def judge_offering(sit: dict, text: str, allow_ai: bool = True, runner=None) -> dict:
    if len(text) < 300:
        return {"status": "no documents", "note": "no filing text on file"}
    stamp = hashlib.md5((text[:JUDGE_CHARS] + MODEL + PROMPT_VERSION).encode()).hexdigest()
    return _ask(f"{sit['symbol']}::offering::{sit['kind']}", stamp, offering_prompt(sit, text), allow_ai, runner)


def segment_table(seg: dict) -> dict:
    """Growth and margins computed from the judge's extracted numbers;
    nothing is filled in."""
    years = [y for y in (seg.get("years") or []) if isinstance(y, dict)]
    if not years:
        return {"available": False}
    labels = [str(y.get("fy") or "n/a") for y in years]     # a year the judge left unlabelled still renders
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
    assets, liabs, capex = col("segment_assets"), col("segment_liabilities"), col("capex")
    if any(v is not None for v in assets + liabs + capex):
        ce = [(a - l) if a is not None and l is not None else None for a, l in zip(assets, liabs)]
        rows += [
            {"metric": f"Segment assets ({seg.get('unit', '')})", "values": assets},
            {"metric": f"Segment liabilities ({seg.get('unit', '')})", "values": liabs},
            {"metric": f"Capital employed ({seg.get('unit', '')})", "values": ce},
            {"metric": "Return on capital employed (%)", "values": [FN._margin(o, c) if c and c > 0 else None for o, c in zip(op, ce)]},
            {"metric": "Segment assets / revenue (x)", "values": [round(a / r, 2) if a is not None and r else None for a, r in zip(assets, rev)]},
            {"metric": f"Capex ({seg.get('unit', '')})", "values": capex},
        ]
    found = sum(1 for v in rev + op + pat if v is not None)
    return {"available": found > 0, "years": labels, "rows": rows,
            "sources": [y.get("source", "") for y in years], "found_numbers": found}


def segment_tables(seg: dict) -> list[dict]:
    """One table per separated business the judge found numbers for (an
    older single-business answer is read as one). Each carries the entity
    it belongs to, the segment's name, the unit and its ₹-crore factor."""
    if seg.get("status") not in ("judged", "cached"):
        return []
    items = [b for b in (seg.get("businesses") or []) if isinstance(b, dict)]
    if not items and seg.get("years"):
        items = [seg]
    out = []
    for b in items:
        st = segment_table(b)
        st.update({"side": "remaining" if str(b.get("side") or "").lower().startswith("remain") else "separated",
                   "entity": str(b.get("entity") or ""), "segment_name": str(b.get("segment_name") or ""),
                   "unit": str(b.get("unit") or ""), "unit_factor": DL.unit_factor(str(b.get("unit") or "")),
                   "measure_notes": str(b.get("measure_notes") or ""), "not_found": str(b.get("not_found") or ""),
                   "latest_quarter": b.get("latest_quarter") if isinstance(b.get("latest_quarter"), dict) else {}})
        out.append(st)
    return out


def scheme_text_for(sit: dict, rows: list[dict], budget: int = FILINGS_CHARS) -> str:
    """EVERY filing of the situation's company, full text, newest first,
    each headed by its date and headline — whole documents, not excerpts.
    Over budget, the oldest are dropped and the header says so."""
    mine = sorted((r for r in rows if r["symbol"] == sit["symbol"] and r.get("source") != "CALLS"),
                  key=lambda r: r["date"], reverse=True)
    docs, used, dropped = [], 0, 0
    for r in mine:
        t = SO.load_text(r) or SO.load_first_pages(r)
        if not t:
            continue
        head = f"### FILING {r['date']} · {r['category']} · {r['headline'][:160]}\n"
        if used + len(t) + len(head) > budget and docs:
            dropped += 1
            continue
        docs.append(head + t)
        used += len(t) + len(head)
    note = (f"[{len(docs)} filings in full; {dropped} older filings omitted for length]\n\n"
            if dropped else f"[{len(docs)} filings in full]\n\n")
    return note + "\n\n".join(docs)


def calls_text_for(symbol: str, months: int, today: dt.date, budget: int = CALLS_CHARS) -> str:
    """The COMPLETE transcripts of the last `months` of calls, newest first,
    each headed by its label and link — not snippets. Over budget, the
    oldest calls are dropped whole and the header says so."""
    text = SO.concall_text(symbol)
    if not text:
        return ""
    links = FN.doc_links(symbol)["calls"]
    cutoff = dt.date(today.year, today.month, 1) - dt.timedelta(days=months * 31)
    secs = []
    for label, body in SO.concall_sections(text):
        d = SO._label_date(label)
        if d and cutoff <= d <= today:                  # as-of: no later calls
            secs.append((d, label.replace("Call: ", ""), body))
    secs.sort(key=lambda x: x[0], reverse=True)
    out, used, dropped = [], 0, 0
    for d, lab, body in secs:
        head = f"### CALL {lab}" + (f" · {links[lab]}" if links.get(lab) else "") + "\n"
        if used + len(body) > budget and out:
            dropped += 1
            continue
        out.append(head + body.strip())
        used += len(body)
    note = (f"[{len(out)} calls in full; {dropped} older calls omitted for length]\n\n"
            if dropped else f"[{len(out)} calls in full]\n\n")
    return note + "\n\n".join(out) if out else ""


def listing_prompt(sit: dict, scheme_text: str, calls_text: str) -> str:
    return (
        f"The filings of {sit['company']} ({sit['symbol']}) were flagged as a possible LISTING OF A "
        f"SUBSIDIARY (an IPO / DRHP / listing of a subsidiary, associate or joint venture in which "
        f"the company holds a significant stake). Read the complete documents below and decide what "
        f"is really there. Answer STRICT JSON only, every field from the documents — never from "
        f"memory; write \"not stated\" when they do not say:\n"
        '{"what_it_is": one of '
        '"subsidiary_ipo_announced" (a subsidiary / associate / JV of THIS company is to be listed by IPO or '
        'offer for sale and is not listed yet: board approval, DRHP, SEBI observations, offer open), '
        '"subsidiary_already_listed" (such an entity completed its IPO in the period these documents cover and '
        'now trades; if the offer is open or allotment is pending and trading has not begun, answer '
        'subsidiary_ipo_announced with ipo_stage "offer open"), '
        '"listed_entity_acquired_or_long_listed" (the listed entity was ACQUIRED by this company already listed, '
        'or has been listed for years — no IPO of it in the period), '
        '"subsidiary_ipo_withdrawn" (the IPO was withdrawn or shelved), '
        '"stake_sale_in_other_ipo" (the company only sells shares it holds, as a minority financial investor, '
        'in some OTHER company\'s IPO — e.g. a bank selling its stake in an exchange), '
        '"sale_or_transfer" (a sale, slump sale, stake purchase or transfer of a business or subsidiary; nothing is listed), '
        '"merger" (a merger / amalgamation; nothing new is listed), '
        '"own_ipo" (the listing discussed is this company\'s OWN recent IPO), '
        '"no_event" (none of these: ESOP notices, policies, results that merely mention a subsidiary), '
        '"subsidiary": "<the full legal name of the entity being listed, with no bracketed abbreviation or '
        'former name; when several, the main one; or not stated>", '
        '"other_subsidiaries": ["<any further entities being listed>"], '
        '"relation": "subsidiary"|"associate"|"joint venture"|"not stated", '
        '"parent_stake_before": "<the company\'s holding before the IPO, e.g. 94.5%, or not stated>", '
        '"parent_stake_after": "<its holding after, or not stated>", '
        '"ipo_stage": "board approval"|"DRHP filed"|"SEBI observations"|"offer open"|"listed"|"not stated", '
        '"listing_date": "<YYYY-MM-DD when the entity listed, or not stated>", '
        '"exchange": "<where it lists or listed, or not stated>", '
        '"timeline": "<when the listing is expected, in the documents\' words with their date; or not stated>", '
        '"quote": "<one verbatim sentence from the documents that settles your answer>"}\n\n'
        f"THE COMPANY'S FILINGS, COMPLETE (newest first):\n{scheme_text}\n\n"
        f"THE COMPANY'S EARNINGS CALLS, COMPLETE (last 12 months, newest first):\n"
        f"{calls_text or '(no transcripts on file)'}"
    )


def judge_listing(sit: dict, scheme_text: str, calls_text: str,
                  allow_ai: bool = True, runner=None) -> dict:
    """One pointed, forced-choice question for a subsidiary-listing
    situation: is it a partial spin-off (announced or already listed), or
    something else that only looked like one?"""
    if len(scheme_text) < 300 and len(calls_text) < 300:
        return {"status": "no documents", "note": "nothing on file to read"}
    stamp = hashlib.md5((scheme_text + calls_text + MODEL + PROMPT_VERSION + LISTING_PROMPT_VERSION).encode()).hexdigest()
    return _ask(f"{sit['symbol']}::listing", stamp, listing_prompt(sit, scheme_text, calls_text), allow_ai, runner)


def resolution_prompt(sit: dict, scheme_text: str, calls_text: str) -> str:
    return (
        f"The filings and calls of {sit['company']} ({sit['symbol']}) mention a DEMERGER, spin-off, carve-out or "
        f"scheme of arrangement, but no filing settles what it is. Read the complete documents below and decide. "
        f"Answer STRICT JSON only, every field from the documents — never from memory; write \"not stated\" "
        f"when they do not say:\n"
        '{"what_it_is": one of '
        '"demerger_in_progress" (a business of THIS company is being demerged / spun off under a scheme its board '
        'has approved or that is further along, THIS company is the demerged company, its shareholders are to '
        'receive shares of a resulting company, and the scheme is not yet complete), '
        '"demerger_completed" (a demerger of THIS company — as the demerged company, or as the resulting company '
        'that was spun out — is already effective; however long ago), '
        '"other_companys_demerger" (the demerger discussed is the parent\'s, a subsidiary\'s, a group company\'s or '
        'an unrelated company\'s; or THIS company only RECEIVES a business), '
        '"internal_reorganisation" (a business moved to a wholly-owned subsidiary, a slump sale, a business transfer, '
        'a new line of business — nothing is listed for the shareholders), '
        '"merger_or_acquisition" (an amalgamation, merger or acquisition; nothing is separated), '
        '"subsidiary_ipo" (a subsidiary, associate or JV is being or has been listed by IPO), '
        '"management_indication" (MANAGEMENT ITSELF — in a filing, or answering on a call — has said it is planning '
        'or evaluating a demerger of this company\'s business, and no scheme is approved; an analyst merely asking '
        'does not count), '
        '"withdrawn" (a proposed demerger was withdrawn or called off), '
        '"news_report_only" (press speculation the company did not confirm), '
        '"no_event" (none of these: an analyst\'s question with no commitment, covenant or ESOP boilerplate, the word '
        '\"carve-out\" or \"demerger\" used in another sense), '
        '"business": "<the business demerged or to be demerged, <=25 words, or not stated>", '
        '"role": "demerged company"|"resulting company"|"not stated", '
        '"resulting_company": "<full legal name of the resulting company; or, when THIS company is the resulting '
        'company, the name of the company it was demerged from; or not stated>", '
        '"stage": "board approval"|"exchange NOC"|"shareholder meeting"|"NCLT sanction"|"effective"|"not stated", '
        '"completed_date": "<when the demerger became effective or the resulting company listed: YYYY-MM-DD, '
        'YYYY-MM, YYYY or a fiscal year, as the documents give it; or not stated>", '
        '"listing_sought": "yes"|"no"|"not stated", '
        '"timeline": "<when completion or listing is expected, in the documents\' words with their date; or not stated>", '
        '"quote": "<one verbatim sentence from the documents that settles your answer>"}\n\n'
        f"THE COMPANY'S FILINGS, COMPLETE (newest first):\n{scheme_text}\n\n"
        f"THE COMPANY'S EARNINGS CALLS, COMPLETE (last 12 months, newest first):\n"
        f"{calls_text or '(no transcripts on file)'}"
    )


def judge_resolution(sit: dict, scheme_text: str, calls_text: str,
                     allow_ai: bool = True, runner=None) -> dict:
    """One forced-choice question for a probable or indicated demerger /
    scheme row: in progress, completed (and when), or something that only
    looked like one."""
    if len(scheme_text) < 300 and len(calls_text) < 300:
        return {"status": "no documents", "note": "nothing on file to read"}
    stamp = hashlib.md5((scheme_text + calls_text + MODEL + PROMPT_VERSION + RESOLUTION_PROMPT_VERSION).encode()).hexdigest()
    return _ask(f"{sit['symbol']}::resolution", stamp, resolution_prompt(sit, scheme_text, calls_text), allow_ai, runner)


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
    A = ["| | " + " | ".join(str(y or "n/a") for y in fin["years"]) + " |", "|---|" + "---:|" * len(fin["years"])]
    for r in fin["rows"]:
        pct = any(k in r["metric"].lower() for k in pct_rows)
        A.append(f"| {r['metric']} | " + " | ".join(_v(v, pct and 'growth' in r['metric'].lower())
                                                  if pct else _v(v) for v in r["values"]) + " |")
    return A


def entity_cell(s: dict) -> str:
    """The separated entities for the summary table — ALL of them, each
    with its NSE symbol and listing date when it trades; else the filings'
    resulting company; else the judge's words."""
    ents = DL.separated(s.get("entities"))
    if s["facts"].get("is_the_spin"):
        fp = [e for e in (s.get("entities") or []) if e.get("role") in ("former_parent", "parent") and not e.get("is_parent")]
        if fp:
            e = fp[0]
            return f"this company — spun out of {_short(e['name'], 50)}" + (f" ({e['symbol']})" if e.get("symbol") else "")
    if ents:
        bits = []
        for e in ents[:6]:
            tag = f" ({e['symbol']}, listed {e['listed_on']})" if e.get("symbol") and e.get("listed_on") else \
                (f" ({e['symbol']})" if e.get("symbol") else "")
            bits.append(f"{_short(e['name'], 55)}{tag}")
        more = f"; +{len(ents) - 6} more" if len(ents) > 6 else ""
        return "; ".join(bits) + more
    rc = s["facts"].get("resulting_company")
    if rc:
        return rc[:70]
    w = (s.get("judge") or {}).get("what_is_spun") or ""
    return (w[:70] + ("…" if len(w) > 70 else "")) if w and not w.lower().startswith("not stated") else "—"


def category_of(s: dict) -> str:
    """The line-1 label: what this company's situation is."""
    conf, f = s["confidence"][0], s["facts"]
    if f.get("is_the_spin"):
        return "THE SPIN-OFF ITSELF (the resulting company of a demerger)"
    if f.get("completed") or f.get("mature"):
        return "COMPLETED DEMERGER"
    if s["kind"] == "subsidiary_listing":
        return {"confirmed": "PARTIAL SPIN-OFF (subsidiary IPO)", "probable": "PROBABLE SUBSIDIARY LISTING",
                "indicated": "INDICATED SUBSIDIARY LISTING"}.get(conf, "SUBSIDIARY LISTING — " + conf.upper())
    if s["kind"] == "demerger":
        if conf == "confirmed":
            return "CONFIRMED DEMERGER" + (" (in progress — read from the filings' text)" if f.get("resolved_from_text") else "")
        return {"probable": "PROBABLE DEMERGER", "indicated": "INDICATED DEMERGER"}.get(conf, "DEMERGER — " + conf.upper())
    return f"{s['family'].upper()} — {conf.upper()}"


def timeline_rows(s: dict) -> list[dict]:
    """Every dated event of the situation, oldest first: the stages the
    filings set (with the filing), the dates the documents state (deal
    sheet), NSE's record date, and each entity's listing date."""
    rows: list[dict] = []
    hist = s.get("history") or {}
    heads = hist.get("headlines") or s.get("headlines") or []
    stages = dict(hist.get("stage_dates") or {})
    stages.update(s.get("stage_dates") or {})          # the run's own reading (register-corrected) wins
    for stage, date in stages.items():
        hs = [h for h in heads if h["date"] == date and not h["category"].startswith("Earnings call")]
        h = next((x for x in hs if x.get("attachment")), hs[0] if hs else None)
        src = (f"[{_short(h['category'], 40)}]({h['attachment']})" if h and h.get("attachment")
               else (_short(h["category"], 40) if h else "filing"))
        rows.append({"date": date, "event": f"Stage reached: **{stage.replace('_', ' ')}**", "source": src, "rank": 1})
    f = s["facts"]
    if f.get("record_date"):
        rows.append({"date": str(f["record_date"]), "event": "**Record date**",
                     "source": f.get("record_date_source") or "the filings", "rank": 0})
    for e in s.get("entities") or []:
        if e.get("listed_on") and DL.is_separated(e):
            rows.append({"date": e["listed_on"], "event": f"**{e['name']}** listed" + (f" ({e['symbol']})" if e.get("symbol") else ""),
                         "source": "NSE equity list", "rank": 0})
    if f.get("is_the_spin") and s.get("listed_on"):
        rows.append({"date": s["listed_on"], "event": f"**{s['company']}** itself listed", "source": "NSE equity list", "rank": 0})
    if f.get("partial_spin") and s.get("listed_on") and not any(r["date"] == s["listed_on"] and "listed" in r["event"] for r in rows):
        rows.append({"date": s["listed_on"], "event": f"**{f.get('subsidiary', 'the subsidiary')}** listed",
                     "source": f.get("subsidiary_listing_source", "the filings"), "rank": 0})
    d = s.get("deal") or {}
    for ev in (d.get("dates") or []) if d.get("status") in ("judged", "cached") else []:
        if not isinstance(ev, dict) or not re.match(r"\d{4}-\d{2}", str(ev.get("date") or "")):
            continue
        what = str(ev.get("event") or "").strip()
        if ev.get("entity") and not re.match(SO.UNNAMED_RX, str(ev["entity"])):
            what += f" — {ev['entity']}"
        rows.append({"date": str(ev["date"])[:10], "event": what[0:1].upper() + what[1:],
                     "source": "as stated: " + _short(ev.get("source") or "the documents", 70), "rank": 2})
    seen, out = set(), []
    for r in sorted(rows, key=lambda r: (r["date"], r["rank"])):
        key = (r["date"], re.sub(r"\W", "", r["event"].lower())[:24])
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def _fmt_metric(v) -> str:
    if v is None:
        return "—"
    val, year = v
    return f"{val:,.1f}" .rstrip("0").rstrip(".") + f" ({year})" if isinstance(val, float) else f"{val} ({year})"


def render_exchanges(s: dict, verbatim: bool) -> list[str]:
    cx = s.get("call_exchanges") or []
    n_qa = sum(1 for c in cx for e in c["exchanges"] if e["kind"] == "qa")
    n_rm = sum(1 for c in cx for e in c["exchanges"] if e["kind"] == "remarks")
    if not cx:
        return ["No call in the last 36 months carries a statement about it (or no transcript is on file).", ""]
    A = [f"{len(cx)} call(s), oldest first: **{n_qa} question-and-answer exchange(s)** given in full — the question and "
         f"every answer to it, nothing trimmed — and {n_rm} passage(s) from management's prepared remarks (the complete "
         f"sentences about it; the whole remarks are in the linked transcript). Text is as the transcript prints it.", ""]
    if not verbatim:
        A += ["| Call | Q&A exchanges | Prepared-remarks passages | Transcript |", "|---|---:|---:|---|"]
        for c in cx:
            A.append(f"| {c['call']} | {sum(1 for e in c['exchanges'] if e['kind'] == 'qa')} | "
                     f"{sum(1 for e in c['exchanges'] if e['kind'] == 'remarks')} | "
                     + (f"[transcript]({c['url']})" if c.get("url") else "—") + " |")
        A += ["", f"**The full verbatim text of every exchange is in [companies/{s['symbol']}.md](companies/{s['symbol']}.md#6-on-the-calls-verbatim).**", ""]
        return A
    for c in cx:
        A += [f"#### {c['call']}" + (f" — [transcript]({c['url']})" if c.get("url") else ""), ""]
        for e in c["exchanges"]:
            if e["kind"] == "qa":
                A += ["**Question and answer**", ""]
            else:
                A += [f"**From the prepared remarks** *(the passage about it; the whole turn runs to "
                      f"{e.get('full_chars', 0):,} characters in the transcript)*", ""]
            for speaker, text in e["turns"]:
                A += [f"> **{speaker}:** {text}", ">"]
            A[-1] = ""
    return A


def render_company(s: dict, heavy: bool, verbatim: bool = False) -> list[str]:
    """One company's analysis in nine parts: what it is; stages and dates;
    size beside the parent; insider ownership; why; the calls verbatim; the
    parent's statements; the separated business's statements; other
    financial differences. `verbatim` writes every call exchange in full
    (the company file); otherwise part 6 is a table that links to it."""
    conf, why = s["confidence"]
    L = s["listing"]
    f = s["facts"]
    j = s.get("judge") or {}
    d = s.get("deal") if (s.get("deal") or {}).get("status") in ("judged", "cached") else {}
    ents = DL.separated(s.get("entities"))
    others = [e for e in (s.get("entities") or []) if not DL.is_separated(e)
              and (e.get("dropped") or e.get("note") or e.get("role") == "merged_in"
                   or (e.get("role") == "former_parent" and f.get("is_the_spin"))) and not e.get("is_parent")]
    A = [f"## {s['symbol']} — {s['company']}", "",
         f"### 1. {s['company']} — {category_of(s)}", "",
         f"**{conf.upper()}** ({why}) · **{s['verdict']['label']}** · score {s['verdict']['score']}/10 · "
         f"{s['family']} · {s['n_filings']} filing(s) from {', '.join(s['sources'])} · "
         f"first {s['first_filing']}, latest {s['latest_filing']}", ""]
    if ents:
        A += ["**The separated entities — every one the documents name:**", "",
              "| Entity | Scheme | Business | Listing | Who runs it |", "|---|---|---|---|---|"]
        for e in ents:
            listing = (f"listed {e['listed_on']} as {e['symbol']} (NSE)" if e.get("listed_on")
                       else _short(e.get("listing") or "not stated", 60))
            was = [x for x in (e.get("former_names") or []) if isinstance(x, str) and x.strip()] if isinstance(e.get("former_names"), list) else []
            nm = f"**{e['name']}**" + (f" (earlier {_short(was[0], 45)})" if was else "")
            A.append(f"| {nm} | {_short(e.get('scheme') or '—', 60)} | {_short(e.get('business') or '—', 110)} | {listing} | {_short(e.get('who_runs_it') or '—', 50)} |")
        A.append("")
    if others:
        label = {"parent": "the company itself, what remains", "former_parent": "the company this one was spun out of",
                 "merged_in": "merged in — no shares for the parent's holders", "other": "other party"}
        A += ["**The other parties to the scheme(s)** — not separated entities: "
              + "; ".join(f"{e['name']}" + (f" ({e['symbol']})" if e.get("symbol") else "")
                          + f" — {'dropped / withdrawn' if e.get('dropped') else e.get('note') or label.get(e.get('role'), e.get('role') or 'other party')}"
                          for e in others), ""]
    for a in s.get("uncovered_listings") or []:
        A += [f"> ⚠ NSE's equity list shows **{a['name']} ({a['symbol']})** listed on {a['listed_on']}, after the record "
              f"date, under the parent's name — the documents read do not connect it to this scheme. Check by hand.", ""]
    if j.get("status") in ("judged", "cached"):
        A += [f"**What is being separated, as the documents put it:** {j.get('what_is_spun', '—')} — class "
              f"`{j.get('reason_class', '—')}`.", ""]

    # ---- 2
    A += ["### 2. Stages and dates", "", f"> **Listing:** {L['text']}", ""]
    tl = timeline_rows(s)
    if tl:
        A += ["| Date | Event | Source |", "|---|---|---|"]
        A += [f"| {r['date']} | {r['event']} | {r['source']} |" for r in tl] + [""]
    stages = {**((s.get("history") or {}).get("stage_dates") or {}), **(s.get("stage_dates") or {})}
    if stages:
        order = sorted(stages.items(), key=lambda kv: kv[1])
        A += ["**The stages, as filed:** " + " → ".join(f"{k.replace('_', ' ')} ({v})" for k, v in order), ""]
    if f.get("partial_spin"):
        res = s.get("listing_resolution") or {}
        bits = [f"**{f.get('subsidiary', '—')}**" + (f" ({res['relation']})" if res.get("relation") not in (None, "", "not stated") else ""),
                f"parent's stake {f['parent_stake_before']}" + (f" → {f['parent_stake_after']}" if f.get("parent_stake_after") else "")
                if f.get("parent_stake_before") else (f"parent's stake after: {f['parent_stake_after']}" if f.get("parent_stake_after") else ""),
                f"IPO stage: {f['ipo_stage']}" if f.get("ipo_stage") else "",
                f"exchange: {f['listing_exchange']}" if f.get("listing_exchange") else "",
                f"NSE symbol {f['subsidiary_symbol']}" if f.get("subsidiary_symbol") else "",
                f"timeline: {f['ipo_timeline']}" if f.get("ipo_timeline") else ""]
        A += ["**The partial spin-off:** " + "; ".join(b for b in bits if b) + ".",
              "", f"> “{f.get('listing_quote', '')}”", ""]
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
    if j.get("listing_timeline") and not str(j["listing_timeline"]).lower().startswith("not stated"):
        A += [f"**When it lists, in the documents' words:** {j['listing_timeline']}", ""]

    full = heavy and "parent_financials" in s           # a list-only run has no numbers
    # ---- 3
    A += ["### 3. Size of the separated business beside the parent — is institutional selling likely?", ""]
    sz = s.get("size") or {}
    if sz.get("rows"):
        A += [f"**Reading: {sz['reading']}.**", "",
              "| Entity | Stated turnover | Stated share of the whole | Market cap (₹ cr) | Share of the whole by market cap | Segment revenue share | Index member | Selling on size |",
              "|---|---|---:|---:|---:|---:|---|---|"]
        for r in sz["rows"]:
            A.append(f"| {r['entity']} | {_short(r['stated_turnover'] or '—', 60)} | "
                     + (f"{r['stated_pct']}%" + (f" ({r['stated_basis']})" if r.get("stated_basis") else "")
                        if r["stated_pct"] is not None else "—") + " | "
                     + (f"{r['mcap_cr']:,}" if r["mcap_cr"] else "—") + " | "
                     + (f"{r['mcap_pct']}%" if r["mcap_pct"] is not None else "—") + " | "
                     + (f"{r['segment_pct']}% ({r['segment_fy']})" if r["segment_pct"] is not None else "—") + " | "
                     + ("yes" if r["index_member"] else ("no" if r["symbol"] else "not listed")) + " | "
                     + (r.get("reading") or "—").split(" on size")[0].lower() + " |")
        A += ["", "*Stated figures are the documents' own (a turnover share, or the cost-of-acquisition split the company "
                  "publishes for tax, which reflects relative value). The market-cap share is the entity's value over the whole — "
                  "the parent plus every separated entity that trades"
              + (f" (parent ₹{sz['parent_mcap_cr']:,} cr, whole ₹{sz.get('whole_mcap_cr') or sz['parent_mcap_cr']:,} cr, "
                 f"NSE bhavcopy of {sz['mcap_date']})" if sz.get("parent_mcap_cr") else "")
              + "; the segment share is the business's revenue over the parent's reported sales of that year. Both are computed "
                "here. The reading uses the stated share, else the market-cap share, else the segment share.*", ""]
    elif full:
        A += ["The documents on file give no size for the separated piece, and it has no market value yet.", ""]
    if d.get("size_statement") and not re.match(SO.UNNAMED_RX, str(d["size_statement"])):
        A += [f"**In the documents' words:** “{d['size_statement']}”", ""]
    if j.get("selling_pressure"):
        A += [f"**The judge's read of selling pressure:** {j.get('selling_pressure', '—')} — {j.get('selling_pressure_why', '')}", ""]

    # ---- 4
    A += ["### 4. Insider ownership — share swap, promoters' holding, management incentives", ""]
    swaps = [(e["name"], e.get("swap_ratio")) for e in ents
             if e.get("swap_ratio") and not re.match(SO.UNNAMED_RX, str(e["swap_ratio"]))]
    if swaps:
        A += ["**Share swap / entitlement, entity by entity:**", ""] + [f"- **{n}:** {r}" for n, r in swaps] + [""]
    elif f.get("entitlement_ratio"):
        A += [f"**Share swap / entitlement:** {f['entitlement_ratio']}", ""]
    elif full:
        A += ["**Share swap / entitlement:** not stated in the documents on file.", ""]
    shp = s.get("shareholding") or {}
    if shp:
        A += ["**Promoters' holding, from the shareholding pattern:**", "",
              "| Company | Promoters | FIIs | DIIs | Public | Quarter |", "|---|---:|---:|---:|---:|---|"]
        for sym, table in shp.items():
            p, q = DL.latest_holding(table, "Promoters")
            cells = [DL.latest_holding(table, k)[0] for k in ("FIIs", "DIIs", "Public")]
            label = s["company"] if sym == s["symbol"] else next((e["name"] for e in ents if e.get("symbol") == sym), sym)
            A.append(f"| {label} ({sym}) | " + (f"{p}%" if p is not None else "—") + " | "
                     + " | ".join(f"{c}%" if c is not None else "—" for c in cells) + f" | {q} |")
        A += ["", "*Source: screener.in shareholding pattern, stored under `ShareholdingPattern/NiftyTotalMarket/`. In a "
                  "mirror demerger each shareholder holds the same proportion of the new company as of the parent on the record date.*", ""]
    for label, key in (("Promoters in the parent, per the documents", "promoter_holding_parent"),
                       ("What the promoters will hold in the separated entity", "promoter_holding_after"),
                       ("What a public shareholder receives", "public_shareholders_get"),
                       ("Management incentives", "management_incentives"),
                       ("Insider actions around the separation", "insider_actions")):
        v = d.get(key)
        if v and not re.match(SO.UNNAMED_RX, str(v)):
            A += [f"- **{label}:** {v}"]
        elif full and d:
            A += [f"- **{label}:** not stated in the documents on file."]
    if j.get("status") in ("judged", "cached"):
        A += [f"- **Insiders, per the checklist read:** {j.get('insiders', '—')} · *option pricing date:* {j.get('option_pricing_date', '—')}"]
    A.append("")

    # ---- 5
    r = s.get("rationale") or {}
    A += ["### 5. Why the demerger — point by point", ""]
    if r.get("status") in ("judged", "cached"):
        A += [r.get("rationale", ""), ""]
        pts = [p for p in (r.get("points") or []) if isinstance(p, dict)]
        if pts:
            A += ["**Point by point, with the source:**", ""]
            for n, p in enumerate(pts, 1):
                url = s.get("call_links", {}).get(p.get("call", ""), "")
                src = f"[{p.get('call', '')}]({url})" if url else p.get("call", "")
                A.append(f"{n}. {p.get('point', '')}" + (f" “{p['quote']}”" if p.get("quote") else "") + f" — *{src}*")
            A.append("")
        if r.get("evolution"):
            A += [f"**How it evolved:** {r['evolution']}", ""]
        if r.get("what_management_expects"):
            A += [f"**What management expects from it:** {r['what_management_expects']}", ""]
        if r.get("gaps"):
            A += [f"*Not explained on the calls:* {r['gaps']}", ""]
    elif s["reasons"]:
        A += ["Mechanical read only (judge not run). Stated reasons: " +
              "; ".join(f"{x['reason']} — “{x['quote']}”" for x in s["reasons"]), ""]
    else:
        A += ["No rationale on file: " + (r.get("note") or "no call passages and no scheme rationale text."), ""]
    if j.get("status") in ("judged", "cached"):
        A += [f"- *Stated reason, in one line:* {j.get('reason', '—')}",
              f"- *What it reveals:* {j.get('hidden_value', '—')}",
              f"- *Parent or spin:* {j.get('parent_or_spin', '—')} · *Read next:* {j.get('read_next', '—')}"]
        if j.get("quote"):
            A.append(f"- *In their words:* “{j['quote']}”")
        A.append("")

    # ---- 6
    A += ["### 6. On the calls, verbatim", ""] + render_exchanges(s, verbatim)
    if not full:
        return A + render_light_tail(s)

    # ---- 7
    fin = s["parent_financials"]
    A += ["### 7. The parent's financial statements", "", "**The parent, last three fiscal years (consolidated)**", ""]
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

    # ---- 8
    seg = s.get("segments") or {}
    tables = s.get("segment_tables") or ([s["segment_table"]] if (s.get("segment_table") or {}).get("available") else [])
    own = s.get("entity_financials") or {}
    A += ["### 8. The separated business's financial statements", "",
          "**The business being separated — its own numbers**, entity by entity: its reported statements once it is "
          "listed and on file, and the segment numbers the annual reports and presentations carry for it before that.", ""]
    docs = s.get("docs", {})
    searched = (f"{len(docs.get('annual_reports', []))} annual report(s) and "
                f"{len(docs.get('presentations', []))} presentation(s) on file")
    shown = 0
    for e in ents:
        if e.get("symbol") in own:
            ofin = own[e["symbol"]]
            A += [f"**{e['name']} ({e['symbol']}) — as reported since listing**", ""] + table_md(ofin)
            A += ["", f"*Source: {ofin['source']}; growth and margins computed here.*", ""]
            shown += 1
    for st in tables:
        if not st.get("available") or st.get("side") == "remaining":
            continue
        head = st.get("segment_name") or seg.get("segment_name", "")
        ent = f" → {st['entity']}" if st.get("entity") and st["entity"].lower() not in head.lower() else ""
        A += [f"**{head}{ent}** · unit {st.get('unit') or seg.get('unit', '')} · {st.get('measure_notes') or seg.get('measure_notes', '')}", ""]
        A += table_md(st) + [""]
        srcs = [x for x in st.get("sources", []) if x]
        if srcs:
            A += ["*Sources:* " + "; ".join(dict.fromkeys(srcs)), ""]
        lq = st.get("latest_quarter") or seg.get("latest_quarter") or {}
        if isinstance(lq, dict) and lq.get("period"):
            A += [f"*Latest quarter ({lq['period']}):* revenue {lq.get('revenue', '—')}, "
                  f"operating profit {lq.get('operating_profit', '—')} — {lq.get('source', '')}", ""]
        nf = st.get("not_found") or ""
        if nf:
            A += [f"*Not in the pages read:* {nf}", ""]
        shown += 1
    if seg.get("status") in ("judged", "cached") and seg.get("not_found") and not re.match(SO.UNNAMED_RX, str(seg["not_found"])):
        A += [f"*Businesses with no numbers in the pages read ({searched}):* {seg['not_found']}", ""]
    if not shown:
        if seg.get("status") in ("judged", "cached"):
            A += [f"The segment pages read ({searched}) do not carry this business's own revenue or profit.", ""]
        else:
            A += [f"Not extracted — {seg.get('note') or seg.get('status') or 'judge not run'} ({searched}).", ""]
    if docs.get("annual_reports") or docs.get("presentations"):
        A += ["*Documents on file:* " + "; ".join(
            [f"[{l}]({u})" for l, u, _ in docs.get("annual_reports", [])] +
            [f"[Presentation {l}]({u})" for l, u, _ in docs.get("presentations", [])[:6]]), ""]

    # ---- 9
    A += ["### 9. Other financial differences — working capital, margins, returns, debt", ""]
    cmp_ = s.get("compare") or {}
    cols = [c for c in cmp_.get("columns", [])]
    if len(cols) > 1 and cmp_.get("metrics") and any(c["metrics"] for c in cols[1:]):
        A += ["| Metric (latest year) | " + " | ".join(_short(c["label"], 46) for c in cols) + " |",
              "|---|" + "---:|" * len(cols),
              "| *Basis* | " + " | ".join(f"*{_short(c['basis'], 46)}*" for c in cols) + " |"]
        for k in cmp_["metrics"]:
            A.append(f"| {k} | " + " | ".join(_fmt_metric(c["metrics"].get(k)) for c in cols) + " |")
        A += ["", "*Each figure is the latest on file, with its year. Working-capital days and ROCE come from the stored "
                  "working-capital file; segment figures from the pages cited in part 8. A dash means the documents do not carry it.*", ""]
    elif cols and cols[0]["metrics"]:
        A += ["Only the parent's figures are on file: " + "; ".join(
            f"{k} {_fmt_metric(v)}" for k, v in cols[0]["metrics"].items()) + ". The separated business has no "
            "comparable numbers in the documents read.", ""]
    else:
        A += ["No comparable figures on file for either side.", ""]
    stay = [st for st in tables if st.get("available") and st.get("side") == "remaining"]
    if stay:
        A += ["**What stays with the parent — its segments, from the same pages:**", "",
              "| Remaining segment | Revenue | Operating margin | ROCE | Segment assets / revenue | Unit | Year |",
              "|---|---:|---:|---:|---:|---|---|"]
        for st in stay:
            def last(prefix):
                row = next((r for r in st["rows"] if r["metric"].startswith(prefix)), None)
                return DL._last(row["values"], st["years"]) if row else (None, "")
            rev, yr = last("Revenue (")
            opm, _ = last("Operating margin")
            roce, _ = last("Return on capital employed")
            atr, _ = last("Segment assets / revenue")
            A.append(f"| {st.get('segment_name', '')} | " + (f"{rev:,.0f}" if rev is not None else "—") + " | "
                     + (f"{opm}%" if opm is not None else "—") + " | " + (f"{roce}%" if roce is not None else "—") + " | "
                     + (f"{atr}x" if atr is not None else "—") + f" | {_short(st.get('unit', ''), 24)} | {yr} |")
        A.append("")
    diffs = [x for x in (d.get("other_differences") or []) if isinstance(x, dict)]
    if diffs:
        A += ["**What the documents themselves say about the differences:**", ""]
        for x in diffs[:10]:
            A.append(f"- **{x.get('metric', '')}** — parent / remaining: {x.get('parent_or_remaining', '—')}; "
                     f"separated business: {x.get('separated_business', '—')}"
                     + (f" “{x['quote']}”" if x.get("quote") else ""))
        A.append("")
    return A + render_light_tail(s)


def _short(x, n: int = 70) -> str:
    x = str(x or "—").replace("|", "/").replace("\n", " ")
    return x if len(x) <= n else x[:n - 1] + "…"


def _buyers(o: dict, f: dict) -> str:
    """One cell: who is buying, promoters first."""
    al = [a for a in (o.get("allottees") or []) if isinstance(a, dict) and a.get("name")]
    if al:
        parts = []
        for a in al[:5]:
            tag = a.get("category", "")
            parts.append(f"**{a['name']}** ({tag})" if tag and "promoter" in tag.lower() else f"{a['name']} ({tag})" if tag else a["name"])
        more = f" +{len(al) - 5} more" if len(al) > 5 else ""
        return "; ".join(parts) + more
    if f.get("allottees"):
        return "; ".join(f["allottees"][:4])
    return "not named in the filings on file"


def render_offerings(offs: list[dict]) -> list[str]:
    """Rights and preferential offerings — the paper, the price, and WHO
    IS BUYING. The notes' tell: insiders taking the paper."""
    A = ["## Rights and preferential offerings — who is buying", "",
         "A rights issue hands the paper to existing holders; a preferential issue of equity or "
         "warrants hands it to named buyers at a fixed price. The notes' question is the same for "
         "both: are the insiders putting money in? Promoters taking warrants (25% upfront, 18 "
         "months to convert) is insiders betting on the stock; paper placed with outsiders is "
         "dilution. Each row names the buyers the filings name.", ""]
    if not offs:
        return A + ["- (none on file)", ""]
    A += ["| Company | Instrument | Size | Price | Who is buying | Promoters in? | Stage | Latest filing |",
          "|---|---|---|---|---|---|---|---|"]
    def key(s):
        o = s.get("offering") or {}
        prom = any("promoter" in str(a.get("category", "")).lower() for a in (o.get("allottees") or []) if isinstance(a, dict)) \
            or s["facts"].get("promoters_buying")
        return (not prom, s["kind"] != "preferential_issue", s["symbol"])
    for s in sorted(offs, key=key):
        o, f = s.get("offering") or {}, s["facts"]
        judged = o.get("status") in ("judged", "cached")
        instrument = o.get("instrument") if judged else f.get("instrument", "—")
        size = (o.get("total_amount") if judged and o.get("total_amount") not in (None, "not stated") else f.get("amount")) or \
               (f"{f['securities']} securities" if f.get("securities") else "—")
        price = (o.get("issue_price") if judged and o.get("issue_price") not in (None, "not stated") else
                 (f"₹{f['issue_price']}" if f.get("issue_price") else "—"))
        prom_in = "yes" if (judged and any("promoter" in str(a.get("category", "")).lower() for a in (o.get("allottees") or []) if isinstance(a, dict))) \
            or f.get("promoters_buying") else ("no" if judged and o.get("allottees") else "unknown")
        if judged and o.get("promoter_share_of_issue") not in (None, "", "not stated"):
            prom_in += f" ({o['promoter_share_of_issue']})"
        stage = o.get("stage") if judged and o.get("stage") != "not stated" else s["stage"]
        A.append(f"| **{s['symbol']}** | {instrument or '—'} | {_short(size)} | {_short(price)} | {_buyers(o, f)} | "
                 f"{_short(prom_in, 60)} | {stage} | {s['latest_filing']} |")
    A.append("")
    A += ["<details><summary>Each offering, with the filing's own words</summary>", ""]
    for s in sorted(offs, key=key):
        o, f = s.get("offering") or {}, s["facts"]
        A.append(f"**{s['symbol']} — {s['company']}** · {s['family']} · {s['n_filings']} filing(s), {s['first_filing']} → {s['latest_filing']}")
        if o.get("status") in ("judged", "cached"):
            bits = [x for x in (
                f"purpose: {o['purpose']}" if o.get("purpose") not in (None, "not stated") else "",
                f"pricing: {o['pricing_basis']}" if o.get("pricing_basis") not in (None, "not stated") else "",
                f"warrants: {o['upfront_paid']}" if o.get("upfront_paid") not in (None, "not stated") else "",
                f"promoters' intent: {o['promoter_intent']}" if o.get("promoter_intent") not in (None, "not stated") else "") if x]
            if bits:
                A.append("- " + "; ".join(bits))
            if o.get("quote"):
                A.append(f"- “{o['quote']}”")
        elif f.get("promoter_quote"):
            A.append(f"- “{f['promoter_quote']}”")
        else:
            A.append(f"- {o.get('note') or 'mechanical read only'}")
        link = next((h["attachment"] for h in reversed(s["headlines"]) if h["attachment"]), "")
        if link:
            A.append(f"- filing: [{s['headlines'][-1]['headline'][:120]}]({link})")
        A.append("")
    A += ["</details>", ""]
    return A


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


def completed_date_of(s: dict) -> str:
    """A sortable date for a completed demerger: the full date when there
    is one, else the year the documents give, else ''."""
    f = s["facts"]
    d = f.get("completed_date") if f.get("completed") else f.get("record_date")
    d = str(d or "")
    m = re.search(r"\d{4}-\d{2}-\d{2}", d) or re.search(r"\d{4}-\d{2}", d) or re.search(r"(?:19|20)\d\d", d)
    return m.group(0) if m else ""


KIND_RANK = {"demerger": 0, "subsidiary_listing": 1, "scheme_other": 2, "merger": 3}
CONF_RANK = {"confirmed": 0, "probable": 1, "indicated": 2, "other": 3}
NSE_QUOTE = "https://www.nseindia.com/get-quotes/equity?symbol={sym}"


def probable_order(s: dict) -> tuple:
    """Demergers first, then subsidiary listings, then unclear schemes;
    probable before indicated; higher score first."""
    return (KIND_RANK.get(s["kind"], 9), CONF_RANK.get(s["confidence"][0], 9),
            -float(s.get("verdict", {}).get("score") or 0), s["symbol"])


def rows_index(rows: list[dict]) -> dict:
    """The filings store keyed two ways, so a saved run's headlines (which
    may predate ann_id on headlines) find their stored text file."""
    idx: dict = {}
    for r in rows:
        if r.get("ann_id"):
            idx[("id", r["symbol"], r["ann_id"])] = r
        idx[("hd", r["symbol"], r["date"], (r.get("headline") or "")[:220])] = r
    return idx


_CALL_PAGES: dict[str, list[str]] = {}


def call_page(symbol: str, quote: str) -> int | None:
    """The page of the consolidated transcript PDF (ConferenceCalls/…/
    SYMBOL.pdf) that carries the quote, or None."""
    if symbol not in _CALL_PAGES:
        pages: list[str] = []
        p = SO.CONCALLS / f"{symbol}.pdf"
        if p.exists():
            try:
                import PyPDF2                                   # noqa: PLC0415
                reader = PyPDF2.PdfReader(str(p), strict=False)
                pages = [re.sub(r"\s+", " ", pg.extract_text() or "") for pg in reader.pages]
            except Exception:                                   # noqa: BLE001
                pages = []
        _CALL_PAGES[symbol] = pages
    needle = re.sub(r"\s+", " ", quote.strip(" …\"“”"))[:80]
    if len(needle) < 20:
        return None
    for i, t in enumerate(_CALL_PAGES[symbol], 1):
        if needle in t:
            return i
    return None


def _rel(path: Path) -> str:
    return os.path.relpath(path, OUT_DIR).replace(os.sep, "/")


def sources_and_evidence(s: dict, idx: dict | None = None, limit: int = 3) -> str:
    """One cell: for each document the row was read from (its kind's
    filings newest first, then the rest), the link, and the KEYWORD, the
    stored text file with LINE number, and the SENTENCE that made it a
    spin-off / demerger / listing / scheme. Call mentions cite the
    transcript page; a register record date cites the register file."""
    idx = idx or {}
    kind = s["kind"]
    heads = sorted(s.get("headlines", []), key=lambda h: h["date"], reverse=True)
    own = [h for h in heads if h["kind"] == kind] or heads
    seen, out = set(), []
    for h in own + [h for h in heads if h not in own]:
        cat, url = h.get("category", ""), h.get("attachment") or ""
        row = (idx.get(("id", s["symbol"], h.get("ann_id") or "")) or
               idx.get(("hd", s["symbol"], h["date"], h["headline"][:220])) or {})
        if cat.startswith("Record Date (corporate"):
            key = f"reg{h['date']}"
            if key in seen:
                continue
            seen.add(key)
            gt = SO.REGISTER
            line = ""
            if gt.exists():
                for n, ln in enumerate(gt.read_text(errors="replace").splitlines(), 1):
                    if ln.startswith(f"{h['date']},{s['symbol']},"):
                        line = f" · [register line {n}]({_rel(gt)}#L{n})"
                        break
            out.append(f"[{h['date']} NSE register]({NSE_QUOTE.format(sym=s['symbol'])}) · **Demerger** record date{line}")
        elif cat.startswith("Earnings call"):
            ev = SO.evidence_in(h["headline"], kind, 1)
            kw = ev[0]["keyword"] if ev else (SO.MENTION_RX.search(h["headline"]) or [""])[0]
            page = call_page(s["symbol"], h["headline"])
            key = ("call", cat, kw.lower(), page)         # one quote per call, keyword and page
            if key in seen:
                continue
            seen.add(key)
            link = f"[{h['date'][:7]} call transcript]({url})" if url else f"{h['date'][:7]} call"
            where = f"{s['symbol']}.pdf page {page}" if page else f"{s['symbol']}.pdf"
            out.append(f"{link} · **{kw or 'call mention'}** · {where} · “{h['headline'][:220].strip(' …')}”")
        else:
            if not url or url in seen:
                continue
            seen.add(url)
            tf = row.get("text_file") or h.get("text_file") or ""
            text, where = "", ""
            if tf.startswith("text/") and (SO.ANN_DIR / tf).exists():
                text, where = SO.load_text({"text_file": tf}), SO.ANN_DIR / tf
            elif row:
                text = SO.load_first_pages(row)
                safe = re.sub(r"[^A-Za-z0-9_-]", "_", row.get("ann_id", ""))[:40]
                where = SO.ANN_DIR / "text" / "first" / f"{s['symbol']}_{safe}.txt"
            ev = SO.evidence_in(text, kind, 1) if text else []
            link = f"[{h['date']} {cat[:28]}]({url})"
            if ev:
                e = ev[0]
                out.append(f"{link} · **{e['keyword']}** · [text line {e['line']}]({_rel(where)}#L{e['line']}) · “{e['sentence']}”")
            else:
                hev = SO.evidence_in(f"{cat} {h['headline']}", kind, 1)
                kw = hev[0]["keyword"] if hev else cat
                out.append(f"{link} · **{kw}** · headline · “{h['headline'][:200]}”")
        if len(out) == limit:
            break
    more = len({h.get("attachment") for h in heads if h.get("attachment")}) - len(out)
    if more > 0:
        out.append(f"+{more} more documents")
    return "<br>".join(out) if out else "—"


def source_links(s: dict, limit: int = 4) -> str:
    """Links only (the evidence cell without the quotes) — kept for callers
    that want the short form."""
    return re.sub(r" · \*\*.*?(?=<br>|$)", "", sources_and_evidence(s, None, limit))


def render_report(record: dict, idx: dict | None = None) -> str:
    """The report. `idx` (rows_index of the filings store) lets the
    probable table cite each row's stored text with line numbers."""
    m = record["meta"]
    sits = record["situations"]
    spins = [s for s in sits if s["kind"] in SO.SPIN_KINDS and s["confidence"][0] != "other"]
    offs = [s for s in sits if s["kind"] in SO.OFFERING_KINDS]
    others = [s for s in sits if (s["kind"] not in SO.SPIN_KINDS and s["kind"] not in SO.OFFERING_KINDS)
              or (s["kind"] in SO.SPIN_KINDS and s["confidence"][0] == "other")]
    conf = {s["symbol"]: s["confidence"][0] for s in spins}
    all_confirmed = [s for s in spins if conf[s["symbol"]] == "confirmed"]
    # partial spin-offs — a subsidiary listed, or being listed, by IPO while
    # the parent keeps a stake — sit in the confirmed list below the demergers
    partial = [s for s in all_confirmed if s["kind"] == "subsidiary_listing"]
    partial += [s["also_partial"] for s in sits if s.get("also_partial")]      # also a demerger, shown above or among the others
    partial.sort(key=lambda s: (s["stage"] != "listed", -(s["verdict"].get("score") or 0), s["symbol"]))
    confirmed = [s for s in all_confirmed if s["kind"] != "subsidiary_listing"]
    # demergers confirmed by reading the filings' text (no scheme-category
    # filing names them) go to the bottom of the demerger list
    confirmed.sort(key=lambda s: bool(s["facts"].get("resolved_from_text")))
    # completed demergers: read as completed from the documents, or recorded
    # by NSE's register more than two years before the run
    completed = [s for s in sits if s["kind"] == "demerger"
                 and (s["confidence"][0] == "completed" or s["facts"].get("mature"))]
    completed.sort(key=lambda s: str(completed_date_of(s)), reverse=True)
    done = {id(s) for s in completed}
    others = [s for s in others if id(s) not in done]
    probable = [s for s in spins if conf[s["symbol"]] == "probable"]
    indicated = [s for s in spins if conf[s["symbol"]] == "indicated"]
    A = ["# Spin-offs and demergers — NiftyTotalMarket", "",
         f"*Run {m['run_date']} · filings window {m['window_from']} → {m['window_to']} · "
         f"{m['filings']} restructuring filings across {m['companies']} companies · "
         f"{len(confirmed)} confirmed demergers, {len(partial)} partial spin-offs (subsidiary IPOs), "
         f"{len(completed)} completed demergers, {len(probable)} probable, {len(indicated)} indicated, "
         f"{len(offs)} rights / preferential offerings, {len(others)} other restructurings · judge: {m['judge']}.*", "",
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
        mark = " †" if s["facts"].get("resolved_from_text") else ""
        A.append(f"| **{s['symbol']}**{mark} | {entity_cell(s)} | "
                 f"{s['stage']} | {s['listing']['short']} | {s['verdict']['score']} | {s['verdict']['label'].split(' — ')[0]} |")
    if not confirmed:
        A.append("| — | | | | | |")
    if any(s["facts"].get("resolved_from_text") for s in confirmed):
        A += ["", "† *A demerger in progress, confirmed by reading the complete filings: the text describes this company's "
                  "scheme, but no filing sits in a scheme category or names it in its headline. Listed last.*"]
    A += ["", "### Partial spin-offs — a subsidiary listed, or being listed, by IPO", "",
          "The parent keeps a stake and the piece gets its own price (the notes' Sears case: once the piece trades, "
          "the parent's stub can be valued). Already listed first, then IPOs in motion. A listing date marked "
          "*NSE* is from the exchange's equity list; otherwise it is the date the filings give.", "",
          "| Company | Subsidiary | Relation · parent's stake | IPO stage | Listing | Score | Verdict | Evidence |",
          "|---|---|---|---|---|---:|---|---|"]
    also = {s["symbol"] for s in sits if s.get("also_partial")}
    for s in partial:
        f = s["facts"]
        res = s.get("listing_resolution") or {}
        stake = " → ".join(x for x in (f.get("parent_stake_before"), f.get("parent_stake_after")) if x) or "not stated"
        rel = res.get("relation") if res.get("relation") not in (None, "", "not stated") else "subsidiary"
        when = (f"{s['listed_on']} ({'NSE' if f.get('subsidiary_listing_source') == 'NSE equity list' else 'filings'})"
                if s.get("listed_on") else ("listed; date not stated" if s["stage"] == "listed"
                                             else _short(f.get("ipo_timeline") or "date not fixed", 110)))
        more = f"; also {', '.join(str(x) for x in f['other_subsidiaries'] if x)}"[:70] if f.get("other_subsidiaries") else ""
        subs = [e for e in DL.separated(s.get("entities")) if e.get("role") == "listed_subsidiary"]
        if len(subs) > 1:                 # several subsidiaries: each with where it stands (Coal India's four)
            main = SO._norm_name(f.get("subsidiary") or "")
            rest = [e for e in subs if SO._norm_name(e["name"]) != main]
            more = "; also " + "; ".join(
                f"{_short(e['name'], 50)} — " + (f"listed {e['listed_on']} ({e['symbol']})" if e.get("listed_on") else "IPO in motion")
                for e in rest[:5])
        if s["symbol"] in also:
            more += " *(the company also has a demerger on file)*"
        A.append(f"| **{s['symbol']}** | {f.get('subsidiary', '—')[:60]}{more} | {rel} · {stake[:40]} | "
                 f"{f.get('ipo_stage', '—')} | {when} | {s['verdict']['score']} | "
                 f"{s['verdict']['label'].split(' — ')[0]} | “{(f.get('listing_quote') or '')[:160]}” |")
    if not partial:
        A.append("| — | | | | | | | |")
    A += ["", "### Completed demergers — already effective, with their dates", "",
          "Demergers the documents describe as already done, newest first. The date is NSE's record date when the "
          "register has one, the resulting company's listing date from NSE's equity list when it is found there, "
          "and otherwise the date the filings give. Kept for the record; older than two years they are past the "
          "window the notes care about.", "",
          "| Company | Role | Business · counterpart | Completed | Source of the date | Evidence |",
          "|---|---|---|---|---|---|"]
    for s in completed:
        f = s["facts"]
        j = s.get("judge") or {}
        if f.get("completed"):
            role, when, src = f.get("completed_role", ""), f.get("completed_date", ""), f.get("completed_date_source", "")
            biz = f.get("demerged_business", "")
            other = f.get("completed_counterpart", "")
            ev = f.get("resolution_quote", "")
        else:                                         # recorded by the register, more than two years ago
            role, when, src = "demerged company", f.get("record_date", ""), "NSE register (record date)"
            biz = j.get("what_is_spun") or ""
            other = f.get("resulting_company", "")
            ev = j.get("quote") or ""
        A.append(f"| **{s['symbol']}** | {role} | {_short(biz, 90)}" + (f" · {_short(other, 50)}" if other else "")
                 + f" | {when} | {src} | “{_short(ev, 170)}” |")
    if not completed:
        A.append("| — | | | | | |")
    # demergers first, then subsidiary listings, then schemes of unclear
    # nature; probable before indicated; then by score
    probable.sort(key=probable_order)
    indicated.sort(key=probable_order)
    A += ["", "## Probable and indicated", "",
          "What is left after every row has been read and settled: management's own indications, withdrawn "
          "proposals, and any row the judge could not be asked about. Demergers first. "
          "**Sources & evidence**: for each document the row was read from (exchange filings newest first, or the "
          "call transcript), the link, the **keyword** that made it a spin-off / demerger / listing / scheme, the "
          "stored text file with the line number, and the sentence around it. Call mentions cite the transcript "
          "page; a register record date cites the register file.", "",
          "| Company | What | Confidence | Stage | Listing | Score | Sources & evidence |", "|---|---|---|---|---|---:|---|"]
    for s in sorted(probable + indicated, key=probable_order):
        A.append(f"| **{s['symbol']}** | {s['family']} | {s['confidence'][0]} — {s['confidence'][1][:60]} | "
                 f"{s['stage']} | {s['listing']['short']} | {s['verdict']['score']} | {sources_and_evidence(s, idx)} |")
    if not probable and not indicated:
        A.append("| — | | | | | | |")
    A.append("")
    if others:
        A += ["<details><summary>Other restructurings on file (mergers, slump sales, rights, "
              f"capital actions) — {len(others)}</summary>", "",
              "| Company | What | Stage | First filing | Filings |", "|---|---|---|---|---:|"]
        A += [f"| {s['symbol']} | {s['family']} | {s['stage']} | {s['first_filing']} | {s['n_filings']} |"
              for s in others]
        A += ["", "</details>", ""]
    A += ["---", "", "**How each company is written up.** Nine parts, in this order: (1) the company and what its situation "
          "is; (2) stages and dates — filings, record date and every entity's listing; (3) the size of the separated "
          "business beside the parent, and whether institutional selling is likely; (4) insider ownership — share swap, "
          "promoters' holding, management incentives; (5) why, point by point; (6) the management calls, verbatim; "
          "(7) the parent's financial statements; (8) the separated business's financial statements; (9) other "
          "financial differences — working capital, margins, returns, debt. In this report part 6 is a table of calls; "
          "**the complete text of every question and answer is in the company's own file under `companies/`**, which "
          "carries all nine parts.", ""]
    A += ["---", "", "# Confirmed demergers — in full", ""]
    for s in confirmed:
        A += render_company(s, heavy=True)
    A += ["---", "", "# Partial spin-offs (subsidiary IPOs) — in full", ""]
    for s in partial:
        if s["symbol"] not in also:                 # those are written up once, under their demerger
            A += render_company(s, heavy=True)
    A += ["---", "", "# Probable spin-offs and listings", ""]
    for s in probable:
        A += render_company(s, heavy=True)
    A += ["---", "", "# Indicated only", ""]
    for s in indicated:
        A += render_company(s, heavy=False)
    A += render_offerings([s for s in sits if s["kind"] in SO.OFFERING_KINDS])
    only_calls = record.get("call_only", [])
    A += ["## Indicated on the calls, not yet filed", "",
          "Companies whose management used forward-looking spin-off / demerger / listing language "
          f"in the last {SO.CONCALL_MONTHS} months of calls but have no restructuring filing on file.", ""]
    if only_calls:
        A += ["| Company | What the calls indicate | Forward-looking / all mentions | Latest | Example |", "|---|---|---:|---|---|"]
        for c in only_calls:
            A.append(f"| **{c['symbol']}** | {SO.family_of(c.get('kind', ''))} | {c['forward']} / {c['n']} | {c['latest']} | “{c['example'][:200]}” |")
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
                    "subsidiary": f.get("subsidiary", ""), "ipo_stage": f.get("ipo_stage", ""),
                    "listing_resolution": f.get("listing_resolution", ""),
                    "resolution": f.get("resolution", ""), "completed_date": f.get("completed_date", ""),
                    "completed_date_source": f.get("completed_date_source", ""),
                    "confidence_reason": s["confidence"][1][:240],
                    "entitlement_ratio": f.get("entitlement_ratio", ""),
                    "record_date": f.get("record_date", ""),
                    "reasons": "; ".join(r["reason"] for r in s["reasons"]),
                    "concall_mentions": len(s["concall_mentions"]),
                    "judge_status": (s.get("judge") or {}).get("status", "")})
    return out


def offering_rows(sits: list[dict]) -> list[dict]:
    out = []
    for s in sits:
        if s["kind"] not in SO.OFFERING_KINDS:
            continue
        o, f = s.get("offering") or {}, s["facts"]
        al = [a for a in (o.get("allottees") or []) if isinstance(a, dict)]
        out.append({"symbol": s["symbol"], "company": s["company"], "kind": s["kind"],
                    "instrument": o.get("instrument") or f.get("instrument", ""),
                    "securities": o.get("securities") or f.get("securities", ""),
                    "issue_price": o.get("issue_price") or f.get("issue_price", ""),
                    "total_amount": o.get("total_amount") or f.get("amount", ""),
                    "allottees": "; ".join(f"{a.get('name', '')} [{a.get('category', '')}]" for a in al) or "; ".join(f.get("allottees", [])),
                    "promoters_buying": "yes" if any("promoter" in str(a.get("category", "")).lower() for a in al) or f.get("promoters_buying") else "",
                    "promoter_share_of_issue": o.get("promoter_share_of_issue", ""),
                    "promoter_intent": o.get("promoter_intent", ""), "purpose": o.get("purpose", ""),
                    "stage": o.get("stage") or s["stage"], "first_filing": s["first_filing"],
                    "latest_filing": s["latest_filing"], "n_filings": s["n_filings"],
                    "judge_status": o.get("status", "")})
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
                    "parent_pnl": "yes" if (s.get("parent_financials") or {}).get("available") else "no",
                    "cash_flow": "yes" if (s.get("cash_flows") or {}).get("available") else "no",
                    "pe": "yes" if (s.get("pe") or {}).get("pe") is not None else "no",
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


_MEMBERS: dict | None = None


def _members() -> dict:
    global _MEMBERS
    if _MEMBERS is None:
        _MEMBERS = FA.universe()
    return _MEMBERS


_STORE: list[dict] | None = None
SPIN_TAGS = {"demerger", "scheme_other", "subsidiary_listing"}
SCHEME_FIRST = ("Scheme of Arrangement", "Demerger", "Amalgamation/Merger")


def store_rows(symbol: str, today: dt.date) -> list[dict]:
    """Every filing of a company in the store up to `today` — the run's
    window is a year, but a scheme's documents can be older."""
    global _STORE
    if _STORE is None:
        _STORE = SO.load_filings()
    lim = today.isoformat()
    return [r for r in _STORE if r["symbol"] == symbol and r["date"] <= lim]


DEAL_HEAD_CHARS = 6_000


def deal_text_for(symbol: str, today: dt.date, budget: int = FILINGS_CHARS, head: int = DEAL_HEAD_CHARS) -> str:
    """The documents of the company's separations over the WHOLE store —
    every filing tagged demerger / scheme / subsidiary listing. When they
    fit the budget they are given complete. When they do not, coverage
    comes first: EVERY filing contributes its opening pages (the
    Regulation 30 disclosure that names the entities, the ratio, the
    turnover and the listing), so an older scheme is never crowded out by
    a newer one (Vedanta's four demerged companies behind its later
    real-estate scheme); the room left then completes whole documents,
    the shortest first, and what remains is shared among the longest.
    Each truncated filing says how much of it is shown. Newest first."""
    rows = [r for r in store_rows(symbol, today) if r.get("source") != "CALLS"
            and SPIN_TAGS & set((r.get("tags") or r.get("kind") or "").split("|"))]
    rows.sort(key=lambda r: r["date"], reverse=True)
    docs, seen = [], set()
    for r in rows:
        t = SO.load_text(r) or SO.load_first_pages(r)
        key = hashlib.md5(t[:4000].encode()).hexdigest() if t else ""
        if not t or key in seen:
            continue
        seen.add(key)
        docs.append((r, t))
    if not docs:
        return "[0 filings in full]\n\n"
    heads = [f"### FILING {r['date']} · {r['category']} · {r['headline'][:160]}\n" for r, _ in docs]
    room = budget - sum(len(h) for h in heads)
    sizes = [len(t) for _, t in docs]
    if sum(sizes) <= room:
        take = sizes[:]
    else:
        h = max(1_500, min(head, int(room * 0.6 / len(docs))))
        take = [min(n, h) for n in sizes]
        left = room - sum(take)
        for i in sorted(range(len(docs)), key=lambda i: sizes[i]):          # whole documents, shortest first
            need = sizes[i] - take[i]
            if 0 < need <= left:
                take[i], left = sizes[i], left - need
        cut = [i for i in range(len(docs)) if take[i] < sizes[i]]
        for i in cut:                                                      # the rest, shared among the longest
            take[i] += min(sizes[i] - take[i], max(0, left) // len(cut))
    parts, whole = [], 0
    for (r, t), hd, n in zip(docs, heads, take):
        if n >= len(t):
            parts.append(hd + t)
            whole += 1
        else:
            parts.append(hd + f"[the first {n:,} of {len(t):,} characters of this filing]\n" + t[:max(n, 0)])
    note = (f"[{len(docs)} filings: {whole} in full, {len(docs) - whole} by their opening pages]\n\n"
            if whole < len(docs) else f"[{len(docs)} filings in full]\n\n")
    return note + "\n\n".join(parts)


def full_history(s: dict, today: dt.date) -> dict:
    """The stages and filings of this company's separation over the whole
    store, for the dated timeline (the run's own window may hold only the
    last of them)."""
    rows = store_rows(s["symbol"], today)
    if not rows:
        return {}
    for sit in SO.build_situations(rows, None, today):
        if sit["kind"] in SO.SPIN_KINDS:
            return {"stage_dates": sit["stage_dates"], "first_filing": sit["first_filing"], "n_filings": sit["n_filings"],
                    "headlines": [h for h in sit["headlines"] if not h["category"].startswith("Earnings call")]}
    return {}


def entities_for(s: dict, today: dt.date) -> list[dict]:
    """Every separated entity of a situation: the deal sheet's list, then
    whatever the mechanical read and the listing resolution named that the
    deal sheet lacks — each with its NSE symbol and listing date."""
    d = s.get("deal") or {}
    raw = [e for e in (d.get("entities") or []) if isinstance(e, dict)] if d.get("status") in ("judged", "cached") else []
    f = s["facts"]
    if not raw:                          # no deal sheet: the mechanical read's names are all there is
        for extra in [f.get("resulting_company"), f.get("subsidiary")] + list(f.get("other_subsidiaries") or []):
            if extra and isinstance(extra, str):
                raw.append({"name": extra, "role": "listed_subsidiary" if s["kind"] == "subsidiary_listing" else "resulting"})
    return settle_roles(s, DL.enrich_entities(raw, s["symbol"], today))


HISTORY_DAYS = 365


def settle_roles(s: dict, ents: list[dict]) -> list[dict]:
    """The judge's role, held to what this situation is. A resulting
    company that listed more than a year BEFORE the record date is an
    earlier separation the documents still mention (Triveni Turbine, 2011,
    beside Triveni Power Transmission). In a subsidiary-IPO situation only
    the subsidiaries being listed are separated entities — a 'resulting'
    company there is a scheme inside the group (Reliance Consumer
    Products). In a demerger, a 'listed subsidiary' counts only when the
    listing question found one or the exchange shows it listed (not
    Lloyds' acquisition of Steel Infra Solutions)."""
    rd = str(s["facts"].get("record_date") or "")[:10]
    for e in ents:
        if e["role"] == "resulting" and e.get("listed_on") and rd:
            try:
                early = (dt.date.fromisoformat(rd) - dt.date.fromisoformat(e["listed_on"])).days > HISTORY_DAYS
            except ValueError:
                early = False
            if early:
                e["role"], e["note"] = "other", f"an earlier separation — listed {e['listed_on']}"
        if s["kind"] == "subsidiary_listing" and e["role"] == "resulting":
            e["role"], e["note"] = "other", "a scheme inside the group, not a listing for the parent's holders"
        if s["kind"] != "subsidiary_listing" and e["role"] == "listed_subsidiary" \
                and not (s.get("also_partial") or s["facts"].get("partial_spin") or e.get("listed_on")):
            e["role"], e["note"] = "other", "no listing of it on the record"
    return ents


def uncovered_listings(s: dict) -> list[dict]:
    """New listings after the record date that carry the parent's name and
    that the deal sheet did not account for at all — shown as a warning,
    never added to the entities on the name alone."""
    have = {e.get("symbol") for e in s.get("entities") or [] if e.get("symbol")}
    return [a for a in (s.get("nse_arrivals") or []) if a["symbol"] not in have and a["why"].startswith("carries")]


def enrich(s: dict, rows: list[dict], ai: bool, today: dt.date, live: dict,
           fetch_docs: bool = False, runner=None, list_only: bool = False) -> None:
    """Everything beyond the mechanical situation: confidence, judge,
    listing status, and — for confirmed / probable — rationale, parent
    numbers, documents and segment numbers. `list_only` stops after the
    judge's classification and the listing status (a backtest of the
    LIST needs no rationale, numbers or offerings)."""
    s["confidence"] = SO.confidence(s)
    if s["kind"] == "demerger" and s["facts"].get("mature"):
        s["family"] = f"completed spin-off — mature (record date {s['facts'].get('record_date', '')})"
    scheme = scheme_text_for(s, rows)
    calls12 = calls_text_for(s["symbol"], SO.CONCALL_MONTHS, today) if s["kind"] in SO.SPIN_KINDS else ""
    s["documents_read"] = {"filings_chars": len(scheme), "calls_12m_chars": len(calls12)}
    s["judge"] = judge(s, scheme, calls12, allow_ai=ai, runner=runner) \
        if s["kind"] in SO.SPIN_KINDS else {}
    if SO.spin_identity(s, s["judge"], today):        # this company IS the spun entity
        s["verdict"] = SO.verdict(s, s["checklist"])
    new_kind, why = SO.judge_override(s, s["judge"])
    if new_kind == "merger":
        s["kind"], s["family"] = "merger", SO.family_of("merger")
        s["confidence"] = ("other", why)
        s["verdict"] = SO.verdict(s, s["checklist"])
    elif new_kind == "other":
        s["family"] = "not a spin-off for this company's holders (" + why.split(";")[0] + ")"
        s["confidence"] = ("other", why)
        s["verdict"] = {"label": "NOT A SPIN-OFF — " + why, "score": s["verdict"]["score"]}
    else:
        conf, stage = SO.judge_adjust(s, s["judge"])
        if conf:
            s["confidence"] = conf
        if stage:
            s["stage"], s["listed_on"], s["days_since_listing"] = stage, None, None
            s["verdict"] = SO.verdict(s, s["checklist"])
    # a subsidiary listing is resolved with one pointed question: a partial
    # spin-off (announced or already listed) joins the confirmed list below
    # the demergers; anything else leaves the confirmed and probable lists
    if s["kind"] == "subsidiary_listing" and s["confidence"][0] == "probable":
        s["listing_resolution"] = judge_listing(s, scheme, calls12, allow_ai=ai, runner=runner)
        if SO.resolve_subsidiary_listing(s, s["listing_resolution"], today) != "unresolved":
            s["verdict"] = SO.verdict(s, s["checklist"])
    elif s["kind"] in ("demerger", "scheme_other") and any(
            h["kind"] == "subsidiary_listing" and not h["category"].startswith("Earnings call") for h in s["headlines"]):
        # a company is one spin situation, and a demerger tag outranks a
        # subsidiary-listing tag — so HDFC Bank's HDB Financial IPO sat hidden
        # behind a text-only 'demerger'. Ask the listing question here too.
        res = judge_listing(s, scheme, calls12, allow_ai=ai, runner=runner)
        shadow = {**s, "kind": "subsidiary_listing", "facts": dict(s["facts"]),
                  "stage_dates": dict(s.get("stage_dates") or {}), "confidence": ("probable", "")}
        if SO.resolve_subsidiary_listing(shadow, res, today) == "partial":
            shadow["listing_resolution"] = res
            shadow["verdict"] = SO.verdict(shadow, s["checklist"])
            shadow["listing"] = SO.listing_status(shadow, s["judge"], today)
            if s["kind"] == "demerger" and (s["confidence"][0] == "confirmed"
                                             or str(s["facts"].get("record_date_source", "")).startswith("NSE")):
                # a confirmed (or register-recorded) demerger AND a partial
                # spin-off: it stays a demerger and is shown in the partial
                # table as well
                s["also_partial"] = {k: shadow[k] for k in ("symbol", "company", "kind", "facts", "stage", "listed_on",
                                                            "days_since_listing", "confidence", "verdict", "listing",
                                                            "listing_resolution", "family")}
            else:
                was = f"{s['kind']} / {s['confidence'][0]}"
                for k in ("kind", "facts", "stage", "listed_on", "days_since_listing", "confidence", "verdict", "family"):
                    s[k] = shadow[k]
                s["listing_resolution"] = res
                s["facts"]["previously_held_as"] = was
    # every PROBABLE or INDICATED demerger / scheme row is settled the same
    # way: a demerger in progress joins the confirmed demergers (last in that
    # list), a completed one goes to the dated 'completed' list, management's
    # own indication stays indicated, and anything else is discarded
    if s["kind"] in ("demerger", "scheme_other") and s["confidence"][0] in ("probable", "indicated") \
            and s["stage"] != "withdrawn":
        s["resolution"] = judge_resolution(s, scheme, calls12, allow_ai=ai, runner=runner)
        out = SO.resolve_probable(s, s["resolution"], today)
        if out == "subsidiary_ipo":
            res = judge_listing(s, scheme, calls12, allow_ai=ai, runner=runner)
            s["kind"], s["confidence"] = "subsidiary_listing", ("probable", "a subsidiary's listing is in motion")
            s["listing_resolution"] = res
            if SO.resolve_subsidiary_listing(s, res, today) == "unresolved":
                s["family"] = SO.family_of("subsidiary_listing")
        if out != "unresolved":
            s["verdict"] = SO.verdict(s, s["checklist"])
    s["listing"] = SO.listing_status(s, s["judge"], today)
    if list_only:
        if s["kind"] in SO.OFFERING_KINDS:
            s["confidence"] = ("offering", SO.family_of(s["kind"]))
            s["offering"] = {"status": "not assessed", "note": "list-only run"}
        return
    if s["kind"] in SO.OFFERING_KINDS:
        s["confidence"] = ("offering", SO.family_of(s["kind"]))
        s["offering"] = judge_offering(s, scheme_text_for(s, rows), allow_ai=ai, runner=runner)
        return
    if s["confidence"][0] not in ("confirmed", "probable"):
        if s["confidence"][0] == "indicated" and s["kind"] in SO.SPIN_KINDS:
            links = FN.doc_links(s["symbol"])["calls"]
            s["call_links"] = links
            s["call_exchanges"] = DL.call_exchanges(s["symbol"], today, 36, [], s["company"], links=links)
        return
    sym = s["symbol"]
    if fetch_docs:
        sys.path.insert(0, str(INDIA / "InvestorPresentations"))
        import fetch_presentations as FP                      # noqa: PLC0415
        try:
            FP.fetch_company(sym)
        except Exception as e:                                # noqa: BLE001
            print(f"  {sym}: document fetch failed ({e})", file=sys.stderr)
    s["docs"] = FN.doc_links(sym)
    s["call_links"] = s["docs"]["calls"]
    calls36 = calls_text_for(sym, 36, today)
    s["documents_read"]["calls_36m_chars"] = len(calls36)
    s["rationale_excerpts"] = FN.rationale_excerpts(sym, today=today)   # the links list
    s["rationale"] = judge_rationale(s, calls36, scheme, allow_ai=ai, runner=runner)
    s["parent_financials"] = FN.parent_financials(sym)
    s["cash_flows"] = FN.cash_flows(sym)
    s["pe"] = FN.pe_ratio(sym, live)
    # ---- the deal sheet: EVERY resulting / listed entity, with size, swap,
    # holdings, incentives and dates (one company can separate several)
    deal_text = deal_text_for(sym, today)
    s["documents_read"]["deal_filings_chars"] = len(deal_text)
    deal_docs = deal_text if len(deal_text) > len(scheme) / 2 else scheme
    # the exchange's cross-check: what began trading after the record date under the parent's name, or named in the filings
    s["nse_arrivals"] = (DL.arrivals(s["company"], sym, s["facts"]["record_date"], today, deal_docs)
                         if s["kind"] == "demerger" and s["facts"].get("record_date") and not s["facts"].get("is_the_spin") else [])
    s["deal"] = judge_deal(s, deal_docs, calls12, allow_ai=ai, runner=runner, arrivals=s["nse_arrivals"])
    s["history"] = full_history(s, today)
    s["entities"] = entities_for(s, today)
    s["uncovered_listings"] = uncovered_listings(s)
    spun = DL.separated(s["entities"])
    if fetch_docs:                       # a listed resulting company that is not on file: pull its statements
        for e in spun:
            if e.get("symbol") and e.get("listed_on"):
                DL.fetch_entity_statements(e["symbol"])
    names = [e["name"] for e in spun] + [str(e.get("business") or "") for e in spun]
    names += [s["facts"].get("resulting_company", ""), s["facts"].get("demerged_undertaking", "")]
    j = s["judge"] or {}
    for n in (j.get("demerged_business_names") or []):
        if isinstance(n, str):
            names.append(n)
    if isinstance(j.get("what_is_spun"), str):
        names.append(j["what_is_spun"])
    names = [n for n in dict.fromkeys(x.strip() for x in names if x) if len(n) > 3][:14]
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
    s["segment_tables"] = segment_tables(s["segments"])
    s["segment_table"] = next((x for x in s["segment_tables"] if x.get("available")), {})
    # ---- who holds what, how big the piece is, how the businesses differ
    holders = {sym: DL.shareholding(sym, fetch=fetch_docs)}
    own = {}
    for e in spun:
        if e.get("symbol"):
            holders[e["symbol"]] = DL.shareholding(e["symbol"], fetch=fetch_docs)
            fin = FN.parent_financials(e["symbol"], min_years=1)
            if fin.get("available"):
                own[e["symbol"]] = fin
    listed = sorted((e for e in spun if e.get("listed_on")), key=lambda e: e["listed_on"])
    if s["kind"] == "demerger" and listed and not s["facts"].get("is_the_spin"):
        names_ = "; ".join(f"{e['name']} ({e['symbol']}) since {e['listed_on']}" for e in listed)
        rd = f"; record date {s['facts']['record_date']}" if s["facts"].get("record_date") else ""
        pending = [e["name"] for e in spun if not e.get("listed_on")]
        s["listing"] = {**s["listing"], "state": "listed",
                        "short": (f"LISTED {listed[0]['listed_on']}: " + ", ".join(e["symbol"] for e in listed)
                                  if len({e["listed_on"] for e in listed}) == 1 else
                                  "LISTED: " + ", ".join(f"{e['symbol']} {e['listed_on']}" for e in listed)),
                        "text": f"LISTED — {names_} (NSE equity list){rd}"
                                + (f"; not yet listed: {', '.join(pending)}" if pending else "")}
    elif (s["kind"] == "demerger" and spun and not s["facts"].get("is_the_spin")
          and s["listing"].get("short", "").startswith("LISTED since ~") and SO.equity_list()[0]):
        # the record date has passed but the exchange's list has none of the new companies: say exactly that
        upto = max(SO.equity_list()[0].values())
        rd = s["facts"].get("record_date", "")
        s["listing"] = {**s["listing"], "short": f"RECORD DATE {rd}; listing awaited",
                        "text": f"RECORD DATE {rd} PASSED — {', '.join(e['name'] for e in spun)} not in NSE's equity list "
                                f"(complete to {upto}): the new shares are allotted but not yet trading"}
    s["shareholding"] = {k: v for k, v in holders.items() if v}
    s["entity_financials"] = own
    s["size"] = DL.size_view(s["entities"], s["parent_financials"], s["segment_tables"], sym,
                             DL.latest_mcaps(as_of=today), _members(),
                             size_statement=str((s.get("deal") or {}).get("size_statement") or ""))
    s["compare"] = DL.compare(sym, s["parent_financials"], s["entities"], s["segment_tables"])
    # ---- the calls, verbatim: every question and answer about it, oldest first
    s["call_exchanges"] = DL.call_exchanges(sym, today, 36, [e["name"] for e in spun], s["company"],
                                            links=s["call_links"])


def cmd_run(args, runner=None) -> dict:
    today = dt.date.fromisoformat(args.as_of) if getattr(args, "as_of", None) else dt.date.today()
    only = {s.strip().upper() for s in args.only.split(",") if s.strip()} or None
    if args.refresh:
        print("refreshing the last year of filings…", file=sys.stderr)
        FA.run(days=args.days, bse=not args.no_bse, pdf=True, only=only)
    if getattr(args, "out", None):
        set_out_dir(Path(args.out))
    # the window: filings dated within `days` of the as-of date and never
    # after it; a register record date (the exchange's own word) stays
    # whatever its age, as long as it is not in the future
    days = int(getattr(args, "days", 400) or 400)
    start = (today - dt.timedelta(days=days)).isoformat()
    rows = [r for r in SO.load_filings()
            if r["date"] <= today.isoformat() and (r["date"] >= start or r.get("source") == "NSE-register")]
    SO.set_register(Path(args.register) if getattr(args, "register", None) else None, today)
    members = FA.universe()
    if only:
        rows = [r for r in rows if r["symbol"] in only]
    list_only = bool(getattr(args, "list_only", False))
    if not args.no_calls:
        # the calls are a SOURCE of situations, not only colour on them
        links = {}
        for r in FA.read_csv(FN.LINKS):
            if r.get("transcript_url"):
                links.setdefault(r["symbol"], {})[r["label"]] = r["transcript_url"]
        syms = sorted(only) if only else sorted(members)
        call_rows = SO.concall_candidates(syms, members, today, links=links)
        print(f"  calls: {len(call_rows)} forward-looking mentions at "
              f"{len({r['symbol'] for r in call_rows})} companies join as situations", file=sys.stderr)
        rows = rows + call_rows
    live = SO.live_market()
    sits = SO.analyse(rows, today=today, with_calls=not args.no_calls, live=live)
    ai = (runner is not None) or (_ai_available() and not args.quick)
    workers = max(1, int(getattr(args, "workers", 1) or 1))

    def _one(s):
        enrich(s, rows, ai, today, live, fetch_docs=args.fetch_docs, runner=runner, list_only=list_only)
        if s["kind"] in SO.SPIN_KINDS:
            print(f"  {s['symbol']}: {s['confidence'][0]} / {s['stage']} — {s['listing']['state']}"
                  f" [{(s.get('judge') or {}).get('status')} / {(s.get('rationale') or {}).get('status', '-')}"
                  f" / {(s.get('segments') or {}).get('status', '-')}]", file=sys.stderr, flush=True)
        return s

    if workers > 1:
        with cf.ThreadPoolExecutor(max_workers=workers) as ex:
            list(ex.map(_one, sits))
    else:
        for s in sits:
            _one(s)
    sits.sort(key=lambda s: (s["kind"] not in SO.SPIN_KINDS, s["kind"] not in SO.OFFERING_KINDS,
                             SO.CONFIDENCE_ORDER.get(s["confidence"][0], 9),
                             -s["verdict"]["score"], s["symbol"]))
    # companies whose ONLY evidence is the calls
    filed = {s["symbol"] for s in sits if "CALLS" != "".join(s["sources"])}
    call_only = []
    for s in sits:
        if s["sources"] == ["CALLS"] and s["symbol"] not in filed:
            ms = s["concall_mentions"]
            fwd = [m for m in ms if m.get("tone") == "forward"]
            call_only.append({"symbol": s["symbol"], "n": len(ms), "forward": len(fwd) or s["n_filings"],
                              "latest": s["latest_filing"][:7], "example": s["headlines"][-1]["headline"],
                              "mentions": ms, "kind": s["kind"]})
    dates = [r["date"] for r in rows] or [today.isoformat()]
    meta = {"run_date": today.isoformat(), "window_from": min(dates), "window_to": max(dates),
            "filings": len(rows), "companies": len({r["symbol"] for r in rows}), "universe": len(members),
            "judge": (f"{MODEL} read the schemes, three years of calls and the segment pages" if ai else
                      "not run (--quick or no CLI); mechanical read only")}
    record = {"meta": meta, "situations": sits, "call_only": call_only}
    # the record first: a fault in rendering must never cost the run (render can be re-run)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LATEST.write_text(json.dumps(record, indent=1, default=str))
    md = render_report(record, rows_index(rows))
    REPORT.write_text(md)
    write_company_files(record)
    srows = situation_rows(sits)
    FA.write_csv(SITUATIONS, srows, list(srows[0].keys()) if srows else ["symbol"])
    crows = coverage_rows(sits)
    FA.write_csv(COVERAGE, crows, list(crows[0].keys()) if crows else ["symbol"])
    orows = offering_rows(sits)
    FA.write_csv(OFFERINGS, orows, list(orows[0].keys()) if orows else ["symbol"])
    mrows = [{"symbol": s["symbol"], **mm} for s in sits for mm in s["concall_mentions"]]
    mrows += [{"symbol": c["symbol"], **mm} for c in call_only for mm in c["mentions"]]
    FA.write_csv(MENTIONS, mrows, ["symbol", "call", "term", "tone", "quote"])
    snap = HISTORY / today.isoformat()
    snap.mkdir(parents=True, exist_ok=True)
    for p in (REPORT, SITUATIONS, MENTIONS, COVERAGE, OFFERINGS):
        if p.exists():
            shutil.copy(p, snap / p.name)
    (snap / "run.json").write_text(json.dumps(record, indent=1, default=str))
    n_conf = sum(1 for s in sits if s.get("confidence", ("",))[0] == "confirmed" and s["kind"] != "subsidiary_listing")
    n_part = sum(1 for s in sits if (s.get("confidence", ("",))[0] == "confirmed" and s["kind"] == "subsidiary_listing")
                 or s.get("also_partial"))
    print(f"wrote {REPORT} ({len(md.splitlines())} lines); {len(sits)} situations, "
          f"{n_conf} confirmed demergers, {n_part} partial spin-offs, "
          f"{sum(1 for s in sits if s.get('confidence', ('',))[0] == 'completed')} completed, "
          f"{sum(1 for s in sits if s.get('confidence', ('',))[0] == 'probable')} probable, "
          f"{len(call_only)} call-only indications", file=sys.stderr)
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


def write_company_files(record: dict) -> int:
    """One file per company under <out>/companies/: the complete nine-part
    analysis with EVERY call exchange verbatim (the main report links here
    for part 6). Written for every company the report writes up."""
    folder = OUT_DIR / "companies"
    folder.mkdir(parents=True, exist_ok=True)
    m = record["meta"]
    n = 0
    seen = set()
    for s in record["situations"]:
        conf = s.get("confidence", ("",))[0]
        if s["kind"] not in SO.SPIN_KINDS or conf not in ("confirmed", "probable", "indicated") or s["symbol"] in seen:
            continue
        seen.add(s["symbol"])
        body = [f"*Run {m['run_date']} · part of [SPINOFF_REPORT.md](../SPINOFF_REPORT.md) · "
                f"the complete analysis of one company, with every management-call exchange in full.*", ""]
        body += render_company(s, heavy=(conf != "indicated"), verbatim=True)
        if s.get("also_partial"):
            ap = s["also_partial"]
            body += ["---", "", f"*{s['company']} also has a partial spin-off on file: "
                     f"{ap['facts'].get('subsidiary', '')} — {ap['listing']['text']}*", ""]
        (folder / f"{s['symbol'].replace('&', '_')}.md").write_text("\n".join(body))
        n += 1
    return n


def cmd_render(args) -> None:
    """Re-render the report from the saved run (spinoff_latest.json) — a
    presentation change needs no re-judging."""
    record = json.loads(LATEST.read_text())
    # re-derive what is derived: a saved subsidiary-listing answer is applied
    # again, so a change to how answers are applied needs no re-judging
    as_of = dt.date.fromisoformat(record["meta"]["run_date"])
    for s in record["situations"]:
        res = s.get("listing_resolution")
        if s.get("kind") == "subsidiary_listing" and isinstance(res, dict) and res.get("status") in ("judged", "cached"):
            if SO.resolve_subsidiary_listing(s, res, as_of) != "unresolved":
                s["confidence"] = tuple(s["confidence"])
                s["verdict"] = SO.verdict(s, s.get("checklist") or [])
                s["listing"] = SO.listing_status(s, s.get("judge") or {}, as_of)
    for s in record["situations"]:
        res = s.get("resolution")
        if s.get("kind") in ("demerger", "scheme_other") and isinstance(res, dict) and res.get("status") in ("judged", "cached") \
                and (s.get("facts") or {}).get("resolution") not in (None, "subsidiary_ipo"):
            if SO.resolve_probable(s, res, as_of) not in ("unresolved", "subsidiary_ipo"):
                s["confidence"] = tuple(s["confidence"])
                s["verdict"] = SO.verdict(s, s.get("checklist") or [])
                s["listing"] = SO.listing_status(s, s.get("judge") or {}, as_of)
    LATEST.write_text(json.dumps(record, indent=1, default=str))
    srows = situation_rows(record["situations"])
    FA.write_csv(SITUATIONS, srows, list(srows[0].keys()) if srows else ["symbol"])
    md = render_report(record, rows_index(SO.load_filings()))
    REPORT.write_text(md)
    write_company_files(record)
    snap = HISTORY / record["meta"]["run_date"]
    if snap.exists():
        shutil.copy(REPORT, snap / REPORT.name)
    print(f"re-rendered {REPORT} ({len(md.splitlines())} lines) from the run of {record['meta']['run_date']}",
          file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("render", help="re-render the report from the saved run, no judge")
    r = sub.add_parser("run")
    r.add_argument("--refresh", action="store_true", help="re-pull the filings first")
    r.add_argument("--fetch-docs", action="store_true",
                   help="pull annual reports and presentations for the highlighted companies")
    r.add_argument("--days", type=int, default=400,
                   help="filings window: this many days before the as-of date (register record dates always join)")
    r.add_argument("--out", default=None, help="write outputs under this folder (a backtest keeps its own)")
    r.add_argument("--register", default=None, help="the demerger register CSV to consult (default: production)")
    r.add_argument("--list-only", dest="list_only", action="store_true",
                   help="judge classification and listing only — no rationale, numbers, documents or offerings")
    r.add_argument("--no-bse", action="store_true")
    r.add_argument("--quick", action="store_true", help="no AI judge")
    r.add_argument("--no-calls", action="store_true", help="skip the conference-call scan")
    r.add_argument("--only", default="")
    r.add_argument("--workers", type=int, default=1,
                   help="judge several situations at once (the cache is locked)")
    r.add_argument("--as-of", dest="as_of", default=None,
                   help="judge stages and timing as of this date (YYYY-MM-DD)")
    c = sub.add_parser("company")
    c.add_argument("symbol")
    c.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    {"run": cmd_run, "company": cmd_company, "render": cmd_render}[args.cmd](args)


if __name__ == "__main__":
    main()
