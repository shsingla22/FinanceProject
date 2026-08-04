"""
validate_reports.py — thorough checks over every stored report pair.

Run directly, via `analyze_batch.py validate`, or through pytest
(test_reports.py). Checks per company:

  structure   every required section present, in the analyst's order
  language    no internal codes / analyst shorthand / formatting bugs
              ("CAP.headline", "1 days", "nan"…) outside quoted lines
  substance   a verdict with its derivation, non-trivial length
  consistency the comparison's long-view rating must EQUAL the rating in
              that company's own analysis MD — the two files were built
              from the same cached records, so any disagreement means a
              real bug, and it is checked, not assumed
"""

from __future__ import annotations

import re
from pathlib import Path

ANALYSIS_SECTIONS = [
    "## About the business",
    "## The verdict:",
    "## Section 1 — How good is the business?",
    "## Section 2 — Does it look like a long-term winner?",
    "## Section 3 — What could break it?",
    "## What to watch",
    "## How this report was built",
]
COMPARISON_SECTIONS = [
    "— Then vs Now: The One-Year Comparison",
    "## Step 1 — The overall rating",
    "## Step 2 — Where it improved and where it regressed",
    "### Bucket 1 — Business quality (34-check framework)",
    "### Bucket 2 — Multibagger patterns (11 patterns)",
    "### Bucket 3 — Risks (8 channels)",
    "## How this comparison was built",
]
JARGON = [r"\b(CAP|ROC|GRW|MGT|IND|CUS|MOAT)\.[a-z_]+", r"\bopm\b",
          r"\byoy\b", r"\b1 days\b", r"\bnan\b", r"\bNone\b(?! of)",
          r"1 checks\b", r"1 fingerprints\b", r"1 high risks\b"]


def _body(md: str) -> str:
    """Strip quoted transcript lines — verbatim management speech may
    legitimately contain anything."""
    return re.sub(r"^> .*$", "", md, flags=re.M)


def _sections_ok(md: str, sections: list[str]) -> str | None:
    idx = [md.find(s) for s in sections]
    missing = [s for s, i in zip(sections, idx) if i < 0]
    if missing:
        return f"missing sections: {missing[:3]}"
    if idx != sorted(idx):
        return "sections out of order"
    return None


def _jargon(md: str) -> str | None:
    body = _body(md)
    for pat in JARGON:
        m = re.search(pat, body)
        if m:
            return f"jargon leaked: {pat} -> {m.group()[:30]!r}"
    return None


def _analysis_rating(md: str) -> tuple[str, int | None] | None:
    """(grade, score) from the analysis MD's verdict heading."""
    m = re.search(r"^## The verdict: (.+?)(?:\s*[—(]|$)", md, flags=re.M)
    if not m:
        return None
    grade = m.group(1).strip()
    s = re.search(r"(\d+) out of 100", md)
    return grade, (int(s.group(1)) if s else None)


def _comparison_long_rating(md: str) -> tuple[str, int] | None:
    m = re.search(r"Long-term view: (\w[\w ]*?) \((\d+)/100\)", md)
    return (m.group(1), int(m.group(2))) if m else None


def validate_pair(sym: str, a_md: str, c_md: str) -> list[tuple]:
    problems = []
    for kind, md, sections, min_lines in (
            ("analysis", a_md, ANALYSIS_SECTIONS, 40),
            ("comparison", c_md, COMPARISON_SECTIONS, 30)):
        if (e := _sections_ok(md, sections)):
            problems.append((sym, kind, e))
        if (e := _jargon(md)):
            problems.append((sym, kind, e))
        if len(md.splitlines()) < min_lines:
            problems.append((sym, kind,
                             f"suspiciously short: {len(md.splitlines())} lines"))
        if sym not in md.splitlines()[0]:
            problems.append((sym, kind, "title lacks the symbol"))
    ar = _analysis_rating(a_md)
    if ar is None:
        problems.append((sym, "analysis", "no verdict heading"))
    cr = _comparison_long_rating(c_md)
    # cross-file consistency: same records -> same long-view rating
    if ar and cr and ar[1] is not None:
        if (ar[0], ar[1]) != cr:
            problems.append((sym, "cross",
                             f"analysis says {ar[0]} {ar[1]}/100 but "
                             f"comparison's long view says {cr[0]} "
                             f"{cr[1]}/100"))
    elif ar and ar[1] is None and cr is not None:
        problems.append((sym, "cross",
                         "analysis is Not rated but the comparison "
                         "claims a long-view score"))
    return problems


def validate_all(folder: Path) -> list[tuple]:
    problems = []
    pairs = 0
    for a_path in sorted(folder.glob("*_analysis.md")):
        sym = a_path.name[:-len("_analysis.md")]
        c_path = folder / f"{sym}_comparison.md"
        if not c_path.exists():
            problems.append((sym, "pair", "comparison MD missing"))
            continue
        pairs += 1
        problems += validate_pair(sym, a_path.read_text(), c_path.read_text())
    for c_path in sorted(folder.glob("*_comparison.md")):
        sym = c_path.name[:-len("_comparison.md")]
        if not (folder / f"{sym}_analysis.md").exists():
            problems.append((sym, "pair", "analysis MD missing"))
    print(f"validated {pairs} report pairs, {len(problems)} problems")
    return problems


if __name__ == "__main__":
    import sys
    probs = validate_all(Path(__file__).resolve().parent)
    for p in probs[:40]:
        print("  ", *p)
    sys.exit(1 if probs else 0)
