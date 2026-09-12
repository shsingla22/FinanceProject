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
   fetched for every symbol ON EVERY RUN and aggregated into completed
   Monday–Friday weeks. A stock qualifies when its last completed week
   traded at least **1.5×** its average weekly volume of the prior 12
   completed weeks (minimum 6) **and** the price rose that week — volume
   without price appreciation is distribution, price without volume is
   drift; Darvas required both. Tiers: ≥3× *multifold*, ≥2× *strong*,
   ≥1.5× *elevated*. The report lists the best volume reactions in
   order, with the exact volume numbers.

2. **Earnings power + new-age industries.** For each qualifier: EBITDA
   ("Operating Profit"; "Financing Profit" for lenders), EBITDA margin,
   PAT and PAT margin over the last four fiscal years from the stored
   P&L archive → verdict RISING / FLAT / FALLING with the numbers shown.
   The conference calls are read by the judge model (`ANALYST_MODEL`,
   default claude-opus-5) for the new-age / entering-new-age question,
   cached per transcript content + model. A BUY on falling earnings is
   downgraded to WATCH, and says so.

3. **Box theory.** Darvas's own definition on daily bars: a top is a
   high that stands unbroken for three sessions; then a bottom is a low
   undercut-free for three sessions; together they seal a box. Every
   stock gets its **own box height** measured from its own prices —
   nothing assumes a fixed 5/10/15% range; the report states each
   stock's measured range.

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
python3 -m pytest scripts/test_skill.py -q     # 25 tests
```

## Data and outputs

| Where | What |
|---|---|
| `India/VolumeAndPricing/NiftyTotalMarket/_all_daily_long.csv` | six months of daily OHLCV per symbol, refreshed every run |
| `…/_all_weekly_long.csv` | ISO-week aggregates, with a `complete` flag — the trigger reads completed weeks only |
| `…/_fetch_log.csv`, `_fetched_at.txt` | per-symbol fetch status and the run stamp — failures are listed, never hidden |
| `India/Analysis/NiftyTotalMarketAnalysis/DarvasAnalysis/DARVAS_REPORT.md` | the screen: ranked trigger table, per-pick deep dives with text charts, recommendations, the stop ledger, methodology |
| `…/DarvasAnalysis/_positions.csv` | positions carried between runs; stops ratchet up only |

## Pictures

Text-drawn (GitHub strips inline SVG — established empirically in this
repository), so they render everywhere: a weekly volume-bar chart with
the close and week-on-week move beside every bar and the trigger week
marked, and a box ladder showing each sealed box's edges with dates, the
stock's own box height, the stop and the buy point — every picture
carries its exact numbers.

## Honest limitations

- Yahoo Finance is the price/volume source; symbols it does not serve
  appear in `_fetch_log.csv` and are absent from the scan, stated in the
  report header.
- Earnings power is fiscal-year statements — no quarterly TTM view; the
  calls partially cover the gap.
- The new-age read needs the judge model; without it the verdict is
  "not assessed", never guessed.
- Research tooling — not investment advice.
