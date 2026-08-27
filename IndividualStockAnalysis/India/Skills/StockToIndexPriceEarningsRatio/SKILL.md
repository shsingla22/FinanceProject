# StockToIndexPriceEarningsRatio skill

Compares one company against the **Nifty 50 index** on three measures,
one data point per fiscal year, up to the last 15 fiscal years:

1. **Price ratio** — company share price at its fiscal-year end ÷ the
   Nifty 50 close of the same month (shown ×1000 for readability).
2. **PAT ratio** — company Net Profit ÷ the summed Net Profit of the
   Nifty 50 constituents, as % of the index.
3. **Operating-profit ratio** — company Operating Profit (Financing
   Profit for lenders) ÷ the summed Operating Profit of the index, as %.

A **rising** ratio means the company outgrew the index on that measure;
a **falling** ratio means it lagged. Each chart carries a one-line
verdict (GAINED / LAGGED / MOVED WITH the index) plus year-by-year
moves; years either side cannot cover are listed, never guessed.

## Data

- **Company side** (stored, no network): share prices per fiscal year
  from `StockInfo/Nifty500/{SYM}.csv`; Net Profit and Operating Profit
  from `ProfitStatement/NiftyTotalMarket/_all_profit_loss_long.csv`.
- **Index side** (fetched once, saved under `data/`):
  - `nifty50_price_monthly.csv` / `nifty50_price_yearly.csv` — real
    ^NSEI closes (Yahoo Finance), 15 fiscal years of March closes
    (Mar 2012..Mar 2026) plus the monthly series so companies with
    Jun/Dec year-ends divide by the matching month.
  - `nifty50_constituents.csv` — current 50 constituents (screener.in
    mirror; the official NSE archive blocks scripts).
  - `nifty50_earnings_yearly.csv` — per fiscal year, the summed PAT and
    summed Operating Profit of the current constituents aggregated from
    the stored Nifty 500 statements (Mar 2015..Mar 2026). NSE publishes
    no such series, so this is the honest constructible one; it uses
    today's membership, so older years carry a survivorship caveat.

## Usage (from `scripts/`)

```bash
python3 fetch_index_data.py            # refresh the index series
python3 analyze.py report SYM out.md   # one company's report
python3 -m pytest test_skill.py -q     # the skill's test suite
```

Stored outputs for the top-rated companies live under
`Analysis/NiftyTotalMarketAnalysis/StockToIndexRatios/`.

## Known limits

- The stored statements span FY2015..FY2026, so the two earnings charts
  cover ~12 fiscal years even though the price chart covers 15.
- A company whose stored statements are stale (e.g. COLPAL's P&L stops
  at FY2010) gets a price chart plus an explicit "could not cover" list
  instead of guessed earnings ratios.
