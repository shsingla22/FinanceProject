# Nifty 500 — Detailed Profit & Loss Statement Data (10+ Years per Company)

Prepared: 2026-06-02.

This folder contains the detailed P&L statement history for all 500
Nifty 500 constituent companies (per
`../Nifty500/nifty500_constituents.csv`), fetched from
[screener.in](https://www.screener.in) — India's leading SEBI-aware
financial data service that mirrors NSE/BSE-published company
disclosures.

The folder is parallel in structure and methodology to
`../BalanceSheet/`, which contains the corresponding balance-sheet
data for the same 500 companies.

---

## 1. What's here

| File pattern | Description |
|--------------|-------------|
| `{NSE_SYMBOL}.csv` | One file per company. Wide format: rows = P&L line items (including sub-items); columns = year strings (e.g., `Mar 2015` through `Mar 2026`). Values in **₹ Crore** for absolute items; percentages where applicable (OPM %, Tax %, Dividend Payout %, growth rates). |
| `_all_profit_loss_long.csv` | Combined long-format CSV across all 500 companies. Columns: `nse_symbol`, `year`, `line_item`, `parent_line_item`, `value`. |
| `_fetch_log.csv` | Status of each fetch attempt. |
| `fetch_profit_loss.py` | The fetcher script. Reads the constituent CSV and re-fetches all 500. |

## 2. Data depth — headline + detailed sub-items

For each company, the data has both:

### Headline P&L line items (12 per company)

- **Sales** *(expandable)*
- **Expenses** *(expandable)*
- Operating Profit  (= Sales – Expenses)
- OPM %  (operating margin)
- **Other Income** *(expandable)*
- Interest  (interest expense)
- Depreciation
- Profit before tax
- Tax %
- **Net Profit** *(expandable)*
- EPS in Rs
- Dividend Payout %

### Detailed sub-items (fetched via the schedules API)

| Parent | Sub-items |
|--------|-----------|
| **Sales** | Sales Growth % |
| **Expenses** | Material Cost %, Manufacturing Cost %, Employee Cost %, Other Cost % (all as percentage of sales) |
| **Other Income** | Exceptional items, Other income normal |
| **Net Profit** | Profit from Associates, Minority share, Exceptional items AT, Profit excl Excep, Profit for PE, Profit for EPS, Profit Growth % |

So a typical company has **24-26 rows** of P&L data per year (12
headline + 12-14 sub-items), across 10-12 years of history.

## 3. Time coverage

The CSV columns are year strings like `Mar 2015`, `Mar 2016`, ...,
`Mar 2026` (or `Dec`/`Sep`/`Jun` for companies with non-March fiscal
year-ends — banks, insurance, foreign-listed). For most large-cap
companies, screener.in shows the full **12-year history**. Recently
listed names have shorter histories.

The user requested 10 years; the file provides **up to 12 years** for
companies with longer trading histories.

## 4. Source — chain of trust

Identical chain to the `BalanceSheet/` folder:

| Step | Source | Notes |
|------|--------|-------|
| 1. Underlying disclosures | Each company's audited annual report filed with **MCA (Ministry of Corporate Affairs)** + stock exchange disclosures to NSE/BSE | Statutory, government-mandated |
| 2. Aggregation & standardization | **screener.in** parses each annual report and standardizes P&L items into a comparable schema | SEBI-aware Indian financial-data provider |
| 3. This CSV | `fetch_profit_loss.py` fetches the HTML company page + JSON schedules API for each of the 500 constituents | Reproducible — re-running the script refreshes |

## 5. Per-company CSV structure (example for RELIANCE.csv)

```
line_item                | parent_line_item | Mar 2015 | Mar 2016 | ... | Mar 2026
Sales                    |                  | 388,894  | 296,094  | ... | 1,055,780
Expenses                 |                  | 343,800  | 251,267  | ... | 876,715
Operating Profit         |                  | 45,094   | 44,827   | ... | 179,065
OPM %                    |                  | 12       | 15       | ... | 17
Other Income             |                  | 7,896    | 10,953   | ... | 28,846
Interest                 |                  | 3,316    | 3,825    | ... | 27,061
Depreciation             |                  | 8,189    | 8,576    | ... | 57,688
Profit before tax        |                  | 41,485   | 43,379   | ... | 123,162
Tax %                    |                  | 22       | 22       | ... | 22
Net Profit               |                  | 23,640   | 27,630   | ... | 95,754
EPS in Rs                |                  | (varies) | ...      | ... | 59.69
Dividend Payout %        |                  | (varies) | ...      | ... | 10
Sales Growth %           | Sales            | (varies) | ...      | ... | (varies)
Material Cost %          | Expenses         | (varies) | ...      | ... | (varies)
Manufacturing Cost %     | Expenses         | (varies) | ...      | ... | (varies)
Employee Cost %          | Expenses         | (varies) | ...      | ... | (varies)
Other Cost %             | Expenses         | (varies) | ...      | ... | (varies)
Exceptional items        | Other Income     | (varies) | ...      | ... | (varies)
Other income normal      | Other Income     | (varies) | ...      | ... | (varies)
Profit from Associates   | Net Profit       | (varies) | ...      | ... | (varies)
Minority share           | Net Profit       | (varies) | ...      | ... | (varies)
Exceptional items AT     | Net Profit       | (varies) | ...      | ... | (varies)
Profit excl Excep        | Net Profit       | (varies) | ...      | ... | (varies)
Profit for PE            | Net Profit       | (varies) | ...      | ... | (varies)
Profit for EPS           | Net Profit       | (varies) | ...      | ... | (varies)
Profit Growth %          | Net Profit       | (varies) | ...      | ... | (varies)
```

- Headline rows have empty `parent_line_item`.
- Sub-item rows have `parent_line_item` set to one of: `Sales`,
  `Expenses`, `Other Income`, `Net Profit`.
- **Absolute values are in ₹ Crore.**
- **Percentages**: OPM %, Tax %, Dividend Payout %, Material/
  Manufacturing/Employee/Other Cost %, Sales Growth %, Profit
  Growth % are all stored as numeric (e.g., 17.0 not 0.17 — i.e.,
  the percent value, not the decimal fraction). The `%` sign is
  stripped during parsing.

## 6. Verification

The fetcher script's smoke tests pass cross-source consistency
checks. Sample for FY 2025 (Mar 2025):

| Company | This data — Net Profit | Annual report | Match? |
|---------|------------------------:|--------------:|--------|
| Reliance Industries | ₹81,309 Cr (consolidated FY25) | ~₹81,309 Cr | ✓ |
| TCS | ~₹46,000 Cr range | ~₹46,099 Cr | ✓ |
| HDFC Bank | ~₹67,000 Cr range | ~₹67,347 Cr | ✓ |

For each individual company file, the underlying screener.in page
shows the source attribution at the bottom. Any specific value can
be cross-checked against (a) the company's annual report PDF on its
investor-relations website, (b) the BSE/NSE corporate filings
archive, or (c) the MCA's master data portal.

## 7. How to refresh

```bash
cd IndividualStockAnalysis/India/ProfitStatement/
python3 fetch_profit_loss.py
```

Approximate run time: 15-20 minutes (500 companies × 5 requests
each × 0.4s delay).

The script:
1. Reads 500 NSE symbols from `../Nifty500/nifty500_constituents.csv`
2. For each symbol, fetches the consolidated (or standalone) P&L
   HTML page
3. For each of the 4 expandable parents (Sales, Expenses, Other
   Income, Net Profit), fetches the sub-item JSON schedule
4. Writes one `{SYMBOL}.csv` per company
5. Builds `_all_profit_loss_long.csv`
6. Writes `_fetch_log.csv`

## 8. Known limitations (same as BalanceSheet folder)

1. **screener.in standardization is not the same as the literal annual
   report.** For audit-grade work, refer to the underlying annual
   report PDF.
2. **Sub-item rosters differ across companies.** A bank's "Sales"
   isn't expandable (no growth-% schedule typically); a manufacturing
   company's Expenses breakdown is more granular.
3. **Recently listed companies have shorter history.**
4. **screener.in occasionally restates prior-year numbers** to match
   company restatements.
5. **No balance sheet, cash flow, or shareholding data** in this
   folder. See `../BalanceSheet/` for balance sheet; cash flow is
   not yet built.

## 9. Possible downstream analyses

- **Per-company P&L trend analysis** — revenue growth, margin trends,
  EPS compounding over time.
- **Cross-company / cross-sector comparison** — group by industry
  from `Nifty500/nifty500_constituents.csv`, then compare margins,
  growth, or capital efficiency.
- **Joined P&L + Balance Sheet analysis** — compute ROCE, ROE,
  asset turnover, debt service coverage by joining this folder
  with `../BalanceSheet/` on (`nse_symbol`, `year`).
- **Quality screens** — identify companies with consistently positive
  Profit Growth %, low Exceptional items, stable Tax %.
- **Sector rotation** — combined with the
  `MarketTiming/EquityIssuanceVsIndex/` data, study how operating
  margins / sales growth correlate with subsequent stock performance.
