---
name: multibagger-pattern
description: >
  Identify which multibagger patterns a company fits — Recurring Revenue,
  Friendly Middleman, Toll Roads, Low Price Plus, Pricing Power, Brand
  Strength, Innovation Dominance, Forward Integration, Market Share Gainers,
  Corporate Culture, and Cost to Replicate — by combining quantitative
  evidence from stored financial statements (balance sheet, P&L, cash flow,
  working capital) with qualitative judgement over conference-call
  transcripts and management history. Every verdict states WHICH patterns fit
  and HOW the conclusion was reached, with evidence attached at compute time.
  Use when asked to find multibagger candidates, test a company against these
  patterns, or explain a pattern verdict.
license: internal
---

# MultibaggerPattern — pattern-matching skill

## What this skill does

Transcribed in full from `Multibagger_patterns.docx`: a **core-principle
foundation gate** (strong predictable cash generation + sustainable high
returns on capital + attractive growth) and **11 multibagger patterns**, each
with its traits, quantitative fingerprints, qualitative markers, worked
examples (KONE, Geberit, CHR Hansen, Hermès, Diageo, Novo Nordisk, Luxottica,
Fielmann, Handelsbanken…) and explicit red flags (price deflation, share
bought with bad credit).

Given a company from the NiftyTotalMarket dataset it produces an explainable
verdict per pattern on a fixed ladder:

| Verdict | Meaning |
|---|---|
| STRONG FIT | the concall judge confirms AND the numbers agree |
| LIKELY FIT | good evidence on one side, not yet conclusive |
| QUANT SIGNAL | the numbers alone point this way — needs call evidence |
| PARTIAL | some traits present |
| NO FIT | evidence contradicts the pattern |
| NOT ASSESSED | insufficient evidence (never guessed) |

## Files

| File | Purpose |
|---|---|
| `reference/patterns.yaml` | canonical taxonomy — 11 patterns, traits, checks, markers, examples, red flags |
| `reference/checklist.yaml` | completeness guarantee (tests fail if a pattern or check goes missing) |
| `scripts/quant_evidence.py` | computable checks over the stored CSVs; every check returns value + plain-English explanation |
| `scripts/pattern_engine.py` | taxonomy loader/validator, deterministic verdict combiner, core gate, explainable record |
| `scripts/analyze.py` | CLI: `screen` the universe · `company SYM [--ai]` · `report SYM out.md [--ai]`; the `--ai` judge reads the concall timeline + management history via headless Claude (Fable by default, `MB_JUDGE_MODEL` to override; no timeout, cached per transcript+model) |
| `tests/test_skill.py` | 14 tests: completeness, synthetic profiles shaped like the document's examples, verdict ladder, explainability contract, report jargon scan, real-data integration |

## How the conclusion is reached (built-in explainability)

- Every **quant check** is born with its explanation, templated from the same
  numbers that decided it ("Customers effectively fund the business — cash
  arrives 38 days before suppliers are paid").
- The **qualitative judge** must return fit + rationale + verbatim quote per
  pattern, or null when the calls are silent — never a bare verdict.
- The **combiner** is a deterministic, unit-tested ladder — no hidden
  weighting; a judge's "none" overrides supportive numbers, and numbers alone
  can never claim more than "QUANT SIGNAL".
- The **record** is a tree: company → foundation gate → 11 pattern verdicts →
  per-check evidence and per-pattern quotes. The Markdown report renders that
  record; it never re-narrates.

## Data sources

`IndividualStockAnalysis/India/{BalanceSheet, ProfitStatement, CashFlow,
WorkingCapital, ConferenceCalls, ManagementInfo}/NiftyTotalMarket/` — the
same long-format CSVs and merged transcript PDFs the other skills use.
Location is discovered relative to the skill; no hard-coded absolute paths.

## Honest limitations

- R&D %, attach rates, market shares and franchise mix are not separable in
  the standard statements — those signals come only from the concall judge.
- Quant checks are FINGERPRINTS, not proofs: high stable margins are
  consistent with several patterns, which is why numbers alone cap out at
  "QUANT SIGNAL".
- CULTURE and MOATTEST are qualitative-only by design.
