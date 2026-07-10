# Balance Sheets — NIFTY Total Market constituents

**Universe:** the ~750 cos that comprise the NSE NIFTY TOTAL MARKET
index (Nifty 500 ∪ Nifty Microcap 250). The exact constituent list
is in `../../NiftyTotalMarket/niftytotalmarket_constituents.csv`
(742 cos as of the latest scrape).

## Files

- `{NSE_SYMBOL}.csv` — one per company, wide format. Rows are
  balance-sheet line items (headline + sub-component breakdown of
  Fixed Assets / Borrowings / Other Liabilities / Other Assets);
  columns are fiscal year-end strings (e.g. `Mar 2015 … Mar 2026`,
  or `Dec` / `Jun` / `Sep` etc. for non-Mar fiscal-year reporters).
  Same schema as `../Nifty500/{NSE_SYMBOL}.csv`.
- `_all_balance_sheets_long.csv` — consolidated long-format combining
  all companies. Cols: `nse_symbol, year, line_item,
  parent_line_item, value_rs_cr`.
- `_fetch_log.csv` — per-co status (ok / skip:existing / error).

## Data source

screener.in's per-company balance-sheet section + the documented
schedules API for sub-item breakdowns. Same fetcher as Nifty500
(`../fetch_balance_sheets.py`), invoked with
`--universe NiftyTotalMarket`.

## Reproducibility

```
python3 ../fetch_balance_sheets.py --universe NiftyTotalMarket
```

To skip re-fetching cos whose CSV is already present (useful for
incremental updates), add `--skip-existing`. To avoid duplicate
HTTP fetches for the 493 cos that already exist in
`../Nifty500/`, the initial bootstrap of this folder was done by
copying those 493 CSVs first, then HTTP-fetching the remaining
249 (the Microcap 250 segment).
