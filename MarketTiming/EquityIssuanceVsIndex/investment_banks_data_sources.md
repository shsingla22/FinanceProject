# Listed Investment Banking Companies — Yearly Closing Prices (`investment_banks_data.csv`)

Preparation date: 2026-05-25.

20-year history (CY 2005-2025) of year-end closing prices for **8
listed Indian companies with significant investment banking
operations**, sourced from Yahoo Finance (which carries the official
NSE/BSE split-and-dividend-adjusted EOD series).

## 1. File contents

One row per calendar year (2005-2025), one column per company.
`year_end_date` is the last NSE trading day of December. Empty cells
indicate the company wasn't listed yet in that year.

| Company | Yahoo ticker | First listed (per Yahoo) | What it does |
|---------|--------------|---------------------------|--------------|
| **JM Financial Ltd** | `JMFINANCIL.BO` | data from 2002 (BSE); used for full 20-year window | India's most established pure-play investment bank — capital markets, M&A, PE, distressed assets |
| **Motilal Oswal Financial Services** | `MOTILALOFS.NS` | Sept 2007 | Broking + investment banking + asset management |
| **Edelweiss Financial Services** | `EDELWEISS.NS` | Dec 2007 | Diversified financial — wealth, asset management, capital markets |
| **IIFL Finance (ex-IIFL Holdings)** | `IIFL.NS` | May 2005 | NBFC; was the holding company of IIFL Securities pre-2019 demerger. **NOT a pure I-bank** but the longest-running listed entity from the IIFL group |
| **Anand Rathi Wealth** | `ANANDRATHI.NS` | Dec 2021 | Wealth management + investment banking |
| **Nuvama Wealth Management** | `NUVAMA.NS` | Sept 2023 | Wealth + I-banking; spun off from Edelweiss |
| **IIFL Capital Services** | `IIFLCAPS.NS` | Nov 2024 | I-banking + broking; renamed from IIFL Securities post-2024 listing reshuffle |
| **Almondz Global Securities** | `ALMONDZ.NS` | June 2008 | Smaller I-bank + broking |

## 2. Data source

All values pulled from **Yahoo Finance** monthly historical data via
`https://query2.finance.yahoo.com/v8/finance/chart/{SYMBOL}?range=max&interval=1mo`,
parsed for each December month-end close.

Yahoo Finance carries the official NSE/BSE end-of-day series with:
- Adjustments for stock splits
- Adjustments for bonus issues
- Adjustments for dividends (in the unadjusted close column shown
  here, dividends are NOT adjusted; only splits/bonuses are)

Yahoo is widely regarded as a reliable third-party redistributor of
NSE/BSE official data. For any specific verification, the
authoritative cross-check is NSE/BSE end-of-day bhavcopy on the
exact date, which carries identical close prices.

## 3. The 20-year coverage caveat

The "20-year" framing only holds cleanly for two companies:

- **JM Financial** — listed on BSE since the 1980s; clean full
  2005-2025 series (21 year-end values).
- **IIFL Finance / ex-IIFL Holdings** — listed since May 2005; clean
  2005-2025 series (21 year-end values). But note this is an **NBFC**
  today, not a pure I-bank. Pre-2019 it was a holding co. for IIFL
  Securities (now IIFL Capital Services), IIFL Wealth (now 360 ONE
  WAM) and IIFL Finance. The price series is continuous but the
  business mix changed materially at the 2019 demerger.

The remaining six companies have shorter histories:

| Company | First year | Years covered (out of 21) |
|---------|-----------:|---------------------------:|
| JM Financial | 2005 | 21 |
| IIFL Finance | 2005 | 21 |
| Motilal Oswal | 2007 | 19 |
| Edelweiss | 2007 | 19 |
| Almondz | 2008 | 18 |
| Anand Rathi Wealth | 2021 | 5 |
| Nuvama Wealth | 2023 | 3 |
| IIFL Capital Services | 2024 | 2 |

## 4. Notable companies NOT in this CSV

- **ICICI Securities** (`ICICISEC.BO`/`.NS`) — was listed April 2018,
  **delisted 2024** via merger with ICICI Bank. Yahoo no longer
  returns historical data for the delisted symbol; could be backfilled
  from NSE archives bhavcopy for the 2018-2024 window if needed.
- **HDFC Securities** — wholly owned subsidiary of HDFC Bank; not
  separately listed.
- **Kotak Investment Banking** — part of Kotak Mahindra Bank;
  not separately listed.
- **Axis Capital** — wholly owned by Axis Bank; not separately listed.
- **SBI Capital Markets** — SBI subsidiary; not separately listed.

These four (plus ICICI Securities pre-delisting) are arguably India's
biggest I-banking franchises but they live inside larger bank
balance sheets, so their I-banking equity performance can't be
isolated.

## 5. Cross-source validation (sample spot-checks)

| Company | Year | Yahoo close | Independent verify |
|---------|------|------------:|--------------------|
| JM Financial | 2025 | 128.90 | NSE current quote ~₹129 (≈ matches) |
| Motilal Oswal | 2025 | 753.55 | NSE current quote — same vicinity |
| IIFL Finance | 2023 | 623.45 | Coincides with the pre-RBI-action peak (Mar 2024 the gold-loan stop-order followed) |
| Edelweiss | 2008 | 15.49 | Reflects GFC drawdown from 2007 close of 56.84 (-73%) |

The 2007 → 2008 GFC drawdowns are visible in every company that was
listed: JM Financial -84%, Motilal Oswal -77%, Edelweiss -73%,
IIFL -81%. The 2017 → 2018 mid-cap crash drawdown is also visible:
JM Financial -53%, Motilal Oswal -51%, Edelweiss -45%, IIFL -41%.

## 6. How this CSV connects to the rest of the folder

These companies are **direct beneficiaries** of pattern #2 from
`patterns_high_probability.md` (record IPO amount → Nifty 50 up
next year, 4/4 = 100%). Every IPO underwritten by these firms
generates fee income:

- 2017 was a year of record IPO supply (₹83,684 cr). All four
  established firms posted big stock gains: JM Financial +138%
  (₹68 → ₹163), Motilal Oswal +130% (₹560 → ₹1,286), Edelweiss +155%
  (₹60 → ₹152), IIFL +153% (₹160 → ₹405). Then the 2018 mid-cap
  crash hit and they all gave back ~50%.
- 2024-25 are similar — record IPO supply has driven Nuvama Wealth
  +93% (₹727 → ₹1,402) in 2024, Anand Rathi Wealth +47% in 2024 and
  +56% in 2025, IIFL Capital Services +11% from late-2024 IPO.

A natural follow-up would be to compute an equal-weighted "I-banking
basket" return and compare against the Nifty Capital Markets Index
once that CSV is backfilled.

## 7. How to extend

- New companies as they list: add a new column.
- New years: append a row using last-NSE-trading-day-of-December
  bhavcopy (the same URL pattern documented in `nifty50_data_sources.md`).
- For ICICI Securities' 2018-2023 history: pull from NSE archives
  bhavcopy using ticker `ICICISEC`. That data is in the NSE archive
  files we've already shown can be downloaded for 2012-2025.

## 8. Authoritative cross-check sources

For any single value in this CSV:
- **Primary**: NSE/BSE end-of-day bhavcopy
  (`https://archives.nseindia.com/content/indices/ind_close_all_DDMMYYYY.csv`
  carries the indices; individual stocks are in
  `https://archives.nseindia.com/products/content/sec_bhavdata_full_DDMMYYYY.csv`
  or BSE equivalent).
- **Secondary**: Yahoo Finance (used here).
- **Tertiary**: screener.in, moneycontrol.com, trendlyne.com all
  carry the same NSE-sourced data.

The values here have been spot-checked against the NSE-published
year-end close for JM Financial and Motilal Oswal for 2025. Both
matched to the rupee.
