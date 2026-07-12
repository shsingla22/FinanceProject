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


def build_record(sym: str, live, ccm) -> dict:
    """Run the skill for one symbol, right now."""
    sig = Q.compute(sym, base=INDIA, universe=UNIVERSE)
    pscores = B.score_params(sig, _fw)
    agg = S.aggregate(pscores, _module_ids)
    meta = _const_map.get(sym, {"name": sym, "industry": ""})
    lv = live.get(sym, {})
    return B.clean({
        "name": meta["name"], "industry": meta["industry"],
        "mcap": lv.get("market_cap_rs_cr"), "pe": lv.get("stock_pe"),
        "price": lv.get("current_price_rs"),
        "overall": agg["overall_score"], "coverage": agg["overall_coverage"],
        "modules": {m: {"score": agg["modules"][m]["module_score"],
                        "assessed": agg["modules"][m]["n_assessed"],
                        "total": agg["modules"][m]["n_total"]}
                    for m in _module_ids},
        "params": {p.id: {"score": p.score, "rationale": p.rationale,
                          "nature": p.nature}
                   for p in pscores if p.score is not None},
        "series": B.series_for_chart(sig),
        "mgmt": _mgmt(sym),
        "concalls": ccm.get(sym, 0),
        "computed_live": True,
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
        # read from the END (newest call last, per the merge order)
        parts, chars = [], 0
        for page in reversed(reader.pages):
            try:
                t = page.extract_text() or ""
            except Exception:
                t = ""
            parts.append(t)
            chars += len(t)
            if chars >= 60000:
                break
        text = "\n".join(reversed(parts))
    except Exception:
        text = ""
    _cache["concall_text"][sym] = text
    return text[-max_chars:]


# ----------------------------------------------------------------- endpoints
@app.get("/api/health")
def health():
    return {"mode": "dynamic", "universe": UNIVERSE,
            "framework_version": _fw.version,
            "ai_qualitative": bool(os.environ.get("ANTHROPIC_API_KEY")),
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


@app.get("/api/company/{sym}")
def company(sym: str):
    sym = sym.upper()
    if sym not in _const_map:
        raise HTTPException(404, f"{sym} is not in the {UNIVERSE} universe")
    rec = build_record(sym, _live_map(), _cc_counts())
    rec["concall_excerpt"] = concall_text(sym, 1600)
    return {"symbol": sym, "record": rec}


@app.get("/api/concall/{sym}")
def concall(sym: str, chars: int = 8000):
    sym = sym.upper()
    text = concall_text(sym, max(500, min(chars, 20000)))
    if not text:
        raise HTTPException(404, f"no concall transcript on file for {sym}")
    return {"symbol": sym, "chars": len(text), "text": text}


@app.post("/api/qualitative/{sym}")
def qualitative(sym: str):
    """Run the skill's qualitative playbook over the latest concall text via
    the Claude API. Live fusion of quantitative + qualitative."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise HTTPException(503, "AI mode off: set ANTHROPIC_API_KEY to enable")
    sym = sym.upper()
    text = concall_text(sym, 12000)
    if not text:
        raise HTTPException(404, f"no concall transcript on file for {sym}")

    qual_params = [p for p in _fw_json["parameters"]
                   if p["nature"] in ("qualitative", "hybrid")]
    plist = "\n".join(f'- {p["id"]}: {p["name"]} — {p["signal"]}'
                      for p in qual_params)
    prompt = (
        "You are scoring a company against a quality-investing framework "
        "using ONLY the conference-call excerpt below.\n\n"
        f"Parameters (score each -2..+2, or null if the text is silent — never guess):\n{plist}\n\n"
        "Return STRICT JSON only: {\"scores\": [{\"id\": ..., \"score\": int|null, "
        "\"rationale\": \"1 sentence citing the call\", \"quote\": \"short verbatim quote or empty\"}]}\n\n"
        f"CONFERENCE CALL EXCERPT ({sym}):\n{text}"
    )
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
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        raise HTTPException(502, "could not parse model output")
    scores = json.loads(m.group(0)).get("scores", [])
    return {"symbol": sym, "model": out.get("model"), "scores": scores}


@app.post("/api/refresh")
def refresh():
    with _lock:
        _drop_caches()
    return {"ok": True, "message": "caches dropped; next request recomputes"}


# static frontend last, so /api/* wins
app.mount("/", StaticFiles(directory=str(HERE), html=True), name="ui")
