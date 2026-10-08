---
name: analyst-skill
description: >
  The orchestrator: executes every sibling analysis skill in this folder —
  BusinessAnalysis (34-check quality framework), MultibaggerPattern (11
  patterns long-term winners share), QualityRisks (8 channels through
  which quality companies fail) and StockToIndexPriceEarningsRatio (price,
  profit after tax and operating profit measured against the Nifty 50) —
  on one company and composes their explainable records into ONE coherent
  analyst's report: an AI-written grounded summary that connects the
  analyses, a combined 0–100 rating with every point earned or lost
  listed, the evidence sections, and a what-to-watch list. Use when asked for a complete,
  single-document analysis of a company.
license: internal
---

# AnalystSkill — the orchestrator

## What this skill does

It does **no analysis of its own**. It discovers and executes the sibling
skills in this folder, then composes their records into one coherent
report, in reading order:

1. **The analyst's summary** — a narrative that CONNECTS the three
   analyses (when the same trait drives both a pattern and a risk, it says
   so), written by the judge model STRICTLY from the records. A grounding
   gate scans it: any pattern/risk/area name that does not exist in the
   records rejects the whole summary — it is omitted honestly rather than
   published unverified.
2. **The rating** — business quality 45% + multibagger fit 30% + risk
   safety 25% = one score out of 100 with a plain-words grade
   (Outstanding / Strong / Decent / Mixed / Weak) and stars. Every pillar
   lists exactly what earned or cost points; the composite states its
   arithmetic in one sentence.
3. **Three evidence sections** — one per skill, every verdict carrying its
   "why", rationale, verbatim call quote and numeric evidence.
4. **What to watch** — the open questions the evidence left, each tied to
   a named pattern, risk or check.
5. **How this report was built** — which skills ran, on what evidence
   ("with_calls" vs "numbers_only"), and the honesty rules.

## Run it

```bash
cd IndividualStockAnalysis/India/Skills/AnalystSkill
python3 scripts/analyze.py report DIXON dixon.md          # full (AI judges + synthesis)
python3 scripts/analyze.py report DIXON dixon.md --quick  # numbers only, no AI
python3 scripts/analyze.py company DIXON                  # combined JSON record
python3 scripts/analyze.py batch DIXON CRISIL TITAN --out-dir reports/
                                                          # one MD per company
```

## Run it over YOUR OWN document (`--source`)

The analysis normally reads the repository's stored data — statements from
the CSV archives, qualitative evidence from the company's conference-call
PDF. `--source` swaps the qualitative evidence for a document YOU supply
(a PDF, a Markdown file, or plain text), judged by the same skills under
the same honesty rules:

```bash
# a universe company, judged against a supplied document instead of its calls
python3 scripts/analyze.py report DIXON out.md --source ~/annual_report.pdf

# a company that is NOT in the universe at all — notes, a prospectus, a memo
python3 scripts/analyze.py report ACME out.md --source notes.md --name "Acme Ltd"
```

What holds, by design (`scripts/source_override.py`):

- **The quantitative side is untouched.** A symbol in the universe keeps
  its statements, trends and index comparison; an unknown company honestly
  has none, and the rating re-normalises over what could be scored — a
  document alone with no judged evidence composes a **Not rated** report,
  never an invented number.
- **No mixing of evidence.** The concall archive is not read in a source
  run, and supplied-document judgements are cached in separate,
  gitignored files (`.source_*_cache.json`) keyed by the document's
  content hash — re-running the same document is free, an edited document
  is honestly a fresh judgement, and the committed archive caches are
  never touched.
- **Provenance in the report itself.** The generated Markdown names the
  supplied document (file, kind, size, hash) under "How this report was
  built", so the file alone tells a reader what evidence produced it.

## Extensibility — future skills join automatically

The three current skills run natively, in a fixed, deliberate order:
**BusinessAnalysis** (what the business is) → **MultibaggerPattern** (what
it could become) → **QualityRisks** (what could stop it). Any FUTURE
sibling skill joins the analysis by shipping an `analyst_interface.py` in
its folder exposing `run(symbol, ai=True) -> dict` with at least
`{name, status, record}` and optionally `order`, `pillar` (points 0–100 +
derivation + weight — folded into the rating with ALL weights
re-normalized to keep the arithmetic honest), `section_md` (its own report
section) and `facts` (fed to the analyst's-summary synthesis and its
grounding vocabulary). No AnalystSkill code change needed. A broken
extension is reported in the methodology section — never silently dropped,
never allowed to sink the report. The contract is unit-tested with a fake
future skill.

The judge/synthesis model is `ANALYST_MODEL` (default **Opus 5,
`claude-opus-5`**, via the Claude Code CLI on your subscription); it is
propagated to the sibling skills' judges so one variable steers everything.
First run of a company = three deep concall reads + one synthesis call
(several minutes, no timeouts); every step is cached — the sibling judges
per transcript+model in their own folders, the summary per record content
in `.synth_cache.json` here (so it regenerates whenever any underlying
verdict changes).

## Files

| File | Purpose |
|---|---|
| `scripts/registry.py` | discovers + loads the sibling skills collision-safely, executes each; the BusinessAnalysis concall pass lives here (the sibling itself is quant-only) |
| `scripts/composer.py` | pillars → rating with derivations; grounded-or-dropped synthesis; the coherent Markdown report |
| `scripts/analyze.py` | CLI: `report SYM out.md [--quick]` · `company SYM [--quick]` · `batch SYM… --out-dir DIR [--quick]` |
| `tests/test_skill.py` | 11 tests: sibling discovery, real-data execution of all three, honest quick-mode coverage, rating bounds + arithmetic-matches-its-claim, report coherence/order, jargon scan, synthesis grounding gate, extension contract (fake future skill discovered/executed/folded in; broken extension can't sink the report) |

## Explainability

Inherited from the siblings and preserved end-to-end: every number's check
explains itself, every judge verdict carries rationale + verbatim quote,
every ladder position states its "why", the rating lists its arithmetic —
and the one new AI step this skill adds (the summary) is grounded-or-
dropped by construction. Statuses in the methodology section say exactly
what evidence each skill ran on.

## Honest limitations

- Report quality is bounded by the siblings: no concall transcript means
  numbers-only pillars and no summary.
- The quant→score mapping and its humanized wording are shared with the
  UI layer (`UserInterface/build_data.py`) — one source of truth.
- The summary can only connect what the records contain; it never adds
  outside knowledge, and the grounding gate enforces that mechanically.


## The combined rating

Four pillars, weighted:

| Pillar | Weight | From |
|---|---|---|
| Business quality | 40.5% | BusinessAnalysis |
| Multibagger fit | 27% | MultibaggerPattern |
| Risk safety | 22.5% | QualityRisks |
| Relative to the index | 10% | StockToIndexPriceEarningsRatio |

The first three keep their historic 45/30/25 proportions, scaled to 90%
so the index pillar takes exactly 10%. `compute_rating` re-normalises
over whatever can actually be scored, so a company whose stored history
is too short to compare with the index falls back to the original
45/30/25 split rather than being marked down for missing data.

The index pillar scores the change in the company-to-index ratio over
the last 10, 5, 3 and 1 fiscal years, on the same −2..+2 scale the
34-check framework uses, mapped onto 0–100. It reads stored data only —
no AI call, no network.

### Wiring

It arrives through the extensibility contract in `scripts/registry.py`:
`StockToIndexPriceEarningsRatio/analyst_interface.py` declares the
pillar, its 10% weight and its report section, so the analyst picks it
up automatically. Nothing in the orchestrator hard-codes it.

### Back-filling the stored reports

`scripts/add_relative_index.py` folds the new pillar into reports that
already exist, instead of re-running thousands of judge calls for
verdicts that have not changed. It rescores the headline, adds the
fourth pillar bullet and Section 4 to `{SYM}_analysis.md`, and adds the
pillar row and Bucket 4 to `{SYM}_comparison.md`. It is idempotent —
running it twice gives the same file as running it once — and it only
ever adds: every existing verdict, quote, chart and derivation is kept.

```bash
python3 scripts/add_relative_index.py            # all 742 companies
python3 scripts/add_relative_index.py --symbols DIXON,TITAN
python3 -m pytest tests/ -q                      # 56 tests
```
