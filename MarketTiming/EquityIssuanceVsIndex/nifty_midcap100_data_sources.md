# Nifty Midcap 100 Yearly Closing Values — Data Sources (`nifty_midcap100_data.csv`)

Preparation date: 2026-05-12 (extended 2026-05-18 with SEBI Annual Reports for 2006-2009).

This file gives **year-end (last trading day of December)** closing
values of the Nifty Midcap 100 index, calendar years **2006 through
2025** — sourced from three SEBI/NSE publications.

## File format

| Column                 | Meaning                                                                  |
|------------------------|--------------------------------------------------------------------------|
| calendar_year          | Calendar year (Jan-Dec).                                                 |
| year_end_date          | Last NSE trading day of December that year.                              |
| index_name_in_source   | Name under which the index appeared in the source (see note 1).          |
| year_end_close         | Closing index value on `year_end_date`.                                  |
| source                 | NSE bhavcopy filename or SEBI handbook/annual-report reference.          |

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

### SEBI Annual Reports Part II (2006-2009)
For calendar years 2006 through 2009 the Dec close is taken from the
monthly "Major Stock Indices and their Returns" table (Table 2.8) in
each year's SEBI Annual Report Part II "Review of Trends and Operations":

| Calendar year | SEBI Annual Report (Part II)               | URL                                                                                  |
|---------------|---------------------------------------------|--------------------------------------------------------------------------------------|
| 2006 (Dec)    | Annual Report 2006-07 Part II, Table 2.8   | https://www.sebi.gov.in/sebi_data/commondocs/part2_p.pdf                            |
| 2007 (Dec)    | Annual Report 2007-08 Part II, Table 2.8   | https://www.sebi.gov.in/sebi_data/commondocs/parttwo_p.pdf                          |
| 2008 (Dec)    | Annual Report 2008-09, Table 2.8           | https://www.sebi.gov.in/sebi_data/attachdocs/1289364867230.pdf                      |
| 2009 (Dec)    | Annual Report 2009-10, Table 2.8           | https://www.sebi.gov.in/sebi_data/attachdocs/1287808880614.pdf                      |

The index appears in these reports under the column header "CNX Mid Cap"
(later renamed "CNX Mid-cap" then "CNX Midcap" then "Nifty Midcap 100").

## Verification (cross-checks across the source chain)

- SEBI Handbook 2015 Table 80 Dec-12 = 8,505.1 matches NSE bhavcopy
  31-12-2012 = 8,505.10 **exactly**.
- SEBI Handbook 2015 Table 80 Dec-13 = 8,071.3 matches NSE bhavcopy
  31-12-2013 = 8,071.30 **exactly**.
- SEBI AR 2008-09 Mar-09 CNX Mid-cap = 3,407/3,408 and SEBI AR 2009-10
  reports same value for FY 2008-09 ending → series is continuous
  across reporting years.
- SEBI AR 2008-09 Apr-08 monthly = 7,005 connects smoothly to AR
  2007-08 Mar-08 = 6,241 (the latter is the FY-end close on which the
  next FY's monthly series picks up).

## Note 1 — Index-name evolution

NSE renamed and briefly restructured the midcap index over the years.
The underlying methodology used by every recent source (free-float MV,
100 midcap constituents, base date 1 January 2003 = 1000) has been
consistent. The CSV preserves the source label per row.

| Calendar year | Name in source                                                                     |
|---------------|-------------------------------------------------------------------------------------|
| 2006-2007     | **CNX Mid Cap** (SEBI Annual Report column header)                                  |
| 2008-2009     | **CNX Mid-cap** (SEBI Annual Report column header, slight spelling change)          |
| 2010-2011     | **Nifty Midcap 100** (SEBI Handbook 2015 column header)                             |
| 2012-2014     | **CNX Midcap** (NSE bhavcopy)                                                       |
| 2015          | **Nifty Midcap 100** (renamed in NSE bhavcopy)                                      |
| 2016-2017     | **Nifty Free Float Midcap 100** (NSE briefly published two parallel versions — Free Float and Full; the Free Float version is the one continuing as today's Nifty Midcap 100) |
| 2018-2025     | **NIFTY Midcap 100** (Full version discontinued)                                    |

## Why FY 2003-04, FY 2004-05, FY 2005-06 are not in the CSV

The SEBI Annual Reports from 2006-07 onwards back-compute and publish
the CNX Mid Cap series annually, but they only show **March-end (FY)**
values for years before the start of their monthly tables:

| FY ending | Mar-end value | Source                       |
|-----------|---------------|------------------------------|
| Mar-2004  | 2,165         | SEBI AR 2006-07 Table 2.8    |
| Mar-2005  | 2,927         | SEBI AR 2006-07 Table 2.8    |
| Mar-2006  | 4,787         | SEBI AR 2006-07 Table 2.8    |

The CSV uses **December-end** (calendar year) closes, so I excluded these
March values. The corresponding **December** closes for 2003, 2004, 2005
are not published in any SEBI source I could access.

The earlier SEBI AR 2004-05 Part II Table 2.8 does publish monthly CNX
Mid Cap values for FY 2004-05 (including Dec-04 = 2,595 and Apr-04 =
1,739), **but those use the older index methodology**. The 2004-05 AR
reports FY 2003-04 ending value as 1,603, whereas later SEBI ARs (2006-
07 and 2007-08) report FY 2003-04 ending value as 2,165 using the
back-computed modern methodology. These are not directly comparable, so
the older AR 2004-05 values are not included here.

The SEBI Annual Report 2005-06 does **not** track the CNX Mid Cap /
Nifty Midcap 100 at all (the index was launched in July 2005, in the
middle of FY 2005-06, and SEBI began including it from AR 2006-07).

To get Dec 2003 / 2004 / 2005 close values on the modern methodology,
the only authoritative source is **niftyindices.com historical data
download** (which has back-computed daily values from 1 January 2003).
That site blocks programmatic access from this environment, so a
manual browser download is required (procedure documented in
`nifty_smallcap100_data_sources.md`).

## Quick reference of the underlying SEBI tables I extracted

### From SEBI AR 2006-07 Table 2.8 (Apr-06 to Mar-07 monthly)
Apr-06: 5,141 · May-06: 4,400 · Jun-06: 3,945 · Jul-06: 3,878 ·
Aug-06: 4,307 · Sep-06: 4,692 · Oct-06: 4,835 · Nov-06: 5,069 ·
**Dec-06: 5,200** · Jan-07: 5,280 · Feb-07: 4,877 · Mar-07: 4,850

### From SEBI AR 2007-08 Table 2.8 (Apr-07 to Mar-08 monthly)
Apr-07: 5,246 · May-07: 5,644 · Jun-07: 5,976 · Jul-07: 6,178 ·
Aug-07: 6,044 · Sep-07: 6,867 · Oct-07: 7,450 · Nov-07: 7,994 ·
**Dec-07: 9,200** · Jan-08: 7,308 · Feb-08: 7,246 · Mar-08: 6,241

### From SEBI AR 2008-09 Table 2.8 (Apr-08 to Mar-09 monthly)
Apr-08: 7,005 · May-08: 6,563 · Jun-08: 5,239 · Jul-08: 5,537 ·
Aug-08: 5,699 · Sep-08: 4,891 · Oct-08: 3,506 · Nov-08: 3,310 ·
**Dec-08: 3,736** · Jan-09: 3,357 · Feb-09: 3,176 · Mar-09: 3,407

### From SEBI AR 2009-10 Table 2.8 (Apr-09 to Mar-10 monthly)
Apr-09: 3,861 · May-09: 5,354 · Jun-09: 5,427 · Jul-09: 5,950 ·
Aug-09: 6,118 · Sep-09: 6,713 · Oct-09: 6,580 · Nov-09: 7,149 ·
**Dec-09: 7,419** · Jan-10: 7,202 · Feb-10: 7,167 · Mar-10: 7,705

## How to use / extend

- Add a new row each year by downloading the year-end NSE bhavcopy from
  the URL pattern above.
- For pre-2006 backfill, download from niftyindices.com via a browser
  (their historical-data form has data from 1 January 2003 onwards).
- Combine with `nifty_smallcap100_data.csv` and the `data.csv` Nifty 50
  series to study size-segment relative performance over time.
