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
    if mb["core_gate"]["of"] <= 1 and not (strong or likely or signal):
        return {"name": "Multibagger fit", "points": None,
                "derivation": f"The foundation test was essentially "
                              f"untestable (only {mb['core_gate']['of']} of "
                              f"its 3 checks had data) and no pattern shows "
                              f"any evidence — this pillar is left unscored "
                              f"rather than guessed.",
                "strong": [], "likely": []}
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
    tested = [v for v in vs if v["verdict"] != "NOT ASSESSED"]
    if not tested and frag == "UNKNOWN":
        return {"name": "Risk safety", "points": None,
                "derivation": "None of the eight risk channels could be "
                              "tested — an untested company is not a safe "
                              "one, so this pillar is left unscored rather "
                              "than given a perfect mark.",
                "high": [], "elevated": []}
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
    synth = None
    for attempt in range(2):        # one retry: broken JSON / a CLI blip
        proc = subprocess.run(["claude", "-p", "--model", REG.MODEL],
                              input=prompt, capture_output=True, text=True,
                              timeout=None)
        if proc.returncode != 0:
            continue
        m = re.search(r"\{.*\}", proc.stdout, re.DOTALL)
        if not m:
            continue
        try:
            candidate = json.loads(m.group(0))
        except json.JSONDecodeError:
            continue
        if candidate.get("summary"):
            synth = candidate
            break
    if synth is None:
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
    STOP = {"the", "a", "an", "this", "that", "its", "each", "one", "no",
            "any", "every", "both", "another", "same", "such", "which"}
    for phrase in re.findall(
            r"(?:[A-Z][a-z]+ ){1,3}(?:pattern|risk|test)\b", text):
        words = [w for w in phrase.rsplit(" ", 1)[0].strip().split()
                 if w.lower() not in STOP]
        base = " ".join(words).lower()
        if base and base not in known and \
                not any(base in k or k in base for k in known):
            return None            # unverifiable name — reject the synthesis
    cache[sym] = {"key": key, "synth": synth}
    SYNTH_CACHE.write_text(json.dumps(cache))
    return synth


# ------------------------------------------------------------- the report
OVERVIEW_CACHE = HERE.parent / ".overview_cache.json"


def _word(score):
    if score is None:
        return "Not assessed"
    return WORD.get(int(max(-2, min(2, round(score)))), "Neutral")


def business_overview(sym: str, name: str) -> dict | None:
    """What the company does and its business segments, written by the
    judge model STRICTLY from the conference-call transcripts (cached per
    transcript + model). None when no transcripts or the call fails."""
    excerpt, n_calls, rng = REG.MB_AZ._timeline_excerpt(sym, budget=45000)
    if not excerpt:
        return None
    pdf = (REG.INDIA / "ConferenceCalls" / "NiftyTotalMarket"
           / f"{sym.replace('&', '_AND_')}.pdf")
    stamp = f"{pdf.stat().st_mtime}:ov1:{REG.MODEL}"
    cache = {}
    if OVERVIEW_CACHE.exists():
        try:
            cache = json.loads(OVERVIEW_CACHE.read_text())
        except Exception:
            cache = {}
    hit = cache.get(sym)
    if hit and hit.get("stamp") == stamp:
        return hit["overview"]
    prompt = (
        f"From the conference-call excerpts below ({n_calls} calls, {rng}), "
        f"describe what {name} ({sym}) actually DOES, for a reader who has "
        "never heard of it. Use ONLY what the calls state — no outside "
        "knowledge. Plain, everyday financial language.\n\n"
        "Return STRICT JSON only:\n"
        "{\"what_it_does\": \"3-4 sentences: what it sells, to whom, how "
        "it makes money, where it operates\", "
        "\"parts\": [{\"name\": \"business line / segment as management "
        "calls it\", \"what\": \"one plain sentence on what this part does "
        "and roughly how big or important the calls say it is\"}]}\n\n"
        f"CONFERENCE-CALL EXCERPTS ({sym}):\n{excerpt}"
    )
    for _ in range(2):
        proc = subprocess.run(["claude", "-p", "--model", REG.MODEL],
                              input=prompt, capture_output=True, text=True,
                              timeout=None)
        if proc.returncode != 0:
            continue
        m = re.search(r"\{.*\}", proc.stdout, re.DOTALL)
        if not m:
            continue
        try:
            ov = json.loads(m.group(0))
        except json.JSONDecodeError:
            continue
        if ov.get("what_it_does"):
            cache[sym] = {"stamp": stamp, "overview": ov}
            OVERVIEW_CACHE.write_text(json.dumps(cache))
            return ov
    return None


def _fmt_val(v, unit):
    if unit == "%":
        return f"{v:.0f}%"
    if unit == "d":
        return f"{v:.0f} days" if round(v) != 1 and round(v) != -1 else f"{v:.0f} day"
    return f"{v:,.0f}"


def _chart(title, series, unit="", yoy="pct"):
    """A year-by-year bar chart in plain text (renders everywhere), with
    the change vs the prior year on every row — the pictorial view of the
    same numbers the checks above judged."""
    years, vals = series.get("years", []), series.get("values", [])
    pairs = [(y, v) for y, v in zip(years, vals) if v is not None]
    if len(pairs) < 3:
        return ""
    pairs = pairs[-12:]
    vmax = max(abs(v) for _, v in pairs) or 1
    rows = []
    prev = None
    for y, v in pairs:
        bar = "█" * max(1, round(abs(v) / vmax * 22))
        if v < 0:
            bar = "▒" * max(1, round(abs(v) / vmax * 22))   # negative years
        change = ""
        if prev is not None:
            if yoy == "pct" and prev != 0:
                ch = (v - prev) / abs(prev) * 100
                arrow = "▲" if ch > 0.5 else ("▼" if ch < -0.5 else "▬")
                change = f"  {arrow} {abs(ch):.0f}% vs prior year"
            elif yoy == "pts":
                ch = v - prev
                arrow = "▲" if ch > 0.2 else ("▼" if ch < -0.2 else "▬")
                change = (f"  {arrow} {abs(ch):.1f} point"
                          f"{'s' if abs(ch) >= 1.05 or abs(ch) < 0.95 else ''}"
                          f" vs prior year")
            elif yoy == "days":
                ch = v - prev
                arrow = "▼" if ch < -0.5 else ("▲" if ch > 0.5 else "▬")
                d = round(abs(ch))
                change = (f"  {arrow} {d} day{'s' if d != 1 else ''} "
                          f"vs prior year")
        rows.append(f"{y:<8}{bar:<24}{_fmt_val(v, unit):>10}{change}")
        prev = v
    return (f"**{title}**\n\n```\n" + "\n".join(rows) + "\n```")


def _verdict_plain(rt) -> str:
    """A few plain lines on WHY the rating is what it is — deterministic,
    from the same pillar facts that produced the number."""
    if rt["score"] is None:
        return rt["derivation"]
    q = rt["pillars"]["quality"]
    p = rt["pillars"]["patterns"]
    s = rt["pillars"]["safety"]
    bits = []
    if q["points"] is not None:
        w = ("an excellent" if q["points"] >= 80 else
             "a good" if q["points"] >= 62 else
             "an average" if q["points"] >= 45 else "a weak")
        bits.append(f"the quality framework finds {w} business today "
                    f"({q['points']}/100)")
    if p["points"] is not None:
        n = len(p.get("strong", []))
        bits.append(f"it strongly fits {n} of the 11 patterns long-term "
                    f"winners share" if n else
                    "no winning pattern is strongly confirmed yet")
    if s["points"] is not None:
        high, elev = s.get("high", []), s.get("elevated", [])
        if high:
            bits.append(f"the risk review found "
                        f"{len(high)} high risk{'s' if len(high) > 1 else ''} "
                        f"({', '.join(high[:2])}{'…' if len(high) > 2 else ''})")
        elif elev:
            bits.append(f"the main risks are elevated but not severe "
                        f"({', '.join(elev[:2])})")
        else:
            bits.append("the risk review found nothing severe")
    return (f"In one breath: " + "; ".join(bits) +
            f". Weighing those together gives {rt['score']} out of 100 — "
            f"{rt['grade'].lower()}.")


def render(sym: str, name: str, ba: dict, mb: dict, qr: dict, rt: dict,
           synth: dict | None, statuses: dict,
           extensions: list | None = None,
           overview: dict | None = None,
           trends: dict | None = None,
           industry: str = "") -> str:
    L: list[str] = []
    A = L.append
    fw_names = {p.id: p.name for p in REG.FW.parameters}

    A(f"# {name} ({sym}) — The Analyst's Report")
    A("")

    # ---- 1. about the business
    A("## About the business")
    A("")
    if industry:
        A(f"*Industry: {industry}*")
        A("")
    if overview:
        A(overview.get("what_it_does", "").strip())
        A("")
        parts = overview.get("parts") or []
        if parts:
            A("**The parts of the business:**")
            A("")
            for pt in parts:
                A(f"- **{pt.get('name', '?')}** — {pt.get('what', '')}")
            A("")
        A("*Described strictly from management's own words on the "
          "earnings calls.*")
        A("")
    else:
        A("*No conference-call transcripts were available to describe the "
          "business in management's own words — run the full analysis, or "
          "see the evidence sections below.*")
        A("")

    # ---- 2. the verdict
    if rt["score"] is not None:
        A(f"## The verdict: {rt['grade']} — {rt['score']} out of 100 "
          f"{'★' * rt['stars']}{'☆' * (5 - rt['stars'])}")
        A("")
        A(_verdict_plain(rt))
        A("")
        A(f"**The exact arithmetic:** {rt['derivation']}")
        A("")
        for key in rt.get("pillar_order", ("quality", "patterns", "safety")):
            p = rt["pillars"].get(key)
            if p is None:
                continue
            pts = "—" if p["points"] is None else f"{p['points']}/100"
            A(f"- **{p['name']} ({pts}):** {p['derivation']}")
        A("")
    else:
        A(f"## The verdict: {rt['grade']}")
        A("")
        A(rt["derivation"])
        A("")
    if synth:
        A("### The story in depth")
        A("")
        for para in synth["summary"]:
            A(para)
            A("")
        A("*Written strictly from the three analyses below — every claim "
          "traces to a captured verdict; names it could not ground were "
          "grounds to reject it.*")
        A("")

    # ---- 3a. business quality — every dimension
    A("## Section 1 — How good is the business? (34-check quality framework)")
    A("")
    A(f"**Overall: {_word(ba['overall'])}** — score "
      + (f"{ba['overall']:+.2f}" if ba["overall"] is not None else "n/a")
      + f" on a −2 (poor) to +2 (excellent) scale; {ba['coverage']:.0%} of "
        f"the 34 checks had evidence (unanswerable checks are marked, "
        f"never guessed).")
    A("")
    A("| Area | Verdict | Score | Checks done |")
    A("|---|---|---|---|")
    for m in REG.MODULE_IDS:
        md_ = ba["modules"][m]
        A(f"| {MODULE_SHORT[m]} | {_word(md_['score'])} | "
          f"{'—' if md_['score'] is None else format(md_['score'], '+.2f')} | "
          f"{md_['assessed']} of {md_['total']} |")
    A("")

    if trends:
        charts = [c for c in [
            _chart("Sales, year by year (₹ crore)", trends.get("sales", {}),
                   "", "pct"),
            _chart("Operating margin — the share of sales kept as profit",
                   trends.get("opm", {}), "%", "pts"),
            _chart("Return on capital employed — what the business earns "
                   "on the money in it", trends.get("roce", {}), "%", "pts"),
            _chart("Cash conversion cycle — days cash is stuck in the "
                   "trade loop (negative = customers pay first: good)",
                   trends.get("ccc", {}), "d", "days"),
        ] if c]
        if charts:
            A("### The numbers over time")
            A("")
            A("*The same figures the checks below judged, drawn year by "
              "year — █ bars scale to the biggest year (▒ marks a negative "
              "year), and every row shows the change on the year before.*")
            A("")
            for c in charts:
                A(c)
                A("")

    A("### Every check, area by area")
    A("")
    for m in REG.MODULE_IDS:
        md_ = ba["modules"][m]
        A(f"**{MODULE_SHORT[m]} — {_word(md_['score'])}"
          + (f" ({md_['score']:+.2f})" if md_["score"] is not None else "")
          + f"** · {md_['assessed']} of {md_['total']} checks had evidence")
        A("")
        assessed = [(pid, p) for pid, p in ba["params"].items()
                    if p.get("module") == m]
        assessed.sort(key=lambda kv: -kv[1]["score"])
        for pid, p in assessed:
            src = {"calls": "from the conference calls",
                   "fused": "from the numbers and the calls together"}.get(
                  p.get("source"), "from the financial statements")
            A(f"- **{fw_names.get(pid, pid)} — {_word(p['score'])}** "
              f"*({src})*: {p['rationale']}")
            if p.get("quote"):
                A(f"  > \"{p['quote']}\" — *management, on an earnings call*")
        silent = [fw_names[q.id] for q in REG.FW.parameters
                  if q.module == m and q.id not in ba["params"]]
        if silent:
            A(f"- *Not assessed (the evidence was silent — never guessed): "
              + "; ".join(silent) + ".*")
        A("")

    # ---- 3b. patterns — every dimension
    A("## Section 2 — Does it look like a long-term winner? "
      "(11 multibagger patterns)")
    A("")
    g = mb["core_gate"]
    gate_word = {"PASS": "passes", "PARTIAL": "partly passes",
                 "FAIL": "fails", "UNKNOWN": "could not be tested against"}[g["status"]]
    matched = [v for v in mb["verdicts"]
               if v["verdict"] in ("STRONG FIT", "LIKELY FIT", "QUANT SIGNAL")]
    A(f"**Overall:** the company {gate_word} the foundation every "
      f"multibagger shares (steady cash + high returns on capital + "
      f"growth), {g['passed']} of {g['of']} testable checks passing"
      + (f", and fits {len(matched)} of the 11 patterns: "
         + ", ".join(v["name"] for v in matched) + "."
         if matched else "; no pattern is confirmed by the evidence."))
    A("")
    for v in mb["verdicts"]:
        A(f"### {v['name']} — {v['verdict']}")
        A(f"*\"{v['friendly']}\"*")
        A("")
        A(f"**Why this verdict:** {v.get('derivation') or v['verdict_friendly']}")
        A("")
        if v["qual"].get("fit") and v["qual"].get("rationale"):
            A(f"**What the calls show:** {v['qual']['rationale']}")
            A("")
        if v["qual"].get("quote"):
            A(f"> \"{v['qual']['quote']}\" — *management, on an earnings call*")
            A("")
        for e in v["quant"]["evidence"]:
            mark = {"supports": "✅", "against": "❌", "no data": "⬜"}[e["status"]]
            A(f"- {mark} {e['explanation']}")
        if v["quant"]["evidence"]:
            A("")

    # ---- 3c. risks — every dimension
    A("## Section 3 — What could break it? (8 risk channels)")
    A("")
    fr = qr["fragility"]
    fr_word = {"SOUND": "shows no financial stress",
               "STRAINED": "shows one financial stress signal",
               "STRESSED": "shows multiple financial stress signals",
               "UNKNOWN": "could not be stress-tested"}[fr["status"]]
    material = [v for v in qr["verdicts"]
                if v["verdict"] in ("HIGH RISK", "ELEVATED", "QUANT FLAG")]
    A(f"**Overall:** "
      + (f"the risks worth attention are "
         + ", ".join(v["name"] for v in material)
         if material else
         "no risk channel shows both meaningful evidence and severity today")
      + f". The balance sheet and cash engine {fr_word} — {fr['derivation']}")
    A("")
    for c in fr["checks"]:
        mark = "⚠️" if c["flagged"] else ("⬜" if c["flagged"] is None else "✅")
        A(f"- {mark} {c['explanation']}")
    A("")
    for v in qr["verdicts"]:
        A(f"### {v['name']} — {v['verdict']}")
        A(f"*\"{v['friendly']}\"*")
        A("")
        A(f"**Why this verdict:** {v.get('derivation') or v['verdict_friendly']}")
        A("")
        if v["qual"].get("exposure") and v["qual"].get("rationale"):
            A(f"**What the calls show:** {v['qual']['rationale']}")
            A("")
        if v["qual"].get("quote"):
            A(f"> \"{v['qual']['quote']}\" — *management, on an earnings call*")
            A("")
        if v["qual"].get("mitigant"):
            A(f"*Silver lining: {v['qual']['mitigant']}*")
            A("")
        for e in v["quant"]["evidence"]:
            mark = {"flags the risk": "⚠️", "no fingerprint": "✅",
                    "no data": "⬜"}[e["status"]]
            A(f"- {mark} {e['explanation']}")
        if v["quant"]["evidence"]:
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
      "financial statements could be used. The charts draw the same yearly "
      "figures the checks judged — nothing is computed twice. Research "
      "tooling; not investment advice.")
    return "\n".join(L)
