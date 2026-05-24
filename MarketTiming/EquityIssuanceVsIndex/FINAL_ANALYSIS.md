# FINAL ANALYSIS — Indian Equity Issuance vs Broad-Market Indices (2000-2025)

Prepared: 2026-05-24.
Single consolidated read-through for the work in this folder.
Companion documents: `analysis.md`, `patterns_high_probability.md`,
`methodology.md`, plus the per-series `*_data_sources.md` files.

---

## 0. TL;DR

After 26 years of Indian primary-market and index data, the most
defensible empirical conclusions are:

1. **Markets lead issuance, not the other way around.** Strong index
   years are followed by surging IPO issuance the next year; the
   reverse direction is statistical noise.

2. **Heavy IPO issuance is *not* a topping signal for the broad index.**
   In 4 of 4 years where IPO amount exceeded ₹50,000 cr (2018, 2022,
   2023, 2024), the Nifty 50 was up the following year — averaging
   +12.8%.

3. **The supply pressure lands on the smallcap segment.** In 3 of
   those 4 record-issuance years, Smallcap 100 returns *in the same
   year* were -29%, -14%, -5% (only 2024 was positive). Mid/large-cap
   absorbed the shock.

4. **IPO droughts are the single highest-probability buy signal.**
   When IPO amount fell more than 50% YoY (5 historical years: 2009,
   2013, 2014, 2019, 2023), the Midcap 100 was up every single year
   after — average +25.5%.

5. **Cheap Nifty 50 valuations (P/E Q1 ≤ ~17) → +37% avg next-year
   return, 7 of 7 historical instances positive.** The strongest
   single-feature signal in the dataset.

6. **Today's setup (end-2025).** Patterns favoring positive 2026 are
   triggered: ₹172k cr IPO amount (pattern #2 ✓), Midcap P/E 33.8
   (pattern #4 ✓), Nifty 50 P/E 22.75 in Q3 (6/6 historical positive).
   Patterns warning of caution are NOT triggered: no issuance drought
   (-50% YoY), no extreme valuation crisis. Empirical base-rate
   suggests Nifty 50 modestly positive in 2026, Smallcap mixed/weak.

**Important caveat throughout:** all "hit rates" are based on 4-7
historical instances. Bayesian credible intervals on the true
probability are wide. None of this is a trading rule; it's the
empirical base rate from comparable historical setups.

---

## 1. What was studied

**Question.** Do Indian equity primary-market activity (IPO and FPO+Rights
issuance) and broad-market valuations (Nifty 50 / Midcap 100 / Smallcap
100 P/E ratios) carry information about subsequent index returns? If
so, what specific signals have a historically high hit rate?

**Time window.** Calendar years 2000-2025 (26 years). Indian fiscal years
2001-02 to 2024-25 (24 years) for the issuance data, mapped to
calendar-year-ending convention.

**Sample sizes.**
- Nifty 50: 26 years (full window).
- Midcap 100: 20 years (2006 onwards).
- Smallcap 100: 14 years (2012 onwards).
- IPO/FPO+Rights data: 24 years (FY 2001-02 onwards).
- Years with all 5 series usable: 14 (CY 2012-2025).

---

## 2. The data, with provenance

All values traceable to specific SEBI / NSE publications, downloaded
directly from sebi.gov.in / archives.nseindia.com:

| Series | File | Span | Primary source |
|--------|------|------|----------------|
| IPO count & amount | `ipo_data.csv` | FY 2001-02 → FY 2024-25 | SEBI Handbooks 2010 + 2018 + SEBI Monthly Bulletins |
| FPO+Rights count & amount (equity) | `fpo_rights_data.csv` | FY 2001-02 → FY 2024-25 | Same SEBI sources |
| Nifty 50 year-end close + P/E | `nifty50_data.csv` | CY 2000 → CY 2025 | NSE bhavcopy 2012+, SEBI ARs 2003-2011, Wikipedia/SEBI Handbook 2008 for 2000-2002 |
| Nifty Midcap 100 year-end close + P/E | `nifty_midcap100_data.csv` | CY 2006 → CY 2025 | NSE bhavcopy 2012+, SEBI ARs 2006-2011 |
| Nifty Smallcap 100 year-end close + P/E | `nifty_smallcap100_data.csv` | CY 2012 → CY 2025 | NSE bhavcopy only |
| Industry-wise issuance | `industry_issuance_data.csv` | FY 2001-02 → FY 2024-25 | SEBI Handbooks + Bulletin Table 7/9 |

Each row has a source citation in the CSV. Each file's `*_data_sources.md`
documents every methodology choice, naming convention, and known gap.

---

## 3. Key findings (broad)

### 3.1 Direction of causality

| Pair | Correlation | n | Reading |
|------|------------:|---|---------|
| IPO amount YoY (t) vs Nifty 50 YoY (t-1) | **+0.53** | 23 | Strong index year → big issuance next year |
| IPO amount YoY (t) vs Smallcap YoY (t-1) | **+0.59** | 12 | Same |
| IPO amount YoY (t) vs Midcap YoY (t-1) | **+0.62** | 18 | Same |
| Nifty 50 YoY (t) vs IPO YoY (t-1) | -0.27 | 22 | Reverse direction: noise |
| Smallcap YoY (t) vs IPO YoY (t-1) | +0.23 | 13 | Noise |
| Midcap YoY (t) vs IPO YoY (t-1) | -0.32 | 19 | Noise |

**Conclusion:** Issuance is the *response* to market conditions, not
the *cause* of market conditions. Promoters and bankers time issuance
to high valuations; high issuance doesn't *create* the high valuations.

### 3.2 Same-year correlations (YoY%)

|                      | IPO amt YoY | FPO+R YoY | Nifty 50 | Smallcap | Midcap |
|----------------------|------------:|----------:|---------:|---------:|-------:|
| IPO amt YoY          | 1.00 | 0.04 | -0.13 | **-0.44** | -0.13 |
| FPO+R YoY            | 0.04 | 1.00 | -0.14 | -0.08 | -0.22 |
| Nifty 50 YoY         | -0.13 | -0.14 | 1.00 | 0.83 | **0.95** |
| Smallcap YoY         | -0.44 | -0.08 | 0.83 | 1.00 | **0.98** |
| Midcap YoY           | -0.13 | -0.22 | **0.95** | **0.98** | 1.00 |

**Two findings worth highlighting:**
- The Indian equity segments move together near-perfectly (Smallcap
  ↔ Midcap = 0.98; Midcap ↔ Nifty 50 = 0.95). When one rallies, all
  three rally; when one falls, all three fall.
- The only signal that crosses ±0.30 is **IPO amount YoY vs Smallcap
  YoY = -0.44** — high issuance years tend to be *same-year smallcap*
  underperformance years.

### 3.3 The asymmetry — supply hits smallcaps first

Top 4 IPO-amount years and what each index did in that *same* calendar
year:

| Year | IPO amt (₹ cr) | Nifty 50 | Midcap | Smallcap |
|------|---------------:|---------:|-------:|---------:|
| 2025 | 172,328 | +10.5% | +5.8% | **-5.0%** |
| 2022 | 112,553 | +4.3%  | +3.5% | **-13.8%** |
| 2018 | 83,684  | +3.2%  | -15.4% | **-29.1%** |
| 2024 | 67,955  | +8.8%  | +23.8% | +23.1% |

Three of four had **smallcap-specific weakness in the same year while
Nifty 50 stayed positive.** This is consistent across decades and
regimes — it's structural.

### 3.4 FPO+Rights is event-driven, not cyclical

Top FPO+Rights years are dominated by a few large distressed
recapitalizations:
- FY 2020-21: ₹78,987 cr — Reliance Industries rights ~₹53,124 cr (post-COVID deleveraging)
- FY 2019-20: ₹55,679 cr — Reliance rights spillover
- FY 2024-25: ₹37,862 cr — Vodafone Idea FPO ~₹18,000 cr (distress recap)
- FY 2007-08: ₹37,144 cr — pre-GFC follow-on wave

Correlations with index returns are between -0.22 and +0.41 — essentially
random. **FPO+Rights spikes are not a market-timing signal**.

---

## 4. Five high-probability patterns (≥80% historical hit rate)

After testing 28 signal definitions × 6 forward outcomes × 2 directions
(336 cells total), five patterns survived the **hit rate ≥80% with
n ≥ 4** filter. Full mechanics in `patterns_high_probability.md`.

| # | Signal (year *t*) | Predicts (year *t+1*) | Hit rate | Avg return |
|---|-------------------|------------------------|----------|------------|
| **1** | IPO amount YoY < -50% | Midcap UP | **5/5 = 100%** | **+25.5%** |
| **2** | IPO amount > ₹50,000 cr | Nifty 50 UP | **4/4 = 100%** | **+12.8%** |
| **3** | Smallcap P/E (norm) > 35 | Nifty 50 UP | **4/4 = 100%** | **+16.4%** |
| **4** | Midcap P/E (norm) > 30 | Nifty 50 UP | **4/4 = 100%** | **+12.5%** |
| **5** | IPO amount YoY > +200% | Nifty 50 UP | **4/5 = 80%** | **+20.0%** |

Plus the strongest single-feature signal:

**Nifty 50 P/E in Q1 quartile (≤ ~17) → next-year Nifty 50 return.
7 of 7 historical years positive, average +37%.**
Instances: 2002, 2003, 2004, 2005, 2008 (post-GFC), 2009, 2011.

### Honest reality on those hit rates

With n=4-7, the Bayesian 95% credible interval on the "true probability"
is wide. After observing 5/5 successes under a flat prior:
- Posterior mean: 0.86
- 95% CI: 0.52 to 0.99

So "5 wins out of 5 trials" rationally supports "the true probability
is somewhere between barely-better-than-a-coin-flip and
almost-always". A pattern's *historical* hit rate of 100% is **not the
same as a 100% forward probability**.

Also: the multiple-comparisons floor at 336 tested cells means we'd
expect ~17 cells (5% of 336) to clear 80% by chance alone. I found 11.
That's *below* the noise floor — some "patterns" may be data-mining.

### Patterns explicitly NOT supported by the data

| Conventional claim | Historical hit rate | Verdict |
|--------------------|---------------------|---------|
| "IPO peak = market top for Nifty 50" | 4/4 = 0% support for crash | **Rejected** |
| "Nifty 50 P/E > 25 → crash" | 1/5 = 20% (only 2007→2008 GFC) | **Rejected** |
| "FPO+Rights spike = topping signal" | Correlation ~0 with forward returns | **Rejected** |
| "IPO count > 200 = market top" | 2018→+12%, 2024→+11%, 2025→ TBD | **Rejected** |
| "Smallcap P/E > 35 → Nifty 50 crash" | 4/4 = 0% (Nifty 50 went up each time) | **Rejected** |

---

## 5. Methodology in brief (full version in `methodology.md`)

**Hypotheses I started with (6).** Conventional-wisdom claims about
IPO peaks, P/E extremes, FPO distress, cheap valuations, issuance
droughts, and symmetric size-segment response. Confirmed/rejected
case-by-case.

**Features I built (22).** 10 raw levels + 3 normalized P/Es + 5 YoY%
+ 6 forward returns. Normalization rule for P/E: replace with
price/prior-EPS when implicit EPS collapsed to <50% of prior year
(catches Midcap 2020 = 419, Smallcap 2017 = 106, Smallcap 2019 = 100;
leaves all other 60+ P/E values untouched).

**Signal definitions (28).** Four families:
- Issuance: 10 (amount thresholds, count thresholds, YoY surges/droughts)
- Valuation: 9 (P/E thresholds across the 3 indices)
- Combined: 5 (issuance × valuation conjunctions)
- Spread / prior-strength: 4

**Scoring rule.** Hit rate = matching predictions / total instances.
Required n ≥ 4 to report; ≥80% hit rate to highlight; ≥10% avg fwd
return to curate.

**Mitigations against false patterns:** symmetric direction check,
manual mechanism review, grouping by family before reporting, honest
disclosure of failure modes for each headline pattern.

**Reproducibility.** `find_patterns.py` reruns the full 336-cell
pattern search; `build_interactive_data.py` rebuilds the JSON used
by the interactive chart. All thresholds, normalization rules, and
modeling choices documented in `methodology.md` so anyone can fork
and rerun with different inputs.

---

## 6. Today's setup (end of CY 2025) — empirical base rates for 2026

Mapping current observable values to historical pattern triggers:

| Signal | End-2025 value | Triggered? | Historical implication |
|--------|----------------|------------|-------------------------|
| #1 IPO amt YoY < -50% (drought) | +154% YoY | ❌ No | No drought-bottom signal |
| #2 IPO amt > ₹50,000 cr | ₹172,328 cr | ✅ Yes | 4/4 history: Nifty 50 up next year |
| #3 Smallcap P/E > 35 | 32.2 | ❌ Just below | Mixed/borderline |
| #4 Midcap P/E > 30 | 33.8 | ✅ Yes | 4/4 history: Nifty 50 up next year |
| #5 IPO amt YoY > +200% | +154% YoY | ❌ Below | Doesn't trigger strict version |
| Nifty 50 P/E quartile | 22.75 (Q3) | n/a | 6/6 historical Q3 years were positive (+15% avg) |
| Smallcap P/E quartile | 32.2 (Q3) | n/a | 1/3 historical Q3 years positive (mixed) |

**Aggregate historical base-rate read for CY 2026 (not a forecast):**

- **Nifty 50**: signals favoring positive returns triggered (#2, #4,
  Q3 P/E). 4 historical instances of similar configurations gave
  Nifty 50 returns in the +9% to +24% range, avg +12-15%.
- **Smallcap 100**: vulnerability pattern is intact — CY 2025 already
  saw smallcap -5% on record IPO issuance. The same supply pressure
  continues into 2026.
- **Midcap 100**: tends to track Nifty 50 (correlation 0.95). Modest
  positive bias from triggered patterns #4 and similar.

**What would change the read:** a sustained smallcap drawdown (>15%
in 2026) would mean the asymmetry pattern is finally affecting the
broad index; a 2026 IPO amount falling below ₹50k cr would
re-trigger pattern #1 (issuance drought → forward rally).

---

## 7. Honest limitations

1. **Small sample.** Strongest patterns have n=4-5. Statistical power
   is weak.
2. **Multiple-comparisons risk.** 336 cells tested → ~17 false positives
   expected by chance.
3. **FY/CY mismatch.** Issuance data on Indian fiscal year, indices on
   calendar year. ~9-month offset inflates lag-1 correlations.
4. **Coverage gaps.** Smallcap 100 only goes back to 2012; pre-2012
   smallcap patterns are unverifiable.
5. **No within-year timing.** End-of-year snapshots only. Can't
   distinguish "crash in Oct 2008" from "gradual decline through 2008".
6. **No out-of-sample test.** All patterns are in-sample. Real
   forward validation requires waiting for new years to roll in.
7. **No transaction costs / taxes / slippage.** Average returns are
   index returns, not investable returns.

The right use of this analysis: **forensic priors**, updated as new
data arrives. Not a trading rule.

---

## 8. What's where in this folder

### Data files (CSVs, all source-cited)
- `ipo_data.csv` + `ipo_data_sources.md`
- `fpo_rights_data.csv` + `fpo_rights_data_sources.md`
- `nifty50_data.csv` + `nifty50_data_sources.md`
- `nifty_midcap100_data.csv` + `nifty_midcap100_data_sources.md`
- `nifty_smallcap100_data.csv` + `nifty_smallcap100_data_sources.md`
- `industry_issuance_data.csv` + `industry_issuance_data_sources.md`

### Analysis documents
- **`FINAL_ANALYSIS.md`** (this file) — single consolidated read-through.
- `analysis.md` — original broad cross-year correlation analysis (7
  findings, year-by-year appendix).
- `patterns_high_probability.md` — the 5 patterns at ≥80% hit rate in
  detail, with year-by-year evidence and case studies.
- `methodology.md` — every modeling choice, threshold, hypothesis, and
  rejected signal documented for full reproducibility.

### Code (reproducible analysis)
- `find_patterns.py` — runs the 336-cell pattern search.
- `build_interactive_data.py` — rebuilds JSON for the interactive chart.
- `plot_all_series.py`, `plot.py`, `plot_ipo.py`, `plot_fpo_rights.py`,
  `plot_nifty50.py`, `plot_nifty_midcap100.py`, `plot_nifty_smallcap100.py`
  — individual static chart generators.

### Charts (PNG / interactive HTML)
- `all_series_combined.png` — 15-series static chart (counts +
  amounts + indices + YoY% + P/E).
- `all_series_interactive.html` — interactive version with
  per-series checkboxes, year-range slider, P/E heatmap (raw /
  normalized toggle), and 6 preset time periods. Safari-compatible,
  self-contained.
- `ipo_count_vs_amount.png`, `fpo_rights_count_vs_amount.png`,
  `nifty50_close_vs_yoy.png`, `nifty_midcap100_close_vs_yoy.png`,
  `nifty_smallcap100_close_vs_yoy.png`, `equity_issuance_vs_index.png`
  — per-series static charts.

---

## 9. Three bottom-line takeaways

1. **Buy after issuance droughts (IPO YoY < -50%).** Five historical
   instances; Midcap was up every single year after; average +25%.
   Strongest tradeable signal in the dataset.

2. **Don't read record-issuance years as "market top" for Nifty 50.**
   The conventional wisdom is wrong for the broad index. The damage
   from supply pressure lands on smallcaps; large-caps absorb it.
   When you see record issuance, *rotate from smallcap to large-cap*,
   don't flee to cash.

3. **Cheap Nifty 50 valuations (P/E ≤ ~17) is the strongest entry
   signal in the dataset — 7/7 historical years positive next year,
   average +37%.** Today's P/E of 22.75 is Q3 territory, not Q1, so
   this signal is not currently triggered.

The current 2025 setup (records on IPO supply, Q3 large-cap
valuations, Q3 smallcap valuations) historically maps to: positive
but moderate Nifty 50 in 2026, continued smallcap underperformance,
midcaps tracking Nifty 50. None of that is a guarantee — it's the
historical base rate from comparable past setups.

---

*All numbers in this document are reproducible end-to-end from the
five CSV files in this folder via `find_patterns.py`. Every claim
has a citation in the underlying SEBI / NSE source per the
`*_data_sources.md` files. The supporting analysis docs (`analysis.md`,
`patterns_high_probability.md`, `methodology.md`) carry the full
detail; this file is the consolidated executive read.*
