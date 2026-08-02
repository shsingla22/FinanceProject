"""
compare_engine.py — compare the AnalystSkill (full history) with the
RecentAnalystSkill (last one year) for one company.

The two views answer different questions — "what has this business been
over the long run?" vs "what does it look like RIGHT NOW?" — and the
comparison answers the third: "is it improving or regressing?"

HONEST-COMPARISON RULES (enforced everywhere, stated in the report):
  - only items assessed on BOTH sides are compared;
  - items the one-year lens silences by design (trend checks that need
    longer history) are listed separately as "not comparable in the
    window" — they are NEVER counted as regressions;
  - every improvement/regression line carries both sides' evidence, so
    the reader sees WHY the verdict moved, not just that it moved.

Each side is produced by its own skill's CLI in a SUBPROCESS (the
one-year skill windows its engines in-process, so the two must never
share an interpreter); their AI judge caches are reused automatically.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILLS = HERE.parent.parent
sys.path.insert(0, str(SKILLS / "BusinessAnalysis" / "scripts"))

import framework as FWK      # noqa: E402  (inert: names for the 34 checks)

FW = FWK.load_framework()
PARAM_NAME = {p.id: p.name for p in FW.parameters}
PARAM_MODULE = {p.id: p.module for p in FW.parameters}
MODULE_SHORT = {"CAP": "Capital Allocation", "ROC": "Return on Capital",
                "GRW": "Growth", "MGT": "Management",
                "IND": "Industry Structure", "CUS": "Customer Benefits",
                "MOAT": "Competitive Advantage"}
MODULE_IDS = list(MODULE_SHORT)
WORD = {2: "Excellent", 1: "Good", 0: "Neutral", -1: "Weak", -2: "Poor"}

# ladder positions: LOWER index = better fit / worse risk
MB_ORDER = ["STRONG FIT", "LIKELY FIT", "QUANT SIGNAL", "PARTIAL",
            "NO FIT", "NOT ASSESSED"]
QR_ORDER = ["HIGH RISK", "ELEVATED", "WATCH", "QUANT FLAG", "LOW",
            "NO SIGNAL", "NOT ASSESSED"]


def _word(score):
    if score is None:
        return "not assessed"
    return WORD.get(int(max(-2, min(2, round(score)))), "Neutral")


# ------------------------------------------------------------ run the sides
def run_analysis(sym: str, which: str, ai: bool = True) -> dict:
    """One side's combined record via its skill's own CLI (subprocess)."""
    folder = {"full": "AnalystSkill", "recent": "RecentAnalystSkill"}[which]
    cmd = [sys.executable, str(SKILLS / folder / "scripts" / "analyze.py"),
           "company", sym]
    if not ai:
        cmd.append("--quick")
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=None)
    if proc.returncode != 0:
        raise RuntimeError(f"{folder} failed for {sym}: "
                           + (proc.stderr or "")[-300:])
    return json.loads(proc.stdout)


# ------------------------------------------------------------- comparison
def _rating_delta(full: dict, recent: dict) -> dict:
    f, r = full["rating"], recent["rating"]
    if f["score"] is None or r["score"] is None:
        return {"full": f, "recent": r, "delta": None,
                "direction": "not comparable",
                "derivation": ("The two views cannot be compared on the "
                               "overall rating: "
                               + ("the long view could not be rated. "
                                  if f["score"] is None else "")
                               + ("the one-year view could not be rated "
                                  "(too little was assessable in the "
                                  "window)." if r["score"] is None else ""))}
    delta = r["score"] - f["score"]
    direction = ("improved" if delta > 2 else
                 "declined" if delta < -2 else "held steady")
    verb = {"improved": "looks STRONGER than", "declined": "looks WEAKER than",
            "held steady": "looks in line with"}[direction]
    return {"full": {"score": f["score"], "grade": f["grade"],
                     "derivation": f["derivation"]},
            "recent": {"score": r["score"], "grade": r["grade"],
                       "derivation": r["derivation"]},
            "delta": delta, "direction": direction,
            "derivation": (
                f"Long-term view: {f['grade']} ({f['score']}/100). "
                f"Last one year: {r['grade']} ({r['score']}/100). "
                f"The last year {verb} the long-term picture "
                f"({delta:+d} points) — the company has {direction} "
                f"in the recent period.")}


def _pillar_deltas(full: dict, recent: dict) -> list:
    out = []
    for key in ("quality", "patterns", "safety"):
        fp = full["rating"]["pillars"].get(key, {})
        rp = recent["rating"]["pillars"].get(key, {})
        fpts, rpts = fp.get("points"), rp.get("points")
        out.append({"pillar": fp.get("name") or rp.get("name") or key,
                    "full": fpts, "recent": rpts,
                    "delta": (rpts - fpts) if None not in (fpts, rpts)
                             else None,
                    "full_why": fp.get("derivation", ""),
                    "recent_why": rp.get("derivation", "")})
    return out


def _compare_business(full: dict, recent: dict) -> dict:
    fb, rb = full["business"], recent["business"]
    areas = []
    for m in MODULE_IDS:
        fs = fb["modules"].get(m, {}).get("score")
        rs = rb["modules"].get(m, {}).get("score")
        areas.append({"area": MODULE_SHORT[m],
                      "full": fs, "full_word": _word(fs),
                      "recent": rs, "recent_word": _word(rs),
                      "delta": (rs - fs) if None not in (fs, rs) else None})
    improved, regressed, unchanged, window_excluded, newly = [], [], [], [], []
    for pid in {p.id for p in FW.parameters}:
        f = fb["params"].get(pid)
        r = rb["params"].get(pid)
        name = PARAM_NAME.get(pid, pid)
        if f and r:
            d = r["score"] - f["score"]
            item = {"check": name, "area": MODULE_SHORT.get(
                        PARAM_MODULE.get(pid, ""), ""),
                    "full": f["score"], "full_word": _word(f["score"]),
                    "recent": r["score"], "recent_word": _word(r["score"]),
                    "delta": d,
                    "explanation": (
                        f"Now: {r['rationale']}"
                        + (f" | The long view had said: {f['rationale']}"
                           if d != 0 else ""))}
            (improved if d > 0 else regressed if d < 0
             else unchanged).append(item)
        elif f and not r:
            window_excluded.append({"check": name,
                                    "full_word": _word(f["score"]),
                                    "note": "assessable only with longer "
                                            "history — silenced by the "
                                            "one-year lens, not a "
                                            "regression"})
        elif r and not f:
            newly.append({"check": name, "recent_word": _word(r["score"]),
                          "explanation": r["rationale"]})
    for bucket in (improved, regressed):
        bucket.sort(key=lambda x: -abs(x["delta"]))
    n_cmp = len(improved) + len(regressed) + len(unchanged)
    nw = len(window_excluded)
    overall = (
        f"Of the 34 quality checks, {n_cmp} could be compared on both "
        f"views: {len(improved)} improved, {len(regressed)} regressed, "
        f"{len(unchanged)} unchanged. {nw} check{'s' if nw != 1 else ''} "
        f"need{'s' if nw == 1 else ''} longer history than the one-year "
        f"lens allows (listed, not counted), and {len(newly)} "
        f"{'was' if len(newly) == 1 else 'were'} newly assessable in the "
        f"recent view.")
    return {"areas": areas, "improved": improved, "regressed": regressed,
            "unchanged": unchanged, "window_excluded": window_excluded,
            "newly_visible": newly, "overall": overall,
            "full_overall": fb["overall"], "recent_overall": rb["overall"]}


def _transitions(full_verdicts: list, recent_verdicts: list, order: list,
                 better_is_lower: bool) -> dict:
    """Verdict transitions for patterns (lower index = better) or risks
    (lower index = MORE severe, so improvement = moving to higher index)."""
    fmap = {v["pattern" if "pattern" in v else "risk"]: v
            for v in full_verdicts}
    rmap = {v["pattern" if "pattern" in v else "risk"]: v
            for v in recent_verdicts}
    improved, regressed, unchanged, not_comparable = [], [], [], []
    for key, fv in fmap.items():
        rv = rmap.get(key)
        if rv is None:
            continue
        f_v, r_v = fv["verdict"], rv["verdict"]
        item = {"name": fv["name"], "from": f_v, "to": r_v,
                "why_now": rv.get("derivation", ""),
                "then": (fv.get("qual") or {}).get("rationale", "")
                        or fv.get("derivation", ""),
                "now": (rv.get("qual") or {}).get("rationale", "")
                       or rv.get("derivation", "")}
        if f_v == "NOT ASSESSED" or r_v == "NOT ASSESSED":
            item["note"] = ("could not be assessed on "
                            + ("either view" if f_v == r_v else
                               "the one-year view (window design or "
                               "silent recent calls)" if r_v ==
                               "NOT ASSESSED" else "the long view"))
            not_comparable.append(item)
            continue
        fi, ri = order.index(f_v), order.index(r_v)
        moved_better = ri < fi if better_is_lower else ri > fi
        moved_worse = ri > fi if better_is_lower else ri < fi
        (improved if moved_better else regressed if moved_worse
         else unchanged).append(item)
    return {"improved": improved, "regressed": regressed,
            "unchanged": unchanged, "not_comparable": not_comparable}


def _compare_patterns(full: dict, recent: dict) -> dict:
    t = _transitions(full["patterns"]["verdicts"],
                     recent["patterns"]["verdicts"],
                     MB_ORDER, better_is_lower=True)
    fm = full["patterns"]["matched_patterns"]
    rm = recent["patterns"]["matched_patterns"]
    t["overall"] = (
        f"The long view matches {len(fm)} of the 11 winning patterns; the "
        f"one-year view matches {len(rm)}. Comparable pattern verdicts: "
        f"{len(t['improved'])} strengthened, {len(t['regressed'])} "
        f"weakened, {len(t['unchanged'])} unchanged; "
        f"{len(t['not_comparable'])} could not be compared.")
    t["gate_full"] = full["patterns"]["core_gate"]["status"]
    t["gate_recent"] = recent["patterns"]["core_gate"]["status"]
    return t


def _compare_risks(full: dict, recent: dict) -> dict:
    t = _transitions(full["risks"]["verdicts"], recent["risks"]["verdicts"],
                     QR_ORDER, better_is_lower=False)
    ff = full["risks"]["fragility"]["status"]
    rf = recent["risks"]["fragility"]["status"]
    t["fragility"] = {"full": ff, "recent": rf,
                      "full_why": full["risks"]["fragility"].get(
                          "derivation", ""),
                      "recent_why": recent["risks"]["fragility"].get(
                          "derivation", "")}
    t["overall"] = (
        f"Comparable risk verdicts: {len(t['improved'])} eased, "
        f"{len(t['regressed'])} worsened, {len(t['unchanged'])} unchanged; "
        f"{len(t['not_comparable'])} could not be compared. Financial "
        f"resilience: {ff.title()} on the long view, {rf.title()} on the "
        f"one-year view.")
    return t


def compare(sym: str, full: dict, recent: dict) -> dict:
    """The full explainable comparison record."""
    return {
        "symbol": sym,
        "rating": _rating_delta(full, recent),
        "pillars": _pillar_deltas(full, recent),
        "business": _compare_business(full, recent),
        "patterns": _compare_patterns(full, recent),
        "risks": _compare_risks(full, recent),
        "statuses": {"full": full["statuses"],
                     "recent": recent["statuses"]},
    }
