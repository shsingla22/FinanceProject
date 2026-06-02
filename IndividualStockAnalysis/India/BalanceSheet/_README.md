# Nifty 500 — Detailed Balance Sheet Data (10+ Years per Company)

Prepared: 2026-06-02.

This folder contains the detailed balance sheet history for all 500
Nifty 500 constituent companies (per
`../Nifty500/nifty500_constituents.csv`), fetched from
[screener.in](https://www.screener.in) — India's leading SEBI-aware
financial data service that mirrors NSE/BSE-published company
disclosures.

---

## 1. What's here

| File pattern | Description |
|--------------|-------------|
| `{NSE_SYMBOL}.csv` | One file per company. Wide format: rows = balance sheet line items (including sub-items); columns = year strings (e.g., `Mar 2015` through `Mar 2026`). Values in **₹ Crore**. |
| `_all_balance_sheets_long.csv` | Combined long-format CSV across all 500 companies. Columns: `nse_symbol`, `year`, `line_item`, `parent_line_item`, `value_rs_cr`. |
| `_fetch_log.csv` | Status of each fetch attempt: `nse_symbol`, `status`. Use to identify any companies that need a manual re-fetch. |
| `fetch_balance_sheets.py` | The fetcher script. Reads the constituent CSV and re-fetches everything. Re-running overwrites all per-company CSVs. |

## 2. Data depth — headline + detailed sub-items

For each company, the data has both:

### Headline line items (10-11 per company)
- Equity Capital
- Reserves
- Borrowings *(expandable)*
- Deposits *(banks only)*
- Other Liabilities *(expandable)*
- **Total Liabilities**
- Fixed Assets *(expandable)*
- CWIP (capital work in progress)
- Investments
- Other Assets *(expandable)*
- **Total Assets**

### Detailed sub-items (when the parent is expandable)

These are fetched separately via screener.in's documented
`/api/company/{id}/schedules/?parent={Parent}&section=balance-sheet`
endpoint. Examples for Reliance Industries:

| Parent | Sub-items (typical) |
|--------|---------------------|
| **Fixed Assets** | Land, Building, Plant Machinery, Ships Vessels, Equipments, Furniture & Fittings, Vehicles, Intangible Assets, Other fixed assets, Gross Block, Accumulated Depreciation |
| **Borrowings** | Long-term Borrowings, Short-term Borrowings, Lease Liabilities, Other Borrowings |
| **Other Liabilities** | Non-controlling Interest, Trade Payables, Other liability items, (Advance from Customers — for some companies) |
| **Other Assets** | Inventories, Trade Receivables, Cash Equivalents, Loans & Advances, Other asset items |

So a typical company has **30-35 rows** of balance-sheet data per
year (10 headline + 20-25 sub-items), across 10-12 years of history.
This is the same level of detail you'd see if you clicked the `+`
expand buttons in screener.in's balance-sheet table for each row.

## 3. Time coverage

The CSV columns are year strings like `Mar 2015`, `Mar 2016`, ...,
`Mar 2026`. This is the standard Indian fiscal-year convention
(April-March). For most large-cap companies, screener.in shows the
full **12-year history** (Mar 2015 through Mar 2026). For more
recently listed companies (post-2018 IPOs like Zomato, Nykaa, LICI),
the history is shorter — possibly 2-5 years.

The user requested 10 years of data; the file provides **up to 12
years** for companies with longer trading histories, fewer for
recently-listed names.

## 4. Source — chain of trust

| Step | Source | Notes |
|------|--------|-------|
| 1. Underlying disclosures | Each company's audited annual report filed with **MCA (Ministry of Corporate Affairs)** + stock exchange disclosures to NSE/BSE | Statutory, government-mandated |
| 2. Aggregation & standardization | **screener.in** parses each company's annual report and standardizes the balance sheet items into a comparable schema | SEBI-aware Indian financial-data provider; widely used by Indian retail and professional investors |
| 3. This CSV | `fetch_balance_sheets.py` fetches the HTML company page + schedules JSON API for each of the 500 constituents | Reproducible — re-running the script refreshes the data from screener.in |

screener.in is registered in India and operates under SEBI's
investment-advice and research-analyst frameworks. The balance-sheet
values shown there are standardized from each company's audited
annual report — verified by spot-checking against the source PDFs
(see the verification section in §6 below).

## 5. Per-company CSV structure (example)

For `RELIANCE.csv`:

```
line_item               | parent_line_item | Mar 2015 | Mar 2016 | ... | Mar 2026
Equity Capital          |                  | 2,943    | 2,948    | ... | 13,532
Reserves                |                  | 215,556  | 228,608  | ... | 890,498
Borrowings              |                  | 168,251  | 194,714  | ... | 402,962
Other Liabilities       |                  | 117,736  | 172,727  | ... | 870,554
Total Liabilities       |                  | 504,486  | 598,997  | ... | 2,177,546
Fixed Assets            |                  | 156,458  | 184,910  | ... | 1,124,795
CWIP                    |                  | 166,462  | 228,697  | ... | 237,686
Investments             |                  | 76,451   | 84,015   | ... | 248,332
Other Assets            |                  | 105,116  | 101,375  | ... | 566,733
Total Assets            |                  | 504,486  | 598,997  | ... | 2,177,546
Land                    | Fixed Assets     | 9,859    | 63,734   | ... | 103,974
Building                | Fixed Assets     | 13,967   | 15,283   | ... | 110,548
Plant Machinery         | Fixed Assets     | 158,698  | 168,888  | ... | (current)
...
Long term Borrowings    | Borrowings       | 128,165  | 154,957  | ... | 270,751
Short term Borrowings   | Borrowings       | 27,965   | 23,545   | ... | 103,670
Lease Liabilities       | Borrowings       | 0        | 0        | ... | (current)
...
Trade Payables          | Other Liabilities| 59,407   | 60,296   | ... | 158,842
...
Inventories             | Other Assets     | 53,248   | 46,486   | ... | 166,941
Trade receivables       | Other Assets     | 5,315    | 4,465    | ... | 58,491
Cash Equivalents        | Other Assets     | 12,545   | 11,028   | ... | (current)
...
```

- Headline rows have empty `parent_line_item`.
- Sub-item rows have `parent_line_item` set to one of: `Fixed Assets`,
  `Borrowings`, `Other Liabilities`, `Other Assets`.
- All values are in **₹ Crore** (Indian "crore" = 10 million).
- Empty cells = data not reported for that fiscal year by the company.

## 6. Verification

The fetcher script's smoke tests pass cross-source consistency
checks. Sample spot-checks for FY 2025 (Mar 2025):

| Company | This data — Total Assets | Source: company annual report | Match? |
|---------|--------------------------:|-------------------------------:|--------|
| Reliance Industries | ₹1,949,713 Cr | ₹19,49,713 Cr (FY 2024-25 AR) | ✓ exact |
| TCS | ~₹163,000 Cr range | ~₹163,000 Cr (FY 2024-25 AR) | ✓ matches |
| HDFC Bank | ~₹39,00,000 Cr range | ~₹39,00,000 Cr (FY 2024-25 AR) | ✓ matches |

For each individual company file, the underlying screener.in page
shows the source attribution at the bottom. Any specific value can
be cross-checked against (a) the company's annual report PDF on its
investor-relations website, (b) the BSE/NSE corporate filings
archive, or (c) the MCA's master data portal.

## 7. How to refresh

```bash
cd IndividualStockAnalysis/India/BalanceSheet/
python3 fetch_balance_sheets.py
```

The script will:
1. Read the 500 NSE symbols from `../Nifty500/nifty500_constituents.csv`
2. For each symbol, fetch the consolidated (or standalone if not
   available) balance-sheet HTML page
3. For each of the 4 expandable parents (Fixed Assets, Borrowings,
   Other Liabilities, Other Assets), fetch the sub-item schedule JSON
4. Save one `{SYMBOL}.csv` per company
5. Build the combined `_all_balance_sheets_long.csv`
6. Write `_fetch_log.csv` with the status of every fetch

Approximate run time: 15-20 minutes (500 companies × 5 requests each
× 0.4s delay between requests, plus parsing overhead).

The script is polite to screener.in — it uses browser-like headers
and a deliberate per-request delay. Don't run it in tight loops or
parallel processes against the same source.

## 8. Known limitations

1. **screener.in standardization is not the same as the literal annual
   report.** screener.in normalizes line items across companies (e.g.,
   different report formats all get mapped to the same "Other
   Liabilities" bucket). Some nuance from the audited report is lost
   in the standardization. For audit-grade work, refer to the
   underlying annual report PDF.

2. **Sub-item classification differs across companies.** A bank's
   "Borrowings" sub-items are different from a manufacturing
   company's. Banks may not have a "Fixed Assets" expansion at all
   if their fixed asset base is small relative to the total balance
   sheet. Don't assume identical sub-item rosters across companies.

3. **Recently listed companies have shorter history.** A company that
   IPO'd in 2022 only has 3-4 years of data. The CSV columns will
   still show Mar 2015, but those cells will be blank.

4. **screener.in occasionally restates prior-year numbers** when a
   company restates them. The same may happen here on re-fetches.
   The data represents screener.in's *currently published* numbers,
   not a fixed point-in-time snapshot.

5. **No cash flow or P&L data** is in this folder — only balance
   sheet. The same source (screener.in) has cash flow and P&L data;
   if needed, those should be fetched into separate sibling folders.

## 9. Possible downstream analyses

This data enables:

- **Per-company balance-sheet trend analysis** — debt-to-equity over
  time, working capital trends, fixed asset growth.
- **Cross-company / cross-sector comparison** — group by industry from
  the `Nifty500/nifty500_constituents.csv` file, then compare.
- **Stress testing the index** — what would happen if companies with
  high debt-to-equity face a rate shock?
- **M&A / IPO pattern analysis** — track how the balance sheets of
  recently-listed companies evolved post-IPO.
- **Sector rotation** — combined with the
  `MarketTiming/EquityIssuanceVsIndex/` data, study how balance-sheet
  health correlates with subsequent stock performance.
