# The Darvas screen — 2015-03-01 → 2020-03-31

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2014-03-01 → 2020-03-31, 1522 symbols, in `ROLLING_2014-03-01_to_2020-03-31/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **The universe is POINT-IN-TIME with a ROLLING radar:** membership is recomputed EVERY MONTH as the top symbols by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and new listings or emerging names ENTER the month they earn their place, so neither survivorship bias nor an emergence blind spot remains. Membership gates fresh entries only; a held position runs to its stop regardless (`_membership_long.csv`). Raw exchange data means heuristic split/bonus adjustment, every one listed in `_adjustments.csv`. No slippage, stop exits at the stop price, fractional shares. Stored fiscal statements exist for 31% of this universe — a stock without statements cannot be blocked by the earnings gate (only a FALLING verdict blocks), which loosens that gate for the rest.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), at the next trading day's open, falling earnings power refused, nothing below half a slice. **Funding order:** a fully-qualified signal the cash never reached climbs the queue each time it is starved and goes to the FRONT ahead of louder newcomers, resetting to normal once funded — so a steady climber flagged week after week can no longer be outbid forever by one-week volume spikes; fresh names rank by volume reaction. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with a RECYCLING POCKET, 3× cap.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled at the next day's open — at most THREE times per position (8× the first slice). The doubling money lives in its own POCKET, outside the trading book: when a doubled position sells, the pyramid lots' capital AND their returns go OUT to the pocket (only the initial slice and its returns stay in the portfolio, so the trading book can never balloon), and later doubles draw the pocket FIRST — fresh outside money enters only for the shortfall, each such injection dated and logged, so the honest yardstick is the money-weighted return (XIRR) and the capital requirement stays bounded. Each add-on is its own tax lot on its own holding clock (the pocket pays tax on its own gains); the ratcheted stop covers the whole enlarged position; a jump past the cap is logged, never doubled.

## The headline — XIRR is the honest yardstick

| Engine | Money put in | Final value | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | ₹606.60 (₹100 + ₹506.60 injected) | **₹393.78** | **-8.71%** |
| B: doubling, before charges and tax | ₹611.24 | ₹406.67 | -8.24% |
| **A: no doubling, NET of charges and tax** | ₹100.00 | **₹88.99** | **-2.27%** |
| A: no doubling, before charges and tax | ₹100.00 | ₹97.76 | -0.45% |
| Nifty 50 (pre-cost, pre-tax) | ₹100.00 | ₹96.20 | -0.76% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹0.00; unrealised gains in both end books carry further deferred liabilities.*

5.07 years, 266 weekly screens. Engine B's total doubling spend was ₹4,237.03: the pocket recycled ₹3,730.43 of it, and only ₹506.60 was fresh outside money across 21 dated injections (all in the blotter and events CSV). The pocket holds ₹349.85 at the end, counted in the final value.

## What the frictions took (net runs)

| | Engine A: no doubling | Engine B: doubling |
|---|---:|---:|
| Transaction charges | ₹4.52 | ₹3.26 |
| Capital-gains tax paid | ₹8.71 | ₹0.00 |
| Tax accrued, final part-year | ₹0.00 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling) — portfolio book

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2015 | 2015-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹4.14 / ₹0.00 |
| FY2016 | 2016-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹19.58 / ₹0.00 |
| FY2017 | 2017-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹34.47 / ₹0.00 |
| FY2018 | 2018-04-02 | ₹0.00 | ₹0.00 | ₹0.00 | ₹36.59 / ₹0.00 |
| FY2019 | 2019-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹43.28 / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹60.38 / ₹0.00 |

### Tax ledger — Engine B — the doubling pocket's own book

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2015 | 2015-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹1.81 / ₹0.00 |
| FY2016 | 2016-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹86.78 / ₹0.00 |
| FY2017 | 2017-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹102.00 / ₹0.00 |
| FY2018 | 2018-04-02 | ₹0.00 | ₹0.00 | ₹0.00 | ₹145.01 / ₹0.00 |
| FY2019 | 2019-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹141.02 / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹141.65 / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2015 | 2015-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹4.90 / ₹0.00 |
| FY2016 | 2016-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹9.98 / ₹0.00 |
| FY2017 | 2017-04-03 | ₹2.76 | ₹0.00 | ₹0.55 | ₹0.00 / ₹0.00 |
| FY2018 | 2018-04-02 | ₹40.80 | ₹0.00 | ₹8.16 | ₹0.00 / ₹0.00 |
| FY2019 | 2019-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹14.75 / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹42.13 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2015 (2015-12-24) | ₹104.49 | +4.5% | ₹493.15 | ₹470.27 | -20.0% | -12.0% |
| 2016 (2016-12-30) | ₹104.63 | +0.1% | ₹482.35 | ₹36.34 | -9.3% | +4.1% |
| 2017 (2017-12-29) | ₹159.26 | +52.2% | ₹471.71 | ₹0.00 | -2.2% | +28.6% |
| 2018 (2018-12-28) | ₹123.23 | -22.6% | ₹415.29 | ₹0.00 | -12.0% | +3.1% |
| 2019 (2019-12-27) | ₹103.25 | -16.2% | ₹408.14 | ₹0.00 | -1.7% | +12.8% |
| 2020 (2020-03-31) | ₹88.99 | -13.8% | ₹393.78 | ₹0.00 | -3.5% | -29.8% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-37.6%** (A: -50.5%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **117 closed trades**: 19 winners (16%), average winner +12.5%, average loser -11.5% (returns per blended entry price).
- Best closed trade BALMLAWRIE +82.4%; worst RUCHISOYA -38.4%.
- Median holding period 46 days.
- Cash share of equity averaged 3%; fully in cash 1 of 266 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

*B equity counts the whole system — trading book plus the idle doubling pocket (shown separately).*

| Month-end screen | B equity | B pocket | B injected so far | B cash | B positions | A equity |
|---|---:|---:|---:|---:|---:|---:|
| 2015-03-27 | ₹168.44 | ₹18.03 | ₹81.57 | ₹18.51 | 7 | ₹90.61 |
| 2015-04-30 | ₹172.64 | ₹64.82 | ₹90.83 | ₹37.48 | 4 | ₹87.86 |
| 2015-05-29 | ₹170.25 | ₹4.86 | ₹90.83 | ₹2.29 | 7 | ₹86.72 |
| 2015-06-26 | ₹210.67 | ₹0.00 | ₹121.58 | ₹0.00 | 7 | ₹88.81 |
| 2015-07-31 | ₹487.68 | ₹40.15 | ₹325.91 | ₹13.40 | 6 | ₹106.27 |
| 2015-08-28 | ₹566.26 | ₹419.79 | ₹470.27 | ₹73.10 | 2 | ₹100.18 |
| 2015-09-24 | ₹555.84 | ₹399.16 | ₹470.27 | ₹7.30 | 6 | ₹94.13 |
| 2015-10-30 | ₹537.89 | ₹285.54 | ₹470.27 | ₹38.03 | 4 | ₹96.51 |
| 2015-11-27 | ₹528.54 | ₹320.30 | ₹470.27 | ₹18.54 | 3 | ₹101.43 |
| 2015-12-24 | ₹493.15 | ₹340.47 | ₹470.27 | ₹0.00 | 6 | ₹104.49 |
| 2016-01-29 | ₹478.79 | ₹325.19 | ₹470.27 | ₹29.93 | 3 | ₹100.03 |
| 2016-02-26 | ₹456.12 | ₹359.27 | ₹470.27 | ₹26.31 | 4 | ₹88.45 |
| 2016-03-23 | ₹464.46 | ₹341.21 | ₹470.27 | ₹1.82 | 7 | ₹97.12 |
| 2016-04-29 | ₹466.59 | ₹277.31 | ₹470.27 | ₹0.00 | 7 | ₹96.96 |
| 2016-05-27 | ₹462.48 | ₹175.76 | ₹470.27 | ₹9.55 | 5 | ₹93.14 |
| 2016-06-24 | ₹493.23 | ₹130.31 | ₹470.27 | ₹9.55 | 5 | ₹98.76 |
| 2016-07-29 | ₹547.99 | ₹102.54 | ₹506.60 | ₹0.00 | 5 | ₹109.96 |
| 2016-08-26 | ₹537.50 | ₹111.50 | ₹506.60 | ₹12.09 | 4 | ₹112.10 |
| 2016-09-30 | ₹509.60 | ₹293.14 | ₹506.60 | ₹35.22 | 3 | ₹117.14 |
| 2016-10-28 | ₹505.34 | ₹233.69 | ₹506.60 | ₹0.00 | 5 | ₹117.82 |
| 2016-11-25 | ₹480.19 | ₹416.05 | ₹506.60 | ₹25.46 | 3 | ₹102.13 |
| 2016-12-30 | ₹482.35 | ₹373.51 | ₹506.60 | ₹8.04 | 5 | ₹104.63 |
| 2017-01-27 | ₹486.55 | ₹311.19 | ₹506.60 | ₹0.00 | 6 | ₹108.50 |
| 2017-02-23 | ₹467.40 | ₹355.62 | ₹506.60 | ₹14.04 | 5 | ₹106.31 |
| 2017-03-31 | ₹474.89 | ₹257.69 | ₹506.60 | ₹9.99 | 5 | ₹109.85 |
| 2017-04-28 | ₹503.30 | ₹148.93 | ₹506.60 | ₹9.99 | 5 | ₹117.21 |
| 2017-05-26 | ₹482.12 | ₹245.44 | ₹506.60 | ₹45.73 | 2 | ₹112.71 |
| 2017-06-30 | ₹481.99 | ₹295.15 | ₹506.60 | ₹30.91 | 2 | ₹120.48 |
| 2017-07-28 | ₹459.82 | ₹395.50 | ₹506.60 | ₹19.18 | 3 | ₹122.63 |
| 2017-08-24 | ₹450.94 | ₹382.45 | ₹506.60 | ₹0.00 | 7 | ₹112.38 |
| 2017-09-29 | ₹444.10 | ₹307.85 | ₹506.60 | ₹12.79 | 5 | ₹120.04 |
| 2017-10-27 | ₹462.88 | ₹219.61 | ₹506.60 | ₹0.00 | 6 | ₹142.08 |
| 2017-11-24 | ₹445.03 | ₹357.76 | ₹506.60 | ₹3.62 | 6 | ₹153.02 |
| 2017-12-29 | ₹471.71 | ₹265.66 | ₹506.60 | ₹0.00 | 6 | ₹159.26 |
| 2018-01-25 | ₹474.61 | ₹224.41 | ₹506.60 | ₹0.00 | 6 | ₹169.37 |
| 2018-02-23 | ₹428.27 | ₹271.04 | ₹506.60 | ₹0.00 | 5 | ₹156.50 |
| 2018-03-28 | ₹413.70 | ₹290.64 | ₹506.60 | ₹17.43 | 4 | ₹149.96 |
| 2018-04-27 | ₹439.07 | ₹216.34 | ₹506.60 | ₹4.45 | 5 | ₹159.15 |
| 2018-05-25 | ₹446.10 | ₹188.86 | ₹506.60 | ₹2.56 | 4 | ₹152.40 |
| 2018-06-29 | ₹425.88 | ₹201.24 | ₹506.60 | ₹17.33 | 3 | ₹137.65 |
| 2018-07-27 | ₹433.92 | ₹183.54 | ₹506.60 | ₹0.00 | 4 | ₹141.41 |
| 2018-08-31 | ₹458.12 | ₹146.89 | ₹506.60 | ₹0.00 | 4 | ₹150.43 |
| 2018-09-28 | ₹421.71 | ₹361.27 | ₹506.60 | ₹53.74 | 1 | ₹132.82 |
| 2018-10-26 | ₹421.00 | ₹361.27 | ₹506.60 | ₹41.72 | 3 | ₹129.41 |
| 2018-11-30 | ₹419.97 | ₹348.56 | ₹506.60 | ₹21.38 | 6 | ₹127.70 |
| 2018-12-28 | ₹415.29 | ₹352.90 | ₹506.60 | ₹6.80 | 8 | ₹123.23 |
| 2019-01-25 | ₹412.55 | ₹297.82 | ₹506.60 | ₹0.00 | 9 | ₹120.47 |
| 2019-02-22 | ₹407.49 | ₹306.95 | ₹506.60 | ₹5.25 | 7 | ₹115.10 |
| 2019-03-29 | ₹416.70 | ₹283.66 | ₹506.60 | ₹0.00 | 7 | ₹119.20 |
| 2019-04-26 | ₹409.22 | ₹264.73 | ₹506.60 | ₹17.52 | 5 | ₹113.04 |
| 2019-05-31 | ₹402.21 | ₹301.61 | ₹506.60 | ₹0.54 | 5 | ₹104.82 |
| 2019-06-28 | ₹398.29 | ₹292.36 | ₹506.60 | ₹5.66 | 4 | ₹98.03 |
| 2019-07-26 | ₹394.45 | ₹316.57 | ₹506.60 | ₹13.24 | 3 | ₹95.06 |
| 2019-08-30 | ₹394.20 | ₹273.57 | ₹506.60 | ₹1.41 | 5 | ₹97.27 |
| 2019-09-27 | ₹394.62 | ₹229.16 | ₹506.60 | ₹1.41 | 5 | ₹98.86 |
| 2019-10-25 | ₹408.26 | ₹173.64 | ₹506.60 | ₹1.41 | 5 | ₹102.82 |
| 2019-11-29 | ₹401.57 | ₹173.64 | ₹506.60 | ₹1.41 | 5 | ₹101.25 |
| 2019-12-27 | ₹408.14 | ₹199.49 | ₹506.60 | ₹10.04 | 4 | ₹103.25 |
| 2020-01-31 | ₹408.37 | ₹199.49 | ₹506.60 | ₹10.04 | 4 | ₹102.38 |
| 2020-02-28 | ₹402.60 | ₹288.66 | ₹506.60 | ₹0.00 | 5 | ₹102.50 |
| 2020-03-31 | ₹393.78 | ₹349.85 | ₹506.60 | ₹23.81 | 2 | ₹88.99 |

## Engine B — still held at the end

| Stock | First entry | Blended entry ₹ | Lots | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|---:|
| BOROSIL | 2020-02-10 | 197.13 | 2 | 220.15 | 181.45 | +11.7% |
| TUBEINVEST | 2017-07-31 | 756.00 | 1 | 793.20 | 680.20 | +4.9% |

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
| ITDCEM | 2015-03-09 | 75.95 | 2 | 2015-04-27 | 64.03 | -15.7% |
| SOMANYCERA | 2015-03-09 | 395.05 | 3 | 2015-04-27 | 418.24 | +5.9% |
| HCC | 2015-03-09 | 34.68 | 2 | 2015-04-27 | 31.21 | -10.0% |
| CIMMCO | 2015-04-27 | 105.58 | 2 | 2015-06-03 | 85.29 | -19.2% |
| ABIRLANUVO | 2015-05-11 | 930.90 | 2 | 2015-06-03 | 850.92 | -8.6% |
| MANINFRA | 2015-04-27 | 46.45 | 3 | 2015-07-27 | 41.85 | -9.9% |
| VADILALIND | 2015-05-04 | 605.41 | 4 | 2015-08-13 | 716.44 | +18.3% |
| SMLISUZU | 2015-03-09 | 1,138.57 | 4 | 2015-08-24 | 1,110.20 | -2.5% |
| NILKAMAL | 2015-05-18 | 896.53 | 4 | 2015-08-24 | 927.12 | +3.4% |
| MANINDS | 2015-06-08 | 98.13 | 4 | 2015-08-24 | 95.77 | -2.4% |
| GARWALLROP | 2015-08-17 | 309.90 | 1 | 2015-08-25 | 274.60 | -11.4% |
| MANGALAM | 2015-06-08 | 69.68 | 3 | 2015-09-08 | 73.50 | +5.5% |
| ICIL | 2015-08-31 | 199.78 | 1 | 2015-09-08 | 145.90 | -27.0% |
| CAPLIPOINT | 2015-09-07 | 304.00 | 2 | 2015-10-28 | 262.64 | -13.6% |
| NEULANDLAB | 2015-09-14 | 808.82 | 4 | 2015-10-29 | 714.39 | -11.7% |
| JUBLINDS | 2015-08-31 | 298.50 | 2 | 2015-11-02 | 224.21 | -24.9% |
| ABBOTINDIA | 2015-09-07 | 5,544.31 | 2 | 2015-11-06 | 5,365.17 | -3.2% |
| UCOBANK | 2015-11-02 | 50.30 | 1 | 2015-11-09 | 45.79 | -9.0% |
| JINDALPOLY | 2015-09-07 | 518.59 | 4 | 2015-11-26 | 494.38 | -4.7% |
| INTELLECT | 2015-11-09 | 264.39 | 3 | 2015-12-09 | 252.22 | -4.6% |
| TRIGYN | 2015-11-16 | 88.11 | 3 | 2015-12-10 | 82.94 | -5.9% |
| ECLERX | 2015-03-09 | 1,718.52 | 4 | 2015-12-17 | 1,619.75 | -5.7% |
| NCLIND | 2015-12-14 | 170.72 | 2 | 2016-01-07 | 151.19 | -11.4% |
| TWL | 2015-12-21 | 161.17 | 2 | 2016-01-07 | 151.43 | -6.0% |
| SHARONBIO | 2015-12-14 | 30.40 | 2 | 2016-01-12 | 26.93 | -11.4% |
| EDL | 2015-12-14 | 102.97 | 2 | 2016-01-13 | 87.83 | -14.7% |
| NILKAMAL | 2016-01-11 | 1,423.80 | 1 | 2016-01-18 | 1,174.87 | -17.5% |
| AJMERA | 2015-12-14 | 130.62 | 2 | 2016-01-22 | 103.22 | -21.0% |
| TRIVENI | 2015-11-30 | 45.50 | 3 | 2016-02-04 | 41.33 | -9.2% |
| PRICOL | 2016-02-01 | 50.17 | 2 | 2016-02-29 | 41.77 | -16.7% |
| ENERGYDEV | 2016-03-08 | 64.92 | 3 | 2016-04-12 | 60.80 | -6.3% |
| RSSOFTWARE | 2016-04-18 | 111.20 | 2 | 2016-05-18 | 93.44 | -16.0% |
| BBL | 2016-01-11 | 982.64 | 3 | 2016-05-20 | 878.75 | -10.6% |
| DALMIASUG | 2016-03-14 | 99.02 | 2 | 2016-05-24 | 86.86 | -12.3% |
| TPLPLASTEH | 2016-05-23 | 492.24 | 4 | 2016-07-22 | 465.74 | -5.4% |
| RAMKY | 2016-03-08 | 78.44 | 4 | 2016-08-10 | 79.04 | +0.8% |
| SOMANYCERA | 2016-01-25 | 400.86 | 4 | 2016-09-21 | 551.10 | +37.5% |
| TATAMETALI | 2016-07-25 | 446.05 | 2 | 2016-09-29 | 366.19 | -17.9% |
| HERITGFOOD | 2016-09-26 | 451.85 | 2 | 2016-11-04 | 398.05 | -11.9% |
| GLOBUSSPR | 2016-10-03 | 107.10 | 2 | 2016-11-04 | 95.00 | -11.3% |
| CENTURYTEX | 2016-10-03 | 939.51 | 2 | 2016-11-09 | 863.60 | -8.1% |
| GOLDBEES | 2016-02-15 | 2,681.07 | 4 | 2016-11-17 | 2,689.64 | +0.3% |
| HDFCMFGETF | 2016-03-14 | 2,865.83 | 4 | 2016-11-18 | 2,718.90 | -5.1% |
| SESHAPAPER | 2016-11-07 | 164.20 | 1 | 2016-11-22 | 113.48 | -30.9% |
| STARPAPER | 2016-11-15 | 186.62 | 3 | 2016-12-13 | 175.94 | -5.7% |
| SWANENERGY | 2016-12-19 | 202.30 | 1 | 2016-12-22 | 155.80 | -23.0% |
| BALMLAWRIE | 2016-11-21 | 547.18 | 2 | 2016-12-26 | 997.98 | +82.4% |
| STCINDIA | 2016-12-26 | 187.58 | 2 | 2017-01-30 | 187.15 | -0.2% |
| SHREEPUSHK | 2016-11-07 | 189.88 | 4 | 2017-02-15 | 176.18 | -7.2% |
| UJAAS | 2016-12-05 | 48.65 | 2 | 2017-02-21 | 40.27 | -17.2% |
| ESSELPACK | 2016-12-05 | 126.41 | 3 | 2017-02-21 | 115.95 | -8.3% |
| INDIAGLYCO | 2017-01-09 | 154.17 | 2 | 2017-03-20 | 150.48 | -2.4% |
| MERCK | 2016-12-05 | 993.86 | 4 | 2017-05-19 | 1,045.00 | +5.1% |
| VIJAYABANK | 2017-02-06 | 67.07 | 4 | 2017-05-23 | 78.29 | +16.7% |
| RAIN | 2017-02-27 | 101.06 | 3 | 2017-05-23 | 96.95 | -4.1% |
| NFL | 2017-02-20 | 78.16 | 4 | 2017-06-23 | 74.38 | -4.8% |
| SHAKTIPUMP | 2017-05-29 | 433.31 | 3 | 2017-06-28 | 415.62 | -4.1% |
| GVKPIL | 2017-07-03 | 8.55 | 2 | 2017-07-13 | 7.32 | -14.4% |
| GRASIM | 2017-02-20 | 1,137.12 | 4 | 2017-07-19 | 1,180.47 | +3.8% |
| MEP | 2017-07-03 | 129.85 | 3 | 2017-07-27 | 115.55 | -11.0% |
| BALAJITELE | 2017-07-24 | 188.00 | 1 | 2017-08-10 | 149.25 | -20.6% |
| SREINFRA | 2017-07-24 | 128.45 | 2 | 2017-08-10 | 108.49 | -15.5% |
| BEML | 2017-07-31 | 1,673.00 | 1 | 2017-08-10 | 1,438.35 | -14.0% |
| JPINFRATEC | 2017-07-31 | 22.40 | 1 | 2017-08-14 | 17.20 | -23.2% |
| INSECTICID | 2017-08-14 | 847.44 | 3 | 2017-09-21 | 821.75 | -3.0% |
| SPARC | 2017-08-21 | 393.50 | 2 | 2017-09-25 | 362.19 | -8.0% |
| FRETAIL | 2017-08-14 | 529.87 | 4 | 2017-11-09 | 500.65 | -5.5% |
| AVANTIFEED | 2017-08-21 | 2,350.31 | 4 | 2017-11-15 | 2,641.00 | +12.4% |
| BBTC | 2017-10-03 | 1,551.58 | 4 | 2017-11-16 | 1,497.44 | -3.5% |
| UTTAMSUGAR | 2017-08-14 | 188.35 | 2 | 2017-12-05 | 155.58 | -17.4% |
| AJMERA | 2017-11-20 | 319.89 | 2 | 2017-12-12 | 313.50 | -2.0% |
| WSTCSTPAPR | 2017-12-11 | 316.65 | 3 | 2018-01-30 | 287.04 | -9.4% |
| AUTOAXLES | 2017-11-20 | 1,538.19 | 3 | 2018-01-31 | 1,530.26 | -0.5% |
| HINDOILEXP | 2017-11-20 | 132.90 | 4 | 2018-02-02 | 122.15 | -8.1% |
| JKPAPER | 2017-12-18 | 147.51 | 4 | 2018-02-02 | 132.33 | -10.3% |
| HOVS | 2017-05-29 | 297.15 | 3 | 2018-03-22 | 243.00 | -18.2% |
| ESTER | 2018-02-05 | 69.32 | 2 | 2018-05-10 | 65.17 | -6.0% |
| EXCELINDUS | 2018-04-09 | 1,214.40 | 2 | 2018-05-11 | 1,282.59 | +5.6% |
| LUXIND | 2018-02-05 | 1,769.42 | 4 | 2018-05-30 | 1,852.59 | +4.7% |
| BODALCHEM | 2018-06-04 | 144.55 | 2 | 2018-06-26 | 129.25 | -10.6% |
| FSL | 2018-05-14 | 71.65 | 2 | 2018-08-10 | 63.32 | -11.6% |
| PAGEIND | 2018-07-02 | 31,724.70 | 4 | 2018-09-05 | 32,310.88 | +1.8% |
| TCIEXP | 2018-08-13 | 716.25 | 2 | 2018-09-05 | 652.46 | -8.9% |
| LTI | 2018-09-10 | 1,955.00 | 1 | 2018-09-21 | 1,643.31 | -15.9% |
| MPHASIS | 2018-02-05 | 1,018.02 | 4 | 2018-09-25 | 1,173.72 | +15.3% |
| VINDHYATEL | 2018-09-10 | 1,569.01 | 2 | 2018-09-26 | 1,378.45 | -12.1% |
| MUTHOOTFIN | 2018-09-24 | 452.00 | 1 | 2018-09-27 | 412.35 | -8.8% |
| BIRLACABLE | 2018-11-26 | 217.45 | 2 | 2018-12-04 | 195.70 | -10.0% |
| DALMIASUG | 2018-11-19 | 103.00 | 2 | 2018-12-10 | 94.14 | -8.6% |
| GODFRYPHLP | 2018-12-03 | 928.20 | 2 | 2018-12-26 | 812.30 | -12.5% |
| BEML | 2018-12-24 | 893.05 | 2 | 2019-01-28 | 809.88 | -9.3% |
| KESORAMIND | 2018-12-03 | 85.00 | 1 | 2019-01-29 | 71.39 | -16.0% |
| HATHWAY | 2018-10-22 | 30.43 | 2 | 2019-02-19 | 26.93 | -11.5% |
| BAJAJHIND | 2018-10-15 | 9.98 | 2 | 2019-03-20 | 7.69 | -22.9% |
| JUSTDIAL | 2019-03-25 | 613.48 | 2 | 2019-04-22 | 565.25 | -7.9% |
| INFRATEL | 2019-02-11 | 319.80 | 2 | 2019-04-25 | 277.35 | -13.3% |
| TIIL | 2018-11-05 | 648.95 | 1 | 2019-04-30 | 502.60 | -22.6% |
| SKFINDIA | 2019-01-14 | 2,015.13 | 3 | 2019-05-08 | 1,891.83 | -6.1% |
| PREMEXPLN | 2018-12-17 | 237.36 | 3 | 2019-05-10 | 214.62 | -9.6% |
| IBREALEST | 2019-04-30 | 125.40 | 1 | 2019-05-14 | 91.19 | -27.3% |
| MTEDUCARE | 2019-05-13 | 94.20 | 1 | 2019-05-17 | 73.96 | -21.5% |
| RUCHISOYA | 2019-05-06 | 9.10 | 1 | 2019-06-25 | 5.61 | -38.4% |
| BANKBEES | 2018-12-17 | 281.62 | 4 | 2019-07-22 | 295.55 | +4.9% |
| INOXLEISUR | 2019-05-27 | 336.18 | 2 | 2019-07-31 | 291.23 | -13.4% |
| HEIDELBERG | 2019-05-27 | 199.44 | 3 | 2019-12-09 | 177.65 | -10.9% |
| SBILIFE | 2019-07-29 | 824.67 | 4 | 2020-02-03 | 910.24 | +10.4% |
| HDFCLIFE | 2019-07-29 | 554.24 | 4 | 2020-02-03 | 552.05 | -0.4% |
| SUDARSCHEM | 2020-02-10 | 463.00 | 2 | 2020-03-09 | 431.73 | -6.8% |
| HDFCMFGETF | 2019-08-05 | 3,433.53 | 4 | 2020-03-13 | 3,540.65 | +3.1% |
| TRENT | 2020-02-10 | 665.00 | 1 | 2020-03-13 | 539.60 | -18.9% |

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
2015-03-17  MADHUCON    SELL ₹17.27 at stop ₹55.38 (-9.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.63 of doubled capital and its returns OUT to the pocket
2015-03-23  ECLERX      PYRAMID BUY ₹9.98 at ₹1,569.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,320.70; charges ₹0.01)
2015-03-23  GEOMETRIC   PYRAMID BUY ₹22.13 at ₹175.00 (box jump — doubling the stake with NEW capital; stop stays ₹158.22; charges ₹0.03)
2015-03-23  ITDCEM      PYRAMID BUY ₹9.73 at ₹74.94 (box jump — doubling the stake with NEW capital; stop stays ₹64.03; funded ₹8.63 from the pocket + ₹1.10 fresh; charges ₹0.01)
2015-03-23  JBMA        SELL ₹18.28 at stop ₹222.30 (-6.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹9.14 of doubled capital and its returns OUT to the pocket
2015-03-23  KEI         SELL ₹17.80 at stop ₹59.38 (-8.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.89 of doubled capital and its returns OUT to the pocket
2015-03-23  SOMANYCERA  PYRAMID BUY ₹9.17 at ₹372.00 (box jump — doubling the stake with NEW capital; stop stays ₹341.63; charges ₹0.01)
2015-03-23  ZYDUSWELL   BUY ₹17.58 at ₹1,051.70 (fresh Friday signal — BUY: 3.59× weekly, month 2.15×, ladder rising; stop ₹663.79; charges ₹0.02)
2015-03-30  DYNAMATECH  BUY ₹17.39 at ₹3,843.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 10.44× weekly, month 3.95×, ladder rising; stop ₹3,081.75; charges ₹0.02)
2015-03-30  ZYDUSWELL   PYRAMID BUY ₹17.11 at ₹1,025.00 (box jump — doubling the stake with NEW capital; stop stays ₹960.45; funded ₹17.11 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-04-01  TAX         FY2015 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹4.14 / LT ₹0.00)
2015-04-06  SMLISUZU    PYRAMID BUY ₹10.17 at ₹1,232.00 (box jump — doubling the stake with NEW capital; stop stays ₹983.70; funded ₹0.92 from the pocket + ₹9.26 fresh; charges ₹0.01)
2015-04-20  ZYDUSWELL   SELL ₹32.02 at stop ₹960.45 (-7.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹16.00 of doubled capital and its returns OUT to the pocket
2015-04-22  DYNAMATECH  SELL ₹13.91 at stop ₹3,081.75 (-19.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2015-04-22  GEOMETRIC   SELL ₹39.94 at stop ₹158.22 (-6.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹29.94 of doubled capital and its returns OUT to the pocket
2015-04-27  CIMMCO      BUY ₹15.40 at ₹110.55 (fresh Friday signal — ACCUMULATE: 3.65× weekly, month 2.21×, ladder rising; stop ₹66.22; charges ₹0.02)
2015-04-27  HCC         PYRAMID BUY ₹8.94 at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹31.21; funded ₹8.94 from the pocket + ₹0.00 fresh; charges ₹0.01)
2015-04-27  HCC         SELL ₹16.94 at stop ₹31.21 (-10.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.47 of doubled capital and its returns OUT to the pocket
2015-04-27  ITDCEM      SELL ₹16.59 at stop ₹64.03 (-15.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.29 of doubled capital and its returns OUT to the pocket
2015-04-27  MANINFRA    BUY ₹15.25 at ₹47.50 (fresh Friday signal — BUY: 2.74× weekly, month 1.90×, ladder rising; stop ₹39.19; charges ₹0.02)
2015-04-27  SOMANYCERA  PYRAMID BUY ₹19.78 at ₹401.60 (box jump — doubling the stake with NEW capital; stop stays ₹418.24; funded ₹19.78 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-04-27  SOMANYCERA  SELL ₹41.14 at stop ₹418.24 (+5.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹30.84 of doubled capital and its returns OUT to the pocket
2015-05-04  VADILALIND  BUY ₹11.20 at ₹487.00 (fresh Friday signal — BUY: 10.46× weekly, month 4.23×, ladder rising; stop ₹323.00; charges ₹0.01)
2015-05-11  ABIRLANUVO  BUY ₹11.97 at ₹945.00 (fresh Friday signal — BUY: 5.18× weekly, month 1.67×, ladder rising; stop ₹713.90; charges ₹0.01)
2015-05-11  VADILALIND  PYRAMID BUY ₹11.60 at ₹505.00 (box jump — doubling the stake with NEW capital; stop stays ₹451.91; funded ₹11.60 from the pocket + ₹0.00 fresh; charges ₹0.01)
2015-05-18  NILKAMAL    BUY ₹12.02 at ₹524.95 (fresh Friday signal — BUY: 5.24× weekly, month 2.21×, ladder rising; stop ₹413.10; charges ₹0.01)
2015-05-25  ABIRLANUVO  PYRAMID BUY ₹11.60 at ₹916.77 (box jump — doubling the stake with NEW capital; stop stays ₹850.92; funded ₹11.60 from the pocket + ₹0.00 fresh; charges ₹0.01)
2015-05-25  CIMMCO      PYRAMID BUY ₹14.00 at ₹100.60 (box jump — doubling the stake with NEW capital; stop stays ₹85.29; funded ₹14.00 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-05-25  VADILALIND  PYRAMID BUY ₹22.76 at ₹496.00 (box jump — doubling the stake with NEW capital; stop stays ₹463.60; funded ₹22.76 from the pocket + ₹0.00 fresh; charges ₹0.03)
2015-06-03  ABIRLANUVO  SELL ₹21.50 at stop ₹850.92 (-8.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹10.74 of doubled capital and its returns OUT to the pocket
2015-06-03  CIMMCO      SELL ₹23.70 at stop ₹85.29 (-19.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹11.84 of doubled capital and its returns OUT to the pocket
2015-06-08  MANGALAM    BUY ₹11.19 at ₹64.10 (fresh Friday signal — BUY: 8.22× weekly, month 7.28×, ladder rising; stop ₹34.31; charges ₹0.01)
2015-06-08  MANINDS     BUY ₹13.71 at ₹80.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.06× weekly, month 2.62×, ladder rising; stop ₹54.94; charges ₹0.02)
2015-06-22  MANINDS     PYRAMID BUY ₹12.56 at ₹73.35 (box jump — doubling the stake with NEW capital; stop stays ₹67.54; charges ₹0.01)
2015-06-22  MANINFRA    PYRAMID BUY ₹14.81 at ₹46.20 (box jump — doubling the stake with NEW capital; stop stays ₹41.18; funded ₹8.83 from the pocket + ₹5.99 fresh; charges ₹0.02)
2015-06-22  NILKAMAL    PYRAMID BUY ₹12.21 at ₹534.00 (box jump — doubling the stake with NEW capital; stop stays ₹479.89; charges ₹0.01)
2015-06-22  SMLISUZU    PYRAMID BUY ₹18.62 at ₹1,127.95 (box jump — doubling the stake with NEW capital; stop stays ₹997.50; funded ₹18.62 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-07-06  MANGALAM    PYRAMID BUY ₹9.53 at ₹54.65 (box jump — doubling the stake with NEW capital; stop stays ₹36.95; charges ₹0.01)
2015-07-06  MANINDS     PYRAMID BUY ₹30.08 at ₹87.90 (box jump — doubling the stake with NEW capital; stop stays ₹81.13; charges ₹0.04)
2015-07-06  SMLISUZU    PYRAMID BUY ₹36.46 at ₹1,105.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,053.55; charges ₹0.04)
2015-07-20  MANINFRA    PYRAMID BUY ₹29.51 at ₹46.05 (box jump — doubling the stake with NEW capital; stop stays ₹41.85; charges ₹0.03)
2015-07-20  NILKAMAL    PYRAMID BUY ₹33.16 at ₹725.50 (box jump — doubling the stake with NEW capital; stop stays ₹547.82; charges ₹0.04)
2015-07-20  VADILALIND  PYRAMID BUY ₹65.59 at ₹714.95 (box jump — doubling the stake with NEW capital; stop stays ₹637.45; charges ₹0.08)
2015-07-27  MANINFRA    SELL ₹53.56 at stop ₹41.85 (-9.9%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹40.15 of doubled capital and its returns OUT to the pocket
2015-08-03  MANINDS     PYRAMID BUY ₹77.99 at ₹114.00 (box jump — doubling the stake with NEW capital; stop stays ₹95.77; funded ₹40.15 from the pocket + ₹37.83 fresh; charges ₹0.09)
2015-08-10  NILKAMAL    PYRAMID BUY ₹106.52 at ₹1,165.95 (box jump — doubling the stake with NEW capital; stop stays ₹730.69; charges ₹0.13)
2015-08-13  VADILALIND  SELL ₹131.23 at stop ₹716.44 (+18.3%, charges ₹0.14) — the cash goes back to work at the next Friday screen; ₹114.80 of doubled capital and its returns OUT to the pocket
2015-08-17  GARWALLROP  BUY ₹29.84 at ₹309.90 (fresh Friday signal — ACCUMULATE: 6.87× weekly, month 5.41×, ladder rising; stop ₹274.60; charges ₹0.04)
2015-08-24  ECLERX      PYRAMID BUY ₹21.37 at ₹1,680.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,531.40; funded ₹21.37 from the pocket + ₹0.00 fresh; charges ₹0.03)
2015-08-24  MANINDS     SELL ₹130.82 at stop ₹95.77 (-2.4%, charges ₹0.14) — the cash goes back to work at the next Friday screen; ₹114.43 of doubled capital and its returns OUT to the pocket
2015-08-24  NILKAMAL    SELL ₹169.13 at stop ₹927.12 (+3.4%, charges ₹0.18) — the cash goes back to work at the next Friday screen; ₹147.95 of doubled capital and its returns OUT to the pocket
2015-08-24  SMLISUZU    SELL ₹73.13 at stop ₹1,110.20 (-2.5%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹63.97 of doubled capital and its returns OUT to the pocket
2015-08-25  GARWALLROP  SELL ₹26.38 at stop ₹274.60 (-11.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2015-08-31  ICIL        BUY ₹14.47 at ₹199.78 (fresh Friday signal — ACCUMULATE: 1.94× weekly, month 2.05×, ladder rising; stop ₹145.90; charges ₹0.02)
2015-08-31  JUBLINDS    BUY ₹14.47 at ₹302.00 (fresh Friday signal — BUY: 3.23× weekly, month 8.31×, ladder rising; stop ₹200.99; charges ₹0.02)
2015-09-07  ABBOTINDIA  BUY ₹16.53 at ₹5,269.00 (fresh Friday signal — BUY: 5.86× weekly, month 1.67×, ladder rising; stop ₹4,181.09; charges ₹0.02)
2015-09-07  CAPLIPOINT  BUY ₹16.55 at ₹300.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.25×, ladder rising; stop ₹207.81; charges ₹0.02)
2015-09-07  JINDALPOLY  BUY ₹11.07 at ₹376.90 (fresh Friday signal — ACCUMULATE: 1.73× weekly, month 2.65×, ladder rising; stop ₹305.60; charges ₹0.01)
2015-09-07  MANGALAM    PYRAMID BUY ₹27.88 at ₹80.00 (box jump — doubling the stake with NEW capital; stop stays ₹73.50; funded ₹27.88 from the pocket + ₹0.00 fresh; charges ₹0.03)
2015-09-08  ICIL        SELL ₹10.54 at stop ₹145.90 (-27.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2015-09-08  MANGALAM    SELL ₹51.14 at stop ₹73.50 (+5.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹38.34 of doubled capital and its returns OUT to the pocket
2015-09-14  CAPLIPOINT  PYRAMID BUY ₹16.97 at ₹308.00 (box jump — doubling the stake with NEW capital; stop stays ₹262.64; funded ₹16.97 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-09-14  JUBLINDS    PYRAMID BUY ₹14.12 at ₹295.00 (box jump — doubling the stake with NEW capital; stop stays ₹224.21; funded ₹14.12 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-09-14  NEULANDLAB  BUY ₹16.05 at ₹702.80 (fresh Friday signal — BUY: 3.47× weekly, month 2.09×, ladder rising; stop ₹429.56; charges ₹0.02)
2015-09-28  ABBOTINDIA  PYRAMID BUY ₹18.24 at ₹5,819.95 (box jump — doubling the stake with NEW capital; stop stays ₹5,365.17; funded ₹18.24 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-09-28  NEULANDLAB  PYRAMID BUY ₹17.65 at ₹774.00 (box jump — doubling the stake with NEW capital; stop stays ₹668.18; funded ₹17.65 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-10-05  NEULANDLAB  PYRAMID BUY ₹40.16 at ₹881.00 (box jump — doubling the stake with NEW capital; stop stays ₹674.55; funded ₹40.16 from the pocket + ₹0.00 fresh; charges ₹0.05)
2015-10-12  JINDALPOLY  PYRAMID BUY ₹14.09 at ₹480.15 (box jump — doubling the stake with NEW capital; stop stays ₹402.90; funded ₹14.09 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-10-19  ECLERX      PYRAMID BUY ₹46.21 at ₹1,817.45 (box jump — doubling the stake with NEW capital; stop stays ₹1,548.50; funded ₹46.21 from the pocket + ₹0.00 fresh; charges ₹0.05)
2015-10-26  JINDALPOLY  PYRAMID BUY ₹31.79 at ₹541.90 (box jump — doubling the stake with NEW capital; stop stays ₹451.25; funded ₹31.79 from the pocket + ₹0.00 fresh; charges ₹0.04)
2015-10-26  NEULANDLAB  PYRAMID BUY ₹73.62 at ₹808.00 (box jump — doubling the stake with NEW capital; stop stays ₹714.39; funded ₹73.62 from the pocket + ₹0.00 fresh; charges ₹0.09)
2015-10-28  CAPLIPOINT  SELL ₹28.90 at stop ₹262.64 (-13.6%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹14.44 of doubled capital and its returns OUT to the pocket
2015-10-29  NEULANDLAB  SELL ₹129.97 at stop ₹714.39 (-11.7%, charges ₹0.13) — the cash goes back to work at the next Friday screen; ₹113.69 of doubled capital and its returns OUT to the pocket
2015-11-02  JINDALPOLY  PYRAMID BUY ₹64.73 at ₹552.05 (box jump — doubling the stake with NEW capital; stop stays ₹494.38; funded ₹64.73 from the pocket + ₹0.00 fresh; charges ₹0.08)
2015-11-02  JUBLINDS    SELL ₹21.42 at stop ₹224.21 (-24.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹10.71 of doubled capital and its returns OUT to the pocket
2015-11-02  UCOBANK     BUY ₹31.39 at ₹50.30 (fresh Friday signal — BUY: 4.92× weekly, month 2.00×, ladder rising; stop ₹45.79; charges ₹0.04)
2015-11-06  ABBOTINDIA  SELL ₹33.57 at stop ₹5,365.17 (-3.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹16.77 of doubled capital and its returns OUT to the pocket
2015-11-09  INTELLECT   BUY ₹27.58 at ₹242.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.50× weekly, month 1.86×, ladder rising; stop ₹197.60; charges ₹0.03)
2015-11-09  UCOBANK     SELL ₹28.51 at stop ₹45.79 (-9.0%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2015-11-16  INTELLECT   PYRAMID BUY ₹29.24 at ₹256.90 (box jump — doubling the stake with NEW capital; stop stays ₹224.56; funded ₹29.24 from the pocket + ₹0.00 fresh; charges ₹0.03)
2015-11-16  TRIGYN      BUY ₹31.05 at ₹78.80 (fresh Friday signal — starved 1×, front of the queue — BUY: 7.34× weekly, month 10.13×, ladder rising; stop ₹48.40; charges ₹0.04)
2015-11-26  JINDALPOLY  SELL ₹115.74 at stop ₹494.38 (-4.7%, charges ₹0.12) — the cash goes back to work at the next Friday screen; ₹101.25 of doubled capital and its returns OUT to the pocket
2015-11-30  TRIGYN      PYRAMID BUY ₹36.06 at ₹91.65 (box jump — doubling the stake with NEW capital; stop stays ₹68.97; funded ₹36.06 from the pocket + ₹0.00 fresh; charges ₹0.04)
2015-11-30  TRIVENI     BUY ₹18.54 at ₹39.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.71× weekly, month 18.79×, ladder rising; stop ₹21.99; charges ₹0.02)
2015-12-07  INTELLECT   PYRAMID BUY ₹63.56 at ₹279.35 (box jump — doubling the stake with NEW capital; stop stays ₹252.22; funded ₹63.56 from the pocket + ₹0.00 fresh; charges ₹0.08)
2015-12-07  TRIGYN      PYRAMID BUY ₹71.58 at ₹91.00 (box jump — doubling the stake with NEW capital; stop stays ₹82.94; funded ₹71.58 from the pocket + ₹0.00 fresh; charges ₹0.08)
2015-12-09  INTELLECT   SELL ₹114.59 at stop ₹252.22 (-4.6%, charges ₹0.12) — the cash goes back to work at the next Friday screen; ₹85.91 of doubled capital and its returns OUT to the pocket
2015-12-10  TRIGYN      SELL ₹130.26 at stop ₹82.94 (-5.9%, charges ₹0.14) — the cash goes back to work at the next Friday screen; ₹97.66 of doubled capital and its returns OUT to the pocket
2015-12-14  AJMERA      BUY ₹17.03 at ₹124.80 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.63× weekly, month 2.71×, ladder rising; stop ₹86.59; charges ₹0.02)
2015-12-14  EDL         BUY ₹9.98 at ₹98.25 (fresh Friday signal — BUY: 9.13× weekly, month 22.01×, ladder rising; stop ₹68.12; charges ₹0.01)
2015-12-14  NCLIND      BUY ₹17.11 at ₹166.75 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.05× weekly, month 2.94×, ladder rising; stop ₹148.29; charges ₹0.02)
2015-12-14  SHARONBIO   BUY ₹17.17 at ₹30.80 (fresh Friday signal — BUY: 12.91× weekly, month 1.78×, ladder rising; stop ₹11.82; charges ₹0.02)
2015-12-17  ECLERX      SELL ₹82.23 at stop ₹1,619.75 (-5.7%, charges ₹0.09) — the cash goes back to work at the next Friday screen; ₹71.93 of doubled capital and its returns OUT to the pocket
2015-12-21  AJMERA      PYRAMID BUY ₹18.59 at ₹136.44 (box jump — doubling the stake with NEW capital; stop stays ₹103.22; funded ₹18.59 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-12-21  EDL         PYRAMID BUY ₹10.93 at ₹107.70 (box jump — doubling the stake with NEW capital; stop stays ₹87.83; funded ₹10.93 from the pocket + ₹0.00 fresh; charges ₹0.01)
2015-12-21  NCLIND      PYRAMID BUY ₹17.91 at ₹174.70 (box jump — doubling the stake with NEW capital; stop stays ₹151.19; funded ₹17.91 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-12-21  SHARONBIO   PYRAMID BUY ₹16.70 at ₹30.00 (box jump — doubling the stake with NEW capital; stop stays ₹26.93; funded ₹16.70 from the pocket + ₹0.00 fresh; charges ₹0.02)
2015-12-21  TWL         BUY ₹10.30 at ₹159.45 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.40× weekly, month 3.18×, ladder rising; stop ₹140.17; charges ₹0.01)
2016-01-04  TRIVENI     PYRAMID BUY ₹22.07 at ₹46.50 (box jump — doubling the stake with NEW capital; stop stays ₹37.15; funded ₹22.07 from the pocket + ₹0.00 fresh; charges ₹0.03)
2016-01-04  TWL         PYRAMID BUY ₹10.51 at ₹162.90 (box jump — doubling the stake with NEW capital; stop stays ₹151.43; funded ₹10.51 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-01-07  NCLIND      SELL ₹30.94 at stop ₹151.19 (-11.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹15.46 of doubled capital and its returns OUT to the pocket
2016-01-07  TWL         SELL ₹19.50 at stop ₹151.43 (-6.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹9.75 of doubled capital and its returns OUT to the pocket
2016-01-11  BBL         BUY ₹16.41 at ₹874.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.78× weekly, month 4.75×, ladder rising; stop ₹631.79; charges ₹0.02)
2016-01-11  NILKAMAL    BUY ₹8.83 at ₹1,423.80 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.23× weekly, month 2.08×, ladder rising; stop ₹1,174.87; charges ₹0.01)
2016-01-12  SHARONBIO   SELL ₹29.93 at stop ₹26.93 (-11.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹14.96 of doubled capital and its returns OUT to the pocket
2016-01-13  EDL         SELL ₹17.79 at stop ₹87.83 (-14.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.89 of doubled capital and its returns OUT to the pocket
2016-01-18  NILKAMAL    SELL ₹7.27 at stop ₹1,174.87 (-17.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2016-01-18  TRIVENI     PYRAMID BUY ₹45.78 at ₹48.25 (box jump — doubling the stake with NEW capital; stop stays ₹41.33; funded ₹45.78 from the pocket + ₹0.00 fresh; charges ₹0.05)
2016-01-22  AJMERA      SELL ₹28.09 at stop ₹103.22 (-21.0%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹14.04 of doubled capital and its returns OUT to the pocket
2016-01-25  SOMANYCERA  BUY ₹15.26 at ₹377.00 (fresh Friday signal — ACCUMULATE: 1.72× weekly, month 2.16×, ladder rising; stop ₹317.01; charges ₹0.02)
2016-02-01  PRICOL      BUY ₹15.28 at ₹47.90 (fresh Friday signal — BUY: 2.18× weekly, month 2.31×, ladder rising; stop ₹35.02; charges ₹0.02)
2016-02-04  TRIVENI     SELL ₹78.31 at stop ₹41.33 (-9.2%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹58.71 of doubled capital and its returns OUT to the pocket
2016-02-15  GOLDBEES    BUY ₹7.94 at ₹2,614.80 (fresh Friday signal — BUY: 3.06× weekly, month 1.75×, ladder rising; stop ₹2,285.70; charges ₹0.01)
2016-02-22  GOLDBEES    PYRAMID BUY ₹7.93 at ₹2,612.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,424.21; funded ₹7.93 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-02-22  PRICOL      PYRAMID BUY ₹16.71 at ₹52.45 (box jump — doubling the stake with NEW capital; stop stays ₹41.77; funded ₹16.71 from the pocket + ₹0.00 fresh; charges ₹0.02)
2016-02-29  PRICOL      SELL ₹26.57 at stop ₹41.77 (-16.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹13.28 of doubled capital and its returns OUT to the pocket
2016-03-08  ENERGYDEV   BUY ₹8.55 at ₹56.00 (fresh Friday signal — BUY: 1.56× weekly, month 3.05×, ladder rising; stop ₹34.68; charges ₹0.01)
2016-03-08  RAMKY       BUY ₹8.47 at ₹55.25 (fresh Friday signal — BUY: 1.57× weekly, month 3.26×, ladder rising; stop ₹38.53; charges ₹0.01)
2016-03-14  DALMIASUG   BUY ₹10.36 at ₹94.05 (fresh Friday signal — BUY: 4.21× weekly, month 2.75×, ladder rising; stop ₹49.84; charges ₹0.01)
2016-03-14  GOLDBEES    PYRAMID BUY ₹16.13 at ₹2,659.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,476.18; funded ₹16.13 from the pocket + ₹0.00 fresh; charges ₹0.02)
2016-03-14  HDFCMFGETF  BUY ₹10.40 at ₹2,734.00 (fresh Friday signal — ACCUMULATE: 1.54× weekly, month 1.73×, ladder rising; stop ₹2,484.30; charges ₹0.01)
2016-03-21  SOMANYCERA  PYRAMID BUY ₹15.20 at ₹375.95 (box jump — doubling the stake with NEW capital; stop stays ₹337.25; funded ₹15.20 from the pocket + ₹0.00 fresh; charges ₹0.02)
2016-03-28  DALMIASUG   PYRAMID BUY ₹11.45 at ₹104.00 (box jump — doubling the stake with NEW capital; stop stays ₹86.86; funded ₹11.45 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-03-28  ENERGYDEV   PYRAMID BUY ₹10.33 at ₹67.70 (box jump — doubling the stake with NEW capital; stop stays ₹48.84; funded ₹10.33 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-04-01  TAX         FY2016 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹19.58 / LT ₹0.00)
2016-04-04  BBL         PYRAMID BUY ₹17.46 at ₹930.90 (box jump — doubling the stake with NEW capital; stop stays ₹803.37; funded ₹17.46 from the pocket + ₹0.00 fresh; charges ₹0.02)
2016-04-04  ENERGYDEV   PYRAMID BUY ₹20.74 at ₹68.00 (box jump — doubling the stake with NEW capital; stop stays ₹60.80; funded ₹20.74 from the pocket + ₹0.00 fresh; charges ₹0.02)
2016-04-11  SOMANYCERA  PYRAMID BUY ₹31.69 at ₹392.00 (box jump — doubling the stake with NEW capital; stop stays ₹351.50; funded ₹31.69 from the pocket + ₹0.00 fresh; charges ₹0.04)
2016-04-12  ENERGYDEV   SELL ₹37.02 at stop ₹60.80 (-6.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹27.76 of doubled capital and its returns OUT to the pocket
2016-04-18  RSSOFTWARE  BUY ₹11.08 at ₹117.40 (fresh Friday signal — BUY: 10.97× weekly, month 3.36×, ladder rising; stop ₹68.78; charges ₹0.01)
2016-05-02  BBL         PYRAMID BUY ₹39.84 at ₹1,062.95 (box jump — doubling the stake with NEW capital; stop stays ₹878.75; funded ₹39.84 from the pocket + ₹0.00 fresh; charges ₹0.05)
2016-05-02  GOLDBEES    PYRAMID BUY ₹33.05 at ₹2,726.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,508.05; funded ₹33.05 from the pocket + ₹0.00 fresh; charges ₹0.04)
2016-05-02  RSSOFTWARE  PYRAMID BUY ₹9.90 at ₹105.00 (box jump — doubling the stake with NEW capital; stop stays ₹93.44; funded ₹9.90 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-05-09  RAMKY       PYRAMID BUY ₹8.29 at ₹54.15 (box jump — doubling the stake with NEW capital; stop stays ₹49.76; funded ₹8.29 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-05-09  SOMANYCERA  PYRAMID BUY ₹67.45 at ₹417.50 (box jump — doubling the stake with NEW capital; stop stays ₹382.85; funded ₹67.45 from the pocket + ₹0.00 fresh; charges ₹0.08)
2016-05-16  HDFCMFGETF  PYRAMID BUY ₹10.66 at ₹2,805.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,629.60; funded ₹10.66 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-05-18  RSSOFTWARE  SELL ₹17.59 at stop ₹93.44 (-16.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.79 of doubled capital and its returns OUT to the pocket
2016-05-20  BBL         SELL ₹65.77 at stop ₹878.75 (-10.6%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹49.31 of doubled capital and its returns OUT to the pocket
2016-05-23  TPLPLASTEH  BUY ₹25.26 at ₹513.50 (fresh Friday signal — BUY: 16.66× weekly, month 19.21×, ladder rising; stop ₹343.95; charges ₹0.03)
2016-05-24  DALMIASUG   SELL ₹19.09 at stop ₹86.86 (-12.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹9.54 of doubled capital and its returns OUT to the pocket
2016-05-30  TPLPLASTEH  PYRAMID BUY ₹23.34 at ₹475.00 (box jump — doubling the stake with NEW capital; stop stays ₹352.26; funded ₹23.34 from the pocket + ₹0.00 fresh; charges ₹0.03)
2016-06-13  RAMKY       PYRAMID BUY ₹22.10 at ₹72.20 (box jump — doubling the stake with NEW capital; stop stays ₹59.65; funded ₹22.10 from the pocket + ₹0.00 fresh; charges ₹0.03)
2016-07-04  HDFCMFGETF  PYRAMID BUY ₹21.85 at ₹2,878.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,691.35; funded ₹21.85 from the pocket + ₹0.00 fresh; charges ₹0.03)
2016-07-04  TPLPLASTEH  PYRAMID BUY ₹47.15 at ₹480.00 (box jump — doubling the stake with NEW capital; stop stays ₹382.18; funded ₹47.15 from the pocket + ₹0.00 fresh; charges ₹0.06)
2016-07-18  TPLPLASTEH  PYRAMID BUY ₹97.65 at ₹497.35 (box jump — doubling the stake with NEW capital; stop stays ₹465.74; funded ₹61.31 from the pocket + ₹36.34 fresh; charges ₹0.12)
2016-07-22  TPLPLASTEH  SELL ₹182.59 at stop ₹465.74 (-5.4%, charges ₹0.19) — the cash goes back to work at the next Friday screen; ₹159.72 of doubled capital and its returns OUT to the pocket
2016-07-25  RAMKY       PYRAMID BUY ₹57.18 at ₹93.45 (box jump — doubling the stake with NEW capital; stop stays ₹79.04; funded ₹57.18 from the pocket + ₹0.00 fresh; charges ₹0.07)
2016-07-25  TATAMETALI  BUY ₹32.41 at ₹453.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 7.99× weekly, month 6.02×, ladder rising; stop ₹304.18; charges ₹0.04)
2016-08-01  HDFCMFGETF  PYRAMID BUY ₹44.14 at ₹2,908.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,694.68; funded ₹44.14 from the pocket + ₹0.00 fresh; charges ₹0.05)
2016-08-08  TATAMETALI  PYRAMID BUY ₹31.38 at ₹439.10 (box jump — doubling the stake with NEW capital; stop stays ₹366.19; funded ₹31.38 from the pocket + ₹0.00 fresh; charges ₹0.04)
2016-08-10  RAMKY       SELL ₹96.57 at stop ₹79.04 (+0.8%, charges ₹0.10) — the cash goes back to work at the next Friday screen; ₹84.48 of doubled capital and its returns OUT to the pocket
2016-09-21  SOMANYCERA  SELL ₹177.79 at stop ₹551.10 (+37.5%, charges ₹0.18) — the cash goes back to work at the next Friday screen; ₹155.53 of doubled capital and its returns OUT to the pocket
2016-09-26  HERITGFOOD  BUY ₹25.28 at ₹453.85 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.51× weekly, month 2.75×, ladder rising; stop ₹346.27; charges ₹0.03)
2016-09-29  TATAMETALI  SELL ₹52.26 at stop ₹366.19 (-17.9%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹26.11 of doubled capital and its returns OUT to the pocket
2016-10-03  CENTURYTEX  BUY ₹13.52 at ₹952.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.78× weekly, month 2.24×, ladder rising; stop ₹628.90; charges ₹0.02)
2016-10-03  GLOBUSSPR   BUY ₹21.70 at ₹108.10 (fresh Friday signal — starved 2×, front of the queue — BUY: 11.16× weekly, month 4.83×, ladder rising; stop ₹71.55; charges ₹0.03)
2016-10-10  GLOBUSSPR   PYRAMID BUY ₹21.27 at ₹106.10 (box jump — doubling the stake with NEW capital; stop stays ₹95.00; funded ₹21.27 from the pocket + ₹0.00 fresh; charges ₹0.03)
2016-10-17  HERITGFOOD  PYRAMID BUY ₹25.03 at ₹449.85 (box jump — doubling the stake with NEW capital; stop stays ₹398.05; funded ₹25.03 from the pocket + ₹0.00 fresh; charges ₹0.03)
2016-10-24  CENTURYTEX  PYRAMID BUY ₹13.15 at ₹927.00 (box jump — doubling the stake with NEW capital; stop stays ₹863.60; funded ₹13.15 from the pocket + ₹0.00 fresh; charges ₹0.02)
2016-11-04  GLOBUSSPR   SELL ₹38.03 at stop ₹95.00 (-11.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹19.01 of doubled capital and its returns OUT to the pocket
2016-11-04  HERITGFOOD  SELL ₹44.22 at stop ₹398.05 (-11.9%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹22.10 of doubled capital and its returns OUT to the pocket
2016-11-07  SESHAPAPER  BUY ₹18.90 at ₹164.20 (fresh Friday signal — BUY: 2.47× weekly, month 6.45×, ladder rising; stop ₹113.48; charges ₹0.02)
2016-11-07  SHREEPUSHK  BUY ₹22.25 at ₹182.10 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 4.98×, ladder rising; stop ₹143.41; charges ₹0.03)
2016-11-09  CENTURYTEX  SELL ₹24.46 at stop ₹863.60 (-8.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹12.22 of doubled capital and its returns OUT to the pocket
2016-11-15  STARPAPER   BUY ₹12.24 at ₹187.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.23× weekly, month 4.09×, ladder rising; stop ₹113.76; charges ₹0.01)
2016-11-17  GOLDBEES    SELL ₹65.11 at stop ₹2,689.64 (+0.3%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹56.95 of doubled capital and its returns OUT to the pocket
2016-11-18  HDFCMFGETF  SELL ₹82.40 at stop ₹2,718.90 (-5.1%, charges ₹0.09) — the cash goes back to work at the next Friday screen; ₹72.08 of doubled capital and its returns OUT to the pocket
2016-11-21  BALMLAWRIE  BUY ₹6.05 at ₹849.00 (fresh Friday signal — ACCUMULATE: 1.75× weekly, month 2.76×, ladder rising; stop ₹768.17; charges ₹0.01)
2016-11-22  SESHAPAPER  SELL ₹13.03 at stop ₹113.48 (-30.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2016-11-28  STARPAPER   PYRAMID BUY ₹11.90 at ₹182.00 (box jump — doubling the stake with NEW capital; stop stays ₹119.08; funded ₹11.90 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-12-05  ESSELPACK   BUY ₹7.85 at ₹126.50 (fresh Friday signal — BUY: 4.47× weekly, month 2.09×, ladder rising; stop ₹104.50; charges ₹0.01)
2016-12-05  MERCK       BUY ₹7.82 at ₹962.00 (fresh Friday signal — BUY: 2.25× weekly, month 3.58×, ladder rising; stop ₹816.81; charges ₹0.01)
2016-12-05  UJAAS       BUY ₹7.85 at ₹46.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.01× weekly, month 3.61×, ladder rising; stop ₹32.04; charges ₹0.01)
2016-12-12  ESSELPACK   PYRAMID BUY ₹7.82 at ₹126.12 (box jump — doubling the stake with NEW capital; stop stays ₹114.95; funded ₹7.82 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-12-12  MERCK       PYRAMID BUY ₹8.05 at ₹991.00 (box jump — doubling the stake with NEW capital; stop stays ₹902.78; funded ₹8.05 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-12-12  SHREEPUSHK  PYRAMID BUY ₹21.12 at ₹173.00 (box jump — doubling the stake with NEW capital; stop stays ₹151.34; funded ₹21.12 from the pocket + ₹0.00 fresh; charges ₹0.03)
2016-12-12  STARPAPER   PYRAMID BUY ₹24.66 at ₹188.75 (box jump — doubling the stake with NEW capital; stop stays ₹175.94; funded ₹24.66 from the pocket + ₹0.00 fresh; charges ₹0.03)
2016-12-13  STARPAPER   SELL ₹45.90 at stop ₹175.94 (-5.7%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹34.41 of doubled capital and its returns OUT to the pocket
2016-12-19  SWANENERGY  BUY ₹11.03 at ₹202.30 (fresh Friday signal — BUY: 6.50× weekly, month 6.89×, ladder rising; stop ₹155.80; charges ₹0.01)
2016-12-19  UJAAS       PYRAMID BUY ₹8.75 at ₹51.30 (box jump — doubling the stake with NEW capital; stop stays ₹40.27; funded ₹8.75 from the pocket + ₹0.00 fresh; charges ₹0.01)
2016-12-22  SWANENERGY  SELL ₹8.48 at stop ₹155.80 (-23.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2016-12-26  BALMLAWRIE  PYRAMID BUY ₹1.74 at ₹245.00 (box jump — doubling the stake with NEW capital; stop stays ₹997.98; funded ₹1.74 from the pocket + ₹0.00 fresh; charges ₹0.00)
2016-12-26  BALMLAWRIE  SELL ₹14.18 at stop ₹997.98 (+82.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹7.08 of doubled capital and its returns OUT to the pocket
2016-12-26  STCINDIA    BUY ₹9.91 at ₹152.20 (fresh Friday signal — BUY: 3.37× weekly, month 1.67×, ladder rising; stop ₹109.25; charges ₹0.01)
2017-01-09  INDIAGLYCO  BUY ₹8.04 at ₹148.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.72× weekly, month 2.32×, ladder rising; stop ₹97.73; charges ₹0.01)
2017-01-16  STCINDIA    PYRAMID BUY ₹14.50 at ₹223.00 (box jump — doubling the stake with NEW capital; stop stays ₹187.15; funded ₹14.50 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-01-23  SHREEPUSHK  PYRAMID BUY ₹47.82 at ₹196.00 (box jump — doubling the stake with NEW capital; stop stays ₹172.04; funded ₹47.82 from the pocket + ₹0.00 fresh; charges ₹0.06)
2017-01-30  ESSELPACK   PYRAMID BUY ₹15.67 at ₹126.50 (box jump — doubling the stake with NEW capital; stop stays ₹115.95; funded ₹15.67 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-01-30  INDIAGLYCO  PYRAMID BUY ₹8.70 at ₹160.35 (box jump — doubling the stake with NEW capital; stop stays ₹150.48; funded ₹8.70 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-01-30  STCINDIA    SELL ₹24.30 at stop ₹187.15 (-0.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹12.14 of doubled capital and its returns OUT to the pocket
2017-02-06  VIJAYABANK  BUY ₹12.16 at ₹68.25 (fresh Friday signal — starved 1×, front of the queue — BUY: 8.31× weekly, month 2.91×, ladder rising; stop ₹39.32; charges ₹0.01)
2017-02-13  MERCK       PYRAMID BUY ₹16.09 at ₹991.00 (box jump — doubling the stake with NEW capital; stop stays ₹919.79; funded ₹16.09 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-02-13  SHREEPUSHK  PYRAMID BUY ₹94.11 at ₹193.00 (box jump — doubling the stake with NEW capital; stop stays ₹176.18; funded ₹94.11 from the pocket + ₹0.00 fresh; charges ₹0.11)
2017-02-15  SHREEPUSHK  SELL ₹171.55 at stop ₹176.18 (-7.2%, charges ₹0.18) — the cash goes back to work at the next Friday screen; ₹150.06 of doubled capital and its returns OUT to the pocket
2017-02-20  GRASIM      BUY ₹14.12 at ₹1,044.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.77× weekly, month 2.99×, ladder rising; stop ₹861.41; charges ₹0.02)
2017-02-20  NFL         BUY ₹7.37 at ₹70.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.69× weekly, month 7.77×, ladder rising; stop ₹41.42; charges ₹0.01)
2017-02-20  VIJAYABANK  PYRAMID BUY ₹11.55 at ₹64.90 (box jump — doubling the stake with NEW capital; stop stays ₹56.94; funded ₹11.55 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-02-21  ESSELPACK   SELL ₹28.68 at stop ₹115.95 (-8.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹21.50 of doubled capital and its returns OUT to the pocket
2017-02-21  UJAAS       SELL ₹13.71 at stop ₹40.27 (-17.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹6.85 of doubled capital and its returns OUT to the pocket
2017-02-27  NFL         PYRAMID BUY ₹7.39 at ₹70.30 (box jump — doubling the stake with NEW capital; stop stays ₹60.33; funded ₹7.39 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-02-27  RAIN        BUY ₹12.21 at ₹88.50 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.20× weekly, month 3.50×, ladder rising; stop ₹72.39; charges ₹0.01)
2017-03-14  GRASIM      PYRAMID BUY ₹13.72 at ₹1,016.00 (box jump — doubling the stake with NEW capital; stop stays ₹927.01; funded ₹13.72 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-03-14  MERCK       PYRAMID BUY ₹32.59 at ₹1,004.00 (box jump — doubling the stake with NEW capital; stop stays ₹941.26; funded ₹32.59 from the pocket + ₹0.00 fresh; charges ₹0.04)
2017-03-14  NFL         PYRAMID BUY ₹15.50 at ₹73.80 (box jump — doubling the stake with NEW capital; stop stays ₹65.12; funded ₹15.50 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-03-20  INDIAGLYCO  SELL ₹16.31 at stop ₹150.48 (-2.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.15 of doubled capital and its returns OUT to the pocket
2017-03-20  RAIN        PYRAMID BUY ₹14.05 at ₹101.95 (box jump — doubling the stake with NEW capital; stop stays ₹93.77; funded ₹14.05 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-03-20  VIJAYABANK  PYRAMID BUY ₹22.83 at ₹64.20 (box jump — doubling the stake with NEW capital; stop stays ₹59.24; funded ₹22.83 from the pocket + ₹0.00 fresh; charges ₹0.03)
2017-04-03  TAX         FY2017 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹34.47 / LT ₹0.00)
2017-04-03  VIJAYABANK  PYRAMID BUY ₹48.88 at ₹68.75 (box jump — doubling the stake with NEW capital; stop stays ₹61.08; funded ₹48.88 from the pocket + ₹0.00 fresh; charges ₹0.06)
2017-04-17  RAIN        PYRAMID BUY ₹29.45 at ₹106.90 (box jump — doubling the stake with NEW capital; stop stays ₹96.95; funded ₹29.45 from the pocket + ₹0.00 fresh; charges ₹0.03)
2017-04-24  GRASIM      PYRAMID BUY ₹30.43 at ₹1,127.25 (box jump — doubling the stake with NEW capital; stop stays ₹995.60; funded ₹30.43 from the pocket + ₹0.00 fresh; charges ₹0.04)
2017-05-08  GRASIM      PYRAMID BUY ₹64.51 at ₹1,195.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,082.91; funded ₹64.51 from the pocket + ₹0.00 fresh; charges ₹0.08)
2017-05-08  NFL         PYRAMID BUY ₹35.42 at ₹84.35 (box jump — doubling the stake with NEW capital; stop stays ₹73.15; funded ₹35.42 from the pocket + ₹0.00 fresh; charges ₹0.04)
2017-05-19  MERCK       SELL ₹67.72 at stop ₹1,045.00 (+5.1%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹59.24 of doubled capital and its returns OUT to the pocket
2017-05-23  RAIN        SELL ₹53.33 at stop ₹96.95 (-4.1%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹39.98 of doubled capital and its returns OUT to the pocket
2017-05-23  VIJAYABANK  SELL ₹111.14 at stop ₹78.29 (+16.7%, charges ₹0.12) — the cash goes back to work at the next Friday screen; ₹97.22 of doubled capital and its returns OUT to the pocket
2017-05-29  HOVS        BUY ₹23.34 at ₹324.70 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.64× weekly, month 2.39×, ladder rising; stop ₹189.53; charges ₹0.03)
2017-05-29  SHAKTIPUMP  BUY ₹22.39 at ₹402.00 (fresh Friday signal — BUY: 12.55× weekly, month 12.33×, ladder rising; stop ₹248.90; charges ₹0.03)
2017-06-12  SHAKTIPUMP  PYRAMID BUY ₹24.58 at ₹441.80 (box jump — doubling the stake with NEW capital; stop stays ₹357.49; funded ₹24.58 from the pocket + ₹0.00 fresh; charges ₹0.03)
2017-06-19  SHAKTIPUMP  PYRAMID BUY ₹49.45 at ₹444.75 (box jump — doubling the stake with NEW capital; stop stays ₹415.62; funded ₹49.45 from the pocket + ₹0.00 fresh; charges ₹0.06)
2017-06-23  NFL         SELL ₹62.37 at stop ₹74.38 (-4.8%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹54.56 of doubled capital and its returns OUT to the pocket
2017-06-28  SHAKTIPUMP  SELL ₹92.27 at stop ₹415.62 (-4.1%, charges ₹0.10) — the cash goes back to work at the next Friday screen; ₹69.18 of doubled capital and its returns OUT to the pocket
2017-07-03  GVKPIL      BUY ₹11.78 at ₹8.90 (fresh Friday signal — BUY: 4.75× weekly, month 2.80×, ladder rising; stop ₹5.83; charges ₹0.01)
2017-07-03  MEP         BUY ₹19.13 at ₹115.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.16× weekly, month 8.67×, ladder rising; stop ₹82.47; charges ₹0.02)
2017-07-10  GVKPIL      PYRAMID BUY ₹10.84 at ₹8.20 (box jump — doubling the stake with NEW capital; stop stays ₹7.32; funded ₹10.84 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-07-10  MEP         PYRAMID BUY ₹24.92 at ₹150.00 (box jump — doubling the stake with NEW capital; stop stays ₹102.98; funded ₹24.92 from the pocket + ₹0.00 fresh; charges ₹0.03)
2017-07-13  GVKPIL      SELL ₹19.32 at stop ₹7.32 (-14.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹9.65 of doubled capital and its returns OUT to the pocket
2017-07-19  GRASIM      SELL ₹127.17 at stop ₹1,180.47 (+3.8%, charges ₹0.13) — the cash goes back to work at the next Friday screen; ₹111.25 of doubled capital and its returns OUT to the pocket
2017-07-24  BALAJITELE  BUY ₹13.33 at ₹188.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 7.42× weekly, month 6.58×, ladder rising; stop ₹149.25; charges ₹0.02)
2017-07-24  MEP         PYRAMID BUY ₹42.24 at ₹127.20 (box jump — doubling the stake with NEW capital; stop stays ₹115.55; funded ₹42.24 from the pocket + ₹0.00 fresh; charges ₹0.05)
2017-07-24  SREINFRA    BUY ₹12.26 at ₹136.75 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.06× weekly, month 1.74×, ladder rising; stop ₹105.69; charges ₹0.01)
2017-07-27  MEP         SELL ₹76.62 at stop ₹115.55 (-11.0%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹57.44 of doubled capital and its returns OUT to the pocket
2017-07-31  BEML        BUY ₹6.40 at ₹1,673.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.01× weekly, month 1.59×, ladder rising; stop ₹1,438.35; charges ₹0.01)
2017-07-31  JPINFRATEC  BUY ₹6.39 at ₹22.40 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.85× weekly, month 4.10×, ladder rising; stop ₹17.20; charges ₹0.01)
2017-07-31  TUBEINVEST  BUY ₹6.39 at ₹756.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 3.66× weekly, month 2.21×, ladder rising; stop ₹680.20; charges ₹0.01)
2017-08-07  SREINFRA    PYRAMID BUY ₹10.76 at ₹120.15 (box jump — doubling the stake with NEW capital; stop stays ₹108.49; funded ₹10.76 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-08-10  BALAJITELE  SELL ₹10.56 at stop ₹149.25 (-20.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2017-08-10  BEML        SELL ₹5.49 at stop ₹1,438.35 (-14.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2017-08-10  SREINFRA    SELL ₹19.40 at stop ₹108.49 (-15.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹9.69 of doubled capital and its returns OUT to the pocket
2017-08-14  FRETAIL     BUY ₹5.98 at ₹452.95 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 2.34×, ladder rising; stop ₹377.15; charges ₹0.01)
2017-08-14  INSECTICID  BUY ₹5.97 at ₹771.85 (fresh Friday signal — BUY: 3.90× weekly, month 2.53×, ladder rising; stop ₹669.32; charges ₹0.01)
2017-08-14  JPINFRATEC  SELL ₹4.89 at stop ₹17.20 (-23.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2017-08-14  UTTAMSUGAR  BUY ₹5.93 at ₹188.00 (fresh Friday signal — BUY: 5.58× weekly, month 1.92×, ladder rising; stop ₹147.25; charges ₹0.01)
2017-08-21  AVANTIFEED  BUY ₹5.68 at ₹1,928.50 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.51× weekly, month 2.88×, ladder rising; stop ₹1,292.50; charges ₹0.01)
2017-08-21  INSECTICID  PYRAMID BUY ₹6.04 at ₹782.00 (box jump — doubling the stake with NEW capital; stop stays ₹682.10; funded ₹6.04 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-08-21  SPARC       BUY ₹7.09 at ₹397.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.36× weekly, month 2.85×, ladder rising; stop ₹307.62; charges ₹0.01)
2017-08-21  UTTAMSUGAR  PYRAMID BUY ₹5.95 at ₹188.70 (box jump — doubling the stake with NEW capital; stop stays ₹155.58; funded ₹5.95 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-08-28  AVANTIFEED  PYRAMID BUY ₹5.70 at ₹1,938.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,726.43; funded ₹5.70 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-08-28  FRETAIL     PYRAMID BUY ₹6.72 at ₹509.80 (box jump — doubling the stake with NEW capital; stop stays ₹447.45; funded ₹6.72 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-09-04  FRETAIL     PYRAMID BUY ₹14.50 at ₹550.00 (box jump — doubling the stake with NEW capital; stop stays ₹475.00; funded ₹14.50 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-09-04  SPARC       PYRAMID BUY ₹6.96 at ₹390.00 (box jump — doubling the stake with NEW capital; stop stays ₹362.19; funded ₹6.96 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-09-11  HOVS        PYRAMID BUY ₹23.30 at ₹324.45 (box jump — doubling the stake with NEW capital; stop stays ₹233.27; funded ₹23.30 from the pocket + ₹0.00 fresh; charges ₹0.03)
2017-09-11  INSECTICID  PYRAMID BUY ₹14.16 at ₹918.05 (box jump — doubling the stake with NEW capital; stop stays ₹821.75; funded ₹14.16 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-09-21  INSECTICID  SELL ₹25.32 at stop ₹821.75 (-3.0%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹18.98 of doubled capital and its returns OUT to the pocket
2017-09-25  FRETAIL     PYRAMID BUY ₹28.68 at ₹544.10 (box jump — doubling the stake with NEW capital; stop stays ₹495.38; funded ₹28.68 from the pocket + ₹0.00 fresh; charges ₹0.03)
2017-09-25  SPARC       SELL ₹12.90 at stop ₹362.19 (-8.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹6.44 of doubled capital and its returns OUT to the pocket
2017-10-03  AVANTIFEED  PYRAMID BUY ₹12.11 at ₹2,058.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,776.69; funded ₹12.11 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-10-03  BBTC        BUY ₹12.79 at ₹1,295.40 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.83× weekly, month 2.74×, ladder rising; stop ₹959.83; charges ₹0.02)
2017-10-09  BBTC        PYRAMID BUY ₹13.94 at ₹1,414.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,094.59; funded ₹13.94 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-10-16  BBTC        PYRAMID BUY ₹30.39 at ₹1,542.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,257.13; funded ₹30.39 from the pocket + ₹0.00 fresh; charges ₹0.04)
2017-10-23  AVANTIFEED  PYRAMID BUY ₹31.79 at ₹2,705.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,232.50; funded ₹31.79 from the pocket + ₹0.00 fresh; charges ₹0.04)
2017-11-06  BBTC        PYRAMID BUY ₹65.20 at ₹1,655.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,497.44; funded ₹65.20 from the pocket + ₹0.00 fresh; charges ₹0.08)
2017-11-09  FRETAIL     SELL ₹52.69 at stop ₹500.65 (-5.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹46.09 of doubled capital and its returns OUT to the pocket
2017-11-15  AVANTIFEED  SELL ₹61.98 at stop ₹2,641.00 (+12.4%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹54.22 of doubled capital and its returns OUT to the pocket
2017-11-16  BBTC        SELL ₹117.80 at stop ₹1,497.44 (-3.5%, charges ₹0.12) — the cash goes back to work at the next Friday screen; ₹103.05 of doubled capital and its returns OUT to the pocket
2017-11-20  AJMERA      BUY ₹8.47 at ₹300.30 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.68× weekly, month 2.75×, ladder rising; stop ₹259.02; charges ₹0.01)
2017-11-20  AUTOAXLES   BUY ₹8.53 at ₹1,150.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.34× weekly, month 2.76×, ladder rising; stop ₹842.08; charges ₹0.01)
2017-11-20  HINDOILEXP  BUY ₹8.49 at ₹124.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.39× weekly, month 2.70×, ladder rising; stop ₹102.93; charges ₹0.01)
2017-11-27  HINDOILEXP  PYRAMID BUY ₹8.67 at ₹126.85 (box jump — doubling the stake with NEW capital; stop stays ₹113.14; funded ₹8.67 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-11-27  HOVS        PYRAMID BUY ₹38.71 at ₹269.70 (box jump — doubling the stake with NEW capital; stop stays ₹243.00; funded ₹38.71 from the pocket + ₹0.00 fresh; charges ₹0.05)
2017-12-05  UTTAMSUGAR  SELL ₹9.79 at stop ₹155.58 (-17.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹4.89 of doubled capital and its returns OUT to the pocket
2017-12-11  AJMERA      PYRAMID BUY ₹9.57 at ₹339.50 (box jump — doubling the stake with NEW capital; stop stays ₹313.50; funded ₹9.57 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-12-11  AUTOAXLES   PYRAMID BUY ₹10.62 at ₹1,433.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,241.56; funded ₹10.62 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-12-11  WSTCSTPAPR  BUY ₹8.52 at ₹289.25 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.63× weekly, month 2.08×, ladder rising; stop ₹211.56; charges ₹0.01)
2017-12-12  AJMERA      SELL ₹17.64 at stop ₹313.50 (-2.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.81 of doubled capital and its returns OUT to the pocket
2017-12-18  JKPAPER     BUY ₹8.82 at ₹128.70 (fresh Friday signal — starved 2×, front of the queue — BUY: 5.23× weekly, month 2.77×, ladder rising; stop ₹108.25; charges ₹0.01)
2017-12-26  HINDOILEXP  PYRAMID BUY ₹18.45 at ₹135.00 (box jump — doubling the stake with NEW capital; stop stays ₹118.61; funded ₹18.45 from the pocket + ₹0.00 fresh; charges ₹0.02)
2017-12-26  JKPAPER     PYRAMID BUY ₹9.85 at ₹143.80 (box jump — doubling the stake with NEW capital; stop stays ₹113.73; funded ₹9.85 from the pocket + ₹0.00 fresh; charges ₹0.01)
2017-12-26  WSTCSTPAPR  PYRAMID BUY ₹9.95 at ₹338.00 (box jump — doubling the stake with NEW capital; stop stays ₹252.59; funded ₹9.95 from the pocket + ₹0.00 fresh; charges ₹0.01)
2018-01-08  JKPAPER     PYRAMID BUY ₹22.45 at ₹164.00 (box jump — doubling the stake with NEW capital; stop stays ₹129.20; funded ₹22.45 from the pocket + ₹0.00 fresh; charges ₹0.03)
2018-01-08  WSTCSTPAPR  PYRAMID BUY ₹18.80 at ₹319.70 (box jump — doubling the stake with NEW capital; stop stays ₹287.04; funded ₹18.80 from the pocket + ₹0.00 fresh; charges ₹0.02)
2018-01-29  AUTOAXLES   PYRAMID BUY ₹26.43 at ₹1,785.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,530.26; funded ₹26.43 from the pocket + ₹0.00 fresh; charges ₹0.03)
2018-01-29  HINDOILEXP  PYRAMID BUY ₹37.04 at ₹135.60 (box jump — doubling the stake with NEW capital; stop stays ₹122.15; funded ₹37.04 from the pocket + ₹0.00 fresh; charges ₹0.04)
2018-01-29  JKPAPER     PYRAMID BUY ₹39.65 at ₹144.90 (box jump — doubling the stake with NEW capital; stop stays ₹132.33; funded ₹39.65 from the pocket + ₹0.00 fresh; charges ₹0.05)
2018-01-30  WSTCSTPAPR  SELL ₹33.71 at stop ₹287.04 (-9.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹25.27 of doubled capital and its returns OUT to the pocket
2018-01-31  AUTOAXLES   SELL ₹45.24 at stop ₹1,530.26 (-0.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹33.92 of doubled capital and its returns OUT to the pocket
2018-02-02  HINDOILEXP  SELL ₹66.62 at stop ₹122.15 (-8.1%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹58.28 of doubled capital and its returns OUT to the pocket
2018-02-02  JKPAPER     SELL ₹72.29 at stop ₹132.33 (-10.3%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹63.24 of doubled capital and its returns OUT to the pocket
2018-02-05  ESTER       BUY ₹7.48 at ₹65.15 (fresh Friday signal — ACCUMULATE: 2.57× weekly, month 3.16×, ladder rising; stop ₹52.83; charges ₹0.01)
2018-02-05  LUXIND      BUY ₹14.83 at ₹1,621.10 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.54× weekly, month 2.50×, ladder rising; stop ₹1,425.00; charges ₹0.02)
2018-02-05  MPHASIS     BUY ₹14.84 at ₹851.10 (fresh Friday signal — BUY: 3.88× weekly, month 3.19×, ladder rising; stop ₹668.70; charges ₹0.02)
2018-02-12  LUXIND      PYRAMID BUY ₹15.99 at ₹1,749.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,448.75; funded ₹15.99 from the pocket + ₹0.00 fresh; charges ₹0.02)
2018-02-19  MPHASIS     PYRAMID BUY ₹14.98 at ₹860.10 (box jump — doubling the stake with NEW capital; stop stays ₹771.50; funded ₹14.98 from the pocket + ₹0.00 fresh; charges ₹0.02)
2018-03-19  LUXIND      PYRAMID BUY ₹32.61 at ₹1,785.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,578.09; funded ₹32.61 from the pocket + ₹0.00 fresh; charges ₹0.04)
2018-03-22  HOVS        SELL ₹69.64 at stop ₹243.00 (-18.2%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹52.21 of doubled capital and its returns OUT to the pocket
2018-04-02  TAX         FY2018 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹36.59 / LT ₹0.00)
2018-04-09  EXCELINDUS  BUY ₹12.99 at ₹1,054.00 (fresh Friday signal — BUY: 1.80× weekly, month 1.75×, ladder rising; stop ₹763.20; charges ₹0.02)
2018-04-16  LUXIND      PYRAMID BUY ₹65.87 at ₹1,803.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,691.24; funded ₹65.87 from the pocket + ₹0.00 fresh; charges ₹0.08)
2018-04-23  ESTER       PYRAMID BUY ₹8.43 at ₹73.50 (box jump — doubling the stake with NEW capital; stop stays ₹65.17; funded ₹8.43 from the pocket + ₹0.00 fresh; charges ₹0.01)
2018-05-07  EXCELINDUS  PYRAMID BUY ₹16.92 at ₹1,375.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,282.59; funded ₹16.92 from the pocket + ₹0.00 fresh; charges ₹0.02)
2018-05-10  ESTER       SELL ₹14.93 at stop ₹65.17 (-6.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹7.46 of doubled capital and its returns OUT to the pocket
2018-05-11  EXCELINDUS  SELL ₹31.52 at stop ₹1,282.59 (+5.6%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹15.75 of doubled capital and its returns OUT to the pocket
2018-05-14  FSL         BUY ₹25.12 at ₹71.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.75× weekly, month 2.12×, ladder rising; stop ₹57.09; charges ₹0.03)
2018-05-14  MPHASIS     PYRAMID BUY ₹33.77 at ₹970.00 (box jump — doubling the stake with NEW capital; stop stays ₹913.00; funded ₹33.77 from the pocket + ₹0.00 fresh; charges ₹0.04)
2018-05-28  FSL         PYRAMID BUY ₹25.55 at ₹72.30 (box jump — doubling the stake with NEW capital; stop stays ₹63.32; funded ₹25.55 from the pocket + ₹0.00 fresh; charges ₹0.03)
2018-05-28  MPHASIS     PYRAMID BUY ₹78.17 at ₹1,123.40 (box jump — doubling the stake with NEW capital; stop stays ₹978.50; funded ₹78.17 from the pocket + ₹0.00 fresh; charges ₹0.09)
2018-05-30  LUXIND      SELL ₹135.07 at stop ₹1,852.59 (+4.7%, charges ₹0.14) — the cash goes back to work at the next Friday screen; ₹118.16 of doubled capital and its returns OUT to the pocket
2018-06-04  BODALCHEM   BUY ₹19.47 at ₹144.85 (fresh Friday signal — starved 2×, front of the queue — BUY: 4.06× weekly, month 1.85×, ladder rising; stop ₹116.38; charges ₹0.02)
2018-06-11  BODALCHEM   PYRAMID BUY ₹19.37 at ₹144.25 (box jump — doubling the stake with NEW capital; stop stays ₹129.25; funded ₹19.37 from the pocket + ₹0.00 fresh; charges ₹0.02)
2018-06-26  BODALCHEM   SELL ₹34.65 at stop ₹129.25 (-10.6%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹17.31 of doubled capital and its returns OUT to the pocket
2018-07-02  PAGEIND     BUY ₹17.33 at ₹27,870.00 (fresh Friday signal — BUY: 1.79× weekly, month 1.61×, ladder rising; stop ₹24,890.52; charges ₹0.02)
2018-07-09  PAGEIND     PYRAMID BUY ₹17.71 at ₹28,500.00 (box jump — doubling the stake with NEW capital; stop stays ₹25,560.37; funded ₹17.71 from the pocket + ₹0.00 fresh; charges ₹0.02)
2018-07-30  PAGEIND     PYRAMID BUY ₹36.26 at ₹29,200.00 (box jump — doubling the stake with NEW capital; stop stays ₹26,333.33; funded ₹36.26 from the pocket + ₹0.00 fresh; charges ₹0.04)
2018-08-10  FSL         SELL ₹44.69 at stop ₹63.32 (-11.6%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹22.33 of doubled capital and its returns OUT to the pocket
2018-08-13  TCIEXP      BUY ₹22.36 at ₹710.00 (fresh Friday signal — BUY: 2.91× weekly, month 2.87×, ladder rising; stop ₹580.45; charges ₹0.03)
2018-08-20  TCIEXP      PYRAMID BUY ₹22.72 at ₹722.50 (box jump — doubling the stake with NEW capital; stop stays ₹652.46; funded ₹22.72 from the pocket + ₹0.00 fresh; charges ₹0.03)
2018-09-03  PAGEIND     PYRAMID BUY ₹86.28 at ₹34,760.90 (box jump — doubling the stake with NEW capital; stop stays ₹32,310.88; funded ₹86.28 from the pocket + ₹0.00 fresh; charges ₹0.10)
2018-09-05  PAGEIND     SELL ₹160.13 at stop ₹32,310.88 (+1.8%, charges ₹0.17) — the cash goes back to work at the next Friday screen; ₹140.08 of doubled capital and its returns OUT to the pocket
2018-09-05  TCIEXP      SELL ₹40.97 at stop ₹652.46 (-8.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹20.47 of doubled capital and its returns OUT to the pocket
2018-09-10  LTI         BUY ₹18.60 at ₹1,955.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 11.33× weekly, month 3.91×, ladder rising; stop ₹1,643.31; charges ₹0.02)
2018-09-10  VINDHYATEL  BUY ₹21.95 at ₹1,579.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.16× weekly, month 3.88×, ladder rising; stop ₹1,234.67; charges ₹0.03)
2018-09-21  LTI         SELL ₹15.60 at stop ₹1,643.31 (-15.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2018-09-24  MUTHOOTFIN  BUY ₹15.60 at ₹452.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.94× weekly, month 2.74×, ladder rising; stop ₹412.35; charges ₹0.02)
2018-09-24  VINDHYATEL  PYRAMID BUY ₹21.65 at ₹1,559.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,378.45; funded ₹21.65 from the pocket + ₹0.00 fresh; charges ₹0.03)
2018-09-25  MPHASIS     SELL ₹163.08 at stop ₹1,173.72 (+15.3%, charges ₹0.17) — the cash goes back to work at the next Friday screen; ₹142.66 of doubled capital and its returns OUT to the pocket
2018-09-26  VINDHYATEL  SELL ₹38.22 at stop ₹1,378.45 (-12.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹19.10 of doubled capital and its returns OUT to the pocket
2018-09-27  MUTHOOTFIN  SELL ₹14.20 at stop ₹412.35 (-8.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2018-10-15  BAJAJHIND   BUY ₹6.04 at ₹11.00 (fresh Friday signal — ACCUMULATE: 2.11× weekly, month 4.50×, ladder rising; stop ₹6.18; charges ₹0.01)
2018-10-22  HATHWAY     BUY ₹5.98 at ₹30.60 (fresh Friday signal — BUY: 3.56× weekly, month 1.61×, ladder rising; stop ₹18.96; charges ₹0.01)
2018-10-29  HATHWAY     PYRAMID BUY ₹5.90 at ₹30.25 (box jump — doubling the stake with NEW capital; stop stays ₹26.93; funded ₹5.90 from the pocket + ₹0.00 fresh; charges ₹0.01)
2018-11-05  TIIL        BUY ₹6.61 at ₹648.95 (fresh Friday signal — ACCUMULATE: 2.84× weekly, month 1.63×, ladder rising; stop ₹502.60; charges ₹0.01)
2018-11-19  DALMIASUG   BUY ₹6.59 at ₹101.20 (fresh Friday signal — BUY: 1.89× weekly, month 2.53×, ladder rising; stop ₹51.84; charges ₹0.01)
2018-11-26  BIRLACABLE  BUY ₹7.14 at ₹216.10 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.57× weekly, month 2.89×, ladder rising; stop ₹168.72; charges ₹0.01)
2018-11-26  DALMIASUG   PYRAMID BUY ₹6.81 at ₹104.80 (box jump — doubling the stake with NEW capital; stop stays ₹94.14; funded ₹6.81 from the pocket + ₹0.00 fresh; charges ₹0.01)
2018-12-03  BIRLACABLE  PYRAMID BUY ₹7.22 at ₹218.80 (box jump — doubling the stake with NEW capital; stop stays ₹195.70; funded ₹7.22 from the pocket + ₹0.00 fresh; charges ₹0.01)
2018-12-03  GODFRYPHLP  BUY ₹7.79 at ₹928.40 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.59× weekly, month 1.69×, ladder rising; stop ₹795.15; charges ₹0.01)
2018-12-03  KESORAMIND  BUY ₹7.78 at ₹85.00 (fresh Friday signal — BUY: 4.55× weekly, month 1.54×, ladder rising; stop ₹71.39; charges ₹0.01)
2018-12-04  BIRLACABLE  SELL ₹12.90 at stop ₹195.70 (-10.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹6.45 of doubled capital and its returns OUT to the pocket
2018-12-10  DALMIASUG   SELL ₹12.22 at stop ₹94.14 (-8.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹6.11 of doubled capital and its returns OUT to the pocket
2018-12-17  BANKBEES    BUY ₹7.04 at ₹274.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.75× weekly, month 4.65×, ladder rising; stop ₹248.08; charges ₹0.01)
2018-12-17  GODFRYPHLP  PYRAMID BUY ₹7.78 at ₹928.00 (box jump — doubling the stake with NEW capital; stop stays ₹812.30; funded ₹7.78 from the pocket + ₹0.00 fresh; charges ₹0.01)
2018-12-17  PREMEXPLN   BUY ₹7.04 at ₹264.80 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 5.68×, ladder rising; stop ₹184.16; charges ₹0.01)
2018-12-24  BEML        BUY ₹4.28 at ₹890.10 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.73× weekly, month 2.62×, ladder rising; stop ₹648.90; charges ₹0.01)
2018-12-26  GODFRYPHLP  SELL ₹13.59 at stop ₹812.30 (-12.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹6.79 of doubled capital and its returns OUT to the pocket
2019-01-07  BANKBEES    PYRAMID BUY ₹7.18 at ₹279.65 (box jump — doubling the stake with NEW capital; stop stays ₹255.55; funded ₹7.18 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-01-07  BEML        PYRAMID BUY ₹4.30 at ₹896.00 (box jump — doubling the stake with NEW capital; stop stays ₹809.88; funded ₹4.30 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-01-14  BANKBEES    PYRAMID BUY ₹14.37 at ₹279.88 (box jump — doubling the stake with NEW capital; stop stays ₹260.57; funded ₹14.37 from the pocket + ₹0.00 fresh; charges ₹0.02)
2019-01-14  SKFINDIA    BUY ₹6.80 at ₹1,940.00 (fresh Friday signal — ACCUMULATE: 6.62× weekly, month 3.44×, ladder rising; stop ₹1,776.45; charges ₹0.01)
2019-01-21  BANKBEES    PYRAMID BUY ₹29.23 at ₹284.90 (box jump — doubling the stake with NEW capital; stop stays ₹263.25; funded ₹29.23 from the pocket + ₹0.00 fresh; charges ₹0.03)
2019-01-28  BEML        SELL ₹7.77 at stop ₹809.88 (-9.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹3.88 of doubled capital and its returns OUT to the pocket
2019-01-29  KESORAMIND  SELL ₹6.52 at stop ₹71.39 (-16.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2019-02-11  INFRATEL    BUY ₹10.41 at ₹326.00 (fresh Friday signal — BUY: 1.56× weekly, month 1.65×, ladder rising; stop ₹270.75; charges ₹0.01)
2019-02-19  HATHWAY     SELL ₹10.50 at stop ₹26.93 (-11.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹5.24 of doubled capital and its returns OUT to the pocket
2019-02-25  INFRATEL    PYRAMID BUY ₹10.00 at ₹313.60 (box jump — doubling the stake with NEW capital; stop stays ₹277.35; funded ₹10.00 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-02-25  PREMEXPLN   PYRAMID BUY ₹5.74 at ₹216.00 (box jump — doubling the stake with NEW capital; stop stays ₹193.80; funded ₹5.74 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-03-11  BAJAJHIND   PYRAMID BUY ₹4.91 at ₹8.95 (box jump — doubling the stake with NEW capital; stop stays ₹7.69; funded ₹4.91 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-03-11  SKFINDIA    PYRAMID BUY ₹6.84 at ₹1,955.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,828.80; funded ₹6.84 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-03-20  BAJAJHIND   SELL ₹8.43 at stop ₹7.69 (-22.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen; ₹4.21 of doubled capital and its returns OUT to the pocket
2019-03-25  JUSTDIAL    BUY ₹9.47 at ₹615.00 (fresh Friday signal — BUY: 3.82× weekly, month 1.70×, ladder rising; stop ₹467.69; charges ₹0.01)
2019-04-01  JUSTDIAL    PYRAMID BUY ₹9.41 at ₹611.95 (box jump — doubling the stake with NEW capital; stop stays ₹565.25; funded ₹9.41 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-04-01  TAX         FY2019 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹43.28 / LT ₹0.00)
2019-04-08  PREMEXPLN   PYRAMID BUY ₹12.44 at ₹234.30 (box jump — doubling the stake with NEW capital; stop stays ₹214.62; funded ₹12.44 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-04-08  SKFINDIA    PYRAMID BUY ₹14.58 at ₹2,082.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,891.83; funded ₹14.58 from the pocket + ₹0.00 fresh; charges ₹0.02)
2019-04-22  JUSTDIAL    SELL ₹17.35 at stop ₹565.25 (-7.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.67 of doubled capital and its returns OUT to the pocket
2019-04-25  INFRATEL    SELL ₹17.66 at stop ₹277.35 (-13.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.83 of doubled capital and its returns OUT to the pocket
2019-04-30  IBREALEST   BUY ₹14.31 at ₹125.40 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 3.85× weekly, month 3.02×, ladder rising; stop ₹91.19; charges ₹0.02)
2019-04-30  TIIL        SELL ₹5.11 at stop ₹502.60 (-22.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2019-05-06  RUCHISOYA   BUY ₹8.32 at ₹9.10 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.65× weekly, month 1.62×, ladder rising; stop ₹5.61; charges ₹0.01)
2019-05-08  SKFINDIA    SELL ₹26.44 at stop ₹1,891.83 (-6.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹19.82 of doubled capital and its returns OUT to the pocket
2019-05-10  PREMEXPLN   SELL ₹22.76 at stop ₹214.62 (-9.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹17.06 of doubled capital and its returns OUT to the pocket
2019-05-13  MTEDUCARE   BUY ₹9.66 at ₹94.20 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.93× weekly, month 4.89×, ladder rising; stop ₹73.96; charges ₹0.01)
2019-05-14  IBREALEST   SELL ₹10.38 at stop ₹91.19 (-27.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2019-05-17  MTEDUCARE   SELL ₹7.57 at stop ₹73.96 (-21.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2019-05-27  HEIDELBERG  BUY ₹10.04 at ₹206.20 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.76× weekly, month 1.79×, ladder rising; stop ₹162.93; charges ₹0.01)
2019-05-27  INOXLEISUR  BUY ₹10.02 at ₹349.40 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.36× weekly, month 1.76×, ladder rising; stop ₹282.15; charges ₹0.01)
2019-06-24  INOXLEISUR  PYRAMID BUY ₹9.25 at ₹322.95 (box jump — doubling the stake with NEW capital; stop stays ₹291.23; funded ₹9.25 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-06-25  RUCHISOYA   SELL ₹5.12 at stop ₹5.61 (-38.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2019-07-01  HEIDELBERG  PYRAMID BUY ₹9.51 at ₹195.55 (box jump — doubling the stake with NEW capital; stop stays ₹172.09; funded ₹9.51 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-07-15  HEIDELBERG  PYRAMID BUY ₹19.25 at ₹198.00 (box jump — doubling the stake with NEW capital; stop stays ₹177.65; funded ₹19.25 from the pocket + ₹0.00 fresh; charges ₹0.02)
2019-07-22  BANKBEES    SELL ₹60.55 at stop ₹295.55 (+4.9%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹52.96 of doubled capital and its returns OUT to the pocket
2019-07-29  HDFCLIFE    BUY ₹5.58 at ₹499.80 (fresh Friday signal — BUY: 2.03× weekly, month 1.79×, ladder rising; stop ₹425.27; charges ₹0.01)
2019-07-29  SBILIFE     BUY ₹7.67 at ₹793.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.60× weekly, month 2.01×, ladder rising; stop ₹695.26; charges ₹0.01)
2019-07-31  INOXLEISUR  SELL ₹16.66 at stop ₹291.23 (-13.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.32 of doubled capital and its returns OUT to the pocket
2019-08-05  HDFCLIFE    PYRAMID BUY ₹5.48 at ₹491.50 (box jump — doubling the stake with NEW capital; stop stays ₹451.35; funded ₹5.48 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-08-05  HDFCMFGETF  BUY ₹6.92 at ₹3,253.50 (fresh Friday signal — BUY: 2.01× weekly, month 1.54×, ladder rising; stop ₹2,862.02; charges ₹0.01)
2019-08-13  HDFCMFGETF  PYRAMID BUY ₹7.19 at ₹3,383.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,961.24; funded ₹7.19 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-08-13  SBILIFE     PYRAMID BUY ₹7.70 at ₹797.25 (box jump — doubling the stake with NEW capital; stop stays ₹714.92; funded ₹7.70 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-08-26  HDFCMFGETF  PYRAMID BUY ₹14.77 at ₹3,476.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,204.40; funded ₹14.77 from the pocket + ₹0.00 fresh; charges ₹0.02)
2019-08-26  SBILIFE     PYRAMID BUY ₹16.18 at ₹838.00 (box jump — doubling the stake with NEW capital; stop stays ₹723.62; funded ₹16.18 from the pocket + ₹0.00 fresh; charges ₹0.02)
2019-09-03  HDFCLIFE    PYRAMID BUY ₹12.28 at ₹551.40 (box jump — doubling the stake with NEW capital; stop stays ₹487.11; funded ₹12.28 from the pocket + ₹0.00 fresh; charges ₹0.01)
2019-09-03  SBILIFE     PYRAMID BUY ₹32.13 at ₹832.80 (box jump — doubling the stake with NEW capital; stop stays ₹765.27; funded ₹32.13 from the pocket + ₹0.00 fresh; charges ₹0.04)
2019-09-30  HDFCLIFE    PYRAMID BUY ₹26.05 at ₹585.00 (box jump — doubling the stake with NEW capital; stop stays ₹513.00; funded ₹26.05 from the pocket + ₹0.00 fresh; charges ₹0.03)
2019-10-22  HDFCMFGETF  PYRAMID BUY ₹29.47 at ₹3,470.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,260.49; funded ₹29.47 from the pocket + ₹0.00 fresh; charges ₹0.03)
2019-12-09  HEIDELBERG  SELL ₹34.48 at stop ₹177.65 (-10.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹25.85 of doubled capital and its returns OUT to the pocket
2020-02-03  HDFCLIFE    SELL ₹49.08 at stop ₹552.05 (-0.4%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹42.93 of doubled capital and its returns OUT to the pocket
2020-02-03  SBILIFE     SELL ₹70.12 at stop ₹910.24 (+10.4%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹61.34 of doubled capital and its returns OUT to the pocket
2020-02-10  BOROSIL     BUY ₹6.17 at ₹202.25 (fresh Friday signal — BUY: 8.28× weekly, month 4.15×, ladder rising; stop ₹159.55; charges ₹0.01)
2020-02-10  SUDARSCHEM  BUY ₹9.39 at ₹466.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.70× weekly, month 2.74×, ladder rising; stop ₹423.70; charges ₹0.01)
2020-02-10  TRENT       BUY ₹9.40 at ₹665.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.26× weekly, month 1.73×, ladder rising; stop ₹539.60; charges ₹0.01)
2020-02-17  BOROSIL     PYRAMID BUY ₹5.85 at ₹192.00 (box jump — doubling the stake with NEW capital; stop stays ₹181.45; funded ₹5.85 from the pocket + ₹0.00 fresh; charges ₹0.01)
2020-02-24  SUDARSCHEM  PYRAMID BUY ₹9.26 at ₹460.00 (box jump — doubling the stake with NEW capital; stop stays ₹431.73; funded ₹9.26 from the pocket + ₹0.00 fresh; charges ₹0.01)
2020-03-09  SUDARSCHEM  SELL ₹17.35 at stop ₹431.73 (-6.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.67 of doubled capital and its returns OUT to the pocket
2020-03-13  HDFCMFGETF  SELL ₹60.04 at stop ₹3,540.65 (+3.1%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹52.52 of doubled capital and its returns OUT to the pocket
2020-03-13  TRENT       SELL ₹7.61 at stop ₹539.60 (-18.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
```
