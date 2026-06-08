# Cash Flow — NIFTY Total Market constituents

**Universe:** the ~750 cos that comprise the NSE NIFTY TOTAL MARKET
index (Nifty 500 ∪ Nifty Microcap 250). The exact constituent list
is in `../../NiftyTotalMarket/niftytotalmarket_constituents.csv`
(742 cos as of the latest scrape).

## Files

- `{NSE_SYMBOL}.csv` — one per company, wide format. Rows are
  cash-flow line items, columns are fiscal year-end strings
  (`Mar 2015 … Mar 2026`, or `Dec` / `Jun` / `Sep` / `Nov` for
  non-Mar reporters). Headline rows have `parent_line_item = ""`;
  expanded sub-items have `parent_line_item` set to one of the
  three top-level CF buckets.
- `_all_cash_flow_long.csv` — consolidated long-format combining
  all 742 companies. Cols: `nse_symbol, year, line_item,
  parent_line_item, value_rs_cr`.
- `_fetch_log.csv` — per-co fetch status.

## Schema (per-company CSV)

Each per-co CSV contains the 6 headline rows
  - **Cash from Operating Activity** (expandable)
  - **Cash from Investing Activity** (expandable)
  - **Cash from Financing Activity** (expandable)
  - Net Cash Flow
  - Free Cash Flow
  - CFO/OP

PLUS the expanded sub-items for the three expandable parents,
fetched via screener.in's documented schedules API:

  ``/api/company/{companyId}/schedules/?parent={Parent}&section=cash-flow&consolidated=``

Typical Operating-Activity expansion:
  Profit from operations, Receivables, Inventory, Payables,
  Working capital changes, Direct taxes.

Typical Investing-Activity expansion:
  Fixed assets purchased, Fixed assets sold, Investments
  purchased, Investments sold, Interest received, Dividends
  received, Other investing items.

Typical Financing-Activity expansion:
  Proceeds from shares, Proceeds from borrowings, Repayment of
  borrowings, Interest paid fin, Dividends paid, Financial
  liabilities, Share application money, Other financing items.

Across the 742 cos the union of cash-flow line items is **54
distinct rows** (varies by industry — banks have different
sub-items than industrial companies).

## Coverage

- 742 / 742 cos fetched (all `ok` after retry pass)
- Median years per co: **12** (FY15 → FY26)
- 519 cos have ≥ 10 years of cash-flow history
- ~220 cos with < 10 yrs are recent IPOs — screener.in only
  publishes data from the year of listing

## Reproducibility

```
python3 ../fetch_cash_flow.py                       # default universe = NiftyTotalMarket
python3 ../fetch_cash_flow.py --skip-existing       # incremental (skip already-fetched cos)
python3 ../fetch_cash_flow.py --universe Nifty500   # alternate universe
```

The script is polite: 0.4s between requests, browser-like headers,
no concurrency. The original fetch run had 71 transient
`no_data_on_either_url` failures (all big-name cos with valid CF
pages — likely intermittent HTTP issues). A second pass with
`--skip-existing` recovered all 71.
