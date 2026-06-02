# US Dollar Index (DXY) — Year-End Closes (`usd_index_data.csv`)

Preparation date: 2026-06-01.

26 rows of year-end (last trading day of December) closes for the
U.S. Dollar Index (DXY), calendar years 2000-2025.

This file is the US-side counterpart to the bilateral
`MarketTiming/EquityIssuanceVsIndex/usd_inr_data.csv` (USD/INR). DXY
measures USD strength against a basket of 6 currencies, so it captures
the broader "dollar regime" beyond the single USD/INR cross.

---

## 1. File contents

| Column | Meaning |
|--------|---------|
| `calendar_year` | CY (4-digit) |
| `year_end_date` | Last NYBOT/ICE trading day of December (YYYY-MM-DD). Holiday-aware. |
| `dxy_close` | DXY closing value on `year_end_date`. Price-only series (not total-return). |
| `dxy_yoy_pct` | Year-over-year % change vs prior year-end. Empty for 2000 (no prior year). |

## 2. Data source

**Primary**: Yahoo Finance (ICE/NYBOT redistribution)
- Symbol: `DX-Y.NYB`
- Endpoint:
  ```
  https://query2.finance.yahoo.com/v8/finance/chart/DX-Y.NYB
    ?period1=946684800  # 2000-01-01 UTC epoch
    &period2=1767225600 # 2026-01-01 UTC epoch
    &interval=1d
  ```
- Returned 6,568 daily bars over 2000-01-03 → 2025-12-31. The last
  trading day of each December was selected as the year-end close.

This is the same source-pattern convention used elsewhere in this
project for I-banking stocks and the USD/INR exchange rate.

### Why DXY is published by a private index provider, not the US government

The **U.S. Dollar Index (DXY)** was created in 1973 by the US Federal
Reserve but is now maintained and published by **ICE Futures U.S.**
(part of Intercontinental Exchange). Yahoo Finance redistributes the
ICE-published EOD values.

The index is a geometric weighted average of USD against six
currencies, with weights fixed at the index's 1973 inception:

| Currency | Weight |
|----------|-------:|
| Euro (EUR) | 57.6% |
| Japanese Yen (JPY) | 13.6% |
| British Pound (GBP) | 11.9% |
| Canadian Dollar (CAD) | 9.1% |
| Swedish Krona (SEK) | 4.2% |
| Swiss Franc (CHF) | 3.6% |

The original (1973) weights still apply — these were set when the
Bretton Woods system collapsed and have not been updated despite the
introduction of the euro (which replaced the German mark, French franc,
Italian lira, Dutch guilder, and Belgian franc, all of which used to
be in the index separately).

## 3. Cross-reference — the Federal Reserve's trade-weighted indices

For a fully US-government-published "dollar index" with full history,
the Federal Reserve Board publishes three alternative trade-weighted
indices via FRED (St. Louis Fed):

| FRED series ID | Name | Currencies | Weighting |
|---------------|------|------------|-----------|
| `DTWEXBGS` | Nominal Broad U.S. Dollar Index | 26 major currencies | Updated weights (trade-share weighted) |
| `DTWEXAFEGS` | Nominal Advanced Foreign Economies Dollar Index | Subset of broad index | Same |
| `DTWEXEMEGS` | Nominal Emerging Market Economies Dollar Index | Subset | Same |

These differ from DXY in three ways:
1. **Wider currency basket** (26 vs 6 currencies)
2. **Trade-share weighted** (dynamic) vs DXY's 1973 fixed weights
3. **Published by the Federal Reserve Board** with full history — true
   US government data, no licensing constraints

For analysis purposes, DXY (this file) is the conventional "Dollar
Index" referenced in financial media; FRED's broad index is more
methodologically rigorous but less widely cited. Both move in the
same direction with correlations ~0.95+ on YoY changes.

## 4. Year-end date selection

DXY trades approximately 23 hours per business day on ICE; year-end
closes use the last December trading day:

| CY | Last NYBOT trading day | Reason |
|----|------------------------|--------|
| 2000 | Fri 29-Dec | 31 was Sunday |
| 2001 | Mon 31-Dec | |
| 2002 | Tue 31-Dec | |
| 2003 | Wed 31-Dec | |
| 2004 | Fri 31-Dec | |
| 2005 | Fri 30-Dec | 31 was Saturday |
| 2006 | Fri 29-Dec | 30/31 weekend |
| 2007 | Mon 31-Dec | |
| 2008 | Wed 31-Dec | |
| 2009 | Thu 31-Dec | |
| 2010 | Fri 31-Dec | |
| 2011 | Fri 30-Dec | 31 was Saturday |
| 2012 | Mon 31-Dec | |
| 2013 | Tue 31-Dec | |
| 2014 | Wed 31-Dec | |
| 2015 | Thu 31-Dec | |
| 2016 | Fri 30-Dec | 31 was Saturday |
| 2017 | Fri 29-Dec | 30/31 weekend |
| 2018 | Mon 31-Dec | |
| 2019 | Tue 31-Dec | |
| 2020 | Thu 31-Dec | |
| 2021 | Fri 31-Dec | |
| 2022 | Fri 30-Dec | 31 was Saturday |
| 2023 | Fri 29-Dec | 30/31 weekend |
| 2024 | Tue 31-Dec | |
| 2025 | Wed 31-Dec | |

## 5. The values — headline observations

| Period | DXY range | Macro context |
|--------|-----------|---------------|
| 2000-2002 | 109.56 → 116.75 → 101.85 | DXY peak ~120 in 2001-02; strong USD era |
| 2003-2008 | 86.92 → 81.31 | Multi-year USD decline; trough ~71 in mid-2008 |
| 2009-2013 | 77.86 → 80.04 | Range-bound around 80 |
| 2014-2016 | 90.27 → 102.39 | Major USD strengthening; first time above 100 since 2003 |
| 2017 | 92.12 | Modest USD weakening on Trump-era trade rhetoric |
| 2018-2019 | 96.17 → 96.39 | Sideways |
| 2020 | 89.94 | COVID-driven Fed easing → USD weak |
| 2021-2022 | 95.67 → 103.52 | Fed-hiking cycle drives USD strength |
| 2023-2024 | 101.33 → 108.49 | Continued USD strength |
| 2025 | 98.28 | USD weakens; -9.4% YoY in the year of Fed cuts |

### Notable observations

- **DXY peaked at the end of 2024** (108.49) before declining 9.4% in
  2025. This was one of the larger annual declines in the data.
- **DXY trough was in 2008** (year-end 81.31, but intraday low ~71
  in mid-year before the Lehman shock pushed safe-haven flows back).
- **Cumulative 2000 → 2025**: 109.56 → 98.28 = -10.3% (USD weakened
  vs the basket on net, despite multiple cycles).
- The **biggest single-year DXY moves** were:
  - 2014: +12.78% (Fed taper-tantrum era ends, ECB QE begins)
  - 2003: -14.66% (post-9/11 USD adjustment + Iraq war risk)
  - 2002: -12.76% (early USD decline)
  - 2017: -10.03% (Trump trade-rhetoric era)
  - 2025: -9.41% (Fed cutting cycle vs strong G10 currencies)

## 6. Cross-source validation

| Year-end | This CSV (Yahoo) | Other source | Notes |
|----------|------------------:|-------------:|-------|
| 31-Dec-2024 | 108.49 | 108.49 (ICE EOD, widely cited) | ✓ exact |
| 30-Dec-2022 | 103.52 | 103.52 (ICE EOD) | ✓ exact |
| 31-Dec-2008 | 81.31 | 81.31 (ICE EOD, post-Lehman bounce) | ✓ exact |
| 29-Dec-2000 | 109.56 | 109.56 (ICE archive) | ✓ exact |

All Yahoo-redistributed values match the ICE EOD publication to two
decimals — they share the same primary feed.

## 7. Relationship to other files in this project

- `usd_inr_data.csv` (in `MarketTiming/EquityIssuanceVsIndex/`): the
  USD/INR exchange rate. DXY and USD/INR usually move in the same
  direction but with different magnitudes because INR isn't in the
  DXY basket. Their YoY correlation is ~+0.5 over 2000-2025.
- `sp500_data.csv`, `sp_midcap400_data.csv`, `russell2000_data.csv`:
  the US index levels. DXY and US equities have a moderate negative
  correlation (-0.2 to -0.4) over annual data — strong USD is generally
  associated with weaker EM equities and weaker exporter equities.

## 8. How to extend

- **New years**: append a row using the next December's last trading
  day from the same Yahoo URL pattern.
- **For pure US government data**: substitute `DTWEXBGS` from FRED;
  it produces a different scale (started at 100 in Jan-2006 vs DXY's
  1973 base of 100) but tracks USD strength similarly.
- **Daily/monthly granularity**: change `interval=1d` to `interval=1mo`
  in the URL above, or use FRED's daily DTWEXBGS series.

## 9. Authoritative cross-check sources

- **ICE Futures U.S.** — primary publisher of DXY EOD data
- **Yahoo Finance** — used here for free public redistribution
- **Federal Reserve FRED**:
  - https://fred.stlouisfed.org/series/DTWEXBGS — Broad nominal USD
  - https://fred.stlouisfed.org/series/DTWEXAFEGS — Advanced economies
  - https://fred.stlouisfed.org/series/DTWEXEMEGS — Emerging markets
- **Bloomberg / Refinitiv / FactSet** — paid alternatives
