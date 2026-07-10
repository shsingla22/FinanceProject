---
name: business-analysis
description: >
  Identify the best-quality businesses by scoring companies against a complete
  34-parameter quality-investing framework (capital allocation, return on
  capital, growth, management, industry structure, customer benefits,
  competitive advantage). Works over a company's financial statements
  (P&L, balance sheet, cash flow, working capital) AND its qualitative record
  (conference-call transcripts, annual reports, management history), combining
  quantitative signals with human-commentary judgement into an explainable,
  ranked verdict. Use when asked to analyse, rank, screen, or compare businesses
  by fundamental quality, or to build software that does so.
license: internal
---

# Business Analysis — quality-investing framework skill

## What this skill does

Given a list of companies that each have financial + textual data, it scores
them against a **complete quality framework of 7 modules and 34 parameters**
(transcribed from `Company_analysis.docx`), producing for each company an
**explainable, source-cited quality score and ranking** that fuses:

- **Quantitative signals** computed from the CSV financials (return on capital,
  asset turns, margins & their stability, working-capital cycle, growth
  persistence, capex intensity, distributions), and
- **Qualitative judgement** extracted from conference calls, annual reports, and
  management history (capital-allocation intent, management quality, industry
  structure, customer benefits, moat).

No parameter is skipped: `reference/checklist.yaml` is the authoritative list and
`tests/test_parameters_complete.py` fails if any is missing.

## Files (what to read, in order)

| File | Purpose |
|---|---|
| `reference/framework.md` | The full framework in prose — read this to understand the philosophy |
| `reference/parameters.yaml` | **Canonical machine-readable taxonomy** — every parameter with nature, data sources, signal, direction |
| `reference/checklist.yaml` | The completeness guarantee (all 34 parameters) |
| `reference/data_sources.md` | Where each parameter's data lives, and availability caveats |
| `reference/qualitative_playbook.md` | How to judge every qualitative/hybrid parameter from text |
| `reference/scoring_rubric.md` | The −2..+2 scale, thresholds, weights, aggregation |
| `reference/glossary.md` | Definitions so scoring is consistent |
| `reference/examples.md` | The worked company examples from the document |
| `scripts/framework.py` | Load + validate the taxonomy (run it first) |
| `scripts/quant_signals.py` | Compute the quantitative signals for a symbol |
| `scripts/scoring.py` | Pure scoring / module + overall aggregation / ranking |
| `templates/analysis_record.schema.json` | The explainable result schema (persist this) |
| `templates/company_analysis_report.md` | Human-readable report template |

## Workflow (per company)

1. **Load the framework:** `python3 scripts/framework.py` — confirms all 34
   parameters are present and valid. Read `parameters.yaml` to get the list.
2. **Quantitative pass:** `python3 scripts/quant_signals.py <SYMBOL> --universe <U>`
   → raw signals + evidence for the quantitative/hybrid parameters. Parameters
   whose data is not separable (R&D, A&P, growth-vs-maintenance capex split)
   return `data_available: false` — hand those to the qualitative pass.
3. **Qualitative pass:** for every qualitative and hybrid parameter, follow
   `reference/qualitative_playbook.md` over the concall transcript / annual
   report / management CSV. Emit a `ParamScore` (−2..+2 + rationale + quote +
   source). Score `None` if the text is silent — never guess.
4. **Score & aggregate:** map quantitative values to −2..+2 with the rubric's
   thresholds (`scoring.quant_to_score`), reconcile hybrids (text arbitrates
   intent), then `scoring.aggregate(...)` → module scores + overall + coverage.
5. **Emit the record:** serialize to `analysis_record.schema.json` (the
   explainable decision tree) and render `company_analysis_report.md`.
6. **Rank:** across companies, `scoring.rank(...)` orders best-first by
   `(overall_score, coverage)`.

## How quantitative and qualitative combine (important)

- **Quantitative** answers "what do the numbers say" — deterministic, cited to a
  cell. **Qualitative** answers "what does management/industry/customer reality
  say" — cited to a quote. 30 of 34 parameters need the qualitative layer (16
  pure + 14 hybrid), so **the text is the majority of this framework**, not an
  add-on.
- For a **hybrid** parameter, if the two disagree, **the text arbitrates intent**
  and the rationale must state the conflict (e.g. high capex that commentary
  reveals is maintenance ⇒ do not credit as growth capex).

## Explainability (build follow-ups on this)

The result is a **decision tree**: overall → 7 modules → 34 parameters, each node
carrying `score + rationale + evidence + sources`. Persist it (schema provided) so
a user can drill from the headline verdict to the exact number or quote, and so a
follow-up agent can **re-run any single parameter's scoring deterministically**
(counterfactuals: "what if working capital improved?"). Never explain a conclusion
by re-reading code from memory — explain it from the persisted record.

## For an autonomous agent building software on top of this

- `parameters.yaml` is the contract: iterate it to enumerate work; `nature` tells
  you which engine (quant vs qualitative-LLM) owns each parameter; `data_sources`
  tells you what to fetch; `direction` + the rubric tell you how to score.
- `scripts/` are importable pure modules (no network, no wall-clock) — safe to
  wrap in an API, a batch job, or an MCP tool.
- Data location is **discovered** (`base` path + `universe`), never hard-coded, so
  the same skill runs over `Nifty500`, `NiftyTotalMarket`, or any same-layout
  universe.
- Everything is **tested**: `python3 -m pytest tests/` (framework completeness,
  scoring math, and the quant engine against a bundled fixture universe).

## Guardrails

- **No parameter skipped** — enforced by the completeness test.
- **No bare scores** — every score carries evidence + a source.
- **Honest coverage** — unassessed parameters are `None` and reduce coverage; a
  high score at low coverage is reported as the weaker claim it is.
- **Data caveats surfaced** — R&D / A&P not separable, GM proxied from Material
  Cost %, capex split inferred qualitatively, short histories flagged.

## Requirements

Python 3.10+, `pandas`, `pyyaml` (see `requirements.txt`). The quantitative engine
expects the repo's long-format CSVs under `<base>/<Statement>/<universe>/`; if
absent, it degrades gracefully (signals simply become unavailable) and the
qualitative layer still runs.
