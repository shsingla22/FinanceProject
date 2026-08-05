"""
analyze.py — run the QualityRisks skill.

Modes:
  python3 analyze.py screen                 quant-screen the whole universe;
                                            list companies per flagged risk
  python3 analyze.py company SYMBOL         full analysis of one company
                                            (add --ai to run the qualitative
                                            judge over its concalls via the
                                            Claude Code CLI — no timeout;
                                            model via RISK_JUDGE_MODEL,
                                            default "opus")
  python3 analyze.py report SYMBOL out.md   write the human-readable report

The qualitative judge reads the company's merged concall transcript (sampled
across the timeline, oldest-first) plus its 5-year management history, and
returns per-risk {exposure, rationale, quote, mitigant} — exposure is null
when the evidence is silent (never guessed), and "low" only when the calls
affirmatively show mitigation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import risk_engine as RE        # noqa: E402
import risk_evidence as QE      # noqa: E402

INDIA = QE.INDIA
UNIVERSE = QE.UNIVERSE
CACHE = HERE.parent / ".qual_cache.json"
CALL_HEADER_RE = re.compile(r"Call:\s+([A-Z][a-z]{2}\s+\d{4})")
JUDGE_MODEL = os.environ.get("RISK_JUDGE_MODEL", "opus")


# ------------------------------------------------------------- qualitative
def _concall_text(sym: str) -> str:
    pdf = INDIA / "ConferenceCalls" / UNIVERSE / f"{sym.replace('&', '_AND_')}.pdf"
    if not pdf.exists():
        return ""
    import PyPDF2
    try:
        reader = PyPDF2.PdfReader(str(pdf), strict=False)
        return "\n".join((p.extract_text() or "") for p in reader.pages)
    except Exception:
        return ""


def _timeline_excerpt(sym: str, budget: int = 90000) -> tuple[str, int, str]:
    full = _concall_text(sym)
    if not full:
        return "", 0, ""
    parts = CALL_HEADER_RE.split(full)
    calls = [(parts[i], parts[i + 1].strip())
             for i in range(1, len(parts) - 1, 2)]
    calls = [(d, t) for d, t in calls if len(t) > 800]
    if not calls:
        return full[-budget:], 1, ""
    n = len(calls)
    idx = sorted({0, n // 2, max(0, n - 2), n - 1})
    per = budget // len(idx)
    ex = "\n\n".join(f"===== CALL {i+1} of {n} ({calls[i][0]}) =====\n"
                     f"{calls[i][1][:per]}" for i in idx)
    return ex, n, f"{calls[0][0]} to {calls[-1][0]}"


def _mgmt_lines(sym: str) -> str:
    f = INDIA / "ManagementInfo" / UNIVERSE / f"{sym.replace('&', '_AND_')}.csv"
    if not f.exists():
        return "(no management history on file)"
    try:
        mdf = pd.read_csv(f)
        return "\n".join(
            f"- {r['role']}: {' '.join(str(r['name']).split())} "
            f"({r.get('years_present', '?')}, {r['status']})"
            for _, r in mdf.head(15).iterrows())
    except Exception:
        return "(unreadable management history)"


def _qual_prompt(sym: str, tax: dict) -> str | None:
    excerpt, n_calls, rng = _timeline_excerpt(sym)
    if not excerpt:
        return None
    rlist = "\n".join(
        f"- {r['id']}: {r['name']} — {r['description'].strip()} "
        f"Look for: {'; '.join(r['qual_markers'])}"
        for r in tax["risks"])
    return (
        "You are judging which RISKS TO QUALITY INVESTING a company is "
        f"exposed to, using excerpts from {n_calls} quarterly earnings calls "
        f"({rng}, oldest first) and its 5-year management history. Judge the "
        "trajectory across the years, not one quarter. These are RISKS — be "
        "a skeptic, but a grounded one.\n\n"
        f"RISK CHANNELS:\n{rlist}\n\n"
        "For each risk return exposure = \"high\" (clear, repeated evidence "
        "of material exposure), \"moderate\" (real but bounded exposure), "
        "\"low\" (the calls AFFIRMATIVELY show the risk is absent or "
        "mitigated — cite the mitigation), or null (the evidence is silent "
        "— NEVER guess). Every non-null exposure must cite evidence. "
        "Markers labelled MITIGANT reduce exposure; name them in the "
        "mitigant field when present.\n\n"
        "Return STRICT JSON only: {\"risks\": [{\"id\": ..., \"exposure\": "
        "..., \"rationale\": \"1-2 sentences citing the calls/management "
        "record\", \"quote\": \"short verbatim quote or empty\", "
        "\"mitigant\": \"the mitigating factor seen, or empty\"}]}\n\n"
        f"MANAGEMENT HISTORY ({sym}):\n{_mgmt_lines(sym)}\n\n"
        f"CONFERENCE-CALL EXCERPTS ({sym}):\n{excerpt}"
    )


def qual_judge(sym: str, tax: dict, use_cache: bool = True) -> dict | None:
    """Per-risk qualitative exposure via headless Claude (subscription).
    Cached on disk keyed by transcript mtime + model. No timeout."""
    pdf = INDIA / "ConferenceCalls" / UNIVERSE / f"{sym.replace('&', '_AND_')}.pdf"
    if not pdf.exists():
        return None
    stamp = f"{pdf.stat().st_mtime}:v1:{JUDGE_MODEL}"
    cache = {}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text())
        except Exception:
            cache = {}
    hit = cache.get(sym)
    if use_cache and hit and hit.get("stamp") == stamp:
        return _plain_speech(hit["by_risk"])

    prompt = _qual_prompt(sym, tax)
    if prompt is None:
        return None
    proc = subprocess.run(["claude", "-p", "--model", JUDGE_MODEL],
                          input=prompt, capture_output=True, text=True,
                          timeout=None)
    if proc.returncode != 0:
        raise RuntimeError("claude CLI failed: " + (proc.stderr or "")[-300:])
    by_risk = parse_judge(proc.stdout)
    if by_risk is None:
        raise RuntimeError("could not parse judge output")
    cache[sym] = {"stamp": stamp, "by_risk": by_risk}
    CACHE.write_text(json.dumps(cache))
    return _plain_speech(by_risk)


def _plain_speech(by_id: dict | None) -> dict | None:
    """Expand analyst shorthand the judge may use in its free-text fields
    (never the verbatim quote) — readers get plain financial English."""
    for it in (by_id or {}).values():
        for k in ("rationale", "mitigant"):
            if isinstance(it.get(k), str):
                it[k] = re.sub(r"\b[yY]o[yY]\b", "year-on-year", it[k])
                it[k] = re.sub(r"\b[qQ]o[qQ]\b", "quarter-on-quarter", it[k])
    return by_id


def parse_judge(stdout: str) -> dict | None:
    m = re.search(r"\{.*\}", stdout, re.DOTALL)
    if not m:
        return None
    try:
        items = json.loads(m.group(0)).get("risks", [])
    except json.JSONDecodeError:
        items = []
        for it in re.findall(r'\{[^{}]*"id"\s*:\s*"[^"]+"[^{}]*\}', m.group(0)):
            try:
                items.append(json.loads(it))
            except json.JSONDecodeError:
                continue
    valid = {r["id"] for r in RE.load_taxonomy()["risks"]}
    by_risk = {it["id"]: it for it in items if it.get("id") in valid}
    return by_risk or None


# ------------------------------------------------------------- report
def render_report(rec: dict, name: str = "") -> str:
    L = []
    A = L.append
    sym = rec["symbol"]
    A(f"# {name or sym} ({sym}) — Quality-Risk Analysis")
    A("")
    material = rec["material_risks"]
    tax = RE.load_taxonomy()
    by_id = {r["id"]: r for r in tax["risks"]}
    if material:
        A("**Material risks found:** "
          + "; ".join(f"{by_id[m]['name']} (*{by_id[m]['friendly']}*)"
                      for m in material))
    else:
        A("**Material risks found:** none — no risk channel shows both "
          "meaningful evidence and severity today.")
    A("")
    if not rec.get("judged"):
        A("*No conference-call transcripts are on file for this company — "
          "the verdicts below rest on the numbers alone, and the "
          "qualitative risk channels could not be assessed.*")
        A("")
    fr = rec["fragility"]
    fr_word = {"SOUND": "shows no financial stress",
               "STRAINED": "shows one financial stress signal",
               "STRESSED": "shows multiple financial stress signals",
               "UNKNOWN": "could not be stress-tested (insufficient data)"}[fr["status"]]
    A(f"**Financial resilience:** the balance sheet and cash engine "
      f"{fr_word} — {fr['derivation']}")
    A("")
    for c in fr["checks"]:
        mark = "⚠️" if c["flagged"] else ("⬜" if c["flagged"] is None else "✅")
        A(f"- {mark} {c['explanation']}")
    A("")
    A("---")
    for v in rec["verdicts"]:
        A(f"## {v['name']} — {v['verdict']}")
        A(f"*\"{v['friendly']}\" · {v['verdict_friendly']}*")
        A("")
        A(f"**Why this severity:** {v['derivation']}")
        A("")
        q = v["qual"]
        if q.get("exposure"):
            A(f"**What the calls show:** {q.get('rationale', '')}")
            if q.get("quote"):
                A("")
                A(f"> \"{q['quote']}\" — *management, on an earnings call*")
            if q.get("mitigant"):
                A("")
                A(f"**Silver lining:** {q['mitigant']}")
            A("")
        for e in v["quant"]["evidence"]:
            mark = {"flags the risk": "⚠️", "no fingerprint": "✅",
                    "no data": "⬜"}[e["status"]]
            A(f"- {mark} {e['explanation']}")
        if not v["quant"]["evidence"] and not q.get("exposure"):
            A("*No usable evidence either way — honestly not assessed.*")
        A("")
    A("---")
    A("*Every verdict above was produced with its evidence attached at the "
      "moment of analysis — numbers from the financial statements, quotes "
      "from the earnings calls, tenure from the annual reports. A risk the "
      "evidence could not support is marked, never guessed; numbers alone "
      "are only ever a flag to investigate. Research tooling; not "
      "investment advice.*")
    return "\n".join(L)


# ------------------------------------------------------------- CLI
def cmd_screen(args):
    const = pd.read_csv(INDIA / "NiftyTotalMarket" /
                        "niftytotalmarket_constituents.csv")
    tax = RE.load_taxonomy()
    rows = []
    for i, r in enumerate(const.itertuples(), 1):
        sym = str(r.nse_symbol)
        try:
            checks = QE.compute_checks(sym)
        except Exception:
            continue
        rec = RE.analyse(sym, checks)
        rows.append({"symbol": sym, "name": r.company_name,
                     "fragility": rec["fragility"]["status"],
                     "flags": [v["risk"] for v in rec["verdicts"]
                               if v["verdict"] == "QUANT FLAG"]})
        if i % 200 == 0:
            print(f"  [{i}/{len(const)}]", file=sys.stderr)
    by_risk = {r["id"]: [] for r in tax["risks"]}
    for row in rows:
        for s in row["flags"]:
            by_risk[s].append(row)
    print("\n=== QUANT-FLAGGED COMPANIES (numbers only — verify with --ai) ===")
    for rid, cands in by_risk.items():
        if not cands:
            continue
        r = next(x for x in tax["risks"] if x["id"] == rid)
        print(f"\n{r['name']} ({r['friendly']}): {len(cands)} flagged")
        for c in cands[:12]:
            print(f"   {c['symbol']:<12} {c['name']}")
    stressed = [r for r in rows if r["fragility"] == "STRESSED"]
    print(f"\nFinancially stressed (2+ fragility signals): {len(stressed)}")
    for c in stressed[:20]:
        print(f"   {c['symbol']:<12} {c['name']}")


def cmd_company(args):
    tax = RE.load_taxonomy()
    checks = QE.compute_checks(args.symbol)
    qual = None
    if args.ai:
        print(f"Running the risk judge over {args.symbol}'s concalls "
              f"({JUDGE_MODEL}, no timeout — can take several minutes)…",
              file=sys.stderr)
        qual = qual_judge(args.symbol, tax)
    rec = RE.analyse(args.symbol, checks, qual)
    print(json.dumps(rec, indent=2, default=str))


def cmd_report(args):
    tax = RE.load_taxonomy()
    checks = QE.compute_checks(args.symbol)
    qual = qual_judge(args.symbol, tax) if args.ai else None
    rec = RE.analyse(args.symbol, checks, qual)
    const = pd.read_csv(INDIA / "NiftyTotalMarket" /
                        "niftytotalmarket_constituents.csv")
    row = const[const.nse_symbol == args.symbol]
    name = str(row.iloc[0].company_name) if len(row) else args.symbol
    md = render_report(rec, name)
    Path(args.out).write_text(md)
    print(f"wrote {args.out} ({len(md.splitlines())} lines)")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("screen")
    c = sub.add_parser("company")
    c.add_argument("symbol")
    c.add_argument("--ai", action="store_true")
    r = sub.add_parser("report")
    r.add_argument("symbol")
    r.add_argument("out")
    r.add_argument("--ai", action="store_true")
    args = ap.parse_args()
    if hasattr(args, "symbol"):
        args.symbol = args.symbol.upper()
    {"screen": cmd_screen, "company": cmd_company,
     "report": cmd_report}[args.cmd](args)


if __name__ == "__main__":
    main()
