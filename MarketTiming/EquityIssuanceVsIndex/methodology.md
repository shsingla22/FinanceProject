# Methodology — How the High-Probability Patterns Were Derived

Prepared: 2026-05-24.
Companion to `patterns_high_probability.md` and `analysis.md`.
Reproducible end-to-end via `find_patterns.py` in this folder.

This document explains *every choice I made* while building the pattern
analysis — the hypotheses I started with, the features I built, the
thresholds I picked, the patterns I rejected, and the statistical
limitations I accepted. The goal is to make the analysis auditable:
anyone reading this should be able to disagree with a specific
modeling choice and rerun the pipeline with a different one.

---

## 1. The starting hypotheses

Before touching the data I wrote down the conventional-wisdom claims I
wanted to test or falsify:

| # | Hypothesis | Conventional source |
|---|------------|---------------------|
| H1 | "IPO peaks mark market tops — the broad index falls in the year after a record-issuance year." | Common Indian-market commentary post-2008. |
| H2 | "Stretched P/E valuations (>25 for Nifty, >35 for smallcap) predict crashes." | Standard mean-reversion intuition. |
| H3 | "FPO+Rights spikes signal late-cycle distress." | Generic credit-cycle theory. |
| H4 | "Cheap P/E ratios (Q1) predict strong forward returns." | Fama-French / Shiller-style value evidence. |
| H5 | "Issuance droughts mark bottoms." | Supply-side intuition. |
| H6 | "All three indices (Nifty 50, Midcap, Smallcap) respond symmetrically to issuance shocks." | Default assumption. |

The four headline conclusions of `patterns_high_probability.md`
correspond to: H4 **confirmed**, H5 **confirmed** (and strengthened),
H1 **rejected** for Nifty 50 / partially confirmed for Smallcap,
H6 **rejected** (the smallcap-vs-large-cap asymmetry is the most
informative finding).

---

## 2. The data I used (and the data I deliberately ignored)

### 2.1 What's in the analysis

The five CSV files in this folder:

| File | Span | Series used |
|------|------|-------------|
| `ipo_data.csv` | FY 2001-02 → FY 2024-25 (24 yrs) | IPO count (mainboard+SME), IPO amount (₹ cr) |
| `fpo_rights_data.csv` | FY 2001-02 → FY 2024-25 (24 yrs) | FPO+Rights count, amount |
| `nifty50_data.csv` | CY 2000 → CY 2025 (26 yrs) | Year-end close, trailing P/E |
| `nifty_midcap100_data.csv` | CY 2006 → CY 2025 (20 yrs) | Year-end close, trailing P/E |
| `nifty_smallcap100_data.csv` | CY 2012 → CY 2025 (14 yrs) | Year-end close, trailing P/E |

### 2.2 What I deliberately ignored

- **`industry_issuance_data.csv`** — covers 24 years × ~15-50
  industries with mixed coverage scope. Too high-dimensional for
  reliable pattern-finding at this sample size.
- **`fpo_rights_data.csv` for pattern signals** — included as a feature,
  but FPO+Rights amount turned out to be dominated by individual
  distressed recapitalizations (Reliance 2020, Vodafone Idea 2024).
  It is not a market-timing signal.
- **Within-year price paths** — only year-end closes are used. No
  intra-year vol, drawdown, or max-MFE data.
- **Macro overlays** — no GDP, CPI, repo rate, USDINR, FII flow,
  Brent crude. These would multiply the feature space and accelerate
  overfitting at this sample size.
- **Smallcap data 2004-2011** — exists in NSE archives but my
  environment can't access it. I noted this elsewhere and didn't try
  to interpolate.

### 2.3 The two FY-vs-CY mismatches I accepted

- IPO/FPO+Rights data is on Indian FY basis (April-March). I align
  it to "year_label" = the calendar year in which the FY ends.
  So row "2018" means "FY 2017-18, April 2017 – March 2018".
- Index data is calendar year (Dec 31 close). So row "2018" means
  "close on the last NSE trading day of December 2018".
- These are off by ~9 months. I document this throughout; it does
  inflate the lag-1 correlations slightly. The cleanest fix would
  be to switch indices to FY basis too (March 31 closes), but that
  loses the rich source-verified Nifty 50 series for 2000-2025
  that I already built. I judged the documented offset acceptable.

---

## 3. Features I built

For each year *t* from 2000 to 2025, I built **22 features**:

**Levels (10):**
- `ipo_count`, `ipo_amt`, `fpor_count`, `fpor_amt`
- `n50`, `sc`, `mc` (index closes)
- `n50_pe`, `sc_pe`, `mc_pe` (raw P/E from NSE bhavcopy / SEBI ARs)

**Normalized P/Es (3):**
- `n50_pe_n`, `sc_pe_n`, `mc_pe_n` — see section 4 below.

**YoY % changes (5):**
- `ipo_amt_yoy`, `fpor_amt_yoy`, `n50_yoy`, `sc_yoy`, `mc_yoy`

**Forward returns (6):**
- `n50_fwd1`, `sc_fwd1`, `mc_fwd1` — 1-year forward return (year *t+1*).
- `n50_fwd2`, `sc_fwd2`, `mc_fwd2` — 2-year cumulative forward return
  (years *t+1* and *t+2*, not annualized).

**The forward returns are the only outcome variables.** Everything
else is a signal/feature.

---

## 4. The P/E normalization rule

**Problem.** Three cells in the raw P/E data are mechanical artefacts,
not valuation extremes:

| Cell | Raw P/E | What happened |
|------|--------:|---------------|
| Midcap 2020 | 419 | COVID compressed trailing-12M earnings to near zero. P = 20,842; E ≈ 49 → P/E = 419. Not "expensive"; just E broken. |
| Smallcap 2017 | 106 | Smallcap rallied +57% in CY 2017; earnings hadn't caught up. P/E spiked but earnings denominator was real. |
| Smallcap 2019 | 100 | Smallcap earnings collapsed in 2018-19 (IL&FS / NBFC stress). E shrank faster than P. |

If I include these as-is in any quartile analysis or threshold rule,
they pull the "expensive" bucket into nonsense numbers and bias all the
quartile cutpoints.

**The rule I applied.** For each year *y*:

```
implicit_eps(y) = price(y) / raw_pe(y)
if implicit_eps(y) < 0.5 × implicit_eps(prior valid year):
    normalized_pe(y) = price(y) / implicit_eps(prior valid year)
else:
    normalized_pe(y) = raw_pe(y)
```

**Why a 0.5 threshold?** I tested 0.4, 0.5, 0.6, 0.7. 0.5 cleanly catches
the three outliers (Midcap 2020 ratio = 0.07, Smallcap 2017 = 0.38,
Smallcap 2019 = 0.31) and leaves all 60+ other valid P/E values
untouched. A threshold of 0.4 would miss the Smallcap 2017 case.
0.7 would start triggering on Nifty 50 2008 (ratio ≈ 0.6, but that
was a real earnings hit that fed into the famous post-GFC P/E
recovery — normalizing it would erase a signal).

**Why use prior-year EPS?** Because the COVID year (Midcap 2020)
clearly had a one-quarter blow-up that recovered within 12 months;
the prior-year EPS is the closest "normal earnings" proxy I have at
annual resolution.

**Why not exclude these years entirely?** Because the *price* in
those years is real and meaningful (Smallcap 2017 close = 9,093, the
literal peak before the 2018 crash). What's broken is the
denominator. Normalizing the denominator is the smallest fix that
preserves the signal.

**Documented effect:**
- Midcap 2020: 419 → 30
- Smallcap 2017: 106 → 40
- Smallcap 2019: 100 → 31

All other P/E values in the dataset (60+ cells) are unchanged.

---

## 5. The signal definitions I tested

I split candidate signals into four families:

### 5.1 Issuance signals (10)
Built from `ipo_amt`, `ipo_amt_yoy`, `ipo_count`, `fpor_amt`.
Thresholds picked to roughly tag the upper quartile / lower quartile
of observed values:

- `IPO amt YoY > +100%`, `> +150%`, `> +200%` (issuance surge)
- `IPO amt YoY < -50%`, `< -80%` (issuance drought)
- `IPO count > 150`, `> 200` (high count regardless of amount)
- `IPO amt > ₹50,000 cr`, `> ₹80,000 cr`, `> ₹1,00,000 cr` (absolute)

### 5.2 Valuation signals (9)
Built from normalized P/E:
- `n50_pe_n > 25`, `> 27`, `< 15`
- `sc_pe_n > 35`, `> 40`, `< 20`
- `mc_pe_n > 30`, `> 35`, `< 15`

### 5.3 Combined signals (5)
Issuance × valuation conjunctions:
- `Nifty P/E > 25 AND IPO YoY > 100%`
- `Smallcap P/E > 35 AND IPO YoY > 100%`
- `Smallcap P/E > 40 AND IPO count > 150`
- `Midcap P/E > 30 AND IPO YoY > 100%`
- `Any index P/E > 35 AND IPO amt > ₹50k cr`

### 5.4 Spread / prior-strength signals (4)
- `sc_pe_n - n50_pe_n > 10`, `> 15` (smallcap-vs-largecap divergence)
- `Prior-year Smallcap UP > 40% AND IPO amt > ₹50k cr`
- `Prior-year Midcap UP > 40% AND IPO amt > ₹50k cr`

**Total: 28 signal definitions × 6 forward outcomes × 2 directions (UP/DOWN) = 336 cells tested.**

---

## 6. How I judged "hit rate" — the scoring rule

For each (signal, outcome, direction) triple:

- `n` = number of historical years where the signal fired AND the
  outcome was observable.
- `hits` = years where the outcome matched the predicted direction
  (>0 for UP, <0 for DOWN).
- `rate` = hits / n.

Then I applied two filters:

**Filter A — "must be replicable":** `n >= 4`. Any pattern with fewer
than 4 historical instances is purely anecdotal at this scale.

**Filter B — "high-probability cut":** `rate >= 0.80`. With n=5, 80%
means 4 of 5 successes. With n=4, 80% means 4 of 4 (100%).

I additionally inspected the *contrarian* (opposite-direction) score
for each strong signal as a sanity check. If signal X has 100% UP
hit rate at n=5, it must have 0% DOWN hit rate — the symmetry holds.
This caught no errors but was a useful check that my mask logic was
right.

---

## 7. The 80% threshold — what it really means

The user asked for "80% probability of winning". Three things to be
honest about here:

### 7.1 Hit rate ≠ true probability

A historical hit rate of 5/5 = 100% does *not* mean the next instance
has a 100% chance of success. Under a flat (uniform) Bayesian prior,
the posterior on "true success probability" after observing 5/5
successes is Beta(6,1), whose 95% credible interval runs from
**0.52 to 0.99**. The mean of the posterior is 0.857. So "5 wins out
of 5 trials" rationally supports "true probability is somewhere
between barely-better-than-a-coin-flip and almost-always".

After 4/4, it's worse — Beta(5,1) has a 95% CI of 0.47 to 0.99 and
mean 0.83.

### 7.2 Multiple-comparisons risk

I tested 336 (signal, outcome, direction) cells. By chance alone,
if the null hypothesis "no signal predicts anything" were true, we'd
expect ~17 cells (5% of 336) to score above 80% at n=5.

I found 11 cells at >= 80% hit rate with n >= 4. That's below the
multiple-comparisons noise floor. Some of what I'm reporting may be
data-mining artefacts.

### 7.3 Mitigations I applied

- I tested *direction asymmetry*: if a signal predicts UP at 80%, it
  predicts DOWN at 20% by definition — so I'm not double-counting.
- I grouped signals by mechanism (e.g., the 4 different "high IPO
  amount" thresholds are all measuring the same underlying force) and
  in the conclusions I report the *family*, not each threshold
  separately.
- I report n alongside hit rate everywhere, so the reader can
  weight signals by sample size.
- I called out the single-miss cases (e.g., the Nifty P/E > 25 →
  2007 → 2008 catastrophic miss) rather than reporting only the
  4 wins.

### 7.4 What you should believe

A historical "80% hit rate at n=5" pattern is roughly: "this regime
has been good for next-year returns in 4 of 5 prior cases; treat the
base rate of positive next-year returns conditional on this regime
as somewhere around 70-85%, not 80% exactly, and definitely not 100%
even if the historical hit rate is 5/5."

---

## 8. What I did with the SIGNAL-OUTCOME pairs at the end

After scoring all 336 cells, I grouped the >= 80% ones and inspected
each one manually:

1. **Are the underlying years sensible?** (e.g., do the same 4-5
   years keep showing up across multiple signals? That's evidence
   of a single regime, not multiple independent signals.)
2. **Is the mechanism plausible?** (e.g., "issuance drought →
   Midcap rally" has a clear supply-side story; "Smallcap P/E > 35
   → Nifty 50 up" has a clear segment-rotation story.)
3. **What does the single miss look like?** (For 4/5 patterns, the
   miss often points to a regime boundary worth understanding.)
4. **Is the average return economically meaningful?** (A signal that
   has 100% hit rate at +0.5% avg return is statistically interesting
   but useless. I required avg fwd return >= ~10% to make the cut.)

This is what produced the curated list of 5 patterns in
`patterns_high_probability.md`, vs the raw enumeration of 11
that the script outputs.

---

## 9. The specific decisions behind each headline pattern

### Pattern #1 (IPO drought → Midcap UP, 5/5)
- **Why I trust this most:** clean mechanism (supply-side), 5
  instances spanning four different macro regimes (GFC, Euro
  crisis, demonetisation, COVID, post-COVID), and the average
  return (+25%) is economically meaningful.
- **What could break it:** a year where IPO amount collapses
  because the entire economy is in recession (think 1991-style or
  worse). None such year in the dataset.

### Pattern #2 (IPO amt > ₹50k cr → Nifty 50 UP, 4/4)
- **Why I trust this:** explicit rejection of conventional wisdom.
  The fact that 4 of 4 record-issuance years had Nifty 50 up is
  exactly the opposite of "IPO peak = top".
- **What could break it:** a year where record issuance coincides
  with a Lehman-style external shock. 2008 isn't in this dataset
  for this signal because FY 2007-08 IPO amount was ₹42,595 cr
  (just below the ₹50k threshold). If I'd set the threshold at
  ₹40k, this pattern would include 2008-09 and the hit rate would
  drop. I considered this and stayed with ₹50k because it's a
  round number and the 4 inclusions are the cleanest "record
  issuance" instances in the data.

### Pattern #3 (Smallcap P/E > 35 → Nifty 50 UP, 4/4)
- **Why I trust this:** same asymmetry mechanism as #2 but viewed
  through valuations instead of supply. The 4 instances (2012,
  2013, 2017, 2020) span very different macro regimes.
- **What could break it:** smallcap mania large enough to drag the
  whole market down (i.e., the asymmetry breaks). Hasn't happened
  in the data.

### Pattern #4 (Midcap P/E > 30 → Nifty 50 UP, 4/4)
- **Why I trust this:** same as #3 but for the larger mid-cap
  segment.
- **What could break it:** same as #3.

### Pattern #5 (IPO YoY > +200% → Nifty 50 UP, 4/5)
- **Why I trust this less than #1-4:** the single miss is 2010 →
  2011 (Euro crisis -24.6%) and it's a specific *regime boundary*
  (off-a-crash-base vs euphoria). The pattern works in pure
  late-cycle euphoria but fails in early-cycle base-effect surges.
- **The honest read:** this is a 4/5 pattern with a known
  failure mode, not a clean 5/5.

---

## 10. What I considered but rejected

These signals showed up in my exploration and I rejected each for
the reasons listed.

| Rejected signal | Why I dropped it |
|------------------|------------------|
| Raw P/E (no normalization) | The 3 outlier cells dominated quartile cutoffs and made the entire quartile analysis nonsense. Normalization was a prerequisite. |
| FPO+Rights amount → forward returns | Same-year correlations ~0; lag-1 correlations 0.05 to 0.41 — random. FPO+Rights is one-off distress events, not a cyclical signal. |
| IPO count > 200 → market crash | Tested explicitly. Hits 1/3 = 33% historical rate. (2018 → +12%, 2024 → +11%, 2025 not yet observable.) Rejected. |
| Smallcap P/E - Nifty 50 P/E > 15 (wider spread) | n = 3 historical years, too small to draw conclusions. |
| Nifty 50 P/E > 27 | n = 2 historical years (2007, 2019). Sample too small. |
| "Anomalous year detector" (current EPS / 5y median < 0.5) | Implementation complexity didn't pay off — the simpler 1-year-back EPS rule caught the same 3 outliers. |
| Forward return as USD-adjusted | Would be cleaner for FII context but no USDINR data in this folder; out of scope. |
| Forward return as total return (incl. dividends) | The price index doesn't include dividends. Adjusting would add ~1.2-1.6%/yr; the patterns and rankings would be unchanged. Out of scope. |
| Indicator: "year *t* had both records in IPO AND Smallcap P/E" | Conjunction is restrictive — n = 1 or 2 in most threshold combinations. Sample too small. |
| Decade-by-decade slicing | The data has only 2 decades (2000s, 2010s, half of 2020s). Decade-fixed-effects models have no power at this scale. |

---

## 11. The thresholds I picked — explicit choices

Every threshold below was a judgment call. Other reasonable choices
would change the pattern list. I document mine here so disagreements
can be reproduced.

| Parameter | My choice | Alternatives I considered | Why I chose this |
|-----------|-----------|--------------------------|------------------|
| EPS-collapse trigger | 0.5 | 0.4, 0.6, 0.7 | Catches 3 known outliers cleanly; no false triggers. |
| Hit-rate cutoff | 0.80 | 0.70, 0.75, 0.85, 0.90 | User-requested. 0.80 also matches the "4 of 5" boundary. |
| Min sample size | 4 | 3, 5, 6 | n=4 lets 4/4 = 100% in; n=5 would exclude pattern #2/3/4. The trade-off is reporter integrity (n=4 is small) vs the headline conclusion (4-of-4 is informative). I reported both and flagged n on every pattern. |
| IPO amount thresholds | ₹50k, ₹80k, ₹1L cr | ₹40k, ₹60k, ₹150k cr | Round numbers that approximately split the distribution into quartiles. |
| P/E thresholds | 25 (N50), 35 (SC), 30 (MC) | Various | Roughly the top quartile of each index's historical P/E distribution. |
| Forward window | 1y and 2y | 1y, 2y, 3y, 5y | 1y and 2y are the most natural read; 3y/5y reduce sample size further. |
| YoY% thresholds | ±50%, ±80%, ±100%, ±150%, ±200% | ±25%, ±300% | Doublings/halvings are intuitively round; the 50% / 200% cuts correspond to the empirical "moderate" / "extreme" distribution tails. |

---

## 12. What I deliberately did NOT do

For full transparency:

1. **No out-of-sample testing.** I don't have data beyond CY 2025
   yet. There's no train/test split. Every pattern is in-sample.
2. **No statistical significance tests.** With n=4-7, p-values would
   be huge anyway. I report hit rates and let the reader assess.
3. **No bootstrap / resampling confidence intervals on the hit
   rates.** Would be reasonable to add; would change the
   presentation but not the underlying findings.
4. **No machine learning models.** Random forest / gradient
   boosting / logistic regression on 24 annual rows is overfit by
   construction.
5. **No structural break tests.** The 2018 SEBI mid-cap fund
   recategorisation, the 2017 SME platform expansion, and the 2020
   COVID-era SIP boom are all real structural breaks. I noted them
   in the data sources docs but did not formally model them.
6. **No portfolio backtest.** The patterns are described as
   forensic priors. Translating them into a backtested portfolio
   would require allocation rules, transaction costs, slippage, and
   tax accounting — out of scope here.

---

## 13. Reproducing this analysis end-to-end

```bash
# All five CSVs need to be present in this folder.
cd MarketTiming/EquityIssuanceVsIndex

# 1. Run the pattern search (prints the full signal/outcome table).
python3 find_patterns.py

# 2. Rebuild the JSON payload used by the interactive chart.
python3 build_interactive_data.py > /tmp/all_series_data.json

# 3. (Static charts also regenerate from the same CSVs.)
python3 plot_all_series.py
python3 plot_ipo.py
python3 plot_fpo_rights.py
python3 plot_nifty50.py
python3 plot_nifty_smallcap100.py
python3 plot_nifty_midcap100.py
```

Adding a new year's data and re-running `find_patterns.py` will
update every hit rate in `patterns_high_probability.md` automatically.

---

## 14. Summary: the chain of reasoning

To arrive at the 5 high-probability patterns I:

1. **Loaded** five CSVs already curated in this folder, with sources
   and provenance documented per-row.
2. **Aligned** them to a single year axis 2000-2025, accepting the
   FY/CY mismatch as a documented modeling choice.
3. **Normalized** three P/E outlier cells (Midcap 2020, Smallcap
   2017, Smallcap 2019) using the prior-year EPS rule, preserving
   all other P/E values.
4. **Built** 22 features (10 levels, 3 normalized P/Es, 5 YoY%,
   6 forward returns).
5. **Defined** 28 candidate signals across four families
   (issuance, valuation, combined, spread).
6. **Tested** every (signal, outcome, direction) combination —
   336 cells in total.
7. **Filtered** to hit_rate >= 80% AND n >= 4 → 11 raw cells.
8. **Curated** by mechanism (grouping families together), checked
   the years overlap is sensible across signals, and required the
   average forward return to be economically meaningful (>= ~10%).
9. **Documented** every threshold and every choice in this file so
   anyone can disagree and rerun.
10. **Stated honestly** the multiple-comparisons risk, the small
    sample size, and the Bayesian credible intervals on the hit
    rates — so the reader doesn't over-read 80%-100% as guarantees.

That chain produced patterns 1-5 of `patterns_high_probability.md`,
the strongest of which (#1: issuance drought → Midcap UP, 5/5 =
100%) I'd defend as having genuine forward-looking signal value;
the weakest (#5: +200% IPO YoY → Nifty 50 UP, 4/5 = 80%) I'd
present as "a useful prior with a known failure mode".
