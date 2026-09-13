---
name: darvas-skill
description: >
  Nicolas Darvas's method, run mechanically over the NiftyTotalMarket
  universe: a weekly volume surge with the price appreciating is the
  trigger; rising earnings power (EBITDA, EBITDA margin, PAT, PAT margin
  from the stored statements) and a new-age-industry read from the
  conference calls are the confirmation; the stock's own Darvas boxes give
  the buy point, the accumulation point and the stop loss; a drop to a
  lower box is the exit. Fetches fresh weekly volume and price data on
  every run. Use when asked for momentum/Darvas screening, volume-surge
  candidates, box breakouts, or stop-loss levels.
license: internal
---

# DarvasSkill — the box method, mechanised

## The five steps, as implemented

1. **The volume trigger.** Fresh daily bars for the last six months are
   fetched for every symbol ON EVERY RUN and aggregated into
   Monday–Friday weeks. The week under test is THE LATEST week — the
   running (partial) week when there is one, pro-rated to five days
   (volume ÷ (average × days÷5)) and labelled, so a surge is caught the
   day it happens, never a week late. A stock qualifies at **1.5×** the
   average weekly volume of the prior 12 completed weeks (minimum 6)
   **and** a rising price — volume without price appreciation is
   distribution, price without volume is drift; Darvas required both.
   Tiers: ≥3× *multifold*, ≥2× *strong*, ≥1.5× *elevated*. The report
   lists EVERY qualifier in order with the last four weeks of volume
   beside the 12-week average, and deep-dives the top 25 by default.
   Each deep dive also judges the MONTHLY volume trend from the same
   daily bars — **BUILDING** (rose month over month for ≥2 complete
   months: buying pressure accumulating), **STEPPED UP**, or **SPIKE
   ONLY** (flat months, one-week event); the running month is shown but
   never argued from.

2. **Earnings power + new-age industries.** For each qualifier: EBITDA
   ("Operating Profit"; "Financing Profit" for lenders), EBITDA margin,
   PAT and PAT margin over the last four fiscal years from the stored
   P&L archive → verdict RISING / FLAT / FALLING with the numbers shown.
   The conference calls are read by the judge model (`ANALYST_MODEL`,
   default claude-opus-5) for the new-age / entering-new-age question,
   cached per transcript content + model. A BUY on falling earnings is
   downgraded to WATCH, and says so.

3. **Box theory.** Darvas's own definition on DAILY bars over the full
   six months of fetched history: a top is a high that stands unbroken
   for three sessions; then a bottom is a low undercut-free for three
   sessions; together they seal a box. Every stock gets its **own box
   height** measured from its own prices — nothing assumes a fixed
   5/10/15% range — and the report draws the COMPLETE six-month ladder
   of sealed boxes. (Measured on live picks: extending the window to 12
   months left the current box — the buy point and the stop — identical
   in 25 of 25 cases, so six months is the window; three months would
   genuinely distort the edges.)

4. **Accumulation.** A close above the box top on trigger volume = BUY
   (reaching for the higher box). A stock that sealed a higher box after
   an upward break and is holding it = ACCUMULATE. Inside a box with no
   break yet = WATCH, with the exact buy-above price. A close below the
   box bottom = SELL — the red flag; a stock dropping to a lower box is
   sold, never averaged.

5. **Stop losses and the rhythm.** stop = box bottom − 0.3 × box height
   (a 50–55 box stops near 48.5; a 70–85 box near 65.5 — the method's
   worked examples). The rhythm: **run the skill weekly, after Friday's
   close.** Each run re-fetches, re-ranks, re-seals boxes and recomputes
   every held stop from the CURRENT box — the ledger ratchets stops UP
   only, and "decisively" is built in: a higher box exists only after
   three quiet sessions on each edge.

## Run it

```bash
cd IndividualStockAnalysis/India/Skills/DarvasSkill
python3 scripts/analyze.py run                 # fetch fresh + full report
python3 scripts/analyze.py run --top 15        # deep-dive the top 15
python3 scripts/analyze.py run --no-fetch      # reuse the stored fetch
python3 scripts/analyze.py run --quick         # skip the AI call-read
python3 -m pytest scripts/test_skill.py -q     # 43 tests
```

## Backtesting — the same skill, as of a past date

```bash
python3 scripts/backtest.py --start 2025-06-01 --end 2026-03-31 --top 25
```

The runner re-points the unchanged skill at a frozen window: prices and
volumes are fetched for [start, end] only into a SEPARATE archive
(`India/VolumeAndPricingBacktest/<start>_to_<end>/`), week completeness
is judged as of `end` (an unfinished final week is tested pro-rated,
exactly as a live run that day would have), statements are cut at the
as-of fiscal year, the conference-call read is EXCLUDED (the transcript
archive contains calls after the window — excluded beats contaminated),
and the backtest keeps its own report and ledger so the live
`_positions.csv` is never touched. The report opens with a banner
stating every one of these cuts, including the honest caveat that the
as-of fiscal year's annuals would not all have been public on the as-of
date.

## Data and outputs

| Where | What |
|---|---|
| `India/VolumeAndPricing/NiftyTotalMarket/_all_daily_long.csv` | six months of daily OHLCV per symbol, refreshed every run |
| `…/_all_weekly_long.csv` | ISO-week aggregates with traded-day counts and a `complete` flag — the trigger tests the latest week, pro-rating a partial one |
| `…/_fetch_log.csv`, `_fetched_at.txt` | per-symbol fetch status and the run stamp — failures are listed, never hidden |
| `India/Analysis/NiftyTotalMarketAnalysis/DarvasAnalysis/DARVAS_REPORT.md` | the screen: ranked trigger table, per-pick deep dives with text charts, recommendations, the stop ledger, methodology |
| `…/DarvasAnalysis/_positions.csv` | positions carried between runs; stops ratchet up only |

## Pictures

Text-drawn (GitHub strips inline SVG — established empirically in this
repository), so they render everywhere: a COMBINED chart per pick — the
weekly close as a line over the weekly volume as bars on the same week
axis, so a genuine surge shows as the price stepping up exactly where a
volume bar towers — plus a month-wise volume table with the trend
verdict, and the full six-month box ladder with each sealed box's edges
and dates, the stock's own box height, the stop and the buy point.
Every picture carries its exact numbers.

## Honest limitations

- Yahoo Finance is the price/volume source; symbols it does not serve
  appear in `_fetch_log.csv` and are absent from the scan, stated in the
  report header.
- Earnings power is fiscal-year statements — no quarterly TTM view; the
  calls partially cover the gap.
- The new-age read needs the judge model; without it the verdict is
  "not assessed", never guessed.
- Research tooling — not investment advice.
