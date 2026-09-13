# The Darvas screen — 2015-03-01 → 2020-03-31

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2014-03-01 → 2020-03-31, 1522 symbols, in `ROLLING_2014-03-01_to_2020-03-31/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **The universe is POINT-IN-TIME with a ROLLING radar:** membership is recomputed EVERY MONTH as the top symbols by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and new listings or emerging names ENTER the month they earn their place, so neither survivorship bias nor an emergence blind spot remains. Membership gates fresh entries only; a held position runs to its stop regardless (`_membership_long.csv`). Raw exchange data means heuristic split/bonus adjustment, every one listed in `_adjustments.csv`. No slippage, stop exits at the stop price, fractional shares. Stored fiscal statements exist for 31% of this universe — a stock without statements cannot be blocked by the earnings gate (only a FALLING verdict blocks), which loosens that gate for the rest.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), best volume reaction first, at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with NEW capital, 3× cap.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled with FRESH MONEY from outside the portfolio, equal to the position's market value, at the next day's open — but AT MOST THREE TIMES per position (8× the first slice), so the capital the rule demands stays realistic. The new money never touches the portfolio's cash — fresh entries are never starved — and every injection is dated and logged, so the honest yardstick is the money-weighted return (XIRR), not a naive multiple. Each add-on is its own tax lot on its own holding clock; the ratcheted stop covers the whole enlarged position; a jump past the cap is logged, never doubled.

## The headline — XIRR is the honest yardstick

| Engine | Money put in | Final value | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | ₹11.20 lakh crore (₹100 + ₹11.20 lakh crore injected) | **₹9.52 lakh crore** | **-36.05%** |
| B: doubling, before charges and tax | ₹11.35 lakh crore | ₹9.69 lakh crore | -35.29% |
| **A: no doubling, NET of charges and tax** | ₹100.00 | **₹92.90** | **-1.44%** |
| A: no doubling, before charges and tax | ₹100.00 | ₹106.27 | +1.21% |
| Nifty 50 (pre-cost, pre-tax) | ₹100.00 | ₹96.20 | -0.76% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹0.00; unrealised gains in both end books carry further deferred liabilities.*

5.07 years, 266 weekly screens. Engine B injected new capital 292 times (gross run: 290); the complete dated injection list is in the blotter and the events CSV.

## The radar, measured — an honest negative result

This run uses ROLLING monthly membership; the same window was also run
on a FIXED start-month cohort (in this repository's history). Side by
side:

| Engine A (₹100 →) | Fixed cohort | Rolling radar (this run) |
|---|---:|---:|
| A: no doubling, net | ₹108.99 (+1.71%/yr) | ₹92.90 (−1.44%/yr) |
| A: no doubling, gross | ₹124.68 (+4.44%/yr) | ₹106.27 (+1.21%/yr) |
| Nifty 50 | ₹96.20 (−0.76%/yr) | ₹96.20 (−0.76%/yr) |

The radar was built to catch emerging stocks — and it does (the IPO
entries are in `_membership_long.csv`) — but on this window it COST
money, and the ledger says why: cohort trades averaged **+1.2%** (115 closed) while radar-admitted trades averaged **−0.9%** (69 closed). A stock typically enters
the radar BECAUSE its turnover just spiked, and the weekly volume
trigger then fires on exactly that spike — so the boundary's monthly
churn (~40 names in and out) feeds the screens one-month wonders that
mean-revert, and those trades crowd a third of the slots away from
the steadier cohort names. The fixed cohort's blind spot was,
accidentally, a quality filter. A stricter door (ranking by three
months of trailing turnover, or requiring two consecutive qualifying
months before entry) would keep the genuine emergers while shutting
out the wonders — measurable the same way if wanted.

## What the frictions took (net runs)

| | Engine A: no doubling | Engine B: doubling |
|---|---:|---:|
| Transaction charges | ₹4.46 | ₹4,788.39 crore |
| Capital-gains tax paid | ₹10.81 | ₹0.00 |
| Tax accrued, final part-year | ₹0.00 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2015 | 2015-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹5.94 / ₹0.00 |
| FY2016 | 2016-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹6,722.55 / ₹0.00 |
| FY2017 | 2017-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹6.37 lakh / ₹0.00 |
| FY2018 | 2018-04-02 | ₹0.00 | ₹0.00 | ₹0.00 | ₹6.20 crore / ₹0.00 |
| FY2019 | 2019-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹3,659.17 crore / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹1.79 lakh crore / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2015 | 2015-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹4.90 / ₹0.00 |
| FY2016 | 2016-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹8.81 / ₹0.00 |
| FY2017 | 2017-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹4.27 / ₹0.00 |
| FY2018 | 2018-04-02 | ₹54.05 | ₹0.00 | ₹10.81 | ₹0.00 / ₹0.00 |
| FY2019 | 2019-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹27.73 / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹51.55 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2015 (2015-12-24) | ₹111.94 | +11.9% | ₹33,047.28 | ₹31,681.81 | +36.3% | -12.0% |
| 2016 (2016-12-30) | ₹98.13 | -12.3% | ₹24.61 lakh | ₹24.88 lakh | -10.6% | +4.1% |
| 2017 (2017-12-29) | ₹165.43 | +68.6% | ₹234.01 crore | ₹215.11 crore | +65.7% | +28.6% |
| 2018 (2018-12-28) | ₹122.80 | -25.8% | ₹11,412.40 crore | ₹13,451.73 crore | -54.8% | +3.1% |
| 2019 (2019-12-27) | ₹107.55 | -12.4% | ₹6.60 lakh crore | ₹5.91 lakh crore | +28.2% | +12.8% |
| 2020 (2020-03-31) | ₹92.90 | -13.6% | ₹9.52 lakh crore | ₹5.15 lakh crore | -25.2% | -29.8% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-14.0%** (A: -48.8%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **197 closed trades**: 36 winners (18%), average winner +15.7%, average loser -11.7% (returns per blended entry price).
- Best closed trade GOACARBON +131.1%; worst RUCHISOYA -38.4%.
- Median holding period 49 days.
- Cash share of equity averaged 17%; fully in cash 1 of 266 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

| Month-end screen | B equity | B injected so far | B cash | B positions | A equity |
|---|---:|---:|---:|---:|---:|
| 2015-03-27 | ₹177.04 | ₹90.20 | ₹44.31 | 7 | ₹90.61 |
| 2015-04-30 | ₹249.49 | ₹170.11 | ₹161.38 | 4 | ₹88.45 |
| 2015-05-29 | ₹395.65 | ₹328.58 | ₹0.00 | 10 | ₹87.27 |
| 2015-06-26 | ₹528.70 | ₹428.97 | ₹11.16 | 10 | ₹89.78 |
| 2015-07-31 | ₹1,163.44 | ₹884.70 | ₹97.84 | 9 | ₹107.02 |
| 2015-08-28 | ₹1,965.46 | ₹1,916.20 | ₹1,396.14 | 4 | ₹102.01 |
| 2015-09-24 | ₹2,456.07 | ₹2,406.77 | ₹0.68 | 10 | ₹100.56 |
| 2015-10-30 | ₹6,426.76 | ₹6,690.64 | ₹3,204.16 | 7 | ₹103.35 |
| 2015-11-27 | ₹9,599.84 | ₹9,607.41 | ₹2,066.33 | 9 | ₹108.12 |
| 2015-12-24 | ₹33,047.28 | ₹31,681.81 | ₹82.23 | 10 | ₹111.94 |
| 2016-01-29 | ₹32,018.42 | ₹36,226.47 | ₹22,656.99 | 4 | ₹97.03 |
| 2016-02-26 | ₹38,894.46 | ₹45,499.69 | ₹20,479.71 | 4 | ₹93.03 |
| 2016-03-23 | ₹50,661.39 | ₹55,427.64 | ₹9,209.14 | 7 | ₹98.56 |
| 2016-04-29 | ₹74,488.72 | ₹81,557.79 | ₹0.00 | 10 | ₹93.14 |
| 2016-05-27 | ₹1.31 lakh | ₹1.39 lakh | ₹8,604.51 | 9 | ₹92.33 |
| 2016-06-24 | ₹1.88 lakh | ₹1.89 lakh | ₹2,559.88 | 9 | ₹98.26 |
| 2016-07-29 | ₹3.80 lakh | ₹3.69 lakh | ₹72.15 | 10 | ₹110.63 |
| 2016-08-26 | ₹5.89 lakh | ₹5.60 lakh | ₹0.00 | 10 | ₹104.51 |
| 2016-09-30 | ₹9.39 lakh | ₹9.52 lakh | ₹3.34 lakh | 6 | ₹105.86 |
| 2016-10-28 | ₹14.21 lakh | ₹13.92 lakh | ₹42,053.78 | 9 | ₹111.23 |
| 2016-11-25 | ₹12.22 lakh | ₹13.92 lakh | ₹2.87 lakh | 8 | ₹95.68 |
| 2016-12-30 | ₹24.61 lakh | ₹25.19 lakh | ₹3.44 lakh | 10 | ₹98.13 |
| 2017-01-27 | ₹38.11 lakh | ₹37.91 lakh | ₹71,559.49 | 11 | ₹106.83 |
| 2017-02-23 | ₹65.28 lakh | ₹68.37 lakh | ₹5.97 lakh | 10 | ₹108.40 |
| 2017-03-31 | ₹1.43 crore | ₹1.39 crore | ₹25.18 lakh | 11 | ₹112.64 |
| 2017-04-28 | ₹2.85 crore | ₹2.68 crore | ₹15.59 lakh | 12 | ₹121.16 |
| 2017-05-26 | ₹3.75 crore | ₹3.79 crore | ₹2.17 crore | 5 | ₹114.47 |
| 2017-06-30 | ₹6.34 crore | ₹6.50 crore | ₹2.05 crore | 10 | ₹121.48 |
| 2017-07-28 | ₹11.62 crore | ₹11.81 crore | ₹10.53 lakh | 13 | ₹125.96 |
| 2017-08-24 | ₹16.38 crore | ₹16.93 crore | ₹0.00 | 11 | ₹117.74 |
| 2017-09-29 | ₹39.03 crore | ₹39.29 crore | ₹10.65 crore | 9 | ₹128.73 |
| 2017-10-27 | ₹70.22 crore | ₹62.76 crore | ₹49.46 lakh | 11 | ₹146.21 |
| 2017-11-24 | ₹106.59 crore | ₹98.10 crore | ₹4.36 crore | 11 | ₹152.69 |
| 2017-12-29 | ₹234.01 crore | ₹215.36 crore | ₹6.55 crore | 10 | ₹165.43 |
| 2018-01-25 | ₹247.12 crore | ₹228.14 crore | ₹19.99 crore | 10 | ₹170.33 |
| 2018-02-23 | ₹365.80 crore | ₹331.73 crore | ₹8.66 crore | 10 | ₹168.91 |
| 2018-03-28 | ₹492.95 crore | ₹505.54 crore | ₹182.68 crore | 7 | ₹158.89 |
| 2018-04-27 | ₹717.56 crore | ₹652.58 crore | ₹53.90 crore | 9 | ₹164.68 |
| 2018-05-25 | ₹1,145.76 crore | ₹1,077.27 crore | ₹189.65 crore | 8 | ₹155.55 |
| 2018-06-29 | ₹2,080.26 crore | ₹2,161.72 crore | ₹697.90 crore | 6 | ₹143.56 |
| 2018-07-27 | ₹3,132.58 crore | ₹3,173.29 crore | ₹196.82 crore | 7 | ₹143.87 |
| 2018-08-31 | ₹6,200.31 crore | ₹5,656.90 crore | ₹0.00 | 8 | ₹154.16 |
| 2018-09-28 | ₹7,033.64 crore | ₹8,094.47 crore | ₹6,523.54 crore | 2 | ₹130.46 |
| 2018-10-26 | ₹7,374.38 crore | ₹8,631.16 crore | ₹5,029.07 crore | 4 | ₹128.93 |
| 2018-11-30 | ₹10,105.65 crore | ₹11,525.22 crore | ₹2,227.39 crore | 7 | ₹127.23 |
| 2018-12-28 | ₹11,412.40 crore | ₹13,667.09 crore | ₹4,028.66 crore | 8 | ₹122.80 |
| 2019-01-25 | ₹20,156.23 crore | ₹23,163.60 crore | ₹752.24 crore | 10 | ₹119.92 |
| 2019-02-22 | ₹19,530.11 crore | ₹23,163.60 crore | ₹2,510.29 crore | 8 | ₹114.67 |
| 2019-03-29 | ₹30,959.61 crore | ₹32,786.90 crore | ₹2,280.27 crore | 8 | ₹119.22 |
| 2019-04-26 | ₹41,891.86 crore | ₹46,329.05 crore | ₹18,152.22 crore | 6 | ₹113.44 |
| 2019-05-31 | ₹45,674.71 crore | ₹52,788.67 crore | ₹8,454.12 crore | 7 | ₹105.87 |
| 2019-06-28 | ₹64,221.52 crore | ₹74,118.82 crore | ₹2,488.72 crore | 9 | ₹99.54 |
| 2019-07-26 | ₹1.07 lakh crore | ₹1.20 lakh crore | ₹13,804.95 crore | 8 | ₹97.80 |
| 2019-08-30 | ₹2.89 lakh crore | ₹2.95 lakh crore | ₹0.00 | 8 | ₹100.60 |
| 2019-09-27 | ₹4.02 lakh crore | ₹3.87 lakh crore | ₹0.00 | 8 | ₹102.24 |
| 2019-10-25 | ₹5.76 lakh crore | ₹5.29 lakh crore | ₹0.00 | 8 | ₹107.10 |
| 2019-11-29 | ₹6.44 lakh crore | ₹6.05 lakh crore | ₹0.00 | 8 | ₹105.30 |
| 2019-12-27 | ₹6.60 lakh crore | ₹6.05 lakh crore | ₹17,509.02 crore | 7 | ₹107.55 |
| 2020-01-31 | ₹7.19 lakh crore | ₹6.72 lakh crore | ₹29,573.21 crore | 8 | ₹107.55 |
| 2020-02-28 | ₹10.64 lakh crore | ₹10.70 lakh crore | ₹2.88 lakh crore | 8 | ₹105.40 |
| 2020-03-31 | ₹9.52 lakh crore | ₹11.20 lakh crore | ₹8.03 lakh crore | 2 | ₹92.90 |

## Engine B — still held at the end

| Stock | First entry | Blended entry ₹ | Lots | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|---:|
| ATLASCYCLE | 2016-04-18 | 235.87 | 4 | 665.30 | 239.25 | +182.1% |
| BOROSIL | 2020-02-10 | 197.13 | 2 | 220.15 | 181.45 | +11.7% |

## Engine B — every closed trade

*Returns are on the blended entry price across lots.*

| Stock | First entry | Blended ₹ | Lots | Exit | Exit ₹ | Return |
|---|---|---:|---:|---|---:|---:|
| TAKE | 2015-03-09 | 147.85 | 1 | 2015-03-16 | 130.91 | -11.5% |
| MADHUCON | 2015-03-09 | 61.15 | 2 | 2015-03-17 | 55.38 | -9.4% |
| KEI | 2015-03-09 | 65.00 | 2 | 2015-03-23 | 59.38 | -8.6% |
| JBMA | 2015-03-09 | 238.40 | 2 | 2015-03-23 | 222.30 | -6.8% |
| ZYDUSWELL | 2015-03-23 | 1,038.36 | 2 | 2015-04-20 | 960.45 | -7.5% |
| GEOMETRIC | 2015-03-09 | 169.06 | 3 | 2015-04-22 | 158.22 | -6.4% |
| DYNAMATECH | 2015-03-30 | 3,843.00 | 1 | 2015-04-22 | 3,081.75 | -19.8% |
| SOLARINDS | 2015-03-30 | 701.67 | 2 | 2015-04-24 | 694.01 | -1.1% |
| ITDCEM | 2015-03-09 | 75.95 | 2 | 2015-04-27 | 64.03 | -15.7% |
| SOMANYCERA | 2015-03-09 | 395.05 | 3 | 2015-04-27 | 418.24 | +5.9% |
| HCC | 2015-03-09 | 34.68 | 2 | 2015-04-27 | 31.21 | -10.0% |
| CIMMCO | 2015-04-27 | 105.58 | 2 | 2015-06-03 | 85.29 | -19.2% |
| ABIRLANUVO | 2015-05-11 | 930.90 | 2 | 2015-06-03 | 850.92 | -8.6% |
| MANINFRA | 2015-04-27 | 46.45 | 3 | 2015-07-27 | 41.85 | -9.9% |
| VADILALIND | 2015-05-04 | 605.41 | 4 | 2015-08-13 | 716.44 | +18.3% |
| SMLISUZU | 2015-03-09 | 1,138.57 | 4 | 2015-08-24 | 1,110.20 | -2.5% |
| NILKAMAL | 2015-05-18 | 896.53 | 4 | 2015-08-24 | 927.12 | +3.4% |
| REPRO | 2015-05-18 | 529.09 | 2 | 2015-08-24 | 404.70 | -23.5% |
| MANINDS | 2015-05-18 | 96.88 | 4 | 2015-08-24 | 95.77 | -1.1% |
| PUNJABCHEM | 2015-05-18 | 233.92 | 2 | 2015-08-24 | 179.72 | -23.2% |
| CENTENKA | 2015-08-03 | 217.84 | 3 | 2015-08-25 | 185.69 | -14.8% |
| GARWALLROP | 2015-08-17 | 309.90 | 1 | 2015-08-25 | 274.60 | -11.4% |
| MANGALAM | 2015-06-08 | 69.68 | 3 | 2015-09-08 | 73.50 | +5.5% |
| ICIL | 2015-08-31 | 199.78 | 1 | 2015-09-08 | 145.90 | -27.0% |
| CAPLIPOINT | 2015-09-07 | 304.00 | 2 | 2015-10-28 | 262.64 | -13.6% |
| NEULANDLAB | 2015-09-14 | 808.82 | 4 | 2015-10-29 | 714.39 | -11.7% |
| CEATLTD | 2015-09-14 | 1,253.99 | 3 | 2015-10-29 | 1,131.45 | -9.8% |
| JUBLINDS | 2015-08-31 | 298.50 | 2 | 2015-11-02 | 224.21 | -24.9% |
| ABBOTINDIA | 2015-09-07 | 5,544.31 | 2 | 2015-11-06 | 5,365.17 | -3.2% |
| UCOBANK | 2015-11-02 | 50.30 | 1 | 2015-11-09 | 45.79 | -9.0% |
| JINDALPOLY | 2015-09-07 | 518.59 | 4 | 2015-11-26 | 494.38 | -4.7% |
| TORNTPHARM | 2015-06-08 | 1,461.24 | 4 | 2015-11-30 | 1,426.04 | -2.4% |
| GHCL | 2015-08-17 | 127.37 | 3 | 2015-12-09 | 129.53 | +1.7% |
| TRIGYN | 2015-11-09 | 82.18 | 3 | 2015-12-10 | 82.94 | +0.9% |
| ECLERX | 2015-03-09 | 1,718.52 | 4 | 2015-12-17 | 1,619.75 | -5.7% |
| NIITTECH | 2015-11-02 | 582.82 | 3 | 2016-01-07 | 537.51 | -7.8% |
| SHARONBIO | 2015-12-14 | 30.40 | 2 | 2016-01-12 | 26.93 | -11.4% |
| NECLIFE | 2015-11-02 | 53.52 | 3 | 2016-01-13 | 49.46 | -7.6% |
| MOREPENLAB | 2015-11-16 | 34.20 | 4 | 2016-01-13 | 34.82 | +1.8% |
| EDL | 2015-12-14 | 102.97 | 2 | 2016-01-13 | 87.83 | -14.7% |
| KANORICHEM | 2015-12-14 | 78.00 | 2 | 2016-01-13 | 65.32 | -16.3% |
| TRF | 2015-11-02 | 367.51 | 3 | 2016-01-14 | 334.26 | -9.0% |
| GLOBUSSPR | 2015-11-30 | 78.95 | 2 | 2016-01-18 | 65.41 | -17.1% |
| NELCO | 2015-11-30 | 110.10 | 2 | 2016-02-10 | 83.25 | -24.4% |
| ROHLTD | 2016-01-11 | 96.46 | 2 | 2016-02-12 | 64.83 | -32.8% |
| PRICOL | 2016-02-01 | 50.17 | 2 | 2016-02-29 | 41.77 | -16.7% |
| ENERGYDEV | 2016-03-08 | 64.92 | 3 | 2016-04-12 | 60.80 | -6.3% |
| RSSOFTWARE | 2016-04-18 | 111.20 | 2 | 2016-05-18 | 93.44 | -16.0% |
| DALMIASUG | 2016-03-14 | 99.02 | 2 | 2016-05-24 | 86.86 | -12.3% |
| VIVIMEDLAB | 2015-09-14 | 77.82 | 4 | 2016-05-31 | 79.42 | +2.1% |
| MCLEODRUSS | 2016-03-28 | 198.54 | 3 | 2016-07-19 | 198.74 | +0.1% |
| TPLPLASTEH | 2016-05-23 | 492.24 | 4 | 2016-07-22 | 465.74 | -5.4% |
| VSTTILLERS | 2016-04-18 | 1,879.48 | 4 | 2016-08-01 | 1,826.38 | -2.8% |
| RAMKY | 2016-03-08 | 78.44 | 4 | 2016-08-10 | 79.04 | +0.8% |
| UFO | 2016-07-25 | 602.25 | 1 | 2016-08-16 | 510.05 | -15.3% |
| KSL | 2016-08-22 | 372.26 | 2 | 2016-09-01 | 337.73 | -9.3% |
| SOMANYCERA | 2016-01-25 | 400.86 | 4 | 2016-09-21 | 551.10 | +37.5% |
| GUJALKALI | 2016-05-30 | 251.45 | 4 | 2016-09-29 | 286.90 | +14.1% |
| TATAMETALI | 2016-07-25 | 446.05 | 2 | 2016-09-29 | 366.19 | -17.9% |
| DBCORP | 2016-07-25 | 412.14 | 3 | 2016-09-29 | 382.47 | -7.2% |
| UNIPLY | 2016-09-06 | 55.01 | 3 | 2016-11-04 | 50.16 | -8.8% |
| VIVIMEDLAB | 2016-10-03 | 114.00 | 2 | 2016-11-04 | 99.84 | -12.4% |
| GLOBUSSPR | 2016-10-03 | 107.10 | 2 | 2016-11-04 | 95.00 | -11.3% |
| RAIN | 2016-08-08 | 42.82 | 3 | 2016-11-09 | 42.08 | -1.7% |
| TVSSRICHAK | 2016-10-03 | 3,981.06 | 2 | 2016-11-09 | 3,633.84 | -8.7% |
| GOLDBEES | 2016-02-15 | 2,681.07 | 4 | 2016-11-17 | 2,689.64 | +0.3% |
| HDFCMFGETF | 2016-03-14 | 2,865.83 | 4 | 2016-11-18 | 2,718.90 | -5.1% |
| HONDAPOWER | 2016-11-15 | 1,556.00 | 1 | 2016-11-18 | 1,438.87 | -7.5% |
| SESHAPAPER | 2016-11-07 | 164.20 | 1 | 2016-11-22 | 113.48 | -30.9% |
| STARPAPER | 2016-11-07 | 181.87 | 3 | 2016-12-13 | 175.94 | -3.3% |
| SWANENERGY | 2016-12-19 | 202.30 | 1 | 2016-12-22 | 155.80 | -23.0% |
| BALMLAWRIE | 2016-11-21 | 547.18 | 2 | 2016-12-26 | 997.98 | +82.4% |
| STCINDIA | 2016-12-26 | 187.58 | 2 | 2017-01-30 | 187.15 | -0.2% |
| LUXIND | 2016-11-15 | 765.59 | 2 | 2017-02-09 | 684.00 | -10.7% |
| SHREEPUSHK | 2016-11-07 | 189.88 | 4 | 2017-02-15 | 176.18 | -7.2% |
| CPSEETF | 2016-11-15 | 26.46 | 2 | 2017-02-17 | 24.98 | -5.6% |
| ESSELPACK | 2016-12-05 | 126.41 | 3 | 2017-02-21 | 115.95 | -8.3% |
| MONNETISPA | 2017-02-06 | 37.02 | 3 | 2017-02-27 | 33.06 | -10.7% |
| KOHINOOR | 2017-01-09 | 92.07 | 2 | 2017-03-03 | 77.53 | -15.8% |
| MAWANASUG | 2017-02-20 | 82.84 | 3 | 2017-03-29 | 81.37 | -1.8% |
| EROSMEDIA | 2017-04-03 | 264.86 | 2 | 2017-04-26 | 225.15 | -15.0% |
| DOLPHINOFF | 2016-12-19 | 125.23 | 3 | 2017-05-18 | 112.10 | -10.5% |
| MERCK | 2016-12-05 | 993.86 | 4 | 2017-05-19 | 1,045.00 | +5.1% |
| DHANBANK | 2017-03-06 | 36.73 | 4 | 2017-05-22 | 36.62 | -0.3% |
| SUNDRMFAST | 2016-08-16 | 294.27 | 4 | 2017-05-23 | 375.25 | +27.5% |
| VIJAYABANK | 2016-11-15 | 60.05 | 4 | 2017-05-23 | 78.29 | +30.4% |
| PRABHAT | 2017-02-13 | 135.86 | 2 | 2017-05-23 | 115.19 | -15.2% |
| NITINSPIN | 2017-02-20 | 115.84 | 4 | 2017-05-23 | 119.13 | +2.8% |
| RAIN | 2017-03-06 | 103.89 | 3 | 2017-05-23 | 96.95 | -6.7% |
| DAAWAT | 2017-05-29 | 74.23 | 2 | 2017-06-22 | 65.59 | -11.6% |
| VOLTAS | 2017-05-29 | 493.98 | 3 | 2017-06-23 | 456.19 | -7.6% |
| WALCHANNAG | 2017-05-29 | 174.10 | 1 | 2017-06-27 | 163.40 | -6.1% |
| SHAKTIPUMP | 2017-05-29 | 433.31 | 3 | 2017-06-28 | 415.62 | -4.1% |
| GVKPIL | 2017-07-03 | 8.55 | 2 | 2017-07-13 | 7.32 | -14.4% |
| BBL | 2017-06-27 | 1,393.02 | 2 | 2017-07-18 | 1,279.03 | -8.2% |
| ALLCARGO | 2017-05-02 | 187.48 | 2 | 2017-08-09 | 167.29 | -10.8% |
| KARURVYSYA | 2017-02-27 | 113.59 | 4 | 2017-08-10 | 128.39 | +13.0% |
| AVANTIFEED | 2017-05-29 | 1,536.93 | 2 | 2017-08-10 | 1,481.05 | -3.6% |
| EVERESTIND | 2017-06-27 | 375.99 | 2 | 2017-08-10 | 318.64 | -15.3% |
| BALAJITELE | 2017-07-24 | 188.00 | 1 | 2017-08-10 | 149.25 | -20.6% |
| VENKEYS | 2017-07-03 | 1,861.21 | 2 | 2017-08-11 | 1,719.30 | -7.6% |
| VETO | 2017-07-17 | 211.53 | 2 | 2017-08-14 | 200.31 | -5.3% |
| INSECTICID | 2017-08-14 | 847.44 | 3 | 2017-09-21 | 821.75 | -3.0% |
| BEPL | 2017-07-03 | 80.40 | 4 | 2017-09-25 | 79.33 | -1.3% |
| BEML | 2017-08-21 | 1,808.45 | 2 | 2017-09-25 | 1,744.63 | -3.5% |
| FRETAIL | 2017-08-14 | 529.87 | 4 | 2017-11-09 | 500.65 | -5.5% |
| OMMETALS | 2017-09-25 | 74.80 | 2 | 2017-11-09 | 65.75 | -12.1% |
| AVANTIFEED | 2017-08-21 | 2,350.31 | 4 | 2017-11-15 | 2,641.00 | +12.4% |
| UTTAMSUGAR | 2017-08-14 | 188.35 | 2 | 2017-12-05 | 155.58 | -17.4% |
| SHOPERSTOP | 2017-10-03 | 548.91 | 4 | 2018-01-17 | 513.28 | -6.5% |
| HATSUN | 2017-11-20 | 885.39 | 2 | 2018-01-22 | 808.92 | -8.6% |
| EKC | 2017-11-13 | 61.54 | 3 | 2018-01-30 | 55.05 | -10.6% |
| GOACARBON | 2017-06-27 | 395.02 | 4 | 2018-01-31 | 913.01 | +131.1% |
| DEN | 2017-10-03 | 113.96 | 4 | 2018-02-01 | 107.61 | -5.6% |
| GOLDINFRA | 2017-03-06 | 173.62 | 4 | 2018-02-02 | 199.60 | +15.0% |
| PRISMCEM | 2018-01-22 | 142.00 | 1 | 2018-02-02 | 125.35 | -11.7% |
| SUNTECK | 2018-01-22 | 420.50 | 1 | 2018-02-06 | 369.93 | -12.0% |
| ELGIEQUIP | 2018-02-05 | 309.10 | 2 | 2018-03-08 | 287.85 | -6.9% |
| LTI | 2017-11-13 | 1,046.84 | 4 | 2018-03-19 | 1,309.10 | +25.1% |
| LTTS | 2018-01-29 | 1,366.23 | 3 | 2018-03-19 | 1,168.00 | -14.5% |
| HOVS | 2017-05-29 | 297.15 | 3 | 2018-03-22 | 243.00 | -18.2% |
| SANWARIA | 2018-04-16 | 21.30 | 1 | 2018-04-26 | 18.00 | -15.5% |
| TAJGVK | 2018-04-23 | 228.50 | 2 | 2018-05-04 | 212.37 | -7.1% |
| ESTER | 2018-02-05 | 69.32 | 2 | 2018-05-10 | 65.17 | -6.0% |
| EXCELINDUS | 2018-04-09 | 1,214.40 | 2 | 2018-05-11 | 1,282.59 | +5.6% |
| FLFL | 2017-04-03 | 305.24 | 4 | 2018-05-21 | 407.74 | +33.6% |
| WINDMACHIN | 2018-05-14 | 139.50 | 2 | 2018-05-21 | 130.06 | -6.8% |
| LUXIND | 2018-02-05 | 1,769.42 | 4 | 2018-05-30 | 1,852.59 | +4.7% |
| DENORA | 2018-02-12 | 490.00 | 1 | 2018-06-01 | 303.38 | -38.1% |
| HIL | 2018-04-30 | 2,183.76 | 2 | 2018-06-05 | 1,939.95 | -11.2% |
| SASKEN | 2018-05-14 | 1,008.83 | 3 | 2018-06-26 | 946.20 | -6.2% |
| BODALCHEM | 2018-06-04 | 144.55 | 2 | 2018-06-26 | 129.25 | -10.6% |
| COLPAL | 2018-05-28 | 1,260.00 | 1 | 2018-07-18 | 1,116.91 | -11.4% |
| GSS | 2018-03-12 | 77.46 | 3 | 2018-07-26 | 68.61 | -11.4% |
| WHEELS | 2018-07-09 | 2,272.00 | 1 | 2018-08-08 | 2,006.50 | -11.7% |
| PAGEIND | 2018-07-02 | 31,724.70 | 4 | 2018-09-05 | 32,310.88 | +1.8% |
| TCIEXP | 2018-08-13 | 716.25 | 2 | 2018-09-05 | 652.46 | -8.9% |
| ASTRAZEN | 2018-06-18 | 1,253.70 | 4 | 2018-09-12 | 1,345.20 | +7.3% |
| GREAVESCOT | 2018-05-14 | 139.39 | 4 | 2018-09-21 | 143.78 | +3.2% |
| RBLBANK | 2018-07-23 | 592.54 | 3 | 2018-09-21 | 549.72 | -7.2% |
| ACC | 2018-07-30 | 1,570.61 | 3 | 2018-09-21 | 1,436.88 | -8.5% |
| LTI | 2018-09-10 | 1,955.00 | 1 | 2018-09-21 | 1,643.31 | -15.9% |
| SUVEN | 2018-09-17 | 310.80 | 1 | 2018-09-21 | 244.67 | -21.3% |
| ALBERTDAVD | 2018-09-17 | 770.05 | 1 | 2018-09-24 | 608.24 | -21.0% |
| MPHASIS | 2018-02-05 | 1,018.02 | 4 | 2018-09-25 | 1,173.72 | +15.3% |
| BBL | 2018-09-10 | 1,500.15 | 1 | 2018-09-27 | 1,217.66 | -18.8% |
| MUTHOOTFIN | 2018-09-10 | 460.40 | 2 | 2018-09-27 | 412.35 | -10.4% |
| GUJFLUORO | 2018-09-24 | 854.00 | 1 | 2018-09-28 | 775.25 | -9.2% |
| BIRLACABLE | 2018-11-26 | 217.45 | 2 | 2018-12-04 | 195.70 | -10.0% |
| POLYPLEX | 2018-09-10 | 612.91 | 3 | 2018-12-10 | 508.35 | -17.1% |
| DALMIASUG | 2018-11-19 | 103.00 | 2 | 2018-12-10 | 94.14 | -8.6% |
| GODFRYPHLP | 2018-12-03 | 928.20 | 2 | 2018-12-26 | 812.30 | -12.5% |
| MOHOTAIND | 2019-01-14 | 78.80 | 1 | 2019-01-17 | 69.95 | -11.2% |
| BEML | 2018-12-24 | 893.05 | 2 | 2019-01-28 | 809.88 | -9.3% |
| ADORWELD | 2019-01-14 | 394.90 | 1 | 2019-01-28 | 336.57 | -14.8% |
| KESORAMIND | 2018-12-03 | 85.00 | 1 | 2019-01-29 | 71.39 | -16.0% |
| HATHWAY | 2018-10-22 | 30.43 | 2 | 2019-02-19 | 26.93 | -11.5% |
| BAJAJHIND | 2018-10-15 | 9.98 | 2 | 2019-03-20 | 7.69 | -22.9% |
| DHAMPURSUG | 2019-03-05 | 237.23 | 2 | 2019-03-20 | 211.42 | -10.9% |
| YESBANK | 2019-02-18 | 246.96 | 3 | 2019-04-22 | 245.34 | -0.7% |
| JUSTDIAL | 2019-03-25 | 613.48 | 2 | 2019-04-22 | 565.25 | -7.9% |
| INFRATEL | 2019-02-11 | 319.80 | 2 | 2019-04-25 | 277.35 | -13.3% |
| TIIL | 2018-11-05 | 648.95 | 1 | 2019-04-30 | 502.60 | -22.6% |
| MTEDUCARE | 2019-04-30 | 85.85 | 1 | 2019-05-03 | 73.96 | -13.8% |
| SKFINDIA | 2019-01-14 | 2,015.13 | 3 | 2019-05-08 | 1,891.83 | -6.1% |
| PREMEXPLN | 2018-12-17 | 237.36 | 3 | 2019-05-10 | 214.62 | -9.6% |
| IBREALEST | 2019-04-30 | 125.40 | 1 | 2019-05-14 | 91.19 | -27.3% |
| FLFL | 2019-04-30 | 483.00 | 1 | 2019-05-16 | 434.20 | -10.1% |
| MTEDUCARE | 2019-05-13 | 94.20 | 1 | 2019-05-17 | 73.96 | -21.5% |
| AVADHSUGAR | 2019-06-03 | 696.04 | 2 | 2019-06-19 | 653.70 | -6.1% |
| RUCHISOYA | 2019-05-06 | 9.10 | 1 | 2019-06-25 | 5.61 | -38.4% |
| ONGC | 2019-04-30 | 171.00 | 3 | 2019-07-01 | 160.36 | -6.2% |
| MAHSCOOTER | 2019-06-03 | 4,477.12 | 3 | 2019-07-08 | 4,157.82 | -7.1% |
| BANKBEES | 2018-12-17 | 281.62 | 4 | 2019-07-22 | 295.55 | +4.9% |
| GRUH | 2019-05-27 | 313.00 | 1 | 2019-07-23 | 265.98 | -15.0% |
| TANLA | 2019-06-24 | 70.00 | 2 | 2019-07-30 | 60.15 | -14.1% |
| TRENT | 2019-07-15 | 458.20 | 1 | 2019-07-30 | 393.30 | -14.2% |
| INOXLEISUR | 2019-05-27 | 336.18 | 2 | 2019-07-31 | 291.23 | -13.4% |
| HEIDELBERG | 2019-04-01 | 194.04 | 4 | 2019-12-09 | 177.65 | -8.4% |
| BERGEPAINT | 2019-08-13 | 465.10 | 4 | 2020-01-08 | 484.17 | +4.1% |
| SBILIFE | 2019-06-24 | 775.47 | 4 | 2020-02-03 | 910.24 | +17.4% |
| GRSE | 2019-07-22 | 145.52 | 4 | 2020-02-03 | 177.65 | +22.1% |
| HDFCLIFE | 2019-07-29 | 554.24 | 4 | 2020-02-03 | 552.05 | -0.4% |
| KITEX | 2020-01-13 | 125.55 | 2 | 2020-02-03 | 115.04 | -8.4% |
| SMLISUZU | 2020-01-13 | 595.00 | 1 | 2020-02-27 | 523.55 | -12.0% |
| GMMPFAUDLR | 2020-02-10 | 3,195.99 | 3 | 2020-02-27 | 3,002.00 | -6.1% |
| SYMPHONY | 2020-02-10 | 1,368.26 | 2 | 2020-03-06 | 1,240.08 | -9.4% |
| FAIRCHEM | 2020-03-02 | 657.00 | 1 | 2020-03-06 | 561.73 | -14.5% |
| ALKYLAMINE | 2020-02-10 | 1,551.20 | 2 | 2020-03-09 | 1,447.61 | -6.7% |
| HDFCMFGETF | 2019-08-05 | 3,433.53 | 4 | 2020-03-13 | 3,540.65 | +3.1% |
| TRENT | 2020-02-10 | 665.00 | 1 | 2020-03-13 | 539.60 | -18.9% |
| INDOCO | 2020-03-09 | 228.20 | 1 | 2020-03-13 | 164.08 | -28.1% |
| LALPATHLAB | 2020-03-09 | 1,670.00 | 1 | 2020-03-13 | 1,486.75 | -11.0% |
| KOTAKGOLD | 2019-07-15 | 333.42 | 4 | 2020-03-17 | 352.69 | +5.8% |
| ORISSAMINE | 2020-02-10 | 1,999.68 | 2 | 2020-03-17 | 1,383.30 | -30.8% |
| SETFGOLD | 2020-03-09 | 3,862.80 | 1 | 2020-03-17 | 3,548.39 | -8.1% |
| DEEPAKNTR | 2020-03-09 | 508.80 | 1 | 2020-03-19 | 356.25 | -30.0% |

## Engine B — the complete trade blotter

*Buys, pyramid injections, sells and tax settlements; every stop raise and refused signal is in `_longrun_events_2015-03-01_to_2020-03-31.csv`, and engine A's full ledger in `_longrun_events_2015-03-01_to_2020-03-31_no_doubling.csv`.*

```
2015-03-09  ECLERX      BUY ₹9.88 at ₹1,550.00 (fresh Friday signal — BUY: 3.25× weekly, month 2.52×, ladder rising; stop ₹1,171.35; charges ₹0.01)
2015-03-09  GEOMETRIC   BUY ₹9.98 at ₹157.60 (fresh Friday signal — BUY: 6.64× weekly, month 1.62×, ladder rising; stop ₹130.15; charges ₹0.01)
2015-03-09  HCC         BUY ₹9.92 at ₹36.45 (fresh Friday signal — BUY: 3.01× weekly, month 1.69×, ladder rising; stop ₹28.57; charges ₹0.01)
2015-03-09  ITDCEM      BUY ₹10.00 at ₹76.97 (fresh Friday signal — BUY: 6.68× weekly, month 7.24×, ladder rising; stop ₹58.42; charges ₹0.01)
2015-03-09  JBMA        BUY ₹9.89 at ₹239.80 (fresh Friday signal — BUY: 2.78× weekly, month 2.63×, ladder rising; stop ₹188.60; charges ₹0.01)
2015-03-09  KEI         BUY ₹9.91 at ₹65.95 (fresh Friday signal — BUY: 3.70× weekly, month 1.68×, ladder rising; stop ₹51.77; charges ₹0.01)
2015-03-09  MADHUCON    BUY ₹9.96 at ₹63.70 (fresh Friday signal — BUY: 4.43× weekly, month 2.44×, ladder rising; stop ₹45.42; charges ₹0.01)
2015-03-09  SMLISUZU    BUY ₹9.92 at ₹1,200.00 (fresh Friday signal — BUY: 2.25× weekly, month 1.55×, ladder rising; stop ₹949.52; charges ₹0.01)
2015-03-09  SOMANYCERA  BUY ₹9.99 at ₹405.00 (fresh Friday signal — BUY: 6.10× weekly, month 1.53×, ladder rising; stop ₹336.63; charges ₹0.01)
2015-03-09  TAKE        BUY ₹9.88 at ₹147.85 (fresh Friday signal — BUY: 2.20× weekly, month 5.42×, ladder rising; stop ₹130.91; charges ₹0.01)
2015-03-16  GEOMETRIC   PYRAMID BUY ₹10.67 at ₹168.65 (box jump — doubling the stake with NEW capital; stop stays ₹145.35; charges ₹0.01)
2015-03-16  JBMA        PYRAMID BUY ₹9.76 at ₹237.00 (box jump — doubling the stake with NEW capital; stop stays ₹222.30; charges ₹0.01)
2015-03-16  KEI         PYRAMID BUY ₹9.61 at ₹64.05 (box jump — doubling the stake with NEW capital; stop stays ₹59.38; charges ₹0.01)
2015-03-16  MADHUCON    PYRAMID BUY ₹9.15 at ₹58.60 (box jump — doubling the stake with NEW capital; stop stays ₹55.38; charges ₹0.01)
2015-03-16  TAKE        SELL ₹8.72 at stop ₹130.91 (-11.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2015-03-17  MADHUCON    SELL ₹17.27 at stop ₹55.38 (-9.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-03-23  ECLERX      PYRAMID BUY ₹9.98 at ₹1,569.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,320.70; charges ₹0.01)
2015-03-23  GEOMETRIC   PYRAMID BUY ₹22.13 at ₹175.00 (box jump — doubling the stake with NEW capital; stop stays ₹158.22; charges ₹0.03)
2015-03-23  ITDCEM      PYRAMID BUY ₹9.73 at ₹74.94 (box jump — doubling the stake with NEW capital; stop stays ₹64.03; charges ₹0.01)
2015-03-23  JBMA        SELL ₹18.28 at stop ₹222.30 (-6.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-03-23  KEI         SELL ₹17.80 at stop ₹59.38 (-8.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-03-23  SOMANYCERA  PYRAMID BUY ₹9.17 at ₹372.00 (box jump — doubling the stake with NEW capital; stop stays ₹341.63; charges ₹0.01)
2015-03-23  ZYDUSWELL   BUY ₹18.44 at ₹1,051.70 (fresh Friday signal — BUY: 3.59× weekly, month 2.15×, ladder rising; stop ₹663.79; charges ₹0.02)
2015-03-30  DYNAMATECH  BUY ₹20.13 at ₹3,843.00 (fresh Friday signal — BUY: 10.44× weekly, month 3.95×, ladder rising; stop ₹3,081.75; charges ₹0.02)
2015-03-30  SOLARINDS   BUY ₹20.21 at ₹655.00 (fresh Friday signal — ACCUMULATE: 6.38× weekly, month 1.95×, ladder rising; stop ₹605.15; charges ₹0.02)
2015-03-30  ZYDUSWELL   PYRAMID BUY ₹17.95 at ₹1,025.00 (box jump — doubling the stake with NEW capital; stop stays ₹960.45; charges ₹0.02)
2015-04-01  TAX         FY2015 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹5.94 / LT ₹0.00)
2015-04-06  SMLISUZU    PYRAMID BUY ₹10.17 at ₹1,232.00 (box jump — doubling the stake with NEW capital; stop stays ₹983.70; charges ₹0.01)
2015-04-20  SOLARINDS   PYRAMID BUY ₹23.06 at ₹748.39 (box jump — doubling the stake with NEW capital; stop stays ₹694.01; charges ₹0.03)
2015-04-20  ZYDUSWELL   SELL ₹33.59 at stop ₹960.45 (-7.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2015-04-22  DYNAMATECH  SELL ₹16.11 at stop ₹3,081.75 (-19.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-04-22  GEOMETRIC   SELL ₹39.94 at stop ₹158.22 (-6.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2015-04-24  SOLARINDS   SELL ₹42.70 at stop ₹694.01 (-1.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2015-04-27  CIMMCO      BUY ₹24.93 at ₹110.55 (fresh Friday signal — ACCUMULATE: 3.65× weekly, month 2.21×, ladder rising; stop ₹66.22; charges ₹0.03)
2015-04-27  HCC         PYRAMID BUY ₹8.94 at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹31.21; charges ₹0.01)
2015-04-27  HCC         SELL ₹16.94 at stop ₹31.21 (-10.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-04-27  ITDCEM      SELL ₹16.59 at stop ₹64.03 (-15.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-04-27  MANINFRA    BUY ₹24.68 at ₹47.50 (fresh Friday signal — BUY: 2.74× weekly, month 1.90×, ladder rising; stop ₹39.19; charges ₹0.03)
2015-04-27  SOMANYCERA  PYRAMID BUY ₹19.78 at ₹401.60 (box jump — doubling the stake with NEW capital; stop stays ₹418.24; charges ₹0.02)
2015-04-27  SOMANYCERA  SELL ₹41.14 at stop ₹418.24 (+5.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2015-05-04  VADILALIND  BUY ₹25.58 at ₹487.00 (fresh Friday signal — BUY: 10.46× weekly, month 4.23×, ladder rising; stop ₹323.00; charges ₹0.03)
2015-05-11  ABIRLANUVO  BUY ₹27.80 at ₹945.00 (fresh Friday signal — BUY: 5.18× weekly, month 1.67×, ladder rising; stop ₹713.90; charges ₹0.03)
2015-05-11  VADILALIND  PYRAMID BUY ₹26.50 at ₹505.00 (box jump — doubling the stake with NEW capital; stop stays ₹451.91; charges ₹0.03)
2015-05-18  MANINDS     BUY ₹28.22 at ₹70.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 3.68×, ladder rising; stop ₹54.94; charges ₹0.03)
2015-05-18  NILKAMAL    BUY ₹27.82 at ₹524.95 (fresh Friday signal — BUY: 5.24× weekly, month 2.21×, ladder rising; stop ₹413.10; charges ₹0.03)
2015-05-18  PUNJABCHEM  BUY ₹24.05 at ₹262.80 (fresh Friday signal — BUY: 3.31× weekly, month 3.29×, ladder rising; stop ₹175.46; charges ₹0.03)
2015-05-18  REPRO       BUY ₹27.90 at ₹506.50 (fresh Friday signal — BUY: 5.22× weekly, month 2.55×, ladder rising; stop ₹368.31; charges ₹0.03)
2015-05-25  ABIRLANUVO  PYRAMID BUY ₹26.94 at ₹916.77 (box jump — doubling the stake with NEW capital; stop stays ₹850.92; charges ₹0.03)
2015-05-25  CIMMCO      PYRAMID BUY ₹22.65 at ₹100.60 (box jump — doubling the stake with NEW capital; stop stays ₹85.29; charges ₹0.03)
2015-05-25  REPRO       PYRAMID BUY ₹30.36 at ₹551.70 (box jump — doubling the stake with NEW capital; stop stays ₹404.70; charges ₹0.04)
2015-05-25  VADILALIND  PYRAMID BUY ₹52.02 at ₹496.00 (box jump — doubling the stake with NEW capital; stop stays ₹463.60; charges ₹0.06)
2015-06-03  ABIRLANUVO  SELL ₹49.93 at stop ₹850.92 (-8.6%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2015-06-03  CIMMCO      SELL ₹38.35 at stop ₹85.29 (-19.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2015-06-08  MANGALAM    BUY ₹38.42 at ₹64.10 (fresh Friday signal — BUY: 8.22× weekly, month 7.28×, ladder rising; stop ₹34.31; charges ₹0.05)
2015-06-08  TORNTPHARM  BUY ₹38.70 at ₹1,244.00 (fresh Friday signal — ACCUMULATE: 1.79× weekly, month 1.51×, ladder rising; stop ₹1,107.70; charges ₹0.05)
2015-06-22  MANINDS     PYRAMID BUY ₹29.53 at ₹73.35 (box jump — doubling the stake with NEW capital; stop stays ₹67.54; charges ₹0.03)
2015-06-22  MANINFRA    PYRAMID BUY ₹23.98 at ₹46.20 (box jump — doubling the stake with NEW capital; stop stays ₹41.18; charges ₹0.03)
2015-06-22  NILKAMAL    PYRAMID BUY ₹28.26 at ₹534.00 (box jump — doubling the stake with NEW capital; stop stays ₹479.89; charges ₹0.03)
2015-06-22  SMLISUZU    PYRAMID BUY ₹18.62 at ₹1,127.95 (box jump — doubling the stake with NEW capital; stop stays ₹997.50; charges ₹0.02)
2015-06-29  TORNTPHARM  PYRAMID BUY ₹41.42 at ₹1,332.95 (box jump — doubling the stake with NEW capital; stop stays ₹1,249.25; charges ₹0.05)
2015-07-06  MANGALAM    PYRAMID BUY ₹32.72 at ₹54.65 (box jump — doubling the stake with NEW capital; stop stays ₹36.95; charges ₹0.04)
2015-07-06  MANINDS     PYRAMID BUY ₹70.74 at ₹87.90 (box jump — doubling the stake with NEW capital; stop stays ₹81.13; charges ₹0.08)
2015-07-06  SMLISUZU    PYRAMID BUY ₹36.46 at ₹1,105.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,053.55; charges ₹0.04)
2015-07-20  MANINFRA    PYRAMID BUY ₹47.77 at ₹46.05 (box jump — doubling the stake with NEW capital; stop stays ₹41.85; charges ₹0.06)
2015-07-20  NILKAMAL    PYRAMID BUY ₹76.75 at ₹725.50 (box jump — doubling the stake with NEW capital; stop stays ₹547.82; charges ₹0.09)
2015-07-20  VADILALIND  PYRAMID BUY ₹149.87 at ₹714.95 (box jump — doubling the stake with NEW capital; stop stays ₹637.45; charges ₹0.18)
2015-07-27  MANINFRA    SELL ₹86.68 at stop ₹41.85 (-9.9%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2015-08-03  CENTENKA    BUY ₹97.84 at ₹188.40 (fresh Friday signal — BUY: 8.30× weekly, month 2.74×, ladder rising; stop ₹158.18; charges ₹0.12)
2015-08-03  MANINDS     PYRAMID BUY ₹183.38 at ₹114.00 (box jump — doubling the stake with NEW capital; stop stays ₹95.77; charges ₹0.22)
2015-08-10  CENTENKA    PYRAMID BUY ₹126.05 at ₹243.00 (box jump — doubling the stake with NEW capital; stop stays ₹173.00; charges ₹0.15)
2015-08-10  NILKAMAL    PYRAMID BUY ₹246.56 at ₹1,165.95 (box jump — doubling the stake with NEW capital; stop stays ₹730.69; charges ₹0.29)
2015-08-10  TORNTPHARM  PYRAMID BUY ₹92.61 at ₹1,491.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,330.00; charges ₹0.11)
2015-08-13  VADILALIND  SELL ₹299.88 at stop ₹716.44 (+18.3%, charges ₹0.31) — the cash goes back to work at the next Friday screen
2015-08-17  GARWALLROP  BUY ₹183.50 at ₹309.90 (fresh Friday signal — ACCUMULATE: 6.87× weekly, month 5.41×, ladder rising; stop ₹274.60; charges ₹0.22)
2015-08-17  GHCL        BUY ₹116.38 at ₹120.50 (fresh Friday signal — BUY: 6.38× weekly, month 4.31×, ladder rising; stop ₹60.81; charges ₹0.14)
2015-08-24  CENTENKA    PYRAMID BUY ₹228.10 at ₹220.00 (box jump — doubling the stake with NEW capital; stop stays ₹185.69; charges ₹0.27)
2015-08-24  ECLERX      PYRAMID BUY ₹21.37 at ₹1,680.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,531.40; charges ₹0.03)
2015-08-24  GHCL        PYRAMID BUY ₹114.69 at ₹118.90 (box jump — doubling the stake with NEW capital; stop stays ₹100.88; charges ₹0.14)
2015-08-24  MANINDS     SELL ₹307.60 at stop ₹95.77 (-1.1%, charges ₹0.32) — the cash goes back to work at the next Friday screen
2015-08-24  NILKAMAL    SELL ₹391.47 at stop ₹927.12 (+3.4%, charges ₹0.41) — the cash goes back to work at the next Friday screen
2015-08-24  PUNJABCHEM  PYRAMID BUY ₹18.74 at ₹205.00 (box jump — doubling the stake with NEW capital; stop stays ₹179.72; charges ₹0.02)
2015-08-24  PUNJABCHEM  SELL ₹32.80 at stop ₹179.72 (-23.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2015-08-24  REPRO       SELL ₹44.47 at stop ₹404.70 (-23.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2015-08-24  SMLISUZU    SELL ₹73.13 at stop ₹1,110.20 (-2.5%, charges ₹0.08) — the cash goes back to work at the next Friday screen
2015-08-25  CENTENKA    SELL ₹384.42 at stop ₹185.69 (-14.8%, charges ₹0.40) — the cash goes back to work at the next Friday screen
2015-08-25  GARWALLROP  SELL ₹162.24 at stop ₹274.60 (-11.4%, charges ₹0.17) — the cash goes back to work at the next Friday screen
2015-08-31  ICIL        BUY ₹196.08 at ₹199.78 (fresh Friday signal — ACCUMULATE: 1.94× weekly, month 2.05×, ladder rising; stop ₹145.90; charges ₹0.23)
2015-08-31  JUBLINDS    BUY ₹196.06 at ₹302.00 (fresh Friday signal — BUY: 3.23× weekly, month 8.31×, ladder rising; stop ₹200.99; charges ₹0.23)
2015-09-07  ABBOTINDIA  BUY ₹198.22 at ₹5,269.00 (fresh Friday signal — BUY: 5.86× weekly, month 1.67×, ladder rising; stop ₹4,181.09; charges ₹0.23)
2015-09-07  CAPLIPOINT  BUY ₹198.49 at ₹300.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.25×, ladder rising; stop ₹207.81; charges ₹0.24)
2015-09-07  JINDALPOLY  BUY ₹197.70 at ₹376.90 (fresh Friday signal — ACCUMULATE: 1.73× weekly, month 2.65×, ladder rising; stop ₹305.60; charges ₹0.23)
2015-09-07  MANGALAM    PYRAMID BUY ₹95.73 at ₹80.00 (box jump — doubling the stake with NEW capital; stop stays ₹73.50; charges ₹0.11)
2015-09-08  ICIL        SELL ₹142.88 at stop ₹145.90 (-27.0%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2015-09-08  MANGALAM    SELL ₹175.62 at stop ₹73.50 (+5.5%, charges ₹0.18) — the cash goes back to work at the next Friday screen
2015-09-14  CAPLIPOINT  PYRAMID BUY ₹203.55 at ₹308.00 (box jump — doubling the stake with NEW capital; stop stays ₹262.64; charges ₹0.24)
2015-09-14  CEATLTD     BUY ₹242.94 at ₹1,219.00 (fresh Friday signal — BUY: 1.70× weekly, month 1.85×, ladder rising; stop ₹857.01; charges ₹0.29)
2015-09-14  JUBLINDS    PYRAMID BUY ₹191.29 at ₹295.00 (box jump — doubling the stake with NEW capital; stop stays ₹224.21; charges ₹0.23)
2015-09-14  NEULANDLAB  BUY ₹241.75 at ₹702.80 (fresh Friday signal — BUY: 3.47× weekly, month 2.09×, ladder rising; stop ₹429.56; charges ₹0.29)
2015-09-14  VIVIMEDLAB  BUY ₹242.71 at ₹60.00 (fresh Friday signal — ACCUMULATE: 1.88× weekly, month 2.85×, ladder rising; stop ₹41.11; charges ₹0.29)
2015-09-28  ABBOTINDIA  PYRAMID BUY ₹218.69 at ₹5,819.95 (box jump — doubling the stake with NEW capital; stop stays ₹5,365.17; charges ₹0.26)
2015-09-28  CEATLTD     PYRAMID BUY ₹254.79 at ₹1,280.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,123.90; charges ₹0.30)
2015-09-28  NEULANDLAB  PYRAMID BUY ₹265.92 at ₹774.00 (box jump — doubling the stake with NEW capital; stop stays ₹668.18; charges ₹0.32)
2015-10-05  NEULANDLAB  PYRAMID BUY ₹605.01 at ₹881.00 (box jump — doubling the stake with NEW capital; stop stays ₹674.55; charges ₹0.72)
2015-10-12  JINDALPOLY  PYRAMID BUY ₹251.56 at ₹480.15 (box jump — doubling the stake with NEW capital; stop stays ₹402.90; charges ₹0.30)
2015-10-19  CEATLTD     PYRAMID BUY ₹500.72 at ₹1,258.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,131.45; charges ₹0.59)
2015-10-19  ECLERX      PYRAMID BUY ₹46.21 at ₹1,817.45 (box jump — doubling the stake with NEW capital; stop stays ₹1,548.50; charges ₹0.05)
2015-10-19  TORNTPHARM  PYRAMID BUY ₹190.31 at ₹1,532.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,426.04; charges ₹0.23)
2015-10-19  VIVIMEDLAB  PYRAMID BUY ₹274.06 at ₹67.83 (box jump — doubling the stake with NEW capital; stop stays ₹60.62; charges ₹0.32)
2015-10-26  JINDALPOLY  PYRAMID BUY ₹567.50 at ₹541.90 (box jump — doubling the stake with NEW capital; stop stays ₹451.25; charges ₹0.67)
2015-10-26  NEULANDLAB  PYRAMID BUY ₹1,109.10 at ₹808.00 (box jump — doubling the stake with NEW capital; stop stays ₹714.39; charges ₹1.31)
2015-10-28  CAPLIPOINT  SELL ₹346.57 at stop ₹262.64 (-13.6%, charges ₹0.36) — the cash goes back to work at the next Friday screen
2015-10-29  CEATLTD     SELL ₹898.88 at stop ₹1,131.45 (-9.8%, charges ₹0.93) — the cash goes back to work at the next Friday screen
2015-10-29  NEULANDLAB  SELL ₹1,958.01 at stop ₹714.39 (-11.7%, charges ₹2.03) — the cash goes back to work at the next Friday screen
2015-11-02  JINDALPOLY  PYRAMID BUY ₹1,155.56 at ₹552.05 (box jump — doubling the stake with NEW capital; stop stays ₹494.38; charges ₹1.37)
2015-11-02  JUBLINDS    SELL ₹290.30 at stop ₹224.21 (-24.9%, charges ₹0.30) — the cash goes back to work at the next Friday screen
2015-11-02  NECLIFE     BUY ₹759.45 at ₹53.70 (fresh Friday signal — BUY: 2.33× weekly, month 3.48×, ladder rising; stop ₹29.97; charges ₹0.90)
2015-11-02  NIITTECH    BUY ₹753.09 at ₹569.00 (fresh Friday signal — ACCUMULATE: 3.88× weekly, month 5.06×, ladder rising; stop ₹490.96; charges ₹0.89)
2015-11-02  TRF         BUY ₹755.82 at ₹314.40 (fresh Friday signal — BUY: 2.83× weekly, month 2.25×, ladder rising; stop ₹251.75; charges ₹0.90)
2015-11-02  UCOBANK     BUY ₹753.70 at ₹50.30 (fresh Friday signal — BUY: 4.92× weekly, month 2.00×, ladder rising; stop ₹45.79; charges ₹0.89)
2015-11-06  ABBOTINDIA  SELL ₹402.55 at stop ₹5,365.17 (-3.2%, charges ₹0.42) — the cash goes back to work at the next Friday screen
2015-11-09  GHCL        PYRAMID BUY ₹260.39 at ₹135.05 (box jump — doubling the stake with NEW capital; stop stays ₹129.53; charges ₹0.31)
2015-11-09  TRIGYN      BUY ₹767.54 at ₹55.10 (fresh Friday signal — BUY: 5.33× weekly, month 5.78×, ladder rising; stop ₹48.40; charges ₹0.91)
2015-11-09  UCOBANK     SELL ₹684.60 at stop ₹45.79 (-9.0%, charges ₹0.71) — the cash goes back to work at the next Friday screen
2015-11-16  MOREPENLAB  BUY ₹792.00 at ₹27.40 (fresh Friday signal — BUY: 4.90× weekly, month 5.22×, ladder rising; stop ₹17.34; charges ₹0.94)
2015-11-16  NECLIFE     PYRAMID BUY ₹727.48 at ₹51.50 (box jump — doubling the stake with NEW capital; stop stays ₹42.20; charges ₹0.86)
2015-11-23  NIITTECH    PYRAMID BUY ₹773.35 at ₹585.00 (box jump — doubling the stake with NEW capital; stop stays ₹529.62; charges ₹0.92)
2015-11-26  JINDALPOLY  SELL ₹2,066.33 at stop ₹494.38 (-4.7%, charges ₹2.14) — the cash goes back to work at the next Friday screen
2015-11-30  GLOBUSSPR   BUY ₹1,326.92 at ₹76.50 (fresh Friday signal — BUY: 29.71× weekly, month 8.18×, ladder rising; stop ₹48.23; charges ₹1.57)
2015-11-30  MOREPENLAB  PYRAMID BUY ₹778.07 at ₹26.95 (box jump — doubling the stake with NEW capital; stop stays ₹22.93; charges ₹0.92)
2015-11-30  NELCO       BUY ₹739.41 at ₹113.75 (fresh Friday signal — BUY: 11.41× weekly, month 3.77×, ladder rising; stop ₹62.61; charges ₹0.88)
2015-11-30  TORNTPHARM  SELL ₹353.52 at stop ₹1,426.04 (-2.4%, charges ₹0.37) — the cash goes back to work at the next Friday screen
2015-11-30  TRF         PYRAMID BUY ₹806.19 at ₹335.75 (box jump — doubling the stake with NEW capital; stop stays ₹275.60; charges ₹0.96)
2015-11-30  TRIGYN      PYRAMID BUY ₹1,275.17 at ₹91.65 (box jump — doubling the stake with NEW capital; stop stays ₹68.97; charges ₹1.51)
2015-11-30  VIVIMEDLAB  PYRAMID BUY ₹673.54 at ₹83.40 (box jump — doubling the stake with NEW capital; stop stays ₹67.66; charges ₹0.80)
2015-12-07  GLOBUSSPR   PYRAMID BUY ₹1,410.23 at ₹81.40 (box jump — doubling the stake with NEW capital; stop stays ₹65.41; charges ₹1.67)
2015-12-07  NIITTECH    PYRAMID BUY ₹1,555.42 at ₹588.65 (box jump — doubling the stake with NEW capital; stop stays ₹537.51; charges ₹1.84)
2015-12-07  TRIGYN      PYRAMID BUY ₹2,530.76 at ₹91.00 (box jump — doubling the stake with NEW capital; stop stays ₹82.94; charges ₹3.00)
2015-12-09  GHCL        SELL ₹498.68 at stop ₹129.53 (+1.7%, charges ₹0.52) — the cash goes back to work at the next Friday screen
2015-12-10  TRIGYN      SELL ₹4,605.70 at stop ₹82.94 (+0.9%, charges ₹4.78) — the cash goes back to work at the next Friday screen
2015-12-14  EDL         BUY ₹1,850.55 at ₹98.25 (fresh Friday signal — BUY: 9.13× weekly, month 22.01×, ladder rising; stop ₹68.12; charges ₹2.19)
2015-12-14  KANORICHEM  BUY ₹1,745.72 at ₹74.50 (fresh Friday signal — BUY: 4.81× weekly, month 2.89×, ladder rising; stop ₹51.20; charges ₹2.07)
2015-12-14  SHARONBIO   BUY ₹1,861.64 at ₹30.80 (fresh Friday signal — BUY: 12.91× weekly, month 1.78×, ladder rising; stop ₹11.82; charges ₹2.21)
2015-12-17  ECLERX      SELL ₹82.23 at stop ₹1,619.75 (-5.7%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2015-12-21  EDL         PYRAMID BUY ₹2,026.14 at ₹107.70 (box jump — doubling the stake with NEW capital; stop stays ₹87.83; charges ₹2.40)
2015-12-21  KANORICHEM  PYRAMID BUY ₹1,907.48 at ₹81.50 (box jump — doubling the stake with NEW capital; stop stays ₹65.32; charges ₹2.26)
2015-12-21  MOREPENLAB  PYRAMID BUY ₹1,780.28 at ₹30.85 (box jump — doubling the stake with NEW capital; stop stays ₹24.19; charges ₹2.11)
2015-12-21  NECLIFE     PYRAMID BUY ₹1,537.38 at ₹54.45 (box jump — doubling the stake with NEW capital; stop stays ₹49.46; charges ₹1.82)
2015-12-21  NELCO       PYRAMID BUY ₹691.14 at ₹106.45 (box jump — doubling the stake with NEW capital; stop stays ₹83.25; charges ₹0.82)
2015-12-21  SHARONBIO   PYRAMID BUY ₹1,811.13 at ₹30.00 (box jump — doubling the stake with NEW capital; stop stays ₹26.93; charges ₹2.15)
2015-12-21  TRF         PYRAMID BUY ₹1,967.78 at ₹410.00 (box jump — doubling the stake with NEW capital; stop stays ₹334.26; charges ₹2.33)
2015-12-21  VIVIMEDLAB  PYRAMID BUY ₹1,323.67 at ₹82.00 (box jump — doubling the stake with NEW capital; stop stays ₹72.12; charges ₹1.57)
2016-01-04  MOREPENLAB  PYRAMID BUY ₹4,544.67 at ₹39.40 (box jump — doubling the stake with NEW capital; stop stays ₹34.82; charges ₹5.38)
2016-01-07  NIITTECH    SELL ₹2,835.96 at stop ₹537.51 (-7.8%, charges ₹2.94) — the cash goes back to work at the next Friday screen
2016-01-11  ROHLTD      BUY ₹2,918.18 at ₹109.00 (fresh Friday signal — BUY: 15.78× weekly, month 50.05×, ladder rising; stop ₹54.15; charges ₹3.46)
2016-01-12  SHARONBIO   SELL ₹3,246.29 at stop ₹26.93 (-11.4%, charges ₹3.37) — the cash goes back to work at the next Friday screen
2016-01-13  EDL         SELL ₹3,299.27 at stop ₹87.83 (-14.7%, charges ₹3.42) — the cash goes back to work at the next Friday screen
2016-01-13  KANORICHEM  SELL ₹3,052.61 at stop ₹65.32 (-16.3%, charges ₹3.17) — the cash goes back to work at the next Friday screen
2016-01-13  MOREPENLAB  SELL ₹8,019.68 at stop ₹34.82 (+1.8%, charges ₹8.32) — the cash goes back to work at the next Friday screen
2016-01-13  NECLIFE     SELL ₹2,788.43 at stop ₹49.46 (-7.6%, charges ₹2.89) — the cash goes back to work at the next Friday screen
2016-01-14  TRF         SELL ₹3,203.32 at stop ₹334.26 (-9.0%, charges ₹3.32) — the cash goes back to work at the next Friday screen
2016-01-18  GLOBUSSPR   SELL ₹2,262.73 at stop ₹65.41 (-17.1%, charges ₹2.35) — the cash goes back to work at the next Friday screen
2016-01-25  SOMANYCERA  BUY ₹3,215.36 at ₹377.00 (fresh Friday signal — ACCUMULATE: 1.72× weekly, month 2.16×, ladder rising; stop ₹317.01; charges ₹3.81)
2016-02-01  PRICOL      BUY ₹3,405.42 at ₹47.90 (fresh Friday signal — BUY: 2.18× weekly, month 2.31×, ladder rising; stop ₹35.02; charges ₹4.03)
2016-02-01  ROHLTD      PYRAMID BUY ₹2,243.54 at ₹83.90 (box jump — doubling the stake with NEW capital; stop stays ₹64.83; charges ₹2.66)
2016-02-10  NELCO       SELL ₹1,079.26 at stop ₹83.25 (-24.4%, charges ₹1.12) — the cash goes back to work at the next Friday screen
2016-02-12  ROHLTD      SELL ₹3,461.54 at stop ₹64.83 (-32.8%, charges ₹3.59) — the cash goes back to work at the next Friday screen
2016-02-15  GOLDBEES    BUY ₹3,312.66 at ₹2,614.80 (fresh Friday signal — BUY: 3.06× weekly, month 1.75×, ladder rising; stop ₹2,285.70; charges ₹3.92)
2016-02-22  GOLDBEES    PYRAMID BUY ₹3,305.20 at ₹2,612.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,424.21; charges ₹3.92)
2016-02-22  PRICOL      PYRAMID BUY ₹3,724.48 at ₹52.45 (box jump — doubling the stake with NEW capital; stop stays ₹41.77; charges ₹4.41)
2016-02-29  PRICOL      SELL ₹5,922.52 at stop ₹41.77 (-16.7%, charges ₹6.14) — the cash goes back to work at the next Friday screen
2016-03-08  ENERGYDEV   BUY ₹3,936.35 at ₹56.00 (fresh Friday signal — BUY: 1.56× weekly, month 3.05×, ladder rising; stop ₹34.68; charges ₹4.66)
2016-03-08  RAMKY       BUY ₹3,898.40 at ₹55.25 (fresh Friday signal — BUY: 1.57× weekly, month 3.26×, ladder rising; stop ₹38.53; charges ₹4.62)
2016-03-14  DALMIASUG   BUY ₹4,671.51 at ₹94.05 (fresh Friday signal — BUY: 4.21× weekly, month 2.75×, ladder rising; stop ₹49.84; charges ₹5.53)
2016-03-14  GOLDBEES    PYRAMID BUY ₹6,725.35 at ₹2,659.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,476.18; charges ₹7.97)
2016-03-14  HDFCMFGETF  BUY ₹4,686.84 at ₹2,734.00 (fresh Friday signal — ACCUMULATE: 1.54× weekly, month 1.73×, ladder rising; stop ₹2,484.30; charges ₹5.55)
2016-03-21  SOMANYCERA  PYRAMID BUY ₹3,202.60 at ₹375.95 (box jump — doubling the stake with NEW capital; stop stays ₹337.25; charges ₹3.79)
2016-03-28  DALMIASUG   PYRAMID BUY ₹5,159.61 at ₹104.00 (box jump — doubling the stake with NEW capital; stop stays ₹86.86; charges ₹6.11)
2016-03-28  ENERGYDEV   PYRAMID BUY ₹4,753.12 at ₹67.70 (box jump — doubling the stake with NEW capital; stop stays ₹48.84; charges ₹5.63)
2016-03-28  MCLEODRUSS  BUY ₹5,963.99 at ₹184.00 (fresh Friday signal — ACCUMULATE: 3.85× weekly, month 1.53×, ladder rising; stop ₹166.63; charges ₹7.07)
2016-04-01  TAX         FY2016 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹6,722.55 / LT ₹0.00)
2016-04-04  ENERGYDEV   PYRAMID BUY ₹9,542.72 at ₹68.00 (box jump — doubling the stake with NEW capital; stop stays ₹60.80; charges ₹11.31)
2016-04-11  SOMANYCERA  PYRAMID BUY ₹6,674.70 at ₹392.00 (box jump — doubling the stake with NEW capital; stop stays ₹351.50; charges ₹7.91)
2016-04-12  ENERGYDEV   SELL ₹17,036.84 at stop ₹60.80 (-6.3%, charges ₹17.67) — the cash goes back to work at the next Friday screen
2016-04-18  ATLASCYCLE  BUY ₹4,968.27 at ₹212.40 (fresh Friday signal — ACCUMULATE: 7.41× weekly, month 2.46×, ladder rising; stop ₹170.09; charges ₹5.89)
2016-04-18  RSSOFTWARE  BUY ₹7,645.44 at ₹117.40 (fresh Friday signal — BUY: 10.97× weekly, month 3.36×, ladder rising; stop ₹68.78; charges ₹9.06)
2016-04-18  VSTTILLERS  BUY ₹7,668.28 at ₹1,797.00 (fresh Friday signal — BUY: 9.68× weekly, month 1.84×, ladder rising; stop ₹1,234.43; charges ₹9.09)
2016-05-02  GOLDBEES    PYRAMID BUY ₹13,781.46 at ₹2,726.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,508.05; charges ₹16.33)
2016-05-02  RSSOFTWARE  PYRAMID BUY ₹6,829.82 at ₹105.00 (box jump — doubling the stake with NEW capital; stop stays ₹93.44; charges ₹8.09)
2016-05-02  VSTTILLERS  PYRAMID BUY ₹7,566.06 at ₹1,775.15 (box jump — doubling the stake with NEW capital; stop stays ₹1,643.64; charges ₹8.96)
2016-05-09  RAMKY       PYRAMID BUY ₹3,816.26 at ₹54.15 (box jump — doubling the stake with NEW capital; stop stays ₹49.76; charges ₹4.52)
2016-05-09  SOMANYCERA  PYRAMID BUY ₹14,209.37 at ₹417.50 (box jump — doubling the stake with NEW capital; stop stays ₹382.85; charges ₹16.84)
2016-05-16  HDFCMFGETF  PYRAMID BUY ₹4,802.85 at ₹2,805.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,629.60; charges ₹5.69)
2016-05-16  MCLEODRUSS  PYRAMID BUY ₹6,047.57 at ₹186.80 (box jump — doubling the stake with NEW capital; stop stays ₹169.72; charges ₹7.17)
2016-05-18  RSSOFTWARE  SELL ₹12,135.98 at stop ₹93.44 (-16.0%, charges ₹12.59) — the cash goes back to work at the next Friday screen
2016-05-23  TPLPLASTEH  BUY ₹12,135.98 at ₹513.50 (fresh Friday signal — BUY: 16.66× weekly, month 19.21×, ladder rising; stop ₹343.95; charges ₹14.38)
2016-05-24  DALMIASUG   SELL ₹8,604.51 at stop ₹86.86 (-12.3%, charges ₹8.93) — the cash goes back to work at the next Friday screen
2016-05-30  ATLASCYCLE  PYRAMID BUY ₹4,724.08 at ₹202.20 (box jump — doubling the stake with NEW capital; stop stays ₹186.20; charges ₹5.60)
2016-05-30  GUJALKALI   BUY ₹8,604.51 at ₹215.75 (fresh Friday signal — BUY: 7.86× weekly, month 2.80×, ladder rising; stop ₹180.74; charges ₹10.19)
2016-05-30  TPLPLASTEH  PYRAMID BUY ₹11,212.78 at ₹475.00 (box jump — doubling the stake with NEW capital; stop stays ₹352.26; charges ₹13.29)
2016-05-30  VSTTILLERS  PYRAMID BUY ₹16,033.46 at ₹1,882.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,681.50; charges ₹19.00)
2016-05-31  VIVIMEDLAB  SELL ₹2,559.88 at stop ₹79.42 (+2.1%, charges ₹2.66) — the cash goes back to work at the next Friday screen
2016-06-06  GUJALKALI   PYRAMID BUY ₹8,588.34 at ₹215.60 (box jump — doubling the stake with NEW capital; stop stays ₹197.74; charges ₹10.18)
2016-06-13  RAMKY       PYRAMID BUY ₹10,170.66 at ₹72.20 (box jump — doubling the stake with NEW capital; stop stays ₹59.65; charges ₹12.05)
2016-06-27  VSTTILLERS  PYRAMID BUY ₹32,780.16 at ₹1,925.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,758.45; charges ₹38.84)
2016-07-04  HDFCMFGETF  PYRAMID BUY ₹9,849.85 at ₹2,878.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,691.35; charges ₹11.67)
2016-07-04  TPLPLASTEH  PYRAMID BUY ₹22,648.19 at ₹480.00 (box jump — doubling the stake with NEW capital; stop stays ₹382.18; charges ₹26.83)
2016-07-18  ATLASCYCLE  PYRAMID BUY ₹10,005.28 at ₹214.25 (box jump — doubling the stake with NEW capital; stop stays ₹193.51; charges ₹11.85)
2016-07-18  GUJALKALI   PYRAMID BUY ₹17,676.08 at ₹222.00 (box jump — doubling the stake with NEW capital; stop stays ₹209.05; charges ₹20.94)
2016-07-18  MCLEODRUSS  PYRAMID BUY ₹13,699.27 at ₹211.70 (box jump — doubling the stake with NEW capital; stop stays ₹198.74; charges ₹16.23)
2016-07-18  TPLPLASTEH  PYRAMID BUY ₹46,905.85 at ₹497.35 (box jump — doubling the stake with NEW capital; stop stays ₹465.74; charges ₹55.58)
2016-07-19  MCLEODRUSS  SELL ₹25,679.36 at stop ₹198.74 (+0.1%, charges ₹26.64) — the cash goes back to work at the next Friday screen
2016-07-22  TPLPLASTEH  SELL ₹87,706.31 at stop ₹465.74 (-5.4%, charges ₹90.98) — the cash goes back to work at the next Friday screen
2016-07-25  DBCORP      BUY ₹38,614.84 at ₹410.00 (fresh Friday signal — BUY: 7.57× weekly, month 2.54×, ladder rising; stop ₹345.13; charges ₹45.75)
2016-07-25  RAMKY       PYRAMID BUY ₹26,312.60 at ₹93.45 (box jump — doubling the stake with NEW capital; stop stays ₹79.04; charges ₹31.18)
2016-07-25  TATAMETALI  BUY ₹38,569.24 at ₹453.00 (fresh Friday signal — BUY: 7.99× weekly, month 6.02×, ladder rising; stop ₹304.18; charges ₹45.70)
2016-07-25  UFO         BUY ₹38,689.32 at ₹602.25 (fresh Friday signal — ACCUMULATE: 8.26× weekly, month 1.91×, ladder rising; stop ₹510.05; charges ₹45.84)
2016-08-01  HDFCMFGETF  PYRAMID BUY ₹19,893.26 at ₹2,908.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,694.68; charges ₹23.57)
2016-08-01  VSTTILLERS  SELL ₹62,100.32 at stop ₹1,826.38 (-2.8%, charges ₹64.42) — the cash goes back to work at the next Friday screen
2016-08-08  DBCORP      PYRAMID BUY ₹38,931.26 at ₹413.85 (box jump — doubling the stake with NEW capital; stop stays ₹377.25; charges ₹46.13)
2016-08-08  RAIN        BUY ₹46,324.61 at ₹39.00 (fresh Friday signal — BUY: 9.00× weekly, month 1.85×, ladder rising; stop ₹27.70; charges ₹54.89)
2016-08-08  TATAMETALI  PYRAMID BUY ₹37,341.47 at ₹439.10 (box jump — doubling the stake with NEW capital; stop stays ₹366.19; charges ₹44.24)
2016-08-10  RAMKY       SELL ₹44,437.92 at stop ₹79.04 (+0.8%, charges ₹46.10) — the cash goes back to work at the next Friday screen
2016-08-16  GUJALKALI   PYRAMID BUY ₹45,214.42 at ₹284.10 (box jump — doubling the stake with NEW capital; stop stays ₹250.14; charges ₹53.57)
2016-08-16  SUNDRMFAST  BUY ₹50,482.99 at ₹234.00 (fresh Friday signal — BUY: 7.63× weekly, month 4.43×, ladder rising; stop ₹176.94; charges ₹59.81)
2016-08-16  UFO         SELL ₹32,693.54 at stop ₹510.05 (-15.3%, charges ₹33.91) — the cash goes back to work at the next Friday screen
2016-08-22  KSL         BUY ₹42,496.33 at ₹382.00 (fresh Friday signal — BUY: 3.58× weekly, month 8.08×, ladder rising; stop ₹259.35; charges ₹50.35)
2016-08-22  RAIN        PYRAMID BUY ₹49,235.73 at ₹41.50 (box jump — doubling the stake with NEW capital; stop stays ₹34.58; charges ₹58.34)
2016-08-29  DBCORP      PYRAMID BUY ₹77,534.35 at ₹412.35 (box jump — doubling the stake with NEW capital; stop stays ₹382.47; charges ₹91.86)
2016-08-29  KSL         PYRAMID BUY ₹40,279.23 at ₹362.50 (box jump — doubling the stake with NEW capital; stop stays ₹337.73; charges ₹47.72)
2016-08-29  SUNDRMFAST  PYRAMID BUY ₹59,365.75 at ₹275.50 (box jump — doubling the stake with NEW capital; stop stays ₹256.98; charges ₹70.34)
2016-09-01  KSL         SELL ₹74,931.63 at stop ₹337.73 (-9.3%, charges ₹77.73) — the cash goes back to work at the next Friday screen
2016-09-06  RAIN        PYRAMID BUY ₹1.08 lakh at ₹45.40 (box jump — doubling the stake with NEW capital; stop stays ₹42.08; charges ₹127.56)
2016-09-06  UNIPLY      BUY ₹74,931.63 at ₹52.72 (fresh Friday signal — BUY: 9.06× weekly, month 3.11×, ladder rising; stop ₹36.86; charges ₹88.78)
2016-09-12  UNIPLY      PYRAMID BUY ₹82,906.35 at ₹58.40 (box jump — doubling the stake with NEW capital; stop stays ₹44.11; charges ₹98.23)
2016-09-21  SOMANYCERA  SELL ₹37,451.66 at stop ₹551.10 (+37.5%, charges ₹38.85) — the cash goes back to work at the next Friday screen
2016-09-26  ATLASCYCLE  PYRAMID BUY ₹24,362.48 at ₹261.00 (box jump — doubling the stake with NEW capital; stop stays ₹235.69; charges ₹28.87)
2016-09-29  DBCORP      SELL ₹1.44 lakh at stop ₹382.47 (-7.2%, charges ₹148.95) — the cash goes back to work at the next Friday screen
2016-09-29  GUJALKALI   SELL ₹91,171.40 at stop ₹286.90 (+14.1%, charges ₹94.57) — the cash goes back to work at the next Friday screen
2016-09-29  TATAMETALI  SELL ₹62,180.87 at stop ₹366.19 (-17.9%, charges ₹64.50) — the cash goes back to work at the next Friday screen
2016-10-03  GLOBUSSPR   BUY ₹97,301.03 at ₹108.10 (fresh Friday signal — BUY: 11.16× weekly, month 4.83×, ladder rising; stop ₹71.55; charges ₹115.28)
2016-10-03  TVSSRICHAK  BUY ₹97,743.64 at ₹4,077.00 (fresh Friday signal — BUY: 15.60× weekly, month 4.39×, ladder rising; stop ₹2,467.20; charges ₹115.81)
2016-10-03  VIVIMEDLAB  BUY ₹97,303.33 at ₹114.00 (fresh Friday signal — BUY: 26.46× weekly, month 6.60×, ladder rising; stop ₹79.89; charges ₹115.29)
2016-10-10  GLOBUSSPR   PYRAMID BUY ₹95,387.68 at ₹106.10 (box jump — doubling the stake with NEW capital; stop stays ₹95.00; charges ₹113.02)
2016-10-10  TVSSRICHAK  PYRAMID BUY ₹93,030.20 at ₹3,885.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,633.84; charges ₹110.22)
2016-10-24  UNIPLY      PYRAMID BUY ₹1.55 lakh at ₹54.47 (box jump — doubling the stake with NEW capital; stop stays ₹50.16; charges ₹183.13)
2016-10-24  VIVIMEDLAB  PYRAMID BUY ₹97,188.04 at ₹114.00 (box jump — doubling the stake with NEW capital; stop stays ₹99.84; charges ₹115.15)
2016-11-04  GLOBUSSPR   SELL ₹1.71 lakh at stop ₹95.00 (-11.3%, charges ₹176.90) — the cash goes back to work at the next Friday screen
2016-11-04  UNIPLY      SELL ₹2.84 lakh at stop ₹50.16 (-8.8%, charges ₹294.80) — the cash goes back to work at the next Friday screen
2016-11-04  VIVIMEDLAB  SELL ₹1.70 lakh at stop ₹99.84 (-12.4%, charges ₹176.29) — the cash goes back to work at the next Friday screen
2016-11-07  SESHAPAPER  BUY ₹1.35 lakh at ₹164.20 (fresh Friday signal — BUY: 2.47× weekly, month 6.45×, ladder rising; stop ₹113.48; charges ₹160.29)
2016-11-07  SHREEPUSHK  BUY ₹1.35 lakh at ₹182.10 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 4.98×, ladder rising; stop ₹143.41; charges ₹160.37)
2016-11-07  STARPAPER   BUY ₹1.35 lakh at ₹168.00 (fresh Friday signal — BUY: 1.64× weekly, month 3.32×, ladder rising; stop ₹113.76; charges ₹159.64)
2016-11-09  RAIN        SELL ₹1.99 lakh at stop ₹42.08 (-1.7%, charges ₹206.68) — the cash goes back to work at the next Friday screen
2016-11-09  TVSSRICHAK  SELL ₹1.74 lakh at stop ₹3,633.84 (-8.7%, charges ₹180.23) — the cash goes back to work at the next Friday screen
2016-11-15  CPSEETF     BUY ₹1.26 lakh at ₹25.10 (fresh Friday signal — BUY: 2.33× weekly, month 3.31×, ladder rising; stop ₹23.40; charges ₹149.72)
2016-11-15  HONDAPOWER  BUY ₹1.26 lakh at ₹1,556.00 (fresh Friday signal — ACCUMULATE: 2.24× weekly, month 1.89×, ladder rising; stop ₹1,438.87; charges ₹149.37)
2016-11-15  LUXIND      BUY ₹1.25 lakh at ₹799.20 (fresh Friday signal — BUY: 1.59× weekly, month 1.98×, ladder rising; stop ₹669.75; charges ₹148.64)
2016-11-15  VIJAYABANK  BUY ₹1.27 lakh at ₹49.55 (fresh Friday signal — BUY: 5.15× weekly, month 2.83×, ladder rising; stop ₹37.62; charges ₹150.05)
2016-11-17  GOLDBEES    SELL ₹27,151.01 at stop ₹2,689.64 (+0.3%, charges ₹28.16) — the cash goes back to work at the next Friday screen
2016-11-18  HDFCMFGETF  SELL ₹37,138.74 at stop ₹2,718.90 (-5.1%, charges ₹38.52) — the cash goes back to work at the next Friday screen
2016-11-18  HONDAPOWER  SELL ₹1.16 lakh at stop ₹1,438.87 (-7.5%, charges ₹120.66) — the cash goes back to work at the next Friday screen
2016-11-21  BALMLAWRIE  BUY ₹1.17 lakh at ₹849.00 (fresh Friday signal — ACCUMULATE: 1.75× weekly, month 2.76×, ladder rising; stop ₹768.17; charges ₹138.89)
2016-11-22  SESHAPAPER  SELL ₹93,290.28 at stop ₹113.48 (-30.9%, charges ₹96.77) — the cash goes back to work at the next Friday screen
2016-11-28  LUXIND      PYRAMID BUY ₹1.15 lakh at ₹731.95 (box jump — doubling the stake with NEW capital; stop stays ₹684.00; charges ₹135.97)
2016-11-28  STARPAPER   PYRAMID BUY ₹1.46 lakh at ₹182.00 (box jump — doubling the stake with NEW capital; stop stays ₹119.08; charges ₹172.74)
2016-12-05  ESSELPACK   BUY ₹1.63 lakh at ₹126.50 (fresh Friday signal — BUY: 4.47× weekly, month 2.09×, ladder rising; stop ₹104.50; charges ₹193.48)
2016-12-05  MERCK       BUY ₹1.23 lakh at ₹962.00 (fresh Friday signal — BUY: 2.25× weekly, month 3.58×, ladder rising; stop ₹816.81; charges ₹145.98)
2016-12-05  VIJAYABANK  PYRAMID BUY ₹1.13 lakh at ₹44.25 (box jump — doubling the stake with NEW capital; stop stays ₹39.32; charges ₹133.85)
2016-12-12  ESSELPACK   PYRAMID BUY ₹1.63 lakh at ₹126.12 (box jump — doubling the stake with NEW capital; stop stays ₹114.95; charges ₹192.68)
2016-12-12  MERCK       PYRAMID BUY ₹1.27 lakh at ₹991.00 (box jump — doubling the stake with NEW capital; stop stays ₹902.78; charges ₹150.21)
2016-12-12  SHREEPUSHK  PYRAMID BUY ₹1.28 lakh at ₹173.00 (box jump — doubling the stake with NEW capital; stop stays ₹151.34; charges ₹152.18)
2016-12-12  STARPAPER   PYRAMID BUY ₹3.02 lakh at ₹188.75 (box jump — doubling the stake with NEW capital; stop stays ₹175.94; charges ₹358.08)
2016-12-13  STARPAPER   SELL ₹5.63 lakh at stop ₹175.94 (-3.3%, charges ₹583.49) — the cash goes back to work at the next Friday screen
2016-12-19  DOLPHINOFF  BUY ₹2.29 lakh at ₹129.70 (fresh Friday signal — BUY: 2.99× weekly, month 3.74×, ladder rising; stop ₹108.68; charges ₹271.45)
2016-12-19  SWANENERGY  BUY ₹2.34 lakh at ₹202.30 (fresh Friday signal — BUY: 6.50× weekly, month 6.89×, ladder rising; stop ₹155.80; charges ₹276.80)
2016-12-22  SWANENERGY  SELL ₹1.80 lakh at stop ₹155.80 (-23.0%, charges ₹186.22) — the cash goes back to work at the next Friday screen
2016-12-26  BALMLAWRIE  PYRAMID BUY ₹33,787.27 at ₹245.00 (box jump — doubling the stake with NEW capital; stop stays ₹997.98; charges ₹40.03)
2016-12-26  BALMLAWRIE  SELL ₹2.75 lakh at stop ₹997.98 (+82.4%, charges ₹285.06) — the cash goes back to work at the next Friday screen
2016-12-26  STCINDIA    BUY ₹2.10 lakh at ₹152.20 (fresh Friday signal — BUY: 3.37× weekly, month 1.67×, ladder rising; stop ₹109.25; charges ₹249.08)
2017-01-09  KOHINOOR    BUY ₹2.72 lakh at ₹91.50 (fresh Friday signal — BUY: 7.58× weekly, month 6.18×, ladder rising; stop ₹53.92; charges ₹322.66)
2017-01-09  SUNDRMFAST  PYRAMID BUY ₹1.32 lakh at ₹306.40 (box jump — doubling the stake with NEW capital; stop stays ₹269.13; charges ₹156.36)
2017-01-16  STCINDIA    PYRAMID BUY ₹3.08 lakh at ₹223.00 (box jump — doubling the stake with NEW capital; stop stays ₹187.15; charges ₹364.52)
2017-01-16  SUNDRMFAST  PYRAMID BUY ₹2.65 lakh at ₹308.00 (box jump — doubling the stake with NEW capital; stop stays ₹283.29; charges ₹314.17)
2017-01-23  KOHINOOR    PYRAMID BUY ₹2.75 lakh at ₹92.65 (box jump — doubling the stake with NEW capital; stop stays ₹77.53; charges ₹326.33)
2017-01-23  SHREEPUSHK  PYRAMID BUY ₹2.91 lakh at ₹196.00 (box jump — doubling the stake with NEW capital; stop stays ₹172.04; charges ₹344.61)
2017-01-30  CPSEETF     PYRAMID BUY ₹1.40 lakh at ₹27.83 (box jump — doubling the stake with NEW capital; stop stays ₹24.98; charges ₹165.81)
2017-01-30  ESSELPACK   PYRAMID BUY ₹3.26 lakh at ₹126.50 (box jump — doubling the stake with NEW capital; stop stays ₹115.95; charges ₹386.27)
2017-01-30  STCINDIA    SELL ₹5.16 lakh at stop ₹187.15 (-0.2%, charges ₹534.78) — the cash goes back to work at the next Friday screen
2017-02-06  MONNETISPA  BUY ₹4.39 lakh at ₹34.85 (fresh Friday signal — BUY: 12.75× weekly, month 9.82×, ladder rising; stop ₹24.32; charges ₹519.86)
2017-02-09  LUXIND      SELL ₹2.14 lakh at stop ₹684.00 (-10.7%, charges ₹222.13) — the cash goes back to work at the next Friday screen
2017-02-13  MERCK       PYRAMID BUY ₹2.53 lakh at ₹991.00 (box jump — doubling the stake with NEW capital; stop stays ₹919.79; charges ₹300.23)
2017-02-13  MONNETISPA  PYRAMID BUY ₹4.81 lakh at ₹38.25 (box jump — doubling the stake with NEW capital; stop stays ₹31.54; charges ₹569.90)
2017-02-13  PRABHAT     BUY ₹3.62 lakh at ₹144.65 (fresh Friday signal — BUY: 7.47× weekly, month 2.18×, ladder rising; stop ₹102.51; charges ₹429.48)
2017-02-13  SHREEPUSHK  PYRAMID BUY ₹5.72 lakh at ₹193.00 (box jump — doubling the stake with NEW capital; stop stays ₹176.18; charges ₹678.27)
2017-02-15  SHREEPUSHK  SELL ₹10.43 lakh at stop ₹176.18 (-7.2%, charges ₹1,082.38) — the cash goes back to work at the next Friday screen
2017-02-17  CPSEETF     SELL ₹2.51 lakh at stop ₹24.98 (-5.6%, charges ₹260.17) — the cash goes back to work at the next Friday screen
2017-02-20  MAWANASUG   BUY ₹6.17 lakh at ₹79.50 (fresh Friday signal — BUY: 6.41× weekly, month 3.50×, ladder rising; stop ₹55.99; charges ₹731.16)
2017-02-20  MONNETISPA  PYRAMID BUY ₹9.43 lakh at ₹37.50 (box jump — doubling the stake with NEW capital; stop stays ₹33.06; charges ₹1,116.78)
2017-02-20  NITINSPIN   BUY ₹6.77 lakh at ₹96.00 (fresh Friday signal — BUY: 7.78× weekly, month 3.17×, ladder rising; stop ₹78.99; charges ₹802.32)
2017-02-20  VIJAYABANK  PYRAMID BUY ₹3.31 lakh at ₹64.90 (box jump — doubling the stake with NEW capital; stop stays ₹56.94; charges ₹392.38)
2017-02-21  ESSELPACK   SELL ₹5.97 lakh at stop ₹115.95 (-8.3%, charges ₹618.94) — the cash goes back to work at the next Friday screen
2017-02-27  KARURVYSYA  BUY ₹5.97 lakh at ₹99.65 (fresh Friday signal — BUY: 5.67× weekly, month 2.66×, ladder rising; stop ₹85.97; charges ₹706.97)
2017-02-27  MONNETISPA  SELL ₹16.59 lakh at stop ₹33.06 (-10.7%, charges ₹1,721.13) — the cash goes back to work at the next Friday screen
2017-02-27  PRABHAT     PYRAMID BUY ₹3.18 lakh at ₹127.05 (box jump — doubling the stake with NEW capital; stop stays ₹115.19; charges ₹376.78)
2017-03-03  KOHINOOR    SELL ₹4.60 lakh at stop ₹77.53 (-15.8%, charges ₹477.36) — the cash goes back to work at the next Friday screen
2017-03-06  DHANBANK    BUY ₹7.49 lakh at ₹29.45 (fresh Friday signal — BUY: 7.14× weekly, month 2.95×, ladder rising; stop ₹22.32; charges ₹887.16)
2017-03-06  GOLDINFRA   BUY ₹6.21 lakh at ₹57.60 (fresh Friday signal — BUY: 3.22× weekly, month 17.82×, ladder rising; stop ₹43.03; charges ₹736.18)
2017-03-06  MAWANASUG   PYRAMID BUY ₹6.27 lakh at ₹80.85 (box jump — doubling the stake with NEW capital; stop stays ₹67.73; charges ₹742.69)
2017-03-06  RAIN        BUY ₹7.49 lakh at ₹99.80 (fresh Friday signal — BUY: 3.51× weekly, month 4.51×, ladder rising; stop ₹72.39; charges ₹887.81)
2017-03-14  KARURVYSYA  PYRAMID BUY ₹5.98 lakh at ₹100.00 (box jump — doubling the stake with NEW capital; stop stays ₹91.82; charges ₹708.61)
2017-03-14  MERCK       PYRAMID BUY ₹5.13 lakh at ₹1,004.00 (box jump — doubling the stake with NEW capital; stop stays ₹941.26; charges ₹607.98)
2017-03-20  NITINSPIN   PYRAMID BUY ₹6.97 lakh at ₹99.00 (box jump — doubling the stake with NEW capital; stop stays ₹85.88; charges ₹826.41)
2017-03-20  RAIN        PYRAMID BUY ₹7.65 lakh at ₹101.95 (box jump — doubling the stake with NEW capital; stop stays ₹93.77; charges ₹905.86)
2017-03-20  VIJAYABANK  PYRAMID BUY ₹6.55 lakh at ₹64.20 (box jump — doubling the stake with NEW capital; stop stays ₹59.24; charges ₹775.84)
2017-03-27  MAWANASUG   PYRAMID BUY ₹13.25 lakh at ₹85.50 (box jump — doubling the stake with NEW capital; stop stays ₹81.37; charges ₹1,569.89)
2017-03-27  NITINSPIN   PYRAMID BUY ₹15.49 lakh at ₹110.00 (box jump — doubling the stake with NEW capital; stop stays ₹91.25; charges ₹1,835.37)
2017-03-29  MAWANASUG   SELL ₹25.18 lakh at stop ₹81.37 (-1.8%, charges ₹2,611.81) — the cash goes back to work at the next Friday screen
2017-04-03  DHANBANK    PYRAMID BUY ₹7.67 lakh at ₹30.20 (box jump — doubling the stake with NEW capital; stop stays ₹24.70; charges ₹908.68)
2017-04-03  EROSMEDIA   BUY ₹9.61 lakh at ₹276.80 (fresh Friday signal — BUY: 6.24× weekly, month 4.26×, ladder rising; stop ₹187.60; charges ₹1,138.46)
2017-04-03  FLFL        BUY ₹15.57 lakh at ₹279.25 (fresh Friday signal — BUY: 19.50× weekly, month 7.20×, ladder rising; stop ₹171.00; charges ₹1,844.78)
2017-04-03  TAX         FY2017 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹6.37 lakh / LT ₹0.00)
2017-04-10  DOLPHINOFF  PYRAMID BUY ₹2.27 lakh at ₹128.40 (box jump — doubling the stake with NEW capital; stop stays ₹110.15; charges ₹268.41)
2017-04-10  NITINSPIN   PYRAMID BUY ₹36.02 lakh at ₹127.95 (box jump — doubling the stake with NEW capital; stop stays ₹107.54; charges ₹4,267.22)
2017-04-17  KARURVYSYA  PYRAMID BUY ₹14.24 lakh at ₹119.15 (box jump — doubling the stake with NEW capital; stop stays ₹107.54; charges ₹1,687.61)
2017-04-17  RAIN        PYRAMID BUY ₹16.02 lakh at ₹106.90 (box jump — doubling the stake with NEW capital; stop stays ₹96.95; charges ₹1,898.56)
2017-04-24  EROSMEDIA   PYRAMID BUY ₹8.77 lakh at ₹252.90 (box jump — doubling the stake with NEW capital; stop stays ₹225.15; charges ₹1,038.93)
2017-04-24  FLFL        PYRAMID BUY ₹15.82 lakh at ₹284.00 (box jump — doubling the stake with NEW capital; stop stays ₹253.13; charges ₹1,873.94)
2017-04-24  KARURVYSYA  PYRAMID BUY ₹28.12 lakh at ₹117.70 (box jump — doubling the stake with NEW capital; stop stays ₹110.29; charges ₹3,332.18)
2017-04-26  EROSMEDIA   SELL ₹15.59 lakh at stop ₹225.15 (-15.0%, charges ₹1,616.90) — the cash goes back to work at the next Friday screen
2017-05-02  ALLCARGO    BUY ₹15.59 lakh at ₹190.00 (fresh Friday signal — BUY: 10.92× weekly, month 3.68×, ladder rising; stop ₹158.32; charges ₹1,846.85)
2017-05-02  DHANBANK    PYRAMID BUY ₹19.69 lakh at ₹38.80 (box jump — doubling the stake with NEW capital; stop stays ₹30.50; charges ₹2,333.50)
2017-05-15  ALLCARGO    PYRAMID BUY ₹15.16 lakh at ₹184.95 (box jump — doubling the stake with NEW capital; stop stays ₹167.29; charges ₹1,795.63)
2017-05-15  DHANBANK    PYRAMID BUY ₹39.72 lakh at ₹39.15 (box jump — doubling the stake with NEW capital; stop stays ₹36.62; charges ₹4,706.31)
2017-05-15  DOLPHINOFF  PYRAMID BUY ₹4.28 lakh at ₹121.40 (box jump — doubling the stake with NEW capital; stop stays ₹112.10; charges ₹507.26)
2017-05-18  DOLPHINOFF  SELL ₹7.89 lakh at stop ₹112.10 (-10.5%, charges ₹818.83) — the cash goes back to work at the next Friday screen
2017-05-19  MERCK       SELL ₹10.66 lakh at stop ₹1,045.00 (+5.1%, charges ₹1,106.24) — the cash goes back to work at the next Friday screen
2017-05-22  DHANBANK    SELL ₹74.19 lakh at stop ₹36.62 (-0.3%, charges ₹7,695.59) — the cash goes back to work at the next Friday screen
2017-05-22  FLFL        PYRAMID BUY ₹32.28 lakh at ₹290.00 (box jump — doubling the stake with NEW capital; stop stays ₹266.90; charges ₹3,824.80)
2017-05-23  NITINSPIN   SELL ₹66.96 lakh at stop ₹119.13 (+2.8%, charges ₹6,945.45) — the cash goes back to work at the next Friday screen
2017-05-23  PRABHAT     SELL ₹5.76 lakh at stop ₹115.19 (-15.2%, charges ₹597.17) — the cash goes back to work at the next Friday screen
2017-05-23  RAIN        SELL ₹29.02 lakh at stop ₹96.95 (-6.7%, charges ₹3,010.02) — the cash goes back to work at the next Friday screen
2017-05-23  SUNDRMFAST  SELL ₹6.45 lakh at stop ₹375.25 (+27.5%, charges ₹669.13) — the cash goes back to work at the next Friday screen
2017-05-23  VIJAYABANK  SELL ₹15.94 lakh at stop ₹78.29 (+30.4%, charges ₹1,653.93) — the cash goes back to work at the next Friday screen
2017-05-29  AVANTIFEED  BUY ₹29.76 lakh at ₹1,423.00 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 4.65×, ladder rising; stop ₹1,187.50; charges ₹3,526.10)
2017-05-29  DAAWAT      BUY ₹37.48 lakh at ₹75.85 (fresh Friday signal — BUY: 3.24× weekly, month 1.54×, ladder rising; stop ₹59.66; charges ₹4,440.34)
2017-05-29  HOVS        BUY ₹37.42 lakh at ₹324.70 (fresh Friday signal — BUY: 2.64× weekly, month 2.39×, ladder rising; stop ₹189.53; charges ₹4,433.39)
2017-05-29  SHAKTIPUMP  BUY ₹37.44 lakh at ₹402.00 (fresh Friday signal — BUY: 12.55× weekly, month 12.33×, ladder rising; stop ₹248.90; charges ₹4,436.48)
2017-05-29  VOLTAS      BUY ₹37.57 lakh at ₹496.90 (fresh Friday signal — BUY: 4.55× weekly, month 1.70×, ladder rising; stop ₹383.23; charges ₹4,451.88)
2017-05-29  WALCHANNAG  BUY ₹37.20 lakh at ₹174.10 (fresh Friday signal — ACCUMULATE: 2.55× weekly, month 2.77×, ladder rising; stop ₹163.40; charges ₹4,407.49)
2017-06-05  DAAWAT      PYRAMID BUY ₹35.83 lakh at ₹72.60 (box jump — doubling the stake with NEW capital; stop stays ₹65.59; charges ₹4,245.05)
2017-06-05  VOLTAS      PYRAMID BUY ₹37.84 lakh at ₹501.00 (box jump — doubling the stake with NEW capital; stop stays ₹453.86; charges ₹4,483.29)
2017-06-12  SHAKTIPUMP  PYRAMID BUY ₹41.10 lakh at ₹441.80 (box jump — doubling the stake with NEW capital; stop stays ₹357.49; charges ₹4,869.93)
2017-06-19  SHAKTIPUMP  PYRAMID BUY ₹82.71 lakh at ₹444.75 (box jump — doubling the stake with NEW capital; stop stays ₹415.62; charges ₹9,799.09)
2017-06-19  VOLTAS      PYRAMID BUY ₹73.82 lakh at ₹489.00 (box jump — doubling the stake with NEW capital; stop stays ₹456.19; charges ₹8,746.63)
2017-06-22  DAAWAT      SELL ₹64.63 lakh at stop ₹65.59 (-11.6%, charges ₹6,704.38) — the cash goes back to work at the next Friday screen
2017-06-23  VOLTAS      SELL ₹1.38 crore at stop ₹456.19 (-7.6%, charges ₹14,264.36) — the cash goes back to work at the next Friday screen
2017-06-27  BBL         BUY ₹61.91 lakh at ₹1,420.00 (fresh Friday signal — BUY: 5.07× weekly, month 3.38×, ladder rising; stop ₹1,117.77; charges ₹7,335.53)
2017-06-27  EVERESTIND  BUY ₹62.15 lakh at ₹365.20 (fresh Friday signal — BUY: 7.06× weekly, month 4.53×, ladder rising; stop ₹281.87; charges ₹7,363.69)
2017-06-27  GOACARBON   BUY ₹62.59 lakh at ₹248.70 (fresh Friday signal — BUY: 9.59× weekly, month 4.76×, ladder rising; stop ₹148.25; charges ₹7,415.95)
2017-06-27  WALCHANNAG  SELL ₹34.84 lakh at stop ₹163.40 (-6.1%, charges ₹3,613.53) — the cash goes back to work at the next Friday screen
2017-06-28  SHAKTIPUMP  SELL ₹1.54 crore at stop ₹415.62 (-4.1%, charges ₹16,008.14) — the cash goes back to work at the next Friday screen
2017-07-03  BEPL        BUY ₹63.04 lakh at ₹67.70 (fresh Friday signal — BUY: 2.55× weekly, month 3.44×, ladder rising; stop ₹47.31; charges ₹7,469.52)
2017-07-03  FLFL        PYRAMID BUY ₹72.25 lakh at ₹324.70 (box jump — doubling the stake with NEW capital; stop stays ₹269.20; charges ₹8,559.83)
2017-07-03  GVKPIL      BUY ₹70.99 lakh at ₹8.90 (fresh Friday signal — BUY: 4.75× weekly, month 2.80×, ladder rising; stop ₹5.83; charges ₹8,410.88)
2017-07-03  VENKEYS     BUY ₹70.62 lakh at ₹1,702.90 (fresh Friday signal — BUY: 3.61× weekly, month 1.67×, ladder rising; stop ₹1,311.00; charges ₹8,367.41)
2017-07-10  BBL         PYRAMID BUY ₹59.49 lakh at ₹1,366.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,279.03; charges ₹7,048.21)
2017-07-10  EVERESTIND  PYRAMID BUY ₹65.75 lakh at ₹386.80 (box jump — doubling the stake with NEW capital; stop stays ₹318.64; charges ₹7,789.98)
2017-07-10  GOACARBON   PYRAMID BUY ₹75.41 lakh at ₹300.00 (box jump — doubling the stake with NEW capital; stop stays ₹212.73; charges ₹8,935.05)
2017-07-10  GVKPIL      PYRAMID BUY ₹65.33 lakh at ₹8.20 (box jump — doubling the stake with NEW capital; stop stays ₹7.32; charges ₹7,740.17)
2017-07-13  GVKPIL      SELL ₹1.16 crore at stop ₹7.32 (-14.4%, charges ₹12,078.75) — the cash goes back to work at the next Friday screen
2017-07-17  VETO        BUY ₹99.90 lakh at ₹221.00 (fresh Friday signal — BUY: 10.87× weekly, month 5.50×, ladder rising; stop ₹167.68; charges ₹11,836.16)
2017-07-18  BBL         SELL ₹1.11 crore at stop ₹1,279.03 (-8.2%, charges ₹11,536.75) — the cash goes back to work at the next Friday screen
2017-07-24  AVANTIFEED  PYRAMID BUY ₹34.49 lakh at ₹1,651.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,481.05; charges ₹4,086.22)
2017-07-24  BALAJITELE  BUY ₹1.17 crore at ₹188.00 (fresh Friday signal — BUY: 7.42× weekly, month 6.58×, ladder rising; stop ₹149.25; charges ₹13,889.97)
2017-07-24  BEPL        PYRAMID BUY ₹73.94 lakh at ₹79.50 (box jump — doubling the stake with NEW capital; stop stays ₹64.55; charges ₹8,761.05)
2017-07-24  VENKEYS     PYRAMID BUY ₹83.66 lakh at ₹2,019.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,719.30; charges ₹9,912.28)
2017-08-07  GOLDINFRA   PYRAMID BUY ₹8.46 lakh at ₹78.50 (box jump — doubling the stake with NEW capital; stop stays ₹64.93; charges ₹1,002.12)
2017-08-09  ALLCARGO    SELL ₹27.37 lakh at stop ₹167.29 (-10.8%, charges ₹2,839.28) — the cash goes back to work at the next Friday screen
2017-08-10  AVANTIFEED  SELL ₹61.78 lakh at stop ₹1,481.05 (-3.6%, charges ₹6,407.94) — the cash goes back to work at the next Friday screen
2017-08-10  BALAJITELE  SELL ₹92.86 lakh at stop ₹149.25 (-20.6%, charges ₹9,632.63) — the cash goes back to work at the next Friday screen
2017-08-10  EVERESTIND  SELL ₹1.08 crore at stop ₹318.64 (-15.3%, charges ₹11,218.24) — the cash goes back to work at the next Friday screen
2017-08-10  KARURVYSYA  SELL ₹61.26 lakh at stop ₹128.39 (+13.0%, charges ₹6,354.15) — the cash goes back to work at the next Friday screen
2017-08-11  VENKEYS     SELL ₹1.42 crore at stop ₹1,719.30 (-7.6%, charges ₹14,750.71) — the cash goes back to work at the next Friday screen
2017-08-14  BEPL        PYRAMID BUY ₹1.45 crore at ₹78.00 (box jump — doubling the stake with NEW capital; stop stays ₹65.39; charges ₹17,181.31)
2017-08-14  FRETAIL     BUY ₹1.34 crore at ₹452.95 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 2.34×, ladder rising; stop ₹377.15; charges ₹15,863.92)
2017-08-14  INSECTICID  BUY ₹1.34 crore at ₹771.85 (fresh Friday signal — BUY: 3.90× weekly, month 2.53×, ladder rising; stop ₹669.32; charges ₹15,818.92)
2017-08-14  UTTAMSUGAR  BUY ₹1.33 crore at ₹188.00 (fresh Friday signal — BUY: 5.58× weekly, month 1.92×, ladder rising; stop ₹147.25; charges ₹15,733.43)
2017-08-14  VETO        PYRAMID BUY ₹91.22 lakh at ₹202.05 (box jump — doubling the stake with NEW capital; stop stays ₹200.31; charges ₹10,808.43)
2017-08-14  VETO        SELL ₹1.81 crore at stop ₹200.31 (-5.3%, charges ₹18,731.86) — the cash goes back to work at the next Friday screen
2017-08-21  AVANTIFEED  BUY ₹1.21 crore at ₹1,928.50 (fresh Friday signal — BUY: 2.51× weekly, month 2.88×, ladder rising; stop ₹1,292.50; charges ₹14,333.86)
2017-08-21  BEML        BUY ₹1.64 crore at ₹1,897.00 (fresh Friday signal — BUY: 3.75× weekly, month 2.60×, ladder rising; stop ₹1,325.12; charges ₹19,378.31)
2017-08-21  INSECTICID  PYRAMID BUY ₹1.35 crore at ₹782.00 (box jump — doubling the stake with NEW capital; stop stays ₹682.10; charges ₹16,007.95)
2017-08-21  UTTAMSUGAR  PYRAMID BUY ₹1.33 crore at ₹188.70 (box jump — doubling the stake with NEW capital; stop stays ₹155.58; charges ₹15,773.30)
2017-08-28  AVANTIFEED  PYRAMID BUY ₹1.21 crore at ₹1,938.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,726.43; charges ₹14,387.40)
2017-08-28  FRETAIL     PYRAMID BUY ₹1.51 crore at ₹509.80 (box jump — doubling the stake with NEW capital; stop stays ₹447.45; charges ₹17,833.86)
2017-09-04  BEPL        PYRAMID BUY ₹3.16 crore at ₹85.00 (box jump — doubling the stake with NEW capital; stop stays ₹79.33; charges ₹37,424.26)
2017-09-04  FRETAIL     PYRAMID BUY ₹3.25 crore at ₹550.00 (box jump — doubling the stake with NEW capital; stop stays ₹475.00; charges ₹38,457.47)
2017-09-04  GOACARBON   PYRAMID BUY ₹1.78 crore at ₹355.00 (box jump — doubling the stake with NEW capital; stop stays ₹245.45; charges ₹21,133.77)
2017-09-11  HOVS        PYRAMID BUY ₹37.35 lakh at ₹324.45 (box jump — doubling the stake with NEW capital; stop stays ₹233.27; charges ₹4,424.72)
2017-09-11  INSECTICID  PYRAMID BUY ₹3.17 crore at ₹918.05 (box jump — doubling the stake with NEW capital; stop stays ₹821.75; charges ₹37,563.67)
2017-09-21  INSECTICID  SELL ₹5.67 crore at stop ₹821.75 (-3.0%, charges ₹58,778.15) — the cash goes back to work at the next Friday screen
2017-09-25  BEML        PYRAMID BUY ₹1.48 crore at ₹1,719.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,744.63; charges ₹17,547.35)
2017-09-25  BEML        SELL ₹3.00 crore at stop ₹1,744.63 (-3.5%, charges ₹31,117.99) — the cash goes back to work at the next Friday screen
2017-09-25  BEPL        SELL ₹5.89 crore at stop ₹79.33 (-1.3%, charges ₹61,058.52) — the cash goes back to work at the next Friday screen
2017-09-25  FRETAIL     PYRAMID BUY ₹6.42 crore at ₹544.10 (box jump — doubling the stake with NEW capital; stop stays ₹495.38; charges ₹76,044.78)
2017-09-25  OMMETALS    BUY ₹3.91 crore at ₹74.35 (fresh Friday signal — BUY: 12.73× weekly, month 7.65×, ladder rising; stop ₹48.10; charges ₹46,274.71)
2017-10-03  AVANTIFEED  PYRAMID BUY ₹2.58 crore at ₹2,058.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,776.69; charges ₹30,551.78)
2017-10-03  DEN         BUY ₹5.07 crore at ₹89.40 (fresh Friday signal — ACCUMULATE: 5.36× weekly, month 1.96×, ladder rising; stop ₹78.80; charges ₹60,037.52)
2017-10-03  GOACARBON   PYRAMID BUY ₹4.78 crore at ₹475.50 (box jump — doubling the stake with NEW capital; stop stays ₹378.80; charges ₹56,581.15)
2017-10-03  OMMETALS    PYRAMID BUY ₹3.95 crore at ₹75.25 (box jump — doubling the stake with NEW capital; stop stays ₹65.75; charges ₹46,779.37)
2017-10-03  SHOPERSTOP  BUY ₹5.09 crore at ₹486.40 (fresh Friday signal — BUY: 12.98× weekly, month 10.59×, ladder rising; stop ₹386.60; charges ₹60,250.04)
2017-10-09  SHOPERSTOP  PYRAMID BUY ₹5.40 crore at ₹516.80 (box jump — doubling the stake with NEW capital; stop stays ₹412.79; charges ₹63,939.82)
2017-10-23  AVANTIFEED  PYRAMID BUY ₹6.77 crore at ₹2,705.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,232.50; charges ₹80,230.82)
2017-11-06  SHOPERSTOP  PYRAMID BUY ₹12.11 crore at ₹580.00 (box jump — doubling the stake with NEW capital; stop stays ₹475.00; charges ₹1.43 lakh)
2017-11-09  FRETAIL     SELL ₹11.79 crore at stop ₹500.65 (-5.5%, charges ₹1.22 lakh) — the cash goes back to work at the next Friday screen
2017-11-09  OMMETALS    SELL ₹6.89 crore at stop ₹65.75 (-12.1%, charges ₹71,452.62) — the cash goes back to work at the next Friday screen
2017-11-13  EKC         BUY ₹8.63 crore at ₹52.95 (fresh Friday signal — BUY: 8.00× weekly, month 3.41×, ladder rising; stop ₹27.09; charges ₹1.02 lakh)
2017-11-13  LTI         BUY ₹8.60 crore at ₹945.00 (fresh Friday signal — BUY: 8.95× weekly, month 1.84×, ladder rising; stop ₹768.41; charges ₹1.02 lakh)
2017-11-15  AVANTIFEED  SELL ₹13.20 crore at stop ₹2,641.00 (+12.4%, charges ₹1.37 lakh) — the cash goes back to work at the next Friday screen
2017-11-20  HATSUN      BUY ₹10.78 crore at ₹875.00 (fresh Friday signal — BUY: 26.67× weekly, month 8.94×, ladder rising; stop ₹658.15; charges ₹1.28 lakh)
2017-11-20  SHOPERSTOP  PYRAMID BUY ₹23.24 crore at ₹557.05 (box jump — doubling the stake with NEW capital; stop stays ₹513.28; charges ₹2.75 lakh)
2017-11-27  EKC         PYRAMID BUY ₹8.72 crore at ₹53.55 (box jump — doubling the stake with NEW capital; stop stays ₹45.02; charges ₹1.03 lakh)
2017-11-27  HATSUN      PYRAMID BUY ₹11.03 crore at ₹895.80 (box jump — doubling the stake with NEW capital; stop stays ₹808.92; charges ₹1.31 lakh)
2017-11-27  HOVS        PYRAMID BUY ₹62.05 lakh at ₹269.70 (box jump — doubling the stake with NEW capital; stop stays ₹243.00; charges ₹7,351.77)
2017-11-27  LTI         PYRAMID BUY ₹9.00 crore at ₹990.00 (box jump — doubling the stake with NEW capital; stop stays ₹885.83; charges ₹1.07 lakh)
2017-12-05  UTTAMSUGAR  SELL ₹2.19 crore at stop ₹155.58 (-17.4%, charges ₹22,734.17) — the cash goes back to work at the next Friday screen
2017-12-18  GOLDINFRA   PYRAMID BUY ₹40.66 lakh at ₹188.80 (box jump — doubling the stake with NEW capital; stop stays ₹155.82; charges ₹4,817.52)
2017-12-18  LTI         PYRAMID BUY ₹18.91 crore at ₹1,040.00 (box jump — doubling the stake with NEW capital; stop stays ₹910.81; charges ₹2.24 lakh)
2017-12-26  DEN         PYRAMID BUY ₹6.25 crore at ₹110.35 (box jump — doubling the stake with NEW capital; stop stays ₹93.62; charges ₹74,018.91)
2017-12-26  EKC         PYRAMID BUY ₹22.73 crore at ₹69.85 (box jump — doubling the stake with NEW capital; stop stays ₹55.05; charges ₹2.69 lakh)
2017-12-26  LTI         PYRAMID BUY ₹39.61 crore at ₹1,090.00 (box jump — doubling the stake with NEW capital; stop stays ₹961.40; charges ₹4.69 lakh)
2018-01-08  DEN         PYRAMID BUY ₹12.78 crore at ₹112.90 (box jump — doubling the stake with NEW capital; stop stays ₹98.04; charges ₹1.51 lakh)
2018-01-17  SHOPERSTOP  SELL ₹42.76 crore at stop ₹513.28 (-6.5%, charges ₹4.44 lakh) — the cash goes back to work at the next Friday screen
2018-01-22  HATSUN      SELL ₹19.88 crore at stop ₹808.92 (-8.6%, charges ₹2.06 lakh) — the cash goes back to work at the next Friday screen
2018-01-22  PRISMCEM    BUY ₹24.60 crore at ₹142.00 (fresh Friday signal — BUY: 9.05× weekly, month 7.67×, ladder rising; stop ₹125.35; charges ₹2.91 lakh)
2018-01-22  SUNTECK     BUY ₹24.60 crore at ₹420.50 (fresh Friday signal — ACCUMULATE: 7.60× weekly, month 1.99×, ladder rising; stop ₹369.93; charges ₹2.91 lakh)
2018-01-29  DEN         PYRAMID BUY ₹27.49 crore at ₹121.55 (box jump — doubling the stake with NEW capital; stop stays ₹107.61; charges ₹3.26 lakh)
2018-01-29  GOLDINFRA   PYRAMID BUY ₹94.23 lakh at ₹218.90 (box jump — doubling the stake with NEW capital; stop stays ₹199.60; charges ₹11,164.53)
2018-01-29  LTTS        BUY ₹19.99 crore at ₹1,329.00 (fresh Friday signal — BUY: 8.62× weekly, month 3.03×, ladder rising; stop ₹922.39; charges ₹2.37 lakh)
2018-01-30  EKC         SELL ₹35.76 crore at stop ₹55.05 (-10.6%, charges ₹3.71 lakh) — the cash goes back to work at the next Friday screen
2018-01-31  GOACARBON   SELL ₹18.31 crore at stop ₹913.01 (+131.1%, charges ₹1.90 lakh) — the cash goes back to work at the next Friday screen
2018-02-01  DEN         SELL ₹48.60 crore at stop ₹107.61 (-5.6%, charges ₹5.04 lakh) — the cash goes back to work at the next Friday screen
2018-02-02  GOLDINFRA   SELL ₹1.72 crore at stop ₹199.60 (+15.0%, charges ₹17,796.30) — the cash goes back to work at the next Friday screen
2018-02-02  PRISMCEM    SELL ₹21.66 crore at stop ₹125.35 (-11.7%, charges ₹2.25 lakh) — the cash goes back to work at the next Friday screen
2018-02-05  ELGIEQUIP   BUY ₹26.43 crore at ₹308.00 (fresh Friday signal — ACCUMULATE: 1.72× weekly, month 1.79×, ladder rising; stop ₹282.62; charges ₹3.13 lakh)
2018-02-05  ESTER       BUY ₹26.42 crore at ₹65.15 (fresh Friday signal — ACCUMULATE: 2.57× weekly, month 3.16×, ladder rising; stop ₹52.83; charges ₹3.13 lakh)
2018-02-05  LUXIND      BUY ₹26.41 crore at ₹1,621.10 (fresh Friday signal — BUY: 2.54× weekly, month 2.50×, ladder rising; stop ₹1,425.00; charges ₹3.13 lakh)
2018-02-05  MPHASIS     BUY ₹26.40 crore at ₹851.10 (fresh Friday signal — BUY: 3.88× weekly, month 3.19×, ladder rising; stop ₹668.70; charges ₹3.13 lakh)
2018-02-06  SUNTECK     SELL ₹21.60 crore at stop ₹369.93 (-12.0%, charges ₹2.24 lakh) — the cash goes back to work at the next Friday screen
2018-02-12  DENORA      BUY ₹33.33 crore at ₹490.00 (fresh Friday signal — BUY: 6.77× weekly, month 12.51×, ladder rising; stop ₹303.38; charges ₹3.95 lakh)
2018-02-12  LTTS        PYRAMID BUY ₹20.04 crore at ₹1,334.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,133.56; charges ₹2.37 lakh)
2018-02-12  LUXIND      PYRAMID BUY ₹28.46 crore at ₹1,749.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,448.75; charges ₹3.37 lakh)
2018-02-19  MPHASIS     PYRAMID BUY ₹26.65 crore at ₹860.10 (box jump — doubling the stake with NEW capital; stop stays ₹771.50; charges ₹3.16 lakh)
2018-02-26  ELGIEQUIP   PYRAMID BUY ₹26.58 crore at ₹310.20 (box jump — doubling the stake with NEW capital; stop stays ₹287.85; charges ₹3.15 lakh)
2018-02-26  LTTS        PYRAMID BUY ₹42.08 crore at ₹1,401.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,168.00; charges ₹4.99 lakh)
2018-03-08  ELGIEQUIP   SELL ₹49.25 crore at stop ₹287.85 (-6.9%, charges ₹5.11 lakh) — the cash goes back to work at the next Friday screen
2018-03-12  GSS         BUY ₹41.38 crore at ₹57.50 (fresh Friday signal — BUY: 4.39× weekly, month 9.03×, ladder rising; stop ₹40.30; charges ₹4.90 lakh)
2018-03-19  GSS         PYRAMID BUY ₹47.08 crore at ₹65.50 (box jump — doubling the stake with NEW capital; stop stays ₹47.83; charges ₹5.58 lakh)
2018-03-19  LTI         SELL ₹94.98 crore at stop ₹1,309.10 (+25.1%, charges ₹9.85 lakh) — the cash goes back to work at the next Friday screen
2018-03-19  LTTS        SELL ₹70.05 crore at stop ₹1,168.00 (-14.5%, charges ₹7.27 lakh) — the cash goes back to work at the next Friday screen
2018-03-19  LUXIND      PYRAMID BUY ₹58.07 crore at ₹1,785.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,578.09; charges ₹6.88 lakh)
2018-03-22  HOVS        SELL ₹1.12 crore at stop ₹243.00 (-18.2%, charges ₹11,579.55) — the cash goes back to work at the next Friday screen
2018-04-02  TAX         FY2018 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹6.20 crore / LT ₹0.00)
2018-04-09  EXCELINDUS  BUY ₹50.68 crore at ₹1,054.00 (fresh Friday signal — BUY: 1.80× weekly, month 1.75×, ladder rising; stop ₹763.20; charges ₹6.00 lakh)
2018-04-16  LUXIND      PYRAMID BUY ₹117.28 crore at ₹1,803.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,691.24; charges ₹13.90 lakh)
2018-04-16  SANWARIA    BUY ₹63.92 crore at ₹21.30 (fresh Friday signal — BUY: 1.97× weekly, month 2.08×, ladder rising; stop ₹18.00; charges ₹7.57 lakh)
2018-04-23  ESTER       PYRAMID BUY ₹29.77 crore at ₹73.50 (box jump — doubling the stake with NEW capital; stop stays ₹65.17; charges ₹3.53 lakh)
2018-04-23  TAJGVK      BUY ₹68.09 crore at ₹232.00 (fresh Friday signal — BUY: 16.51× weekly, month 4.06×, ladder rising; stop ₹159.60; charges ₹8.07 lakh)
2018-04-26  SANWARIA    SELL ₹53.90 crore at stop ₹18.00 (-15.5%, charges ₹5.59 lakh) — the cash goes back to work at the next Friday screen
2018-04-30  HIL         BUY ₹53.90 crore at ₹2,239.45 (fresh Friday signal — BUY: 6.62× weekly, month 1.77×, ladder rising; stop ₹1,790.75; charges ₹6.39 lakh)
2018-04-30  TAJGVK      PYRAMID BUY ₹65.95 crore at ₹225.00 (box jump — doubling the stake with NEW capital; stop stays ₹212.37; charges ₹7.81 lakh)
2018-05-04  TAJGVK      SELL ₹124.30 crore at stop ₹212.37 (-7.1%, charges ₹12.89 lakh) — the cash goes back to work at the next Friday screen
2018-05-07  EXCELINDUS  PYRAMID BUY ₹66.04 crore at ₹1,375.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,282.59; charges ₹7.82 lakh)
2018-05-10  ESTER       SELL ₹52.70 crore at stop ₹65.17 (-6.0%, charges ₹5.47 lakh) — the cash goes back to work at the next Friday screen
2018-05-11  EXCELINDUS  SELL ₹122.99 crore at stop ₹1,282.59 (+5.6%, charges ₹12.76 lakh) — the cash goes back to work at the next Friday screen
2018-05-14  GREAVESCOT  BUY ₹103.41 crore at ₹139.00 (fresh Friday signal — BUY: 4.24× weekly, month 1.83×, ladder rising; stop ₹116.23; charges ₹12.25 lakh)
2018-05-14  GSS         PYRAMID BUY ₹134.25 crore at ₹93.45 (box jump — doubling the stake with NEW capital; stop stays ₹68.61; charges ₹15.91 lakh)
2018-05-14  MPHASIS     PYRAMID BUY ₹60.08 crore at ₹970.00 (box jump — doubling the stake with NEW capital; stop stays ₹913.00; charges ₹7.12 lakh)
2018-05-14  SASKEN      BUY ₹93.03 crore at ₹1,021.00 (fresh Friday signal — BUY: 3.21× weekly, month 3.90×, ladder rising; stop ₹827.45; charges ₹11.02 lakh)
2018-05-14  WINDMACHIN  BUY ₹103.55 crore at ₹143.00 (fresh Friday signal — BUY: 5.82× weekly, month 3.65×, ladder rising; stop ₹109.96; charges ₹12.27 lakh)
2018-05-21  FLFL        SELL ₹1.81 crore at stop ₹407.74 (+33.6%, charges ₹18,790.60) — the cash goes back to work at the next Friday screen
2018-05-21  WINDMACHIN  PYRAMID BUY ₹98.37 crore at ₹136.00 (box jump — doubling the stake with NEW capital; stop stays ₹130.06; charges ₹11.65 lakh)
2018-05-21  WINDMACHIN  SELL ₹187.84 crore at stop ₹130.06 (-6.8%, charges ₹19.48 lakh) — the cash goes back to work at the next Friday screen
2018-05-28  COLPAL      BUY ₹141.31 crore at ₹1,260.00 (fresh Friday signal — ACCUMULATE: 4.83× weekly, month 2.16×, ladder rising; stop ₹1,116.91; charges ₹16.74 lakh)
2018-05-28  HIL         PYRAMID BUY ₹51.15 crore at ₹2,128.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,939.95; charges ₹6.06 lakh)
2018-05-28  MPHASIS     PYRAMID BUY ₹139.07 crore at ₹1,123.40 (box jump — doubling the stake with NEW capital; stop stays ₹978.50; charges ₹16.48 lakh)
2018-05-28  SASKEN      PYRAMID BUY ₹90.55 crore at ₹995.00 (box jump — doubling the stake with NEW capital; stop stays ₹907.82; charges ₹10.73 lakh)
2018-05-30  LUXIND      SELL ₹240.51 crore at stop ₹1,852.59 (+4.7%, charges ₹24.95 lakh) — the cash goes back to work at the next Friday screen
2018-06-01  DENORA      SELL ₹20.59 crore at stop ₹303.38 (-38.1%, charges ₹2.14 lakh) — the cash goes back to work at the next Friday screen
2018-06-04  BODALCHEM   BUY ₹140.97 crore at ₹144.85 (fresh Friday signal — BUY: 4.06× weekly, month 1.85×, ladder rising; stop ₹116.38; charges ₹16.70 lakh)
2018-06-04  GREAVESCOT  PYRAMID BUY ₹98.01 crore at ₹131.90 (box jump — doubling the stake with NEW capital; stop stays ₹117.04; charges ₹11.61 lakh)
2018-06-05  HIL         SELL ₹93.11 crore at stop ₹1,939.95 (-11.2%, charges ₹9.66 lakh) — the cash goes back to work at the next Friday screen
2018-06-11  BODALCHEM   PYRAMID BUY ₹140.22 crore at ₹144.25 (box jump — doubling the stake with NEW capital; stop stays ₹129.25; charges ₹16.61 lakh)
2018-06-18  ASTRAZEN    BUY ₹158.23 crore at ₹1,048.00 (fresh Friday signal — BUY: 7.17× weekly, month 3.61×, ladder rising; stop ₹842.73; charges ₹18.75 lakh)
2018-06-25  ASTRAZEN    PYRAMID BUY ₹179.64 crore at ₹1,191.20 (box jump — doubling the stake with NEW capital; stop stays ₹974.32; charges ₹21.28 lakh)
2018-06-25  GREAVESCOT  PYRAMID BUY ₹202.15 crore at ₹136.10 (box jump — doubling the stake with NEW capital; stop stays ₹121.79; charges ₹23.95 lakh)
2018-06-25  SASKEN      PYRAMID BUY ₹183.66 crore at ₹1,009.65 (box jump — doubling the stake with NEW capital; stop stays ₹946.20; charges ₹21.76 lakh)
2018-06-26  BODALCHEM   SELL ₹250.87 crore at stop ₹129.25 (-10.6%, charges ₹26.02 lakh) — the cash goes back to work at the next Friday screen
2018-06-26  SASKEN      SELL ₹343.68 crore at stop ₹946.20 (-6.2%, charges ₹35.65 lakh) — the cash goes back to work at the next Friday screen
2018-07-02  ASTRAZEN    PYRAMID BUY ₹342.29 crore at ₹1,135.56 (box jump — doubling the stake with NEW capital; stop stays ₹1,019.92; charges ₹40.56 lakh)
2018-07-02  PAGEIND     BUY ₹239.61 crore at ₹27,870.00 (fresh Friday signal — BUY: 1.79× weekly, month 1.61×, ladder rising; stop ₹24,890.52; charges ₹28.39 lakh)
2018-07-09  GREAVESCOT  PYRAMID BUY ₹424.54 crore at ₹143.00 (box jump — doubling the stake with NEW capital; stop stays ₹126.02; charges ₹50.30 lakh)
2018-07-09  PAGEIND     PYRAMID BUY ₹244.74 crore at ₹28,500.00 (box jump — doubling the stake with NEW capital; stop stays ₹25,560.37; charges ₹29.00 lakh)
2018-07-09  WHEELS      BUY ₹311.74 crore at ₹2,272.00 (fresh Friday signal — ACCUMULATE: 2.33× weekly, month 10.11×, ladder rising; stop ₹2,006.50; charges ₹36.94 lakh)
2018-07-18  COLPAL      SELL ₹124.99 crore at stop ₹1,116.91 (-11.4%, charges ₹12.96 lakh) — the cash goes back to work at the next Friday screen
2018-07-23  RBLBANK     BUY ₹271.53 crore at ₹580.80 (fresh Friday signal — BUY: 3.22× weekly, month 1.82×, ladder rising; stop ₹507.44; charges ₹32.17 lakh)
2018-07-26  GSS         SELL ₹196.82 crore at stop ₹68.61 (-11.4%, charges ₹20.42 lakh) — the cash goes back to work at the next Friday screen
2018-07-30  ACC         BUY ₹196.82 crore at ₹1,537.70 (fresh Friday signal — BUY: 4.61× weekly, month 2.47×, ladder rising; stop ₹1,192.87; charges ₹23.32 lakh)
2018-07-30  PAGEIND     PYRAMID BUY ₹501.20 crore at ₹29,200.00 (box jump — doubling the stake with NEW capital; stop stays ₹26,333.33; charges ₹59.38 lakh)
2018-07-30  RBLBANK     PYRAMID BUY ₹265.42 crore at ₹568.40 (box jump — doubling the stake with NEW capital; stop stays ₹519.65; charges ₹31.45 lakh)
2018-08-06  ASTRAZEN    PYRAMID BUY ₹831.45 crore at ₹1,380.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,124.80; charges ₹98.51 lakh)
2018-08-08  WHEELS      SELL ₹274.70 crore at stop ₹2,006.50 (-11.7%, charges ₹28.49 lakh) — the cash goes back to work at the next Friday screen
2018-08-13  ACC         PYRAMID BUY ₹197.00 crore at ₹1,541.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,424.10; charges ₹23.34 lakh)
2018-08-13  TCIEXP      BUY ₹274.70 crore at ₹710.00 (fresh Friday signal — BUY: 2.91× weekly, month 2.87×, ladder rising; stop ₹580.45; charges ₹32.55 lakh)
2018-08-20  ACC         PYRAMID BUY ₹409.34 crore at ₹1,601.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,436.88; charges ₹48.50 lakh)
2018-08-20  TCIEXP      PYRAMID BUY ₹279.20 crore at ₹722.50 (box jump — doubling the stake with NEW capital; stop stays ₹652.46; charges ₹33.08 lakh)
2018-09-03  PAGEIND     PYRAMID BUY ₹1,192.60 crore at ₹34,760.90 (box jump — doubling the stake with NEW capital; stop stays ₹32,310.88; charges ₹1.41 crore)
2018-09-05  PAGEIND     SELL ₹2,213.47 crore at stop ₹32,310.88 (+1.8%, charges ₹2.30 crore) — the cash goes back to work at the next Friday screen
2018-09-05  TCIEXP      SELL ₹503.45 crore at stop ₹652.46 (-8.9%, charges ₹52.22 lakh) — the cash goes back to work at the next Friday screen
2018-09-10  BBL         BUY ₹702.43 crore at ₹1,500.15 (fresh Friday signal — BUY: 9.73× weekly, month 1.54×, ladder rising; stop ₹1,217.66; charges ₹83.22 lakh)
2018-09-10  LTI         BUY ₹703.82 crore at ₹1,955.00 (fresh Friday signal — BUY: 11.33× weekly, month 3.91×, ladder rising; stop ₹1,643.31; charges ₹83.39 lakh)
2018-09-10  MUTHOOTFIN  BUY ₹701.08 crore at ₹468.80 (fresh Friday signal — BUY: 6.85× weekly, month 1.77×, ladder rising; stop ₹370.50; charges ₹83.07 lakh)
2018-09-10  POLYPLEX    BUY ₹609.60 crore at ₹641.00 (fresh Friday signal — BUY: 4.88× weekly, month 3.06×, ladder rising; stop ₹442.27; charges ₹72.23 lakh)
2018-09-12  ASTRAZEN    SELL ₹1,618.32 crore at stop ₹1,345.20 (+7.3%, charges ₹1.68 crore) — the cash goes back to work at the next Friday screen
2018-09-17  ALBERTDAVD  BUY ₹741.51 crore at ₹770.05 (fresh Friday signal — BUY: 5.58× weekly, month 13.30×, ladder rising; stop ₹608.24; charges ₹87.86 lakh)
2018-09-17  RBLBANK     PYRAMID BUY ₹569.82 crore at ₹610.50 (box jump — doubling the stake with NEW capital; stop stays ₹549.72; charges ₹67.51 lakh)
2018-09-17  SUVEN       BUY ₹740.33 crore at ₹310.80 (fresh Friday signal — BUY: 2.23× weekly, month 3.48×, ladder rising; stop ₹244.67; charges ₹87.72 lakh)
2018-09-21  ACC         SELL ₹733.14 crore at stop ₹1,436.88 (-8.5%, charges ₹76.05 lakh) — the cash goes back to work at the next Friday screen
2018-09-21  GREAVESCOT  SELL ₹852.32 crore at stop ₹143.78 (+3.2%, charges ₹88.41 lakh) — the cash goes back to work at the next Friday screen
2018-09-21  LTI         SELL ₹590.29 crore at stop ₹1,643.31 (-15.9%, charges ₹61.23 lakh) — the cash goes back to work at the next Friday screen
2018-09-21  RBLBANK     SELL ₹1,024.51 crore at stop ₹549.72 (-7.2%, charges ₹1.06 crore) — the cash goes back to work at the next Friday screen
2018-09-21  SUVEN       SELL ₹581.51 crore at stop ₹244.67 (-21.3%, charges ₹60.32 lakh) — the cash goes back to work at the next Friday screen
2018-09-24  ALBERTDAVD  SELL ₹584.40 crore at stop ₹608.24 (-21.0%, charges ₹60.62 lakh) — the cash goes back to work at the next Friday screen
2018-09-24  GUJFLUORO   BUY ₹721.48 crore at ₹854.00 (fresh Friday signal — ACCUMULATE: 2.91× weekly, month 1.88×, ladder rising; stop ₹775.25; charges ₹85.48 lakh)
2018-09-24  MUTHOOTFIN  PYRAMID BUY ₹675.15 crore at ₹452.00 (box jump — doubling the stake with NEW capital; stop stays ₹412.35; charges ₹79.99 lakh)
2018-09-25  MPHASIS     SELL ₹290.12 crore at stop ₹1,173.72 (+15.3%, charges ₹30.09 lakh) — the cash goes back to work at the next Friday screen
2018-09-27  BBL         SELL ₹568.89 crore at stop ₹1,217.66 (-18.8%, charges ₹59.01 lakh) — the cash goes back to work at the next Friday screen
2018-09-27  MUTHOOTFIN  SELL ₹1,229.85 crore at stop ₹412.35 (-10.4%, charges ₹1.28 crore) — the cash goes back to work at the next Friday screen
2018-09-28  GUJFLUORO   SELL ₹653.50 crore at stop ₹775.25 (-9.2%, charges ₹67.79 lakh) — the cash goes back to work at the next Friday screen
2018-10-15  BAJAJHIND   BUY ₹755.01 crore at ₹11.00 (fresh Friday signal — ACCUMULATE: 2.11× weekly, month 4.50×, ladder rising; stop ₹6.18; charges ₹89.46 lakh)
2018-10-15  POLYPLEX    PYRAMID BUY ₹536.69 crore at ₹565.00 (box jump — doubling the stake with NEW capital; stop stays ₹462.70; charges ₹63.59 lakh)
2018-10-22  HATHWAY     BUY ₹739.46 crore at ₹30.60 (fresh Friday signal — BUY: 3.56× weekly, month 1.61×, ladder rising; stop ₹18.96; charges ₹87.61 lakh)
2018-10-29  HATHWAY     PYRAMID BUY ₹730.13 crore at ₹30.25 (box jump — doubling the stake with NEW capital; stop stays ₹26.93; charges ₹86.51 lakh)
2018-11-05  TIIL        BUY ₹826.88 crore at ₹648.95 (fresh Friday signal — ACCUMULATE: 2.84× weekly, month 1.63×, ladder rising; stop ₹502.60; charges ₹97.97 lakh)
2018-11-19  DALMIASUG   BUY ₹948.86 crore at ₹101.20 (fresh Friday signal — BUY: 1.89× weekly, month 2.53×, ladder rising; stop ₹51.84; charges ₹1.12 crore)
2018-11-19  POLYPLEX    PYRAMID BUY ₹1,182.48 crore at ₹622.80 (box jump — doubling the stake with NEW capital; stop stays ₹508.35; charges ₹1.40 crore)
2018-11-26  BIRLACABLE  BUY ₹1,025.93 crore at ₹216.10 (fresh Friday signal — BUY: 2.57× weekly, month 2.89×, ladder rising; stop ₹168.72; charges ₹1.22 crore)
2018-11-26  DALMIASUG   PYRAMID BUY ₹981.45 crore at ₹104.80 (box jump — doubling the stake with NEW capital; stop stays ₹94.14; charges ₹1.16 crore)
2018-12-03  BIRLACABLE  PYRAMID BUY ₹1,037.52 crore at ₹218.80 (box jump — doubling the stake with NEW capital; stop stays ₹195.70; charges ₹1.23 crore)
2018-12-03  GODFRYPHLP  BUY ₹1,106.14 crore at ₹928.40 (fresh Friday signal — BUY: 1.59× weekly, month 1.69×, ladder rising; stop ₹795.15; charges ₹1.31 crore)
2018-12-03  KESORAMIND  BUY ₹1,097.95 crore at ₹85.00 (fresh Friday signal — BUY: 4.55× weekly, month 1.54×, ladder rising; stop ₹71.39; charges ₹1.30 crore)
2018-12-04  BIRLACABLE  SELL ₹1,852.95 crore at stop ₹195.70 (-10.0%, charges ₹1.92 crore) — the cash goes back to work at the next Friday screen
2018-12-10  DALMIASUG   SELL ₹1,760.37 crore at stop ₹94.14 (-8.6%, charges ₹1.83 crore) — the cash goes back to work at the next Friday screen
2018-12-10  POLYPLEX    SELL ₹1,927.21 crore at stop ₹508.35 (-17.1%, charges ₹2.00 crore) — the cash goes back to work at the next Friday screen
2018-12-17  BANKBEES    BUY ₹1,157.28 crore at ₹274.00 (fresh Friday signal — ACCUMULATE: 1.75× weekly, month 4.65×, ladder rising; stop ₹248.08; charges ₹1.37 crore)
2018-12-17  GODFRYPHLP  PYRAMID BUY ₹1,104.35 crore at ₹928.00 (box jump — doubling the stake with NEW capital; stop stays ₹812.30; charges ₹1.31 crore)
2018-12-17  PREMEXPLN   BUY ₹1,159.48 crore at ₹264.80 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 5.68×, ladder rising; stop ₹184.16; charges ₹1.37 crore)
2018-12-24  BEML        BUY ₹1,148.59 crore at ₹890.10 (fresh Friday signal — BUY: 5.73× weekly, month 2.62×, ladder rising; stop ₹648.90; charges ₹1.36 crore)
2018-12-26  GODFRYPHLP  SELL ₹1,930.18 crore at stop ₹812.30 (-12.5%, charges ₹2.00 crore) — the cash goes back to work at the next Friday screen
2019-01-07  BANKBEES    PYRAMID BUY ₹1,179.75 crore at ₹279.65 (box jump — doubling the stake with NEW capital; stop stays ₹255.55; charges ₹1.40 crore)
2019-01-07  BEML        PYRAMID BUY ₹1,154.83 crore at ₹896.00 (box jump — doubling the stake with NEW capital; stop stays ₹809.88; charges ₹1.37 crore)
2019-01-14  ADORWELD    BUY ₹1,588.65 crore at ₹394.90 (fresh Friday signal — ACCUMULATE: 4.44× weekly, month 1.83×, ladder rising; stop ₹336.57; charges ₹1.88 crore)
2019-01-14  BANKBEES    PYRAMID BUY ₹2,360.04 crore at ₹279.88 (box jump — doubling the stake with NEW capital; stop stays ₹260.57; charges ₹2.80 crore)
2019-01-14  MOHOTAIND   BUY ₹849.30 crore at ₹78.80 (fresh Friday signal — ACCUMULATE: 3.20× weekly, month 12.02×, ladder rising; stop ₹69.95; charges ₹1.01 crore)
2019-01-14  SKFINDIA    BUY ₹1,590.72 crore at ₹1,940.00 (fresh Friday signal — ACCUMULATE: 6.62× weekly, month 3.44×, ladder rising; stop ₹1,776.45; charges ₹1.88 crore)
2019-01-17  MOHOTAIND   SELL ₹752.24 crore at stop ₹69.95 (-11.2%, charges ₹78.03 lakh) — the cash goes back to work at the next Friday screen
2019-01-21  BANKBEES    PYRAMID BUY ₹4,801.89 crore at ₹284.90 (box jump — doubling the stake with NEW capital; stop stays ₹263.25; charges ₹5.69 crore)
2019-01-28  ADORWELD    SELL ₹1,350.99 crore at stop ₹336.57 (-14.8%, charges ₹1.40 crore) — the cash goes back to work at the next Friday screen
2019-01-28  BEML        SELL ₹2,084.27 crore at stop ₹809.88 (-9.3%, charges ₹2.16 crore) — the cash goes back to work at the next Friday screen
2019-01-29  KESORAMIND  SELL ₹920.10 crore at stop ₹71.39 (-16.0%, charges ₹95.44 lakh) — the cash goes back to work at the next Friday screen
2019-02-11  INFRATEL    BUY ₹1,969.65 crore at ₹326.00 (fresh Friday signal — BUY: 1.56× weekly, month 1.65×, ladder rising; stop ₹270.75; charges ₹2.33 crore)
2019-02-18  YESBANK     BUY ₹1,925.54 crore at ₹201.00 (fresh Friday signal — BUY: 1.58× weekly, month 2.31×, ladder rising; stop ₹178.03; charges ₹2.28 crore)
2019-02-19  HATHWAY     SELL ₹1,297.88 crore at stop ₹26.93 (-11.5%, charges ₹1.35 crore) — the cash goes back to work at the next Friday screen
2019-02-25  INFRATEL    PYRAMID BUY ₹1,892.48 crore at ₹313.60 (box jump — doubling the stake with NEW capital; stop stays ₹277.35; charges ₹2.24 crore)
2019-02-25  PREMEXPLN   PYRAMID BUY ₹944.68 crore at ₹216.00 (box jump — doubling the stake with NEW capital; stop stays ₹193.80; charges ₹1.12 crore)
2019-03-05  DHAMPURSUG  BUY ₹2,278.27 crore at ₹242.35 (fresh Friday signal — BUY: 3.72× weekly, month 1.52×, ladder rising; stop ₹198.55; charges ₹2.70 crore)
2019-03-11  BAJAJHIND   PYRAMID BUY ₹613.58 crore at ₹8.95 (box jump — doubling the stake with NEW capital; stop stays ₹7.69; charges ₹72.70 lakh)
2019-03-11  DHAMPURSUG  PYRAMID BUY ₹2,179.33 crore at ₹232.10 (box jump — doubling the stake with NEW capital; stop stays ₹211.42; charges ₹2.58 crore)
2019-03-11  SKFINDIA    PYRAMID BUY ₹1,601.12 crore at ₹1,955.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,828.80; charges ₹1.90 crore)
2019-03-20  BAJAJHIND   SELL ₹1,052.68 crore at stop ₹7.69 (-22.9%, charges ₹1.09 crore) — the cash goes back to work at the next Friday screen
2019-03-20  DHAMPURSUG  SELL ₹3,963.84 crore at stop ₹211.42 (-10.9%, charges ₹4.11 crore) — the cash goes back to work at the next Friday screen
2019-03-25  JUSTDIAL    BUY ₹2,968.27 crore at ₹615.00 (fresh Friday signal — BUY: 3.82× weekly, month 1.70×, ladder rising; stop ₹467.69; charges ₹3.52 crore)
2019-03-25  YESBANK     PYRAMID BUY ₹2,392.11 crore at ₹250.00 (box jump — doubling the stake with NEW capital; stop stays ₹229.71; charges ₹2.83 crore)
2019-04-01  HEIDELBERG  BUY ₹2,280.27 crore at ₹184.35 (fresh Friday signal — ACCUMULATE: 2.71× weekly, month 1.87×, ladder rising; stop ₹159.93; charges ₹2.70 crore)
2019-04-01  JUSTDIAL    PYRAMID BUY ₹2,950.05 crore at ₹611.95 (box jump — doubling the stake with NEW capital; stop stays ₹565.25; charges ₹3.50 crore)
2019-04-01  TAX         FY2019 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹3,659.17 crore / LT ₹0.00)
2019-04-08  PREMEXPLN   PYRAMID BUY ₹2,048.21 crore at ₹234.30 (box jump — doubling the stake with NEW capital; stop stays ₹214.62; charges ₹2.43 crore)
2019-04-08  SKFINDIA    PYRAMID BUY ₹3,409.63 crore at ₹2,082.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,891.83; charges ₹4.04 crore)
2019-04-15  YESBANK     PYRAMID BUY ₹5,134.26 crore at ₹268.45 (box jump — doubling the stake with NEW capital; stop stays ₹245.34; charges ₹6.08 crore)
2019-04-22  JUSTDIAL    SELL ₹5,440.96 crore at stop ₹565.25 (-7.9%, charges ₹5.64 crore) — the cash goes back to work at the next Friday screen
2019-04-22  YESBANK     SELL ₹9,369.26 crore at stop ₹245.34 (-0.7%, charges ₹9.72 crore) — the cash goes back to work at the next Friday screen
2019-04-25  INFRATEL    SELL ₹3,342.00 crore at stop ₹277.35 (-13.3%, charges ₹3.47 crore) — the cash goes back to work at the next Friday screen
2019-04-30  FLFL        BUY ₹4,134.92 crore at ₹483.00 (fresh Friday signal — ACCUMULATE: 1.61× weekly, month 1.89×, ladder rising; stop ₹434.20; charges ₹4.90 crore)
2019-04-30  IBREALEST   BUY ₹4,165.86 crore at ₹125.40 (fresh Friday signal — ACCUMULATE: 3.85× weekly, month 3.02×, ladder rising; stop ₹91.19; charges ₹4.94 crore)
2019-04-30  MTEDUCARE   BUY ₹4,133.49 crore at ₹85.85 (fresh Friday signal — BUY: 2.57× weekly, month 7.09×, ladder rising; stop ₹73.96; charges ₹4.90 crore)
2019-04-30  ONGC        BUY ₹4,131.03 crore at ₹168.00 (fresh Friday signal — BUY: 2.93× weekly, month 1.91×, ladder rising; stop ₹147.44; charges ₹4.89 crore)
2019-04-30  TIIL        SELL ₹638.98 crore at stop ₹502.60 (-22.6%, charges ₹66.28 lakh) — the cash goes back to work at the next Friday screen
2019-05-03  MTEDUCARE   SELL ₹3,553.10 crore at stop ₹73.96 (-13.8%, charges ₹3.69 crore) — the cash goes back to work at the next Friday screen
2019-05-06  RUCHISOYA   BUY ₹4,045.94 crore at ₹9.10 (fresh Friday signal — BUY: 2.65× weekly, month 1.62×, ladder rising; stop ₹5.61; charges ₹4.79 crore)
2019-05-08  SKFINDIA    SELL ₹6,183.77 crore at stop ₹1,891.83 (-6.1%, charges ₹6.41 crore) — the cash goes back to work at the next Friday screen
2019-05-10  PREMEXPLN   SELL ₹3,746.23 crore at stop ₹214.62 (-9.6%, charges ₹3.89 crore) — the cash goes back to work at the next Friday screen
2019-05-13  MTEDUCARE   BUY ₹3,816.99 crore at ₹94.20 (fresh Friday signal — BUY: 1.93× weekly, month 4.89×, ladder rising; stop ₹73.96; charges ₹4.52 crore)
2019-05-14  IBREALEST   SELL ₹3,022.66 crore at stop ₹91.19 (-27.3%, charges ₹3.14 crore) — the cash goes back to work at the next Friday screen
2019-05-16  FLFL        SELL ₹3,708.90 crore at stop ₹434.20 (-10.1%, charges ₹3.85 crore) — the cash goes back to work at the next Friday screen
2019-05-17  MTEDUCARE   SELL ₹2,990.21 crore at stop ₹73.96 (-21.5%, charges ₹3.10 crore) — the cash goes back to work at the next Friday screen
2019-05-20  HEIDELBERG  PYRAMID BUY ₹2,284.37 crore at ₹184.90 (box jump — doubling the stake with NEW capital; stop stays ₹162.93; charges ₹2.71 crore)
2019-05-20  ONGC        PYRAMID BUY ₹4,175.25 crore at ₹170.00 (box jump — doubling the stake with NEW capital; stop stays ₹152.81; charges ₹4.95 crore)
2019-05-27  GRUH        BUY ₹4,550.57 crore at ₹313.00 (fresh Friday signal — ACCUMULATE: 6.22× weekly, month 1.85×, ladder rising; stop ₹265.98; charges ₹5.39 crore)
2019-05-27  INOXLEISUR  BUY ₹4,563.17 crore at ₹349.40 (fresh Friday signal — BUY: 2.36× weekly, month 1.76×, ladder rising; stop ₹282.15; charges ₹5.41 crore)
2019-06-03  AVADHSUGAR  BUY ₹5,404.41 crore at ₹685.10 (fresh Friday signal — ACCUMULATE: 3.70× weekly, month 2.30×, ladder rising; stop ₹617.50; charges ₹6.40 crore)
2019-06-03  MAHSCOOTER  BUY ₹3,049.71 crore at ₹4,343.70 (fresh Friday signal — BUY: 3.58× weekly, month 1.65×, ladder rising; stop ₹3,431.88; charges ₹3.61 crore)
2019-06-03  ONGC        PYRAMID BUY ₹8,492.83 crore at ₹173.00 (box jump — doubling the stake with NEW capital; stop stays ₹160.36; charges ₹10.06 crore)
2019-06-10  MAHSCOOTER  PYRAMID BUY ₹3,054.02 crore at ₹4,355.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,952.00; charges ₹3.62 crore)
2019-06-17  AVADHSUGAR  PYRAMID BUY ₹5,570.56 crore at ₹707.00 (box jump — doubling the stake with NEW capital; stop stays ₹653.70; charges ₹6.60 crore)
2019-06-19  AVADHSUGAR  SELL ₹10,284.43 crore at stop ₹653.70 (-6.1%, charges ₹10.67 crore) — the cash goes back to work at the next Friday screen
2019-06-24  INOXLEISUR  PYRAMID BUY ₹4,212.74 crore at ₹322.95 (box jump — doubling the stake with NEW capital; stop stays ₹291.23; charges ₹4.99 crore)
2019-06-24  SBILIFE     BUY ₹6,438.34 crore at ₹705.15 (fresh Friday signal — BUY: 2.10× weekly, month 1.80×, ladder rising; stop ₹640.30; charges ₹7.63 crore)
2019-06-24  TANLA       BUY ₹3,846.09 crore at ₹69.20 (fresh Friday signal — BUY: 1.54× weekly, month 1.55×, ladder rising; stop ₹49.80; charges ₹4.56 crore)
2019-06-25  RUCHISOYA   SELL ₹2,488.72 crore at stop ₹5.61 (-38.4%, charges ₹2.58 crore) — the cash goes back to work at the next Friday screen
2019-07-01  HEIDELBERG  PYRAMID BUY ₹4,829.03 crore at ₹195.55 (box jump — doubling the stake with NEW capital; stop stays ₹172.09; charges ₹5.72 crore)
2019-07-01  MAHSCOOTER  PYRAMID BUY ₹6,454.91 crore at ₹4,605.05 (box jump — doubling the stake with NEW capital; stop stays ₹4,157.82; charges ₹7.65 crore)
2019-07-01  ONGC        SELL ₹15,719.00 crore at stop ₹160.36 (-6.2%, charges ₹16.31 crore) — the cash goes back to work at the next Friday screen
2019-07-08  MAHSCOOTER  SELL ₹11,637.08 crore at stop ₹4,157.82 (-7.1%, charges ₹12.07 crore) — the cash goes back to work at the next Friday screen
2019-07-08  SBILIFE     PYRAMID BUY ₹6,828.78 crore at ₹748.80 (box jump — doubling the stake with NEW capital; stop stays ₹670.70; charges ₹8.09 crore)
2019-07-15  HEIDELBERG  PYRAMID BUY ₹9,773.26 crore at ₹198.00 (box jump — doubling the stake with NEW capital; stop stays ₹177.65; charges ₹11.58 crore)
2019-07-15  KOTAKGOLD   BUY ₹10,798.96 crore at ₹301.80 (fresh Friday signal — ACCUMULATE: 1.58× weekly, month 1.61×, ladder rising; stop ₹275.74; charges ₹12.79 crore)
2019-07-15  SBILIFE     PYRAMID BUY ₹14,227.32 crore at ₹780.50 (box jump — doubling the stake with NEW capital; stop stays ₹702.62; charges ₹16.86 crore)
2019-07-15  TANLA       PYRAMID BUY ₹3,930.36 crore at ₹70.80 (box jump — doubling the stake with NEW capital; stop stays ₹60.15; charges ₹4.66 crore)
2019-07-15  TRENT       BUY ₹10,828.92 crore at ₹458.20 (fresh Friday signal — ACCUMULATE: 1.80× weekly, month 1.78×, ladder rising; stop ₹393.30; charges ₹12.83 crore)
2019-07-22  BANKBEES    SELL ₹9,946.57 crore at stop ₹295.55 (+4.9%, charges ₹10.32 crore) — the cash goes back to work at the next Friday screen
2019-07-22  GRSE        BUY ₹8,216.92 crore at ₹132.95 (fresh Friday signal — BUY: 2.55× weekly, month 2.75×, ladder rising; stop ₹110.29; charges ₹9.74 crore)
2019-07-23  GRUH        SELL ₹3,858.38 crore at stop ₹265.98 (-15.0%, charges ₹4.00 crore) — the cash goes back to work at the next Friday screen
2019-07-29  HDFCLIFE    BUY ₹10,610.63 crore at ₹499.80 (fresh Friday signal — BUY: 2.03× weekly, month 1.79×, ladder rising; stop ₹425.27; charges ₹12.57 crore)
2019-07-30  TANLA       SELL ₹6,667.41 crore at stop ₹60.15 (-14.1%, charges ₹6.92 crore) — the cash goes back to work at the next Friday screen
2019-07-30  TRENT       SELL ₹9,274.47 crore at stop ₹393.30 (-14.2%, charges ₹9.62 crore) — the cash goes back to work at the next Friday screen
2019-07-31  INOXLEISUR  SELL ₹7,585.56 crore at stop ₹291.23 (-13.4%, charges ₹7.87 crore) — the cash goes back to work at the next Friday screen
2019-08-05  GRSE        PYRAMID BUY ₹8,287.44 crore at ₹134.25 (box jump — doubling the stake with NEW capital; stop stays ₹119.32; charges ₹9.82 crore)
2019-08-05  HDFCLIFE    PYRAMID BUY ₹10,422.06 crore at ₹491.50 (box jump — doubling the stake with NEW capital; stop stays ₹451.35; charges ₹12.35 crore)
2019-08-05  HDFCMFGETF  BUY ₹13,384.73 crore at ₹3,253.50 (fresh Friday signal — BUY: 2.01× weekly, month 1.54×, ladder rising; stop ₹2,862.02; charges ₹15.86 crore)
2019-08-05  KOTAKGOLD   PYRAMID BUY ₹11,349.06 crore at ₹317.55 (box jump — doubling the stake with NEW capital; stop stays ₹287.42; charges ₹13.45 crore)
2019-08-13  BERGEPAINT  BUY ₹13,337.02 crore at ₹359.00 (fresh Friday signal — BUY: 2.99× weekly, month 1.66×, ladder rising; stop ₹311.22; charges ₹15.80 crore)
2019-08-13  HDFCMFGETF  PYRAMID BUY ₹13,900.99 crore at ₹3,383.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,961.24; charges ₹16.47 crore)
2019-08-13  KOTAKGOLD   PYRAMID BUY ₹24,141.97 crore at ₹337.95 (box jump — doubling the stake with NEW capital; stop stays ₹305.90; charges ₹28.60 crore)
2019-08-13  SBILIFE     PYRAMID BUY ₹29,048.07 crore at ₹797.25 (box jump — doubling the stake with NEW capital; stop stays ₹714.92; charges ₹34.42 crore)
2019-08-26  HDFCMFGETF  PYRAMID BUY ₹28,550.17 crore at ₹3,476.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,204.40; charges ₹33.83 crore)
2019-08-26  KOTAKGOLD   PYRAMID BUY ₹48,983.57 crore at ₹343.05 (box jump — doubling the stake with NEW capital; stop stays ₹310.46; charges ₹58.04 crore)
2019-09-03  BERGEPAINT  PYRAMID BUY ₹13,697.85 crore at ₹369.15 (box jump — doubling the stake with NEW capital; stop stays ₹339.44; charges ₹16.23 crore)
2019-09-03  HDFCLIFE    PYRAMID BUY ₹23,370.57 crore at ₹551.40 (box jump — doubling the stake with NEW capital; stop stays ₹487.11; charges ₹27.69 crore)
2019-09-09  GRSE        PYRAMID BUY ₹16,842.69 crore at ₹136.50 (box jump — doubling the stake with NEW capital; stop stays ₹124.07; charges ₹19.96 crore)
2019-09-23  GRSE        PYRAMID BUY ₹38,474.77 crore at ₹156.00 (box jump — doubling the stake with NEW capital; stop stays ₹128.77; charges ₹45.59 crore)
2019-09-30  HDFCLIFE    PYRAMID BUY ₹49,559.97 crore at ₹585.00 (box jump — doubling the stake with NEW capital; stop stays ₹513.00; charges ₹58.72 crore)
2019-10-14  BERGEPAINT  PYRAMID BUY ₹35,489.85 crore at ₹478.50 (box jump — doubling the stake with NEW capital; stop stays ₹401.04; charges ₹42.05 crore)
2019-10-22  HDFCMFGETF  PYRAMID BUY ₹56,966.38 crore at ₹3,470.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,260.49; charges ₹67.49 crore)
2019-11-04  BERGEPAINT  PYRAMID BUY ₹75,459.28 crore at ₹509.00 (box jump — doubling the stake with NEW capital; stop stays ₹451.25; charges ₹89.41 crore)
2019-12-09  HEIDELBERG  SELL ₹17,509.02 crore at stop ₹177.65 (-8.4%, charges ₹18.16 crore) — the cash goes back to work at the next Friday screen
2020-01-08  BERGEPAINT  SELL ₹1.43 lakh crore at stop ₹484.17 (+4.1%, charges ₹148.67 crore) — the cash goes back to work at the next Friday screen
2020-01-13  KITEX       BUY ₹65,634.76 crore at ₹124.10 (fresh Friday signal — BUY: 4.14× weekly, month 2.76×, ladder rising; stop ₹100.79; charges ₹77.77 crore)
2020-01-13  SMLISUZU    BUY ₹65,623.80 crore at ₹595.00 (fresh Friday signal — ACCUMULATE: 4.80× weekly, month 5.17×, ladder rising; stop ₹523.55; charges ₹77.75 crore)
2020-01-20  KITEX       PYRAMID BUY ₹67,088.94 crore at ₹127.00 (box jump — doubling the stake with NEW capital; stop stays ₹115.04; charges ₹79.49 crore)
2020-02-03  GRSE        SELL ₹87,486.08 crore at stop ₹177.65 (+22.1%, charges ₹90.75 crore) — the cash goes back to work at the next Friday screen
2020-02-03  HDFCLIFE    SELL ₹93,384.76 crore at stop ₹552.05 (-0.4%, charges ₹96.87 crore) — the cash goes back to work at the next Friday screen
2020-02-03  KITEX       SELL ₹1.21 lakh crore at stop ₹115.04 (-8.4%, charges ₹125.87 crore) — the cash goes back to work at the next Friday screen
2020-02-03  SBILIFE     SELL ₹66,221.81 crore at stop ₹910.24 (+17.4%, charges ₹68.69 crore) — the cash goes back to work at the next Friday screen
2020-02-10  ALKYLAMINE  BUY ₹68,503.32 crore at ₹1,463.50 (fresh Friday signal — BUY: 4.06× weekly, month 2.68×, ladder rising; stop ₹1,211.25; charges ₹81.16 crore)
2020-02-10  BOROSIL     BUY ₹68,459.72 crore at ₹202.25 (fresh Friday signal — BUY: 8.28× weekly, month 4.15×, ladder rising; stop ₹159.55; charges ₹81.11 crore)
2020-02-10  GMMPFAUDLR  BUY ₹56,688.69 crore at ₹2,940.00 (fresh Friday signal — BUY: 3.83× weekly, month 8.31×, ladder rising; stop ₹2,346.83; charges ₹67.17 crore)
2020-02-10  ORISSAMINE  BUY ₹68,226.14 crore at ₹2,310.00 (fresh Friday signal — BUY: 4.22× weekly, month 3.88×, ladder rising; stop ₹1,110.04; charges ₹80.84 crore)
2020-02-10  SYMPHONY    BUY ₹68,211.56 crore at ₹1,379.50 (fresh Friday signal — BUY: 5.07× weekly, month 2.16×, ladder rising; stop ₹1,131.31; charges ₹80.82 crore)
2020-02-10  TRENT       BUY ₹67,920.49 crore at ₹665.00 (fresh Friday signal — BUY: 4.26× weekly, month 1.73×, ladder rising; stop ₹539.60; charges ₹80.47 crore)
2020-02-17  BOROSIL     PYRAMID BUY ₹64,913.19 crore at ₹192.00 (box jump — doubling the stake with NEW capital; stop stays ₹181.45; charges ₹76.91 crore)
2020-02-17  GMMPFAUDLR  PYRAMID BUY ₹62,141.16 crore at ₹3,226.60 (box jump — doubling the stake with NEW capital; stop stays ₹2,743.17; charges ₹73.63 crore)
2020-02-17  SYMPHONY    PYRAMID BUY ₹67,019.51 crore at ₹1,357.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,240.08; charges ₹79.41 crore)
2020-02-24  ALKYLAMINE  PYRAMID BUY ₹76,627.20 crore at ₹1,639.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,447.61; charges ₹90.79 crore)
2020-02-24  GMMPFAUDLR  PYRAMID BUY ₹1.27 lakh crore at ₹3,308.90 (box jump — doubling the stake with NEW capital; stop stays ₹3,002.00; charges ₹150.92 crore)
2020-02-27  GMMPFAUDLR  SELL ₹2.31 lakh crore at stop ₹3,002.00 (-6.1%, charges ₹239.36 crore) — the cash goes back to work at the next Friday screen
2020-02-27  SMLISUZU    SELL ₹57,615.25 crore at stop ₹523.55 (-12.0%, charges ₹59.76 crore) — the cash goes back to work at the next Friday screen
2020-03-02  FAIRCHEM    BUY ₹1.06 lakh crore at ₹657.00 (fresh Friday signal — BUY: 9.81× weekly, month 11.50×, ladder rising; stop ₹561.73; charges ₹125.88 crore)
2020-03-06  FAIRCHEM    SELL ₹90,636.99 crore at stop ₹561.73 (-14.5%, charges ₹94.02 crore) — the cash goes back to work at the next Friday screen
2020-03-06  SYMPHONY    SELL ₹1.22 lakh crore at stop ₹1,240.08 (-9.4%, charges ₹126.85 crore) — the cash goes back to work at the next Friday screen
2020-03-09  ALKYLAMINE  SELL ₹1.35 lakh crore at stop ₹1,447.61 (-6.7%, charges ₹140.18 crore) — the cash goes back to work at the next Friday screen
2020-03-09  DEEPAKNTR   BUY ₹1.08 lakh crore at ₹508.80 (fresh Friday signal — BUY: 2.89× weekly, month 3.36×, ladder rising; stop ₹356.25; charges ₹128.55 crore)
2020-03-09  INDOCO      BUY ₹1.08 lakh crore at ₹228.20 (fresh Friday signal — ACCUMULATE: 2.23× weekly, month 2.83×, ladder rising; stop ₹164.08; charges ₹128.07 crore)
2020-03-09  LALPATHLAB  BUY ₹70,110.62 crore at ₹1,670.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.76×, ladder rising; stop ₹1,486.75; charges ₹83.07 crore)
2020-03-09  ORISSAMINE  PYRAMID BUY ₹49,825.72 crore at ₹1,689.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,383.30; charges ₹59.03 crore)
2020-03-09  SETFGOLD    BUY ₹1.08 lakh crore at ₹3,862.80 (fresh Friday signal — BUY: 3.14× weekly, month 2.47×, ladder rising; stop ₹3,548.39; charges ₹128.37 crore)
2020-03-13  HDFCMFGETF  SELL ₹1.16 lakh crore at stop ₹3,540.65 (+3.1%, charges ₹120.39 crore) — the cash goes back to work at the next Friday screen
2020-03-13  INDOCO      SELL ₹77,549.09 crore at stop ₹164.08 (-28.1%, charges ₹80.44 crore) — the cash goes back to work at the next Friday screen
2020-03-13  LALPATHLAB  SELL ₹62,278.79 crore at stop ₹1,486.75 (-11.0%, charges ₹64.60 crore) — the cash goes back to work at the next Friday screen
2020-03-13  TRENT       SELL ₹54,990.28 crore at stop ₹539.60 (-18.9%, charges ₹57.04 crore) — the cash goes back to work at the next Friday screen
2020-03-17  KOTAKGOLD   SELL ₹1.01 lakh crore at stop ₹352.69 (+5.8%, charges ₹104.31 crore) — the cash goes back to work at the next Friday screen
2020-03-17  ORISSAMINE  SELL ₹81,482.19 crore at stop ₹1,383.30 (-30.8%, charges ₹84.52 crore) — the cash goes back to work at the next Friday screen
2020-03-17  SETFGOLD    SELL ₹99,308.00 crore at stop ₹3,548.39 (-8.1%, charges ₹103.01 crore) — the cash goes back to work at the next Friday screen
2020-03-19  DEEPAKNTR   SELL ₹75,796.74 crore at stop ₹356.25 (-30.0%, charges ₹78.62 crore) — the cash goes back to work at the next Friday screen
```
