"""
analyze.py — run the MultibaggerPattern skill.

Modes:
  python3 analyze.py screen                 quant-screen the whole universe;
                                            list candidates per pattern
  python3 analyze.py company SYMBOL         full analysis of one company
                                            (add --ai to run the qualitative
                                            judge over its concalls via the
                                            Claude Code CLI — no timeout;
                                            model via MB_JUDGE_MODEL,
                                            default "opus")
  python3 analyze.py report SYMBOL out.md   write the human-readable report

The qualitative judge reads the company's merged concall transcript (sampled
across the timeline, oldest-first) plus its 5-year management history, and
returns per-pattern {fit, rationale, quote} — fit is null when the evidence
is silent (never guessed).
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
import pattern_engine as PE     # noqa: E402
import quant_evidence as QE     # noqa: E402

INDIA = QE.INDIA
UNIVERSE = QE.UNIVERSE
CACHE = HERE.parent / ".qual_cache.json"
CALL_HEADER_RE = re.compile(r"Call:\s+([A-Z][a-z]{2}\s+\d{4})")
JUDGE_MODEL = os.environ.get("MB_JUDGE_MODEL", "opus")


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
    plist = "\n".join(
        f"- {p['id']}: {p['name']} — {p['description'].strip()} "
        f"Look for: {'; '.join(p['qual_markers'])}"
        for p in tax["patterns"])
    return (
        "You are judging which MULTIBAGGER PATTERNS a company fits, using "
        f"excerpts from {n_calls} quarterly earnings calls ({rng}, oldest "
        "first) and its 5-year management history. Judge the trajectory — "
        "delivery vs promises across the years — not one quarter.\n\n"
        f"PATTERNS:\n{plist}\n\n"
        "For each pattern return fit = \"strong\" (clear, repeated evidence), "
        "\"partial\" (some traits), \"none\" (evidence contradicts it), or "
        "null (the evidence is silent — NEVER guess). Every non-null fit "
        "must cite evidence.\n\n"
        "Return STRICT JSON only: {\"patterns\": [{\"id\": ..., \"fit\": ..., "
        "\"rationale\": \"1-2 sentences citing the calls/management record\", "
        "\"quote\": \"short verbatim quote or empty\"}]}\n\n"
        f"MANAGEMENT HISTORY ({sym}):\n{_mgmt_lines(sym)}\n\n"
        f"CONFERENCE-CALL EXCERPTS ({sym}):\n{excerpt}"
    )


def qual_judge(sym: str, tax: dict, use_cache: bool = True) -> dict | None:
    """Per-pattern qualitative fits via headless Claude Code (subscription).
    Cached on disk keyed by transcript mtime. No timeout — quality first."""
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
        return hit["by_pattern"]

    prompt = _qual_prompt(sym, tax)
    if prompt is None:
        return None
    proc = subprocess.run(["claude", "-p", "--model", JUDGE_MODEL],
                          input=prompt, capture_output=True, text=True,
                          timeout=None)
    if proc.returncode != 0:
        raise RuntimeError("claude CLI failed: " + (proc.stderr or "")[-300:])
    m = re.search(r"\{.*\}", proc.stdout, re.DOTALL)
    if not m:
        raise RuntimeError("could not parse judge output")
    try:
        items = json.loads(m.group(0)).get("patterns", [])
    except json.JSONDecodeError:
        items = []
        for it in re.findall(r'\{[^{}]*"id"\s*:\s*"[^"]+"[^{}]*\}', m.group(0)):
            try:
                items.append(json.loads(it))
            except json.JSONDecodeError:
                continue
    by_pattern = {it["id"]: it for it in items if it.get("id")}
    cache[sym] = {"stamp": stamp, "by_pattern": by_pattern}
    CACHE.write_text(json.dumps(cache))
    return by_pattern


# ------------------------------------------------------------- report
def render_report(rec: dict, name: str = "") -> str:
    L = []
    A = L.append
    sym = rec["symbol"]
    A(f"# {name or sym} ({sym}) — Multibagger Pattern Analysis")
    A("")
    matched = rec["matched_patterns"]
    if matched:
        tax = PE.load_taxonomy()
        by_id = {p["id"]: p for p in tax["patterns"]}
        A("**Patterns this company fits:** "
          + "; ".join(f"{by_id[m]['name']} (*{by_id[m]['friendly']}*)"
                      for m in matched))
    else:
        A("**Patterns this company fits:** none confirmed by the evidence.")
    A("")
    g = rec["core_gate"]
    gate_word = {"PASS": "passes", "PARTIAL": "partly passes",
                 "FAIL": "fails", "UNKNOWN": "could not be tested against"}[g["status"]]
    untested = sum(1 for c in g["checks"] if c["passed"] is None)
    line = (f"**Foundation test:** the company {gate_word} the core "
            f"multibagger foundation (predictable cash + high returns on "
            f"capital + growth), {g['passed']} of {g['of']} "
            f"{'testable ' if untested else ''}checks passing")
    if untested:
        line += (f" — note that {untested} of the 3 foundation checks could "
                 f"not be judged because the company has too little listed "
                 f"history")
    A(line + ":")
    A("")
    for c in g["checks"]:
        mark = "✅" if c["passed"] else ("❌" if c["passed"] is False else "⬜")
        A(f"- {mark} {c['explanation']}")
    A("")
    A("---")
    for v in rec["verdicts"]:
        A(f"## {v['name']} — {v['verdict']}")
        A(f"*\"{v['friendly']}\" · {v['verdict_friendly']}*")
        A("")
        if v.get("derivation"):
            A(f"**Why this verdict:** {v['derivation']}")
            A("")
        q = v["qual"]
        if q.get("fit"):
            A(f"**What the calls show:** {q.get('rationale', '')}")
            if q.get("quote"):
                A("")
                A(f"> \"{q['quote']}\" — *management, on an earnings call*")
            A("")
        for e in v["quant"]["evidence"]:
            mark = {"supports": "✅", "against": "❌", "no data": "⬜"}[e["status"]]
            A(f"- {mark} {e['explanation']}")
        if not v["quant"]["evidence"] and not q.get("fit"):
            A("*No usable evidence either way — honestly not assessed.*")
        A("")
    A("---")
    A("*Every verdict above was produced with its evidence attached at the "
      "moment of analysis — numbers from the financial statements, quotes "
      "from the earnings calls, tenure from the annual reports. Verdicts the "
      "evidence could not support are marked, never guessed. Research "
      "tooling; not investment advice.*")
    return "\n".join(L)


# ------------------------------------------------------------- CLI
def cmd_screen(args):
    const = pd.read_csv(INDIA / "NiftyTotalMarket" /
                        "niftytotalmarket_constituents.csv")
    tax = PE.load_taxonomy()
    rows = []
    for i, r in enumerate(const.itertuples(), 1):
        sym = str(r.nse_symbol)
        try:
            checks = QE.compute_checks(sym)
        except Exception:
            continue
        rec = PE.analyse(sym, checks)
        rows.append({"symbol": sym, "name": r.company_name,
                     "gate": rec["core_gate"]["status"],
                     "signals": [v["pattern"] for v in rec["verdicts"]
                                 if v["verdict"] == "QUANT SIGNAL"]})
        if i % 200 == 0:
            print(f"  [{i}/{len(const)}]", file=sys.stderr)
    by_pattern = {p["id"]: [] for p in tax["patterns"]}
    for row in rows:
        if row["gate"] != "PASS":
            continue
        for s in row["signals"]:
            by_pattern[s].append(row)
    print("\n=== QUANT-SIGNAL CANDIDATES (foundation PASS only) ===")
    for pid, cands in by_pattern.items():
        if not cands:
            continue
        p = next(x for x in tax["patterns"] if x["id"] == pid)
        print(f"\n{p['name']} ({p['friendly']}): {len(cands)} candidates")
        for c in cands[:12]:
            print(f"   {c['symbol']:<12} {c['name']}")
    n_pass = sum(1 for r in rows if r["gate"] == "PASS")
    print(f"\nFoundation gate: {n_pass}/{len(rows)} companies pass "
          f"(cash + returns + growth)")


def cmd_company(args):
    tax = PE.load_taxonomy()
    checks = QE.compute_checks(args.symbol)
    qual = None
    if args.ai:
        print(f"Running the qualitative judge over {args.symbol}'s concalls "
              f"(Opus, no timeout — can take several minutes)…", file=sys.stderr)
        qual = qual_judge(args.symbol, tax)
    rec = PE.analyse(args.symbol, checks, qual)
    print(json.dumps(rec, indent=2, default=str))


def cmd_report(args):
    tax = PE.load_taxonomy()
    checks = QE.compute_checks(args.symbol)
    qual = qual_judge(args.symbol, tax) if args.ai else None
    rec = PE.analyse(args.symbol, checks, qual)
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
    args.symbol = getattr(args, "symbol", "").upper() if hasattr(args, "symbol") else ""
    {"screen": cmd_screen, "company": cmd_company,
     "report": cmd_report}[args.cmd](args)


if __name__ == "__main__":
    main()
