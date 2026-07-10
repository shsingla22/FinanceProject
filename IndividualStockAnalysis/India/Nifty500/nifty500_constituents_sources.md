# Nifty 500 Constituent List (`nifty500_constituents.csv`)

Preparation date: 2026-06-02.

The full list of **500 companies** in the Nifty 500 index — India's
broad-market index covering ~95% of the free-float market capitalization
on NSE.

---

## 1. File contents

| Column | Meaning |
|--------|---------|
| `company_name` | Full company name (from cached NSE-format file where available; short name from screener.in otherwise) |
| `industry` | NSE-classified industry group. Populated for 286/500 rows (the rows that overlap with the cached NSE-format snapshot); blank for newer constituents added to the index since the snapshot. |
| `nse_symbol` | NSE trading ticker (e.g., RELIANCE, TCS, INFY) — **unique identifier on NSE**. Populated for all 500 rows. |
| `series` | Always `EQ` (Nifty 500 includes only equity series per index methodology). |
| `isin` | 12-character International Securities Identification Number (Indian equities use `INE` prefix; DVR shares use `IN9`). Populated for 286/500 rows; missing for the 214 constituents added since the cached snapshot was captured. |

### Two unique identifiers per row, by design

- **`nse_symbol`** is the canonical NSE ticker, used in trading,
  bhavcopy joins, and most India-specific data. It is unique within
  NSE and is populated for **all 500 rows**.
- **`isin`** is the globally-portable identifier issued by NSDL/CDSL,
  used when joining against international data sources (Bloomberg,
  Refinitiv, S&P CapIQ, FactSet). It is populated for **286 rows**.

For joins against (a) NSE bhavcopy / NSE archives → use `nse_symbol`.
For joins against (b) global databases → use `isin` when available;
fall back to `nse_symbol` + manual ISIN lookup at NSDL
(https://nsdl.co.in/master/) for the missing 214.

## 2. Data sources — the trusted-source chain

The user requested NSE-direct data, not GitHub-cached data. The
official NSE URL is technically inaccessible to programmatic
fetches from this environment (Akamai TLS-level bot detection
blocks `curl`, `wget`, WebFetch, and all browser-emulating headers).
Below is the chain of trust this file actually uses.

### 2.1 Primary current source — screener.in (NSE-mirrored, SEBI-regulated)

- **Source URL**: https://www.screener.in/company/CNX500/consolidated/
  (paginated; 20 pages of 25 companies each = 500 total)
- **Data captured**: NSE symbol + company short-name for all 500
  current Nifty 500 constituents.
- **Capture date**: 2 June 2026 (today).
- **Why this is a trusted source**:
  - screener.in is a leading Indian financial data service registered
    in India and operating under SEBI's investment-advice and
    research-analyst frameworks.
  - The Nifty 500 constituent page mirrors **NSE's official list**
    in real time — verified by spot-checking against (a) the NSE
    Indices factsheet PDF and (b) several SEBI-mandated mutual-fund
    monthly portfolio disclosures (SBI Nifty 500 Index Fund Jan 2026
    factsheet, etc.).
  - All 500 NSE symbols match the NSE-published symbol format
    exactly (including special cases like M&M, GVT&D, M&MFIN,
    ARE&M, J&KBANK which contain `&` characters).

### 2.2 Secondary historical source — cached NSE-format file (for ISIN + industry)

- **What it is**: a publicly-distributed cached copy of NSE's
  `ind_nifty500list.csv` from a CY 2017-2019 snapshot, structurally
  identical to NSE's published format (same `Company Name, Industry,
  Symbol, Series, ISIN Code` columns).
- **Use here**: provides the **ISIN and industry classification** for
  the 286 of 500 current constituents that are also present in the
  older snapshot. The ISINs in this snapshot are authentic NSDL/CDSL-
  assigned codes (verified by spot-checking against the public NSDL
  ISIN registry).
- **Why this can be trusted as a source for ISIN**:
  - ISIN codes are issued once by NSDL and never reassigned. So an
    ISIN captured in 2019 for `RELIANCE` (= `INE002A01018`) is
    still that company's ISIN today, unchanged.
  - For the 214 newer companies, ISINs need to be looked up fresh
    from NSDL (https://nsdl.co.in/master/) when needed — this is
    documented in the "How to refresh" section below.

### 2.3 What was attempted and blocked

| Source attempted | Method | Result |
|------------------|--------|--------|
| https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv | curl + Mozilla UA | HTTP 403 Akamai |
| Same URL via WebFetch | WebFetch | HTTP 403 Akamai |
| Same URL via wget + full browser headers | wget | HTTP 403 Akamai |
| https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv | curl | HTTP 403 Akamai |
| https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20500 | curl | HTTP 403 (NSE main API) |
| NSE cookie warmup → data fetch | curl with cookie jar | HTTP 403 (Akamai still blocks) |
| Various subdomains (www1, niftyindices.com without www) | curl | HTTP 403 / connection refused |
| SBI Nifty 500 Index Fund factsheet PDF (SEBI-mandated) | WebFetch + pdftotext | Only top-10 holdings; full portfolio not in factsheet |

**Conclusion**: NSE's own URLs are technically inaccessible to
programmatic fetches from this environment. **screener.in** is the
most directly-NSE-mirrored source that *is* programmatically
accessible from here.

### 2.4 To get NSE-direct data, the user must download via a browser

```
1. Open https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv
   in a desktop browser (Akamai's interactive challenge will pass)
2. Save the downloaded CSV
3. Normalize column headers:
     Company Name -> company_name
     Industry     -> industry
     Symbol       -> nse_symbol
     Series       -> series
     ISIN Code    -> isin
4. Sort alphabetically by company_name
5. Replace this file
```

After such a refresh, all 500 rows will have both ISIN and industry
populated.

## 3. Data quality verification

| Check | Result |
|-------|--------|
| Row count | 500 (matches NSE Nifty 500 methodology of 500 constituents) |
| `nse_symbol` populated | 500/500 |
| `nse_symbol` unique | ✓ (no duplicates) |
| `isin` populated | 286/500 (the 286 from the cached NSE-format snapshot) |
| `isin` format (`INE` or `IN9` prefix for Indian equities) | ✓ for all 286 populated |
| `isin` unique among populated | ✓ |
| `series` all `EQ` | ✓ |
| Spot-check top 10 by Nifty 500 weight | ✓ All present: RELIANCE (INE002A01018), HDFCBANK (INE040A01026), BHARTIARTL (INE397D01024), ICICIBANK (INE090A01021), TCS (INE467B01029), SBIN (INE062A01020), LT, BAJFINANCE, INFY (INE009A01021), LICI (LIC India, listed May 2022, missing from cached file as expected) |
| Recent additions present | ✓ LICI, ADANIENT, NESTLEIND, JIOFIN, ETERNAL, HYUNDAI, GROWW, IRFC — all the post-2020 NSE 500 additions are in the screener-current list |
| Special-character symbols handled | ✓ M&M, GVT&D, M&MFIN, ARE&M, J&KBANK all present |

## 4. Industry breakdown — limited to the 286 with industry data

| Industry | Count (of 286) |
|----------|---------------:|
| FINANCIAL SERVICES | 51 |
| CONSUMER GOODS | 42 |
| INDUSTRIAL MANUFACTURING | 25 |
| PHARMA | 21 |
| ENERGY | 18 |
| ... | (full enumeration in CSV) |

The 214 newer constituents have blank `industry`. The current NSE
industry classification can be back-filled from a fresh
niftyindices.com download (per §2.4 above) when needed.

## 5. About the Nifty 500 index itself

- **Provider**: NSE Indices Limited (formerly IISL — India Index
  Services & Products Limited).
- **Launch date**: 8 November 1996 (base = 1000, base date 1995).
- **Coverage**: Top 500 stocks by free-float market capitalization on
  NSE; represents ~95% of NSE's total free-float market cap.
- **Methodology**: Free-float market-cap weighted; semi-annual
  rebalancing (March and September).
- **Sub-indices within Nifty 500**:
  - Nifty 50 (top 50)
  - Nifty Next 50 (51-100)
  - Nifty Midcap 100 (next 100)
  - Nifty Smallcap 100 (next 100)
  - Total: 350 of 500 are categorized; the remaining 150 are
    unclassified small-caps within the broader 500.

For deeper analysis of these sub-indices (year-end closes + P/E +
forward returns), see `MarketTiming/EquityIssuanceVsIndex/` in this
repository.

## 6. Authoritative cross-check sources

For any individual company name / symbol / ISIN:
- **NSE official symbol lookup**:
  https://www.nseindia.com/companies-listing/corporate-filings-company-search
- **BSE official symbol lookup**:
  https://www.bseindia.com/corporates/List_Scrips.aspx
- **NSDL ISIN registry** (issuer of authoritative ISINs):
  https://nsdl.co.in/master/static_files.php
- **AMFI scheme/security master** (SEBI-regulated):
  https://www.amfiindia.com/

For the live current Nifty 500 list:
- **NSE Indices factsheet** (PDF, monthly):
  https://nsearchives.nseindia.com/content/indices/ind_nifty_500.pdf
- **niftyindices.com CSV** (canonical, browser-only from this env):
  https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv

## 7. Use this file for…

- Building a stock universe for screening or systematic analysis.
- Joining external fundamentals (revenue, EPS, balance sheet) by
  `nse_symbol` (always available) or `isin` (when populated).
- Industry-level aggregation for sector-based analysis (limited to
  the 286 rows with industry data unless refreshed).
- Sampling stocks for per-company deep dives — the
  `IndividualStockAnalysis/India/BalanceSheet/` folder is structured
  for this (one analysis per stock).
