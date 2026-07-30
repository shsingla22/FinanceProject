---
name: recent-analyst-skill
description: >
  The AnalystSkill through a one-year lens: exactly the same complete
  company analysis — the BusinessAnalysis 34-check quality framework, the
  11 MultibaggerPattern patterns and the 8 QualityRisks channels, combined
  into one explainable rating and one coherent report — but every piece of
  evidence is restricted to the LAST ONE YEAR (latest fiscal year with the
  prior year as comparison baseline; last 12 months of earnings calls).
  Answers "what does this business look like RIGHT NOW?" Use when asked
  for a recent-period / last-one-year analysis of a company; use the
  full-history AnalystSkill for the long view.
license: internal
---

# RecentAnalystSkill — the AnalystSkill, last one year

## What this skill is

**It IS the AnalystSkill.** It loads the AnalystSkill's own registry and
composer — same sibling skills, same check engines, same verdict ladders,
same rating arithmetic, same report structure — and applies exactly one
change, at the DATA layer (`scripts/window.py`):

| Evidence | Full AnalystSkill | This skill |
|---|---|---|
| Financial statements | ~12 fiscal years | latest fiscal year + the prior year (baseline only) |
| Conference calls | whole timeline, sampled oldest→newest | the last 4 quarterly calls (~12 months) |
| Judge instruction | judge the multi-year trajectory | judge the CURRENT state; null when a call needs history it doesn't have |
| AI caches | AnalystSkill folder | this folder — fully separate, the two skills never share a verdict |

Because the window is applied where the data is read, every engine
behaves identically and honestly: level checks (margins, capital
intensity, working-capital days, leverage) assess normally; trend checks
that genuinely need longer history return "not assessed" — and their
explanations say WHY: *"(One-year lens: this view only sees the latest
two financial years, so longer-trend checks are out of scope by
design.)"* The window can never silently compute on data it excludes.

## Run it

```bash
cd IndividualStockAnalysis/India/Skills/RecentAnalystSkill
python3 scripts/analyze.py report DIXON dixon_1y.md          # full (AI)
python3 scripts/analyze.py report DIXON dixon_1y.md --quick  # numbers only
python3 scripts/analyze.py company DIXON                     # JSON record
python3 scripts/analyze.py batch DIXON CRISIL --out-dir out/
```

Judge model: `ANALYST_MODEL` (default Opus 5, `claude-opus-5`). The report
is the AnalystSkill report — About the business, the verdict with its
arithmetic, three complete sections, charts, what to watch — titled
"· Last One Year" with a lens banner explaining the window up front, and
a methodology section stating the restriction.

## Explainability

Inherited unchanged from the AnalystSkill and extended for the lens:
every check explains itself from its numbers, every judge verdict carries
rationale + verbatim quote or abstains, every ladder position states its
why, the rating lists its arithmetic, the summary is grounded-or-dropped
— AND every check the window silences carries the lens note so the reader
knows the absence is a design choice, not missing data.

## Files

| File | Purpose |
|---|---|
| `scripts/window.py` | the one-year lens: frame filters (last 2 FYs per company), last-4-calls timeline, lens-prefixed judge prompts, separate caches, window-aware explanations, lens banner on the report |
| `scripts/analyze.py` | CLI identical to the AnalystSkill: `report` · `company` · `batch` |
| `tests/test_skill.py` | 10 tests: window applied to all three engines and the charts, timeline ≤4 recent calls, lens instruction in every judge prompt, caches separate from the full-history skill, lens-note on silenced checks, level checks still assess, record shape identical, report structure + banner, jargon scan, and the lens must actually change a verdict (a 2-point window cannot claim a multi-year growth check) |

## Honest limitations

- A one-year window cannot see trends: pattern/risk checks built on
  multi-year fingerprints stay honestly unassessed, so quant-only runs
  are thinner than the full skill's — by design.
- `window.py` windows the engine instances in-process; run this skill in
  its own process (the CLI does). Don't import it alongside the
  full-history AnalystSkill in one interpreter.
- Ratings from this skill answer a different question than the full
  skill's — compare the two reports, don't average them.
