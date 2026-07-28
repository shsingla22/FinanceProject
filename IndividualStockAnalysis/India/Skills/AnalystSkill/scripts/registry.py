"""
registry.py — discover and execute the sibling skills.

The AnalystSkill does no analysis of its own: it RUNS the other skills in
the Skills/ folder — BusinessAnalysis (34-check quality framework),
MultibaggerPattern (11 winning patterns) and QualityRisks (8 failure
channels) — and hands their explainable records to the composer.

Each sibling keeps its own judgement rules and its own disk cache; this
module only orchestrates. The judge model for every skill is steered by
one env var, ANALYST_MODEL (default Opus 5 / claude-opus-5).
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parent.parent            # .../Skills
INDIA = SKILLS.parent                  # .../India
REPO = INDIA.parent.parent

MODEL = os.environ.get("ANALYST_MODEL", "claude-opus-5")
# Steer the sibling skills' judges to the same model BEFORE loading them.
os.environ.setdefault("MB_JUDGE_MODEL", MODEL)
os.environ.setdefault("RISK_JUDGE_MODEL", MODEL)

sys.path.insert(0, str(SKILLS / "BusinessAnalysis" / "scripts"))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# BusinessAnalysis pieces (unique module names — plain imports are safe)
import quant_signals as Q        # noqa: E402
import scoring as SC             # noqa: E402
import framework as FWK          # noqa: E402

# The quant->score mapping with humanized rationales is the shared library
# in UserInterface/build_data.py — one source of truth for the wording.
BD = _load("analyst_build_data", REPO / "UserInterface" / "build_data.py")

# The two judge-bearing siblings both call their entry point analyze.py, so
# they are loaded under unique names; their engine imports keep their own
# unique real names (pattern_engine, quant_evidence, risk_engine, ...).
MB_AZ = _load("mb_analyze", SKILLS / "MultibaggerPattern" / "scripts" / "analyze.py")
QR_AZ = _load("qr_analyze", SKILLS / "QualityRisks" / "scripts" / "analyze.py")
MB_PE = sys.modules["pattern_engine"]
MB_QE = sys.modules["quant_evidence"]
QR_RE = sys.modules["risk_engine"]
QR_QE = sys.modules["risk_evidence"]

FW = FWK.load_framework()
MODULE_IDS = [m.id for m in FW.modules]

_mb_lock = threading.Lock()
_qr_lock = threading.Lock()
_ba_lock = threading.Lock()

BA_CACHE = HERE.parent / ".qual_cache.json"


def discover() -> dict:
    """Which sibling skills exist and are wired in — used by tests and the
    report's methodology section."""
    return {
        "BusinessAnalysis": (SKILLS / "BusinessAnalysis" / "SKILL.md").exists(),
        "MultibaggerPattern": (SKILLS / "MultibaggerPattern" / "SKILL.md").exists(),
        "QualityRisks": (SKILLS / "QualityRisks" / "SKILL.md").exists(),
    }


# ------------------------------------------------------------ extensions
# EXTENSIBILITY CONTRACT: any FUTURE sibling skill becomes part of the
# analyst's report automatically by shipping a file named
# `analyst_interface.py` in its folder, exposing:
#
#     def run(symbol: str, ai: bool = True) -> dict
#
# returning at least {"name": str, "status": str, "record": dict} and
# optionally:
#     "order":      int   — where its section sits (built-ins are 10/20/30;
#                            default 100 = after them)
#     "pillar":     {"name": str, "points": 0-100 | None,
#                    "derivation": str, "weight": float}
#                          — folded into the combined rating, with all
#                            weights re-normalized to sum to 1
#     "section_md": str   — the skill's own Markdown section (headings at
#                            "## " level), embedded verbatim in the report
#     "facts":      dict  — compact facts fed to the analyst's-summary
#                            synthesis (and to its grounding vocabulary via
#                            a "names" list, if provided)
#
# The three built-in skills are wired natively (in that fixed order:
# business quality -> multibagger patterns -> risks); extensions run after
# them. A broken extension is reported in the methodology section, never
# silently dropped and never allowed to sink the report.
BUILTIN_FOLDERS = {"AnalystSkill", "BusinessAnalysis", "MultibaggerPattern",
                   "QualityRisks"}


def discover_extensions(skills_dir: Path | None = None) -> list[dict]:
    """Future sibling skills that ship an analyst_interface.py."""
    base = skills_dir or SKILLS
    out = []
    for d in sorted(base.iterdir()):
        if not d.is_dir() or d.name in BUILTIN_FOLDERS:
            continue
        iface = d / "analyst_interface.py"
        if iface.exists():
            out.append({"skill": d.name, "path": iface})
    return out


def run_extensions(sym: str, ai: bool = True,
                   skills_dir: Path | None = None) -> list[dict]:
    """Execute every discovered extension. Failures are captured as a
    status, not raised — one broken extension must not sink the report."""
    results = []
    for ext in discover_extensions(skills_dir):
        try:
            mod = _load(f"analyst_ext_{ext['skill']}", ext["path"])
            res = mod.run(sym, ai=ai)
            if not isinstance(res, dict) or "record" not in res:
                raise ValueError("run() must return a dict with 'record'")
            res.setdefault("name", ext["skill"])
            res.setdefault("status", "ok")
            res.setdefault("order", 100)
            res["skill"] = ext["skill"]
            results.append(res)
        except Exception as e:
            results.append({"skill": ext["skill"], "name": ext["skill"],
                            "status": f"failed: {str(e)[:120]}",
                            "record": None, "order": 100})
    results.sort(key=lambda r: (r.get("order", 100), r["skill"]))
    return results


# ------------------------------------------------- BusinessAnalysis pillar
def _ba_qual_prompt(sym: str) -> str | None:
    excerpt, n_calls, rng = MB_AZ._timeline_excerpt(sym)
    if not excerpt:
        return None
    params = [p for p in FW.parameters if p.nature in ("qualitative", "hybrid")]
    plist = "\n".join(f"- {p.id}: {p.name} — {p.signal}" for p in params)
    return (
        "You are scoring a company against a quality-investing framework "
        f"using excerpts from {n_calls} quarterly earnings calls ({rng}, "
        "oldest first) and its 5-year management history. Judge the "
        "trajectory — delivery vs promises across the years — not one "
        "quarter. Score each parameter -2..+2 when the evidence supports a "
        "judgement; null ONLY when genuinely silent. Never guess — every "
        "score must cite its evidence.\n\n"
        f"Parameters:\n{plist}\n\n"
        "Return STRICT JSON only: {\"scores\": [{\"id\": ..., "
        "\"score\": int|null, \"rationale\": \"1 sentence citing the "
        "evidence\", \"quote\": \"short verbatim quote or empty\"}]}\n\n"
        f"MANAGEMENT HISTORY ({sym}):\n{MB_AZ._mgmt_lines(sym)}\n\n"
        f"CONFERENCE-CALL EXCERPTS ({sym}):\n{excerpt}"
    )


def _ba_qual_scores(sym: str) -> list | None:
    """AI concall scores for the framework's qualitative/hybrid parameters,
    cached on disk keyed by transcript mtime + model. No timeout."""
    pdf = INDIA / "ConferenceCalls" / "NiftyTotalMarket" / f"{sym.replace('&', '_AND_')}.pdf"
    if not pdf.exists():
        return None
    stamp = f"{pdf.stat().st_mtime}:ba1:{MODEL}"
    cache = {}
    if BA_CACHE.exists():
        try:
            cache = json.loads(BA_CACHE.read_text())
        except Exception:
            cache = {}
    hit = cache.get(sym)
    if hit and hit.get("stamp") == stamp:
        return hit["scores"]
    prompt = _ba_qual_prompt(sym)
    if prompt is None:
        return None
    proc = subprocess.run(["claude", "-p", "--model", MODEL], input=prompt,
                          capture_output=True, text=True, timeout=None)
    if proc.returncode != 0:
        raise RuntimeError("claude CLI failed: " + (proc.stderr or "")[-300:])
    m = re.search(r"\{.*\}", proc.stdout, re.DOTALL)
    if not m:
        raise RuntimeError("could not parse judge output")
    try:
        scores = json.loads(m.group(0)).get("scores", [])
    except json.JSONDecodeError:
        scores = []
        for it in re.findall(r'\{[^{}]*"id"\s*:\s*"[^"]+"[^{}]*\}', m.group(0)):
            try:
                scores.append(json.loads(it))
            except json.JSONDecodeError:
                continue
    cache[sym] = {"stamp": stamp, "scores": scores}
    BA_CACHE.write_text(json.dumps(cache))
    return scores


def run_business(sym: str, ai: bool = True) -> tuple[dict, str]:
    """Execute the BusinessAnalysis skill: quant signals + scoring, fused
    with the concall judge per the skill's hybrid rule."""
    sig = Q.compute(sym, base=INDIA, universe="NiftyTotalMarket")
    pscores = BD.score_params(sig, FW)
    status = "numbers_only"
    qual = None
    if ai:
        try:
            with _ba_lock:
                qual = _ba_qual_scores(sym)
            status = "with_calls" if qual else "no_concalls"
        except Exception as e:
            status = f"judge_failed: {str(e)[:120]}"
    meta = {}
    if qual:
        valid = {p.id for p in FW.parameters}
        by_id = {p.id: p for p in pscores}
        for s in qual:
            pid = s.get("id")
            if pid not in valid or s.get("score") is None:
                continue
            a = int(max(-2, min(2, s["score"])))
            tgt = by_id.get(pid)
            if tgt is None:
                continue
            if tgt.score is not None:            # hybrid: fuse, keep both
                tgt.rationale = (f"{tgt.rationale} And from the calls: "
                                 f"{s.get('rationale', '')}")
                tgt.score = int(max(-2, min(2, round((tgt.score + a) / 2))))
                meta[pid] = {"source": "fused", "quote": s.get("quote", "")}
            else:
                tgt.score = a
                tgt.rationale = s.get("rationale", "")
                meta[pid] = {"source": "calls", "quote": s.get("quote", "")}
    agg = SC.aggregate(pscores, MODULE_IDS)
    rec = {
        "overall": agg["overall_score"],
        "coverage": agg["overall_coverage"],
        "modules": {m: {"score": agg["modules"][m]["module_score"],
                        "assessed": agg["modules"][m]["n_assessed"],
                        "total": agg["modules"][m]["n_total"]}
                    for m in MODULE_IDS},
        "params": {p.id: {"score": p.score, "rationale": p.rationale,
                          "module": p.module,
                          **meta.get(p.id, {})}
                   for p in pscores if p.score is not None},
        "qualitative_included": bool(qual),
    }
    return rec, status


# --------------------------------------------- pattern and risk pillars
def run_patterns(sym: str, ai: bool = True) -> tuple[dict, str]:
    checks = MB_QE.compute_checks(sym)
    qual, status = None, "numbers_only"
    if ai:
        try:
            with _mb_lock:
                qual = MB_AZ.qual_judge(sym, MB_PE.load_taxonomy())
            status = "with_calls" if qual else "no_concalls"
        except Exception as e:
            status = f"judge_failed: {str(e)[:120]}"
    return MB_PE.analyse(sym, checks, qual), status


def run_risks(sym: str, ai: bool = True) -> tuple[dict, str]:
    checks = QR_QE.compute_checks(sym)
    qual, status = None, "numbers_only"
    if ai:
        try:
            with _qr_lock:
                qual = QR_AZ.qual_judge(sym, QR_RE.load_taxonomy())
            status = "with_calls" if qual else "no_concalls"
        except Exception as e:
            status = f"judge_failed: {str(e)[:120]}"
    return QR_RE.analyse(sym, checks, qual), status


def company_name(sym: str) -> str:
    return company_meta(sym)["name"]


def company_meta(sym: str) -> dict:
    import pandas as pd
    const = pd.read_csv(INDIA / "NiftyTotalMarket"
                        / "niftytotalmarket_constituents.csv")
    row = const[const.nse_symbol == sym]
    if not len(row):
        return {"name": sym, "industry": ""}
    ind = row.iloc[0].industry if "industry" in row.columns else ""
    return {"name": str(row.iloc[0].company_name),
            "industry": str(ind) if isinstance(ind, str) else ""}


def trend_series(sym: str) -> dict:
    """Yearly series WITH their FY labels, for the report's charts. Each
    metric carries its own years so mismatched histories can't misalign."""
    frames = MB_QE._load(INDIA, "NiftyTotalMarket")

    def with_years(df, item, value_col, item_col="line_item"):
        if df.empty:
            return [], []
        sub = df[(df["nse_symbol"] == sym) & (df[item_col] == item)]
        if sub.empty:
            return [], []
        sub = sub.sort_values("year", key=lambda s: s.map(MB_QE._year_key))
        years, vals = [], []
        for _, r in sub.iterrows():
            v = r[value_col]
            try:
                v = float(v)
                if v != v:          # NaN
                    continue
            except (TypeError, ValueError):
                continue
            years.append(re.sub(r"^[A-Z][a-z]{2}\s+", "FY", str(r["year"])))
            vals.append(v)
        return years, vals

    out = {}
    for key, (frame, item, col, icol) in {
        "sales": ("pl", "Sales", "value", "line_item"),
        "opm": ("pl", "OPM %", "value", "line_item"),
        "roce": ("wc", "ROCE %", "value", "metric"),
        "ccc": ("wc", "Cash Conversion Cycle", "value", "metric"),
    }.items():
        years, vals = with_years(frames[frame], item, col, icol)
        out[key] = {"years": years, "values": vals}
    return out
