"""
server.py — PRECOMPUTED mode for the Business Quality Analyst (UX v2).

Where the original UserInterface runs the three analysis skills LIVE per
request (minutes per first-time company), this server answers from the
ALREADY-WRITTEN Markdown reports in
Analysis/NiftyTotalMarketAnalysis/QualityAnalysis — the same reports the
batch run produced and validated ({SYM}_analysis.md + {SYM}_comparison.md,
plus RANKING.md / _ranking.csv). Every company view is a file read, so the
whole app answers in milliseconds and needs no AI to browse.

    uvicorn server:app --host 0.0.0.0 --port 8001    (from UserInterfaceV2/)

Endpoints
  GET  /api/health                 mode + how many companies are analysed
  GET  /api/companies              every analysed company: name, industry,
                                   rating, grade, 1-yr direction, mcap/PE
  GET  /api/analysis/{sym}         the stored analyst report (raw MD +
                                   parsed section map) — instant
  GET  /api/comparison/{sym}       the stored then-vs-now report — instant
  GET  /api/report/{sym}           MD download (exact stored file)
  GET  /api/comparison_report/{sym}  MD download (exact stored file)
  GET  /api/ranking?n=20&order=best  ranked list for drill-down
  GET  /api/charts/{sym}           yearly financial series (sales, profit,
                                   margins, returns, cash flow, debt…) for
                                   the charts, straight from the statements
  POST /api/jobs/ask/{sym}         Q&A grounded ONLY in the two stored MDs
  GET  /api/jobs/ask/{id}          poll twin (proxy-proof, like v1)

The static frontend is served from this same process at / .
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import threading
import time
import urllib.request
import uuid
from functools import lru_cache
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
INDIA = REPO / "IndividualStockAnalysis" / "India"
UNIVERSE = "NiftyTotalMarket"
QA = INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "QualityAnalysis"

app = FastAPI(title="Business Quality Analyst API (precomputed v2)")

# ------------------------------------------------------------------ inventory
_const = pd.read_csv(INDIA / UNIVERSE / "niftytotalmarket_constituents.csv")
_const_map = {str(r.nse_symbol): {"name": r.company_name,
                                  "industry": (r.industry if isinstance(r.industry, str) else "") or ""}
              for r in _const.itertuples()}


def _report_paths(sym: str) -> tuple[Path, Path]:
    return QA / f"{sym}_analysis.md", QA / f"{sym}_comparison.md"


def analysed_symbols() -> list[str]:
    """Symbols with BOTH stored reports, in constituents order."""
    return [s for s in _const_map
            if _report_paths(s)[0].exists() and _report_paths(s)[1].exists()]


def _ranking_rows() -> list[dict]:
    path = QA / "_ranking.csv"
    if not path.exists():
        return []
    df = pd.read_csv(path)
    rows = []
    for r in df.itertuples():
        # "Not rated" companies carry no rank/score — keep them listed
        # honestly (they surface in /api/companies, never in rankings)
        rows.append({"rank": None if pd.isna(r.rank) else int(r.rank),
                     "symbol": str(r.symbol), "name": str(r.name),
                     "score": None if pd.isna(r.score) else int(r.score),
                     "grade": str(r.grade),
                     "direction": None if pd.isna(r.one_year_direction)
                     else str(r.one_year_direction)})
    return rows


def _live_map() -> dict:
    path = INDIA / "StockInfo" / "Nifty500" / "live_market_data.csv"
    if not path.exists():
        return {}
    live = pd.read_csv(path)
    return live.set_index("nse_symbol").to_dict("index")


def _clean(v):
    try:
        return None if v is None or pd.isna(v) else v
    except Exception:
        return v


# --------------------------------------------------------------- MD utilities
SECTION_RE = re.compile(r"^(#{1,4})\s+(.*)$", re.M)


def _read_md(path: Path) -> str:
    try:
        return path.read_text()
    except Exception:
        raise HTTPException(500, f"stored report unreadable: {path.name}")


def md_sections(md: str) -> list[dict]:
    """A section map of the report: [{level, title}] in order — the client
    uses it for the explainability outline / jump list."""
    return [{"level": len(m.group(1)), "title": m.group(2).strip()}
            for m in SECTION_RE.finditer(md)]


VERDICT_RE = re.compile(r"^## The verdict: (.+?) — (\d+) out of 100", re.M)
DIRECTION_RE = re.compile(r"^## Step 1 — The overall rating: (.+?) in the last year", re.M)


def _split_by_headings(md: str) -> list[tuple[str, str]]:
    """[(heading, body)] pairs — used by the no-AI extractive Q&A."""
    parts = SECTION_RE.split(md)
    out = []
    # parts = [pre, hashes, title, body, hashes, title, body, ...]
    for i in range(1, len(parts) - 2, 3):
        out.append((parts[i + 1].strip(), parts[i + 2].strip()))
    return out


# ------------------------------------------------------------------- AI setup
ANALYSIS_MODEL = os.environ.get("ANALYSIS_MODEL", "claude-opus-5")
API_MODEL_MAP = {"opus": "claude-opus-5", "sonnet": "claude-sonnet-5"}
API_MODEL = API_MODEL_MAP.get(ANALYSIS_MODEL, ANALYSIS_MODEL)
HTTP_AI_TIMEOUT = 3600


def _ai_backend() -> str | None:
    """Same two paths as v1: the Claude API (key in env) or the logged-in
    Claude Code CLI (personal subscription — keep the port private)."""
    if os.environ.get("UI_DISABLE_AI"):
        return None
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "api"
    if shutil.which("claude"):
        return "claude_code_cli"
    return None


# ----------------------------------------------------------------- endpoints
@app.get("/api/health")
def health():
    syms = analysed_symbols()
    return {"mode": "precomputed", "universe": UNIVERSE,
            "n_universe": len(_const_map), "n_analysed": len(syms),
            "reports_dir": str(QA.relative_to(REPO)),
            "ai_qa": _ai_backend() is not None,
            "ai_backend": _ai_backend(),
            "analysis_model": ANALYSIS_MODEL}


@app.get("/api/companies")
def companies():
    """Every analysed company with its stored rating — one CSV-backed pass,
    no computation. Unanalysed constituents are listed too (flagged), so
    the client can say 'not analysed yet' instead of 'no such company'."""
    live = _live_map()
    ranked = {r["symbol"]: r for r in _ranking_rows()}
    have = set(analysed_symbols())
    out = {}
    for sym, meta in _const_map.items():
        rk = ranked.get(sym)
        lv = live.get(sym, {})
        out[sym] = {"name": meta["name"], "industry": meta["industry"],
                    "analysed": sym in have,
                    "rank": rk["rank"] if rk else None,
                    "score": rk["score"] if rk else None,
                    "grade": rk["grade"] if rk else None,
                    "direction": rk["direction"] if rk else None,
                    "mcap": _clean(lv.get("market_cap_rs_cr")),
                    "pe": _clean(lv.get("stock_pe")),
                    "price": _clean(lv.get("current_price_rs"))}
    return {"universe": UNIVERSE, "n": len(out),
            "n_analysed": len(have), "companies": out}


def _require_analysed(sym: str) -> str:
    sym = sym.upper()
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")
    a, c = _report_paths(sym)
    if not (a.exists() and c.exists()):
        raise HTTPException(404, f"{sym} has not been analysed yet — "
                            f"{len(analysed_symbols())} of "
                            f"{len(_const_map)} companies have stored reports")
    return sym


@app.get("/api/analysis/{sym}")
def analysis(sym: str):
    """The stored analyst report — served as-is (page and downloadable file
    can never disagree: they are the same bytes) plus a parsed header."""
    sym = _require_analysed(sym)
    md = _read_md(_report_paths(sym)[0])
    m = VERDICT_RE.search(md)
    live = _live_map().get(sym, {})
    return {"symbol": sym, "name": _const_map[sym]["name"],
            "industry": _const_map[sym]["industry"],
            "grade": m.group(1) if m else None,
            "score": int(m.group(2)) if m else None,
            "market": {"mcap": _clean(live.get("market_cap_rs_cr")),
                       "pe": _clean(live.get("stock_pe")),
                       "price": _clean(live.get("current_price_rs"))},
            "sections": md_sections(md), "md": md}


@app.get("/api/comparison/{sym}")
def comparison(sym: str):
    sym = _require_analysed(sym)
    md = _read_md(_report_paths(sym)[1])
    m = DIRECTION_RE.search(md)
    return {"symbol": sym, "name": _const_map[sym]["name"],
            "direction": m.group(1).lower() if m else None,
            "sections": md_sections(md), "md": md}


@app.get("/api/report/{sym}")
def report(sym: str):
    sym = _require_analysed(sym)
    return Response(content=_read_md(_report_paths(sym)[0]),
                    media_type="text/markdown",
                    headers={"Content-Disposition":
                             f'attachment; filename="{sym}_analysis.md"'})


@app.get("/api/comparison_report/{sym}")
def comparison_report(sym: str):
    sym = _require_analysed(sym)
    return Response(content=_read_md(_report_paths(sym)[1]),
                    media_type="text/markdown",
                    headers={"Content-Disposition":
                             f'attachment; filename="{sym}_comparison.md"'})


@app.get("/api/ranking")
def ranking(n: int = 20, order: str = "best", industry: str | None = None):
    """Best/worst N from the stored ranking — every row carries what the
    drill-down needs (click a company -> its full stored reports)."""
    rows = [r for r in _ranking_rows() if r["score"] is not None]
    if not rows:
        raise HTTPException(404, "no stored ranking — run rank_companies.py")
    if industry:
        want = industry.strip().lower()
        rows = [r for r in rows
                if _const_map.get(r["symbol"], {}).get("industry", "").lower() == want]
    rows.sort(key=lambda r: r["rank"], reverse=(order == "worst"))
    n = max(1, min(200, n))
    live = _live_map()
    out = []
    for r in rows[:n]:
        lv = live.get(r["symbol"], {})
        out.append({**r,
                    "industry": _const_map.get(r["symbol"], {}).get("industry", ""),
                    "mcap": _clean(lv.get("market_cap_rs_cr")),
                    "pe": _clean(lv.get("stock_pe"))})
    return {"order": order, "n": len(out), "industry": industry,
            "n_ranked": len(rows) if not industry else len(rows),
            "rows": out}


# -------------------------------------------------------------------- charts
PL_ITEMS = {"Sales": "sales", "Net Profit": "net_profit", "OPM %": "opm",
            "EPS in Rs": "eps"}
WC_ITEMS = {"ROCE %": "roce", "ROE %": "roe",
            "Cash Conversion Cycle": "ccc"}
BS_ITEMS = {"Borrowing": "borrowings", "Borrowings": "borrowings",
            "Reserves": "reserves"}
CF_ITEMS = {"Cash from Operating Activity": "cfo", "Free Cash Flow": "fcf"}

_MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def _year_key(label: str) -> tuple:
    parts = str(label).split()
    try:
        return (int(parts[1]), _MONTHS.get(parts[0], 0))
    except Exception:
        return (0, 0)


@lru_cache(maxsize=1)
def _statement_frames():
    def load(path, item_col, val_col):
        df = pd.read_csv(path)
        df = df[df["parent_line_item"].isna()] if "parent_line_item" in df else df
        return df.rename(columns={item_col: "item", val_col: "value"})[
            ["nse_symbol", "year", "item", "value"]]
    return {
        "pl": load(INDIA / "ProfitStatement" / UNIVERSE / "_all_profit_loss_long.csv",
                   "line_item", "value"),
        "bs": load(INDIA / "BalanceSheet" / UNIVERSE / "_all_balance_sheets_long.csv",
                   "line_item", "value_rs_cr"),
        "cf": load(INDIA / "CashFlow" / UNIVERSE / "_all_cash_flow_long.csv",
                   "line_item", "value_rs_cr"),
        "wc": load(INDIA / "WorkingCapital" / UNIVERSE / "_all_working_capital_long.csv",
                   "metric", "value"),
    }


@lru_cache(maxsize=1024)
def _charts_for(sym: str) -> dict:
    frames = _statement_frames()
    series: dict[str, dict] = {}
    years: set = set()
    for key, items in (("pl", PL_ITEMS), ("bs", BS_ITEMS),
                       ("cf", CF_ITEMS), ("wc", WC_ITEMS)):
        df = frames[key]
        sub = df[df["nse_symbol"] == sym]
        for item, out_key in items.items():
            rows = sub[sub["item"] == item]
            if rows.empty:
                continue
            d = {}
            for r in rows.itertuples():
                if not pd.isna(r.value):
                    d[str(r.year)] = float(r.value)
            if d:
                # 'Borrowing' vs 'Borrowings': merge, don't overwrite
                series.setdefault(out_key, {}).update(d)
                years.update(d)
    labels = sorted(years, key=_year_key)
    return {"symbol": sym, "years": labels,
            "series": {k: [v.get(y) for y in labels]
                       for k, v in series.items()}}


CHART_META = [
    {"key": "sales", "title": "Sales", "unit": "₹ Cr", "kind": "bar"},
    {"key": "net_profit", "title": "Net profit", "unit": "₹ Cr", "kind": "bar"},
    {"key": "opm", "title": "Operating margin", "unit": "%", "kind": "line"},
    {"key": "roce", "title": "Return on capital (ROCE)", "unit": "%", "kind": "line"},
    {"key": "roe", "title": "Return on equity (ROE)", "unit": "%", "kind": "line"},
    {"key": "eps", "title": "Earnings per share", "unit": "₹", "kind": "line"},
    {"key": "cfo", "title": "Cash from operations", "unit": "₹ Cr", "kind": "bar"},
    {"key": "fcf", "title": "Free cash flow", "unit": "₹ Cr", "kind": "bar"},
    {"key": "borrowings", "title": "Borrowings", "unit": "₹ Cr", "kind": "bar"},
    {"key": "reserves", "title": "Reserves", "unit": "₹ Cr", "kind": "bar"},
    {"key": "ccc", "title": "Cash conversion cycle", "unit": "days", "kind": "line"},
]


@app.get("/api/charts/{sym}")
def charts(sym: str):
    """Yearly financial series for the charts — read from the SAME statement
    CSVs the analyses were computed from, so charts and verdicts describe
    the same numbers."""
    sym = sym.upper()
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")
    data = _charts_for(sym)
    charts = [dict(m) for m in CHART_META
              if sum(v is not None for v in data["series"].get(m["key"], [])) >= 3]
    return {**data, "charts": charts}


# ------------------------------------------------------- Q&A (explainability)
def _extractive_answer(sym: str, question: str, a_md: str, c_md: str) -> str:
    """No-AI fallback: return the report sections most relevant to the
    question, verbatim. Honest and instant — never invents."""
    stop = {"the", "and", "for", "what", "why", "how", "does", "this",
            "that", "with", "about", "are", "was", "has", "have", "its",
            "can", "you", "tell"}
    words = {w for w in re.findall(r"[a-z]{3,}", question.lower())
             if w not in stop}
    scored = []
    for src, md in (("analysis", a_md), ("comparison", c_md)):
        for title, body in _split_by_headings(md):
            if re.match(r"How this (report|comparison) was built", title, re.I):
                continue
            hay = (title + " " + body).lower()
            score = sum(hay.count(w) for w in words)
            if score > 0 and body:
                scored.append((score, src, title, body))
    scored.sort(key=lambda t: -t[0])
    if not scored:
        return ("AI answering is off, and no stored section matches that "
                "question. The full reports are on this page — try the "
                "outline, or ask about a check, pattern, risk or number "
                "they mention.")
    picks = scored[:2]
    parts = [f"[from the stored {src} report — “{title}”]\n{body[:1500]}"
             for _, src, title, body in picks]
    return ("AI answering is off, so here are the most relevant passages "
            "from the stored reports, verbatim:\n\n" + "\n\n".join(parts))


def _answer_question(sym: str, question: str, backend: str | None) -> dict:
    """Q&A grounded ONLY in the two stored MD reports — the explainability
    contract of v2: the page, the downloads and the answers all come from
    the same files."""
    a_md = _read_md(_report_paths(sym)[0])
    c_md = _read_md(_report_paths(sym)[1])
    if backend is None:
        return {"symbol": sym, "question": question,
                "answer": _extractive_answer(sym, question, a_md, c_md),
                "grounded_on": "stored_reports", "ai": False}
    name = _const_map[sym]["name"]
    prompt = (
        f"You are explaining a STORED investment analysis for {name} "
        f"({sym}). Answer the user's question USING ONLY the two Markdown "
        "reports below — the full analyst report and the one-year "
        "then-vs-now comparison. They contain the verdicts, every check/"
        "pattern/risk with its why, the exact rating arithmetic, and "
        "management quotes.\n"
        "Rules: cite the specific check names, pattern/risk names, numbers "
        "or quotes you rely on, exactly as the reports word them; plain, "
        "everyday financial language; if the reports don't contain the "
        "answer, say so plainly — never invent, never use outside "
        "knowledge. Be concise (<= 200 words).\n\n"
        f"QUESTION: {question}\n\n"
        f"===== STORED ANALYST REPORT ({sym}) =====\n{a_md[:60000]}\n\n"
        f"===== STORED ONE-YEAR COMPARISON ({sym}) =====\n{c_md[:25000]}")
    if backend == "api":
        body = json.dumps({"model": API_MODEL, "max_tokens": 700,
                           "messages": [{"role": "user",
                                         "content": prompt}]}).encode()
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
    return {"symbol": sym, "question": question, "answer": answer,
            "grounded_on": "stored_reports", "ai": True}



def _ai_text(prompt: str, backend: str, max_tokens: int = 500) -> str:
    """One short AI call through whichever backend is configured."""
    if backend == "api":
        body = json.dumps({"model": API_MODEL, "max_tokens": max_tokens,
                           "messages": [{"role": "user",
                                         "content": prompt}]}).encode()
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages", data=body,
            headers={"content-type": "application/json",
                     "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                     "anthropic-version": "2023-06-01"})
        try:
            with urllib.request.urlopen(req, timeout=HTTP_AI_TIMEOUT) as resp:
                out = json.loads(resp.read())
            return "".join(b.get("text", "") for b in out.get("content", []))
        except Exception as e:
            raise HTTPException(502, f"Claude API error: {e}")
    proc = subprocess.run(["claude", "-p", "--model", ANALYSIS_MODEL],
                          input=prompt, capture_output=True,
                          text=True, timeout=None)
    if proc.returncode != 0:
        raise HTTPException(502, "claude CLI failed: " +
                            (proc.stderr or "")[-300:])
    return proc.stdout.strip()


def _candidates_for(query: str, k: int = 25) -> list[str]:
    """Fuzzy company candidates for the interpreter (same spirit as the
    client's matcher): exact symbol tokens first, then name-word prefixes."""
    up = query.upper()
    tokens = [t for t in re.split(r"[^A-Z0-9&\-]+", up) if len(t) >= 2]
    hits = []
    for sym, meta in _const_map.items():
        if sym in tokens:
            hits.append((100, sym))
            continue
        words = str(meta["name"]).upper().split()
        w = sum(len(t) for t in tokens
                if len(t) >= 4 and any(wd.startswith(t) for wd in words))
        if w:
            hits.append((w, sym))
    hits.sort(key=lambda h: -h[0])
    return [s for _, s in hits[:k]]


def _interpret(query: str, backend: str) -> dict:
    """Turn a free-form request into a routed intent, grounded in the real
    universe (candidate symbols + industries) so the model never invents a
    ticker. Strict JSON out; everything is validated before it is returned."""
    cands = _candidates_for(query)
    cand_lines = "\n".join(f"- {s}: {_const_map[s]['name']}" for s in cands) \
                 or "(none)"
    inds = sorted({m["industry"] for m in _const_map.values() if m["industry"]})
    universe = "\n".join(f"{s}|{m['name']}|{m['industry']}"
                          for s, m in _const_map.items())
    prompt = (
        "You route requests for an equity-research app. Decide what the "
        "user wants and answer with STRICT JSON only, no prose:\n"
        '{"intent": "company"|"rank"|"compare"|"question"|"unknown", '
        '"symbols": [tickers from the universe below only], '
        '"n": int|null, "order": "best"|"worst"|null, '
        '"industry": string|null, "question": string|null}\n\n'
        "Rules: 'company' = open one company's research (one symbol). "
        "'rank' = a best/worst list (set n, order, industry when named). "
        "'compare' = two symbols. 'question' = the user asks something "
        "specific about one company (including descriptions like 'the "
        "biggest toothpaste maker' — resolve them to the ticker) — set "
        "symbols and put the question, reworded standalone, in "
        "'question'. Use ONLY tickers from the universe; if nothing "
        "fits, intent 'unknown'.\n\n"
        f"USER REQUEST: {query}\n\n"
        f"NAME-MATCH HINTS:\n{cand_lines}\n\n"
        f"KNOWN INDUSTRIES: {', '.join(inds)}\n\n"
        f"UNIVERSE (ticker|name|industry):\n{universe}")
    raw = _ai_text(prompt, backend, max_tokens=300)
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        return {"intent": "unknown", "symbols": [], "query": query}
    try:
        d = json.loads(m.group(0))
    except json.JSONDecodeError:
        return {"intent": "unknown", "symbols": [], "query": query}
    intent = d.get("intent")
    if intent not in {"company", "rank", "compare", "question"}:
        intent = "unknown"
    syms = [s for s in (d.get("symbols") or [])
            if isinstance(s, str) and s.upper() in _const_map][:2]
    syms = [s.upper() for s in syms]
    if intent in {"company", "question"} and not syms:
        intent = "unknown"
    if intent == "compare" and len(syms) < 2:
        intent = "company" if syms else "unknown"
    n = d.get("n")
    n = max(1, min(200, int(n))) if isinstance(n, (int, float)) else None
    order = d.get("order") if d.get("order") in ("best", "worst") else None
    ind = d.get("industry")
    ind_l = {i.lower(): i for i in inds}
    industry = ind_l.get(str(ind).lower()) if ind else None
    q = d.get("question")
    question = str(q).strip() if q else None
    return {"intent": intent, "symbols": syms, "n": n, "order": order,
            "industry": industry, "question": question, "query": query}


@app.post("/api/jobs/interpret")
def job_interpret(payload: dict | None = None):
    """AI request routing (job form): free-form English in, a validated
    intent out. 503 when no AI backend is configured — the client then
    keeps its plain pattern matching."""
    backend = _ai_backend()
    if backend is None:
        raise HTTPException(503, "AI is off — log in the Claude Code CLI "
                                 "or set ANTHROPIC_API_KEY")
    query = (payload or {}).get("query", "").strip()
    if not query:
        raise HTTPException(422, "missing 'query'")
    job_id = uuid.uuid4().hex.upper()
    return _job_start("interpret", job_id,
                      lambda: _interpret(query, backend))


@app.post("/api/ask/{sym}")
def ask(sym: str, payload: dict):
    """Synchronous Q&A (scripts / tests). The UI uses the job form below."""
    sym = _require_analysed(sym)
    question = (payload or {}).get("question", "").strip()
    if not question:
        raise HTTPException(422, "missing 'question'")
    return _answer_question(sym, question, _ai_backend())


# ------------------------------------------------- proxy-proof job endpoints
# Same pattern as v1: an AI answer can outlive proxy timeouts (Codespaces
# kills requests after ~100s), so the UI starts a job with a short POST and
# polls with short GETs. Company views don't need jobs here — they are
# file reads — only Q&A does.
_jobs: dict = {}
_jobs_lock = threading.Lock()


def _job_start(kind: str, job_id: str, fn) -> dict:
    key = f"{kind}:{job_id}"
    with _jobs_lock:
        cutoff = time.time() - 3600
        for k in [k for k, j in _jobs.items()
                  if j["state"] != "running" and j["started"] < cutoff]:
            _jobs.pop(k, None)
        _jobs[key] = {"state": "running", "started": time.time(),
                      "result": None, "error": None}

    def run():
        try:
            res = fn()
            _jobs[key].update(state="done", result=res)
        except Exception as e:
            _jobs[key].update(state="error", error=str(e)[:400])

    threading.Thread(target=run, daemon=True).start()
    return {"job": key, "state": "running"}


@app.post("/api/jobs/ask/{sym}")
def job_ask(sym: str, payload: dict | None = None):
    sym = _require_analysed(sym)
    question = (payload or {}).get("question", "").strip()
    if not question:
        raise HTTPException(422, "missing 'question'")
    backend = _ai_backend()
    job_id = uuid.uuid4().hex.upper()
    return _job_start("ask", job_id,
                      lambda: _answer_question(sym, question, backend))


@app.get("/api/jobs/{kind}/{job_id}")
def job_status(kind: str, job_id: str):
    if kind not in ("ask", "interpret"):
        raise HTTPException(404, f"unknown job kind '{kind}'")
    key = f"{kind}:{job_id.upper()}"
    j = _jobs.get(key)
    if j is None:
        raise HTTPException(404, f"no such job: {key} (POST it first)")
    out = {"job": key, "state": j["state"],
           "elapsed": round(time.time() - j["started"], 1)}
    if j["state"] == "done":
        out["result"] = j["result"]
    elif j["state"] == "error":
        out["error"] = j["error"]
    return out


# static frontend last, so /api/* wins
app.mount("/", StaticFiles(directory=str(HERE), html=True), name="ui")
