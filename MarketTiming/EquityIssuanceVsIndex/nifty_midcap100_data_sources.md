# Nifty Midcap 100 Yearly Closing Values — Data Sources (`nifty_midcap100_data.csv`)

Preparation date: 2026-05-12.

This file gives **year-end (last trading day of December)** closing
values of the Nifty Midcap 100 index, calendar years **2010 through
2025** — sourced from NSE archives bhavcopy files and the SEBI Handbook
of Statistics 2015.

## File format

| Column                 | Meaning                                                                  |
|------------------------|--------------------------------------------------------------------------|
| calendar_year          | Calendar year (Jan-Dec).                                                 |
| year_end_date          | Last NSE trading day of December that year.                              |
| index_name_in_source   | Name under which the index appeared in the source (see note 1).          |
| year_end_close         | Closing index value on `year_end_date`.                                  |
| source                 | NSE bhavcopy filename or SEBI Handbook reference.                        |

## Sources

### NSE archives bhavcopy (2012-2025)
Pulled directly from the publicly accessible NSE end-of-day index
bhavcopy at:

  `https://archives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv`

where `DDMMYYYY` is the last NSE trading day of December that year.
These are the official NSE EOD index files used by every Indian
financial-data redistributor.

### SEBI Handbook of Statistics 2015 (2010-2011)
NSE bhavcopy archives don't go back before 2012. For 2010 and 2011 the
Dec values are taken from **SEBI Handbook of Statistics on the Indian
Securities Market 2015, Table 80 "Trends of Broader Stock Indices"**
(monthly indices), which has the Nifty Midcap 100 month-end close in
its "Nifty Midcap 100" column starting Apr-10:

  https://www.sebi.gov.in/sebi_data/attachdocs/1462441113708.pdf

Verification: SEBI Table 80 Dec-12 = 8,505.1 and Dec-13 = 8,071.3 —
both exactly match NSE bhavcopy values, confirming the SEBI series is
the same Nifty Midcap 100 index and not a different aggregate.

## Note 1 — Index-name evolution

NSE renamed and briefly restructured the midcap index just like the
smallcap index. The underlying methodology (free-float market-cap
weighted, 100 midcap constituents, base date 1 January 2003 = 1000) has
been consistent throughout; only the index label changed. The values
are continuous across the rename.

| Calendar year | Name appearing in source                                       |
|---------------|----------------------------------------------------------------|
| 2010-2011     | Nifty Midcap 100 (SEBI Handbook column header)                 |
| 2012-2014     | **CNX Midcap** (NSE bhavcopy)                                  |
| 2015          | **Nifty Midcap 100** (renamed)                                 |
| 2016-2017     | **Nifty Free Float Midcap 100** (NSE briefly published two parallel versions — Free Float and Full — during transition; the Free Float version is the one continuing as today's Nifty Midcap 100) |
| 2018-2025     | **NIFTY Midcap 100** (Full version discontinued)               |

Cross-check that the series is continuous: 2014 (12,583.85, CNX Midcap)
→ 2015 (13,396.70, Nifty Midcap 100) → 2016 Free Float (14,351.45). The
year-on-year changes are consistent with single-year market moves. The
parallel Full version published in 2016-2017 (4,402 in 2016, 6,697 in
2017) is a different index and is **not** used here.

## Missing years (2003 through 2009)

The Nifty Midcap 100 has a **base date of 1 January 2003** (base value
= 1000), so values exist back to 2003. However:

- NSE archives bhavcopy CSV files (`ind_close_all_DDMMYYYY.csv`) only
  start from 2012 — older files return 404.
- SEBI Handbook of Statistics 2010 (covering FY 2001-02 to FY 2009-10)
  tracks Sensex, BSE 100, BSE 500, Nifty 50, and CNX Nifty Junior in its
  broader-indices table but **does not** include the Nifty Midcap 100 —
  even though the index existed and was being computed from 2003. SEBI
  began including Nifty Midcap 100 in its Handbook from the 2014/2015
  edition onwards.
- The official NSE Indices historical-data download at
  https://www.niftyindices.com/reports/historical-data exposes all
  values from 2003 but blocks programmatic access from this environment
  (Akamai bot defense).

To complete the 2003-2009 rows, manually download the daily index data
for Nifty Midcap 100 from niftyindices.com via a browser (same procedure
as the Smallcap 100 backfill — see `nifty_smallcap100_data_sources.md`).
Take the last December trading day each year and append to this CSV.

## Verification (sample cross-checks)

| Year | year_end_close | Notes                                                                                 |
|------|----------------|---------------------------------------------------------------------------------------|
| 2024 | 57,189.75      | Bhavcopy for 30-12-2024; 31-12-2024 was a holiday (year-end NSE settlement).          |
| 2018 | 17,875.50      | Bhavcopy for 31-12-2018; reflects the well-known 2018 midcap drawdown.                |
| 2014 | 12,583.85      | Bhavcopy for 31-12-2014; index still named "CNX Midcap" then.                         |
| 2012 | 8,505.10       | NSE bhavcopy matches SEBI Handbook 2015 Table 80 Dec-12 = 8,505.1 exactly.            |
| 2011 | 6,111.90       | From SEBI Handbook 2015 Table 80 (NSE archives unavailable for 2011).                 |

All values are unrounded — taken as published in the NSE bhavcopy or
SEBI Handbook.

## How to use / extend

- Add a new row each year by downloading the year-end NSE bhavcopy from
  the URL pattern above.
- For pre-2010 backfill, download from niftyindices.com via a browser.
- Combine with `nifty_smallcap100_data.csv` and the `data.csv` Nifty 50
  series to study size-segment relative performance over time.
