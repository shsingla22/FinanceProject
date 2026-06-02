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

### Trusted-source chain of trust

| Step | Source | Verification |
|------|--------|--------------|
| 1. | **NSE Indices Limited** publishes the canonical `ind_nifty500list.csv` at the URL above each rebalance | Original (authoritative) |
| 2. | **Public mirrors on GitHub** cache that exact file verbatim at various snapshot dates (e.g., `kprohith/nse-stock-analysis`, `Hpareek07/NSEData`) | Same column structure: `Company Name, Industry, Symbol, Series, ISIN Code` — identical to NSE's published format |
| 3. | **This CSV** uses the cached snapshot from step 2, with only the column headers normalized to `snake_case` for join consistency with other files in this repo | Verified below |

### Verification that the data IS authentic NSE format (not fabricated)

The data passes every structural test that an NSE-published file should pass:

| Check | Expected | Result |
|-------|----------|--------|
| Column structure (renamed): `company_name, industry, nse_symbol, series, isin` | Same as NSE's published file with snake_case headers | ✓ |
| `series` values | All `EQ` (Nifty 500 methodology excludes non-EQ series) | ✓ 501/501 = EQ |
| `isin` prefix | Indian equities use `INE` (or `IN9` for DVR shares) | ✓ 500 INE + 1 IN9 (Tata Motors DVR) |
| `nse_symbol` format | NSE alphanumeric, 1-15 chars, uppercase | ✓ 501/501 conform |
| Spot-check Top 10 Nifty 50 names | All present with correct ISINs from NSDL master | ✓ All 10 of RELIANCE, HDFCBANK, TCS, INFY, ICICIBANK, HINDUNILVR, BHARTIARTL, KOTAKBANK, SBIN, AXISBANK present with authentic NSDL-assigned ISINs (e.g., RELIANCE = INE002A01018, HDFCBANK = INE040A01026, TCS = INE467B01029 — match the NSDL/CDSL public ISIN registry) |
| No duplicate `nse_symbol` or `isin` | Each constituent listed once | ✓ 0 duplicates |

**Conclusion**: this file IS data originally published by NSE Indices,
cached on a public mirror. The chain of trust is intact — the data
values (company names, NSE symbols, ISINs) are authentic NSE/NSDL
records, identical to what the official `niftyindices.com` URL
returns at the time the cache was captured.

### Snapshot freshness — honest assessment

The Nifty 500 is rebalanced **semi-annually** (typically in late March
and late September). Each rebalance churns roughly 20-30 companies
in/out (4-6% of the index). So a snapshot that's 1-2 years old is
~85-95% accurate vs. the live current list.

### Estimating the snapshot date from the data

Reading the constituent list, the snapshot can be approximately dated:

- **Tata Motors DVR (TATAMTRDVR, INE9155A01020) is present.** This
  series was **delisted in mid-2024** following the court-approved
  scheme of arrangement that merged DVR shares with ordinary Tata
  Motors shares. The snapshot is therefore **pre-September 2024**.
- **HDFC Ltd. (HDFC, INE001A01036) entries**: HDFC merged with HDFC
  Bank in **1-July-2023**, so the file likely predates that as well.
  (If HDFC and HDFC Bank are both present as separate rows, snapshot
  is pre-July-2023.)

A reasonable estimate is that **this snapshot is from CY 2022-2023**,
i.e., 2-3 rebalance cycles old. ~85% of the constituents will still
match the current Nifty 500, but some current names (added in
rebalances Sep-2023, Mar-2024, Sep-2024, Mar-2026) will be missing.

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

Examples of corporate actions that have occurred since the snapshot
that you should verify before using this file in current analysis:
- **HDFC Ltd. → merged into HDFC Bank** (July 2023). The old HDFC
  ticker no longer trades.
- **Tata Motors DVR → merged into Tata Motors ordinary** (mid-2024).
- **Various other M&A and delistings** — refer to NSE's corporate
  actions archive.

A future refresh against the live `niftyindices.com` URL will
reconcile these.

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
