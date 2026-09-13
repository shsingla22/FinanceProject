# The Darvas screen — 2015-03-01 → 2020-03-31

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2014-03-01 → 2020-03-31, 750 symbols, in `2014-03-01_to_2020-03-31/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **The universe is POINT-IN-TIME:** the top symbols by actual traded value in the as-of month, from NSE's official bhavcopies (`constituents_asof.csv`) — companies that later died or delisted are IN, later IPOs are OUT, so survivorship bias is removed; the price of using raw exchange data is heuristic split/bonus adjustment (standard ratio against the prior close AND a matching volume step; every adjustment applied is listed in `_adjustments.csv`). No slippage, stop exits at the stop price, fractional shares. Stored fiscal statements exist for 43% of this universe — a stock without statements cannot be blocked by the earnings gate (only a FALLING verdict blocks), which loosens that gate for the rest.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), best volume reaction first, at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with NEW capital, 3× cap.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled with FRESH MONEY from outside the portfolio, equal to the position's market value, at the next day's open — but AT MOST THREE TIMES per position (8× the first slice), so the capital the rule demands stays realistic. The new money never touches the portfolio's cash — fresh entries are never starved — and every injection is dated and logged, so the honest yardstick is the money-weighted return (XIRR), not a naive multiple. Each add-on is its own tax lot on its own holding clock; the ratcheted stop covers the whole enlarged position; a jump past the cap is logged, never doubled.

## The headline — XIRR is the honest yardstick

| Engine | Money put in | Final value | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | ₹93,742.02 crore (₹100 + ₹93,742.02 crore injected) | **₹75,629.45 crore** | **-51.35%** |
| B: doubling, before charges and tax | ₹1.01 lakh crore | ₹81,683.00 crore | -50.77% |
| **A: no doubling, NET of charges and tax** | ₹100.00 | **₹108.99** | **+1.71%** |
| A: no doubling, before charges and tax | ₹100.00 | ₹124.68 | +4.44% |
| Nifty 50 (pre-cost, pre-tax) | ₹100.00 | ₹96.20 | -0.76% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹0.00; unrealised gains in both end books carry further deferred liabilities.*

5.07 years, 266 weekly screens. Engine B injected new capital 253 times (gross run: 253); the complete dated injection list is in the blotter and the events CSV.

## What the frictions took (net runs)

| | Engine A: no doubling | Engine B: doubling |
|---|---:|---:|
| Transaction charges | ₹4.62 | ₹365.40 crore |
| Capital-gains tax paid | ₹16.14 | ₹0.00 |
| Tax accrued, final part-year | ₹0.00 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2015 | 2015-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹1.34 / ₹0.00 |
| FY2016 | 2016-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹2,738.21 / ₹0.00 |
| FY2017 | 2017-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹36,557.91 / ₹0.00 |
| FY2018 | 2018-04-02 | ₹0.00 | ₹0.00 | ₹0.00 | ₹19.82 lakh / ₹0.00 |
| FY2019 | 2019-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹255.67 crore / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹17,747.32 crore / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2015 | 2015-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹0.73 / ₹0.00 |
| FY2016 | 2016-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹0.10 / ₹0.00 |
| FY2017 | 2017-04-03 | ₹13.32 | ₹0.00 | ₹2.66 | ₹0.00 / ₹0.00 |
| FY2018 | 2018-04-02 | ₹67.35 | ₹0.02 | ₹13.47 | ₹0.00 / ₹0.00 |
| FY2019 | 2019-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹19.38 / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹52.64 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2015 (2015-12-24) | ₹113.89 | +13.9% | ₹11,124.20 | ₹11,076.80 | -2.6% | -12.0% |
| 2016 (2016-12-30) | ₹113.65 | -0.2% | ₹4.57 lakh | ₹4.24 lakh | +17.0% | +4.1% |
| 2017 (2017-12-29) | ₹181.59 | +59.8% | ₹23.76 crore | ₹20.84 crore | +81.0% | +28.6% |
| 2018 (2018-12-28) | ₹157.05 | -13.5% | ₹971.19 crore | ₹1,088.20 crore | -32.0% | +3.1% |
| 2019 (2019-12-27) | ₹120.26 | -23.4% | ₹34,664.60 crore | ₹35,208.77 crore | -12.8% | +12.8% |
| 2020 (2020-03-31) | ₹108.99 | -9.4% | ₹75,629.45 crore | ₹57,424.17 crore | -24.5% | -29.8% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-13.3%** (A: -47.8%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **167 closed trades**: 29 winners (17%), average winner +18.5%, average loser -10.8% (returns per blended entry price).
- Best closed trade GOACARBON +131.1%; worst RUCHISOYA -38.4%.
- Median holding period 49 days.
- Cash share of equity averaged 17%; fully in cash 1 of 266 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

| Month-end screen | B equity | B injected so far | B cash | B positions | A equity |
|---|---:|---:|---:|---:|---:|
| 2015-03-27 | ₹160.09 | ₹71.82 | ₹18.48 | 9 | ₹91.49 |
| 2015-04-30 | ₹214.10 | ₹131.14 | ₹150.67 | 3 | ₹89.86 |
| 2015-05-29 | ₹301.48 | ₹220.34 | ₹34.11 | 8 | ₹88.97 |
| 2015-06-26 | ₹426.79 | ₹313.31 | ₹11.64 | 9 | ₹93.40 |
| 2015-07-31 | ₹974.13 | ₹704.15 | ₹11.64 | 9 | ₹110.83 |
| 2015-08-28 | ₹1,841.38 | ₹1,707.33 | ₹1,216.82 | 4 | ₹107.00 |
| 2015-09-24 | ₹1,991.64 | ₹1,810.57 | ₹614.29 | 7 | ₹109.39 |
| 2015-10-30 | ₹4,049.53 | ₹3,868.31 | ₹708.09 | 9 | ₹113.67 |
| 2015-11-27 | ₹5,825.81 | ₹5,880.66 | ₹1,991.20 | 9 | ₹112.30 |
| 2015-12-24 | ₹11,124.20 | ₹11,076.80 | ₹176.70 | 11 | ₹113.89 |
| 2016-01-29 | ₹13,234.57 | ₹15,013.30 | ₹5,650.36 | 6 | ₹105.93 |
| 2016-02-26 | ₹19,168.12 | ₹22,060.11 | ₹4,313.61 | 6 | ₹97.35 |
| 2016-03-23 | ₹25,308.23 | ₹28,535.48 | ₹6,633.34 | 5 | ₹100.77 |
| 2016-04-29 | ₹37,893.43 | ₹40,221.95 | ₹0.00 | 8 | ₹105.75 |
| 2016-05-27 | ₹63,233.29 | ₹64,353.62 | ₹2,803.35 | 7 | ₹103.25 |
| 2016-06-24 | ₹73,840.44 | ₹74,506.60 | ₹19,882.87 | 6 | ₹107.72 |
| 2016-07-29 | ₹1.05 lakh | ₹1.02 lakh | ₹350.07 | 9 | ₹115.33 |
| 2016-08-26 | ₹1.73 lakh | ₹1.73 lakh | ₹350.07 | 9 | ₹115.81 |
| 2016-09-30 | ₹1.94 lakh | ₹1.89 lakh | ₹23,255.68 | 7 | ₹116.40 |
| 2016-10-28 | ₹3.21 lakh | ₹3.06 lakh | ₹6,797.41 | 9 | ₹117.43 |
| 2016-11-25 | ₹3.42 lakh | ₹3.60 lakh | ₹46,883.79 | 7 | ₹108.08 |
| 2016-12-30 | ₹4.57 lakh | ₹4.35 lakh | ₹85,898.48 | 7 | ₹113.65 |
| 2017-01-27 | ₹8.04 lakh | ₹7.16 lakh | ₹0.00 | 9 | ₹122.40 |
| 2017-02-23 | ₹12.50 lakh | ₹11.71 lakh | ₹1.39 lakh | 8 | ₹125.99 |
| 2017-03-31 | ₹19.81 lakh | ₹18.06 lakh | ₹0.00 | 10 | ₹129.96 |
| 2017-04-28 | ₹40.44 lakh | ₹36.23 lakh | ₹0.00 | 10 | ₹134.52 |
| 2017-05-26 | ₹63.65 lakh | ₹62.81 lakh | ₹39.52 lakh | 5 | ₹129.42 |
| 2017-06-30 | ₹1.16 crore | ₹1.16 crore | ₹35.00 lakh | 9 | ₹134.23 |
| 2017-07-28 | ₹2.02 crore | ₹1.99 crore | ₹2.52 lakh | 12 | ₹134.94 |
| 2017-08-24 | ₹2.04 crore | ₹2.18 crore | ₹16.40 lakh | 11 | ₹125.36 |
| 2017-09-29 | ₹4.67 crore | ₹4.65 crore | ₹1.43 crore | 8 | ₹133.60 |
| 2017-10-27 | ₹8.69 crore | ₹7.49 crore | ₹0.00 | 11 | ₹151.21 |
| 2017-11-24 | ₹14.76 crore | ₹12.72 crore | ₹0.00 | 12 | ₹170.67 |
| 2017-12-29 | ₹23.76 crore | ₹20.88 crore | ₹54.68 lakh | 11 | ₹181.59 |
| 2018-01-25 | ₹46.04 crore | ₹34.12 crore | ₹84.93 lakh | 11 | ₹208.39 |
| 2018-02-23 | ₹72.47 crore | ₹67.00 crore | ₹0.00 | 11 | ₹196.18 |
| 2018-03-28 | ₹82.05 crore | ₹79.90 crore | ₹1.96 crore | 10 | ₹188.26 |
| 2018-04-27 | ₹122.26 crore | ₹115.19 crore | ₹22.22 crore | 8 | ₹188.11 |
| 2018-05-25 | ₹154.64 crore | ₹148.88 crore | ₹0.00 | 10 | ₹180.07 |
| 2018-06-29 | ₹222.25 crore | ₹225.50 crore | ₹64.99 lakh | 9 | ₹177.33 |
| 2018-07-27 | ₹345.19 crore | ₹341.54 crore | ₹89.04 lakh | 9 | ₹179.24 |
| 2018-08-31 | ₹776.06 crore | ₹708.12 crore | ₹0.00 | 8 | ₹190.13 |
| 2018-09-28 | ₹843.68 crore | ₹936.85 crore | ₹754.60 crore | 3 | ₹163.34 |
| 2018-10-26 | ₹822.77 crore | ₹936.85 crore | ₹662.34 crore | 4 | ₹159.67 |
| 2018-11-30 | ₹903.67 crore | ₹1,018.19 crore | ₹662.34 crore | 4 | ₹159.45 |
| 2018-12-28 | ₹971.19 crore | ₹1,109.08 crore | ₹443.84 crore | 7 | ₹157.05 |
| 2019-01-25 | ₹1,704.74 crore | ₹1,915.88 crore | ₹0.00 | 10 | ₹150.59 |
| 2019-02-22 | ₹1,808.68 crore | ₹2,068.14 crore | ₹158.83 crore | 8 | ₹146.55 |
| 2019-03-29 | ₹2,739.58 crore | ₹2,821.98 crore | ₹130.41 crore | 8 | ₹149.94 |
| 2019-04-26 | ₹3,516.16 crore | ₹3,848.64 crore | ₹1,788.86 crore | 5 | ₹142.63 |
| 2019-05-31 | ₹3,604.77 crore | ₹4,199.33 crore | ₹291.51 crore | 9 | ₹134.41 |
| 2019-06-28 | ₹4,714.13 crore | ₹5,539.25 crore | ₹460.35 crore | 8 | ₹125.48 |
| 2019-07-26 | ₹6,527.61 crore | ₹7,662.76 crore | ₹2,379.10 crore | 7 | ₹121.66 |
| 2019-08-30 | ₹15,535.00 crore | ₹16,540.02 crore | ₹0.00 | 9 | ₹123.36 |
| 2019-09-27 | ₹19,384.93 crore | ₹20,395.23 crore | ₹0.00 | 9 | ₹124.32 |
| 2019-10-25 | ₹25,850.10 crore | ₹26,738.31 crore | ₹2,715.06 crore | 8 | ₹123.28 |
| 2019-11-29 | ₹32,008.83 crore | ₹33,926.74 crore | ₹0.00 | 9 | ₹120.48 |
| 2019-12-27 | ₹34,664.60 crore | ₹36,317.85 crore | ₹1,362.34 crore | 8 | ₹120.26 |
| 2020-01-31 | ₹52,596.87 crore | ₹56,813.85 crore | ₹8,524.79 crore | 10 | ₹122.15 |
| 2020-02-28 | ₹84,874.90 crore | ₹89,631.65 crore | ₹8,088.44 crore | 11 | ₹121.09 |
| 2020-03-31 | ₹75,629.45 crore | ₹93,742.02 crore | ₹75,624.88 crore | 2 | ₹108.99 |

## Engine B — still held at the end

| Stock | First entry | Blended entry ₹ | Lots | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|---:|
| RELGOLD | 2016-02-15 | 2,549.56 | 4 | 2,713.30 | 2,556.50 | +6.4% |
| SEINV | 2018-01-22 | 340.05 | 1 | 352.20 | 153.56 | +3.6% |

## Engine B — every closed trade

*Returns are on the blended entry price across lots.*

| Stock | First entry | Blended ₹ | Lots | Exit | Exit ₹ | Return |
|---|---|---:|---:|---|---:|---:|
| JBMA | 2015-03-09 | 238.40 | 2 | 2015-03-23 | 222.30 | -6.8% |
| SPARC | 2015-03-09 | 491.72 | 2 | 2015-04-21 | 426.12 | -13.3% |
| GEOMETRIC | 2015-03-09 | 169.06 | 3 | 2015-04-22 | 158.22 | -6.4% |
| DYNAMATECH | 2015-03-30 | 3,843.00 | 1 | 2015-04-22 | 3,081.75 | -19.8% |
| TWL | 2015-03-09 | 728.70 | 1 | 2015-04-23 | 479.92 | -34.1% |
| SOMANYCERA | 2015-03-09 | 395.05 | 3 | 2015-04-27 | 418.24 | +5.9% |
| HCC | 2015-03-09 | 34.68 | 2 | 2015-04-27 | 31.21 | -10.0% |
| RAMCOSYS | 2015-03-09 | 689.70 | 2 | 2015-04-27 | 597.69 | -13.3% |
| AARTIIND | 2015-03-16 | 351.88 | 2 | 2015-04-27 | 300.44 | -14.6% |
| PETRONENGG | 2015-04-27 | 250.10 | 1 | 2015-06-03 | 207.41 | -17.1% |
| ABIRLANUVO | 2015-05-11 | 930.90 | 2 | 2015-06-03 | 850.92 | -8.6% |
| WELSPUNIND | 2015-05-18 | 44.19 | 2 | 2015-06-09 | 40.67 | -8.0% |
| VADILALIND | 2015-05-04 | 605.41 | 4 | 2015-08-13 | 716.44 | +18.3% |
| INFRATEL | 2015-06-01 | 462.10 | 1 | 2015-08-19 | 400.24 | -13.4% |
| SMLISUZU | 2015-03-09 | 1,138.57 | 4 | 2015-08-24 | 1,110.20 | -2.5% |
| NILKAMAL | 2015-05-18 | 896.53 | 4 | 2015-08-24 | 927.12 | +3.4% |
| MANINDS | 2015-05-18 | 96.88 | 4 | 2015-08-24 | 95.77 | -1.1% |
| CHENNPETRO | 2015-06-15 | 205.86 | 4 | 2015-08-24 | 218.07 | +5.9% |
| DISHTV | 2015-06-15 | 112.25 | 3 | 2015-08-24 | 102.60 | -8.6% |
| JUBILANT | 2015-08-17 | 278.52 | 2 | 2015-09-08 | 218.37 | -21.6% |
| CEATLTD | 2015-09-14 | 1,253.99 | 3 | 2015-10-29 | 1,131.45 | -9.8% |
| FDC | 2015-09-28 | 251.52 | 2 | 2015-11-02 | 232.89 | -7.4% |
| ABBOTINDIA | 2015-09-07 | 5,544.31 | 2 | 2015-11-06 | 5,365.17 | -3.2% |
| UCOBANK | 2015-11-02 | 50.30 | 1 | 2015-11-09 | 45.79 | -9.0% |
| JINDALPOLY | 2015-09-07 | 518.59 | 4 | 2015-11-26 | 494.38 | -4.7% |
| TORNTPHARM | 2015-06-08 | 1,461.24 | 4 | 2015-11-30 | 1,426.04 | -2.4% |
| GHCL | 2015-08-17 | 127.37 | 3 | 2015-12-09 | 129.53 | +1.7% |
| RADICO | 2015-11-16 | 115.60 | 2 | 2015-12-09 | 100.09 | -13.4% |
| KOHINOOR | 2015-11-09 | 50.85 | 2 | 2015-12-14 | 49.50 | -2.6% |
| ECLERX | 2015-03-09 | 1,718.52 | 4 | 2015-12-17 | 1,619.75 | -5.7% |
| TV18BRDCST | 2015-12-21 | 45.17 | 2 | 2016-01-07 | 44.46 | -1.6% |
| SHARONBIO | 2015-12-14 | 30.40 | 2 | 2016-01-12 | 26.93 | -11.4% |
| UNICHEMLAB | 2015-10-05 | 294.55 | 2 | 2016-01-13 | 235.30 | -20.1% |
| NILKAMAL | 2015-11-09 | 1,196.77 | 2 | 2016-01-18 | 1,174.87 | -1.8% |
| GLOBUSSPR | 2015-11-30 | 78.95 | 2 | 2016-01-18 | 65.41 | -17.1% |
| RPGLIFE | 2015-11-30 | 303.28 | 2 | 2016-01-18 | 247.38 | -18.4% |
| EIHOTEL | 2015-12-07 | 124.23 | 2 | 2016-01-18 | 113.05 | -9.0% |
| AJMERA | 2015-12-14 | 130.62 | 2 | 2016-01-22 | 103.22 | -21.0% |
| SREINFRA | 2015-09-14 | 52.55 | 4 | 2016-02-10 | 51.83 | -1.4% |
| NELCO | 2015-11-30 | 110.10 | 2 | 2016-02-10 | 83.25 | -24.4% |
| GODREJPROP | 2015-10-05 | 318.58 | 2 | 2016-02-11 | 284.19 | -10.8% |
| ZUARIGLOB | 2016-01-11 | 120.10 | 1 | 2016-02-11 | 87.03 | -27.5% |
| PRICOL | 2016-02-01 | 50.17 | 2 | 2016-02-29 | 41.77 | -16.7% |
| HINDZINC | 2016-04-04 | 186.00 | 1 | 2016-04-08 | 158.46 | -14.8% |
| BAJAJHIND | 2016-04-04 | 20.10 | 2 | 2016-05-24 | 17.95 | -10.7% |
| BAJAJELEC | 2016-04-11 | 238.63 | 4 | 2016-06-24 | 213.99 | -10.3% |
| MCLEODRUSS | 2016-03-28 | 198.54 | 3 | 2016-07-19 | 198.74 | +0.1% |
| SOMANYCERA | 2016-01-25 | 400.86 | 4 | 2016-09-21 | 551.10 | +37.5% |
| UJAAS | 2016-01-11 | 24.24 | 4 | 2016-09-29 | 21.90 | -9.7% |
| TATAMETALI | 2016-07-25 | 446.05 | 2 | 2016-09-29 | 366.19 | -17.9% |
| MANAPPURAM | 2016-06-27 | 84.03 | 4 | 2016-10-13 | 89.49 | +6.5% |
| JSWHL | 2016-06-27 | 1,275.63 | 4 | 2016-11-02 | 1,193.20 | -6.5% |
| SUNILHITEC | 2016-10-17 | 408.88 | 2 | 2016-11-08 | 311.57 | -23.8% |
| BANKBEES | 2016-09-26 | 200.99 | 1 | 2016-11-09 | 189.48 | -5.7% |
| TVSSRICHAK | 2016-10-03 | 3,981.06 | 2 | 2016-11-09 | 3,633.84 | -8.7% |
| GOLDBEES | 2016-02-15 | 2,681.07 | 4 | 2016-11-17 | 2,689.64 | +0.3% |
| HDFCMFGETF | 2016-02-15 | 2,805.62 | 4 | 2016-11-18 | 2,718.90 | -3.1% |
| HONDAPOWER | 2016-11-15 | 1,556.00 | 1 | 2016-11-18 | 1,438.87 | -7.5% |
| BALMLAWRIE | 2016-11-21 | 547.18 | 2 | 2016-12-26 | 997.98 | +82.4% |
| STCINDIA | 2017-01-02 | 217.00 | 2 | 2017-01-30 | 187.15 | -13.8% |
| ESSELPACK | 2016-12-05 | 126.41 | 3 | 2017-02-21 | 115.95 | -8.3% |
| MONNETISPA | 2017-02-06 | 37.02 | 3 | 2017-02-27 | 33.06 | -10.7% |
| KOHINOOR | 2017-01-02 | 82.17 | 2 | 2017-03-03 | 77.53 | -5.6% |
| INDIAGLYCO | 2016-06-27 | 116.65 | 4 | 2017-03-20 | 150.48 | +29.0% |
| CENTENKA | 2017-03-27 | 425.94 | 4 | 2017-05-18 | 399.00 | -6.3% |
| NAVNETEDUL | 2016-11-15 | 144.49 | 4 | 2017-05-19 | 156.99 | +8.7% |
| DHANBANK | 2017-03-06 | 36.73 | 4 | 2017-05-22 | 36.62 | -0.3% |
| VIJAYABANK | 2016-11-15 | 60.05 | 4 | 2017-05-23 | 78.29 | +30.4% |
| RAIN | 2017-03-06 | 103.89 | 3 | 2017-05-23 | 96.95 | -6.7% |
| KTKBANK | 2017-03-06 | 160.15 | 4 | 2017-05-23 | 154.85 | -3.3% |
| SUMEETINDS | 2017-05-22 | 38.35 | 1 | 2017-05-24 | 32.82 | -14.4% |
| JKPAPER | 2016-10-17 | 103.89 | 4 | 2017-06-12 | 101.08 | -2.7% |
| VOLTAS | 2017-05-29 | 493.98 | 3 | 2017-06-23 | 456.19 | -7.6% |
| WALCHANNAG | 2017-05-29 | 174.10 | 1 | 2017-06-27 | 163.40 | -6.1% |
| SHAKTIPUMP | 2017-05-22 | 416.29 | 3 | 2017-06-28 | 415.62 | -0.2% |
| GVKPIL | 2017-07-03 | 8.55 | 2 | 2017-07-13 | 7.32 | -14.4% |
| KARURVYSYA | 2017-02-27 | 113.59 | 4 | 2017-08-10 | 128.39 | +13.0% |
| BIL | 2017-05-29 | 599.63 | 2 | 2017-08-10 | 551.00 | -8.1% |
| GRINDWELL | 2017-06-05 | 414.49 | 3 | 2017-08-10 | 389.45 | -6.0% |
| EVERESTIND | 2017-06-27 | 375.99 | 2 | 2017-08-10 | 318.64 | -15.3% |
| VENKEYS | 2017-07-03 | 1,861.21 | 2 | 2017-08-11 | 1,719.30 | -7.6% |
| SEAMECLTD | 2017-07-03 | 160.15 | 2 | 2017-09-11 | 142.50 | -11.0% |
| INSECTICID | 2017-08-14 | 847.44 | 3 | 2017-09-21 | 821.75 | -3.0% |
| SOTL | 2016-11-15 | 739.33 | 4 | 2017-09-25 | 1,192.30 | +61.3% |
| TITAN | 2017-06-12 | 605.92 | 4 | 2017-09-25 | 597.79 | -1.3% |
| BEML | 2017-08-21 | 1,808.45 | 2 | 2017-09-25 | 1,744.63 | -3.5% |
| SPARC | 2017-08-21 | 393.50 | 2 | 2017-09-25 | 362.19 | -8.0% |
| GRAVITA | 2017-08-21 | 143.84 | 4 | 2017-11-08 | 147.96 | +2.9% |
| HIKAL | 2017-09-25 | 232.42 | 2 | 2017-12-15 | 226.62 | -2.5% |
| BFINVEST | 2017-10-03 | 329.42 | 3 | 2017-12-18 | 357.49 | +8.5% |
| SHOPERSTOP | 2017-10-03 | 548.91 | 4 | 2018-01-17 | 513.28 | -6.5% |
| TTKPRESTIG | 2017-06-05 | 7,402.18 | 4 | 2018-01-31 | 7,267.50 | -1.8% |
| GOACARBON | 2017-06-27 | 395.02 | 4 | 2018-01-31 | 913.01 | +131.1% |
| DEN | 2017-10-03 | 113.96 | 4 | 2018-02-01 | 107.61 | -5.6% |
| TRENT | 2017-08-28 | 317.81 | 3 | 2018-02-02 | 302.43 | -4.8% |
| GPIL | 2017-12-26 | 481.87 | 3 | 2018-02-06 | 463.12 | -3.9% |
| JUBILANT | 2018-02-12 | 760.80 | 1 | 2018-03-06 | 647.52 | -14.9% |
| NELCO | 2017-09-25 | 141.30 | 3 | 2018-03-23 | 145.64 | +3.1% |
| NOIDATOLL | 2018-02-12 | 12.61 | 3 | 2018-04-24 | 11.30 | -10.4% |
| VENKEYS | 2018-03-19 | 4,309.40 | 2 | 2018-04-26 | 4,047.95 | -6.1% |
| WHEELS | 2017-11-13 | 2,069.67 | 4 | 2018-05-15 | 1,985.50 | -4.1% |
| EXCELCROP | 2017-11-13 | 2,471.37 | 4 | 2018-05-17 | 3,277.55 | +32.6% |
| ZYDUSWELL | 2018-02-12 | 1,237.67 | 3 | 2018-05-31 | 1,192.25 | -3.7% |
| THOMASCOOK | 2018-04-30 | 287.50 | 2 | 2018-06-04 | 264.43 | -8.0% |
| RML | 2017-07-17 | 692.01 | 4 | 2018-06-05 | 732.64 | +5.9% |
| HIL | 2018-04-30 | 2,183.76 | 2 | 2018-06-05 | 1,939.95 | -11.2% |
| MMFL | 2018-06-18 | 1,374.53 | 2 | 2018-07-18 | 1,197.94 | -12.8% |
| GOLDSHARE | 2018-02-05 | 2,762.91 | 4 | 2018-08-01 | 2,652.16 | -4.0% |
| MAHLIFE | 2018-05-21 | 527.00 | 1 | 2018-08-07 | 484.50 | -8.1% |
| WHEELS | 2018-06-25 | 2,386.07 | 2 | 2018-08-08 | 2,006.50 | -15.9% |
| BAJFINANCE | 2018-07-23 | 2,836.18 | 4 | 2018-09-04 | 2,683.56 | -5.4% |
| GLOBUSSPR | 2018-09-10 | 186.35 | 1 | 2018-09-11 | 166.34 | -10.7% |
| ASTRAZEN | 2018-06-18 | 1,253.70 | 4 | 2018-09-12 | 1,345.20 | +7.3% |
| ABBOTINDIA | 2018-05-21 | 7,355.64 | 4 | 2018-09-21 | 7,657.95 | +4.1% |
| PEL | 2018-08-06 | 2,811.46 | 2 | 2018-09-21 | 2,627.89 | -6.5% |
| EVERESTIND | 2018-08-13 | 552.49 | 2 | 2018-09-21 | 510.10 | -7.7% |
| SUVEN | 2018-09-17 | 310.80 | 1 | 2018-09-21 | 244.67 | -21.3% |
| MPHASIS | 2018-02-05 | 1,018.02 | 4 | 2018-09-25 | 1,173.72 | +15.3% |
| BBL | 2018-09-10 | 1,500.15 | 1 | 2018-09-27 | 1,217.66 | -18.8% |
| MUTHOOTFIN | 2018-09-10 | 460.40 | 2 | 2018-09-27 | 412.35 | -10.4% |
| GUJFLUORO | 2018-09-24 | 854.00 | 1 | 2018-09-28 | 775.25 | -9.2% |
| JSWHL | 2018-09-17 | 2,358.85 | 1 | 2018-10-09 | 2,044.64 | -13.3% |
| GODFRYPHLP | 2018-12-03 | 928.20 | 2 | 2018-12-26 | 812.30 | -12.5% |
| BEML | 2018-12-24 | 893.05 | 2 | 2019-01-28 | 809.88 | -9.3% |
| SOMANYCERA | 2019-01-14 | 369.90 | 1 | 2019-01-28 | 335.82 | -9.2% |
| KESORAMIND | 2018-12-03 | 85.00 | 1 | 2019-01-29 | 71.39 | -16.0% |
| HATHWAY | 2018-10-22 | 30.43 | 2 | 2019-02-19 | 26.93 | -11.5% |
| BAJAJHIND | 2018-10-15 | 9.98 | 2 | 2019-03-20 | 7.69 | -22.9% |
| DHAMPURSUG | 2019-03-05 | 237.23 | 2 | 2019-03-20 | 211.42 | -10.9% |
| YESBANK | 2019-02-18 | 246.96 | 3 | 2019-04-22 | 245.34 | -0.7% |
| JUSTDIAL | 2019-03-25 | 613.48 | 2 | 2019-04-22 | 565.25 | -7.9% |
| INFRATEL | 2019-02-11 | 319.80 | 2 | 2019-04-25 | 277.35 | -13.3% |
| MTEDUCARE | 2019-04-30 | 85.85 | 1 | 2019-05-03 | 73.96 | -13.8% |
| SKFINDIA | 2019-01-14 | 2,015.13 | 3 | 2019-05-08 | 1,891.83 | -6.1% |
| IBREALEST | 2019-04-30 | 125.40 | 1 | 2019-05-14 | 91.19 | -27.3% |
| FLFL | 2019-04-30 | 483.00 | 1 | 2019-05-16 | 434.20 | -10.1% |
| MTEDUCARE | 2019-05-13 | 94.20 | 1 | 2019-05-17 | 73.96 | -21.5% |
| SPECIALITY | 2019-01-21 | 102.23 | 2 | 2019-06-10 | 78.76 | -23.0% |
| RUCHISOYA | 2019-05-06 | 9.10 | 1 | 2019-06-25 | 5.61 | -38.4% |
| ONGC | 2019-04-30 | 171.00 | 3 | 2019-07-01 | 160.36 | -6.2% |
| MAHSCOOTER | 2019-06-03 | 4,477.12 | 3 | 2019-07-08 | 4,157.82 | -7.1% |
| BANKBEES | 2018-12-17 | 281.62 | 4 | 2019-07-22 | 295.55 | +4.9% |
| GRUH | 2019-05-27 | 313.00 | 1 | 2019-07-23 | 265.98 | -15.0% |
| TRENT | 2019-07-01 | 453.10 | 2 | 2019-07-30 | 393.30 | -13.2% |
| INOXLEISUR | 2019-05-27 | 336.18 | 2 | 2019-07-31 | 291.23 | -13.4% |
| TRENT | 2019-08-26 | 474.35 | 2 | 2019-09-17 | 439.04 | -7.4% |
| JKPAPER | 2019-09-23 | 137.85 | 1 | 2019-10-07 | 118.84 | -13.8% |
| JBMA | 2019-10-14 | 230.01 | 2 | 2019-10-23 | 207.67 | -9.7% |
| TVTODAY | 2019-10-29 | 333.00 | 1 | 2019-12-02 | 275.74 | -17.2% |
| HEIDELBERG | 2019-05-27 | 199.44 | 3 | 2019-12-09 | 177.65 | -10.9% |
| GOLDBEES | 2019-08-13 | 3,370.75 | 3 | 2019-12-19 | 3,189.29 | -5.4% |
| ASTRAZEN | 2019-12-09 | 2,195.32 | 2 | 2020-01-06 | 2,006.40 | -8.6% |
| BERGEPAINT | 2019-08-13 | 465.10 | 4 | 2020-01-08 | 484.17 | +4.1% |
| GPIL | 2019-12-23 | 241.99 | 3 | 2020-01-22 | 223.25 | -7.7% |
| ASAHISONG | 2020-01-13 | 160.18 | 2 | 2020-01-30 | 148.58 | -7.2% |
| INDRAMEDCO | 2020-01-13 | 45.28 | 2 | 2020-02-27 | 40.23 | -11.1% |
| INDOCO | 2020-01-27 | 221.00 | 1 | 2020-03-02 | 199.59 | -9.7% |
| ATULAUTO | 2020-01-27 | 255.58 | 2 | 2020-03-03 | 217.66 | -14.8% |
| HARITASEAT | 2020-01-13 | 476.39 | 2 | 2020-03-12 | 404.35 | -15.1% |
| GRANULES | 2020-01-27 | 169.79 | 3 | 2020-03-12 | 149.58 | -11.9% |
| HDFCMFGETF | 2019-07-08 | 3,415.56 | 4 | 2020-03-13 | 3,540.65 | +3.7% |
| LAOPALA | 2020-02-03 | 186.25 | 2 | 2020-03-13 | 165.00 | -11.4% |
| INDOCO | 2020-03-09 | 228.20 | 1 | 2020-03-13 | 164.08 | -28.1% |
| KOTAKGOLD | 2019-07-15 | 333.42 | 4 | 2020-03-17 | 352.69 | +5.8% |
| GOLDSHARE | 2019-08-13 | 3,475.25 | 4 | 2020-03-17 | 3,562.50 | +2.5% |
| DEEPAKNTR | 2020-03-09 | 508.80 | 1 | 2020-03-19 | 356.25 | -30.0% |
| AKZOINDIA | 2020-02-03 | 2,029.25 | 1 | 2020-03-25 | 1,787.63 | -11.9% |

## Engine B — the complete trade blotter

*Buys, pyramid injections, sells and tax settlements; every stop raise and refused signal is in `_longrun_events_2015-03-01_to_2020-03-31.csv`, and engine A's full ledger in `_longrun_events_2015-03-01_to_2020-03-31_no_doubling.csv`.*

```
2015-03-09  ECLERX      BUY ₹9.98 at ₹1,550.00 (fresh Friday signal — BUY: 3.25× weekly, month 2.52×, ladder rising; stop ₹1,171.35; charges ₹0.01)
2015-03-09  GEOMETRIC   BUY ₹10.00 at ₹157.60 (fresh Friday signal — BUY: 6.64× weekly, month 1.62×, ladder rising; stop ₹130.15; charges ₹0.01)
2015-03-09  HCC         BUY ₹10.03 at ₹36.45 (fresh Friday signal — BUY: 3.01× weekly, month 1.69×, ladder rising; stop ₹28.57; charges ₹0.01)
2015-03-09  JBMA        BUY ₹9.99 at ₹239.80 (fresh Friday signal — BUY: 2.78× weekly, month 2.63×, ladder rising; stop ₹188.60; charges ₹0.01)
2015-03-09  RAMCOSYS    BUY ₹9.98 at ₹694.70 (fresh Friday signal — BUY: 2.12× weekly, month 5.40×, ladder rising; stop ₹532.00; charges ₹0.01)
2015-03-09  SMLISUZU    BUY ₹10.03 at ₹1,200.00 (fresh Friday signal — BUY: 2.25× weekly, month 1.55×, ladder rising; stop ₹949.52; charges ₹0.01)
2015-03-09  SOMANYCERA  BUY ₹10.01 at ₹405.00 (fresh Friday signal — BUY: 6.10× weekly, month 1.53×, ladder rising; stop ₹336.63; charges ₹0.01)
2015-03-09  SPARC       BUY ₹10.09 at ₹476.00 (fresh Friday signal — BUY: 1.67× weekly, month 2.23×, ladder rising; stop ₹295.36; charges ₹0.01)
2015-03-09  TWL         BUY ₹9.96 at ₹728.70 (fresh Friday signal — BUY: 2.00× weekly, month 9.35×, ladder rising; stop ₹479.92; charges ₹0.01)
2015-03-16  AARTIIND    BUY ₹9.93 at ₹360.80 (fresh Friday signal — BUY: 5.16× weekly, month 1.97×, ladder rising; stop ₹270.94; charges ₹0.01)
2015-03-16  GEOMETRIC   PYRAMID BUY ₹10.69 at ₹168.65 (box jump — doubling the stake with NEW capital; stop stays ₹145.35; charges ₹0.01)
2015-03-16  JBMA        PYRAMID BUY ₹9.86 at ₹237.00 (box jump — doubling the stake with NEW capital; stop stays ₹222.30; charges ₹0.01)
2015-03-23  ECLERX      PYRAMID BUY ₹10.09 at ₹1,569.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,320.70; charges ₹0.01)
2015-03-23  GEOMETRIC   PYRAMID BUY ₹22.17 at ₹175.00 (box jump — doubling the stake with NEW capital; stop stays ₹158.22; charges ₹0.03)
2015-03-23  JBMA        SELL ₹18.48 at stop ₹222.30 (-6.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-03-23  RAMCOSYS    PYRAMID BUY ₹9.82 at ₹684.70 (box jump — doubling the stake with NEW capital; stop stays ₹597.69; charges ₹0.01)
2015-03-23  SOMANYCERA  PYRAMID BUY ₹9.19 at ₹372.00 (box jump — doubling the stake with NEW capital; stop stays ₹341.63; charges ₹0.01)
2015-03-30  DYNAMATECH  BUY ₹16.69 at ₹3,843.00 (fresh Friday signal — BUY: 10.44× weekly, month 3.95×, ladder rising; stop ₹3,081.75; charges ₹0.02)
2015-04-01  TAX         FY2015 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹1.34 / LT ₹0.00)
2015-04-06  AARTIIND    PYRAMID BUY ₹9.42 at ₹342.95 (box jump — doubling the stake with NEW capital; stop stays ₹300.44; charges ₹0.01)
2015-04-06  SMLISUZU    PYRAMID BUY ₹10.28 at ₹1,232.00 (box jump — doubling the stake with NEW capital; stop stays ₹983.70; charges ₹0.01)
2015-04-06  SPARC       PYRAMID BUY ₹10.75 at ₹507.45 (box jump — doubling the stake with NEW capital; stop stays ₹426.12; charges ₹0.01)
2015-04-21  SPARC       SELL ₹18.02 at stop ₹426.12 (-13.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-04-22  DYNAMATECH  SELL ₹13.36 at stop ₹3,081.75 (-19.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2015-04-22  GEOMETRIC   SELL ₹40.02 at stop ₹158.22 (-6.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2015-04-23  TWL         SELL ₹6.55 at stop ₹479.92 (-34.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2015-04-27  AARTIIND    SELL ₹16.48 at stop ₹300.44 (-14.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-04-27  HCC         PYRAMID BUY ₹9.04 at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹31.21; charges ₹0.01)
2015-04-27  HCC         SELL ₹17.12 at stop ₹31.21 (-10.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-04-27  PETRONENGG  BUY ₹21.01 at ₹250.10 (fresh Friday signal — BUY: 5.67× weekly, month 3.79×, ladder rising; stop ₹207.41; charges ₹0.02)
2015-04-27  RAMCOSYS    SELL ₹17.12 at stop ₹597.69 (-13.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-04-27  SOMANYCERA  PYRAMID BUY ₹19.82 at ₹401.60 (box jump — doubling the stake with NEW capital; stop stays ₹418.24; charges ₹0.02)
2015-04-27  SOMANYCERA  SELL ₹41.22 at stop ₹418.24 (+5.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2015-05-04  VADILALIND  BUY ₹21.57 at ₹487.00 (fresh Friday signal — BUY: 10.46× weekly, month 4.23×, ladder rising; stop ₹323.00; charges ₹0.03)
2015-05-11  ABIRLANUVO  BUY ₹23.75 at ₹945.00 (fresh Friday signal — BUY: 5.18× weekly, month 1.67×, ladder rising; stop ₹713.90; charges ₹0.03)
2015-05-11  VADILALIND  PYRAMID BUY ₹22.34 at ₹505.00 (box jump — doubling the stake with NEW capital; stop stays ₹451.91; charges ₹0.03)
2015-05-18  MANINDS     BUY ₹23.77 at ₹70.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 3.68×, ladder rising; stop ₹54.94; charges ₹0.03)
2015-05-18  NILKAMAL    BUY ₹23.69 at ₹524.95 (fresh Friday signal — BUY: 5.24× weekly, month 2.21×, ladder rising; stop ₹413.10; charges ₹0.03)
2015-05-18  WELSPUNIND  BUY ₹23.79 at ₹42.88 (fresh Friday signal — BUY: 1.85× weekly, month 1.82×, ladder rising; stop ₹37.14; charges ₹0.03)
2015-05-25  ABIRLANUVO  PYRAMID BUY ₹23.01 at ₹916.77 (box jump — doubling the stake with NEW capital; stop stays ₹850.92; charges ₹0.03)
2015-05-25  VADILALIND  PYRAMID BUY ₹43.85 at ₹496.00 (box jump — doubling the stake with NEW capital; stop stays ₹463.60; charges ₹0.05)
2015-06-01  INFRATEL    BUY ₹32.81 at ₹462.10 (fresh Friday signal — BUY: 5.86× weekly, month 3.68×, ladder rising; stop ₹400.24; charges ₹0.04)
2015-06-01  WELSPUNIND  PYRAMID BUY ₹25.21 at ₹45.50 (box jump — doubling the stake with NEW capital; stop stays ₹40.67; charges ₹0.03)
2015-06-03  ABIRLANUVO  SELL ₹42.65 at stop ₹850.92 (-8.6%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2015-06-03  PETRONENGG  SELL ₹17.39 at stop ₹207.41 (-17.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2015-06-08  TORNTPHARM  BUY ₹32.00 at ₹1,244.00 (fresh Friday signal — ACCUMULATE: 1.79× weekly, month 1.51×, ladder rising; stop ₹1,107.70; charges ₹0.04)
2015-06-09  WELSPUNIND  SELL ₹44.99 at stop ₹40.67 (-8.0%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2015-06-15  CHENNPETRO  BUY ₹31.34 at ₹135.25 (fresh Friday signal — BUY: 3.80× weekly, month 3.78×, ladder rising; stop ₹94.03; charges ₹0.04)
2015-06-15  DISHTV      BUY ₹31.34 at ₹107.40 (fresh Friday signal — BUY: 3.53× weekly, month 2.47×, ladder rising; stop ₹90.11; charges ₹0.04)
2015-06-22  MANINDS     PYRAMID BUY ₹24.87 at ₹73.35 (box jump — doubling the stake with NEW capital; stop stays ₹67.54; charges ₹0.03)
2015-06-22  NILKAMAL    PYRAMID BUY ₹24.07 at ₹534.00 (box jump — doubling the stake with NEW capital; stop stays ₹479.89; charges ₹0.03)
2015-06-22  SMLISUZU    PYRAMID BUY ₹18.81 at ₹1,127.95 (box jump — doubling the stake with NEW capital; stop stays ₹997.50; charges ₹0.02)
2015-06-29  TORNTPHARM  PYRAMID BUY ₹34.24 at ₹1,332.95 (box jump — doubling the stake with NEW capital; stop stays ₹1,249.25; charges ₹0.04)
2015-07-06  CHENNPETRO  PYRAMID BUY ₹37.85 at ₹163.50 (box jump — doubling the stake with NEW capital; stop stays ₹141.50; charges ₹0.04)
2015-07-06  DISHTV      PYRAMID BUY ₹30.61 at ₹105.00 (box jump — doubling the stake with NEW capital; stop stays ₹93.74; charges ₹0.04)
2015-07-06  MANINDS     PYRAMID BUY ₹59.58 at ₹87.90 (box jump — doubling the stake with NEW capital; stop stays ₹81.13; charges ₹0.07)
2015-07-06  SMLISUZU    PYRAMID BUY ₹36.84 at ₹1,105.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,053.55; charges ₹0.04)
2015-07-20  NILKAMAL    PYRAMID BUY ₹65.37 at ₹725.50 (box jump — doubling the stake with NEW capital; stop stays ₹547.82; charges ₹0.08)
2015-07-20  VADILALIND  PYRAMID BUY ₹126.35 at ₹714.95 (box jump — doubling the stake with NEW capital; stop stays ₹637.45; charges ₹0.15)
2015-08-03  CHENNPETRO  PYRAMID BUY ₹88.93 at ₹192.20 (box jump — doubling the stake with NEW capital; stop stays ₹161.50; charges ₹0.11)
2015-08-03  MANINDS     PYRAMID BUY ₹154.45 at ₹114.00 (box jump — doubling the stake with NEW capital; stop stays ₹95.77; charges ₹0.18)
2015-08-10  DISHTV      PYRAMID BUY ₹68.92 at ₹118.30 (box jump — doubling the stake with NEW capital; stop stays ₹102.60; charges ₹0.08)
2015-08-10  NILKAMAL    PYRAMID BUY ₹210.00 at ₹1,165.95 (box jump — doubling the stake with NEW capital; stop stays ₹730.69; charges ₹0.25)
2015-08-10  TORNTPHARM  PYRAMID BUY ₹76.56 at ₹1,491.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,330.00; charges ₹0.09)
2015-08-13  VADILALIND  SELL ₹252.81 at stop ₹716.44 (+18.3%, charges ₹0.26) — the cash goes back to work at the next Friday screen
2015-08-17  GHCL        BUY ₹162.19 at ₹120.50 (fresh Friday signal — BUY: 6.38× weekly, month 4.31×, ladder rising; stop ₹60.81; charges ₹0.19)
2015-08-17  JUBILANT    BUY ₹102.26 at ₹277.04 (fresh Friday signal — BUY: 4.47× weekly, month 4.36×, ladder rising; stop ₹148.58; charges ₹0.12)
2015-08-19  INFRATEL    SELL ₹28.36 at stop ₹400.24 (-13.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2015-08-24  CHENNPETRO  PYRAMID BUY ₹222.88 at ₹241.00 (box jump — doubling the stake with NEW capital; stop stays ₹218.07; charges ₹0.26)
2015-08-24  CHENNPETRO  SELL ₹402.68 at stop ₹218.07 (+5.9%, charges ₹0.42) — the cash goes back to work at the next Friday screen
2015-08-24  DISHTV      SELL ₹119.36 at stop ₹102.60 (-8.6%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2015-08-24  ECLERX      PYRAMID BUY ₹21.60 at ₹1,680.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,531.40; charges ₹0.03)
2015-08-24  GHCL        PYRAMID BUY ₹159.84 at ₹118.90 (box jump — doubling the stake with NEW capital; stop stays ₹100.88; charges ₹0.19)
2015-08-24  MANINDS     SELL ₹259.08 at stop ₹95.77 (-1.1%, charges ₹0.27) — the cash goes back to work at the next Friday screen
2015-08-24  NILKAMAL    SELL ₹333.42 at stop ₹927.12 (+3.4%, charges ₹0.35) — the cash goes back to work at the next Friday screen
2015-08-24  SMLISUZU    SELL ₹73.91 at stop ₹1,110.20 (-2.5%, charges ₹0.08) — the cash goes back to work at the next Friday screen
2015-08-31  JUBILANT    PYRAMID BUY ₹103.23 at ₹280.00 (box jump — doubling the stake with NEW capital; stop stays ₹218.37; charges ₹0.12)
2015-09-07  ABBOTINDIA  BUY ₹190.25 at ₹5,269.00 (fresh Friday signal — BUY: 5.86× weekly, month 1.67×, ladder rising; stop ₹4,181.09; charges ₹0.23)
2015-09-07  JINDALPOLY  BUY ₹190.51 at ₹376.90 (fresh Friday signal — ACCUMULATE: 1.73× weekly, month 2.65×, ladder rising; stop ₹305.60; charges ₹0.23)
2015-09-08  JUBILANT    SELL ₹160.76 at stop ₹218.37 (-21.6%, charges ₹0.17) — the cash goes back to work at the next Friday screen
2015-09-14  CEATLTD     BUY ₹191.37 at ₹1,219.00 (fresh Friday signal — BUY: 1.70× weekly, month 1.85×, ladder rising; stop ₹857.01; charges ₹0.23)
2015-09-14  SREINFRA    BUY ₹191.16 at ₹46.00 (fresh Friday signal — ACCUMULATE: 1.51× weekly, month 1.57×, ladder rising; stop ₹32.22; charges ₹0.23)
2015-09-28  ABBOTINDIA  PYRAMID BUY ₹209.90 at ₹5,819.95 (box jump — doubling the stake with NEW capital; stop stays ₹5,365.17; charges ₹0.25)
2015-09-28  CEATLTD     PYRAMID BUY ₹200.71 at ₹1,280.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,123.90; charges ₹0.24)
2015-09-28  FDC         BUY ₹236.94 at ₹240.00 (fresh Friday signal — BUY: 5.35× weekly, month 2.52×, ladder rising; stop ₹165.06; charges ₹0.28)
2015-10-05  GODREJPROP  BUY ₹133.59 at ₹321.00 (fresh Friday signal — ACCUMULATE: 1.92× weekly, month 1.55×, ladder rising; stop ₹243.45; charges ₹0.16)
2015-10-05  UNICHEMLAB  BUY ₹243.76 at ₹301.50 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 2.98×, ladder rising; stop ₹233.99; charges ₹0.29)
2015-10-12  JINDALPOLY  PYRAMID BUY ₹242.42 at ₹480.15 (box jump — doubling the stake with NEW capital; stop stays ₹402.90; charges ₹0.29)
2015-10-19  CEATLTD     PYRAMID BUY ₹394.44 at ₹1,258.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,131.45; charges ₹0.47)
2015-10-19  ECLERX      PYRAMID BUY ₹46.70 at ₹1,817.45 (box jump — doubling the stake with NEW capital; stop stays ₹1,548.50; charges ₹0.06)
2015-10-19  TORNTPHARM  PYRAMID BUY ₹157.33 at ₹1,532.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,426.04; charges ₹0.19)
2015-10-26  FDC         PYRAMID BUY ₹259.39 at ₹263.05 (box jump — doubling the stake with NEW capital; stop stays ₹232.89; charges ₹0.31)
2015-10-26  JINDALPOLY  PYRAMID BUY ₹546.86 at ₹541.90 (box jump — doubling the stake with NEW capital; stop stays ₹451.25; charges ₹0.65)
2015-10-29  CEATLTD     SELL ₹708.09 at stop ₹1,131.45 (-9.8%, charges ₹0.73) — the cash goes back to work at the next Friday screen
2015-11-02  FDC         SELL ₹458.55 at stop ₹232.89 (-7.4%, charges ₹0.48) — the cash goes back to work at the next Friday screen
2015-11-02  JINDALPOLY  PYRAMID BUY ₹1,113.55 at ₹552.05 (box jump — doubling the stake with NEW capital; stop stays ₹494.38; charges ₹1.32)
2015-11-02  UCOBANK     BUY ₹510.68 at ₹50.30 (fresh Friday signal — BUY: 4.92× weekly, month 2.00×, ladder rising; stop ₹45.79; charges ₹0.61)
2015-11-06  ABBOTINDIA  SELL ₹386.36 at stop ₹5,365.17 (-3.2%, charges ₹0.40) — the cash goes back to work at the next Friday screen
2015-11-09  GHCL        PYRAMID BUY ₹362.90 at ₹135.05 (box jump — doubling the stake with NEW capital; stop stays ₹129.53; charges ₹0.43)
2015-11-09  KOHINOOR    BUY ₹534.60 at ₹45.00 (fresh Friday signal — BUY: 7.56× weekly, month 2.53×, ladder rising; stop ₹40.84; charges ₹0.63)
2015-11-09  NILKAMAL    BUY ₹507.72 at ₹970.00 (fresh Friday signal — BUY: 5.23× weekly, month 1.58×, ladder rising; stop ₹902.50; charges ₹0.60)
2015-11-09  UCOBANK     SELL ₹463.86 at stop ₹45.79 (-9.0%, charges ₹0.48) — the cash goes back to work at the next Friday screen
2015-11-16  GODREJPROP  PYRAMID BUY ₹131.41 at ₹316.15 (box jump — doubling the stake with NEW capital; stop stays ₹284.19; charges ₹0.16)
2015-11-16  RADICO      BUY ₹463.86 at ₹121.80 (fresh Friday signal — BUY: 3.01× weekly, month 2.77×, ladder rising; stop ₹93.88; charges ₹0.55)
2015-11-16  SREINFRA    PYRAMID BUY ₹172.25 at ₹41.50 (box jump — doubling the stake with NEW capital; stop stays ₹36.95; charges ₹0.20)
2015-11-23  UNICHEMLAB  PYRAMID BUY ₹232.24 at ₹287.60 (box jump — doubling the stake with NEW capital; stop stays ₹235.30; charges ₹0.28)
2015-11-26  JINDALPOLY  SELL ₹1,991.20 at stop ₹494.38 (-4.7%, charges ₹2.07) — the cash goes back to work at the next Friday screen
2015-11-30  GLOBUSSPR   BUY ₹583.03 at ₹76.50 (fresh Friday signal — BUY: 29.71× weekly, month 8.18×, ladder rising; stop ₹48.23; charges ₹0.69)
2015-11-30  NELCO       BUY ₹580.11 at ₹113.75 (fresh Friday signal — BUY: 11.41× weekly, month 3.77×, ladder rising; stop ₹62.61; charges ₹0.69)
2015-11-30  RPGLIFE     BUY ₹579.51 at ₹307.60 (fresh Friday signal — BUY: 9.91× weekly, month 2.24×, ladder rising; stop ₹168.66; charges ₹0.69)
2015-11-30  TORNTPHARM  SELL ₹292.25 at stop ₹1,426.04 (-2.4%, charges ₹0.30) — the cash goes back to work at the next Friday screen
2015-12-07  EIHOTEL     BUY ₹540.80 at ₹127.10 (fresh Friday signal — BUY: 18.40× weekly, month 2.70×, ladder rising; stop ₹101.65; charges ₹0.64)
2015-12-07  GLOBUSSPR   PYRAMID BUY ₹619.64 at ₹81.40 (box jump — doubling the stake with NEW capital; stop stays ₹65.41; charges ₹0.73)
2015-12-07  KOHINOOR    PYRAMID BUY ₹672.80 at ₹56.70 (box jump — doubling the stake with NEW capital; stop stays ₹49.50; charges ₹0.80)
2015-12-07  RADICO      PYRAMID BUY ₹416.14 at ₹109.40 (box jump — doubling the stake with NEW capital; stop stays ₹100.09; charges ₹0.49)
2015-12-09  GHCL        SELL ₹694.99 at stop ₹129.53 (+1.7%, charges ₹0.72) — the cash goes back to work at the next Friday screen
2015-12-09  RADICO      SELL ₹760.21 at stop ₹100.09 (-13.4%, charges ₹0.79) — the cash goes back to work at the next Friday screen
2015-12-14  AJMERA      BUY ₹693.12 at ₹124.80 (fresh Friday signal — BUY: 3.63× weekly, month 2.71×, ladder rising; stop ₹86.59; charges ₹0.82)
2015-12-14  EIHOTEL     PYRAMID BUY ₹515.72 at ₹121.35 (box jump — doubling the stake with NEW capital; stop stays ₹113.05; charges ₹0.61)
2015-12-14  KOHINOOR    SELL ₹1,172.81 at stop ₹49.50 (-2.6%, charges ₹1.22) — the cash goes back to work at the next Friday screen
2015-12-14  SHARONBIO   BUY ₹762.09 at ₹30.80 (fresh Friday signal — BUY: 12.91× weekly, month 1.78×, ladder rising; stop ₹11.82; charges ₹0.90)
2015-12-17  ECLERX      SELL ₹83.10 at stop ₹1,619.75 (-5.7%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2015-12-21  AJMERA      PYRAMID BUY ₹756.87 at ₹136.44 (box jump — doubling the stake with NEW capital; stop stays ₹103.22; charges ₹0.90)
2015-12-21  NELCO       PYRAMID BUY ₹542.24 at ₹106.45 (box jump — doubling the stake with NEW capital; stop stays ₹83.25; charges ₹0.64)
2015-12-21  RPGLIFE     PYRAMID BUY ₹562.54 at ₹298.95 (box jump — doubling the stake with NEW capital; stop stays ₹247.38; charges ₹0.67)
2015-12-21  SHARONBIO   PYRAMID BUY ₹741.41 at ₹30.00 (box jump — doubling the stake with NEW capital; stop stays ₹26.93; charges ₹0.88)
2015-12-21  SREINFRA    PYRAMID BUY ₹368.78 at ₹44.45 (box jump — doubling the stake with NEW capital; stop stays ₹38.36; charges ₹0.44)
2015-12-21  TV18BRDCST  BUY ₹1,079.22 at ₹42.80 (fresh Friday signal — BUY: 3.95× weekly, month 2.19×, ladder rising; stop ₹33.68; charges ₹1.28)
2016-01-04  TV18BRDCST  PYRAMID BUY ₹1,197.57 at ₹47.55 (box jump — doubling the stake with NEW capital; stop stays ₹44.46; charges ₹1.42)
2016-01-07  TV18BRDCST  SELL ₹2,235.84 at stop ₹44.46 (-1.6%, charges ₹2.32) — the cash goes back to work at the next Friday screen
2016-01-11  NILKAMAL    PYRAMID BUY ₹744.36 at ₹1,423.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,174.87; charges ₹0.88)
2016-01-11  UJAAS       BUY ₹1,096.21 at ₹29.35 (fresh Friday signal — BUY: 8.35× weekly, month 3.66×, ladder rising; stop ₹17.68; charges ₹1.30)
2016-01-11  ZUARIGLOB   BUY ₹1,316.33 at ₹120.10 (fresh Friday signal — BUY: 12.59× weekly, month 6.85×, ladder rising; stop ₹87.03; charges ₹1.56)
2016-01-12  SHARONBIO   SELL ₹1,328.92 at stop ₹26.93 (-11.4%, charges ₹1.38) — the cash goes back to work at the next Friday screen
2016-01-13  UNICHEMLAB  SELL ₹379.40 at stop ₹235.30 (-20.1%, charges ₹0.39) — the cash goes back to work at the next Friday screen
2016-01-18  EIHOTEL     SELL ₹959.33 at stop ₹113.05 (-9.0%, charges ₹1.00) — the cash goes back to work at the next Friday screen
2016-01-18  GLOBUSSPR   SELL ₹994.22 at stop ₹65.41 (-17.1%, charges ₹1.03) — the cash goes back to work at the next Friday screen
2016-01-18  NILKAMAL    SELL ₹1,226.45 at stop ₹1,174.87 (-1.8%, charges ₹1.27) — the cash goes back to work at the next Friday screen
2016-01-18  RPGLIFE     SELL ₹929.49 at stop ₹247.38 (-18.4%, charges ₹0.96) — the cash goes back to work at the next Friday screen
2016-01-22  AJMERA      SELL ₹1,143.31 at stop ₹103.22 (-21.0%, charges ₹1.19) — the cash goes back to work at the next Friday screen
2016-01-25  SOMANYCERA  BUY ₹1,310.75 at ₹377.00 (fresh Friday signal — ACCUMULATE: 1.72× weekly, month 2.16×, ladder rising; stop ₹317.01; charges ₹1.55)
2016-01-25  SREINFRA    PYRAMID BUY ₹1,011.56 at ₹61.00 (box jump — doubling the stake with NEW capital; stop stays ₹51.83; charges ₹1.20)
2016-01-25  UJAAS       PYRAMID BUY ₹983.00 at ₹26.35 (box jump — doubling the stake with NEW capital; stop stays ₹18.56; charges ₹1.16)
2016-02-01  PRICOL      BUY ₹1,333.83 at ₹47.90 (fresh Friday signal — BUY: 2.18× weekly, month 2.31×, ladder rising; stop ₹35.02; charges ₹1.58)
2016-02-10  NELCO       SELL ₹846.74 at stop ₹83.25 (-24.4%, charges ₹0.88) — the cash goes back to work at the next Friday screen
2016-02-10  SREINFRA    SELL ₹1,716.20 at stop ₹51.83 (-1.4%, charges ₹1.78) — the cash goes back to work at the next Friday screen
2016-02-11  GODREJPROP  SELL ₹235.87 at stop ₹284.19 (-10.8%, charges ₹0.24) — the cash goes back to work at the next Friday screen
2016-02-11  ZUARIGLOB   SELL ₹951.76 at stop ₹87.03 (-27.5%, charges ₹0.99) — the cash goes back to work at the next Friday screen
2016-02-15  GOLDBEES    BUY ₹1,251.61 at ₹2,614.80 (fresh Friday signal — BUY: 3.06× weekly, month 1.75×, ladder rising; stop ₹2,285.70; charges ₹1.48)
2016-02-15  HDFCMFGETF  BUY ₹1,251.72 at ₹2,652.00 (fresh Friday signal — BUY: 2.25× weekly, month 1.69×, ladder rising; stop ₹2,357.00; charges ₹1.48)
2016-02-15  RELGOLD     BUY ₹1,250.16 at ₹2,443.80 (fresh Friday signal — BUY: 2.86× weekly, month 1.79×, ladder rising; stop ₹2,139.40; charges ₹1.48)
2016-02-22  GOLDBEES    PYRAMID BUY ₹1,248.79 at ₹2,612.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,424.21; charges ₹1.48)
2016-02-22  HDFCMFGETF  PYRAMID BUY ₹1,259.43 at ₹2,671.50 (box jump — doubling the stake with NEW capital; stop stays ₹2,484.30; charges ₹1.49)
2016-02-22  PRICOL      PYRAMID BUY ₹1,458.80 at ₹52.45 (box jump — doubling the stake with NEW capital; stop stays ₹41.77; charges ₹1.73)
2016-02-22  RELGOLD     PYRAMID BUY ₹1,290.19 at ₹2,525.05 (box jump — doubling the stake with NEW capital; stop stays ₹2,321.61; charges ₹1.53)
2016-02-22  UJAAS       PYRAMID BUY ₹1,789.60 at ₹24.00 (box jump — doubling the stake with NEW capital; stop stays ₹20.02; charges ₹2.12)
2016-02-29  PRICOL      SELL ₹2,319.73 at stop ₹41.77 (-16.7%, charges ₹2.41) — the cash goes back to work at the next Friday screen
2016-03-14  GOLDBEES    PYRAMID BUY ₹2,541.02 at ₹2,659.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,476.18; charges ₹3.01)
2016-03-21  RELGOLD     PYRAMID BUY ₹2,628.79 at ₹2,573.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,421.55; charges ₹3.11)
2016-03-21  SOMANYCERA  PYRAMID BUY ₹1,305.55 at ₹375.95 (box jump — doubling the stake with NEW capital; stop stays ₹337.25; charges ₹1.55)
2016-03-28  MCLEODRUSS  BUY ₹2,492.56 at ₹184.00 (fresh Friday signal — ACCUMULATE: 3.85× weekly, month 1.53×, ladder rising; stop ₹166.63; charges ₹2.95)
2016-04-01  TAX         FY2016 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹2,738.21 / LT ₹0.00)
2016-04-04  BAJAJHIND   BUY ₹1,613.14 at ₹20.60 (fresh Friday signal — BUY: 1.60× weekly, month 2.27×, ladder rising; stop ₹17.15; charges ₹1.91)
2016-04-04  HINDZINC    BUY ₹2,527.64 at ₹186.00 (fresh Friday signal — BUY: 5.26× weekly, month 2.44×, ladder rising; stop ₹158.46; charges ₹2.99)
2016-04-08  HINDZINC    SELL ₹2,148.61 at stop ₹158.46 (-14.8%, charges ₹2.23) — the cash goes back to work at the next Friday screen
2016-04-11  BAJAJELEC   BUY ₹2,148.61 at ₹214.50 (fresh Friday signal — BUY: 3.17× weekly, month 1.60×, ladder rising; stop ₹175.84; charges ₹2.55)
2016-04-11  SOMANYCERA  PYRAMID BUY ₹2,720.97 at ₹392.00 (box jump — doubling the stake with NEW capital; stop stays ₹351.50; charges ₹3.22)
2016-04-25  BAJAJELEC   PYRAMID BUY ₹2,186.08 at ₹218.50 (box jump — doubling the stake with NEW capital; stop stays ₹198.55; charges ₹2.59)
2016-04-25  BAJAJHIND   PYRAMID BUY ₹1,533.01 at ₹19.60 (box jump — doubling the stake with NEW capital; stop stays ₹17.95; charges ₹1.82)
2016-04-25  RELGOLD     PYRAMID BUY ₹5,246.41 at ₹2,570.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,423.45; charges ₹6.22)
2016-05-02  GOLDBEES    PYRAMID BUY ₹5,207.00 at ₹2,726.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,508.05; charges ₹6.17)
2016-05-09  SOMANYCERA  PYRAMID BUY ₹5,792.50 at ₹417.50 (box jump — doubling the stake with NEW capital; stop stays ₹382.85; charges ₹6.86)
2016-05-16  BAJAJELEC   PYRAMID BUY ₹4,600.55 at ₹230.05 (box jump — doubling the stake with NEW capital; stop stays ₹212.80; charges ₹5.45)
2016-05-16  HDFCMFGETF  PYRAMID BUY ₹2,643.16 at ₹2,805.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,629.60; charges ₹3.13)
2016-05-16  MCLEODRUSS  PYRAMID BUY ₹2,527.49 at ₹186.80 (box jump — doubling the stake with NEW capital; stop stays ₹169.72; charges ₹2.99)
2016-05-16  UJAAS       PYRAMID BUY ₹3,360.97 at ₹22.55 (box jump — doubling the stake with NEW capital; stop stays ₹20.85; charges ₹3.98)
2016-05-24  BAJAJHIND   SELL ₹2,803.35 at stop ₹17.95 (-10.7%, charges ₹2.91) — the cash goes back to work at the next Friday screen
2016-05-30  BAJAJELEC   PYRAMID BUY ₹10,152.98 at ₹254.00 (box jump — doubling the stake with NEW capital; stop stays ₹213.99; charges ₹12.03)
2016-06-24  BAJAJELEC   SELL ₹17,079.52 at stop ₹213.99 (-10.3%, charges ₹17.72) — the cash goes back to work at the next Friday screen
2016-06-27  INDIAGLYCO  BUY ₹7,435.00 at ₹94.50 (fresh Friday signal — BUY: 10.89× weekly, month 2.22×, ladder rising; stop ₹82.89; charges ₹8.81)
2016-06-27  JSWHL       BUY ₹7,440.41 at ₹1,221.00 (fresh Friday signal — BUY: 4.90× weekly, month 1.93×, ladder rising; stop ₹938.60; charges ₹8.82)
2016-06-27  MANAPPURAM  BUY ₹5,007.46 at ₹66.50 (fresh Friday signal — BUY: 2.43× weekly, month 2.08×, ladder rising; stop ₹53.01; charges ₹5.93)
2016-07-04  HDFCMFGETF  PYRAMID BUY ₹5,420.69 at ₹2,878.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,691.35; charges ₹6.42)
2016-07-04  INDIAGLYCO  PYRAMID BUY ₹8,172.74 at ₹104.00 (box jump — doubling the stake with NEW capital; stop stays ₹83.06; charges ₹9.68)
2016-07-04  JSWHL       PYRAMID BUY ₹7,729.83 at ₹1,270.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,113.45; charges ₹9.16)
2016-07-18  MCLEODRUSS  PYRAMID BUY ₹5,725.41 at ₹211.70 (box jump — doubling the stake with NEW capital; stop stays ₹198.74; charges ₹6.78)
2016-07-19  MCLEODRUSS  SELL ₹10,732.32 at stop ₹198.74 (+0.1%, charges ₹11.13) — the cash goes back to work at the next Friday screen
2016-07-25  TATAMETALI  BUY ₹10,382.24 at ₹453.00 (fresh Friday signal — BUY: 7.99× weekly, month 6.02×, ladder rising; stop ₹304.18; charges ₹12.30)
2016-08-01  MANAPPURAM  PYRAMID BUY ₹6,174.81 at ₹82.10 (box jump — doubling the stake with NEW capital; stop stays ₹69.97; charges ₹7.32)
2016-08-08  TATAMETALI  PYRAMID BUY ₹10,051.75 at ₹439.10 (box jump — doubling the stake with NEW capital; stop stays ₹366.19; charges ₹11.91)
2016-08-16  MANAPPURAM  PYRAMID BUY ₹12,996.26 at ₹86.45 (box jump — doubling the stake with NEW capital; stop stays ₹76.57; charges ₹15.40)
2016-08-22  JSWHL       PYRAMID BUY ₹15,658.54 at ₹1,287.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,136.20; charges ₹18.55)
2016-08-22  MANAPPURAM  PYRAMID BUY ₹26,352.72 at ₹87.70 (box jump — doubling the stake with NEW capital; stop stays ₹78.04; charges ₹31.22)
2016-09-12  INDIAGLYCO  PYRAMID BUY ₹16,492.88 at ₹105.00 (box jump — doubling the stake with NEW capital; stop stays ₹99.94; charges ₹19.54)
2016-09-21  SOMANYCERA  SELL ₹15,267.31 at stop ₹551.10 (+37.5%, charges ₹15.84) — the cash goes back to work at the next Friday screen
2016-09-26  BANKBEES    BUY ₹15,617.38 at ₹200.99 (fresh Friday signal — ACCUMULATE: 6.55× weekly, month 1.75×, ladder rising; stop ₹189.48; charges ₹18.50)
2016-09-29  TATAMETALI  SELL ₹16,738.13 at stop ₹366.19 (-17.9%, charges ₹17.36) — the cash goes back to work at the next Friday screen
2016-09-29  UJAAS       SELL ₹6,517.55 at stop ₹21.90 (-9.7%, charges ₹6.76) — the cash goes back to work at the next Friday screen
2016-10-03  TVSSRICHAK  BUY ₹19,934.99 at ₹4,077.00 (fresh Friday signal — BUY: 15.60× weekly, month 4.39×, ladder rising; stop ₹2,467.20; charges ₹23.62)
2016-10-10  INDIAGLYCO  PYRAMID BUY ₹41,192.08 at ₹131.20 (box jump — doubling the stake with NEW capital; stop stays ₹102.72; charges ₹48.81)
2016-10-10  TVSSRICHAK  PYRAMID BUY ₹18,973.67 at ₹3,885.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,633.84; charges ₹22.48)
2016-10-13  MANAPPURAM  SELL ₹53,693.63 at stop ₹89.49 (+6.5%, charges ₹55.70) — the cash goes back to work at the next Friday screen
2016-10-17  JKPAPER     BUY ₹25,095.20 at ₹79.20 (fresh Friday signal — BUY: 1.69× weekly, month 4.22×, ladder rising; stop ₹53.67; charges ₹29.73)
2016-10-17  SUNILHITEC  BUY ₹25,121.71 at ₹410.40 (fresh Friday signal — BUY: 4.33× weekly, month 5.72×, ladder rising; stop ₹234.71; charges ₹29.76)
2016-10-24  JKPAPER     PYRAMID BUY ₹25,445.24 at ₹80.40 (box jump — doubling the stake with NEW capital; stop stays ₹73.53; charges ₹30.15)
2016-10-24  JSWHL       PYRAMID BUY ₹31,247.46 at ₹1,285.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,193.20; charges ₹37.02)
2016-11-02  JSWHL       SELL ₹57,935.84 at stop ₹1,193.20 (-6.5%, charges ₹60.10) — the cash goes back to work at the next Friday screen
2016-11-07  SUNILHITEC  PYRAMID BUY ₹24,905.47 at ₹407.35 (box jump — doubling the stake with NEW capital; stop stays ₹311.57; charges ₹29.51)
2016-11-08  SUNILHITEC  SELL ₹38,036.89 at stop ₹311.57 (-23.8%, charges ₹39.46) — the cash goes back to work at the next Friday screen
2016-11-09  BANKBEES    SELL ₹14,690.71 at stop ₹189.48 (-5.7%, charges ₹15.24) — the cash goes back to work at the next Friday screen
2016-11-09  TVSSRICHAK  SELL ₹35,436.32 at stop ₹3,633.84 (-8.7%, charges ₹36.76) — the cash goes back to work at the next Friday screen
2016-11-15  HONDAPOWER  BUY ₹30,435.10 at ₹1,556.00 (fresh Friday signal — ACCUMULATE: 2.24× weekly, month 1.89×, ladder rising; stop ₹1,438.87; charges ₹36.06)
2016-11-15  NAVNETEDUL  BUY ₹30,434.40 at ₹105.85 (fresh Friday signal — BUY: 4.95× weekly, month 3.78×, ladder rising; stop ₹91.20; charges ₹36.06)
2016-11-15  SOTL        BUY ₹30,285.75 at ₹745.05 (fresh Friday signal — BUY: 2.13× weekly, month 2.02×, ladder rising; stop ₹661.96; charges ₹35.88)
2016-11-15  VIJAYABANK  BUY ₹30,502.57 at ₹49.55 (fresh Friday signal — BUY: 5.15× weekly, month 2.83×, ladder rising; stop ₹37.62; charges ₹36.14)
2016-11-17  GOLDBEES    SELL ₹10,258.37 at stop ₹2,689.64 (+0.3%, charges ₹10.64) — the cash goes back to work at the next Friday screen
2016-11-18  HDFCMFGETF  SELL ₹10,225.38 at stop ₹2,718.90 (-3.1%, charges ₹10.61) — the cash goes back to work at the next Friday screen
2016-11-18  HONDAPOWER  SELL ₹28,081.58 at stop ₹1,438.87 (-7.5%, charges ₹29.13) — the cash goes back to work at the next Friday screen
2016-11-21  BALMLAWRIE  BUY ₹32,920.90 at ₹849.00 (fresh Friday signal — ACCUMULATE: 1.75× weekly, month 2.76×, ladder rising; stop ₹768.17; charges ₹39.01)
2016-11-21  SOTL        PYRAMID BUY ₹29,234.84 at ₹720.05 (box jump — doubling the stake with NEW capital; stop stays ₹669.75; charges ₹34.64)
2016-12-05  ESSELPACK   BUY ₹38,163.28 at ₹126.50 (fresh Friday signal — BUY: 4.47× weekly, month 2.09×, ladder rising; stop ₹104.50; charges ₹45.22)
2016-12-05  VIJAYABANK  PYRAMID BUY ₹27,207.66 at ₹44.25 (box jump — doubling the stake with NEW capital; stop stays ₹39.32; charges ₹32.24)
2016-12-12  ESSELPACK   PYRAMID BUY ₹38,005.07 at ₹126.12 (box jump — doubling the stake with NEW capital; stop stays ₹114.95; charges ₹45.03)
2016-12-26  BALMLAWRIE  PYRAMID BUY ₹9,488.89 at ₹245.00 (box jump — doubling the stake with NEW capital; stop stays ₹997.98; charges ₹11.24)
2016-12-26  BALMLAWRIE  SELL ₹77,177.97 at stop ₹997.98 (+82.4%, charges ₹80.06) — the cash goes back to work at the next Friday screen
2017-01-02  KOHINOOR    BUY ₹39,960.12 at ₹71.70 (fresh Friday signal — ACCUMULATE: 1.70× weekly, month 3.58×, ladder rising; stop ₹53.92; charges ₹47.35)
2017-01-02  STCINDIA    BUY ₹45,938.37 at ₹211.00 (fresh Friday signal — BUY: 8.14× weekly, month 3.52×, ladder rising; stop ₹109.25; charges ₹54.43)
2017-01-09  SOTL        PYRAMID BUY ₹58,836.75 at ₹725.00 (box jump — doubling the stake with NEW capital; stop stays ₹670.27; charges ₹69.71)
2017-01-16  SOTL        PYRAMID BUY ₹1.22 lakh at ₹749.90 (box jump — doubling the stake with NEW capital; stop stays ₹679.30; charges ₹144.12)
2017-01-16  STCINDIA    PYRAMID BUY ₹48,493.45 at ₹223.00 (box jump — doubling the stake with NEW capital; stop stays ₹187.15; charges ₹57.46)
2017-01-23  KOHINOOR    PYRAMID BUY ₹51,574.87 at ₹92.65 (box jump — doubling the stake with NEW capital; stop stays ₹77.53; charges ₹61.11)
2017-01-30  ESSELPACK   PYRAMID BUY ₹76,190.97 at ₹126.50 (box jump — doubling the stake with NEW capital; stop stays ₹115.95; charges ₹90.27)
2017-01-30  NAVNETEDUL  PYRAMID BUY ₹35,438.40 at ₹123.40 (box jump — doubling the stake with NEW capital; stop stays ₹109.30; charges ₹41.99)
2017-01-30  STCINDIA    SELL ₹81,262.55 at stop ₹187.15 (-13.8%, charges ₹84.29) — the cash goes back to work at the next Friday screen
2017-02-06  MONNETISPA  BUY ₹81,262.55 at ₹34.85 (fresh Friday signal — BUY: 12.75× weekly, month 9.82×, ladder rising; stop ₹24.32; charges ₹96.28)
2017-02-13  MONNETISPA  PYRAMID BUY ₹89,084.93 at ₹38.25 (box jump — doubling the stake with NEW capital; stop stays ₹31.54; charges ₹105.55)
2017-02-20  MONNETISPA  PYRAMID BUY ₹1.75 lakh at ₹37.50 (box jump — doubling the stake with NEW capital; stop stays ₹33.06; charges ₹206.84)
2017-02-20  VIJAYABANK  PYRAMID BUY ₹79,761.85 at ₹64.90 (box jump — doubling the stake with NEW capital; stop stays ₹56.94; charges ₹94.50)
2017-02-21  ESSELPACK   SELL ₹1.39 lakh at stop ₹115.95 (-8.3%, charges ₹144.65) — the cash goes back to work at the next Friday screen
2017-02-27  KARURVYSYA  BUY ₹1.25 lakh at ₹99.65 (fresh Friday signal — BUY: 5.67× weekly, month 2.66×, ladder rising; stop ₹85.97; charges ₹147.88)
2017-02-27  MONNETISPA  SELL ₹3.07 lakh at stop ₹33.06 (-10.7%, charges ₹318.77) — the cash goes back to work at the next Friday screen
2017-03-03  KOHINOOR    SELL ₹86,175.71 at stop ₹77.53 (-5.6%, charges ₹89.39) — the cash goes back to work at the next Friday screen
2017-03-06  DHANBANK    BUY ₹1.32 lakh at ₹29.45 (fresh Friday signal — BUY: 7.14× weekly, month 2.95×, ladder rising; stop ₹22.32; charges ₹156.87)
2017-03-06  KTKBANK     BUY ₹1.33 lakh at ₹137.30 (fresh Friday signal — BUY: 3.16× weekly, month 2.19×, ladder rising; stop ₹106.12; charges ₹157.47)
2017-03-06  NAVNETEDUL  PYRAMID BUY ₹82,143.13 at ₹143.10 (box jump — doubling the stake with NEW capital; stop stays ₹130.72; charges ₹97.32)
2017-03-06  RAIN        BUY ₹1.32 lakh at ₹99.80 (fresh Friday signal — BUY: 3.51× weekly, month 4.51×, ladder rising; stop ₹72.39; charges ₹156.98)
2017-03-14  KARURVYSYA  PYRAMID BUY ₹1.25 lakh at ₹100.00 (box jump — doubling the stake with NEW capital; stop stays ₹91.82; charges ₹148.23)
2017-03-20  INDIAGLYCO  SELL ₹94,336.77 at stop ₹150.48 (+29.0%, charges ₹97.86) — the cash goes back to work at the next Friday screen
2017-03-20  KTKBANK     PYRAMID BUY ₹1.35 lakh at ₹140.00 (box jump — doubling the stake with NEW capital; stop stays ₹126.59; charges ₹160.38)
2017-03-20  RAIN        PYRAMID BUY ₹1.35 lakh at ₹101.95 (box jump — doubling the stake with NEW capital; stop stays ₹93.77; charges ₹160.17)
2017-03-20  VIJAYABANK  PYRAMID BUY ₹1.58 lakh at ₹64.20 (box jump — doubling the stake with NEW capital; stop stays ₹59.24; charges ₹186.86)
2017-03-27  CENTENKA    BUY ₹1.05 lakh at ₹415.00 (fresh Friday signal — BUY: 17.44× weekly, month 2.99×, ladder rising; stop ₹295.45; charges ₹123.99)
2017-04-03  CENTENKA    PYRAMID BUY ₹1.10 lakh at ₹434.90 (box jump — doubling the stake with NEW capital; stop stays ₹391.59; charges ₹129.78)
2017-04-03  DHANBANK    PYRAMID BUY ₹1.36 lakh at ₹30.20 (box jump — doubling the stake with NEW capital; stop stays ₹24.70; charges ₹160.67)
2017-04-03  TAX         FY2017 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹36,557.91 / LT ₹0.00)
2017-04-10  NAVNETEDUL  PYRAMID BUY ₹1.84 lakh at ₹160.15 (box jump — doubling the stake with NEW capital; stop stays ₹152.95; charges ₹217.71)
2017-04-17  CENTENKA    PYRAMID BUY ₹2.19 lakh at ₹434.80 (box jump — doubling the stake with NEW capital; stop stays ₹398.05; charges ₹259.34)
2017-04-17  KARURVYSYA  PYRAMID BUY ₹2.98 lakh at ₹119.15 (box jump — doubling the stake with NEW capital; stop stays ₹107.54; charges ₹353.02)
2017-04-17  RAIN        PYRAMID BUY ₹2.83 lakh at ₹106.90 (box jump — doubling the stake with NEW capital; stop stays ₹96.95; charges ₹335.70)
2017-04-24  KARURVYSYA  PYRAMID BUY ₹5.88 lakh at ₹117.70 (box jump — doubling the stake with NEW capital; stop stays ₹110.29; charges ₹697.03)
2017-05-02  CENTENKA    PYRAMID BUY ₹4.25 lakh at ₹422.00 (box jump — doubling the stake with NEW capital; stop stays ₹399.00; charges ₹503.12)
2017-05-02  DHANBANK    PYRAMID BUY ₹3.48 lakh at ₹38.80 (box jump — doubling the stake with NEW capital; stop stays ₹30.50; charges ₹412.61)
2017-05-02  JKPAPER     PYRAMID BUY ₹68,825.93 at ₹108.80 (box jump — doubling the stake with NEW capital; stop stays ₹95.52; charges ₹81.55)
2017-05-02  KTKBANK     PYRAMID BUY ₹3.21 lakh at ₹166.00 (box jump — doubling the stake with NEW capital; stop stays ₹141.60; charges ₹380.11)
2017-05-08  JKPAPER     PYRAMID BUY ₹1.44 lakh at ₹113.50 (box jump — doubling the stake with NEW capital; stop stays ₹101.08; charges ₹170.04)
2017-05-15  DHANBANK    PYRAMID BUY ₹7.02 lakh at ₹39.15 (box jump — doubling the stake with NEW capital; stop stays ₹36.62; charges ₹832.17)
2017-05-18  CENTENKA    SELL ₹8.02 lakh at stop ₹399.00 (-6.3%, charges ₹831.58) — the cash goes back to work at the next Friday screen
2017-05-19  NAVNETEDUL  SELL ₹3.60 lakh at stop ₹156.99 (+8.7%, charges ₹373.08) — the cash goes back to work at the next Friday screen
2017-05-22  DHANBANK    SELL ₹13.12 lakh at stop ₹36.62 (-0.3%, charges ₹1,360.73) — the cash goes back to work at the next Friday screen
2017-05-22  KTKBANK     PYRAMID BUY ₹6.49 lakh at ₹168.00 (box jump — doubling the stake with NEW capital; stop stays ₹154.85; charges ₹768.92)
2017-05-22  SHAKTIPUMP  BUY ₹5.18 lakh at ₹334.00 (fresh Friday signal — BUY: 5.25× weekly, month 4.33×, ladder rising; stop ₹248.90; charges ₹614.18)
2017-05-22  SUMEETINDS  BUY ₹6.43 lakh at ₹38.35 (fresh Friday signal — BUY: 8.84× weekly, month 1.57×, ladder rising; stop ₹32.82; charges ₹761.80)
2017-05-23  KTKBANK     SELL ₹11.94 lakh at stop ₹154.85 (-3.3%, charges ₹1,238.96) — the cash goes back to work at the next Friday screen
2017-05-23  RAIN        SELL ₹5.13 lakh at stop ₹96.95 (-6.7%, charges ₹532.23) — the cash goes back to work at the next Friday screen
2017-05-23  VIJAYABANK  SELL ₹3.84 lakh at stop ₹78.29 (+30.4%, charges ₹398.34) — the cash goes back to work at the next Friday screen
2017-05-24  SUMEETINDS  SELL ₹5.49 lakh at stop ₹32.82 (-14.4%, charges ₹569.51) — the cash goes back to work at the next Friday screen
2017-05-29  BIL         BUY ₹6.39 lakh at ₹614.80 (fresh Friday signal — BUY: 1.54× weekly, month 1.92×, ladder rising; stop ₹527.49; charges ₹757.45)
2017-05-29  VOLTAS      BUY ₹6.43 lakh at ₹496.90 (fresh Friday signal — BUY: 4.55× weekly, month 1.70×, ladder rising; stop ₹383.23; charges ₹761.94)
2017-05-29  WALCHANNAG  BUY ₹6.41 lakh at ₹174.10 (fresh Friday signal — ACCUMULATE: 2.55× weekly, month 2.77×, ladder rising; stop ₹163.40; charges ₹759.96)
2017-06-05  GRINDWELL   BUY ₹7.07 lakh at ₹400.00 (fresh Friday signal — BUY: 5.57× weekly, month 2.00×, ladder rising; stop ₹357.34; charges ₹838.00)
2017-06-05  TTKPRESTIG  BUY ₹7.07 lakh at ₹6,725.00 (fresh Friday signal — ACCUMULATE: 2.99× weekly, month 1.54×, ladder rising; stop ₹5,890.95; charges ₹837.38)
2017-06-05  VOLTAS      PYRAMID BUY ₹6.48 lakh at ₹501.00 (box jump — doubling the stake with NEW capital; stop stays ₹453.86; charges ₹767.31)
2017-06-12  BIL         PYRAMID BUY ₹6.07 lakh at ₹584.45 (box jump — doubling the stake with NEW capital; stop stays ₹551.00; charges ₹719.21)
2017-06-12  GRINDWELL   PYRAMID BUY ₹7.14 lakh at ₹404.00 (box jump — doubling the stake with NEW capital; stop stays ₹364.37; charges ₹845.38)
2017-06-12  JKPAPER     SELL ₹2.55 lakh at stop ₹101.08 (-2.7%, charges ₹264.72) — the cash goes back to work at the next Friday screen
2017-06-12  SHAKTIPUMP  PYRAMID BUY ₹6.85 lakh at ₹441.80 (box jump — doubling the stake with NEW capital; stop stays ₹357.49; charges ₹811.45)
2017-06-12  TITAN       BUY ₹6.15 lakh at ₹541.90 (fresh Friday signal — ACCUMULATE: 7.25× weekly, month 2.38×, ladder rising; stop ₹495.33; charges ₹728.08)
2017-06-19  SHAKTIPUMP  PYRAMID BUY ₹13.78 lakh at ₹444.75 (box jump — doubling the stake with NEW capital; stop stays ₹415.62; charges ₹1,632.77)
2017-06-19  VOLTAS      PYRAMID BUY ₹12.63 lakh at ₹489.00 (box jump — doubling the stake with NEW capital; stop stays ₹456.19; charges ₹1,496.98)
2017-06-23  VOLTAS      SELL ₹23.54 lakh at stop ₹456.19 (-7.6%, charges ₹2,441.34) — the cash goes back to work at the next Friday screen
2017-06-27  EVERESTIND  BUY ₹11.36 lakh at ₹365.20 (fresh Friday signal — BUY: 7.06× weekly, month 4.53×, ladder rising; stop ₹281.87; charges ₹1,346.51)
2017-06-27  GOACARBON   BUY ₹11.45 lakh at ₹248.70 (fresh Friday signal — BUY: 9.59× weekly, month 4.76×, ladder rising; stop ₹148.25; charges ₹1,356.07)
2017-06-27  WALCHANNAG  SELL ₹6.01 lakh at stop ₹163.40 (-6.1%, charges ₹623.06) — the cash goes back to work at the next Friday screen
2017-06-28  SHAKTIPUMP  SELL ₹25.71 lakh at stop ₹415.62 (-0.2%, charges ₹2,667.35) — the cash goes back to work at the next Friday screen
2017-07-03  GVKPIL      BUY ₹11.79 lakh at ₹8.90 (fresh Friday signal — BUY: 4.75× weekly, month 2.80×, ladder rising; stop ₹5.83; charges ₹1,396.33)
2017-07-03  SEAMECLTD   BUY ₹11.72 lakh at ₹161.20 (fresh Friday signal — BUY: 4.52× weekly, month 1.56×, ladder rising; stop ₹128.25; charges ₹1,389.12)
2017-07-03  VENKEYS     BUY ₹11.49 lakh at ₹1,702.90 (fresh Friday signal — BUY: 3.61× weekly, month 1.67×, ladder rising; stop ₹1,311.00; charges ₹1,361.22)
2017-07-10  EVERESTIND  PYRAMID BUY ₹12.02 lakh at ₹386.80 (box jump — doubling the stake with NEW capital; stop stays ₹318.64; charges ₹1,424.47)
2017-07-10  GOACARBON   PYRAMID BUY ₹13.79 lakh at ₹300.00 (box jump — doubling the stake with NEW capital; stop stays ₹212.73; charges ₹1,633.85)
2017-07-10  GVKPIL      PYRAMID BUY ₹10.85 lakh at ₹8.20 (box jump — doubling the stake with NEW capital; stop stays ₹7.32; charges ₹1,284.99)
2017-07-13  GVKPIL      SELL ₹19.33 lakh at stop ₹7.32 (-14.4%, charges ₹2,005.26) — the cash goes back to work at the next Friday screen
2017-07-17  RML         BUY ₹16.82 lakh at ₹522.00 (fresh Friday signal — BUY: 3.37× weekly, month 1.74×, ladder rising; stop ₹447.55; charges ₹1,992.36)
2017-07-17  SEAMECLTD   PYRAMID BUY ₹11.56 lakh at ₹159.10 (box jump — doubling the stake with NEW capital; stop stays ₹142.50; charges ₹1,369.40)
2017-07-24  GRINDWELL   PYRAMID BUY ₹15.07 lakh at ₹427.00 (box jump — doubling the stake with NEW capital; stop stays ₹389.45; charges ₹1,785.96)
2017-07-24  TITAN       PYRAMID BUY ₹6.18 lakh at ₹545.30 (box jump — doubling the stake with NEW capital; stop stays ₹498.75; charges ₹731.78)
2017-07-24  VENKEYS     PYRAMID BUY ₹13.61 lakh at ₹2,019.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,719.30; charges ₹1,612.54)
2017-08-10  BIL         SELL ₹11.43 lakh at stop ₹551.00 (-8.1%, charges ₹1,185.31) — the cash goes back to work at the next Friday screen
2017-08-10  EVERESTIND  SELL ₹19.78 lakh at stop ₹318.64 (-15.3%, charges ₹2,051.35) — the cash goes back to work at the next Friday screen
2017-08-10  GRINDWELL   SELL ₹27.45 lakh at stop ₹389.45 (-6.0%, charges ₹2,847.54) — the cash goes back to work at the next Friday screen
2017-08-10  KARURVYSYA  SELL ₹12.81 lakh at stop ₹128.39 (+13.0%, charges ₹1,329.17) — the cash goes back to work at the next Friday screen
2017-08-11  VENKEYS     SELL ₹23.13 lakh at stop ₹1,719.30 (-7.6%, charges ₹2,399.67) — the cash goes back to work at the next Friday screen
2017-08-14  INSECTICID  BUY ₹18.91 lakh at ₹771.85 (fresh Friday signal — BUY: 3.90× weekly, month 2.53×, ladder rising; stop ₹669.32; charges ₹2,240.79)
2017-08-21  BEML        BUY ₹20.63 lakh at ₹1,897.00 (fresh Friday signal — BUY: 3.75× weekly, month 2.60×, ladder rising; stop ₹1,325.12; charges ₹2,444.83)
2017-08-21  GRAVITA     BUY ₹20.61 lakh at ₹111.50 (fresh Friday signal — BUY: 2.35× weekly, month 1.91×, ladder rising; stop ₹77.56; charges ₹2,441.62)
2017-08-21  INSECTICID  PYRAMID BUY ₹19.14 lakh at ₹782.00 (box jump — doubling the stake with NEW capital; stop stays ₹682.10; charges ₹2,267.57)
2017-08-21  SPARC       BUY ₹20.56 lakh at ₹397.00 (fresh Friday signal — BUY: 2.36× weekly, month 2.85×, ladder rising; stop ₹307.62; charges ₹2,436.27)
2017-08-28  TRENT       BUY ₹16.40 lakh at ₹296.00 (fresh Friday signal — ACCUMULATE: 3.27× weekly, month 1.58×, ladder rising; stop ₹249.47; charges ₹1,943.16)
2017-09-04  GOACARBON   PYRAMID BUY ₹32.62 lakh at ₹355.00 (box jump — doubling the stake with NEW capital; stop stays ₹245.45; charges ₹3,864.49)
2017-09-04  GRAVITA     PYRAMID BUY ₹23.38 lakh at ₹126.65 (box jump — doubling the stake with NEW capital; stop stays ₹99.75; charges ₹2,770.09)
2017-09-04  SPARC       PYRAMID BUY ₹20.18 lakh at ₹390.00 (box jump — doubling the stake with NEW capital; stop stays ₹362.19; charges ₹2,390.48)
2017-09-04  TITAN       PYRAMID BUY ₹13.81 lakh at ₹610.00 (box jump — doubling the stake with NEW capital; stop stays ₹568.72; charges ₹1,636.24)
2017-09-11  GRAVITA     PYRAMID BUY ₹48.58 lakh at ₹131.65 (box jump — doubling the stake with NEW capital; stop stays ₹114.19; charges ₹5,755.49)
2017-09-11  INSECTICID  PYRAMID BUY ₹44.91 lakh at ₹918.05 (box jump — doubling the stake with NEW capital; stop stays ₹821.75; charges ₹5,321.00)
2017-09-11  SEAMECLTD   SELL ₹20.67 lakh at stop ₹142.50 (-11.0%, charges ₹2,144.12) — the cash goes back to work at the next Friday screen
2017-09-18  TITAN       PYRAMID BUY ₹28.74 lakh at ₹635.10 (box jump — doubling the stake with NEW capital; stop stays ₹597.79; charges ₹3,405.12)
2017-09-21  INSECTICID  SELL ₹80.27 lakh at stop ₹821.75 (-3.0%, charges ₹8,326.09) — the cash goes back to work at the next Friday screen
2017-09-25  BEML        PYRAMID BUY ₹18.68 lakh at ₹1,719.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,744.63; charges ₹2,213.83)
2017-09-25  BEML        SELL ₹37.85 lakh at stop ₹1,744.63 (-3.5%, charges ₹3,925.95) — the cash goes back to work at the next Friday screen
2017-09-25  HIKAL       BUY ₹45.60 lakh at ₹223.35 (fresh Friday signal — ACCUMULATE: 7.48× weekly, month 2.19×, ladder rising; stop ₹184.26; charges ₹5,403.19)
2017-09-25  NELCO       BUY ₹45.60 lakh at ₹134.75 (fresh Friday signal — BUY: 7.97× weekly, month 4.45×, ladder rising; stop ₹74.89; charges ₹5,402.23)
2017-09-25  SOTL        SELL ₹3.86 lakh at stop ₹1,192.30 (+61.3%, charges ₹400.59) — the cash goes back to work at the next Friday screen
2017-09-25  SPARC       SELL ₹37.41 lakh at stop ₹362.19 (-8.0%, charges ₹3,880.89) — the cash goes back to work at the next Friday screen
2017-09-25  TITAN       SELL ₹54.01 lakh at stop ₹597.79 (-1.3%, charges ₹5,602.92) — the cash goes back to work at the next Friday screen
2017-09-25  TRENT       PYRAMID BUY ₹16.57 lakh at ₹299.50 (box jump — doubling the stake with NEW capital; stop stays ₹274.55; charges ₹1,963.80)
2017-10-03  BFINVEST    BUY ₹30.83 lakh at ₹228.00 (fresh Friday signal — ACCUMULATE: 3.24× weekly, month 5.43×, ladder rising; stop ₹158.40; charges ₹3,652.96)
2017-10-03  DEN         BUY ₹55.92 lakh at ₹89.40 (fresh Friday signal — ACCUMULATE: 5.36× weekly, month 1.96×, ladder rising; stop ₹78.80; charges ₹6,625.89)
2017-10-03  GOACARBON   PYRAMID BUY ₹87.32 lakh at ₹475.50 (box jump — doubling the stake with NEW capital; stop stays ₹378.80; charges ₹10,346.35)
2017-10-03  SHOPERSTOP  BUY ₹56.12 lakh at ₹486.40 (fresh Friday signal — BUY: 12.98× weekly, month 10.59×, ladder rising; stop ₹386.60; charges ₹6,649.34)
2017-10-09  SHOPERSTOP  PYRAMID BUY ₹59.56 lakh at ₹516.80 (box jump — doubling the stake with NEW capital; stop stays ₹412.79; charges ₹7,056.55)
2017-10-23  GRAVITA     PYRAMID BUY ₹1.20 crore at ₹162.35 (box jump — doubling the stake with NEW capital; stop stays ₹147.96; charges ₹14,186.87)
2017-10-23  RML         PYRAMID BUY ₹17.18 lakh at ₹534.00 (box jump — doubling the stake with NEW capital; stop stays ₹475.00; charges ₹2,035.75)
2017-11-06  SHOPERSTOP  PYRAMID BUY ₹1.34 crore at ₹580.00 (box jump — doubling the stake with NEW capital; stop stays ₹475.00; charges ₹15,829.63)
2017-11-06  TTKPRESTIG  PYRAMID BUY ₹6.89 lakh at ₹6,565.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,049.55; charges ₹816.49)
2017-11-08  GRAVITA     SELL ₹2.18 crore at stop ₹147.96 (+2.9%, charges ₹22,602.33) — the cash goes back to work at the next Friday screen
2017-11-13  EXCELCROP   BUY ₹1.03 crore at ₹2,085.00 (fresh Friday signal — BUY: 4.05× weekly, month 4.95×, ladder rising; stop ₹1,605.50; charges ₹12,212.72)
2017-11-13  HIKAL       PYRAMID BUY ₹49.25 lakh at ₹241.50 (box jump — doubling the stake with NEW capital; stop stays ₹226.62; charges ₹5,835.34)
2017-11-13  WHEELS      BUY ₹1.15 crore at ₹1,771.20 (fresh Friday signal — BUY: 19.87× weekly, month 5.54×, ladder rising; stop ₹1,521.19; charges ₹13,604.00)
2017-11-20  BFINVEST    PYRAMID BUY ₹39.84 lakh at ₹295.00 (box jump — doubling the stake with NEW capital; stop stays ₹239.40; charges ₹4,720.82)
2017-11-20  NELCO       PYRAMID BUY ₹36.40 lakh at ₹107.70 (box jump — doubling the stake with NEW capital; stop stays ₹92.76; charges ₹4,312.66)
2017-11-20  SHOPERSTOP  PYRAMID BUY ₹2.56 crore at ₹557.05 (box jump — doubling the stake with NEW capital; stop stays ₹513.28; charges ₹30,388.53)
2017-11-27  RML         PYRAMID BUY ₹43.07 lakh at ₹669.75 (box jump — doubling the stake with NEW capital; stop stays ₹492.20; charges ₹5,103.50)
2017-11-27  WHEELS      PYRAMID BUY ₹1.12 crore at ₹1,729.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,588.26; charges ₹13,264.14)
2017-12-04  EXCELCROP   PYRAMID BUY ₹1.02 crore at ₹2,069.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,881.00; charges ₹12,104.64)
2017-12-11  BFINVEST    PYRAMID BUY ₹1.07 crore at ₹397.45 (box jump — doubling the stake with NEW capital; stop stays ₹357.49; charges ₹12,713.08)
2017-12-11  RML         PYRAMID BUY ₹1.01 crore at ₹785.30 (box jump — doubling the stake with NEW capital; stop stays ₹604.20; charges ₹11,960.89)
2017-12-11  TRENT       PYRAMID BUY ₹37.38 lakh at ₹337.90 (box jump — doubling the stake with NEW capital; stop stays ₹302.43; charges ₹4,428.56)
2017-12-11  TTKPRESTIG  PYRAMID BUY ₹14.87 lakh at ₹7,085.10 (box jump — doubling the stake with NEW capital; stop stays ₹6,100.47; charges ₹1,761.31)
2017-12-15  HIKAL       SELL ₹92.28 lakh at stop ₹226.62 (-2.5%, charges ₹9,572.43) — the cash goes back to work at the next Friday screen
2017-12-18  BFINVEST    SELL ₹1.93 crore at stop ₹357.49 (+8.5%, charges ₹19,989.73) — the cash goes back to work at the next Friday screen
2017-12-18  EXCELCROP   PYRAMID BUY ₹1.96 crore at ₹1,989.65 (box jump — doubling the stake with NEW capital; stop stays ₹1,882.90; charges ₹23,267.02)
2017-12-26  DEN         PYRAMID BUY ₹68.95 lakh at ₹110.35 (box jump — doubling the stake with NEW capital; stop stays ₹93.62; charges ₹8,168.91)
2017-12-26  GPIL        BUY ₹2.30 crore at ₹300.95 (fresh Friday signal — BUY: 6.72× weekly, month 4.60×, ladder rising; stop ₹141.76; charges ₹27,288.23)
2017-12-26  TTKPRESTIG  PYRAMID BUY ₹33.30 lakh at ₹7,940.05 (box jump — doubling the stake with NEW capital; stop stays ₹6,697.50; charges ₹3,945.34)
2018-01-08  DEN         PYRAMID BUY ₹1.41 crore at ₹112.90 (box jump — doubling the stake with NEW capital; stop stays ₹98.04; charges ₹16,705.45)
2018-01-08  GPIL        PYRAMID BUY ₹3.30 crore at ₹431.30 (box jump — doubling the stake with NEW capital; stop stays ₹311.41; charges ₹39,061.21)
2018-01-15  EXCELCROP   PYRAMID BUY ₹5.74 crore at ₹2,909.90 (box jump — doubling the stake with NEW capital; stop stays ₹2,214.45; charges ₹68,016.57)
2018-01-15  WHEELS      PYRAMID BUY ₹2.79 crore at ₹2,159.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,957.00; charges ₹33,106.20)
2018-01-17  SHOPERSTOP  SELL ₹4.72 crore at stop ₹513.28 (-6.5%, charges ₹48,949.06) — the cash goes back to work at the next Friday screen
2018-01-22  SEINV       BUY ₹4.42 crore at ₹340.05 (fresh Friday signal — BUY: 19.93× weekly, month 2.87×, ladder rising; stop ₹153.56; charges ₹52,325.23)
2018-01-29  DEN         PYRAMID BUY ₹3.03 crore at ₹121.55 (box jump — doubling the stake with NEW capital; stop stays ₹107.61; charges ₹35,949.42)
2018-01-29  GPIL        PYRAMID BUY ₹9.13 crore at ₹597.80 (box jump — doubling the stake with NEW capital; stop stays ₹463.12; charges ₹1.08 lakh)
2018-01-31  GOACARBON   SELL ₹3.35 crore at stop ₹913.01 (+131.1%, charges ₹34,728.56) — the cash goes back to work at the next Friday screen
2018-01-31  TTKPRESTIG  SELL ₹60.86 lakh at stop ₹7,267.50 (-1.8%, charges ₹6,312.79) — the cash goes back to work at the next Friday screen
2018-02-01  DEN         SELL ₹5.36 crore at stop ₹107.61 (-5.6%, charges ₹55,637.05) — the cash goes back to work at the next Friday screen
2018-02-02  TRENT       SELL ₹66.80 lakh at stop ₹302.43 (-4.8%, charges ₹6,929.05) — the cash goes back to work at the next Friday screen
2018-02-05  GOLDSHARE   BUY ₹5.13 crore at ₹2,702.50 (fresh Friday signal — BUY: 2.12× weekly, month 1.67×, ladder rising; stop ₹2,510.28; charges ₹60,750.36)
2018-02-05  MPHASIS     BUY ₹5.12 crore at ₹851.10 (fresh Friday signal — BUY: 3.88× weekly, month 3.19×, ladder rising; stop ₹668.70; charges ₹60,720.50)
2018-02-06  GPIL        SELL ₹14.13 crore at stop ₹463.12 (-3.9%, charges ₹1.47 lakh) — the cash goes back to work at the next Friday screen
2018-02-12  GOLDSHARE   PYRAMID BUY ₹5.12 crore at ₹2,701.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,511.51; charges ₹60,644.70)
2018-02-12  JUBILANT    BUY ₹5.75 crore at ₹760.80 (fresh Friday signal — BUY: 1.99× weekly, month 3.28×, ladder rising; stop ₹647.52; charges ₹68,093.36)
2018-02-12  NOIDATOLL   BUY ₹3.20 crore at ₹13.40 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 2.25×, ladder rising; stop ₹10.94; charges ₹37,929.04)
2018-02-12  ZYDUSWELL   BUY ₹5.77 crore at ₹1,170.00 (fresh Friday signal — ACCUMULATE: 3.31× weekly, month 2.12×, ladder rising; stop ₹840.61; charges ₹68,311.68)
2018-02-19  GOLDSHARE   PYRAMID BUY ₹10.42 crore at ₹2,750.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,547.00; charges ₹1.23 lakh)
2018-02-19  MPHASIS     PYRAMID BUY ₹5.17 crore at ₹860.10 (box jump — doubling the stake with NEW capital; stop stays ₹771.50; charges ₹61,289.89)
2018-02-26  NELCO       PYRAMID BUY ₹1.09 crore at ₹161.40 (box jump — doubling the stake with NEW capital; stop stays ₹145.64; charges ₹12,918.30)
2018-02-26  ZYDUSWELL   PYRAMID BUY ₹6.16 crore at ₹1,250.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,087.75; charges ₹72,942.75)
2018-03-06  JUBILANT    SELL ₹4.88 crore at stop ₹647.52 (-14.9%, charges ₹50,626.10) — the cash goes back to work at the next Friday screen
2018-03-12  WHEELS      PYRAMID BUY ₹5.65 crore at ₹2,185.05 (box jump — doubling the stake with NEW capital; stop stays ₹1,985.50; charges ₹66,971.60)
2018-03-19  VENKEYS     BUY ₹4.88 crore at ₹4,149.00 (fresh Friday signal — ACCUMULATE: 2.69× weekly, month 2.51×, ladder rising; stop ₹3,417.97; charges ₹57,825.89)
2018-03-23  NELCO       SELL ₹1.96 crore at stop ₹145.64 (+3.1%, charges ₹20,377.79) — the cash goes back to work at the next Friday screen
2018-04-02  TAX         FY2018 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹19.82 lakh / LT ₹0.00)
2018-04-09  NOIDATOLL   PYRAMID BUY ₹3.04 crore at ₹12.75 (box jump — doubling the stake with NEW capital; stop stays ₹11.02; charges ₹36,046.44)
2018-04-16  GOLDSHARE   PYRAMID BUY ₹21.20 crore at ₹2,800.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,584.00; charges ₹2.51 lakh)
2018-04-16  NOIDATOLL   PYRAMID BUY ₹5.79 crore at ₹12.15 (box jump — doubling the stake with NEW capital; stop stays ₹11.30; charges ₹68,659.57)
2018-04-23  VENKEYS     PYRAMID BUY ₹5.25 crore at ₹4,470.00 (box jump — doubling the stake with NEW capital; stop stays ₹4,047.95; charges ₹62,225.95)
2018-04-24  NOIDATOLL   SELL ₹10.76 crore at stop ₹11.30 (-10.4%, charges ₹1.12 lakh) — the cash goes back to work at the next Friday screen
2018-04-26  VENKEYS     SELL ₹9.50 crore at stop ₹4,047.95 (-6.1%, charges ₹98,508.49) — the cash goes back to work at the next Friday screen
2018-04-30  HIL         BUY ₹12.25 crore at ₹2,239.45 (fresh Friday signal — BUY: 6.62× weekly, month 1.77×, ladder rising; stop ₹1,790.75; charges ₹1.45 lakh)
2018-04-30  THOMASCOOK  BUY ₹9.97 crore at ₹293.00 (fresh Friday signal — BUY: 3.95× weekly, month 2.10×, ladder rising; stop ₹247.95; charges ₹1.18 lakh)
2018-05-14  MPHASIS     PYRAMID BUY ₹11.66 crore at ₹970.00 (box jump — doubling the stake with NEW capital; stop stays ₹913.00; charges ₹1.38 lakh)
2018-05-14  THOMASCOOK  PYRAMID BUY ₹9.59 crore at ₹282.00 (box jump — doubling the stake with NEW capital; stop stays ₹264.43; charges ₹1.14 lakh)
2018-05-15  WHEELS      SELL ₹10.26 crore at stop ₹1,985.50 (-4.1%, charges ₹1.06 lakh) — the cash goes back to work at the next Friday screen
2018-05-17  EXCELCROP   SELL ₹12.91 crore at stop ₹3,277.55 (+32.6%, charges ₹1.34 lakh) — the cash goes back to work at the next Friday screen
2018-05-21  ABBOTINDIA  BUY ₹15.26 crore at ₹6,847.00 (fresh Friday signal — BUY: 3.50× weekly, month 2.31×, ladder rising; stop ₹5,757.95; charges ₹1.81 lakh)
2018-05-21  MAHLIFE     BUY ₹7.90 crore at ₹527.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 1.91×, ladder rising; stop ₹484.50; charges ₹93,643.07)
2018-05-21  ZYDUSWELL   PYRAMID BUY ₹12.45 crore at ₹1,265.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,192.25; charges ₹1.47 lakh)
2018-05-28  HIL         PYRAMID BUY ₹11.63 crore at ₹2,128.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,939.95; charges ₹1.38 lakh)
2018-05-28  MPHASIS     PYRAMID BUY ₹26.99 crore at ₹1,123.40 (box jump — doubling the stake with NEW capital; stop stays ₹978.50; charges ₹3.20 lakh)
2018-05-31  ZYDUSWELL   SELL ₹23.42 crore at stop ₹1,192.25 (-3.7%, charges ₹2.43 lakh) — the cash goes back to work at the next Friday screen
2018-06-04  ABBOTINDIA  PYRAMID BUY ₹14.98 crore at ₹6,729.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,184.50; charges ₹1.78 lakh)
2018-06-04  THOMASCOOK  SELL ₹17.95 crore at stop ₹264.43 (-8.0%, charges ₹1.86 lakh) — the cash goes back to work at the next Friday screen
2018-06-05  HIL         SELL ₹21.17 crore at stop ₹1,939.95 (-11.2%, charges ₹2.20 lakh) — the cash goes back to work at the next Friday screen
2018-06-05  RML         SELL ₹1.88 crore at stop ₹732.64 (+5.9%, charges ₹19,507.11) — the cash goes back to work at the next Friday screen
2018-06-18  ASTRAZEN    BUY ₹20.27 crore at ₹1,048.00 (fresh Friday signal — BUY: 7.17× weekly, month 3.61×, ladder rising; stop ₹842.73; charges ₹2.40 lakh)
2018-06-18  MMFL        BUY ₹20.44 crore at ₹1,429.00 (fresh Friday signal — BUY: 6.00× weekly, month 2.27×, ladder rising; stop ₹972.06; charges ₹2.42 lakh)
2018-06-25  ASTRAZEN    PYRAMID BUY ₹23.02 crore at ₹1,191.20 (box jump — doubling the stake with NEW capital; stop stays ₹974.32; charges ₹2.73 lakh)
2018-06-25  WHEELS      BUY ₹23.06 crore at ₹2,500.00 (fresh Friday signal — BUY: 150.85× weekly, month 7.43×, ladder rising; stop ₹1,876.91; charges ₹2.73 lakh)
2018-07-02  ASTRAZEN    PYRAMID BUY ₹43.86 crore at ₹1,135.56 (box jump — doubling the stake with NEW capital; stop stays ₹1,019.92; charges ₹5.20 lakh)
2018-07-09  ABBOTINDIA  PYRAMID BUY ₹32.40 crore at ₹7,280.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,669.48; charges ₹3.84 lakh)
2018-07-09  MMFL        PYRAMID BUY ₹18.85 crore at ₹1,320.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,197.94; charges ₹2.23 lakh)
2018-07-09  WHEELS      PYRAMID BUY ₹20.93 crore at ₹2,272.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,006.50; charges ₹2.48 lakh)
2018-07-18  MMFL        SELL ₹34.17 crore at stop ₹1,197.94 (-12.8%, charges ₹3.54 lakh) — the cash goes back to work at the next Friday screen
2018-07-23  BAJFINANCE  BUY ₹33.93 crore at ₹2,720.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.51×, ladder rising; stop ₹2,141.11; charges ₹4.02 lakh)
2018-08-01  GOLDSHARE   SELL ₹40.09 crore at stop ₹2,652.16 (-4.0%, charges ₹4.16 lakh) — the cash goes back to work at the next Friday screen
2018-08-06  ASTRAZEN    PYRAMID BUY ₹106.54 crore at ₹1,380.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,124.80; charges ₹12.62 lakh)
2018-08-06  BAJFINANCE  PYRAMID BUY ₹33.56 crore at ₹2,693.90 (box jump — doubling the stake with NEW capital; stop stays ₹2,522.06; charges ₹3.98 lakh)
2018-08-06  PEL         BUY ₹40.98 crore at ₹2,824.90 (fresh Friday signal — BUY: 3.49× weekly, month 1.76×, ladder rising; stop ₹2,498.69; charges ₹4.86 lakh)
2018-08-07  MAHLIFE     SELL ₹7.25 crore at stop ₹484.50 (-8.1%, charges ₹75,204.85) — the cash goes back to work at the next Friday screen
2018-08-08  WHEELS      SELL ₹36.90 crore at stop ₹2,006.50 (-15.9%, charges ₹3.83 lakh) — the cash goes back to work at the next Friday screen
2018-08-13  EVERESTIND  BUY ₹44.15 crore at ₹541.00 (fresh Friday signal — BUY: 1.87× weekly, month 2.03×, ladder rising; stop ₹457.95; charges ₹5.23 lakh)
2018-08-13  PEL         PYRAMID BUY ₹40.55 crore at ₹2,798.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,627.89; charges ₹4.80 lakh)
2018-08-20  BAJFINANCE  PYRAMID BUY ₹71.66 crore at ₹2,877.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,616.49; charges ₹8.49 lakh)
2018-08-20  EVERESTIND  PYRAMID BUY ₹45.98 crore at ₹564.00 (box jump — doubling the stake with NEW capital; stop stays ₹510.10; charges ₹5.45 lakh)
2018-08-27  ABBOTINDIA  PYRAMID BUY ₹68.30 crore at ₹7,677.80 (box jump — doubling the stake with NEW capital; stop stays ₹7,130.70; charges ₹8.09 lakh)
2018-09-03  BAJFINANCE  PYRAMID BUY ₹143.34 crore at ₹2,880.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,683.56; charges ₹16.98 lakh)
2018-09-04  BAJFINANCE  SELL ₹266.70 crore at stop ₹2,683.56 (-5.4%, charges ₹27.66 lakh) — the cash goes back to work at the next Friday screen
2018-09-10  BBL         BUY ₹88.84 crore at ₹1,500.15 (fresh Friday signal — BUY: 9.73× weekly, month 1.54×, ladder rising; stop ₹1,217.66; charges ₹10.53 lakh)
2018-09-10  GLOBUSSPR   BUY ₹88.36 crore at ₹186.35 (fresh Friday signal — ACCUMULATE: 4.28× weekly, month 1.77×, ladder rising; stop ₹166.34; charges ₹10.47 lakh)
2018-09-10  MUTHOOTFIN  BUY ₹88.66 crore at ₹468.80 (fresh Friday signal — BUY: 6.85× weekly, month 1.77×, ladder rising; stop ₹370.50; charges ₹10.51 lakh)
2018-09-11  GLOBUSSPR   SELL ₹78.70 crore at stop ₹166.34 (-10.7%, charges ₹8.16 lakh) — the cash goes back to work at the next Friday screen
2018-09-12  ASTRAZEN    SELL ₹207.36 crore at stop ₹1,345.20 (+7.3%, charges ₹21.51 lakh) — the cash goes back to work at the next Friday screen
2018-09-17  JSWHL       BUY ₹84.83 crore at ₹2,358.85 (fresh Friday signal — ACCUMULATE: 2.15× weekly, month 2.26×, ladder rising; stop ₹2,044.64; charges ₹10.05 lakh)
2018-09-17  SUVEN       BUY ₹84.76 crore at ₹310.80 (fresh Friday signal — BUY: 2.23× weekly, month 3.48×, ladder rising; stop ₹244.67; charges ₹10.04 lakh)
2018-09-21  ABBOTINDIA  SELL ₹136.02 crore at stop ₹7,657.95 (+4.1%, charges ₹14.11 lakh) — the cash goes back to work at the next Friday screen
2018-09-21  EVERESTIND  SELL ₹83.03 crore at stop ₹510.10 (-7.7%, charges ₹8.61 lakh) — the cash goes back to work at the next Friday screen
2018-09-21  PEL         SELL ₹76.04 crore at stop ₹2,627.89 (-6.5%, charges ₹7.89 lakh) — the cash goes back to work at the next Friday screen
2018-09-21  SUVEN       SELL ₹66.57 crore at stop ₹244.67 (-21.3%, charges ₹6.91 lakh) — the cash goes back to work at the next Friday screen
2018-09-24  GUJFLUORO   BUY ₹86.75 crore at ₹854.00 (fresh Friday signal — ACCUMULATE: 2.91× weekly, month 1.88×, ladder rising; stop ₹775.25; charges ₹10.28 lakh)
2018-09-24  MUTHOOTFIN  PYRAMID BUY ₹85.39 crore at ₹452.00 (box jump — doubling the stake with NEW capital; stop stays ₹412.35; charges ₹10.12 lakh)
2018-09-25  MPHASIS     SELL ₹56.31 crore at stop ₹1,173.72 (+15.3%, charges ₹5.84 lakh) — the cash goes back to work at the next Friday screen
2018-09-27  BBL         SELL ₹71.95 crore at stop ₹1,217.66 (-18.8%, charges ₹7.46 lakh) — the cash goes back to work at the next Friday screen
2018-09-27  MUTHOOTFIN  SELL ₹155.54 crore at stop ₹412.35 (-10.4%, charges ₹16.13 lakh) — the cash goes back to work at the next Friday screen
2018-09-28  GUJFLUORO   SELL ₹78.58 crore at stop ₹775.25 (-9.2%, charges ₹8.15 lakh) — the cash goes back to work at the next Friday screen
2018-10-09  JSWHL       SELL ₹73.37 crore at stop ₹2,044.64 (-13.3%, charges ₹7.61 lakh) — the cash goes back to work at the next Friday screen
2018-10-15  BAJAJHIND   BUY ₹83.25 crore at ₹11.00 (fresh Friday signal — ACCUMULATE: 2.11× weekly, month 4.50×, ladder rising; stop ₹6.18; charges ₹9.86 lakh)
2018-10-22  HATHWAY     BUY ₹82.37 crore at ₹30.60 (fresh Friday signal — BUY: 3.56× weekly, month 1.61×, ladder rising; stop ₹18.96; charges ₹9.76 lakh)
2018-10-29  HATHWAY     PYRAMID BUY ₹81.34 crore at ₹30.25 (box jump — doubling the stake with NEW capital; stop stays ₹26.93; charges ₹9.64 lakh)
2018-12-03  GODFRYPHLP  BUY ₹91.04 crore at ₹928.40 (fresh Friday signal — BUY: 1.59× weekly, month 1.69×, ladder rising; stop ₹795.15; charges ₹10.79 lakh)
2018-12-03  KESORAMIND  BUY ₹90.37 crore at ₹85.00 (fresh Friday signal — BUY: 4.55× weekly, month 1.54×, ladder rising; stop ₹71.39; charges ₹10.71 lakh)
2018-12-17  BANKBEES    BUY ₹98.31 crore at ₹274.00 (fresh Friday signal — ACCUMULATE: 1.75× weekly, month 4.65×, ladder rising; stop ₹248.08; charges ₹11.65 lakh)
2018-12-17  GODFRYPHLP  PYRAMID BUY ₹90.89 crore at ₹928.00 (box jump — doubling the stake with NEW capital; stop stays ₹812.30; charges ₹10.77 lakh)
2018-12-24  BEML        BUY ₹97.65 crore at ₹890.10 (fresh Friday signal — BUY: 5.73× weekly, month 2.62×, ladder rising; stop ₹648.90; charges ₹11.57 lakh)
2018-12-26  GODFRYPHLP  SELL ₹158.86 crore at stop ₹812.30 (-12.5%, charges ₹16.48 lakh) — the cash goes back to work at the next Friday screen
2019-01-07  BANKBEES    PYRAMID BUY ₹100.22 crore at ₹279.65 (box jump — doubling the stake with NEW capital; stop stays ₹255.55; charges ₹11.87 lakh)
2019-01-07  BEML        PYRAMID BUY ₹98.18 crore at ₹896.00 (box jump — doubling the stake with NEW capital; stop stays ₹809.88; charges ₹11.63 lakh)
2019-01-14  BANKBEES    PYRAMID BUY ₹200.48 crore at ₹279.88 (box jump — doubling the stake with NEW capital; stop stays ₹260.57; charges ₹23.75 lakh)
2019-01-14  SKFINDIA    BUY ₹135.81 crore at ₹1,940.00 (fresh Friday signal — ACCUMULATE: 6.62× weekly, month 3.44×, ladder rising; stop ₹1,776.45; charges ₹16.09 lakh)
2019-01-14  SOMANYCERA  BUY ₹135.64 crore at ₹369.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 2.26×, ladder rising; stop ₹335.82; charges ₹16.07 lakh)
2019-01-21  BANKBEES    PYRAMID BUY ₹407.92 crore at ₹284.90 (box jump — doubling the stake with NEW capital; stop stays ₹263.25; charges ₹48.33 lakh)
2019-01-21  SPECIALITY  BUY ₹172.38 crore at ₹108.50 (fresh Friday signal — BUY: 26.29× weekly, month 3.83×, ladder rising; stop ₹73.15; charges ₹20.42 lakh)
2019-01-28  BEML        SELL ₹177.20 crore at stop ₹809.88 (-9.3%, charges ₹18.38 lakh) — the cash goes back to work at the next Friday screen
2019-01-28  SOMANYCERA  SELL ₹122.87 crore at stop ₹335.82 (-9.2%, charges ₹12.75 lakh) — the cash goes back to work at the next Friday screen
2019-01-29  KESORAMIND  SELL ₹75.73 crore at stop ₹71.39 (-16.0%, charges ₹7.86 lakh) — the cash goes back to work at the next Friday screen
2019-02-04  SPECIALITY  PYRAMID BUY ₹152.26 crore at ₹95.95 (box jump — doubling the stake with NEW capital; stop stays ₹78.76; charges ₹18.04 lakh)
2019-02-11  INFRATEL    BUY ₹183.35 crore at ₹326.00 (fresh Friday signal — BUY: 1.56× weekly, month 1.65×, ladder rising; stop ₹270.75; charges ₹21.72 lakh)
2019-02-18  YESBANK     BUY ₹178.20 crore at ₹201.00 (fresh Friday signal — BUY: 1.58× weekly, month 2.31×, ladder rising; stop ₹178.03; charges ₹21.11 lakh)
2019-02-19  HATHWAY     SELL ₹144.58 crore at stop ₹26.93 (-11.5%, charges ₹15.00 lakh) — the cash goes back to work at the next Friday screen
2019-02-25  INFRATEL    PYRAMID BUY ₹176.16 crore at ₹313.60 (box jump — doubling the stake with NEW capital; stop stays ₹277.35; charges ₹20.87 lakh)
2019-03-05  DHAMPURSUG  BUY ₹158.83 crore at ₹242.35 (fresh Friday signal — BUY: 3.72× weekly, month 1.52×, ladder rising; stop ₹198.55; charges ₹18.82 lakh)
2019-03-11  BAJAJHIND   PYRAMID BUY ₹67.66 crore at ₹8.95 (box jump — doubling the stake with NEW capital; stop stays ₹7.69; charges ₹8.02 lakh)
2019-03-11  DHAMPURSUG  PYRAMID BUY ₹151.93 crore at ₹232.10 (box jump — doubling the stake with NEW capital; stop stays ₹211.42; charges ₹18.00 lakh)
2019-03-11  SKFINDIA    PYRAMID BUY ₹136.70 crore at ₹1,955.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,828.80; charges ₹16.20 lakh)
2019-03-20  BAJAJHIND   SELL ₹116.08 crore at stop ₹7.69 (-22.9%, charges ₹12.04 lakh) — the cash goes back to work at the next Friday screen
2019-03-20  DHAMPURSUG  SELL ₹276.34 crore at stop ₹211.42 (-10.9%, charges ₹28.66 lakh) — the cash goes back to work at the next Friday screen
2019-03-25  JUSTDIAL    BUY ₹262.00 crore at ₹615.00 (fresh Friday signal — BUY: 3.82× weekly, month 1.70×, ladder rising; stop ₹467.69; charges ₹31.04 lakh)
2019-03-25  YESBANK     PYRAMID BUY ₹221.38 crore at ₹250.00 (box jump — doubling the stake with NEW capital; stop stays ₹229.71; charges ₹26.23 lakh)
2019-04-01  JUSTDIAL    PYRAMID BUY ₹260.40 crore at ₹611.95 (box jump — doubling the stake with NEW capital; stop stays ₹565.25; charges ₹30.85 lakh)
2019-04-01  TAX         FY2019 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹255.67 crore / LT ₹0.00)
2019-04-08  SKFINDIA    PYRAMID BUY ₹291.11 crore at ₹2,082.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,891.83; charges ₹34.49 lakh)
2019-04-15  YESBANK     PYRAMID BUY ₹475.16 crore at ₹268.45 (box jump — doubling the stake with NEW capital; stop stays ₹245.34; charges ₹56.30 lakh)
2019-04-22  JUSTDIAL    SELL ₹480.27 crore at stop ₹565.25 (-7.9%, charges ₹49.82 lakh) — the cash goes back to work at the next Friday screen
2019-04-22  YESBANK     SELL ₹867.09 crore at stop ₹245.34 (-0.7%, charges ₹89.94 lakh) — the cash goes back to work at the next Friday screen
2019-04-25  INFRATEL    SELL ₹311.09 crore at stop ₹277.35 (-13.3%, charges ₹32.27 lakh) — the cash goes back to work at the next Friday screen
2019-04-30  FLFL        BUY ₹347.29 crore at ₹483.00 (fresh Friday signal — ACCUMULATE: 1.61× weekly, month 1.89×, ladder rising; stop ₹434.20; charges ₹41.15 lakh)
2019-04-30  IBREALEST   BUY ₹349.89 crore at ₹125.40 (fresh Friday signal — ACCUMULATE: 3.85× weekly, month 3.02×, ladder rising; stop ₹91.19; charges ₹41.46 lakh)
2019-04-30  MTEDUCARE   BUY ₹347.17 crore at ₹85.85 (fresh Friday signal — BUY: 2.57× weekly, month 7.09×, ladder rising; stop ₹73.96; charges ₹41.13 lakh)
2019-04-30  ONGC        BUY ₹346.97 crore at ₹168.00 (fresh Friday signal — BUY: 2.93× weekly, month 1.91×, ladder rising; stop ₹147.44; charges ₹41.11 lakh)
2019-05-03  MTEDUCARE   SELL ₹298.43 crore at stop ₹73.96 (-13.8%, charges ₹30.96 lakh) — the cash goes back to work at the next Friday screen
2019-05-06  RUCHISOYA   BUY ₹342.68 crore at ₹9.10 (fresh Friday signal — BUY: 2.65× weekly, month 1.62×, ladder rising; stop ₹5.61; charges ₹40.60 lakh)
2019-05-08  SKFINDIA    SELL ₹527.97 crore at stop ₹1,891.83 (-6.1%, charges ₹54.77 lakh) — the cash goes back to work at the next Friday screen
2019-05-13  MTEDUCARE   BUY ₹323.36 crore at ₹94.20 (fresh Friday signal — BUY: 1.93× weekly, month 4.89×, ladder rising; stop ₹73.96; charges ₹38.31 lakh)
2019-05-14  IBREALEST   SELL ₹253.88 crore at stop ₹91.19 (-27.3%, charges ₹26.33 lakh) — the cash goes back to work at the next Friday screen
2019-05-16  FLFL        SELL ₹311.51 crore at stop ₹434.20 (-10.1%, charges ₹32.31 lakh) — the cash goes back to work at the next Friday screen
2019-05-17  MTEDUCARE   SELL ₹253.32 crore at stop ₹73.96 (-21.5%, charges ₹26.28 lakh) — the cash goes back to work at the next Friday screen
2019-05-20  ONGC        PYRAMID BUY ₹350.68 crore at ₹170.00 (box jump — doubling the stake with NEW capital; stop stays ₹152.81; charges ₹41.55 lakh)
2019-05-27  GRUH        BUY ₹360.78 crore at ₹313.00 (fresh Friday signal — ACCUMULATE: 6.22× weekly, month 1.85×, ladder rising; stop ₹265.98; charges ₹42.75 lakh)
2019-05-27  HEIDELBERG  BUY ₹361.78 crore at ₹206.20 (fresh Friday signal — BUY: 3.76× weekly, month 1.79×, ladder rising; stop ₹162.93; charges ₹42.86 lakh)
2019-05-27  INOXLEISUR  BUY ₹362.52 crore at ₹349.40 (fresh Friday signal — BUY: 2.36× weekly, month 1.76×, ladder rising; stop ₹282.15; charges ₹42.95 lakh)
2019-06-03  MAHSCOOTER  BUY ₹291.51 crore at ₹4,343.70 (fresh Friday signal — BUY: 3.58× weekly, month 1.65×, ladder rising; stop ₹3,431.88; charges ₹34.54 lakh)
2019-06-03  ONGC        PYRAMID BUY ₹713.32 crore at ₹173.00 (box jump — doubling the stake with NEW capital; stop stays ₹160.36; charges ₹84.52 lakh)
2019-06-10  MAHSCOOTER  PYRAMID BUY ₹291.93 crore at ₹4,355.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,952.00; charges ₹34.59 lakh)
2019-06-10  SPECIALITY  SELL ₹249.56 crore at stop ₹78.76 (-23.0%, charges ₹25.89 lakh) — the cash goes back to work at the next Friday screen
2019-06-24  INOXLEISUR  PYRAMID BUY ₹334.68 crore at ₹322.95 (box jump — doubling the stake with NEW capital; stop stays ₹291.23; charges ₹39.65 lakh)
2019-06-25  RUCHISOYA   SELL ₹210.79 crore at stop ₹5.61 (-38.4%, charges ₹21.86 lakh) — the cash goes back to work at the next Friday screen
2019-07-01  HEIDELBERG  PYRAMID BUY ₹342.69 crore at ₹195.55 (box jump — doubling the stake with NEW capital; stop stays ₹172.09; charges ₹40.60 lakh)
2019-07-01  MAHSCOOTER  PYRAMID BUY ₹617.01 crore at ₹4,605.05 (box jump — doubling the stake with NEW capital; stop stays ₹4,157.82; charges ₹73.10 lakh)
2019-07-01  ONGC        SELL ₹1,320.25 crore at stop ₹160.36 (-6.2%, charges ₹1.37 crore) — the cash goes back to work at the next Friday screen
2019-07-01  TRENT       BUY ₹460.35 crore at ₹448.00 (fresh Friday signal — BUY: 2.03× weekly, month 1.51×, ladder rising; stop ₹364.32; charges ₹54.54 lakh)
2019-07-08  HDFCMFGETF  BUY ₹543.99 crore at ₹3,110.00 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 1.57×, ladder rising; stop ₹2,862.02; charges ₹64.45 lakh)
2019-07-08  MAHSCOOTER  SELL ₹1,112.36 crore at stop ₹4,157.82 (-7.1%, charges ₹1.15 crore) — the cash goes back to work at the next Friday screen
2019-07-15  HEIDELBERG  PYRAMID BUY ₹693.55 crore at ₹198.00 (box jump — doubling the stake with NEW capital; stop stays ₹177.65; charges ₹82.17 lakh)
2019-07-15  KOTAKGOLD   BUY ₹660.36 crore at ₹301.80 (fresh Friday signal — ACCUMULATE: 1.58× weekly, month 1.61×, ladder rising; stop ₹275.74; charges ₹78.24 lakh)
2019-07-15  TRENT       PYRAMID BUY ₹470.27 crore at ₹458.20 (box jump — doubling the stake with NEW capital; stop stays ₹393.30; charges ₹55.72 lakh)
2019-07-22  BANKBEES    SELL ₹844.95 crore at stop ₹295.55 (+4.9%, charges ₹87.65 lakh) — the cash goes back to work at the next Friday screen
2019-07-23  GRUH        SELL ₹305.90 crore at stop ₹265.98 (-15.0%, charges ₹31.73 lakh) — the cash goes back to work at the next Friday screen
2019-07-30  TRENT       SELL ₹806.01 crore at stop ₹393.30 (-13.2%, charges ₹83.61 lakh) — the cash goes back to work at the next Friday screen
2019-07-31  INOXLEISUR  SELL ₹602.64 crore at stop ₹291.23 (-13.4%, charges ₹62.51 lakh) — the cash goes back to work at the next Friday screen
2019-08-05  KOTAKGOLD   PYRAMID BUY ₹694.00 crore at ₹317.55 (box jump — doubling the stake with NEW capital; stop stays ₹287.42; charges ₹82.23 lakh)
2019-08-13  BERGEPAINT  BUY ₹929.71 crore at ₹359.00 (fresh Friday signal — BUY: 2.99× weekly, month 1.66×, ladder rising; stop ₹311.22; charges ₹1.10 crore)
2019-08-13  GOLDBEES    BUY ₹930.78 crore at ₹3,290.05 (fresh Friday signal — BUY: 2.88× weekly, month 1.71×, ladder rising; stop ₹2,888.00; charges ₹1.10 crore)
2019-08-13  GOLDSHARE   BUY ₹928.80 crore at ₹3,311.00 (fresh Friday signal — BUY: 3.55× weekly, month 1.54×, ladder rising; stop ₹2,916.55; charges ₹1.10 crore)
2019-08-13  HDFCMFGETF  PYRAMID BUY ₹591.04 crore at ₹3,383.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,961.24; charges ₹70.03 lakh)
2019-08-13  KOTAKGOLD   PYRAMID BUY ₹1,476.30 crore at ₹337.95 (box jump — doubling the stake with NEW capital; stop stays ₹305.90; charges ₹1.75 crore)
2019-08-26  GOLDBEES    PYRAMID BUY ₹950.88 crore at ₹3,365.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,116.95; charges ₹1.13 crore)
2019-08-26  GOLDSHARE   PYRAMID BUY ₹955.74 crore at ₹3,411.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,124.26; charges ₹1.13 crore)
2019-08-26  HDFCMFGETF  PYRAMID BUY ₹1,213.90 crore at ₹3,476.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,204.40; charges ₹1.44 crore)
2019-08-26  KOTAKGOLD   PYRAMID BUY ₹2,995.38 crore at ₹343.05 (box jump — doubling the stake with NEW capital; stop stays ₹310.46; charges ₹3.55 crore)
2019-08-26  TRENT       BUY ₹998.47 crore at ₹480.00 (fresh Friday signal — BUY: 2.69× weekly, month 2.05×, ladder rising; stop ₹408.55; charges ₹1.18 crore)
2019-09-03  BERGEPAINT  PYRAMID BUY ₹954.86 crore at ₹369.15 (box jump — doubling the stake with NEW capital; stop stays ₹339.44; charges ₹1.13 crore)
2019-09-03  TRENT       PYRAMID BUY ₹973.81 crore at ₹468.70 (box jump — doubling the stake with NEW capital; stop stays ₹439.04; charges ₹1.15 crore)
2019-09-09  GOLDSHARE   PYRAMID BUY ₹1,926.54 crore at ₹3,440.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,263.34; charges ₹2.28 crore)
2019-09-17  TRENT       SELL ₹1,821.40 crore at stop ₹439.04 (-7.4%, charges ₹1.89 crore) — the cash goes back to work at the next Friday screen
2019-09-23  JKPAPER     BUY ₹1,821.40 crore at ₹137.85 (fresh Friday signal — ACCUMULATE: 3.84× weekly, month 2.27×, ladder rising; stop ₹118.84; charges ₹2.16 crore)
2019-10-07  JKPAPER     SELL ₹1,566.74 crore at stop ₹118.84 (-13.8%, charges ₹1.63 crore) — the cash goes back to work at the next Friday screen
2019-10-14  BERGEPAINT  PYRAMID BUY ₹2,473.96 crore at ₹478.50 (box jump — doubling the stake with NEW capital; stop stays ₹401.04; charges ₹2.93 crore)
2019-10-14  JBMA        BUY ₹1,566.74 crore at ₹239.00 (fresh Friday signal — BUY: 9.76× weekly, month 9.94×, ladder rising; stop ₹146.20; charges ₹1.86 crore)
2019-10-22  HDFCMFGETF  PYRAMID BUY ₹2,422.11 crore at ₹3,470.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,260.49; charges ₹2.87 crore)
2019-10-22  JBMA        PYRAMID BUY ₹1,447.03 crore at ₹221.00 (box jump — doubling the stake with NEW capital; stop stays ₹207.67; charges ₹1.71 crore)
2019-10-23  JBMA        SELL ₹2,715.06 crore at stop ₹207.67 (-9.7%, charges ₹2.82 crore) — the cash goes back to work at the next Friday screen
2019-10-29  GOLDBEES    PYRAMID BUY ₹1,928.25 crore at ₹3,414.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,189.29; charges ₹2.28 crore)
2019-10-29  TVTODAY     BUY ₹2,715.06 crore at ₹333.00 (fresh Friday signal — BUY: 3.77× weekly, month 2.07×, ladder rising; stop ₹275.74; charges ₹3.22 crore)
2019-11-04  BERGEPAINT  PYRAMID BUY ₹5,260.18 crore at ₹509.00 (box jump — doubling the stake with NEW capital; stop stays ₹451.25; charges ₹6.23 crore)
2019-12-02  TVTODAY     SELL ₹2,243.21 crore at stop ₹275.74 (-17.2%, charges ₹2.33 crore) — the cash goes back to work at the next Friday screen
2019-12-09  ASTRAZEN    BUY ₹2,243.21 crore at ₹2,124.00 (fresh Friday signal — BUY: 2.54× weekly, month 1.99×, ladder rising; stop ₹1,862.00; charges ₹2.66 crore)
2019-12-09  HEIDELBERG  SELL ₹1,242.50 crore at stop ₹177.65 (-10.9%, charges ₹1.29 crore) — the cash goes back to work at the next Friday screen
2019-12-16  ASTRAZEN    PYRAMID BUY ₹2,391.11 crore at ₹2,266.72 (box jump — doubling the stake with NEW capital; stop stays ₹2,006.40; charges ₹2.83 crore)
2019-12-19  GOLDBEES    SELL ₹3,596.80 crore at stop ₹3,189.29 (-5.4%, charges ₹3.73 crore) — the cash goes back to work at the next Friday screen
2019-12-23  GPIL        BUY ₹3,476.97 crore at ₹218.00 (fresh Friday signal — BUY: 7.46× weekly, month 1.91×, ladder rising; stop ₹142.34; charges ₹4.12 crore)
2020-01-06  ASTRAZEN    SELL ₹4,226.11 crore at stop ₹2,006.40 (-8.6%, charges ₹4.38 crore) — the cash goes back to work at the next Friday screen
2020-01-06  GPIL        PYRAMID BUY ₹3,982.62 crore at ₹250.00 (box jump — doubling the stake with NEW capital; stop stays ₹201.88; charges ₹4.72 crore)
2020-01-08  BERGEPAINT  SELL ₹9,990.86 crore at stop ₹484.17 (+4.1%, charges ₹10.36 crore) — the cash goes back to work at the next Friday screen
2020-01-13  ASAHISONG   BUY ₹4,631.71 crore at ₹161.00 (fresh Friday signal — ACCUMULATE: 5.09× weekly, month 3.88×, ladder rising; stop ₹138.84; charges ₹5.49 crore)
2020-01-13  GPIL        PYRAMID BUY ₹7,960.53 crore at ₹250.00 (box jump — doubling the stake with NEW capital; stop stays ₹223.25; charges ₹9.43 crore)
2020-01-13  HARITASEAT  BUY ₹4,641.43 crore at ₹505.00 (fresh Friday signal — BUY: 23.75× weekly, month 4.43×, ladder rising; stop ₹402.04; charges ₹5.50 crore)
2020-01-13  INDRAMEDCO  BUY ₹4,637.30 crore at ₹46.00 (fresh Friday signal — ACCUMULATE: 9.74× weekly, month 6.46×, ladder rising; stop ₹34.49; charges ₹5.49 crore)
2020-01-20  GOLDSHARE   PYRAMID BUY ₹3,974.04 crore at ₹3,550.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,348.80; charges ₹4.71 crore)
2020-01-22  GPIL        SELL ₹14,194.36 crore at stop ₹223.25 (-7.7%, charges ₹14.72 crore) — the cash goes back to work at the next Friday screen
2020-01-27  ASAHISONG   PYRAMID BUY ₹4,578.81 crore at ₹159.35 (box jump — doubling the stake with NEW capital; stop stays ₹148.58; charges ₹5.43 crore)
2020-01-27  ATULAUTO    BUY ₹5,357.06 crore at ₹265.75 (fresh Friday signal — BUY: 12.30× weekly, month 4.64×, ladder rising; stop ₹216.60; charges ₹6.35 crore)
2020-01-27  GRANULES    BUY ₹5,166.05 crore at ₹153.00 (fresh Friday signal — BUY: 4.69× weekly, month 2.63×, ladder rising; stop ₹112.10; charges ₹6.12 crore)
2020-01-27  INDOCO      BUY ₹5,340.12 crore at ₹221.00 (fresh Friday signal — ACCUMULATE: 7.37× weekly, month 4.15×, ladder rising; stop ₹199.59; charges ₹6.33 crore)
2020-01-30  ASAHISONG   SELL ₹8,524.79 crore at stop ₹148.58 (-7.2%, charges ₹8.84 crore) — the cash goes back to work at the next Friday screen
2020-02-03  AKZOINDIA   BUY ₹3,334.80 crore at ₹2,029.25 (fresh Friday signal — ACCUMULATE: 6.34× weekly, month 3.18×, ladder rising; stop ₹1,787.63; charges ₹3.95 crore)
2020-02-03  LAOPALA     BUY ₹5,189.98 crore at ₹178.20 (fresh Friday signal — BUY: 12.10× weekly, month 6.41×, ladder rising; stop ₹157.84; charges ₹6.15 crore)
2020-02-10  ATULAUTO    PYRAMID BUY ₹4,940.98 crore at ₹245.40 (box jump — doubling the stake with NEW capital; stop stays ₹217.66; charges ₹5.85 crore)
2020-02-10  GRANULES    PYRAMID BUY ₹5,463.46 crore at ₹162.00 (box jump — doubling the stake with NEW capital; stop stays ₹131.29; charges ₹6.47 crore)
2020-02-10  INDRAMEDCO  PYRAMID BUY ₹4,485.80 crore at ₹44.55 (box jump — doubling the stake with NEW capital; stop stays ₹40.23; charges ₹5.31 crore)
2020-02-10  LAOPALA     PYRAMID BUY ₹5,652.18 crore at ₹194.30 (box jump — doubling the stake with NEW capital; stop stays ₹165.00; charges ₹6.70 crore)
2020-02-24  GRANULES    PYRAMID BUY ₹12,275.38 crore at ₹182.10 (box jump — doubling the stake with NEW capital; stop stays ₹149.58; charges ₹14.54 crore)
2020-02-27  INDRAMEDCO  SELL ₹8,088.44 crore at stop ₹40.23 (-11.1%, charges ₹8.39 crore) — the cash goes back to work at the next Friday screen
2020-03-02  INDOCO      SELL ₹4,812.07 crore at stop ₹199.59 (-9.7%, charges ₹4.99 crore) — the cash goes back to work at the next Friday screen
2020-03-03  ATULAUTO    SELL ₹8,750.64 crore at stop ₹217.66 (-14.8%, charges ₹9.08 crore) — the cash goes back to work at the next Friday screen
2020-03-09  DEEPAKNTR   BUY ₹8,806.94 crore at ₹508.80 (fresh Friday signal — BUY: 2.89× weekly, month 3.36×, ladder rising; stop ₹356.25; charges ₹10.43 crore)
2020-03-09  HARITASEAT  PYRAMID BUY ₹4,110.37 crore at ₹447.75 (box jump — doubling the stake with NEW capital; stop stays ₹404.35; charges ₹4.87 crore)
2020-03-09  INDOCO      BUY ₹8,774.43 crore at ₹228.20 (fresh Friday signal — ACCUMULATE: 2.23× weekly, month 2.83×, ladder rising; stop ₹164.08; charges ₹10.40 crore)
2020-03-12  GRANULES    SELL ₹20,133.58 crore at stop ₹149.58 (-11.9%, charges ₹20.88 crore) — the cash goes back to work at the next Friday screen
2020-03-12  HARITASEAT  SELL ₹7,411.82 crore at stop ₹404.35 (-15.1%, charges ₹7.69 crore) — the cash goes back to work at the next Friday screen
2020-03-13  HDFCMFGETF  SELL ₹4,934.79 crore at stop ₹3,540.65 (+3.7%, charges ₹5.12 crore) — the cash goes back to work at the next Friday screen
2020-03-13  INDOCO      SELL ₹6,294.97 crore at stop ₹164.08 (-28.1%, charges ₹6.53 crore) — the cash goes back to work at the next Friday screen
2020-03-13  LAOPALA     SELL ₹9,584.06 crore at stop ₹165.00 (-11.4%, charges ₹9.94 crore) — the cash goes back to work at the next Friday screen
2020-03-17  GOLDSHARE   SELL ₹7,962.85 crore at stop ₹3,562.50 (+2.5%, charges ₹8.26 crore) — the cash goes back to work at the next Friday screen
2020-03-17  KOTAKGOLD   SELL ₹6,149.09 crore at stop ₹352.69 (+5.8%, charges ₹6.38 crore) — the cash goes back to work at the next Friday screen
2020-03-19  DEEPAKNTR   SELL ₹6,152.73 crore at stop ₹356.25 (-30.0%, charges ₹6.38 crore) — the cash goes back to work at the next Friday screen
2020-03-25  AKZOINDIA   SELL ₹2,931.21 crore at stop ₹1,787.63 (-11.9%, charges ₹3.04 crore) — the cash goes back to work at the next Friday screen
```
