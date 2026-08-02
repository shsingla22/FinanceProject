"""
carry.py — the carry-forward policy for the one-year lens.

Where the one-year window genuinely cannot judge something — a trend
check that needs longer history, or a topic the last four calls never
mention — the verdict is NOT left as "not assessed": the full-history
AnalystSkill's verdict for that item is carried forward UNCHANGED and
clearly labeled as carried. The one-year picture stays complete, and the
ComparisonSkill can treat those items as "unchanged by construction"
instead of "not comparable".

Explainability rule: every carried item says so, in its own text —
nothing carried is ever presentable as a fresh one-year judgement.

The full-history record comes from the AnalystSkill's own CLI in a
subprocess (matching quick/AI mode), so the two engines never share an
interpreter and each side's caches stay intact.
"""

from __future__ import annotations

import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parent.parent

CARRY_BA = ("Carried forward from the full-history analysis — the "
            "one-year window could not re-test this: ")
CARRY_V = ("carried forward from the full-history analysis (the one-year "
           "window could not assess this) — ")
CARRY_CHECK = " (Carried forward from the full-history analysis.)"


def fetch_full(sym: str, ai: bool) -> dict:
    cmd = [sys.executable,
           str(SKILLS / "AnalystSkill" / "scripts" / "analyze.py"),
           "company", sym]
    if not ai:
        cmd.append("--quick")
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=None)
    if proc.returncode != 0:
        raise RuntimeError("full-history side failed: "
                           + (proc.stderr or "")[-300:])
    return json.loads(proc.stdout)


def _merge_business(wb: dict, fb: dict, weights: dict) -> int:
    """Fill silent checks from the full record; recompute aggregates."""
    carried = 0
    for pid, fp in fb.get("params", {}).items():
        if pid not in wb["params"] and fp.get("score") is not None:
            wb["params"][pid] = {**deepcopy(fp), "source": "carried",
                                 "rationale": CARRY_BA + fp["rationale"]}
            carried += 1
    by_mod: dict = {}
    for p in wb["params"].values():
        by_mod.setdefault(p.get("module"), []).append(p["score"])
    n_assessed = 0
    for m, d in wb["modules"].items():
        scores = by_mod.get(m, [])
        d["score"] = (sum(scores) / len(scores)) if scores else None
        d["assessed"] = len(scores)
        n_assessed += len(scores)
    n_total = sum(d["total"] for d in wb["modules"].values()) or 1
    wb["coverage"] = n_assessed / n_total
    scored = [(d["score"], weights.get(m, 1.0))
              for m, d in wb["modules"].items() if d["score"] is not None]
    wb["overall"] = (sum(s * w for s, w in scored)
                     / sum(w for _, w in scored)) if scored else None
    return carried


def _merge_ladder(wrec: dict, frec: dict, id_key: str, order: list) -> int:
    """Replace NOT ASSESSED verdicts with the full-history verdicts,
    labeled; resort on the ladder."""
    carried = 0
    fmap = {v[id_key]: v for v in frec["verdicts"]}
    for i, v in enumerate(wrec["verdicts"]):
        fv = fmap.get(v[id_key])
        if v["verdict"] == "NOT ASSESSED" and fv is not None \
                and fv["verdict"] != "NOT ASSESSED":
            nv = deepcopy(fv)
            nv["carried_forward"] = True
            nv["derivation"] = CARRY_V + (fv.get("derivation")
                                          or fv.get("verdict_friendly", ""))
            wrec["verdicts"][i] = nv
            carried += 1
    pos = {v: i for i, v in enumerate(order)}
    wrec["verdicts"].sort(key=lambda v: pos.get(v["verdict"], len(order)))
    return carried


def _merge_checks_list(wrows: list, frows: list, flag_key: str) -> list:
    """Merge gate/fragility check rows: fill unknowns from the full side."""
    fmap = {r["check"]: r for r in frows}
    out = []
    for r in wrows:
        fr = fmap.get(r["check"])
        if r.get(flag_key) is None and fr is not None \
                and fr.get(flag_key) is not None:
            nr = deepcopy(fr)
            nr["explanation"] = fr["explanation"].rstrip() + CARRY_CHECK
            out.append(nr)
        else:
            out.append(r)
    return out


def merge(windowed: dict, full: dict, AR, AC) -> dict:
    """The carried-forward one-year record (windowed values always win;
    the full record only fills what the window could not judge)."""
    out = deepcopy(windowed)
    weights = AR.SC.DEFAULT_MODULE_WEIGHTS
    n_ba = _merge_business(out["business"], full["business"], weights)

    # patterns: verdicts + foundation gate
    n_mb = _merge_ladder(out["patterns"], full["patterns"], "pattern",
                         AR.MB_PE.VERDICTS)
    gate_rows = _merge_checks_list(out["patterns"]["core_gate"]["checks"],
                                   full["patterns"]["core_gate"]["checks"],
                                   "passed")
    known = [r for r in gate_rows if r.get("passed") is not None]
    passed = sum(1 for r in known if r["passed"])
    out["patterns"]["core_gate"] = {
        "status": ("PASS" if known and passed == len(known) else
                   "PARTIAL" if passed > 0 else
                   "FAIL" if known else "UNKNOWN"),
        "passed": passed, "of": len(known), "checks": gate_rows}
    out["patterns"]["matched_patterns"] = [
        v["pattern"] for v in out["patterns"]["verdicts"]
        if v["verdict"] in ("STRONG FIT", "LIKELY FIT", "QUANT SIGNAL")]

    # risks: verdicts + fragility
    n_qr = _merge_ladder(out["risks"], full["risks"], "risk",
                         AR.QR_RE.SEVERITY_ORDER)
    frag_rows = _merge_checks_list(out["risks"]["fragility"]["checks"],
                                   full["risks"]["fragility"]["checks"],
                                   "flagged")
    checks_dict = {r["check"]: {"flagged": r["flagged"],
                                "explanation": r["explanation"]}
                   for r in frag_rows}
    out["risks"]["fragility"] = AR.QR_RE.fragility(
        checks_dict, AR.QR_RE.load_taxonomy())
    out["risks"]["material_risks"] = [
        v["risk"] for v in out["risks"]["verdicts"]
        if v["verdict"] in ("HIGH RISK", "ELEVATED", "QUANT FLAG")]

    # the rating, recomputed over the completed records
    out["rating"] = AC.compute_rating(out["business"], out["patterns"],
                                      out["risks"],
                                      extensions=out.get("extensions"))
    out["carried"] = {"business_checks": n_ba, "patterns": n_mb,
                      "risks": n_qr}
    return out
