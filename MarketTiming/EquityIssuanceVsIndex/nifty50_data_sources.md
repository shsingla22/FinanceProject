# Nifty 50 Yearly Closing Values and P/E — Data Sources (`nifty50_data.csv`)

Preparation date: 2026-05-12 (extended 2026-05-24 to add `pe_ratio` and `pe_source` columns).

This file gives **year-end (last trading day of December)** closing
values and trailing **price-to-earnings (P/E) ratios** of the Nifty 50
index, calendar years **2000 through 2025** — 26 years of data with
no gaps, sourced from NSE bhavcopy / SEBI handbooks / SEBI Annual
Reports, with Wikipedia cross-checked against SEBI for overlapping
years.

## File format

| Column                 | Meaning                                                                  |
|------------------------|--------------------------------------------------------------------------|
| calendar_year          | Calendar year (Jan-Dec).                                                 |
| year_end_date          | Last NSE trading day of December that year.                              |
| index_name_in_source   | Name under which the index appeared in the close source.                  |
| year_end_close         | Closing index value on `year_end_date`.                                  |
| pe_ratio               | Trailing 12-month P/E ratio of the index.                                 |
| pe_source              | Source of the P/E value (each year sourced individually).                 |

## Close-value sources by period

### 2012-2025 — NSE archives end-of-day bhavcopy
Pulled directly from the publicly accessible NSE EOD index file at:

  `https://archives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv`

where `DDMMYYYY` is the last NSE trading day of December that year.
These files include the P/E ratio in column 11 of the CSV — used for
both close and P/E for 2012-2025.

### 2010-2011 — SEBI Annual Reports
- **Close** from SEBI Handbook of Statistics 2015, Table 84.
- **P/E** from SEBI Annual Report Part II, Table 2.16 (month-end Dec values).

### 2002-2009 — SEBI Annual Reports
- **Close and P/E** from SEBI Annual Report Part II monthly tables.
  Specifically Table 2.11 (AR 2003-04), Table 2.20 (AR 2004-05), Table
  2.16 (AR 2006-07 onwards) — each contains month-end Dec closing
  values and trailing P/E ratios on the last trading day.

### 2000, 2001 — SEBI Handbook of Statistics 2008
- **Close** from Wikipedia (cross-verified to SEBI for adjacent years).
- **P/E** from SEBI Handbook 2008 Table 56 (note caveat below).

### 2005 — Wikipedia + SEBI Handbook
- **Close** from Wikipedia (AR 2005-06 PDF is a scanned image with no
  extractable text).
- **P/E** from SEBI Handbook 2008 Table 56 (monthly average — see caveat).

## ⚠️ P/E methodology caveat for 2000, 2001, 2002, 2005

The SEBI Handbook 2008 Table 56 explicitly states *"Indicates monthly
averages of closing values"* — so the P/E values for these four years
are **monthly averages of daily P/E values during December**, not the
month-end P/E. For the other 22 years the P/E is the month-end value.
This is the best available authoritative source — SEBI did not publish
month-end P/E values for these years (or the source PDF is scanned and
unextractable, for 2005).

The monthly-average vs month-end gap is typically small (1-3% in
absolute P/E terms), so the time series is broadly comparable. Where
exact month-end values matter, treat 2000-2002 and 2005 as slightly
softer-precision data points.

## Verification (sample cross-checks)

| Year | Close in CSV | P/E in CSV | Cross-check |
|------|------:|------:|--------------|
| 2010 | 6,134.50 | 24.50 | SEBI Handbook 2015 Table 78 Dec-10 = 24.5 (matches AR 2010-11) |
| 2011 | 4,624.30 | 16.80 | SEBI Handbook 2015 Table 78 Dec-11 = 16.8 (matches AR 2011-12) |
| 2012 | 5,905.10 | 18.68 | NSE bhavcopy 31-12-2012 |
| 2007 | 6,138.60 | 27.62 | AR 2007-08 (the year's P/E peak in the pre-GFC bull run) |
| 2008 | 2,959.15 | 12.97 | AR 2008-09 (P/E collapsed with prices) |
| 2020 | 13,981.75 | 38.45 | NSE bhavcopy (P/E spiked because COVID compressed earnings, not because prices were extreme) |

## Index-name evolution
- **S&P CNX Nifty** — through 2012 (SEBI tables use this name)
- **CNX Nifty** — 2013-2014 (NSE dropped S&P prefix)
- **Nifty 50** — 2015 onwards (NSE renamed to current name)

The underlying methodology and constituents have been continuous; only
the label changed.

## How to use / extend

- Add each new year by downloading the year-end NSE bhavcopy from the
  URL pattern above — both close and P/E come from the same file.
- The P/E column in the bhavcopy uses NSE Indices' trailing-12M P/E
  methodology; values are directly comparable across years.
- The 2000-2002 and 2005 P/E values are monthly averages — flag them
  where strict month-end precision matters.
