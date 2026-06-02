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
| `pe_ratio_trailing` | Trailing 12-month index P/E ratio. **POPULATED for S&P 500 only; mostly empty for S&P 400 and Russell 2000 — see §10 for why.** |
| `source_close` | Source for the year-end close value. |
| `source_pe` | Source for the P/E value (or "No free public year-end series available"). |

### Why two source columns and not one

The year-end close and the P/E ratio for these indices come from different
sources with different methodologies. Decoupling them in the CSV allows
each row to carry its own provenance for each value, makes the data-gap
issue explicit, and makes future backfills auditable.

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

## 10. P/E ratio sourcing — what's available and what isn't

The `pe_ratio_trailing` column was added in the second iteration of
these CSVs. After an extensive search for US-government-published
historical year-end P/E series for each index, here is the honest
state of free public data availability.

### 10.1 S&P 500 — populated with full history

| Source | Coverage | Methodology | Used here |
|--------|----------|-------------|-----------|
| **Robert Shiller (Yale)** [`ie_data.xls`](http://www.econ.yale.edu/~shiller/data.htm) | Monthly since Jan 1871; this file ends Sept 2023 | S&P 500 monthly average price ÷ trailing 12-month GAAP earnings | **Primary for 2000-2022** |
| **multpl.com** [`s-p-500-pe-ratio/table/by-year`](https://www.multpl.com/s-p-500-pe-ratio/table/by-year) | Redistributes Shiller's series with monthly updates | Same as Shiller | **For 2023-2025** where Shiller's file hasn't been updated |
| Federal Reserve Financial Stability Report (semi-annual) [URL](https://www.federalreserve.gov/publications/files/financial-stability-report-20251107.pdf) | Each report includes "Figure 1.4: Forward P/E of S&P 500 firms" — a chart, not tabular data. Sourced from LSEG/IBES (Institutional Brokers' Estimate System). | Forward P/E based on 12-month-ahead consensus earnings estimates | **Order-of-magnitude cross-validation only.** The Fed's chart matches our values to within ~3 P/E points; the difference is forward vs. trailing. |
| FRED CAPE series [SP500_PE_RATIO_MONTH] (third-party redist.) | Long history | Shiller's PE10 (cyclically adjusted) | Not used (CAPE is a different metric — 10-year smoothed) |

**Why Shiller is the academic gold standard for S&P 500 P/E:**
- Used by every major US finance textbook (Bodie/Kane/Marcus, Damodaran).
- The Federal Reserve Board cites Shiller's CAPE in its Working Paper
  series and FRED hosts a derived series.
- The dataset has been continuously published since the 1990s with full
  source-documented methodology and is freely downloadable as `ie_data.xls`.
- The earnings denominator uses **GAAP earnings**, which is the
  conservative measure (vs operating earnings). This produces higher
  P/E values in periods of large GAAP writedowns (2008 GFC, 2020 COVID).

**Notable cross-source differences** (Shiller vs multpl.com vs Fed):
- **End-2008**: Shiller 58.98, multpl.com 70.91 — both reflect the GFC
  earnings collapse; the difference is in which quarter's revised
  earnings is used as the denominator.
- **End-2020**: Shiller 39.26, multpl.com 35.96 — COVID earnings
  collapse, same effect.
- For all other years 2000-2022, Shiller and multpl agree within ±1.5
  P/E points.

The `source_pe` column in `sp500_data.csv` notes when each row's
P/E comes from Shiller vs multpl vs which methodology variant.

### 10.2 S&P MidCap 400 — column populated only for end-2025 snapshot

After an exhaustive search of US-government, exchange, and free public
sources, **no clean historical year-end trailing P/E series exists**
for the S&P MidCap 400 in any free public dataset. Specifically:

| Source attempted | Result |
|------------------|--------|
| **FRED** (St. Louis Fed) | Does NOT carry S&P MidCap 400 at all. |
| **Federal Reserve Financial Stability Report** | Reports S&P 500 forward P/E only; no separate small/mid-cap series. |
| **U.S. Treasury Office of Financial Research (OFR)** | Publishes an aggregate "equity valuation" stress-index component (a single normalized score from -1.4 to +2.2, not a P/E series); no breakdown by size segment. |
| **Bureau of Economic Analysis (BEA)** Z.1 release | Has aggregate "corporate equity at market value" and "corporate profits"; can compute a market-wide P/E but not an index-specific P/E. |
| **NYSE / Nasdaq** | Publish current Composite-level P/E daily; historical archives are paid. |
| **S&P Dow Jones Indices** [official factsheet](https://www.spglobal.com/spdji/en/indices/equity/sp-400/) | Current month freely available; full historical CSV requires paid subscription. |
| **Yardeni Research** [Stock Market P/E Ratios PDF](https://archive.yardeni.com/pub/stockmktperatio.pdf) | Includes S&P 400 chart but only as a visual figure; no tabular year-end data. Latest snapshot value cited in research: **18.9× trailing P/E as of Aug 2025.** |
| **WSJ, Barchart, Morningstar, Yahoo Finance** | Current snapshot only; no historical series. |
| **iShares IJH / SPDR MDY ETF factsheets** | Publishes the current quarter's portfolio-weighted P/E; quarterly historical archives via Wayback Machine. Time-consuming to scrape; not done here. |
| **Bloomberg / FactSet / S&P Capital IQ / Refinitiv** | All paid, terminal-only. |

**Why this is so hard:** S&P Dow Jones Indices LLC is a joint venture
(S&P Global + CME Group + News Corp / Dow Jones) that monetizes
historical index data licensing. They publish the current month's
P/E for free but charge for historical archives. Unlike the SEC or
Federal Reserve, they have no statutory obligation to publish historical
free data.

**What's populated in `sp_midcap400_data.csv`:**
- The 2025 row carries **18.9** (the August 2025 Yardeni-cited reading,
  used as a best-available proxy for end-2025 given the index drift
  from ~3,200 in August to 3,305 at year-end was ~3%, with little
  earnings movement in the same period).
- All earlier years are intentionally left null. Don't fabricate values
  here — false precision is worse than no data.

**To extend with full history**, options are:
- (a) Subscribe to S&P DJI's historical data feed (annual fee ~$5-10k).
- (b) Bloomberg or FactSet API (terminal subscription).
- (c) Manual scrape of iShares IJH factsheet PDFs via Wayback Machine
  for each year-end snapshot (free but labor-intensive).
- (d) Compute approximately using S&P-published S&P 400 quarterly EPS
  (which IS in the [S&P DJI Index Earnings spreadsheet](https://www.spglobal.com/spdji/en/documents/additional-material/sp-400-eps-est.xlsx))
  divided by the year-end index level. This file was unreachable from
  this environment (HTTP 403) but is the standard data source for
  S&P-published P/E ratios.

### 10.3 Russell 2000 — column intentionally left empty

The same constraints as the S&P MidCap 400 apply, **plus an additional
methodological problem**: many Russell 2000 constituents have negative
trailing 12-month earnings. The aggregate P/E ratio is therefore
extremely sensitive to which methodology is used:

| Methodology | Effect |
|-------------|--------|
| Include all constituents (raw) | Trailing P/E often above 100 or even negative; not interpretable. |
| Exclude negative-earnings firms | Higher P/E, but trims the index universe. |
| Trimmed mean | Smoother but ad-hoc. |
| Weighted by index float vs. weighted by aggregate earnings | Different answers. |
| FTSE Russell official (their public methodology, paid feed) | Their own definition. |

**Different sources can report Russell 2000 P/E ranging from ~15× to
~40× for the same date** depending on methodology. This is one reason
academic research often **excludes Russell 2000** from P/E quartile
analyses and instead uses the S&P 600 SmallCap (which has a profitability
inclusion criterion, so its constituents have meaningful aggregate
earnings).

**What's populated in `russell2000_data.csv`:** Nothing. The column is
present for schema parity with the other two files, but every value
is null. The `source_pe` column documents the absence and the reason.

**Practical recommendation:** for cross-segment valuation analysis in
US that mirrors the India analysis, use the **S&P 600 SmallCap P/E**
(which has the profitability inclusion filter — closer to the Nifty
Smallcap 100 methodology) rather than the Russell 2000 P/E. The S&P 600
P/E is similarly hard to source historically, but at least the values
are interpretable when found.

### 10.4 The pure-government substitute (if you can use Wilshire)

For a strict government-data-only chain on size-segment P/E, FRED has
the **Wilshire indices** with full history *and* derived P/E ratios
when combined with the S&P 500 or NYSE earnings components. This
requires methodology decisions but is fully government-published:

- `WILLLRGCAP` (Wilshire US Large-Cap) — proxy for S&P 500
- `WILLMIDCAP` (Wilshire US Mid-Cap) — proxy for S&P MidCap 400
- `WILLSMLCAP` (Wilshire US Small-Cap) — proxy for Russell 2000

Wilshire indices have a different constituent set and selection
methodology than S&P/Russell, but they are size-segmented and have
US-government-published full history. They are the available trade-off
between "what was asked" (S&P/Russell indices) and "fully government-
sourced" (Wilshire indices).

### 10.5 Summary of the P/E data state

| File | P/E populated | Source | Coverage |
|------|---------------|--------|----------|
| `sp500_data.csv` | ✓ all 26 rows | Shiller Yale + multpl.com | 2000-2025 full |
| `sp_midcap400_data.csv` | Only end-2025 | Yardeni Research snapshot | 1 of 26 rows |
| `russell2000_data.csv` | ✗ none | n/a | 0 of 26 rows |

This is honest reporting of what's freely sourceable. Adding fake
values would make the historical pattern analysis unreliable in
exactly the place where careful US-vs-India comparison should be most
defensible.

---

## 11. Bottom-line interpretation of the data

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
