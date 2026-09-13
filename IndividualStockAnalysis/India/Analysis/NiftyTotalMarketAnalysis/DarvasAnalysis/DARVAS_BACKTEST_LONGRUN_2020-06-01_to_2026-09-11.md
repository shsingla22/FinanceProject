# The Darvas screen — 2020-06-01 → 2026-09-11

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2019-06-01 → 2026-09-11, 741 symbols, in `2019-06-01_to_2026-09-13/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **Two limits that cannot be engineered away:** the universe is TODAY'S NiftyTotalMarket constituents (survivorship bias flatters the early years), and Yahoo serves split-adjusted history. No slippage, stop exits at the stop price, fractional shares.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), best volume reaction first, at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with NEW capital.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled with FRESH MONEY from outside the portfolio, equal to the position's market value, at the next day's open. The new money never touches the portfolio's cash — fresh entries are never starved — and every injection is dated and logged, so the honest yardstick is the money-weighted return (XIRR), not a naive multiple. Each add-on is its own tax lot on its own holding clock; the ratcheted stop covers the whole enlarged position.

## The headline — XIRR is the honest yardstick

| Engine | Money put in | Final value | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | ₹842.65 lakh crore crore (₹100 + ₹842.65 lakh crore crore injected) | **₹897.23 lakh crore crore** | **+50.85%** |
| B: doubling, before charges and tax | ₹945.71 lakh crore crore | ₹1,012.81 lakh crore crore | +56.47% |
| **A: no doubling, NET of charges and tax** | ₹100.00 | **₹788.82** | **+39.04%** |
| A: no doubling, before charges and tax | ₹100.00 | ₹1,050.49 | +45.54% |
| Nifty 50 (pre-cost, pre-tax) | ₹100.00 | ₹230.70 | +14.27% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹6.38; unrealised gains in both end books carry further deferred liabilities.*

6.27 years, 328 weekly screens. Engine B injected new capital 488 times (gross run: 489); the complete dated injection list is in the blotter and the events CSV.

## Reality check — what doubling on EVERY jump actually demands

Doubling with new capital on every box jump is EXPONENTIAL twice over:
within a position (each jump doubles it) and across the portfolio (a
doubled position that stops out turns giant proceeds into internal
cash, funding giant new entries that each double again). Per ₹100
started, the fresh capital the rule demanded crossed:

| Cumulative new capital demanded | Reached by |
|---|---|
| ₹1,000 (10× the start) | 2020-09-07 |
| ₹1 lakh (1,000×) | 2021-03-15 |
| ₹1 crore (10⁵×) | 2021-09-20 |
| ₹100 crore (10⁷×) | 2022-06-20 |
| ₹1 lakh crore (10¹⁰×) | 2023-05-15 |
| 10¹⁵ ₹ — the scale of India's entire market cap per ₹100 started | 2024-02-26 |
| 10¹⁸ ₹ | 2025-05-19 |

No investor has this money and no market absorbs it — beyond the first
year or two the simulation is arithmetic (zero market impact assumed),
not an implementable strategy. **The one scale-free, honest number is the XIRR: +50.85% a year net for the doubling engine against +39.04% without — but see the March-2025 window's report, where the identical rule LOSES 39% a year because the window ends inside a correction.**

## What the frictions took (net runs)

| | Engine A: no doubling | Engine B: doubling |
|---|---:|---:|
| Transaction charges | ₹27.58 | ₹2.56 lakh crore crore |
| Capital-gains tax paid | ₹120.33 | ₹0.00 |
| Tax accrued, final part-year | ₹6.38 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹6,471.72 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹2.35 crore / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹4,323.15 crore / ₹0.00 |
| FY2024 | 2024-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹84.15 lakh crore / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹820.19 crore crore / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹2.00 lakh crore crore / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹3.65 lakh crore crore / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹51.45 | ₹0.00 | ₹10.29 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹84.66 | ₹0.00 | ₹16.93 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹83.74 | ₹4.00 | ₹17.25 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹251.30 | ₹0.00 | ₹50.26 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹65.15 | ₹36.67 | ₹17.61 | ₹0.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹39.90 | ₹0.00 | ₹7.98 | ₹0.00 / ₹0.00 |
| Final part-year (accrued) | — | ₹31.89 | ₹0.00 | ₹6.38 | ₹0.00 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2020 (2020-12-24) | ₹149.03 | +49.0% | ₹14,434.28 | ₹12,403.12 | +84.2% | +35.6% |
| 2021 (2021-12-31) | ₹256.28 | +72.0% | ₹12.73 crore | ₹11.97 crore | +51.0% | +26.2% |
| 2022 (2022-12-30) | ₹316.25 | +23.4% | ₹10,264.92 crore | ₹9,518.88 crore | +55.4% | +4.3% |
| 2023 (2023-12-29) | ₹569.39 | +80.0% | ₹2.37 crore crore | ₹2.25 crore crore | +40.0% | +20.0% |
| 2024 (2024-12-27) | ₹661.71 | +16.2% | ₹2,326.06 crore crore | ₹2,391.65 crore crore | -22.7% | +9.6% |
| 2025 (2025-12-26) | ₹648.81 | -1.9% | ₹5.23 lakh crore crore | ₹5.45 lakh crore crore | -23.5% | +9.4% |
| 2026 (2026-09-11) | ₹788.82 | +21.6% | ₹897.23 lakh crore crore | ₹837.18 lakh crore crore | +31.2% | -10.2% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-8.6%** (A: -26.4%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **190 closed trades**: 22 winners (12%), average winner +4.2%, average loser -8.1% (returns per blended entry price).
- Best closed trade GNFC +13.4%; worst MAHABANK -27.1%.
- Median holding period 72 days.
- Cash share of equity averaged 15%; fully in cash 1 of 328 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

| Month-end screen | B equity | B injected so far | B cash | B positions | A equity |
|---|---:|---:|---:|---:|---:|
| 2020-06-26 | ₹152.23 | ₹45.02 | ₹0.00 | 10 | ₹104.31 |
| 2020-07-31 | ₹374.16 | ₹258.24 | ₹32.65 | 7 | ₹107.40 |
| 2020-08-28 | ₹975.83 | ₹847.28 | ₹0.04 | 8 | ₹119.98 |
| 2020-09-25 | ₹1,450.44 | ₹1,387.29 | ₹133.80 | 9 | ₹119.66 |
| 2020-10-30 | ₹3,431.92 | ₹3,215.25 | ₹257.21 | 9 | ₹125.57 |
| 2020-11-27 | ₹5,445.39 | ₹5,023.77 | ₹95.51 | 10 | ₹129.68 |
| 2020-12-24 | ₹14,434.28 | ₹12,403.12 | ₹3,542.61 | 8 | ₹149.03 |
| 2021-01-29 | ₹33,533.47 | ₹32,469.93 | ₹6,458.72 | 9 | ₹153.13 |
| 2021-02-26 | ₹75,190.67 | ₹73,756.93 | ₹24,258.27 | 7 | ₹164.84 |
| 2021-03-26 | ₹1.12 lakh | ₹1.20 lakh | ₹37,875.64 | 8 | ₹157.68 |
| 2021-04-30 | ₹2.27 lakh | ₹2.21 lakh | ₹12,107.50 | 10 | ₹160.88 |
| 2021-05-28 | ₹3.63 lakh | ₹3.22 lakh | ₹0.00 | 11 | ₹179.09 |
| 2021-06-25 | ₹9.79 lakh | ₹8.54 lakh | ₹15,024.82 | 10 | ₹195.71 |
| 2021-07-30 | ₹30.84 lakh | ₹21.93 lakh | ₹15,024.82 | 10 | ₹235.11 |
| 2021-08-27 | ₹65.80 lakh | ₹61.00 lakh | ₹32.13 lakh | 6 | ₹225.77 |
| 2021-09-24 | ₹1.41 crore | ₹1.30 crore | ₹0.00 | 10 | ₹240.91 |
| 2021-10-29 | ₹3.15 crore | ₹3.19 crore | ₹1.07 crore | 7 | ₹238.34 |
| 2021-11-26 | ₹5.65 crore | ₹5.79 crore | ₹2.49 crore | 6 | ₹245.23 |
| 2021-12-31 | ₹12.73 crore | ₹11.97 crore | ₹0.00 | 10 | ₹256.28 |
| 2022-01-28 | ₹17.58 crore | ₹18.71 crore | ₹11.15 crore | 5 | ₹236.92 |
| 2022-02-25 | ₹22.79 crore | ₹25.36 crore | ₹12.52 crore | 4 | ₹222.22 |
| 2022-03-25 | ₹28.04 crore | ₹27.42 crore | ₹12.52 crore | 4 | ₹244.79 |
| 2022-04-29 | ₹60.78 crore | ₹53.26 crore | ₹0.00 | 8 | ₹261.86 |
| 2022-05-27 | ₹69.56 crore | ₹62.75 crore | ₹10.66 crore | 6 | ₹249.20 |
| 2022-06-24 | ₹104.65 crore | ₹101.47 crore | ₹1.32 crore | 7 | ₹245.76 |
| 2022-07-29 | ₹263.00 crore | ₹229.47 crore | ₹0.00 | 7 | ₹274.24 |
| 2022-08-26 | ₹635.68 crore | ₹584.30 crore | ₹194.95 crore | 5 | ₹293.42 |
| 2022-09-30 | ₹1,171.83 crore | ₹1,116.51 crore | ₹107.38 crore | 7 | ₹300.55 |
| 2022-10-28 | ₹2,553.85 crore | ₹2,469.11 crore | ₹0.00 | 8 | ₹299.16 |
| 2022-11-25 | ₹5,495.63 crore | ₹5,512.15 crore | ₹2,675.39 crore | 7 | ₹312.77 |
| 2022-12-30 | ₹10,264.92 crore | ₹9,530.84 crore | ₹4,689.86 crore | 6 | ₹316.25 |
| 2023-01-27 | ₹14,702.95 crore | ₹14,829.62 crore | ₹1,156.68 crore | 8 | ₹312.11 |
| 2023-02-24 | ₹24,619.26 crore | ₹25,432.54 crore | ₹5,535.19 crore | 7 | ₹307.72 |
| 2023-03-31 | ₹53,321.44 crore | ₹57,521.20 crore | ₹26,426.84 crore | 5 | ₹297.19 |
| 2023-04-28 | ₹77,139.40 crore | ₹79,879.52 crore | ₹32,062.97 crore | 7 | ₹299.95 |
| 2023-05-26 | ₹1.37 lakh crore | ₹1.31 lakh crore | ₹5,883.87 crore | 10 | ₹319.09 |
| 2023-06-30 | ₹3.36 lakh crore | ₹2.99 lakh crore | ₹4,428.48 crore | 10 | ₹355.41 |
| 2023-07-28 | ₹7.81 lakh crore | ₹7.12 lakh crore | ₹10,496.52 crore | 9 | ₹408.13 |
| 2023-08-25 | ₹13.27 lakh crore | ₹12.49 lakh crore | ₹49,876.87 crore | 8 | ₹411.51 |
| 2023-09-29 | ₹27.87 lakh crore | ₹25.79 lakh crore | ₹49,876.87 crore | 8 | ₹442.41 |
| 2023-10-27 | ₹43.13 lakh crore | ₹43.28 lakh crore | ₹15.21 lakh crore | 7 | ₹445.22 |
| 2023-11-24 | ₹1.45 crore crore | ₹1.42 crore crore | ₹2.19 lakh crore | 10 | ₹545.23 |
| 2023-12-29 | ₹2.37 crore crore | ₹2.25 crore crore | ₹2.19 lakh crore | 10 | ₹569.39 |
| 2024-01-25 | ₹4.33 crore crore | ₹4.04 crore crore | ₹91.03 lakh crore | 8 | ₹637.42 |
| 2024-02-23 | ₹8.81 crore crore | ₹7.93 crore crore | ₹22.83 lakh crore | 9 | ₹721.84 |
| 2024-03-28 | ₹13.49 crore crore | ₹13.32 crore crore | ₹0.00 | 11 | ₹714.58 |
| 2024-04-26 | ₹19.56 crore crore | ₹18.78 crore crore | ₹0.00 | 11 | ₹691.03 |
| 2024-05-31 | ₹39.22 crore crore | ₹39.17 crore crore | ₹5.17 crore crore | 10 | ₹667.04 |
| 2024-06-28 | ₹62.42 crore crore | ₹63.68 crore crore | ₹0.00 | 9 | ₹655.80 |
| 2024-07-26 | ₹107.63 crore crore | ₹107.15 crore crore | ₹23.32 crore crore | 7 | ₹679.15 |
| 2024-08-30 | ₹255.51 crore crore | ₹252.06 crore crore | ₹0.00 | 9 | ₹719.51 |
| 2024-09-27 | ₹370.55 crore crore | ₹388.53 crore crore | ₹60.53 crore crore | 7 | ₹696.12 |
| 2024-10-25 | ₹478.28 crore crore | ₹542.50 crore crore | ₹110.36 crore crore | 6 | ₹624.52 |
| 2024-11-29 | ₹1,134.06 crore crore | ₹1,127.84 crore crore | ₹0.00 | 8 | ₹671.33 |
| 2024-12-27 | ₹2,326.06 crore crore | ₹2,393.90 crore crore | ₹707.37 crore crore | 6 | ₹661.71 |
| 2025-01-24 | ₹4,019.82 crore crore | ₹4,630.53 crore crore | ₹2,647.83 crore crore | 4 | ₹598.60 |
| 2025-02-28 | ₹4,192.25 crore crore | ₹5,018.47 crore crore | ₹3,640.56 crore crore | 2 | ₹561.04 |
| 2025-03-28 | ₹5,226.56 crore crore | ₹5,904.44 crore crore | ₹2,699.18 crore crore | 4 | ₹576.77 |
| 2025-04-25 | ₹6,012.49 crore crore | ₹6,578.79 crore crore | ₹2,128.04 crore crore | 5 | ₹567.84 |
| 2025-05-30 | ₹11,445.25 crore crore | ₹11,676.01 crore crore | ₹0.00 | 9 | ₹605.96 |
| 2025-06-27 | ₹22,787.87 crore crore | ₹21,224.59 crore crore | ₹0.00 | 9 | ₹655.25 |
| 2025-07-25 | ₹1.06 lakh crore crore | ₹95,536.37 crore crore | ₹0.00 | 9 | ₹745.37 |
| 2025-08-29 | ₹1.27 lakh crore crore | ₹1.13 lakh crore crore | ₹13,749.21 crore crore | 6 | ₹745.56 |
| 2025-09-26 | ₹1.35 lakh crore crore | ₹1.28 lakh crore crore | ₹14,794.02 crore crore | 5 | ₹702.19 |
| 2025-10-31 | ₹2.25 lakh crore crore | ₹2.31 lakh crore crore | ₹76,788.63 crore crore | 6 | ₹672.46 |
| 2025-11-28 | ₹3.23 lakh crore crore | ₹3.42 lakh crore crore | ₹1.04 lakh crore crore | 8 | ₹662.80 |
| 2025-12-26 | ₹5.23 lakh crore crore | ₹5.47 lakh crore crore | ₹0.00 | 11 | ₹648.81 |
| 2026-01-30 | ₹8.51 lakh crore crore | ₹9.00 lakh crore crore | ₹3.41 lakh crore crore | 5 | ₹622.61 |
| 2026-02-27 | ₹14.62 lakh crore crore | ₹15.23 lakh crore crore | ₹3.78 lakh crore crore | 5 | ₹620.86 |
| 2026-03-27 | ₹21.66 lakh crore crore | ₹23.34 lakh crore crore | ₹7.80 lakh crore crore | 5 | ₹592.70 |
| 2026-04-24 | ₹31.84 lakh crore crore | ₹30.12 lakh crore crore | ₹29,081.85 crore crore | 7 | ₹620.65 |
| 2026-05-29 | ₹103.36 lakh crore crore | ₹95.57 lakh crore crore | ₹0.00 | 10 | ₹641.48 |
| 2026-06-26 | ₹193.87 lakh crore crore | ₹182.43 lakh crore crore | ₹8.16 lakh crore crore | 8 | ₹665.71 |
| 2026-07-31 | ₹468.41 lakh crore crore | ₹465.47 lakh crore crore | ₹36.97 lakh crore crore | 7 | ₹721.02 |
| 2026-08-28 | ₹716.74 lakh crore crore | ₹701.20 lakh crore crore | ₹0.00 | 8 | ₹750.33 |
| 2026-09-11 | ₹897.23 lakh crore crore | ₹842.65 lakh crore crore | ₹64.03 lakh crore crore | 7 | ₹788.82 |

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
2020-06-08  EIDPARRY    BUY ₹10.00 at ₹219.00 (fresh Friday signal — BUY: 4.34× weekly, month 3.59×, ladder rising; stop ₹132.60; charges ₹0.01)
2020-06-08  IGL         BUY ₹9.95 at ₹247.75 (fresh Friday signal — BUY: 1.53× weekly, month 1.89×, ladder rising; stop ₹208.81; charges ₹0.01)
2020-06-08  KIRLOSBROS  BUY ₹9.96 at ₹106.50 (fresh Friday signal — ACCUMULATE: 2.95× weekly, month 1.69×, ladder rising; stop ₹91.63; charges ₹0.01)
2020-06-08  LLOYDSENGG  BUY ₹10.00 at ₹0.87 (fresh Friday signal — BUY: 4.83× weekly, month 4.76×, ladder rising; stop ₹0.46; charges ₹0.01)
2020-06-08  RCF         BUY ₹10.02 at ₹45.20 (fresh Friday signal — BUY: 2.38× weekly, month 2.29×, ladder rising; stop ₹35.25; charges ₹0.01)
2020-06-08  RELAXO      BUY ₹10.00 at ₹759.45 (fresh Friday signal — BUY: 1.89× weekly, month 1.81×, ladder rising; stop ₹603.77; charges ₹0.01)
2020-06-08  SYNGENE     BUY ₹9.95 at ₹373.90 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 2.27×, ladder rising; stop ₹323.19; charges ₹0.01)
2020-06-15  ADVENZYMES  BUY ₹10.89 at ₹172.70 (fresh Friday signal — BUY: 4.13× weekly, month 2.92×, ladder rising; stop ₹126.20; charges ₹0.01)
2020-06-15  CAPLIPOINT  BUY ₹10.84 at ₹383.80 (fresh Friday signal — BUY: 5.39× weekly, month 2.09×, ladder rising; stop ₹291.46; charges ₹0.01)
2020-06-15  GRANULES    BUY ₹8.39 at ₹216.75 (fresh Friday signal — BUY: 3.46× weekly, month 2.65×, ladder rising; stop ₹170.34; charges ₹0.01)
2020-06-15  RCF         PYRAMID BUY ₹9.95 at ₹44.95 (box jump — doubling the stake with NEW capital; stop stays ₹40.28; charges ₹0.01)
2020-06-22  ADVENZYMES  PYRAMID BUY ₹10.67 at ₹169.35 (box jump — doubling the stake with NEW capital; stop stays ₹149.98; charges ₹0.01)
2020-06-22  EIDPARRY    PYRAMID BUY ₹12.20 at ₹267.45 (box jump — doubling the stake with NEW capital; stop stays ₹204.49; charges ₹0.01)
2020-06-22  LLOYDSENGG  PYRAMID BUY ₹12.21 at ₹1.06 (box jump — doubling the stake with NEW capital; stop stays ₹0.71; charges ₹0.01)
2020-06-29  EIDPARRY    PYRAMID BUY ₹24.79 at ₹272.00 (box jump — doubling the stake with NEW capital; stop stays ₹249.19; charges ₹0.03)
2020-06-29  GRANULES    PYRAMID BUY ₹7.93 at ₹205.00 (box jump — doubling the stake with NEW capital; stop stays ₹190.95; charges ₹0.01)
2020-06-29  KIRLOSBROS  PYRAMID BUY ₹11.12 at ₹119.05 (box jump — doubling the stake with NEW capital; stop stays ₹93.65; charges ₹0.01)
2020-07-06  RCF         PYRAMID BUY ₹21.13 at ₹47.75 (box jump — doubling the stake with NEW capital; stop stays ₹43.23; charges ₹0.03)
2020-07-06  SYNGENE     PYRAMID BUY ₹11.64 at ₹438.00 (box jump — doubling the stake with NEW capital; stop stays ₹375.25; charges ₹0.01)
2020-07-07  IGL         SELL ₹8.36 at stop ₹208.81 (-15.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-07-13  GRANULES    PYRAMID BUY ₹18.25 at ₹236.20 (box jump — doubling the stake with NEW capital; stop stays ₹194.80; charges ₹0.02)
2020-07-20  KIRLOSBROS  PYRAMID BUY ₹20.91 at ₹112.00 (box jump — doubling the stake with NEW capital; stop stays ₹97.15; charges ₹0.02)
2020-07-27  EIDPARRY    PYRAMID BUY ₹53.57 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹273.03; charges ₹0.06)
2020-07-27  RCF         PYRAMID BUY ₹43.87 at ₹49.60 (box jump — doubling the stake with NEW capital; stop stays ₹43.37; charges ₹0.05)
2020-07-28  RELAXO      SELL ₹7.93 at stop ₹603.77 (-20.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-07-31  LLOYDSENGG  SELL ₹16.36 at stop ₹0.71 (-26.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-08-03  ZENTEC      BUY ₹32.65 at ₹58.80 (fresh Friday signal — ACCUMULATE: 4.33× weekly, month 4.91×, ladder rising; stop ₹42.67; charges ₹0.04)
2020-08-10  GRANULES    PYRAMID BUY ₹49.28 at ₹319.00 (box jump — doubling the stake with NEW capital; stop stays ₹257.64; charges ₹0.06)
2020-08-10  KIRLOSBROS  PYRAMID BUY ₹53.91 at ₹144.45 (box jump — doubling the stake with NEW capital; stop stays ₹119.79; charges ₹0.06)
2020-08-10  RCF         PYRAMID BUY ₹91.49 at ₹51.75 (box jump — doubling the stake with NEW capital; stop stays ₹43.89; charges ₹0.11)
2020-08-17  ADVENZYMES  PYRAMID BUY ₹28.19 at ₹223.90 (box jump — doubling the stake with NEW capital; stop stays ₹194.75; charges ₹0.03)
2020-08-17  EIDPARRY    SELL ₹99.33 at stop ₹273.03 (-1.0%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2020-08-17  SYNGENE     PYRAMID BUY ₹26.23 at ₹493.80 (box jump — doubling the stake with NEW capital; stop stays ₹434.44; charges ₹0.03)
2020-08-24  CAPLIPOINT  PYRAMID BUY ₹15.26 at ₹540.80 (box jump — doubling the stake with NEW capital; stop stays ₹454.79; charges ₹0.02)
2020-08-24  KIRLOSBROS  PYRAMID BUY ₹98.51 at ₹132.05 (box jump — doubling the stake with NEW capital; stop stays ₹120.79; charges ₹0.12)
2020-08-24  RCF         PYRAMID BUY ₹175.98 at ₹49.80 (box jump — doubling the stake with NEW capital; stop stays ₹45.84; charges ₹0.21)
2020-08-24  THYROCARE   BUY ₹99.29 at ₹263.35 (fresh Friday signal — BUY: 7.09× weekly, month 4.48×, ladder rising; stop ₹199.77; charges ₹0.12)
2020-08-24  ZENTEC      PYRAMID BUY ₹50.20 at ₹90.50 (box jump — doubling the stake with NEW capital; stop stays ₹80.56; charges ₹0.06)
2020-08-31  GRANULES    PYRAMID BUY ₹96.35 at ₹312.05 (box jump — doubling the stake with NEW capital; stop stays ₹286.95; charges ₹0.11)
2020-08-31  GRANULES    SELL ₹176.92 at stop ₹286.95 (-1.6%, charges ₹0.18) — the cash goes back to work at the next Friday screen
2020-08-31  ZENTEC      SELL ₹89.23 at stop ₹80.56 (+7.9%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2020-09-07  INDIAMART   BUY ₹111.06 at ₹2,124.50 (fresh Friday signal — BUY: 2.46× weekly, month 1.96×, ladder rising; stop ₹1,655.61; charges ₹0.13)
2020-09-07  POLYMED     BUY ₹111.77 at ₹449.70 (fresh Friday signal — BUY: 2.13× weekly, month 2.66×, ladder rising; stop ₹372.40; charges ₹0.13)
2020-09-07  THYROCARE   PYRAMID BUY ₹94.77 at ₹251.67 (box jump — doubling the stake with NEW capital; stop stays ₹235.03; charges ₹0.11)
2020-09-08  KIRLOSBROS  SELL ₹179.92 at stop ₹120.79 (-7.2%, charges ₹0.19) — the cash goes back to work at the next Friday screen
2020-09-09  RCF         SELL ₹323.44 at stop ₹45.84 (-8.0%, charges ₹0.34) — the cash goes back to work at the next Friday screen
2020-09-14  ATGL        BUY ₹127.05 at ₹209.75 (fresh Friday signal — BUY: 1.66× weekly, month 1.67×, ladder rising; stop ₹159.58; charges ₹0.15)
2020-09-14  GLAXO       BUY ₹126.54 at ₹1,675.00 (fresh Friday signal — BUY: 2.55× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.15)
2020-09-14  POLYMED     PYRAMID BUY ₹119.65 at ₹481.95 (box jump — doubling the stake with NEW capital; stop stays ₹408.50; charges ₹0.14)
2020-09-14  SCHAEFFLER  BUY ₹126.92 at ₹814.00 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 1.89×, ladder rising; stop ₹724.67; charges ₹0.15)
2020-09-21  ADVENZYMES  PYRAMID BUY ₹63.64 at ₹252.85 (box jump — doubling the stake with NEW capital; stop stays ₹212.37; charges ₹0.08)
2020-09-21  CAPLIPOINT  PYRAMID BUY ₹33.95 at ₹602.00 (box jump — doubling the stake with NEW capital; stop stays ₹486.88; charges ₹0.04)
2020-09-21  INDIAMART   PYRAMID BUY ₹131.64 at ₹2,521.27 (box jump — doubling the stake with NEW capital; stop stays ₹2,099.50; charges ₹0.16)
2020-09-21  LINDEINDIA  BUY ₹145.13 at ₹826.00 (fresh Friday signal — BUY: 4.50× weekly, month 2.39×, ladder rising; stop ₹641.27; charges ₹0.17)
2020-09-23  SCHAEFFLER  SELL ₹112.74 at stop ₹724.67 (-11.0%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2020-09-28  CAPLIPOINT  PYRAMID BUY ₹63.13 at ₹560.00 (box jump — doubling the stake with NEW capital; stop stays ₹498.06; charges ₹0.07)
2020-09-28  HCLTECH     BUY ₹133.80 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.16)
2020-09-28  SYNGENE     PYRAMID BUY ₹62.25 at ₹586.30 (box jump — doubling the stake with NEW capital; stop stays ₹501.60; charges ₹0.07)
2020-10-05  ATGL        PYRAMID BUY ₹117.98 at ₹195.00 (box jump — doubling the stake with NEW capital; stop stays ₹162.03; charges ₹0.14)
2020-10-05  GLAXO       PYRAMID BUY ₹118.47 at ₹1,570.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,441.55; charges ₹0.14)
2020-10-05  LINDEINDIA  PYRAMID BUY ₹142.51 at ₹812.00 (box jump — doubling the stake with NEW capital; stop stays ₹658.50; charges ₹0.17)
2020-10-05  POLYMED     PYRAMID BUY ₹233.40 at ₹470.35 (box jump — doubling the stake with NEW capital; stop stays ₹420.11; charges ₹0.28)
2020-10-12  HCLTECH     PYRAMID BUY ₹137.21 at ₹860.80 (box jump — doubling the stake with NEW capital; stop stays ₹766.75; charges ₹0.16)
2020-10-12  INDIAMART   PYRAMID BUY ₹263.00 at ₹2,520.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,315.62; charges ₹0.31)
2020-10-19  INDIAMART   SELL ₹482.55 at stop ₹2,315.62 (-4.4%, charges ₹0.50) — the cash goes back to work at the next Friday screen
2020-10-19  THYROCARE   PYRAMID BUY ₹259.55 at ₹344.82 (box jump — doubling the stake with NEW capital; stop stays ₹311.14; charges ₹0.31)
2020-10-26  ADVENZYMES  PYRAMID BUY ₹158.68 at ₹315.40 (box jump — doubling the stake with NEW capital; stop stays ₹292.33; charges ₹0.19)
2020-10-26  HCLTECH     PYRAMID BUY ₹271.78 at ₹853.00 (box jump — doubling the stake with NEW capital; stop stays ₹779.57; charges ₹0.32)
2020-10-26  JUSTDIAL    BUY ₹337.45 at ₹584.00 (fresh Friday signal — BUY: 4.99× weekly, month 1.82×, ladder rising; stop ₹383.80; charges ₹0.40)
2020-10-30  CAPLIPOINT  SELL ₹112.11 at stop ₹498.06 (-8.8%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹217.19 at stop ₹1,441.55 (-11.2%, charges ₹0.23) — the cash goes back to work at the next Friday screen
2020-11-02  KPRMILL     BUY ₹257.21 at ₹151.00 (fresh Friday signal — BUY: 2.37× weekly, month 3.11×, ladder rising; stop ₹108.58; charges ₹0.30)
2020-11-03  ADVENZYMES  SELL ₹293.66 at stop ₹292.33 (+8.2%, charges ₹0.30) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹428.15 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 1.65×, ladder rising; stop ₹77.16; charges ₹0.51)
2020-11-09  KPRMILL     PYRAMID BUY ₹265.42 at ₹156.00 (box jump — doubling the stake with NEW capital; stop stays ₹134.58; charges ₹0.31)
2020-11-09  THYROCARE   PYRAMID BUY ₹570.57 at ₹379.23 (box jump — doubling the stake with NEW capital; stop stays ₹338.83; charges ₹0.68)
2020-11-12  THYROCARE   SELL ₹1,017.91 at stop ₹338.83 (-0.4%, charges ₹1.06) — the cash goes back to work at the next Friday screen
2020-11-17  ATGL        PYRAMID BUY ₹297.80 at ₹246.25 (box jump — doubling the stake with NEW capital; stop stays ₹219.69; charges ₹0.35)
2020-11-17  JUSTDIAL    PYRAMID BUY ₹360.71 at ₹625.00 (box jump — doubling the stake with NEW capital; stop stays ₹523.11; charges ₹0.43)
2020-11-17  PIIND       BUY ₹502.14 at ₹2,348.20 (fresh Friday signal — ACCUMULATE: 1.62× weekly, month 1.81×, ladder rising; stop ₹2,107.67; charges ₹0.59)
2020-11-17  TRENT       BUY ₹502.95 at ₹755.00 (fresh Friday signal — ACCUMULATE: 3.32× weekly, month 1.93×, ladder rising; stop ₹551.90; charges ₹0.60)
2020-11-23  LINDEINDIA  PYRAMID BUY ₹314.03 at ₹895.20 (box jump — doubling the stake with NEW capital; stop stays ₹769.64; charges ₹0.37)
2020-12-01  BORORENEW   PYRAMID BUY ₹544.74 at ₹127.00 (box jump — doubling the stake with NEW capital; stop stays ₹106.40; charges ₹0.65)
2020-12-01  KPRMILL     PYRAMID BUY ₹535.31 at ₹157.41 (box jump — doubling the stake with NEW capital; stop stays ₹148.69; charges ₹0.63)
2020-12-07  ATGL        PYRAMID BUY ₹875.28 at ₹362.10 (box jump — doubling the stake with NEW capital; stop stays ₹295.81; charges ₹1.04)
2020-12-14  BORORENEW   PYRAMID BUY ₹1,139.85 at ₹132.95 (box jump — doubling the stake with NEW capital; stop stays ₹123.97; charges ₹1.35)
2020-12-14  TRENT       PYRAMID BUY ₹462.43 at ₹695.00 (box jump — doubling the stake with NEW capital; stop stays ₹626.30; charges ₹0.55)
2020-12-21  ATGL        PYRAMID BUY ₹1,738.17 at ₹359.75 (box jump — doubling the stake with NEW capital; stop stays ₹332.60; charges ₹2.06)
2020-12-21  ATGL        SELL ₹3,208.76 at stop ₹332.60 (+1.9%, charges ₹3.33) — the cash goes back to work at the next Friday screen
2020-12-21  KPRMILL     PYRAMID BUY ₹1,291.52 at ₹190.00 (box jump — doubling the stake with NEW capital; stop stays ₹156.39; charges ₹1.53)
2020-12-21  LINDEINDIA  PYRAMID BUY ₹662.57 at ₹944.95 (box jump — doubling the stake with NEW capital; stop stays ₹868.06; charges ₹0.79)
2020-12-21  SYNGENE     PYRAMID BUY ₹129.47 at ₹610.00 (box jump — doubling the stake with NEW capital; stop stays ₹562.40; charges ₹0.15)
2020-12-22  SYNGENE     SELL ₹238.34 at stop ₹562.40 (-0.3%, charges ₹0.25) — the cash goes back to work at the next Friday screen
2020-12-28  BORORENEW   PYRAMID BUY ₹4,027.16 at ₹235.00 (box jump — doubling the stake with NEW capital; stop stays ₹148.20; charges ₹4.77)
2020-12-28  GRAVITA     BUY ₹1,620.06 at ₹69.65 (fresh Friday signal — BUY: 2.45× weekly, month 4.29×, ladder rising; stop ₹46.41; charges ₹1.92)
2020-12-28  HONAUT      BUY ₹1,922.55 at ₹38,887.75 (fresh Friday signal — BUY: 5.49× weekly, month 1.69×, ladder rising; stop ₹29,024.49; charges ₹2.28)
2021-01-04  LINDEINDIA  PYRAMID BUY ₹1,367.87 at ₹976.00 (box jump — doubling the stake with NEW capital; stop stays ₹898.70; charges ₹1.62)
2021-01-11  HONAUT      PYRAMID BUY ₹2,024.57 at ₹41,000.00 (box jump — doubling the stake with NEW capital; stop stays ₹34,722.50; charges ₹2.40)
2021-01-18  BORORENEW   PYRAMID BUY ₹9,419.69 at ₹275.00 (box jump — doubling the stake with NEW capital; stop stays ₹247.59; charges ₹11.16)
2021-01-18  GRAVITA     PYRAMID BUY ₹1,816.78 at ₹78.20 (box jump — doubling the stake with NEW capital; stop stays ₹70.89; charges ₹2.15)
2021-01-20  BORORENEW   SELL ₹16,934.00 at stop ₹247.59 (+9.1%, charges ₹17.57) — the cash goes back to work at the next Friday screen
2021-01-25  GABRIEL     BUY ₹3,360.42 at ₹114.60 (fresh Friday signal — ACCUMULATE: 1.54× weekly, month 3.77×, ladder rising; stop ₹86.90; charges ₹3.98)
2021-01-25  HCLTECH     PYRAMID BUY ₹634.95 at ₹997.00 (box jump — doubling the stake with NEW capital; stop stays ₹928.05; charges ₹0.75)
2021-01-25  HINDZINC    BUY ₹3,375.96 at ₹277.40 (fresh Friday signal — ACCUMULATE: 2.31× weekly, month 2.09×, ladder rising; stop ₹248.97; charges ₹4.00)
2021-01-25  INDIAMART   BUY ₹3,383.96 at ₹3,990.00 (fresh Friday signal — BUY: 2.37× weekly, month 1.58×, ladder rising; stop ₹3,323.20; charges ₹4.01)
2021-01-25  JUSTDIAL    PYRAMID BUY ₹775.79 at ₹672.50 (box jump — doubling the stake with NEW capital; stop stays ₹622.35; charges ₹0.92)
2021-01-25  JUSTDIAL    SELL ₹1,433.54 at stop ₹622.35 (-2.5%, charges ₹1.49) — the cash goes back to work at the next Friday screen
2021-01-25  PIIND       SELL ₹449.71 at stop ₹2,107.67 (-10.2%, charges ₹0.47) — the cash goes back to work at the next Friday screen
2021-01-25  TATAELXSI   BUY ₹3,401.20 at ₹2,608.00 (fresh Friday signal — BUY: 2.94× weekly, month 2.74×, ladder rising; stop ₹1,712.61; charges ₹4.03)
2021-01-25  WHIRLPOOL   BUY ₹3,364.20 at ₹2,697.50 (fresh Friday signal — BUY: 1.73× weekly, month 2.10×, ladder rising; stop ₹2,244.99; charges ₹3.99)
2021-01-27  LINDEINDIA  SELL ₹2,514.96 at stop ₹898.70 (-4.2%, charges ₹2.61) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹1,180.15 at stop ₹928.05 (+0.4%, charges ₹1.22) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹832.09 at stop ₹626.30 (-13.6%, charges ₹0.86) — the cash goes back to work at the next Friday screen
2021-02-01  GAEL        BUY ₹4,406.95 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹5.22)
2021-02-01  INDIAMART   PYRAMID BUY ₹3,328.34 at ₹3,929.07 (box jump — doubling the stake with NEW capital; stop stays ₹3,460.38; charges ₹3.94)
2021-02-01  KPRMILL     PYRAMID BUY ₹2,485.45 at ₹182.93 (box jump — doubling the stake with NEW capital; stop stays ₹166.62; charges ₹2.94)
2021-02-01  TATAELXSI   PYRAMID BUY ₹3,532.31 at ₹2,711.75 (box jump — doubling the stake with NEW capital; stop stays ₹2,275.70; charges ₹4.19)
2021-02-08  HONAUT      PYRAMID BUY ₹4,145.35 at ₹41,999.00 (box jump — doubling the stake with NEW capital; stop stays ₹35,971.61; charges ₹4.91)
2021-02-15  HINDZINC    PYRAMID BUY ₹3,647.89 at ₹300.10 (box jump — doubling the stake with NEW capital; stop stays ₹279.30; charges ₹4.32)
2021-02-15  INDIAMART   PYRAMID BUY ₹7,846.82 at ₹4,634.30 (box jump — doubling the stake with NEW capital; stop stays ₹4,137.25; charges ₹9.30)
2021-02-15  TATAELXSI   PYRAMID BUY ₹7,422.99 at ₹2,851.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,660.00; charges ₹8.79)
2021-02-22  HONAUT      PYRAMID BUY ₹8,877.83 at ₹45,000.00 (box jump — doubling the stake with NEW capital; stop stays ₹39,140.00; charges ₹10.52)
2021-02-22  TATAELXSI   SELL ₹13,828.84 at stop ₹2,660.00 (-3.5%, charges ₹14.34) — the cash goes back to work at the next Friday screen
2021-02-23  GAEL        SELL ₹3,857.33 at stop ₹62.70 (-12.3%, charges ₹4.00) — the cash goes back to work at the next Friday screen
2021-02-24  KPRMILL     SELL ₹4,520.33 at stop ₹166.62 (-6.3%, charges ₹4.69) — the cash goes back to work at the next Friday screen
2021-03-01  IOB         BUY ₹7,742.13 at ₹18.90 (fresh Friday signal — ACCUMULATE: 3.52× weekly, month 9.60×, ladder rising; stop ₹13.70; charges ₹9.17)
2021-03-01  MAHABANK    BUY ₹7,696.21 at ₹25.20 (fresh Friday signal — ACCUMULATE: 3.28× weekly, month 6.34×, ladder rising; stop ₹18.37; charges ₹9.12)
2021-03-01  RCF         BUY ₹7,637.67 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.12×, ladder rising; stop ₹50.16; charges ₹9.05)
2021-03-02  INDIAMART   SELL ₹13,987.62 at stop ₹4,137.25 (-3.7%, charges ₹14.51) — the cash goes back to work at the next Friday screen
2021-03-08  HONAUT      PYRAMID BUY ₹18,631.97 at ₹47,248.90 (box jump — doubling the stake with NEW capital; stop stays ₹41,911.15; charges ₹22.08)
2021-03-08  JSWENERGY   BUY ₹9,639.02 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.49×, ladder rising; stop ₹65.79; charges ₹11.42)
2021-03-08  POLYMED     PYRAMID BUY ₹713.04 at ₹718.90 (box jump — doubling the stake with NEW capital; stop stays ₹642.77; charges ₹0.84)
2021-03-08  SJVN        BUY ₹5,530.86 at ₹27.35 (fresh Friday signal — ACCUMULATE: 2.55× weekly, month 2.70×, ladder rising; stop ₹23.89; charges ₹6.55)
2021-03-15  GRAVITA     PYRAMID BUY ₹5,010.59 at ₹107.90 (box jump — doubling the stake with NEW capital; stop stays ₹96.13; charges ₹5.94)
2021-03-15  JSWENERGY   PYRAMID BUY ₹10,056.93 at ₹85.50 (box jump — doubling the stake with NEW capital; stop stays ₹76.43; charges ₹11.92)
2021-03-15  RCF         PYRAMID BUY ₹8,181.69 at ₹85.80 (box jump — doubling the stake with NEW capital; stop stays ₹79.16; charges ₹9.69)
2021-03-17  GRAVITA     SELL ₹8,913.51 at stop ₹96.13 (+5.8%, charges ₹9.25) — the cash goes back to work at the next Friday screen
2021-03-17  RCF         SELL ₹15,072.46 at stop ₹79.16 (-4.5%, charges ₹15.63) — the cash goes back to work at the next Friday screen
2021-03-19  HINDZINC    SELL ₹6,779.06 at stop ₹279.30 (-3.3%, charges ₹7.03) — the cash goes back to work at the next Friday screen
2021-03-19  MAHABANK    SELL ₹5,597.84 at stop ₹18.37 (-27.1%, charges ₹5.81) — the cash goes back to work at the next Friday screen
2021-03-22  DEEPAKFERT  BUY ₹11,449.23 at ₹237.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.82×, ladder rising; stop ₹184.78; charges ₹13.57)
2021-03-22  GABRIEL     PYRAMID BUY ₹3,242.21 at ₹110.70 (box jump — doubling the stake with NEW capital; stop stays ₹86.92; charges ₹3.84)
2021-03-22  HONAUT      SELL ₹33,000.40 at stop ₹41,911.15 (-7.1%, charges ₹34.23) — the cash goes back to work at the next Friday screen
2021-03-22  KEI         BUY ₹11,387.06 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹13.49)
2021-03-22  WELSPUNLIV  BUY ₹11,444.97 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.45×, ladder rising; stop ₹67.45; charges ₹13.56)
2021-03-24  WHIRLPOOL   SELL ₹2,793.63 at stop ₹2,244.99 (-16.8%, charges ₹2.90) — the cash goes back to work at the next Friday screen
2021-03-30  DEEPAKFERT  PYRAMID BUY ₹10,767.38 at ₹223.15 (box jump — doubling the stake with NEW capital; stop stays ₹209.52; charges ₹12.76)
2021-03-30  KEI         PYRAMID BUY ₹11,334.35 at ₹520.20 (box jump — doubling the stake with NEW capital; stop stays ₹471.20; charges ₹13.43)
2021-03-30  KPITTECH    BUY ₹14,789.34 at ₹182.00 (fresh Friday signal — BUY: 1.71× weekly, month 2.75×, ladder rising; stop ₹136.62; charges ₹17.52)
2021-03-30  POLYMED     PYRAMID BUY ₹1,616.65 at ₹815.45 (box jump — doubling the stake with NEW capital; stop stays ₹719.96; charges ₹1.92)
2021-03-30  WELSPUNLIV  PYRAMID BUY ₹11,789.30 at ₹84.00 (box jump — doubling the stake with NEW capital; stop stays ₹68.17; charges ₹13.97)
2021-04-01  TAX         FY2021 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹6,471.72 / LT ₹0.00)
2021-04-05  AUBANK      BUY ₹15,299.85 at ₹631.00 (fresh Friday signal — ACCUMULATE: 3.80× weekly, month 2.02×, ladder rising; stop ₹533.06; charges ₹18.13)
2021-04-05  GICRE       BUY ₹7,786.45 at ₹205.90 (fresh Friday signal — BUY: 1.92× weekly, month 3.20×, ladder rising; stop ₹157.44; charges ₹9.23)
2021-04-05  IOB         PYRAMID BUY ₹6,894.20 at ₹16.85 (box jump — doubling the stake with NEW capital; stop stays ₹14.82; charges ₹8.17)
2021-04-12  AUBANK      SELL ₹12,896.40 at stop ₹533.06 (-15.5%, charges ₹13.38) — the cash goes back to work at the next Friday screen
2021-04-12  GICRE       PYRAMID BUY ₹7,705.46 at ₹204.00 (box jump — doubling the stake with NEW capital; stop stays ₹164.12; charges ₹9.13)
2021-04-19  JSWENERGY   PYRAMID BUY ₹22,382.51 at ₹95.20 (box jump — doubling the stake with NEW capital; stop stays ₹81.99; charges ₹26.52)
2021-04-19  KPITTECH    PYRAMID BUY ₹15,400.84 at ₹189.75 (box jump — doubling the stake with NEW capital; stop stays ₹171.05; charges ₹18.25)
2021-04-19  KPRMILL     BUY ₹12,896.40 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹15.28)
2021-04-26  KPRMILL     PYRAMID BUY ₹13,295.39 at ₹243.59 (box jump — doubling the stake with NEW capital; stop stays ₹221.37; charges ₹15.75)
2021-04-28  IOB         SELL ₹12,107.50 at stop ₹14.82 (-17.1%, charges ₹12.56) — the cash goes back to work at the next Friday screen
2021-05-03  MARKSANS    BUY ₹12,107.50 at ₹70.95 (fresh Friday signal — ACCUMULATE: 3.13× weekly, month 3.97×, ladder rising; stop ₹64.12; charges ₹14.35)
2021-05-10  KEI         PYRAMID BUY ₹23,016.74 at ₹528.50 (box jump — doubling the stake with NEW capital; stop stays ₹485.02; charges ₹27.27)
2021-05-17  KPRMILL     PYRAMID BUY ₹32,074.64 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹268.28; charges ₹38.00)
2021-05-17  POLYMED     PYRAMID BUY ₹3,979.34 at ₹1,004.20 (box jump — doubling the stake with NEW capital; stop stays ₹902.50; charges ₹4.71)
2021-05-24  DEEPAKFERT  PYRAMID BUY ₹28,933.90 at ₹300.00 (box jump — doubling the stake with NEW capital; stop stays ₹264.10; charges ₹34.28)
2021-05-24  MARKSANS    PYRAMID BUY ₹12,774.94 at ₹74.95 (box jump — doubling the stake with NEW capital; stop stays ₹68.02; charges ₹15.14)
2021-05-31  KEI         PYRAMID BUY ₹54,319.54 at ₹624.00 (box jump — doubling the stake with NEW capital; stop stays ₹558.60; charges ₹64.36)
2021-05-31  SJVN        PYRAMID BUY ₹5,483.91 at ₹27.15 (box jump — doubling the stake with NEW capital; stop stays ₹25.13; charges ₹6.50)
2021-06-07  DEEPAKFERT  PYRAMID BUY ₹57,255.19 at ₹297.00 (box jump — doubling the stake with NEW capital; stop stays ₹269.80; charges ₹67.84)
2021-06-07  JSWENERGY   PYRAMID BUY ₹64,100.13 at ₹136.40 (box jump — doubling the stake with NEW capital; stop stays ₹108.49; charges ₹75.95)
2021-06-07  KPITTECH    PYRAMID BUY ₹39,406.04 at ₹242.90 (box jump — doubling the stake with NEW capital; stop stays ₹214.70; charges ₹46.69)
2021-06-07  POLYMED     PYRAMID BUY ₹7,984.46 at ₹1,008.05 (box jump — doubling the stake with NEW capital; stop stays ₹950.00; charges ₹9.46)
2021-06-07  WELSPUNLIV  PYRAMID BUY ₹26,061.37 at ₹92.90 (box jump — doubling the stake with NEW capital; stop stays ₹80.48; charges ₹30.88)
2021-06-14  JSWENERGY   PYRAMID BUY ₹1.47 lakh at ₹156.95 (box jump — doubling the stake with NEW capital; stop stays ₹126.83; charges ₹174.68)
2021-06-14  POLYMED     SELL ₹15,024.82 at stop ₹950.00 (+2.0%, charges ₹15.59) — the cash goes back to work at the next Friday screen
2021-06-21  KEI         PYRAMID BUY ₹1.19 lakh at ₹682.20 (box jump — doubling the stake with NEW capital; stop stays ₹608.00; charges ₹140.64)
2021-06-21  SJVN        PYRAMID BUY ₹11,425.62 at ₹28.30 (box jump — doubling the stake with NEW capital; stop stays ₹26.98; charges ₹13.54)
2021-06-28  JSWENERGY   PYRAMID BUY ₹2.89 lakh at ₹154.10 (box jump — doubling the stake with NEW capital; stop stays ₹138.04; charges ₹342.80)
2021-06-28  MARKSANS    PYRAMID BUY ₹29,810.42 at ₹87.50 (box jump — doubling the stake with NEW capital; stop stays ₹76.87; charges ₹35.32)
2021-07-05  DEEPAKFERT  PYRAMID BUY ₹1.52 lakh at ₹395.00 (box jump — doubling the stake with NEW capital; stop stays ₹364.65; charges ₹180.34)
2021-07-12  JSWENERGY   PYRAMID BUY ₹6.30 lakh at ₹168.00 (box jump — doubling the stake with NEW capital; stop stays ₹154.47; charges ₹747.01)
2021-07-19  KPITTECH    PYRAMID BUY ₹86,596.52 at ₹267.05 (box jump — doubling the stake with NEW capital; stop stays ₹232.94; charges ₹102.60)
2021-07-19  KPRMILL     PYRAMID BUY ₹81,120.38 at ₹372.00 (box jump — doubling the stake with NEW capital; stop stays ₹333.07; charges ₹96.11)
2021-07-19  WELSPUNLIV  PYRAMID BUY ₹70,063.27 at ₹124.95 (box jump — doubling the stake with NEW capital; stop stays ₹97.56; charges ₹83.01)
2021-08-02  WELSPUNLIV  PYRAMID BUY ₹1.51 lakh at ₹134.75 (box jump — doubling the stake with NEW capital; stop stays ₹117.99; charges ₹178.94)
2021-08-09  JSWENERGY   PYRAMID BUY ₹18.98 lakh at ₹253.00 (box jump — doubling the stake with NEW capital; stop stays ₹228.00; charges ₹2,248.58)
2021-08-09  KPITTECH    PYRAMID BUY ₹2.03 lakh at ₹312.45 (box jump — doubling the stake with NEW capital; stop stays ₹266.76; charges ₹239.95)
2021-08-09  KPRMILL     PYRAMID BUY ₹1.74 lakh at ₹399.60 (box jump — doubling the stake with NEW capital; stop stays ₹352.48; charges ₹206.37)
2021-08-09  MARKSANS    PYRAMID BUY ₹57,202.09 at ₹84.00 (box jump — doubling the stake with NEW capital; stop stays ₹77.14; charges ₹67.77)
2021-08-09  WELSPUNLIV  PYRAMID BUY ₹3.04 lakh at ₹135.90 (box jump — doubling the stake with NEW capital; stop stays ₹124.64; charges ₹360.72)
2021-08-10  MARKSANS    SELL ₹1.05 lakh at stop ₹77.14 (-6.1%, charges ₹108.80) — the cash goes back to work at the next Friday screen
2021-08-10  SJVN        SELL ₹21,749.92 at stop ₹26.98 (-2.9%, charges ₹22.56) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNLIV  SELL ₹5.58 lakh at stop ₹124.64 (-2.8%, charges ₹578.34) — the cash goes back to work at the next Friday screen
2021-08-11  GICRE       SELL ₹12,378.05 at stop ₹164.12 (-19.9%, charges ₹12.84) — the cash goes back to work at the next Friday screen
2021-08-11  JSWENERGY   SELL ₹34.15 lakh at stop ₹228.00 (+11.4%, charges ₹3,542.40) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹3.07 lakh at stop ₹352.48 (-1.9%, charges ₹318.22) — the cash goes back to work at the next Friday screen
2021-08-16  GABRIEL     PYRAMID BUY ₹8,740.29 at ₹149.30 (box jump — doubling the stake with NEW capital; stop stays ₹118.77; charges ₹10.36)
2021-08-16  KEI         PYRAMID BUY ₹2.59 lakh at ₹744.95 (box jump — doubling the stake with NEW capital; stop stays ₹663.29; charges ₹306.97)
2021-08-16  TATAINVEST  BUY ₹5.76 lakh at ₹130.81 (fresh Friday signal — BUY: 8.45× weekly, month 4.82×, ladder rising; stop ₹103.11; charges ₹682.21)
2021-08-23  DEEPAKFERT  PYRAMID BUY ₹3.09 lakh at ₹401.00 (box jump — doubling the stake with NEW capital; stop stays ₹380.00; charges ₹365.93)
2021-08-23  GRAVITA     BUY ₹6.45 lakh at ₹188.60 (fresh Friday signal — BUY: 2.16× weekly, month 1.88×, ladder rising; stop ₹151.95; charges ₹764.30)
2021-08-23  TATAINVEST  PYRAMID BUY ₹5.43 lakh at ₹123.50 (box jump — doubling the stake with NEW capital; stop stays ₹113.90; charges ₹643.35)
2021-08-30  GABRIEL     PYRAMID BUY ₹16,112.86 at ₹137.70 (box jump — doubling the stake with NEW capital; stop stays ₹124.06; charges ₹19.09)
2021-08-30  GRAVITA     PYRAMID BUY ₹6.63 lakh at ₹194.00 (box jump — doubling the stake with NEW capital; stop stays ₹164.49; charges ₹785.25)
2021-08-30  KPITTECH    PYRAMID BUY ₹4.40 lakh at ₹339.50 (box jump — doubling the stake with NEW capital; stop stays ₹278.89; charges ₹521.13)
2021-09-06  HAL         BUY ₹7.75 lakh at ₹705.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.49×, ladder rising; stop ₹500.63; charges ₹918.18)
2021-09-06  NHPC        BUY ₹7.77 lakh at ₹27.90 (fresh Friday signal — BUY: 5.07× weekly, month 1.59×, ladder rising; stop ₹24.13; charges ₹920.10)
2021-09-06  TDPOWERSYS  BUY ₹7.72 lakh at ₹32.80 (fresh Friday signal — BUY: 2.60× weekly, month 4.52×, ladder rising; stop ₹25.56; charges ₹914.89)
2021-09-13  HAL         PYRAMID BUY ₹7.54 lakh at ₹687.02 (box jump — doubling the stake with NEW capital; stop stays ₹636.29; charges ₹893.71)
2021-09-13  KEI         PYRAMID BUY ₹5.54 lakh at ₹796.70 (box jump — doubling the stake with NEW capital; stop stays ₹718.20; charges ₹656.20)
2021-09-13  NEOGEN      BUY ₹8.89 lakh at ₹1,165.00 (fresh Friday signal — BUY: 10.32× weekly, month 3.05×, ladder rising; stop ₹841.94; charges ₹1,053.07)
2021-09-13  TATAINVEST  PYRAMID BUY ₹11.31 lakh at ₹128.69 (box jump — doubling the stake with NEW capital; stop stays ₹118.32; charges ₹1,339.93)
2021-09-20  DEEPAKFERT  PYRAMID BUY ₹6.62 lakh at ₹430.00 (box jump — doubling the stake with NEW capital; stop stays ₹385.70; charges ₹784.33)
2021-09-20  KEI         PYRAMID BUY ₹11.80 lakh at ₹849.00 (box jump — doubling the stake with NEW capital; stop stays ₹737.39; charges ₹1,397.73)
2021-09-20  NHPC        PYRAMID BUY ₹7.69 lakh at ₹27.65 (box jump — doubling the stake with NEW capital; stop stays ₹25.55; charges ₹910.77)
2021-09-20  TDPOWERSYS  PYRAMID BUY ₹7.48 lakh at ₹31.80 (box jump — doubling the stake with NEW capital; stop stays ₹29.75; charges ₹885.95)
2021-09-27  NEOGEN      PYRAMID BUY ₹9.56 lakh at ₹1,255.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,035.55; charges ₹1,133.08)
2021-09-27  TATAINVEST  PYRAMID BUY ₹22.99 lakh at ₹130.90 (box jump — doubling the stake with NEW capital; stop stays ₹118.77; charges ₹2,724.37)
2021-10-04  NEOGEN      PYRAMID BUY ₹19.12 lakh at ₹1,255.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,142.85; charges ₹2,265.00)
2021-10-11  KEI         PYRAMID BUY ₹27.32 lakh at ₹983.80 (box jump — doubling the stake with NEW capital; stop stays ₹853.10; charges ₹3,237.38)
2021-10-18  HAL         PYRAMID BUY ₹16.18 lakh at ₹737.50 (box jump — doubling the stake with NEW capital; stop stays ₹636.50; charges ₹1,917.60)
2021-10-18  TATAINVEST  PYRAMID BUY ₹59.02 lakh at ₹168.10 (box jump — doubling the stake with NEW capital; stop stays ₹134.91; charges ₹6,993.06)
2021-10-18  TDPOWERSYS  PYRAMID BUY ₹16.37 lakh at ₹34.84 (box jump — doubling the stake with NEW capital; stop stays ₹30.53; charges ₹1,940.13)
2021-10-22  KEI         SELL ₹47.31 lakh at stop ₹853.10 (-4.1%, charges ₹4,907.52) — the cash goes back to work at the next Friday screen
2021-10-22  TDPOWERSYS  SELL ₹28.65 lakh at stop ₹30.53 (-9.1%, charges ₹2,972.04) — the cash goes back to work at the next Friday screen
2021-10-25  LTM         BUY ₹31.91 lakh at ₹6,555.00 (fresh Friday signal — BUY: 4.63× weekly, month 1.86×, ladder rising; stop ₹5,353.77; charges ₹3,781.35)
2021-10-25  NEOGEN      SELL ₹34.76 lakh at stop ₹1,142.85 (-7.3%, charges ₹3,605.40) — the cash goes back to work at the next Friday screen
2021-10-25  NHPC        PYRAMID BUY ₹18.28 lakh at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹27.60; charges ₹2,166.13)
2021-10-28  HAL         SELL ₹27.89 lakh at stop ₹636.50 (-11.2%, charges ₹2,893.13) — the cash goes back to work at the next Friday screen
2021-11-01  LTM         PYRAMID BUY ₹32.68 lakh at ₹6,720.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,950.99; charges ₹3,871.94)
2021-11-01  PERSISTENT  BUY ₹45.36 lakh at ₹1,977.15 (fresh Friday signal — ACCUMULATE: 1.71× weekly, month 2.09×, ladder rising; stop ₹1,728.75; charges ₹5,373.97)
2021-11-01  TATAINVEST  PYRAMID BUY ₹1.04 crore at ₹148.00 (box jump — doubling the stake with NEW capital; stop stays ₹143.65; charges ₹12,306.48)
2021-11-11  DEEPAKFERT  SELL ₹11.86 lakh at stop ₹385.70 (-3.5%, charges ₹1,229.85) — the cash goes back to work at the next Friday screen
2021-11-15  GOKULAGRO   BUY ₹52.01 lakh at ₹31.05 (fresh Friday signal — BUY: 2.63× weekly, month 1.60×, ladder rising; stop ₹24.87; charges ₹6,161.81)
2021-11-15  GRAVITA     PYRAMID BUY ₹15.01 lakh at ₹219.80 (box jump — doubling the stake with NEW capital; stop stays ₹197.03; charges ₹1,778.30)
2021-11-15  NHPC        PYRAMID BUY ₹35.88 lakh at ₹32.30 (box jump — doubling the stake with NEW capital; stop stays ₹28.69; charges ₹4,250.73)
2021-11-22  GRAVITA     SELL ₹26.86 lakh at stop ₹197.03 (-4.1%, charges ₹2,786.66) — the cash goes back to work at the next Friday screen
2021-11-22  NHPC        PYRAMID BUY ₹73.04 lakh at ₹32.90 (box jump — doubling the stake with NEW capital; stop stays ₹30.11; charges ₹8,654.25)
2021-11-26  TATAINVEST  SELL ₹2.01 crore at stop ₹143.65 (-3.2%, charges ₹20,881.05) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹69.46 lakh at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹8,230.31)
2021-11-29  ESCORTS     BUY ₹69.59 lakh at ₹1,875.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.18×, ladder rising; stop ₹1,369.04; charges ₹8,245.15)
2021-11-29  GOKULAGRO   PYRAMID BUY ₹58.02 lakh at ₹34.68 (box jump — doubling the stake with NEW capital; stop stays ₹26.03; charges ₹6,873.93)
2021-11-29  KPITTECH    PYRAMID BUY ₹11.78 lakh at ₹455.00 (box jump — doubling the stake with NEW capital; stop stays ₹398.63; charges ₹1,396.01)
2021-11-29  LTM         PYRAMID BUY ₹63.47 lakh at ₹6,530.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,270.00; charges ₹7,520.47)
2021-11-29  NHPC        SELL ₹1.33 crore at stop ₹30.11 (-6.2%, charges ₹13,845.82) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹75.75 lakh at ₹209.99 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹158.85; charges ₹8,975.29)
2021-12-06  BSOFT       PYRAMID BUY ₹72.34 lakh at ₹485.00 (box jump — doubling the stake with NEW capital; stop stays ₹424.65; charges ₹8,570.45)
2021-12-06  CHAMBLFERT  BUY ₹75.58 lakh at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹8,954.49)
2021-12-06  PGEL        BUY ₹75.31 lakh at ₹61.77 (fresh Friday signal — BUY: 2.46× weekly, month 1.72×, ladder rising; stop ₹37.43; charges ₹8,923.36)
2021-12-13  ESCORTS     PYRAMID BUY ₹69.29 lakh at ₹1,869.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,739.73; charges ₹8,209.03)
2021-12-13  KPITTECH    PYRAMID BUY ₹26.14 lakh at ₹505.00 (box jump — doubling the stake with NEW capital; stop stays ₹458.85; charges ₹3,097.01)
2021-12-13  PERSISTENT  PYRAMID BUY ₹49.95 lakh at ₹2,180.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,961.89; charges ₹5,918.30)
2021-12-20  KPITTECH    SELL ₹47.42 lakh at stop ₹458.85 (+3.5%, charges ₹4,919.22) — the cash goes back to work at the next Friday screen
2021-12-27  BSE         PYRAMID BUY ₹74.06 lakh at ₹205.56 (box jump — doubling the stake with NEW capital; stop stays ₹181.60; charges ₹8,775.16)
2021-12-27  PERSISTENT  PYRAMID BUY ₹1.06 crore at ₹2,311.50 (box jump — doubling the stake with NEW capital; stop stays ₹2,067.34; charges ₹12,543.16)
2021-12-27  PGEL        PYRAMID BUY ₹86.47 lakh at ₹71.00 (box jump — doubling the stake with NEW capital; stop stays ₹56.96; charges ₹10,245.41)
2021-12-27  UNOMINDA    BUY ₹64.56 lakh at ₹590.00 (fresh Friday signal — BUY: 3.66× weekly, month 2.64×, ladder rising; stop ₹464.60; charges ₹7,649.22)
2022-01-03  GABRIEL     PYRAMID BUY ₹32,744.58 at ₹140.00 (box jump — doubling the stake with NEW capital; stop stays ₹125.40; charges ₹38.80)
2022-01-03  UNOMINDA    PYRAMID BUY ₹67.21 lakh at ₹614.92 (box jump — doubling the stake with NEW capital; stop stays ₹544.21; charges ₹7,962.92)
2022-01-07  UNOMINDA    SELL ₹1.19 crore at stop ₹544.21 (-9.7%, charges ₹12,319.46) — the cash goes back to work at the next Friday screen
2022-01-10  AFFLE       BUY ₹1.19 crore at ₹1,307.00 (fresh Friday signal — BUY: 4.57× weekly, month 1.57×, ladder rising; stop ₹955.80; charges ₹14,071.47)
2022-01-10  PGEL        PYRAMID BUY ₹2.06 crore at ₹84.50 (box jump — doubling the stake with NEW capital; stop stays ₹72.44; charges ₹24,372.52)
2022-01-17  AFFLE       PYRAMID BUY ₹1.36 crore at ₹1,493.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,206.50; charges ₹16,054.94)
2022-01-24  ESCORTS     PYRAMID BUY ₹1.39 crore at ₹1,869.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,754.65; charges ₹16,414.48)
2022-01-24  GOKULAGRO   PYRAMID BUY ₹1.27 crore at ₹37.98 (box jump — doubling the stake with NEW capital; stop stays ₹35.00; charges ₹15,049.65)
2022-01-24  LTM         SELL ₹1.22 crore at stop ₹6,270.00 (-4.8%, charges ₹12,623.33) — the cash goes back to work at the next Friday screen
2022-01-24  PERSISTENT  SELL ₹1.89 crore at stop ₹2,067.34 (-5.8%, charges ₹19,611.00) — the cash goes back to work at the next Friday screen
2022-01-24  PGEL        SELL ₹3.52 crore at stop ₹72.44 (-4.0%, charges ₹36,525.54) — the cash goes back to work at the next Friday screen
2022-01-25  AFFLE       SELL ₹2.19 crore at stop ₹1,206.50 (-13.8%, charges ₹22,680.40) — the cash goes back to work at the next Friday screen
2022-01-25  GOKULAGRO   SELL ₹2.34 crore at stop ₹35.00 (-1.2%, charges ₹24,243.84) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹1.77 crore at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹20,948.87)
2022-02-07  CCL         BUY ₹1.99 crore at ₹503.55 (fresh Friday signal — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹23,536.90)
2022-02-07  SHARDACROP  PYRAMID BUY ₹1.99 crore at ₹660.10 (box jump — doubling the stake with NEW capital; stop stays ₹545.30; charges ₹23,541.78)
2022-02-11  SHARDACROP  SELL ₹3.28 crore at stop ₹545.30 (-12.5%, charges ₹33,996.93) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹1.26 crore at stop ₹424.65 (-10.6%, charges ₹13,118.00) — the cash goes back to work at the next Friday screen
2022-02-14  CCL         PYRAMID BUY ₹1.83 crore at ₹465.00 (box jump — doubling the stake with NEW capital; stop stays ₹441.75; charges ₹21,709.25)
2022-02-14  CHAMBLFERT  PYRAMID BUY ₹71.22 lakh at ₹384.40 (box jump — doubling the stake with NEW capital; stop stays ₹353.85; charges ₹8,437.91)
2022-02-14  GABRIEL     SELL ₹58,564.09 at stop ₹125.40 (-8.6%, charges ₹60.75) — the cash goes back to work at the next Friday screen
2022-02-14  GNFC        BUY ₹2.14 crore at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹25,332.62)
2022-02-21  ADANIPOWER  BUY ₹2.34 crore at ₹26.40 (fresh Friday signal — BUY: 8.22× weekly, month 2.70×, ladder rising; stop ₹18.02; charges ₹27,772.67)
2022-02-21  CGCL        BUY ₹2.32 crore at ₹567.08 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹507.72; charges ₹27,520.35)
2022-02-21  GNFC        PYRAMID BUY ₹2.12 crore at ₹548.00 (box jump — doubling the stake with NEW capital; stop stays ₹497.80; charges ₹25,073.83)
2022-02-24  CCL         SELL ₹3.48 crore at stop ₹441.75 (-8.8%, charges ₹36,053.12) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹1.31 crore at stop ₹353.85 (-10.6%, charges ₹13,578.30) — the cash goes back to work at the next Friday screen
2022-02-25  ESCORTS     SELL ₹2.60 crore at stop ₹1,754.65 (-6.2%, charges ₹26,929.01) — the cash goes back to work at the next Friday screen
2022-03-07  ADANIPOWER  PYRAMID BUY ₹2.06 crore at ₹23.20 (box jump — doubling the stake with NEW capital; stop stays ₹20.00; charges ₹24,377.36)
2022-04-01  TAX         FY2022 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹2.35 crore / LT ₹0.00)
2022-04-04  RCF         BUY ₹3.14 crore at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹37,238.08)
2022-04-04  SPLPETRO    BUY ₹3.16 crore at ₹475.00 (fresh Friday signal — BUY: 4.41× weekly, month 2.84×, ladder rising; stop ₹398.29; charges ₹37,420.80)
2022-04-11  BLS         BUY ₹3.52 crore at ₹82.50 (fresh Friday signal — BUY: 8.78× weekly, month 1.73×, ladder rising; stop ₹54.82; charges ₹41,760.13)
2022-04-11  MINDACORP   BUY ₹2.70 crore at ₹230.05 (fresh Friday signal — BUY: 2.10× weekly, month 1.60×, ladder rising; stop ₹186.63; charges ₹31,938.92)
2022-04-11  SPLPETRO    PYRAMID BUY ₹3.06 crore at ₹460.65 (box jump — doubling the stake with NEW capital; stop stays ₹424.27; charges ₹36,247.30)
2022-04-25  ADANIPOWER  PYRAMID BUY ₹9.34 crore at ₹52.68 (box jump — doubling the stake with NEW capital; stop stays ₹40.22; charges ₹1.11 lakh)
2022-04-25  BLS         PYRAMID BUY ₹3.52 crore at ₹82.42 (box jump — doubling the stake with NEW capital; stop stays ₹75.36; charges ₹41,672.74)
2022-04-25  GNFC        PYRAMID BUY ₹6.53 crore at ₹846.40 (box jump — doubling the stake with NEW capital; stop stays ₹792.16; charges ₹77,408.46)
2022-04-25  RCF         PYRAMID BUY ₹3.39 crore at ₹104.20 (box jump — doubling the stake with NEW capital; stop stays ₹93.15; charges ₹40,203.43)
2022-05-02  BSE         PYRAMID BUY ₹2.14 crore at ₹296.70 (box jump — doubling the stake with NEW capital; stop stays ₹255.87; charges ₹25,317.22)
2022-05-04  RCF         SELL ₹6.06 crore at stop ₹93.15 (-7.1%, charges ₹62,827.94) — the cash goes back to work at the next Friday screen
2022-05-06  GNFC        SELL ₹12.21 crore at stop ₹792.16 (+13.4%, charges ₹1.27 lakh) — the cash goes back to work at the next Friday screen
2022-05-09  MRPL        BUY ₹6.06 crore at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹71,800.85)
2022-05-10  BSE         SELL ₹3.68 crore at stop ₹255.87 (+1.5%, charges ₹38,167.38) — the cash goes back to work at the next Friday screen
2022-05-11  MINDACORP   SELL ₹2.18 crore at stop ₹186.63 (-18.9%, charges ₹22,634.27) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹5.84 crore at ₹146.67 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.79×, ladder rising; stop ₹130.85; charges ₹69,247.35)
2022-05-23  ACC         BUY ₹7.19 crore at ₹2,260.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹85,153.07)
2022-05-23  MRPL        PYRAMID BUY ₹7.36 crore at ₹94.80 (box jump — doubling the stake with NEW capital; stop stays ₹60.81; charges ₹87,162.25)
2022-05-24  SPLPETRO    SELL ₹5.63 crore at stop ₹424.27 (-9.3%, charges ₹58,360.83) — the cash goes back to work at the next Friday screen
2022-06-06  MRPL        PYRAMID BUY ₹13.70 crore at ₹88.35 (box jump — doubling the stake with NEW capital; stop stays ₹69.61; charges ₹1.62 lakh)
2022-06-13  ELECON      BUY ₹9.34 crore at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹1.11 lakh)
2022-06-13  VBL         PYRAMID BUY ₹5.96 crore at ₹149.70 (box jump — doubling the stake with NEW capital; stop stays ₹136.81; charges ₹70,595.76)
2022-06-20  BLS         PYRAMID BUY ₹9.05 crore at ₹106.12 (box jump — doubling the stake with NEW capital; stop stays ₹83.17; charges ₹1.07 lakh)
2022-06-20  ELECON      PYRAMID BUY ₹10.00 crore at ₹131.25 (box jump — doubling the stake with NEW capital; stop stays ₹111.01; charges ₹1.19 lakh)
2022-06-27  ADANIPOWER  PYRAMID BUY ₹19.20 crore at ₹54.19 (box jump — doubling the stake with NEW capital; stop stays ₹43.79; charges ₹2.27 lakh)
2022-06-27  VBL         PYRAMID BUY ₹12.41 crore at ₹155.98 (box jump — doubling the stake with NEW capital; stop stays ₹136.99; charges ₹1.47 lakh)
2022-07-04  BLS         PYRAMID BUY ₹16.62 crore at ₹97.47 (box jump — doubling the stake with NEW capital; stop stays ₹90.53; charges ₹1.97 lakh)
2022-07-06  MRPL        SELL ₹21.56 crore at stop ₹69.61 (-20.3%, charges ₹2.24 lakh) — the cash goes back to work at the next Friday screen
2022-07-11  ELECON      PYRAMID BUY ₹22.39 crore at ₹147.00 (box jump — doubling the stake with NEW capital; stop stays ₹120.65; charges ₹2.65 lakh)
2022-07-18  ACC         PYRAMID BUY ₹6.86 crore at ₹2,160.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,030.05; charges ₹81,324.56)
2022-07-25  ELECON      PYRAMID BUY ₹50.52 crore at ₹165.95 (box jump — doubling the stake with NEW capital; stop stays ₹142.64; charges ₹5.99 lakh)
2022-07-25  TIINDIA     BUY ₹22.88 crore at ₹2,135.00 (fresh Friday signal — BUY: 4.17× weekly, month 2.43×, ladder rising; stop ₹1,862.00; charges ₹2.71 lakh)
2022-08-01  VBL         PYRAMID BUY ₹28.36 crore at ₹178.36 (box jump — doubling the stake with NEW capital; stop stays ₹162.49; charges ₹3.36 lakh)
2022-08-08  ACC         PYRAMID BUY ₹14.35 crore at ₹2,260.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,053.90; charges ₹1.70 lakh)
2022-08-08  BLS         PYRAMID BUY ₹40.30 crore at ₹118.25 (box jump — doubling the stake with NEW capital; stop stays ₹110.67; charges ₹4.77 lakh)
2022-08-08  TIINDIA     PYRAMID BUY ₹24.32 crore at ₹2,272.15 (box jump — doubling the stake with NEW capital; stop stays ₹1,867.30; charges ₹2.88 lakh)
2022-08-16  ACC         PYRAMID BUY ₹28.53 crore at ₹2,248.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,085.11; charges ₹3.38 lakh)
2022-08-16  ADANIPOWER  PYRAMID BUY ₹49.43 crore at ₹69.80 (box jump — doubling the stake with NEW capital; stop stays ₹61.19; charges ₹5.86 lakh)
2022-08-16  ELECON      PYRAMID BUY ₹104.06 crore at ₹171.00 (box jump — doubling the stake with NEW capital; stop stays ₹156.67; charges ₹12.33 lakh)
2022-08-16  VBL         PYRAMID BUY ₹65.48 crore at ₹206.00 (box jump — doubling the stake with NEW capital; stop stays ₹188.52; charges ₹7.76 lakh)
2022-08-22  VBL         SELL ₹119.65 crore at stop ₹188.52 (+1.6%, charges ₹12.41 lakh) — the cash goes back to work at the next Friday screen
2022-08-23  BLS         SELL ₹75.30 crore at stop ₹110.67 (+3.4%, charges ₹7.81 lakh) — the cash goes back to work at the next Friday screen
2022-08-29  ACC         PYRAMID BUY ₹57.68 crore at ₹2,274.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,151.37; charges ₹6.83 lakh)
2022-08-29  HOMEFIRST   BUY ₹69.35 crore at ₹944.95 (fresh Friday signal — ACCUMULATE: 3.67× weekly, month 2.49×, ladder rising; stop ₹849.35; charges ₹8.22 lakh)
2022-08-29  KALYANKJIL  BUY ₹69.43 crore at ₹78.10 (fresh Friday signal — BUY: 9.54× weekly, month 2.93×, ladder rising; stop ₹65.55; charges ₹8.23 lakh)
2022-08-29  SIEMENS     BUY ₹56.16 crore at ₹1,688.21 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 1.62×, ladder rising; stop ₹1,573.13; charges ₹6.65 lakh)
2022-09-05  ADANIPOWER  PYRAMID BUY ₹114.28 crore at ₹80.73 (box jump — doubling the stake with NEW capital; stop stays ₹66.80; charges ₹13.54 lakh)
2022-09-05  KALYANKJIL  PYRAMID BUY ₹75.17 crore at ₹84.65 (box jump — doubling the stake with NEW capital; stop stays ₹73.15; charges ₹8.91 lakh)
2022-09-14  HOMEFIRST   SELL ₹62.20 crore at stop ₹849.35 (-10.1%, charges ₹6.45 lakh) — the cash goes back to work at the next Friday screen
2022-09-19  KALYANKJIL  PYRAMID BUY ₹168.79 crore at ₹95.10 (box jump — doubling the stake with NEW capital; stop stays ₹76.00; charges ₹20.00 lakh)
2022-09-19  MAHSCOOTER  BUY ₹62.20 crore at ₹5,103.50 (fresh Friday signal — BUY: 10.17× weekly, month 2.61×, ladder rising; stop ₹3,847.79; charges ₹7.37 lakh)
2022-09-19  SIEMENS     PYRAMID BUY ₹57.72 crore at ₹1,737.02 (box jump — doubling the stake with NEW capital; stop stays ₹1,618.44; charges ₹6.84 lakh)
2022-09-26  SIEMENS     SELL ₹107.38 crore at stop ₹1,618.44 (-5.5%, charges ₹11.14 lakh) — the cash goes back to work at the next Friday screen
2022-09-26  TIINDIA     PYRAMID BUY ₹58.57 crore at ₹2,737.75 (box jump — doubling the stake with NEW capital; stop stays ₹2,360.75; charges ₹6.94 lakh)
2022-10-03  ACC         PYRAMID BUY ₹122.69 crore at ₹2,419.80 (box jump — doubling the stake with NEW capital; stop stays ₹2,171.53; charges ₹14.54 lakh)
2022-10-03  KALYANKJIL  PYRAMID BUY ₹343.77 crore at ₹96.90 (box jump — doubling the stake with NEW capital; stop stays ₹81.12; charges ₹40.73 lakh)
2022-10-03  MAHSCOOTER  PYRAMID BUY ₹60.84 crore at ₹4,998.05 (box jump — doubling the stake with NEW capital; stop stays ₹4,617.00; charges ₹7.21 lakh)
2022-10-03  TSFINV      BUY ₹107.38 crore at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹12.72 lakh)
2022-10-10  TSFINV      PYRAMID BUY ₹103.05 crore at ₹99.45 (box jump — doubling the stake with NEW capital; stop stays ₹92.20; charges ₹12.21 lakh)
2022-10-11  TSFINV      SELL ₹190.77 crore at stop ₹92.20 (-9.1%, charges ₹19.79 lakh) — the cash goes back to work at the next Friday screen
2022-10-14  ADANIPOWER  SELL ₹188.81 crore at stop ₹66.80 (-3.8%, charges ₹19.59 lakh) — the cash goes back to work at the next Friday screen
2022-10-17  APOLLO      BUY ₹178.89 crore at ₹24.00 (fresh Friday signal — BUY: 6.98× weekly, month 4.78×, ladder rising; stop ₹14.17; charges ₹21.20 lakh)
2022-10-24  GODFRYPHLP  BUY ₹200.69 crore at ₹483.67 (fresh Friday signal — BUY: 4.48× weekly, month 3.07×, ladder rising; stop ₹403.15; charges ₹23.78 lakh)
2022-10-24  KALYANKJIL  PYRAMID BUY ₹722.24 crore at ₹101.85 (box jump — doubling the stake with NEW capital; stop stays ₹89.78; charges ₹85.57 lakh)
2022-10-31  APOLLO      PYRAMID BUY ₹161.59 crore at ₹21.70 (box jump — doubling the stake with NEW capital; stop stays ₹19.45; charges ₹19.15 lakh)
2022-10-31  KALYANKJIL  PYRAMID BUY ₹1,498.20 crore at ₹105.70 (box jump — doubling the stake with NEW capital; stop stays ₹94.53; charges ₹1.78 crore)
2022-10-31  TIINDIA     PYRAMID BUY ₹114.38 crore at ₹2,675.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,465.49; charges ₹13.55 lakh)
2022-11-07  ELECON      PYRAMID BUY ₹244.31 crore at ₹200.85 (box jump — doubling the stake with NEW capital; stop stays ₹164.33; charges ₹28.95 lakh)
2022-11-14  CGCL        PYRAMID BUY ₹2.85 crore at ₹696.24 (box jump — doubling the stake with NEW capital; stop stays ₹661.39; charges ₹33,748.71)
2022-11-21  ACC         PYRAMID BUY ₹248.56 crore at ₹2,452.70 (box jump — doubling the stake with NEW capital; stop stays ₹2,259.81; charges ₹29.45 lakh)
2022-11-21  ELECON      PYRAMID BUY ₹518.96 crore at ₹213.45 (box jump — doubling the stake with NEW capital; stop stays ₹202.49; charges ₹61.49 lakh)
2022-11-21  GODFRYPHLP  PYRAMID BUY ₹254.19 crore at ₹613.33 (box jump — doubling the stake with NEW capital; stop stays ₹497.48; charges ₹30.12 lakh)
2022-11-22  KALYANKJIL  SELL ₹2,675.39 crore at stop ₹94.53 (-6.8%, charges ₹2.78 crore) — the cash goes back to work at the next Friday screen
2022-11-28  IOB         BUY ₹551.31 crore at ₹23.00 (fresh Friday signal — BUY: 7.22× weekly, month 5.74×, ladder rising; stop ₹18.76; charges ₹65.32 lakh)
2022-11-28  IRFC        BUY ₹549.39 crore at ₹32.00 (fresh Friday signal — BUY: 9.02× weekly, month 13.28×, ladder rising; stop ₹23.09; charges ₹65.09 lakh)
2022-11-28  MAHABANK    BUY ₹551.98 crore at ₹27.60 (fresh Friday signal — BUY: 8.71× weekly, month 8.20×, ladder rising; stop ₹21.47; charges ₹65.40 lakh)
2022-11-28  SKIPPER     BUY ₹472.35 crore at ₹89.34 (fresh Friday signal — BUY: 6.40× weekly, month 2.23×, ladder rising; stop ₹65.34; charges ₹55.96 lakh)
2022-11-28  UCOBANK     BUY ₹550.37 crore at ₹21.05 (fresh Friday signal — BUY: 13.59× weekly, month 16.04×, ladder rising; stop ₹13.59; charges ₹65.21 lakh)
2022-12-05  GODFRYPHLP  PYRAMID BUY ₹505.32 crore at ₹610.00 (box jump — doubling the stake with NEW capital; stop stays ₹547.85; charges ₹59.87 lakh)
2022-12-05  IOB         PYRAMID BUY ₹550.66 crore at ₹23.00 (box jump — doubling the stake with NEW capital; stop stays ₹20.76; charges ₹65.24 lakh)
2022-12-12  APOLLO      PYRAMID BUY ₹384.02 crore at ₹25.80 (box jump — doubling the stake with NEW capital; stop stays ₹24.42; charges ₹45.50 lakh)
2022-12-12  UCOBANK     PYRAMID BUY ₹616.31 crore at ₹23.60 (box jump — doubling the stake with NEW capital; stop stays ₹18.29; charges ₹73.02 lakh)
2022-12-19  ACC         PYRAMID BUY ₹529.29 crore at ₹2,612.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,465.15; charges ₹62.71 lakh)
2022-12-19  IRFC        PYRAMID BUY ₹553.88 crore at ₹32.30 (box jump — doubling the stake with NEW capital; stop stays ₹28.20; charges ₹65.62 lakh)
2022-12-19  SKIPPER     PYRAMID BUY ₹641.78 crore at ₹121.53 (box jump — doubling the stake with NEW capital; stop stays ₹109.70; charges ₹76.04 lakh)
2022-12-21  ELECON      SELL ₹983.01 crore at stop ₹202.49 (+2.7%, charges ₹1.02 crore) — the cash goes back to work at the next Friday screen
2022-12-22  MAHSCOOTER  SELL ₹112.22 crore at stop ₹4,617.00 (-8.6%, charges ₹11.64 lakh) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹997.07 crore at stop ₹2,465.15 (-1.6%, charges ₹1.03 crore) — the cash goes back to work at the next Friday screen
2022-12-23  IRFC        SELL ₹965.57 crore at stop ₹28.20 (-12.3%, charges ₹1.00 crore) — the cash goes back to work at the next Friday screen
2022-12-26  APOLLO      SELL ₹725.77 crore at stop ₹24.42 (+0.4%, charges ₹75.28 lakh) — the cash goes back to work at the next Friday screen
2022-12-26  GODFRYPHLP  SELL ₹906.20 crore at stop ₹547.85 (-5.4%, charges ₹94.00 lakh) — the cash goes back to work at the next Friday screen
2022-12-26  TIINDIA     PYRAMID BUY ₹237.44 crore at ₹2,778.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,598.35; charges ₹28.13 lakh)
2023-01-02  GICRE       BUY ₹1,406.41 crore at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 11.13×, ladder rising; stop ₹137.57; charges ₹1.67 crore)
2023-01-02  IOB         PYRAMID BUY ₹1,550.51 crore at ₹32.40 (box jump — doubling the stake with NEW capital; stop stays ₹21.23; charges ₹1.84 crore)
2023-01-02  LLOYDSENGG  BUY ₹1,412.98 crore at ₹15.63 (fresh Friday signal — ACCUMULATE: 2.36× weekly, month 2.74×, ladder rising; stop ₹10.86; charges ₹1.67 crore)
2023-01-02  MAHABANK    PYRAMID BUY ₹616.25 crore at ₹30.85 (box jump — doubling the stake with NEW capital; stop stays ₹22.08; charges ₹73.01 lakh)
2023-01-02  UCOBANK     PYRAMID BUY ₹1,659.91 crore at ₹31.80 (box jump — doubling the stake with NEW capital; stop stays ₹23.46; charges ₹1.97 crore)
2023-01-02  YESBANK     BUY ₹1,401.20 crore at ₹20.85 (fresh Friday signal — ACCUMULATE: 2.89× weekly, month 3.19×, ladder rising; stop ₹15.00; charges ₹1.66 crore)
2023-01-09  CGCL        PYRAMID BUY ₹5.84 crore at ₹714.12 (box jump — doubling the stake with NEW capital; stop stays ₹666.82; charges ₹69,189.58)
2023-01-11  TIINDIA     SELL ₹443.44 crore at stop ₹2,598.35 (-2.9%, charges ₹46.00 lakh) — the cash goes back to work at the next Friday screen
2023-01-16  ANUP        BUY ₹912.71 crore at ₹476.12 (fresh Friday signal — ACCUMULATE: 4.79× weekly, month 1.56×, ladder rising; stop ₹364.75; charges ₹1.08 crore)
2023-01-16  GICRE       PYRAMID BUY ₹1,466.28 crore at ₹187.05 (box jump — doubling the stake with NEW capital; stop stays ₹167.72; charges ₹1.74 crore)
2023-01-25  SKIPPER     SELL ₹1,156.68 crore at stop ₹109.70 (+4.1%, charges ₹1.20 crore) — the cash goes back to work at the next Friday screen
2023-02-01  GICRE       SELL ₹2,625.22 crore at stop ₹167.72 (-8.4%, charges ₹2.72 crore) — the cash goes back to work at the next Friday screen
2023-02-06  ANUP        PYRAMID BUY ₹1,076.24 crore at ₹562.10 (box jump — doubling the stake with NEW capital; stop stays ₹466.90; charges ₹1.28 crore)
2023-02-06  JINDALSAW   BUY ₹1,720.76 crore at ₹65.22 (fresh Friday signal — BUY: 2.71× weekly, month 3.60×, ladder rising; stop ₹51.25; charges ₹2.04 crore)
2023-02-06  LLOYDSENGG  PYRAMID BUY ₹1,897.67 crore at ₹21.02 (box jump — doubling the stake with NEW capital; stop stays ₹19.27; charges ₹2.25 crore)
2023-02-07  LLOYDSENGG  SELL ₹3,474.05 crore at stop ₹19.27 (+5.2%, charges ₹3.60 crore) — the cash goes back to work at the next Friday screen
2023-02-13  ANUP        PYRAMID BUY ₹2,181.44 crore at ₹570.00 (box jump — doubling the stake with NEW capital; stop stays ₹518.77; charges ₹2.58 crore)
2023-02-13  YESBANK     PYRAMID BUY ₹1,144.47 crore at ₹17.05 (box jump — doubling the stake with NEW capital; stop stays ₹15.34; charges ₹1.36 crore)
2023-02-20  ANUP        PYRAMID BUY ₹4,303.11 crore at ₹562.52 (box jump — doubling the stake with NEW capital; stop stays ₹527.27; charges ₹5.10 crore)
2023-02-27  CERA        BUY ₹2,430.24 crore at ₹6,150.00 (fresh Friday signal — BUY: 5.94× weekly, month 1.75×, ladder rising; stop ₹5,579.40; charges ₹2.88 crore)
2023-02-27  SONATSOFTW  BUY ₹2,430.53 crore at ₹360.00 (fresh Friday signal — BUY: 9.70× weekly, month 3.34×, ladder rising; stop ₹282.62; charges ₹2.88 crore)
2023-03-06  CERA        PYRAMID BUY ₹2,500.18 crore at ₹6,334.50 (box jump — doubling the stake with NEW capital; stop stays ₹5,714.25; charges ₹2.96 crore)
2023-03-06  IOB         PYRAMID BUY ₹2,496.56 crore at ₹26.10 (box jump — doubling the stake with NEW capital; stop stays ₹22.18; charges ₹2.96 crore)
2023-03-06  JINDALSAW   PYRAMID BUY ₹1,949.29 crore at ₹73.97 (box jump — doubling the stake with NEW capital; stop stays ₹67.92; charges ₹2.31 crore)
2023-03-06  SONATSOFTW  PYRAMID BUY ₹2,702.45 crore at ₹400.75 (box jump — doubling the stake with NEW capital; stop stays ₹325.85; charges ₹3.20 crore)
2023-03-08  CGCL        SELL ₹10.89 crore at stop ₹666.82 (-0.9%, charges ₹1.13 lakh) — the cash goes back to work at the next Friday screen
2023-03-10  ANUP        SELL ₹8,053.71 crore at stop ₹527.27 (-4.7%, charges ₹8.35 crore) — the cash goes back to work at the next Friday screen
2023-03-13  YESBANK     SELL ₹2,056.02 crore at stop ₹15.34 (-19.1%, charges ₹2.13 crore) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹3,825.56 crore at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.60×, ladder rising; stop ₹691.46; charges ₹4.53 crore)
2023-03-20  IOB         SELL ₹4,236.29 crore at stop ₹22.18 (-17.5%, charges ₹4.39 crore) — the cash goes back to work at the next Friday screen
2023-03-20  SONATSOFTW  PYRAMID BUY ₹5,357.88 crore at ₹397.50 (box jump — doubling the stake with NEW capital; stop stays ₹357.20; charges ₹6.35 crore)
2023-03-27  CERA        PYRAMID BUY ₹4,962.18 crore at ₹6,289.85 (box jump — doubling the stake with NEW capital; stop stays ₹5,852.00; charges ₹5.88 crore)
2023-03-27  JINDALSAW   SELL ₹3,573.65 crore at stop ₹67.92 (-2.4%, charges ₹3.71 crore) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹5,395.23 crore at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.85×, ladder rising; stop ₹372.21; charges ₹6.39 crore)
2023-03-27  MAHABANK    PYRAMID BUY ₹974.23 crore at ₹24.40 (box jump — doubling the stake with NEW capital; stop stays ₹22.36; charges ₹1.15 crore)
2023-03-27  SONATSOFTW  PYRAMID BUY ₹11,145.88 crore at ₹413.70 (box jump — doubling the stake with NEW capital; stop stays ₹371.45; charges ₹13.21 crore)
2023-03-27  TDPOWERSYS  BUY ₹5,385.09 crore at ₹84.62 (fresh Friday signal — BUY: 1.62× weekly, month 2.13×, ladder rising; stop ₹64.12; charges ₹6.38 crore)
2023-03-27  UCOBANK     SELL ₹2,445.16 crore at stop ₹23.46 (-13.3%, charges ₹2.54 crore) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹19,982.58 crore at stop ₹371.45 (-7.4%, charges ₹20.73 crore) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹5,354.60 crore at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.04×, ladder rising; stop ₹1,171.71; charges ₹6.34 crore)
2023-04-03  TAX         FY2023 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹4,323.15 crore / LT ₹0.00)
2023-04-10  CERA        PYRAMID BUY ₹10,309.78 crore at ₹6,538.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,037.30; charges ₹12.22 crore)
2023-04-10  KIRLOSBROS  BUY ₹6,887.93 crore at ₹425.00 (fresh Friday signal — BUY: 1.86× weekly, month 2.34×, ladder rising; stop ₹357.44; charges ₹8.16 crore)
2023-04-10  TDPOWERSYS  PYRAMID BUY ₹5,049.79 crore at ₹79.45 (box jump — doubling the stake with NEW capital; stop stays ₹73.22; charges ₹5.98 crore)
2023-04-24  KIRLOSBROS  PYRAMID BUY ₹6,998.75 crore at ₹432.35 (box jump — doubling the stake with NEW capital; stop stays ₹403.85; charges ₹8.29 crore)
2023-04-24  MARKSANS    BUY ₹6,399.93 crore at ₹78.00 (fresh Friday signal — ACCUMULATE: 1.64× weekly, month 1.51×, ladder rising; stop ₹71.87; charges ₹7.58 crore)
2023-04-24  ZFCVINDIA   BUY ₹7,784.38 crore at ₹1,697.50 (fresh Friday signal — ACCUMULATE: 7.38× weekly, month 1.55×, ladder rising; stop ₹1,561.17; charges ₹9.22 crore)
2023-04-26  CERA        SELL ₹19,009.46 crore at stop ₹6,037.30 (-5.7%, charges ₹19.72 crore) — the cash goes back to work at the next Friday screen
2023-04-26  KIRLOSBROS  SELL ₹13,053.51 crore at stop ₹403.85 (-5.8%, charges ₹13.54 crore) — the cash goes back to work at the next Friday screen
2023-05-02  ANURAS      PYRAMID BUY ₹5,757.58 crore at ₹1,139.00 (box jump — doubling the stake with NEW capital; stop stays ₹946.20; charges ₹6.82 crore)
2023-05-02  ASHAPURMIN  BUY ₹8,915.72 crore at ₹143.10 (fresh Friday signal — BUY: 2.05× weekly, month 2.10×, ladder rising; stop ₹123.50; charges ₹10.56 crore)
2023-05-02  ICICIBANK   BUY ₹8,912.48 crore at ₹924.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.24×, ladder rising; stop ₹838.28; charges ₹10.56 crore)
2023-05-02  KSB         PYRAMID BUY ₹5,845.49 crore at ₹453.40 (box jump — doubling the stake with NEW capital; stop stays ₹407.74; charges ₹6.93 crore)
2023-05-02  REFEX       BUY ₹8,948.80 crore at ₹65.32 (fresh Friday signal — BUY: 4.73× weekly, month 1.57×, ladder rising; stop ₹54.53; charges ₹10.60 crore)
2023-05-08  HEG         BUY ₹5,285.98 crore at ₹234.38 (fresh Friday signal — BUY: 2.69× weekly, month 1.85×, ladder rising; stop ₹201.01; charges ₹6.26 crore)
2023-05-08  MAHABANK    PYRAMID BUY ₹2,442.11 crore at ₹30.60 (box jump — doubling the stake with NEW capital; stop stays ₹27.79; charges ₹2.89 crore)
2023-05-15  ANURAS      PYRAMID BUY ₹11,819.54 crore at ₹1,169.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,007.67; charges ₹14.00 crore)
2023-05-15  ASHAPURMIN  PYRAMID BUY ₹9,017.17 crore at ₹144.90 (box jump — doubling the stake with NEW capital; stop stays ₹125.16; charges ₹10.68 crore)
2023-05-15  HAL         PYRAMID BUY ₹5,788.04 crore at ₹1,493.47 (box jump — doubling the stake with NEW capital; stop stays ₹1,370.80; charges ₹6.86 crore)
2023-05-15  REFEX       PYRAMID BUY ₹9,968.58 crore at ₹72.85 (box jump — doubling the stake with NEW capital; stop stays ₹58.14; charges ₹11.81 crore)
2023-05-22  MARKSANS    SELL ₹5,883.87 crore at stop ₹71.87 (-7.9%, charges ₹6.10 crore) — the cash goes back to work at the next Friday screen
2023-05-29  ASHAPURMIN  PYRAMID BUY ₹16,157.85 crore at ₹129.90 (box jump — doubling the stake with NEW capital; stop stays ₹134.24; charges ₹19.14 crore)
2023-05-29  ASHAPURMIN  SELL ₹33,341.01 crore at stop ₹134.24 (-2.0%, charges ₹34.58 crore) — the cash goes back to work at the next Friday screen
2023-05-29  TDPOWERSYS  PYRAMID BUY ₹12,958.43 crore at ₹102.00 (box jump — doubling the stake with NEW capital; stop stays ₹89.54; charges ₹15.35 crore)
2023-06-05  EPL         BUY ₹17,204.05 crore at ₹201.90 (fresh Friday signal — ACCUMULATE: 6.59× weekly, month 6.26×, ladder rising; stop ₹170.76; charges ₹20.38 crore)
2023-06-05  FORCEMOT    BUY ₹22,020.83 crore at ₹1,951.00 (fresh Friday signal — BUY: 23.21× weekly, month 3.12×, ladder rising; stop ₹1,289.01; charges ₹26.09 crore)
2023-06-05  HAL         PYRAMID BUY ₹12,331.47 crore at ₹1,591.88 (box jump — doubling the stake with NEW capital; stop stays ₹1,415.36; charges ₹14.61 crore)
2023-06-05  ICICIBANK   PYRAMID BUY ₹9,084.97 crore at ₹943.00 (box jump — doubling the stake with NEW capital; stop stays ₹886.30; charges ₹10.76 crore)
2023-06-05  REFEX       PYRAMID BUY ₹28,784.39 crore at ₹105.24 (box jump — doubling the stake with NEW capital; stop stays ₹87.60; charges ₹34.10 crore)
2023-06-12  HEG         PYRAMID BUY ₹6,153.73 crore at ₹273.18 (box jump — doubling the stake with NEW capital; stop stays ₹211.53; charges ₹7.29 crore)
2023-06-15  MAHABANK    SELL ₹4,428.48 crore at stop ₹27.79 (-3.2%, charges ₹4.59 crore) — the cash goes back to work at the next Friday screen
2023-06-19  FORCEMOT    PYRAMID BUY ₹25,117.52 crore at ₹2,228.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,995.52; charges ₹29.76 crore)
2023-06-19  HAL         PYRAMID BUY ₹30,185.73 crore at ₹1,949.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,723.32; charges ₹35.76 crore)
2023-06-19  ZFCVINDIA   PYRAMID BUY ₹9,221.02 crore at ₹2,013.17 (box jump — doubling the stake with NEW capital; stop stays ₹1,773.33; charges ₹10.93 crore)
2023-06-26  ZFCVINDIA   PYRAMID BUY ₹18,707.31 crore at ₹2,043.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,860.58; charges ₹22.16 crore)
2023-07-03  ANURAS      SELL ₹20,329.63 crore at stop ₹1,007.67 (-4.8%, charges ₹21.09 crore) — the cash goes back to work at the next Friday screen
2023-07-03  EPL         PYRAMID BUY ₹18,298.60 crore at ₹215.00 (box jump — doubling the stake with NEW capital; stop stays ₹189.81; charges ₹21.68 crore)
2023-07-03  HEG         PYRAMID BUY ₹14,723.02 crore at ₹326.99 (box jump — doubling the stake with NEW capital; stop stays ₹294.79; charges ₹17.44 crore)
2023-07-03  TDPOWERSYS  PYRAMID BUY ₹31,462.70 crore at ₹123.90 (box jump — doubling the stake with NEW capital; stop stays ₹101.58; charges ₹37.28 crore)
2023-07-10  CEATLTD     BUY ₹24,758.12 crore at ₹2,408.00 (fresh Friday signal — BUY: 4.55× weekly, month 2.41×, ladder rising; stop ₹1,892.78; charges ₹29.33 crore)
2023-07-10  EPL         PYRAMID BUY ₹36,890.24 crore at ₹216.85 (box jump — doubling the stake with NEW capital; stop stays ₹200.50; charges ₹43.71 crore)
2023-07-10  ZFCVINDIA   PYRAMID BUY ₹36,741.59 crore at ₹2,007.77 (box jump — doubling the stake with NEW capital; stop stays ₹1,882.66; charges ₹43.53 crore)
2023-07-12  KSB         SELL ₹10,496.52 crore at stop ₹407.74 (-6.4%, charges ₹10.89 crore) — the cash goes back to work at the next Friday screen
2023-07-17  FORCEMOT    PYRAMID BUY ₹62,508.72 crore at ₹2,774.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,337.00; charges ₹74.06 crore)
2023-07-17  TDPOWERSYS  PYRAMID BUY ₹63,218.05 crore at ₹124.55 (box jump — doubling the stake with NEW capital; stop stays ₹110.20; charges ₹74.90 crore)
2023-07-24  ICICIBANK   PYRAMID BUY ₹19,352.14 crore at ₹1,004.95 (box jump — doubling the stake with NEW capital; stop stays ₹894.19; charges ₹22.93 crore)
2023-07-24  TDPOWERSYS  PYRAMID BUY ₹1.29 lakh crore at ₹127.42 (box jump — doubling the stake with NEW capital; stop stays ₹112.05; charges ₹153.17 crore)
2023-07-31  CEATLTD     PYRAMID BUY ₹25,181.67 crore at ₹2,452.10 (box jump — doubling the stake with NEW capital; stop stays ₹2,244.85; charges ₹29.84 crore)
2023-07-31  HEG         PYRAMID BUY ₹30,504.07 crore at ₹338.94 (box jump — doubling the stake with NEW capital; stop stays ₹300.49; charges ₹36.14 crore)
2023-07-31  REFEX       PYRAMID BUY ₹92,392.26 crore at ₹169.00 (box jump — doubling the stake with NEW capital; stop stays ₹121.69; charges ₹109.47 crore)
2023-08-11  EPL         SELL ₹68,106.54 crore at stop ₹200.50 (-5.7%, charges ₹70.65 crore) — the cash goes back to work at the next Friday screen
2023-08-11  REFEX       SELL ₹1.33 lakh crore at stop ₹121.69 (-5.0%, charges ₹137.79 crore) — the cash goes back to work at the next Friday screen
2023-08-14  CEATLTD     SELL ₹46,031.59 crore at stop ₹2,244.85 (-7.6%, charges ₹47.75 crore) — the cash goes back to work at the next Friday screen
2023-08-14  HAL         PYRAMID BUY ₹58,569.27 crore at ₹1,892.42 (box jump — doubling the stake with NEW capital; stop stays ₹1,758.24; charges ₹69.39 crore)
2023-08-14  RATEGAIN    BUY ₹1.04 lakh crore at ₹547.00 (fresh Friday signal — BUY: 5.36× weekly, month 1.91×, ladder rising; stop ₹422.99; charges ₹122.84 crore)
2023-08-14  VARROC      BUY ₹1.04 lakh crore at ₹385.40 (fresh Friday signal — BUY: 6.86× weekly, month 2.37×, ladder rising; stop ₹304.00; charges ₹123.12 crore)
2023-08-14  ZFCVINDIA   PYRAMID BUY ₹81,568.46 crore at ₹2,230.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,046.36; charges ₹96.64 crore)
2023-08-21  ICICIBANK   PYRAMID BUY ₹36,593.22 crore at ₹950.70 (box jump — doubling the stake with NEW capital; stop stays ₹898.70; charges ₹43.36 crore)
2023-08-21  RATEGAIN    PYRAMID BUY ₹1.08 lakh crore at ₹572.80 (box jump — doubling the stake with NEW capital; stop stays ₹489.44; charges ₹128.48 crore)
2023-08-21  VARROC      PYRAMID BUY ₹1.04 lakh crore at ₹384.80 (box jump — doubling the stake with NEW capital; stop stays ₹347.89; charges ₹122.79 crore)
2023-08-28  FORCEMOT    PYRAMID BUY ₹1.58 lakh crore at ₹3,500.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,158.80; charges ₹186.78 crore)
2023-08-28  RATEGAIN    PYRAMID BUY ₹2.19 lakh crore at ₹577.50 (box jump — doubling the stake with NEW capital; stop stays ₹520.60; charges ₹258.92 crore)
2023-09-04  HAL         PYRAMID BUY ₹1.23 lakh crore at ₹1,982.17 (box jump — doubling the stake with NEW capital; stop stays ₹1,840.70; charges ₹145.28 crore)
2023-09-04  HEG         PYRAMID BUY ₹63,170.27 crore at ₹351.16 (box jump — doubling the stake with NEW capital; stop stays ₹324.38; charges ₹74.85 crore)
2023-09-18  VARROC      PYRAMID BUY ₹2.43 lakh crore at ₹450.55 (box jump — doubling the stake with NEW capital; stop stays ₹383.80; charges ₹287.37 crore)
2023-09-18  ZFCVINDIA   PYRAMID BUY ₹1.88 lakh crore at ₹2,576.83 (box jump — doubling the stake with NEW capital; stop stays ₹2,402.91; charges ₹223.22 crore)
2023-09-25  FORCEMOT    PYRAMID BUY ₹3.38 lakh crore at ₹3,749.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,341.72; charges ₹399.90 crore)
2023-10-03  VARROC      PYRAMID BUY ₹5.25 lakh crore at ₹487.95 (box jump — doubling the stake with NEW capital; stop stays ₹450.92; charges ₹622.07 crore)
2023-10-16  FORCEMOT    PYRAMID BUY ₹7.07 lakh crore at ₹3,930.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,709.99; charges ₹837.91 crore)
2023-10-16  HEG         PYRAMID BUY ₹1.31 lakh crore at ₹363.94 (box jump — doubling the stake with NEW capital; stop stays ₹328.78; charges ₹155.05 crore)
2023-10-20  FORCEMOT    SELL ₹13.33 lakh crore at stop ₹3,709.99 (+1.8%, charges ₹1,382.78 crore) — the cash goes back to work at the next Friday screen
2023-10-23  APOLLO      BUY ₹4.36 lakh crore at ₹76.15 (fresh Friday signal — BUY: 3.56× weekly, month 3.24×, ladder rising; stop ₹59.94; charges ₹516.50 crore)
2023-10-23  CRISIL      BUY ₹4.27 lakh crore at ₹4,199.70 (fresh Friday signal — BUY: 3.22× weekly, month 2.05×, ladder rising; stop ₹3,639.83; charges ₹506.14 crore)
2023-10-23  HEG         SELL ₹2.36 lakh crore at stop ₹328.78 (-5.6%, charges ₹244.86 crore) — the cash goes back to work at the next Friday screen
2023-10-23  NBCC        BUY ₹4.31 lakh crore at ₹45.87 (fresh Friday signal — BUY: 3.53× weekly, month 3.62×, ladder rising; stop ₹33.69; charges ₹510.95 crore)
2023-10-23  ZFCVINDIA   PYRAMID BUY ₹3.86 lakh crore at ₹2,642.07 (box jump — doubling the stake with NEW capital; stop stays ₹2,473.96; charges ₹457.47 crore)
2023-10-25  HAL         SELL ₹2.27 lakh crore at stop ₹1,840.70 (-3.0%, charges ₹235.85 crore) — the cash goes back to work at the next Friday screen
2023-10-25  VARROC      SELL ₹9.69 lakh crore at stop ₹450.92 (-0.4%, charges ₹1,004.93 crore) — the cash goes back to work at the next Friday screen
2023-10-30  ANGELONE    BUY ₹4.34 lakh crore at ₹253.50 (fresh Friday signal — BUY: 1.84× weekly, month 2.75×, ladder rising; stop ₹194.37; charges ₹514.57 crore)
2023-10-30  CUPID       BUY ₹4.34 lakh crore at ₹6.05 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹3.66; charges ₹513.77 crore)
2023-10-30  SHAREINDIA  BUY ₹4.34 lakh crore at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹514.22 crore)
2023-11-06  APOLLO      PYRAMID BUY ₹5.48 lakh crore at ₹95.90 (box jump — doubling the stake with NEW capital; stop stays ₹60.83; charges ₹649.68 crore)
2023-11-06  NBCC        PYRAMID BUY ₹4.24 lakh crore at ₹45.10 (box jump — doubling the stake with NEW capital; stop stays ₹37.78; charges ₹501.81 crore)
2023-11-06  RATEGAIN    PYRAMID BUY ₹5.30 lakh crore at ₹701.00 (box jump — doubling the stake with NEW capital; stop stays ₹549.53; charges ₹628.21 crore)
2023-11-13  ANGELONE    PYRAMID BUY ₹4.67 lakh crore at ₹273.19 (box jump — doubling the stake with NEW capital; stop stays ₹236.87; charges ₹553.89 crore)
2023-11-13  APOLLO      PYRAMID BUY ₹14.05 lakh crore at ₹122.90 (box jump — doubling the stake with NEW capital; stop stays ₹88.83; charges ₹1,664.21 crore)
2023-11-13  TDPOWERSYS  PYRAMID BUY ₹2.75 lakh crore at ₹135.78 (box jump — doubling the stake with NEW capital; stop stays ₹113.41; charges ₹326.22 crore)
2023-11-20  APOLLO      PYRAMID BUY ₹36.20 lakh crore at ₹158.45 (box jump — doubling the stake with NEW capital; stop stays ₹105.78; charges ₹4,288.65 crore)
2023-11-20  CRISIL      PYRAMID BUY ₹4.31 lakh crore at ₹4,242.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,861.80; charges ₹510.63 crore)
2023-11-20  RATEGAIN    PYRAMID BUY ₹10.92 lakh crore at ₹722.00 (box jump — doubling the stake with NEW capital; stop stays ₹619.50; charges ₹1,293.29 crore)
2023-11-20  SHAREINDIA  PYRAMID BUY ₹5.14 lakh crore at ₹356.00 (box jump — doubling the stake with NEW capital; stop stays ₹280.63; charges ₹609.49 crore)
2023-11-20  TDPOWERSYS  PYRAMID BUY ₹5.49 lakh crore at ₹135.32 (box jump — doubling the stake with NEW capital; stop stays ₹124.59; charges ₹649.90 crore)
2023-11-28  ANGELONE    PYRAMID BUY ₹10.49 lakh crore at ₹306.80 (box jump — doubling the stake with NEW capital; stop stays ₹274.55; charges ₹1,243.30 crore)
2023-11-28  CUPID       PYRAMID BUY ₹6.32 lakh crore at ₹8.82 (box jump — doubling the stake with NEW capital; stop stays ₹7.93; charges ₹748.35 crore)
2023-11-28  SHAREINDIA  PYRAMID BUY ₹9.90 lakh crore at ₹342.61 (box jump — doubling the stake with NEW capital; stop stays ₹321.67; charges ₹1,172.43 crore)
2023-12-18  ANGELONE    PYRAMID BUY ₹22.21 lakh crore at ₹324.80 (box jump — doubling the stake with NEW capital; stop stays ₹279.31; charges ₹2,630.93 crore)
2023-12-18  SHAREINDIA  PYRAMID BUY ₹21.22 lakh crore at ₹367.60 (box jump — doubling the stake with NEW capital; stop stays ₹328.89; charges ₹2,514.40 crore)
2023-12-26  CUPID       PYRAMID BUY ₹13.45 lakh crore at ₹9.40 (box jump — doubling the stake with NEW capital; stop stays ₹8.10; charges ₹1,593.65 crore)
2024-01-01  ANGELONE    PYRAMID BUY ₹47.61 lakh crore at ₹348.40 (box jump — doubling the stake with NEW capital; stop stays ₹296.88; charges ₹5,640.84 crore)
2024-01-01  ICICIBANK   PYRAMID BUY ₹76,285.92 crore at ₹991.55 (box jump — doubling the stake with NEW capital; stop stays ₹939.74; charges ₹90.39 crore)
2024-01-01  NBCC        PYRAMID BUY ₹10.26 lakh crore at ₹54.63 (box jump — doubling the stake with NEW capital; stop stays ₹45.65; charges ₹1,215.05 crore)
2024-01-01  SHAREINDIA  PYRAMID BUY ₹43.12 lakh crore at ₹373.70 (box jump — doubling the stake with NEW capital; stop stays ₹330.37; charges ₹5,109.23 crore)
2024-01-15  RATEGAIN    PYRAMID BUY ₹22.11 lakh crore at ₹731.75 (box jump — doubling the stake with NEW capital; stop stays ₹669.56; charges ₹2,619.95 crore)
2024-01-23  ANGELONE    SELL ₹81.01 lakh crore at stop ₹296.88 (-9.1%, charges ₹8,402.74 crore) — the cash goes back to work at the next Friday screen
2024-01-23  APOLLO      PYRAMID BUY ₹55.07 lakh crore at ₹120.60 (box jump — doubling the stake with NEW capital; stop stays ₹112.10; charges ₹6,524.52 crore)
2024-01-24  CRISIL      SELL ₹7.83 lakh crore at stop ₹3,861.80 (-8.5%, charges ₹812.65 crore) — the cash goes back to work at the next Friday screen
2024-01-29  IDBI        BUY ₹44.03 lakh crore at ₹84.30 (fresh Friday signal — BUY: 8.31× weekly, month 1.96×, ladder rising; stop ₹60.23; charges ₹5,216.82 crore)
2024-01-29  NBCC        PYRAMID BUY ₹29.27 lakh crore at ₹78.00 (box jump — doubling the stake with NEW capital; stop stays ₹53.58; charges ₹3,467.41 crore)
2024-01-29  RITES       BUY ₹47.00 lakh crore at ₹342.50 (fresh Friday signal — BUY: 11.32× weekly, month 2.99×, ladder rising; stop ₹240.21; charges ₹5,568.44 crore)
2024-02-02  ZFCVINDIA   SELL ₹7.22 lakh crore at stop ₹2,473.96 (-0.7%, charges ₹748.83 crore) — the cash goes back to work at the next Friday screen
2024-02-05  CUPID       PYRAMID BUY ₹48.94 lakh crore at ₹17.11 (box jump — doubling the stake with NEW capital; stop stays ₹16.11; charges ₹5,798.22 crore)
2024-02-13  APOLLO      SELL ₹1.02 crore crore at stop ₹112.10 (-11.0%, charges ₹10,601.84 crore) — the cash goes back to work at the next Friday screen
2024-02-19  IDBI        PYRAMID BUY ₹47.71 lakh crore at ₹91.45 (box jump — doubling the stake with NEW capital; stop stays ₹72.11; charges ₹5,652.58 crore)
2024-02-19  NBCC        PYRAMID BUY ₹68.25 lakh crore at ₹91.00 (box jump — doubling the stake with NEW capital; stop stays ₹69.28; charges ₹8,085.82 crore)
2024-02-19  PRUDENT     BUY ₹86.60 lakh crore at ₹1,332.00 (fresh Friday signal — BUY: 19.33× weekly, month 4.96×, ladder rising; stop ₹1,008.17; charges ₹10,260.40 crore)
2024-02-19  RATEGAIN    PYRAMID BUY ₹52.79 lakh crore at ₹874.00 (box jump — doubling the stake with NEW capital; stop stays ₹720.34; charges ₹6,254.81 crore)
2024-02-19  RITES       PYRAMID BUY ₹52.10 lakh crore at ₹380.10 (box jump — doubling the stake with NEW capital; stop stays ₹314.37; charges ₹6,172.42 crore)
2024-02-19  SHAREINDIA  PYRAMID BUY ₹89.12 lakh crore at ₹386.39 (box jump — doubling the stake with NEW capital; stop stays ₹357.20; charges ₹10,559.19 crore)
2024-02-26  CUPID       PYRAMID BUY ₹1.40 crore crore at ₹24.50 (box jump — doubling the stake with NEW capital; stop stays ₹17.77; charges ₹16,596.69 crore)
2024-02-26  PRUDENT     PYRAMID BUY ₹89.75 lakh crore at ₹1,382.05 (box jump — doubling the stake with NEW capital; stop stays ₹1,176.05; charges ₹10,633.32 crore)
2024-03-04  RATEGAIN    PYRAMID BUY ₹99.18 lakh crore at ₹821.50 (box jump — doubling the stake with NEW capital; stop stays ₹730.99; charges ₹11,751.21 crore)
2024-03-06  SHAREINDIA  SELL ₹1.65 crore crore at stop ₹357.20 (-4.6%, charges ₹17,064.39 crore) — the cash goes back to work at the next Friday screen
2024-03-11  BHEL        BUY ₹73.24 lakh crore at ₹259.10 (fresh Friday signal — BUY: 3.01× weekly, month 1.67×, ladder rising; stop ₹188.78; charges ₹8,677.56 crore)
2024-03-11  ICICIBANK   PYRAMID BUY ₹1.67 lakh crore at ₹1,087.95 (box jump — doubling the stake with NEW capital; stop stays ₹986.58; charges ₹198.23 crore)
2024-03-11  SOLARINDS   BUY ₹1.14 crore crore at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹13,518.15 crore)
2024-03-13  PRUDENT     SELL ₹1.52 crore crore at stop ₹1,176.05 (-13.3%, charges ₹15,817.78 crore) — the cash goes back to work at the next Friday screen
2024-03-13  RATEGAIN    SELL ₹1.76 crore crore at stop ₹730.99 (-9.2%, charges ₹18,279.36 crore) — the cash goes back to work at the next Friday screen
2024-03-13  RITES       SELL ₹86.03 lakh crore at stop ₹314.37 (-13.0%, charges ₹8,924.28 crore) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹98.12 lakh crore at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹11,625.42 crore)
2024-03-18  FORCEMOT    BUY ₹1.05 crore crore at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 3.03× weekly, month 1.69×, ladder rising; stop ₹5,500.61; charges ₹12,491.79 crore)
2024-03-18  ICICIBANK   PYRAMID BUY ₹3.30 lakh crore at ₹1,075.05 (box jump — doubling the stake with NEW capital; stop stays ₹1,002.87; charges ₹391.52 crore)
2024-03-18  INDIGO      BUY ₹1.05 crore crore at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹12,474.12 crore)
2024-03-18  JIOFIN      BUY ₹1.06 crore crore at ₹346.95 (fresh Friday signal — BUY: 2.56× weekly, month 2.25×, ladder rising; stop ₹290.75; charges ₹12,548.38 crore)
2024-03-26  BOSCHLTD    PYRAMID BUY ₹1.00 crore crore at ₹30,245.00 (box jump — doubling the stake with NEW capital; stop stays ₹26,710.20; charges ₹11,904.87 crore)
2024-03-26  JIOFIN      PYRAMID BUY ₹1.05 crore crore at ₹345.00 (box jump — doubling the stake with NEW capital; stop stays ₹301.05; charges ₹12,463.07 crore)
2024-04-01  IDBI        PYRAMID BUY ₹84.78 lakh crore at ₹81.30 (box jump — doubling the stake with NEW capital; stop stays ₹74.19; charges ₹10,044.46 crore)
2024-04-01  SOLARINDS   PYRAMID BUY ₹1.35 crore crore at ₹8,950.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,980.95; charges ₹15,976.21 crore)
2024-04-01  TAX         FY2024 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹84.15 lakh crore / LT ₹0.00)
2024-04-08  BOSCHLTD    PYRAMID BUY ₹2.06 crore crore at ₹30,980.00 (box jump — doubling the stake with NEW capital; stop stays ₹28,244.40; charges ₹24,373.90 crore)
2024-04-15  INDIGO      PYRAMID BUY ₹1.21 crore crore at ₹3,670.30 (box jump — doubling the stake with NEW capital; stop stays ₹3,287.00; charges ₹14,290.47 crore)
2024-04-29  FORCEMOT    PYRAMID BUY ₹1.62 crore crore at ₹10,100.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,483.47; charges ₹19,187.48 crore)
2024-04-29  IDBI        PYRAMID BUY ₹1.84 crore crore at ₹88.50 (box jump — doubling the stake with NEW capital; stop stays ₹78.19; charges ₹21,855.05 crore)
2024-04-29  NBCC        PYRAMID BUY ₹1.38 crore crore at ₹92.00 (box jump — doubling the stake with NEW capital; stop stays ₹74.74; charges ₹16,339.67 crore)
2024-05-13  INDIGO      PYRAMID BUY ₹2.63 crore crore at ₹4,006.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,719.77; charges ₹31,177.36 crore)
2024-05-13  NBCC        PYRAMID BUY ₹2.65 crore crore at ₹88.60 (box jump — doubling the stake with NEW capital; stop stays ₹80.15; charges ₹31,452.99 crore)
2024-05-21  BHEL        PYRAMID BUY ₹88.06 lakh crore at ₹311.90 (box jump — doubling the stake with NEW capital; stop stays ₹251.68; charges ₹10,433.52 crore)
2024-05-21  FORCEMOT    PYRAMID BUY ₹2.88 crore crore at ₹8,987.50 (box jump — doubling the stake with NEW capital; stop stays ₹8,083.65; charges ₹34,127.79 crore)
2024-05-21  ICICIBANK   PYRAMID BUY ₹6.89 lakh crore at ₹1,122.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,051.37; charges ₹816.90 crore)
2024-05-21  JIOFIN      PYRAMID BUY ₹2.20 crore crore at ₹361.00 (box jump — doubling the stake with NEW capital; stop stays ₹317.61; charges ₹26,066.68 crore)
2024-05-21  TDPOWERSYS  PYRAMID BUY ₹13.29 lakh crore at ₹164.00 (box jump — doubling the stake with NEW capital; stop stays ₹129.90; charges ₹1,574.29 crore)
2024-05-27  BOSCHLTD    PYRAMID BUY ₹4.10 crore crore at ₹30,901.00 (box jump — doubling the stake with NEW capital; stop stays ₹29,015.09; charges ₹48,594.69 crore)
2024-05-28  FORCEMOT    SELL ₹5.17 crore crore at stop ₹8,083.65 (-6.7%, charges ₹53,660.08 crore) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹4.02 crore crore at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹47,606.58 crore)
2024-06-04  BHEL        SELL ₹1.42 crore crore at stop ₹251.68 (-11.8%, charges ₹14,717.66 crore) — the cash goes back to work at the next Friday screen
2024-06-04  BOSCHLTD    SELL ₹7.69 crore crore at stop ₹29,015.09 (-5.4%, charges ₹79,765.44 crore) — the cash goes back to work at the next Friday screen
2024-06-04  CUPID       SELL ₹2.03 crore crore at stop ₹17.77 (-4.6%, charges ₹21,043.47 crore) — the cash goes back to work at the next Friday screen
2024-06-04  IDBI        SELL ₹3.25 crore crore at stop ₹78.19 (-9.7%, charges ₹33,754.71 crore) — the cash goes back to work at the next Friday screen
2024-06-04  JIOFIN      SELL ₹3.86 crore crore at stop ₹317.61 (-10.1%, charges ₹40,091.04 crore) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹2.40 crore crore at stop ₹7,980.95 (-3.3%, charges ₹24,904.62 crore) — the cash goes back to work at the next Friday screen
2024-06-05  ICICIBANK   SELL ₹12.90 lakh crore at stop ₹1,051.37 (-3.3%, charges ₹1,337.92 crore) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹4.79 crore crore at ₹156.60 (fresh Friday signal — BUY: 7.81× weekly, month 1.77×, ladder rising; stop ₹126.55; charges ₹56,748.78 crore)
2024-06-10  CAMPUS      PYRAMID BUY ₹4.06 crore crore at ₹289.00 (box jump — doubling the stake with NEW capital; stop stays ₹248.05; charges ₹48,048.96 crore)
2024-06-10  DABUR       BUY ₹4.77 crore crore at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹56,506.95 crore)
2024-06-10  FIEMIND     BUY ₹4.81 crore crore at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹56,930.86 crore)
2024-06-10  INDIGO      PYRAMID BUY ₹5.77 crore crore at ₹4,398.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,805.04; charges ₹68,414.07 crore)
2024-06-10  NCC         BUY ₹2.80 crore crore at ₹327.60 (fresh Friday signal — BUY: 2.80× weekly, month 1.63×, ladder rising; stop ₹260.92; charges ₹33,130.91 crore)
2024-06-10  UNOMINDA    BUY ₹4.78 crore crore at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.61×, ladder rising; stop ₹769.64; charges ₹56,645.78 crore)
2024-06-18  DABUR       PYRAMID BUY ₹4.79 crore crore at ₹608.10 (box jump — doubling the stake with NEW capital; stop stays ₹552.95; charges ₹56,804.31 crore)
2024-06-18  UNOMINDA    PYRAMID BUY ₹5.20 crore crore at ₹1,056.60 (box jump — doubling the stake with NEW capital; stop stays ₹895.00; charges ₹61,629.91 crore)
2024-06-24  FIEMIND     PYRAMID BUY ₹4.68 crore crore at ₹1,286.35 (box jump — doubling the stake with NEW capital; stop stays ₹1,162.80; charges ₹55,413.82 crore)
2024-07-01  INDIGO      PYRAMID BUY ₹11.22 crore crore at ₹4,276.35 (box jump — doubling the stake with NEW capital; stop stays ₹3,976.70; charges ₹1.33 lakh crore)
2024-07-01  NCC         PYRAMID BUY ₹2.70 crore crore at ₹316.50 (box jump — doubling the stake with NEW capital; stop stays ₹297.87; charges ₹31,970.42 crore)
2024-07-08  NBCC        PYRAMID BUY ₹7.57 crore crore at ₹126.34 (box jump — doubling the stake with NEW capital; stop stays ₹98.17; charges ₹89,648.22 crore)
2024-07-08  TDPOWERSYS  PYRAMID BUY ₹33.14 lakh crore at ₹204.62 (box jump — doubling the stake with NEW capital; stop stays ₹162.59; charges ₹3,926.19 crore)
2024-07-08  UNOMINDA    PYRAMID BUY ₹11.56 crore crore at ₹1,174.40 (box jump — doubling the stake with NEW capital; stop stays ₹981.87; charges ₹1.37 lakh crore)
2024-07-15  TDPOWERSYS  PYRAMID BUY ₹66.00 lakh crore at ₹203.90 (box jump — doubling the stake with NEW capital; stop stays ₹188.72; charges ₹7,819.93 crore)
2024-07-19  TDPOWERSYS  SELL ₹1.22 crore crore at stop ₹188.72 (-0.7%, charges ₹12,652.56 crore) — the cash goes back to work at the next Friday screen
2024-07-19  UNOMINDA    SELL ₹19.29 crore crore at stop ₹981.87 (-10.2%, charges ₹2.00 lakh crore) — the cash goes back to work at the next Friday screen
2024-07-22  FIEMIND     PYRAMID BUY ₹9.44 crore crore at ₹1,299.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,257.56; charges ₹1.12 lakh crore)
2024-07-22  INDIAGLYCO  BUY ₹10.04 crore crore at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹1.19 lakh crore)
2024-07-22  PGIL        BUY ₹10.47 crore crore at ₹405.00 (fresh Friday signal — BUY: 3.81× weekly, month 8.12×, ladder rising; stop ₹335.38; charges ₹1.24 lakh crore)
2024-07-23  FIEMIND     SELL ₹18.25 crore crore at stop ₹1,257.56 (-3.3%, charges ₹1.89 lakh crore) — the cash goes back to work at the next Friday screen
2024-07-23  NCC         SELL ₹5.07 crore crore at stop ₹297.87 (-7.5%, charges ₹52,598.81 crore) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹10.94 crore crore at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹1.30 lakh crore)
2024-07-29  THYROCARE   BUY ₹10.95 crore crore at ₹261.67 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹196.33; charges ₹1.30 lakh crore)
2024-08-05  DABUR       PYRAMID BUY ₹9.69 crore crore at ₹615.00 (box jump — doubling the stake with NEW capital; stop stays ₹587.15; charges ₹1.15 lakh crore)
2024-08-05  NBCC        PYRAMID BUY ₹13.87 crore crore at ₹115.87 (box jump — doubling the stake with NEW capital; stop stays ₹109.78; charges ₹1.64 lakh crore)
2024-08-05  THYROCARE   PYRAMID BUY ₹11.15 crore crore at ₹266.65 (box jump — doubling the stake with NEW capital; stop stays ₹243.17; charges ₹1.32 lakh crore)
2024-08-06  NBCC        SELL ₹26.24 crore crore at stop ₹109.78 (-1.3%, charges ₹2.72 lakh crore) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹3.86 crore crore at stop ₹126.55 (-19.2%, charges ₹40,060.28 crore) — the cash goes back to work at the next Friday screen
2024-08-12  AVANTIFEED  PYRAMID BUY ₹11.88 crore crore at ₹758.00 (box jump — doubling the stake with NEW capital; stop stays ₹596.83; charges ₹1.41 lakh crore)
2024-08-12  CAMPUS      PYRAMID BUY ₹8.19 crore crore at ₹291.85 (box jump — doubling the stake with NEW capital; stop stays ₹277.07; charges ₹96,988.10 crore)
2024-08-12  CERA        BUY ₹18.48 crore crore at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹2.19 lakh crore)
2024-08-12  INDIAGLYCO  PYRAMID BUY ₹11.70 crore crore at ₹600.55 (box jump — doubling the stake with NEW capital; stop stays ₹535.82; charges ₹1.39 lakh crore)
2024-08-12  PGIL        PYRAMID BUY ₹12.40 crore crore at ₹480.18 (box jump — doubling the stake with NEW capital; stop stays ₹388.64; charges ₹1.47 lakh crore)
2024-08-16  CAMPUS      SELL ₹15.52 crore crore at stop ₹277.07 (-4.4%, charges ₹1.61 lakh crore) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹18.47 crore crore at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.15×, ladder rising; stop ₹361.00; charges ₹2.19 lakh crore)
2024-08-19  VGUARD      BUY ₹10.09 crore crore at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹1.20 lakh crore)
2024-08-26  AVANTIFEED  PYRAMID BUY ₹21.76 crore crore at ₹695.00 (box jump — doubling the stake with NEW capital; stop stays ₹650.13; charges ₹2.58 lakh crore)
2024-08-26  INDIAGLYCO  PYRAMID BUY ₹24.78 crore crore at ₹636.50 (box jump — doubling the stake with NEW capital; stop stays ₹587.91; charges ₹2.94 lakh crore)
2024-08-26  SUPRIYA     PYRAMID BUY ₹19.50 crore crore at ₹558.30 (box jump — doubling the stake with NEW capital; stop stays ₹470.87; charges ₹2.31 lakh crore)
2024-09-09  AVANTIFEED  SELL ₹40.65 crore crore at stop ₹650.13 (-8.6%, charges ₹4.22 lakh crore) — the cash goes back to work at the next Friday screen
2024-09-09  INDIGO      PYRAMID BUY ₹25.07 crore crore at ₹4,780.00 (box jump — doubling the stake with NEW capital; stop stays ₹4,485.14; charges ₹2.97 lakh crore)
2024-09-09  SUPRIYA     PYRAMID BUY ₹41.90 crore crore at ₹600.00 (box jump — doubling the stake with NEW capital; stop stays ₹498.75; charges ₹4.96 lakh crore)
2024-09-09  THYROCARE   PYRAMID BUY ₹23.55 crore crore at ₹281.75 (box jump — doubling the stake with NEW capital; stop stays ₹265.38; charges ₹2.79 lakh crore)
2024-09-16  DABUR       PYRAMID BUY ₹20.79 crore crore at ₹660.00 (box jump — doubling the stake with NEW capital; stop stays ₹602.49; charges ₹2.46 lakh crore)
2024-09-16  PGIL        PYRAMID BUY ₹25.16 crore crore at ₹487.50 (box jump — doubling the stake with NEW capital; stop stays ₹434.53; charges ₹2.98 lakh crore)
2024-09-16  PRSMJOHNSN  BUY ₹39.31 crore crore at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹4.66 lakh crore)
2024-09-19  CERA        SELL ₹14.40 crore crore at stop ₹8,198.93 (-21.9%, charges ₹1.49 lakh crore) — the cash goes back to work at the next Friday screen
2024-09-23  PGIL        SELL ₹44.78 crore crore at stop ₹434.53 (-6.6%, charges ₹4.65 lakh crore) — the cash goes back to work at the next Friday screen
2024-09-30  PRSMJOHNSN  PYRAMID BUY ₹38.25 crore crore at ₹209.00 (box jump — doubling the stake with NEW capital; stop stays ₹168.72; charges ₹4.53 lakh crore)
2024-09-30  VIYASH      BUY ₹40.52 crore crore at ₹216.00 (fresh Friday signal — BUY: 5.97× weekly, month 2.57×, ladder rising; stop ₹161.73; charges ₹4.80 lakh crore)
2024-10-03  DABUR       SELL ₹37.89 crore crore at stop ₹602.49 (-5.2%, charges ₹3.93 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹8.07 crore crore at stop ₹420.24 (-19.8%, charges ₹83,735.10 crore) — the cash goes back to work at the next Friday screen
2024-10-07  BSE         BUY ₹27.35 crore crore at ₹1,396.67 (fresh Friday signal — ACCUMULATE: 2.88× weekly, month 3.26×, ladder rising; stop ₹1,131.31; charges ₹3.24 lakh crore)
2024-10-07  CEMPRO      BUY ₹38.62 crore crore at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹4.58 lakh crore)
2024-10-07  INDIGO      SELL ₹46.98 crore crore at stop ₹4,485.14 (+0.3%, charges ₹4.87 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹44.28 crore crore at stop ₹265.38 (-2.8%, charges ₹4.59 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-14  PAYTM       BUY ₹39.95 crore crore at ₹729.60 (fresh Friday signal — BUY: 1.93× weekly, month 2.08×, ladder rising; stop ₹617.60; charges ₹4.73 lakh crore)
2024-10-14  SKIPPER     BUY ₹51.31 crore crore at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.80×, ladder rising; stop ₹418.00; charges ₹6.08 lakh crore)
2024-10-14  SUPRIYA     PYRAMID BUY ₹79.84 crore crore at ₹572.00 (box jump — doubling the stake with NEW capital; stop stays ₹500.65; charges ₹9.46 lakh crore)
2024-10-14  VIYASH      PYRAMID BUY ₹35.88 crore crore at ₹191.50 (box jump — doubling the stake with NEW capital; stop stays ₹172.84; charges ₹4.25 lakh crore)
2024-10-23  VIYASH      SELL ₹64.66 crore crore at stop ₹172.84 (-15.2%, charges ₹6.71 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹45.69 crore crore at stop ₹587.91 (-1.5%, charges ₹4.74 lakh crore) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       PYRAMID BUY ₹40.89 crore crore at ₹747.70 (box jump — doubling the stake with NEW capital; stop stays ₹636.31; charges ₹4.84 lakh crore)
2024-10-28  PRSMJOHNSN  PYRAMID BUY ₹69.88 crore crore at ₹191.00 (box jump — doubling the stake with NEW capital; stop stays ₹170.55; charges ₹8.28 lakh crore)
2024-11-04  BSE         PYRAMID BUY ₹28.98 crore crore at ₹1,481.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,231.60; charges ₹6.84 lakh crore)
2024-11-04  CEMPRO      PYRAMID BUY ₹32.22 crore crore at ₹547.15 (box jump — doubling the stake with NEW capital; stop stays ₹430.14; charges ₹7.61 lakh crore)
2024-11-04  JSWDULUX    BUY ₹72.93 crore crore at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹17.22 lakh crore)
2024-11-04  KIRLPNU     BUY ₹37.43 crore crore at ₹849.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.99×, ladder rising; stop ₹594.25; charges ₹8.84 lakh crore)
2024-11-04  SKIPPER     PYRAMID BUY ₹50.62 crore crore at ₹546.15 (box jump — doubling the stake with NEW capital; stop stays ₹448.15; charges ₹11.95 lakh crore)
2024-11-11  KIRLPNU     PYRAMID BUY ₹37.16 crore crore at ₹845.00 (box jump — doubling the stake with NEW capital; stop stays ₹752.42; charges ₹8.77 lakh crore)
2024-11-25  PAYTM       PYRAMID BUY ₹99.89 crore crore at ₹913.80 (box jump — doubling the stake with NEW capital; stop stays ₹712.50; charges ₹23.58 lakh crore)
2024-11-25  SUPRIYA     PYRAMID BUY ₹225.70 crore crore at ₹809.00 (box jump — doubling the stake with NEW capital; stop stays ₹574.32; charges ₹53.28 lakh crore)
2024-12-09  JSWDULUX    PYRAMID BUY ₹59.89 crore crore at ₹3,718.70 (box jump — doubling the stake with NEW capital; stop stays ₹3,423.18; charges ₹14.14 lakh crore)
2024-12-09  PAYTM       PYRAMID BUY ₹217.81 crore crore at ₹997.45 (box jump — doubling the stake with NEW capital; stop stays ₹838.09; charges ₹51.42 lakh crore)
2024-12-09  SUPRIYA     PYRAMID BUY ₹434.70 crore crore at ₹780.00 (box jump — doubling the stake with NEW capital; stop stays ₹717.25; charges ₹1.03 crore crore)
2024-12-16  CEMPRO      PYRAMID BUY ₹60.57 crore crore at ₹514.85 (box jump — doubling the stake with NEW capital; stop stays ₹477.71; charges ₹14.30 lakh crore)
2024-12-16  KIRLPNU     PYRAMID BUY ₹74.41 crore crore at ₹846.95 (box jump — doubling the stake with NEW capital; stop stays ₹798.00; charges ₹17.57 lakh crore)
2024-12-17  SUPRIYA     SELL ₹796.74 crore crore at stop ₹717.25 (-2.4%, charges ₹1.77 crore crore) — the cash goes back to work at the next Friday screen
2024-12-23  KAYNES      BUY ₹231.79 crore crore at ₹7,358.80 (fresh Friday signal — BUY: 3.40× weekly, month 2.00×, ladder rising; stop ₹5,824.55; charges ₹54.72 lakh crore)
2024-12-23  KIRLPNU     SELL ₹139.75 crore crore at stop ₹798.00 (-5.8%, charges ₹31.04 lakh crore) — the cash goes back to work at the next Friday screen
2024-12-23  PAYTM       PYRAMID BUY ₹418.69 crore crore at ₹959.80 (box jump — doubling the stake with NEW capital; stop stays ₹887.49; charges ₹98.84 lakh crore)
2024-12-23  ZENTEC      BUY ₹231.64 crore crore at ₹2,555.00 (fresh Friday signal — BUY: 3.53× weekly, month 2.25×, ladder rising; stop ₹1,537.95; charges ₹54.68 lakh crore)
2024-12-26  PRSMJOHNSN  SELL ₹124.44 crore crore at stop ₹170.55 (-15.3%, charges ₹27.64 lakh crore) — the cash goes back to work at the next Friday screen
2024-12-27  JSWDULUX    SELL ₹109.88 crore crore at stop ₹3,423.18 (-16.9%, charges ₹24.41 lakh crore) — the cash goes back to work at the next Friday screen
2024-12-30  KAYNES      PYRAMID BUY ₹222.73 crore crore at ₹7,088.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,670.80; charges ₹52.58 lakh crore)
2024-12-30  KFINTECH    BUY ₹344.92 crore crore at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.22×, ladder rising; stop ₹1,159.14; charges ₹81.42 lakh crore)
2024-12-30  PAYTM       PYRAMID BUY ₹886.24 crore crore at ₹1,017.00 (box jump — doubling the stake with NEW capital; stop stays ₹893.05; charges ₹2.09 crore crore)
2025-01-06  BSE         PYRAMID BUY ₹69.69 crore crore at ₹1,783.33 (box jump — doubling the stake with NEW capital; stop stays ₹1,651.54; charges ₹16.45 lakh crore)
2025-01-06  LLOYDSME    BUY ₹362.45 crore crore at ₹1,439.00 (fresh Friday signal — BUY: 2.97× weekly, month 1.94×, ladder rising; stop ₹1,064.09; charges ₹85.56 lakh crore)
2025-01-06  SKIPPER     PYRAMID BUY ₹103.14 crore crore at ₹557.10 (box jump — doubling the stake with NEW capital; stop stays ₹477.28; charges ₹24.35 lakh crore)
2025-01-06  ZENTEC      PYRAMID BUY ₹229.15 crore crore at ₹2,533.45 (box jump — doubling the stake with NEW capital; stop stays ₹2,213.55; charges ₹54.09 lakh crore)
2025-01-09  PAYTM       SELL ₹1,551.17 crore crore at stop ₹893.05 (-8.5%, charges ₹3.45 crore crore) — the cash goes back to work at the next Friday screen
2025-01-10  KAYNES      SELL ₹417.82 crore crore at stop ₹6,670.80 (-7.7%, charges ₹92.80 lakh crore) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹176.12 crore crore at stop ₹477.28 (-13.7%, charges ₹39.12 lakh crore) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹378.29 crore crore at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 4.81×, ladder rising; stop ₹697.76; charges ₹89.30 lakh crore)
2025-01-13  LLOYDSME    PYRAMID BUY ₹362.33 crore crore at ₹1,441.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,258.75; charges ₹85.53 lakh crore)
2025-01-13  ZENTEC      SELL ₹399.07 crore crore at stop ₹2,213.55 (-13.0%, charges ₹88.64 lakh crore) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹263.31 crore crore at stop ₹1,159.14 (-23.3%, charges ₹58.49 lakh crore) — the cash goes back to work at the next Friday screen
2025-01-20  AEGISLOG    PYRAMID BUY ₹363.36 crore crore at ₹803.60 (box jump — doubling the stake with NEW capital; stop stays ₹700.36; charges ₹85.78 lakh crore)
2025-01-20  APOLLO      BUY ₹412.57 crore crore at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 5.79×, ladder rising; stop ₹110.19; charges ₹97.39 lakh crore)
2025-01-24  AEGISLOG    SELL ₹631.21 crore crore at stop ₹700.36 (-14.5%, charges ₹1.40 crore crore) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹394.54 crore crore at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹93.14 lakh crore)
2025-01-28  LLOYDSME    SELL ₹630.46 crore crore at stop ₹1,258.75 (-12.6%, charges ₹1.40 crore crore) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹400.25 crore crore at ₹947.00 (fresh Friday signal — BUY: 4.92× weekly, month 3.02×, ladder rising; stop ₹727.84; charges ₹94.48 lakh crore)
2025-02-10  ZENSARTECH  PYRAMID BUY ₹387.94 crore crore at ₹920.05 (box jump — doubling the stake with NEW capital; stop stays ₹814.20; charges ₹91.58 lakh crore)
2025-02-17  APOLLO      SELL ₹344.13 crore crore at stop ₹110.19 (-16.2%, charges ₹76.44 lakh crore) — the cash goes back to work at the next Friday screen
2025-02-17  ZENSARTECH  SELL ₹684.28 crore crore at stop ₹814.20 (-12.8%, charges ₹1.52 crore crore) — the cash goes back to work at the next Friday screen
2025-02-28  BSE         SELL ₹128.63 crore crore at stop ₹1,651.54 (+2.5%, charges ₹28.57 lakh crore) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹417.95 crore crore at ₹1,450.00 (fresh Friday signal — BUY: 4.67× weekly, month 1.70×, ladder rising; stop ₹1,235.90; charges ₹98.66 lakh crore)
2025-03-10  CREDITACC   PYRAMID BUY ₹448.59 crore crore at ₹968.75 (box jump — doubling the stake with NEW capital; stop stays ₹837.38; charges ₹1.06 crore crore)
2025-03-17  NH          PYRAMID BUY ₹437.38 crore crore at ₹1,521.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,436.97; charges ₹1.03 crore crore)
2025-03-24  INDIASHLTR  BUY ₹523.43 crore crore at ₹794.95 (fresh Friday signal — BUY: 4.59× weekly, month 1.56×, ladder rising; stop ₹692.55; charges ₹1.24 crore crore)
2025-04-01  INDIASHLTR  PYRAMID BUY ₹545.09 crore crore at ₹829.80 (box jump — doubling the stake with NEW capital; stop stays ₹738.82; charges ₹1.29 crore crore)
2025-04-01  TAX         FY2025 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹820.19 crore crore / LT ₹0.00)
2025-04-07  CEMPRO      PYRAMID BUY ₹129.26 crore crore at ₹550.00 (box jump — doubling the stake with NEW capital; stop stays ₹524.92; charges ₹30.51 lakh crore)
2025-04-07  INDIASHLTR  SELL ₹967.36 crore crore at stop ₹738.82 (-9.1%, charges ₹2.15 crore crore) — the cash goes back to work at the next Friday screen
2025-04-11  CEMPRO      SELL ₹245.89 crore crore at stop ₹524.92 (-5.3%, charges ₹54.62 lakh crore) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹589.31 crore crore at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.61× weekly, month 1.63×, ladder rising; stop ₹492.75; charges ₹1.39 crore crore)
2025-04-15  INDIASHLTR  BUY ₹588.23 crore crore at ₹865.00 (fresh Friday signal — BUY: 1.66× weekly, month 2.04×, ladder rising; stop ₹738.82; charges ₹1.39 crore crore)
2025-04-21  GALLANTT    BUY ₹606.84 crore crore at ₹474.75 (fresh Friday signal — BUY: 3.71× weekly, month 3.71×, ladder rising; stop ₹328.99; charges ₹1.43 crore crore)
2025-04-28  FORCEMOT    BUY ₹600.30 crore crore at ₹9,275.00 (fresh Friday signal — ACCUMULATE: 1.94× weekly, month 1.70×, ladder rising; stop ₹7,633.31; charges ₹1.42 crore crore)
2025-04-28  SMLMAH      BUY ₹598.47 crore crore at ₹1,680.00 (fresh Friday signal — BUY: 1.70× weekly, month 3.85×, ladder rising; stop ₹1,419.23; charges ₹1.41 crore crore)
2025-04-28  WHIRLPOOL   BUY ₹598.07 crore crore at ₹1,153.90 (fresh Friday signal — BUY: 2.17× weekly, month 1.78×, ladder rising; stop ₹1,017.54; charges ₹1.41 crore crore)
2025-05-05  PARAS       BUY ₹331.21 crore crore at ₹686.10 (fresh Friday signal — BUY: 25.11× weekly, month 4.49×, ladder rising; stop ₹486.64; charges ₹78.19 lakh crore)
2025-05-12  CREDITACC   PYRAMID BUY ₹1,062.50 crore crore at ₹1,148.60 (box jump — doubling the stake with NEW capital; stop stays ₹1,019.35; charges ₹2.51 crore crore)
2025-05-12  INDIASHLTR  PYRAMID BUY ₹629.38 crore crore at ₹927.70 (box jump — doubling the stake with NEW capital; stop stays ₹804.65; charges ₹1.49 crore crore)
2025-05-12  NH          PYRAMID BUY ₹1,050.65 crore crore at ₹1,829.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,641.69; charges ₹2.48 crore crore)
2025-05-12  PARAS       PYRAMID BUY ₹361.20 crore crore at ₹750.00 (box jump — doubling the stake with NEW capital; stop stays ₹617.98; charges ₹85.27 lakh crore)
2025-05-19  FORCEMOT    PYRAMID BUY ₹707.33 crore crore at ₹10,954.50 (box jump — doubling the stake with NEW capital; stop stays ₹8,910.52; charges ₹1.67 crore crore)
2025-05-19  GALLANTT    PYRAMID BUY ₹608.28 crore crore at ₹477.00 (box jump — doubling the stake with NEW capital; stop stays ₹371.68; charges ₹1.44 crore crore)
2025-05-19  WHIRLPOOL   PYRAMID BUY ₹677.89 crore crore at ₹1,311.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,111.50; charges ₹1.60 crore crore)
2025-06-02  CREDITACC   PYRAMID BUY ₹2,106.59 crore crore at ₹1,140.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,029.71; charges ₹4.97 crore crore)
2025-06-02  FORCEMOT    PYRAMID BUY ₹1,643.55 crore crore at ₹12,742.00 (box jump — doubling the stake with NEW capital; stop stays ₹9,650.58; charges ₹3.88 crore crore)
2025-06-02  PARAS       PYRAMID BUY ₹770.13 crore crore at ₹800.50 (box jump — doubling the stake with NEW capital; stop stays ₹708.99; charges ₹1.82 crore crore)
2025-06-23  FORCEMOT    PYRAMID BUY ₹3,653.49 crore crore at ₹14,179.00 (box jump — doubling the stake with NEW capital; stop stays ₹11,433.25; charges ₹8.62 crore crore)
2025-06-23  WHIRLPOOL   PYRAMID BUY ₹1,374.83 crore crore at ₹1,331.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,233.96; charges ₹3.25 crore crore)
2025-06-30  FORCEMOT    PYRAMID BUY ₹7,520.20 crore crore at ₹14,610.00 (box jump — doubling the stake with NEW capital; stop stays ₹12,858.25; charges ₹17.75 crore crore)
2025-06-30  NH          PYRAMID BUY ₹2,553.23 crore crore at ₹2,225.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,763.87; charges ₹6.03 crore crore)
2025-07-07  GALLANTT    PYRAMID BUY ₹1,406.18 crore crore at ₹552.00 (box jump — doubling the stake with NEW capital; stop stays ₹494.33; charges ₹3.32 crore crore)
2025-07-07  WHIRLPOOL   PYRAMID BUY ₹2,841.33 crore crore at ₹1,377.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,301.97; charges ₹6.71 crore crore)
2025-07-14  CREDITACC   PYRAMID BUY ₹4,809.91 crore crore at ₹1,303.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,193.20; charges ₹11.35 crore crore)
2025-07-14  FORCEMOT    PYRAMID BUY ₹16,884.80 crore crore at ₹16,421.00 (box jump — doubling the stake with NEW capital; stop stays ₹13,468.15; charges ₹39.86 crore crore)
2025-07-21  FORCEMOT    PYRAMID BUY ₹34,132.34 crore crore at ₹16,617.00 (box jump — doubling the stake with NEW capital; stop stays ₹15,350.10; charges ₹80.57 crore crore)
2025-07-21  GALLANTT    PYRAMID BUY ₹2,987.40 crore crore at ₹587.05 (box jump — doubling the stake with NEW capital; stop stays ₹544.35; charges ₹7.05 crore crore)
2025-07-21  SMLMAH      PYRAMID BUY ₹1,176.38 crore crore at ₹3,310.10 (box jump — doubling the stake with NEW capital; stop stays ₹2,822.07; charges ₹2.78 crore crore)
2025-07-28  NH          PYRAMID BUY ₹4,527.35 crore crore at ₹1,975.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,814.78; charges ₹10.69 crore crore)
2025-07-28  PARAS       SELL ₹1,359.55 crore crore at stop ₹708.99 (-6.6%, charges ₹3.02 crore crore) — the cash goes back to work at the next Friday screen
2025-08-04  INDIASHLTR  PYRAMID BUY ₹1,223.13 crore crore at ₹902.50 (box jump — doubling the stake with NEW capital; stop stays ₹853.86; charges ₹2.89 crore crore)
2025-08-04  NH          SELL ₹8,291.91 crore crore at stop ₹1,814.78 (-7.3%, charges ₹18.42 crore crore) — the cash goes back to work at the next Friday screen
2025-08-07  WHIRLPOOL   SELL ₹5,354.79 crore crore at stop ₹1,301.97 (-2.1%, charges ₹11.89 crore crore) — the cash goes back to work at the next Friday screen
2025-08-11  RAIN        BUY ₹11,666.54 crore crore at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.83×, ladder rising; stop ₹143.64; charges ₹27.54 crore crore)
2025-08-11  SMLMAH      PYRAMID BUY ₹2,802.86 crore crore at ₹3,948.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,878.57; charges ₹6.62 crore crore)
2025-08-18  INDIASHLTR  PYRAMID BUY ₹2,520.52 crore crore at ₹931.00 (box jump — doubling the stake with NEW capital; stop stays ₹862.60; charges ₹5.95 crore crore)
2025-08-25  GALLANTT    PYRAMID BUY ₹6,241.71 crore crore at ₹614.00 (box jump — doubling the stake with NEW capital; stop stays ₹557.33; charges ₹14.73 crore crore)
2025-08-26  RAIN        SELL ₹10,409.49 crore crore at stop ₹143.64 (-10.4%, charges ₹23.12 crore crore) — the cash goes back to work at the next Friday screen
2025-09-08  CREDITACC   PYRAMID BUY ₹9,880.57 crore crore at ₹1,339.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,256.94; charges ₹23.32 crore crore)
2025-09-08  NETWEB      BUY ₹12,813.13 crore crore at ₹3,135.50 (fresh Friday signal — BUY: 6.14× weekly, month 4.05×, ladder rising; stop ₹2,081.16; charges ₹30.25 crore crore)
2025-09-22  SMLMAH      PYRAMID BUY ₹5,344.67 crore crore at ₹3,768.60 (box jump — doubling the stake with NEW capital; stop stays ₹3,255.67; charges ₹12.62 crore crore)
2025-09-25  INDIASHLTR  SELL ₹4,654.83 crore crore at stop ₹862.60 (-5.7%, charges ₹10.34 crore crore) — the cash goes back to work at the next Friday screen
2025-09-26  SMLMAH      SELL ₹9,203.11 crore crore at stop ₹3,255.67 (-6.8%, charges ₹20.44 crore crore) — the cash goes back to work at the next Friday screen
2025-09-29  CREDITACC   PYRAMID BUY ₹20,269.59 crore crore at ₹1,376.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,274.42; charges ₹47.85 crore crore)
2025-09-29  GALLANTT    PYRAMID BUY ₹13,280.97 crore crore at ₹654.00 (box jump — doubling the stake with NEW capital; stop stays ₹616.41; charges ₹31.35 crore crore)
2025-09-29  NETWEB      PYRAMID BUY ₹15,084.25 crore crore at ₹3,700.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,674.79; charges ₹35.61 crore crore)
2025-09-29  SUBROS      BUY ₹14,794.02 crore crore at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹34.92 crore crore)
2025-10-06  AVANTIFEED  PYRAMID BUY ₹469.33 crore crore at ₹653.00 (box jump — doubling the stake with NEW capital; stop stays ₹497.91; charges ₹1.11 crore crore)
2025-10-06  SUBROS      PYRAMID BUY ₹14,018.54 crore crore at ₹1,075.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,046.90; charges ₹33.09 crore crore)
2025-10-09  FORCEMOT    SELL ₹62,846.08 crore crore at stop ₹15,350.10 (-3.1%, charges ₹139.59 crore crore) — the cash goes back to work at the next Friday screen
2025-10-13  AVANTIFEED  PYRAMID BUY ₹943.94 crore crore at ₹657.45 (box jump — doubling the stake with NEW capital; stop stays ₹511.29; charges ₹2.23 crore crore)
2025-10-13  SHAILY      BUY ₹19,186.12 crore crore at ₹2,434.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 1.99×, ladder rising; stop ₹1,942.00; charges ₹45.29 crore crore)
2025-10-13  VIYASH      BUY ₹19,171.84 crore crore at ₹216.04 (fresh Friday signal — BUY: 3.38× weekly, month 2.33×, ladder rising; stop ₹174.14; charges ₹45.26 crore crore)
2025-10-14  SUBROS      SELL ₹27,206.47 crore crore at stop ₹1,046.90 (-5.1%, charges ₹60.43 crore crore) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹18,624.11 crore crore at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.36×, ladder rising; stop ₹1,311.00; charges ₹43.96 crore crore)
2025-10-20  AVANTIFEED  PYRAMID BUY ₹1,972.42 crore crore at ₹687.70 (box jump — doubling the stake with NEW capital; stop stays ₹600.07; charges ₹4.66 crore crore)
2025-10-20  CIEINDIA    BUY ₹18,651.17 crore crore at ₹432.50 (fresh Friday signal — ACCUMULATE: 5.23× weekly, month 2.05×, ladder rising; stop ₹377.39; charges ₹44.03 crore crore)
2025-10-20  CREDITACC   SELL ₹37,419.05 crore crore at stop ₹1,274.42 (-3.5%, charges ₹83.11 crore crore) — the cash goes back to work at the next Friday screen
2025-10-20  GALLANTT    SELL ₹24,950.27 crore crore at stop ₹616.41 (-0.3%, charges ₹55.42 crore crore) — the cash goes back to work at the next Friday screen
2025-10-27  ANANDRATHI  PYRAMID BUY ₹18,491.05 crore crore at ₹1,566.95 (box jump — doubling the stake with NEW capital; stop stays ₹1,450.17; charges ₹43.65 crore crore)
2025-10-27  VIYASH      PYRAMID BUY ₹17,966.81 crore crore at ₹202.94 (box jump — doubling the stake with NEW capital; stop stays ₹185.91; charges ₹42.41 crore crore)
2025-11-03  MAHABANK    BUY ₹25,619.27 crore crore at ₹59.70 (fresh Friday signal — ACCUMULATE: 2.08× weekly, month 1.71×, ladder rising; stop ₹53.69; charges ₹60.48 crore crore)
2025-11-03  NETWEB      PYRAMID BUY ₹31,419.64 crore crore at ₹3,858.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,515.95; charges ₹74.17 crore crore)
2025-11-03  TDPOWERSYS  BUY ₹25,453.23 crore crore at ₹382.27 (fresh Friday signal — BUY: 4.87× weekly, month 1.96×, ladder rising; stop ₹276.78; charges ₹60.09 crore crore)
2025-11-06  NETWEB      SELL ₹57,073.59 crore crore at stop ₹3,515.95 (-3.3%, charges ₹126.77 crore crore) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹25,241.92 crore crore at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹59.59 crore crore)
2025-11-10  CUB         BUY ₹25,368.84 crore crore at ₹190.65 (fresh Friday signal — BUY: 6.02× weekly, month 1.75×, ladder rising; stop ₹160.31; charges ₹59.89 crore crore)
2025-11-10  LTF         BUY ₹25,359.76 crore crore at ₹304.00 (fresh Friday signal — BUY: 2.98× weekly, month 1.55×, ladder rising; stop ₹250.80; charges ₹59.87 crore crore)
2025-11-17  CCL         PYRAMID BUY ₹26,437.86 crore crore at ₹1,065.50 (box jump — doubling the stake with NEW capital; stop stays ₹976.41; charges ₹62.41 crore crore)
2025-11-17  CUB         PYRAMID BUY ₹27,081.17 crore crore at ₹204.00 (box jump — doubling the stake with NEW capital; stop stays ₹174.66; charges ₹63.93 crore crore)
2025-11-17  TDPOWERSYS  PYRAMID BUY ₹26,206.87 crore crore at ₹394.52 (box jump — doubling the stake with NEW capital; stop stays ₹357.49; charges ₹61.86 crore crore)
2025-11-20  ANANDRATHI  SELL ₹34,109.78 crore crore at stop ₹1,450.17 (-7.7%, charges ₹75.76 crore crore) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹48,290.15 crore crore at stop ₹976.41 (-6.1%, charges ₹107.26 crore crore) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹32,512.06 crore crore at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.37×, ladder rising; stop ₹2,956.50; charges ₹76.75 crore crore)
2025-11-24  TDPOWERSYS  SELL ₹47,332.35 crore crore at stop ₹357.49 (-8.0%, charges ₹105.13 crore crore) — the cash goes back to work at the next Friday screen
2025-12-01  CUB         PYRAMID BUY ₹54,177.98 crore crore at ₹204.30 (box jump — doubling the stake with NEW capital; stop stays ₹185.32; charges ₹127.89 crore crore)
2025-12-01  EUREKAFORB  BUY ₹40,133.37 crore crore at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.35×, ladder rising; stop ₹535.37; charges ₹94.74 crore crore)
2025-12-01  GMRAIRPORT  BUY ₹23,849.69 crore crore at ₹108.90 (fresh Friday signal — BUY: 1.69× weekly, month 1.84×, ladder rising; stop ₹89.73; charges ₹56.30 crore crore)
2025-12-01  SANSERA     BUY ₹40,056.36 crore crore at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.61×, ladder rising; stop ₹1,413.60; charges ₹94.56 crore crore)
2025-12-01  SHAILY      PYRAMID BUY ₹20,704.18 crore crore at ₹2,632.80 (box jump — doubling the stake with NEW capital; stop stays ₹2,340.80; charges ₹48.88 crore crore)
2025-12-08  AVANTIFEED  PYRAMID BUY ₹4,703.63 crore crore at ₹820.95 (box jump — doubling the stake with NEW capital; stop stays ₹748.60; charges ₹11.10 crore crore)
2025-12-15  EUREKAFORB  PYRAMID BUY ₹39,254.74 crore crore at ₹651.00 (box jump — doubling the stake with NEW capital; stop stays ₹589.10; charges ₹92.67 crore crore)
2025-12-15  LTF         PYRAMID BUY ₹25,553.73 crore crore at ₹307.05 (box jump — doubling the stake with NEW capital; stop stays ₹281.77; charges ₹60.32 crore crore)
2025-12-15  SANSERA     PYRAMID BUY ₹38,943.11 crore crore at ₹1,705.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,517.72; charges ₹91.93 crore crore)
2025-12-15  SHAILY      SELL ₹36,690.87 crore crore at stop ₹2,340.80 (-7.6%, charges ₹81.50 crore crore) — the cash goes back to work at the next Friday screen
2025-12-22  GMRAIRPORT  PYRAMID BUY ₹22,296.74 crore crore at ₹102.05 (box jump — doubling the stake with NEW capital; stop stays ₹92.10; charges ₹52.63 crore crore)
2025-12-22  KIRLOSENG   BUY ₹36,690.87 crore crore at ₹1,258.30 (fresh Friday signal — BUY: 4.09× weekly, month 1.72×, ladder rising; stop ₹1,014.88; charges ₹86.61 crore crore)
2026-01-05  KIRLOSENG   PYRAMID BUY ₹36,653.71 crore crore at ₹1,260.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,140.95; charges ₹86.53 crore crore)
2026-01-05  VIYASH      PYRAMID BUY ₹37,228.23 crore crore at ₹210.50 (box jump — doubling the stake with NEW capital; stop stays ₹195.04; charges ₹87.88 crore crore)
2026-01-08  EUREKAFORB  SELL ₹70,803.32 crore crore at stop ₹589.10 (-10.4%, charges ₹157.26 crore crore) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹29,088.12 crore crore at stop ₹2,956.50 (-10.1%, charges ₹64.61 crore crore) — the cash goes back to work at the next Friday screen
2026-01-12  KIRLOSENG   SELL ₹66,155.74 crore crore at stop ₹1,140.95 (-9.4%, charges ₹146.94 crore crore) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹56,844.53 crore crore at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.57×, ladder rising; stop ₹246.34; charges ₹134.19 crore crore)
2026-01-12  VIYASH      SELL ₹68,753.93 crore crore at stop ₹195.04 (-7.1%, charges ₹152.71 crore crore) — the cash goes back to work at the next Friday screen
2026-01-19  CUB         PYRAMID BUY ₹1.07 lakh crore crore at ₹202.24 (box jump — doubling the stake with NEW capital; stop stays ₹185.96; charges ₹252.91 crore crore)
2026-01-19  MAHABANK    PYRAMID BUY ₹28,607.01 crore crore at ₹66.82 (box jump — doubling the stake with NEW capital; stop stays ₹58.71; charges ₹67.53 crore crore)
2026-01-19  NATIONALUM  PYRAMID BUY ₹58,482.54 crore crore at ₹363.00 (box jump — doubling the stake with NEW capital; stop stays ₹312.41; charges ₹138.06 crore crore)
2026-01-19  SANSERA     PYRAMID BUY ₹84,227.72 crore crore at ₹1,846.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,672.76; charges ₹198.83 crore crore)
2026-01-21  AVANTIFEED  SELL ₹8,549.09 crore crore at stop ₹748.60 (-1.0%, charges ₹18.99 crore crore) — the cash goes back to work at the next Friday screen
2026-01-21  LTF         SELL ₹46,740.51 crore crore at stop ₹281.77 (-7.8%, charges ₹103.82 crore crore) — the cash goes back to work at the next Friday screen
2026-01-23  GMRAIRPORT  SELL ₹40,108.97 crore crore at stop ₹92.10 (-12.7%, charges ₹89.09 crore crore) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹1.52 lakh crore crore at stop ₹1,672.76 (-6.4%, charges ₹337.90 crore crore) — the cash goes back to work at the next Friday screen
2026-01-27  HINDZINC    BUY ₹84,809.07 crore crore at ₹733.00 (fresh Friday signal — BUY: 3.59× weekly, month 3.42×, ladder rising; stop ₹602.35; charges ₹200.20 crore crore)
2026-02-02  CIEINDIA    PYRAMID BUY ₹17,716.58 crore crore at ₹411.80 (box jump — doubling the stake with NEW capital; stop stays ₹382.33; charges ₹41.82 crore crore)
2026-02-02  HINDCOPPER  BUY ₹1.02 lakh crore crore at ₹590.15 (fresh Friday signal — BUY: 2.81× weekly, month 4.41×, ladder rising; stop ₹485.74; charges ₹239.93 crore crore)
2026-02-02  HINDZINC    SELL ₹69,374.08 crore crore at stop ₹602.35 (-17.8%, charges ₹154.09 crore crore) — the cash goes back to work at the next Friday screen
2026-02-02  MAHABANK    PYRAMID BUY ₹51,724.33 crore crore at ₹60.48 (box jump — doubling the stake with NEW capital; stop stays ₹59.76; charges ₹122.10 crore crore)
2026-02-02  NATIONALUM  PYRAMID BUY ₹1.12 lakh crore crore at ₹347.10 (box jump — doubling the stake with NEW capital; stop stays ₹335.49; charges ₹263.71 crore crore)
2026-02-16  HINDCOPPER  PYRAMID BUY ₹1.01 lakh crore crore at ₹585.00 (box jump — doubling the stake with NEW capital; stop stays ₹520.46; charges ₹237.28 crore crore)
2026-02-17  NATIONALUM  SELL ₹2.15 lakh crore crore at stop ₹335.49 (-4.8%, charges ₹478.02 crore crore) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹1.46 lakh crore crore at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.69×, ladder rising; stop ₹5,440.18; charges ₹344.31 crore crore)
2026-02-23  CUB         PYRAMID BUY ₹2.24 lakh crore crore at ₹211.28 (box jump — doubling the stake with NEW capital; stop stays ₹188.57; charges ₹527.80 crore crore)
2026-02-23  MAHABANK    PYRAMID BUY ₹1.18 lakh crore crore at ₹69.36 (box jump — doubling the stake with NEW capital; stop stays ₹61.05; charges ₹279.73 crore crore)
2026-03-02  ABB         PYRAMID BUY ₹1.40 lakh crore crore at ₹5,840.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,486.25; charges ₹329.40 crore crore)
2026-03-02  HINDCOPPER  PYRAMID BUY ₹1.93 lakh crore crore at ₹563.50 (box jump — doubling the stake with NEW capital; stop stays ₹528.63; charges ₹456.57 crore crore)
2026-03-02  KSB         BUY ₹1.78 lakh crore crore at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.80×, ladder rising; stop ₹658.54; charges ₹421.09 crore crore)
2026-03-02  TORNTPOWER  BUY ₹1.78 lakh crore crore at ₹1,491.00 (fresh Friday signal — BUY: 1.57× weekly, month 1.71×, ladder rising; stop ₹1,315.84; charges ₹421.15 crore crore)
2026-03-09  CUB         SELL ₹3.98 lakh crore crore at stop ₹188.57 (-8.6%, charges ₹883.47 crore crore) — the cash goes back to work at the next Friday screen
2026-03-09  KSB         PYRAMID BUY ₹1.78 lakh crore crore at ₹739.00 (box jump — doubling the stake with NEW capital; stop stays ₹681.58; charges ₹420.67 crore crore)
2026-03-12  HINDCOPPER  SELL ₹3.62 lakh crore crore at stop ₹528.63 (-8.2%, charges ₹803.28 crore crore) — the cash goes back to work at the next Friday screen
2026-03-23  ABB         PYRAMID BUY ₹2.99 lakh crore crore at ₹6,264.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,854.38; charges ₹705.79 crore crore)
2026-03-30  AETHER      BUY ₹2.52 lakh crore crore at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹594.20 crore crore)
2026-03-30  KSB         PYRAMID BUY ₹3.83 lakh crore crore at ₹795.85 (box jump — doubling the stake with NEW capital; stop stays ₹719.20; charges ₹904.99 crore crore)
2026-03-30  MAHABANK    SELL ₹2.08 lakh crore crore at stop ₹61.05 (-7.0%, charges ₹461.76 crore crore) — the cash goes back to work at the next Friday screen
2026-03-30  TORNTPOWER  SELL ₹1.57 lakh crore crore at stop ₹1,315.84 (-11.7%, charges ₹348.11 crore crore) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹2.00 lakh crore crore / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹2.61 lakh crore crore at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.66×, ladder rising; stop ₹891.29; charges ₹614.99 crore crore)
2026-04-06  CIEINDIA    PYRAMID BUY ₹39,447.84 crore crore at ₹459.00 (box jump — doubling the stake with NEW capital; stop stays ₹409.40; charges ₹93.12 crore crore)
2026-04-13  AETHER      PYRAMID BUY ₹2.55 lakh crore crore at ₹1,170.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,010.28; charges ₹602.85 crore crore)
2026-04-13  INOXINDIA   BUY ₹3.01 lakh crore crore at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹709.57 crore crore)
2026-04-13  THERMAX     BUY ₹3.03 lakh crore crore at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹715.54 crore crore)
2026-05-04  KSB         PYRAMID BUY ₹9.34 lakh crore crore at ₹971.00 (box jump — doubling the stake with NEW capital; stop stays ₹917.42; charges ₹2,205.71 crore crore)
2026-05-04  KSB         SELL ₹17.60 lakh crore crore at stop ₹917.42 (+5.6%, charges ₹3,908.40 crore crore) — the cash goes back to work at the next Friday screen
2026-05-11  AETHER      PYRAMID BUY ₹5.29 lakh crore crore at ₹1,213.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,125.84; charges ₹1,248.94 crore crore)
2026-05-11  CIEINDIA    PYRAMID BUY ₹81,995.86 crore crore at ₹477.60 (box jump — doubling the stake with NEW capital; stop stays ₹429.88; charges ₹193.56 crore crore)
2026-05-11  CRAFTSMAN   BUY ₹5.32 lakh crore crore at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹1,255.76 crore crore)
2026-05-11  INOXINDIA   PYRAMID BUY ₹3.44 lakh crore crore at ₹1,491.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,372.18; charges ₹812.85 crore crore)
2026-05-11  SPARC       BUY ₹5.31 lakh crore crore at ₹172.05 (fresh Friday signal — BUY: 5.97× weekly, month 2.00×, ladder rising; stop ₹129.88; charges ₹1,252.84 crore crore)
2026-05-11  THERMAX     PYRAMID BUY ₹3.96 lakh crore crore at ₹4,707.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,726.38; charges ₹934.39 crore crore)
2026-05-11  WOCKPHARMA  BUY ₹5.30 lakh crore crore at ₹1,613.90 (fresh Friday signal — BUY: 16.73× weekly, month 2.98×, ladder rising; stop ₹1,312.90; charges ₹1,252.23 crore crore)
2026-05-13  INOXINDIA   SELL ₹6.31 lakh crore crore at stop ₹1,372.18 (-1.7%, charges ₹1,402.30 crore crore) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹9.78 lakh crore crore at stop ₹1,125.84 (-5.1%, charges ₹2,173.28 crore crore) — the cash goes back to work at the next Friday screen
2026-05-18  ABB         PYRAMID BUY ₹6.02 lakh crore crore at ₹6,310.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,862.93; charges ₹1,420.27 crore crore)
2026-05-18  ALKYLAMINE  BUY ₹7.18 lakh crore crore at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.24×, ladder rising; stop ₹1,502.04; charges ₹1,695.69 crore crore)
2026-05-18  CAPLIPOINT  BUY ₹7.18 lakh crore crore at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹1,695.39 crore crore)
2026-05-18  CHENNPETRO  PYRAMID BUY ₹2.61 lakh crore crore at ₹995.00 (box jump — doubling the stake with NEW capital; stop stays ₹953.23; charges ₹617.26 crore crore)
2026-05-18  NLCINDIA    BUY ₹3.69 lakh crore crore at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 4.61×, ladder rising; stop ₹278.49; charges ₹870.72 crore crore)
2026-05-18  SPARC       PYRAMID BUY ₹5.00 lakh crore crore at ₹162.55 (box jump — doubling the stake with NEW capital; stop stays ₹153.91; charges ₹1,180.87 crore crore)
2026-05-18  THERMAX     PYRAMID BUY ₹7.49 lakh crore crore at ₹4,458.60 (box jump — doubling the stake with NEW capital; stop stays ₹4,181.80; charges ₹1,768.08 crore crore)
2026-05-25  CAPLIPOINT  PYRAMID BUY ₹7.41 lakh crore crore at ₹2,059.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,851.17; charges ₹1,750.38 crore crore)
2026-05-25  CRAFTSMAN   PYRAMID BUY ₹5.20 lakh crore crore at ₹8,850.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,793.85; charges ₹1,226.54 crore crore)
2026-05-25  NLCINDIA    PYRAMID BUY ₹3.64 lakh crore crore at ₹348.10 (box jump — doubling the stake with NEW capital; stop stays ₹320.62; charges ₹860.14 crore crore)
2026-05-25  WOCKPHARMA  PYRAMID BUY ₹5.22 lakh crore crore at ₹1,591.60 (box jump — doubling the stake with NEW capital; stop stays ₹1,423.10; charges ₹1,232.01 crore crore)
2026-06-08  ABB         PYRAMID BUY ₹13.53 lakh crore crore at ₹7,105.50 (box jump — doubling the stake with NEW capital; stop stays ₹6,609.15; charges ₹3,194.88 crore crore)
2026-06-08  SPARC       PYRAMID BUY ₹12.85 lakh crore crore at ₹209.00 (box jump — doubling the stake with NEW capital; stop stays ₹177.70; charges ₹3,033.04 crore crore)
2026-06-09  NLCINDIA    SELL ₹6.69 lakh crore crore at stop ₹320.62 (-8.3%, charges ₹1,485.79 crore crore) — the cash goes back to work at the next Friday screen
2026-06-11  CIEINDIA    SELL ₹1.47 lakh crore crore at stop ₹429.88 (-6.4%, charges ₹326.74 crore crore) — the cash goes back to work at the next Friday screen
2026-06-15  ALKYLAMINE  PYRAMID BUY ₹7.88 lakh crore crore at ₹1,880.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,614.05; charges ₹1,859.87 crore crore)
2026-06-15  CAPLIPOINT  PYRAMID BUY ₹17.51 lakh crore crore at ₹2,435.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,852.50; charges ₹4,134.35 crore crore)
2026-06-15  CHENNPETRO  PYRAMID BUY ₹6.08 lakh crore crore at ₹1,158.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,075.02; charges ₹1,435.06 crore crore)
2026-06-22  THERMAX     PYRAMID BUY ₹15.81 lakh crore crore at ₹4,712.10 (box jump — doubling the stake with NEW capital; stop stays ₹4,306.63; charges ₹3,732.80 crore crore)
2026-06-22  WOCKPHARMA  PYRAMID BUY ₹13.19 lakh crore crore at ₹2,014.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,639.31; charges ₹3,114.28 crore crore)
2026-06-29  CAPLIPOINT  PYRAMID BUY ₹36.01 lakh crore crore at ₹2,506.40 (box jump — doubling the stake with NEW capital; stop stays ₹2,209.13; charges ₹8,501.11 crore crore)
2026-07-06  CAPLIPOINT  PYRAMID BUY ₹73.33 lakh crore crore at ₹2,555.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,351.25; charges ₹17,311.43 crore crore)
2026-07-20  CAPLIPOINT  PYRAMID BUY ₹149.88 lakh crore crore at ₹2,614.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,376.52; charges ₹35,380.57 crore crore)
2026-07-27  CHENNPETRO  PYRAMID BUY ₹12.90 lakh crore crore at ₹1,230.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,130.59; charges ₹3,044.97 crore crore)
2026-07-27  CRAFTSMAN   PYRAMID BUY ₹10.92 lakh crore crore at ₹9,312.00 (box jump — doubling the stake with NEW capital; stop stays ₹8,593.23; charges ₹2,578.09 crore crore)
2026-07-29  THERMAX     SELL ₹28.81 lakh crore crore at stop ₹4,306.63 (-4.5%, charges ₹6,398.22 crore crore) — the cash goes back to work at the next Friday screen
2026-08-03  ALKYLAMINE  PYRAMID BUY ₹14.95 lakh crore crore at ₹1,785.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,676.66; charges ₹3,529.39 crore crore)
2026-08-03  TMB         BUY ₹36.97 lakh crore crore at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.57×, ladder rising; stop ₹748.60; charges ₹8,726.40 crore crore)
2026-08-03  WOCKPHARMA  PYRAMID BUY ₹25.74 lakh crore crore at ₹1,967.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,734.41; charges ₹6,076.04 crore crore)
2026-08-10  SPARC       PYRAMID BUY ₹26.19 lakh crore crore at ₹213.25 (box jump — doubling the stake with NEW capital; stop stays ₹179.80; charges ₹6,182.13 crore crore)
2026-08-10  TMB         PYRAMID BUY ₹37.52 lakh crore crore at ₹880.00 (box jump — doubling the stake with NEW capital; stop stays ₹796.29; charges ₹8,857.79 crore crore)
2026-08-17  ABB         PYRAMID BUY ₹29.12 lakh crore crore at ₹7,652.50 (box jump — doubling the stake with NEW capital; stop stays ₹7,158.25; charges ₹6,873.53 crore crore)
2026-08-17  CRAFTSMAN   PYRAMID BUY ₹24.02 lakh crore crore at ₹10,251.00 (box jump — doubling the stake with NEW capital; stop stays ₹9,690.00; charges ₹5,669.41 crore crore)
2026-08-24  CHENNPETRO  PYRAMID BUY ₹29.43 lakh crore crore at ₹1,405.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,242.60; charges ₹6,948.18 crore crore)
2026-08-24  SPARC       PYRAMID BUY ₹48.76 lakh crore crore at ₹198.75 (box jump — doubling the stake with NEW capital; stop stays ₹182.29; charges ₹11,509.95 crore crore)
2026-08-31  ALKYLAMINE  PYRAMID BUY ₹34.20 lakh crore crore at ₹2,045.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,920.99; charges ₹8,073.33 crore crore)
2026-08-31  CRAFTSMAN   PYRAMID BUY ₹52.03 lakh crore crore at ₹11,118.00 (box jump — doubling the stake with NEW capital; stop stays ₹9,832.50; charges ₹12,283.31 crore crore)
2026-09-07  WOCKPHARMA  PYRAMID BUY ₹55.22 lakh crore crore at ₹2,112.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,741.63; charges ₹13,035.56 crore crore)
2026-09-10  ALKYLAMINE  SELL ₹64.03 lakh crore crore at stop ₹1,920.99 (+0.2%, charges ₹14,222.82 crore crore) — the cash goes back to work at the next Friday screen
```
