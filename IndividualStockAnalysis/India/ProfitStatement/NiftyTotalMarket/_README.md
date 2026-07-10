# Profit & Loss — NIFTY Total Market constituents

**Universe:** the ~750 cos that comprise the NSE NIFTY TOTAL MARKET
index (Nifty 500 ∪ Nifty Microcap 250). The exact constituent list
is in `../../NiftyTotalMarket/niftytotalmarket_constituents.csv`
(742 cos as of the latest scrape).

## Files

- `{NSE_SYMBOL}.csv` — one per company, wide format. Rows are P&L
  line items (Sales, Expenses, Operating Profit, OPM %, Other Income,
  Interest, Depreciation, Profit before tax, Tax %, Net Profit, EPS,
  Dividend Payout %, plus expandable sub-items for Sales / Expenses /
  Other Income / Net Profit). Columns are fiscal year-end strings
  (`Mar 2015 … Mar 2026`, or `Dec` / `Jun` / `Sep` for non-Mar
  reporters). Same schema as `../Nifty500/{NSE_SYMBOL}.csv`.
- `_all_profit_loss_long.csv` — consolidated long-format combining
  all companies. Cols: `nse_symbol, year, line_item,
  parent_line_item, value`.
- `_fetch_log.csv` — per-co status.

## Data source

screener.in's per-company P&L section + the documented schedules API
for sub-item breakdowns. Same fetcher as Nifty500
(`../fetch_profit_loss.py`), invoked with
`--universe NiftyTotalMarket`.

## Reproducibility

```
python3 ../fetch_profit_loss.py --universe NiftyTotalMarket
```

To skip re-fetching cos whose CSV is already present, add
`--skip-existing`. The initial bootstrap of this folder copied
493 cos from `../Nifty500/` (the overlap) and HTTP-fetched the
remaining 249 (the Microcap 250 segment).
