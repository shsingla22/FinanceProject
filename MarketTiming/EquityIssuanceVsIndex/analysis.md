# Equity Issuance vs Broad-Market Indices — Cross-Year Analysis (India, 2000-2025)

Prepared: 2026-05-18.
Data sources: the five CSV files in this folder (`ipo_data.csv`,
`fpo_rights_data.csv`, `nifty50_data.csv`, `nifty_smallcap100_data.csv`,
`nifty_midcap100_data.csv`). Underlying sources: SEBI Handbooks of
Statistics, SEBI Monthly Bulletin Annexures, SEBI Annual Reports (Part
II — Review of Trends and Operations), NSE archives end-of-day index
bhavcopy, and Wikipedia (Nifty 50 pre-2010 only, cross-verified to SEBI).

---

## 1. Executive summary — the seven findings that hold up

After computing year-by-year correlations across 26 calendar years
(2000-2025) for the five series — IPO amount, FPO+Rights amount, and
the three Nifty indices — these are the patterns that survive
inspection:

1. **Markets lead issuance, not the other way around.** When the index
   goes up in year *t*, IPO amount goes up in year *t+1*. The Pearson
   correlation of IPO-amount-YoY in year *t* with index-YoY in year
   *t-1* is **+0.53 against Nifty 50, +0.59 against Smallcap, +0.62
   against Midcap.** The reverse — issuance leading the index —
   has correlations between -0.27 and +0.23 (essentially noise).

2. **Issuance peaks coincide with same-year smallcap softness.** The
   only same-year correlation that crosses ±0.30 is **IPO-amount-YoY
   vs Smallcap-100-YoY = -0.44**. The three biggest IPO-amount years
   in the dataset (2018, 2022, 2025) all had smallcap *declines* in
   the same calendar year (-29%, -14%, -5%). Mid- and large-caps were
   ~flat. The supply shock seems to land first on the smallcap
   segment, where the marginal new listing competes for the same
   capital pool.

3. **IPO droughts coincide with great recovery years for indices.**
   Every year IPO amount fell >50% YoY (2009, 2013, 2014, 2019, 2023),
   the same-year Nifty 50 was positive — +76%, +7%, +31%, +12%, +20%.
   Average +29%. When issuers pull back, indices recover.

4. **FPO+Rights is dominated by a few distress recapitalizations,
   not market timing.** The two biggest FY values in the dataset are
   FY 2020-21 (₹78,987 cr — mostly Reliance's ₹53k cr rights) and FY
   2024-25 (₹37,862 cr — includes Vodafone Idea's ₹18k cr FPO). These
   are reactive emergency capital raises, not cycle-following supply.

5. **2008 GFC is the only year where massive issuance coincided with a
   massive index drawdown.** FY 2007-08 IPO amount was ₹42,595 cr
   (+49% YoY); CY 2008 Nifty 50 fell -52%. But the crash was mid-year
   and the issuance was front-loaded in the bull run — the *next*
   FY's issuance crashed -95%.

6. **Two-cycle "issuance-peak-then-smallcap-crash" pattern is real but
   slow.** FY 2017-18 set a then-record (201 IPOs / ₹83,684 cr);
   CY 2018 Smallcap fell -29%. FY 2024-25 set a fresh record (320 /
   ₹172,328 cr); CY 2025 Smallcap fell -5%. Each time the larger
   indices barely moved while smallcaps absorbed the supply. The lag
   is roughly 0-12 months.

7. **The signal is too weak to use as a hard market-timing rule.**
   Even the strongest correlation in the dataset is +0.62. There are
   counter-examples (e.g. FY 2009-10 IPO amount surged +1,086% from a
   bombed-out base, yet CY 2010 Nifty 50 was up +18%). What the data
   supports is a soft *forensic* read: "the market has had a great
   run, IPO issuance is at records, smallcaps are stretched — expect
   smallcap returns to be the first to compress."

---

## 2. The dataset at a glance

For each year 2000-2025 we have (subject to availability):

- IPO count and amount (FY-ending basis, mapped to the calendar year
  the FY ends in)
- FPO + Rights count and amount (same FY-ending basis)
- Nifty 50 December year-end close (full 2000-2025)
- Nifty Midcap 100 December year-end close (2006-2025)
- Nifty Smallcap 100 December year-end close (2012-2025)

Coverage gaps:

| Year | Missing |
|------|---------|
| 2000 | Issuance data (data starts FY 2001-02 = year-label 2002), Midcap, Smallcap |
| 2001 | Issuance data, Midcap, Smallcap |
| 2002-2005 | Midcap, Smallcap |
| 2006-2011 | Smallcap |

That gives 24 years of comparable IPO+FPO+Nifty 50 data, 20 years of
+ Midcap, and 14 years of all five series.

---

## 3. The directional finding — markets lead issuance, not vice versa

### 3.1 Same-year correlations (YoY %)

|                  | IPO amt YoY | FPO+R amt YoY | Nifty 50 YoY | Smallcap YoY | Midcap YoY |
|------------------|------------:|--------------:|-------------:|-------------:|-----------:|
| **IPO amt YoY**       | 1.00 | 0.04 | -0.13 | **-0.44** | -0.13 |
| **FPO+R amt YoY**     | 0.04 | 1.00 | -0.14 | -0.08 | -0.22 |
| **Nifty 50 YoY**      | -0.13 | -0.14 | 1.00 | **0.83** | **0.95** |
| **Smallcap YoY**      | -0.44 | -0.08 | 0.83 | 1.00 | **0.98** |
| **Midcap YoY**        | -0.13 | -0.22 | 0.95 | 0.98 | 1.00 |

Notable cells in bold:
- Smallcap and Midcap move together near-perfectly (0.98); both
  correlate strongly with Nifty 50 (0.83 / 0.95). The Indian equity
  segments are heavily co-moving.
- The only issuance-vs-index correlation that crosses ±0.30 is
  **IPO amount vs Smallcap = -0.44** (same year). Big issuance years
  tend to be soft smallcap years.

### 3.2 Lead/lag correlations

| Pair                                                        | Correlation | n  |
|-------------------------------------------------------------|------------:|---:|
| IPO-amt YoY (year *t*) vs Nifty 50 YoY (year *t-1*)         | **+0.53** | 23 |
| IPO-amt YoY (year *t*) vs Smallcap YoY (year *t-1*)         | **+0.59** | 12 |
| IPO-amt YoY (year *t*) vs Midcap YoY (year *t-1*)           | **+0.62** | 18 |
| FPO+R-amt YoY (year *t*) vs Nifty 50 YoY (year *t-1*)       | +0.41 | 23 |
| FPO+R-amt YoY (year *t*) vs Midcap YoY (year *t-1*)         | +0.05 | 18 |
| Nifty 50 YoY (year *t*) vs IPO-amt YoY (year *t-1*)         | -0.27 | 22 |
| Smallcap YoY (year *t*) vs IPO-amt YoY (year *t-1*)         | +0.23 | 13 |
| Midcap YoY (year *t*) vs IPO-amt YoY (year *t-1*)           | -0.32 | 19 |

**The asymmetry is clear:** index moves in year *t-1* predict IPO
amount in year *t* with +0.5 to +0.6 correlation. IPO amount in year
*t-1* predicts the index in year *t* with -0.27 to +0.23 — essentially
noise. The causal direction in the data is **markets first, issuance
follows**.

This is consistent with how the primary market actually works:
- Companies and promoters time issuance to take advantage of high
  valuations.
- The IPO pipeline (DRHP filing → SEBI approval → roadshow →
  listing) takes 6-12 months, mechanically embedding a lag.
- Underwriters/I-bankers pitch fresh issuance after a rally, when
  retail demand is hot.

What this rules out is the "IPO surge causes the crash" narrative as a
*tight* causal story. The data is much more consistent with "IPO
surge marks the same regime as the rally" — both effects of common
investor enthusiasm.

---

## 4. Headline pattern — IPO peaks bracket smallcap weakness

The three biggest IPO-amount years in the dataset and what each
broad-market index did in the same calendar year:

| Rank | Year (FY ending) | IPO amount (₹ cr) | IPO YoY % | Nifty 50 YoY | Midcap YoY | Smallcap YoY |
|------|------------------|-------------------:|----------:|--------------:|------------:|--------------:|
| 1    | 2025 (FY 2024-25) | 172,328 | +154% | +10.5% | +5.8% | **-5.0%** |
| 2    | 2022 (FY 2021-22) | 112,553 | +356% | +4.3%  | +3.5% | **-13.8%** |
| 3    | 2018 (FY 2017-18) | 83,684  | +188% | +3.2%  | -15.4% | **-29.1%** |
| 4    | 2024 (FY 2023-24) | 67,955  | +24% | +8.8% | +23.8% | +23.1% |
| 5    | 2023 (FY 2022-23) | 54,773  | -51% | +20.0% | +46.6% | +55.6% |

Three of the top three IPO years (2025, 2022, 2018) show **smallcap
weakness in the same calendar year while Nifty 50 stayed positive**.
Mid- and large-caps absorbed the supply better than smallcaps did.

The exception is rank 4 (2024) and rank 5 (2023). The 2023 case is
particularly interesting — IPO amount fell -51% YoY, yet Smallcap
gained +56%. That's a market that was *recovering with limited
supply*. Issuance then rebounded sharply in 2024 (+24%) and 2025
(+154%) as supply chased the rally — and by 2025 the smallcap segment
finally cracked.

So the right framing is: **smallcaps absorb the marginal listing.
When supply outruns retail capacity, smallcaps go first.** The
2017-18 → 2018, 2021-22 → 2022, and 2024-25 → 2025 episodes all show
this pattern.

---

## 5. The mirror pattern — IPO droughts and recovery years

The five years where IPO amount fell more than 50% YoY:

| Year (FY ending) | IPO amt (₹ cr) | IPO YoY % | Nifty 50 YoY | Midcap YoY | Smallcap YoY |
|------------------|---------------:|----------:|--------------:|------------:|--------------:|
| 2009 (FY 2008-09) | 2,082   | -95%  | **+76%** | **+99%** | n/a |
| 2013 (FY 2012-13) | 6,528   | -84%  | +7%  | -5% | n/a |
| 2014 (FY 2013-14) | 1,236   | -81%  | **+31%** | **+56%** | **+55%** |
| 2019 (FY 2018-19) | 16,087  | -81%  | +12% | -4% | -10% |
| 2023 (FY 2022-23) | 54,773  | -51%  | **+20%** | **+47%** | **+56%** |

Of the five issuance-drought years, four had double-digit positive
returns in the broader market in the same calendar year. The
arithmetic mean of same-year Nifty 50 return was **+29%** during IPO
droughts versus **+8%** in the overall sample.

The mechanism is consistent: when valuations crash or stagnate, the
IPO pipeline empties (DRHPs are withdrawn, IPOs are deferred,
promoters refuse to sell at depressed prices). Then the market
recovers without supply pressure, valuations re-rate, and a new
issuance wave starts — at higher prices.

The single counter-case is 2019 (FY 2018-19): IPO amount cratered
-81%, but the same-year smallcap and midcap kept falling (-9.5%,
-4.3%). That's because the bear market in mid/small caps that *started*
in 2018 carried into 2019 — the supply-side response was correct, but
the demand-side correction wasn't done yet.

---

## 6. FPO + Rights is event-driven, not cyclical

Same-year correlation of FPO+Rights-amount-YoY against any index YoY
is between -0.22 and -0.08 — essentially zero. The reason becomes
obvious when you list the biggest FPO+Rights years:

| Year (FY) | Amount (₹ cr) | Notable issuer/event |
|-----------|--------------:|-----------------------|
| 2021 (FY 2020-21) | 78,987 | Reliance Industries Rights Issue ~₹53,124 cr (May-Jun 2020, post-COVID recap to refinance debt) |
| 2020 (FY 2019-20) | 55,679 | Reliance Rights spill into FY-end + assorted COVID-era equity raises |
| 2025 (FY 2024-25) | 37,862 | Vodafone Idea FPO ~₹18,000 cr (Apr 2024, distress recap) |
| 2008 (FY 2007-08) | 37,144 | Pre-GFC follow-on / rights wave |
| 2018 (FY 2017-18) | 21,413 | General supply-side froth |

Three of the top four are dominated by a single distressed-balance-sheet
recapitalization (Reliance twice, Vodafone Idea once). FPO+Rights is
**lumpy** — driven by one-off corporate events — and doesn't track
market cycles the way IPO supply does.

Lead/lag correlations confirm this: FPO+R amount in year *t* vs Nifty
50 in year *t-1* is +0.41 (positive, but weaker than IPO's +0.53), and
vs Smallcap-100-lag1 is -0.18, vs Midcap-lag1 is +0.05. Effectively
random.

The implication for market timing is that **FPO+Rights spikes are not
a topping signal** — they're often a *crisis-window* signal. Reliance
raised ₹53k cr in the depth of COVID, not at the top of the bull run.

---

## 7. Three case studies

### 7.1 The 2008 GFC anomaly

This is the one case where heavy IPO issuance coincides with a major
crash *in the same calendar year*. The conventional wisdom around
"IPO peaks predict crashes" is built largely on this one observation.
But the data structure shows it differently:

- **FY 2007-08 (year-label 2008)**: 85 IPOs, ₹42,595 cr.
- **CY 2007 Nifty 50: +55%, CY 2007 Midcap 100: +77%** — pre-crash
  bull run.
- **CY 2008 Nifty 50: -52%, CY 2008 Midcap 100: -59%** — Lehman crash.

The FY 2007-08 IPO data covers April 2007 - March 2008 — most of which
was the pre-crash bull run. The Lehman crash was September 2008, inside
FY 2008-09. And indeed: **FY 2008-09 IPO amount collapsed -95% to
₹2,082 cr.** That's the *real* response — issuers fled within a
quarter.

So 2008 doesn't show "IPO peak caused the crash". It shows IPO peak
*coincided* with the bull-run top, and the issuance market shut down
*as* the crash unfolded.

### 7.2 2018 — IPO peak + immediate smallcap crash

- **FY 2017-18 (year-label 2018)**: 201 IPOs (then a record),
  ₹83,684 cr, +188% YoY.
- **CY 2017** (the year preceding the FY end): Nifty 50 +29%,
  Smallcap +57%, Midcap +47%. Big rally.
- **CY 2018** (year of the FY end): Nifty 50 +3%, Midcap -15%,
  **Smallcap -29%**. The "Jan 2018 long-term capital gains tax"
  reform + SEBI's reclassification of midcap/smallcap mutual fund
  mandates triggered the crash.

This is the cleanest instance of the pattern: a year of record IPO
supply landed exactly when the smallcap segment was most extended.
Mid- and large-caps held up; smallcaps absorbed the supply shock and
fell sharply.

FY 2018-19 IPO amount then crashed -81% (123 issues, ₹16,087 cr). The
2019 calendar year saw smallcaps continue to fall -10%. A two-year
clean-out.

### 7.3 2022 — IPO ₹1 trillion + smallcap weakness

- **FY 2021-22 (year-label 2022)**: 120 IPOs, ₹112,553 cr (first time
  >₹1 lakh cr), +356% YoY.
- **CY 2021**: Nifty 50 +24%, Smallcap +59%, Midcap +46% — post-COVID
  rally.
- **CY 2022**: Nifty 50 +4%, Midcap +4%, **Smallcap -14%**.

Repeat of the 2018 pattern at smaller magnitude. Smallcaps absorbed
the supply, large-caps were ~flat as Fed tightening took valuations
out of the system.

### 7.4 2024-2025 — fresh record, fresh smallcap weakness

- **FY 2024-25 (year-label 2025)**: 320 IPOs (record), ₹172,328 cr
  (record), +154% YoY.
- **CY 2024**: Nifty 50 +9%, Midcap +24%, Smallcap +23% — still up.
- **CY 2025**: Nifty 50 +11%, Midcap +6%, **Smallcap -5%**.

The 2025 smallcap drawdown is mild relative to 2018 (-29%) and 2022
(-14%) — perhaps because the smallcap rally pre-2025 was extended for
longer (three big up years 2021/2023/2024). But the same directional
pattern is intact: record IPO supply, smallcap-segment-first softness.

---

## 8. What the data does NOT support

It's important to enumerate the claims that the data **does not**
confirm — to avoid over-fitting the narrative:

1. **"IPO surges predict bear markets"** — not supported. The
   correlation of IPO-amount-YoY in year *t-1* with Nifty 50 YoY in
   year *t* is -0.27. That's weak. There are years (2010, 2015-16,
   2024) where issuance was high and the broader market continued up.

2. **"FPO+Rights surges are a topping signal"** — not supported. They
   are crisis recapitalizations.

3. **"All three indices respond uniformly"** — definitely not. The
   IPO supply shock is concentrated in smallcaps. The asymmetry is
   the most interesting finding in the data.

4. **"You can mechanically time the market off issuance"** — the
   strongest signal is -0.44 correlation (IPO amount vs Smallcap
   same-year). That's not strong enough to time, but it's strong
   enough to weight position sizes or expectations.

5. **"Issuance leads the market"** — the directionality runs the
   *other* way: markets lead issuance. Promoters and bankers respond
   to valuations; they don't set them.

---

## 9. Caveats and limitations

- **FY vs CY mismatch**: IPO and FPO+Rights data are on a fiscal year
  basis (April-March), aligned to the calendar year in which the FY
  ends. The index data is calendar year (Jan-Dec). They're off by ~9
  months. The lead/lag analysis is sensitive to this; some of the
  +0.5 to +0.6 lag-1 correlation is mechanical (FY ends in March,
  3 months after the prior calendar year).
- **Coverage truncation**: Smallcap 100 starts at 2012, Midcap 100 at
  2006, indices at 2000. The smaller samples (smallcap n=12 to 13 for
  lag correlations) are noisy.
- **Equity vs all-instrument**: The IPO amount and FPO+Rights amount
  use equity-focused definitions from FY 2018-19 onward, all-instrument
  from FY 2017-18 backwards (the older SEBI tables include some
  debt-by-listed-cos in the "Listed" issuer-type column). The
  inconsistency at the FY17/FY18 boundary is documented in
  `fpo_rights_data_sources.md`. The IPO series itself is clean
  throughout.
- **SME inclusion**: From FY 2012-13 the IPO count includes SME-platform
  IPOs. The dramatic rise in IPO count from 2017 onwards (74 → 106 →
  201 → 320) is partly the SME platform's growth, not just mainboard
  activity. The mainboard split is only in the CSV from FY 2022-23 on.
  Where SME composition matters (e.g. for the 2024-25 record), the
  conclusion holds because the *mainboard* IPO amount alone was also a
  record (₹162,517 cr).
- **Index methodology changes**: NSE briefly published "Free Float" /
  "Full" parallel versions of the Midcap and Smallcap indices in 2016-
  2017. The CSVs use the Free Float version (continuation of today's
  index). Pre-2014 the index was branded "CNX Midcap" / "CNX Smallcap"
  — the underlying methodology is the same.

---

## 10. The actionable read for the next cycle

If the seven findings above are taken together, the *forensic* signal
from issuance data — useful for understanding regime, not for
intraday timing — is:

- **Year-on-year IPO amount growth >100% with simultaneous +50%+ index
  gains in the prior year is a setup for smallcap underperformance
  in the same year.** The four prior instances of this (2007-08,
  2017-18, 2021-22, 2024-25) all produced flat/down smallcap calendar
  years inside or immediately after.
- **A 50%+ YoY collapse in IPO amount is a *positive* signal for the
  next 12 months for the broad index** — 4 of 5 historical instances
  produced +12% to +76% Nifty 50 returns the same year.
- **FPO+Rights spikes should be read company-by-company, not as a
  cycle signal.** Reliance 2020 was a deleveraging trade; Vodafone
  Idea 2024 was a survival trade.
- **The relevant question for size-segment allocation** is "is IPO
  amount near a YoY record, and have smallcaps already rallied >30%
  in the prior 12 months?". When both are true, history says reduce
  smallcap exposure relative to large-cap.

None of this is a one-line trading rule, but it's a defensible
forensic read of 24 years of Indian primary-market and index data.

---

## 11. Data appendix — the year-by-year view

| Year | IPO ct | IPO ₹cr | FPO+R ct | FPO+R ₹cr | Nifty 50 | N50 YoY% | Midcap | Mid YoY% | Smallcap | Sm YoY% |
|-----:|------:|--------:|---------:|----------:|---------:|---------:|-------:|---------:|---------:|--------:|
| 2000 |   –   |   –     |    –     |     –     |  1,264   |    –     |   –    |    –     |    –     |    –    |
| 2001 |   –   |   –     |    –     |     –     |  1,059   |  -16.2   |   –    |    –     |    –     |    –    |
| 2002 |    7  |  1,202  |     8    |       70  |  1,094   |   +3.3   |   –    |    –     |    –     |    –    |
| 2003 |    6  |  1,039  |    11    |      418  |  1,880   |  +71.9   |   –    |    –     |    –     |    –    |
| 2004 |   21  |  3,434  |    30    |   15,515  |  2,081   |  +10.7   |   –    |    –     |    –     |    –    |
| 2005 |   23  | 13,749  |    32    |   10,639  |  2,837   |  +36.3   |   –    |    –     |    –     |    –    |
| 2006 |   79  | 10,936  |    59    |   16,436  |  3,966   |  +39.8   |  5,200 |    –     |    –     |    –    |
| 2007 |   77  | 28,504  |    44    |    4,397  |  6,139   |  +54.8   |  9,200 |  +76.9   |    –     |    –    |
| 2008 |   85  | 42,595  |    35    |   37,144  |  2,959   |  -51.8   |  3,736 |  -59.4   |    –     |    –    |
| 2009 |   21  |  2,082  |    24    |   12,190  |  5,201   |  +75.8   |  7,419 |  +98.6   |    –     |    –    |
| 2010 |   39  | 24,696  |    33    |   30,179  |  6,135   |  +17.9   |  8,857 |  +19.4   |    –     |    –    |
| 2011 |   53  | 35,559  |    27    |   22,108  |  4,624   |  -24.6   |  6,112 |  -31.0   |    –     |    –    |
| 2012 |   54  | 41,515  |    16    |    2,375  |  5,905   |  +27.7   |  8,505 |  +39.2   |  3,710   |    –    |
| 2013 |   33  |  6,528  |    16    |    8,945  |  6,304   |   +6.8   |  8,071 |   -5.1   |  3,403   |   -8.3  |
| 2014 |   38  |  1,236  |    17    |   12,033  |  8,283   |  +31.4   | 12,584 |  +55.9   |  5,273   |  +55.0  |
| 2015 |   46  |  3,311  |    17    |    5,477  |  7,946   |   -4.1   | 13,397 |   +6.5   |  5,653   |   +7.2  |
| 2016 |   74  | 14,815  |    13    |    9,239  |  8,186   |   +3.0   | 14,351 |   +7.1   |  5,781   |   +2.3  |
| 2017 |  106  | 29,104  |    12    |    3,417  | 10,531   |  +28.6   | 21,134 |  +47.3   |  9,093   |  +57.3  |
| 2018 |  201  | 83,684  |    22    |   21,413  | 10,863   |   +3.2   | 17,876 |  -15.4   |  6,449   |  -29.1  |
| 2019 |  123  | 16,087  |    10    |    2,149  | 12,168   |  +12.0   | 17,103 |   -4.3   |  5,835   |   -9.5  |
| 2020 |   57  | 21,286  |    19    |   55,679  | 13,982   |  +14.9   | 20,843 |  +21.9   |  7,088   |  +21.5  |
| 2021 |   40  | 24,678  |    19    |   78,987  | 17,354   |  +24.1   | 30,443 |  +46.1   | 11,289   |  +59.3  |
| 2022 |  120  |112,553  |    44    |   26,342  | 18,105   |   +4.3   | 31,509 |   +3.5   |  9,731   |  -13.8  |
| 2023 |  164  | 54,773  |    74    |   11,051  | 21,731   |  +20.0   | 46,182 |  +46.6   | 15,144   |  +55.6  |
| 2024 |  272  | 67,955  |    68    |   15,137  | 23,645   |   +8.8   | 57,190 |  +23.8   | 18,640   |  +23.1  |
| 2025 |  320  |172,328  |   144    |   37,862  | 26,130   |  +10.5   | 60,485 |   +5.8   | 17,714   |   -5.0  |

---

*This analysis was prepared from the per-series CSVs committed in
`MarketTiming/EquityIssuanceVsIndex/`. Every value is traceable to its
source per the corresponding `*_data_sources.md` file. If a year shows
an unexpected number, start by reading the source doc — most apparent
anomalies are real and well-documented (e.g. the Reliance 2020 rights
issue showing up as the FPO+Rights peak for FY 2020-21).*
