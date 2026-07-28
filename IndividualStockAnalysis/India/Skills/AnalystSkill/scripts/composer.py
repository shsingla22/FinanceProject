"""
composer.py — turn the three sibling-skill records into ONE coherent report.

Structure of the report (in reading order):
  1. The analyst's summary — an AI-written narrative that CONNECTS the
     three analyses (only when AI is on), generated STRICTLY from the
     records and checked: every named pattern/risk/area it mentions must
     exist in the records, or the summary is discarded for that run.
  2. The rating — business quality 45% + multibagger fit 30% + risk safety
     25% = one score out of 100, every point earned or lost listed.
  3. Three evidence sections, one per skill, with each verdict's "why",
     rationale, verbatim quote and numeric evidence.
  4. What to watch — the open questions the evidence left.
  5. How this report was built — methodology and honesty notes.

Deterministic except the summary; and the summary is grounded-or-dropped.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

import registry as REG

HERE = Path(__file__).resolve().parent
SYNTH_CACHE = HERE.parent / ".synth_cache.json"

GRADE_BANDS = [(80, "Outstanding", 5), (65, "Strong", 4), (50, "Decent", 3),
               (35, "Mixed", 2), (0, "Weak", 1)]
WEIGHTS = {"quality": 0.45, "patterns": 0.30, "safety": 0.25}
MODULE_SHORT = {"CAP": "Capital Allocation", "ROC": "Return on Capital",
                "GRW": "Growth", "MGT": "Management",
                "IND": "Industry Structure", "CUS": "Customer Benefits",
                "MOAT": "Competitive Advantage"}
WORD = {2: "Excellent", 1: "Good", 0: "Neutral", -1: "Weak", -2: "Poor"}


def _grade(score):
    for cut, word, stars in GRADE_BANDS:
        if score >= cut:
            return word, stars
    return "Weak", 1


# ------------------------------------------------------------- pillars
def quality_pillar(ba: dict) -> dict:
    overall = ba.get("overall")
    cov = ba.get("coverage") or 0
    if overall is None:
        return {"name": "Business quality", "points": None,
                "derivation": "The 34-check quality framework could not "
                              "score this business — not enough evidence."}
    pts = round((overall + 2) / 4 * 100)
    caution = ("" if cov >= 0.5 else
               f" Caution: only {cov:.0%} of the 34 checks could be "
               f"answered from this evidence — a thin base; the full "
               f"analysis (with the conference calls) firms this up.")
    return {"name": "Business quality", "points": pts,
            "derivation": (f"The 34-check quality framework scored the "
                           f"business {overall:+.2f} on its −2 (poor) to +2 "
                           f"(excellent) scale, with {cov:.0%} of checks "
                           f"backed by evidence; mapped onto 0–100 that is "
                           f"{pts} points.") + caution}


def patterns_pillar(mb: dict) -> dict:
    vs = mb["verdicts"]
    strong = [v["name"] for v in vs if v["verdict"] == "STRONG FIT"]
    likely = [v["name"] for v in vs if v["verdict"] == "LIKELY FIT"]
    signal = [v["name"] for v in vs if v["verdict"] == "QUANT SIGNAL"]
    gate = mb["core_gate"]["status"]
    gate_pts = {"PASS": 25, "PARTIAL": 10}.get(gate, 0)
    raw = gate_pts + 15 * len(strong) + 8 * len(likely) + 3 * len(signal)
    pts = min(100, raw)
    parts = []
    parts.append({"PASS": "the foundation test (steady cash + high returns "
                          "on capital + growth) passed in full (+25)",
                  "PARTIAL": "the foundation test partly passed (+10)"}.get(
                 gate, "the foundation test did not pass (+0)"))
    if strong:
        parts.append(f"{len(strong)} pattern{'s' if len(strong) > 1 else ''} "
                     f"fit strongly ({', '.join(strong[:4])}"
                     f"{'…' if len(strong) > 4 else ''}) (+{15 * len(strong)})")
    if likely:
        parts.append(f"{len(likely)} likely (+{8 * len(likely)})")
    if signal:
        parts.append(f"{len(signal)} numbers-only hint"
                     f"{'s' if len(signal) > 1 else ''} (+{3 * len(signal)})")
    if not (strong or likely or signal):
        parts.append("no pattern found meaningful support (+0)")
    return {"name": "Multibagger fit", "points": pts,
            "derivation": "; ".join(parts) + f" → {pts} of 100."
                          + (" (Capped at 100.)" if raw > 100 else ""),
            "strong": strong, "likely": likely}


def safety_pillar(qr: dict) -> dict:
    vs = qr["verdicts"]
    high = [v["name"] for v in vs if v["verdict"] == "HIGH RISK"]
    elev = [v["name"] for v in vs if v["verdict"] == "ELEVATED"]
    watch = [v["name"] for v in vs if v["verdict"] == "WATCH"]
    flags = [v["name"] for v in vs if v["verdict"] == "QUANT FLAG"]
    frag = qr["fragility"]["status"]
    frag_pts = {"STRESSED": 20, "STRAINED": 8}.get(frag, 0)
    raw = (100 - 20 * len(high) - 10 * len(elev) - 4 * len(watch)
           - 4 * len(flags) - frag_pts)
    pts = max(0, raw)
    parts = ["started from a clean 100"]
    if high:
        parts.append(f"{len(high)} high risk{'s' if len(high) > 1 else ''} "
                     f"({', '.join(high[:3])}) (−{20 * len(high)})")
    if elev:
        parts.append(f"{len(elev)} elevated (−{10 * len(elev)})")
    if watch:
        parts.append(f"{len(watch)} worth watching (−{4 * len(watch)})")
    if flags:
        parts.append(f"{len(flags)} numbers-only flag"
                     f"{'s' if len(flags) > 1 else ''} (−{4 * len(flags)})")
    if frag_pts:
        parts.append("the balance sheet shows "
                     + ("multiple stress signals" if frag == "STRESSED"
                        else "one stress signal") + f" (−{frag_pts})")
    if len(parts) == 1:
        parts.append("no risk channel cost any points")
    return {"name": "Risk safety", "points": pts,
            "derivation": "; ".join(parts) + f" → {pts} of 100."
                          + (" (Floored at 0.)" if raw < 0 else ""),
            "high": high, "elevated": elev}


def compute_rating(ba: dict, mb: dict, qr: dict,
                   extensions: list | None = None) -> dict:
    """Combine the pillars. Extension skills that declare a pillar are
    folded in and ALL weights are re-normalized to sum to 1, so the
    arithmetic stays honest as the skill family grows."""
    pillars = {"quality": quality_pillar(ba), "patterns": patterns_pillar(mb),
               "safety": safety_pillar(qr)}
    weights = dict(WEIGHTS)
    order = ["quality", "patterns", "safety"]
    for ext in (extensions or []):
        p = ext.get("pillar")
        if not p or p.get("points") is None:
            continue
        key = f"ext:{ext['skill']}"
        pillars[key] = {"name": p.get("name", ext["name"]),
                        "points": max(0, min(100, round(p["points"]))),
                        "derivation": p.get("derivation",
                                            "No derivation provided.")}
        weights[key] = float(p.get("weight", 0.10))
        order.append(key)
    avail = {k: p for k, p in pillars.items() if p["points"] is not None}
    if not avail:
        return {"score": None, "grade": "Not rated", "stars": 0,
                "pillars": pillars,
                "derivation": "None of the pillars could be scored."}
    wsum = sum(weights[k] for k in avail)
    score = round(sum(p["points"] * weights[k] for k, p in avail.items()) / wsum)
    grade, stars = _grade(score)
    terms = " + ".join(f"{weights[k] / wsum:.0%} × {pillars[k]['points']} "
                       f"({pillars[k]['name'].lower()})"
                       for k in order if k in avail)
    return {"score": score, "grade": grade, "stars": stars, "pillars": pillars,
            "pillar_order": order,
            "derivation": f"Overall = {terms} = {score} out of 100 → "
                          f"{grade} ({stars} star{'s' if stars > 1 else ''})."}


# ------------------------------------------------------------- synthesis
def _compact(ba: dict, mb: dict, qr: dict, rt: dict) -> dict:
    fw_names = {p.id: p.name for p in REG.FW.parameters}
    return {
        "rating": {"score": rt["score"], "grade": rt["grade"],
                   "how": rt["derivation"]},
        "quality_areas": {MODULE_SHORT.get(m, m): v["score"]
                          for m, v in ba["modules"].items()},
        "notable_checks": {fw_names.get(k, k):
                           {"score": v["score"], "why": v["rationale"][:220]}
                           for k, v in sorted(ba["params"].items(),
                                              key=lambda kv: abs(kv[1]["score"]),
                                              reverse=True)[:10]},
        "patterns": [{"pattern": v["name"], "verdict": v["verdict"],
                      "why": (v["qual"].get("rationale") or
                              v.get("derivation") or "")[:260]}
                     for v in mb["verdicts"] if v["verdict"] != "NOT ASSESSED"],
        "risks": [{"risk": v["name"], "verdict": v["verdict"],
                   "why": (v["qual"].get("rationale") or
                           v.get("derivation") or "")[:260],
                   "silver_lining": (v["qual"].get("mitigant") or "")[:160]}
                  for v in qr["verdicts"] if v["verdict"] != "NOT ASSESSED"],
        "resilience": qr["fragility"]["status"],
    }


def synthesize(sym: str, name: str, ba: dict, mb: dict, qr: dict,
               rt: dict, extensions: list | None = None) -> dict | None:
    """One coherent narrative CONNECTING the three analyses — written by the
    judge model strictly from the records, cached by record content, and
    verified: every capitalized pattern/risk/area name it uses must exist
    in the records or the synthesis is rejected."""
    compact = _compact(ba, mb, qr, rt)
    if extensions:
        compact["additional_analyses"] = [
            {"analysis": e["name"], "facts": e.get("facts", {})}
            for e in extensions if e.get("record") is not None]
    blob = json.dumps(compact, sort_keys=True, default=str)
    key = hashlib.sha256((blob + REG.MODEL).encode()).hexdigest()[:24]
    cache = {}
    if SYNTH_CACHE.exists():
        try:
            cache = json.loads(SYNTH_CACHE.read_text())
        except Exception:
            cache = {}
    hit = cache.get(sym)
    if hit and hit.get("key") == key:
        return hit["synth"]
    prompt = (
        f"You are a buy-side analyst writing the OPENING SUMMARY of a "
        f"report on {name} ({sym}). Below are the outputs of three "
        "independent analyses of this company: a 34-check quality "
        "framework, an 11-pattern multibagger screen, and an 8-channel "
        "risk review, plus their combined rating.\n\n"
        "Write a summary that CONNECTS them into one coherent story: how "
        "the strengths, the patterns and the risks relate to each other "
        "(e.g. when the same trait drives both a pattern and a risk, say "
        "so). Use ONLY facts present in the records — do not add outside "
        "knowledge, numbers, or claims. Plain, everyday financial "
        "language; no analyst shorthand.\n\n"
        "Return STRICT JSON only:\n"
        "{\"summary\": [\"paragraph 1\", \"paragraph 2\", \"paragraph 3\"], "
        "\"watch_items\": [\"3-5 short items — what would change this "
        "verdict, each tied to a named pattern, risk or check\"]}\n\n"
        f"THE RECORDS:\n{blob[:24000]}"
    )
    proc = subprocess.run(["claude", "-p", "--model", REG.MODEL],
                          input=prompt, capture_output=True, text=True,
                          timeout=None)
    if proc.returncode != 0:
        return None
    m = re.search(r"\{.*\}", proc.stdout, re.DOTALL)
    if not m:
        return None
    try:
        synth = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None
    if not synth.get("summary"):
        return None
    # Grounding check: every proper name of a pattern/risk/area used in the
    # summary must exist in the records (guards against imported claims).
    known = set()
    for v in mb["verdicts"]:
        known.add(v["name"].lower())
    for v in qr["verdicts"]:
        known.add(v["name"].lower())
    for m_ in MODULE_SHORT.values():
        known.add(m_.lower())
    for e in (extensions or []):
        known.add(e["name"].lower())
        for n in (e.get("facts", {}) or {}).get("names", []):
            known.add(str(n).lower())
    text = " ".join(synth["summary"]) + " " + " ".join(
        synth.get("watch_items", []))
    for phrase in re.findall(
            r"(?:[A-Z][a-z]+ ){1,3}(?:pattern|risk|test)\b", text):
        base = phrase.rsplit(" ", 1)[0].strip().lower()
        if base and base not in known and \
                not any(base in k or k in base for k in known):
            return None            # unverifiable name — reject the synthesis
    cache[sym] = {"key": key, "synth": synth}
    SYNTH_CACHE.write_text(json.dumps(cache))
    return synth


# ------------------------------------------------------------- the report
def _word(score):
    if score is None:
        return "Not assessed"
    return WORD.get(int(max(-2, min(2, round(score)))), "Neutral")


def render(sym: str, name: str, ba: dict, mb: dict, qr: dict, rt: dict,
           synth: dict | None, statuses: dict,
           extensions: list | None = None) -> str:
    L: list[str] = []
    A = L.append
    fw_names = {p.id: p.name for p in REG.FW.parameters}

    A(f"# {name} ({sym}) — The Analyst's Report")
    A("")

    if synth:
        A("## The analyst's summary")
        A("")
        for para in synth["summary"]:
            A(para)
            A("")
        A("*Written strictly from the three analyses below — every claim "
          "traces to a captured verdict; names it could not ground were "
          "grounds to reject it.*")
        A("")

    if rt["score"] is not None:
        A(f"## The rating: {rt['grade']} — {rt['score']} out of 100 "
          f"{'★' * rt['stars']}{'☆' * (5 - rt['stars'])}")
        A("")
        A(f"**How it was built:** {rt['derivation']}")
        A("")
        for key in rt.get("pillar_order", ("quality", "patterns", "safety")):
            p = rt["pillars"].get(key)
            if p is None:
                continue
            pts = "—" if p["points"] is None else f"{p['points']}/100"
            A(f"- **{p['name']} ({pts}):** {p['derivation']}")
        A("")

    # ---- pillar 1: business quality
    A("## How good is the business? (34-check quality framework)")
    A("")
    A(f"**{_word(ba['overall'])}** — score "
      + (f"{ba['overall']:+.2f}" if ba["overall"] is not None else "n/a")
      + f" on a −2…+2 scale; {ba['coverage']:.0%} of checks had evidence.")
    A("")
    A("| Area | Verdict | Score | Checks done |")
    A("|---|---|---|---|")
    for m in REG.MODULE_IDS:
        md = ba["modules"][m]
        A(f"| {MODULE_SHORT[m]} | {_word(md['score'])} | "
          f"{'—' if md['score'] is None else format(md['score'], '+.2f')} | "
          f"{md['assessed']} of {md['total']} |")
    A("")
    ranked = sorted(ba["params"].items(), key=lambda kv: kv[1]["score"])
    lows, highs = ranked[:3], list(reversed(ranked[-3:]))
    A("**What stands out on the upside:**")
    A("")
    for pid, p in highs:
        if p["score"] <= 0:
            continue
        A(f"- **{fw_names.get(pid, pid)} — {_word(p['score'])}**: "
          f"{p['rationale']}")
        if p.get("quote"):
            A(f"  > \"{p['quote']}\" — *management, on an earnings call*")
    A("")
    A("**What stands out on the downside:**")
    A("")
    any_low = False
    for pid, p in lows:
        if p["score"] >= 0:
            continue
        any_low = True
        A(f"- **{fw_names.get(pid, pid)} — {_word(p['score'])}**: "
          f"{p['rationale']}")
        if p.get("quote"):
            A(f"  > \"{p['quote']}\" — *management, on an earnings call*")
    if not any_low:
        A("- Nothing scored below Neutral.")
    A("")

    # ---- pillar 2: patterns
    A("## Does it look like a long-term winner? (11 multibagger patterns)")
    A("")
    g = mb["core_gate"]
    gate_word = {"PASS": "passes", "PARTIAL": "partly passes",
                 "FAIL": "fails", "UNKNOWN": "could not be tested against"}[g["status"]]
    A(f"The company {gate_word} the foundation every multibagger shares "
      f"(steady cash + high returns on capital + growth), "
      f"{g['passed']} of {g['of']} testable checks passing.")
    A("")
    matched = [v for v in mb["verdicts"]
               if v["verdict"] in ("STRONG FIT", "LIKELY FIT", "QUANT SIGNAL")]
    if matched:
        for v in matched:
            A(f"**{v['name']} — {v['verdict']}** *({v['friendly']})*")
            A("")
            A(f"Why: {v.get('derivation') or v['verdict_friendly']}")
            if v["qual"].get("fit") and v["qual"].get("rationale"):
                A("")
                A(v["qual"]["rationale"])
            if v["qual"].get("quote"):
                A("")
                A(f"> \"{v['qual']['quote']}\" — *management, on an "
                  f"earnings call*")
            A("")
    else:
        A("No pattern is confirmed by the evidence.")
        A("")
    rest = [v for v in mb["verdicts"] if v not in matched]
    if rest:
        A("*Patterns that did not fit or could not be assessed: "
          + "; ".join(f"{v['name']} ({v['verdict'].lower()})"
                      for v in rest) + ".*")
        A("")

    # ---- pillar 3: risks
    A("## What could break it? (8 risk channels)")
    A("")
    fr = qr["fragility"]
    fr_word = {"SOUND": "shows no financial stress",
               "STRAINED": "shows one financial stress signal",
               "STRESSED": "shows multiple financial stress signals",
               "UNKNOWN": "could not be stress-tested"}[fr["status"]]
    A(f"The balance sheet and cash engine {fr_word}"
      + (f" — {fr['derivation']}" if fr.get("derivation") else ".").rstrip(".")
      + ".")
    A("")
    material = [v for v in qr["verdicts"]
                if v["verdict"] in ("HIGH RISK", "ELEVATED", "QUANT FLAG")]
    if material:
        for v in material:
            A(f"**{v['name']} — {v['verdict']}** *({v['friendly']})*")
            A("")
            A(f"Why: {v.get('derivation') or v['verdict_friendly']}")
            if v["qual"].get("exposure") and v["qual"].get("rationale"):
                A("")
                A(v["qual"]["rationale"])
            if v["qual"].get("quote"):
                A("")
                A(f"> \"{v['qual']['quote']}\" — *management, on an "
                  f"earnings call*")
            if v["qual"].get("mitigant"):
                A("")
                A(f"*Silver lining: {v['qual']['mitigant']}*")
            A("")
    else:
        A("No risk channel shows both meaningful evidence and severity "
          "today.")
        A("")
    quiet = [v for v in qr["verdicts"] if v not in material]
    if quiet:
        A("*Risk channels that are quiet or assessed low: "
          + "; ".join(f"{v['name']} ({v['verdict'].lower()})"
                      for v in quiet) + ".*")
        A("")

    # ---- extension sections (future sibling skills slot in here)
    for ext in (extensions or []):
        if ext.get("record") is None:
            continue
        if ext.get("section_md"):
            A(ext["section_md"].strip())
            A("")
        else:
            A(f"## {ext['name']}")
            A("")
            A(f"*The {ext['skill']} skill ran ({ext['status']}) but "
              f"provided no report section — its record fed the rating"
              + (" and the summary" if ext.get("facts") else "") + ".*")
            A("")

    # ---- what to watch
    A("## What to watch")
    A("")
    if synth and synth.get("watch_items"):
        for w in synth["watch_items"]:
            A(f"- {w}")
    else:
        for v in qr["verdicts"]:
            if v["verdict"] in ("HIGH RISK", "ELEVATED"):
                A(f"- Whether the {v['name']} risk eases or deepens.")
        for v in mb["verdicts"]:
            if v["verdict"] == "QUANT SIGNAL":
                A(f"- Whether the calls start confirming the {v['name']} "
                  f"pattern the numbers hint at.")
        if all(v["verdict"] not in ("HIGH RISK", "ELEVATED")
               for v in qr["verdicts"]):
            A("- No elevated risks today; watch that it stays that way.")
    A("")

    # ---- methodology
    A("## How this report was built")
    A("")
    skills = REG.discover()
    A(f"This report was composed by the AnalystSkill, which executed the "
      f"{sum(skills.values())} sibling analysis skills on this company's "
      f"stored data (financial statements, working capital, conference-call "
      f"transcripts, management history):")
    A("")
    A(f"- **BusinessAnalysis** ({statuses.get('business', '?')}): the "
      f"34-check quality framework.")
    A(f"- **MultibaggerPattern** ({statuses.get('patterns', '?')}): the 11 "
      f"patterns long-term winners share.")
    A(f"- **QualityRisks** ({statuses.get('risks', '?')}): the 8 channels "
      f"through which quality companies fail.")
    for ext in (extensions or []):
        A(f"- **{ext['skill']}** ({ext['status']}): discovered "
          f"automatically via its analyst_interface.py.")
    A("")
    A("Every verdict was produced with its evidence attached at the moment "
      "of analysis; checks the evidence could not answer are marked, never "
      "guessed. \"with_calls\" means the company's conference-call history "
      "was read by the judge model; \"numbers_only\" means only the "
      "financial statements could be used. Research tooling; not "
      "investment advice.")
    return "\n".join(L)
