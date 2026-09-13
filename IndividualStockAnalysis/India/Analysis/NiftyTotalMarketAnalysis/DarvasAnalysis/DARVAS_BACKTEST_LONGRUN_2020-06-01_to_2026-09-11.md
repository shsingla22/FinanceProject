# The Darvas screen, run for six years — 2020-06-01 → 2026-09-11

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2019-06-01 → 2026-09-11, 741 symbols, in `2019-06-01_to_2026-09-13/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **Two limits that cannot be engineered away:** the universe is TODAY'S NiftyTotalMarket constituents (survivorship bias flatters the early years), and Yahoo serves split-adjusted history. No slippage, stop exits at the stop price, fractional shares.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), best volume reaction first, at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with NEW capital.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled with FRESH MONEY from outside the portfolio, equal to the position's market value, at the next day's open. The new money never touches the portfolio's cash — fresh entries are never starved — and every injection is dated and logged, so the honest yardstick is the money-weighted return (XIRR), not a naive multiple. Each add-on is its own tax lot on its own holding clock; the ratcheted stop covers the whole enlarged position.

## The headline — XIRR is the honest yardstick

| Engine | Money put in (₹) | Final value (₹) | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | 8,426,516,662,722,397,995,008.00 (₹100 + ₹8,426,516,662,722,397,995,008.00 injected) | **8,972,316,222,477,184,270,336.00** | **+50.85%** |
| B: doubling, before charges and tax | 9,457,074,865,822,251,352,064.00 | 10,128,147,536,928,464,437,248.00 | +56.47% |
| **A: no doubling, NET of charges and tax** | 100.00 | **788.82** | **+39.04%** |
| A: no doubling, before charges and tax | 100.00 | 1,050.49 | +45.54% |
| Nifty 50 (pre-cost, pre-tax) | 100.00 | 230.70 | +14.27% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹6.38; unrealised gains in both end books carry further deferred liabilities.*

6.27 years, 328 weekly screens. Engine B injected new capital 488 times (gross run: 489); the complete dated injection list is in the blotter and the events CSV.

## Reality check — what doubling on EVERY jump actually demands

The rule was applied exactly as specified, and the arithmetic must be
read for what it is. Doubling with new capital on every box jump is
EXPONENTIAL twice over: within a position (13 jumps on TDPOWERSYS =
2¹³ ≈ 8,000× the first slice) and across the portfolio (a doubled
position that finally stops out turns its giant proceeds into internal
cash, which funds giant new entries — capped at 10% of a now-giant
book — and each of those doubles again). Starting from ₹100, the fresh
capital the rule demanded crossed:

| Cumulative new capital demanded | Reached by |
|---|---|
| ₹1,000 (10× the start) | 2020-09-07 — within 3 months |
| ₹1 lakh (1,000×) | 2021-03-15 |
| ₹1 crore (10⁵×) | 2021-09-20 |
| ₹100 crore (10⁷×) | 2022-06-20 |
| ₹1 lakh crore (10¹⁰×) | 2023-05-15 |
| 10¹⁵ ₹ (≈ India's entire market cap per ₹100 started) | 2024-02-26 |
| 10¹⁸ ₹ | 2025-05-19 |

No investor has this money, and no market absorbs it — beyond the
first year or two the simulation is arithmetic, not an implementable
strategy (and it assumes zero market impact throughout). **The one
scale-free, honest number is the XIRR: every rupee the rule called
for, weighted by how long it was invested, compounded at +50.85% a
year net — against +39.04% for the same skill without doubling.** The
doubling engine's edge is real on this window, but capturing it in
practice would require capping the add-ons long before the cascade —
the rule as stated cannot be funded past its opening years.

## What the frictions took (net runs)

| | Engine A: no doubling | Engine B: doubling |
|---|---:|---:|
| Transaction charges | ₹27.58 | ₹25,611,917,162,454,294,528.00 |
| Capital-gains tax paid | ₹120.33 | ₹0.00 |
| Tax accrued, final part-year | ₹6.38 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹6,471.72 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹23,484,685.65 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹43,231,489,295.72 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹84,147,275,976,707.69 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹82,018,571,248,192,768.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹20,012,987,126,820,765,696.00 / ₹0.00 |
| FY2027 (accrued) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹36,533,457,182,288,437,248.00 / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹51.45 | ₹0.00 | ₹10.2909 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹84.66 | ₹0.00 | ₹16.9329 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹83.74 | ₹4.00 | ₹17.2485 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹251.30 | ₹0.00 | ₹50.2609 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹65.15 | ₹36.67 | ₹17.6142 | ₹0.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹39.90 | ₹0.00 | ₹7.9809 | ₹0.00 / ₹0.00 |
| FY2027 (accrued) | — | ₹31.89 | ₹0.00 | ₹6.3789 | ₹0.00 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2020 (2020-12-24) | 149.03 | +49.0% | 14,434.28 | ₹12,403.12 | +84.2% | +35.6% |
| 2021 (2021-12-31) | 256.28 | +72.0% | 127,291,215.79 | ₹119,675,853.22 | +51.0% | +26.2% |
| 2022 (2022-12-30) | 316.25 | +23.4% | 102,649,202,644.95 | ₹95,188,751,937.09 | +55.4% | +4.3% |
| 2023 (2023-12-29) | 569.39 | +80.0% | 236,885,174,839,896.62 | ₹225,315,824,397,560.75 | +40.0% | +20.0% |
| 2024 (2024-12-27) | 661.71 | +16.2% | 232,606,141,881,398,688.00 | ₹239,165,057,576,473,280.00 | -22.7% | +9.6% |
| 2025 (2025-12-26) | 648.81 | -1.9% | 52,331,949,551,162,556,416.00 | ₹54,495,980,125,669,335,040.00 | -23.5% | +9.4% |
| 2026 (2026-09-11) | 788.82 | +21.6% | 8,972,316,222,477,185,318,912.00 | ₹8,371,781,292,128,019,152,896.00 | +31.2% | -10.2% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-8.6%** (A: -26.4%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **190 closed trades**: 22 winners (12%), average winner +4.2%, average loser -8.1% (returns per blended entry price).
- Best closed trade GNFC +13.4%; worst MAHABANK -27.1%.
- Median holding period 72 days.
- Cash share of equity averaged 15%; fully in cash 1 of 328 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

| Month-end screen | B equity (₹) | B injected so far | B cash | B positions | A equity (₹) |
|---|---:|---:|---:|---:|---:|
| 2020-06-26 | 152.23 | 45.02 | 0.00 | 10 | 104.31 |
| 2020-07-31 | 374.16 | 258.24 | 32.65 | 7 | 107.40 |
| 2020-08-28 | 975.83 | 847.28 | 0.04 | 8 | 119.98 |
| 2020-09-25 | 1,450.44 | 1,387.29 | 133.80 | 9 | 119.66 |
| 2020-10-30 | 3,431.92 | 3,215.25 | 257.21 | 9 | 125.57 |
| 2020-11-27 | 5,445.39 | 5,023.77 | 95.51 | 10 | 129.68 |
| 2020-12-24 | 14,434.28 | 12,403.12 | 3,542.61 | 8 | 149.03 |
| 2021-01-29 | 33,533.47 | 32,469.93 | 6,458.72 | 9 | 153.13 |
| 2021-02-26 | 75,190.67 | 73,756.93 | 24,258.27 | 7 | 164.84 |
| 2021-03-26 | 111,711.93 | 119,593.37 | 37,875.64 | 8 | 157.68 |
| 2021-04-30 | 226,514.17 | 220,779.45 | 12,107.50 | 10 | 160.88 |
| 2021-05-28 | 362,781.32 | 321,559.01 | 0.00 | 11 | 179.09 |
| 2021-06-25 | 978,967.12 | 853,724.15 | 15,024.82 | 10 | 195.71 |
| 2021-07-30 | 3,083,689.81 | 2,193,329.36 | 15,024.82 | 10 | 235.11 |
| 2021-08-27 | 6,580,456.82 | 6,100,196.63 | 3,212,503.61 | 6 | 225.77 |
| 2021-09-24 | 14,075,076.10 | 13,016,081.58 | 0.00 | 10 | 240.91 |
| 2021-10-29 | 31,512,752.36 | 31,902,278.97 | 10,669,568.93 | 7 | 238.34 |
| 2021-11-26 | 56,532,229.10 | 57,949,845.37 | 24,935,525.16 | 6 | 245.23 |
| 2021-12-31 | 127,291,215.79 | 119,688,256.34 | 0.00 | 10 | 256.28 |
| 2022-01-28 | 175,791,400.45 | 187,118,982.23 | 111,524,153.17 | 5 | 236.92 |
| 2022-02-25 | 227,906,346.35 | 253,595,526.29 | 125,215,530.07 | 4 | 222.22 |
| 2022-03-25 | 280,407,187.64 | 274,170,258.28 | 125,215,530.07 | 4 | 244.79 |
| 2022-04-29 | 607,841,757.90 | 532,583,404.90 | 0.00 | 8 | 261.86 |
| 2022-05-27 | 695,610,950.51 | 627,517,164.89 | 106,624,382.55 | 6 | 249.20 |
| 2022-06-24 | 1,046,465,199.19 | 1,014,673,684.92 | 13,184,386.42 | 7 | 245.76 |
| 2022-07-29 | 2,629,983,098.71 | 2,294,727,053.09 | 0.00 | 7 | 274.24 |
| 2022-08-26 | 6,356,823,080.88 | 5,842,963,190.52 | 1,949,497,607.04 | 5 | 293.42 |
| 2022-09-30 | 11,718,318,770.75 | 11,165,055,119.70 | 1,073,779,961.78 | 7 | 300.55 |
| 2022-10-28 | 25,538,486,157.54 | 24,691,068,564.92 | 0.00 | 8 | 299.16 |
| 2022-11-25 | 54,956,297,748.29 | 55,121,504,414.45 | 26,753,940,540.31 | 7 | 312.77 |
| 2022-12-30 | 102,649,202,644.95 | 95,308,440,193.44 | 46,898,573,962.08 | 6 | 316.25 |
| 2023-01-27 | 147,029,544,583.61 | 148,296,249,538.30 | 11,566,838,964.35 | 8 | 312.11 |
| 2023-02-24 | 246,192,622,879.52 | 254,325,442,505.24 | 55,351,945,998.00 | 7 | 307.72 |
| 2023-03-31 | 533,214,378,021.32 | 575,211,970,798.85 | 264,268,377,981.90 | 5 | 297.19 |
| 2023-04-28 | 771,394,003,530.03 | 798,795,191,032.21 | 320,629,708,256.86 | 7 | 299.95 |
| 2023-05-26 | 1,366,211,617,176.58 | 1,305,180,212,789.16 | 58,838,675,024.19 | 10 | 319.09 |
| 2023-06-30 | 3,357,100,599,843.19 | 2,992,204,454,262.91 | 44,284,836,954.59 | 10 | 355.41 |
| 2023-07-28 | 7,807,295,291,396.57 | 7,116,935,237,773.05 | 104,965,220,825.30 | 9 | 408.13 |
| 2023-08-25 | 13,267,649,856,250.51 | 12,485,762,050,949.33 | 498,768,729,730.93 | 8 | 411.51 |
| 2023-09-29 | 27,872,227,777,794.80 | 25,789,942,807,722.55 | 498,768,729,730.93 | 8 | 442.41 |
| 2023-10-27 | 43,128,023,933,112.30 | 43,281,991,208,605.34 | 15,207,847,238,078.00 | 7 | 445.22 |
| 2023-11-24 | 145,450,156,311,480.06 | 141,828,373,654,094.28 | 2,188,485,365,961.38 | 10 | 545.23 |
| 2023-12-29 | 236,885,174,839,896.62 | 225,411,132,837,754.19 | 2,188,485,365,961.38 | 10 | 569.39 |
| 2024-01-25 | 433,130,976,593,801.75 | 404,340,948,225,290.12 | 91,028,595,999,016.31 | 8 | 637.42 |
| 2024-02-23 | 881,360,449,600,045.25 | 792,504,846,816,420.12 | 22,826,326,536,638.23 | 9 | 721.84 |
| 2024-03-28 | 1,348,840,473,531,552.00 | 1,332,155,448,045,325.50 | 0.00 | 11 | 714.58 |
| 2024-04-26 | 1,955,999,996,845,619.50 | 1,878,103,495,618,467.25 | 0.00 | 11 | 691.03 |
| 2024-05-31 | 3,922,459,669,381,457.00 | 3,917,454,031,179,383.00 | 517,304,914,936,162.19 | 10 | 667.04 |
| 2024-06-28 | 6,241,840,867,920,569.00 | 6,367,707,603,816,932.00 | 0.00 | 9 | 655.80 |
| 2024-07-26 | 10,762,560,880,377,780.00 | 10,715,213,905,140,158.00 | 2,331,935,959,911,033.00 | 7 | 679.15 |
| 2024-08-30 | 25,550,740,756,901,284.00 | 25,206,316,468,655,212.00 | 0.00 | 9 | 719.51 |
| 2024-09-27 | 37,055,344,629,531,088.00 | 38,853,093,644,020,888.00 | 6,052,918,781,010,921.00 | 7 | 696.12 |
| 2024-10-25 | 47,828,337,801,626,080.00 | 54,250,083,714,881,856.00 | 11,035,824,166,672,404.00 | 6 | 624.52 |
| 2024-11-29 | 113,406,495,806,450,544.00 | 112,783,529,391,500,192.00 | 0.00 | 8 | 671.33 |
| 2024-12-27 | 232,606,141,881,398,688.00 | 239,390,468,709,311,040.00 | 70,737,169,641,485,376.00 | 6 | 661.71 |
| 2025-01-24 | 401,981,894,398,188,416.00 | 463,053,332,309,062,848.00 | 264,782,848,439,311,808.00 | 4 | 598.60 |
| 2025-02-28 | 419,224,697,780,710,208.00 | 501,847,195,763,322,368.00 | 364,055,952,731,228,544.00 | 2 | 561.04 |
| 2025-03-28 | 522,656,066,925,416,960.00 | 590,444,163,487,402,752.00 | 269,918,010,682,524,096.00 | 4 | 576.77 |
| 2025-04-25 | 601,248,837,333,521,920.00 | 657,878,978,414,023,040.00 | 212,804,217,730,625,984.00 | 5 | 567.84 |
| 2025-05-30 | 1,144,525,317,583,458,688.00 | 1,167,600,501,557,265,920.00 | 0.00 | 9 | 605.96 |
| 2025-06-27 | 2,278,787,337,383,369,984.00 | 2,122,459,471,699,632,640.00 | 0.00 | 9 | 655.25 |
| 2025-07-25 | 10,575,331,378,301,325,312.00 | 9,553,636,704,897,474,560.00 | 0.00 | 9 | 745.37 |
| 2025-08-29 | 12,717,688,650,230,980,608.00 | 11,285,193,049,247,913,984.00 | 1,374,920,975,629,605,376.00 | 6 | 745.56 |
| 2025-09-26 | 13,522,152,547,717,535,744.00 | 12,807,716,732,718,782,464.00 | 1,479,402,401,278,626,048.00 | 5 | 702.19 |
| 2025-10-31 | 22,450,713,252,365,172,736.00 | 23,057,406,418,242,166,784.00 | 7,678,862,522,794,853,376.00 | 6 | 672.46 |
| 2025-11-28 | 32,296,654,607,998,083,072.00 | 34,171,960,280,982,822,912.00 | 10,403,940,847,155,544,064.00 | 8 | 662.80 |
| 2025-12-26 | 52,331,949,551,162,556,416.00 | 54,735,370,594,378,653,696.00 | 0.00 | 11 | 648.81 |
| 2026-01-30 | 85,058,161,330,030,788,608.00 | 89,968,835,897,848,184,832.00 | 34,067,455,543,449,149,440.00 | 5 | 622.61 |
| 2026-02-27 | 146,170,102,083,159,359,488.00 | 152,343,205,167,190,900,736.00 | 37,776,863,729,103,912,960.00 | 5 | 620.86 |
| 2026-03-27 | 216,565,367,787,674,697,728.00 | 233,356,468,931,941,761,024.00 | 78,038,993,472,430,850,048.00 | 5 | 592.70 |
| 2026-04-24 | 318,397,035,910,434,914,304.00 | 301,175,331,733,243,428,864.00 | 2,908,185,451,711,135,744.00 | 7 | 620.65 |
| 2026-05-29 | 1,033,586,919,583,819,628,544.00 | 955,701,541,504,109,117,440.00 | 0.00 | 10 | 641.48 |
| 2026-06-26 | 1,938,711,372,195,423,584,256.00 | 1,824,291,378,435,897,425,920.00 | 81,603,245,148,355,723,264.00 | 8 | 665.71 |
| 2026-07-31 | 4,684,065,457,106,355,486,720.00 | 4,654,717,000,128,999,194,624.00 | 369,662,256,518,096,879,616.00 | 7 | 721.02 |
| 2026-08-28 | 7,167,383,055,421,885,382,656.00 | 7,011,976,869,587,651,133,440.00 | 0.00 | 8 | 750.33 |
| 2026-09-11 | 8,972,316,222,477,185,318,912.00 | 8,426,516,662,722,397,995,008.00 | 640,336,179,204,409,393,152.00 | 7 | 788.82 |

## Engine B — still held at the end

| Stock | First entry | Blended entry ₹ | Lots | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|---:|
| ABB | 2026-02-23 | 7,154.79 | 6 | 7,274.00 | 7,158.25 | +1.7% |
| CAPLIPOINT | 2026-05-18 | 2,537.56 | 6 | 2,754.90 | 2,376.52 | +8.6% |
| CHENNPETRO | 2026-04-06 | 1,278.53 | 5 | 1,572.90 | 1,242.60 | +23.0% |
| CRAFTSMAN | 2026-05-11 | 10,402.63 | 5 | 11,669.00 | 10,380.65 | +12.2% |
| SPARC | 2026-05-11 | 199.71 | 5 | 196.01 | 185.03 | -1.9% |
| TMB | 2026-08-03 | 872.44 | 2 | 910.90 | 796.29 | +4.4% |
| WOCKPHARMA | 2026-05-11 | 1,999.85 | 5 | 2,179.40 | 1,741.63 | +9.0% |

## Engine B — every closed trade

*Returns are on the blended entry price across lots.*

| Stock | First entry | Blended ₹ | Lots | Exit | Exit ₹ | Return |
|---|---|---:|---:|---|---:|---:|
| IGL | 2020-06-08 | 247.75 | 1 | 2020-07-07 | 208.81 | -15.7% |
| RELAXO | 2020-06-08 | 759.45 | 1 | 2020-07-28 | 603.77 | -20.5% |
| LLOYDSENGG | 2020-06-08 | 0.96 | 2 | 2020-07-31 | 0.71 | -26.2% |
| EIDPARRY | 2020-06-08 | 275.79 | 4 | 2020-08-17 | 273.03 | -1.0% |
| GRANULES | 2020-06-15 | 291.63 | 5 | 2020-08-31 | 286.95 | -1.6% |
| ZENTEC | 2020-08-03 | 74.64 | 2 | 2020-08-31 | 80.56 | +7.9% |
| KIRLOSBROS | 2020-06-08 | 130.23 | 5 | 2020-09-08 | 120.79 | -7.2% |
| RCF | 2020-06-08 | 49.84 | 6 | 2020-09-09 | 45.84 | -8.0% |
| SCHAEFFLER | 2020-09-14 | 814.00 | 1 | 2020-09-23 | 724.67 | -11.0% |
| INDIAMART | 2020-09-07 | 2,421.33 | 3 | 2020-10-19 | 2,315.62 | -4.4% |
| CAPLIPOINT | 2020-06-15 | 546.03 | 4 | 2020-10-30 | 498.06 | -8.8% |
| GLAXO | 2020-09-14 | 1,622.53 | 2 | 2020-11-02 | 1,441.55 | -11.2% |
| ADVENZYMES | 2020-06-15 | 270.24 | 5 | 2020-11-03 | 292.33 | +8.2% |
| THYROCARE | 2020-08-24 | 340.16 | 4 | 2020-11-12 | 338.83 | -0.4% |
| ATGL | 2020-09-14 | 326.44 | 5 | 2020-12-21 | 332.60 | +1.9% |
| SYNGENE | 2020-06-08 | 563.99 | 5 | 2020-12-22 | 562.40 | -0.3% |
| BORORENEW | 2020-11-09 | 226.99 | 5 | 2021-01-20 | 247.59 | +9.1% |
| JUSTDIAL | 2020-10-26 | 638.47 | 3 | 2021-01-25 | 622.35 | -2.5% |
| PIIND | 2020-11-17 | 2,348.20 | 1 | 2021-01-25 | 2,107.67 | -10.2% |
| LINDEINDIA | 2020-09-21 | 938.47 | 5 | 2021-01-27 | 898.70 | -4.2% |
| HCLTECH | 2020-09-28 | 924.10 | 4 | 2021-01-29 | 928.05 | +0.4% |
| TRENT | 2020-11-17 | 725.02 | 2 | 2021-01-29 | 626.30 | -13.6% |
| TATAELXSI | 2021-01-25 | 2,755.37 | 3 | 2021-02-22 | 2,660.00 | -3.5% |
| GAEL | 2021-02-01 | 71.47 | 1 | 2021-02-23 | 62.70 | -12.3% |
| KPRMILL | 2020-11-02 | 177.82 | 5 | 2021-02-24 | 166.62 | -6.3% |
| INDIAMART | 2021-01-25 | 4,296.73 | 3 | 2021-03-02 | 4,137.25 | -3.7% |
| GRAVITA | 2020-12-28 | 90.90 | 3 | 2021-03-17 | 96.13 | +5.8% |
| RCF | 2021-03-01 | 82.90 | 2 | 2021-03-17 | 79.16 | -4.5% |
| HINDZINC | 2021-01-25 | 288.74 | 2 | 2021-03-19 | 279.30 | -3.3% |
| MAHABANK | 2021-03-01 | 25.20 | 1 | 2021-03-19 | 18.37 | -27.1% |
| HONAUT | 2020-12-28 | 45,115.22 | 5 | 2021-03-22 | 41,911.15 | -7.1% |
| WHIRLPOOL | 2021-01-25 | 2,697.50 | 1 | 2021-03-24 | 2,244.99 | -16.8% |
| AUBANK | 2021-04-05 | 631.00 | 1 | 2021-04-12 | 533.06 | -15.5% |
| IOB | 2021-03-01 | 17.88 | 2 | 2021-04-28 | 14.82 | -17.1% |
| POLYMED | 2020-09-07 | 931.08 | 7 | 2021-06-14 | 950.00 | +2.0% |
| SJVN | 2021-03-08 | 27.77 | 3 | 2021-08-10 | 26.98 | -2.9% |
| WELSPUNLIV | 2021-03-22 | 128.22 | 6 | 2021-08-10 | 124.64 | -2.8% |
| MARKSANS | 2021-05-03 | 82.11 | 4 | 2021-08-10 | 77.14 | -6.1% |
| JSWENERGY | 2021-03-08 | 204.59 | 8 | 2021-08-11 | 228.00 | +11.4% |
| GICRE | 2021-04-05 | 204.95 | 2 | 2021-08-11 | 164.12 | -19.9% |
| KPRMILL | 2021-04-19 | 359.48 | 5 | 2021-08-11 | 352.48 | -1.9% |
| KEI | 2021-03-22 | 889.48 | 9 | 2021-10-22 | 853.10 | -4.1% |
| TDPOWERSYS | 2021-09-06 | 33.57 | 3 | 2021-10-22 | 30.53 | -9.1% |
| NEOGEN | 2021-09-13 | 1,232.52 | 3 | 2021-10-25 | 1,142.85 | -7.3% |
| HAL | 2021-09-06 | 716.75 | 3 | 2021-10-28 | 636.50 | -11.2% |
| DEEPAKFERT | 2021-03-22 | 399.71 | 7 | 2021-11-11 | 385.70 | -3.5% |
| GRAVITA | 2021-08-23 | 205.54 | 3 | 2021-11-22 | 197.03 | -4.1% |
| TATAINVEST | 2021-08-16 | 148.37 | 6 | 2021-11-26 | 143.65 | -3.2% |
| NHPC | 2021-09-06 | 32.11 | 5 | 2021-11-29 | 30.11 | -6.2% |
| KPITTECH | 2021-03-30 | 443.19 | 8 | 2021-12-20 | 458.85 | +3.5% |
| UNOMINDA | 2021-12-27 | 602.46 | 2 | 2022-01-07 | 544.21 | -9.7% |
| LTM | 2021-10-25 | 6,583.76 | 3 | 2022-01-24 | 6,270.00 | -4.8% |
| PERSISTENT | 2021-11-01 | 2,194.94 | 3 | 2022-01-24 | 2,067.34 | -5.8% |
| PGEL | 2021-12-06 | 75.43 | 3 | 2022-01-24 | 72.44 | -4.0% |
| GOKULAGRO | 2021-11-15 | 35.42 | 3 | 2022-01-25 | 35.00 | -1.2% |
| AFFLE | 2022-01-10 | 1,399.94 | 2 | 2022-01-25 | 1,206.50 | -13.8% |
| SHARDACROP | 2022-01-31 | 623.38 | 2 | 2022-02-11 | 545.30 | -12.5% |
| GABRIEL | 2021-01-25 | 137.16 | 5 | 2022-02-14 | 125.40 | -8.6% |
| BSOFT | 2021-11-29 | 475.09 | 2 | 2022-02-14 | 424.65 | -10.6% |
| CHAMBLFERT | 2021-12-06 | 395.93 | 2 | 2022-02-24 | 353.85 | -10.6% |
| CCL | 2022-02-07 | 484.29 | 2 | 2022-02-24 | 441.75 | -8.8% |
| ESCORTS | 2021-11-29 | 1,870.85 | 3 | 2022-02-25 | 1,754.65 | -6.2% |
| RCF | 2022-04-04 | 100.30 | 2 | 2022-05-04 | 93.15 | -7.1% |
| GNFC | 2022-02-14 | 698.36 | 3 | 2022-05-06 | 792.16 | +13.4% |
| BSE | 2021-12-06 | 252.21 | 3 | 2022-05-10 | 255.87 | +1.5% |
| MINDACORP | 2022-04-11 | 230.05 | 1 | 2022-05-11 | 186.63 | -18.9% |
| SPLPETRO | 2022-04-04 | 467.83 | 2 | 2022-05-24 | 424.27 | -9.3% |
| MRPL | 2022-05-09 | 87.37 | 3 | 2022-07-06 | 69.61 | -20.3% |
| VBL | 2022-05-16 | 185.59 | 5 | 2022-08-22 | 188.52 | +1.6% |
| BLS | 2022-04-11 | 107.06 | 5 | 2022-08-23 | 110.67 | +3.4% |
| HOMEFIRST | 2022-08-29 | 944.95 | 1 | 2022-09-14 | 849.35 | -10.1% |
| SIEMENS | 2022-08-29 | 1,712.60 | 2 | 2022-09-26 | 1,618.44 | -5.5% |
| TSFINV | 2022-10-03 | 101.48 | 2 | 2022-10-11 | 92.20 | -9.1% |
| ADANIPOWER | 2022-02-21 | 69.42 | 6 | 2022-10-14 | 66.80 | -3.8% |
| KALYANKJIL | 2022-08-29 | 101.45 | 6 | 2022-11-22 | 94.53 | -6.8% |
| ELECON | 2022-06-13 | 197.22 | 7 | 2022-12-21 | 202.49 | +2.7% |
| MAHSCOOTER | 2022-09-19 | 5,050.81 | 2 | 2022-12-22 | 4,617.00 | -8.6% |
| ACC | 2022-05-23 | 2,504.26 | 8 | 2022-12-23 | 2,465.15 | -1.6% |
| IRFC | 2022-11-28 | 32.15 | 2 | 2022-12-23 | 28.20 | -12.3% |
| APOLLO | 2022-10-17 | 24.32 | 3 | 2022-12-26 | 24.42 | +0.4% |
| GODFRYPHLP | 2022-10-24 | 579.21 | 3 | 2022-12-26 | 547.85 | -5.4% |
| TIINDIA | 2022-07-25 | 2,675.28 | 5 | 2023-01-11 | 2,598.35 | -2.9% |
| SKIPPER | 2022-11-28 | 105.43 | 2 | 2023-01-25 | 109.70 | +4.1% |
| GICRE | 2023-01-02 | 183.12 | 2 | 2023-02-01 | 167.72 | -8.4% |
| LLOYDSENGG | 2023-01-02 | 18.32 | 2 | 2023-02-07 | 19.27 | +5.2% |
| CGCL | 2022-02-21 | 672.85 | 3 | 2023-03-08 | 666.82 | -0.9% |
| ANUP | 2023-01-16 | 553.52 | 4 | 2023-03-10 | 527.27 | -4.7% |
| YESBANK | 2023-01-02 | 18.95 | 2 | 2023-03-13 | 15.34 | -19.1% |
| IOB | 2022-11-28 | 26.90 | 4 | 2023-03-20 | 22.18 | -17.5% |
| UCOBANK | 2022-11-28 | 27.06 | 3 | 2023-03-27 | 23.46 | -13.3% |
| JINDALSAW | 2023-02-06 | 69.60 | 2 | 2023-03-27 | 67.92 | -2.4% |
| SONATSOFTW | 2023-02-27 | 401.31 | 4 | 2023-03-29 | 371.45 | -7.4% |
| CERA | 2023-02-27 | 6,401.92 | 4 | 2023-04-26 | 6,037.30 | -5.7% |
| KIRLOSBROS | 2023-04-10 | 428.67 | 2 | 2023-04-26 | 403.85 | -5.8% |
| MARKSANS | 2023-04-24 | 78.00 | 1 | 2023-05-22 | 71.87 | -7.9% |
| ASHAPURMIN | 2023-05-02 | 136.95 | 3 | 2023-05-29 | 134.24 | -2.0% |
| MAHABANK | 2022-11-28 | 28.71 | 4 | 2023-06-15 | 27.79 | -3.2% |
| ANURAS | 2023-03-20 | 1,058.50 | 3 | 2023-07-03 | 1,007.67 | -4.8% |
| KSB | 2023-03-27 | 435.68 | 2 | 2023-07-12 | 407.74 | -6.4% |
| REFEX | 2023-05-02 | 128.05 | 4 | 2023-08-11 | 121.69 | -5.0% |
| EPL | 2023-06-05 | 212.65 | 3 | 2023-08-11 | 200.50 | -5.7% |
| CEATLTD | 2023-07-10 | 2,430.04 | 2 | 2023-08-14 | 2,244.85 | -7.6% |
| FORCEMOT | 2023-06-05 | 3,643.32 | 6 | 2023-10-20 | 3,709.99 | +1.8% |
| HEG | 2023-05-08 | 348.40 | 6 | 2023-10-23 | 328.78 | -5.6% |
| HAL | 2023-04-03 | 1,897.06 | 6 | 2023-10-25 | 1,840.70 | -3.0% |
| VARROC | 2023-08-14 | 452.86 | 4 | 2023-10-25 | 450.92 | -0.4% |
| ANGELONE | 2023-10-30 | 326.65 | 5 | 2024-01-23 | 296.88 | -9.1% |
| CRISIL | 2023-10-23 | 4,220.84 | 2 | 2024-01-24 | 3,861.80 | -8.5% |
| ZFCVINDIA | 2023-04-24 | 2,491.13 | 7 | 2024-02-02 | 2,473.96 | -0.7% |
| APOLLO | 2023-10-23 | 126.02 | 5 | 2024-02-13 | 112.10 | -11.0% |
| SHAREINDIA | 2023-10-30 | 374.47 | 6 | 2024-03-06 | 357.20 | -4.6% |
| RATEGAIN | 2023-08-14 | 805.48 | 8 | 2024-03-13 | 730.99 | -9.2% |
| RITES | 2024-01-29 | 361.29 | 2 | 2024-03-13 | 314.37 | -13.0% |
| PRUDENT | 2024-02-19 | 1,357.01 | 2 | 2024-03-13 | 1,176.05 | -13.3% |
| FORCEMOT | 2024-03-18 | 8,659.96 | 3 | 2024-05-28 | 8,083.65 | -6.7% |
| CUPID | 2023-10-30 | 18.63 | 5 | 2024-06-04 | 17.77 | -4.6% |
| IDBI | 2024-01-29 | 86.54 | 4 | 2024-06-04 | 78.19 | -9.7% |
| SOLARINDS | 2024-03-11 | 8,256.59 | 2 | 2024-06-04 | 7,980.95 | -3.3% |
| BHEL | 2024-03-11 | 285.48 | 2 | 2024-06-04 | 251.68 | -11.8% |
| JIOFIN | 2024-03-18 | 353.48 | 3 | 2024-06-04 | 317.61 | -10.1% |
| BOSCHLTD | 2024-03-18 | 30,663.27 | 4 | 2024-06-04 | 29,015.09 | -5.4% |
| ICICIBANK | 2023-05-02 | 1,087.79 | 8 | 2024-06-05 | 1,051.37 | -3.3% |
| TDPOWERSYS | 2023-03-27 | 190.09 | 11 | 2024-07-19 | 188.72 | -0.7% |
| UNOMINDA | 2024-06-10 | 1,093.79 | 3 | 2024-07-19 | 981.87 | -10.2% |
| FIEMIND | 2024-06-10 | 1,301.09 | 3 | 2024-07-23 | 1,257.56 | -3.3% |
| NCC | 2024-06-10 | 322.05 | 2 | 2024-07-23 | 297.87 | -7.5% |
| NBCC | 2023-10-23 | 111.18 | 9 | 2024-08-06 | 109.78 | -1.3% |
| ADANIPOWER | 2024-06-10 | 156.60 | 1 | 2024-08-12 | 126.55 | -19.2% |
| CAMPUS | 2024-06-03 | 289.67 | 3 | 2024-08-16 | 277.07 | -4.4% |
| AVANTIFEED | 2024-07-29 | 711.41 | 3 | 2024-09-09 | 650.13 | -8.6% |
| CERA | 2024-08-12 | 10,499.95 | 1 | 2024-09-19 | 8,198.93 | -21.9% |
| PGIL | 2024-07-22 | 465.02 | 3 | 2024-09-23 | 434.53 | -6.6% |
| DABUR | 2024-06-10 | 635.27 | 4 | 2024-10-03 | 602.49 | -5.2% |
| VGUARD | 2024-08-19 | 524.15 | 1 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 4,473.62 | 6 | 2024-10-07 | 4,485.14 | +0.3% |
| THYROCARE | 2024-07-29 | 272.95 | 3 | 2024-10-07 | 265.38 | -2.8% |
| VIYASH | 2024-09-30 | 203.76 | 2 | 2024-10-23 | 172.84 | -15.2% |
| INDIAGLYCO | 2024-07-22 | 597.10 | 3 | 2024-10-25 | 587.91 | -1.5% |
| SUPRIYA | 2024-08-19 | 735.07 | 6 | 2024-12-17 | 717.25 | -2.4% |
| KIRLPNU | 2024-11-04 | 846.98 | 3 | 2024-12-23 | 798.00 | -5.8% |
| PRSMJOHNSN | 2024-09-16 | 201.38 | 3 | 2024-12-26 | 170.55 | -15.3% |
| JSWDULUX | 2024-11-04 | 4,118.82 | 2 | 2024-12-27 | 3,423.18 | -16.9% |
| PAYTM | 2024-10-14 | 976.31 | 6 | 2025-01-09 | 893.05 | -8.5% |
| SKIPPER | 2024-10-14 | 553.34 | 3 | 2025-01-10 | 477.28 | -13.7% |
| KAYNES | 2024-12-23 | 7,223.56 | 2 | 2025-01-10 | 6,670.80 | -7.7% |
| ZENTEC | 2024-12-23 | 2,544.24 | 2 | 2025-01-13 | 2,213.55 | -13.0% |
| KFINTECH | 2024-12-30 | 1,511.45 | 1 | 2025-01-15 | 1,159.14 | -23.3% |
| AEGISLOG | 2025-01-13 | 819.14 | 2 | 2025-01-24 | 700.36 | -14.5% |
| LLOYDSME | 2025-01-06 | 1,440.45 | 2 | 2025-01-28 | 1,258.75 | -12.6% |
| APOLLO | 2025-01-20 | 131.50 | 1 | 2025-02-17 | 110.19 | -16.2% |
| ZENSARTECH | 2025-02-03 | 933.54 | 2 | 2025-02-17 | 814.20 | -12.8% |
| BSE | 2024-10-07 | 1,610.94 | 3 | 2025-02-28 | 1,651.54 | +2.5% |
| INDIASHLTR | 2025-03-24 | 812.35 | 2 | 2025-04-07 | 738.82 | -9.1% |
| CEMPRO | 2024-10-07 | 554.03 | 4 | 2025-04-11 | 524.92 | -5.3% |
| PARAS | 2025-05-05 | 759.21 | 3 | 2025-07-28 | 708.99 | -6.6% |
| NH | 2025-03-03 | 1,957.82 | 5 | 2025-08-04 | 1,814.78 | -7.3% |
| WHIRLPOOL | 2025-04-28 | 1,329.25 | 4 | 2025-08-07 | 1,301.97 | -2.1% |
| RAIN | 2025-08-11 | 160.25 | 1 | 2025-08-26 | 143.64 | -10.4% |
| INDIASHLTR | 2025-04-15 | 915.18 | 4 | 2025-09-25 | 862.60 | -5.7% |
| SMLMAH | 2025-04-28 | 3,494.07 | 4 | 2025-09-26 | 3,255.67 | -6.8% |
| FORCEMOT | 2025-04-28 | 15,838.14 | 7 | 2025-10-09 | 15,350.10 | -3.1% |
| SUBROS | 2025-09-29 | 1,103.63 | 2 | 2025-10-14 | 1,046.90 | -5.1% |
| CREDITACC | 2025-01-27 | 1,321.25 | 7 | 2025-10-20 | 1,274.42 | -3.5% |
| GALLANTT | 2025-04-21 | 618.05 | 6 | 2025-10-20 | 616.41 | -0.3% |
| NETWEB | 2025-09-08 | 3,637.45 | 3 | 2025-11-06 | 3,515.95 | -3.3% |
| ANANDRATHI | 2025-10-20 | 1,570.73 | 2 | 2025-11-20 | 1,450.17 | -7.7% |
| TDPOWERSYS | 2025-11-03 | 388.39 | 2 | 2025-11-24 | 357.49 | -8.0% |
| CCL | 2025-11-10 | 1,040.17 | 2 | 2025-11-24 | 976.41 | -6.1% |
| SHAILY | 2025-10-13 | 2,533.28 | 2 | 2025-12-15 | 2,340.80 | -7.6% |
| EUREKAFORB | 2025-12-01 | 657.51 | 2 | 2026-01-08 | 589.10 | -10.4% |
| RADICO | 2025-11-24 | 3,289.40 | 1 | 2026-01-09 | 2,956.50 | -10.1% |
| VIYASH | 2025-10-13 | 210.00 | 3 | 2026-01-12 | 195.04 | -7.1% |
| KIRLOSENG | 2025-12-22 | 1,259.15 | 2 | 2026-01-12 | 1,140.95 | -9.4% |
| AVANTIFEED | 2025-04-15 | 756.47 | 5 | 2026-01-21 | 748.60 | -1.0% |
| LTF | 2025-11-10 | 305.52 | 2 | 2026-01-21 | 281.77 | -7.8% |
| SANSERA | 2025-12-01 | 1,786.59 | 3 | 2026-01-23 | 1,672.76 | -6.4% |
| GMRAIRPORT | 2025-12-01 | 105.48 | 2 | 2026-01-23 | 92.10 | -12.7% |
| HINDZINC | 2026-01-27 | 733.00 | 1 | 2026-02-02 | 602.35 | -17.8% |
| NATIONALUM | 2026-01-12 | 352.30 | 3 | 2026-02-17 | 335.49 | -4.8% |
| CUB | 2025-11-10 | 206.39 | 5 | 2026-03-09 | 188.57 | -8.6% |
| HINDCOPPER | 2026-02-02 | 575.55 | 3 | 2026-03-12 | 528.63 | -8.2% |
| MAHABANK | 2025-11-03 | 65.61 | 4 | 2026-03-30 | 61.05 | -7.0% |
| TORNTPOWER | 2026-03-02 | 1,491.00 | 1 | 2026-03-30 | 1,315.84 | -11.7% |
| KSB | 2026-03-02 | 868.95 | 4 | 2026-05-04 | 917.42 | +5.6% |
| INOXINDIA | 2026-04-13 | 1,395.29 | 2 | 2026-05-13 | 1,372.18 | -1.7% |
| AETHER | 2026-03-30 | 1,186.79 | 3 | 2026-05-14 | 1,125.84 | -5.1% |
| NLCINDIA | 2026-05-18 | 349.83 | 2 | 2026-06-09 | 320.62 | -8.3% |
| CIEINDIA | 2025-10-20 | 459.06 | 4 | 2026-06-11 | 429.88 | -6.4% |
| THERMAX | 2026-04-13 | 4,508.08 | 4 | 2026-07-29 | 4,306.63 | -4.5% |
| ALKYLAMINE | 2026-05-18 | 1,917.55 | 4 | 2026-09-10 | 1,920.99 | +0.2% |

## Engine B — the complete trade blotter

*Buys, pyramid injections, sells and tax settlements; every stop raise and refused signal is in `_longrun_events_2020-06-01_to_2026-09-11.csv`, and engine A's full ledger in `_longrun_events_2020-06-01_to_2026-09-11_no_doubling.csv`.*

```
2020-06-08  EIDPARRY    BUY ₹10.00 at ₹219.00 (fresh Friday signal — BUY: 4.34× weekly, month 3.59×, ladder rising; stop ₹132.60; charges ₹0.0118)
2020-06-08  IGL         BUY ₹9.95 at ₹247.75 (fresh Friday signal — BUY: 1.53× weekly, month 1.89×, ladder rising; stop ₹208.81; charges ₹0.0118)
2020-06-08  KIRLOSBROS  BUY ₹9.96 at ₹106.50 (fresh Friday signal — ACCUMULATE: 2.95× weekly, month 1.69×, ladder rising; stop ₹91.63; charges ₹0.0118)
2020-06-08  LLOYDSENGG  BUY ₹10.00 at ₹0.87 (fresh Friday signal — BUY: 4.83× weekly, month 4.76×, ladder rising; stop ₹0.46; charges ₹0.0118)
2020-06-08  RCF         BUY ₹10.02 at ₹45.20 (fresh Friday signal — BUY: 2.38× weekly, month 2.29×, ladder rising; stop ₹35.25; charges ₹0.0119)
2020-06-08  RELAXO      BUY ₹10.00 at ₹759.45 (fresh Friday signal — BUY: 1.89× weekly, month 1.81×, ladder rising; stop ₹603.77; charges ₹0.0118)
2020-06-08  SYNGENE     BUY ₹9.95 at ₹373.90 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 2.27×, ladder rising; stop ₹323.19; charges ₹0.0118)
2020-06-15  ADVENZYMES  BUY ₹10.89 at ₹172.70 (fresh Friday signal — BUY: 4.13× weekly, month 2.92×, ladder rising; stop ₹126.20; charges ₹0.0129)
2020-06-15  CAPLIPOINT  BUY ₹10.84 at ₹383.80 (fresh Friday signal — BUY: 5.39× weekly, month 2.09×, ladder rising; stop ₹291.46; charges ₹0.0128)
2020-06-15  GRANULES    BUY ₹8.39 at ₹216.75 (fresh Friday signal — BUY: 3.46× weekly, month 2.65×, ladder rising; stop ₹170.34; charges ₹0.0099)
2020-06-15  RCF         PYRAMID BUY ₹9.95 at ₹44.95 (box jump — doubling the stake with NEW capital; stop stays ₹40.28; charges ₹0.0118)
2020-06-22  ADVENZYMES  PYRAMID BUY ₹10.67 at ₹169.35 (box jump — doubling the stake with NEW capital; stop stays ₹149.98; charges ₹0.0126)
2020-06-22  EIDPARRY    PYRAMID BUY ₹12.20 at ₹267.45 (box jump — doubling the stake with NEW capital; stop stays ₹204.49; charges ₹0.0145)
2020-06-22  LLOYDSENGG  PYRAMID BUY ₹12.21 at ₹1.06 (box jump — doubling the stake with NEW capital; stop stays ₹0.71; charges ₹0.0145)
2020-06-29  EIDPARRY    PYRAMID BUY ₹24.79 at ₹272.00 (box jump — doubling the stake with NEW capital; stop stays ₹249.19; charges ₹0.0294)
2020-06-29  GRANULES    PYRAMID BUY ₹7.93 at ₹205.00 (box jump — doubling the stake with NEW capital; stop stays ₹190.95; charges ₹0.0094)
2020-06-29  KIRLOSBROS  PYRAMID BUY ₹11.12 at ₹119.05 (box jump — doubling the stake with NEW capital; stop stays ₹93.65; charges ₹0.0132)
2020-07-06  RCF         PYRAMID BUY ₹21.13 at ₹47.75 (box jump — doubling the stake with NEW capital; stop stays ₹43.23; charges ₹0.0250)
2020-07-06  SYNGENE     PYRAMID BUY ₹11.64 at ₹438.00 (box jump — doubling the stake with NEW capital; stop stays ₹375.25; charges ₹0.0138)
2020-07-07  IGL         SELL ₹8.36 at stop ₹208.81 (-15.7%, charges ₹0.0087) — the cash goes back to work at the next Friday screen
2020-07-13  GRANULES    PYRAMID BUY ₹18.25 at ₹236.20 (box jump — doubling the stake with NEW capital; stop stays ₹194.80; charges ₹0.0216)
2020-07-20  KIRLOSBROS  PYRAMID BUY ₹20.91 at ₹112.00 (box jump — doubling the stake with NEW capital; stop stays ₹97.15; charges ₹0.0248)
2020-07-27  EIDPARRY    PYRAMID BUY ₹53.57 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹273.03; charges ₹0.0635)
2020-07-27  RCF         PYRAMID BUY ₹43.87 at ₹49.60 (box jump — doubling the stake with NEW capital; stop stays ₹43.37; charges ₹0.0520)
2020-07-28  RELAXO      SELL ₹7.93 at stop ₹603.77 (-20.5%, charges ₹0.0082) — the cash goes back to work at the next Friday screen
2020-07-31  LLOYDSENGG  SELL ₹16.36 at stop ₹0.71 (-26.2%, charges ₹0.0170) — the cash goes back to work at the next Friday screen
2020-08-03  ZENTEC      BUY ₹32.65 at ₹58.80 (fresh Friday signal — ACCUMULATE: 4.33× weekly, month 4.91×, ladder rising; stop ₹42.67; charges ₹0.0387)
2020-08-10  GRANULES    PYRAMID BUY ₹49.28 at ₹319.00 (box jump — doubling the stake with NEW capital; stop stays ₹257.64; charges ₹0.0584)
2020-08-10  KIRLOSBROS  PYRAMID BUY ₹53.91 at ₹144.45 (box jump — doubling the stake with NEW capital; stop stays ₹119.79; charges ₹0.0639)
2020-08-10  RCF         PYRAMID BUY ₹91.49 at ₹51.75 (box jump — doubling the stake with NEW capital; stop stays ₹43.89; charges ₹0.1084)
2020-08-17  ADVENZYMES  PYRAMID BUY ₹28.19 at ₹223.90 (box jump — doubling the stake with NEW capital; stop stays ₹194.75; charges ₹0.0334)
2020-08-17  EIDPARRY    SELL ₹99.33 at stop ₹273.03 (-1.0%, charges ₹0.1030) — the cash goes back to work at the next Friday screen
2020-08-17  SYNGENE     PYRAMID BUY ₹26.23 at ₹493.80 (box jump — doubling the stake with NEW capital; stop stays ₹434.44; charges ₹0.0311)
2020-08-24  CAPLIPOINT  PYRAMID BUY ₹15.26 at ₹540.80 (box jump — doubling the stake with NEW capital; stop stays ₹454.79; charges ₹0.0181)
2020-08-24  KIRLOSBROS  PYRAMID BUY ₹98.51 at ₹132.05 (box jump — doubling the stake with NEW capital; stop stays ₹120.79; charges ₹0.1167)
2020-08-24  RCF         PYRAMID BUY ₹175.98 at ₹49.80 (box jump — doubling the stake with NEW capital; stop stays ₹45.84; charges ₹0.2085)
2020-08-24  THYROCARE   BUY ₹99.29 at ₹263.35 (fresh Friday signal — BUY: 7.09× weekly, month 4.48×, ladder rising; stop ₹199.77; charges ₹0.1176)
2020-08-24  ZENTEC      PYRAMID BUY ₹50.20 at ₹90.50 (box jump — doubling the stake with NEW capital; stop stays ₹80.56; charges ₹0.0595)
2020-08-31  GRANULES    PYRAMID BUY ₹96.35 at ₹312.05 (box jump — doubling the stake with NEW capital; stop stays ₹286.95; charges ₹0.1142)
2020-08-31  GRANULES    SELL ₹176.92 at stop ₹286.95 (-1.6%, charges ₹0.1835) — the cash goes back to work at the next Friday screen
2020-08-31  ZENTEC      SELL ₹89.23 at stop ₹80.56 (+7.9%, charges ₹0.0926) — the cash goes back to work at the next Friday screen
2020-09-07  INDIAMART   BUY ₹111.06 at ₹2,124.50 (fresh Friday signal — BUY: 2.46× weekly, month 1.96×, ladder rising; stop ₹1,655.61; charges ₹0.1316)
2020-09-07  POLYMED     BUY ₹111.77 at ₹449.70 (fresh Friday signal — BUY: 2.13× weekly, month 2.66×, ladder rising; stop ₹372.40; charges ₹0.1324)
2020-09-07  THYROCARE   PYRAMID BUY ₹94.77 at ₹251.67 (box jump — doubling the stake with NEW capital; stop stays ₹235.03; charges ₹0.1123)
2020-09-08  KIRLOSBROS  SELL ₹179.92 at stop ₹120.79 (-7.2%, charges ₹0.1866) — the cash goes back to work at the next Friday screen
2020-09-09  RCF         SELL ₹323.44 at stop ₹45.84 (-8.0%, charges ₹0.3355) — the cash goes back to work at the next Friday screen
2020-09-14  ATGL        BUY ₹127.05 at ₹209.75 (fresh Friday signal — BUY: 1.66× weekly, month 1.67×, ladder rising; stop ₹159.58; charges ₹0.1505)
2020-09-14  GLAXO       BUY ₹126.54 at ₹1,675.00 (fresh Friday signal — BUY: 2.55× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.1499)
2020-09-14  POLYMED     PYRAMID BUY ₹119.65 at ₹481.95 (box jump — doubling the stake with NEW capital; stop stays ₹408.50; charges ₹0.1418)
2020-09-14  SCHAEFFLER  BUY ₹126.92 at ₹814.00 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 1.89×, ladder rising; stop ₹724.67; charges ₹0.1504)
2020-09-21  ADVENZYMES  PYRAMID BUY ₹63.64 at ₹252.85 (box jump — doubling the stake with NEW capital; stop stays ₹212.37; charges ₹0.0754)
2020-09-21  CAPLIPOINT  PYRAMID BUY ₹33.95 at ₹602.00 (box jump — doubling the stake with NEW capital; stop stays ₹486.88; charges ₹0.0402)
2020-09-21  INDIAMART   PYRAMID BUY ₹131.64 at ₹2,521.27 (box jump — doubling the stake with NEW capital; stop stays ₹2,099.50; charges ₹0.1560)
2020-09-21  LINDEINDIA  BUY ₹145.13 at ₹826.00 (fresh Friday signal — BUY: 4.50× weekly, month 2.39×, ladder rising; stop ₹641.27; charges ₹0.1720)
2020-09-23  SCHAEFFLER  SELL ₹112.74 at stop ₹724.67 (-11.0%, charges ₹0.1170) — the cash goes back to work at the next Friday screen
2020-09-28  CAPLIPOINT  PYRAMID BUY ₹63.13 at ₹560.00 (box jump — doubling the stake with NEW capital; stop stays ₹498.06; charges ₹0.0748)
2020-09-28  HCLTECH     BUY ₹133.80 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.1585)
2020-09-28  SYNGENE     PYRAMID BUY ₹62.25 at ₹586.30 (box jump — doubling the stake with NEW capital; stop stays ₹501.60; charges ₹0.0738)
2020-10-05  ATGL        PYRAMID BUY ₹117.98 at ₹195.00 (box jump — doubling the stake with NEW capital; stop stays ₹162.03; charges ₹0.1398)
2020-10-05  GLAXO       PYRAMID BUY ₹118.47 at ₹1,570.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,441.55; charges ₹0.1404)
2020-10-05  LINDEINDIA  PYRAMID BUY ₹142.51 at ₹812.00 (box jump — doubling the stake with NEW capital; stop stays ₹658.50; charges ₹0.1688)
2020-10-05  POLYMED     PYRAMID BUY ₹233.40 at ₹470.35 (box jump — doubling the stake with NEW capital; stop stays ₹420.11; charges ₹0.2765)
2020-10-12  HCLTECH     PYRAMID BUY ₹137.21 at ₹860.80 (box jump — doubling the stake with NEW capital; stop stays ₹766.75; charges ₹0.1626)
2020-10-12  INDIAMART   PYRAMID BUY ₹263.00 at ₹2,520.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,315.62; charges ₹0.3116)
2020-10-19  INDIAMART   SELL ₹482.55 at stop ₹2,315.62 (-4.4%, charges ₹0.5005) — the cash goes back to work at the next Friday screen
2020-10-19  THYROCARE   PYRAMID BUY ₹259.55 at ₹344.82 (box jump — doubling the stake with NEW capital; stop stays ₹311.14; charges ₹0.3075)
2020-10-26  ADVENZYMES  PYRAMID BUY ₹158.68 at ₹315.40 (box jump — doubling the stake with NEW capital; stop stays ₹292.33; charges ₹0.1880)
2020-10-26  HCLTECH     PYRAMID BUY ₹271.78 at ₹853.00 (box jump — doubling the stake with NEW capital; stop stays ₹779.57; charges ₹0.3220)
2020-10-26  JUSTDIAL    BUY ₹337.45 at ₹584.00 (fresh Friday signal — BUY: 4.99× weekly, month 1.82×, ladder rising; stop ₹383.80; charges ₹0.3998)
2020-10-30  CAPLIPOINT  SELL ₹112.11 at stop ₹498.06 (-8.8%, charges ₹0.1163) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹217.19 at stop ₹1,441.55 (-11.2%, charges ₹0.2253) — the cash goes back to work at the next Friday screen
2020-11-02  KPRMILL     BUY ₹257.21 at ₹151.00 (fresh Friday signal — BUY: 2.37× weekly, month 3.11×, ladder rising; stop ₹108.58; charges ₹0.3048)
2020-11-03  ADVENZYMES  SELL ₹293.66 at stop ₹292.33 (+8.2%, charges ₹0.3046) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹428.15 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 1.65×, ladder rising; stop ₹77.16; charges ₹0.5073)
2020-11-09  KPRMILL     PYRAMID BUY ₹265.42 at ₹156.00 (box jump — doubling the stake with NEW capital; stop stays ₹134.58; charges ₹0.3145)
2020-11-09  THYROCARE   PYRAMID BUY ₹570.57 at ₹379.23 (box jump — doubling the stake with NEW capital; stop stays ₹338.83; charges ₹0.6760)
2020-11-12  THYROCARE   SELL ₹1,017.91 at stop ₹338.83 (-0.4%, charges ₹1.0559) — the cash goes back to work at the next Friday screen
2020-11-17  ATGL        PYRAMID BUY ₹297.80 at ₹246.25 (box jump — doubling the stake with NEW capital; stop stays ₹219.69; charges ₹0.3528)
2020-11-17  JUSTDIAL    PYRAMID BUY ₹360.71 at ₹625.00 (box jump — doubling the stake with NEW capital; stop stays ₹523.11; charges ₹0.4274)
2020-11-17  PIIND       BUY ₹502.14 at ₹2,348.20 (fresh Friday signal — ACCUMULATE: 1.62× weekly, month 1.81×, ladder rising; stop ₹2,107.67; charges ₹0.5950)
2020-11-17  TRENT       BUY ₹502.95 at ₹755.00 (fresh Friday signal — ACCUMULATE: 3.32× weekly, month 1.93×, ladder rising; stop ₹551.90; charges ₹0.5959)
2020-11-23  LINDEINDIA  PYRAMID BUY ₹314.03 at ₹895.20 (box jump — doubling the stake with NEW capital; stop stays ₹769.64; charges ₹0.3721)
2020-12-01  BORORENEW   PYRAMID BUY ₹544.74 at ₹127.00 (box jump — doubling the stake with NEW capital; stop stays ₹106.40; charges ₹0.6454)
2020-12-01  KPRMILL     PYRAMID BUY ₹535.31 at ₹157.41 (box jump — doubling the stake with NEW capital; stop stays ₹148.69; charges ₹0.6342)
2020-12-07  ATGL        PYRAMID BUY ₹875.28 at ₹362.10 (box jump — doubling the stake with NEW capital; stop stays ₹295.81; charges ₹1.0371)
2020-12-14  BORORENEW   PYRAMID BUY ₹1,139.85 at ₹132.95 (box jump — doubling the stake with NEW capital; stop stays ₹123.97; charges ₹1.3505)
2020-12-14  TRENT       PYRAMID BUY ₹462.43 at ₹695.00 (box jump — doubling the stake with NEW capital; stop stays ₹626.30; charges ₹0.5479)
2020-12-21  ATGL        PYRAMID BUY ₹1,738.17 at ₹359.75 (box jump — doubling the stake with NEW capital; stop stays ₹332.60; charges ₹2.0594)
2020-12-21  ATGL        SELL ₹3,208.76 at stop ₹332.60 (+1.9%, charges ₹3.3284) — the cash goes back to work at the next Friday screen
2020-12-21  KPRMILL     PYRAMID BUY ₹1,291.52 at ₹190.00 (box jump — doubling the stake with NEW capital; stop stays ₹156.39; charges ₹1.5302)
2020-12-21  LINDEINDIA  PYRAMID BUY ₹662.57 at ₹944.95 (box jump — doubling the stake with NEW capital; stop stays ₹868.06; charges ₹0.7850)
2020-12-21  SYNGENE     PYRAMID BUY ₹129.47 at ₹610.00 (box jump — doubling the stake with NEW capital; stop stays ₹562.40; charges ₹0.1534)
2020-12-22  SYNGENE     SELL ₹238.34 at stop ₹562.40 (-0.3%, charges ₹0.2472) — the cash goes back to work at the next Friday screen
2020-12-28  BORORENEW   PYRAMID BUY ₹4,027.16 at ₹235.00 (box jump — doubling the stake with NEW capital; stop stays ₹148.20; charges ₹4.7715)
2020-12-28  GRAVITA     BUY ₹1,620.06 at ₹69.65 (fresh Friday signal — BUY: 2.45× weekly, month 4.29×, ladder rising; stop ₹46.41; charges ₹1.9195)
2020-12-28  HONAUT      BUY ₹1,922.55 at ₹38,887.75 (fresh Friday signal — BUY: 5.49× weekly, month 1.69×, ladder rising; stop ₹29,024.49; charges ₹2.2779)
2021-01-04  LINDEINDIA  PYRAMID BUY ₹1,367.87 at ₹976.00 (box jump — doubling the stake with NEW capital; stop stays ₹898.70; charges ₹1.6207)
2021-01-11  HONAUT      PYRAMID BUY ₹2,024.57 at ₹41,000.00 (box jump — doubling the stake with NEW capital; stop stays ₹34,722.50; charges ₹2.3988)
2021-01-18  BORORENEW   PYRAMID BUY ₹9,419.69 at ₹275.00 (box jump — doubling the stake with NEW capital; stop stays ₹247.59; charges ₹11.1606)
2021-01-18  GRAVITA     PYRAMID BUY ₹1,816.78 at ₹78.20 (box jump — doubling the stake with NEW capital; stop stays ₹70.89; charges ₹2.1526)
2021-01-20  BORORENEW   SELL ₹16,934.00 at stop ₹247.59 (+9.1%, charges ₹17.5657) — the cash goes back to work at the next Friday screen
2021-01-25  GABRIEL     BUY ₹3,360.42 at ₹114.60 (fresh Friday signal — ACCUMULATE: 1.54× weekly, month 3.77×, ladder rising; stop ₹86.90; charges ₹3.9815)
2021-01-25  HCLTECH     PYRAMID BUY ₹634.95 at ₹997.00 (box jump — doubling the stake with NEW capital; stop stays ₹928.05; charges ₹0.7523)
2021-01-25  HINDZINC    BUY ₹3,375.96 at ₹277.40 (fresh Friday signal — ACCUMULATE: 2.31× weekly, month 2.09×, ladder rising; stop ₹248.97; charges ₹3.9999)
2021-01-25  INDIAMART   BUY ₹3,383.96 at ₹3,990.00 (fresh Friday signal — BUY: 2.37× weekly, month 1.58×, ladder rising; stop ₹3,323.20; charges ₹4.0094)
2021-01-25  JUSTDIAL    PYRAMID BUY ₹775.79 at ₹672.50 (box jump — doubling the stake with NEW capital; stop stays ₹622.35; charges ₹0.9192)
2021-01-25  JUSTDIAL    SELL ₹1,433.54 at stop ₹622.35 (-2.5%, charges ₹1.4870) — the cash goes back to work at the next Friday screen
2021-01-25  PIIND       SELL ₹449.71 at stop ₹2,107.67 (-10.2%, charges ₹0.4665) — the cash goes back to work at the next Friday screen
2021-01-25  TATAELXSI   BUY ₹3,401.20 at ₹2,608.00 (fresh Friday signal — BUY: 2.94× weekly, month 2.74×, ladder rising; stop ₹1,712.61; charges ₹4.0298)
2021-01-25  WHIRLPOOL   BUY ₹3,364.20 at ₹2,697.50 (fresh Friday signal — BUY: 1.73× weekly, month 2.10×, ladder rising; stop ₹2,244.99; charges ₹3.9860)
2021-01-27  LINDEINDIA  SELL ₹2,514.96 at stop ₹898.70 (-4.2%, charges ₹2.6088) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹1,180.15 at stop ₹928.05 (+0.4%, charges ₹1.2242) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹832.09 at stop ₹626.30 (-13.6%, charges ₹0.8631) — the cash goes back to work at the next Friday screen
2021-02-01  GAEL        BUY ₹4,406.95 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹5.2214)
2021-02-01  INDIAMART   PYRAMID BUY ₹3,328.34 at ₹3,929.07 (box jump — doubling the stake with NEW capital; stop stays ₹3,460.38; charges ₹3.9435)
2021-02-01  KPRMILL     PYRAMID BUY ₹2,485.45 at ₹182.93 (box jump — doubling the stake with NEW capital; stop stays ₹166.62; charges ₹2.9448)
2021-02-01  TATAELXSI   PYRAMID BUY ₹3,532.31 at ₹2,711.75 (box jump — doubling the stake with NEW capital; stop stays ₹2,275.70; charges ₹4.1852)
2021-02-08  HONAUT      PYRAMID BUY ₹4,145.35 at ₹41,999.00 (box jump — doubling the stake with NEW capital; stop stays ₹35,971.61; charges ₹4.9115)
2021-02-15  HINDZINC    PYRAMID BUY ₹3,647.89 at ₹300.10 (box jump — doubling the stake with NEW capital; stop stays ₹279.30; charges ₹4.3221)
2021-02-15  INDIAMART   PYRAMID BUY ₹7,846.82 at ₹4,634.30 (box jump — doubling the stake with NEW capital; stop stays ₹4,137.25; charges ₹9.2971)
2021-02-15  TATAELXSI   PYRAMID BUY ₹7,422.99 at ₹2,851.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,660.00; charges ₹8.7949)
2021-02-22  HONAUT      PYRAMID BUY ₹8,877.83 at ₹45,000.00 (box jump — doubling the stake with NEW capital; stop stays ₹39,140.00; charges ₹10.5186)
2021-02-22  TATAELXSI   SELL ₹13,828.84 at stop ₹2,660.00 (-3.5%, charges ₹14.3447) — the cash goes back to work at the next Friday screen
2021-02-23  GAEL        SELL ₹3,857.33 at stop ₹62.70 (-12.3%, charges ₹4.0012) — the cash goes back to work at the next Friday screen
2021-02-24  KPRMILL     SELL ₹4,520.33 at stop ₹166.62 (-6.3%, charges ₹4.6889) — the cash goes back to work at the next Friday screen
2021-03-01  IOB         BUY ₹7,742.13 at ₹18.90 (fresh Friday signal — ACCUMULATE: 3.52× weekly, month 9.60×, ladder rising; stop ₹13.70; charges ₹9.1730)
2021-03-01  MAHABANK    BUY ₹7,696.21 at ₹25.20 (fresh Friday signal — ACCUMULATE: 3.28× weekly, month 6.34×, ladder rising; stop ₹18.37; charges ₹9.1186)
2021-03-01  RCF         BUY ₹7,637.67 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.12×, ladder rising; stop ₹50.16; charges ₹9.0493)
2021-03-02  INDIAMART   SELL ₹13,987.62 at stop ₹4,137.25 (-3.7%, charges ₹14.5094) — the cash goes back to work at the next Friday screen
2021-03-08  HONAUT      PYRAMID BUY ₹18,631.97 at ₹47,248.90 (box jump — doubling the stake with NEW capital; stop stays ₹41,911.15; charges ₹22.0755)
2021-03-08  JSWENERGY   BUY ₹9,639.02 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.49×, ladder rising; stop ₹65.79; charges ₹11.4205)
2021-03-08  POLYMED     PYRAMID BUY ₹713.04 at ₹718.90 (box jump — doubling the stake with NEW capital; stop stays ₹642.77; charges ₹0.8448)
2021-03-08  SJVN        BUY ₹5,530.86 at ₹27.35 (fresh Friday signal — ACCUMULATE: 2.55× weekly, month 2.70×, ladder rising; stop ₹23.89; charges ₹6.5531)
2021-03-15  GRAVITA     PYRAMID BUY ₹5,010.59 at ₹107.90 (box jump — doubling the stake with NEW capital; stop stays ₹96.13; charges ₹5.9367)
2021-03-15  JSWENERGY   PYRAMID BUY ₹10,056.93 at ₹85.50 (box jump — doubling the stake with NEW capital; stop stays ₹76.43; charges ₹11.9157)
2021-03-15  RCF         PYRAMID BUY ₹8,181.69 at ₹85.80 (box jump — doubling the stake with NEW capital; stop stays ₹79.16; charges ₹9.6938)
2021-03-17  GRAVITA     SELL ₹8,913.51 at stop ₹96.13 (+5.8%, charges ₹9.2460) — the cash goes back to work at the next Friday screen
2021-03-17  RCF         SELL ₹15,072.46 at stop ₹79.16 (-4.5%, charges ₹15.6347) — the cash goes back to work at the next Friday screen
2021-03-19  HINDZINC    SELL ₹6,779.06 at stop ₹279.30 (-3.3%, charges ₹7.0319) — the cash goes back to work at the next Friday screen
2021-03-19  MAHABANK    SELL ₹5,597.84 at stop ₹18.37 (-27.1%, charges ₹5.8066) — the cash goes back to work at the next Friday screen
2021-03-22  DEEPAKFERT  BUY ₹11,449.23 at ₹237.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.82×, ladder rising; stop ₹184.78; charges ₹13.5653)
2021-03-22  GABRIEL     PYRAMID BUY ₹3,242.21 at ₹110.70 (box jump — doubling the stake with NEW capital; stop stays ₹86.92; charges ₹3.8414)
2021-03-22  HONAUT      SELL ₹33,000.40 at stop ₹41,911.15 (-7.1%, charges ₹34.2313) — the cash goes back to work at the next Friday screen
2021-03-22  KEI         BUY ₹11,387.06 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹13.4916)
2021-03-22  WELSPUNLIV  BUY ₹11,444.97 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.45×, ladder rising; stop ₹67.45; charges ₹13.5602)
2021-03-24  WHIRLPOOL   SELL ₹2,793.63 at stop ₹2,244.99 (-16.8%, charges ₹2.8978) — the cash goes back to work at the next Friday screen
2021-03-30  DEEPAKFERT  PYRAMID BUY ₹10,767.38 at ₹223.15 (box jump — doubling the stake with NEW capital; stop stays ₹209.52; charges ₹12.7574)
2021-03-30  KEI         PYRAMID BUY ₹11,334.35 at ₹520.20 (box jump — doubling the stake with NEW capital; stop stays ₹471.20; charges ₹13.4292)
2021-03-30  KPITTECH    BUY ₹14,789.34 at ₹182.00 (fresh Friday signal — BUY: 1.71× weekly, month 2.75×, ladder rising; stop ₹136.62; charges ₹17.5227)
2021-03-30  POLYMED     PYRAMID BUY ₹1,616.65 at ₹815.45 (box jump — doubling the stake with NEW capital; stop stays ₹719.96; charges ₹1.9154)
2021-03-30  WELSPUNLIV  PYRAMID BUY ₹11,789.30 at ₹84.00 (box jump — doubling the stake with NEW capital; stop stays ₹68.17; charges ₹13.9682)
2021-04-01  TAX         FY2021 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹6,471.72 / LT ₹0.00)
2021-04-05  AUBANK      BUY ₹15,299.85 at ₹631.00 (fresh Friday signal — ACCUMULATE: 3.80× weekly, month 2.02×, ladder rising; stop ₹533.06; charges ₹18.1276)
2021-04-05  GICRE       BUY ₹7,786.45 at ₹205.90 (fresh Friday signal — BUY: 1.92× weekly, month 3.20×, ladder rising; stop ₹157.44; charges ₹9.2255)
2021-04-05  IOB         PYRAMID BUY ₹6,894.20 at ₹16.85 (box jump — doubling the stake with NEW capital; stop stays ₹14.82; charges ₹8.1684)
2021-04-12  AUBANK      SELL ₹12,896.40 at stop ₹533.06 (-15.5%, charges ₹13.3775) — the cash goes back to work at the next Friday screen
2021-04-12  GICRE       PYRAMID BUY ₹7,705.46 at ₹204.00 (box jump — doubling the stake with NEW capital; stop stays ₹164.12; charges ₹9.1296)
2021-04-19  JSWENERGY   PYRAMID BUY ₹22,382.51 at ₹95.20 (box jump — doubling the stake with NEW capital; stop stays ₹81.99; charges ₹26.5193)
2021-04-19  KPITTECH    PYRAMID BUY ₹15,400.84 at ₹189.75 (box jump — doubling the stake with NEW capital; stop stays ₹171.05; charges ₹18.2472)
2021-04-19  KPRMILL     BUY ₹12,896.40 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹15.2799)
2021-04-26  KPRMILL     PYRAMID BUY ₹13,295.39 at ₹243.59 (box jump — doubling the stake with NEW capital; stop stays ₹221.37; charges ₹15.7527)
2021-04-28  IOB         SELL ₹12,107.50 at stop ₹14.82 (-17.1%, charges ₹12.5591) — the cash goes back to work at the next Friday screen
2021-05-03  MARKSANS    BUY ₹12,107.50 at ₹70.95 (fresh Friday signal — ACCUMULATE: 3.13× weekly, month 3.97×, ladder rising; stop ₹64.12; charges ₹14.3452)
2021-05-10  KEI         PYRAMID BUY ₹23,016.74 at ₹528.50 (box jump — doubling the stake with NEW capital; stop stays ₹485.02; charges ₹27.2707)
2021-05-17  KPRMILL     PYRAMID BUY ₹32,074.64 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹268.28; charges ₹38.0027)
2021-05-17  POLYMED     PYRAMID BUY ₹3,979.34 at ₹1,004.20 (box jump — doubling the stake with NEW capital; stop stays ₹902.50; charges ₹4.7148)
2021-05-24  DEEPAKFERT  PYRAMID BUY ₹28,933.90 at ₹300.00 (box jump — doubling the stake with NEW capital; stop stays ₹264.10; charges ₹34.2815)
2021-05-24  MARKSANS    PYRAMID BUY ₹12,774.94 at ₹74.95 (box jump — doubling the stake with NEW capital; stop stays ₹68.02; charges ₹15.1360)
2021-05-31  KEI         PYRAMID BUY ₹54,319.54 at ₹624.00 (box jump — doubling the stake with NEW capital; stop stays ₹558.60; charges ₹64.3589)
2021-05-31  SJVN        PYRAMID BUY ₹5,483.91 at ₹27.15 (box jump — doubling the stake with NEW capital; stop stays ₹25.13; charges ₹6.4975)
2021-06-07  DEEPAKFERT  PYRAMID BUY ₹57,255.19 at ₹297.00 (box jump — doubling the stake with NEW capital; stop stays ₹269.80; charges ₹67.8371)
2021-06-07  JSWENERGY   PYRAMID BUY ₹64,100.13 at ₹136.40 (box jump — doubling the stake with NEW capital; stop stays ₹108.49; charges ₹75.9471)
2021-06-07  KPITTECH    PYRAMID BUY ₹39,406.04 at ₹242.90 (box jump — doubling the stake with NEW capital; stop stays ₹214.70; charges ₹46.6891)
2021-06-07  POLYMED     PYRAMID BUY ₹7,984.46 at ₹1,008.05 (box jump — doubling the stake with NEW capital; stop stays ₹950.00; charges ₹9.4602)
2021-06-07  WELSPUNLIV  PYRAMID BUY ₹26,061.37 at ₹92.90 (box jump — doubling the stake with NEW capital; stop stays ₹80.48; charges ₹30.8780)
2021-06-14  JSWENERGY   PYRAMID BUY ₹147,427.49 at ₹156.95 (box jump — doubling the stake with NEW capital; stop stays ₹126.83; charges ₹174.6751)
2021-06-14  POLYMED     SELL ₹15,024.82 at stop ₹950.00 (+2.0%, charges ₹15.5853) — the cash goes back to work at the next Friday screen
2021-06-21  KEI         PYRAMID BUY ₹118,701.39 at ₹682.20 (box jump — doubling the stake with NEW capital; stop stays ₹608.00; charges ₹140.6398)
2021-06-21  SJVN        PYRAMID BUY ₹11,425.62 at ₹28.30 (box jump — doubling the stake with NEW capital; stop stays ₹26.98; charges ₹13.5373)
2021-06-28  JSWENERGY   PYRAMID BUY ₹289,329.31 at ₹154.10 (box jump — doubling the stake with NEW capital; stop stays ₹138.04; charges ₹342.8033)
2021-06-28  MARKSANS    PYRAMID BUY ₹29,810.42 at ₹87.50 (box jump — doubling the stake with NEW capital; stop stays ₹76.87; charges ₹35.3200)
2021-07-05  DEEPAKFERT  PYRAMID BUY ₹152,204.73 at ₹395.00 (box jump — doubling the stake with NEW capital; stop stays ₹364.65; charges ₹180.3353)
2021-07-12  JSWENERGY   PYRAMID BUY ₹630,480.58 at ₹168.00 (box jump — doubling the stake with NEW capital; stop stays ₹154.47; charges ₹747.0063)
2021-07-19  KPITTECH    PYRAMID BUY ₹86,596.52 at ₹267.05 (box jump — doubling the stake with NEW capital; stop stays ₹232.94; charges ₹102.6013)
2021-07-19  KPRMILL     PYRAMID BUY ₹81,120.38 at ₹372.00 (box jump — doubling the stake with NEW capital; stop stays ₹333.07; charges ₹96.1131)
2021-07-19  WELSPUNLIV  PYRAMID BUY ₹70,063.27 at ₹124.95 (box jump — doubling the stake with NEW capital; stop stays ₹97.56; charges ₹83.0124)
2021-08-02  WELSPUNLIV  PYRAMID BUY ₹151,027.33 at ₹134.75 (box jump — doubling the stake with NEW capital; stop stays ₹117.99; charges ₹178.9403)
2021-08-09  JSWENERGY   PYRAMID BUY ₹1,897,822.50 at ₹253.00 (box jump — doubling the stake with NEW capital; stop stays ₹228.00; charges ₹2,248.5791)
2021-08-09  KPITTECH    PYRAMID BUY ₹202,516.79 at ₹312.45 (box jump — doubling the stake with NEW capital; stop stays ₹266.76; charges ₹239.9460)
2021-08-09  KPRMILL     PYRAMID BUY ₹174,174.74 at ₹399.60 (box jump — doubling the stake with NEW capital; stop stays ₹352.48; charges ₹206.3658)
2021-08-09  MARKSANS    PYRAMID BUY ₹57,202.09 at ₹84.00 (box jump — doubling the stake with NEW capital; stop stays ₹77.14; charges ₹67.7742)
2021-08-09  WELSPUNLIV  PYRAMID BUY ₹304,452.03 at ₹135.90 (box jump — doubling the stake with NEW capital; stop stays ₹124.64; charges ₹360.7210)
2021-08-10  MARKSANS    SELL ₹104,890.13 at stop ₹77.14 (-6.1%, charges ₹108.8026) — the cash goes back to work at the next Friday screen
2021-08-10  SJVN        SELL ₹21,749.92 at stop ₹26.98 (-2.9%, charges ₹22.5612) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNLIV  SELL ₹557,544.11 at stop ₹124.64 (-2.8%, charges ₹578.3410) — the cash goes back to work at the next Friday screen
2021-08-11  GICRE       SELL ₹12,378.05 at stop ₹164.12 (-19.9%, charges ₹12.8398) — the cash goes back to work at the next Friday screen
2021-08-11  JSWENERGY   SELL ₹3,415,012.49 at stop ₹228.00 (+11.4%, charges ₹3,542.3955) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹306,772.59 at stop ₹352.48 (-1.9%, charges ₹318.2155) — the cash goes back to work at the next Friday screen
2021-08-16  GABRIEL     PYRAMID BUY ₹8,740.29 at ₹149.30 (box jump — doubling the stake with NEW capital; stop stays ₹118.77; charges ₹10.3557)
2021-08-16  KEI         PYRAMID BUY ₹259,085.95 at ₹744.95 (box jump — doubling the stake with NEW capital; stop stays ₹663.29; charges ₹306.9704)
2021-08-16  TATAINVEST  BUY ₹575,795.48 at ₹130.81 (fresh Friday signal — BUY: 8.45× weekly, month 4.82×, ladder rising; stop ₹103.11; charges ₹682.2143)
2021-08-23  DEEPAKFERT  PYRAMID BUY ₹308,850.33 at ₹401.00 (box jump — doubling the stake with NEW capital; stop stays ₹380.00; charges ₹365.9322)
2021-08-23  GRAVITA     BUY ₹645,073.03 at ₹188.60 (fresh Friday signal — BUY: 2.16× weekly, month 1.88×, ladder rising; stop ₹151.95; charges ₹764.2958)
2021-08-23  TATAINVEST  PYRAMID BUY ₹542,995.21 at ₹123.50 (box jump — doubling the stake with NEW capital; stop stays ₹113.90; charges ₹643.3519)
2021-08-30  GABRIEL     PYRAMID BUY ₹16,112.86 at ₹137.70 (box jump — doubling the stake with NEW capital; stop stays ₹124.06; charges ₹19.0909)
2021-08-30  GRAVITA     PYRAMID BUY ₹662,756.60 at ₹194.00 (box jump — doubling the stake with NEW capital; stop stays ₹164.49; charges ₹785.2476)
2021-08-30  KPITTECH    PYRAMID BUY ₹439,838.17 at ₹339.50 (box jump — doubling the stake with NEW capital; stop stays ₹278.89; charges ₹521.1293)
2021-09-06  HAL         BUY ₹774,951.22 at ₹705.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.49×, ladder rising; stop ₹500.63; charges ₹918.1781)
2021-09-06  NHPC        BUY ₹776,572.30 at ₹27.90 (fresh Friday signal — BUY: 5.07× weekly, month 1.59×, ladder rising; stop ₹24.13; charges ₹920.0988)
2021-09-06  TDPOWERSYS  BUY ₹772,177.74 at ₹32.80 (fresh Friday signal — BUY: 2.60× weekly, month 4.52×, ladder rising; stop ₹25.56; charges ₹914.8920)
2021-09-13  HAL         PYRAMID BUY ₹754,297.95 at ₹687.02 (box jump — doubling the stake with NEW capital; stop stays ₹636.29; charges ₹893.7077)
2021-09-13  KEI         PYRAMID BUY ₹553,839.85 at ₹796.70 (box jump — doubling the stake with NEW capital; stop stays ₹718.20; charges ₹656.2008)
2021-09-13  NEOGEN      BUY ₹888,802.35 at ₹1,165.00 (fresh Friday signal — BUY: 10.32× weekly, month 3.05×, ladder rising; stop ₹841.94; charges ₹1,053.0713)
2021-09-13  TATAINVEST  PYRAMID BUY ₹1,130,914.06 at ₹128.69 (box jump — doubling the stake with NEW capital; stop stays ₹118.32; charges ₹1,339.9302)
2021-09-20  DEEPAKFERT  PYRAMID BUY ₹661,979.88 at ₹430.00 (box jump — doubling the stake with NEW capital; stop stays ₹385.70; charges ₹784.3274)
2021-09-20  KEI         PYRAMID BUY ₹1,179,694.93 at ₹849.00 (box jump — doubling the stake with NEW capital; stop stays ₹737.39; charges ₹1,397.7268)
2021-09-20  NHPC        PYRAMID BUY ₹768,701.91 at ₹27.65 (box jump — doubling the stake with NEW capital; stop stays ₹25.55; charges ₹910.7738)
2021-09-20  TDPOWERSYS  PYRAMID BUY ₹747,748.74 at ₹31.80 (box jump — doubling the stake with NEW capital; stop stays ₹29.75; charges ₹885.9481)
2021-09-27  NEOGEN      PYRAMID BUY ₹956,330.76 at ₹1,255.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,035.55; charges ₹1,133.0803)
2021-09-27  TATAINVEST  PYRAMID BUY ₹2,299,397.01 at ₹130.90 (box jump — doubling the stake with NEW capital; stop stays ₹118.77; charges ₹2,724.3728)
2021-10-04  NEOGEN      PYRAMID BUY ₹1,911,680.76 at ₹1,255.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,142.85; charges ₹2,264.9986)
2021-10-11  KEI         PYRAMID BUY ₹2,732,382.40 at ₹983.80 (box jump — doubling the stake with NEW capital; stop stays ₹853.10; charges ₹3,237.3828)
2021-10-18  HAL         PYRAMID BUY ₹1,618,471.47 at ₹737.50 (box jump — doubling the stake with NEW capital; stop stays ₹636.50; charges ₹1,917.5982)
2021-10-18  TATAINVEST  PYRAMID BUY ₹5,902,210.14 at ₹168.10 (box jump — doubling the stake with NEW capital; stop stays ₹134.91; charges ₹6,993.0598)
2021-10-18  TDPOWERSYS  PYRAMID BUY ₹1,637,492.62 at ₹34.84 (box jump — doubling the stake with NEW capital; stop stays ₹30.53; charges ₹1,940.1349)
2021-10-22  KEI         SELL ₹4,731,043.93 at stop ₹853.10 (-4.1%, charges ₹4,907.5160) — the cash goes back to work at the next Friday screen
2021-10-22  TDPOWERSYS  SELL ₹2,865,169.96 at stop ₹30.53 (-9.1%, charges ₹2,972.0433) — the cash goes back to work at the next Friday screen
2021-10-25  LTM         BUY ₹3,191,494.14 at ₹6,555.00 (fresh Friday signal — BUY: 4.63× weekly, month 1.86×, ladder rising; stop ₹5,353.77; charges ₹3,781.3478)
2021-10-25  NEOGEN      SELL ₹3,475,750.95 at stop ₹1,142.85 (-7.3%, charges ₹3,605.3995) — the cash goes back to work at the next Friday screen
2021-10-25  NHPC        PYRAMID BUY ₹1,828,232.23 at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹27.60; charges ₹2,166.1271)
2021-10-28  HAL         SELL ₹2,789,098.24 at stop ₹636.50 (-11.2%, charges ₹2,893.1340) — the cash goes back to work at the next Friday screen
2021-11-01  LTM         PYRAMID BUY ₹3,267,952.71 at ₹6,720.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,950.99; charges ₹3,871.9375)
2021-11-01  PERSISTENT  BUY ₹4,535,680.39 at ₹1,977.15 (fresh Friday signal — ACCUMULATE: 1.71× weekly, month 2.09×, ladder rising; stop ₹1,728.75; charges ₹5,373.9673)
2021-11-01  TATAINVEST  PYRAMID BUY ₹10,386,788.98 at ₹148.00 (box jump — doubling the stake with NEW capital; stop stays ₹143.65; charges ₹12,306.4809)
2021-11-11  DEEPAKFERT  SELL ₹1,185,627.75 at stop ₹385.70 (-3.5%, charges ₹1,229.8527) — the cash goes back to work at the next Friday screen
2021-11-15  GOKULAGRO   BUY ₹5,200,624.36 at ₹31.05 (fresh Friday signal — BUY: 2.63× weekly, month 1.60×, ladder rising; stop ₹24.87; charges ₹6,161.8065)
2021-11-15  GRAVITA     PYRAMID BUY ₹1,500,903.12 at ₹219.80 (box jump — doubling the stake with NEW capital; stop stays ₹197.03; charges ₹1,778.3008)
2021-11-15  NHPC        PYRAMID BUY ₹3,587,654.60 at ₹32.30 (box jump — doubling the stake with NEW capital; stop stays ₹28.69; charges ₹4,250.7268)
2021-11-22  GRAVITA     SELL ₹2,686,455.85 at stop ₹197.03 (-4.1%, charges ₹2,786.6630) — the cash goes back to work at the next Friday screen
2021-11-22  NHPC        PYRAMID BUY ₹7,304,266.99 at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹30.11; charges ₹8,654.2455)
2021-11-26  TATAINVEST  SELL ₹20,130,177.39 at stop ₹143.65 (-3.2%, charges ₹20,881.0507) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹6,946,464.90 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹8,230.3143)
2021-11-29  ESCORTS     BUY ₹6,958,990.36 at ₹1,875.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.18×, ladder rising; stop ₹1,369.04; charges ₹8,245.1547)
2021-11-29  GOKULAGRO   PYRAMID BUY ₹5,801,663.59 at ₹34.68 (box jump — doubling the stake with NEW capital; stop stays ₹26.03; charges ₹6,873.9302)
2021-11-29  KPITTECH    PYRAMID BUY ₹1,178,249.26 at ₹455.00 (box jump — doubling the stake with NEW capital; stop stays ₹398.63; charges ₹1,396.0139)
2021-11-29  LTM         PYRAMID BUY ₹6,347,348.00 at ₹6,530.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,270.00; charges ₹7,520.4683)
2021-11-29  NHPC        SELL ₹13,347,928.61 at stop ₹30.11 (-6.2%, charges ₹13,845.8181) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹7,575,229.27 at ₹209.99 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹158.85; charges ₹8,975.2872)
2021-12-06  BSOFT       PYRAMID BUY ₹7,233,542.07 at ₹485.00 (box jump — doubling the stake with NEW capital; stop stays ₹424.65; charges ₹8,570.4492)
2021-12-06  CHAMBLFERT  BUY ₹7,557,677.61 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹8,954.4916)
2021-12-06  PGEL        BUY ₹7,531,400.52 at ₹61.77 (fresh Friday signal — BUY: 2.46× weekly, month 1.72×, ladder rising; stop ₹37.43; charges ₹8,923.3580)
2021-12-13  ESCORTS     PYRAMID BUY ₹6,928,502.82 at ₹1,869.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,739.73; charges ₹8,209.0324)
2021-12-13  KPITTECH    PYRAMID BUY ₹2,613,904.99 at ₹505.00 (box jump — doubling the stake with NEW capital; stop stays ₹458.85; charges ₹3,097.0083)
2021-12-13  PERSISTENT  PYRAMID BUY ₹4,995,103.05 at ₹2,180.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,961.89; charges ₹5,918.3007)
2021-12-20  KPITTECH    SELL ₹4,742,327.40 at stop ₹458.85 (+3.5%, charges ₹4,919.2204) — the cash goes back to work at the next Friday screen
2021-12-27  BSE         PYRAMID BUY ₹7,406,320.73 at ₹205.56 (box jump — doubling the stake with NEW capital; stop stays ₹181.60; charges ₹8,775.1609)
2021-12-27  PERSISTENT  PYRAMID BUY ₹10,586,551.03 at ₹2,311.50 (box jump — doubling the stake with NEW capital; stop stays ₹2,067.34; charges ₹12,543.1631)
2021-12-27  PGEL        PYRAMID BUY ₹8,647,225.43 at ₹71.00 (box jump — doubling the stake with NEW capital; stop stays ₹56.96; charges ₹10,245.4103)
2021-12-27  UNOMINDA    BUY ₹6,456,018.51 at ₹590.00 (fresh Friday signal — BUY: 3.66× weekly, month 2.64×, ladder rising; stop ₹464.60; charges ₹7,649.2233)
2022-01-03  GABRIEL     PYRAMID BUY ₹32,744.58 at ₹140.00 (box jump — doubling the stake with NEW capital; stop stays ₹125.40; charges ₹38.7965)
2022-01-03  UNOMINDA    PYRAMID BUY ₹6,720,785.57 at ₹614.92 (box jump — doubling the stake with NEW capital; stop stays ₹544.21; charges ₹7,962.9248)
2022-01-07  UNOMINDA    SELL ₹11,876,453.85 at stop ₹544.21 (-9.7%, charges ₹12,319.4560) — the cash goes back to work at the next Friday screen
2022-01-10  AFFLE       BUY ₹11,876,453.85 at ₹1,307.00 (fresh Friday signal — BUY: 4.57× weekly, month 1.57×, ladder rising; stop ₹955.80; charges ₹14,071.4664)
2022-01-10  PGEL        PYRAMID BUY ₹20,570,638.87 at ₹84.50 (box jump — doubling the stake with NEW capital; stop stays ₹72.44; charges ₹24,372.5154)
2022-01-17  AFFLE       PYRAMID BUY ₹13,550,525.56 at ₹1,493.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,206.50; charges ₹16,054.9409)
2022-01-24  ESCORTS     PYRAMID BUY ₹13,853,983.42 at ₹1,869.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,754.65; charges ₹16,414.4841)
2022-01-24  GOKULAGRO   PYRAMID BUY ₹12,702,047.88 at ₹37.98 (box jump — doubling the stake with NEW capital; stop stays ₹35.00; charges ₹15,049.6472)
2022-01-24  LTM         SELL ₹12,169,396.68 at stop ₹6,270.00 (-4.8%, charges ₹12,623.3259) — the cash goes back to work at the next Friday screen
2022-01-24  PERSISTENT  SELL ₹18,905,792.36 at stop ₹2,067.34 (-5.8%, charges ₹19,610.9950) — the cash goes back to work at the next Friday screen
2022-01-24  PGEL        SELL ₹35,212,097.12 at stop ₹72.44 (-4.0%, charges ₹36,525.5393) — the cash goes back to work at the next Friday screen
2022-01-25  AFFLE       SELL ₹21,864,826.55 at stop ₹1,206.50 (-13.8%, charges ₹22,680.4038) — the cash goes back to work at the next Friday screen
2022-01-25  GOKULAGRO   SELL ₹23,372,040.47 at stop ₹35.00 (-1.2%, charges ₹24,243.8381) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹17,681,047.55 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹20,948.8682)
2022-02-07  CCL         BUY ₹19,865,371.24 at ₹503.55 (fresh Friday signal — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹23,536.8998)
2022-02-07  SHARDACROP  PYRAMID BUY ₹19,869,492.31 at ₹660.10 (box jump — doubling the stake with NEW capital; stop stays ₹545.30; charges ₹23,541.7825)
2022-02-11  SHARDACROP  SELL ₹32,774,412.38 at stop ₹545.30 (-12.5%, charges ₹33,996.9267) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹12,646,279.61 at stop ₹424.65 (-10.6%, charges ₹13,117.9969) — the cash goes back to work at the next Friday screen
2022-02-14  CCL         PYRAMID BUY ₹18,322,813.96 at ₹465.00 (box jump — doubling the stake with NEW capital; stop stays ₹441.75; charges ₹21,709.2462)
2022-02-14  CHAMBLFERT  PYRAMID BUY ₹7,121,681.60 at ₹384.40 (box jump — doubling the stake with NEW capital; stop stays ₹353.85; charges ₹8,437.9146)
2022-02-14  GABRIEL     SELL ₹58,564.09 at stop ₹125.40 (-8.6%, charges ₹60.7486) — the cash goes back to work at the next Friday screen
2022-02-14  GNFC        BUY ₹21,380,977.83 at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹25,332.6216)
2022-02-21  ADANIPOWER  BUY ₹23,440,398.72 at ₹26.40 (fresh Friday signal — BUY: 8.22× weekly, month 2.70×, ladder rising; stop ₹18.02; charges ₹27,772.6658)
2022-02-21  CGCL        BUY ₹23,227,439.93 at ₹567.08 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹507.72; charges ₹27,520.3478)
2022-02-21  GNFC        PYRAMID BUY ₹21,162,556.19 at ₹548.00 (box jump — doubling the stake with NEW capital; stop stays ₹497.80; charges ₹25,073.8312)
2022-02-24  CCL         SELL ₹34,756,669.61 at stop ₹441.75 (-8.8%, charges ₹36,053.1239) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹13,090,033.33 at stop ₹353.85 (-10.6%, charges ₹13,578.3031) — the cash goes back to work at the next Friday screen
2022-02-25  ESCORTS     SELL ₹25,960,653.15 at stop ₹1,754.65 (-6.2%, charges ₹26,929.0083) — the cash goes back to work at the next Friday screen
2022-03-07  ADANIPOWER  PYRAMID BUY ₹20,574,731.99 at ₹23.20 (box jump — doubling the stake with NEW capital; stop stays ₹20.00; charges ₹24,377.3650)
2022-04-01  TAX         FY2022 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹23,484,685.65 / LT ₹0.00)
2022-04-04  RCF         BUY ₹31,429,301.39 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹37,238.0817)
2022-04-04  SPLPETRO    BUY ₹31,583,514.83 at ₹475.00 (fresh Friday signal — BUY: 4.41× weekly, month 2.84×, ladder rising; stop ₹398.29; charges ₹37,420.7969)
2022-04-11  BLS         BUY ₹35,245,956.67 at ₹82.50 (fresh Friday signal — BUY: 8.78× weekly, month 1.73×, ladder rising; stop ₹54.82; charges ₹41,760.1332)
2022-04-11  MINDACORP   BUY ₹26,956,757.18 at ₹230.05 (fresh Friday signal — BUY: 2.10× weekly, month 1.60×, ladder rising; stop ₹186.63; charges ₹31,938.9195)
2022-04-11  SPLPETRO    PYRAMID BUY ₹30,593,069.93 at ₹460.65 (box jump — doubling the stake with NEW capital; stop stays ₹424.27; charges ₹36,247.2975)
2022-04-25  ADANIPOWER  PYRAMID BUY ₹93,382,308.74 at ₹52.68 (box jump — doubling the stake with NEW capital; stop stays ₹40.22; charges ₹110,641.2770)
2022-04-25  BLS         PYRAMID BUY ₹35,172,192.72 at ₹82.42 (box jump — doubling the stake with NEW capital; stop stays ₹75.36; charges ₹41,672.7362)
2022-04-25  GNFC        PYRAMID BUY ₹65,333,490.21 at ₹846.40 (box jump — doubling the stake with NEW capital; stop stays ₹792.16; charges ₹77,408.4608)
2022-04-25  RCF         PYRAMID BUY ₹33,932,085.03 at ₹104.20 (box jump — doubling the stake with NEW capital; stop stays ₹93.15; charges ₹40,203.4311)
2022-05-02  BSE         PYRAMID BUY ₹21,367,976.01 at ₹296.70 (box jump — doubling the stake with NEW capital; stop stays ₹255.87; charges ₹25,317.2168)
2022-05-04  RCF         SELL ₹60,568,673.90 at stop ₹93.15 (-7.1%, charges ₹62,827.9386) — the cash goes back to work at the next Friday screen
2022-05-06  GNFC        SELL ₹122,094,328.90 at stop ₹792.16 (+13.4%, charges ₹126,648.5546) — the cash goes back to work at the next Friday screen
2022-05-09  MRPL        BUY ₹60,600,610.45 at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹71,800.8477)
2022-05-10  BSE         SELL ₹36,794,896.74 at stop ₹255.87 (+1.5%, charges ₹38,167.3787) — the cash goes back to work at the next Friday screen
2022-05-11  MINDACORP   SELL ₹21,820,351.31 at stop ₹186.63 (-18.9%, charges ₹22,634.2696) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹58,445,436.04 at ₹146.67 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.79×, ladder rising; stop ₹130.85; charges ₹69,247.3528)
2022-05-23  ACC         BUY ₹71,870,018.72 at ₹2,260.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹85,153.0740)
2022-05-23  MRPL        PYRAMID BUY ₹73,565,783.98 at ₹94.80 (box jump — doubling the stake with NEW capital; stop stays ₹60.81; charges ₹87,162.2515)
2022-05-24  SPLPETRO    SELL ₹56,262,196.91 at stop ₹424.27 (-9.3%, charges ₹58,360.8263) — the cash goes back to work at the next Friday screen
2022-06-06  MRPL        PYRAMID BUY ₹137,039,802.15 at ₹88.35 (box jump — doubling the stake with NEW capital; stop stays ₹69.61; charges ₹162,367.5717)
2022-06-13  ELECON      BUY ₹93,439,996.12 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹110,709.6262)
2022-06-13  VBL         PYRAMID BUY ₹59,583,500.86 at ₹149.70 (box jump — doubling the stake with NEW capital; stop stays ₹136.81; charges ₹70,595.7554)
2022-06-20  BLS         PYRAMID BUY ₹90,517,141.47 at ₹106.12 (box jump — doubling the stake with NEW capital; stop stays ₹83.17; charges ₹107,246.5680)
2022-06-20  ELECON      PYRAMID BUY ₹100,016,075.55 at ₹131.25 (box jump — doubling the stake with NEW capital; stop stays ₹111.01; charges ₹118,501.1001)
2022-06-27  ADANIPOWER  PYRAMID BUY ₹192,004,156.60 at ₹54.19 (box jump — doubling the stake with NEW capital; stop stays ₹43.79; charges ₹227,490.4676)
2022-06-27  VBL         PYRAMID BUY ₹124,092,567.82 at ₹155.98 (box jump — doubling the stake with NEW capital; stop stays ₹136.99; charges ₹147,027.4226)
2022-07-04  BLS         PYRAMID BUY ₹166,180,097.72 at ₹97.47 (box jump — doubling the stake with NEW capital; stop stays ₹90.53; charges ₹196,893.5923)
2022-07-06  MRPL        SELL ₹215,592,764.41 at stop ₹69.61 (-20.3%, charges ₹223,634.5638) — the cash goes back to work at the next Friday screen
2022-07-11  ELECON      PYRAMID BUY ₹223,903,288.00 at ₹147.00 (box jump — doubling the stake with NEW capital; stop stays ₹120.65; charges ₹265,285.2135)
2022-07-18  ACC         PYRAMID BUY ₹68,638,719.21 at ₹2,160.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,030.05; charges ₹81,324.5640)
2022-07-25  ELECON      PYRAMID BUY ₹505,234,538.81 at ₹165.95 (box jump — doubling the stake with NEW capital; stop stays ₹142.64; charges ₹598,612.2566)
2022-07-25  TIINDIA     BUY ₹228,777,150.83 at ₹2,135.00 (fresh Friday signal — BUY: 4.17× weekly, month 2.43×, ladder rising; stop ₹1,862.00; charges ₹271,059.8663)
2022-08-01  VBL         PYRAMID BUY ₹283,626,599.45 at ₹178.36 (box jump — doubling the stake with NEW capital; stop stays ₹162.49; charges ₹336,046.6193)
2022-08-08  ACC         PYRAMID BUY ₹143,484,679.11 at ₹2,260.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,053.90; charges ₹170,003.5943)
2022-08-08  BLS         PYRAMID BUY ₹402,957,788.59 at ₹118.25 (box jump — doubling the stake with NEW capital; stop stays ₹110.67; charges ₹477,432.6627)
2022-08-08  TIINDIA     PYRAMID BUY ₹243,185,054.67 at ₹2,272.15 (box jump — doubling the stake with NEW capital; stop stays ₹1,867.30; charges ₹288,130.6466)
2022-08-16  ACC         PYRAMID BUY ₹285,276,526.20 at ₹2,248.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,085.11; charges ₹338,001.4864)
2022-08-16  ADANIPOWER  PYRAMID BUY ₹494,332,929.09 at ₹69.80 (box jump — doubling the stake with NEW capital; stop stays ₹61.19; charges ₹585,695.8055)
2022-08-16  ELECON      PYRAMID BUY ₹1,040,601,684.71 at ₹171.00 (box jump — doubling the stake with NEW capital; stop stays ₹156.67; charges ₹1,232,926.2449)
2022-08-16  VBL         PYRAMID BUY ₹654,770,875.59 at ₹206.00 (box jump — doubling the stake with NEW capital; stop stays ₹188.52; charges ₹775,785.9792)
2022-08-22  VBL         SELL ₹1,196,470,355.39 at stop ₹188.52 (+1.6%, charges ₹1,241,099.7503) — the cash goes back to work at the next Friday screen
2022-08-23  BLS         SELL ₹753,027,251.65 at stop ₹110.67 (+3.4%, charges ₹781,115.8294) — the cash goes back to work at the next Friday screen
2022-08-29  ACC         PYRAMID BUY ₹576,810,064.85 at ₹2,274.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,151.37; charges ₹683,416.4097)
2022-08-29  HOMEFIRST   BUY ₹693,545,556.29 at ₹944.95 (fresh Friday signal — ACCUMULATE: 3.67× weekly, month 2.49×, ladder rising; stop ₹849.35; charges ₹821,727.0171)
2022-08-29  KALYANKJIL  BUY ₹694,338,210.15 at ₹78.10 (fresh Friday signal — BUY: 9.54× weekly, month 2.93×, ladder rising; stop ₹65.55; charges ₹822,666.1697)
2022-08-29  SIEMENS     BUY ₹561,613,840.61 at ₹1,688.21 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 1.62×, ladder rising; stop ₹1,573.13; charges ₹665,411.6111)
2022-09-05  ADANIPOWER  PYRAMID BUY ₹1,142,803,889.81 at ₹80.73 (box jump — doubling the stake with NEW capital; stop stays ₹66.80; charges ₹1,354,017.5162)
2022-09-05  KALYANKJIL  PYRAMID BUY ₹751,678,499.33 at ₹84.65 (box jump — doubling the stake with NEW capital; stop stays ₹73.15; charges ₹890,604.1218)
2022-09-14  HOMEFIRST   SELL ₹621,996,195.88 at stop ₹849.35 (-10.1%, charges ₹645,197.2002) — the cash goes back to work at the next Friday screen
2022-09-19  KALYANKJIL  PYRAMID BUY ₹1,687,945,116.61 at ₹95.10 (box jump — doubling the stake with NEW capital; stop stays ₹76.00; charges ₹1,999,912.0362)
2022-09-19  MAHSCOOTER  BUY ₹621,996,195.88 at ₹5,103.50 (fresh Friday signal — BUY: 10.17× weekly, month 2.61×, ladder rising; stop ₹3,847.79; charges ₹736,953.8656)
2022-09-19  SIEMENS     PYRAMID BUY ₹577,166,355.70 at ₹1,737.02 (box jump — doubling the stake with NEW capital; stop stays ₹1,618.44; charges ₹683,838.5504)
2022-09-26  SIEMENS     SELL ₹1,073,779,961.78 at stop ₹1,618.44 (-5.5%, charges ₹1,113,832.8973) — the cash goes back to work at the next Friday screen
2022-09-26  TIINDIA     PYRAMID BUY ₹585,688,002.89 at ₹2,737.75 (box jump — doubling the stake with NEW capital; stop stays ₹2,360.75; charges ₹693,935.1730)
2022-10-03  ACC         PYRAMID BUY ₹1,226,858,513.12 at ₹2,419.80 (box jump — doubling the stake with NEW capital; stop stays ₹2,171.53; charges ₹1,453,607.1600)
2022-10-03  KALYANKJIL  PYRAMID BUY ₹3,437,749,443.97 at ₹96.90 (box jump — doubling the stake with NEW capital; stop stays ₹81.12; charges ₹4,073,116.1357)
2022-10-03  MAHSCOOTER  PYRAMID BUY ₹608,422,578.68 at ₹4,998.05 (box jump — doubling the stake with NEW capital; stop stays ₹4,617.00; charges ₹720,871.5652)
2022-10-03  TSFINV      BUY ₹1,073,779,961.78 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹1,272,236.5489)
2022-10-10  TSFINV      PYRAMID BUY ₹1,030,540,031.64 at ₹99.45 (box jump — doubling the stake with NEW capital; stop stays ₹92.20; charges ₹1,221,004.9917)
2022-10-11  TSFINV      SELL ₹1,907,714,491.33 at stop ₹92.20 (-9.1%, charges ₹1,978,873.9171) — the cash goes back to work at the next Friday screen
2022-10-14  ADANIPOWER  SELL ₹1,888,146,110.47 at stop ₹66.80 (-3.8%, charges ₹1,958,575.6184) — the cash goes back to work at the next Friday screen
2022-10-17  APOLLO      BUY ₹1,788,944,618.07 at ₹24.00 (fresh Friday signal — BUY: 6.98× weekly, month 4.78×, ladder rising; stop ₹14.17; charges ₹2,119,578.3196)
2022-10-24  GODFRYPHLP  BUY ₹2,006,915,983.73 at ₹483.67 (fresh Friday signal — BUY: 4.48× weekly, month 3.07×, ladder rising; stop ₹403.15; charges ₹2,377,835.2697)
2022-10-24  KALYANKJIL  PYRAMID BUY ₹7,222,442,877.80 at ₹101.85 (box jump — doubling the stake with NEW capital; stop stays ₹89.78; charges ₹8,557,298.6350)
2022-10-31  APOLLO      PYRAMID BUY ₹1,615,924,291.00 at ₹21.70 (box jump — doubling the stake with NEW capital; stop stays ₹19.45; charges ₹1,914,580.2831)
2022-10-31  KALYANKJIL  PYRAMID BUY ₹14,982,031,594.52 at ₹105.70 (box jump — doubling the stake with NEW capital; stop stays ₹94.53; charges ₹17,751,018.6903)
2022-10-31  TIINDIA     PYRAMID BUY ₹1,143,849,708.28 at ₹2,675.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,465.49; charges ₹1,355,256.6234)
2022-11-07  ELECON      PYRAMID BUY ₹2,443,053,003.00 at ₹200.85 (box jump — doubling the stake with NEW capital; stop stays ₹164.33; charges ₹2,894,579.3662)
2022-11-14  CGCL        PYRAMID BUY ₹28,484,240.49 at ₹696.24 (box jump — doubling the stake with NEW capital; stop stays ₹661.39; charges ₹33,748.7131)
2022-11-21  ACC         PYRAMID BUY ₹2,485,604,797.08 at ₹2,452.70 (box jump — doubling the stake with NEW capital; stop stays ₹2,259.81; charges ₹2,944,995.6057)
2022-11-21  ELECON      PYRAMID BUY ₹5,189,551,799.92 at ₹213.45 (box jump — doubling the stake with NEW capital; stop stays ₹202.49; charges ₹6,148,687.5404)
2022-11-21  GODFRYPHLP  PYRAMID BUY ₹2,541,936,415.25 at ₹613.33 (box jump — doubling the stake with NEW capital; stop stays ₹497.48; charges ₹3,011,738.4636)
2022-11-22  KALYANKJIL  SELL ₹26,753,940,540.31 at stop ₹94.53 (-6.8%, charges ₹27,751,886.0162) — the cash goes back to work at the next Friday screen
2022-11-28  IOB         BUY ₹5,513,146,386.35 at ₹23.00 (fresh Friday signal — BUY: 7.22× weekly, month 5.74×, ladder rising; stop ₹18.76; charges ₹6,532,089.0514)
2022-11-28  IRFC        BUY ₹5,493,864,596.03 at ₹32.00 (fresh Friday signal — BUY: 9.02× weekly, month 13.28×, ladder rising; stop ₹23.09; charges ₹6,509,243.5903)
2022-11-28  MAHABANK    BUY ₹5,519,793,049.16 at ₹27.60 (fresh Friday signal — BUY: 8.71× weekly, month 8.20×, ladder rising; stop ₹21.47; charges ₹6,539,964.1540)
2022-11-28  SKIPPER     BUY ₹4,723,479,697.11 at ₹89.34 (fresh Friday signal — BUY: 6.40× weekly, month 2.23×, ladder rising; stop ₹65.34; charges ₹5,596,475.7422)
2022-11-28  UCOBANK     BUY ₹5,503,656,811.65 at ₹21.05 (fresh Friday signal — BUY: 13.59× weekly, month 16.04×, ladder rising; stop ₹13.59; charges ₹6,520,845.6085)
2022-12-05  GODFRYPHLP  PYRAMID BUY ₹5,053,247,991.16 at ₹610.00 (box jump — doubling the stake with NEW capital; stop stays ₹547.85; charges ₹5,987,191.9888)
2022-12-05  IOB         PYRAMID BUY ₹5,506,614,297.30 at ₹23.00 (box jump — doubling the stake with NEW capital; stop stays ₹20.76; charges ₹6,524,349.6982)
2022-12-12  APOLLO      PYRAMID BUY ₹3,840,198,029.69 at ₹25.80 (box jump — doubling the stake with NEW capital; stop stays ₹24.42; charges ₹4,549,945.4843)
2022-12-12  UCOBANK     PYRAMID BUY ₹6,163,059,800.41 at ₹23.60 (box jump — doubling the stake with NEW capital; stop stays ₹18.29; charges ₹7,302,119.8104)
2022-12-19  ACC         PYRAMID BUY ₹5,292,871,930.04 at ₹2,612.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,465.15; charges ₹6,271,103.3522)
2022-12-19  IRFC        PYRAMID BUY ₹5,538,799,308.87 at ₹32.30 (box jump — doubling the stake with NEW capital; stop stays ₹28.20; charges ₹6,562,483.1608)
2022-12-19  SKIPPER     PYRAMID BUY ₹6,417,765,327.57 at ₹121.53 (box jump — doubling the stake with NEW capital; stop stays ₹109.70; charges ₹7,603,900.1494)
2022-12-21  ELECON      SELL ₹9,830,138,818.21 at stop ₹202.49 (+2.7%, charges ₹10,196,811.6284) — the cash goes back to work at the next Friday screen
2022-12-22  MAHSCOOTER  SELL ₹1,122,243,235.41 at stop ₹4,617.00 (-8.6%, charges ₹1,164,103.8936) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹9,970,708,396.77 at stop ₹2,465.15 (-1.6%, charges ₹10,342,624.5756) — the cash goes back to work at the next Friday screen
2022-12-23  IRFC        SELL ₹9,655,718,448.99 at stop ₹28.20 (-12.3%, charges ₹10,015,885.2262) — the cash goes back to work at the next Friday screen
2022-12-26  APOLLO      SELL ₹7,257,749,131.27 at stop ₹24.42 (+0.4%, charges ₹7,528,469.5472) — the cash goes back to work at the next Friday screen
2022-12-26  GODFRYPHLP  SELL ₹9,062,015,931.41 at stop ₹547.85 (-5.4%, charges ₹9,400,037.0834) — the cash goes back to work at the next Friday screen
2022-12-26  TIINDIA     PYRAMID BUY ₹2,374,379,093.95 at ₹2,778.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,598.35; charges ₹2,813,213.1086)
2023-01-02  GICRE       BUY ₹14,064,078,190.35 at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 11.13×, ladder rising; stop ₹137.57; charges ₹16,663,408.6468)
2023-01-02  IOB         PYRAMID BUY ₹15,505,096,414.55 at ₹32.40 (box jump — doubling the stake with NEW capital; stop stays ₹21.23; charges ₹18,370,756.6303)
2023-01-02  LLOYDSENGG  BUY ₹14,129,826,898.11 at ₹15.63 (fresh Friday signal — ACCUMULATE: 2.36× weekly, month 2.74×, ladder rising; stop ₹10.86; charges ₹16,741,309.0659)
2023-01-02  MAHABANK    PYRAMID BUY ₹6,162,458,611.32 at ₹30.85 (box jump — doubling the stake with NEW capital; stop stays ₹22.08; charges ₹7,301,407.5092)
2023-01-02  UCOBANK     PYRAMID BUY ₹16,599,084,571.87 at ₹31.80 (box jump — doubling the stake with NEW capital; stop stays ₹23.46; charges ₹19,666,936.2642)
2023-01-02  YESBANK     BUY ₹14,012,038,846.66 at ₹20.85 (fresh Friday signal — ACCUMULATE: 2.89× weekly, month 3.19×, ladder rising; stop ₹15.00; charges ₹16,601,751.3638)
2023-01-09  CGCL        PYRAMID BUY ₹58,396,672.80 at ₹714.12 (box jump — doubling the stake with NEW capital; stop stays ₹666.82; charges ₹69,189.5771)
2023-01-11  TIINDIA     SELL ₹4,434,430,444.08 at stop ₹2,598.35 (-2.9%, charges ₹4,599,838.5937) — the cash goes back to work at the next Friday screen
2023-01-16  ANUP        BUY ₹9,127,060,471.04 at ₹476.12 (fresh Friday signal — ACCUMULATE: 4.79× weekly, month 1.56×, ladder rising; stop ₹364.75; charges ₹10,813,928.6710)
2023-01-16  GICRE       PYRAMID BUY ₹14,662,773,074.32 at ₹187.05 (box jump — doubling the stake with NEW capital; stop stays ₹167.72; charges ₹17,372,754.6396)
2023-01-25  SKIPPER     SELL ₹11,566,838,964.35 at stop ₹109.70 (+4.1%, charges ₹11,998,292.2150) — the cash goes back to work at the next Friday screen
2023-02-01  GICRE       SELL ₹26,252,195,688.19 at stop ₹167.72 (-8.4%, charges ₹27,231,425.6405) — the cash goes back to work at the next Friday screen
2023-02-06  ANUP        PYRAMID BUY ₹10,762,388,409.48 at ₹562.10 (box jump — doubling the stake with NEW capital; stop stays ₹466.90; charges ₹12,751,498.7940)
2023-02-06  JINDALSAW   BUY ₹17,207,625,622.31 at ₹65.22 (fresh Friday signal — BUY: 2.71× weekly, month 3.60×, ladder rising; stop ₹51.25; charges ₹20,387,948.1972)
2023-02-06  LLOYDSENGG  PYRAMID BUY ₹18,976,656,172.20 at ₹21.02 (box jump — doubling the stake with NEW capital; stop stays ₹19.27; charges ₹22,483,931.9199)
2023-02-07  LLOYDSENGG  SELL ₹34,740,536,967.77 at stop ₹19.27 (+5.2%, charges ₹36,036,389.5037) — the cash goes back to work at the next Friday screen
2023-02-13  ANUP        PYRAMID BUY ₹21,814,364,761.60 at ₹570.00 (box jump — doubling the stake with NEW capital; stop stays ₹518.77; charges ₹25,846,107.3292)
2023-02-13  YESBANK     PYRAMID BUY ₹11,444,709,950.83 at ₹17.05 (box jump — doubling the stake with NEW capital; stop stays ₹15.34; charges ₹13,559,927.3677)
2023-02-20  ANUP        PYRAMID BUY ₹43,031,073,672.83 at ₹562.52 (box jump — doubling the stake with NEW capital; stop stays ₹527.27; charges ₹50,984,099.7339)
2023-02-27  CERA        BUY ₹24,302,412,205.34 at ₹6,150.00 (fresh Friday signal — BUY: 5.94× weekly, month 1.75×, ladder rising; stop ₹5,579.40; charges ₹28,793,997.0328)
2023-02-27  SONATSOFTW  BUY ₹24,305,291,946.24 at ₹360.00 (fresh Friday signal — BUY: 9.70× weekly, month 3.34×, ladder rising; stop ₹282.62; charges ₹28,797,409.0089)
2023-03-06  CERA        PYRAMID BUY ₹25,001,826,754.56 at ₹6,334.50 (box jump — doubling the stake with NEW capital; stop stays ₹5,714.25; charges ₹29,622,677.7532)
2023-03-06  IOB         PYRAMID BUY ₹24,965,634,447.27 at ₹26.10 (box jump — doubling the stake with NEW capital; stop stays ₹22.18; charges ₹29,579,796.3643)
2023-03-06  JINDALSAW   PYRAMID BUY ₹19,492,923,065.43 at ₹73.97 (box jump — doubling the stake with NEW capital; stop stays ₹67.92; charges ₹23,095,615.5366)
2023-03-06  SONATSOFTW  PYRAMID BUY ₹27,024,458,849.43 at ₹400.75 (box jump — doubling the stake with NEW capital; stop stays ₹325.85; charges ₹32,019,133.7941)
2023-03-08  CGCL        SELL ₹108,879,627.31 at stop ₹666.82 (-0.9%, charges ₹112,940.9330) — the cash goes back to work at the next Friday screen
2023-03-10  ANUP        SELL ₹80,537,064,218.42 at stop ₹527.27 (-4.7%, charges ₹83,541,167.4366) — the cash goes back to work at the next Friday screen
2023-03-13  YESBANK     SELL ₹20,560,238,360.22 at stop ₹15.34 (-19.1%, charges ₹21,327,153.3058) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹38,255,636,259.99 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.60×, ladder rising; stop ₹691.46; charges ₹45,326,063.4232)
2023-03-20  IOB         SELL ₹42,362,932,915.38 at stop ₹22.18 (-17.5%, charges ₹43,943,107.5137) — the cash goes back to work at the next Friday screen
2023-03-20  SONATSOFTW  PYRAMID BUY ₹53,578,832,637.84 at ₹397.50 (box jump — doubling the stake with NEW capital; stop stays ₹357.20; charges ₹63,481,301.1547)
2023-03-27  CERA        PYRAMID BUY ₹49,621,779,591.45 at ₹6,289.85 (box jump — doubling the stake with NEW capital; stop stays ₹5,852.00; charges ₹58,792,903.4470)
2023-03-27  JINDALSAW   SELL ₹35,736,502,849.75 at stop ₹67.92 (-2.4%, charges ₹37,069,505.7877) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹53,952,316,283.21 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.85×, ladder rising; stop ₹372.21; charges ₹63,923,812.2473)
2023-03-27  MAHABANK    PYRAMID BUY ₹9,742,295,814.89 at ₹24.40 (box jump — doubling the stake with NEW capital; stop stays ₹22.36; charges ₹11,542,872.1403)
2023-03-27  SONATSOFTW  PYRAMID BUY ₹111,458,777,132.74 at ₹413.70 (box jump — doubling the stake with NEW capital; stop stays ₹371.45; charges ₹132,058,647.9613)
2023-03-27  TDPOWERSYS  BUY ₹53,850,905,611.03 at ₹84.62 (fresh Friday signal — BUY: 1.62× weekly, month 2.13×, ladder rising; stop ₹64.12; charges ₹63,803,658.8004)
2023-03-27  UCOBANK     SELL ₹24,451,606,823.23 at stop ₹23.46 (-13.3%, charges ₹25,363,673.2297) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹199,825,769,495.40 at stop ₹371.45 (-7.4%, charges ₹207,279,446.1725) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹53,546,015,405.95 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.04×, ladder rising; stop ₹1,171.71; charges ₹63,442,418.6245)
2023-04-03  TAX         FY2023 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹43,231,489,295.72 / LT ₹0.00)
2023-04-10  CERA        PYRAMID BUY ₹103,097,846,788.92 at ₹6,538.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,037.30; charges ₹122,152,445.9976)
2023-04-10  KIRLOSBROS  BUY ₹68,879,282,516.80 at ₹425.00 (fresh Friday signal — BUY: 1.86× weekly, month 2.34×, ladder rising; stop ₹357.44; charges ₹81,609,588.3672)
2023-04-10  TDPOWERSYS  PYRAMID BUY ₹50,497,905,466.53 at ₹79.45 (box jump — doubling the stake with NEW capital; stop stays ₹73.22; charges ₹59,830,955.3751)
2023-04-24  KIRLOSBROS  PYRAMID BUY ₹69,987,467,977.91 at ₹432.35 (box jump — doubling the stake with NEW capital; stop stays ₹403.85; charges ₹82,922,589.2582)
2023-04-24  MARKSANS    BUY ₹63,999,262,422.73 at ₹78.00 (fresh Friday signal — ACCUMULATE: 1.64× weekly, month 1.51×, ladder rising; stop ₹71.87; charges ₹75,827,640.3482)
2023-04-24  ZFCVINDIA   BUY ₹77,843,817,636.41 at ₹1,697.50 (fresh Friday signal — ACCUMULATE: 7.38× weekly, month 1.55×, ladder rising; stop ₹1,561.17; charges ₹92,230,953.6643)
2023-04-26  CERA        SELL ₹190,094,614,914.66 at stop ₹6,037.30 (-5.7%, charges ₹197,185,310.9806) — the cash goes back to work at the next Friday screen
2023-04-26  KIRLOSBROS  SELL ₹130,535,093,342.20 at stop ₹403.85 (-5.8%, charges ₹135,404,166.9519) — the cash goes back to work at the next Friday screen
2023-05-02  ANURAS      PYRAMID BUY ₹57,575,794,832.50 at ₹1,139.00 (box jump — doubling the stake with NEW capital; stop stays ₹946.20; charges ₹68,216,984.0409)
2023-05-02  ASHAPURMIN  BUY ₹89,157,164,727.68 at ₹143.10 (fresh Friday signal — BUY: 2.05× weekly, month 2.10×, ladder rising; stop ₹123.50; charges ₹105,635,239.6185)
2023-05-02  ICICIBANK   BUY ₹89,124,820,606.01 at ₹924.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.24×, ladder rising; stop ₹838.28; charges ₹105,596,917.6390)
2023-05-02  KSB         PYRAMID BUY ₹58,454,943,170.33 at ₹453.40 (box jump — doubling the stake with NEW capital; stop stays ₹407.74; charges ₹69,258,617.0449)
2023-05-02  REFEX       BUY ₹89,487,966,063.22 at ₹65.32 (fresh Friday signal — BUY: 4.73× weekly, month 1.57×, ladder rising; stop ₹54.53; charges ₹106,027,179.8339)
2023-05-08  HEG         BUY ₹52,859,756,859.96 at ₹234.38 (fresh Friday signal — BUY: 2.69× weekly, month 1.85×, ladder rising; stop ₹201.01; charges ₹62,629,325.4068)
2023-05-08  MAHABANK    PYRAMID BUY ₹24,421,118,523.92 at ₹30.60 (box jump — doubling the stake with NEW capital; stop stays ₹27.79; charges ₹28,934,642.7167)
2023-05-15  ANURAS      PYRAMID BUY ₹118,195,372,574.35 at ₹1,169.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,007.67; charges ₹140,040,304.5770)
2023-05-15  ASHAPURMIN  PYRAMID BUY ₹90,171,674,513.07 at ₹144.90 (box jump — doubling the stake with NEW capital; stop stays ₹125.16; charges ₹106,837,251.6453)
2023-05-15  HAL         PYRAMID BUY ₹57,880,351,950.91 at ₹1,493.47 (box jump — doubling the stake with NEW capital; stop stays ₹1,370.80; charges ₹68,577,829.5689)
2023-05-15  REFEX       PYRAMID BUY ₹99,685,766,191.89 at ₹72.85 (box jump — doubling the stake with NEW capital; stop stays ₹58.14; charges ₹118,109,742.8389)
2023-05-22  MARKSANS    SELL ₹58,838,675,024.19 at stop ₹71.87 (-7.9%, charges ₹61,033,409.2712) — the cash goes back to work at the next Friday screen
2023-05-29  ASHAPURMIN  PYRAMID BUY ₹161,578,487,781.27 at ₹129.90 (box jump — doubling the stake with NEW capital; stop stays ₹134.24; charges ₹191,441,510.3498)
2023-05-29  ASHAPURMIN  SELL ₹333,410,067,925.41 at stop ₹134.24 (-2.0%, charges ₹345,846,556.2397) — the cash goes back to work at the next Friday screen
2023-05-29  TDPOWERSYS  PYRAMID BUY ₹129,584,266,302.37 at ₹102.00 (box jump — doubling the stake with NEW capital; stop stays ₹89.54; charges ₹153,534,099.7378)
2023-06-05  EPL         BUY ₹172,040,470,668.09 at ₹201.90 (fresh Friday signal — ACCUMULATE: 6.59× weekly, month 6.26×, ladder rising; stop ₹170.76; charges ₹203,837,082.5117)
2023-06-05  FORCEMOT    BUY ₹220,208,272,281.50 at ₹1,951.00 (fresh Friday signal — BUY: 23.21× weekly, month 3.12×, ladder rising; stop ₹1,289.01; charges ₹260,907,282.9927)
2023-06-05  HAL         PYRAMID BUY ₹123,314,687,685.60 at ₹1,591.88 (box jump — doubling the stake with NEW capital; stop stays ₹1,415.36; charges ₹146,105,774.2464)
2023-06-05  ICICIBANK   PYRAMID BUY ₹90,849,705,560.75 at ₹943.00 (box jump — doubling the stake with NEW capital; stop stays ₹886.30; charges ₹107,640,596.7540)
2023-06-05  REFEX       PYRAMID BUY ₹287,843,928,603.06 at ₹105.24 (box jump — doubling the stake with NEW capital; stop stays ₹87.60; charges ₹341,043,397.5059)
2023-06-12  HEG         PYRAMID BUY ₹61,537,329,549.83 at ₹273.18 (box jump — doubling the stake with NEW capital; stop stays ₹211.53; charges ₹72,910,691.7244)
2023-06-15  MAHABANK    SELL ₹44,284,836,954.59 at stop ₹27.79 (-3.2%, charges ₹45,936,700.2613) — the cash goes back to work at the next Friday screen
2023-06-19  FORCEMOT    PYRAMID BUY ₹251,175,155,928.59 at ₹2,228.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,995.52; charges ₹297,597,482.6451)
2023-06-19  HAL         PYRAMID BUY ₹301,857,328,043.51 at ₹1,949.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,723.32; charges ₹357,646,760.9291)
2023-06-19  ZFCVINDIA   PYRAMID BUY ₹92,210,248,840.47 at ₹2,013.17 (box jump — doubling the stake with NEW capital; stop stays ₹1,773.33; charges ₹109,252,596.3707)
2023-06-26  ZFCVINDIA   PYRAMID BUY ₹187,073,103,178.30 at ₹2,043.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,860.58; charges ₹221,648,054.2060)
2023-07-03  ANURAS      SELL ₹203,296,342,059.69 at stop ₹1,007.67 (-4.8%, charges ₹210,879,474.1411) — the cash goes back to work at the next Friday screen
2023-07-03  EPL         PYRAMID BUY ₹182,986,013,971.77 at ₹215.00 (box jump — doubling the stake with NEW capital; stop stays ₹189.81; charges ₹216,805,586.9854)
2023-07-03  HEG         PYRAMID BUY ₹147,230,184,171.29 at ₹326.99 (box jump — doubling the stake with NEW capital; stop stays ₹294.79; charges ₹174,441,345.5891)
2023-07-03  TDPOWERSYS  PYRAMID BUY ₹314,627,042,301.66 at ₹123.90 (box jump — doubling the stake with NEW capital; stop stays ₹101.58; charges ₹372,776,580.6092)
2023-07-10  CEATLTD     BUY ₹247,581,179,014.28 at ₹2,408.00 (fresh Friday signal — BUY: 4.55× weekly, month 2.41×, ladder rising; stop ₹1,892.78; charges ₹293,339,264.9944)
2023-07-10  EPL         PYRAMID BUY ₹368,902,418,455.90 at ₹216.85 (box jump — doubling the stake with NEW capital; stop stays ₹200.50; charges ₹437,083,160.8257)
2023-07-10  ZFCVINDIA   PYRAMID BUY ₹367,415,947,134.10 at ₹2,007.77 (box jump — doubling the stake with NEW capital; stop stays ₹1,882.66; charges ₹435,321,959.0789)
2023-07-12  KSB         SELL ₹104,965,220,825.30 at stop ₹407.74 (-6.4%, charges ₹108,880,515.7362) — the cash goes back to work at the next Friday screen
2023-07-17  FORCEMOT    PYRAMID BUY ₹625,087,176,694.32 at ₹2,774.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,337.00; charges ₹740,616,123.1600)
2023-07-17  TDPOWERSYS  PYRAMID BUY ₹632,180,523,924.37 at ₹124.55 (box jump — doubling the stake with NEW capital; stop stays ₹110.20; charges ₹749,020,466.6206)
2023-07-24  ICICIBANK   PYRAMID BUY ₹193,521,367,750.63 at ₹1,004.95 (box jump — doubling the stake with NEW capital; stop stays ₹894.19; charges ₹229,288,090.4869)
2023-07-24  TDPOWERSYS  PYRAMID BUY ₹1,292,780,109,106.11 at ₹127.42 (box jump — doubling the stake with NEW capital; stop stays ₹112.05; charges ₹1,531,712,420.6067)
2023-07-31  CEATLTD     PYRAMID BUY ₹251,816,668,014.12 at ₹2,452.10 (box jump — doubling the stake with NEW capital; stop stays ₹2,244.85; charges ₹298,357,559.3375)
2023-07-31  HEG         PYRAMID BUY ₹305,040,741,601.75 at ₹338.94 (box jump — doubling the stake with NEW capital; stop stays ₹300.49; charges ₹361,418,534.6846)
2023-07-31  REFEX       PYRAMID BUY ₹923,922,572,535.70 at ₹169.00 (box jump — doubling the stake with NEW capital; stop stays ₹121.69; charges ₹1,094,682,436.7605)
2023-08-11  EPL         SELL ₹681,065,421,534.02 at stop ₹200.50 (-5.7%, charges ₹706,469,759.8279) — the cash goes back to work at the next Friday screen
2023-08-11  REFEX       SELL ₹1,328,391,666,430.14 at stop ₹121.69 (-5.0%, charges ₹1,377,941,842.1015) — the cash goes back to work at the next Friday screen
2023-08-14  CEATLTD     SELL ₹460,315,907,460.12 at stop ₹2,244.85 (-7.6%, charges ₹477,486,095.0301) — the cash goes back to work at the next Friday screen
2023-08-14  HAL         PYRAMID BUY ₹585,692,684,469.82 at ₹1,892.42 (box jump — doubling the stake with NEW capital; stop stays ₹1,758.24; charges ₹693,940,719.8036)
2023-08-14  RATEGAIN    BUY ₹1,036,785,310,884.27 at ₹547.00 (fresh Friday signal — BUY: 5.36× weekly, month 1.91×, ladder rising; stop ₹422.99; charges ₹1,228,404,526.8008)
2023-08-14  VARROC      BUY ₹1,039,184,175,634.37 at ₹385.40 (fresh Friday signal — BUY: 6.86× weekly, month 2.37×, ladder rising; stop ₹304.00; charges ₹1,231,246,751.0176)
2023-08-14  ZFCVINDIA   PYRAMID BUY ₹815,684,589,374.53 at ₹2,230.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,046.36; charges ₹966,439,851.6359)
2023-08-21  ICICIBANK   PYRAMID BUY ₹365,932,180,161.61 at ₹950.70 (box jump — doubling the stake with NEW capital; stop stays ₹898.70; charges ₹433,563,961.5005)
2023-08-21  RATEGAIN    PYRAMID BUY ₹1,084,400,358,247.82 at ₹572.80 (box jump — doubling the stake with NEW capital; stop stays ₹489.44; charges ₹1,284,819,812.6957)
2023-08-21  VARROC      PYRAMID BUY ₹1,036,337,018,770.93 at ₹384.80 (box jump — doubling the stake with NEW capital; stop stays ₹347.89; charges ₹1,227,873,381.0991)
2023-08-28  FORCEMOT    PYRAMID BUY ₹1,576,430,454,372.44 at ₹3,500.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,158.80; charges ₹1,867,787,174.4595)
2023-08-28  RATEGAIN    PYRAMID BUY ₹2,185,301,030,611.73 at ₹577.50 (box jump — doubling the stake with NEW capital; stop stays ₹520.60; charges ₹2,589,189,536.3914)
2023-09-04  HAL         PYRAMID BUY ₹1,226,212,548,307.94 at ₹1,982.17 (box jump — doubling the stake with NEW capital; stop stays ₹1,840.70; charges ₹1,452,841,807.6030)
2023-09-04  HEG         PYRAMID BUY ₹631,702,655,069.05 at ₹351.16 (box jump — doubling the stake with NEW capital; stop stays ₹324.38; charges ₹748,454,277.7878)
2023-09-18  VARROC      PYRAMID BUY ₹2,425,389,992,886.25 at ₹450.55 (box jump — doubling the stake with NEW capital; stop stays ₹383.80; charges ₹2,873,651,869.1392)
2023-09-18  ZFCVINDIA   PYRAMID BUY ₹1,883,980,300,449.37 at ₹2,576.83 (box jump — doubling the stake with NEW capital; stop stays ₹2,402.91; charges ₹2,232,178,547.6509)
2023-09-25  FORCEMOT    PYRAMID BUY ₹3,375,163,775,076.44 at ₹3,749.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,341.72; charges ₹3,998,963,349.9551)
2023-10-03  VARROC      PYRAMID BUY ₹5,250,329,365,504.70 at ₹487.95 (box jump — doubling the stake with NEW capital; stop stays ₹450.92; charges ₹6,220,698,048.1621)
2023-10-16  FORCEMOT    PYRAMID BUY ₹7,072,038,235,832.35 at ₹3,930.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,709.99; charges ₹8,379,096,126.6562)
2023-10-16  HEG         PYRAMID BUY ₹1,308,609,568,634.82 at ₹363.94 (box jump — doubling the stake with NEW capital; stop stays ₹328.78; charges ₹1,550,467,489.3154)
2023-10-20  FORCEMOT    SELL ₹13,330,522,340,846.98 at stop ₹3,709.99 (+1.8%, charges ₹13,827,762,530.2221) — the cash goes back to work at the next Friday screen
2023-10-23  APOLLO      BUY ₹4,359,287,781,925.30 at ₹76.15 (fresh Friday signal — BUY: 3.56× weekly, month 3.24×, ladder rising; stop ₹59.94; charges ₹5,164,973,682.3306)
2023-10-23  CRISIL      BUY ₹4,271,877,331,142.28 at ₹4,199.70 (fresh Friday signal — BUY: 3.22× weekly, month 2.05×, ladder rising; stop ₹3,639.83; charges ₹5,061,407,985.2627)
2023-10-23  HEG         SELL ₹2,360,522,097,285.59 at stop ₹328.78 (-5.6%, charges ₹2,448,571,644.3826) — the cash goes back to work at the next Friday screen
2023-10-23  NBCC        BUY ₹4,312,456,911,941.48 at ₹45.87 (fresh Friday signal — BUY: 3.53× weekly, month 3.62×, ladder rising; stop ₹33.69; charges ₹5,109,487,505.8984)
2023-10-23  ZFCVINDIA   PYRAMID BUY ₹3,861,071,230,910.91 at ₹2,642.07 (box jump — doubling the stake with NEW capital; stop stays ₹2,473.96; charges ₹4,574,676,481.7739)
2023-10-25  HAL         SELL ₹2,273,679,009,688.58 at stop ₹1,840.70 (-3.0%, charges ₹2,358,489,233.3579) — the cash goes back to work at the next Friday screen
2023-10-25  VARROC      SELL ₹9,687,977,085,534.96 at stop ₹450.92 (-0.4%, charges ₹10,049,347,138.2232) — the cash goes back to work at the next Friday screen
2023-10-30  ANGELONE    BUY ₹4,342,981,706,972.02 at ₹253.50 (fresh Friday signal — BUY: 1.84× weekly, month 2.75×, ladder rising; stop ₹194.37; charges ₹5,145,653,909.8794)
2023-10-30  CUPID       BUY ₹4,336,300,145,202.88 at ₹6.05 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹3.66; charges ₹5,137,737,458.2891)
2023-10-30  SHAREINDIA  BUY ₹4,340,080,019,941.72 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹5,142,215,931.4995)
2023-11-06  APOLLO      PYRAMID BUY ₹5,483,393,004,734.08 at ₹95.90 (box jump — doubling the stake with NEW capital; stop stays ₹60.83; charges ₹6,496,836,633.9004)
2023-11-06  NBCC        PYRAMID BUY ₹4,235,346,533,368.32 at ₹45.10 (box jump — doubling the stake with NEW capital; stop stays ₹37.78; charges ₹5,018,125,545.8975)
2023-11-06  RATEGAIN    PYRAMID BUY ₹5,302,124,715,242.66 at ₹701.00 (box jump — doubling the stake with NEW capital; stop stays ₹549.53; charges ₹6,282,066,242.1533)
2023-11-13  ANGELONE    PYRAMID BUY ₹4,674,852,546,415.43 at ₹273.19 (box jump — doubling the stake with NEW capital; stop stays ₹236.87; charges ₹5,538,861,295.4453)
2023-11-13  APOLLO      PYRAMID BUY ₹14,046,084,873,215.13 at ₹122.90 (box jump — doubling the stake with NEW capital; stop stays ₹88.83; charges ₹16,642,089,795.2051)
2023-11-13  TDPOWERSYS  PYRAMID BUY ₹2,753,356,644,095.40 at ₹135.78 (box jump — doubling the stake with NEW capital; stop stays ₹113.41; charges ₹3,262,233,492.3120)
2023-11-20  APOLLO      PYRAMID BUY ₹36,196,642,450,722.74 at ₹158.45 (box jump — doubling the stake with NEW capital; stop stays ₹105.78; charges ₹42,886,525,276.4141)
2023-11-20  CRISIL      PYRAMID BUY ₹4,309,791,719,426.08 at ₹4,242.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,861.80; charges ₹5,106,329,731.0762)
2023-11-20  RATEGAIN    PYRAMID BUY ₹10,915,452,834,498.66 at ₹722.00 (box jump — doubling the stake with NEW capital; stop stays ₹619.50; charges ₹12,932,852,667.9668)
2023-11-20  SHAREINDIA  PYRAMID BUY ₹5,144,126,194,092.12 at ₹356.00 (box jump — doubling the stake with NEW capital; stop stays ₹280.63; charges ₹6,094,866,349.7822)
2023-11-20  TDPOWERSYS  PYRAMID BUY ₹5,485,210,929,678.32 at ₹135.32 (box jump — doubling the stake with NEW capital; stop stays ₹124.59; charges ₹6,498,990,548.7061)
2023-11-28  ANGELONE    PYRAMID BUY ₹10,493,567,597,631.97 at ₹306.80 (box jump — doubling the stake with NEW capital; stop stays ₹274.55; charges ₹12,432,994,375.8809)
2023-11-28  CUPID       PYRAMID BUY ₹6,316,144,269,959.96 at ₹8.82 (box jump — doubling the stake with NEW capital; stop stays ₹7.93; charges ₹7,483,497,433.5508)
2023-11-28  SHAREINDIA  PYRAMID BUY ₹9,895,421,316,167.71 at ₹342.61 (box jump — doubling the stake with NEW capital; stop stays ₹321.67; charges ₹11,724,298,378.6230)
2023-12-18  ANGELONE    PYRAMID BUY ₹22,205,290,987,120.09 at ₹324.80 (box jump — doubling the stake with NEW capital; stop stays ₹279.31; charges ₹26,309,284,748.8750)
2023-12-18  SHAREINDIA  PYRAMID BUY ₹21,221,808,760,872.49 at ₹367.60 (box jump — doubling the stake with NEW capital; stop stays ₹328.89; charges ₹25,144,034,811.3359)
2023-12-26  CUPID       PYRAMID BUY ₹13,450,526,251,907.66 at ₹9.40 (box jump — doubling the stake with NEW capital; stop stays ₹8.10; charges ₹15,936,459,710.8379)
2024-01-01  ANGELONE    PYRAMID BUY ₹47,609,238,315,944.49 at ₹348.40 (box jump — doubling the stake with NEW capital; stop stays ₹296.88; charges ₹56,408,403,216.0547)
2024-01-01  ICICIBANK   PYRAMID BUY ₹762,859,162,861.54 at ₹991.55 (box jump — doubling the stake with NEW capital; stop stays ₹939.74; charges ₹903,851,201.5292)
2024-01-01  NBCC        PYRAMID BUY ₹10,255,160,948,216.32 at ₹54.63 (box jump — doubling the stake with NEW capital; stop stays ₹45.65; charges ₹12,150,525,281.9551)
2024-01-01  SHAREINDIA  PYRAMID BUY ₹43,122,370,897,897.45 at ₹373.70 (box jump — doubling the stake with NEW capital; stop stays ₹330.37; charges ₹51,092,270,560.9922)
2024-01-15  RATEGAIN    PYRAMID BUY ₹22,112,606,105,746.55 at ₹731.75 (box jump — doubling the stake with NEW capital; stop stays ₹669.56; charges ₹26,199,469,798.1328)
2024-01-23  ANGELONE    SELL ₹81,005,854,346,417.27 at stop ₹296.88 (-9.1%, charges ₹84,027,443,847.9994) — the cash goes back to work at the next Friday screen
2024-01-23  APOLLO      PYRAMID BUY ₹55,067,579,956,869.61 at ₹120.60 (box jump — doubling the stake with NEW capital; stop stays ₹112.10; charges ₹65,245,199,549.8359)
2024-01-24  CRISIL      SELL ₹7,834,256,286,637.67 at stop ₹3,861.80 (-8.5%, charges ₹8,126,480,925.7011) — the cash goes back to work at the next Friday screen
2024-01-29  IDBI        BUY ₹44,030,458,348,946.03 at ₹84.30 (fresh Friday signal — BUY: 8.31× weekly, month 1.96×, ladder rising; stop ₹60.23; charges ₹52,168,191,220.6328)
2024-01-29  NBCC        PYRAMID BUY ₹29,265,253,370,192.78 at ₹78.00 (box jump — doubling the stake with NEW capital; stop stays ₹53.58; charges ₹34,674,073,157.2031)
2024-01-29  RITES       BUY ₹46,998,137,650,070.28 at ₹342.50 (fresh Friday signal — BUY: 11.32× weekly, month 2.99×, ladder rising; stop ₹240.21; charges ₹55,684,358,598.1250)
2024-02-02  ZFCVINDIA   SELL ₹7,219,011,338,765.98 at stop ₹2,473.96 (-0.7%, charges ₹7,488,286,801.0028) — the cash goes back to work at the next Friday screen
2024-02-05  CUPID       PYRAMID BUY ₹48,937,547,381,696.09 at ₹17.11 (box jump — doubling the stake with NEW capital; stop stays ₹16.11; charges ₹57,982,211,074.0859)
2024-02-13  APOLLO      SELL ₹102,206,066,461,824.92 at stop ₹112.10 (-11.0%, charges ₹106,018,442,492.0608) — the cash goes back to work at the next Friday screen
2024-02-19  IDBI        PYRAMID BUY ₹47,708,358,658,647.54 at ₹91.45 (box jump — doubling the stake with NEW capital; stop stays ₹72.11; charges ₹56,525,843,033.5312)
2024-02-19  NBCC        PYRAMID BUY ₹68,245,138,111,766.41 at ₹91.00 (box jump — doubling the stake with NEW capital; stop stays ₹69.28; charges ₹80,858,241,053.9141)
2024-02-19  PRUDENT     BUY ₹86,598,751,263,952.67 at ₹1,332.00 (fresh Friday signal — BUY: 19.33× weekly, month 4.96×, ladder rising; stop ₹1,008.17; charges ₹102,603,978,809.4688)
2024-02-19  RATEGAIN    PYRAMID BUY ₹52,791,167,934,733.73 at ₹874.00 (box jump — doubling the stake with NEW capital; stop stays ₹720.34; charges ₹62,548,059,839.7109)
2024-02-19  RITES       PYRAMID BUY ₹52,095,843,784,200.20 at ₹380.10 (box jump — doubling the stake with NEW capital; stop stays ₹314.37; charges ₹61,724,225,507.6250)
2024-02-19  SHAREINDIA  PYRAMID BUY ₹89,120,589,349,893.30 at ₹386.39 (box jump — doubling the stake with NEW capital; stop stays ₹357.20; charges ₹105,591,904,359.8281)
2024-02-26  CUPID       PYRAMID BUY ₹140,077,695,737,895.97 at ₹24.50 (box jump — doubling the stake with NEW capital; stop stays ₹17.77; charges ₹165,966,930,416.3750)
2024-02-26  PRUDENT     PYRAMID BUY ₹89,746,246,513,087.22 at ₹1,382.05 (box jump — doubling the stake with NEW capital; stop stays ₹1,176.05; charges ₹106,333,195,814.6875)
2024-03-04  RATEGAIN    PYRAMID BUY ₹99,181,356,619,690.16 at ₹821.50 (box jump — doubling the stake with NEW capital; stop stays ₹730.99; charges ₹117,512,108,019.7031)
2024-03-06  SHAREINDIA  SELL ₹164,507,612,801,051.38 at stop ₹357.20 (-4.6%, charges ₹170,643,891,219.2048) — the cash goes back to work at the next Friday screen
2024-03-11  BHEL        BUY ₹73,239,452,399,032.83 at ₹259.10 (fresh Friday signal — BUY: 3.01× weekly, month 1.67×, ladder rising; stop ₹188.78; charges ₹86,775,607,180.0938)
2024-03-11  ICICIBANK   PYRAMID BUY ₹1,673,059,258,288.26 at ₹1,087.95 (box jump — doubling the stake with NEW capital; stop stays ₹986.58; charges ₹1,982,274,965.6189)
2024-03-11  SOLARINDS   BUY ₹114,094,486,938,656.80 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹135,181,491,063.8750)
2024-03-13  PRUDENT     SELL ₹152,489,767,867,519.50 at stop ₹1,176.05 (-13.3%, charges ₹158,177,770,116.3048) — the cash goes back to work at the next Friday screen
2024-03-13  RATEGAIN    SELL ₹176,220,443,840,833.72 at stop ₹730.99 (-9.2%, charges ₹182,793,621,142.2735) — the cash goes back to work at the next Friday screen
2024-03-13  RITES       SELL ₹86,033,715,783,284.09 at stop ₹314.37 (-13.0%, charges ₹89,242,848,931.6264) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹98,119,670,004,188.56 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹116,254,199,915.8281)
2024-03-18  FORCEMOT    BUY ₹105,431,958,022,380.38 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 3.03× weekly, month 1.69×, ladder rising; stop ₹5,500.61; charges ₹124,917,948,918.1719)
2024-03-18  ICICIBANK   PYRAMID BUY ₹3,304,484,274,593.32 at ₹1,075.05 (box jump — doubling the stake with NEW capital; stop stays ₹1,002.87; charges ₹3,915,220,826.3735)
2024-03-18  INDIGO      BUY ₹105,282,751,697,808.11 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹124,741,166,200.8594)
2024-03-18  JIOFIN      BUY ₹105,909,547,767,260.25 at ₹346.95 (fresh Friday signal — BUY: 2.56× weekly, month 2.25×, ladder rising; stop ₹290.75; charges ₹125,483,807,055.2500)
2024-03-26  BOSCHLTD    PYRAMID BUY ₹100,478,244,295,098.94 at ₹30,245.00 (box jump — doubling the stake with NEW capital; stop stays ₹26,710.20; charges ₹119,048,687,169.2031)
2024-03-26  JIOFIN      PYRAMID BUY ₹105,189,514,530,251.41 at ₹345.00 (box jump — doubling the stake with NEW capital; stop stays ₹301.05; charges ₹124,630,696,890.1094)
2024-04-01  IDBI        PYRAMID BUY ₹84,776,200,840,431.53 at ₹81.30 (box jump — doubling the stake with NEW capital; stop stays ₹74.19; charges ₹100,444,583,641.4688)
2024-04-01  SOLARINDS   PYRAMID BUY ₹134,840,796,371,755.25 at ₹8,950.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,980.95; charges ₹159,762,144,507.2500)
2024-04-01  TAX         FY2024 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹84,147,275,976,707.69 / LT ₹0.00)
2024-04-08  BOSCHLTD    PYRAMID BUY ₹205,718,098,469,030.50 at ₹30,980.00 (box jump — doubling the stake with NEW capital; stop stays ₹28,244.40; charges ₹243,739,027,502.8750)
2024-04-15  INDIGO      PYRAMID BUY ₹120,612,951,891,924.41 at ₹3,670.30 (box jump — doubling the stake with NEW capital; stop stays ₹3,287.00; charges ₹142,904,702,197.6719)
2024-04-29  FORCEMOT    PYRAMID BUY ₹161,944,222,841,043.84 at ₹10,100.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,483.47; charges ₹191,874,840,758.9688)
2024-04-29  IDBI        PYRAMID BUY ₹184,458,772,485,905.44 at ₹88.50 (box jump — doubling the stake with NEW capital; stop stays ₹78.19; charges ₹218,550,541,516.1875)
2024-04-29  NBCC        PYRAMID BUY ₹137,908,422,575,692.94 at ₹92.00 (box jump — doubling the stake with NEW capital; stop stays ₹74.74; charges ₹163,396,731,027.6094)
2024-05-13  INDIGO      PYRAMID BUY ₹263,139,968,593,657.91 at ₹4,006.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,719.77; charges ₹311,773,638,389.0000)
2024-05-13  NBCC        PYRAMID BUY ₹265,466,255,761,345.03 at ₹88.60 (box jump — doubling the stake with NEW capital; stop stays ₹80.15; charges ₹314,529,871,195.7500)
2024-05-21  BHEL        PYRAMID BUY ₹88,059,899,233,419.02 at ₹311.90 (box jump — doubling the stake with NEW capital; stop stays ₹251.68; charges ₹104,335,176,928.4688)
2024-05-21  FORCEMOT    PYRAMID BUY ₹288,041,874,300,637.81 at ₹8,987.50 (box jump — doubling the stake with NEW capital; stop stays ₹8,083.65; charges ₹341,277,927,633.1250)
2024-05-21  ICICIBANK   PYRAMID BUY ₹6,894,740,565,634.99 at ₹1,122.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,051.37; charges ₹8,169,030,206.1855)
2024-05-21  JIOFIN      PYRAMID BUY ₹220,005,326,983,374.50 at ₹361.00 (box jump — doubling the stake with NEW capital; stop stays ₹317.61; charges ₹260,666,829,236.0000)
2024-05-21  TDPOWERSYS  PYRAMID BUY ₹13,287,148,350,153.34 at ₹164.00 (box jump — doubling the stake with NEW capital; stop stays ₹129.90; charges ₹15,742,886,217.8613)
2024-05-27  BOSCHLTD    PYRAMID BUY ₹410,143,903,870,050.25 at ₹30,901.00 (box jump — doubling the stake with NEW capital; stop stays ₹29,015.09; charges ₹485,946,919,641.4375)
2024-05-28  FORCEMOT    SELL ₹517,304,914,936,162.19 at stop ₹8,083.65 (-6.7%, charges ₹536,600,842,529.2903) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹401,804,185,418,210.50 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹476,065,849,962.9375)
2024-06-04  BHEL        SELL ₹141,884,153,359,139.41 at stop ₹251.68 (-11.8%, charges ₹147,176,556,873.5504) — the cash goes back to work at the next Friday screen
2024-06-04  BOSCHLTD    SELL ₹768,971,115,977,805.25 at stop ₹29,015.09 (-5.4%, charges ₹797,654,413,867.8818) — the cash goes back to work at the next Friday screen
2024-06-04  CUPID       SELL ₹202,867,609,094,667.50 at stop ₹17.77 (-4.6%, charges ₹210,434,749,060.0103) — the cash goes back to work at the next Friday screen
2024-06-04  IDBI        SELL ₹325,409,056,002,202.81 at stop ₹78.19 (-9.7%, charges ₹337,547,099,545.7124) — the cash goes back to work at the next Friday screen
2024-06-04  JIOFIN      SELL ₹386,493,808,233,726.69 at stop ₹317.61 (-10.1%, charges ₹400,910,366,676.4213) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹240,090,646,936,419.81 at stop ₹7,980.95 (-3.3%, charges ₹249,046,238,900.2892) — the cash goes back to work at the next Friday screen
2024-06-05  ICICIBANK   SELL ₹12,898,096,558,303.05 at stop ₹1,051.37 (-3.3%, charges ₹13,379,206,886.2591) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹478,965,207,510,629.62 at ₹156.60 (fresh Friday signal — BUY: 7.81× weekly, month 1.77×, ladder rising; stop ₹126.55; charges ₹567,487,813,445.5000)
2024-06-10  CAMPUS      PYRAMID BUY ₹405,537,855,088,194.25 at ₹289.00 (box jump — doubling the stake with NEW capital; stop stays ₹248.05; charges ₹480,489,578,459.1250)
2024-06-10  DABUR       BUY ₹476,924,153,149,022.56 at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹565,069,530,324.6250)
2024-06-10  FIEMIND     BUY ₹480,501,930,617,444.06 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹569,308,554,539.1875)
2024-06-10  INDIGO      PYRAMID BUY ₹577,421,413,730,570.50 at ₹4,398.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,805.04; charges ₹684,140,748,380.5000)
2024-06-10  NCC         BUY ₹279,628,069,718,786.69 at ₹327.60 (fresh Friday signal — BUY: 2.80× weekly, month 1.63×, ladder rising; stop ₹260.92; charges ₹331,309,079,186.4688)
2024-06-10  UNOMINDA    BUY ₹478,095,854,684,333.19 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.61×, ladder rising; stop ₹769.64; charges ₹566,457,786,364.6875)
2024-06-18  DABUR       PYRAMID BUY ₹479,433,893,989,623.00 at ₹608.10 (box jump — doubling the stake with NEW capital; stop stays ₹552.95; charges ₹568,043,122,810.3125)
2024-06-18  UNOMINDA    PYRAMID BUY ₹520,162,433,775,663.38 at ₹1,056.60 (box jump — doubling the stake with NEW capital; stop stays ₹895.00; charges ₹616,299,133,112.5000)
2024-06-24  FIEMIND     PYRAMID BUY ₹467,697,976,053,498.19 at ₹1,286.35 (box jump — doubling the stake with NEW capital; stop stays ₹1,162.80; charges ₹554,138,166,241.6250)
2024-07-01  INDIGO      PYRAMID BUY ₹1,122,234,337,276,030.50 at ₹4,276.35 (box jump — doubling the stake with NEW capital; stop stays ₹3,976.70; charges ₹1,329,646,287,972.0000)
2024-07-01  NCC         PYRAMID BUY ₹269,833,408,859,687.00 at ₹316.50 (box jump — doubling the stake with NEW capital; stop stays ₹297.87; charges ₹319,704,163,866.5000)
2024-07-08  NBCC        PYRAMID BUY ₹756,639,681,736,453.75 at ₹126.34 (box jump — doubling the stake with NEW capital; stop stays ₹98.17; charges ₹896,482,232,574.6250)
2024-07-08  TDPOWERSYS  PYRAMID BUY ₹33,137,463,867,121.49 at ₹204.62 (box jump — doubling the stake with NEW capital; stop stays ₹162.59; charges ₹39,261,947,670.1016)
2024-07-08  UNOMINDA    PYRAMID BUY ₹1,155,625,348,050,682.50 at ₹1,174.40 (box jump — doubling the stake with NEW capital; stop stays ₹981.87; charges ₹1,369,208,643,224.7500)
2024-07-15  TDPOWERSYS  PYRAMID BUY ₹66,000,988,412,374.88 at ₹203.90 (box jump — doubling the stake with NEW capital; stop stays ₹188.72; charges ₹78,199,326,406.2891)
2024-07-19  TDPOWERSYS  SELL ₹121,975,756,390,207.80 at stop ₹188.72 (-0.7%, charges ₹126,525,559,215.3229) — the cash goes back to work at the next Friday screen
2024-07-19  UNOMINDA    SELL ₹1,929,200,589,292,898.75 at stop ₹981.87 (-10.2%, charges ₹2,001,161,465,381.2493) — the cash goes back to work at the next Friday screen
2024-07-22  FIEMIND     PYRAMID BUY ₹944,035,073,120,877.25 at ₹1,299.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,257.56; charges ₹1,118,512,140,465.5000)
2024-07-22  INDIAGLYCO  BUY ₹1,004,108,422,955,927.50 at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹1,189,688,278,960.8750)
2024-07-22  PGIL        BUY ₹1,047,067,922,727,179.00 at ₹405.00 (fresh Friday signal — BUY: 3.81× weekly, month 8.12×, ladder rising; stop ₹335.38; charges ₹1,240,587,576,466.5000)
2024-07-23  FIEMIND     SELL ₹1,824,862,185,850,145.00 at stop ₹1,257.56 (-3.3%, charges ₹1,892,931,147,866.3813) — the cash goes back to work at the next Friday screen
2024-07-23  NCC         SELL ₹507,073,774,060,888.19 at stop ₹297.87 (-7.5%, charges ₹525,988,071,114.9971) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹1,094,313,057,209,546.00 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹1,296,564,581,983.6250)
2024-07-29  THYROCARE   BUY ₹1,095,320,838,743,968.75 at ₹261.67 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹196.33; charges ₹1,297,758,622,240.3750)
2024-08-05  DABUR       PYRAMID BUY ₹969,173,397,610,110.00 at ₹615.00 (box jump — doubling the stake with NEW capital; stop stays ₹587.15; charges ₹1,148,296,543,537.7500)
2024-08-05  NBCC        PYRAMID BUY ₹1,387,009,764,016,220.25 at ₹115.87 (box jump — doubling the stake with NEW capital; stop stays ₹109.78; charges ₹1,643,357,650,757.2500)
2024-08-05  THYROCARE   PYRAMID BUY ₹1,114,858,154,723,007.88 at ₹266.65 (box jump — doubling the stake with NEW capital; stop stays ₹243.17; charges ₹1,320,906,835,412.6250)
2024-08-06  NBCC        SELL ₹2,624,016,038,194,513.50 at stop ₹109.78 (-1.3%, charges ₹2,721,894,140,671.9595) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹386,197,299,039,599.44 at stop ₹126.55 (-19.2%, charges ₹400,602,797,428.9766) — the cash goes back to work at the next Friday screen
2024-08-12  AVANTIFEED  PYRAMID BUY ₹1,187,567,550,221,016.75 at ₹758.00 (box jump — doubling the stake with NEW capital; stop stays ₹596.83; charges ₹1,407,054,420,291.7500)
2024-08-12  CAMPUS      PYRAMID BUY ₹818,588,979,693,791.38 at ₹291.85 (box jump — doubling the stake with NEW capital; stop stays ₹277.07; charges ₹969,881,032,928.0000)
2024-08-12  CERA        BUY ₹1,848,431,394,210,859.00 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹2,190,059,473,540.0000)
2024-08-12  INDIAGLYCO  PYRAMID BUY ₹1,169,520,089,534,470.50 at ₹600.55 (box jump — doubling the stake with NEW capital; stop stays ₹535.82; charges ₹1,385,671,418,264.2500)
2024-08-12  PGIL        PYRAMID BUY ₹1,239,950,964,582,699.75 at ₹480.18 (box jump — doubling the stake with NEW capital; stop stays ₹388.64; charges ₹1,469,119,365,324.7500)
2024-08-16  CAMPUS      SELL ₹1,551,736,869,115,880.50 at stop ₹277.07 (-4.4%, charges ₹1,609,618,016,975.7310) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹1,846,739,609,744,407.25 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.15×, ladder rising; stop ₹361.00; charges ₹2,188,055,012,563.2500)
2024-08-19  VGUARD      BUY ₹1,009,081,266,352,245.75 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹1,195,580,205,934.5000)
2024-08-26  AVANTIFEED  PYRAMID BUY ₹2,176,439,303,410,436.00 at ₹695.00 (box jump — doubling the stake with NEW capital; stop stays ₹650.13; charges ₹2,578,689,980,027.0000)
2024-08-26  INDIAGLYCO  PYRAMID BUY ₹2,477,590,698,725,594.50 at ₹636.50 (box jump — doubling the stake with NEW capital; stop stays ₹587.91; charges ₹2,935,500,337,363.0000)
2024-08-26  SUPRIYA     PYRAMID BUY ₹1,950,403,660,997,705.25 at ₹558.30 (box jump — doubling the stake with NEW capital; stop stays ₹470.87; charges ₹2,310,878,309,237.2500)
2024-09-09  AVANTIFEED  SELL ₹4,065,222,687,606,439.50 at stop ₹650.13 (-8.6%, charges ₹4,216,859,063,687.7993) — the cash goes back to work at the next Friday screen
2024-09-09  INDIGO      PYRAMID BUY ₹2,507,326,178,720,106.50 at ₹4,780.00 (box jump — doubling the stake with NEW capital; stop stays ₹4,485.14; charges ₹2,970,731,544,681.0000)
2024-09-09  SUPRIYA     PYRAMID BUY ₹4,189,679,144,208,677.00 at ₹600.00 (box jump — doubling the stake with NEW capital; stop stays ₹498.75; charges ₹4,964,017,885,437.5000)
2024-09-09  THYROCARE   PYRAMID BUY ₹2,354,586,179,206,966.00 at ₹281.75 (box jump — doubling the stake with NEW capital; stop stays ₹265.38; charges ₹2,789,762,056,730.5000)
2024-09-16  DABUR       PYRAMID BUY ₹2,078,944,730,287,171.00 at ₹660.00 (box jump — doubling the stake with NEW capital; stop stays ₹602.49; charges ₹2,463,176,407,732.0000)
2024-09-16  PGIL        PYRAMID BUY ₹2,516,240,942,942,753.00 at ₹487.50 (box jump — doubling the stake with NEW capital; stop stays ₹434.53; charges ₹2,981,293,940,397.5000)
2024-09-16  PRSMJOHNSN  BUY ₹3,930,822,996,697,639.50 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹4,657,319,806,236.0000)
2024-09-19  CERA        SELL ₹1,440,151,392,605,504.75 at stop ₹8,198.93 (-21.9%, charges ₹1,493,870,304,203.8757) — the cash goes back to work at the next Friday screen
2024-09-23  PGIL        SELL ₹4,478,367,697,496,616.00 at stop ₹434.53 (-6.6%, charges ₹4,645,414,745,245.9355) — the cash goes back to work at the next Friday screen
2024-09-30  PRSMJOHNSN  PYRAMID BUY ₹3,825,316,425,669,215.50 at ₹209.00 (box jump — doubling the stake with NEW capital; stop stays ₹168.72; charges ₹4,532,313,454,296.0000)
2024-09-30  VIYASH      BUY ₹4,051,935,224,277,154.50 at ₹216.00 (fresh Friday signal — BUY: 5.97× weekly, month 2.57×, ladder rising; stop ₹161.73; charges ₹4,800,816,060,521.0000)
2024-10-03  DABUR       SELL ₹3,789,406,793,410,931.00 at stop ₹602.49 (-5.2%, charges ₹3,930,754,994,433.8975) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹807,240,261,761,892.25 at stop ₹420.24 (-19.8%, charges ₹837,351,032,395.3734) — the cash goes back to work at the next Friday screen
2024-10-07  BSE         BUY ₹2,735,300,389,724,739.00 at ₹1,396.67 (fresh Friday signal — ACCUMULATE: 2.88× weekly, month 3.26×, ladder rising; stop ₹1,131.31; charges ₹3,240,840,071,347.0000)
2024-10-07  CEMPRO      BUY ₹3,862,330,222,181,851.00 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹4,576,168,160,485.5000)
2024-10-07  INDIGO      SELL ₹4,697,657,184,606,306.00 at stop ₹4,485.14 (+0.3%, charges ₹4,872,883,922,791.6328) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹4,428,342,814,783,077.00 at stop ₹265.38 (-2.8%, charges ₹4,593,523,890,478.3438) — the cash goes back to work at the next Friday screen
2024-10-14  PAYTM       BUY ₹3,994,891,330,880,873.00 at ₹729.60 (fresh Friday signal — BUY: 1.93× weekly, month 2.08×, ladder rising; stop ₹617.60; charges ₹4,733,229,284,224.5000)
2024-10-14  SKIPPER     BUY ₹5,131,108,668,508,511.00 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.80×, ladder rising; stop ₹418.00; charges ₹6,079,442,918,155.0000)
2024-10-14  SUPRIYA     PYRAMID BUY ₹7,983,589,204,573,760.00 at ₹572.00 (box jump — doubling the stake with NEW capital; stop stays ₹500.65; charges ₹9,459,120,433,189.0000)
2024-10-14  VIYASH      PYRAMID BUY ₹3,588,084,440,617,988.00 at ₹191.50 (box jump — doubling the stake with NEW capital; stop stays ₹172.84; charges ₹4,251,236,126,830.5000)
2024-10-23  VIYASH      SELL ₹6,466,369,430,776,692.00 at stop ₹172.84 (-15.2%, charges ₹6,707,570,688,920.7061) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹4,569,454,735,895,711.00 at stop ₹587.91 (-1.5%, charges ₹4,739,899,410,164.4648) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       PYRAMID BUY ₹4,089,146,398,799,087.50 at ₹747.70 (box jump — doubling the stake with NEW capital; stop stays ₹636.31; charges ₹4,844,904,624,229.0000)
2024-10-28  PRSMJOHNSN  PYRAMID BUY ₹6,987,584,702,085,502.00 at ₹191.00 (box jump — doubling the stake with NEW capital; stop stays ₹170.55; charges ₹8,279,033,845,613.0000)
2024-11-04  BSE         PYRAMID BUY ₹2,897,678,702,770,244.50 at ₹1,481.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,231.60; charges ₹6,840,376,808,686.5000)
2024-11-04  CEMPRO      PYRAMID BUY ₹3,222,303,840,405,755.50 at ₹547.15 (box jump — doubling the stake with NEW capital; stop stays ₹430.14; charges ₹7,606,699,955,858.0000)
2024-11-04  JSWDULUX    BUY ₹7,292,943,310,156,644.00 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹17,216,015,094,485.0000)
2024-11-04  KIRLPNU     BUY ₹3,742,880,856,515,760.00 at ₹849.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.99×, ladder rising; stop ₹594.25; charges ₹8,835,594,983,015.5000)
2024-11-04  SKIPPER     PYRAMID BUY ₹5,061,545,590,517,492.00 at ₹546.15 (box jump — doubling the stake with NEW capital; stop stays ₹448.15; charges ₹11,948,487,953,611.0000)
2024-11-11  KIRLPNU     PYRAMID BUY ₹3,716,452,586,566,748.00 at ₹845.00 (box jump — doubling the stake with NEW capital; stop stays ₹752.42; charges ₹8,773,207,346,774.0000)
2024-11-25  PAYTM       PYRAMID BUY ₹9,989,162,343,987,684.00 at ₹913.80 (box jump — doubling the stake with NEW capital; stop stays ₹712.50; charges ₹23,580,818,111,646.0000)
2024-11-25  SUPRIYA     PYRAMID BUY ₹22,569,571,511,485,828.00 at ₹809.00 (box jump — doubling the stake with NEW capital; stop stays ₹574.32; charges ₹53,278,637,621,752.0000)
2024-12-09  JSWDULUX    PYRAMID BUY ₹5,988,545,173,118,116.00 at ₹3,718.70 (box jump — doubling the stake with NEW capital; stop stays ₹3,423.18; charges ₹14,136,800,426,081.0000)
2024-12-09  PAYTM       PYRAMID BUY ₹21,781,417,457,863,396.00 at ₹997.45 (box jump — doubling the stake with NEW capital; stop stays ₹838.09; charges ₹51,418,089,485,436.0000)
2024-12-09  SUPRIYA     PYRAMID BUY ₹43,469,683,832,599,416.00 at ₹780.00 (box jump — doubling the stake with NEW capital; stop stays ₹717.25; charges ₹102,616,282,780,136.0000)
2024-12-16  CEMPRO      PYRAMID BUY ₹6,057,004,395,492,156.00 at ₹514.85 (box jump — doubling the stake with NEW capital; stop stays ₹477.71; charges ₹14,298,408,017,917.0000)
2024-12-16  KIRLPNU     PYRAMID BUY ₹7,441,264,578,015,461.00 at ₹846.95 (box jump — doubling the stake with NEW capital; stop stays ₹798.00; charges ₹17,566,148,240,692.0000)
2024-12-17  SUPRIYA     SELL ₹79,673,878,541,705,024.00 at stop ₹717.25 (-2.4%, charges ₹176,967,521,166,533.5625) — the cash goes back to work at the next Friday screen
2024-12-23  KAYNES      BUY ₹23,178,821,861,057,600.00 at ₹7,358.80 (fresh Friday signal — BUY: 3.40× weekly, month 2.00×, ladder rising; stop ₹5,824.55; charges ₹54,716,858,483,820.0000)
2024-12-23  KIRLPNU     SELL ₹13,974,793,168,954,596.00 at stop ₹798.00 (-5.8%, charges ₹31,040,091,824,202.7500) — the cash goes back to work at the next Friday screen
2024-12-23  PAYTM       PYRAMID BUY ₹41,869,023,880,722,296.00 at ₹959.80 (box jump — doubling the stake with NEW capital; stop stays ₹887.49; charges ₹98,837,700,564,328.0000)
2024-12-23  ZENTEC      BUY ₹23,164,391,369,791,968.00 at ₹2,555.00 (fresh Friday signal — BUY: 3.53× weekly, month 2.25×, ladder rising; stop ₹1,537.95; charges ₹54,682,793,286,148.0000)
2024-12-26  PRSMJOHNSN  SELL ₹12,443,842,850,935,554.00 at stop ₹170.55 (-15.3%, charges ₹27,639,623,718,873.4844) — the cash goes back to work at the next Friday screen
2024-12-27  JSWDULUX    SELL ₹10,987,868,310,739,780.00 at stop ₹3,423.18 (-16.9%, charges ₹24,405,687,955,031.4062) — the cash goes back to work at the next Friday screen
2024-12-30  KAYNES      PYRAMID BUY ₹22,273,150,610,544,256.00 at ₹7,088.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,670.80; charges ₹52,578,894,529,296.0000)
2024-12-30  KFINTECH    BUY ₹34,491,717,623,971,248.00 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.22×, ladder rising; stop ₹1,159.14; charges ₹81,422,534,907,412.0000)
2024-12-30  PAYTM       PYRAMID BUY ₹88,623,751,439,794,976.00 at ₹1,017.00 (box jump — doubling the stake with NEW capital; stop stays ₹893.05; charges ₹209,208,789,596,992.0000)
2025-01-06  BSE         PYRAMID BUY ₹6,968,624,182,649,351.00 at ₹1,783.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,651.54; charges ₹16,450,414,327,121.0000)
2025-01-06  LLOYDSME    BUY ₹36,245,452,017,514,128.00 at ₹1,439.00 (fresh Friday signal — BUY: 2.97× weekly, month 1.94×, ladder rising; stop ₹1,064.09; charges ₹85,562,470,802,552.0000)
2025-01-06  SKIPPER     PYRAMID BUY ₹10,313,865,411,179,408.00 at ₹557.10 (box jump — doubling the stake with NEW capital; stop stays ₹477.28; charges ₹24,347,325,222,460.0000)
2025-01-06  ZENTEC      PYRAMID BUY ₹22,914,791,073,639,400.00 at ₹2,533.45 (box jump — doubling the stake with NEW capital; stop stays ₹2,213.55; charges ₹54,093,576,795,164.0000)
2025-01-09  PAYTM       SELL ₹155,116,670,829,887,040.00 at stop ₹893.05 (-8.5%, charges ₹344,537,171,163,335.8750) — the cash goes back to work at the next Friday screen
2025-01-10  KAYNES      SELL ₹41,782,015,757,237,912.00 at stop ₹6,670.80 (-7.7%, charges ₹92,804,064,434,104.8906) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹17,612,258,900,505,066.00 at stop ₹477.28 (-13.7%, charges ₹39,119,443,622,091.5547) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹37,829,189,816,152,544.00 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 4.81×, ladder rising; stop ₹697.76; charges ₹89,301,105,903,296.0000)
2025-01-13  LLOYDSME    PYRAMID BUY ₹36,232,762,152,469,368.00 at ₹1,441.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,258.75; charges ₹85,532,514,597,104.0000)
2025-01-13  ZENTEC      SELL ₹39,906,755,875,238,840.00 at stop ₹2,213.55 (-13.0%, charges ₹88,638,833,634,066.5625) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹26,330,975,080,116,648.00 at stop ₹1,159.14 (-23.3%, charges ₹58,485,007,572,298.5234) — the cash goes back to work at the next Friday screen
2025-01-20  AEGISLOG    PYRAMID BUY ₹36,335,918,729,474,984.00 at ₹803.60 (box jump — doubling the stake with NEW capital; stop stays ₹700.36; charges ₹85,776,030,158,832.0000)
2025-01-20  APOLLO      BUY ₹41,257,231,876,549,216.00 at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 5.79×, ladder rising; stop ₹110.19; charges ₹97,393,479,770,256.0000)
2025-01-24  AEGISLOG    SELL ₹63,120,593,689,028,048.00 at stop ₹700.36 (-14.5%, charges ₹140,200,216,233,482.1250) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹39,453,590,994,755,904.00 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹93,135,732,613,112.0000)
2025-01-28  LLOYDSME    SELL ₹63,046,257,056,878,664.00 at stop ₹1,258.75 (-12.6%, charges ₹140,035,103,529,492.7344) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹40,024,692,790,573,728.00 at ₹947.00 (fresh Friday signal — BUY: 4.92× weekly, month 3.02×, ladder rising; stop ₹727.84; charges ₹94,483,898,465,936.0000)
2025-02-10  ZENSARTECH  PYRAMID BUY ₹38,793,863,454,259,528.00 at ₹920.05 (box jump — doubling the stake with NEW capital; stop stays ₹814.20; charges ₹91,578,353,265,384.0000)
2025-02-17  APOLLO      SELL ₹34,413,316,469,917,340.00 at stop ₹110.19 (-16.2%, charges ₹76,437,088,569,911.9688) — the cash goes back to work at the next Friday screen
2025-02-17  ZENSARTECH  SELL ₹68,428,374,691,287,072.00 at stop ₹814.20 (-12.8%, charges ₹151,989,586,401,685.0625) — the cash goes back to work at the next Friday screen
2025-02-28  BSE         SELL ₹12,863,439,859,163,296.00 at stop ₹1,651.54 (+2.5%, charges ₹28,571,611,012,501.8281) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹41,794,623,098,055,104.00 at ₹1,450.00 (fresh Friday signal — BUY: 4.67× weekly, month 1.70×, ladder rising; stop ₹1,235.90; charges ₹98,662,067,086,464.0000)
2025-03-10  CREDITACC   PYRAMID BUY ₹44,859,342,394,353,920.00 at ₹968.75 (box jump — doubling the stake with NEW capital; stop stays ₹837.38; charges ₹105,896,766,633,896.0000)
2025-03-17  NH          PYRAMID BUY ₹43,737,625,329,726,416.00 at ₹1,521.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,436.97; charges ₹103,248,796,247,304.0000)
2025-03-24  INDIASHLTR  BUY ₹52,343,318,950,649,344.00 at ₹794.95 (fresh Friday signal — BUY: 4.59× weekly, month 1.56×, ladder rising; stop ₹692.55; charges ₹123,563,742,487,184.0000)
2025-04-01  INDIASHLTR  PYRAMID BUY ₹54,509,029,337,358,272.00 at ₹829.80 (box jump — doubling the stake with NEW capital; stop stays ₹738.82; charges ₹128,676,205,469,848.0000)
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹82,018,571,248,192,768.00 / LT ₹0.00)
2025-04-07  CEMPRO      PYRAMID BUY ₹12,925,785,589,261,952.00 at ₹550.00 (box jump — doubling the stake with NEW capital; stop stays ₹524.92; charges ₹30,513,128,972,620.0000)
2025-04-07  INDIASHLTR  SELL ₹96,735,790,482,076,672.00 at stop ₹738.82 (-9.1%, charges ₹214,864,562,426,659.4375) — the cash goes back to work at the next Friday screen
2025-04-11  CEMPRO      SELL ₹24,589,001,975,983,796.00 at stop ₹524.92 (-5.3%, charges ₹54,615,826,507,945.0547) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹58,931,174,834,279,904.00 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.61× weekly, month 1.63×, ladder rising; stop ₹492.75; charges ₹139,115,299,863,880.0000)
2025-04-15  INDIASHLTR  BUY ₹58,823,282,239,406,032.00 at ₹865.00 (fresh Friday signal — BUY: 1.66× weekly, month 2.04×, ladder rising; stop ₹738.82; charges ₹138,860,604,268,024.0000)
2025-04-21  GALLANTT    BUY ₹60,684,128,336,272,688.00 at ₹474.75 (fresh Friday signal — BUY: 3.71× weekly, month 3.71×, ladder rising; stop ₹328.99; charges ₹143,253,392,355,040.0000)
2025-04-28  FORCEMOT    BUY ₹60,030,003,626,551,424.00 at ₹9,275.00 (fresh Friday signal — ACCUMULATE: 1.94× weekly, month 1.70×, ladder rising; stop ₹7,633.31; charges ₹141,709,239,274,824.0000)
2025-04-28  SMLMAH      BUY ₹59,846,983,225,726,120.00 at ₹1,680.00 (fresh Friday signal — BUY: 1.70× weekly, month 3.85×, ladder rising; stop ₹1,419.23; charges ₹141,277,193,960,712.0000)
2025-04-28  WHIRLPOOL   BUY ₹59,806,525,595,292,712.00 at ₹1,153.90 (fresh Friday signal — BUY: 2.17× weekly, month 1.78×, ladder rising; stop ₹1,017.54; charges ₹141,181,688,052,248.0000)
2025-05-05  PARAS       BUY ₹33,120,705,283,055,736.00 at ₹686.10 (fresh Friday signal — BUY: 25.11× weekly, month 4.49×, ladder rising; stop ₹486.64; charges ₹78,186,068,071,992.0000)
2025-05-12  CREDITACC   PYRAMID BUY ₹106,249,546,655,126,816.00 at ₹1,148.60 (box jump — doubling the stake with NEW capital; stop stays ₹1,019.35; charges ₹250,816,950,194,768.0000)
2025-05-12  INDIASHLTR  PYRAMID BUY ₹62,938,194,162,910,440.00 at ₹927.70 (box jump — doubling the stake with NEW capital; stop stays ₹804.65; charges ₹148,574,430,740,368.0000)
2025-05-12  NH          PYRAMID BUY ₹105,064,688,631,034,128.00 at ₹1,829.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,641.69; charges ₹248,019,926,721,520.0000)
2025-05-12  PARAS       PYRAMID BUY ₹36,119,937,926,304,920.00 at ₹750.00 (box jump — doubling the stake with NEW capital; stop stays ₹617.98; charges ₹85,266,177,194,208.0000)
2025-05-19  FORCEMOT    PYRAMID BUY ₹70,732,756,966,622,264.00 at ₹10,954.50 (box jump — doubling the stake with NEW capital; stop stays ₹8,910.52; charges ₹166,974,588,972,328.0000)
2025-05-19  GALLANTT    PYRAMID BUY ₹60,827,798,521,850,904.00 at ₹477.00 (box jump — doubling the stake with NEW capital; stop stays ₹371.68; charges ₹143,592,545,969,480.0000)
2025-05-19  WHIRLPOOL   PYRAMID BUY ₹67,788,600,279,393,568.00 at ₹1,311.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,111.50; charges ₹160,024,494,365,496.0000)
2025-06-02  CREDITACC   PYRAMID BUY ₹210,659,093,723,199,680.00 at ₹1,140.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,029.71; charges ₹497,290,323,411,456.0000)
2025-06-02  FORCEMOT    PYRAMID BUY ₹164,354,921,568,735,808.00 at ₹12,742.00 (box jump — doubling the stake with NEW capital; stop stays ₹9,650.58; charges ₹387,982,833,575,520.0000)
2025-06-02  PARAS       PYRAMID BUY ₹77,013,020,060,226,944.00 at ₹800.50 (box jump — doubling the stake with NEW capital; stop stays ₹708.99; charges ₹181,800,030,446,176.0000)
2025-06-23  FORCEMOT    PYRAMID BUY ₹365,348,897,916,256,704.00 at ₹14,179.00 (box jump — doubling the stake with NEW capital; stop stays ₹11,433.25; charges ₹862,457,292,451,456.0000)
2025-06-23  WHIRLPOOL   PYRAMID BUY ₹137,483,036,873,947,520.00 at ₹1,331.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,233.96; charges ₹324,547,982,535,552.0000)
2025-06-30  FORCEMOT    PYRAMID BUY ₹752,020,191,555,843,584.00 at ₹14,610.00 (box jump — doubling the stake with NEW capital; stop stays ₹12,858.25; charges ₹1,775,249,089,232,896.0000)
2025-06-30  NH          PYRAMID BUY ₹255,323,138,365,853,728.00 at ₹2,225.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,763.87; charges ₹602,726,062,323,328.0000)
2025-07-07  GALLANTT    PYRAMID BUY ₹140,617,665,582,281,440.00 at ₹552.00 (box jump — doubling the stake with NEW capital; stop stays ₹494.33; charges ₹331,947,713,050,832.0000)
2025-07-07  WHIRLPOOL   PYRAMID BUY ₹284,133,268,954,846,016.00 at ₹1,377.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,301.97; charges ₹670,736,414,522,720.0000)
2025-07-14  CREDITACC   PYRAMID BUY ₹480,990,902,588,818,624.00 at ₹1,303.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,193.20; charges ₹1,135,446,456,542,016.0000)
2025-07-14  FORCEMOT    PYRAMID BUY ₹1,688,480,202,996,763,904.00 at ₹16,421.00 (box jump — doubling the stake with NEW capital; stop stays ₹13,468.15; charges ₹3,985,894,230,255,104.0000)
2025-07-21  FORCEMOT    PYRAMID BUY ₹3,413,234,118,626,777,088.00 at ₹16,617.00 (box jump — doubling the stake with NEW capital; stop stays ₹15,350.10; charges ₹8,057,417,644,458,496.0000)
2025-07-21  GALLANTT    PYRAMID BUY ₹298,739,730,534,800,960.00 at ₹587.05 (box jump — doubling the stake with NEW capital; stop stays ₹544.35; charges ₹705,217,014,788,352.0000)
2025-07-21  SMLMAH      PYRAMID BUY ₹117,638,013,991,855,536.00 at ₹3,310.10 (box jump — doubling the stake with NEW capital; stop stays ₹2,822.07; charges ₹277,701,023,912,880.0000)
2025-07-28  NH          PYRAMID BUY ₹452,735,286,549,228,608.00 at ₹1,975.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,814.78; charges ₹1,068,745,113,674,816.0000)
2025-07-28  PARAS       SELL ₹135,955,396,733,442,448.00 at stop ₹708.99 (-6.6%, charges ₹301,977,134,658,205.2500) — the cash goes back to work at the next Friday screen
2025-08-04  INDIASHLTR  PYRAMID BUY ₹122,312,549,358,963,200.00 at ₹902.50 (box jump — doubling the stake with NEW capital; stop stays ₹853.86; charges ₹288,735,919,978,464.0000)
2025-08-04  NH          SELL ₹829,191,331,161,699,072.00 at stop ₹1,814.78 (-7.3%, charges ₹1,841,757,137,148,201.0000) — the cash goes back to work at the next Friday screen
2025-08-07  WHIRLPOOL   SELL ₹535,479,252,595,892,096.00 at stop ₹1,301.97 (-2.1%, charges ₹1,189,378,974,671,103.0000) — the cash goes back to work at the next Friday screen
2025-08-11  RAIN        BUY ₹1,166,653,878,422,518,528.00 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.83×, ladder rising; stop ₹143.64; charges ₹2,754,050,035,325,184.0000)
2025-08-11  SMLMAH      PYRAMID BUY ₹280,285,600,679,352,032.00 at ₹3,948.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,878.57; charges ₹661,653,454,146,880.0000)
2025-08-18  INDIASHLTR  PYRAMID BUY ₹252,052,247,938,935,776.00 at ₹931.00 (box jump — doubling the stake with NEW capital; stop stays ₹862.60; charges ₹595,004,666,918,560.0000)
2025-08-25  GALLANTT    PYRAMID BUY ₹624,170,659,823,959,808.00 at ₹614.00 (box jump — doubling the stake with NEW capital; stop stays ₹557.33; charges ₹1,473,442,346,123,648.0000)
2025-08-26  RAIN        SELL ₹1,040,948,873,561,090,432.00 at stop ₹143.64 (-10.4%, charges ₹2,312,102,099,043,355.5000) — the cash goes back to work at the next Friday screen
2025-09-08  CREDITACC   PYRAMID BUY ₹988,056,819,685,645,056.00 at ₹1,339.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,256.94; charges ₹2,332,446,640,333,440.0000)
2025-09-08  NETWEB      BUY ₹1,281,312,661,907,432,448.00 at ₹3,135.50 (fresh Friday signal — BUY: 6.14× weekly, month 4.05×, ladder rising; stop ₹2,081.16; charges ₹3,024,718,167,962,880.0000)
2025-09-22  SMLMAH      PYRAMID BUY ₹534,466,863,785,225,152.00 at ₹3,768.60 (box jump — doubling the stake with NEW capital; stop stays ₹3,255.67; charges ₹1,261,683,959,837,440.0000)
2025-09-25  INDIASHLTR  SELL ₹465,483,050,152,896,320.00 at stop ₹862.60 (-5.7%, charges ₹1,033,907,009,905,086.7500) — the cash goes back to work at the next Friday screen
2025-09-26  SMLMAH      SELL ₹920,311,037,403,556,864.00 at stop ₹3,255.67 (-6.8%, charges ₹2,044,147,542,111,398.5000) — the cash goes back to work at the next Friday screen
2025-09-29  CREDITACC   PYRAMID BUY ₹2,026,959,415,775,652,096.00 at ₹1,376.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,274.42; charges ₹4,784,921,864,030,464.0000)
2025-09-29  GALLANTT    PYRAMID BUY ₹1,328,097,054,976,179,968.00 at ₹654.00 (box jump — doubling the stake with NEW capital; stop stays ₹616.41; charges ₹3,135,159,286,589,952.0000)
2025-09-29  NETWEB      PYRAMID BUY ₹1,508,424,618,668,804,864.00 at ₹3,700.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,674.79; charges ₹3,560,847,781,132,288.0000)
2025-09-29  SUBROS      BUY ₹1,479,402,401,278,626,048.00 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹3,492,336,768,305,920.0000)
2025-10-06  AVANTIFEED  PYRAMID BUY ₹46,933,025,520,750,208.00 at ₹653.00 (box jump — doubling the stake with NEW capital; stop stays ₹497.91; charges ₹110,791,986,367,128.0000)
2025-10-06  SUBROS      PYRAMID BUY ₹1,401,853,799,789,307,648.00 at ₹1,075.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,046.90; charges ₹3,309,272,422,812,160.0000)
2025-10-09  FORCEMOT    SELL ₹6,284,607,957,040,572,416.00 at stop ₹15,350.10 (-3.1%, charges ₹13,959,047,959,222,674.0000) — the cash goes back to work at the next Friday screen
2025-10-13  AVANTIFEED  PYRAMID BUY ₹94,394,173,148,234,896.00 at ₹657.45 (box jump — doubling the stake with NEW capital; stop stays ₹511.29; charges ₹222,830,679,005,584.0000)
2025-10-13  SHAILY      BUY ₹1,918,612,211,650,510,080.00 at ₹2,434.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 1.99×, ladder rising; stop ₹1,942.00; charges ₹4,529,153,099,303,168.0000)
2025-10-13  VIYASH      BUY ₹1,917,184,175,612,653,568.00 at ₹216.04 (fresh Friday signal — BUY: 3.38× weekly, month 2.33×, ladder rising; stop ₹174.14; charges ₹4,525,782,020,036,864.0000)
2025-10-14  SUBROS      SELL ₹2,720,646,965,137,247,232.00 at stop ₹1,046.90 (-5.1%, charges ₹6,042,961,108,483,872.0000) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹1,862,411,278,666,760,960.00 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.36×, ladder rising; stop ₹1,311.00; charges ₹4,396,482,918,085,120.0000)
2025-10-20  AVANTIFEED  PYRAMID BUY ₹197,241,623,074,195,968.00 at ₹687.70 (box jump — doubling the stake with NEW capital; stop stays ₹600.07; charges ₹465,616,502,925,088.0000)
2025-10-20  CIEINDIA    BUY ₹1,865,116,507,752,323,584.00 at ₹432.50 (fresh Friday signal — ACCUMULATE: 5.23× weekly, month 2.05×, ladder rising; stop ₹377.39; charges ₹4,402,868,990,592,512.0000)
2025-10-20  CREDITACC   SELL ₹3,741,904,689,156,163,584.00 at stop ₹1,274.42 (-3.5%, charges ₹8,311,326,238,935,018.0000) — the cash goes back to work at the next Friday screen
2025-10-20  GALLANTT    SELL ₹2,495,027,085,143,118,848.00 at stop ₹616.41 (-0.3%, charges ₹5,541,825,835,302,061.0000) — the cash goes back to work at the next Friday screen
2025-10-27  ANANDRATHI  PYRAMID BUY ₹1,849,105,293,234,924,032.00 at ₹1,566.95 (box jump — doubling the stake with NEW capital; stop stays ₹1,450.17; charges ₹4,365,072,274,083,072.0000)
2025-10-27  VIYASH      PYRAMID BUY ₹1,796,680,681,335,334,400.00 at ₹202.94 (box jump — doubling the stake with NEW capital; stop stays ₹185.91; charges ₹4,241,316,628,193,280.0000)
2025-11-03  MAHABANK    BUY ₹2,561,926,830,313,728,000.00 at ₹59.70 (fresh Friday signal — ACCUMULATE: 2.08× weekly, month 1.71×, ladder rising; stop ₹53.69; charges ₹6,047,787,444,092,928.0000)
2025-11-03  NETWEB      PYRAMID BUY ₹3,141,963,947,813,213,696.00 at ₹3,858.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,515.95; charges ₹7,417,046,376,398,848.0000)
2025-11-03  TDPOWERSYS  BUY ₹2,545,323,255,628,815,872.00 at ₹382.27 (fresh Friday signal — BUY: 4.87× weekly, month 1.96×, ladder rising; stop ₹276.78; charges ₹6,008,592,378,364,416.0000)
2025-11-06  NETWEB      SELL ₹5,707,358,960,704,397,312.00 at stop ₹3,515.95 (-3.3%, charges ₹12,676,892,178,090,344.0000) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹2,524,192,365,197,952,512.00 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹5,958,709,949,124,608.0000)
2025-11-10  CUB         BUY ₹2,536,883,656,705,608,704.00 at ₹190.65 (fresh Friday signal — BUY: 6.02× weekly, month 1.75×, ladder rising; stop ₹160.31; charges ₹5,988,669,521,943,552.0000)
2025-11-10  LTF         BUY ₹2,535,976,144,023,270,912.00 at ₹304.00 (fresh Friday signal — BUY: 2.98× weekly, month 1.55×, ladder rising; stop ₹250.80; charges ₹5,986,527,211,031,040.0000)
2025-11-17  CCL         PYRAMID BUY ₹2,643,785,554,899,621,888.00 at ₹1,065.50 (box jump — doubling the stake with NEW capital; stop stays ₹976.41; charges ₹6,241,026,439,399,936.0000)
2025-11-17  CUB         PYRAMID BUY ₹2,708,117,374,169,775,104.00 at ₹204.00 (box jump — doubling the stake with NEW capital; stop stays ₹174.66; charges ₹6,392,890,717,580,800.0000)
2025-11-17  TDPOWERSYS  PYRAMID BUY ₹2,620,686,985,858,045,440.00 at ₹394.52 (box jump — doubling the stake with NEW capital; stop stays ₹357.49; charges ₹6,186,499,028,947,456.0000)
2025-11-20  ANANDRATHI  SELL ₹3,410,978,195,063,329,792.00 at stop ₹1,450.17 (-7.7%, charges ₹7,576,289,330,730,711.0000) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹4,829,014,544,963,416,064.00 at stop ₹976.41 (-6.1%, charges ₹10,725,958,737,555,190.0000) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹3,251,205,881,329,994,752.00 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.37×, ladder rising; stop ₹2,956.50; charges ₹7,674,927,275,288,576.0000)
2025-11-24  TDPOWERSYS  SELL ₹4,733,234,756,828,918,784.00 at stop ₹357.49 (-8.0%, charges ₹10,513,217,598,373,098.0000) — the cash goes back to work at the next Friday screen
2025-12-01  CUB         PYRAMID BUY ₹5,417,797,507,412,590,592.00 at ₹204.30 (box jump — doubling the stake with NEW capital; stop stays ₹185.32; charges ₹12,789,470,547,040,256.0000)
2025-12-01  EUREKAFORB  BUY ₹4,013,336,500,348,971,008.00 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.35×, ladder rising; stop ₹535.37; charges ₹9,474,043,445,947,392.0000)
2025-12-01  GMRAIRPORT  BUY ₹2,384,968,753,741,551,616.00 at ₹108.90 (fresh Friday signal — BUY: 1.69× weekly, month 1.84×, ladder rising; stop ₹89.73; charges ₹5,630,053,096,272,896.0000)
2025-12-01  SANSERA     BUY ₹4,005,635,593,065,021,440.00 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.61×, ladder rising; stop ₹1,413.60; charges ₹9,455,864,374,699,520.0000)
2025-12-01  SHAILY      PYRAMID BUY ₹2,070,418,190,860,155,136.00 at ₹2,632.80 (box jump — doubling the stake with NEW capital; stop stays ₹2,340.80; charges ₹4,887,512,395,181,312.0000)
2025-12-08  AVANTIFEED  PYRAMID BUY ₹470,363,200,607,017,664.00 at ₹820.95 (box jump — doubling the stake with NEW capital; stop stays ₹748.60; charges ₹1,110,358,276,097,280.0000)
2025-12-15  EUREKAFORB  PYRAMID BUY ₹3,925,473,583,499,801,600.00 at ₹651.00 (box jump — doubling the stake with NEW capital; stop stays ₹589.10; charges ₹9,266,630,713,064,448.0000)
2025-12-15  LTF         PYRAMID BUY ₹2,555,372,736,323,020,288.00 at ₹307.05 (box jump — doubling the stake with NEW capital; stop stays ₹281.77; charges ₹6,032,315,586,397,696.0000)
2025-12-15  SANSERA     PYRAMID BUY ₹3,894,310,949,598,193,152.00 at ₹1,705.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,517.72; charges ₹9,193,066,946,993,664.0000)
2025-12-15  SHAILY      SELL ₹3,669,087,237,313,192,448.00 at stop ₹2,340.80 (-7.6%, charges ₹8,149,587,860,106,520.0000) — the cash goes back to work at the next Friday screen
2025-12-22  GMRAIRPORT  PYRAMID BUY ₹2,229,674,145,095,047,680.00 at ₹102.05 (box jump — doubling the stake with NEW capital; stop stays ₹92.10; charges ₹5,263,458,401,531,904.0000)
2025-12-22  KIRLOSENG   BUY ₹3,669,087,237,313,192,448.00 at ₹1,258.30 (fresh Friday signal — BUY: 4.09× weekly, month 1.72×, ladder rising; stop ₹1,014.88; charges ₹8,661,394,799,627,264.0000)
2026-01-05  KIRLOSENG   PYRAMID BUY ₹3,665,371,184,588,009,472.00 at ₹1,260.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,140.95; charges ₹8,652,622,536,209,408.0000)
2026-01-05  VIYASH      PYRAMID BUY ₹3,722,823,345,284,030,464.00 at ₹210.50 (box jump — doubling the stake with NEW capital; stop stays ₹195.04; charges ₹8,788,246,415,854,080.0000)
2026-01-08  EUREKAFORB  SELL ₹7,080,331,908,692,801,536.00 at stop ₹589.10 (-10.4%, charges ₹15,726,469,074,325,328.0000) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹2,908,812,263,313,802,752.00 at stop ₹2,956.50 (-10.1%, charges ₹6,460,904,190,926,336.0000) — the cash goes back to work at the next Friday screen
2026-01-12  KIRLOSENG   SELL ₹6,615,574,315,816,309,760.00 at stop ₹1,140.95 (-9.4%, charges ₹14,694,173,412,810,296.0000) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹5,684,453,007,162,330,112.00 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.57×, ladder rising; stop ₹246.34; charges ₹13,418,948,237,114,368.0000)
2026-01-12  VIYASH      SELL ₹6,875,393,200,303,305,728.00 at stop ₹195.04 (-7.1%, charges ₹15,271,269,755,821,258.0000) — the cash goes back to work at the next Friday screen
2026-01-19  CUB         PYRAMID BUY ₹10,713,544,475,090,309,120.00 at ₹202.24 (box jump — doubling the stake with NEW capital; stop stays ₹185.96; charges ₹25,290,823,684,550,656.0000)
2026-01-19  MAHABANK    PYRAMID BUY ₹2,860,700,798,066,146,816.00 at ₹66.82 (box jump — doubling the stake with NEW capital; stop stays ₹58.71; charges ₹6,753,085,280,633,344.0000)
2026-01-19  NATIONALUM  PYRAMID BUY ₹5,848,253,873,266,628,608.00 at ₹363.00 (box jump — doubling the stake with NEW capital; stop stays ₹312.41; charges ₹13,805,623,145,092,096.0000)
2026-01-19  SANSERA     PYRAMID BUY ₹8,422,771,627,174,415,360.00 at ₹1,846.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,672.76; charges ₹19,883,133,229,472,768.0000)
2026-01-21  AVANTIFEED  SELL ₹854,909,171,054,466,688.00 at stop ₹748.60 (-1.0%, charges ₹1,898,880,280,377,616.5000) — the cash goes back to work at the next Friday screen
2026-01-21  LTF         SELL ₹4,674,050,827,090,887,680.00 at stop ₹281.77 (-7.8%, charges ₹10,381,761,297,633,940.0000) — the cash goes back to work at the next Friday screen
2026-01-23  GMRAIRPORT  SELL ₹4,010,897,306,121,581,568.00 at stop ₹92.10 (-12.7%, charges ₹8,908,798,804,696,346.0000) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹15,212,846,640,311,463,936.00 at stop ₹1,672.76 (-6.4%, charges ₹33,789,992,518,229,620.0000) — the cash goes back to work at the next Friday screen
2026-01-27  HINDZINC    BUY ₹8,480,907,082,093,139,968.00 at ₹733.00 (fresh Friday signal — BUY: 3.59× weekly, month 3.42×, ladder rising; stop ₹602.35; charges ₹20,020,370,120,922,112.0000)
2026-02-02  CIEINDIA    PYRAMID BUY ₹1,771,657,517,785,158,144.00 at ₹411.80 (box jump — doubling the stake with NEW capital; stop stays ₹382.33; charges ₹4,182,245,942,590,720.0000)
2026-02-02  HINDCOPPER  BUY ₹10,163,835,026,984,718,336.00 at ₹590.15 (fresh Friday signal — BUY: 2.81× weekly, month 4.41×, ladder rising; stop ₹485.74; charges ₹23,993,157,467,539,456.0000)
2026-02-02  HINDZINC    SELL ₹6,937,408,326,440,341,504.00 at stop ₹602.35 (-17.8%, charges ₹15,409,014,564,385,542.0000) — the cash goes back to work at the next Friday screen
2026-02-02  MAHABANK    PYRAMID BUY ₹5,172,432,534,215,929,856.00 at ₹60.48 (box jump — doubling the stake with NEW capital; stop stays ₹59.76; charges ₹12,210,252,129,651,712.0000)
2026-02-02  NATIONALUM  PYRAMID BUY ₹11,170,980,460,132,319,232.00 at ₹347.10 (box jump — doubling the stake with NEW capital; stop stays ₹335.49; charges ₹26,370,665,456,017,408.0000)
2026-02-16  HINDCOPPER  PYRAMID BUY ₹10,051,355,576,832,245,760.00 at ₹585.00 (box jump — doubling the stake with NEW capital; stop stays ₹520.46; charges ₹23,727,633,956,757,504.0000)
2026-02-17  NATIONALUM  SELL ₹21,521,363,439,524,904,960.00 at stop ₹335.49 (-4.8%, charges ₹47,802,145,567,988,088.0000) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹14,585,528,553,325,768,704.00 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.69×, ladder rising; stop ₹5,440.18; charges ₹34,431,184,921,649,152.0000)
2026-02-23  CUB         PYRAMID BUY ₹22,358,192,220,411,432,960.00 at ₹211.28 (box jump — doubling the stake with NEW capital; stop stays ₹188.57; charges ₹52,779,647,171,526,656.0000)
2026-02-23  MAHABANK    PYRAMID BUY ₹11,849,750,959,965,628,416.00 at ₹69.36 (box jump — doubling the stake with NEW capital; stop stays ₹61.05; charges ₹27,972,998,378,932,224.0000)
2026-03-02  ABB         PYRAMID BUY ₹13,953,761,680,045,987,840.00 at ₹5,840.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,486.25; charges ₹32,939,810,648,735,744.0000)
2026-03-02  HINDCOPPER  PYRAMID BUY ₹19,341,037,971,547,533,312.00 at ₹563.50 (box jump — doubling the stake with NEW capital; stop stays ₹528.63; charges ₹45,657,231,586,791,424.0000)
2026-03-02  KSB         BUY ₹17,838,104,961,625,186,304.00 at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.80×, ladder rising; stop ₹658.54; charges ₹42,109,347,517,984,768.0000)
2026-03-02  TORNTPOWER  BUY ₹17,840,404,756,976,109,568.00 at ₹1,491.00 (fresh Friday signal — BUY: 1.57× weekly, month 1.71×, ladder rising; stop ₹1,315.84; charges ₹42,114,776,507,322,368.0000)
2026-03-09  CUB         SELL ₹39,775,413,191,147,397,120.00 at stop ₹188.57 (-8.6%, charges ₹88,347,102,019,484,064.0000) — the cash goes back to work at the next Friday screen
2026-03-09  KSB         PYRAMID BUY ₹17,820,109,429,302,470,656.00 at ₹739.00 (box jump — doubling the stake with NEW capital; stop stays ₹681.58; charges ₹42,066,866,541,111,296.0000)
2026-03-12  HINDCOPPER  SELL ₹36,165,226,270,780,829,696.00 at stop ₹528.63 (-8.2%, charges ₹80,328,340,513,971,440.0000) — the cash goes back to work at the next Friday screen
2026-03-23  ABB         PYRAMID BUY ₹29,898,354,683,854,872,576.00 at ₹6,264.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,854.38; charges ₹70,579,257,735,442,432.0000)
2026-03-30  AETHER      BUY ₹25,171,218,882,306,834,432.00 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹59,420,190,970,204,160.0000)
2026-03-30  KSB         PYRAMID BUY ₹38,336,656,648,016,232,448.00 at ₹795.85 (box jump — doubling the stake with NEW capital; stop stays ₹719.20; charges ₹90,499,052,502,597,632.0000)
2026-03-30  MAHABANK    SELL ₹20,789,274,346,290,065,408.00 at stop ₹61.05 (-7.0%, charges ₹46,176,066,927,483,480.0000) — the cash goes back to work at the next Friday screen
2026-03-30  TORNTPOWER  SELL ₹15,672,567,763,691,372,544.00 at stop ₹1,315.84 (-11.7%, charges ₹34,811,101,432,738,544.0000) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹20,012,987,126,820,765,696.00 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹26,051,736,931,114,946,560.00 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.66×, ladder rising; stop ₹891.29; charges ₹61,498,777,265,827,840.0000)
2026-04-06  CIEINDIA    PYRAMID BUY ₹3,944,783,755,315,993,088.00 at ₹459.00 (box jump — doubling the stake with NEW capital; stop stays ₹409.40; charges ₹9,312,215,080,764,416.0000)
2026-04-13  AETHER      PYRAMID BUY ₹25,537,422,397,969,457,152.00 at ₹1,170.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,010.28; charges ₹60,284,665,707,655,168.0000)
2026-04-13  INOXINDIA   BUY ₹30,058,551,126,687,596,544.00 at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹70,957,423,896,977,408.0000)
2026-04-13  THERMAX     BUY ₹30,311,143,190,591,782,912.00 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹71,553,702,875,160,576.0000)
2026-05-04  KSB         PYRAMID BUY ₹93,437,095,722,143,006,720.00 at ₹971.00 (box jump — doubling the stake with NEW capital; stop stays ₹917.42; charges ₹220,571,363,566,895,104.0000)
2026-05-04  KSB         SELL ₹175,963,190,645,669,068,800.00 at stop ₹917.42 (+5.6%, charges ₹390,840,388,783,360,384.0000) — the cash goes back to work at the next Friday screen
2026-05-11  AETHER      PYRAMID BUY ₹52,906,895,095,745,822,720.00 at ₹1,213.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,125.84; charges ₹124,894,142,986,436,608.0000)
2026-05-11  CIEINDIA    PYRAMID BUY ₹8,199,585,902,299,048,960.00 at ₹477.60 (box jump — doubling the stake with NEW capital; stop stays ₹429.88; charges ₹19,356,272,037,095,424.0000)
2026-05-11  CRAFTSMAN   BUY ₹53,195,932,185,547,243,520.00 at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹125,576,455,557,545,984.0000)
2026-05-11  INOXINDIA   PYRAMID BUY ₹34,433,448,946,542,043,136.00 at ₹1,491.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,372.18; charges ₹81,284,983,525,548,032.0000)
2026-05-11  SPARC       BUY ₹53,072,131,018,321,641,472.00 at ₹172.05 (fresh Friday signal — BUY: 5.97× weekly, month 2.00×, ladder rising; stop ₹129.88; charges ₹125,284,205,546,397,696.0000)
2026-05-11  THERMAX     PYRAMID BUY ₹39,582,243,525,773,680,640.00 at ₹4,707.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,726.38; charges ₹93,439,434,948,616,192.0000)
2026-05-11  WOCKPHARMA  BUY ₹53,046,288,107,523,399,680.00 at ₹1,613.90 (fresh Friday signal — BUY: 16.73× weekly, month 2.98×, ladder rising; stop ₹1,312.90; charges ₹125,223,199,732,498,432.0000)
2026-05-13  INOXINDIA   SELL ₹63,134,049,123,792,445,440.00 at stop ₹1,372.18 (-1.7%, charges ₹140,230,102,753,130,192.0000) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹97,844,965,126,418,071,552.00 at stop ₹1,125.84 (-5.1%, charges ₹217,328,204,098,717,888.0000) — the cash goes back to work at the next Friday screen
2026-05-18  ABB         PYRAMID BUY ₹60,164,731,959,440,908,288.00 at ₹6,310.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,862.93; charges ₹142,027,284,392,419,328.0000)
2026-05-18  ALKYLAMINE  BUY ₹71,831,969,682,632,630,272.00 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.24×, ladder rising; stop ₹1,502.04; charges ₹169,569,434,689,085,440.0000)
2026-05-18  CAPLIPOINT  BUY ₹71,819,203,522,803,941,376.00 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹169,539,298,379,096,064.0000)
2026-05-18  CHENNPETRO  PYRAMID BUY ₹26,147,914,017,269,841,920.00 at ₹995.00 (box jump — doubling the stake with NEW capital; stop stays ₹953.23; charges ₹61,725,816,760,934,400.0000)
2026-05-18  NLCINDIA    BUY ₹36,884,865,830,761,873,408.00 at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 4.61×, ladder rising; stop ₹278.49; charges ₹87,071,896,749,301,760.0000)
2026-05-18  SPARC       PYRAMID BUY ₹50,023,306,884,141,907,968.00 at ₹162.55 (box jump — doubling the stake with NEW capital; stop stays ₹153.91; charges ₹118,087,028,757,520,384.0000)
2026-05-18  THERMAX     PYRAMID BUY ₹74,898,275,081,893,330,944.00 at ₹4,458.60 (box jump — doubling the stake with NEW capital; stop stays ₹4,181.80; charges ₹176,807,878,454,919,168.0000)
2026-05-25  CAPLIPOINT  PYRAMID BUY ₹74,148,397,657,695,535,104.00 at ₹2,059.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,851.17; charges ₹175,037,687,668,424,704.0000)
2026-05-25  CRAFTSMAN   PYRAMID BUY ₹51,957,812,734,156,627,968.00 at ₹8,850.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,793.85; charges ₹122,653,701,018,345,472.0000)
2026-05-25  NLCINDIA    PYRAMID BUY ₹36,436,672,076,318,519,296.00 at ₹348.10 (box jump — doubling the stake with NEW capital; stop stays ₹320.62; charges ₹86,013,872,558,845,952.0000)
2026-05-25  WOCKPHARMA  PYRAMID BUY ₹52,189,830,167,445,315,584.00 at ₹1,591.60 (box jump — doubling the stake with NEW capital; stop stays ₹1,423.10; charges ₹123,201,410,696,560,640.0000)
2026-06-08  ABB         PYRAMID BUY ₹135,339,434,390,866,018,304.00 at ₹7,105.50 (box jump — doubling the stake with NEW capital; stop stays ₹6,609.15; charges ₹319,487,708,358,754,304.0000)
2026-06-08  SPARC       PYRAMID BUY ₹128,483,925,490,993,512,448.00 at ₹209.00 (box jump — doubling the stake with NEW capital; stop stays ₹177.70; charges ₹303,304,318,514,462,720.0000)
2026-06-09  NLCINDIA    SELL ₹66,892,713,601,272,487,936.00 at stop ₹320.62 (-8.3%, charges ₹148,578,654,971,887,456.0000) — the cash goes back to work at the next Friday screen
2026-06-11  CIEINDIA    SELL ₹14,710,531,547,083,229,184.00 at stop ₹429.88 (-6.4%, charges ₹32,674,276,068,620,532.0000) — the cash goes back to work at the next Friday screen
2026-06-15  ALKYLAMINE  PYRAMID BUY ₹78,786,732,436,335,591,424.00 at ₹1,880.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,614.05; charges ₹185,987,127,169,925,120.0000)
2026-06-15  CAPLIPOINT  PYRAMID BUY ₹175,136,689,005,134,282,752.00 at ₹2,435.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,852.50; charges ₹413,434,707,124,551,680.0000)
2026-06-15  CHENNPETRO  PYRAMID BUY ₹60,791,045,596,168,634,368.00 at ₹1,158.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,075.02; charges ₹143,505,785,535,946,752.0000)
2026-06-22  THERMAX     PYRAMID BUY ₹158,126,583,854,130,790,400.00 at ₹4,712.10 (box jump — doubling the stake with NEW capital; stop stays ₹4,306.63; charges ₹373,279,969,238,319,104.0000)
2026-06-22  WOCKPHARMA  PYRAMID BUY ₹131,925,426,158,159,626,240.00 at ₹2,014.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,639.31; charges ₹311,428,463,309,488,128.0000)
2026-06-29  CAPLIPOINT  PYRAMID BUY ₹360,118,655,814,786,744,320.00 at ₹2,506.40 (box jump — doubling the stake with NEW capital; stop stays ₹2,209.13; charges ₹850,110,572,733,923,328.0000)
2026-07-06  CAPLIPOINT  PYRAMID BUY ₹733,336,407,610,064,633,856.00 at ₹2,555.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,351.25; charges ₹1,731,143,397,915,623,424.0000)
2026-07-20  CAPLIPOINT  PYRAMID BUY ₹1,498,770,070,506,170,744,832.00 at ₹2,614.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,376.52; charges ₹3,538,056,866,705,965,056.0000)
2026-07-27  CHENNPETRO  PYRAMID BUY ₹128,989,171,027,949,584,384.00 at ₹1,230.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,130.59; charges ₹304,497,021,435,723,776.0000)
2026-07-27  CRAFTSMAN   PYRAMID BUY ₹109,211,316,734,129,963,008.00 at ₹9,312.00 (box jump — doubling the stake with NEW capital; stop stays ₹8,593.23; charges ₹257,808,623,682,142,208.0000)
2026-07-29  THERMAX     SELL ₹288,059,011,369,741,123,584.00 at stop ₹4,306.63 (-4.5%, charges ₹639,821,860,374,245,632.0000) — the cash goes back to work at the next Friday screen
2026-08-03  ALKYLAMINE  PYRAMID BUY ₹149,509,732,183,878,041,600.00 at ₹1,785.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,676.66; charges ₹352,938,682,858,733,568.0000)
2026-08-03  TMB         BUY ₹369,662,256,518,096,879,616.00 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.57×, ladder rising; stop ₹748.60; charges ₹872,639,580,128,608,256.0000)
2026-08-03  WOCKPHARMA  PYRAMID BUY ₹257,389,298,271,534,383,104.00 at ₹1,967.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,734.41; charges ₹607,603,522,439,348,224.0000)
2026-08-10  SPARC       PYRAMID BUY ₹261,883,801,798,973,816,832.00 at ₹213.25 (box jump — doubling the stake with NEW capital; stop stays ₹179.80; charges ₹618,213,428,108,427,264.0000)
2026-08-10  TMB         PYRAMID BUY ₹375,228,191,589,099,372,544.00 at ₹880.00 (box jump — doubling the stake with NEW capital; stop stays ₹796.29; charges ₹885,778,750,162,206,720.0000)
2026-08-17  ABB         PYRAMID BUY ₹291,172,354,326,083,895,296.00 at ₹7,652.50 (box jump — doubling the stake with NEW capital; stop stays ₹7,158.25; charges ₹687,353,162,363,600,896.0000)
2026-08-17  CRAFTSMAN   PYRAMID BUY ₹240,164,048,483,866,738,688.00 at ₹10,251.00 (box jump — doubling the stake with NEW capital; stop stays ₹9,690.00; charges ₹566,940,905,476,751,360.0000)
2026-08-24  CHENNPETRO  PYRAMID BUY ₹294,334,757,945,870,843,904.00 at ₹1,405.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,242.60; charges ₹694,818,459,451,162,624.0000)
2026-08-24  SPARC       PYRAMID BUY ₹487,577,684,859,345,960,960.00 at ₹198.75 (box jump — doubling the stake with NEW capital; stop stays ₹182.29; charges ₹1,150,995,479,504,486,400.0000)
2026-08-31  ALKYLAMINE  PYRAMID BUY ₹341,997,337,491,245,301,760.00 at ₹2,045.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,920.99; charges ₹807,332,660,370,931,712.0000)
2026-08-31  CRAFTSMAN   PYRAMID BUY ₹520,337,970,256,576,839,680.00 at ₹11,118.00 (box jump — doubling the stake with NEW capital; stop stays ₹9,832.50; charges ₹1,228,330,725,908,021,248.0000)
2026-09-07  WOCKPHARMA  PYRAMID BUY ₹552,204,485,386,924,064,768.00 at ₹2,112.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,741.63; charges ₹1,303,556,102,297,419,776.0000)
2026-09-10  ALKYLAMINE  SELL ₹640,336,179,204,409,393,152.00 at stop ₹1,920.99 (+0.2%, charges ₹1,422,281,786,969,078,528.0000) — the cash goes back to work at the next Friday screen
```
