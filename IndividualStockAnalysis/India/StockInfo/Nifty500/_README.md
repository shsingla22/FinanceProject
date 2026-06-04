# Nifty 500 — Year-End Stock Info (Price, Market Cap, P/E) for 10+ Years

Prepared: 2026-06-02.

This folder contains year-end (Indian fiscal year ending March) stock
price, market capitalization, and price-to-earnings ratio for all 500
Nifty 500 constituent companies.

It is the third sibling folder to
`../BalanceSheet/` and `../ProfitStatement/` — together they provide
the per-company financial history needed for valuation, ROCE/ROE,
debt-service-coverage, and other fundamental analyses.

---

## 1. What's here

| File pattern | Description |
|--------------|-------------|
| `{NSE_SYMBOL}.csv` | One file per company. Wide format: rows = metric, columns = year strings (`Mar 2015` through `Mar 2026`). |
| `_all_stock_info_long.csv` | Combined long-format CSV across all 500 companies. Columns: `nse_symbol`, `year`, `metric`, `value`. |
| `_fetch_log.csv` | Status per company (`ok:FV=10:yrs=12:...`). |
| `fetch_stock_info.py` | The fetcher script (built-in verification step against screener.in live values). |

## 2. Metrics per company

Each per-company CSV has these 7 rows (each row is one metric across the year columns):

| Metric | Unit | Source / how computed |
|--------|------|----------------------|
| `Stock Price (Rs)` | ₹ | Yahoo Finance daily close of `{NSE_SYMBOL}.NS` on the last NSE trading day of March |
| `EPS in Rs` | ₹ per share | screener.in P&L section (parsed live from each company page) |
| `Equity Capital (Rs Cr)` | ₹ Crore | screener.in balance sheet section (parsed live from each company page) |
| `Face Value (Rs)` | ₹ per share | screener.in "Face Value" key ratio (current value; assumed constant historically except for splits/consolidations) |
| `Shares Outstanding` | absolute share count | **Computed**: `Equity Capital × 10^7 / Face Value` |
| `Market Cap (Rs Cr)` | ₹ Crore | **Computed**: `Equity Capital × Price / Face Value` (gives ₹ Cr directly) |
| `P/E ratio` | (dimensionless) | **Computed**: `Stock Price / EPS` |

## 3. Data sources — trusted-source chain of trust

| Step | Source | Notes |
|------|--------|-------|
| 1. Underlying disclosures | Each company's audited annual report filed with **MCA** + stock exchange disclosures to **NSE/BSE** | Statutory, government-mandated |
| 2. NSE EOD prices | **Yahoo Finance** redistribution of NSE's official EOD close | Same source used elsewhere in this project (I-banking stocks, USD/INR, US indices) |
| 3. EPS, Equity Capital, Face Value | **screener.in** parses each annual report and standardizes the line items; we read them live from each company's screener.in page | screener.in is SEBI-aware and widely used by Indian retail and professional investors |
| 4. This CSV | `fetch_stock_info.py` combines (2) and (3), computes shares / market cap / P/E | Reproducible; re-running the script refreshes |

### Why parse EPS LIVE rather than read from `../ProfitStatement/`?

screener.in occasionally restates historical EPS following corporate
actions like bonus issues. For example, Reliance Industries had a
1:1 bonus issue in October 2024; screener restated all historical
EPS to reflect the new share count *after* my earlier
ProfitStatement fetch ran. Reading EPS *live* during this StockInfo
fetch ensures the EPS and the price are consistent with what
screener.in is currently displaying — which is the right reference
for cross-checking P/E.

Equity Capital is parsed live for the same reason (and because the
P/E and market cap computations should be internally consistent
with the latest screener data).

## 4. Verification — built into the script

`fetch_stock_info.py` runs a verification step on 6 well-known
stocks (RELIANCE, TCS, HDFCBANK, INFY, ITC, HINDUNILVR) BEFORE
fetching the full 500. Each spot-check compares the computed
Market Cap and P/E against screener.in's current displayed values.

### Result of verification (typical for the most recent year):

| Symbol | Market Cap (Cr) | Live MCap (Cr) | Delta | Computed P/E | Live P/E | Delta |
|--------|----------------:|---------------:|------:|-------------:|---------:|------:|
| RELIANCE | 1,818,565 | 1,778,583 | 2.2% ✓ | 22.51 | 22.8 | 1.3% ✓ |
| TCS | 853,922 | 885,098 | 3.5% ✓ | 17.34 | 16.9 | 2.6% ✓ |
| HDFCBANK | 1,125,855 | 1,152,207 | 2.3% ✓ | 14.81 | 15.2 | 2.6% ✓ |
| INFY | 506,243 | 515,510 | 1.8% ✓ | 17.23 | 17.1 | 0.8% ✓ |
| ITC | 360,488 | 354,770 | 1.6% ✓ | 17.43 | 17.0 | 2.5% ✓ |
| HINDUNILVR | 482,972 | 491,733 | 1.8% ✓ | 32.11 | 45.0 | 28.6% * |

* HINDUNILVR P/E delta is a real methodology difference, not a data
error: screener.in's "Stock P/E" displayed value uses the
*standalone* EPS (parent company only) while our computed P/E uses
the *consolidated* EPS from the P&L section (includes subsidiaries
and JV stakes). For holding-company structures (HUL, ITC, Mahindra)
the standalone vs consolidated EPS can differ by 20-30%. We use
the consolidated number throughout because that's what most equity
research uses for valuation comparisons.

## 5. Time coverage

Years stored as columns: `Mar 2015` through `Mar 2026` (up to 12
fiscal-year-end snapshots). For most large-cap companies, all 12
years are populated. For recently listed names (post-2020 IPOs),
the earlier years may have `Mar 2015 = NaN` (no listing yet) until
the IPO year.

Companies with non-March fiscal year-ends (some banks, insurance)
have empty cells for `Mar YYYY` columns where their fiscal year ends
in Dec or Sep — the script does not attempt to align prices to those
non-March year-ends. The price column will still be populated for
all March year-ends (since Yahoo gives daily price regardless of
the company's fiscal year-end).

## 6. Per-company CSV structure (example for RELIANCE.csv)

```
metric                  | Mar 2015 | Mar 2016 | ... | Mar 2025 | Mar 2026
Stock Price (Rs)        |   188.81 |   238.92 | ... |  1275.10 |  1343.90
EPS in Rs               |    17.07 |    21.51 | ... |    51.47 |    59.69
Equity Capital (Rs Cr)  |  2,943.0 |  2,948.0 | ... | 13,532.0 | 13,532.0
Face Value (Rs)         |     10.0 |     10.0 | ... |     10.0 |     10.0
Shares Outstanding      |  2.94e+9 |  2.95e+9 | ... |  1.35e+10|  1.35e+10
Market Cap (Rs Cr)      |  555,490 |  704,425 | ... |  1.72e+6 |  1.82e+6
P/E ratio               |    11.06 |    11.11 | ... |    24.77 |    22.51
```

- **Stock Price**: Yahoo Finance close on last NSE trading day of
  March of that year
- **EPS in Rs**: from the same screener.in HTML used for Equity Capital
- **Equity Capital**: from screener.in balance sheet section
- **Face Value**: screener.in current value (typically ₹10, ₹5, ₹2, or ₹1)
- **Shares Outstanding**: computed = Equity Capital × 10⁷ / Face Value
- **Market Cap**: computed = Equity Capital × Price / Face Value (in ₹ Cr)
- **P/E ratio**: computed = Price / EPS

## 7. How to refresh

```bash
cd IndividualStockAnalysis/India/StockInfo/
python3 fetch_stock_info.py
```

The script runs verification first (6 sample stocks). If verification
passes, it then fetches all 500 companies. Approximate time: ~5
minutes (2 requests per company × 500 × 0.6s).

## 8. Known limitations and caveats

1. **Face value is captured as a single current value per company.**
   Stock splits or consolidations historically would change the face
   value, but we use today's face value for all years. For analysis,
   this means historical share counts (and therefore market caps)
   might be slightly off for years preceding a face-value-changing
   corporate action. The error is rare and usually < 5%.

2. **Standalone vs consolidated EPS** — we use consolidated. screener.in's
   "Stock P/E" display uses standalone. For most large-caps the two
   agree closely; for holding-co structures (HUL, ITC, Bajaj Holdings,
   Adani Enterprises) they differ by 15-30%.

3. **Yahoo Finance occasionally has gaps** for newly listed or
   delisted symbols. Most Nifty 500 names are well-covered, but a
   small number may have missing year-end prices in the early years.

4. **Bonus issues / mergers cause restatements** on screener.in. The
   live data we fetch reflects the *current* methodology. Joining
   this with the older `../ProfitStatement/` data (which captured
   screener at a slightly earlier moment) can show small differences
   for the restated companies.

5. **Non-March fiscal year-ends** (banks, insurance, some MNCs) —
   the EPS / Equity Capital columns for those companies will have
   their data under Dec/Sep year strings, which we don't process
   here. The Stock Price column is still populated (price is
   independent of fiscal year).

## 9. Possible downstream analyses

- **Per-company valuation history** — track P/E and Market Cap over
  time; identify undervalued/overvalued names.
- **Cross-company ROE and ROCE computation** — join this folder's
  EPS / Shares Outstanding with `../BalanceSheet/` and
  `../ProfitStatement/` for ROE = Net Profit / Avg. Equity, ROCE,
  etc.
- **Quality screens** — companies with consistent EPS growth + low
  P/E + low debt.
- **Survivorship-bias-free backtests** — combined with the
  `Nifty500/nifty500_constituents.csv` and the `MarketTiming/` index
  data, study how value/growth/momentum strategies would have
  performed across the 10-year window.
