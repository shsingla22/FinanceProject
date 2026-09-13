# The Darvas screen — 2020-03-01 → 2025-03-28

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2019-06-01 → 2025-03-28, 741 symbols, in `2019-06-01_to_2026-09-13/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **Two limits that cannot be engineered away:** the universe is TODAY'S NiftyTotalMarket constituents (survivorship bias flatters the early years), and Yahoo serves split-adjusted history. No slippage, stop exits at the stop price, fractional shares. The earliest screens run on ~9 months of history instead of a full year — every gate's own minimum (6 completed weeks, 120 baseline days) is still enforced, screens simply judge a shorter norm at first.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), best volume reaction first, at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with NEW capital.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled with FRESH MONEY from outside the portfolio, equal to the position's market value, at the next day's open. The new money never touches the portfolio's cash — fresh entries are never starved — and every injection is dated and logged, so the honest yardstick is the money-weighted return (XIRR), not a naive multiple. Each add-on is its own tax lot on its own holding clock; the ratcheted stop covers the whole enlarged position.

## The headline — XIRR is the honest yardstick

| Engine | Money put in | Final value | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | ₹7,677.63 crore crore (₹100 + ₹7,677.63 crore crore injected) | **₹6,796.17 crore crore** | **-39.29%** |
| B: doubling, before charges and tax | ₹7,972.45 crore crore | ₹7,105.85 crore crore | -37.59% |
| **A: no doubling, NET of charges and tax** | ₹100.00 | **₹592.33** | **+42.13%** |
| A: no doubling, before charges and tax | ₹100.00 | ₹764.58 | +49.49% |
| Nifty 50 (pre-cost, pre-tax) | ₹100.00 | ₹214.02 | +16.23% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹18.09; unrealised gains in both end books carry further deferred liabilities.*

5.06 years, 265 weekly screens. Engine B injected new capital 389 times (gross run: 390); the complete dated injection list is in the blotter and the events CSV.

## Reality check — what doubling on EVERY jump actually demands

Doubling with new capital on every box jump is EXPONENTIAL twice over:
within a position (each jump doubles it) and across the portfolio (a
doubled position that stops out turns giant proceeds into internal
cash, funding giant new entries that each double again). Per ₹100
started, the fresh capital the rule demanded crossed:

| Cumulative new capital demanded | Reached by |
|---|---|
| ₹1,000 (10× the start) | 2020-08-24 |
| ₹1 lakh (1,000×) | 2021-03-08 |
| ₹1 crore (10⁵×) | 2021-09-13 |
| ₹100 crore (10⁷×) | 2022-06-13 |
| ₹1 lakh crore (10¹⁰×) | 2023-04-24 |
| 10¹⁵ ₹ — the scale of India's entire market cap per ₹100 started | 2024-02-19 |

No investor has this money and no market absorbs it — beyond the first
year or two the simulation is arithmetic (zero market impact assumed),
not an implementable strategy. **On this window the doubling engine LOST money — XIRR −39.29% net — while the same skill without doubling made +42.13%.** The cascade concentrated its biggest injections just before the late-2024 correction, and the window closes before any recovery: doubling's fate depends entirely on where the music stops, while engine A stays solidly positive on both windows.

## What the frictions took (net runs)

| | Engine A: no doubling | Engine B: doubling |
|---|---:|---:|
| Transaction charges | ₹14.75 | ₹48.48 crore crore |
| Capital-gains tax paid | ₹97.98 | ₹0.00 |
| Tax accrued, final part-year | ₹18.09 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹4.09 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹9,480.17 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹3.05 crore / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹5,621.45 crore / ₹0.00 |
| FY2024 | 2024-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹1.09 crore crore / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹1,066.50 crore crore / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹4.09 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹53.36 | ₹0.00 | ₹10.67 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹89.71 | ₹0.00 | ₹17.94 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹86.17 | ₹4.11 | ₹17.75 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹258.09 | ₹0.00 | ₹51.62 | ₹0.00 / ₹0.00 |
| Final part-year (accrued) | — | ₹66.91 | ₹37.66 | ₹18.09 | ₹0.00 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2020 (2020-12-24) | ₹157.81 | +57.8% | ₹15,475.40 | ₹12,846.23 | +128.8% | +25.1% |
| 2021 (2021-12-31) | ₹263.61 | +67.0% | ₹16.56 crore | ₹15.57 crore | +50.9% | +26.2% |
| 2022 (2022-12-30) | ₹324.81 | +23.2% | ₹13,347.63 crore | ₹12,377.52 crore | +55.4% | +4.3% |
| 2023 (2023-12-29) | ₹584.76 | +80.0% | ₹3.08 crore crore | ₹2.93 crore crore | +40.0% | +20.0% |
| 2024 (2024-12-27) | ₹679.56 | +16.2% | ₹3,024.61 crore crore | ₹3,109.90 crore crore | -22.7% | +9.6% |
| 2025 (2025-03-28) | ₹592.33 | -12.8% | ₹6,796.17 crore crore | ₹4,564.80 crore crore | -13.1% | -1.2% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-8.6%** (A: -25.5%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **154 closed trades**: 23 winners (15%), average winner +3.9%, average loser -8.4% (returns per blended entry price).
- Best closed trade GNFC +13.4%; worst DEEPAKNTR -30.0%.
- Median holding period 74 days.
- Cash share of equity averaged 18%; fully in cash 5 of 265 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

| Month-end screen | B equity | B injected so far | B cash | B positions | A equity |
|---|---:|---:|---:|---:|---:|
| 2020-03-27 | ₹95.87 | ₹0.00 | ₹95.87 | 0 | ₹95.87 |
| 2020-04-30 | ₹96.58 | ₹0.00 | ₹76.69 | 2 | ₹96.58 |
| 2020-05-29 | ₹108.27 | ₹10.53 | ₹12.70 | 8 | ₹98.27 |
| 2020-06-26 | ₹299.76 | ₹161.73 | ₹1.69 | 9 | ₹117.79 |
| 2020-07-31 | ₹605.84 | ₹466.71 | ₹51.04 | 8 | ₹122.06 |
| 2020-08-28 | ₹1,240.76 | ₹1,070.52 | ₹9.12 | 9 | ₹134.65 |
| 2020-09-25 | ₹1,935.12 | ₹1,816.84 | ₹277.19 | 9 | ₹135.85 |
| 2020-10-30 | ₹4,363.10 | ₹4,144.23 | ₹183.63 | 10 | ₹140.14 |
| 2020-11-27 | ₹6,268.29 | ₹5,943.37 | ₹0.00 | 11 | ₹140.58 |
| 2020-12-24 | ₹15,475.40 | ₹12,846.23 | ₹3,562.46 | 8 | ₹157.81 |
| 2021-01-29 | ₹44,081.52 | ₹42,877.23 | ₹16,106.07 | 8 | ₹160.82 |
| 2021-02-26 | ₹96,364.52 | ₹95,430.94 | ₹31,033.40 | 8 | ₹167.29 |
| 2021-03-26 | ₹1.43 lakh | ₹1.54 lakh | ₹45,575.79 | 8 | ₹160.16 |
| 2021-04-30 | ₹2.95 lakh | ₹2.87 lakh | ₹15,897.43 | 9 | ₹161.64 |
| 2021-05-28 | ₹4.92 lakh | ₹4.34 lakh | ₹10,412.07 | 9 | ₹180.25 |
| 2021-06-25 | ₹12.54 lakh | ₹10.92 lakh | ₹30,196.80 | 8 | ₹196.77 |
| 2021-07-30 | ₹40.03 lakh | ₹28.50 lakh | ₹30,196.80 | 8 | ₹238.52 |
| 2021-08-27 | ₹85.71 lakh | ₹79.59 lakh | ₹42.16 lakh | 6 | ₹228.06 |
| 2021-09-24 | ₹1.83 crore | ₹1.69 crore | ₹0.00 | 10 | ₹243.39 |
| 2021-10-29 | ₹4.10 crore | ₹4.15 crore | ₹1.39 crore | 7 | ₹245.71 |
| 2021-11-26 | ₹7.36 crore | ₹7.55 crore | ₹3.25 crore | 6 | ₹251.50 |
| 2021-12-31 | ₹16.56 crore | ₹15.58 crore | ₹0.00 | 10 | ₹263.61 |
| 2022-01-28 | ₹22.86 crore | ₹24.33 crore | ₹14.49 crore | 5 | ₹243.69 |
| 2022-02-25 | ₹29.63 crore | ₹32.97 crore | ₹16.28 crore | 4 | ₹228.61 |
| 2022-03-25 | ₹36.46 crore | ₹35.65 crore | ₹16.28 crore | 4 | ₹251.83 |
| 2022-04-29 | ₹79.04 crore | ₹69.25 crore | ₹0.00 | 8 | ₹268.88 |
| 2022-05-27 | ₹90.45 crore | ₹81.59 crore | ₹13.87 crore | 6 | ₹255.92 |
| 2022-06-24 | ₹136.07 crore | ₹131.94 crore | ₹1.72 crore | 7 | ₹252.38 |
| 2022-07-29 | ₹341.98 crore | ₹298.38 crore | ₹0.00 | 7 | ₹281.63 |
| 2022-08-26 | ₹826.59 crore | ₹759.77 crore | ₹253.50 crore | 5 | ₹301.35 |
| 2022-09-30 | ₹1,523.75 crore | ₹1,451.81 crore | ₹139.62 crore | 7 | ₹308.68 |
| 2022-10-28 | ₹3,320.81 crore | ₹3,210.61 crore | ₹0.00 | 8 | ₹307.25 |
| 2022-11-25 | ₹7,146.05 crore | ₹7,167.53 crore | ₹3,478.86 crore | 7 | ₹321.24 |
| 2022-12-30 | ₹13,347.63 crore | ₹12,393.09 crore | ₹6,098.26 crore | 6 | ₹324.81 |
| 2023-01-27 | ₹19,118.47 crore | ₹19,283.18 crore | ₹1,504.05 crore | 8 | ₹320.56 |
| 2023-02-24 | ₹32,012.76 crore | ₹33,070.28 crore | ₹7,197.50 crore | 7 | ₹316.05 |
| 2023-03-31 | ₹69,334.60 crore | ₹74,795.60 crore | ₹34,363.18 crore | 5 | ₹305.23 |
| 2023-04-28 | ₹1.00 lakh crore | ₹1.04 lakh crore | ₹41,691.92 crore | 7 | ₹308.03 |
| 2023-05-26 | ₹1.78 lakh crore | ₹1.70 lakh crore | ₹7,650.87 crore | 10 | ₹327.69 |
| 2023-06-30 | ₹4.37 lakh crore | ₹3.89 lakh crore | ₹5,758.43 crore | 10 | ₹364.99 |
| 2023-07-28 | ₹10.15 lakh crore | ₹9.25 lakh crore | ₹13,648.77 crore | 9 | ₹419.13 |
| 2023-08-25 | ₹17.25 lakh crore | ₹16.24 lakh crore | ₹64,855.60 crore | 8 | ₹422.61 |
| 2023-09-29 | ₹36.24 lakh crore | ₹33.54 lakh crore | ₹64,855.60 crore | 8 | ₹454.34 |
| 2023-10-27 | ₹56.08 lakh crore | ₹56.28 lakh crore | ₹19.77 lakh crore | 7 | ₹457.23 |
| 2023-11-24 | ₹1.89 crore crore | ₹1.84 crore crore | ₹2.85 lakh crore | 10 | ₹559.94 |
| 2023-12-29 | ₹3.08 crore crore | ₹2.93 crore crore | ₹2.85 lakh crore | 10 | ₹584.76 |
| 2024-01-25 | ₹5.63 crore crore | ₹5.26 crore crore | ₹1.18 crore crore | 8 | ₹654.62 |
| 2024-02-23 | ₹11.46 crore crore | ₹10.31 crore crore | ₹29.68 lakh crore | 9 | ₹741.32 |
| 2024-03-28 | ₹17.54 crore crore | ₹17.32 crore crore | ₹0.00 | 11 | ₹733.86 |
| 2024-04-26 | ₹25.43 crore crore | ₹24.42 crore crore | ₹0.00 | 11 | ₹709.67 |
| 2024-05-31 | ₹51.00 crore crore | ₹50.94 crore crore | ₹6.73 crore crore | 10 | ₹685.04 |
| 2024-06-28 | ₹81.16 crore crore | ₹82.80 crore crore | ₹0.00 | 9 | ₹673.50 |
| 2024-07-26 | ₹139.95 crore crore | ₹139.33 crore crore | ₹30.32 crore crore | 7 | ₹697.48 |
| 2024-08-30 | ₹332.24 crore crore | ₹327.76 crore crore | ₹0.00 | 9 | ₹738.92 |
| 2024-09-27 | ₹481.84 crore crore | ₹505.21 crore crore | ₹78.71 crore crore | 7 | ₹714.90 |
| 2024-10-25 | ₹621.92 crore crore | ₹705.42 crore crore | ₹143.50 crore crore | 6 | ₹641.37 |
| 2024-11-29 | ₹1,474.64 crore crore | ₹1,466.54 crore crore | ₹0.00 | 8 | ₹689.44 |
| 2024-12-27 | ₹3,024.61 crore crore | ₹3,112.83 crore crore | ₹919.81 crore crore | 6 | ₹679.56 |
| 2025-01-24 | ₹5,227.03 crore crore | ₹6,021.15 crore crore | ₹3,443.01 crore crore | 4 | ₹614.75 |
| 2025-02-28 | ₹5,451.24 crore crore | ₹6,525.59 crore crore | ₹4,733.87 crore crore | 2 | ₹576.17 |
| 2025-03-28 | ₹6,796.17 crore crore | ₹7,677.63 crore crore | ₹3,509.78 crore crore | 4 | ₹592.33 |

## Engine B — still held at the end

| Stock | First entry | Blended entry ₹ | Lots | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|---:|
| CEMPRO | 2024-10-07 | 558.06 | 3 | 557.30 | 477.71 | -0.1% |
| CREDITACC | 2025-01-27 | 909.30 | 2 | 951.95 | 837.38 | +4.7% |
| INDIASHLTR | 2025-03-24 | 794.95 | 1 | 827.90 | 738.82 | +4.1% |
| NH | 2025-03-03 | 1,485.46 | 2 | 1,692.05 | 1,436.97 | +13.9% |

## Engine B — every closed trade

*Returns are on the blended entry price across lots.*

| Stock | First entry | Blended ₹ | Lots | Exit | Exit ₹ | Return |
|---|---|---:|---:|---|---:|---:|
| LALPATHLAB | 2020-03-09 | 835.00 | 1 | 2020-03-13 | 743.38 | -11.0% |
| DEEPAKNTR | 2020-03-09 | 508.80 | 1 | 2020-03-19 | 356.25 | -30.0% |
| DEEPAKNTR | 2020-04-13 | 498.24 | 2 | 2020-06-12 | 474.05 | -4.9% |
| LLOYDSENGG | 2020-05-18 | 0.87 | 3 | 2020-07-31 | 0.71 | -18.0% |
| EIDPARRY | 2020-06-01 | 273.16 | 4 | 2020-08-17 | 273.03 | -0.0% |
| ZENTEC | 2020-08-03 | 74.64 | 2 | 2020-08-31 | 80.56 | +7.9% |
| APLLTD | 2020-05-11 | 959.93 | 5 | 2020-09-01 | 928.62 | -3.3% |
| RCF | 2020-05-18 | 49.67 | 6 | 2020-09-09 | 45.84 | -7.7% |
| DEEPAKFERT | 2020-05-18 | 147.56 | 4 | 2020-09-22 | 149.57 | +1.4% |
| SCHAEFFLER | 2020-09-14 | 814.00 | 1 | 2020-09-23 | 724.67 | -11.0% |
| INDIAMART | 2020-09-07 | 2,421.33 | 3 | 2020-10-19 | 2,315.62 | -4.4% |
| CAPLIPOINT | 2020-06-15 | 546.03 | 4 | 2020-10-30 | 498.06 | -8.8% |
| GLAXO | 2020-09-14 | 1,622.53 | 2 | 2020-11-02 | 1,441.55 | -11.2% |
| ADVENZYMES | 2020-05-18 | 269.44 | 5 | 2020-11-03 | 292.33 | +8.5% |
| THYROCARE | 2020-08-24 | 340.16 | 4 | 2020-11-12 | 338.83 | -0.4% |
| APOLLO | 2020-05-18 | 11.82 | 6 | 2020-12-21 | 11.88 | +0.5% |
| ATGL | 2020-09-14 | 326.44 | 5 | 2020-12-21 | 332.60 | +1.9% |
| SYNGENE | 2020-04-27 | 562.27 | 6 | 2020-12-22 | 562.40 | +0.0% |
| BORORENEW | 2020-11-09 | 226.99 | 5 | 2021-01-20 | 247.59 | +9.1% |
| JUSTDIAL | 2020-10-26 | 638.47 | 3 | 2021-01-25 | 622.35 | -2.5% |
| PIIND | 2020-11-17 | 2,348.20 | 1 | 2021-01-25 | 2,107.67 | -10.2% |
| HFCL | 2020-11-23 | 28.50 | 5 | 2021-01-28 | 28.12 | -1.3% |
| HCLTECH | 2020-09-28 | 924.10 | 4 | 2021-01-29 | 928.05 | +0.4% |
| TRENT | 2020-11-17 | 725.02 | 2 | 2021-01-29 | 626.30 | -13.6% |
| TATAELXSI | 2021-01-25 | 2,755.37 | 3 | 2021-02-22 | 2,660.00 | -3.5% |
| GAEL | 2021-02-01 | 71.47 | 1 | 2021-02-23 | 62.70 | -12.3% |
| ITC | 2021-02-08 | 216.42 | 2 | 2021-02-26 | 197.41 | -8.8% |
| INDIAMART | 2021-01-25 | 4,296.73 | 3 | 2021-03-02 | 4,137.25 | -3.7% |
| GRAVITA | 2020-12-28 | 90.90 | 3 | 2021-03-17 | 96.13 | +5.8% |
| RCF | 2021-03-01 | 82.90 | 2 | 2021-03-17 | 79.16 | -4.5% |
| UJJIVANSFB | 2021-02-08 | 37.15 | 1 | 2021-03-18 | 32.12 | -13.5% |
| HINDZINC | 2021-01-25 | 288.74 | 2 | 2021-03-19 | 279.30 | -3.3% |
| MAHABANK | 2021-03-01 | 25.20 | 1 | 2021-03-19 | 18.37 | -27.1% |
| HONAUT | 2020-12-28 | 45,115.22 | 5 | 2021-03-22 | 41,911.15 | -7.1% |
| WHIRLPOOL | 2021-01-25 | 2,697.50 | 1 | 2021-03-24 | 2,244.99 | -16.8% |
| AUBANK | 2021-04-05 | 631.00 | 1 | 2021-04-12 | 533.06 | -15.5% |
| IOB | 2021-03-01 | 17.88 | 2 | 2021-04-28 | 14.82 | -17.1% |
| AMBER | 2020-10-26 | 3,032.44 | 6 | 2021-05-11 | 2,977.30 | -1.8% |
| POLYMED | 2020-09-07 | 931.08 | 7 | 2021-06-14 | 950.00 | +2.0% |
| WELSPUNLIV | 2021-03-22 | 128.22 | 6 | 2021-08-10 | 124.64 | -2.8% |
| MARKSANS | 2021-05-03 | 82.11 | 4 | 2021-08-10 | 77.14 | -6.1% |
| JSWENERGY | 2021-03-08 | 204.59 | 8 | 2021-08-11 | 228.00 | +11.4% |
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
| GABRIEL | 2021-03-08 | 137.96 | 5 | 2022-02-14 | 125.40 | -9.1% |
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

## Engine B — the complete trade blotter

*Buys, pyramid injections, sells and tax settlements; every stop raise and refused signal is in `_longrun_events_2020-03-01_to_2025-03-28.csv`, and engine A's full ledger in `_longrun_events_2020-03-01_to_2025-03-28_no_doubling.csv`.*

```
2020-03-09  DEEPAKNTR   BUY ₹10.00 at ₹508.80 (fresh Friday signal — BUY: 2.89× weekly, month 3.36×, ladder rising; stop ₹356.25; charges ₹0.01)
2020-03-09  LALPATHLAB  BUY ₹9.96 at ₹835.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.57×, ladder rising; stop ₹743.38; charges ₹0.01)
2020-03-13  LALPATHLAB  SELL ₹8.85 at stop ₹743.38 (-11.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-19  DEEPAKNTR   SELL ₹6.99 at stop ₹356.25 (-30.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-04-01  TAX         FY2020 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹4.09 / LT ₹0.00)
2020-04-13  DEEPAKNTR   BUY ₹9.59 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.48×, ladder rising; stop ₹240.25; charges ₹0.01)
2020-04-27  SYNGENE     BUY ₹9.60 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.95×, ladder rising; stop ₹285.95; charges ₹0.01)
2020-05-11  APLLTD      BUY ₹9.67 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.70× weekly, month 6.12×, ladder rising; stop ₹694.45; charges ₹0.01)
2020-05-18  ADVENZYMES  BUY ₹10.90 at ₹159.95 (fresh Friday signal — ACCUMULATE: 3.12× weekly, month 2.00×, ladder rising; stop ₹126.20; charges ₹0.01)
2020-05-18  APOLLO      BUY ₹10.83 at ₹8.70 (fresh Friday signal — BUY: 6.25× weekly, month 5.34×, ladder rising; stop ₹6.07; charges ₹0.01)
2020-05-18  DEEPAKFERT  BUY ₹10.81 at ₹101.03 (fresh Friday signal — ACCUMULATE: 2.11× weekly, month 4.53×, ladder rising; stop ₹88.52; charges ₹0.01)
2020-05-18  DEEPAKNTR   PYRAMID BUY ₹10.53 at ₹521.95 (box jump — doubling the stake with NEW capital; stop stays ₹474.05; charges ₹0.01)
2020-05-18  LLOYDSENGG  BUY ₹10.90 at ₹0.63 (fresh Friday signal — BUY: 5.26× weekly, month 1.93×, ladder rising; stop ₹0.37; charges ₹0.01)
2020-05-18  RCF         BUY ₹10.88 at ₹39.90 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 2.56×, ladder rising; stop ₹35.25; charges ₹0.01)
2020-06-01  EIDPARRY    BUY ₹12.35 at ₹198.00 (fresh Friday signal — BUY: 6.29× weekly, month 2.35×, ladder rising; stop ₹132.60; charges ₹0.01)
2020-06-01  LLOYDSENGG  PYRAMID BUY ₹12.56 at ₹0.72 (box jump — doubling the stake with NEW capital; stop stays ₹0.46; charges ₹0.01)
2020-06-08  APLLTD      PYRAMID BUY ₹10.73 at ₹860.95 (box jump — doubling the stake with NEW capital; stop stays ₹785.37; charges ₹0.01)
2020-06-08  APOLLO      PYRAMID BUY ₹11.69 at ₹9.40 (box jump — doubling the stake with NEW capital; stop stays ₹7.57; charges ₹0.01)
2020-06-08  SYNGENE     PYRAMID BUY ₹11.24 at ₹373.90 (box jump — doubling the stake with NEW capital; stop stays ₹323.19; charges ₹0.01)
2020-06-12  DEEPAKNTR   SELL ₹19.10 at stop ₹474.05 (-4.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-06-15  CAPLIPOINT  BUY ₹17.76 at ₹383.80 (fresh Friday signal — BUY: 5.39× weekly, month 2.09×, ladder rising; stop ₹291.46; charges ₹0.02)
2020-06-15  RCF         PYRAMID BUY ₹12.24 at ₹44.95 (box jump — doubling the stake with NEW capital; stop stays ₹40.28; charges ₹0.01)
2020-06-22  ADVENZYMES  PYRAMID BUY ₹11.53 at ₹169.35 (box jump — doubling the stake with NEW capital; stop stays ₹149.98; charges ₹0.01)
2020-06-22  APOLLO      PYRAMID BUY ₹27.71 at ₹11.15 (box jump — doubling the stake with NEW capital; stop stays ₹8.34; charges ₹0.03)
2020-06-22  EIDPARRY    PYRAMID BUY ₹16.67 at ₹267.45 (box jump — doubling the stake with NEW capital; stop stays ₹204.49; charges ₹0.02)
2020-06-22  LLOYDSENGG  PYRAMID BUY ₹36.83 at ₹1.06 (box jump — doubling the stake with NEW capital; stop stays ₹0.71; charges ₹0.04)
2020-06-29  EIDPARRY    PYRAMID BUY ₹33.88 at ₹272.00 (box jump — doubling the stake with NEW capital; stop stays ₹249.19; charges ₹0.04)
2020-07-06  APLLTD      PYRAMID BUY ₹22.33 at ₹896.00 (box jump — doubling the stake with NEW capital; stop stays ₹830.30; charges ₹0.03)
2020-07-06  APOLLO      PYRAMID BUY ₹57.42 at ₹11.56 (box jump — doubling the stake with NEW capital; stop stays ₹9.39; charges ₹0.07)
2020-07-06  DEEPAKFERT  PYRAMID BUY ₹11.92 at ₹111.51 (box jump — doubling the stake with NEW capital; stop stays ₹102.48; charges ₹0.01)
2020-07-06  RCF         PYRAMID BUY ₹25.99 at ₹47.75 (box jump — doubling the stake with NEW capital; stop stays ₹43.23; charges ₹0.03)
2020-07-06  SYNGENE     PYRAMID BUY ₹26.31 at ₹438.00 (box jump — doubling the stake with NEW capital; stop stays ₹375.25; charges ₹0.03)
2020-07-27  EIDPARRY    PYRAMID BUY ₹73.19 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹273.03; charges ₹0.09)
2020-07-27  RCF         PYRAMID BUY ₹53.95 at ₹49.60 (box jump — doubling the stake with NEW capital; stop stays ₹43.37; charges ₹0.06)
2020-07-31  LLOYDSENGG  SELL ₹49.35 at stop ₹0.71 (-18.0%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2020-08-03  APLLTD      PYRAMID BUY ₹49.06 at ₹985.00 (box jump — doubling the stake with NEW capital; stop stays ₹903.45; charges ₹0.06)
2020-08-03  ZENTEC      BUY ₹51.04 at ₹58.80 (fresh Friday signal — ACCUMULATE: 4.33× weekly, month 4.91×, ladder rising; stop ₹42.67; charges ₹0.06)
2020-08-10  RCF         PYRAMID BUY ₹112.52 at ₹51.75 (box jump — doubling the stake with NEW capital; stop stays ₹43.89; charges ₹0.13)
2020-08-17  ADVENZYMES  PYRAMID BUY ₹30.46 at ₹223.90 (box jump — doubling the stake with NEW capital; stop stays ₹194.75; charges ₹0.04)
2020-08-17  DEEPAKFERT  PYRAMID BUY ₹32.61 at ₹152.62 (box jump — doubling the stake with NEW capital; stop stays ₹135.30; charges ₹0.04)
2020-08-17  EIDPARRY    SELL ₹135.72 at stop ₹273.03 (-0.0%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2020-08-17  SYNGENE     PYRAMID BUY ₹59.29 at ₹493.80 (box jump — doubling the stake with NEW capital; stop stays ₹434.44; charges ₹0.07)
2020-08-24  CAPLIPOINT  PYRAMID BUY ₹24.99 at ₹540.80 (box jump — doubling the stake with NEW capital; stop stays ₹454.79; charges ₹0.03)
2020-08-24  RCF         PYRAMID BUY ₹216.43 at ₹49.80 (box jump — doubling the stake with NEW capital; stop stays ₹45.84; charges ₹0.26)
2020-08-24  THYROCARE   BUY ₹126.60 at ₹263.35 (fresh Friday signal — BUY: 7.09× weekly, month 4.48×, ladder rising; stop ₹199.77; charges ₹0.15)
2020-08-24  ZENTEC      PYRAMID BUY ₹78.46 at ₹90.50 (box jump — doubling the stake with NEW capital; stop stays ₹80.56; charges ₹0.09)
2020-08-31  APLLTD      PYRAMID BUY ₹99.45 at ₹999.00 (box jump — doubling the stake with NEW capital; stop stays ₹928.62; charges ₹0.12)
2020-08-31  ZENTEC      SELL ₹139.46 at stop ₹80.56 (+7.9%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹184.58 at stop ₹928.62 (-3.3%, charges ₹0.19) — the cash goes back to work at the next Friday screen
2020-09-07  DEEPAKFERT  PYRAMID BUY ₹70.77 at ₹165.71 (box jump — doubling the stake with NEW capital; stop stays ₹149.57; charges ₹0.08)
2020-09-07  INDIAMART   BUY ₹146.24 at ₹2,124.50 (fresh Friday signal — BUY: 2.46× weekly, month 1.96×, ladder rising; stop ₹1,655.61; charges ₹0.17)
2020-09-07  POLYMED     BUY ₹147.18 at ₹449.70 (fresh Friday signal — BUY: 2.13× weekly, month 2.66×, ladder rising; stop ₹372.40; charges ₹0.17)
2020-09-07  THYROCARE   PYRAMID BUY ₹120.84 at ₹251.67 (box jump — doubling the stake with NEW capital; stop stays ₹235.03; charges ₹0.14)
2020-09-09  RCF         SELL ₹397.79 at stop ₹45.84 (-7.7%, charges ₹0.41) — the cash goes back to work at the next Friday screen
2020-09-14  ATGL        BUY ₹101.09 at ₹209.75 (fresh Friday signal — BUY: 1.66× weekly, month 1.67×, ladder rising; stop ₹159.58; charges ₹0.12)
2020-09-14  GLAXO       BUY ₹167.96 at ₹1,675.00 (fresh Friday signal — BUY: 2.55× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.20)
2020-09-14  POLYMED     PYRAMID BUY ₹157.55 at ₹481.95 (box jump — doubling the stake with NEW capital; stop stays ₹408.50; charges ₹0.19)
2020-09-14  SCHAEFFLER  BUY ₹168.47 at ₹814.00 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 1.89×, ladder rising; stop ₹724.67; charges ₹0.20)
2020-09-21  ADVENZYMES  PYRAMID BUY ₹68.75 at ₹252.85 (box jump — doubling the stake with NEW capital; stop stays ₹212.37; charges ₹0.08)
2020-09-21  CAPLIPOINT  PYRAMID BUY ₹55.61 at ₹602.00 (box jump — doubling the stake with NEW capital; stop stays ₹486.88; charges ₹0.07)
2020-09-21  INDIAMART   PYRAMID BUY ₹173.35 at ₹2,521.27 (box jump — doubling the stake with NEW capital; stop stays ₹2,099.50; charges ₹0.21)
2020-09-22  DEEPAKFERT  SELL ₹127.54 at stop ₹149.57 (+1.4%, charges ₹0.13) — the cash goes back to work at the next Friday screen
2020-09-23  SCHAEFFLER  SELL ₹149.65 at stop ₹724.67 (-11.0%, charges ₹0.16) — the cash goes back to work at the next Friday screen
2020-09-28  CAPLIPOINT  PYRAMID BUY ₹103.40 at ₹560.00 (box jump — doubling the stake with NEW capital; stop stays ₹498.06; charges ₹0.12)
2020-09-28  HCLTECH     BUY ₹221.20 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.26)
2020-09-28  SYNGENE     PYRAMID BUY ₹140.70 at ₹586.30 (box jump — doubling the stake with NEW capital; stop stays ₹501.60; charges ₹0.17)
2020-10-05  ATGL        PYRAMID BUY ₹93.87 at ₹195.00 (box jump — doubling the stake with NEW capital; stop stays ₹162.03; charges ₹0.11)
2020-10-05  GLAXO       PYRAMID BUY ₹157.25 at ₹1,570.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,441.55; charges ₹0.19)
2020-10-05  POLYMED     PYRAMID BUY ₹307.34 at ₹470.35 (box jump — doubling the stake with NEW capital; stop stays ₹420.11; charges ₹0.36)
2020-10-12  HCLTECH     PYRAMID BUY ₹226.84 at ₹860.80 (box jump — doubling the stake with NEW capital; stop stays ₹766.75; charges ₹0.27)
2020-10-12  INDIAMART   PYRAMID BUY ₹346.32 at ₹2,520.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,315.62; charges ₹0.41)
2020-10-19  INDIAMART   SELL ₹635.42 at stop ₹2,315.62 (-4.4%, charges ₹0.66) — the cash goes back to work at the next Friday screen
2020-10-19  THYROCARE   PYRAMID BUY ₹330.93 at ₹344.82 (box jump — doubling the stake with NEW capital; stop stays ₹311.14; charges ₹0.39)
2020-10-26  ADVENZYMES  PYRAMID BUY ₹171.42 at ₹315.40 (box jump — doubling the stake with NEW capital; stop stays ₹292.33; charges ₹0.20)
2020-10-26  AMBER       BUY ₹257.28 at ₹2,342.00 (fresh Friday signal — BUY: 2.70× weekly, month 2.63×, ladder rising; stop ₹1,692.83; charges ₹0.30)
2020-10-26  HCLTECH     PYRAMID BUY ₹449.31 at ₹853.00 (box jump — doubling the stake with NEW capital; stop stays ₹779.57; charges ₹0.53)
2020-10-26  JUSTDIAL    BUY ₹434.14 at ₹584.00 (fresh Friday signal — BUY: 4.99× weekly, month 1.82×, ladder rising; stop ₹383.80; charges ₹0.51)
2020-10-30  CAPLIPOINT  SELL ₹183.63 at stop ₹498.06 (-8.8%, charges ₹0.19) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹288.29 at stop ₹1,441.55 (-11.2%, charges ₹0.30) — the cash goes back to work at the next Friday screen
2020-11-03  ADVENZYMES  SELL ₹317.25 at stop ₹292.33 (+8.5%, charges ₹0.33) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹507.15 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 1.65×, ladder rising; stop ₹77.16; charges ₹0.60)
2020-11-09  THYROCARE   PYRAMID BUY ₹727.50 at ₹379.23 (box jump — doubling the stake with NEW capital; stop stays ₹338.83; charges ₹0.86)
2020-11-12  THYROCARE   SELL ₹1,297.86 at stop ₹338.83 (-0.4%, charges ₹1.35) — the cash goes back to work at the next Friday screen
2020-11-17  AMBER       PYRAMID BUY ₹256.75 at ₹2,340.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,035.85; charges ₹0.30)
2020-11-17  APOLLO      PYRAMID BUY ₹113.88 at ₹11.47 (box jump — doubling the stake with NEW capital; stop stays ₹10.21; charges ₹0.13)
2020-11-17  ATGL        PYRAMID BUY ₹236.94 at ₹246.25 (box jump — doubling the stake with NEW capital; stop stays ₹219.69; charges ₹0.28)
2020-11-17  JUSTDIAL    PYRAMID BUY ₹464.06 at ₹625.00 (box jump — doubling the stake with NEW capital; stop stays ₹523.11; charges ₹0.55)
2020-11-17  PIIND       BUY ₹616.17 at ₹2,348.20 (fresh Friday signal — ACCUMULATE: 1.62× weekly, month 1.81×, ladder rising; stop ₹2,107.67; charges ₹0.73)
2020-11-17  TRENT       BUY ₹617.16 at ₹755.00 (fresh Friday signal — ACCUMULATE: 3.32× weekly, month 1.93×, ladder rising; stop ₹551.90; charges ₹0.73)
2020-11-23  HFCL        BUY ₹346.56 at ₹18.20 (fresh Friday signal — BUY: 3.09× weekly, month 1.77×, ladder rising; stop ₹15.20; charges ₹0.41)
2020-12-01  BORORENEW   PYRAMID BUY ₹645.25 at ₹127.00 (box jump — doubling the stake with NEW capital; stop stays ₹106.40; charges ₹0.76)
2020-12-01  HFCL        PYRAMID BUY ₹351.85 at ₹18.50 (box jump — doubling the stake with NEW capital; stop stays ₹16.81; charges ₹0.42)
2020-12-07  ATGL        PYRAMID BUY ₹696.41 at ₹362.10 (box jump — doubling the stake with NEW capital; stop stays ₹295.81; charges ₹0.83)
2020-12-14  AMBER       PYRAMID BUY ₹512.75 at ₹2,337.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,168.75; charges ₹0.61)
2020-12-14  BORORENEW   PYRAMID BUY ₹1,350.16 at ₹132.95 (box jump — doubling the stake with NEW capital; stop stays ₹123.97; charges ₹1.60)
2020-12-14  HFCL        PYRAMID BUY ₹855.35 at ₹22.50 (box jump — doubling the stake with NEW capital; stop stays ₹19.05; charges ₹1.01)
2020-12-14  TRENT       PYRAMID BUY ₹567.44 at ₹695.00 (box jump — doubling the stake with NEW capital; stop stays ₹626.30; charges ₹0.67)
2020-12-21  APOLLO      PYRAMID BUY ₹248.07 at ₹12.50 (box jump — doubling the stake with NEW capital; stop stays ₹11.88; charges ₹0.29)
2020-12-21  APOLLO      SELL ₹470.76 at stop ₹11.88 (+0.5%, charges ₹0.49) — the cash goes back to work at the next Friday screen
2020-12-21  ATGL        PYRAMID BUY ₹1,382.96 at ₹359.75 (box jump — doubling the stake with NEW capital; stop stays ₹332.60; charges ₹1.64)
2020-12-21  ATGL        SELL ₹2,553.01 at stop ₹332.60 (+1.9%, charges ₹2.65) — the cash goes back to work at the next Friday screen
2020-12-21  SYNGENE     PYRAMID BUY ₹292.61 at ₹610.00 (box jump — doubling the stake with NEW capital; stop stays ₹562.40; charges ₹0.35)
2020-12-22  SYNGENE     SELL ₹538.68 at stop ₹562.40 (+0.0%, charges ₹0.56) — the cash goes back to work at the next Friday screen
2020-12-28  BORORENEW   PYRAMID BUY ₹4,770.21 at ₹235.00 (box jump — doubling the stake with NEW capital; stop stays ₹148.20; charges ₹5.65)
2020-12-28  GRAVITA     BUY ₹1,439.32 at ₹69.65 (fresh Friday signal — BUY: 2.45× weekly, month 4.29×, ladder rising; stop ₹46.41; charges ₹1.71)
2020-12-28  HONAUT      BUY ₹2,123.14 at ₹38,887.75 (fresh Friday signal — BUY: 5.49× weekly, month 1.69×, ladder rising; stop ₹29,024.49; charges ₹2.52)
2021-01-11  HFCL        PYRAMID BUY ₹2,363.17 at ₹31.10 (box jump — doubling the stake with NEW capital; stop stays ₹24.13; charges ₹2.80)
2021-01-11  HONAUT      PYRAMID BUY ₹2,235.81 at ₹41,000.00 (box jump — doubling the stake with NEW capital; stop stays ₹34,722.50; charges ₹2.65)
2021-01-18  BORORENEW   PYRAMID BUY ₹11,157.70 at ₹275.00 (box jump — doubling the stake with NEW capital; stop stays ₹247.59; charges ₹13.22)
2021-01-18  GRAVITA     PYRAMID BUY ₹1,614.09 at ₹78.20 (box jump — doubling the stake with NEW capital; stop stays ₹70.89; charges ₹1.91)
2021-01-20  BORORENEW   SELL ₹20,058.46 at stop ₹247.59 (+9.1%, charges ₹20.81) — the cash goes back to work at the next Friday screen
2021-01-25  AMBER       PYRAMID BUY ₹1,095.94 at ₹2,500.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,347.45; charges ₹1.30)
2021-01-25  HCLTECH     PYRAMID BUY ₹1,049.70 at ₹997.00 (box jump — doubling the stake with NEW capital; stop stays ₹928.05; charges ₹1.24)
2021-01-25  HFCL        PYRAMID BUY ₹4,746.31 at ₹31.25 (box jump — doubling the stake with NEW capital; stop stays ₹28.12; charges ₹5.62)
2021-01-25  HINDZINC    BUY ₹4,455.05 at ₹277.40 (fresh Friday signal — ACCUMULATE: 2.31× weekly, month 2.09×, ladder rising; stop ₹248.97; charges ₹5.28)
2021-01-25  INDIAMART   BUY ₹4,465.60 at ₹3,990.00 (fresh Friday signal — BUY: 2.37× weekly, month 1.58×, ladder rising; stop ₹3,323.20; charges ₹5.29)
2021-01-25  JUSTDIAL    PYRAMID BUY ₹998.07 at ₹672.50 (box jump — doubling the stake with NEW capital; stop stays ₹622.35; charges ₹1.18)
2021-01-25  JUSTDIAL    SELL ₹1,844.28 at stop ₹622.35 (-2.5%, charges ₹1.91) — the cash goes back to work at the next Friday screen
2021-01-25  PIIND       SELL ₹551.83 at stop ₹2,107.67 (-10.2%, charges ₹0.57) — the cash goes back to work at the next Friday screen
2021-01-25  TATAELXSI   BUY ₹4,488.35 at ₹2,608.00 (fresh Friday signal — BUY: 2.94× weekly, month 2.74×, ladder rising; stop ₹1,712.61; charges ₹5.32)
2021-01-25  WHIRLPOOL   BUY ₹4,439.52 at ₹2,697.50 (fresh Friday signal — BUY: 1.73× weekly, month 2.10×, ladder rising; stop ₹2,244.99; charges ₹5.26)
2021-01-28  HFCL        SELL ₹8,527.94 at stop ₹28.12 (-1.3%, charges ₹8.85) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹1,951.04 at stop ₹928.05 (+0.4%, charges ₹2.02) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹1,021.04 at stop ₹626.30 (-13.6%, charges ₹1.06) — the cash goes back to work at the next Friday screen
2021-02-01  GAEL        BUY ₹5,442.74 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹6.45)
2021-02-01  INDIAMART   PYRAMID BUY ₹4,392.20 at ₹3,929.07 (box jump — doubling the stake with NEW capital; stop stays ₹3,460.38; charges ₹5.20)
2021-02-01  TATAELXSI   PYRAMID BUY ₹4,661.37 at ₹2,711.75 (box jump — doubling the stake with NEW capital; stop stays ₹2,275.70; charges ₹5.52)
2021-02-08  HONAUT      PYRAMID BUY ₹4,577.86 at ₹41,999.00 (box jump — doubling the stake with NEW capital; stop stays ₹35,971.61; charges ₹5.42)
2021-02-08  ITC         BUY ₹4,658.76 at ₹228.69 (fresh Friday signal — BUY: 2.38× weekly, month 1.68×, ladder rising; stop ₹184.60; charges ₹5.52)
2021-02-08  UJJIVANSFB  BUY ₹6,004.56 at ₹37.15 (fresh Friday signal — ACCUMULATE: 2.60× weekly, month 2.19×, ladder rising; stop ₹32.12; charges ₹7.11)
2021-02-15  HINDZINC    PYRAMID BUY ₹4,813.90 at ₹300.10 (box jump — doubling the stake with NEW capital; stop stays ₹279.30; charges ₹5.70)
2021-02-15  INDIAMART   PYRAMID BUY ₹10,354.97 at ₹4,634.30 (box jump — doubling the stake with NEW capital; stop stays ₹4,137.25; charges ₹12.27)
2021-02-15  TATAELXSI   PYRAMID BUY ₹9,795.67 at ₹2,851.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,660.00; charges ₹11.61)
2021-02-22  HONAUT      PYRAMID BUY ₹9,804.11 at ₹45,000.00 (box jump — doubling the stake with NEW capital; stop stays ₹39,140.00; charges ₹11.62)
2021-02-22  ITC         PYRAMID BUY ₹4,153.63 at ₹204.14 (box jump — doubling the stake with NEW capital; stop stays ₹197.41; charges ₹4.92)
2021-02-22  TATAELXSI   SELL ₹18,249.07 at stop ₹2,660.00 (-3.5%, charges ₹18.93) — the cash goes back to work at the next Friday screen
2021-02-23  GAEL        SELL ₹4,763.93 at stop ₹62.70 (-12.3%, charges ₹4.94) — the cash goes back to work at the next Friday screen
2021-02-26  ITC         SELL ₹8,020.39 at stop ₹197.41 (-8.8%, charges ₹8.32) — the cash goes back to work at the next Friday screen
2021-03-01  AMBER       PYRAMID BUY ₹2,874.92 at ₹3,281.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,909.80; charges ₹3.41)
2021-03-01  IOB         BUY ₹10,165.60 at ₹18.90 (fresh Friday signal — ACCUMULATE: 3.52× weekly, month 9.60×, ladder rising; stop ₹13.70; charges ₹12.04)
2021-03-01  MAHABANK    BUY ₹10,105.30 at ₹25.20 (fresh Friday signal — ACCUMULATE: 3.28× weekly, month 6.34×, ladder rising; stop ₹18.37; charges ₹11.97)
2021-03-01  RCF         BUY ₹10,028.43 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.12×, ladder rising; stop ₹50.16; charges ₹11.88)
2021-03-02  INDIAMART   SELL ₹18,458.60 at stop ₹4,137.25 (-3.7%, charges ₹19.15) — the cash goes back to work at the next Friday screen
2021-03-08  GABRIEL     BUY ₹6,869.76 at ₹127.30 (fresh Friday signal — BUY: 2.66× weekly, month 2.76×, ladder rising; stop ₹86.90; charges ₹8.14)
2021-03-08  HONAUT      PYRAMID BUY ₹20,575.96 at ₹47,248.90 (box jump — doubling the stake with NEW capital; stop stays ₹41,911.15; charges ₹24.38)
2021-03-08  JSWENERGY   BUY ₹12,322.91 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.49×, ladder rising; stop ₹65.79; charges ₹14.60)
2021-03-08  POLYMED     PYRAMID BUY ₹938.93 at ₹718.90 (box jump — doubling the stake with NEW capital; stop stays ₹642.77; charges ₹1.11)
2021-03-15  GRAVITA     PYRAMID BUY ₹4,451.59 at ₹107.90 (box jump — doubling the stake with NEW capital; stop stays ₹96.13; charges ₹5.27)
2021-03-15  JSWENERGY   PYRAMID BUY ₹12,857.19 at ₹85.50 (box jump — doubling the stake with NEW capital; stop stays ₹76.43; charges ₹15.23)
2021-03-15  RCF         PYRAMID BUY ₹10,742.75 at ₹85.80 (box jump — doubling the stake with NEW capital; stop stays ₹79.16; charges ₹12.73)
2021-03-17  GRAVITA     SELL ₹7,919.08 at stop ₹96.13 (+5.8%, charges ₹8.21) — the cash goes back to work at the next Friday screen
2021-03-17  RCF         SELL ₹19,790.48 at stop ₹79.16 (-4.5%, charges ₹20.53) — the cash goes back to work at the next Friday screen
2021-03-18  UJJIVANSFB  SELL ₹5,180.04 at stop ₹32.12 (-13.5%, charges ₹5.37) — the cash goes back to work at the next Friday screen
2021-03-19  HINDZINC    SELL ₹8,945.91 at stop ₹279.30 (-3.3%, charges ₹9.28) — the cash goes back to work at the next Friday screen
2021-03-19  MAHABANK    SELL ₹7,350.09 at stop ₹18.37 (-27.1%, charges ₹7.62) — the cash goes back to work at the next Friday screen
2021-03-22  DEEPAKFERT  BUY ₹14,608.23 at ₹237.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.82×, ladder rising; stop ₹184.78; charges ₹17.31)
2021-03-22  GABRIEL     PYRAMID BUY ₹5,966.86 at ₹110.70 (box jump — doubling the stake with NEW capital; stop stays ₹86.92; charges ₹7.07)
2021-03-22  HONAUT      SELL ₹36,443.53 at stop ₹41,911.15 (-7.1%, charges ₹37.80) — the cash goes back to work at the next Friday screen
2021-03-22  KEI         BUY ₹14,528.90 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹17.21)
2021-03-22  WELSPUNLIV  BUY ₹14,602.79 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.45×, ladder rising; stop ₹67.45; charges ₹17.30)
2021-03-24  WHIRLPOOL   SELL ₹3,686.58 at stop ₹2,244.99 (-16.8%, charges ₹3.82) — the cash goes back to work at the next Friday screen
2021-03-30  DEEPAKFERT  PYRAMID BUY ₹13,738.24 at ₹223.15 (box jump — doubling the stake with NEW capital; stop stays ₹209.52; charges ₹16.28)
2021-03-30  KEI         PYRAMID BUY ₹14,461.64 at ₹520.20 (box jump — doubling the stake with NEW capital; stop stays ₹471.20; charges ₹17.13)
2021-03-30  KPITTECH    BUY ₹18,870.07 at ₹182.00 (fresh Friday signal — BUY: 1.71× weekly, month 2.75×, ladder rising; stop ₹136.62; charges ₹22.36)
2021-03-30  POLYMED     PYRAMID BUY ₹2,128.81 at ₹815.45 (box jump — doubling the stake with NEW capital; stop stays ₹719.96; charges ₹2.52)
2021-03-30  WELSPUNLIV  PYRAMID BUY ₹15,042.13 at ₹84.00 (box jump — doubling the stake with NEW capital; stop stays ₹68.17; charges ₹17.82)
2021-04-01  TAX         FY2021 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹9,480.17 / LT ₹0.00)
2021-04-05  AUBANK      BUY ₹19,553.48 at ₹631.00 (fresh Friday signal — ACCUMULATE: 3.80× weekly, month 2.02×, ladder rising; stop ₹533.06; charges ₹23.17)
2021-04-05  IOB         PYRAMID BUY ₹9,052.24 at ₹16.85 (box jump — doubling the stake with NEW capital; stop stays ₹14.82; charges ₹10.73)
2021-04-12  AMBER       PYRAMID BUY ₹5,630.84 at ₹3,215.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,977.30; charges ₹6.67)
2021-04-12  AUBANK      SELL ₹16,481.84 at stop ₹533.06 (-15.5%, charges ₹17.10) — the cash goes back to work at the next Friday screen
2021-04-19  JSWENERGY   PYRAMID BUY ₹28,614.72 at ₹95.20 (box jump — doubling the stake with NEW capital; stop stays ₹81.99; charges ₹33.90)
2021-04-19  KPITTECH    PYRAMID BUY ₹19,650.29 at ₹189.75 (box jump — doubling the stake with NEW capital; stop stays ₹171.05; charges ₹23.28)
2021-04-19  KPRMILL     BUY ₹23,634.08 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹28.00)
2021-04-26  KPRMILL     PYRAMID BUY ₹24,365.27 at ₹243.59 (box jump — doubling the stake with NEW capital; stop stays ₹221.37; charges ₹28.87)
2021-04-28  IOB         SELL ₹15,897.43 at stop ₹14.82 (-17.1%, charges ₹16.49) — the cash goes back to work at the next Friday screen
2021-05-03  MARKSANS    BUY ₹15,897.43 at ₹70.95 (fresh Friday signal — ACCUMULATE: 3.13× weekly, month 3.97×, ladder rising; stop ₹64.12; charges ₹18.84)
2021-05-10  KEI         PYRAMID BUY ₹29,367.36 at ₹528.50 (box jump — doubling the stake with NEW capital; stop stays ₹485.02; charges ₹34.80)
2021-05-11  AMBER       SELL ₹10,412.07 at stop ₹2,977.30 (-1.8%, charges ₹10.80) — the cash goes back to work at the next Friday screen
2021-05-17  KPRMILL     PYRAMID BUY ₹58,780.30 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹268.28; charges ₹69.64)
2021-05-17  POLYMED     PYRAMID BUY ₹5,240.01 at ₹1,004.20 (box jump — doubling the stake with NEW capital; stop stays ₹902.50; charges ₹6.21)
2021-05-24  DEEPAKFERT  PYRAMID BUY ₹36,917.15 at ₹300.00 (box jump — doubling the stake with NEW capital; stop stays ₹264.10; charges ₹43.74)
2021-05-24  MARKSANS    PYRAMID BUY ₹16,773.79 at ₹74.95 (box jump — doubling the stake with NEW capital; stop stays ₹68.02; charges ₹19.87)
2021-05-31  KEI         PYRAMID BUY ₹69,307.02 at ₹624.00 (box jump — doubling the stake with NEW capital; stop stays ₹558.60; charges ₹82.12)
2021-06-07  DEEPAKFERT  PYRAMID BUY ₹73,052.66 at ₹297.00 (box jump — doubling the stake with NEW capital; stop stays ₹269.80; charges ₹86.55)
2021-06-07  JSWENERGY   PYRAMID BUY ₹81,948.21 at ₹136.40 (box jump — doubling the stake with NEW capital; stop stays ₹108.49; charges ₹97.09)
2021-06-07  KPITTECH    PYRAMID BUY ₹50,279.09 at ₹242.90 (box jump — doubling the stake with NEW capital; stop stays ₹214.70; charges ₹59.57)
2021-06-07  POLYMED     PYRAMID BUY ₹10,513.96 at ₹1,008.05 (box jump — doubling the stake with NEW capital; stop stays ₹950.00; charges ₹12.46)
2021-06-07  WELSPUNLIV  PYRAMID BUY ₹33,252.04 at ₹92.90 (box jump — doubling the stake with NEW capital; stop stays ₹80.48; charges ₹39.40)
2021-06-14  JSWENERGY   PYRAMID BUY ₹1.88 lakh at ₹156.95 (box jump — doubling the stake with NEW capital; stop stays ₹126.83; charges ₹223.31)
2021-06-14  POLYMED     SELL ₹19,784.74 at stop ₹950.00 (+2.0%, charges ₹20.52) — the cash goes back to work at the next Friday screen
2021-06-21  KEI         PYRAMID BUY ₹1.51 lakh at ₹682.20 (box jump — doubling the stake with NEW capital; stop stays ₹608.00; charges ₹179.44)
2021-06-28  JSWENERGY   PYRAMID BUY ₹3.70 lakh at ₹154.10 (box jump — doubling the stake with NEW capital; stop stays ₹138.04; charges ₹438.25)
2021-06-28  MARKSANS    PYRAMID BUY ₹39,141.75 at ₹87.50 (box jump — doubling the stake with NEW capital; stop stays ₹76.87; charges ₹46.38)
2021-07-05  DEEPAKFERT  PYRAMID BUY ₹1.94 lakh at ₹395.00 (box jump — doubling the stake with NEW capital; stop stays ₹364.65; charges ₹230.09)
2021-07-12  JSWENERGY   PYRAMID BUY ₹8.06 lakh at ₹168.00 (box jump — doubling the stake with NEW capital; stop stays ₹154.47; charges ₹955.00)
2021-07-19  KPITTECH    PYRAMID BUY ₹1.10 lakh at ₹267.05 (box jump — doubling the stake with NEW capital; stop stays ₹232.94; charges ₹130.91)
2021-07-19  KPRMILL     PYRAMID BUY ₹1.49 lakh at ₹372.00 (box jump — doubling the stake with NEW capital; stop stays ₹333.07; charges ₹176.14)
2021-07-19  WELSPUNLIV  PYRAMID BUY ₹89,394.65 at ₹124.95 (box jump — doubling the stake with NEW capital; stop stays ₹97.56; charges ₹105.92)
2021-08-02  WELSPUNLIV  PYRAMID BUY ₹1.93 lakh at ₹134.75 (box jump — doubling the stake with NEW capital; stop stays ₹117.99; charges ₹228.31)
2021-08-09  JSWENERGY   PYRAMID BUY ₹24.26 lakh at ₹253.00 (box jump — doubling the stake with NEW capital; stop stays ₹228.00; charges ₹2,874.68)
2021-08-09  KPITTECH    PYRAMID BUY ₹2.58 lakh at ₹312.45 (box jump — doubling the stake with NEW capital; stop stays ₹266.76; charges ₹306.15)
2021-08-09  KPRMILL     PYRAMID BUY ₹3.19 lakh at ₹399.60 (box jump — doubling the stake with NEW capital; stop stays ₹352.48; charges ₹378.19)
2021-08-09  MARKSANS    PYRAMID BUY ₹75,107.64 at ₹84.00 (box jump — doubling the stake with NEW capital; stop stays ₹77.14; charges ₹88.99)
2021-08-09  WELSPUNLIV  PYRAMID BUY ₹3.88 lakh at ₹135.90 (box jump — doubling the stake with NEW capital; stop stays ₹124.64; charges ₹460.25)
2021-08-10  MARKSANS    SELL ₹1.38 lakh at stop ₹77.14 (-6.1%, charges ₹142.86) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNLIV  SELL ₹7.11 lakh at stop ₹124.64 (-2.8%, charges ₹737.91) — the cash goes back to work at the next Friday screen
2021-08-11  JSWENERGY   SELL ₹43.66 lakh at stop ₹228.00 (+11.4%, charges ₹4,528.74) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹5.62 lakh at stop ₹352.48 (-1.9%, charges ₹583.16) — the cash goes back to work at the next Friday screen
2021-08-16  GABRIEL     PYRAMID BUY ₹16,085.36 at ₹149.30 (box jump — doubling the stake with NEW capital; stop stays ₹118.77; charges ₹19.06)
2021-08-16  KEI         PYRAMID BUY ₹3.31 lakh at ₹744.95 (box jump — doubling the stake with NEW capital; stop stays ₹663.29; charges ₹391.67)
2021-08-16  TATAINVEST  BUY ₹7.51 lakh at ₹130.81 (fresh Friday signal — BUY: 8.45× weekly, month 4.82×, ladder rising; stop ₹103.11; charges ₹889.53)
2021-08-23  DEEPAKFERT  PYRAMID BUY ₹3.94 lakh at ₹401.00 (box jump — doubling the stake with NEW capital; stop stays ₹380.00; charges ₹466.90)
2021-08-23  GRAVITA     BUY ₹8.40 lakh at ₹188.60 (fresh Friday signal — BUY: 2.16× weekly, month 1.88×, ladder rising; stop ₹151.95; charges ₹995.66)
2021-08-23  TATAINVEST  PYRAMID BUY ₹7.08 lakh at ₹123.50 (box jump — doubling the stake with NEW capital; stop stays ₹113.90; charges ₹838.86)
2021-08-30  GABRIEL     PYRAMID BUY ₹29,653.60 at ₹137.70 (box jump — doubling the stake with NEW capital; stop stays ₹124.06; charges ₹35.13)
2021-08-30  GRAVITA     PYRAMID BUY ₹8.63 lakh at ₹194.00 (box jump — doubling the stake with NEW capital; stop stays ₹164.49; charges ₹1,022.95)
2021-08-30  KPITTECH    PYRAMID BUY ₹5.61 lakh at ₹339.50 (box jump — doubling the stake with NEW capital; stop stays ₹278.89; charges ₹664.92)
2021-09-06  HAL         BUY ₹10.09 lakh at ₹705.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.49×, ladder rising; stop ₹500.63; charges ₹1,195.66)
2021-09-06  NHPC        BUY ₹10.11 lakh at ₹27.90 (fresh Friday signal — BUY: 5.07× weekly, month 1.59×, ladder rising; stop ₹24.13; charges ₹1,198.16)
2021-09-06  TDPOWERSYS  BUY ₹10.06 lakh at ₹32.80 (fresh Friday signal — BUY: 2.60× weekly, month 4.52×, ladder rising; stop ₹25.56; charges ₹1,191.38)
2021-09-13  HAL         PYRAMID BUY ₹9.82 lakh at ₹687.02 (box jump — doubling the stake with NEW capital; stop stays ₹636.29; charges ₹1,163.80)
2021-09-13  KEI         PYRAMID BUY ₹7.07 lakh at ₹796.70 (box jump — doubling the stake with NEW capital; stop stays ₹718.20; charges ₹837.26)
2021-09-13  NEOGEN      BUY ₹11.90 lakh at ₹1,165.00 (fresh Friday signal — BUY: 10.32× weekly, month 3.05×, ladder rising; stop ₹841.94; charges ₹1,410.31)
2021-09-13  TATAINVEST  PYRAMID BUY ₹14.75 lakh at ₹128.69 (box jump — doubling the stake with NEW capital; stop stays ₹118.32; charges ₹1,747.13)
2021-09-20  DEEPAKFERT  PYRAMID BUY ₹8.45 lakh at ₹430.00 (box jump — doubling the stake with NEW capital; stop stays ₹385.70; charges ₹1,000.73)
2021-09-20  KEI         PYRAMID BUY ₹15.05 lakh at ₹849.00 (box jump — doubling the stake with NEW capital; stop stays ₹737.39; charges ₹1,783.38)
2021-09-20  NHPC        PYRAMID BUY ₹10.01 lakh at ₹27.65 (box jump — doubling the stake with NEW capital; stop stays ₹25.55; charges ₹1,186.02)
2021-09-20  TDPOWERSYS  PYRAMID BUY ₹9.74 lakh at ₹31.80 (box jump — doubling the stake with NEW capital; stop stays ₹29.75; charges ₹1,153.69)
2021-09-27  NEOGEN      PYRAMID BUY ₹12.81 lakh at ₹1,255.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,035.55; charges ₹1,517.46)
2021-09-27  TATAINVEST  PYRAMID BUY ₹29.98 lakh at ₹130.90 (box jump — doubling the stake with NEW capital; stop stays ₹118.77; charges ₹3,552.29)
2021-10-04  NEOGEN      PYRAMID BUY ₹25.60 lakh at ₹1,255.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,142.85; charges ₹3,033.36)
2021-10-11  KEI         PYRAMID BUY ₹34.86 lakh at ₹983.80 (box jump — doubling the stake with NEW capital; stop stays ₹853.10; charges ₹4,130.62)
2021-10-18  HAL         PYRAMID BUY ₹21.08 lakh at ₹737.50 (box jump — doubling the stake with NEW capital; stop stays ₹636.50; charges ₹2,497.12)
2021-10-18  TATAINVEST  PYRAMID BUY ₹76.96 lakh at ₹168.10 (box jump — doubling the stake with NEW capital; stop stays ₹134.91; charges ₹9,118.21)
2021-10-18  TDPOWERSYS  PYRAMID BUY ₹21.32 lakh at ₹34.84 (box jump — doubling the stake with NEW capital; stop stays ₹30.53; charges ₹2,526.47)
2021-10-22  KEI         SELL ₹60.36 lakh at stop ₹853.10 (-4.1%, charges ₹6,261.56) — the cash goes back to work at the next Friday screen
2021-10-22  TDPOWERSYS  SELL ₹37.31 lakh at stop ₹30.53 (-9.1%, charges ₹3,870.23) — the cash goes back to work at the next Friday screen
2021-10-25  LTM         BUY ₹41.55 lakh at ₹6,555.00 (fresh Friday signal — BUY: 4.63× weekly, month 1.86×, ladder rising; stop ₹5,353.77; charges ₹4,923.51)
2021-10-25  NEOGEN      SELL ₹46.55 lakh at stop ₹1,142.85 (-7.3%, charges ₹4,828.46) — the cash goes back to work at the next Friday screen
2021-10-25  NHPC        PYRAMID BUY ₹23.81 lakh at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹27.60; charges ₹2,820.76)
2021-10-28  HAL         SELL ₹36.32 lakh at stop ₹636.50 (-11.2%, charges ₹3,767.48) — the cash goes back to work at the next Friday screen
2021-11-01  LTM         PYRAMID BUY ₹42.55 lakh at ₹6,720.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,950.99; charges ₹5,041.46)
2021-11-01  PERSISTENT  BUY ₹59.07 lakh at ₹1,977.15 (fresh Friday signal — ACCUMULATE: 1.71× weekly, month 2.09×, ladder rising; stop ₹1,728.75; charges ₹6,998.60)
2021-11-01  TATAINVEST  PYRAMID BUY ₹1.35 crore at ₹148.00 (box jump — doubling the stake with NEW capital; stop stays ₹143.65; charges ₹16,046.34)
2021-11-11  DEEPAKFERT  SELL ₹15.13 lakh at stop ₹385.70 (-3.5%, charges ₹1,569.19) — the cash goes back to work at the next Friday screen
2021-11-15  GOKULAGRO   BUY ₹67.72 lakh at ₹31.05 (fresh Friday signal — BUY: 2.63× weekly, month 1.60×, ladder rising; stop ₹24.87; charges ₹8,023.99)
2021-11-15  GRAVITA     PYRAMID BUY ₹19.55 lakh at ₹219.80 (box jump — doubling the stake with NEW capital; stop stays ₹197.03; charges ₹2,316.61)
2021-11-15  NHPC        PYRAMID BUY ₹46.72 lakh at ₹32.30 (box jump — doubling the stake with NEW capital; stop stays ₹28.69; charges ₹5,535.35)
2021-11-22  GRAVITA     SELL ₹35.00 lakh at stop ₹197.03 (-4.1%, charges ₹3,630.21) — the cash goes back to work at the next Friday screen
2021-11-22  NHPC        PYRAMID BUY ₹95.12 lakh at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹30.11; charges ₹11,269.67)
2021-11-26  TATAINVEST  SELL ₹2.62 crore at stop ₹143.65 (-3.2%, charges ₹27,226.67) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹90.42 lakh at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹10,713.28)
2021-11-29  ESCORTS     BUY ₹90.58 lakh at ₹1,875.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.18×, ladder rising; stop ₹1,369.04; charges ₹10,732.60)
2021-11-29  GOKULAGRO   PYRAMID BUY ₹75.55 lakh at ₹34.68 (box jump — doubling the stake with NEW capital; stop stays ₹26.03; charges ₹8,951.32)
2021-11-29  KPITTECH    PYRAMID BUY ₹15.03 lakh at ₹455.00 (box jump — doubling the stake with NEW capital; stop stays ₹398.63; charges ₹1,781.21)
2021-11-29  LTM         PYRAMID BUY ₹82.65 lakh at ₹6,530.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,270.00; charges ₹9,792.03)
2021-11-29  NHPC        SELL ₹1.74 crore at stop ₹30.11 (-6.2%, charges ₹18,030.20) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹98.60 lakh at ₹209.99 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹158.85; charges ₹11,682.26)
2021-12-06  BSOFT       PYRAMID BUY ₹94.16 lakh at ₹485.00 (box jump — doubling the stake with NEW capital; stop stays ₹424.65; charges ₹11,156.03)
2021-12-06  CHAMBLFERT  BUY ₹98.37 lakh at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹11,655.20)
2021-12-06  PGEL        BUY ₹98.03 lakh at ₹61.77 (fresh Friday signal — BUY: 2.46× weekly, month 1.72×, ladder rising; stop ₹37.43; charges ₹11,614.67)
2021-12-13  ESCORTS     PYRAMID BUY ₹90.19 lakh at ₹1,869.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,739.73; charges ₹10,685.58)
2021-12-13  KPITTECH    PYRAMID BUY ₹33.35 lakh at ₹505.00 (box jump — doubling the stake with NEW capital; stop stays ₹458.85; charges ₹3,951.55)
2021-12-13  PERSISTENT  PYRAMID BUY ₹65.05 lakh at ₹2,180.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,961.89; charges ₹7,707.50)
2021-12-20  KPITTECH    SELL ₹60.51 lakh at stop ₹458.85 (+3.5%, charges ₹6,276.55) — the cash goes back to work at the next Friday screen
2021-12-27  BSE         PYRAMID BUY ₹96.40 lakh at ₹205.56 (box jump — doubling the stake with NEW capital; stop stays ₹181.60; charges ₹11,421.78)
2021-12-27  PERSISTENT  PYRAMID BUY ₹1.38 crore at ₹2,311.50 (box jump — doubling the stake with NEW capital; stop stays ₹2,067.34; charges ₹16,335.16)
2021-12-27  PGEL        PYRAMID BUY ₹1.13 crore at ₹71.00 (box jump — doubling the stake with NEW capital; stop stays ₹56.96; charges ₹13,335.46)
2021-12-27  UNOMINDA    BUY ₹83.12 lakh at ₹590.00 (fresh Friday signal — BUY: 3.66× weekly, month 2.64×, ladder rising; stop ₹464.60; charges ₹9,848.06)
2022-01-03  GABRIEL     PYRAMID BUY ₹60,262.09 at ₹140.00 (box jump — doubling the stake with NEW capital; stop stays ₹125.40; charges ₹71.40)
2022-01-03  UNOMINDA    PYRAMID BUY ₹86.53 lakh at ₹614.92 (box jump — doubling the stake with NEW capital; stop stays ₹544.21; charges ₹10,251.93)
2022-01-07  UNOMINDA    SELL ₹1.53 crore at stop ₹544.21 (-9.7%, charges ₹15,860.79) — the cash goes back to work at the next Friday screen
2022-01-10  AFFLE       BUY ₹1.53 crore at ₹1,307.00 (fresh Friday signal — BUY: 4.57× weekly, month 1.57×, ladder rising; stop ₹955.80; charges ₹18,116.43)
2022-01-10  PGEL        PYRAMID BUY ₹2.68 crore at ₹84.50 (box jump — doubling the stake with NEW capital; stop stays ₹72.44; charges ₹31,723.35)
2022-01-17  AFFLE       PYRAMID BUY ₹1.74 crore at ₹1,493.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,206.50; charges ₹20,670.07)
2022-01-24  ESCORTS     PYRAMID BUY ₹1.80 crore at ₹1,869.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,754.65; charges ₹21,366.50)
2022-01-24  GOKULAGRO   PYRAMID BUY ₹1.65 crore at ₹37.98 (box jump — doubling the stake with NEW capital; stop stays ₹35.00; charges ₹19,597.85)
2022-01-24  LTM         SELL ₹1.58 crore at stop ₹6,270.00 (-4.8%, charges ₹16,436.21) — the cash goes back to work at the next Friday screen
2022-01-24  PERSISTENT  SELL ₹2.46 crore at stop ₹2,067.34 (-5.8%, charges ₹25,539.71) — the cash goes back to work at the next Friday screen
2022-01-24  PGEL        SELL ₹4.58 crore at stop ₹72.44 (-4.0%, charges ₹47,541.76) — the cash goes back to work at the next Friday screen
2022-01-25  AFFLE       SELL ₹2.82 crore at stop ₹1,206.50 (-13.8%, charges ₹29,200.08) — the cash goes back to work at the next Friday screen
2022-01-25  GOKULAGRO   SELL ₹3.04 crore at stop ₹35.00 (-1.2%, charges ₹31,570.64) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹2.30 crore at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹27,238.76)
2022-02-07  CCL         BUY ₹2.58 crore at ₹503.55 (fresh Friday signal — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹30,603.73)
2022-02-07  SHARDACROP  PYRAMID BUY ₹2.58 crore at ₹660.10 (box jump — doubling the stake with NEW capital; stop stays ₹545.30; charges ₹30,610.20)
2022-02-11  SHARDACROP  SELL ₹4.26 crore at stop ₹545.30 (-12.5%, charges ₹44,204.49) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹1.65 crore at stop ₹424.65 (-10.6%, charges ₹17,075.51) — the cash goes back to work at the next Friday screen
2022-02-14  CCL         PYRAMID BUY ₹2.38 crore at ₹465.00 (box jump — doubling the stake with NEW capital; stop stays ₹441.75; charges ₹28,227.34)
2022-02-14  CHAMBLFERT  PYRAMID BUY ₹92.70 lakh at ₹384.40 (box jump — doubling the stake with NEW capital; stop stays ₹353.85; charges ₹10,982.82)
2022-02-14  GABRIEL     SELL ₹1.08 lakh at stop ₹125.40 (-9.1%, charges ₹111.80) — the cash goes back to work at the next Friday screen
2022-02-14  GNFC        BUY ₹2.78 crore at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹32,939.25)
2022-02-21  ADANIPOWER  BUY ₹3.05 crore at ₹26.40 (fresh Friday signal — BUY: 8.22× weekly, month 2.70×, ladder rising; stop ₹18.02; charges ₹36,112.19)
2022-02-21  CGCL        BUY ₹3.02 crore at ₹567.08 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹507.72; charges ₹35,784.11)
2022-02-21  GNFC        PYRAMID BUY ₹2.75 crore at ₹548.00 (box jump — doubling the stake with NEW capital; stop stays ₹497.80; charges ₹32,602.75)
2022-02-24  CCL         SELL ₹4.52 crore at stop ₹441.75 (-8.8%, charges ₹46,877.89) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹1.70 crore at stop ₹353.85 (-10.6%, charges ₹17,673.56) — the cash goes back to work at the next Friday screen
2022-02-25  ESCORTS     SELL ₹3.38 crore at stop ₹1,754.65 (-6.2%, charges ₹35,053.11) — the cash goes back to work at the next Friday screen
2022-03-07  ADANIPOWER  PYRAMID BUY ₹2.68 crore at ₹23.20 (box jump — doubling the stake with NEW capital; stop stays ₹20.00; charges ₹31,697.35)
2022-04-01  TAX         FY2022 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹3.05 crore / LT ₹0.00)
2022-04-04  RCF         BUY ₹4.09 crore at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹48,420.22)
2022-04-04  SPLPETRO    BUY ₹4.11 crore at ₹475.00 (fresh Friday signal — BUY: 4.41× weekly, month 2.84×, ladder rising; stop ₹398.29; charges ₹48,657.80)
2022-04-11  BLS         BUY ₹4.58 crore at ₹82.50 (fresh Friday signal — BUY: 8.78× weekly, month 1.73×, ladder rising; stop ₹54.82; charges ₹54,300.09)
2022-04-11  MINDACORP   BUY ₹3.50 crore at ₹230.05 (fresh Friday signal — BUY: 2.10× weekly, month 1.60×, ladder rising; stop ₹186.63; charges ₹41,497.95)
2022-04-11  SPLPETRO    PYRAMID BUY ₹3.98 crore at ₹460.65 (box jump — doubling the stake with NEW capital; stop stays ₹424.27; charges ₹47,131.91)
2022-04-25  ADANIPOWER  PYRAMID BUY ₹12.14 crore at ₹52.68 (box jump — doubling the stake with NEW capital; stop stays ₹40.22; charges ₹1.44 lakh)
2022-04-25  BLS         PYRAMID BUY ₹4.57 crore at ₹82.42 (box jump — doubling the stake with NEW capital; stop stays ₹75.36; charges ₹54,186.45)
2022-04-25  GNFC        PYRAMID BUY ₹8.50 crore at ₹846.40 (box jump — doubling the stake with NEW capital; stop stays ₹792.16; charges ₹1.01 lakh)
2022-04-25  RCF         PYRAMID BUY ₹4.41 crore at ₹104.20 (box jump — doubling the stake with NEW capital; stop stays ₹93.15; charges ₹52,276.03)
2022-05-02  BSE         PYRAMID BUY ₹2.78 crore at ₹296.70 (box jump — doubling the stake with NEW capital; stop stays ₹255.87; charges ₹32,952.97)
2022-05-04  RCF         SELL ₹7.88 crore at stop ₹93.15 (-7.1%, charges ₹81,694.39) — the cash goes back to work at the next Friday screen
2022-05-06  GNFC        SELL ₹15.88 crore at stop ₹792.16 (+13.4%, charges ₹1.65 lakh) — the cash goes back to work at the next Friday screen
2022-05-09  MRPL        BUY ₹7.88 crore at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹93,363.96)
2022-05-10  BSE         SELL ₹4.79 crore at stop ₹255.87 (+1.5%, charges ₹49,678.79) — the cash goes back to work at the next Friday screen
2022-05-11  MINDACORP   SELL ₹2.84 crore at stop ₹186.63 (-18.9%, charges ₹29,408.50) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹7.60 crore at ₹146.67 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.79×, ladder rising; stop ₹130.85; charges ₹90,044.11)
2022-05-23  ACC         BUY ₹9.35 crore at ₹2,260.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹1.11 lakh)
2022-05-23  MRPL        PYRAMID BUY ₹9.57 crore at ₹94.80 (box jump — doubling the stake with NEW capital; stop stays ₹60.81; charges ₹1.13 lakh)
2022-05-24  SPLPETRO    SELL ₹7.32 crore at stop ₹424.27 (-9.3%, charges ₹75,885.86) — the cash goes back to work at the next Friday screen
2022-06-06  MRPL        PYRAMID BUY ₹17.82 crore at ₹88.35 (box jump — doubling the stake with NEW capital; stop stays ₹69.61; charges ₹2.11 lakh)
2022-06-13  ELECON      BUY ₹12.15 crore at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹1.44 lakh)
2022-06-13  VBL         PYRAMID BUY ₹7.75 crore at ₹149.70 (box jump — doubling the stake with NEW capital; stop stays ₹136.81; charges ₹91,797.47)
2022-06-20  BLS         PYRAMID BUY ₹11.77 crore at ₹106.12 (box jump — doubling the stake with NEW capital; stop stays ₹83.17; charges ₹1.39 lakh)
2022-06-20  ELECON      PYRAMID BUY ₹13.01 crore at ₹131.25 (box jump — doubling the stake with NEW capital; stop stays ₹111.01; charges ₹1.54 lakh)
2022-06-27  ADANIPOWER  PYRAMID BUY ₹24.97 crore at ₹54.19 (box jump — doubling the stake with NEW capital; stop stays ₹43.79; charges ₹2.96 lakh)
2022-06-27  VBL         PYRAMID BUY ₹16.14 crore at ₹155.98 (box jump — doubling the stake with NEW capital; stop stays ₹136.99; charges ₹1.91 lakh)
2022-07-04  BLS         PYRAMID BUY ₹21.61 crore at ₹97.47 (box jump — doubling the stake with NEW capital; stop stays ₹90.53; charges ₹2.56 lakh)
2022-07-06  MRPL        SELL ₹28.03 crore at stop ₹69.61 (-20.3%, charges ₹2.91 lakh) — the cash goes back to work at the next Friday screen
2022-07-11  ELECON      PYRAMID BUY ₹29.11 crore at ₹147.00 (box jump — doubling the stake with NEW capital; stop stays ₹120.65; charges ₹3.45 lakh)
2022-07-18  ACC         PYRAMID BUY ₹8.93 crore at ₹2,160.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,030.05; charges ₹1.06 lakh)
2022-07-25  ELECON      PYRAMID BUY ₹65.70 crore at ₹165.95 (box jump — doubling the stake with NEW capital; stop stays ₹142.64; charges ₹7.78 lakh)
2022-07-25  TIINDIA     BUY ₹29.75 crore at ₹2,135.00 (fresh Friday signal — BUY: 4.17× weekly, month 2.43×, ladder rising; stop ₹1,862.00; charges ₹3.52 lakh)
2022-08-01  VBL         PYRAMID BUY ₹36.88 crore at ₹178.36 (box jump — doubling the stake with NEW capital; stop stays ₹162.49; charges ₹4.37 lakh)
2022-08-08  ACC         PYRAMID BUY ₹18.66 crore at ₹2,260.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,053.90; charges ₹2.21 lakh)
2022-08-08  BLS         PYRAMID BUY ₹52.40 crore at ₹118.25 (box jump — doubling the stake with NEW capital; stop stays ₹110.67; charges ₹6.21 lakh)
2022-08-08  TIINDIA     PYRAMID BUY ₹31.62 crore at ₹2,272.15 (box jump — doubling the stake with NEW capital; stop stays ₹1,867.30; charges ₹3.75 lakh)
2022-08-16  ACC         PYRAMID BUY ₹37.10 crore at ₹2,248.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,085.11; charges ₹4.40 lakh)
2022-08-16  ADANIPOWER  PYRAMID BUY ₹64.28 crore at ₹69.80 (box jump — doubling the stake with NEW capital; stop stays ₹61.19; charges ₹7.62 lakh)
2022-08-16  ELECON      PYRAMID BUY ₹135.31 crore at ₹171.00 (box jump — doubling the stake with NEW capital; stop stays ₹156.67; charges ₹16.03 lakh)
2022-08-16  VBL         PYRAMID BUY ₹85.14 crore at ₹206.00 (box jump — doubling the stake with NEW capital; stop stays ₹188.52; charges ₹10.09 lakh)
2022-08-22  VBL         SELL ₹155.58 crore at stop ₹188.52 (+1.6%, charges ₹16.14 lakh) — the cash goes back to work at the next Friday screen
2022-08-23  BLS         SELL ₹97.92 crore at stop ₹110.67 (+3.4%, charges ₹10.16 lakh) — the cash goes back to work at the next Friday screen
2022-08-29  ACC         PYRAMID BUY ₹75.00 crore at ₹2,274.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,151.37; charges ₹8.89 lakh)
2022-08-29  HOMEFIRST   BUY ₹90.18 crore at ₹944.95 (fresh Friday signal — ACCUMULATE: 3.67× weekly, month 2.49×, ladder rising; stop ₹849.35; charges ₹10.69 lakh)
2022-08-29  KALYANKJIL  BUY ₹90.29 crore at ₹78.10 (fresh Friday signal — BUY: 9.54× weekly, month 2.93×, ladder rising; stop ₹65.55; charges ₹10.70 lakh)
2022-08-29  SIEMENS     BUY ₹73.03 crore at ₹1,688.21 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 1.62×, ladder rising; stop ₹1,573.13; charges ₹8.65 lakh)
2022-09-05  ADANIPOWER  PYRAMID BUY ₹148.60 crore at ₹80.73 (box jump — doubling the stake with NEW capital; stop stays ₹66.80; charges ₹17.61 lakh)
2022-09-05  KALYANKJIL  PYRAMID BUY ₹97.74 crore at ₹84.65 (box jump — doubling the stake with NEW capital; stop stays ₹73.15; charges ₹11.58 lakh)
2022-09-14  HOMEFIRST   SELL ₹80.88 crore at stop ₹849.35 (-10.1%, charges ₹8.39 lakh) — the cash goes back to work at the next Friday screen
2022-09-19  KALYANKJIL  PYRAMID BUY ₹219.49 crore at ₹95.10 (box jump — doubling the stake with NEW capital; stop stays ₹76.00; charges ₹26.01 lakh)
2022-09-19  MAHSCOOTER  BUY ₹80.88 crore at ₹5,103.50 (fresh Friday signal — BUY: 10.17× weekly, month 2.61×, ladder rising; stop ₹3,847.79; charges ₹9.58 lakh)
2022-09-19  SIEMENS     PYRAMID BUY ₹75.05 crore at ₹1,737.02 (box jump — doubling the stake with NEW capital; stop stays ₹1,618.44; charges ₹8.89 lakh)
2022-09-26  SIEMENS     SELL ₹139.62 crore at stop ₹1,618.44 (-5.5%, charges ₹14.48 lakh) — the cash goes back to work at the next Friday screen
2022-09-26  TIINDIA     PYRAMID BUY ₹76.16 crore at ₹2,737.75 (box jump — doubling the stake with NEW capital; stop stays ₹2,360.75; charges ₹9.02 lakh)
2022-10-03  ACC         PYRAMID BUY ₹159.53 crore at ₹2,419.80 (box jump — doubling the stake with NEW capital; stop stays ₹2,171.53; charges ₹18.90 lakh)
2022-10-03  KALYANKJIL  PYRAMID BUY ₹447.02 crore at ₹96.90 (box jump — doubling the stake with NEW capital; stop stays ₹81.12; charges ₹52.96 lakh)
2022-10-03  MAHSCOOTER  PYRAMID BUY ₹79.11 crore at ₹4,998.05 (box jump — doubling the stake with NEW capital; stop stays ₹4,617.00; charges ₹9.37 lakh)
2022-10-03  TSFINV      BUY ₹139.62 crore at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹16.54 lakh)
2022-10-10  TSFINV      PYRAMID BUY ₹134.00 crore at ₹99.45 (box jump — doubling the stake with NEW capital; stop stays ₹92.20; charges ₹15.88 lakh)
2022-10-11  TSFINV      SELL ₹248.06 crore at stop ₹92.20 (-9.1%, charges ₹25.73 lakh) — the cash goes back to work at the next Friday screen
2022-10-14  ADANIPOWER  SELL ₹245.51 crore at stop ₹66.80 (-3.8%, charges ₹25.47 lakh) — the cash goes back to work at the next Friday screen
2022-10-17  APOLLO      BUY ₹232.62 crore at ₹24.00 (fresh Friday signal — BUY: 6.98× weekly, month 4.78×, ladder rising; stop ₹14.17; charges ₹27.56 lakh)
2022-10-24  GODFRYPHLP  BUY ₹260.95 crore at ₹483.67 (fresh Friday signal — BUY: 4.48× weekly, month 3.07×, ladder rising; stop ₹403.15; charges ₹30.92 lakh)
2022-10-24  KALYANKJIL  PYRAMID BUY ₹939.15 crore at ₹101.85 (box jump — doubling the stake with NEW capital; stop stays ₹89.78; charges ₹1.11 crore)
2022-10-31  APOLLO      PYRAMID BUY ₹210.12 crore at ₹21.70 (box jump — doubling the stake with NEW capital; stop stays ₹19.45; charges ₹24.90 lakh)
2022-10-31  KALYANKJIL  PYRAMID BUY ₹1,948.14 crore at ₹105.70 (box jump — doubling the stake with NEW capital; stop stays ₹94.53; charges ₹2.31 crore)
2022-10-31  TIINDIA     PYRAMID BUY ₹148.74 crore at ₹2,675.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,465.49; charges ₹17.62 lakh)
2022-11-07  ELECON      PYRAMID BUY ₹317.68 crore at ₹200.85 (box jump — doubling the stake with NEW capital; stop stays ₹164.33; charges ₹37.64 lakh)
2022-11-14  CGCL        PYRAMID BUY ₹3.70 crore at ₹696.24 (box jump — doubling the stake with NEW capital; stop stays ₹661.39; charges ₹43,882.71)
2022-11-21  ACC         PYRAMID BUY ₹323.21 crore at ₹2,452.70 (box jump — doubling the stake with NEW capital; stop stays ₹2,259.81; charges ₹38.29 lakh)
2022-11-21  ELECON      PYRAMID BUY ₹674.81 crore at ₹213.45 (box jump — doubling the stake with NEW capital; stop stays ₹202.49; charges ₹79.95 lakh)
2022-11-21  GODFRYPHLP  PYRAMID BUY ₹330.52 crore at ₹613.33 (box jump — doubling the stake with NEW capital; stop stays ₹497.48; charges ₹39.16 lakh)
2022-11-22  KALYANKJIL  SELL ₹3,478.86 crore at stop ₹94.53 (-6.8%, charges ₹3.61 crore) — the cash goes back to work at the next Friday screen
2022-11-28  IOB         BUY ₹716.88 crore at ₹23.00 (fresh Friday signal — BUY: 7.22× weekly, month 5.74×, ladder rising; stop ₹18.76; charges ₹84.94 lakh)
2022-11-28  IRFC        BUY ₹714.38 crore at ₹32.00 (fresh Friday signal — BUY: 9.02× weekly, month 13.28×, ladder rising; stop ₹23.09; charges ₹84.64 lakh)
2022-11-28  MAHABANK    BUY ₹717.75 crore at ₹27.60 (fresh Friday signal — BUY: 8.71× weekly, month 8.20×, ladder rising; stop ₹21.47; charges ₹85.04 lakh)
2022-11-28  SKIPPER     BUY ₹614.20 crore at ₹89.34 (fresh Friday signal — BUY: 6.40× weekly, month 2.23×, ladder rising; stop ₹65.34; charges ₹72.77 lakh)
2022-11-28  UCOBANK     BUY ₹715.65 crore at ₹21.05 (fresh Friday signal — BUY: 13.59× weekly, month 16.04×, ladder rising; stop ₹13.59; charges ₹84.79 lakh)
2022-12-05  GODFRYPHLP  PYRAMID BUY ₹657.05 crore at ₹610.00 (box jump — doubling the stake with NEW capital; stop stays ₹547.85; charges ₹77.85 lakh)
2022-12-05  IOB         PYRAMID BUY ₹716.03 crore at ₹23.00 (box jump — doubling the stake with NEW capital; stop stays ₹20.76; charges ₹84.84 lakh)
2022-12-12  APOLLO      PYRAMID BUY ₹499.35 crore at ₹25.80 (box jump — doubling the stake with NEW capital; stop stays ₹24.42; charges ₹59.16 lakh)
2022-12-12  UCOBANK     PYRAMID BUY ₹801.39 crore at ₹23.60 (box jump — doubling the stake with NEW capital; stop stays ₹18.29; charges ₹94.95 lakh)
2022-12-19  ACC         PYRAMID BUY ₹688.24 crore at ₹2,612.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,465.15; charges ₹81.54 lakh)
2022-12-19  IRFC        PYRAMID BUY ₹720.22 crore at ₹32.30 (box jump — doubling the stake with NEW capital; stop stays ₹28.20; charges ₹85.33 lakh)
2022-12-19  SKIPPER     PYRAMID BUY ₹834.51 crore at ₹121.53 (box jump — doubling the stake with NEW capital; stop stays ₹109.70; charges ₹98.87 lakh)
2022-12-21  ELECON      SELL ₹1,278.24 crore at stop ₹202.49 (+2.7%, charges ₹1.33 crore) — the cash goes back to work at the next Friday screen
2022-12-22  MAHSCOOTER  SELL ₹145.93 crore at stop ₹4,617.00 (-8.6%, charges ₹15.14 lakh) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹1,296.51 crore at stop ₹2,465.15 (-1.6%, charges ₹1.34 crore) — the cash goes back to work at the next Friday screen
2022-12-23  IRFC        SELL ₹1,255.55 crore at stop ₹28.20 (-12.3%, charges ₹1.30 crore) — the cash goes back to work at the next Friday screen
2022-12-26  APOLLO      SELL ₹943.74 crore at stop ₹24.42 (+0.4%, charges ₹97.89 lakh) — the cash goes back to work at the next Friday screen
2022-12-26  GODFRYPHLP  SELL ₹1,178.30 crore at stop ₹547.85 (-5.4%, charges ₹1.22 crore) — the cash goes back to work at the next Friday screen
2022-12-26  TIINDIA     PYRAMID BUY ₹308.76 crore at ₹2,778.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,598.35; charges ₹36.58 lakh)
2023-01-02  GICRE       BUY ₹1,828.77 crore at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 11.13×, ladder rising; stop ₹137.57; charges ₹2.17 crore)
2023-01-02  IOB         PYRAMID BUY ₹2,016.15 crore at ₹32.40 (box jump — doubling the stake with NEW capital; stop stays ₹21.23; charges ₹2.39 crore)
2023-01-02  LLOYDSENGG  BUY ₹1,837.32 crore at ₹15.63 (fresh Friday signal — ACCUMULATE: 2.36× weekly, month 2.74×, ladder rising; stop ₹10.86; charges ₹2.18 crore)
2023-01-02  MAHABANK    PYRAMID BUY ₹801.31 crore at ₹30.85 (box jump — doubling the stake with NEW capital; stop stays ₹22.08; charges ₹94.94 lakh)
2023-01-02  UCOBANK     PYRAMID BUY ₹2,158.41 crore at ₹31.80 (box jump — doubling the stake with NEW capital; stop stays ₹23.46; charges ₹2.56 crore)
2023-01-02  YESBANK     BUY ₹1,822.01 crore at ₹20.85 (fresh Friday signal — ACCUMULATE: 2.89× weekly, month 3.19×, ladder rising; stop ₹15.00; charges ₹2.16 crore)
2023-01-09  CGCL        PYRAMID BUY ₹7.59 crore at ₹714.12 (box jump — doubling the stake with NEW capital; stop stays ₹666.82; charges ₹89,965.69)
2023-01-11  TIINDIA     SELL ₹576.64 crore at stop ₹2,598.35 (-2.9%, charges ₹59.82 lakh) — the cash goes back to work at the next Friday screen
2023-01-16  ANUP        BUY ₹1,186.80 crore at ₹476.12 (fresh Friday signal — ACCUMULATE: 4.79× weekly, month 1.56×, ladder rising; stop ₹364.75; charges ₹1.41 crore)
2023-01-16  GICRE       PYRAMID BUY ₹1,906.62 crore at ₹187.05 (box jump — doubling the stake with NEW capital; stop stays ₹167.72; charges ₹2.26 crore)
2023-01-25  SKIPPER     SELL ₹1,504.05 crore at stop ₹109.70 (+4.1%, charges ₹1.56 crore) — the cash goes back to work at the next Friday screen
2023-02-01  GICRE       SELL ₹3,413.61 crore at stop ₹167.72 (-8.4%, charges ₹3.54 crore) — the cash goes back to work at the next Friday screen
2023-02-06  ANUP        PYRAMID BUY ₹1,399.44 crore at ₹562.10 (box jump — doubling the stake with NEW capital; stop stays ₹466.90; charges ₹1.66 crore)
2023-02-06  JINDALSAW   BUY ₹2,237.53 crore at ₹65.22 (fresh Friday signal — BUY: 2.71× weekly, month 3.60×, ladder rising; stop ₹51.25; charges ₹2.65 crore)
2023-02-06  LLOYDSENGG  PYRAMID BUY ₹2,467.56 crore at ₹21.02 (box jump — doubling the stake with NEW capital; stop stays ₹19.27; charges ₹2.92 crore)
2023-02-07  LLOYDSENGG  SELL ₹4,517.37 crore at stop ₹19.27 (+5.2%, charges ₹4.69 crore) — the cash goes back to work at the next Friday screen
2023-02-13  ANUP        PYRAMID BUY ₹2,836.54 crore at ₹570.00 (box jump — doubling the stake with NEW capital; stop stays ₹518.77; charges ₹3.36 crore)
2023-02-13  YESBANK     PYRAMID BUY ₹1,488.17 crore at ₹17.05 (box jump — doubling the stake with NEW capital; stop stays ₹15.34; charges ₹1.76 crore)
2023-02-20  ANUP        PYRAMID BUY ₹5,595.37 crore at ₹562.52 (box jump — doubling the stake with NEW capital; stop stays ₹527.27; charges ₹6.63 crore)
2023-02-27  CERA        BUY ₹3,160.08 crore at ₹6,150.00 (fresh Friday signal — BUY: 5.94× weekly, month 1.75×, ladder rising; stop ₹5,579.40; charges ₹3.74 crore)
2023-02-27  SONATSOFTW  BUY ₹3,160.45 crore at ₹360.00 (fresh Friday signal — BUY: 9.70× weekly, month 3.34×, ladder rising; stop ₹282.62; charges ₹3.74 crore)
2023-03-06  CERA        PYRAMID BUY ₹3,251.02 crore at ₹6,334.50 (box jump — doubling the stake with NEW capital; stop stays ₹5,714.25; charges ₹3.85 crore)
2023-03-06  IOB         PYRAMID BUY ₹3,246.32 crore at ₹26.10 (box jump — doubling the stake with NEW capital; stop stays ₹22.18; charges ₹3.85 crore)
2023-03-06  JINDALSAW   PYRAMID BUY ₹2,534.69 crore at ₹73.97 (box jump — doubling the stake with NEW capital; stop stays ₹67.92; charges ₹3.00 crore)
2023-03-06  SONATSOFTW  PYRAMID BUY ₹3,514.03 crore at ₹400.75 (box jump — doubling the stake with NEW capital; stop stays ₹325.85; charges ₹4.16 crore)
2023-03-08  CGCL        SELL ₹14.16 crore at stop ₹666.82 (-0.9%, charges ₹1.47 lakh) — the cash goes back to work at the next Friday screen
2023-03-10  ANUP        SELL ₹10,472.32 crore at stop ₹527.27 (-4.7%, charges ₹10.86 crore) — the cash goes back to work at the next Friday screen
2023-03-13  YESBANK     SELL ₹2,673.48 crore at stop ₹15.34 (-19.1%, charges ₹2.77 crore) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹4,974.43 crore at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.60×, ladder rising; stop ₹691.46; charges ₹5.89 crore)
2023-03-20  IOB         SELL ₹5,508.52 crore at stop ₹22.18 (-17.5%, charges ₹5.71 crore) — the cash goes back to work at the next Friday screen
2023-03-20  SONATSOFTW  PYRAMID BUY ₹6,966.93 crore at ₹397.50 (box jump — doubling the stake with NEW capital; stop stays ₹357.20; charges ₹8.25 crore)
2023-03-27  CERA        PYRAMID BUY ₹6,452.39 crore at ₹6,289.85 (box jump — doubling the stake with NEW capital; stop stays ₹5,852.00; charges ₹7.64 crore)
2023-03-27  JINDALSAW   SELL ₹4,646.87 crore at stop ₹67.92 (-2.4%, charges ₹4.82 crore) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹7,015.49 crore at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.85×, ladder rising; stop ₹372.21; charges ₹8.31 crore)
2023-03-27  MAHABANK    PYRAMID BUY ₹1,266.81 crore at ₹24.40 (box jump — doubling the stake with NEW capital; stop stays ₹22.36; charges ₹1.50 crore)
2023-03-27  SONATSOFTW  PYRAMID BUY ₹14,493.14 crore at ₹413.70 (box jump — doubling the stake with NEW capital; stop stays ₹371.45; charges ₹17.17 crore)
2023-03-27  TDPOWERSYS  BUY ₹7,002.31 crore at ₹84.62 (fresh Friday signal — BUY: 1.62× weekly, month 2.13×, ladder rising; stop ₹64.12; charges ₹8.30 crore)
2023-03-27  UCOBANK     SELL ₹3,179.48 crore at stop ₹23.46 (-13.3%, charges ₹3.30 crore) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹25,983.62 crore at stop ₹371.45 (-7.4%, charges ₹26.95 crore) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹6,962.66 crore at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.04×, ladder rising; stop ₹1,171.71; charges ₹8.25 crore)
2023-04-03  TAX         FY2023 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹5,621.45 crore / LT ₹0.00)
2023-04-10  CERA        PYRAMID BUY ₹13,405.95 crore at ₹6,538.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,037.30; charges ₹15.88 crore)
2023-04-10  KIRLOSBROS  BUY ₹8,956.47 crore at ₹425.00 (fresh Friday signal — BUY: 1.86× weekly, month 2.34×, ladder rising; stop ₹357.44; charges ₹10.61 crore)
2023-04-10  TDPOWERSYS  PYRAMID BUY ₹6,566.31 crore at ₹79.45 (box jump — doubling the stake with NEW capital; stop stays ₹73.22; charges ₹7.78 crore)
2023-04-24  KIRLOSBROS  PYRAMID BUY ₹9,100.57 crore at ₹432.35 (box jump — doubling the stake with NEW capital; stop stays ₹403.85; charges ₹10.78 crore)
2023-04-24  MARKSANS    BUY ₹8,321.91 crore at ₹78.00 (fresh Friday signal — ACCUMULATE: 1.64× weekly, month 1.51×, ladder rising; stop ₹71.87; charges ₹9.86 crore)
2023-04-24  ZFCVINDIA   BUY ₹10,122.14 crore at ₹1,697.50 (fresh Friday signal — ACCUMULATE: 7.38× weekly, month 1.55×, ladder rising; stop ₹1,561.17; charges ₹11.99 crore)
2023-04-26  CERA        SELL ₹24,718.26 crore at stop ₹6,037.30 (-5.7%, charges ₹25.64 crore) — the cash goes back to work at the next Friday screen
2023-04-26  KIRLOSBROS  SELL ₹16,973.66 crore at stop ₹403.85 (-5.8%, charges ₹17.61 crore) — the cash goes back to work at the next Friday screen
2023-05-02  ANURAS      PYRAMID BUY ₹7,486.66 crore at ₹1,139.00 (box jump — doubling the stake with NEW capital; stop stays ₹946.20; charges ₹8.87 crore)
2023-05-02  ASHAPURMIN  BUY ₹11,593.23 crore at ₹143.10 (fresh Friday signal — BUY: 2.05× weekly, month 2.10×, ladder rising; stop ₹123.50; charges ₹13.74 crore)
2023-05-02  ICICIBANK   BUY ₹11,589.02 crore at ₹924.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.24×, ladder rising; stop ₹838.28; charges ₹13.73 crore)
2023-05-02  KSB         PYRAMID BUY ₹7,600.98 crore at ₹453.40 (box jump — doubling the stake with NEW capital; stop stays ₹407.74; charges ₹9.01 crore)
2023-05-02  REFEX       BUY ₹11,636.24 crore at ₹65.32 (fresh Friday signal — BUY: 4.73× weekly, month 1.57×, ladder rising; stop ₹54.53; charges ₹13.79 crore)
2023-05-08  HEG         BUY ₹6,873.42 crore at ₹234.38 (fresh Friday signal — BUY: 2.69× weekly, month 1.85×, ladder rising; stop ₹201.01; charges ₹8.14 crore)
2023-05-08  MAHABANK    PYRAMID BUY ₹3,175.52 crore at ₹30.60 (box jump — doubling the stake with NEW capital; stop stays ₹27.79; charges ₹3.76 crore)
2023-05-15  ANURAS      PYRAMID BUY ₹15,369.11 crore at ₹1,169.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,007.67; charges ₹18.21 crore)
2023-05-15  ASHAPURMIN  PYRAMID BUY ₹11,725.15 crore at ₹144.90 (box jump — doubling the stake with NEW capital; stop stays ₹125.16; charges ₹13.89 crore)
2023-05-15  HAL         PYRAMID BUY ₹7,526.26 crore at ₹1,493.47 (box jump — doubling the stake with NEW capital; stop stays ₹1,370.80; charges ₹8.92 crore)
2023-05-15  REFEX       PYRAMID BUY ₹12,962.28 crore at ₹72.85 (box jump — doubling the stake with NEW capital; stop stays ₹58.14; charges ₹15.36 crore)
2023-05-22  MARKSANS    SELL ₹7,650.87 crore at stop ₹71.87 (-7.9%, charges ₹7.94 crore) — the cash goes back to work at the next Friday screen
2023-05-29  ASHAPURMIN  PYRAMID BUY ₹21,010.27 crore at ₹129.90 (box jump — doubling the stake with NEW capital; stop stays ₹134.24; charges ₹24.89 crore)
2023-05-29  ASHAPURMIN  SELL ₹43,353.77 crore at stop ₹134.24 (-2.0%, charges ₹44.97 crore) — the cash goes back to work at the next Friday screen
2023-05-29  TDPOWERSYS  PYRAMID BUY ₹16,850.02 crore at ₹102.00 (box jump — doubling the stake with NEW capital; stop stays ₹89.54; charges ₹19.96 crore)
2023-06-05  EPL         BUY ₹22,370.66 crore at ₹201.90 (fresh Friday signal — ACCUMULATE: 6.59× weekly, month 6.26×, ladder rising; stop ₹170.76; charges ₹26.51 crore)
2023-06-05  FORCEMOT    BUY ₹28,633.98 crore at ₹1,951.00 (fresh Friday signal — BUY: 23.21× weekly, month 3.12×, ladder rising; stop ₹1,289.01; charges ₹33.93 crore)
2023-06-05  HAL         PYRAMID BUY ₹16,034.78 crore at ₹1,591.88 (box jump — doubling the stake with NEW capital; stop stays ₹1,415.36; charges ₹19.00 crore)
2023-06-05  ICICIBANK   PYRAMID BUY ₹11,813.31 crore at ₹943.00 (box jump — doubling the stake with NEW capital; stop stays ₹886.30; charges ₹14.00 crore)
2023-06-05  REFEX       PYRAMID BUY ₹37,428.74 crore at ₹105.24 (box jump — doubling the stake with NEW capital; stop stays ₹87.60; charges ₹44.35 crore)
2023-06-12  HEG         PYRAMID BUY ₹8,001.78 crore at ₹273.18 (box jump — doubling the stake with NEW capital; stop stays ₹211.53; charges ₹9.48 crore)
2023-06-15  MAHABANK    SELL ₹5,758.43 crore at stop ₹27.79 (-3.2%, charges ₹5.97 crore) — the cash goes back to work at the next Friday screen
2023-06-19  FORCEMOT    PYRAMID BUY ₹32,660.65 crore at ₹2,228.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,995.52; charges ₹38.70 crore)
2023-06-19  HAL         PYRAMID BUY ₹39,250.92 crore at ₹1,949.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,723.32; charges ₹46.51 crore)
2023-06-19  ZFCVINDIA   PYRAMID BUY ₹11,990.23 crore at ₹2,013.17 (box jump — doubling the stake with NEW capital; stop stays ₹1,773.33; charges ₹14.21 crore)
2023-06-26  ZFCVINDIA   PYRAMID BUY ₹24,325.37 crore at ₹2,043.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,860.58; charges ₹28.82 crore)
2023-07-03  ANURAS      SELL ₹26,434.90 crore at stop ₹1,007.67 (-4.8%, charges ₹27.42 crore) — the cash goes back to work at the next Friday screen
2023-07-03  EPL         PYRAMID BUY ₹23,793.92 crore at ₹215.00 (box jump — doubling the stake with NEW capital; stop stays ₹189.81; charges ₹28.19 crore)
2023-07-03  HEG         PYRAMID BUY ₹19,144.53 crore at ₹326.99 (box jump — doubling the stake with NEW capital; stop stays ₹294.79; charges ₹22.68 crore)
2023-07-03  TDPOWERSYS  PYRAMID BUY ₹40,911.39 crore at ₹123.90 (box jump — doubling the stake with NEW capital; stop stays ₹101.58; charges ₹48.47 crore)
2023-07-10  CEATLTD     BUY ₹32,193.33 crore at ₹2,408.00 (fresh Friday signal — BUY: 4.55× weekly, month 2.41×, ladder rising; stop ₹1,892.78; charges ₹38.14 crore)
2023-07-10  EPL         PYRAMID BUY ₹47,968.88 crore at ₹216.85 (box jump — doubling the stake with NEW capital; stop stays ₹200.50; charges ₹56.83 crore)
2023-07-10  ZFCVINDIA   PYRAMID BUY ₹47,775.60 crore at ₹2,007.77 (box jump — doubling the stake with NEW capital; stop stays ₹1,882.66; charges ₹56.61 crore)
2023-07-12  KSB         SELL ₹13,648.77 crore at stop ₹407.74 (-6.4%, charges ₹14.16 crore) — the cash goes back to work at the next Friday screen
2023-07-17  FORCEMOT    PYRAMID BUY ₹81,280.95 crore at ₹2,774.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,337.00; charges ₹96.30 crore)
2023-07-17  TDPOWERSYS  PYRAMID BUY ₹82,203.30 crore at ₹124.55 (box jump — doubling the stake with NEW capital; stop stays ₹110.20; charges ₹97.40 crore)
2023-07-24  ICICIBANK   PYRAMID BUY ₹25,163.85 crore at ₹1,004.95 (box jump — doubling the stake with NEW capital; stop stays ₹894.19; charges ₹29.81 crore)
2023-07-24  TDPOWERSYS  PYRAMID BUY ₹1.68 lakh crore at ₹127.42 (box jump — doubling the stake with NEW capital; stop stays ₹112.05; charges ₹199.17 crore)
2023-07-31  CEATLTD     PYRAMID BUY ₹32,744.08 crore at ₹2,452.10 (box jump — doubling the stake with NEW capital; stop stays ₹2,244.85; charges ₹38.80 crore)
2023-07-31  HEG         PYRAMID BUY ₹39,664.85 crore at ₹338.94 (box jump — doubling the stake with NEW capital; stop stays ₹300.49; charges ₹47.00 crore)
2023-07-31  REFEX       PYRAMID BUY ₹1.20 lakh crore at ₹169.00 (box jump — doubling the stake with NEW capital; stop stays ₹121.69; charges ₹142.34 crore)
2023-08-11  EPL         SELL ₹88,559.86 crore at stop ₹200.50 (-5.7%, charges ₹91.86 crore) — the cash goes back to work at the next Friday screen
2023-08-11  REFEX       SELL ₹1.73 lakh crore at stop ₹121.69 (-5.0%, charges ₹179.18 crore) — the cash goes back to work at the next Friday screen
2023-08-14  CEATLTD     SELL ₹59,855.53 crore at stop ₹2,244.85 (-7.6%, charges ₹62.09 crore) — the cash goes back to work at the next Friday screen
2023-08-14  HAL         PYRAMID BUY ₹76,158.42 crore at ₹1,892.42 (box jump — doubling the stake with NEW capital; stop stays ₹1,758.24; charges ₹90.23 crore)
2023-08-14  RATEGAIN    BUY ₹1.35 lakh crore at ₹547.00 (fresh Friday signal — BUY: 5.36× weekly, month 1.91×, ladder rising; stop ₹422.99; charges ₹159.73 crore)
2023-08-14  VARROC      BUY ₹1.35 lakh crore at ₹385.40 (fresh Friday signal — BUY: 6.86× weekly, month 2.37×, ladder rising; stop ₹304.00; charges ₹160.10 crore)
2023-08-14  ZFCVINDIA   PYRAMID BUY ₹1.06 lakh crore at ₹2,230.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,046.36; charges ₹125.67 crore)
2023-08-21  ICICIBANK   PYRAMID BUY ₹47,582.66 crore at ₹950.70 (box jump — doubling the stake with NEW capital; stop stays ₹898.70; charges ₹56.38 crore)
2023-08-21  RATEGAIN    PYRAMID BUY ₹1.41 lakh crore at ₹572.80 (box jump — doubling the stake with NEW capital; stop stays ₹489.44; charges ₹167.07 crore)
2023-08-21  VARROC      PYRAMID BUY ₹1.35 lakh crore at ₹384.80 (box jump — doubling the stake with NEW capital; stop stays ₹347.89; charges ₹159.66 crore)
2023-08-28  FORCEMOT    PYRAMID BUY ₹2.05 lakh crore at ₹3,500.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,158.80; charges ₹242.87 crore)
2023-08-28  RATEGAIN    PYRAMID BUY ₹2.84 lakh crore at ₹577.50 (box jump — doubling the stake with NEW capital; stop stays ₹520.60; charges ₹336.68 crore)
2023-09-04  HAL         PYRAMID BUY ₹1.59 lakh crore at ₹1,982.17 (box jump — doubling the stake with NEW capital; stop stays ₹1,840.70; charges ₹188.92 crore)
2023-09-04  HEG         PYRAMID BUY ₹82,141.12 crore at ₹351.16 (box jump — doubling the stake with NEW capital; stop stays ₹324.38; charges ₹97.32 crore)
2023-09-18  VARROC      PYRAMID BUY ₹3.15 lakh crore at ₹450.55 (box jump — doubling the stake with NEW capital; stop stays ₹383.80; charges ₹373.66 crore)
2023-09-18  ZFCVINDIA   PYRAMID BUY ₹2.45 lakh crore at ₹2,576.83 (box jump — doubling the stake with NEW capital; stop stays ₹2,402.91; charges ₹290.25 crore)
2023-09-25  FORCEMOT    PYRAMID BUY ₹4.39 lakh crore at ₹3,749.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,341.72; charges ₹519.99 crore)
2023-10-03  VARROC      PYRAMID BUY ₹6.83 lakh crore at ₹487.95 (box jump — doubling the stake with NEW capital; stop stays ₹450.92; charges ₹808.89 crore)
2023-10-16  FORCEMOT    PYRAMID BUY ₹9.20 lakh crore at ₹3,930.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,709.99; charges ₹1,089.55 crore)
2023-10-16  HEG         PYRAMID BUY ₹1.70 lakh crore at ₹363.94 (box jump — doubling the stake with NEW capital; stop stays ₹328.78; charges ₹201.61 crore)
2023-10-20  FORCEMOT    SELL ₹17.33 lakh crore at stop ₹3,709.99 (+1.8%, charges ₹1,798.04 crore) — the cash goes back to work at the next Friday screen
2023-10-23  APOLLO      BUY ₹5.67 lakh crore at ₹76.15 (fresh Friday signal — BUY: 3.56× weekly, month 3.24×, ladder rising; stop ₹59.94; charges ₹671.61 crore)
2023-10-23  CRISIL      BUY ₹5.55 lakh crore at ₹4,199.70 (fresh Friday signal — BUY: 3.22× weekly, month 2.05×, ladder rising; stop ₹3,639.83; charges ₹658.14 crore)
2023-10-23  HEG         SELL ₹3.07 lakh crore at stop ₹328.78 (-5.6%, charges ₹318.39 crore) — the cash goes back to work at the next Friday screen
2023-10-23  NBCC        BUY ₹5.61 lakh crore at ₹45.87 (fresh Friday signal — BUY: 3.53× weekly, month 3.62×, ladder rising; stop ₹33.69; charges ₹664.39 crore)
2023-10-23  ZFCVINDIA   PYRAMID BUY ₹5.02 lakh crore at ₹2,642.07 (box jump — doubling the stake with NEW capital; stop stays ₹2,473.96; charges ₹594.85 crore)
2023-10-25  HAL         SELL ₹2.96 lakh crore at stop ₹1,840.70 (-3.0%, charges ₹306.68 crore) — the cash goes back to work at the next Friday screen
2023-10-25  VARROC      SELL ₹12.60 lakh crore at stop ₹450.92 (-0.4%, charges ₹1,306.73 crore) — the cash goes back to work at the next Friday screen
2023-10-30  ANGELONE    BUY ₹5.65 lakh crore at ₹253.50 (fresh Friday signal — BUY: 1.84× weekly, month 2.75×, ladder rising; stop ₹194.37; charges ₹669.10 crore)
2023-10-30  CUPID       BUY ₹5.64 lakh crore at ₹6.05 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹3.66; charges ₹668.07 crore)
2023-10-30  SHAREINDIA  BUY ₹5.64 lakh crore at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹668.65 crore)
2023-11-06  APOLLO      PYRAMID BUY ₹7.13 lakh crore at ₹95.90 (box jump — doubling the stake with NEW capital; stop stays ₹60.83; charges ₹844.79 crore)
2023-11-06  NBCC        PYRAMID BUY ₹5.51 lakh crore at ₹45.10 (box jump — doubling the stake with NEW capital; stop stays ₹37.78; charges ₹652.51 crore)
2023-11-06  RATEGAIN    PYRAMID BUY ₹6.89 lakh crore at ₹701.00 (box jump — doubling the stake with NEW capital; stop stays ₹549.53; charges ₹816.87 crore)
2023-11-13  ANGELONE    PYRAMID BUY ₹6.08 lakh crore at ₹273.19 (box jump — doubling the stake with NEW capital; stop stays ₹236.87; charges ₹720.23 crore)
2023-11-13  APOLLO      PYRAMID BUY ₹18.26 lakh crore at ₹122.90 (box jump — doubling the stake with NEW capital; stop stays ₹88.83; charges ₹2,163.99 crore)
2023-11-13  TDPOWERSYS  PYRAMID BUY ₹3.58 lakh crore at ₹135.78 (box jump — doubling the stake with NEW capital; stop stays ₹113.41; charges ₹424.19 crore)
2023-11-20  APOLLO      PYRAMID BUY ₹47.07 lakh crore at ₹158.45 (box jump — doubling the stake with NEW capital; stop stays ₹105.78; charges ₹5,576.59 crore)
2023-11-20  CRISIL      PYRAMID BUY ₹5.60 lakh crore at ₹4,242.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,861.80; charges ₹663.98 crore)
2023-11-20  RATEGAIN    PYRAMID BUY ₹14.19 lakh crore at ₹722.00 (box jump — doubling the stake with NEW capital; stop stays ₹619.50; charges ₹1,681.68 crore)
2023-11-20  SHAREINDIA  PYRAMID BUY ₹6.69 lakh crore at ₹356.00 (box jump — doubling the stake with NEW capital; stop stays ₹280.63; charges ₹792.52 crore)
2023-11-20  TDPOWERSYS  PYRAMID BUY ₹7.13 lakh crore at ₹135.32 (box jump — doubling the stake with NEW capital; stop stays ₹124.59; charges ₹845.07 crore)
2023-11-28  ANGELONE    PYRAMID BUY ₹13.64 lakh crore at ₹306.80 (box jump — doubling the stake with NEW capital; stop stays ₹274.55; charges ₹1,616.68 crore)
2023-11-28  CUPID       PYRAMID BUY ₹8.21 lakh crore at ₹8.82 (box jump — doubling the stake with NEW capital; stop stays ₹7.93; charges ₹973.09 crore)
2023-11-28  SHAREINDIA  PYRAMID BUY ₹12.87 lakh crore at ₹342.61 (box jump — doubling the stake with NEW capital; stop stays ₹321.67; charges ₹1,524.53 crore)
2023-12-18  ANGELONE    PYRAMID BUY ₹28.87 lakh crore at ₹324.80 (box jump — doubling the stake with NEW capital; stop stays ₹279.31; charges ₹3,421.03 crore)
2023-12-18  SHAREINDIA  PYRAMID BUY ₹27.60 lakh crore at ₹367.60 (box jump — doubling the stake with NEW capital; stop stays ₹328.89; charges ₹3,269.51 crore)
2023-12-26  CUPID       PYRAMID BUY ₹17.49 lakh crore at ₹9.40 (box jump — doubling the stake with NEW capital; stop stays ₹8.10; charges ₹2,072.24 crore)
2024-01-01  ANGELONE    PYRAMID BUY ₹61.91 lakh crore at ₹348.40 (box jump — doubling the stake with NEW capital; stop stays ₹296.88; charges ₹7,334.86 crore)
2024-01-01  ICICIBANK   PYRAMID BUY ₹99,195.62 crore at ₹991.55 (box jump — doubling the stake with NEW capital; stop stays ₹939.74; charges ₹117.53 crore)
2024-01-01  NBCC        PYRAMID BUY ₹13.33 lakh crore at ₹54.63 (box jump — doubling the stake with NEW capital; stop stays ₹45.65; charges ₹1,579.95 crore)
2024-01-01  SHAREINDIA  PYRAMID BUY ₹56.07 lakh crore at ₹373.70 (box jump — doubling the stake with NEW capital; stop stays ₹330.37; charges ₹6,643.60 crore)
2024-01-15  RATEGAIN    PYRAMID BUY ₹28.75 lakh crore at ₹731.75 (box jump — doubling the stake with NEW capital; stop stays ₹669.56; charges ₹3,406.75 crore)
2024-01-23  ANGELONE    SELL ₹1.05 crore crore at stop ₹296.88 (-9.1%, charges ₹10,926.20 crore) — the cash goes back to work at the next Friday screen
2024-01-23  APOLLO      PYRAMID BUY ₹71.61 lakh crore at ₹120.60 (box jump — doubling the stake with NEW capital; stop stays ₹112.10; charges ₹8,483.92 crore)
2024-01-24  CRISIL      SELL ₹10.19 lakh crore at stop ₹3,861.80 (-8.5%, charges ₹1,056.70 crore) — the cash goes back to work at the next Friday screen
2024-01-29  IDBI        BUY ₹57.25 lakh crore at ₹84.30 (fresh Friday signal — BUY: 8.31× weekly, month 1.96×, ladder rising; stop ₹60.23; charges ₹6,783.50 crore)
2024-01-29  NBCC        PYRAMID BUY ₹38.05 lakh crore at ₹78.00 (box jump — doubling the stake with NEW capital; stop stays ₹53.58; charges ₹4,508.72 crore)
2024-01-29  RITES       BUY ₹61.11 lakh crore at ₹342.50 (fresh Friday signal — BUY: 11.32× weekly, month 2.99×, ladder rising; stop ₹240.21; charges ₹7,240.71 crore)
2024-02-02  ZFCVINDIA   SELL ₹9.39 lakh crore at stop ₹2,473.96 (-0.7%, charges ₹973.71 crore) — the cash goes back to work at the next Friday screen
2024-02-05  CUPID       PYRAMID BUY ₹63.63 lakh crore at ₹17.11 (box jump — doubling the stake with NEW capital; stop stays ₹16.11; charges ₹7,539.51 crore)
2024-02-13  APOLLO      SELL ₹1.33 crore crore at stop ₹112.10 (-11.0%, charges ₹13,785.72 crore) — the cash goes back to work at the next Friday screen
2024-02-19  IDBI        PYRAMID BUY ₹62.04 lakh crore at ₹91.45 (box jump — doubling the stake with NEW capital; stop stays ₹72.11; charges ₹7,350.13 crore)
2024-02-19  NBCC        PYRAMID BUY ₹88.74 lakh crore at ₹91.00 (box jump — doubling the stake with NEW capital; stop stays ₹69.28; charges ₹10,514.11 crore)
2024-02-19  PRUDENT     BUY ₹1.13 crore crore at ₹1,332.00 (fresh Friday signal — BUY: 19.33× weekly, month 4.96×, ladder rising; stop ₹1,008.17; charges ₹13,341.74 crore)
2024-02-19  RATEGAIN    PYRAMID BUY ₹68.65 lakh crore at ₹874.00 (box jump — doubling the stake with NEW capital; stop stays ₹720.34; charges ₹8,133.21 crore)
2024-02-19  RITES       PYRAMID BUY ₹67.74 lakh crore at ₹380.10 (box jump — doubling the stake with NEW capital; stop stays ₹314.37; charges ₹8,026.09 crore)
2024-02-19  SHAREINDIA  PYRAMID BUY ₹1.16 crore crore at ₹386.39 (box jump — doubling the stake with NEW capital; stop stays ₹357.20; charges ₹13,730.26 crore)
2024-02-26  CUPID       PYRAMID BUY ₹1.82 crore crore at ₹24.50 (box jump — doubling the stake with NEW capital; stop stays ₹17.77; charges ₹21,580.91 crore)
2024-02-26  PRUDENT     PYRAMID BUY ₹1.17 crore crore at ₹1,382.05 (box jump — doubling the stake with NEW capital; stop stays ₹1,176.05; charges ₹13,826.65 crore)
2024-03-04  RATEGAIN    PYRAMID BUY ₹1.29 crore crore at ₹821.50 (box jump — doubling the stake with NEW capital; stop stays ₹730.99; charges ₹15,280.26 crore)
2024-03-06  SHAREINDIA  SELL ₹2.14 crore crore at stop ₹357.20 (-4.6%, charges ₹22,189.06 crore) — the cash goes back to work at the next Friday screen
2024-03-11  BHEL        BUY ₹95.23 lakh crore at ₹259.10 (fresh Friday signal — BUY: 3.01× weekly, month 1.67×, ladder rising; stop ₹188.78; charges ₹11,283.55 crore)
2024-03-11  ICICIBANK   PYRAMID BUY ₹2.18 lakh crore at ₹1,087.95 (box jump — doubling the stake with NEW capital; stop stays ₹986.58; charges ₹257.76 crore)
2024-03-11  SOLARINDS   BUY ₹1.48 crore crore at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹17,577.83 crore)
2024-03-13  PRUDENT     SELL ₹1.98 crore crore at stop ₹1,176.05 (-13.3%, charges ₹20,568.07 crore) — the cash goes back to work at the next Friday screen
2024-03-13  RATEGAIN    SELL ₹2.29 crore crore at stop ₹730.99 (-9.2%, charges ₹23,768.91 crore) — the cash goes back to work at the next Friday screen
2024-03-13  RITES       SELL ₹1.12 crore crore at stop ₹314.37 (-13.0%, charges ₹11,604.37 crore) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹1.28 crore crore at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹15,116.69 crore)
2024-03-18  FORCEMOT    BUY ₹1.37 crore crore at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 3.03× weekly, month 1.69×, ladder rising; stop ₹5,500.61; charges ₹16,243.25 crore)
2024-03-18  ICICIBANK   PYRAMID BUY ₹4.30 lakh crore at ₹1,075.05 (box jump — doubling the stake with NEW capital; stop stays ₹1,002.87; charges ₹509.10 crore)
2024-03-18  INDIGO      BUY ₹1.37 crore crore at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹16,220.26 crore)
2024-03-18  JIOFIN      BUY ₹1.38 crore crore at ₹346.95 (fresh Friday signal — BUY: 2.56× weekly, month 2.25×, ladder rising; stop ₹290.75; charges ₹16,316.83 crore)
2024-03-26  BOSCHLTD    PYRAMID BUY ₹1.31 crore crore at ₹30,245.00 (box jump — doubling the stake with NEW capital; stop stays ₹26,710.20; charges ₹15,480.06 crore)
2024-03-26  JIOFIN      PYRAMID BUY ₹1.37 crore crore at ₹345.00 (box jump — doubling the stake with NEW capital; stop stays ₹301.05; charges ₹16,205.90 crore)
2024-04-01  IDBI        PYRAMID BUY ₹1.10 crore crore at ₹81.30 (box jump — doubling the stake with NEW capital; stop stays ₹74.19; charges ₹13,060.95 crore)
2024-04-01  SOLARINDS   PYRAMID BUY ₹1.75 crore crore at ₹8,950.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,980.95; charges ₹20,774.09 crore)
2024-04-01  TAX         FY2024 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹1.09 crore crore / LT ₹0.00)
2024-04-08  BOSCHLTD    PYRAMID BUY ₹2.67 crore crore at ₹30,980.00 (box jump — doubling the stake with NEW capital; stop stays ₹28,244.40; charges ₹31,693.72 crore)
2024-04-15  INDIGO      PYRAMID BUY ₹1.57 crore crore at ₹3,670.30 (box jump — doubling the stake with NEW capital; stop stays ₹3,287.00; charges ₹18,582.09 crore)
2024-04-29  FORCEMOT    PYRAMID BUY ₹2.11 crore crore at ₹10,100.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,483.47; charges ₹24,949.75 crore)
2024-04-29  IDBI        PYRAMID BUY ₹2.40 crore crore at ₹88.50 (box jump — doubling the stake with NEW capital; stop stays ₹78.19; charges ₹28,418.43 crore)
2024-04-29  NBCC        PYRAMID BUY ₹1.79 crore crore at ₹92.00 (box jump — doubling the stake with NEW capital; stop stays ₹74.74; charges ₹21,246.70 crore)
2024-05-13  INDIGO      PYRAMID BUY ₹3.42 crore crore at ₹4,006.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,719.77; charges ₹40,540.35 crore)
2024-05-13  NBCC        PYRAMID BUY ₹3.45 crore crore at ₹88.60 (box jump — doubling the stake with NEW capital; stop stays ₹80.15; charges ₹40,898.75 crore)
2024-05-21  BHEL        PYRAMID BUY ₹1.15 crore crore at ₹311.90 (box jump — doubling the stake with NEW capital; stop stays ₹251.68; charges ₹13,566.85 crore)
2024-05-21  FORCEMOT    PYRAMID BUY ₹3.75 crore crore at ₹8,987.50 (box jump — doubling the stake with NEW capital; stop stays ₹8,083.65; charges ₹44,376.84 crore)
2024-05-21  ICICIBANK   PYRAMID BUY ₹8.97 lakh crore at ₹1,122.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,051.37; charges ₹1,062.23 crore)
2024-05-21  JIOFIN      PYRAMID BUY ₹2.86 crore crore at ₹361.00 (box jump — doubling the stake with NEW capital; stop stays ₹317.61; charges ₹33,894.86 crore)
2024-05-21  TDPOWERSYS  PYRAMID BUY ₹17.28 lakh crore at ₹164.00 (box jump — doubling the stake with NEW capital; stop stays ₹129.90; charges ₹2,047.07 crore)
2024-05-27  BOSCHLTD    PYRAMID BUY ₹5.33 crore crore at ₹30,901.00 (box jump — doubling the stake with NEW capital; stop stays ₹29,015.09; charges ₹63,188.34 crore)
2024-05-28  FORCEMOT    SELL ₹6.73 crore crore at stop ₹8,083.65 (-6.7%, charges ₹69,774.94 crore) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹5.22 crore crore at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹61,903.49 crore)
2024-06-04  BHEL        SELL ₹1.84 crore crore at stop ₹251.68 (-11.8%, charges ₹19,137.57 crore) — the cash goes back to work at the next Friday screen
2024-06-04  BOSCHLTD    SELL ₹10.00 crore crore at stop ₹29,015.09 (-5.4%, charges ₹1.04 lakh crore) — the cash goes back to work at the next Friday screen
2024-06-04  CUPID       SELL ₹2.64 crore crore at stop ₹17.77 (-4.6%, charges ₹27,363.12 crore) — the cash goes back to work at the next Friday screen
2024-06-04  IDBI        SELL ₹4.23 crore crore at stop ₹78.19 (-9.7%, charges ₹43,891.71 crore) — the cash goes back to work at the next Friday screen
2024-06-04  JIOFIN      SELL ₹5.03 crore crore at stop ₹317.61 (-10.1%, charges ₹52,130.92 crore) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹3.12 crore crore at stop ₹7,980.95 (-3.3%, charges ₹32,383.82 crore) — the cash goes back to work at the next Friday screen
2024-06-05  ICICIBANK   SELL ₹16.77 lakh crore at stop ₹1,051.37 (-3.3%, charges ₹1,739.72 crore) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹6.23 crore crore at ₹156.60 (fresh Friday signal — BUY: 7.81× weekly, month 1.77×, ladder rising; stop ₹126.55; charges ₹73,791.22 crore)
2024-06-10  CAMPUS      PYRAMID BUY ₹5.27 crore crore at ₹289.00 (box jump — doubling the stake with NEW capital; stop stays ₹248.05; charges ₹62,478.72 crore)
2024-06-10  DABUR       BUY ₹6.20 crore crore at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹73,476.77 crore)
2024-06-10  FIEMIND     BUY ₹6.25 crore crore at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹74,027.97 crore)
2024-06-10  INDIGO      PYRAMID BUY ₹7.51 crore crore at ₹4,398.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,805.04; charges ₹88,959.76 crore)
2024-06-10  NCC         BUY ₹3.64 crore crore at ₹327.60 (fresh Friday signal — BUY: 2.80× weekly, month 1.63×, ladder rising; stop ₹260.92; charges ₹43,080.57 crore)
2024-06-10  UNOMINDA    BUY ₹6.22 crore crore at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.61×, ladder rising; stop ₹769.64; charges ₹73,657.28 crore)
2024-06-18  DABUR       PYRAMID BUY ₹6.23 crore crore at ₹608.10 (box jump — doubling the stake with NEW capital; stop stays ₹552.95; charges ₹73,863.43 crore)
2024-06-18  UNOMINDA    PYRAMID BUY ₹6.76 crore crore at ₹1,056.60 (box jump — doubling the stake with NEW capital; stop stays ₹895.00; charges ₹80,138.22 crore)
2024-06-24  FIEMIND     PYRAMID BUY ₹6.08 crore crore at ₹1,286.35 (box jump — doubling the stake with NEW capital; stop stays ₹1,162.80; charges ₹72,055.34 crore)
2024-07-01  INDIGO      PYRAMID BUY ₹14.59 crore crore at ₹4,276.35 (box jump — doubling the stake with NEW capital; stop stays ₹3,976.70; charges ₹1.73 lakh crore)
2024-07-01  NCC         PYRAMID BUY ₹3.51 crore crore at ₹316.50 (box jump — doubling the stake with NEW capital; stop stays ₹297.87; charges ₹41,571.57 crore)
2024-07-08  NBCC        PYRAMID BUY ₹9.84 crore crore at ₹126.34 (box jump — doubling the stake with NEW capital; stop stays ₹98.17; charges ₹1.17 lakh crore)
2024-07-08  TDPOWERSYS  PYRAMID BUY ₹43.09 lakh crore at ₹204.62 (box jump — doubling the stake with NEW capital; stop stays ₹162.59; charges ₹5,105.28 crore)
2024-07-08  UNOMINDA    PYRAMID BUY ₹15.03 crore crore at ₹1,174.40 (box jump — doubling the stake with NEW capital; stop stays ₹981.87; charges ₹1.78 lakh crore)
2024-07-15  TDPOWERSYS  PYRAMID BUY ₹85.82 lakh crore at ₹203.90 (box jump — doubling the stake with NEW capital; stop stays ₹188.72; charges ₹10,168.37 crore)
2024-07-19  TDPOWERSYS  SELL ₹1.59 crore crore at stop ₹188.72 (-0.7%, charges ₹16,452.29 crore) — the cash goes back to work at the next Friday screen
2024-07-19  UNOMINDA    SELL ₹25.09 crore crore at stop ₹981.87 (-10.2%, charges ₹2.60 lakh crore) — the cash goes back to work at the next Friday screen
2024-07-22  FIEMIND     PYRAMID BUY ₹12.28 crore crore at ₹1,299.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,257.56; charges ₹1.45 lakh crore)
2024-07-22  INDIAGLYCO  BUY ₹13.06 crore crore at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹1.55 lakh crore)
2024-07-22  PGIL        BUY ₹13.62 crore crore at ₹405.00 (fresh Friday signal — BUY: 3.81× weekly, month 8.12×, ladder rising; stop ₹335.38; charges ₹1.61 lakh crore)
2024-07-23  FIEMIND     SELL ₹23.73 crore crore at stop ₹1,257.56 (-3.3%, charges ₹2.46 lakh crore) — the cash goes back to work at the next Friday screen
2024-07-23  NCC         SELL ₹6.59 crore crore at stop ₹297.87 (-7.5%, charges ₹68,394.95 crore) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹14.23 crore crore at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹1.69 lakh crore)
2024-07-29  THYROCARE   BUY ₹14.24 crore crore at ₹261.67 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹196.33; charges ₹1.69 lakh crore)
2024-08-05  DABUR       PYRAMID BUY ₹12.60 crore crore at ₹615.00 (box jump — doubling the stake with NEW capital; stop stays ₹587.15; charges ₹1.49 lakh crore)
2024-08-05  NBCC        PYRAMID BUY ₹18.04 crore crore at ₹115.87 (box jump — doubling the stake with NEW capital; stop stays ₹109.78; charges ₹2.14 lakh crore)
2024-08-05  THYROCARE   PYRAMID BUY ₹14.50 crore crore at ₹266.65 (box jump — doubling the stake with NEW capital; stop stays ₹243.17; charges ₹1.72 lakh crore)
2024-08-06  NBCC        SELL ₹34.12 crore crore at stop ₹109.78 (-1.3%, charges ₹3.54 lakh crore) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹5.02 crore crore at stop ₹126.55 (-19.2%, charges ₹52,090.93 crore) — the cash goes back to work at the next Friday screen
2024-08-12  AVANTIFEED  PYRAMID BUY ₹15.44 crore crore at ₹758.00 (box jump — doubling the stake with NEW capital; stop stays ₹596.83; charges ₹1.83 lakh crore)
2024-08-12  CAMPUS      PYRAMID BUY ₹10.64 crore crore at ₹291.85 (box jump — doubling the stake with NEW capital; stop stays ₹277.07; charges ₹1.26 lakh crore)
2024-08-12  CERA        BUY ₹24.04 crore crore at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹2.85 lakh crore)
2024-08-12  INDIAGLYCO  PYRAMID BUY ₹15.21 crore crore at ₹600.55 (box jump — doubling the stake with NEW capital; stop stays ₹535.82; charges ₹1.80 lakh crore)
2024-08-12  PGIL        PYRAMID BUY ₹16.12 crore crore at ₹480.18 (box jump — doubling the stake with NEW capital; stop stays ₹388.64; charges ₹1.91 lakh crore)
2024-08-16  CAMPUS      SELL ₹20.18 crore crore at stop ₹277.07 (-4.4%, charges ₹2.09 lakh crore) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹24.01 crore crore at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.15×, ladder rising; stop ₹361.00; charges ₹2.85 lakh crore)
2024-08-19  VGUARD      BUY ₹13.12 crore crore at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹1.55 lakh crore)
2024-08-26  AVANTIFEED  PYRAMID BUY ₹28.30 crore crore at ₹695.00 (box jump — doubling the stake with NEW capital; stop stays ₹650.13; charges ₹3.35 lakh crore)
2024-08-26  INDIAGLYCO  PYRAMID BUY ₹32.22 crore crore at ₹636.50 (box jump — doubling the stake with NEW capital; stop stays ₹587.91; charges ₹3.82 lakh crore)
2024-08-26  SUPRIYA     PYRAMID BUY ₹25.36 crore crore at ₹558.30 (box jump — doubling the stake with NEW capital; stop stays ₹470.87; charges ₹3.00 lakh crore)
2024-09-09  AVANTIFEED  SELL ₹52.86 crore crore at stop ₹650.13 (-8.6%, charges ₹5.48 lakh crore) — the cash goes back to work at the next Friday screen
2024-09-09  INDIGO      PYRAMID BUY ₹32.60 crore crore at ₹4,780.00 (box jump — doubling the stake with NEW capital; stop stays ₹4,485.14; charges ₹3.86 lakh crore)
2024-09-09  SUPRIYA     PYRAMID BUY ₹54.48 crore crore at ₹600.00 (box jump — doubling the stake with NEW capital; stop stays ₹498.75; charges ₹6.45 lakh crore)
2024-09-09  THYROCARE   PYRAMID BUY ₹30.62 crore crore at ₹281.75 (box jump — doubling the stake with NEW capital; stop stays ₹265.38; charges ₹3.63 lakh crore)
2024-09-16  DABUR       PYRAMID BUY ₹27.03 crore crore at ₹660.00 (box jump — doubling the stake with NEW capital; stop stays ₹602.49; charges ₹3.20 lakh crore)
2024-09-16  PGIL        PYRAMID BUY ₹32.72 crore crore at ₹487.50 (box jump — doubling the stake with NEW capital; stop stays ₹434.53; charges ₹3.88 lakh crore)
2024-09-16  PRSMJOHNSN  BUY ₹51.11 crore crore at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹6.06 lakh crore)
2024-09-19  CERA        SELL ₹18.73 crore crore at stop ₹8,198.93 (-21.9%, charges ₹1.94 lakh crore) — the cash goes back to work at the next Friday screen
2024-09-23  PGIL        SELL ₹58.23 crore crore at stop ₹434.53 (-6.6%, charges ₹6.04 lakh crore) — the cash goes back to work at the next Friday screen
2024-09-30  PRSMJOHNSN  PYRAMID BUY ₹49.74 crore crore at ₹209.00 (box jump — doubling the stake with NEW capital; stop stays ₹168.72; charges ₹5.89 lakh crore)
2024-09-30  VIYASH      BUY ₹52.69 crore crore at ₹216.00 (fresh Friday signal — BUY: 5.97× weekly, month 2.57×, ladder rising; stop ₹161.73; charges ₹6.24 lakh crore)
2024-10-03  DABUR       SELL ₹49.27 crore crore at stop ₹602.49 (-5.2%, charges ₹5.11 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹10.50 crore crore at stop ₹420.24 (-19.8%, charges ₹1.09 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-07  BSE         BUY ₹35.57 crore crore at ₹1,396.67 (fresh Friday signal — ACCUMULATE: 2.88× weekly, month 3.26×, ladder rising; stop ₹1,131.31; charges ₹4.21 lakh crore)
2024-10-07  CEMPRO      BUY ₹50.22 crore crore at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹5.95 lakh crore)
2024-10-07  INDIGO      SELL ₹61.08 crore crore at stop ₹4,485.14 (+0.3%, charges ₹6.34 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹57.58 crore crore at stop ₹265.38 (-2.8%, charges ₹5.97 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-14  PAYTM       BUY ₹51.95 crore crore at ₹729.60 (fresh Friday signal — BUY: 1.93× weekly, month 2.08×, ladder rising; stop ₹617.60; charges ₹6.15 lakh crore)
2024-10-14  SKIPPER     BUY ₹66.72 crore crore at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.80×, ladder rising; stop ₹418.00; charges ₹7.91 lakh crore)
2024-10-14  SUPRIYA     PYRAMID BUY ₹103.81 crore crore at ₹572.00 (box jump — doubling the stake with NEW capital; stop stays ₹500.65; charges ₹12.30 lakh crore)
2024-10-14  VIYASH      PYRAMID BUY ₹46.66 crore crore at ₹191.50 (box jump — doubling the stake with NEW capital; stop stays ₹172.84; charges ₹5.53 lakh crore)
2024-10-23  VIYASH      SELL ₹84.08 crore crore at stop ₹172.84 (-15.2%, charges ₹8.72 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹59.42 crore crore at stop ₹587.91 (-1.5%, charges ₹6.16 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       PYRAMID BUY ₹53.17 crore crore at ₹747.70 (box jump — doubling the stake with NEW capital; stop stays ₹636.31; charges ₹6.30 lakh crore)
2024-10-28  PRSMJOHNSN  PYRAMID BUY ₹90.86 crore crore at ₹191.00 (box jump — doubling the stake with NEW capital; stop stays ₹170.55; charges ₹10.77 lakh crore)
2024-11-04  BSE         PYRAMID BUY ₹37.68 crore crore at ₹1,481.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,231.60; charges ₹8.89 lakh crore)
2024-11-04  CEMPRO      PYRAMID BUY ₹41.90 crore crore at ₹547.15 (box jump — doubling the stake with NEW capital; stop stays ₹430.14; charges ₹9.89 lakh crore)
2024-11-04  JSWDULUX    BUY ₹94.83 crore crore at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹22.39 lakh crore)
2024-11-04  KIRLPNU     BUY ₹48.67 crore crore at ₹849.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.99×, ladder rising; stop ₹594.25; charges ₹11.49 lakh crore)
2024-11-04  SKIPPER     PYRAMID BUY ₹65.82 crore crore at ₹546.15 (box jump — doubling the stake with NEW capital; stop stays ₹448.15; charges ₹15.54 lakh crore)
2024-11-11  KIRLPNU     PYRAMID BUY ₹48.33 crore crore at ₹845.00 (box jump — doubling the stake with NEW capital; stop stays ₹752.42; charges ₹11.41 lakh crore)
2024-11-25  PAYTM       PYRAMID BUY ₹129.89 crore crore at ₹913.80 (box jump — doubling the stake with NEW capital; stop stays ₹712.50; charges ₹30.66 lakh crore)
2024-11-25  SUPRIYA     PYRAMID BUY ₹293.48 crore crore at ₹809.00 (box jump — doubling the stake with NEW capital; stop stays ₹574.32; charges ₹69.28 lakh crore)
2024-12-09  JSWDULUX    PYRAMID BUY ₹77.87 crore crore at ₹3,718.70 (box jump — doubling the stake with NEW capital; stop stays ₹3,423.18; charges ₹18.38 lakh crore)
2024-12-09  PAYTM       PYRAMID BUY ₹283.23 crore crore at ₹997.45 (box jump — doubling the stake with NEW capital; stop stays ₹838.09; charges ₹66.86 lakh crore)
2024-12-09  SUPRIYA     PYRAMID BUY ₹565.24 crore crore at ₹780.00 (box jump — doubling the stake with NEW capital; stop stays ₹717.25; charges ₹1.33 crore crore)
2024-12-16  CEMPRO      PYRAMID BUY ₹78.76 crore crore at ₹514.85 (box jump — doubling the stake with NEW capital; stop stays ₹477.71; charges ₹18.59 lakh crore)
2024-12-16  KIRLPNU     PYRAMID BUY ₹96.76 crore crore at ₹846.95 (box jump — doubling the stake with NEW capital; stop stays ₹798.00; charges ₹22.84 lakh crore)
2024-12-17  SUPRIYA     SELL ₹1,036.01 crore crore at stop ₹717.25 (-2.4%, charges ₹2.30 crore crore) — the cash goes back to work at the next Friday screen
2024-12-23  KAYNES      BUY ₹301.40 crore crore at ₹7,358.80 (fresh Friday signal — BUY: 3.40× weekly, month 2.00×, ladder rising; stop ₹5,824.55; charges ₹71.15 lakh crore)
2024-12-23  KIRLPNU     SELL ₹181.72 crore crore at stop ₹798.00 (-5.8%, charges ₹40.36 lakh crore) — the cash goes back to work at the next Friday screen
2024-12-23  PAYTM       PYRAMID BUY ₹544.43 crore crore at ₹959.80 (box jump — doubling the stake with NEW capital; stop stays ₹887.49; charges ₹1.29 crore crore)
2024-12-23  ZENTEC      BUY ₹301.21 crore crore at ₹2,555.00 (fresh Friday signal — BUY: 3.53× weekly, month 2.25×, ladder rising; stop ₹1,537.95; charges ₹71.10 lakh crore)
2024-12-26  PRSMJOHNSN  SELL ₹161.81 crore crore at stop ₹170.55 (-15.3%, charges ₹35.94 lakh crore) — the cash goes back to work at the next Friday screen
2024-12-27  JSWDULUX    SELL ₹142.88 crore crore at stop ₹3,423.18 (-16.9%, charges ₹31.74 lakh crore) — the cash goes back to work at the next Friday screen
2024-12-30  KAYNES      PYRAMID BUY ₹289.62 crore crore at ₹7,088.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,670.80; charges ₹68.37 lakh crore)
2024-12-30  KFINTECH    BUY ₹448.50 crore crore at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.22×, ladder rising; stop ₹1,159.14; charges ₹1.06 crore crore)
2024-12-30  PAYTM       PYRAMID BUY ₹1,152.39 crore crore at ₹1,017.00 (box jump — doubling the stake with NEW capital; stop stays ₹893.05; charges ₹2.72 crore crore)
2025-01-06  BSE         PYRAMID BUY ₹90.61 crore crore at ₹1,783.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,651.54; charges ₹21.39 lakh crore)
2025-01-06  LLOYDSME    BUY ₹471.30 crore crore at ₹1,439.00 (fresh Friday signal — BUY: 2.97× weekly, month 1.94×, ladder rising; stop ₹1,064.09; charges ₹1.11 crore crore)
2025-01-06  SKIPPER     PYRAMID BUY ₹134.11 crore crore at ₹557.10 (box jump — doubling the stake with NEW capital; stop stays ₹477.28; charges ₹31.66 lakh crore)
2025-01-06  ZENTEC      PYRAMID BUY ₹297.96 crore crore at ₹2,533.45 (box jump — doubling the stake with NEW capital; stop stays ₹2,213.55; charges ₹70.34 lakh crore)
2025-01-09  PAYTM       SELL ₹2,017.00 crore crore at stop ₹893.05 (-8.5%, charges ₹4.48 crore crore) — the cash goes back to work at the next Friday screen
2025-01-10  KAYNES      SELL ₹543.30 crore crore at stop ₹6,670.80 (-7.7%, charges ₹1.21 crore crore) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹229.01 crore crore at stop ₹477.28 (-13.7%, charges ₹50.87 lakh crore) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹491.90 crore crore at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 4.81×, ladder rising; stop ₹697.76; charges ₹1.16 crore crore)
2025-01-13  LLOYDSME    PYRAMID BUY ₹471.14 crore crore at ₹1,441.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,258.75; charges ₹1.11 crore crore)
2025-01-13  ZENTEC      SELL ₹518.91 crore crore at stop ₹2,213.55 (-13.0%, charges ₹1.15 crore crore) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹342.39 crore crore at stop ₹1,159.14 (-23.3%, charges ₹76.05 lakh crore) — the cash goes back to work at the next Friday screen
2025-01-20  AEGISLOG    PYRAMID BUY ₹472.48 crore crore at ₹803.60 (box jump — doubling the stake with NEW capital; stop stays ₹700.36; charges ₹1.12 crore crore)
2025-01-20  APOLLO      BUY ₹536.47 crore crore at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 5.79×, ladder rising; stop ₹110.19; charges ₹1.27 crore crore)
2025-01-24  AEGISLOG    SELL ₹820.77 crore crore at stop ₹700.36 (-14.5%, charges ₹1.82 crore crore) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹513.02 crore crore at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹1.21 crore crore)
2025-01-28  LLOYDSME    SELL ₹819.80 crore crore at stop ₹1,258.75 (-12.6%, charges ₹1.82 crore crore) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹520.45 crore crore at ₹947.00 (fresh Friday signal — BUY: 4.92× weekly, month 3.02×, ladder rising; stop ₹727.84; charges ₹1.23 crore crore)
2025-02-10  ZENSARTECH  PYRAMID BUY ₹504.44 crore crore at ₹920.05 (box jump — doubling the stake with NEW capital; stop stays ₹814.20; charges ₹1.19 crore crore)
2025-02-17  APOLLO      SELL ₹447.48 crore crore at stop ₹110.19 (-16.2%, charges ₹99.39 lakh crore) — the cash goes back to work at the next Friday screen
2025-02-17  ZENSARTECH  SELL ₹889.78 crore crore at stop ₹814.20 (-12.8%, charges ₹1.98 crore crore) — the cash goes back to work at the next Friday screen
2025-02-28  BSE         SELL ₹167.27 crore crore at stop ₹1,651.54 (+2.5%, charges ₹37.15 lakh crore) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹543.46 crore crore at ₹1,450.00 (fresh Friday signal — BUY: 4.67× weekly, month 1.70×, ladder rising; stop ₹1,235.90; charges ₹1.28 crore crore)
2025-03-10  CREDITACC   PYRAMID BUY ₹583.31 crore crore at ₹968.75 (box jump — doubling the stake with NEW capital; stop stays ₹837.38; charges ₹1.38 crore crore)
2025-03-17  NH          PYRAMID BUY ₹568.73 crore crore at ₹1,521.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,436.97; charges ₹1.34 crore crore)
2025-03-24  INDIASHLTR  BUY ₹680.63 crore crore at ₹794.95 (fresh Friday signal — BUY: 4.59× weekly, month 1.56×, ladder rising; stop ₹692.55; charges ₹1.61 crore crore)
```
