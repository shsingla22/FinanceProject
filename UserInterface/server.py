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
import rating as R              # noqa: E402  (MultibaggerPattern + QualityRisks + rating)

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
MIN_CALL_CHARS = 800          # skip scanned/empty call sections when sampling


def split_calls(sym: str) -> list:
    """[(date, text), ...] oldest-first, dropping unextractable sections."""
    full = concall_text(sym, max_chars=10**9)
    if not full:
        return []
    parts = CALL_HEADER_RE.split(full)
    calls = [(parts[i], parts[i + 1].strip())
             for i in range(1, len(parts) - 1, 2)]
    calls = [(d, t) for d, t in calls if len(t) >= MIN_CALL_CHARS]
    if not calls and full.strip():
        calls = [("(undated)", full.strip())]
    return calls


def sample_calls(calls: list, indices: list, per_call: int) -> str:
    n = len(calls)
    picks = []
    for idx in indices:
        if 0 <= idx < n:
            date, text = calls[idx]
            picks.append(f"===== CALL {idx + 1} of {n} ({date}) =====\n{text[:per_call]}")
    return "\n\n".join(picks)


def spread_indices(n: int, k: int, exclude: set) -> list:
    """k indices spread across [0, n) — always trying to include the first,
    a middle, and the latest calls — skipping already-used ones."""
    if n == 0:
        return []
    order = [n - 1, 0, n // 2, n - 2, n // 3, 2 * n // 3, n - 3, 1]
    out = []
    for i in order + list(range(n)):
        if i >= 0 and i < n and i not in exclude and i not in out:
            out.append(i)
        if len(out) >= k:
            break
    return out


def concall_timeline(sym: str, budget: int = 30000) -> dict:
    """Back-compat summary view of the timeline (used by Q&A and the
    company header)."""
    calls = split_calls(sym)
    if not calls:
        return {"excerpt": "", "n_calls": 0, "from": "", "to": ""}
    n = len(calls)
    idx = spread_indices(n, 4, set())
    per_call = max(1, budget // max(1, len(idx)))
    return {"excerpt": sample_calls(calls, sorted(idx), per_call),
            "n_calls": n, "from": calls[0][0], "to": calls[-1][0]}


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

    # Readers shouldn't need analyst shorthand: rewrite YoY/QoQ/etc. in the
    # rationales to everyday words (verbatim call quotes stay untouched).
    for p in pscores:
        if p.rationale:
            p.rationale = R._plain(p.rationale)

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


# Analysis model: Opus 5 by default (per user: quality over speed).
# Override with ANALYSIS_MODEL env var — it steers ALL judges at once (the
# 34-check framework, the multibagger judge and the risk judge, via
# rating.py). No timeouts on analysis calls — the user explicitly prefers a
# slow, top-notch analysis over a fast one.
ANALYSIS_MODEL = os.environ.get("ANALYSIS_MODEL", "claude-opus-5")
API_MODEL_MAP = {"opus": "claude-opus-5", "sonnet": "claude-sonnet-5"}
API_MODEL = API_MODEL_MAP.get(ANALYSIS_MODEL, ANALYSIS_MODEL)
HTTP_AI_TIMEOUT = 3600            # effectively unlimited for one HTTP call


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
            "analysis_model": ANALYSIS_MODEL,
            "skills": ["BusinessAnalysis", "MultibaggerPattern",
                       "QualityRisks"],
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


MAX_QUAL_PASSES = 3
CALLS_PER_PASS = 5
CHARS_PER_CALL = 22000     # ~5 calls x 22k = ~110k chars (~28k tokens) per pass


def _run_qual(sym: str, prompt: str, backend: str) -> list:
    if backend == "api":
        return _qual_via_api(sym, prompt, os.environ["ANTHROPIC_API_KEY"])["scores"]
    return _qual_via_claude_code(sym, prompt)["scores"]


def _qual_scores_cached(sym: str) -> tuple[list | None, str]:
    """AI concall+management scores, cached on disk keyed by PDF mtime, the
    prompt version AND the model.

    COVERAGE LOOP: pass 1 scores all qual/hybrid parameters from ~5 calls
    sampled across the timeline. Parameters still null then get further
    passes with FRESH calls (ones not yet shown), targeting only the gaps.
    Coverage rises by adding evidence — the never-guess rule is unchanged;
    the loop stops when no nulls remain, no fresh calls remain, or a pass
    adds nothing."""
    pdf = INDIA / "ConferenceCalls" / UNIVERSE / f"{sym.replace('&', '_AND_')}.pdf"
    if not pdf.exists():
        return None, "no_concalls"
    stamp = f"{pdf.stat().st_mtime}:v{QUAL_PROMPT_VERSION}:{ANALYSIS_MODEL}"
    with _qual_lock:
        hit = _qual_cache.get(sym)
        if hit and hit.get("stamp") == stamp:
            return hit["scores"], "cached"
    backend = _ai_backend()
    if backend is None:
        return None, "ai_unavailable"
    calls = split_calls(sym)
    if not calls:
        return None, "no_extractable_text"
    n = len(calls)
    date_range = f"{calls[0][0]} to {calls[-1][0]}"
    mgmt_hist = _mgmt_history(sym)
    qual_ids = [p["id"] for p in _fw_json["parameters"]
                if p["nature"] in ("qualitative", "hybrid")]

    merged: dict = {}
    used: set = set()
    for pass_no in range(1, MAX_QUAL_PASSES + 1):
        remaining = [pid for pid in qual_ids
                     if merged.get(pid, {}).get("score") is None]
        fresh = spread_indices(n, CALLS_PER_PASS, used)
        if not remaining or not fresh:
            break
        used.update(fresh)
        excerpt = sample_calls(calls, sorted(fresh), CHARS_PER_CALL)
        prompt = _qual_prompt(sym, excerpt, n, date_range, mgmt_hist,
                              param_ids=None if pass_no == 1 else remaining,
                              pass_no=pass_no)
        try:
            scores = _run_qual(sym, prompt, backend)
        except HTTPException:
            if merged:            # keep what earlier passes earned
                break
            raise
        gained = 0
        for s in scores:
            pid = s.get("id")
            if pid not in qual_ids:
                continue
            prev = merged.get(pid)
            if s.get("score") is not None and (prev is None or prev.get("score") is None):
                merged[pid] = s
                gained += 1
            elif prev is None:
                merged[pid] = s
        print(f"[qual] {sym} pass {pass_no}: +{gained} scored, "
              f"{sum(1 for v in merged.values() if v.get('score') is not None)}"
              f"/{len(qual_ids)} covered, calls used {sorted(used)}")
        if gained == 0 and pass_no > 1:
            break

    scores = list(merged.values())
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


QUAL_PROMPT_VERSION = 3   # bump when the prompt/loop changes -> invalidates qual cache


def _qual_prompt(sym: str, excerpt: str, n_calls: int, date_range: str,
                 mgmt_hist: list, param_ids: list | None = None,
                 pass_no: int = 1) -> str:
    params = [p for p in _fw_json["parameters"]
              if p["nature"] in ("qualitative", "hybrid")
              and (param_ids is None or p["id"] in param_ids)]
    plist = "\n".join(f'- {p["id"]}: {p["name"]} — {p["signal"]}'
                      for p in params)
    mgmt_lines = "\n".join(
        f'- {m["role"]}: {" ".join(str(m["name"]).split())} '
        f'({m["years"] or "?"}, {m["status"]})'
        for m in mgmt_hist) or "(no management history on file)"
    pass_note = ("" if pass_no == 1 else
                 f"\nNOTE: this is evidence pass {pass_no} — the excerpts below are "
                 "DIFFERENT calls than earlier passes, provided specifically to "
                 "assess the parameters listed (they lacked evidence so far). "
                 "Score any that THIS evidence supports; keep null only if still silent.\n")
    return (
        "You are scoring a company against a quality-investing framework.\n"
        + pass_note +
        "\nEVIDENCE 1 — CONFERENCE-CALL TIMELINE: excerpts sampled across "
        f"{n_calls} quarterly calls ({date_range}), oldest first. Judge the "
        "TRAJECTORY, not one quarter: did management deliver what it promised "
        "in earlier calls? Is the narrative consistent over the years? Are "
        "earlier-announced capex/product plans confirmed as executed later?\n\n"
        "EVIDENCE 2 — MANAGEMENT HISTORY (from 5 years of annual reports): "
        "tenure and churn are track-record evidence in their own right — a "
        "stable long-tenured Chairman/MD/CFO table alone justifies scoring "
        "the management-stability aspects of MGT.* parameters; churn or "
        "revolving leadership is a governance flag.\n\n"
        "SCORING RULES: score each parameter -2..+2 when ANY of the evidence "
        "(any call, any year, or the management table) supports a judgement; "
        "use null ONLY when the evidence is genuinely silent. Never guess "
        "beyond the evidence — every score must cite it.\n\n"
        f"Parameters:\n{plist}\n\n"
        "Return STRICT JSON only: {\"scores\": [{\"id\": ..., \"score\": int|null, "
        "\"rationale\": \"1 sentence citing the calls or the management record\", "
        "\"quote\": \"short verbatim quote or empty\"}]}\n\n"
        f"MANAGEMENT HISTORY ({sym}):\n{mgmt_lines}\n\n"
        f"CONFERENCE-CALL EXCERPTS ({sym}):\n{excerpt}"
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
        "model": API_MODEL,
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=body,
        headers={"content-type": "application/json",
                 "x-api-key": key, "anthropic-version": "2023-06-01"})
    try:
        with urllib.request.urlopen(req, timeout=HTTP_AI_TIMEOUT) as resp:
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
            ["claude", "-p", "--model", ANALYSIS_MODEL],
            input=prompt,
            capture_output=True, text=True, timeout=None,   # no timeout: quality > speed
        )
    except FileNotFoundError:
        raise HTTPException(503, "claude CLI not found on PATH")
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "").strip()[-400:]
        raise HTTPException(
            502, f"claude CLI failed (is it logged in? run `claude` once "
                 f"to authenticate): {tail}")
    return {"symbol": sym, "model": f"claude-code {ANALYSIS_MODEL} (subscription)",
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
    # Translate internal parameter/module ids to display names so the
    # answer never leaks developer vocabulary at the reader.
    _fw_names = {p["id"]: p["name"] for p in _fw_json["parameters"]}
    rec_view = {k: rec[k] for k in ("name", "overall", "coverage", "series",
                                    "mgmt")}
    rec_view["areas"] = {MODULE_SHORT.get(m, m): v
                         for m, v in rec["modules"].items()}
    rec_view["checks"] = {_fw_names.get(k, k): v
                          for k, v in rec["params"].items()}
    record_json = json.dumps(rec_view, default=str)[:12000]
    # Ground the answer in ALL THREE stored analyses: quality framework,
    # multibagger patterns and risk channels (judges served from cache).
    ai_on = _ai_backend() is not None
    mb_rec, _s1 = R.patterns_analysis(sym, ai=ai_on)
    qr_rec, _s2 = R.risks_analysis(sym, ai=ai_on)
    rt = R.compute_rating(sym, rec, mb_rec, qr_rec)
    mb_json = json.dumps({
        "core_gate": mb_rec["core_gate"]["status"],
        "verdicts": [{"pattern": v["name"], "verdict": v["verdict"],
                      "why": v.get("derivation", ""),
                      "rationale": v["qual"].get("rationale", ""),
                      "quote": v["qual"].get("quote", "")}
                     for v in mb_rec["verdicts"]]}, default=str)[:7000]
    qr_json = json.dumps({
        "fragility": qr_rec["fragility"]["status"],
        "verdicts": [{"risk": v["name"], "verdict": v["verdict"],
                      "why": v.get("derivation", ""),
                      "rationale": v["qual"].get("rationale", ""),
                      "quote": v["qual"].get("quote", ""),
                      "silver_lining": v["qual"].get("mitigant", "")}
                     for v in qr_rec["verdicts"]]}, default=str)[:7000]
    rt_json = json.dumps({"score": rt["score"], "grade": rt["grade"],
                          "how": rt["derivation"],
                          "pillars": {k: {"points": p["points"],
                                          "why": p["derivation"]}
                                      for k, p in rt["pillars"].items()}},
                         default=str)[:3000]
    prompt = (
        f"You are explaining an investment analysis for {rec['name']} "
        f"({sym}). Answer the user's question USING ONLY the stored records "
        "below (quality framework scores, multibagger-pattern verdicts, "
        "risk verdicts, the combined rating) and the concall excerpts. "
        "Rules: cite the specific check names, pattern/risk names, "
        "numbers, or verbatim quotes you rely on — use the plain display "
        "names exactly as given, never internal codes or analyst "
        "shorthand; explain in plain, everyday financial language; if the "
        "records and excerpts don't contain the answer, say so plainly — "
        "never invent. Be concise (<= 200 words).\n\n"
        f"QUESTION: {question}\n\n"
        f"COMBINED RATING (0-100):\n{rt_json}\n\n"
        f"QUALITY-FRAMEWORK RECORD (scores are -2..+2):\n{record_json}\n\n"
        f"MULTIBAGGER-PATTERN VERDICTS:\n{mb_json}\n\n"
        f"RISK VERDICTS:\n{qr_json}\n\n"
        f"CONCALL EXCERPTS ({timeline['n_calls']} calls, "
        f"{timeline['from']}–{timeline['to']}):\n{timeline['excerpt'][:6000]}"
    )
    if backend == "api":
        body = json.dumps({"model": API_MODEL, "max_tokens": 700,
                           "messages": [{"role": "user", "content": prompt}]}).encode()
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages", data=body,
            headers={"content-type": "application/json",
                     "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                     "anthropic-version": "2023-06-01"})
        try:
            with urllib.request.urlopen(req, timeout=HTTP_AI_TIMEOUT) as resp:
                out = json.loads(resp.read())
            answer = "".join(b.get("text", "") for b in out.get("content", []))
        except Exception as e:
            raise HTTPException(502, f"Claude API error: {e}")
    else:
        proc = subprocess.run(["claude", "-p", "--model", ANALYSIS_MODEL],
                              input=prompt, capture_output=True,
                              text=True, timeout=None)
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


# ------------------------------------------- patterns / risks / rating
@app.get("/api/patterns/{sym}")
def patterns(sym: str, quick: int = 0):
    """MultibaggerPattern analysis: which winning patterns does it fit?"""
    sym = sym.upper()
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")
    ai = not quick and _ai_backend() is not None
    rec, status = R.patterns_analysis(sym, ai=ai)
    return {"symbol": sym, "status": status, "record": rec}


@app.get("/api/risks/{sym}")
def risks(sym: str, quick: int = 0):
    """QualityRisks analysis: which failure channels is it exposed to?"""
    sym = sym.upper()
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")
    ai = not quick and _ai_backend() is not None
    rec, status = R.risks_analysis(sym, ai=ai)
    return {"symbol": sym, "status": status, "record": rec}


@app.get("/api/rating/{sym}")
def rating_endpoint(sym: str, quick: int = 0):
    """The COMPLETE unified analysis: all three skills run live (each judge
    cached per transcript+model), combined into one explainable 0–100
    rating. First run of a company can take several minutes — three deep
    Opus reads of its concall history; cached afterwards."""
    sym = sym.upper()
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")
    ai = not quick and _ai_backend() is not None
    qual, qstatus = (None, "skipped_quick") if quick else _qual_scores_cached(sym)
    rec = build_record(sym, _live_map(), _cc_counts(), qual_scores=qual)
    rec["qualitative_status"] = qstatus
    tl = concall_timeline(sym, budget=4)
    rec["concall_range"] = {"n_calls": tl["n_calls"], "from": tl["from"],
                            "to": tl["to"]}
    mb_rec, mb_status = R.patterns_analysis(sym, ai=ai)
    qr_rec, qr_status = R.risks_analysis(sym, ai=ai)
    rt = R.compute_rating(sym, rec, mb_rec, qr_rec)
    return {"symbol": sym, "rating": rt, "record": rec,
            "patterns": {"status": mb_status, "record": mb_rec},
            "risks": {"status": qr_status, "record": qr_rec}}



# ------------------------------------------------------------- MD report
MODULE_FRIENDLY = {
    "CAP": "How management spends the company's money",
    "ROC": "How much the business earns on its capital",
    "GRW": "Where the growth comes from",
    "MGT": "The people running the company",
    "IND": "The industry it competes in",
    "CUS": "What customers get out of it",
    "MOAT": "What protects it from competition",
}
MODULE_SHORT = {"CAP": "Capital Allocation", "ROC": "Return on Capital",
                "GRW": "Growth", "MGT": "Management", "IND": "Industry Structure",
                "CUS": "Customer Benefits", "MOAT": "Competitive Advantage"}
WORD = {2: "Excellent", 1: "Good", 0: "Neutral", -1: "Weak", -2: "Poor"}
SOURCE_FRIENDLY = {"quant": "from the financial statements",
                   "ai_concall": "from the conference calls",
                   "fused": "from the numbers and the calls together"}


def _word(score):
    if score is None:
        return "Not assessed"
    return WORD.get(int(max(-2, min(2, round(score)))), "Neutral")


def _verdict_phrase(score):
    if score is None:
        return "Not assessed"
    if score >= 1.25:
        return "An excellent business"
    if score >= 0.5:
        return "A good business"
    if score >= -0.25:
        return "A mixed / average business"
    if score >= -1.25:
        return "A weak business"
    return "A poor business"


def _embed_skill_report(md: str) -> str:
    """Embed a skill's standalone report inside the big one: drop its title
    and footer, demote its headings one level. The content itself is
    untouched — the same captured judgements, not a re-narration."""
    out = []
    for ln in md.splitlines()[1:]:
        if ln.startswith("*Every verdict above"):
            break
        out.append("#" + ln if ln.startswith("## ") else ln)
    return "\n".join(out).strip()


def render_report_md(sym: str, quick: bool = False) -> str:
    """Compose the human-readable Markdown report from the SAME stored
    analysis records the UI shows — every line traces to a captured
    judgement; nothing is re-narrated. Covers all three skills plus the
    combined rating."""
    qual, qstatus = (None, "skipped_quick") if quick else _qual_scores_cached(sym)
    rec = build_record(sym, _live_map(), _cc_counts(), qual_scores=qual)
    ai_on = _ai_backend() is not None and not quick
    mb_rec, _s1 = R.patterns_analysis(sym, ai=ai_on)
    qr_rec, _s2 = R.risks_analysis(sym, ai=ai_on)
    rt = R.compute_rating(sym, rec, mb_rec, qr_rec)
    tl = concall_timeline(sym, budget=4)
    fw_by_id = {p["id"]: p for p in _fw_json["parameters"]}
    L: list[str] = []
    A = L.append

    A(f"# {rec['name']} ({sym}) — Complete Company Analysis")
    A("")
    if rt["score"] is not None:
        A(f"## The rating: {rt['grade']} — {rt['score']} out of 100 "
          f"{'★' * rt['stars']}{'☆' * (5 - rt['stars'])}")
        A("")
        A(f"**How it was built:** {rt['derivation']}")
        A("")
        for key in ("quality", "patterns", "safety"):
            p = rt["pillars"][key]
            pts = "—" if p["points"] is None else f"{p['points']}/100"
            A(f"- **{p['name']} ({pts}):** {p['derivation']}")
        A("")
        A("*The three pillars answer three different questions: how good "
          "is the business today (quality), does it look like the long-term "
          "winners (multibagger fit), and what could break it (risk "
          "safety). Each pillar's full evidence follows below.*")
        A("")
    A(f"**Business quality verdict: {_verdict_phrase(rec['overall'])}**"
      + (f" — quality score {rec['overall']:+.2f} on a scale of −2 (poor) "
         f"to +2 (excellent)." if rec['overall'] is not None else "."))
    A("")
    facts = []
    if rec.get("industry"):
        facts.append(f"Industry: {rec['industry']}")
    if rec.get("mcap"):
        facts.append(f"Market value: ₹{rec['mcap']:,.0f} crore")
    if rec.get("pe"):
        facts.append(f"Price-to-earnings: {rec['pe']}")
    if facts:
        A(" · ".join(facts))
        A("")
    cov_line = (f"We assessed **{rec['coverage']:.0%} of the framework's 34 "
                f"quality checks**")
    cov_line += ("." if rec['coverage'] >= 0.995 else
                 " — the checks the evidence could not answer are marked in "
                 "each section rather than guessed.")
    A(cov_line)
    if rec.get("qualitative_included") and tl.get("n_calls"):
        A("")
        A(f"Evidence: the company's financial statements (about a decade), "
          f"**{tl['n_calls']} quarterly earnings calls** "
          f"({tl['from']} to {tl['to']}) read oldest-to-newest to check "
          f"whether management delivered on its promises, and 5 years of "
          f"leadership history from annual reports.")
    A("")
    A("## The verdict at a glance")
    A("")
    A("| Area | Verdict | Score | Checks done |")
    A("|---|---|---|---|")
    for m in _module_ids:
        md = rec["modules"][m]
        A(f"| {MODULE_SHORT[m]} | {_word(md['score'])} | "
          f"{'—' if md['score'] is None else format(md['score'], '+.2f')} | "
          f"{md['assessed']} of {md['total']} |")
    A("")
    A("**How the overall score is built:** each area's score is the simple "
      "average of its assessed checks; the overall is a weighted average of "
      "the areas (returns, industry structure and competitive protection "
      "carry 25% extra weight). The exact arithmetic:")
    calc = rec.get("overall_calc", "")
    for mid, mname in MODULE_SHORT.items():
        calc = calc.replace(f"{mid} ", f"{mname} ")
    calc = calc.replace("weighted mean of assessed module scores",
                        "weighted average of the assessed area scores")
    A("")
    A(f"> {calc}")
    A("")

    for m in _module_ids:
        md = rec["modules"][m]
        A(f"## {MODULE_SHORT[m]} — {_word(md['score'])}"
          + (f" ({md['score']:+.2f})" if md['score'] is not None else ""))
        A("")
        A(f"*{MODULE_FRIENDLY[m]}.*")
        A("")
        assessed = [(pid, rec["params"][pid]) for pid in rec["params"]
                    if fw_by_id.get(pid, {}).get("module") == m]
        silent = [p for p in _fw_json["parameters"]
                  if p["module"] == m and p["id"] not in rec["params"]]
        for pid, got in assessed:
            meta = fw_by_id.get(pid, {})
            src = SOURCE_FRIENDLY.get(got.get("source", "quant"),
                                      "from the financial statements")
            A(f"**{meta.get('name', pid)} — {_word(got['score'])}** "
              f"*({src})*")
            A("")
            rat = got["rationale"]
            rat = rat.replace("From concall: ", "")
            rat = rat.replace(" | Concall: ", " And from the calls: ")
            A(rat)
            q = got.get("quote") or ""
            if q:
                A("")
                if re.search(r"FY\d{4}", q) and re.search(r"current|exited", q):
                    A(f"> \"{q}\" — *from the annual-report leadership record*")
                else:
                    A(f"> \"{q}\" — *management, on an earnings call*")
            A("")
        if silent:
            A("*Not assessed here (the evidence was silent — we never guess): "
              + "; ".join(p["name"] for p in silent) + ".*")
            A("")

    if rec.get("mgmt_history"):
        A("## Who has been running the company (last 5 annual reports)")
        A("")
        A("| Role | Name | Years seen | Still there? |")
        A("|---|---|---|---|")
        for m2 in rec["mgmt_history"][:10]:
            nm = " ".join(str(m2["name"]).split())
            A(f"| {m2['role']} | {nm} | {m2['years'] or '—'} | "
              f"{'Yes' if m2['status'] == 'current' else 'No — exited'} |")
        A("")
        A("*A stable, long-tenured team is a quality signal; frequent exits — "
          "especially the finance chief — are a warning sign. This table fed "
          "the Management verdicts above.*")
        A("")

    series = rec.get("series") or {}
    if any(series.get(k) for k in ("sales", "opm", "ccc")):
        A("## The trend lines behind the numbers")
        A("")
        A("Yearly figures, oldest to latest:")
        A("")
        if series.get("sales"):
            vals = [v for v in series["sales"] if v is not None]
            A(f"- **Sales (₹ crore):** " + " → ".join(f"{v:,.0f}" for v in vals))
        if series.get("opm"):
            vals = [v for v in series["opm"] if v is not None]
            A(f"- **Operating margin (%):** " + " → ".join(f"{v:.0f}" for v in vals))
        if series.get("ccc"):
            vals = [v for v in series["ccc"] if v is not None]
            A(f"- **Days cash is tied up in the trade cycle:** "
              + " → ".join(f"{v:.0f}" for v in vals)
              + "  *(negative = customers pay before suppliers are due — good)*")
        A("")

    mb_name = rec["name"]
    A("## Which winning patterns does it fit?")
    A("")
    A("*From the MultibaggerPattern skill: eleven patterns that long-term "
      "winners share (recurring revenue, toll-road economics, pricing "
      "power, brand strength…), each judged from the calls AND the "
      "numbers, with the reason for every verdict attached.*")
    A("")
    A(_embed_skill_report(R.MB_AZ.render_report(mb_rec, mb_name)))
    A("")
    A("## What could go wrong? (the risk check)")
    A("")
    A("*From the QualityRisks skill: eight ways strong businesses fail "
      "(boom-bust cycles, disruption, government dependency, cheaper "
      "good-enough rivals…), each judged with its severity and the reason "
      "attached — silver linings included.*")
    A("")
    A(_embed_skill_report(R.QR_AZ.render_report(qr_rec, mb_name)))
    A("")
    A("## How to read this report")
    A("")
    A("- The overall rating combines three pillars: business quality "
      "(45%), multibagger fit (30%) and risk safety (25%) — the arithmetic "
      "is shown at the top, and each pillar lists exactly what earned or "
      "cost points.")
    A("- Every verdict word maps to a score: Excellent (+2), Good (+1), "
      "Neutral (0), Weak (−1), Poor (−2).")
    A("- Every judgement above was captured at the moment of analysis with "
      "its evidence — a number from the statements, or a quoted line from an "
      "earnings call. Nothing was written after the fact.")
    A("- Checks the evidence couldn't answer are marked, not guessed, and "
      "they lower the coverage figure rather than the score.")
    A("- This is research tooling over public data (screener.in-derived "
      "statements, exchange-filed call transcripts). It is not investment "
      "advice.")
    A("")
    A(f"*Generated by the Business Quality Analyst · framework v"
      f"{_fw.version} · data through {tl.get('to') or 'latest fiscal year'}*")
    return "\n".join(L)


@app.get("/api/report/{sym}")
def report(sym: str, quick: int = 0):
    from fastapi.responses import Response
    sym = sym.upper()
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")
    md = render_report_md(sym, quick=bool(quick))
    return Response(content=md, media_type="text/markdown",
                    headers={"Content-Disposition":
                             f'attachment; filename="{sym}_quality_report.md"'})


@app.on_event("startup")
def warm_cache():
    """Compute the 742-company cache in the background at startup so the
    first visitor doesn't wait ~30s. The client also handles the cold
    window gracefully, but warm-by-default is the better experience."""
    threading.Thread(target=lambda: companies(), daemon=True).start()


# static frontend last, so /api/* wins
app.mount("/", StaticFiles(directory=str(HERE), html=True), name="ui")
