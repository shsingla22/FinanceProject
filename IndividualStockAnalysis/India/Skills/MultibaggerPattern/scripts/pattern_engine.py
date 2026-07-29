"""
pattern_engine.py — load the taxonomy, combine evidence into per-pattern
verdicts, and build the explainable record.

Verdict ladder per pattern (deterministic, unit-tested):

    STRONG FIT     qualitative judge confirms (fit=strong) AND the pattern's
                   quant checks don't contradict (>=half passed of available)
    LIKELY FIT     qual confirms but quant is thin/mixed, OR qual says partial
                   while quant fully supports
    QUANT SIGNAL   no qualitative evidence yet, but ALL available quant checks
                   pass (a screening hint, clearly labelled as numbers-only)
    PARTIAL        qual says partial, quant mixed
    NO FIT         qual says none, or quant contradicts with no qual support
    NOT ASSESSED   neither side had usable evidence

The core-principle gate (cash + returns + growth) is reported alongside:
patterns on a company failing the gate are annotated, never hidden.

Every verdict carries the full evidence trail: each quant check's value and
plain-English explanation, plus the judge's rationale and verbatim call quote.
"""

from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REFERENCE = HERE.parent / "reference"

VERDICTS = ["STRONG FIT", "LIKELY FIT", "QUANT SIGNAL", "PARTIAL",
            "NO FIT", "NOT ASSESSED"]
FRIENDLY_VERDICT = {
    "STRONG FIT": "Strong fit — confirmed by the calls and the numbers",
    "LIKELY FIT": "Likely fit — good evidence, not yet conclusive",
    "QUANT SIGNAL": "Numbers point this way — needs call evidence to confirm",
    "PARTIAL": "Partial fit — some traits present",
    "NO FIT": "Does not fit this pattern",
    "NOT ASSESSED": "Not assessed — insufficient evidence",
}


def load_taxonomy(path: Path = REFERENCE / "patterns.yaml") -> dict:
    return yaml.safe_load(path.read_text())


def validate(tax: dict | None = None) -> list:
    """Cross-check patterns.yaml against checklist.yaml. Empty list == valid."""
    tax = tax or load_taxonomy()
    chk = yaml.safe_load((REFERENCE / "checklist.yaml").read_text())
    problems = []
    got = [p["id"] for p in tax["patterns"]]
    for pid in chk["expected_patterns"]:
        if pid not in got:
            problems.append(f"MISSING pattern: {pid}")
    for pid in got:
        if pid not in chk["expected_patterns"]:
            problems.append(f"EXTRA pattern not in checklist: {pid}")
    if len(got) != chk["expected_total"]:
        problems.append(f"expected {chk['expected_total']} patterns, got {len(got)}")
    for p in tax["patterns"]:
        for f in ("id", "name", "friendly", "description", "traits",
                  "quant_checks", "qual_markers", "examples"):
            if f not in p:
                problems.append(f"{p.get('id','?')}: missing field '{f}'")
    core = tax.get("core_principle", {}).get("quant_checks", [])
    for c in chk["expected_core_checks"]:
        if c not in core:
            problems.append(f"MISSING core check: {c}")
    declared = set(chk["expected_quant_checks"])
    used = {c for p in tax["patterns"] for c in p["quant_checks"]}
    for c in used:
        if c not in declared:
            problems.append(f"pattern uses undeclared quant check: {c}")
    return problems


def quant_support(pattern: dict, checks: dict) -> dict:
    """Summarize the pattern's quant checks: how many passed / failed / no-data,
    with the full evidence list."""
    ev = []
    passed = failed = nodata = 0
    for cid in pattern["quant_checks"]:
        c = checks.get(cid)
        if c is None or c["passed"] is None:
            nodata += 1
            if c is not None:
                ev.append({"check": cid, "status": "no data",
                           "explanation": c["explanation"]})
            continue
        if c["passed"]:
            passed += 1
            ev.append({"check": cid, "status": "supports",
                       "value": c["value"], "explanation": c["explanation"]})
        else:
            failed += 1
            ev.append({"check": cid, "status": "against",
                       "value": c["value"], "explanation": c["explanation"]})
    return {"passed": passed, "failed": failed, "nodata": nodata,
            "evidence": ev}


def combine(pattern: dict, checks: dict, qual: dict | None) -> dict:
    """The deterministic verdict combiner. `qual` is the judge's output for
    this pattern: {fit: strong|partial|none|null, rationale, quote} or None."""
    q = quant_support(pattern, checks)
    avail = q["passed"] + q["failed"]
    quant_all = avail > 0 and q["failed"] == 0
    quant_majority = avail > 0 and q["passed"] >= q["failed"]
    fit = (qual or {}).get("fit")

    if fit == "strong" and (avail == 0 or quant_majority):
        verdict = "STRONG FIT"
        derivation = ("the calls confirm the pattern with clear, repeated "
                      "evidence"
                      + (f" and the numbers agree ({q['passed']} of {avail} "
                         f"computable checks supporting)." if avail else
                         " (no computable check applies — the calls decide)."))
    elif fit == "strong":
        verdict = "LIKELY FIT"          # judge convinced, numbers push back
        derivation = (f"the calls confirm the pattern, but the numbers push "
                      f"back ({q['passed']} of {avail} checks supporting) — "
                      f"held one step below a full confirmation.")
    elif fit == "partial" and quant_all and avail > 0:
        verdict = "LIKELY FIT"
        derivation = ("the calls show some of the traits and the only "
                      "computable check supports the pattern." if avail == 1
                      else f"the calls show some of the traits and every "
                           f"one of the {avail} computable checks supports "
                           f"the pattern.")
    elif fit == "partial":
        verdict = "PARTIAL"
        derivation = ("the calls show some of the traits"
                      + (f", with mixed numbers ({q['passed']} of {avail} "
                         f"checks supporting)." if avail else
                         " and no computable check to cross-check."))
    elif fit == "none":
        verdict = "NO FIT"
        derivation = ("the calls contradict the pattern — that grounded "
                      "reading overrides any supportive numbers"
                      + (f" ({q['passed']} of {avail} checks had pointed this "
                         f"way)." if q["passed"] else "."))
    elif fit in (None, "null") and quant_all and avail > 0:
        verdict = "QUANT SIGNAL"
        derivation = (("the only computable check points this way"
                       if avail == 1 else
                       f"all {avail} computable checks point this way")
                      + " but the calls offer no evidence — numbers alone "
                        "are only ever a screening hint, never a confirmed "
                        "fit.")
    elif fit in (None, "null") and avail > 0:
        verdict = "NO FIT" if q["passed"] == 0 else "PARTIAL"
        derivation = ("the calls are silent and no computable check "
                      "supports the pattern." if q["passed"] == 0 else
                      f"the calls are silent and the numbers are mixed "
                      f"({q['passed']} of {avail} checks supporting).")
    else:
        verdict = "NOT ASSESSED"
        derivation = ("neither the calls nor the numbers offered usable "
                      "evidence — left unassessed rather than guessed.")

    return {
        "pattern": pattern["id"],
        "name": pattern["name"],
        "friendly": pattern["friendly"],
        "verdict": verdict,
        "verdict_friendly": FRIENDLY_VERDICT[verdict],
        "derivation": derivation,
        "quant": q,
        "qual": qual or {"fit": None, "rationale":
                         "No conference-call judgement available.", "quote": ""},
    }


def core_gate(checks: dict, tax: dict) -> dict:
    """The foundation test: cash + returns + growth."""
    ids = tax["core_principle"]["quant_checks"]
    results = []
    passed = 0
    known = 0
    for cid in ids:
        c = checks.get(cid, {"passed": None, "explanation": "missing"})
        results.append({"check": cid, "passed": c["passed"],
                        "explanation": c["explanation"]})
        if c["passed"] is not None:
            known += 1
            if c["passed"]:
                passed += 1
    status = ("PASS" if known and passed == known else
              "PARTIAL" if passed > 0 else
              "FAIL" if known else "UNKNOWN")
    return {"status": status, "passed": passed, "of": known, "checks": results}


def analyse(sym: str, checks: dict, qual_by_pattern: dict | None = None,
            tax: dict | None = None) -> dict:
    """Full pattern analysis record for one company (explainable by
    construction: every verdict carries its evidence)."""
    tax = tax or load_taxonomy()
    qual_by_pattern = qual_by_pattern or {}
    gate = core_gate(checks, tax)
    verdicts = [combine(p, checks, qual_by_pattern.get(p["id"]))
                for p in tax["patterns"]]
    order = {v: i for i, v in enumerate(VERDICTS)}
    verdicts.sort(key=lambda v: order[v["verdict"]])
    matched = [v for v in verdicts
               if v["verdict"] in ("STRONG FIT", "LIKELY FIT", "QUANT SIGNAL")]
    return {
        "symbol": sym,
        "core_gate": gate,
        "verdicts": verdicts,
        "matched_patterns": [v["pattern"] for v in matched],
        "taxonomy_version": tax["version"],
    }
