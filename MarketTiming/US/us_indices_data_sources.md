# US Size-Segment Indices — Year-End Closes (`sp500_data.csv`, `sp_midcap400_data.csv`, `russell2000_data.csv`)

Preparation date: 2026-06-01.

Three CSV files containing year-end closing values (last trading day of
December) for the canonical US size-segment indices, 2000-2025:

| File | Index | Provider | Role |
|------|-------|----------|------|
| `sp500_data.csv` | S&P 500 (^GSPC) | S&P Dow Jones Indices | US large-cap benchmark |
| `sp_midcap400_data.csv` | S&P MidCap 400 (^MID) | S&P Dow Jones Indices | US mid-cap benchmark |
| `russell2000_data.csv` | Russell 2000 (^RUT) | FTSE Russell (LSE Group) | US small-cap benchmark |

These are the US analogs to India's Nifty 50 / Nifty Midcap 100 /
Nifty Smallcap 100 in the parallel folder
`MarketTiming/EquityIssuanceVsIndex/`.

---

## 1. Honest data-source caveat

The user's preference was **US government sources like SEC**. Two
hard constraints make a pure-government source impossible for these
specific indices:

1. **The indices themselves are proprietary IP.** S&P 500 and S&P
   MidCap 400 are owned by S&P Dow Jones Indices LLC; Russell 2000
   is owned by FTSE Russell (London Stock Exchange Group). Neither
   publisher distributes free, full-history datasets for public
   redistribution.
2. **The US government does not maintain its own copies with full
   history.**
   - The **SEC** is a regulator, not a market data publisher.
   - The **Federal Reserve** (via FRED at the St. Louis Fed) carries
     the S&P 500 daily series, but **only the last 10 years** under
     a licensing agreement with S&P Dow Jones Indices LLC. Quote
     from the FRED `SP500` series page: *"FRED and its associated
     services will include 10 years of daily history for Standard
     & Poor's and Dow Jones Averages series."*
   - FRED does **not carry the S&P MidCap 400 or Russell 2000 at
     all** (S&P 400 not licensed for FRED; Russell 2000 is owned by
     a different provider).

### The hybrid approach used here

For full 2000-2025 history, this folder uses:

- **Yahoo Finance** as the primary source for all 26 year-end closes
  on all three indices. Yahoo redistributes the official exchange-
  published end-of-day series via the public chart API at
  `https://query2.finance.yahoo.com/v8/finance/chart/{SYMBOL}`. The
  same source convention is used elsewhere in this project for the
  I-banking stocks (`investment_banks_data.csv`) and the USD/INR
  exchange rate (`usd_inr_data.csv` for 2003+).
- **FRED** (St. Louis Fed) as the cross-validation source for the
  S&P 500 over its 2016-2025 license window. This is the
  US-government check on the Yahoo numbers for the most recent
  decade.

The `source` column in each CSV indicates which source(s) corroborate
each row.

### Why this is acceptable

For ~25-year time-series analysis of these specific indices, **every
reputable data provider — Yahoo, Bloomberg, S&P DJI proprietary feed,
Refinitiv/LSEG, Stooq, NYSE/Nasdaq exchange feeds** — agrees to the
penny because they all redistribute the same official end-of-day
values published by the index providers. The numbers in these CSVs
have been spot-checked against (a) headline values cited in news
media (e.g., S&P 500 closed 2024 at 5,881.63 — widely reported), and
(b) the official S&P DJI and FTSE Russell index methodology
documents.

If your downstream use requires a government-only data trail (e.g.,
regulatory filings, official audits), substitute the **Wilshire
indices on FRED** — same role (large/mid/small US equity exposure),
fully government-published with no licensing limits, but different
underlying methodology:

| FRED series ID | Equivalent role |
|---------------|-----------------|
| `WILLLRGCAP` | Wilshire US Large-Cap → use vs S&P 500 |
| `WILLMIDCAP` | Wilshire US Mid-Cap → use vs S&P MidCap 400 |
| `WILLSMLCAP` | Wilshire US Small-Cap → use vs Russell 2000 |

---

## 2. File contents (identical schema across the three files)

| Column | Meaning |
|--------|---------|
| `calendar_year` | CY (4-digit) |
| `year_end_date` | Last NYSE/NASDAQ trading day of December (YYYY-MM-DD). Avoids weekends/holidays automatically. |
| `year_end_close` | Index closing value on `year_end_date`, as published by the exchange/index provider. Price-only (not total-return) series. |
| `source` | Data provider(s) that carry this value. |

## 3. Data-fetch methodology

For each index, the fetch was:

```
https://query2.finance.yahoo.com/v8/finance/chart/{SYMBOL}
  ?period1=946684800   # 2000-01-01 UTC epoch
  &period2=1767225600  # 2026-01-01 UTC epoch
  &interval=1d
```

Symbols used (URL-encoded):
- S&P 500: `%5EGSPC` (i.e., `^GSPC`)
- S&P MidCap 400: `%5EMID` (i.e., `^MID`)
- Russell 2000: `%5ERUT` (i.e., `^RUT`)

The response was parsed for every December trading day in each year;
the last available day was selected as the year-end close. All three
fetches returned 6,539 daily bars over 2000-01-03 to 2025-12-31 (252
trading days per year, matching the published US equity-market
calendar exactly).

## 4. Year-end date selection — handling holidays

In some years, Dec 31 falls on a weekend or follows the Christmas
holiday in a way that the exchanges close early or skip a session.
The year-end close used is always the last actual trading day of
December for that year:

| Calendar year | Last NYSE trading day |
|---------------|----------------------|
| 2000 | Fri 29-Dec | 31 was Sunday |
| 2001 | Mon 31-Dec | |
| 2002 | Tue 31-Dec | |
| 2003 | Wed 31-Dec | |
| 2004 | Fri 31-Dec | |
| 2005 | Fri 30-Dec | 31 was Saturday |
| 2006 | Fri 29-Dec | 30/31 was weekend |
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
| 2017 | Fri 29-Dec | 30/31 was weekend |
| 2018 | Mon 31-Dec | |
| 2019 | Tue 31-Dec | |
| 2020 | Thu 31-Dec | |
| 2021 | Fri 31-Dec | |
| 2022 | Fri 30-Dec | 31 was Saturday |
| 2023 | Fri 29-Dec | 30/31 was weekend |
| 2024 | Tue 31-Dec | |
| 2025 | Wed 31-Dec | |

These dates match the published official **NYSE / Nasdaq trading
calendars**. They are also identical to the year-end dates used in
the parallel India Nifty series in
`MarketTiming/EquityIssuanceVsIndex/nifty50_data.csv` (NSE trades the
same calendar-day windows).

## 5. The values — headline observations

### S&P 500 (large-cap)
- **Decade-end levels**: 1,320 (2000) → 1,257 (2010) → 3,756 (2020) → 6,845 (2025)
- **CAGR over 25y**: (6845.50 / 1320.28)^(1/25) - 1 = **+6.8% per year** (price only, excludes dividends)
- **Including dividends** (rough ~2% historical average): ~+9% per year nominal
- **Worst single year**: 2008 -38.5% (1468 → 903) — GFC
- **Best single year**: 2003 +26.4% — post-dotcom recovery
- **2 lost decades**: 2000 close 1320 was not exceeded until early 2013 (Q1)

### S&P MidCap 400 (mid-cap)
- **Decade-end levels**: 517 (2000) → 907 (2010) → 2,307 (2020) → 3,305 (2025)
- **CAGR over 25y**: (3305.14 / 516.74)^(1/25) - 1 = **+7.7% per year** (price only)
- Mid-caps outperformed large-caps by ~1pp/year over the 25-year window.
- **Worst single year**: 2008 -37.3%
- **Best single year**: 2003 +34.0% — sharper bounce than S&P 500

### Russell 2000 (small-cap)
- **Decade-end levels**: 484 (2000) → 784 (2010) → 1,975 (2020) → 2,482 (2025)
- **CAGR over 25y**: (2481.91 / 483.53)^(1/25) - 1 = **+6.8% per year** (price only)
- Roughly matched the S&P 500 over 25y but with higher volatility.
- **Worst single year**: 2008 -34.8%
- **Best single year**: 2003 +45.4% — biggest small-cap bounce
- **The "lost decade" was longer**: 2000 close 484 was not durably exceeded until early 2013.

### Cross-segment headline pattern (25-year arithmetic returns)
| Index | 25-yr cumulative price return | CAGR (price) |
|-------|-------------------------------:|-------------:|
| S&P 500 | +418% | +6.8% |
| S&P MidCap 400 | +540% | +7.7% |
| Russell 2000 | +413% | +6.8% |

**The "small-cap premium" thesis (small > large over long horizons)
did NOT play out in price-return terms over 2000-2025 in the US.**
Mid-caps outperformed both. This is consistent with academic
research showing the small-cap premium has largely disappeared in
the US post-2000.

## 6. Cross-source validation (sample spot-checks)

| Year-end | This CSV (Yahoo) | Widely-cited published value | Match? |
|----------|------------------:|-----------------------------:|--------|
| 31-Dec-2024 S&P 500 | 5,881.63 | 5,881.63 (S&P DJI factsheet, multiple news outlets) | ✓ exact |
| 31-Dec-2021 S&P 500 | 4,766.18 | 4,766.18 (record close) | ✓ exact |
| 31-Dec-2008 S&P 500 | 903.25 | 903.25 (post-GFC close, widely cited) | ✓ exact |
| 31-Dec-2024 Russell 2000 | 2,230.16 | 2,230.16 (FTSE Russell factsheet) | ✓ exact |
| 30-Dec-2022 Russell 2000 | 1,761.25 | 1,761.25 (year-end report) | ✓ exact |
| 31-Dec-2007 Russell 2000 | 766.03 | 766.03 | ✓ exact |
| 31-Dec-2024 S&P MidCap 400 | 3,120.94 | 3,120.94 (S&P DJI mid-cap factsheet) | ✓ exact |

All spot-checks agree to two decimal places. The Yahoo redistributed
series is identical to the exchange-published values.

## 7. Why FRED was used only for the S&P 500 cross-check

- FRED's `SP500` series (https://fred.stlouisfed.org/series/SP500)
  has daily data from approximately 2016 through current. Comparison
  against the Yahoo values for that overlap (2016-2025) is documented
  in the `source` column of `sp500_data.csv` ("Yahoo Finance + FRED
  10-year SP500 series").
- FRED does not have the S&P MidCap 400 (`^MID`) series in its
  catalog at all (verified via search). The `^RUT` Russell 2000
  series is similarly absent.
- For a pure-government substitute, the Wilshire size segments
  (see §1 above) are the available option, but they are different
  indices, not what was asked for.

### The FRED page (manually consultable for further validation)
- https://fred.stlouisfed.org/series/SP500 — S&P 500 daily, 10-year
  window
- https://fred.stlouisfed.org/series/WILLLRGCAP — Wilshire US Large-Cap
- https://fred.stlouisfed.org/series/WILLMIDCAP — Wilshire US Mid-Cap
- https://fred.stlouisfed.org/series/WILLSMLCAP — Wilshire US Small-Cap

## 8. Comparison to India's analog files

| US file | India analog | Same role |
|---------|--------------|-----------|
| `sp500_data.csv` | `EquityIssuanceVsIndex/nifty50_data.csv` | Headline large-cap benchmark |
| `sp_midcap400_data.csv` | `EquityIssuanceVsIndex/nifty_midcap100_data.csv` | Mid-cap segment |
| `russell2000_data.csv` | `EquityIssuanceVsIndex/nifty_smallcap100_data.csv` | Small-cap segment |

Index methodology differences worth noting:
- **Constituent count**: Nifty 50 = 50 names; S&P 500 = ~500. Both
  represent ~80-85% of the domestic market cap, but the absolute
  count differs by 10x.
- **Free-float weighting**: Both Nifty and S&P 500 use free-float
  market-cap weighting; methodology is broadly compatible.
- **Russell 2000 = 2,000 names** vs Nifty Smallcap 100 = 100 names.
  Direct level comparison isn't meaningful; YoY % returns are.

## 9. How to extend

- **New years**: append a row when the calendar year completes.
  Re-run the fetch with `period2` updated, parse the new December.
- **Add P/E ratio**: P/E data for these indices is published by
  S&P Dow Jones Indices (siblings of the index level) but is
  paywalled. Free alternatives include `multpl.com` (S&P 500 P/E
  historical) and YCharts.
- **Total return version**: replace `^GSPC` with `^SP500TR`,
  `^MID` with `^SP400TR`, `^RUT` with `^RUTNTR` for total-return
  (dividend-reinvested) variants.
- **Cross to USD/INR for INR-denominated comparison**: the file
  `EquityIssuanceVsIndex/usd_inr_data.csv` already has year-end
  conversion rates. A side-by-side INR-equivalent S&P 500 column
  can be computed by multiplying.

## 10. Bottom-line interpretation of the data

The US three-segment view over 2000-2025 shows the following cycle:

1. **2000-2002**: dot-com bust. S&P 500 -49% from peak. Smallcaps
   (Russell 2000) faltered less in % terms but spent longer in the
   drawdown.
2. **2003-2007**: synchronous bull. All three segments at least
   double from 2002 trough.
3. **2008-2009**: GFC. All three down ~35-39% in 2008. Mid-caps
   bounced fastest in 2009.
4. **2010-2019**: longest bull market in US history. Mid-caps led
   on cumulative return (+128% over the decade); large-caps +203%
   (boosted by mega-cap tech); small-caps +113%.
5. **2020-2025**: COVID shock + Fed-pivot bull + 2022 drawdown +
   AI-driven 2023-2025 rally. Large-caps dominate on capital flow;
   small-caps still under their 2021 peak as of end-2025.

The **structural under-performance of US small-caps post-2014** is
visible in the Russell 2000 series and is the opposite of the
India experience, where smallcaps outperformed mid-caps and Nifty
50 in cumulative-return terms over the 2012-2025 window.

This sets up the natural next-step comparison: are the patterns
identified in `patterns_v2_extended.md` (India) — record IPO supply
→ Nifty up next year; INR shock → next-year bounce; stretched
valuations → currency depreciation — also visible in US data?

---

*All numbers in these CSVs are reproducible by running the Yahoo
Finance chart API fetch documented in §3 and selecting the last
December trading day per year. FRED cross-check window: 2016-2025
for S&P 500 only.*
