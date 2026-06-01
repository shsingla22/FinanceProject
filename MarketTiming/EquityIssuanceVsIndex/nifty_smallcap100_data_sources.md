# Nifty Smallcap 100 Yearly Closing Values and P/E — Data Sources (`nifty_smallcap100_data.csv`)

Preparation date: 2026-05-12 (extended 2026-05-24 to add `pe_ratio` and `pe_source` columns).

This file gives **year-end (last trading day of December)** closing
values and trailing P/E ratios of the Nifty Smallcap 100 index,
calendar years **2012 through 2025** — sourced directly from NSE
archives bhavcopy files.

## File format

| Column                 | Meaning                                                                  |
|------------------------|--------------------------------------------------------------------------|
| calendar_year          | Calendar year (Jan-Dec).                                                 |
| year_end_date          | Last NSE trading day of December that year.                              |
| index_name_in_source   | Name under which the index appeared in the source.                        |
| year_end_close         | Closing index value on `year_end_date`.                                  |
| pe_ratio               | Trailing P/E ratio at year-end (blank where NSE published no value).      |
| pe_source              | Source of the P/E value.                                                  |

## Source

Both close and P/E pulled directly from the NSE end-of-day index
bhavcopy at:

  `https://archives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv`

P/E is column 11. NSE archives bhavcopy CSV files only start from 2012;
pre-2012 Smallcap data (the index goes back to base date 1 Jan 2004)
requires manual download from niftyindices.com — same procedure as
documented for close-value backfill.

## ⚠️ Notable P/E observations (real, not data errors)

| Year | P/E | Why it looks extreme |
|------|------:|----------------------|
| 2012 | 46.53 | Smallcaps generally trade at higher P/E than the broad index — earnings volatility makes trailing P/E noisy. |
| 2013 | 44.10 | Similar — smallcap structural premium. |
| 2017 | **105.82** | Pre-2018 smallcap mania — the cleanest documented case of supply-side froth. Smallcap rallied +57% in CY 2017 alongside record IPO supply (FY 2017-18). Index then fell -29% in CY 2018. |
| 2019 | **100.44** | Smallcap earnings collapsed in 2018-19 (the lagged effect of the 2018 drawdown plus IL&FS-led NBFC stress); the denominator shrank faster than the index. |
| 2020 | 37.92 | COVID year — smallcap earnings collapsed but the index also fell mid-year. Net effect was a high but not absurd P/E. |
| 2016 | (blank) | NSE bhavcopy published the close (5,780.85 for Nifty Free Float Smallcap 100) but left the P/E field empty. Likely a methodology transition during the Free Float / Full split. The blank is preserved as-is. |

The 2017 and 2019 P/E spikes are arguably the most informative
data points in the file — both flag mid-cycle smallcap valuation
extremes (one driven by price, one by collapsing earnings) that
preceded broader-market repricing.

## Verification

| Year | Close | P/E | Source |
|------|------:|------:|--------|
| 2012 | 3,710.15 | 46.53 | NSE bhavcopy (CNX Smallcap) |
| 2017 | 9,093.25 | 105.82 | NSE bhavcopy (Nifty Free Float Smallcap 100); year of pre-crash peak |
| 2018 | 6,449.15 | 34.39 | NSE bhavcopy; P/E compressed as price fell -29% |
| 2025 | 17,713.95 | 32.18 | NSE bhavcopy (Nifty Smallcap 100) |

## Missing years (2004 through 2011)

Same situation as the close-value backfill:
- NSE archives bhavcopy starts at 2012.
- SEBI handbooks/ARs do not track Nifty Smallcap 100 in their P/E
  tables (only Sensex, BSE 100, S&P CNX Nifty, CNX Mid Cap, CNX IT,
  CNX Bank, CNX PSE — no Smallcap).
- niftyindices.com has the data back to 2004 but blocks scraping.

To backfill: manual browser download from niftyindices.com historical
data (procedure in this same folder's other `*_sources.md`).

## How to extend

Add new rows by downloading the year-end NSE bhavcopy from the URL
pattern above. Both close and P/E come from the same file.
