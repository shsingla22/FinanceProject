---
name: quality-risks
description: >
  Identify which risks to quality investing a company is exposed to —
  Cyclicality, Technological Innovation, Government Dependency, Stakeholder
  Concentration, New Entrants, Shifting Consumer Preferences, Fashion Risk
  and Good Enough Goods — by combining risk fingerprints computed from the
  stored financial statements (balance sheet, P&L, cash flow, working
  capital) with qualitative judgement over conference-call transcripts and
  management history. Every verdict states WHICH risks are material, HOW
  severe, and HOW the conclusion was reached, with evidence attached at
  compute time. Use when asked to find risks in a company, stress-test a
  quality thesis, or explain a risk verdict.
license: internal
---

# QualityRisks — risk-identification skill

## What this skill does

Transcribed in full from `Risks_to_quality_investing.docx`: **eight risk
channels** through which strong businesses fail — Cyclicality (pure cycles,
customer-capex cyclicality, with flow products as the mitigant),
Technological Innovation (the Nokia case), Government Dependency (Europe's
solar boom-to-bankruptcy), Stakeholder Concentration (Safilo's lost
licences), New Entrants (deep discounters, quick commerce), Shifting
Consumer Preferences, Fashion Risk, and Good Enough Goods (Nobel Biocare's
34% → 13% margin collapse) — plus the document's silver linings (the strong
get stronger; countercyclical investment signals strength), kept as
explicit MITIGANT markers.

Given a company from the NiftyTotalMarket dataset it produces an
explainable verdict per risk on a fixed severity ladder:

| Verdict | Meaning |
|---|---|
| HIGH RISK | the concall judge sees high exposure AND the numbers agree (or the risk has no numeric fingerprint) |
| ELEVATED | high exposure without numeric confirmation, or moderate exposure the numbers reinforce |
| WATCH | moderate exposure, numbers quiet |
| QUANT FLAG | the numbers alone show the fingerprint — needs call evidence; numbers can never claim more |
| LOW | the judge affirmatively found mitigation (overrides numeric flags) |
| NO SIGNAL | nothing points to this risk today |
| NOT ASSESSED | insufficient evidence (never guessed) |

A cross-cutting **financial-resilience summary** (leverage rise, cash-
conversion slippage, sliding returns on capital) reports whether the
balance sheet could absorb a risk that bites: SOUND / STRAINED / STRESSED.

## Files

| File | Purpose |
|---|---|
| `reference/risks.yaml` | canonical taxonomy — 8 risks, traits, fingerprints, markers, examples, red flags, mitigants |
| `reference/checklist.yaml` | completeness guarantee (tests fail if a risk or check goes missing) |
| `scripts/risk_evidence.py` | computable risk fingerprints over the stored CSVs; every check returns value + plain-English explanation |
| `scripts/risk_engine.py` | taxonomy loader/validator, deterministic severity ladder, fragility summary, explainable record |
| `scripts/analyze.py` | CLI: `screen` the universe · `company SYM [--ai]` · `report SYM out.md [--ai]`; the `--ai` judge reads the concall timeline + management history via headless Claude (Opus by default, `RISK_JUDGE_MODEL` to override; no timeout, cached per transcript+model) |
| `tests/test_skill.py` | 17 tests: completeness, synthetic profiles shaped like the document's examples, severity ladder, explainability contract, report jargon scan, real-data integration |

## How the conclusion is reached (built-in explainability)

- Every **risk fingerprint** is born with its explanation, templated from
  the same numbers that decided it ("Operating margin has collapsed from a
  peak of 34% to 13% — the Nobel-Biocare-style fingerprint of a premium
  being competed away").
- The **qualitative judge** must return exposure + rationale + verbatim
  quote (and any mitigant) per risk, or null when the calls are silent —
  "low" only when mitigation is affirmatively shown, never by default.
- The **combiner** is a deterministic, unit-tested ladder — a grounded
  "low" overrides scary-looking numbers, and numbers alone can never claim
  more than "QUANT FLAG".
- The **record** is a tree: company → fragility summary → 8 risk verdicts →
  per-check evidence and per-risk quotes. The Markdown report renders that
  record; it never re-narrates.

## Data sources

`IndividualStockAnalysis/India/{BalanceSheet, ProfitStatement, CashFlow,
WorkingCapital, ConferenceCalls, ManagementInfo}/NiftyTotalMarket/` — the
same long-format CSVs and merged transcript PDFs the other skills use.
Location discovered relative to the skill; no hard-coded absolute paths.

## Honest limitations

- Customer/supplier concentration percentages, market shares and
  subsidy dependence are not separable in the standard statements — those
  signals come mainly from the concall judge.
- Quant fingerprints are FLAGS, not proofs: volatile margins are consistent
  with several risks, which is why numbers alone cap out at "QUANT FLAG".
- GOVT_DEPENDENCY is qualitative-only by design.
- A risk the calls never discuss stays NOT ASSESSED / NO SIGNAL — silence
  is not evidence of safety.
