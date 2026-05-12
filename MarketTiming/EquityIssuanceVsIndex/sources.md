# Data Sources & Provenance — EquityIssuanceVsIndex

This document records the source of every numeric value in `data.csv`. Per the
project rule of using only factual data, fields that could not be verified
from public sources at the time of preparation are left blank (NaN) rather
than imputed.

Preparation date: 2026-05-12.

## Conventions

- "Year" is the calendar year (Jan 1 – Dec 31).
- `nifty*_close` is the year-end close, i.e. the close on the last NSE trading
  day of December that year. (User-selected definition.)
- `ipo_amount_cr` and `fpo_amount_cr` are in INR crore (1 crore = 10 million).
- `ipo_count` / `fpo_count` cover mainboard + SME issues (user-selected scope).
- `nifty_smallcap100_constituent_median` = median of the year-end closing
  prices of the 100 constituent stocks of Nifty Smallcap 100 (user-selected
  definition).

## Nifty 50 year-end close (verified)

Source: aggregated public reporting of NSE Nifty 50 year-end closing values,
cross-referenced via Wikipedia's NIFTY 50 entry and multiple financial data
providers (Yahoo Finance, Investing.com).

| Year | Close   | Year | Close    |
|------|---------|------|----------|
| 2001 | 1059.00 | 2014 | 8282.70  |
| 2002 | 1093.50 | 2015 | 7946.30  |
| 2003 | 1879.70 | 2016 | 8185.80  |
| 2004 | 2080.50 | 2017 | 10530.00 |
| 2005 | 2836.50 | 2018 | 10862.55 |
| 2006 | 3966.40 | 2019 | 12168.45 |
| 2007 | 6138.60 | 2020 | 13981.75 |
| 2008 | 2959.10 | 2021 | 17354.05 |
| 2009 | 5201.00 | 2022 | 18105.30 |
| 2010 | 6134.50 | 2023 | 21731.40 |
| 2011 | 4624.30 | 2024 | 23644.80 |
| 2012 | 5905.10 | 2025 | 26130.00 |
| 2013 | 6304.00 |      |          |

2025 close reference: Business Standard, "Stock Market Close: Sensex gains
546 pts today, adds 9% in 2025; Nifty ends at 26,130" (31 Dec 2025).

## Nifty Midcap 100 year-end close (partial)

Verified from public summaries 2015–2024. Values prior to 2015 and the 2025
year-end close could not be cross-verified from free public sources at
preparation time and are left blank.

## Nifty Smallcap 100 year-end close (unverified)

The Nifty Smallcap 100 has a base value of 1000 with base date 1 January 2004
(launched 30 March 2011). Free public sources surfaced index existence and
return summaries but did not present a verifiable year-end close table. All
values are left blank pending sourcing from NSE Indices' historical CSV
exports (https://www.niftyindices.com/reports/historical-data) or a paid
provider.

## Nifty Smallcap 100 constituent median (unverified)

Definition (per user): median of the year-end closing prices of the 100
Nifty Smallcap 100 constituent stocks. Reliable historical computation
requires:
  1. The Nifty Smallcap 100 constituent list as of each year-end (changes
     semi-annually; published by NSE Indices).
  2. Adjusted closing prices for each of those constituents on that date
     (split / bonus / consolidation adjusted).

Free public sources do not surface this in a structured way for a 25-year
horizon. All values are left blank pending sourcing from NSE Indices and
Bhavcopy archives or a paid provider (e.g. Bloomberg, CMIE Prowess).

## IPO data (mostly unverified at the calendar-year level)

The user-selected scope is mainboard + SME. SEBI's Handbook of Statistics
reports values on a fiscal-year basis, while aggregator sites (Chittorgarh,
InvestorGain) report on a calendar-year basis. The two are not directly
comparable. The aggregator pages serving calendar-year totals returned HTTP
403 to programmatic fetches at preparation time.

The only calendar-year values that were independently corroborated:

- CY 2025: 102 mainboard IPOs, ~₹1.8 lakh crore (≈ ₹180,000 cr) raised.
  Source: Prime Infobase summary reported in Business Standard
  ("India 2025 IPOs: Record listings", 30 Dec 2025).

Fiscal-year figures available but not loaded into the calendar-year CSV:

- FY 2001-02: 35 IPOs, ₹7,543 cr
- FY 2002-03: 26 IPOs, ₹4,070 cr
- FY 2003-04: 57 IPOs, ₹23,272 cr
- FY 2004-05: 60 IPOs, ₹28,256 cr
- FY 2023-24: 76 mainboard IPOs
- FY 2024-25: 80 mainboard IPOs, ₹1,63,000 cr
  Source: SEBI Handbook of Statistics; KPMG IPO Reports.

Remaining calendar-year cells are blank pending sourcing from the
Chittorgarh / InvestorGain year-wise pages (which were not fetchable from
this environment) or the PRIME Database.

## FPO data (unverified)

No calendar-year FPO count or amount could be sourced from free public
search at preparation time. SEBI's annual reports aggregate FPOs with
rights and OFS in some tables and separate them in others. All values are
left blank pending sourcing from PRIME Database or SEBI's Handbook of
Statistics.

## How to complete the dataset

1. Subscribe to or download PRIME Database's "Public Issues" calendar-year
   summary for IPOs and FPOs (mainboard + SME).
2. Download Nifty Smallcap 100 and Nifty Midcap 100 historical EOD data
   from https://www.niftyindices.com/reports/historical-data and take the
   31 December close (or last NSE trading day of December) of each year.
3. For the smallcap constituent median: from NSE Indices, download the
   "Nifty Smallcap 100 — index constituents" file effective at each
   31 December; then fetch each constituent's adjusted close on that date
   from NSE Bhavcopy archives; take `median(prices)`.
4. Append values into `data.csv` and re-run `plot.py`.
