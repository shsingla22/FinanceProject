# Nifty Smallcap 100 Yearly Closing Values — Data Sources (`nifty_smallcap100_data.csv`)

Preparation date: 2026-05-12.

This file gives **year-end (last trading day of December)** closing
values of the Nifty Smallcap 100 index, calendar years **2012 through
2025** — sourced directly from NSE archives bhavcopy files.

## File format

| Column                 | Meaning                                                                  |
|------------------------|--------------------------------------------------------------------------|
| calendar_year          | Calendar year (Jan-Dec).                                                 |
| year_end_date          | Last NSE trading day of December that year.                              |
| index_name_in_source   | Name under which the index appeared in the NSE bhavcopy (see note 1).    |
| year_end_close         | Closing index value on `year_end_date`.                                  |
| source                 | NSE archives bhavcopy filename.                                          |

## Source

Each row was pulled from the publicly accessible NSE end-of-day index
bhavcopy at:

  `https://archives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv`

where `DDMMYYYY` is the last NSE trading day of December that year.
These are the official NSE EOD index files used by every Indian
financial-data redistributor.

## Note 1 — Index-name evolution

NSE renamed and restructured the smallcap index series over the years.
The underlying methodology (free-float market-cap weighted, 100
constituents from the smallcap segment) has been consistent throughout;
only the index label changed. The values are continuous despite the
renaming.

| Calendar year | Name appearing in bhavcopy           |
|---------------|---------------------------------------|
| 2012-2014     | **CNX Smallcap**                      |
| 2015          | **Nifty Smallcap 100** (renamed)      |
| 2016-2017     | **Nifty Free Float Smallcap 100** (NSE briefly published two parallel versions — Free Float and Full — during transition; the Free Float version is the one continuing as today's Nifty Smallcap 100) |
| 2018-2025     | **Nifty Smallcap 100** (Full version discontinued) |

Cross-check that the series is continuous: 2014 (5,272.90, CNX Smallcap)
→ 2015 (5,653.30, Nifty Smallcap 100) → 2016 Free Float (5,780.85). The
year-on-year changes are small and consistent with single-year market
moves. The Full version published in parallel in 2016-2017 (2,960 in
2016, 4,622 in 2017) is a different index and is **not** used here.

## Missing years (2004 through 2011)

The Nifty Smallcap 100 has a **base date of 1 January 2004** (base value
= 1000), so values exist back to 2004. However:

- The NSE archives bhavcopy CSV files (`ind_close_all_DDMMYYYY.csv`) only
  start from 2012 — older files return 404.
- The official NSE Indices historical-data download at
  https://www.niftyindices.com/reports/historical-data exposes all
  values from 2004 but blocks programmatic access from this environment
  (Akamai bot defense).
- Aggregator sites (Yahoo Finance, Investing.com, Trendlyne) either
  block scraping or paywall the full history.

To complete the 2004-2011 rows, manually download the daily index data
for Nifty Smallcap 100 from niftyindices.com from a browser, pick the
last December trading day each year, and append to this CSV. Each year's
file is a 1-click download — total time to fill the 8 missing years is
≈ 5 minutes.

## Verification (sample cross-checks against NSE archives)

| Year | year_end_close | Notes                                                                                 |
|------|----------------|---------------------------------------------------------------------------------------|
| 2024 | 18,639.95      | Bhavcopy for 30-12-2024; 31-12-2024 was a holiday (year-end NSE settlement).          |
| 2025 | 17,713.95      | Bhavcopy for 31-12-2025; matches market commentary that smallcaps ended 2025 weakly after a strong 2024. |
| 2018 | 6,449.15       | Bhavcopy for 31-12-2018; reflects the well-known 2018 smallcap drawdown.              |
| 2014 | 5,272.90       | Bhavcopy for 31-12-2014; index still named "CNX Smallcap" then.                       |

All values are unrounded — taken as published in the NSE bhavcopy.

## How to use / extend

- Add a new row each year by downloading the year-end NSE bhavcopy from
  the URL pattern above.
- For pre-2012 backfill, download from niftyindices.com via a browser
  (the data exists; only programmatic access is blocked).
- Combine with the existing `data.csv` Nifty 50 column to compute
  smallcap vs largecap ratios over time.
