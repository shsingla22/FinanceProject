"""
risk_engine.py — taxonomy loader/validator and the deterministic severity
ladder for the QualityRisks skill.

Severity ladder (most severe first):

    HIGH RISK    the concall judge sees high exposure AND the numbers agree
                 (or the risk has no computable fingerprint)
    ELEVATED     judge sees high exposure without numeric confirmation, or
                 moderate exposure that the numbers reinforce
    WATCH        judge sees moderate exposure, numbers quiet
    QUANT FLAG   the numbers alone show the fingerprint — needs call
                 evidence; numbers can never claim more than this
    LOW          the judge affirmatively assessed the risk as low/mitigated
                 (a grounded "low" overrides numeric flags, with a note)
    NO SIGNAL    nothing in the calls or the numbers points to this risk
    NOT ASSESSED insufficient evidence either way (never guessed)
"""

from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REF = HERE.parent / "reference"

SEVERITY_ORDER = ["HIGH RISK", "ELEVATED", "WATCH", "QUANT FLAG",
                  "LOW", "NO SIGNAL", "NOT ASSESSED"]

FRIENDLY_VERDICT = {
    "HIGH RISK": "High risk — the calls and the numbers both point here",
    "ELEVATED": "Elevated — meaningful exposure, keep it front of mind",
    "WATCH": "Worth watching — some exposure visible in the calls",
    "QUANT FLAG": "Numbers flag this — needs call evidence to confirm",
    "LOW": "Assessed low — the calls show real mitigation",
    "NO SIGNAL": "No signal — nothing points to this risk today",
    "NOT ASSESSED": "Not assessed — not enough evidence (never guessed)",
}

_tax_cache: dict = {}


def load_taxonomy() -> dict:
    if "tax" not in _tax_cache:
        _tax_cache["tax"] = yaml.safe_load((REF / "risks.yaml").read_text())
    return _tax_cache["tax"]


def validate() -> list[str]:
    """Cross-check risks.yaml against checklist.yaml. Returns problems."""
    problems = []
    tax = load_taxonomy()
    chk = yaml.safe_load((REF / "checklist.yaml").read_text())
    ids = [r["id"] for r in tax.get("risks", [])]
    if len(ids) != chk["expected_total"]:
        problems.append(f"expected {chk['expected_total']} risks, "
                        f"found {len(ids)}")
    for rid in chk["expected_risks"]:
        if rid not in ids:
            problems.append(f"risk missing from taxonomy: {rid}")
    declared = set()
    for r in tax.get("risks", []):
        for f in ("name", "friendly", "description", "traits",
                  "qual_markers", "examples"):
            if not r.get(f):
                problems.append(f"{r.get('id', '?')}: missing field {f}")
        declared.update(r.get("quant_checks", []))
    for cid in declared:
        if cid not in chk["expected_quant_checks"]:
            problems.append(f"taxonomy references undeclared check: {cid}")
    for fid in tax.get("fragility_checks", []):
        if fid not in chk["expected_fragility_checks"]:
            problems.append(f"undeclared fragility check: {fid}")
    return problems


def quant_support(risk: dict, checks: dict) -> dict:
    """Evidence rows for one risk from the computed checks."""
    evidence = []
    flagged = clear = nodata = 0
    for cid in risk.get("quant_checks", []):
        c = checks.get(cid)
        if c is None:
            continue
        if c["flagged"] is True:
            status = "flags the risk"
            flagged += 1
        elif c["flagged"] is False:
            status = "no fingerprint"
            clear += 1
        else:
            status = "no data"
            nodata += 1
        evidence.append({"check": cid, "status": status,
                         "explanation": c["explanation"]})
    return {"flagged": flagged, "clear": clear, "nodata": nodata,
            "available": flagged + clear, "evidence": evidence}


def combine(risk: dict, checks: dict, qual: dict | None,
            judged: bool = True) -> dict:
    """Deterministic severity ladder for one risk.

    `judged=False` means no qualitative judge ran at all (e.g. the company
    holds no earnings calls) — clean numbers then yield NOT ASSESSED, never
    "NO SIGNAL", because silence that was never examined is not safety.
    """
    q = quant_support(risk, checks)
    exposure = (qual or {}).get("exposure")
    has_quant_dimension = len(risk.get("quant_checks", [])) > 0

    if exposure == "high":
        if q["flagged"] >= 1:
            verdict = "HIGH RISK"
            derivation = (f"the calls show clear, repeated exposure AND "
                          f"{q['flagged']} of {q['available']} numeric "
                          f"fingerprints agree — that combination earns the "
                          f"top severity.")
        elif not has_quant_dimension:
            verdict = "HIGH RISK"
            derivation = ("the calls show clear, repeated exposure; this "
                          "risk has no numeric fingerprint to cross-check, "
                          "so it is judged from the calls alone.")
        elif q["available"] == 0:
            verdict = "HIGH RISK"
            derivation = ("the calls show clear, repeated exposure; the "
                          "numeric fingerprints could not be computed, so "
                          "the call evidence decides alone.")
        else:
            verdict = "ELEVATED"
            derivation = (f"the calls show clear exposure, but none of the "
                          f"{q['available']} computed fingerprints confirms "
                          f"it in the numbers yet — held one step below the "
                          f"top severity.")
    elif exposure == "moderate":
        if q["flagged"] >= 1:
            verdict = "ELEVATED"
            derivation = (f"the calls show real but bounded exposure, and "
                          f"{q['flagged']} numeric fingerprint"
                          f"{'s' if q['flagged'] > 1 else ''} reinforce"
                          f"{'' if q['flagged'] > 1 else 's'} it.")
        else:
            verdict = "WATCH"
            derivation = ("the calls show real but bounded exposure while "
                          "the numbers stay quiet.")
    elif exposure == "low":
        verdict = "LOW"
        derivation = ("the judge affirmatively found the risk absent or "
                      "mitigated in the calls"
                      + (f" — that grounded reading overrides the "
                         f"{q['flagged']} numeric flag"
                         f"{'s' if q['flagged'] > 1 else ''}, kept visible "
                         f"below." if q["flagged"] >= 1 else "."))
    elif q["flagged"] >= 1:
        verdict = "QUANT FLAG"
        derivation = (f"{q['flagged']} numeric fingerprint"
                      f"{'s are' if q['flagged'] > 1 else ' is'} present but "
                      f"the calls offer nothing either way — numbers alone "
                      f"are only ever a flag to investigate, never a "
                      f"verdict.")
    elif judged and q["available"] > 0:
        verdict = "NO SIGNAL"
        derivation = (f"the judge read the calls and found nothing, and all "
                      f"{q['available']} computed fingerprints are clean.")
    else:
        verdict = "NOT ASSESSED"
        derivation = ("neither the calls nor the numbers offered usable "
                      "evidence — left unassessed rather than guessed."
                      if judged else
                      "no call transcripts were available and the numbers "
                      "show no fingerprint — unexamined is not the same as "
                      "safe, so this stays unassessed.")

    return {
        "risk": risk["id"],
        "name": risk["name"],
        "friendly": risk["friendly"],
        "verdict": verdict,
        "verdict_friendly": FRIENDLY_VERDICT[verdict],
        "derivation": derivation,
        "qual": {
            "exposure": exposure,
            "rationale": (qual or {}).get("rationale", ""),
            "quote": (qual or {}).get("quote", ""),
            "mitigant": (qual or {}).get("mitigant", ""),
        },
        "quant": q,
    }


def fragility(checks: dict, tax: dict) -> dict:
    """Cross-cutting balance-sheet / earnings-quality stress summary."""
    rows = []
    flagged = 0
    tested = 0
    for cid in tax.get("fragility_checks", []):
        c = checks.get(cid)
        if c is None:
            continue
        rows.append({"check": cid, "flagged": c["flagged"],
                     "explanation": c["explanation"]})
        if c["flagged"] is not None:
            tested += 1
            if c["flagged"]:
                flagged += 1
    status = ("UNKNOWN" if tested == 0 else
              "STRESSED" if flagged >= 2 else
              "STRAINED" if flagged == 1 else "SOUND")
    derivation = {
        "UNKNOWN": "none of the stress checks could be computed.",
        "SOUND": (f"none of the {tested} stress checks (leverage, cash "
                  f"conversion, returns on capital) is flagged."),
        "STRAINED": (f"1 of the {tested} stress checks is flagged — one "
                     f"warning light, not yet a pattern."),
        "STRESSED": (f"{flagged} of the {tested} stress checks are flagged "
                     f"— multiple warning lights at once."),
    }[status]
    return {"status": status, "flagged": flagged, "tested": tested,
            "derivation": derivation, "checks": rows}


def analyse(sym: str, checks: dict, qual_by_risk: dict | None = None) -> dict:
    """Full explainable risk record for one company."""
    tax = load_taxonomy()
    judged = qual_by_risk is not None
    verdicts = []
    for r in tax["risks"]:
        qual = (qual_by_risk or {}).get(r["id"])
        verdicts.append(combine(r, checks, qual, judged=judged))
    verdicts.sort(key=lambda v: SEVERITY_ORDER.index(v["verdict"]))
    material = [v["risk"] for v in verdicts
                if v["verdict"] in ("HIGH RISK", "ELEVATED", "QUANT FLAG")]
    return {
        "symbol": sym,
        "judged": judged,
        "fragility": fragility(checks, tax),
        "verdicts": verdicts,
        "material_risks": material,
        "taxonomy_version": tax.get("version", "?"),
    }
