# Nifty Capital Markets Index — Yearly Closing Values (`nifty_capital_markets_data.csv`)

Preparation date: 2026-05-25.

This file is **a scaffold with all year-end-close cells empty** —
I was unable to programmatically fetch the values from a trusted
source in this environment. The 7 rows (CY 2019-2025) are pre-filled
with the correct dates and source citations, and the close values
need to be filled in via a one-time manual browser download from
niftyindices.com (procedure below; takes ~5 minutes).

This is the same situation I documented for the pre-2012 Nifty
Smallcap 100 backfill — the data exists at NSE Indices but the
public API / archive endpoints are blocked by Akamai from this
environment.

---

## 1. The index — what it is

- **Name**: Nifty Capital Markets Index (NSE ticker `NIFCAPMARK` / `NIFTYCM`)
- **Launched**: **9 September 2024** by NSE Indices Limited
- **Base date**: **1 April 2019** (base value 1000)
- **Constituents**: Up to 20 stocks (currently 17 per Screener.in) drawn
  from the Nifty 500, selected from the capital-markets sub-segments:
  asset management, exchanges, depositories, stockbroking, wealth
  management, investment banking, registrars, ratings agencies.
- **Methodology**: Free-float market-cap weighted with a 20% stock-level cap
- **Rebalancing**: Semi-annual
- **Pre-launch history**: Values from 1 April 2019 to 9 September 2024
  are NSE Indices' back-computed series (same methodology applied
  retroactively).
- **Post-launch**: Values from 9 September 2024 onwards are live.

## 2. Confirmed reference values (anchors for sanity-checking the backfill)

From sources I was able to fetch in this environment:

| Value | Date | Source |
|------:|------|--------|
| **1,000.00** | 1 Apr 2019 (base) | NSE Indices base methodology |
| **5,649** | 25 May 2026 (close, intraday end) | Finology Ticker (`ticker.finology.in/market/index/nse/niftycm`) |
| **5,649** | 25 May 2026 (close) | Screener.in (`NIFCAPMARK`) |
| **52-week high: 5,674** | within Jun-2025 to May-2026 window | Screener.in |
| **52-week low: 4,087** | within Jun-2025 to May-2026 window | Screener.in |
| **1-Year CAGR: +37.0%** | as of 25 May 2026 | Screener.in |

From the 1-year CAGR, the index was at approximately **5,649 / 1.37 ≈
4,123** around 25 May 2025. This is consistent with the 52-week low
of 4,087 reported by Screener.in (i.e. the low was sometime in mid-2025).

## 3. Why the year-end cells are empty

I attempted three fetch paths:

1. **NSE end-of-day index bhavcopy** — same URL pattern that worked
   for Nifty 50 / Midcap 100 / Smallcap 100 in this folder:
   `https://archives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv`.
   Returned HTTP 403 (Akamai "Access Denied") from this environment
   for every date I tried (31-Dec-2025, 30-Dec-2024, etc.).

2. **NSE Indices factsheet PDF**:
   `https://www.niftyindices.com/Factsheet/Factsheet_NiftyCapitalMarkets.pdf`.
   Returned HTTP 403 (Akamai "Access Denied").

3. **SEBI Monthly Bulletin April 2026 Annexure Tables** —
   downloaded successfully earlier in the project. Searched all 66
   sheets for "Capital Markets" / "NIFCAPMARK" references. SEBI's
   indices-related tables (Daily Volatility of Major Indices, Trends
   in Cash Segment) still track Sensex / BSE 100 / BSE 500 / Nifty 50
   / Nifty Next 50 / Nifty 500 / SX40 — they have not yet been
   updated to include the Nifty Capital Markets Index (launched
   only ~20 months ago).

So no authoritative SEBI/NSE source for year-end Nifty Capital
Markets closes was reachable here. Browser-based download from
niftyindices.com is the only path.

## 4. Manual backfill steps (≈5 minutes)

This is the same procedure documented in `nifty_smallcap100_data_sources.md`,
applied to the Nifty Capital Markets index:

### Step 1
Open **https://www.niftyindices.com/reports/historical-data** in
Chrome / Firefox / Safari.

### Step 2
Fill the form:

| Field | Value |
|-------|-------|
| **Select Index** | type `NIFTY CAPITAL MARKETS` and pick from dropdown |
| **From Date** | `01-Apr-2019` |
| **To Date** | `31-Dec-2025` |

Click **Get Data**.

### Step 3
The page renders a daily table. Click the **Download (.csv)** link at
the top-right of the table to get a file like `NIFTY CAPITAL
MARKETSHistorical.csv`.

### Step 4
For each calendar year 2019-2025, pick the last NSE trading day of
December and grab the **Close** column:

| Calendar year | Last NSE trading day of December |
|---------------|----------------------------------|
| 2019 | 31-Dec-2019 (Tue) |
| 2020 | 31-Dec-2020 (Thu) |
| 2021 | 31-Dec-2021 (Fri) |
| 2022 | 30-Dec-2022 (Fri) |
| 2023 | 29-Dec-2023 (Fri) |
| 2024 | 30-Dec-2024 (Mon) |
| 2025 | 31-Dec-2025 (Wed) |

### Step 5
Paste each Close value into the `year_end_close` column of
`nifty_capital_markets_data.csv`. The dates and `index_name_in_source`
columns are already pre-filled.

### Step 6 (sanity check)
- The base value on 1-Apr-2019 = 1000.0 (definitional).
- Your 25-May-2026 value should be near 5,649.
- The 1-year CAGR from your 2024-12-30 cell to about May 2026
  should be in the 30-40% range (vs Screener.in's reported +37%).

## 5. Where the index fits in this folder's analysis

The Nifty Capital Markets Index is the **leveraged play** on the same
trend that pattern #2 in `patterns_high_probability.md` captures
("Record IPO amount → Nifty 50 UP next year, 4/4 = 100%"). The
mechanism is direct: every constituent of this index earns fees or
revenue from the same activities that drive IPO/FPO/SIP supply:

- **Exchanges (BSE Ltd, MCX)**: listing fees, transaction fees on
  record trading volumes
- **Depositories (CDSL, NSDL)**: demat-account fees on the
  22.5 crore-account base
- **AMCs (HDFC AMC, Nippon Life, UTI, ABSL)**: AUM fees on
  ~₹26-27k cr monthly SIP inflows
- **Brokers / I-banks (Angel One, Motilal, JM Financial, IIFL)**:
  brokerage, underwriting, advisory fees on record IPO supply
- **Wealth managers (360 ONE, Nuvama)**: AUM fees on rising
  household financialization
- **Registrars (KFin, CAMS)**: per-folio fees on growing
  mutual fund + IPO investor base

Once the year-end values are backfilled, this CSV becomes a clean
test of: did the Nifty Capital Markets Index outperform Nifty 50
during the high-issuance period (2022-2025)? The 1-Year CAGR of
+37% (vs Nifty 50's CY 2025 +10.5%) is a strong hint that yes, it
significantly outperformed during the recent IPO supply surge.

## 6. Adding it to the interactive chart and pattern analysis

Once the year-end values are filled in:

1. Re-run `python3 build_interactive_data.py` to refresh the JSON
   that drives `all_series_interactive.html` (you'll need to add the
   new index columns to that script — the existing version only
   loads the original 5 CSVs).

2. Re-run `python3 find_patterns.py` after adding the Nifty Capital
   Markets close + YoY to the loader. Likely strong patterns:
   - "IPO amount > ₹50k cr → Nifty Capital Markets UP next year"
     should test similarly to or stronger than the Nifty 50
     version (pattern #2 in this folder).
   - Outperformance vs Nifty 50 during high-issuance years.

## 7. Caveats

- The Nifty Capital Markets Index has only ~5 years of back-computed
  history (since April 2019) and ~20 months of live history. The
  small sample size limits any pattern analysis to qualitative
  observations.
- Pre-launch (back-computed) values reflect today's methodology
  applied retroactively to today's constituents. Index constituents
  may have been different in 2019-2024.
- The index is by NSE Indices' methodology a "Thematic Index" — it
  trades alongside but separately from Sensex/Nifty 50 mainline
  benchmarks and isn't included in SEBI's standard tracking tables yet.
