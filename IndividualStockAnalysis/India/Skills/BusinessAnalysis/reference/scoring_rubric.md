# Scoring rubric

## Per-parameter scale (`-2 .. +2`)

| Score | Meaning |
|------:|---------|
| **+2** | Strong evidence FOR the quality trait |
| **+1** | Positive |
| **0**  | Neutral / mixed |
| **−1** | Negative |
| **−2** | Strong evidence AGAINST |
| `None` | Not assessed — no data / text silent (counted in *coverage*, not in the average) |

Every score must carry a **rationale** and **evidence** (numbers for quantitative,
quotes for qualitative). No bare scores — this is what makes the analysis
explainable and auditable.

## Quantitative → score mapping

`scoring.quant_to_score(value, direction, thresholds)` converts a raw signal to
`-2..+2` using explicit, injectable thresholds per signal (so they are tunable and
unit-tested). `direction` (`maximize` / `minimize`) comes from the framework;
`stable` and `context` parameters are scored by the qualitative layer, not
auto-mapped. Illustrative thresholds (tune per mandate):

| Signal | direction | strong (+2) | good (+1) | bad (−1) | weak (−2) |
|---|---|---|---|---|---|
| ROC.headline (CROCI proxy) | maximize | ≥ 0.25 | ≥ 0.15 | ≤ 0.08 | ≤ 0.04 |
| ROC.asset_turn | maximize | ≥ 1.5 | ≥ 1.0 | ≤ 0.5 | ≤ 0.3 |
| ROC.profit_margin (OPM level) | maximize | ≥ 25% | ≥ 15% | ≤ 8% | ≤ 3% |
| ROC.profit_margin (OPM std, penalty) | minimize | ≤ 2 | ≤ 4 | ≥ 8 | ≥ 12 |
| CAP.working_capital_cost (CCC days) | minimize | ≤ 0 | ≤ 30 | ≥ 90 | ≥ 150 |
| GRW.persistence (yoy_std, penalty) | minimize | ≤ 0.05 | ≤ 0.10 | ≥ 0.25 | ≥ 0.40 |

## Combining quantitative + qualitative (hybrid parameters)

A hybrid parameter has both a computed signal and a text judgement. Reconcile:
- If they **agree**, take the shared direction; confidence is high.
- If they **disagree**, the **text arbitrates intent** and the rationale must state
  the conflict. Classic case: high capex (quant looks like growth investment) but
  commentary reveals it is *maintenance* → do not credit `CAP.growth_capex`.

## Module and overall aggregation

- **Module score** = simple average of assessed parameter scores in the module
  (None ignored), plus a **coverage** ratio (assessed / total).
- **Overall score** = weighted average of module scores. Default weights favour
  durable economics and discipline: `ROC 1.25, IND 1.25, MOAT 1.25, CAP 1.0,
  GRW 1.0, MGT 1.0, CUS 1.0`. Tune per mandate.
- **Ranking** = sort by `(overall_score, coverage)` so a better-evidenced company
  outranks a thinly-evidenced one at the same score.

## Coverage discipline (why it matters)

The overall score is only as trustworthy as its coverage. Always report
`overall_coverage` and per-module coverage next to the score. A `+1.8` at 40%
coverage is a weaker claim than a `+1.2` at 90% coverage — the ranking key encodes
this, and any report/UI must show it.

## Explainability

The aggregate record IS a decision tree: overall → modules → parameters, each node
carrying score + rationale + evidence + sources. Persist it (see
`templates/analysis_record.schema.json`) so a user can drill from the headline
verdict down to the exact number or quote — and so a follow-up agent can re-run any
parameter's scoring deterministically.
