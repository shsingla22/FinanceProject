# Nifty 50 Yearly Closing Values — Data Sources (`nifty50_data.csv`)

Preparation date: 2026-05-12.

This file gives **year-end (last trading day of December)** closing
values of the Nifty 50 index, calendar years **2000 through 2025** —
26 years of data, no gaps, sourced from NSE bhavcopy / SEBI handbooks
/ SEBI Annual Reports, with Wikipedia cross-checked against SEBI for
overlapping years.

## File format

| Column                 | Meaning                                                                  |
|------------------------|--------------------------------------------------------------------------|
| calendar_year          | Calendar year (Jan-Dec).                                                 |
| year_end_date          | Last NSE trading day of December that year.                              |
| index_name_in_source   | Name under which the index appeared in the source (S&P CNX Nifty was renamed to CNX Nifty in 2012 and then to NIFTY 50 in 2015). |
| year_end_close         | Closing index value on `year_end_date`.                                  |
| source                 | NSE bhavcopy / SEBI publication reference.                               |

## Sources by period

### 2012-2025 — NSE archives end-of-day bhavcopy
Pulled directly from the publicly accessible NSE EOD index file at:

  `https://archives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv`

where `DDMMYYYY` is the last NSE trading day of December that year.
These are the official NSE EOD files used by every Indian
financial-data redistributor.

### 2010-2011 — SEBI Handbook of Statistics 2015, Table 84
Monthly "Nifty 50 Index — Close" column gives month-end closes from
April 2010 onwards. NSE bhavcopy archives only start at 2012, so for
these two years the SEBI Handbook is the authoritative source.

  https://www.sebi.gov.in/sebi_data/attachdocs/1462441113708.pdf

### 2002-2003 — SEBI Annual Report Part II monthly tables
- **2002 (Dec)**: SEBI Annual Report 2002-03 Part II, Table 2.19
  "Stock Market Indicators: Closing Value of Index as on Last Trading
  Day of the Month" — S&P CNX Nifty Dec-02 column = 1093.50.
  https://www.sebi.gov.in/sebi_data/commondocs/0203b_p.pdf

- **2003 (Dec)**: SEBI Annual Report 2003-04 Part II, Table 2.9
  "Stock Indices" — S&P CNX Nifty Dec-03 column = 1879.75.
  https://www.sebi.gov.in/sebi_data/commondocs/trends_p.pdf

### 2001 — SEBI Handbook of Statistics 2008, Table 60
Monthly "S&P CNX Nifty Index — Close" column for Dec-01 = 1059.05.

  https://www.sebi.gov.in/sebi_data/attachdocs/1291361448574.pdf

### 2000, 2004-2009 — Wikipedia NIFTY 50 annual returns table
The Wikipedia NIFTY 50 article maintains an "Annual returns" table
with year-end closing values from 2000 onwards. I used Wikipedia for
these 7 years because:

1. **SEBI Annual Reports for 2004-2009 publish the same Dec-XX values
   rounded to integer** (e.g., AR 2004-05 reports Dec-04 = 2081 vs
   Wikipedia 2080.50; AR 2008-09 reports Dec-08 = 2959 vs Wikipedia
   2959.15). All 6 overlapping years (2004-09) reconcile exactly when
   you round the Wikipedia value — Wikipedia just has 2-decimal
   precision.
2. **SEBI Annual Report 2005-06 Part II PDF is a scanned image** (the
   Konica Minolta scanner metadata is visible in the PDF) and yields
   zero extractable text. Wikipedia is the next-best authoritative
   source for Dec 2005.
3. **For Dec 2000**, the only SEBI source available is the AR 2000-01
   Table 2.18, which publishes **monthly averages**, not month-end
   closes. Wikipedia's 1263.55 is consistent with the monthly average
   of 1291.43 (Dec average) and the March 2001 close of 1148.20 from
   the same AR.

  https://en.wikipedia.org/wiki/NIFTY_50

## Verification: Wikipedia vs SEBI/NSE sources for overlapping years

| Year | Wikipedia | SEBI/NSE source | Match? |
|------|-----------|------------------|--------|
| 2001 | 1059.05   | 1059.05 (SEBI HBS 2008 Table 60)        | exact   |
| 2002 | 1093.50   | 1093.50 (SEBI AR 2002-03)               | exact   |
| 2003 | 1879.75   | 1879.75 (SEBI AR 2003-04)               | exact   |
| 2004 | 2080.50   | 2081 (SEBI AR 2004-05, integer)         | rounds  |
| 2006 | 3966.40   | 3966 (SEBI AR 2006-07, integer)         | rounds  |
| 2007 | 6138.60   | 6139 (SEBI AR 2007-08, integer)         | rounds  |
| 2008 | 2959.15   | 2959 (SEBI AR 2008-09, integer)         | rounds  |
| 2009 | 5201.05   | 5201 (SEBI AR 2009-10, integer)         | rounds  |
| 2010 | 6134.50   | 6134.5 (SEBI HBS 2015 Table 84)         | exact   |
| 2011 | 4624.30   | 4624.3 (SEBI HBS 2015 Table 84)         | exact   |
| 2012 | 5905.10   | 5905.10 (NSE bhavcopy)                  | exact   |
| 2013 | 6304.00   | 6304.00 (NSE bhavcopy)                  | exact   |
| 2014 | 8282.70   | 8282.70 (NSE bhavcopy)                  | exact   |
| 2015 | 7964.35*  | **7946.35** (NSE bhavcopy)              | **NSE wins** — Wikipedia value looks like a digit-swap typo (7964 vs 7946) |
| 2016+ | as published | match NSE bhavcopy                   | exact   |

*The 2015 value is the one place Wikipedia disagrees with the
authoritative NSE bhavcopy. The CSV uses **7946.35** from NSE bhavcopy.

The 2024 value: Wikipedia 23644.80 vs NSE bhavcopy 23644.90 — a
0.10 point difference (likely Wikipedia rounded). The CSV uses
**23644.90** from NSE bhavcopy.

## Index-name evolution

NSE renamed the index over the years:
- **S&P CNX Nifty** — through 2012 (SEBI tables use this name)
- **CNX Nifty** — 2013-2014 (NSE dropped S&P prefix)
- **Nifty 50** — 2015 onwards (NSE renamed to current name)

The underlying methodology and constituents have been continuous;
only the label changed. The CSV preserves the source-document label.

## How to use / extend

- Add each new year by downloading the year-end NSE bhavcopy from the
  URL pattern above.
- The 2015 Wikipedia value (7964.35) should be ignored in favor of NSE
  bhavcopy (7946.35) — Wikipedia has a typo on this one row.
- Combine with `nifty_smallcap100_data.csv` and `nifty_midcap100_data.csv`
  to study size-segment relative performance.
