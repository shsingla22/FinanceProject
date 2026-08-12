"""
rank_companies.py — rank every analysed company from best to worst.

Reads all stored report pairs in this folder, extracts each company's
AnalystSkill rating (grade + score out of 100) and its one-year
direction from the ComparisonSkill report, and writes:

  RANKING.md      the full ranked list, best to worst, in tiers
  _ranking.csv    the same as data (rank, symbol, name, score, grade,
                  one-year direction)

Re-run any time — it re-ranks whatever reports exist:
  python3 rank_companies.py
"""

from __future__ import annotations

import csv
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONST = HERE.parent.parent.parent / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv"


def collect() -> tuple[list, list]:
    names = {r["nse_symbol"]: r["company_name"]
             for r in csv.DictReader(open(CONST))}
    rated, unrated = [], []
    for a in sorted(HERE.glob("*_analysis.md")):
        sym = a.name[: -len("_analysis.md")]
        md = a.read_text()
        m = re.search(r"^## The verdict: (.+?)(?:\s*[—(]|$)", md, flags=re.M)
        s = re.search(r"(\d+) out of 100", md)
        grade = m.group(1).strip() if m else "?"
        c = HERE / f"{sym}_comparison.md"
        direction = ""
        if c.exists():
            d = re.search(r"## Step 1 — The overall rating: (.+)",
                          c.read_text())
            if d:
                direction = (d.group(1).replace(" in the last year", "")
                             .replace("📈", "").replace("📉", "")
                             .replace("➡️", "").strip().lower())
        row = {"symbol": sym, "name": names.get(sym, sym),
               "grade": grade, "direction": direction}
        if s and grade != "Not rated":
            row["score"] = int(s.group(1))
            rated.append(row)
        else:
            row["score"] = None
            unrated.append(row)
    rated.sort(key=lambda r: (-r["score"], r["symbol"]))
    return rated, unrated


TIERS = [("Outstanding (80+)", 80), ("Strong (65–79)", 65),
         ("Decent (50–64)", 50), ("Mixed (35–49)", 35),
         ("Weak (below 35)", 0)]
ARROW = {"improved": "▲ improved", "declined": "▼ declined",
         "held steady": "▬ held steady",
         "could not be compared": "not comparable"}


def render(rated: list, unrated: list) -> str:
    L: list[str] = []
    A = L.append
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    A("# NiftyTotalMarket — Companies Ranked Best to Worst")
    A("")
    A(f"**{len(rated)} rated companies** (plus {len(unrated)} honestly not "
      f"rated), ranked by the AnalystSkill's combined rating out of 100 — "
      f"business quality 45%, multibagger-pattern fit 30%, risk safety 25% "
      f"— with each company's one-year direction from its ComparisonSkill "
      f"report. Generated {stamp} from the report pairs stored in this "
      f"folder; every score and arrow traces to the company's own two "
      f"reports, where the full point-by-point derivation lives.")
    A("")
    def tier_of(score: int) -> str:
        for name, floor in TIERS:
            if score >= floor:
                return name
        return TIERS[-1][0]

    rank = 0
    for tier_name, _ in TIERS:
        tier = [r for r in rated if tier_of(r["score"]) == tier_name]
        if not tier:
            continue
        A(f"## {tier_name}")
        A("")
        A("| # | Company | Symbol | Score | Grade | Last one year |")
        A("|---|---|---|---|---|---|")
        for r in tier:
            rank += 1
            A(f"| {rank} | {r['name']} | {r['symbol']} | {r['score']}/100 "
              f"| {r['grade']} | {ARROW.get(r['direction'], r['direction'] or '—')} |")
        A("")
    if unrated:
        A("## Not rated")
        A("")
        A("The frameworks could not honestly score these (usually lenders "
          "or companies with too little assessable evidence) — a limitation "
          "stated rather than a guess made:")
        A("")
        for r in unrated:
            A(f"- **{r['name']}** ({r['symbol']})")
        A("")
    A("---")
    A(f"*Reports: `{{SYMBOL}}_analysis.md` (full workup) and "
      f"`{{SYMBOL}}_comparison.md` (then-vs-now) beside this file. "
      f"Research tooling, not investment advice.*")
    return "\n".join(L)


def main() -> None:
    rated, unrated = collect()
    md = render(rated, unrated)
    (HERE / "RANKING.md").write_text(md)
    with open(HERE / "_ranking.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["rank", "symbol", "name", "score",
                                          "grade", "one_year_direction"])
        w.writeheader()
        for i, r in enumerate(rated, 1):
            w.writerow({"rank": i, "symbol": r["symbol"], "name": r["name"],
                        "score": r["score"], "grade": r["grade"],
                        "one_year_direction": r["direction"]})
        for r in unrated:
            w.writerow({"rank": "", "symbol": r["symbol"], "name": r["name"],
                        "score": "", "grade": "Not rated",
                        "one_year_direction": r["direction"]})
    print(f"RANKING.md + _ranking.csv written: {len(rated)} rated, "
          f"{len(unrated)} not rated")


if __name__ == "__main__":
    main()
