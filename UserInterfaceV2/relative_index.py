"""
relative_index.py — the stored index comparison, turned into structured data.

v2's contract is that everything on the page comes from the stored Markdown
reports, so this module PARSES those reports rather than recomputing the
analysis. Three files feed it, all written by the batch:

  {SYM}_analysis.md        Section 4 — the verdict, the points, and the
                           10 / 5 / 3 / 1-year window table
  {SYM}_comparison.md      Bucket 4 — the long run vs the latest year
  {SYM}_stock_to_index.md  the full workup — each ratio's level year by
                           year, the change over every window, and the raw
                           company/index prices and profits behind them

Parsing (rather than importing the skill) is deliberate: if a report and
this page ever disagreed, the page would be lying about the file it offers
for download. Anything a report does not state is returned as None — this
module never fills a gap with a computed guess.

Four of the 742 companies have too little history to compare at any window
(and two of those have no chart files); every function here returns cleanly
for them rather than raising.
"""

from __future__ import annotations

import re
from pathlib import Path

# ---------------------------------------------------------------- Section 4

SECTION_HEAD = "## Section 4 — How has it done against the index?"
BUCKET_HEAD = "### Bucket 4 — Against the index"

VERDICT_RE = re.compile(
    r"\*\*Verdict: the company has (?P<verdict>[A-Z][A-Za-z ]+?) — "
    r"(?P<points>\d+) out of 100\.\*\*")
COVERAGE_RE = re.compile(
    r"Across (?P<got>\d+) of (?P<want>\d+) measure-and-window pairs[^.]*?"
    r"scored (?P<mean>[-+][\d.]+) on the")
# "| last 10 years | +43% · gained strongly | -14% · lagged | ... |"
WINDOW_ROW_RE = re.compile(r"^\| last (\d+) years? \|(.+)\|\s*$", re.M)
CELL_RE = re.compile(r"^\s*(?P<pct>[-+]?\d+)% · (?P<word>[a-z ]+?)\s*$")


def _section(md: str, head: str, stop: str = "\n## ") -> str:
    if head not in md:
        return ""
    body = md.split(head, 1)[1]
    return body.split(stop)[0]


def _measures(block: str) -> list[str]:
    """Column headers of the window table, in order."""
    m = re.search(r"^\| Window \|(.+)\|\s*$", block, re.M)
    if not m:
        return []
    return [c.strip() for c in m.group(1).split("|") if c.strip()]


def _window_table(block: str) -> list[dict]:
    """[{window, cells: {measure: {pct, word}}}] straight from the table."""
    cols = _measures(block)
    rows = []
    for m in WINDOW_ROW_RE.finditer(block):
        window = int(m.group(1))
        raw = [c for c in m.group(2).split("|")]
        cells = {}
        for i, cell in enumerate(raw):
            if i >= len(cols):
                break
            hit = CELL_RE.match(cell)
            cells[cols[i]] = ({"pct": int(hit.group("pct")),
                               "word": hit.group("word").strip()}
                              if hit else {"pct": None,
                                           "word": cell.strip() or None})
        rows.append({"window": window, "cells": cells})
    rows.sort(key=lambda r: -r["window"])
    return {"measures": cols, "rows": rows}


def from_analysis(md: str) -> dict | None:
    """Section 4 of a stored analysis report, or None if it has none."""
    block = _section(md, SECTION_HEAD)
    if not block:
        return None
    v = VERDICT_RE.search(block)
    cov = COVERAGE_RE.search(block)
    table = _window_table(block)
    chart = ""
    fence = re.search(r"```\n(.*?)```", block, re.S)
    if fence:
        chart = fence.group(1)
    return {
        "scored": bool(v),
        "verdict": v.group("verdict") if v else None,
        "points": int(v.group("points")) if v else None,
        "coverage": ({"answered": int(cov.group("got")),
                      "possible": int(cov.group("want")),
                      "mean": float(cov.group("mean"))} if cov else None),
        "measures": table["measures"],
        "windows": table["rows"],
        "chart_text": chart.rstrip("\n"),
        # the sentence the report itself uses to explain the scale
        "note": ("Each ratio is the company divided by the index, so a rise "
                 "means the company outgrew the index and a fall means it "
                 "lagged."),
    }


def from_comparison(md: str) -> dict | None:
    """Bucket 4 of a stored comparison report: long run vs latest year."""
    block = _section(md, BUCKET_HEAD)
    if not block:
        return None
    long_m = re.search(r"the company has \*\*(?P<v>[^*]+)\*\* "
                       r"\((?P<p>\d+)/100\)", block)
    recent_m = re.search(r"latest year, it has \*\*(?P<v>[^*]+)\*\*"
                         r"(?: \((?P<p>\d+)/100\))?", block)
    row = re.search(r"^\| Relative to the index \| (\d+|—) \| (\d+|—) \| "
                    r"([-+]\d+|—) \|", md, re.M)
    table = _window_table(block)
    return {
        "scored": bool(long_m),
        "long_verdict": long_m.group("v") if long_m else None,
        "long_points": int(long_m.group("p")) if long_m else None,
        "recent_verdict": recent_m.group("v") if recent_m else None,
        "recent_points": (int(recent_m.group("p"))
                          if recent_m and recent_m.group("p") else None),
        "delta": (None if not row or row.group(3) == "—"
                  else int(row.group(3))),
        "measures": table["measures"],
        "windows": table["rows"],
    }


# ------------------------------------------------- the full index workup

# "## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)"
RATIO_HEAD_RE = re.compile(
    r"^## (?P<n>\d)\. (?P<label>[^—\n]+?) — (?P<desc>[^\n]+)$", re.M)
# sections 1-3 are the three ratios; 4 is the line graph and 5 the raw values
RATIO_SECTIONS = {"1", "2", "3"}
NO_TREND_RE = re.compile(r"\*\*Verdict: (too little[^*]+?)\.?\*\*")
RATIO_VERDICT_RE = re.compile(
    r"\*\*Verdict: (?P<verdict>[A-Z][^:]+): the ratio (?P<dir>rose|fell) "
    r"(?P<pct>[-+][\d.]+)% from FY(?P<from>\d{4}) to FY(?P<to>\d{4})\.\*\*")
# "FY2016  ██████  37.536  ▲ +2.4% vs prior year" — the PAT and operating
# -profit ratios print as a percentage of the index, so the value itself may
# carry a trailing % before the year-on-year arrow.
LEVEL_RE = re.compile(
    r"^FY(?P<fy>\d{4})\s+[█▏▎▍▌▋▊▉ ]*\s*(?P<value>[-\d,.]+)(?P<unit>%?)"
    r"(?:\s+[▲▼▬]\s*(?P<yoy>[-+][\d.]+)%)?", re.M)
# "| last 10 years | FY2016 | FY2026 | +43% |"
WCHANGE_RE = re.compile(
    r"^\| last (?P<w>\d+) years? \| (?P<from>FY\d{4}|n/a) \| "
    r"(?P<to>FY\d{4}|n/a) \| (?P<change>[^|]+?) \|\s*$", re.M)
RAW_ROW_RE = re.compile(r"^\| FY(\d{4}) \|(.+)\|\s*$", re.M)


def _num(s: str):
    s = s.strip().replace(",", "")
    if s in ("", "—", "n/a"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def from_workup(md: str) -> dict | None:
    """The {SYM}_stock_to_index.md report: three ratio series with their
    levels, year-on-year moves, window changes, and the raw values."""
    if not md.strip():
        return None
    heads = list(RATIO_HEAD_RE.finditer(md))
    ratios = []
    for i, h in enumerate(heads):
        if h.group("n") not in RATIO_SECTIONS:
            continue          # the line graph and the raw-values sections
        end = heads[i + 1].start() if i + 1 < len(heads) else len(md)
        block = md[h.start():end]
        v = RATIO_VERDICT_RE.search(block)
        levels = [{"fy": int(m.group("fy")),
                   "value": _num(m.group("value")),
                   "unit": m.group("unit") or "",
                   "yoy": (float(m.group("yoy")) if m.group("yoy") else None)}
                  for m in LEVEL_RE.finditer(block)]
        # a ratio the stored data cannot span says so in its own words —
        # surfacing that beats silently dropping the measure
        nt = NO_TREND_RE.search(block)
        windows = []
        for m in WCHANGE_RE.finditer(block):
            change = m.group("change").strip()
            pct = None
            hit = re.match(r"^([-+]?\d+)%$", change)
            if hit:
                pct = int(hit.group(1))
            windows.append({"window": int(m.group("w")),
                            "from": m.group("from"), "to": m.group("to"),
                            "pct": pct, "text": change})
        ratios.append({
            "label": h.group("label").strip(),
            "description": h.group("desc").strip(),
            "unavailable": (nt.group(1).strip() if nt and not levels else None),
            "verdict": v.group("verdict") if v else None,
            "change_pct": float(v.group("pct")) if v else None,
            "from_fy": int(v.group("from")) if v else None,
            "to_fy": int(v.group("to")) if v else None,
            "levels": levels,
            "windows": windows,
        })

    raw_block = _section(md, "## 5. The raw yearly values behind every ratio",
                         "\n---")
    cols, rows = [], []
    hdr = re.search(r"^\| Fiscal year \|(.+)\|\s*$", raw_block, re.M)
    if hdr:
        cols = [c.strip() for c in hdr.group(1).split("|") if c.strip()]
        for m in RAW_ROW_RE.finditer(raw_block):
            vals = [c.strip() for c in m.group(2).split("|")][:len(cols)]
            rows.append({"fy": int(m.group(1)),
                         "values": [None if v in ("—", "") else v
                                    for v in vals]})
    return {"ratios": ratios, "raw": {"columns": cols, "rows": rows}}


# ------------------------------------------------------------------ loading

def workup_path(qa_dir: Path, sym: str) -> Path:
    return qa_dir / f"{sym}_stock_to_index.md"


def load(qa_dir: Path, sym: str, analysis_md: str,
         comparison_md: str) -> dict:
    """Everything the UI needs about one company's index comparison."""
    wp = workup_path(qa_dir, sym)
    workup_md = wp.read_text() if wp.exists() else ""
    svg = qa_dir / f"{sym}_stock_to_index.svg"
    return {
        "symbol": sym,
        "index": "Nifty 50",
        "section": from_analysis(analysis_md),
        "comparison": from_comparison(comparison_md),
        "workup": from_workup(workup_md),
        "has_workup": bool(workup_md.strip()),
        "has_svg": svg.exists(),
    }
