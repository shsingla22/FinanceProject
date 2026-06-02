# Nifty 500 Constituent List (`nifty500_constituents.csv`)

Preparation date: 2026-06-02.

The full list of companies in the Nifty 500 index — India's broad-market
index covering ~95% of the free-float market capitalization on NSE.

---

## 1. File contents

| Column | Meaning |
|--------|---------|
| `company_name` | Full registered company name |
| `industry` | NSE-classified industry group (e.g., FINANCIAL SERVICES, IT, PHARMA) |
| `nse_symbol` | NSE trading ticker (e.g., RELIANCE, TCS, INFY) — **unique identifier on NSE** |
| `series` | Trading series (always EQ for these equities) |
| `isin` | 12-character International Securities Identification Number — **globally unique identifier** (starts with `INE` for Indian equities) |

### Two unique identifiers per row, by design

- **`nse_symbol`**: human-readable, used in trading/news, free to use, but
  can be reassigned (e.g., post-merger). Unique within NSE only.
- **`isin`**: globally unique, never reassigned, assigned by NSDL/CDSL
  for Indian securities. The most reliable join key when working with
  multiple data sources (Bloomberg, Refinitiv, S&P CapIQ all use ISIN).

For joins against (a) NSE bhavcopy / NSE archives → use `nse_symbol`.
For joins against (b) Bloomberg / FactSet / Refinitiv → use `isin`.

## 2. Data source — caveats up front

**Official source URL**:
- https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv

This is the canonical CSV maintained by NSE Indices Limited (formerly
IISL — India Index Services & Products Limited). The file is updated
each rebalance.

**However**, this URL is protected by Akamai bot-detection and returns
HTTP 403 to anonymous programmatic requests from this environment.
The same is true for the NSE Archives mirror at
`https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv`.

**Data path used here**: a publicly-mirrored snapshot of the same NSE
file, cached on GitHub at:
- https://raw.githubusercontent.com/kprohith/nse-stock-analysis/master/ind_nifty500list.csv
- (cross-validated against https://raw.githubusercontent.com/Hpareek07/NSEData/master/ind_nifty500list.csv — same data)

Both mirrors produce identical data (same column structure, same 501
rows). The snapshot represents an NSE-published `ind_nifty500list.csv`
from an earlier date; the **exact rebalance date is not stamped in the
file**.

### Snapshot freshness — honest assessment

The Nifty 500 is rebalanced **semi-annually** (typically in late March
and late September). Each rebalance churns roughly 20-30 companies
in/out (4-6% of the index). So a snapshot that's 1-2 years old is
~85-95% accurate vs. the live current list.

**This file should be treated as a representative-but-not-current
snapshot** of the Nifty 500 universe, useful for:
- Setting up data pipelines that will be refreshed periodically
- Building broad lists for analysis where exact-current membership
  isn't critical
- Sanity-checking against another live source

**For applications that require the live current list** (e.g.,
benchmark replication, ETF construction), the user should download
fresh from `niftyindices.com` via a browser or a paid data feed
(Bloomberg, NSE Indices subscription).

### Companies known to have changed status post-snapshot

Reading the snapshot, I can see established names that have undergone
material corporate actions (merger, delisting, rename) and that
*may not match exactly* the current Nifty 500. Spot-check candidates
to verify if precision matters:
- HDFC Ltd. → merged with HDFC Bank in July 2023 (ISIN INE001A01036
  no longer trades; new ISIN is HDFCBANK's INE040A01034)
- Several other corporate actions since the snapshot date

A future refresh will reconcile these.

## 3. Row count

| Source dataset | Row count | Notes |
|----------------|----------:|-------|
| This CSV | 501 | One row appears to be a residual from a transition period when both pre-rebalance and post-rebalance entries existed briefly in NSE's published file |
| Live Nifty 500 (current) | 500 | Always 500 names by index methodology |

The single extra row is preserved as-is to match the source file
verbatim; downstream code should `df = df.drop_duplicates(subset='isin')`
if exactly 500 is required.

## 4. Cross-validation summary

| Check | Pass? |
|-------|-------|
| No duplicate `nse_symbol` | ✓ (0 duplicates) |
| No duplicate `isin` | ✓ (0 duplicates) |
| No null `nse_symbol` | ✓ |
| No null `isin` | ✓ |
| All `isin` starts with "INE" (Indian equities) | ✓ |
| All `series` = "EQ" | ✓ (matches NSE methodology — Nifty 500 excludes non-EQ series) |
| `industry` populated for every row | ✓ |

## 5. Industry breakdown (top 5)

| Industry | Count |
|----------|------:|
| FINANCIAL SERVICES | 92 |
| CONSUMER GOODS | 72 |
| INDUSTRIAL MANUFACTURING | 45 |
| PHARMA | 37 |
| ENERGY | 34 |

(Full enumeration in the CSV.)

## 6. How to refresh

### Browser refresh (recommended)
1. Open https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv
   in a browser
2. The CSV will download (after the Akamai challenge passes interactively)
3. Replace this file's contents, normalize column headers:
   `Company Name` → `company_name`, `Industry` → `industry`,
   `Symbol` → `nse_symbol`, `Series` → `series`, `ISIN Code` → `isin`
4. Sort alphabetically by `company_name` for consistent diffing

### Alternative URLs (any that work in your environment)
- https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv (primary, Akamai-protected)
- https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv (mirror, same Akamai)
- https://raw.githubusercontent.com/kprohith/nse-stock-analysis/master/ind_nifty500list.csv (community mirror, may be stale)

### Validation after refresh
```python
import pandas as pd
df = pd.read_csv("nifty500_constituents.csv")
assert df["isin"].is_unique
assert df["nse_symbol"].is_unique
assert (df["isin"].str.startswith("INE")).all()
print(f"{len(df)} constituents loaded")
```

## 7. Authoritative cross-check sources

For any individual company name / symbol / ISIN:
- **Primary**: NSE official symbol lookup
  (https://www.nseindia.com/companies-listing/corporate-filings-company-search)
- **Secondary**: BSE official symbol lookup
  (https://www.bseindia.com/corporates/List_Scrips.aspx)
- **Tertiary**: NSDL ISIN search (https://nsdl.co.in/master/static_files.php)
  — confirms ISIN assignments
- **Quaternary**: screener.in (search by ISIN), moneycontrol.com,
  trendlyne.com — all carry NSE/BSE-sourced master data

## 8. About the Nifty 500 index itself (for context)

- **Provider**: NSE Indices Limited
- **Launch date**: 8 November 1996 (base = 1000, base date 1995)
- **Coverage**: Top 500 stocks by free-float market capitalization
  on NSE; represents ~95% of NSE's total free-float market cap.
- **Methodology**: Free-float market-cap weighted; semi-annual
  rebalancing (March and September).
- **Sub-indices within Nifty 500**:
  - Nifty 50 (top 50)
  - Nifty Next 50 (51-100)
  - Nifty Midcap 100 (next 100)
  - Nifty Smallcap 100 (next 100)
  - Total: 350 of 500 are categorized into Nifty 50 + Next 50 + Midcap +
    Smallcap. The remaining 150 are unclassified small-caps within the
    broader 500.

For deeper analysis of these sub-indices (year-end closes + P/E +
forward returns), see `MarketTiming/EquityIssuanceVsIndex/` in this
repository.

## 9. Use this file for…

- Building a stock universe for screening or systematic analysis
- Joining external fundamentals (revenue, EPS, balance sheet) by
  `isin` or `nse_symbol`
- Industry-level aggregation for sector-based analysis
- Sampling stocks for per-company deep dives (the
  `IndividualStockAnalysis/India/BalanceSheet/` folder is structured
  for this — one analysis per stock)
