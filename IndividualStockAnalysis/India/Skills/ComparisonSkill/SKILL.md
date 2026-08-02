---
name: comparison-skill
description: >
  Compare the AnalystSkill's full-history analysis with the
  RecentAnalystSkill's last-one-year analysis of the same company and
  answer: is it improving or regressing? Step 1 calls out the overall
  rating difference (improved / declined / held steady, with the exact
  point delta and both derivations). Step 2 details every movement in
  three buckets — the 34-check quality framework, the 11 multibagger
  patterns and the 8 risk channels — each with an overall comparison and
  point-wise transitions carrying both sides' evidence. Generates a
  Markdown comparison per company. Use when asked whether a company has
  improved or regressed recently, or for a then-vs-now view.
license: internal
---

# ComparisonSkill — Then vs Now

## What this skill does

The AnalystSkill answers "what has this business been over the long
run?"; the RecentAnalystSkill answers "what does it look like RIGHT
NOW?". This skill runs both (each through its own CLI in a separate
process — the one-year skill windows its engines in-process, so they must
never share an interpreter; each side's AI judge caches are reused) and
composes the third answer: **is it improving or regressing?**

The report, in the order you specified:

1. **Step 1 — the overall rating difference, first.** "Long-term view:
   Decent (58/100). Last one year: Mixed (45/100). The last year looks
   WEAKER than the long-term picture (−13 points) — the company has
   declined in the recent period." Plus the pillar delta table, both
   sides' full derivations, and a note that pillar moves can be partly
   lens-driven (Step 2 separates genuine movement from window effects).
2. **Step 2 — three buckets**, one per skill, each with an overall
   comparison line and point-wise detail:
   - **Business quality:** area-by-area delta table over the 7 areas,
     then every check that improved / regressed / stayed unchanged, each
     movement carrying BOTH sides' rationales ("Now: … | The long view
     had said: …").
   - **Multibagger patterns:** all 11 verdict transitions on the ladder
     (strengthened / weakened / unchanged), plus the foundation-gate
     comparison.
   - **Risks:** all 8 severity transitions (eased / worsened /
     unchanged — direction correctly inverted: moving toward severity is
     the regression), plus the financial-resilience comparison.

## Honest-comparison rules (enforced by tests)

- Only items assessed on BOTH views are compared.
- Checks the one-year lens silences by design (trend checks needing
  longer history) are listed separately as "not comparable in the
  window" and are NEVER counted as regressions.
- A side that could not be rated makes the overall comparison "not
  comparable" — stated, not fudged.
- Every movement line carries both sides' evidence, so the WHY of the
  change is visible, not just the direction.

## Run it

```bash
cd IndividualStockAnalysis/India/Skills/ComparisonSkill
python3 scripts/analyze.py report DIXON dixon_compare.md          # full (AI)
python3 scripts/analyze.py report DIXON dixon_compare.md --quick  # numbers only
python3 scripts/analyze.py company DIXON                          # JSON record
python3 scripts/analyze.py batch DIXON CRISIL --out-dir out/
```

A company already analysed by both underlying skills compares in a
minute or two (cached judges); a never-analysed company triggers both
full analyses first (several minutes per side).

## Files

| File | Purpose |
|---|---|
| `scripts/compare_engine.py` | runs both sides via their CLIs (subprocess isolation), computes the explainable comparison record: rating delta, pillar deltas, per-check/pattern/risk transitions under the honest-comparison rules |
| `scripts/analyze.py` | CLI (`report` · `company` · `batch`) + the Markdown renderer in the two-step order |
| `tests/test_skill.py` | 9 tests: rating direction (improved/declined/held/not-comparable), per-check classification with both-sides evidence, the lens-silence-is-never-a-regression rule, pattern transition direction, inverted risk direction, report section order + jargon scan, real end-to-end quick run, and a RUN_SWEEP=1 stratified 20-company coverage sweep (compounders, cyclicals, PSUs, lenders, recent listings) |
