"""
earnings.py — step 2: is the earnings power rising, and is the company in
(or entering) a new-age industry?

Darvas never bought volume alone: the surge had to sit on top of growing
earnings power, ideally in a forward-looking industry. Two reads:

  NUMBERS — from the stored profit-and-loss archive: EBITDA (the
  statements' "Operating Profit" line; "Financing Profit" for lenders),
  EBITDA margin ("OPM %" / "Financing Margin %"), PAT ("Net Profit") and
  PAT margin (Net Profit / Sales), across the last four fiscal years.
  Verdict RISING / FLAT / FALLING from explicit, listed conditions.

  CALLS — the company's conference-call transcripts, read by the judge
  model, answer what the numbers cannot: is this a new-age industry, is
  the company ENTERING one, and does management talk about growing
  earnings power? Cached per transcript content + model; without AI the
  verdict is honestly "not assessed", never guessed.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
UNIVERSE = "NiftyTotalMarket"
PL_LONG = INDIA / "ProfitStatement" / UNIVERSE / "_all_profit_loss_long.csv"
CONCALLS = INDIA / "ConferenceCalls" / UNIVERSE
CACHE = HERE.parent / ".qual_cache.json"
MODEL = os.environ.get("DARVAS_JUDGE_MODEL",
                       os.environ.get("ANALYST_MODEL", "claude-opus-5"))

_PL_CACHE: dict = {}


def _pl_frame():
    if "df" not in _PL_CACHE:
        import pandas as pd
        _PL_CACHE["df"] = pd.read_csv(PL_LONG)
    return _PL_CACHE["df"]


def _year_key(y: str) -> tuple:
    m = re.search(r"(\d{4})", str(y))
    return (int(m.group(1)) if m else 0, str(y))


def _series(sub, item: str) -> list[tuple[str, float]]:
    rows = sub[sub.line_item == item][["year", "value"]].dropna()
    out = []
    for _, r in rows.iterrows():
        try:
            out.append((r["year"], float(r["value"])))
        except (TypeError, ValueError):
            continue
    out.sort(key=lambda t: _year_key(t[0]))
    return out


def earnings_power(sym: str, years: int = 4) -> dict:
    """The step-2 numbers table + verdict for one company."""
    sub = _pl_frame()
    sub = sub[sub.nse_symbol == sym]
    if not len(sub):
        return {"verdict": "NO DATA", "years": [],
                "why": "no stored profit-and-loss statements"}
    op = _series(sub, "Operating Profit") or _series(sub, "Financing Profit")
    opm = _series(sub, "OPM %") or _series(sub, "Financing Margin %")
    pat = _series(sub, "Net Profit")
    sales = _series(sub, "Sales") or _series(sub, "Revenue")
    lender = not _series(sub, "Operating Profit")

    def last(seq, n):
        return seq[-n:] if seq else []

    op, opm, pat, sales = (last(op, years), last(opm, years),
                           last(pat, years), last(sales, years))
    sales_by_year = dict(sales)
    pat_margin = [(y, round(v / sales_by_year[y] * 100, 1))
                  for y, v in pat if sales_by_year.get(y)]

    def growth(seq):
        if len(seq) < 2 or seq[-2][1] == 0:
            return None
        return round((seq[-1][1] - seq[-2][1]) / abs(seq[-2][1]) * 100, 1)

    op_g, pat_g = growth(op), growth(pat)
    opm_delta = (round(opm[-1][1] - opm[-2][1], 1)
                 if len(opm) >= 2 else None)
    patm_delta = (round(pat_margin[-1][1] - pat_margin[-2][1], 1)
                  if len(pat_margin) >= 2 else None)

    # verdict from explicit conditions, every one visible in the table
    ups = sum(1 for g in (op_g, pat_g) if g is not None and g > 8)
    downs = sum(1 for g in (op_g, pat_g) if g is not None and g < 0)
    margin_ok = all(d is None or d > -1.5 for d in (opm_delta, patm_delta))
    if op_g is None and pat_g is None:
        verdict, why = "NO DATA", "too few statement years to compare"
    elif ups == 2 and margin_ok:
        verdict = "RISING"
        why = (f"EBITDA {op_g:+.1f}% and PAT {pat_g:+.1f}% in the latest "
               f"year with margins holding")
    elif downs >= 1 or not margin_ok:
        verdict = "FALLING"
        why = (f"EBITDA {op_g if op_g is not None else '—'}%, "
               f"PAT {pat_g if pat_g is not None else '—'}%, EBITDA-margin "
               f"change {opm_delta if opm_delta is not None else '—'}pp")
    else:
        verdict = "FLAT"
        why = "growing, but not the step-up Darvas looked for"
    return {
        "verdict": verdict, "why": why, "lender_lines": lender,
        "ebitda": op, "ebitda_margin_pct": opm,
        "pat": pat, "pat_margin_pct": pat_margin,
        "ebitda_growth_pct": op_g, "pat_growth_pct": pat_g,
        "ebitda_margin_delta_pp": opm_delta,
        "pat_margin_delta_pp": patm_delta,
    }


# --------------------------------------------------- the new-age call read

def _concall_pdf(sym: str) -> Path:
    return CONCALLS / f"{sym.replace('&', '_AND_')}.pdf"


def _pdf_text(pdf: Path, budget: int = 60000) -> str:
    import PyPDF2
    try:
        reader = PyPDF2.PdfReader(str(pdf), strict=False)
        text = "\n".join((p.extract_text() or "") for p in reader.pages)
    except Exception:
        return ""
    return text[-budget:]          # the latest calls sit at the end


def new_age_verdict(sym: str, allow_ai: bool = True) -> dict:
    """Judge read of the calls: new-age industry, entering one, and the
    earnings-power narrative. Cache hit serves without AI; a miss without
    AI is honestly 'not assessed'."""
    pdf = _concall_pdf(sym)
    if not pdf.exists():
        return {"status": "no_concalls", "new_age": "not assessed",
                "rationale": "no conference-call transcripts on file"}
    stamp = f"{hashlib.md5(pdf.read_bytes()).hexdigest()}:na1:{MODEL}"
    cache = {}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text())
        except Exception:
            cache = {}
    hit = cache.get(sym)
    if hit and hit.get("stamp") == stamp:
        return {"status": "with_calls", **hit["verdict"]}
    if not allow_ai or not shutil.which("claude"):
        return {"status": "ai_unavailable", "new_age": "not assessed",
                "rationale": "no judge available and no cached verdict"}
    excerpt = _pdf_text(pdf)
    if len(excerpt) < 1000:
        return {"status": "no_extractable_text", "new_age": "not assessed",
                "rationale": "transcript text could not be extracted"}
    prompt = (
        f"You are screening {sym} for the Darvas method's second step. "
        "From the conference-call excerpts below, answer STRICT JSON only:\n"
        '{"new_age": "yes"|"entering"|"no", '
        '"theme": "<the industry/theme in <=8 words>", '
        '"earnings_power": "rising"|"flat"|"falling"|"unclear", '
        '"rationale": "1-2 sentences citing the calls", '
        '"quote": "short verbatim quote or empty"}\n'
        "Rules: 'yes' only for genuinely forward-looking industries (or a "
        "clear pivot into one for 'entering') — EVs, renewables, "
        "semiconductors, AI/data infrastructure, digital platforms, "
        "biotech, defence tech and the like; a conventional business "
        "digitising its back office is 'no'. Judge earnings power from "
        "what management actually says about margins, pricing and order "
        "books — never invent.\n\n"
        f"CONFERENCE-CALL EXCERPTS ({sym}):\n{excerpt}"
    )
    proc = subprocess.run(["claude", "-p", "--model", MODEL], input=prompt,
                          capture_output=True, text=True, timeout=None)
    if proc.returncode != 0:
        return {"status": f"judge_failed: {(proc.stderr or '')[-80:]}",
                "new_age": "not assessed", "rationale": ""}
    m = re.search(r"\{.*\}", proc.stdout, re.DOTALL)
    if not m:
        return {"status": "judge_failed: unparseable", "new_age":
                "not assessed", "rationale": ""}
    try:
        verdict = json.loads(m.group(0))
    except json.JSONDecodeError:
        return {"status": "judge_failed: bad json", "new_age":
                "not assessed", "rationale": ""}
    cache[sym] = {"stamp": stamp, "verdict": verdict}
    CACHE.write_text(json.dumps(cache))
    return {"status": "with_calls", **verdict}
