# Nifty Midcap 100 Yearly Closing Values and P/E — Data Sources (`nifty_midcap100_data.csv`)

Preparation date: 2026-05-12 (extended 2026-05-18 with SEBI ARs for 2006-2009; 2026-05-24 to add `pe_ratio` and `pe_source` columns).

This file gives **year-end (last trading day of December)** closing
values and trailing P/E ratios of the Nifty Midcap 100 index, calendar
years **2006 through 2025** (20 years).

## File format

| Column                 | Meaning                                                                  |
|------------------------|--------------------------------------------------------------------------|
| calendar_year          | Calendar year (Jan-Dec).                                                 |
| year_end_date          | Last NSE trading day of December that year.                              |
| index_name_in_source   | Name under which the index appeared in the source.                        |
| year_end_close         | Closing index value on `year_end_date`.                                  |
| pe_ratio               | Trailing P/E ratio at year-end.                                          |
| pe_source              | Source of the P/E value.                                                  |

## Sources by period

### 2012-2025 — NSE archives end-of-day bhavcopy
Both close and P/E pulled directly from
`https://archives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv`
(P/E is column 11).

### 2010-2011 — SEBI Annual Reports
- **Close** from SEBI Handbook 2015 Table 80 (Nifty Midcap 100 monthly).
- **P/E** from SEBI Annual Report Part II Table 2.16 (CNX Mid Cap
  column, month-end values).

### 2006-2009 — SEBI Annual Reports Part II
Both close and P/E from Table 2.8 (close) and Table 2.16 (P/E) in
each year's AR Part II "Review of Trends and Operations". The CNX Mid
Cap column was added to SEBI's broader-indices tables from AR 2006-07
onwards, when the index moved into mainstream tracking.

## ⚠️ Notable P/E anomalies (real, not data errors)

| Year | P/E | Why it looks extreme |
|------|------:|----------------------|
| 2017 | 52.61 | Pre-2018 mid-cap mania — earnings hadn't kept pace with the index surge. Smallcap was even higher (105.82). |
| 2020 | **419.32** | COVID-era earnings collapse. The denominator (E) was nearly zero for many mid-cap constituents in trailing-12M (Apr 2019 - Mar 2020). When E → 0, P/E → ∞. This is a real bhavcopy value from NSE, not a data-entry error. |
| 2018 | 42.29 | Aftermath of 2017 peak — prices had fallen but earnings hadn't recovered. |
| 2024 | 41.89 | 2024 was a strong-rally year; earnings were still catching up. |

For valuation comparisons across years, the 2020 value is essentially
not interpretable as a valuation metric — it's an artefact of the
denominator. Cross-year comparisons should exclude 2020 or
contextualize.

## Verification

| Year | Close | P/E | Source cross-check |
|------|------:|------:|--------------------|
| 2012 | 8,505.10 | 17.71 | NSE bhavcopy (close matches SEBI Handbook 2015) |
| 2010 | 8,857.20 | 20.00 | Close from Handbook 2015; P/E from AR 2010-11 — both authoritative |
| 2008 | 3,736.00 | 9.43  | AR 2008-09 — captures GFC drawdown (price down 59%, P/E compressed to 9.4) |
| 2007 | 9,200.00 | 25.08 | AR 2007-08 — pre-GFC peak; P/E elevated but not extreme |

## Index-name evolution

| Calendar year | Name in source |
|---------------|----------------|
| 2006-2007 | CNX Mid Cap (SEBI AR column header) |
| 2008-2009 | CNX Mid-cap (slight spelling change) |
| 2010-2011 | Nifty Midcap 100 (SEBI Handbook 2015) |
| 2012-2014 | CNX Midcap (NSE bhavcopy) |
| 2015 | Nifty Midcap 100 |
| 2016-2017 | Nifty Free Float Midcap 100 (NSE briefly published Free Float + Full versions; Free Float is the continuation) |
| 2018-2025 | NIFTY Midcap 100 |

## Why 2003-2005 are not in the CSV

See the original sources doc — same reasoning applies for P/E:
- SEBI AR 2004-05 Table 2.20 reports CNX Mid Cap monthly P/E, but uses
  the older index methodology that doesn't reconcile with today's
  back-computed series.
- AR 2005-06 PDF is scanned image — no extractable data.
- SEBI AR 2006-07 onwards back-computes the modern series.

For pre-2006 backfill, manual download from niftyindices.com is the
only authoritative path.

## How to extend

Add a new year by downloading the year-end NSE bhavcopy from the URL
pattern above — both close and P/E come from the same file.
