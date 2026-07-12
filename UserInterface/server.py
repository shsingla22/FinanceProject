"""
server.py — DYNAMIC mode for the Business Quality Analyst.

Runs the BusinessAnalysis skill LIVE at request time over the repository's
stored data (balance sheets, P&L, cash flow, working capital, market data,
management history, concall transcripts). Nothing is pre-baked: edit a CSV,
hit refresh, ask again — the answer changes.

    uvicorn server:app --host 0.0.0.0 --port 8000       (from UserInterface/)

Endpoints
  GET  /api/health              mode + whether AI qualitative analysis is on
  GET  /api/framework           the 34-parameter taxonomy (from the skill)
  GET  /api/companies           all records (lazy-computed, mtime-invalidated)
  GET  /api/company/{sym}       ONE record recomputed fresh right now,
                                plus an excerpt of the latest concall
  GET  /api/concall/{sym}       extracted transcript text (on-demand PDF parse)
  POST /api/qualitative/{sym}   run the skill's qualitative playbook through
                                the Claude API over the concall text
                                (requires ANTHROPIC_API_KEY in the env)
  POST /api/refresh             drop all caches (after refreshing CSVs)

The static frontend is served from this same process at / .
"""

from __future__ import annotations

import io
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.request
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
INDIA = REPO / "IndividualStockAnalysis" / "India"
SKILL = INDIA / "Skills" / "BusinessAnalysis"
UNIVERSE = "NiftyTotalMarket"

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(SKILL / "scripts"))

import build_data as B          # noqa: E402  (reuses the skill wiring + scoring)
import quant_signals as Q       # noqa: E402
import scoring as S             # noqa: E402
import framework as F           # noqa: E402
import pandas as pd             # noqa: E402

app = FastAPI(title="Business Quality Analyst API")

_lock = threading.Lock()
_cache: dict = {"companies": None, "stamp": None, "concall_text": {}}

# Qualitative (AI) scores are expensive — one Claude call per company — so
# they persist to disk keyed by the concall PDF's mtime. A company's call is
# analysed ONCE per transcript refresh, then served from cache.
QUAL_CACHE_FILE = HERE / ".qual_cache.json"
_qual_lock = threading.Lock()
try:
    _qual_cache: dict = json.loads(QUAL_CACHE_FILE.read_text())
except Exception:
    _qual_cache = {}


def _save_qual_cache():
    try:
        QUAL_CACHE_FILE.write_text(json.dumps(_qual_cache))
    except Exception:
        pass

WATCHED = [
    INDIA / "BalanceSheet" / UNIVERSE / "_all_balance_sheets_long.csv",
    INDIA / "ProfitStatement" / UNIVERSE / "_all_profit_loss_long.csv",
    INDIA / "CashFlow" / UNIVERSE / "_all_cash_flow_long.csv",
    INDIA / "WorkingCapital" / UNIVERSE / "_all_working_capital_long.csv",
    INDIA / "StockInfo" / "Nifty500" / "live_market_data.csv",
]


def _data_stamp() -> tuple:
    return tuple(p.stat().st_mtime if p.exists() else 0 for p in WATCHED)


def _drop_caches():
    _cache["companies"] = None
    _cache["stamp"] = None
    _cache["concall_text"] = {}
    B._load_cache.clear()          # the skill's CSV cache
    Q.load_statement.__wrapped__ if hasattr(Q.load_statement, "__wrapped__") else None


_fw = F.load_framework()
_fw_json = {
    "version": _fw.version,
    "modules": [{"id": m.id, "order": m.order, "name": m.name,
                 "guidance": m.guidance} for m in _fw.modules],
    "parameters": [{"id": p.id, "module": p.module, "name": p.name,
                    "nature": p.nature, "signal": p.signal,
                    "direction": p.direction,
                    "description": " ".join(p.description.split()),
                    "cautions": p.cautions} for p in _fw.parameters],
}
_module_ids = [m.id for m in _fw.modules]

_const = pd.read_csv(INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv")
_const_map = {str(r.nse_symbol): {"name": r.company_name,
                                  "industry": (r.industry if isinstance(r.industry, str) else "") or ""}
              for r in _const.itertuples()}


def _live_map():
    live = pd.read_csv(INDIA / "StockInfo" / "Nifty500" / "live_market_data.csv")
    return live.set_index("nse_symbol").to_dict("index")


def _cc_counts():
    path = INDIA / "ConferenceCalls" / UNIVERSE / "_fetch_log.csv"
    out = {}
    if path.exists():
        for _, r in pd.read_csv(path).iterrows():
            s = str(r["status"])
            n = 0
            if s.startswith("ok"):
                for part in s.split(":"):
                    if part.startswith("text_ok="):
                        n = int(part.split("=")[1])
            out[r["nse_symbol"]] = n
    return out


def _mgmt(sym: str):
    f = INDIA / "ManagementInfo" / UNIVERSE / f"{sym.replace('&', '_AND_')}.csv"
    if not f.exists():
        return []
    try:
        mdf = pd.read_csv(f)
        cur = mdf[mdf["status"] == "current"]
        return [{"role": r["role"], "name": r["name"]}
                for _, r in cur.head(6).iterrows()]
    except Exception:
        return []


def _mgmt_history(sym: str) -> list:
    """Full 5-year management history (current AND exited) from the ARs —
    the raw material for judging stability / churn of the leadership team."""
    f = INDIA / "ManagementInfo" / UNIVERSE / f"{sym.replace('&', '_AND_')}.csv"
    if not f.exists():
        return []
    try:
        mdf = pd.read_csv(f)
        return [{"role": r["role"], "name": r["name"],
                 "years": r.get("years_present", ""),
                 "status": r["status"]}
                for _, r in mdf.head(20).iterrows()]
    except Exception:
        return []


CALL_HEADER_RE = re.compile(r"Call:\s+([A-Z][a-z]{2}\s+\d{4})")


def concall_timeline(sym: str, budget: int = 30000) -> dict:
    """Split the merged transcript (oldest->newest, one 'Call: MMM YYYY'
    header per quarter) into per-call segments and sample ACROSS the
    timeline — earliest, middle, and the two latest calls — so judgement
    covers the full 3-year record (promises vs delivery, consistency),
    not just the latest quarter."""
    full = concall_text(sym, max_chars=10**9)   # full cached extract
    if not full:
        return {"excerpt": "", "n_calls": 0, "from": "", "to": ""}
    parts = CALL_HEADER_RE.split(full)
    # parts = [preamble, date1, text1, date2, text2, ...]
    calls = [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]
    if not calls:
        return {"excerpt": full[-budget:], "n_calls": 1, "from": "", "to": ""}
    n = len(calls)
    picks = []
    seen = set()
    for idx, share in [(0, 0.18), (n // 2, 0.18), (max(0, n - 2), 0.24), (n - 1, 0.40)]:
        if idx in seen:
            continue
        seen.add(idx)
        date, text = calls[idx]
        take = int(budget * share)
        picks.append(f"===== CALL {idx + 1} of {n} ({date}) =====\n{text.strip()[:take]}")
    return {"excerpt": "\n\n".join(picks), "n_calls": n,
            "from": calls[0][0], "to": calls[-1][0]}


def build_record(sym: str, live, ccm, qual_scores: list | None = None) -> dict:
    """Run the skill for one symbol, right now.

    If qual_scores (from the AI concall pass) is provided, FUSE them with the
    quantitative scores per the skill's hybrid rule: pure-qualitative params
    take the AI score; hybrid params that have both take the rounded mean,
    with both rationales kept. Coverage and module/overall aggregation are
    then recomputed over the fused set.
    """
    sig = Q.compute(sym, base=INDIA, universe=UNIVERSE)
    pscores = B.score_params(sig, _fw)

    param_meta = {}   # extra per-param info for the UI (source, quote)
    if qual_scores:
        by_id = {p.id: p for p in pscores}
        ai = {s["id"]: s for s in qual_scores
              if s.get("id") in {p.id for p in _fw.parameters}}
        for pid, s in ai.items():
            if s.get("score") is None:
                continue
            a = int(max(-2, min(2, s["score"])))
            tgt = by_id.get(pid)
            if tgt is not None and tgt.score is not None:
                # hybrid with both signals: fuse, keep both stories
                fused = round((tgt.score + a) / 2)
                tgt.rationale = (f"{tgt.rationale} | Concall: "
                                 f"{s.get('rationale', '')}")
                tgt.score = int(max(-2, min(2, fused)))
                param_meta[pid] = {"source": "fused", "quote": s.get("quote", "")}
            elif tgt is not None:
                tgt.score = a
                tgt.rationale = f"From concall: {s.get('rationale', '')}"
                param_meta[pid] = {"source": "ai_concall", "quote": s.get("quote", "")}
        agg = S.aggregate(pscores, _module_ids)
    else:
        agg = S.aggregate(pscores, _module_ids)

    meta = _const_map.get(sym, {"name": sym, "industry": ""})
    lv = live.get(sym, {})

    # Explanation trace: show exactly how the overall number was computed,
    # from the stored module scores and weights — no black box.
    terms = []
    for m in _module_ids:
        ms = agg["modules"][m]["module_score"]
        if ms is not None:
            w = S.DEFAULT_MODULE_WEIGHTS.get(m, 1.0)
            terms.append(f"{m} {ms:+.2f}×{w}")
    overall_calc = (
        "overall = weighted mean of assessed module scores: (" +
        " + ".join(terms) + ") / Σweights" +
        (f" = {agg['overall_score']:+.2f}" if agg["overall_score"] is not None else "")
        if terms else "no modules assessed")

    return B.clean({
        "name": meta["name"], "industry": meta["industry"],
        "mcap": lv.get("market_cap_rs_cr"), "pe": lv.get("stock_pe"),
        "price": lv.get("current_price_rs"),
        "overall": agg["overall_score"], "coverage": agg["overall_coverage"],
        "modules": {m: {"score": agg["modules"][m]["module_score"],
                        "assessed": agg["modules"][m]["n_assessed"],
                        "total": agg["modules"][m]["n_total"],
                        "weight": S.DEFAULT_MODULE_WEIGHTS.get(m, 1.0)}
                    for m in _module_ids},
        "params": {p.id: {"score": p.score, "rationale": p.rationale,
                          "nature": p.nature,
                          **param_meta.get(p.id, {})}
                   for p in pscores if p.score is not None},
        "series": B.series_for_chart(sig),
        "mgmt": _mgmt(sym),
        "mgmt_history": _mgmt_history(sym),
        "concalls": ccm.get(sym, 0),
        "computed_live": True,
        "qualitative_included": bool(qual_scores),
        "overall_calc": overall_calc,
    })


def concall_text(sym: str, max_chars: int = 8000) -> str:
    """Extract the tail (latest calls) of the merged transcript PDF, cached."""
    if sym in _cache["concall_text"]:
        return _cache["concall_text"][sym][-max_chars:]
    pdf = INDIA / "ConferenceCalls" / UNIVERSE / f"{sym.replace('&', '_AND_')}.pdf"
    if not pdf.exists():
        return ""
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(str(pdf), strict=False)
        # Extract the WHOLE merged transcript (all quarterly calls,
        # oldest-first) — cached, so the PDF is parsed once per process.
        parts = []
        for page in reader.pages:
            try:
                parts.append(page.extract_text() or "")
            except Exception:
                parts.append("")
        text = "\n".join(parts)
    except Exception:
        text = ""
    _cache["concall_text"][sym] = text
    return text[-max_chars:]


def _ai_backend() -> str | None:
    """Two ways to run the qualitative playbook:
      'api'             ANTHROPIC_API_KEY set -> direct Claude API call
      'claude_code_cli' Claude Code CLI on PATH, logged in with the user's
                        own subscription -> headless `claude -p` call.
                        PERSONAL USE ONLY: a subscription must not serve
                        third parties, so keep the port private in this mode.
    """
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "api"
    if shutil.which("claude"):
        return "claude_code_cli"
    return None


# ----------------------------------------------------------------- endpoints
@app.get("/api/health")
def health():
    backend = _ai_backend()
    return {"mode": "dynamic", "universe": UNIVERSE,
            "framework_version": _fw.version,
            "ai_qualitative": backend is not None,
            "ai_backend": backend,
            "data_stamp": _data_stamp()}


@app.get("/api/framework")
def framework():
    return _fw_json


@app.get("/api/companies")
def companies():
    with _lock:
        stamp = _data_stamp()
        if _cache["companies"] is None or _cache["stamp"] != stamp:
            t0 = time.time()
            live, ccm = _live_map(), _cc_counts()
            recs = {}
            for sym in _const_map:
                try:
                    recs[sym] = build_record(sym, live, ccm)
                except Exception:
                    continue
            _cache["companies"] = recs
            _cache["stamp"] = stamp
            print(f"[dynamic] recomputed {len(recs)} companies "
                  f"in {time.time() - t0:.1f}s")
        return {"universe": UNIVERSE, "framework_version": _fw.version,
                "n": len(_cache["companies"]),
                "companies": _cache["companies"]}


def _qual_scores_cached(sym: str) -> tuple[list | None, str]:
    """AI concall+management scores for sym, cached on disk keyed by the PDF
    mtime AND the prompt version. Returns (scores | None, status)."""
    pdf = INDIA / "ConferenceCalls" / UNIVERSE / f"{sym.replace('&', '_AND_')}.pdf"
    if not pdf.exists():
        return None, "no_concalls"
    stamp = f"{pdf.stat().st_mtime}:v{QUAL_PROMPT_VERSION}"
    with _qual_lock:
        hit = _qual_cache.get(sym)
        if hit and hit.get("stamp") == stamp:
            return hit["scores"], "cached"
    backend = _ai_backend()
    if backend is None:
        return None, "ai_unavailable"
    timeline = concall_timeline(sym)
    if not timeline["excerpt"]:
        return None, "no_extractable_text"
    prompt = _qual_prompt(sym, timeline, _mgmt_history(sym))
    if backend == "api":
        scores = _qual_via_api(sym, prompt, os.environ["ANTHROPIC_API_KEY"])["scores"]
    else:
        scores = _qual_via_claude_code(sym, prompt)["scores"]
    with _qual_lock:
        _qual_cache[sym] = {"stamp": stamp, "scores": scores}
        _save_qual_cache()
    return scores, backend


@app.get("/api/company/{sym}")
def company(sym: str, quick: int = 0):
    """The COMPLETE analysis: quantitative signals recomputed now, PLUS the
    qualitative playbook over the latest concall (AI, cached per transcript).
    Pass ?quick=1 to skip the qualitative pass."""
    sym = sym.upper()
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")
    qual, qstatus = (None, "skipped_quick") if quick else _qual_scores_cached(sym)
    rec = build_record(sym, _live_map(), _cc_counts(), qual_scores=qual)
    rec["concall_excerpt"] = concall_text(sym, 1600)
    rec["qualitative_status"] = qstatus
    tl = concall_timeline(sym, budget=4)
    rec["concall_range"] = {"n_calls": tl["n_calls"], "from": tl["from"], "to": tl["to"]}
    return {"symbol": sym, "record": rec}


@app.get("/api/concall/{sym}")
def concall(sym: str, chars: int = 8000):
    sym = sym.upper()
    text = concall_text(sym, max(500, min(chars, 20000)))
    if not text:
        raise HTTPException(404, f"no concall transcript on file for {sym}")
    return {"symbol": sym, "chars": len(text), "text": text}


QUAL_PROMPT_VERSION = 2   # bump when the prompt changes -> invalidates qual cache


def _qual_prompt(sym: str, timeline: dict, mgmt_hist: list) -> str:
    qual_params = [p for p in _fw_json["parameters"]
                   if p["nature"] in ("qualitative", "hybrid")]
    plist = "\n".join(f'- {p["id"]}: {p["name"]} — {p["signal"]}'
                      for p in qual_params)
    mgmt_lines = "\n".join(
        f'- {m["role"]}: {m["name"]} ({m["years"] or "?"}, {m["status"]})'
        for m in mgmt_hist) or "(no management history on file)"
    return (
        "You are scoring a company against a quality-investing framework.\n\n"
        "EVIDENCE 1 — CONFERENCE-CALL TIMELINE: excerpts sampled across "
        f"{timeline['n_calls']} quarterly calls from {timeline['from']} to "
        f"{timeline['to']} (oldest first). Judge the TRAJECTORY, not one "
        "quarter: did management deliver what it promised in earlier calls? "
        "Is the narrative consistent over the years, or does it shift every "
        "quarter? Are earlier-announced capex/product plans confirmed as "
        "executed in later calls?\n\n"
        "EVIDENCE 2 — MANAGEMENT HISTORY (from 5 years of annual reports): "
        "use tenure and churn as track-record evidence. Long-tenured "
        "Chairman/MD/CFO across the window = stability; CFO churn or "
        "revolving leadership = a governance flag. Weigh this especially "
        "for the MGT.* parameters.\n\n"
        f"Parameters (score each -2..+2, or null if the evidence is silent — never guess):\n{plist}\n\n"
        "Return STRICT JSON only: {\"scores\": [{\"id\": ..., \"score\": int|null, "
        "\"rationale\": \"1 sentence citing the calls or the management record\", "
        "\"quote\": \"short verbatim quote or empty\"}]}\n\n"
        f"MANAGEMENT HISTORY ({sym}):\n{mgmt_lines}\n\n"
        f"CONFERENCE-CALL TIMELINE EXCERPTS ({sym}):\n{timeline['excerpt']}"
    )


def _parse_scores(raw: str) -> list:
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        raise HTTPException(502, "could not parse model output")
    blob = m.group(0)
    try:
        return json.loads(blob).get("scores", [])
    except json.JSONDecodeError:
        # Salvage pass: model JSON occasionally breaks on an unescaped quote
        # inside a rationale. Recover the per-parameter objects individually
        # and drop only the broken ones.
        out = []
        for item in re.findall(r'\{[^{}]*"id"\s*:\s*"[^"]+"[^{}]*\}', blob):
            try:
                out.append(json.loads(item))
            except json.JSONDecodeError:
                continue
        if out:
            return out
        raise HTTPException(502, "model output was not valid JSON")


def _qual_via_api(sym: str, prompt: str, key: str) -> dict:
    body = json.dumps({
        "model": "claude-sonnet-5",
        "max_tokens": 3000,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=body,
        headers={"content-type": "application/json",
                 "x-api-key": key, "anthropic-version": "2023-06-01"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            out = json.loads(resp.read())
    except Exception as e:
        raise HTTPException(502, f"Claude API error: {e}")
    raw = "".join(b.get("text", "") for b in out.get("content", []))
    return {"symbol": sym, "model": out.get("model"),
            "backend": "api", "scores": _parse_scores(raw)}


def _qual_via_claude_code(sym: str, prompt: str) -> dict:
    """Headless Claude Code (`claude -p`) authenticated by the user's OWN
    subscription. Personal-use path: the person running the server is the
    person whose subscription pays — do not expose publicly in this mode."""
    try:
        proc = subprocess.run(
            ["claude", "-p", "--model", "sonnet"],
            input=prompt,
            capture_output=True, text=True, timeout=300,
        )
    except FileNotFoundError:
        raise HTTPException(503, "claude CLI not found on PATH")
    except subprocess.TimeoutExpired:
        raise HTTPException(504, "claude CLI timed out")
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "").strip()[-400:]
        raise HTTPException(
            502, f"claude CLI failed (is it logged in? run `claude` once "
                 f"to authenticate): {tail}")
    return {"symbol": sym, "model": "claude-code (subscription)",
            "backend": "claude_code_cli",
            "scores": _parse_scores(proc.stdout)}


@app.post("/api/qualitative/{sym}")
def qualitative(sym: str):
    """Raw AI scores (concall timeline + management history), cache-aware."""
    sym = sym.upper()
    scores, status = _qual_scores_cached(sym)
    if scores is None:
        raise HTTPException(503 if status == "ai_unavailable" else 404,
                            f"qualitative unavailable: {status}")
    return {"symbol": sym, "status": status, "scores": scores}


@app.post("/api/ask/{sym}")
def ask(sym: str, payload: dict):
    """Q&A grounded in the STORED verdict: the question is answered from the
    persisted analysis record (scores + rationales + quotes) plus the concall
    timeline — never from thin air. The explainability pattern: answer from
    the trace, cite the parameter or quote, admit when the record is silent."""
    backend = _ai_backend()
    if backend is None:
        raise HTTPException(503, "AI is off — log in the Claude Code CLI or set ANTHROPIC_API_KEY")
    sym = sym.upper()
    question = (payload or {}).get("question", "").strip()
    if not question:
        raise HTTPException(422, "missing 'question'")
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")

    qual, _ = _qual_scores_cached(sym)          # cached in the normal case
    rec = build_record(sym, _live_map(), _cc_counts(), qual_scores=qual)
    timeline = concall_timeline(sym, budget=12000)
    record_json = json.dumps({k: rec[k] for k in
                              ("name", "overall", "coverage", "modules",
                               "params", "series", "mgmt")}, default=str)[:14000]
    prompt = (
        f"You are explaining an investment-quality verdict for {rec['name']} "
        f"({sym}). Answer the user's question USING ONLY the stored analysis "
        "record and the concall excerpts below. Rules: cite the specific "
        "parameter names, numbers, or verbatim quotes you rely on; if the "
        "record and excerpts don't contain the answer, say so plainly — "
        "never invent. Be concise (<= 200 words).\n\n"
        f"QUESTION: {question}\n\n"
        f"STORED ANALYSIS RECORD (scores are -2..+2):\n{record_json}\n\n"
        f"CONCALL EXCERPTS ({timeline['n_calls']} calls, "
        f"{timeline['from']}–{timeline['to']}):\n{timeline['excerpt'][:8000]}"
    )
    if backend == "api":
        body = json.dumps({"model": "claude-sonnet-5", "max_tokens": 700,
                           "messages": [{"role": "user", "content": prompt}]}).encode()
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages", data=body,
            headers={"content-type": "application/json",
                     "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                     "anthropic-version": "2023-06-01"})
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                out = json.loads(resp.read())
            answer = "".join(b.get("text", "") for b in out.get("content", []))
        except Exception as e:
            raise HTTPException(502, f"Claude API error: {e}")
    else:
        try:
            proc = subprocess.run(["claude", "-p", "--model", "sonnet"],
                                  input=prompt, capture_output=True,
                                  text=True, timeout=300)
        except subprocess.TimeoutExpired:
            raise HTTPException(504, "claude CLI timed out")
        if proc.returncode != 0:
            raise HTTPException(502, "claude CLI failed: " +
                                (proc.stderr or "")[-300:])
        answer = proc.stdout.strip()
    return {"symbol": sym, "question": question, "answer": answer}


@app.post("/api/refresh")
def refresh():
    with _lock:
        _drop_caches()
    return {"ok": True, "message": "caches dropped; next request recomputes"}


@app.on_event("startup")
def warm_cache():
    """Compute the 742-company cache in the background at startup so the
    first visitor doesn't wait ~30s. The client also handles the cold
    window gracefully, but warm-by-default is the better experience."""
    threading.Thread(target=lambda: companies(), daemon=True).start()


# static frontend last, so /api/* wins
app.mount("/", StaticFiles(directory=str(HERE), html=True), name="ui")
