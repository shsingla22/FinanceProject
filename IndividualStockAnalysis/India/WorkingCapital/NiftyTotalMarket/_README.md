# Working Capital — NIFTY Total Market constituents

**Universe:** 742 cos comprising the NSE NIFTY TOTAL MARKET index
(Nifty 500 ∪ Nifty Microcap 250). Exact list in
`../../NiftyTotalMarket/niftytotalmarket_constituents.csv`.

## Metrics captured

Pulled from screener.in's `<section id="ratios">` block for each
company. The standard six rows are:

| Metric | Meaning |
|---|---|
| **Debtor Days** | Receivable days = Avg Trade Receivables / Sales × 365 |
| **Inventory Days** | Avg Inventory / Sales × 365 |
| **Days Payable** | Avg Trade Payables / Sales × 365 |
| Cash Conversion Cycle | Debtor + Inventory − Payable (working capital tied up) |
| Working Capital Days | Net working capital cycle |
| ROCE % | Return on Capital Employed (bundled in same section) |

Banks and finance cos show an alternate row set (ROCE %, ROE %)
because they don't have inventory / trade receivables in the
operating sense.

## Files

- `{NSE_SYMBOL}.csv` — wide format, rows = metric, cols = fiscal
  year-end (`Mar 2015 … Mar 2026` or the co's own calendar)
- `_all_working_capital_long.csv` — `nse_symbol, year, metric, value`
  (41,843 rows across all 742 cos)
- `_fetch_log.csv` — per-co status

## Coverage

- 742 / 742 cos fetched on first pass (0 failures)
- Median years per co: **12** (FY15 → FY26)
- 517 cos have ≥ 10 years of working-capital history
- The remaining ~225 are recent IPOs whose screener.in history is
  shorter than 10 years (Debtor/Inventory/Payable Days are computed
  only from listing year onwards)

## Reproducibility

```
python3 ../fetch_working_capital.py                       # default universe = NiftyTotalMarket
python3 ../fetch_working_capital.py --skip-existing       # incremental
python3 ../fetch_working_capital.py --universe Nifty500   # alternate universe
```
