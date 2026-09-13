# The Darvas screen — 2020-03-01 → 2026-09-11

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2019-03-01 → 2026-09-11, 750 symbols, in `2019-03-01_to_2026-09-13/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **The universe is POINT-IN-TIME:** the top symbols by actual traded value in the as-of month, from NSE's official bhavcopies (`constituents_asof.csv`) — companies that later died or delisted are IN, later IPOs are OUT, so survivorship bias is removed; the price of using raw exchange data is heuristic split/bonus adjustment (standard ratio against the prior close AND a matching volume step; every adjustment applied is listed in `_adjustments.csv`). No slippage, stop exits at the stop price, fractional shares. Stored fiscal statements exist for 57% of this universe — a stock without statements cannot be blocked by the earnings gate (only a FALLING verdict blocks), which loosens that gate for the rest.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), best volume reaction first, at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with NEW capital, 3× cap.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled with FRESH MONEY from outside the portfolio, equal to the position's market value, at the next day's open — but AT MOST THREE TIMES per position (8× the first slice), so the capital the rule demands stays realistic. The new money never touches the portfolio's cash — fresh entries are never starved — and every injection is dated and logged, so the honest yardstick is the money-weighted return (XIRR), not a naive multiple. Each add-on is its own tax lot on its own holding clock; the ratcheted stop covers the whole enlarged position; a jump past the cap is logged, never doubled.

## The headline — XIRR is the honest yardstick

| Engine | Money put in | Final value | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | ₹490.79 crore crore (₹100 + ₹490.79 crore crore injected) | **₹512.65 crore crore** | **+25.85%** |
| B: doubling, before charges and tax | ₹319.97 crore crore | ₹335.37 crore crore | +28.25% |
| **A: no doubling, NET of charges and tax** | ₹100.00 | **₹276.43** | **+16.89%** |
| A: no doubling, before charges and tax | ₹100.00 | ₹348.47 | +21.12% |
| Nifty 50 (pre-cost, pre-tax) | ₹100.00 | ₹212.91 | +12.30% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹0.39; unrealised gains in both end books carry further deferred liabilities.*

6.52 years, 341 weekly screens. Engine B injected new capital 367 times (gross run: 359); the complete dated injection list is in the blotter and the events CSV.

## What the frictions took (net runs)

| | Engine A: no doubling | Engine B: doubling |
|---|---:|---:|
| Transaction charges | ₹10.27 | ₹2.47 crore crore |
| Capital-gains tax paid | ₹35.52 | ₹517.73 crore |
| Tax accrued, final part-year | ₹0.39 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹13.93 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹2,854.12 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹13.35 lakh / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹45.71 crore / ₹0.00 |
| FY2024 | 2024-04-01 | ₹2,588.64 crore | ₹0.00 | ₹517.73 crore | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹2.07 lakh crore / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹2.68 crore crore / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹29.69 crore crore / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹13.93 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹33.24 | ₹0.00 | ₹6.65 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹50.10 | ₹0.00 | ₹10.02 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹7.57 | ₹0.00 | ₹1.51 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹46.87 | ₹0.00 | ₹9.37 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹34.37 | ₹0.08 | ₹6.88 | ₹0.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹8.64 | ₹1.08 | ₹0.00 / ₹0.00 |
| Final part-year (accrued) | — | ₹1.96 | ₹0.00 | ₹0.39 | ₹0.00 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2020 (2020-12-24) | ₹144.66 | +44.7% | ₹6,972.93 | ₹5,425.64 | +142.2% | +25.1% |
| 2021 (2021-12-31) | ₹196.33 | +35.7% | ₹36.52 lakh | ₹34.25 lakh | +36.3% | +26.2% |
| 2022 (2022-12-30) | ₹185.67 | -5.4% | ₹127.04 crore | ₹133.74 crore | -33.1% | +4.3% |
| 2023 (2023-12-29) | ₹244.79 | +31.8% | ₹26,888.48 crore | ₹21,879.98 crore | +114.6% | +20.0% |
| 2024 (2024-12-27) | ₹262.42 | +7.2% | ₹14.13 lakh crore | ₹13.88 lakh crore | -0.7% | +9.6% |
| 2025 (2025-12-26) | ₹268.05 | +2.1% | ₹8.10 crore crore | ₹7.95 crore crore | +0.4% | +9.4% |
| 2026 (2026-09-11) | ₹276.43 | +3.1% | ₹512.65 crore crore | ₹482.70 crore crore | +17.4% | -10.2% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-14.1%** (A: -20.5%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **201 closed trades**: 45 winners (22%), average winner +21.9%, average loser -9.1% (returns per blended entry price).
- Best closed trade LTTS +118.7%; worst DEEPAKNTR -30.0%.
- Median holding period 58 days.
- Cash share of equity averaged 13%; fully in cash 5 of 341 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

| Month-end screen | B equity | B injected so far | B cash | B positions | A equity |
|---|---:|---:|---:|---:|---:|
| 2020-03-27 | ₹85.91 | ₹0.00 | ₹85.91 | 0 | ₹85.91 |
| 2020-04-30 | ₹86.99 | ₹0.00 | ₹34.24 | 6 | ₹86.99 |
| 2020-05-29 | ₹129.82 | ₹39.70 | ₹3.20 | 9 | ₹90.80 |
| 2020-06-26 | ₹214.68 | ₹120.88 | ₹3.99 | 9 | ₹96.03 |
| 2020-07-31 | ₹423.70 | ₹316.68 | ₹0.00 | 9 | ₹102.13 |
| 2020-08-28 | ₹633.11 | ₹532.24 | ₹8.08 | 10 | ₹105.24 |
| 2020-09-25 | ₹1,151.49 | ₹957.86 | ₹35.17 | 9 | ₹117.34 |
| 2020-10-30 | ₹2,329.47 | ₹1,947.64 | ₹261.73 | 9 | ₹125.67 |
| 2020-11-27 | ₹3,254.80 | ₹2,865.46 | ₹0.00 | 12 | ₹129.34 |
| 2020-12-24 | ₹6,972.93 | ₹5,425.64 | ₹416.58 | 10 | ₹144.66 |
| 2021-01-29 | ₹14,024.75 | ₹13,128.66 | ₹3,997.89 | 9 | ₹134.67 |
| 2021-02-26 | ₹39,455.77 | ₹38,249.19 | ₹7,847.26 | 9 | ₹140.15 |
| 2021-03-26 | ₹57,697.99 | ₹59,808.95 | ₹16,349.05 | 10 | ₹134.77 |
| 2021-04-30 | ₹1.20 lakh | ₹1.10 lakh | ₹1,597.66 | 11 | ₹142.59 |
| 2021-05-28 | ₹1.84 lakh | ₹1.57 lakh | ₹1,597.66 | 11 | ₹157.87 |
| 2021-06-25 | ₹4.28 lakh | ₹3.44 lakh | ₹1,597.66 | 11 | ₹174.38 |
| 2021-07-30 | ₹6.34 lakh | ₹4.76 lakh | ₹1,597.66 | 11 | ₹189.57 |
| 2021-08-27 | ₹6.87 lakh | ₹5.23 lakh | ₹0.00 | 11 | ₹188.33 |
| 2021-09-24 | ₹8.70 lakh | ₹6.82 lakh | ₹19,061.30 | 10 | ₹190.35 |
| 2021-10-29 | ₹12.07 lakh | ₹10.00 lakh | ₹2.26 lakh | 9 | ₹180.44 |
| 2021-11-26 | ₹20.35 lakh | ₹17.98 lakh | ₹11.18 lakh | 7 | ₹193.77 |
| 2021-12-31 | ₹36.52 lakh | ₹34.30 lakh | ₹82,668.88 | 12 | ₹196.33 |
| 2022-01-28 | ₹53.15 lakh | ₹53.44 lakh | ₹17.66 lakh | 9 | ₹191.88 |
| 2022-02-25 | ₹95.90 lakh | ₹1.07 crore | ₹57.67 lakh | 7 | ₹177.58 |
| 2022-03-25 | ₹1.28 crore | ₹1.32 crore | ₹31.03 lakh | 9 | ₹184.20 |
| 2022-04-29 | ₹2.04 crore | ₹2.11 crore | ₹41.74 lakh | 9 | ₹172.86 |
| 2022-05-27 | ₹3.06 crore | ₹3.38 crore | ₹45.52 lakh | 11 | ₹161.87 |
| 2022-06-24 | ₹4.34 crore | ₹4.56 crore | ₹64.92 lakh | 9 | ₹164.54 |
| 2022-07-29 | ₹8.54 crore | ₹8.40 crore | ₹7.35 lakh | 10 | ₹169.63 |
| 2022-08-26 | ₹16.79 crore | ₹15.93 crore | ₹37.81 lakh | 11 | ₹177.79 |
| 2022-09-30 | ₹32.57 crore | ₹31.50 crore | ₹14.59 crore | 9 | ₹180.30 |
| 2022-10-28 | ₹35.43 crore | ₹34.83 crore | ₹1.22 crore | 13 | ₹178.98 |
| 2022-11-25 | ₹82.24 crore | ₹75.22 crore | ₹49.40 lakh | 13 | ₹196.31 |
| 2022-12-30 | ₹127.04 crore | ₹134.08 crore | ₹87.39 crore | 8 | ₹185.67 |
| 2023-01-27 | ₹157.70 crore | ₹174.62 crore | ₹9.27 crore | 14 | ₹178.34 |
| 2023-02-24 | ₹243.08 crore | ₹252.78 crore | ₹13.82 crore | 11 | ₹179.42 |
| 2023-03-31 | ₹471.89 crore | ₹512.99 crore | ₹333.31 crore | 7 | ₹175.30 |
| 2023-04-28 | ₹631.37 crore | ₹673.97 crore | ₹58.26 crore | 13 | ₹180.08 |
| 2023-05-26 | ₹998.78 crore | ₹1,052.51 crore | ₹273.38 crore | 12 | ₹180.33 |
| 2023-06-30 | ₹2,381.49 crore | ₹2,343.46 crore | ₹56.53 crore | 14 | ₹194.08 |
| 2023-07-28 | ₹4,451.33 crore | ₹4,285.65 crore | ₹0.00 | 13 | ₹197.27 |
| 2023-08-25 | ₹6,729.77 crore | ₹6,109.56 crore | ₹0.00 | 13 | ₹209.99 |
| 2023-09-29 | ₹8,508.77 crore | ₹7,799.70 crore | ₹0.00 | 13 | ₹210.66 |
| 2023-10-27 | ₹8,119.14 crore | ₹7,799.70 crore | ₹2,247.61 crore | 9 | ₹201.16 |
| 2023-11-24 | ₹11,732.82 crore | ₹9,847.02 crore | ₹0.00 | 12 | ₹217.99 |
| 2023-12-29 | ₹26,888.48 crore | ₹22,014.06 crore | ₹0.00 | 12 | ₹244.79 |
| 2024-01-25 | ₹36,080.68 crore | ₹28,051.14 crore | ₹0.00 | 12 | ₹266.03 |
| 2024-02-23 | ₹42,063.14 crore | ₹31,327.47 crore | ₹0.00 | 12 | ₹277.55 |
| 2024-03-28 | ₹42,076.41 crore | ₹35,042.62 crore | ₹1,624.84 crore | 12 | ₹266.08 |
| 2024-04-26 | ₹66,450.49 crore | ₹56,628.45 crore | ₹0.00 | 13 | ₹277.89 |
| 2024-05-31 | ₹1.15 lakh crore | ₹1.07 lakh crore | ₹20,823.80 crore | 12 | ₹277.62 |
| 2024-06-28 | ₹1.87 lakh crore | ₹1.84 lakh crore | ₹0.00 | 14 | ₹272.29 |
| 2024-07-26 | ₹2.61 lakh crore | ₹2.53 lakh crore | ₹22,862.97 crore | 13 | ₹274.20 |
| 2024-08-30 | ₹3.44 lakh crore | ₹3.35 lakh crore | ₹0.00 | 14 | ₹275.70 |
| 2024-09-27 | ₹5.52 lakh crore | ₹5.28 lakh crore | ₹0.00 | 14 | ₹276.45 |
| 2024-10-25 | ₹5.94 lakh crore | ₹6.21 lakh crore | ₹2.32 lakh crore | 11 | ₹259.37 |
| 2024-11-29 | ₹7.91 lakh crore | ₹8.11 lakh crore | ₹1.78 lakh crore | 12 | ₹255.47 |
| 2024-12-27 | ₹14.13 lakh crore | ₹14.10 lakh crore | ₹1.02 lakh crore | 13 | ₹262.42 |
| 2025-01-31 | ₹17.53 lakh crore | ₹18.62 lakh crore | ₹12.00 lakh crore | 7 | ₹256.04 |
| 2025-02-28 | ₹18.17 lakh crore | ₹20.28 lakh crore | ₹11.29 lakh crore | 8 | ₹243.94 |
| 2025-03-27 | ₹23.39 lakh crore | ₹24.58 lakh crore | ₹8.51 lakh crore | 9 | ₹252.87 |
| 2025-04-25 | ₹27.75 lakh crore | ₹27.34 lakh crore | ₹6.18 lakh crore | 10 | ₹257.91 |
| 2025-05-30 | ₹51.55 lakh crore | ₹52.76 lakh crore | ₹10.70 lakh crore | 11 | ₹250.51 |
| 2025-06-27 | ₹1.30 crore crore | ₹1.21 crore crore | ₹0.00 | 13 | ₹264.61 |
| 2025-07-25 | ₹2.10 crore crore | ₹1.87 crore crore | ₹0.00 | 13 | ₹267.56 |
| 2025-08-29 | ₹2.14 crore crore | ₹2.07 crore crore | ₹22.04 lakh crore | 14 | ₹254.11 |
| 2025-09-26 | ₹2.94 crore crore | ₹2.86 crore crore | ₹19.47 lakh crore | 13 | ₹265.26 |
| 2025-10-31 | ₹4.36 crore crore | ₹4.49 crore crore | ₹21.56 lakh crore | 13 | ₹265.01 |
| 2025-11-28 | ₹6.22 crore crore | ₹6.34 crore crore | ₹98.79 lakh crore | 13 | ₹263.48 |
| 2025-12-26 | ₹8.10 crore crore | ₹8.09 crore crore | ₹0.00 | 14 | ₹268.05 |
| 2026-01-30 | ₹13.44 crore crore | ₹12.95 crore crore | ₹1.40 crore crore | 12 | ₹265.63 |
| 2026-02-27 | ₹22.43 crore crore | ₹22.90 crore crore | ₹0.00 | 12 | ₹251.95 |
| 2026-03-27 | ₹36.03 crore crore | ₹38.84 crore crore | ₹10.94 crore crore | 10 | ₹244.38 |
| 2026-04-30 | ₹59.01 crore crore | ₹57.62 crore crore | ₹0.00 | 13 | ₹267.53 |
| 2026-05-29 | ₹120.96 crore crore | ₹116.22 crore crore | ₹0.00 | 13 | ₹274.58 |
| 2026-06-25 | ₹194.43 crore crore | ₹199.40 crore crore | ₹0.00 | 13 | ₹269.19 |
| 2026-07-31 | ₹256.28 crore crore | ₹273.03 crore crore | ₹9.43 crore crore | 15 | ₹262.25 |
| 2026-08-28 | ₹408.35 crore crore | ₹385.01 crore crore | ₹9.43 crore crore | 15 | ₹277.68 |
| 2026-09-11 | ₹512.65 crore crore | ₹490.79 crore crore | ₹27.33 crore crore | 14 | ₹276.43 |

## Engine B — still held at the end

| Stock | First entry | Blended entry ₹ | Lots | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|---:|
| ABB | 2026-02-23 | 6,212.08 | 4 | 7,274.00 | 7,158.25 | +17.1% |
| APOLLOPIPE | 2026-03-16 | 490.37 | 4 | 554.90 | 440.44 | +13.2% |
| AVADHSUGAR | 2026-03-23 | 541.58 | 4 | 769.60 | 749.03 | +42.1% |
| BODALCHEM | 2026-09-07 | 168.00 | 1 | 172.40 | 63.20 | +2.6% |
| CHENNPETRO | 2026-04-06 | 1,152.36 | 4 | 1,572.90 | 1,242.60 | +36.5% |
| EBBETF0423 | 2023-02-06 | 1,216.48 | 1 | 1,230.39 | 1,124.88 | +1.1% |
| GOLDSHARE | 2025-10-20 | 105.45 | 2 | 114.90 | 91.06 | +9.0% |
| HDFCMFGETF | 2022-03-07 | 47.27 | 4 | 51.67 | 49.92 | +9.3% |
| JBCHEPHARM | 2026-03-16 | 2,169.48 | 3 | 2,408.90 | 1,976.86 | +11.0% |
| ORIENTREF | 2021-04-26 | 324.61 | 4 | 322.40 | 301.44 | -0.7% |
| RITES | 2026-07-13 | 222.72 | 2 | 209.15 | 204.83 | -6.1% |
| SHALPAINTS | 2026-07-27 | 69.89 | 2 | 86.19 | 57.85 | +23.3% |
| SUBEX | 2020-10-19 | 15.55 | 1 | 16.95 | 11.11 | +9.0% |
| TASTYBITE | 2026-07-06 | 9,674.35 | 4 | 10,273.00 | 9,267.25 | +6.2% |

## Engine B — every closed trade

*Returns are on the blended entry price across lots.*

| Stock | First entry | Blended ₹ | Lots | Exit | Exit ₹ | Return |
|---|---|---:|---:|---|---:|---:|
| HDFCMFGETF | 2020-03-09 | 4,002.50 | 1 | 2020-03-13 | 3,540.65 | -11.5% |
| INDOCO | 2020-03-09 | 228.20 | 1 | 2020-03-13 | 164.08 | -28.1% |
| LALPATHLAB | 2020-03-09 | 835.00 | 1 | 2020-03-13 | 743.38 | -11.0% |
| SETFGOLD | 2020-03-09 | 3,862.80 | 1 | 2020-03-17 | 3,548.39 | -8.1% |
| GOLDSHARE | 2020-03-09 | 3,937.00 | 1 | 2020-03-17 | 3,562.50 | -9.5% |
| AXISGOLD | 2020-03-09 | 4,037.70 | 1 | 2020-03-17 | 3,450.88 | -14.5% |
| DEEPAKNTR | 2020-03-09 | 508.80 | 1 | 2020-03-19 | 356.25 | -30.0% |
| IOLCP | 2020-03-09 | 51.20 | 1 | 2020-03-19 | 36.91 | -27.9% |
| DEEPAKNTR | 2020-04-13 | 498.24 | 2 | 2020-06-12 | 474.05 | -4.9% |
| IOLCP | 2020-05-11 | 73.59 | 2 | 2020-06-16 | 69.35 | -5.8% |
| AXISGOLD | 2020-04-13 | 4,227.60 | 3 | 2020-07-23 | 3,971.05 | -6.1% |
| EIDPARRY | 2020-05-11 | 267.40 | 4 | 2020-08-17 | 273.03 | +2.1% |
| APLLTD | 2020-05-11 | 920.90 | 4 | 2020-09-01 | 928.62 | +0.8% |
| GOLDBEES | 2020-04-13 | 43.84 | 2 | 2020-09-04 | 41.00 | -6.5% |
| CADILAHC | 2020-04-27 | 377.33 | 4 | 2020-09-08 | 364.99 | -3.3% |
| HDFCMFGETF | 2020-04-20 | 4,685.38 | 3 | 2020-09-23 | 4,492.07 | -4.1% |
| AARTIDRUGS | 2020-08-24 | 3,064.61 | 2 | 2020-09-30 | 2,264.30 | -26.1% |
| PRINCEPIPE | 2020-09-07 | 225.49 | 3 | 2020-10-12 | 220.88 | -2.0% |
| INDIAMART | 2020-09-07 | 2,421.33 | 3 | 2020-10-19 | 2,315.62 | -4.4% |
| CIGNITITEC | 2020-10-05 | 453.73 | 2 | 2020-10-27 | 441.27 | -2.7% |
| ALEMBICLTD | 2020-06-22 | 95.52 | 4 | 2020-11-02 | 91.41 | -4.3% |
| SHREDIGCEM | 2020-11-02 | 64.67 | 2 | 2020-11-10 | 56.43 | -12.7% |
| THYROCARE | 2020-08-24 | 1,020.49 | 4 | 2020-11-12 | 1,016.50 | -0.4% |
| SYNGENE | 2020-04-27 | 442.96 | 4 | 2020-12-22 | 562.40 | +27.0% |
| TCI | 2020-09-14 | 248.49 | 3 | 2020-12-22 | 234.75 | -5.5% |
| PILANIINVS | 2020-11-17 | 2,088.34 | 3 | 2021-01-04 | 2,132.80 | +2.1% |
| BORORENEW | 2020-11-09 | 179.04 | 4 | 2021-01-20 | 247.59 | +38.3% |
| JSLHISAR | 2020-11-17 | 147.20 | 4 | 2021-01-22 | 142.59 | -3.1% |
| TATASTLBSL | 2020-11-17 | 39.71 | 3 | 2021-01-22 | 40.61 | +2.3% |
| JUSTDIAL | 2020-10-26 | 637.80 | 3 | 2021-01-25 | 622.35 | -2.4% |
| FILATEX | 2021-01-11 | 32.93 | 2 | 2021-01-25 | 30.16 | -8.4% |
| ICIL | 2020-07-27 | 87.30 | 4 | 2021-01-27 | 132.29 | +51.5% |
| TRENT | 2020-11-17 | 483.35 | 2 | 2021-01-29 | 417.53 | -13.6% |
| TATAELXSI | 2021-01-25 | 2,755.37 | 3 | 2021-02-22 | 2,660.00 | -3.5% |
| GAEL | 2021-02-01 | 71.47 | 1 | 2021-02-23 | 62.70 | -12.3% |
| INDIAMART | 2021-01-25 | 4,296.73 | 3 | 2021-03-02 | 4,137.25 | -3.7% |
| RCF | 2021-03-01 | 82.90 | 2 | 2021-03-17 | 79.16 | -4.5% |
| TATAMOTORS | 2021-01-25 | 318.85 | 3 | 2021-03-19 | 296.97 | -6.9% |
| HINDZINC | 2021-01-25 | 288.74 | 2 | 2021-03-19 | 279.30 | -3.3% |
| APTECHT | 2021-02-01 | 219.72 | 4 | 2021-03-19 | 204.25 | -7.0% |
| MATRIMONY | 2021-03-01 | 1,097.77 | 2 | 2021-03-24 | 943.21 | -14.1% |
| JTEKTINDIA | 2020-06-15 | 83.86 | 4 | 2021-03-31 | 83.60 | -0.3% |
| AUBANK | 2021-04-05 | 631.00 | 1 | 2021-04-12 | 533.06 | -15.5% |
| PRAKASH | 2021-03-22 | 72.57 | 2 | 2021-04-19 | 74.58 | +2.8% |
| WELSPUNIND | 2021-03-22 | 106.37 | 4 | 2021-08-10 | 124.64 | +17.2% |
| MOREPENLAB | 2021-04-19 | 54.89 | 3 | 2021-08-10 | 56.33 | +2.6% |
| GDL | 2021-01-25 | 209.76 | 4 | 2021-09-20 | 266.00 | +26.8% |
| KEI | 2021-03-22 | 574.37 | 4 | 2021-10-22 | 853.10 | +48.5% |
| BASF | 2021-08-16 | 3,460.21 | 3 | 2021-10-25 | 3,220.59 | -6.9% |
| DEEPAKFERT | 2021-03-22 | 281.00 | 4 | 2021-11-18 | 368.55 | +31.2% |
| SHOPERSTOP | 2021-10-25 | 363.06 | 3 | 2021-11-22 | 335.82 | -7.5% |
| TATAINVEST | 2021-08-16 | 1,294.09 | 4 | 2021-11-26 | 1,436.49 | +11.0% |
| TTKPRESTIG | 2021-11-01 | 11,245.38 | 2 | 2021-11-26 | 10,070.05 | -10.5% |
| MAHLOG | 2021-01-25 | 531.95 | 4 | 2021-11-30 | 654.55 | +23.0% |
| KPITTECH | 2021-03-30 | 240.69 | 4 | 2021-12-20 | 458.85 | +90.6% |
| TCIEXP | 2021-11-01 | 2,118.52 | 4 | 2021-12-21 | 2,039.74 | -3.7% |
| MINDAIND | 2021-12-27 | 1,204.91 | 2 | 2022-01-07 | 1,088.41 | -9.7% |
| LTTS | 2020-10-19 | 2,220.53 | 4 | 2022-01-21 | 4,856.88 | +118.7% |
| TVTODAY | 2021-11-29 | 335.62 | 2 | 2022-01-24 | 311.68 | -7.1% |
| EVERESTIND | 2022-01-10 | 596.08 | 2 | 2022-01-24 | 536.75 | -10.0% |
| SWANENERGY | 2021-12-27 | 162.44 | 2 | 2022-01-25 | 162.64 | +0.1% |
| DIAMONDYD | 2021-12-27 | 850.03 | 2 | 2022-01-31 | 817.00 | -3.9% |
| SHARDACROP | 2022-01-31 | 623.38 | 2 | 2022-02-11 | 545.30 | -12.5% |
| BSOFT | 2021-11-29 | 475.09 | 2 | 2022-02-14 | 424.65 | -10.6% |
| RAYMOND | 2021-11-29 | 703.20 | 3 | 2022-02-15 | 679.35 | -3.4% |
| ANDHRSUGAR | 2022-01-31 | 160.92 | 2 | 2022-02-21 | 135.28 | -15.9% |
| ZEELEARN | 2022-01-10 | 16.70 | 2 | 2022-02-22 | 13.28 | -20.5% |
| TV18BRDCST | 2022-01-31 | 63.72 | 3 | 2022-02-22 | 58.38 | -8.4% |
| CCL | 2022-02-07 | 484.29 | 2 | 2022-02-24 | 441.75 | -8.8% |
| ESCORTS | 2021-11-29 | 1,870.85 | 3 | 2022-02-25 | 1,754.65 | -6.2% |
| BSE | 2021-12-06 | 1,869.99 | 2 | 2022-03-21 | 1,634.39 | -12.6% |
| EXCELINDUS | 2022-03-07 | 1,603.38 | 2 | 2022-03-29 | 1,438.30 | -10.3% |
| KOTAKGOLD | 2022-03-14 | 44.41 | 2 | 2022-04-27 | 41.14 | -7.4% |
| EVERESTIND | 2022-02-21 | 705.00 | 3 | 2022-04-28 | 594.70 | -15.6% |
| RCF | 2022-04-04 | 100.30 | 2 | 2022-05-04 | 93.15 | -7.1% |
| GNFC | 2022-02-14 | 698.36 | 3 | 2022-05-06 | 792.16 | +13.4% |
| INOXLEISUR | 2022-04-04 | 520.85 | 1 | 2022-05-06 | 470.35 | -9.7% |
| TNPL | 2022-04-11 | 205.45 | 3 | 2022-05-10 | 195.61 | -4.8% |
| RIIL | 2022-05-02 | 1,070.02 | 2 | 2022-05-26 | 863.73 | -19.3% |
| GEPIL | 2022-05-09 | 182.65 | 1 | 2022-05-31 | 163.45 | -10.5% |
| VBL | 2022-05-02 | 214.20 | 2 | 2022-06-06 | 196.27 | -8.4% |
| JSWENERGY | 2021-03-08 | 112.90 | 4 | 2022-06-20 | 201.99 | +78.9% |
| MRPL | 2022-05-09 | 87.37 | 3 | 2022-07-06 | 69.61 | -20.3% |
| JKIL | 2022-05-09 | 298.61 | 4 | 2022-08-05 | 308.80 | +3.4% |
| NAVNETEDUL | 2022-08-08 | 134.26 | 4 | 2022-09-26 | 127.30 | -5.2% |
| TVSSRICHAK | 2022-08-08 | 2,347.94 | 3 | 2022-09-26 | 2,432.24 | +3.6% |
| VADILALIND | 2022-05-23 | 2,029.48 | 4 | 2022-10-20 | 2,295.06 | +13.1% |
| LUMAXIND | 2022-07-18 | 1,548.51 | 3 | 2022-11-01 | 1,492.45 | -3.6% |
| APARINDS | 2022-06-20 | 1,157.19 | 4 | 2022-11-03 | 1,358.50 | +17.4% |
| SCHNEIDER | 2022-10-03 | 186.52 | 2 | 2022-11-10 | 159.60 | -14.4% |
| ALLCARGO | 2022-10-03 | 439.83 | 2 | 2022-11-29 | 432.77 | -1.6% |
| MSTCLTD | 2022-12-05 | 327.36 | 2 | 2022-12-22 | 290.44 | -11.3% |
| ACC | 2022-05-23 | 2,241.61 | 4 | 2022-12-23 | 2,465.16 | +10.0% |
| KTKBANK | 2022-11-07 | 146.35 | 3 | 2022-12-23 | 139.84 | -4.4% |
| GODFRYPHLP | 2022-10-24 | 1,737.64 | 3 | 2022-12-26 | 1,643.55 | -5.4% |
| RVNL | 2022-11-07 | 66.08 | 4 | 2022-12-26 | 60.57 | -8.3% |
| TIINDIA | 2022-07-25 | 2,572.68 | 4 | 2023-01-11 | 2,598.34 | +1.0% |
| WESTLIFE | 2022-10-03 | 750.44 | 3 | 2023-01-16 | 708.51 | -5.6% |
| PIIND | 2022-11-14 | 3,421.96 | 2 | 2023-01-23 | 3,123.65 | -8.7% |
| BAJAJHIND | 2023-01-02 | 17.20 | 1 | 2023-01-30 | 13.98 | -18.7% |
| GICRE | 2023-01-02 | 183.12 | 2 | 2023-02-01 | 167.72 | -8.4% |
| LIBERTSHOE | 2022-10-03 | 304.01 | 2 | 2023-02-06 | 240.31 | -21.0% |
| ORIENTPPR | 2023-02-06 | 45.70 | 1 | 2023-02-13 | 39.90 | -12.7% |
| CGCL | 2022-02-21 | 711.32 | 3 | 2023-02-17 | 704.95 | -0.9% |
| USHAMART | 2023-01-23 | 203.00 | 1 | 2023-02-22 | 166.25 | -18.1% |
| ANUP | 2023-01-16 | 553.52 | 4 | 2023-03-10 | 527.27 | -4.7% |
| YESBANK | 2023-01-02 | 18.95 | 2 | 2023-03-13 | 15.34 | -19.1% |
| IOB | 2023-01-02 | 29.25 | 2 | 2023-03-20 | 22.18 | -24.2% |
| JINDALSAW | 2023-01-02 | 64.60 | 3 | 2023-03-27 | 67.92 | +5.1% |
| CIGNITITEC | 2023-02-20 | 761.00 | 3 | 2023-03-29 | 705.14 | -7.3% |
| SONATSOFTW | 2023-02-27 | 401.31 | 4 | 2023-03-29 | 371.45 | -7.4% |
| JSL | 2023-01-02 | 270.35 | 4 | 2023-04-13 | 256.98 | -4.9% |
| JISLJALEQS | 2023-04-10 | 38.11 | 3 | 2023-05-22 | 37.15 | -2.5% |
| MARKSANS | 2023-04-24 | 78.00 | 1 | 2023-05-22 | 71.87 | -7.9% |
| GSFC | 2023-01-02 | 159.39 | 3 | 2023-05-29 | 155.85 | -2.2% |
| KSB | 2023-03-27 | 435.68 | 2 | 2023-07-12 | 407.74 | -6.4% |
| THANGAMAYL | 2023-05-29 | 1,391.82 | 2 | 2023-07-17 | 1,344.25 | -3.4% |
| CPSEETF | 2023-04-03 | 43.74 | 4 | 2023-07-31 | 41.97 | -4.0% |
| SETFGOLD | 2023-04-03 | 52.85 | 2 | 2023-10-03 | 49.74 | -5.9% |
| BALMLAWRIE | 2023-05-29 | 135.37 | 4 | 2023-10-09 | 142.24 | +5.1% |
| FDC | 2023-04-24 | 321.81 | 4 | 2023-10-23 | 354.97 | +10.3% |
| SCHNEIDER | 2023-05-29 | 272.45 | 4 | 2023-10-23 | 315.45 | +15.8% |
| HAL | 2023-04-03 | 1,731.74 | 4 | 2023-10-25 | 1,840.70 | +6.3% |
| SEQUENT | 2023-10-16 | 121.75 | 4 | 2024-03-06 | 120.65 | -0.9% |
| GEOJITFSL | 2023-11-06 | 72.98 | 4 | 2024-03-11 | 68.81 | -5.7% |
| UFO | 2023-08-07 | 122.87 | 4 | 2024-03-12 | 125.82 | +2.4% |
| ASHIANA | 2023-04-24 | 192.91 | 4 | 2024-03-13 | 271.51 | +40.7% |
| TFCILTD | 2023-07-24 | 19.16 | 4 | 2024-03-20 | 33.40 | +74.3% |
| SADBHAV | 2024-03-26 | 29.42 | 2 | 2024-04-18 | 30.68 | +4.3% |
| JUSTDIAL | 2024-04-22 | 1,094.49 | 2 | 2024-05-09 | 1,008.00 | -7.9% |
| FORCEMOT | 2024-03-18 | 8,659.96 | 3 | 2024-05-28 | 8,083.64 | -6.7% |
| MANGLMCEM | 2023-10-30 | 613.07 | 4 | 2024-06-04 | 796.10 | +29.9% |
| SOLARINDS | 2024-03-11 | 8,256.59 | 2 | 2024-06-04 | 7,980.95 | -3.3% |
| BOSCHLTD | 2024-03-18 | 30,663.27 | 4 | 2024-06-04 | 29,015.09 | -5.4% |
| CENTURYTEX | 2024-05-13 | 2,000.00 | 1 | 2024-06-04 | 1,715.70 | -14.2% |
| ICICIBANK | 2023-05-02 | 959.96 | 4 | 2024-06-05 | 1,051.37 | +9.5% |
| MATRIMONY | 2024-06-10 | 634.28 | 2 | 2024-07-23 | 564.77 | -11.0% |
| THERMAX | 2024-06-03 | 5,528.77 | 2 | 2024-08-05 | 4,719.70 | -14.6% |
| DABUR | 2024-06-10 | 635.27 | 4 | 2024-10-03 | 602.49 | -5.2% |
| INDIGO | 2024-03-18 | 4,058.99 | 4 | 2024-10-07 | 4,485.14 | +10.5% |
| THYROCARE | 2024-07-29 | 818.84 | 3 | 2024-10-07 | 796.15 | -2.8% |
| BASF | 2024-08-12 | 7,616.24 | 3 | 2024-10-22 | 7,611.30 | -0.1% |
| JCHAC | 2024-06-03 | 2,248.83 | 4 | 2024-10-23 | 2,362.13 | +5.0% |
| DBCORP | 2024-10-14 | 352.00 | 1 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 148.70 | 2 | 2024-10-28 | 158.66 | +6.7% |
| UTINIFTETF | 2024-06-10 | 271.25 | 4 | 2024-11-13 | 256.51 | -5.4% |
| GOLDSHARE | 2024-04-22 | 64.66 | 3 | 2024-11-14 | 62.46 | -3.4% |
| NIFTYBEES | 2024-06-10 | 274.63 | 4 | 2024-11-14 | 262.66 | -4.4% |
| ASTRAZEN | 2024-10-07 | 7,396.38 | 2 | 2024-11-14 | 6,854.77 | -7.3% |
| AKZOINDIA | 2024-11-04 | 4,118.82 | 2 | 2024-12-27 | 3,423.18 | -16.9% |
| BANKBEES | 2024-06-10 | 526.98 | 2 | 2025-01-08 | 507.06 | -3.8% |
| GARFIBRES | 2024-11-25 | 946.01 | 2 | 2025-01-09 | 829.35 | -12.3% |
| SWANENERGY | 2024-12-02 | 710.93 | 3 | 2025-01-09 | 671.32 | -5.6% |
| GANECOS | 2024-12-02 | 2,418.80 | 1 | 2025-01-10 | 1,751.78 | -27.6% |
| CARERATING | 2024-10-28 | 1,457.48 | 2 | 2025-01-13 | 1,239.70 | -14.9% |
| CAMLINFINE | 2025-01-06 | 131.08 | 2 | 2025-01-13 | 120.37 | -8.2% |
| SASKEN | 2024-11-18 | 2,126.99 | 2 | 2025-01-21 | 1,993.24 | -6.3% |
| 63MOONS | 2024-11-04 | 799.46 | 3 | 2025-01-22 | 790.40 | -1.1% |
| BSE | 2024-10-14 | 4,919.52 | 3 | 2025-02-28 | 4,954.63 | +0.7% |
| ZENSARTECH | 2025-02-03 | 947.00 | 1 | 2025-03-03 | 727.84 | -23.1% |
| SETFGOLD | 2025-02-17 | 75.90 | 2 | 2025-04-07 | 69.36 | -8.6% |
| AVANTIFEED | 2025-03-17 | 842.55 | 1 | 2025-04-07 | 648.95 | -23.0% |
| VADILALIND | 2025-04-07 | 6,081.19 | 3 | 2025-05-30 | 5,401.40 | -11.2% |
| NH | 2025-03-03 | 1,940.68 | 4 | 2025-08-04 | 1,814.78 | -6.5% |
| WHIRLPOOL | 2025-04-28 | 1,329.25 | 4 | 2025-08-07 | 1,301.97 | -2.1% |
| LUMAXIND | 2025-06-02 | 3,332.86 | 4 | 2025-08-08 | 3,319.20 | -0.4% |
| RAIN | 2025-08-11 | 160.25 | 1 | 2025-08-26 | 143.64 | -10.4% |
| RPOWER | 2025-06-02 | 58.64 | 1 | 2025-09-09 | 47.24 | -19.4% |
| BLISSGVS | 2025-08-11 | 178.60 | 1 | 2025-09-26 | 143.93 | -19.4% |
| FORCEMOT | 2025-04-28 | 12,801.04 | 4 | 2025-10-09 | 15,350.10 | +19.9% |
| SUBROS | 2025-09-29 | 1,103.63 | 2 | 2025-10-14 | 1,046.90 | -5.1% |
| CREDITACC | 2025-01-27 | 1,084.34 | 4 | 2025-10-20 | 1,274.42 | +17.5% |
| PGHL | 2025-08-11 | 6,440.91 | 3 | 2025-11-06 | 5,938.45 | -7.8% |
| PRAKASH | 2025-08-11 | 171.78 | 2 | 2025-11-14 | 147.31 | -14.2% |
| CCL | 2025-11-10 | 1,040.17 | 2 | 2025-11-24 | 976.41 | -6.1% |
| PARAGMILK | 2025-11-17 | 354.00 | 1 | 2025-12-09 | 293.55 | -17.1% |
| MIRZAINT | 2025-08-11 | 37.63 | 4 | 2025-12-29 | 36.49 | -3.0% |
| LUMAXIND | 2025-12-01 | 5,670.25 | 2 | 2026-01-01 | 5,078.70 | -10.4% |
| KIRIINDUS | 2026-01-05 | 622.00 | 1 | 2026-01-08 | 525.16 | -15.6% |
| ESABINDIA | 2025-12-15 | 6,148.56 | 2 | 2026-01-12 | 5,605.00 | -8.8% |
| SHREDIGCEM | 2025-09-01 | 93.81 | 2 | 2026-01-20 | 83.06 | -11.5% |
| AVANTIFEED | 2025-04-15 | 766.81 | 4 | 2026-01-21 | 748.60 | -2.4% |
| AXISGOLD | 2024-11-04 | 78.43 | 4 | 2026-02-02 | 112.59 | +43.6% |
| GOLDBEES | 2025-04-07 | 79.90 | 4 | 2026-02-02 | 113.05 | +41.5% |
| NATIONALUM | 2026-01-12 | 352.30 | 3 | 2026-02-17 | 335.49 | -4.8% |
| KIRIINDUS | 2026-01-19 | 476.51 | 3 | 2026-03-02 | 427.56 | -10.3% |
| CUB | 2025-11-10 | 268.69 | 4 | 2026-03-09 | 251.43 | -6.4% |
| HINDCOPPER | 2026-01-05 | 568.62 | 4 | 2026-03-12 | 528.63 | -7.0% |
| SETFGOLD | 2025-10-13 | 120.93 | 4 | 2026-03-23 | 115.37 | -4.6% |
| ICICIB22 | 2026-02-23 | 127.18 | 1 | 2026-03-23 | 114.46 | -10.0% |
| J&KBANK | 2026-03-16 | 118.41 | 2 | 2026-03-23 | 110.67 | -6.5% |
| BAJAJHIND | 2026-03-30 | 18.46 | 2 | 2026-05-14 | 17.96 | -2.7% |
| DWARKESH | 2026-03-30 | 45.44 | 2 | 2026-05-18 | 41.52 | -8.6% |
| CPSEETF | 2026-02-02 | 105.47 | 4 | 2026-06-02 | 100.15 | -5.0% |
| BALAMINES | 2026-06-08 | 2,135.89 | 3 | 2026-06-29 | 1,931.44 | -9.6% |
| SASKEN | 2026-05-18 | 2,174.49 | 3 | 2026-07-08 | 1,933.72 | -11.1% |
| DHANUKA | 2026-05-25 | 1,136.96 | 2 | 2026-07-22 | 1,004.15 | -11.7% |
| ADFFOODS | 2026-07-06 | 320.18 | 2 | 2026-07-24 | 287.38 | -10.2% |
| MIRZAINT | 2026-07-13 | 39.06 | 2 | 2026-07-24 | 34.99 | -10.4% |
| MAHLOG | 2026-07-27 | 410.01 | 2 | 2026-09-02 | 380.33 | -7.2% |
| ASHIANA | 2026-07-27 | 388.55 | 1 | 2026-09-07 | 349.27 | -10.1% |

## Engine B — the complete trade blotter

*Buys, pyramid injections, sells and tax settlements; every stop raise and refused signal is in `_longrun_events_2020-03-01_to_2026-09-11.csv`, and engine A's full ledger in `_longrun_events_2020-03-01_to_2026-09-11_no_doubling.csv`.*

```
2020-03-09  AXISGOLD    BUY ₹9.96 at ₹4,037.70 (fresh Friday signal — BUY: 2.88× weekly, month 2.18×, ladder rising; stop ₹3,450.88; charges ₹0.01)
2020-03-09  DEEPAKNTR   BUY ₹9.99 at ₹508.80 (fresh Friday signal — BUY: 2.89× weekly, month 3.33×, ladder rising; stop ₹356.25; charges ₹0.01)
2020-03-09  GOLDSHARE   BUY ₹10.01 at ₹3,937.00 (fresh Friday signal — ACCUMULATE: 2.94× weekly, month 1.52×, ladder rising; stop ₹3,562.50; charges ₹0.01)
2020-03-09  HDFCMFGETF  BUY ₹9.91 at ₹4,002.50 (fresh Friday signal — ACCUMULATE: 2.73× weekly, month 2.32×, ladder rising; stop ₹3,540.65; charges ₹0.01)
2020-03-09  INDOCO      BUY ₹9.89 at ₹228.20 (fresh Friday signal — ACCUMULATE: 2.23× weekly, month 2.79×, ladder rising; stop ₹164.08; charges ₹0.01)
2020-03-09  IOLCP       BUY ₹9.80 at ₹51.20 (fresh Friday signal — ACCUMULATE: 2.04× weekly, month 9.15×, ladder rising; stop ₹36.91; charges ₹0.01)
2020-03-09  LALPATHLAB  BUY ₹9.82 at ₹835.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.75×, ladder rising; stop ₹743.38; charges ₹0.01)
2020-03-09  SETFGOLD    BUY ₹10.00 at ₹3,862.80 (fresh Friday signal — BUY: 3.14× weekly, month 2.45×, ladder rising; stop ₹3,548.39; charges ₹0.01)
2020-03-13  HDFCMFGETF  SELL ₹8.74 at stop ₹3,540.65 (-11.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-13  INDOCO      SELL ₹7.09 at stop ₹164.08 (-28.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-13  LALPATHLAB  SELL ₹8.72 at stop ₹743.38 (-11.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-17  AXISGOLD    SELL ₹8.49 at stop ₹3,450.88 (-14.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-17  GOLDSHARE   SELL ₹9.04 at stop ₹3,562.50 (-9.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-17  SETFGOLD    SELL ₹9.17 at stop ₹3,548.39 (-8.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-19  DEEPAKNTR   SELL ₹6.98 at stop ₹356.25 (-30.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-19  IOLCP       SELL ₹7.05 at stop ₹36.91 (-27.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-04-01  TAX         FY2020 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹13.93 / LT ₹0.00)
2020-04-13  AXISGOLD    BUY ₹8.59 at ₹4,049.00 (fresh Friday signal — ACCUMULATE: 1.53× weekly, month 3.08×, ladder rising; stop ₹3,199.23; charges ₹0.01)
2020-04-13  DEEPAKNTR   BUY ₹8.59 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.54×, ladder rising; stop ₹240.25; charges ₹0.01)
2020-04-13  GOLDBEES    BUY ₹8.56 at ₹41.24 (fresh Friday signal — ACCUMULATE: 1.55× weekly, month 9.44×, ladder rising; stop ₹31.74; charges ₹0.01)
2020-04-20  HDFCMFGETF  BUY ₹8.61 at ₹4,385.40 (fresh Friday signal — BUY: 2.66× weekly, month 4.34×, ladder rising; stop ₹3,695.50; charges ₹0.01)
2020-04-27  CADILAHC    BUY ₹8.66 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 4.52×, ladder rising; stop ₹310.03; charges ₹0.01)
2020-04-27  SYNGENE     BUY ₹8.67 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.67×, ladder rising; stop ₹285.95; charges ₹0.01)
2020-05-04  AXISGOLD    PYRAMID BUY ₹9.05 at ₹4,271.70 (box jump — doubling the stake with NEW capital; stop stays ₹3,943.45; charges ₹0.01)
2020-05-04  HDFCMFGETF  PYRAMID BUY ₹8.59 at ₹4,376.95 (box jump — doubling the stake with NEW capital; stop stays ₹4,037.50; charges ₹0.01)
2020-05-11  APLLTD      BUY ₹10.33 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.70× weekly, month 6.57×, ladder rising; stop ₹694.45; charges ₹0.01)
2020-05-11  EIDPARRY    BUY ₹10.37 at ₹164.00 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 1.53×, ladder rising; stop ₹132.60; charges ₹0.01)
2020-05-11  IOLCP       BUY ₹10.33 at ₹66.18 (fresh Friday signal — BUY: 2.18× weekly, month 2.73×, ladder rising; stop ₹51.22; charges ₹0.01)
2020-05-18  DEEPAKNTR   PYRAMID BUY ₹9.44 at ₹521.95 (box jump — doubling the stake with NEW capital; stop stays ₹474.05; charges ₹0.01)
2020-05-26  IOLCP       PYRAMID BUY ₹12.63 at ₹81.00 (box jump — doubling the stake with NEW capital; stop stays ₹69.35; charges ₹0.01)
2020-06-08  APLLTD      PYRAMID BUY ₹11.47 at ₹860.95 (box jump — doubling the stake with NEW capital; stop stays ₹785.37; charges ₹0.01)
2020-06-08  CADILAHC    PYRAMID BUY ₹9.43 at ₹360.00 (box jump — doubling the stake with NEW capital; stop stays ₹316.35; charges ₹0.01)
2020-06-08  SYNGENE     PYRAMID BUY ₹10.15 at ₹373.90 (box jump — doubling the stake with NEW capital; stop stays ₹323.19; charges ₹0.01)
2020-06-12  DEEPAKNTR   SELL ₹17.12 at stop ₹474.05 (-4.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-06-15  JTEKTINDIA  BUY ₹16.32 at ₹78.45 (fresh Friday signal — BUY: 8.49× weekly, month 5.74×, ladder rising; stop ₹47.22; charges ₹0.02)
2020-06-16  IOLCP       SELL ₹21.59 at stop ₹69.35 (-5.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-06-22  ALEMBICLTD  BUY ₹21.61 at ₹81.65 (fresh Friday signal — BUY: 11.73× weekly, month 8.56×, ladder rising; stop ₹44.84; charges ₹0.03)
2020-06-22  CADILAHC    PYRAMID BUY ₹19.15 at ₹365.95 (box jump — doubling the stake with NEW capital; stop stays ₹338.53; charges ₹0.02)
2020-06-22  EIDPARRY    PYRAMID BUY ₹16.89 at ₹267.45 (box jump — doubling the stake with NEW capital; stop stays ₹204.49; charges ₹0.02)
2020-06-22  JTEKTINDIA  PYRAMID BUY ₹14.10 at ₹67.85 (box jump — doubling the stake with NEW capital; stop stays ₹55.96; charges ₹0.02)
2020-07-06  ALEMBICLTD  PYRAMID BUY ₹22.23 at ₹84.10 (box jump — doubling the stake with NEW capital; stop stays ₹69.64; charges ₹0.03)
2020-07-06  APLLTD      PYRAMID BUY ₹23.85 at ₹896.00 (box jump — doubling the stake with NEW capital; stop stays ₹830.30; charges ₹0.03)
2020-07-06  EIDPARRY    PYRAMID BUY ₹33.58 at ₹266.00 (box jump — doubling the stake with NEW capital; stop stays ₹249.19; charges ₹0.04)
2020-07-06  SYNGENE     PYRAMID BUY ₹23.76 at ₹438.00 (box jump — doubling the stake with NEW capital; stop stays ₹378.10; charges ₹0.03)
2020-07-13  AXISGOLD    PYRAMID BUY ₹18.18 at ₹4,295.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,971.05; charges ₹0.02)
2020-07-23  AXISGOLD    SELL ₹33.57 at stop ₹3,971.05 (-6.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2020-07-27  EIDPARRY    PYRAMID BUY ₹74.19 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹273.03; charges ₹0.09)
2020-07-27  ICIL        BUY ₹37.55 at ₹69.75 (fresh Friday signal — BUY: 6.90× weekly, month 3.19×, ladder rising; stop ₹32.84; charges ₹0.04)
2020-08-03  APLLTD      PYRAMID BUY ₹52.41 at ₹985.00 (box jump — doubling the stake with NEW capital; stop stays ₹903.45; charges ₹0.06)
2020-08-10  HDFCMFGETF  PYRAMID BUY ₹19.56 at ₹4,989.95 (box jump — doubling the stake with NEW capital; stop stays ₹4,492.07; charges ₹0.02)
2020-08-10  ICIL        PYRAMID BUY ₹38.66 at ₹71.90 (box jump — doubling the stake with NEW capital; stop stays ₹58.18; charges ₹0.05)
2020-08-17  CADILAHC    PYRAMID BUY ₹41.76 at ₹399.15 (box jump — doubling the stake with NEW capital; stop stays ₹364.99; charges ₹0.05)
2020-08-17  EIDPARRY    SELL ₹137.57 at stop ₹273.03 (+2.1%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2020-08-17  SYNGENE     PYRAMID BUY ₹53.54 at ₹493.80 (box jump — doubling the stake with NEW capital; stop stays ₹434.44; charges ₹0.06)
2020-08-24  AARTIDRUGS  BUY ₹64.80 at ₹3,250.00 (fresh Friday signal — BUY: 5.29× weekly, month 7.63×, ladder rising; stop ₹1,888.30; charges ₹0.08)
2020-08-24  GOLDBEES    PYRAMID BUY ₹9.63 at ₹46.45 (box jump — doubling the stake with NEW capital; stop stays ₹41.00; charges ₹0.01)
2020-08-24  THYROCARE   BUY ₹64.69 at ₹790.05 (fresh Friday signal — BUY: 7.11× weekly, month 4.47×, ladder rising; stop ₹599.31; charges ₹0.08)
2020-08-31  ALEMBICLTD  PYRAMID BUY ₹45.57 at ₹86.25 (box jump — doubling the stake with NEW capital; stop stays ₹76.77; charges ₹0.05)
2020-09-01  APLLTD      SELL ₹98.66 at stop ₹928.62 (+0.8%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2020-09-04  GOLDBEES    SELL ₹16.97 at stop ₹41.00 (-6.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-09-07  AARTIDRUGS  PYRAMID BUY ₹57.33 at ₹2,879.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,264.30; charges ₹0.07)
2020-09-07  INDIAMART   BUY ₹41.83 at ₹2,124.50 (fresh Friday signal — BUY: 2.47× weekly, month 1.96×, ladder rising; stop ₹1,655.61; charges ₹0.05)
2020-09-07  JTEKTINDIA  PYRAMID BUY ₹31.94 at ₹76.90 (box jump — doubling the stake with NEW capital; stop stays ₹69.05; charges ₹0.04)
2020-09-07  PRINCEPIPE  BUY ₹81.88 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.10)
2020-09-07  THYROCARE   PYRAMID BUY ₹61.75 at ₹755.00 (box jump — doubling the stake with NEW capital; stop stays ₹705.09; charges ₹0.07)
2020-09-08  CADILAHC    SELL ₹76.24 at stop ₹364.99 (-3.3%, charges ₹0.08) — the cash goes back to work at the next Friday screen
2020-09-14  ICIL        PYRAMID BUY ₹91.36 at ₹85.00 (box jump — doubling the stake with NEW capital; stop stays ₹63.12; charges ₹0.11)
2020-09-14  TCI         BUY ₹76.24 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.76× weekly, month 3.77×, ladder rising; stop ₹190.07; charges ₹0.09)
2020-09-21  INDIAMART   PYRAMID BUY ₹49.59 at ₹2,521.28 (box jump — doubling the stake with NEW capital; stop stays ₹2,099.50; charges ₹0.06)
2020-09-21  PRINCEPIPE  PYRAMID BUY ₹88.07 at ₹224.00 (box jump — doubling the stake with NEW capital; stop stays ₹178.66; charges ₹0.10)
2020-09-23  HDFCMFGETF  SELL ₹35.17 at stop ₹4,492.07 (-4.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2020-09-28  ALEMBICLTD  PYRAMID BUY ₹112.47 at ₹106.50 (box jump — doubling the stake with NEW capital; stop stays ₹91.41; charges ₹0.13)
2020-09-28  ICIL        PYRAMID BUY ₹207.75 at ₹96.70 (box jump — doubling the stake with NEW capital; stop stays ₹80.43; charges ₹0.25)
2020-09-30  AARTIDRUGS  SELL ₹90.04 at stop ₹2,264.30 (-26.1%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2020-10-05  CIGNITITEC  BUY ₹125.20 at ₹421.00 (fresh Friday signal — BUY: 2.22× weekly, month 2.13×, ladder rising; stop ₹354.87; charges ₹0.15)
2020-10-05  TCI         PYRAMID BUY ₹72.19 at ₹229.40 (box jump — doubling the stake with NEW capital; stop stays ₹202.40; charges ₹0.09)
2020-10-12  INDIAMART   PYRAMID BUY ₹99.07 at ₹2,520.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,315.62; charges ₹0.12)
2020-10-12  PRINCEPIPE  PYRAMID BUY ₹184.69 at ₹235.00 (box jump — doubling the stake with NEW capital; stop stays ₹220.88; charges ₹0.22)
2020-10-12  PRINCEPIPE  SELL ₹346.62 at stop ₹220.88 (-2.0%, charges ₹0.36) — the cash goes back to work at the next Friday screen
2020-10-19  CIGNITITEC  PYRAMID BUY ₹144.51 at ₹486.50 (box jump — doubling the stake with NEW capital; stop stays ₹441.27; charges ₹0.17)
2020-10-19  INDIAMART   SELL ₹181.77 at stop ₹2,315.62 (-4.4%, charges ₹0.19) — the cash goes back to work at the next Friday screen
2020-10-19  LTTS        BUY ₹119.33 at ₹1,745.00 (fresh Friday signal — BUY: 4.76× weekly, month 2.59×, ladder rising; stop ₹1,482.95; charges ₹0.14)
2020-10-19  SUBEX       BUY ₹227.29 at ₹15.55 (fresh Friday signal — BUY: 6.85× weekly, month 4.86×, ladder rising; stop ₹11.11; charges ₹0.27)
2020-10-19  THYROCARE   PYRAMID BUY ₹169.11 at ₹1,034.45 (box jump — doubling the stake with NEW capital; stop stays ₹933.42; charges ₹0.20)
2020-10-26  JUSTDIAL    BUY ₹181.77 at ₹584.00 (fresh Friday signal — BUY: 4.99× weekly, month 1.82×, ladder rising; stop ₹383.80; charges ₹0.22)
2020-10-27  CIGNITITEC  SELL ₹261.73 at stop ₹441.27 (-2.7%, charges ₹0.27) — the cash goes back to work at the next Friday screen
2020-11-02  ALEMBICLTD  SELL ₹192.75 at stop ₹91.41 (-4.3%, charges ₹0.20) — the cash goes back to work at the next Friday screen
2020-11-02  SHREDIGCEM  BUY ₹233.70 at ₹64.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.86×, ladder rising; stop ₹46.65; charges ₹0.28)
2020-11-09  BORORENEW   BUY ₹220.78 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.26)
2020-11-09  SHREDIGCEM  PYRAMID BUY ₹238.34 at ₹65.35 (box jump — doubling the stake with NEW capital; stop stays ₹56.43; charges ₹0.28)
2020-11-09  THYROCARE   PYRAMID BUY ₹371.76 at ₹1,137.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,016.50; charges ₹0.44)
2020-11-10  SHREDIGCEM  SELL ₹410.95 at stop ₹56.43 (-12.7%, charges ₹0.43) — the cash goes back to work at the next Friday screen
2020-11-12  THYROCARE   SELL ₹663.23 at stop ₹1,016.50 (-0.4%, charges ₹0.69) — the cash goes back to work at the next Friday screen
2020-11-17  JSLHISAR    BUY ₹289.45 at ₹119.70 (fresh Friday signal — BUY: 2.03× weekly, month 1.66×, ladder rising; stop ₹89.02; charges ₹0.34)
2020-11-17  PILANIINVS  BUY ₹289.96 at ₹2,054.50 (fresh Friday signal — ACCUMULATE: 3.04× weekly, month 1.77×, ladder rising; stop ₹1,752.75; charges ₹0.34)
2020-11-17  TATASTLBSL  BUY ₹204.33 at ₹30.95 (fresh Friday signal — BUY: 2.01× weekly, month 2.00×, ladder rising; stop ₹22.80; charges ₹0.24)
2020-11-17  TRENT       BUY ₹290.43 at ₹503.33 (fresh Friday signal — ACCUMULATE: 3.30× weekly, month 1.95×, ladder rising; stop ₹367.93; charges ₹0.34)
2020-11-23  JUSTDIAL    PYRAMID BUY ₹193.46 at ₹622.30 (box jump — doubling the stake with NEW capital; stop stays ₹523.11; charges ₹0.23)
2020-11-23  LTTS        PYRAMID BUY ₹114.25 at ₹1,672.75 (box jump — doubling the stake with NEW capital; stop stays ₹1,545.70; charges ₹0.14)
2020-12-01  BORORENEW   PYRAMID BUY ₹280.90 at ₹127.00 (box jump — doubling the stake with NEW capital; stop stays ₹106.40; charges ₹0.33)
2020-12-07  PILANIINVS  PYRAMID BUY ₹307.15 at ₹2,178.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,999.75; charges ₹0.36)
2020-12-07  TCI         PYRAMID BUY ₹164.35 at ₹261.30 (box jump — doubling the stake with NEW capital; stop stays ₹234.75; charges ₹0.19)
2020-12-14  BORORENEW   PYRAMID BUY ₹587.78 at ₹132.95 (box jump — doubling the stake with NEW capital; stop stays ₹123.97; charges ₹0.70)
2020-12-14  JSLHISAR    PYRAMID BUY ₹323.17 at ₹133.80 (box jump — doubling the stake with NEW capital; stop stays ₹106.69; charges ₹0.38)
2020-12-14  TRENT       PYRAMID BUY ₹267.03 at ₹463.33 (box jump — doubling the stake with NEW capital; stop stays ₹417.53; charges ₹0.32)
2020-12-21  JTEKTINDIA  PYRAMID BUY ₹76.95 at ₹92.70 (box jump — doubling the stake with NEW capital; stop stays ₹78.47; charges ₹0.09)
2020-12-21  LTTS        PYRAMID BUY ₹301.60 at ₹2,209.15 (box jump — doubling the stake with NEW capital; stop stays ₹1,712.85; charges ₹0.36)
2020-12-21  TATASTLBSL  PYRAMID BUY ₹251.24 at ₹38.10 (box jump — doubling the stake with NEW capital; stop stays ₹34.30; charges ₹0.30)
2020-12-22  SYNGENE     SELL ₹121.76 at stop ₹562.40 (+27.0%, charges ₹0.13) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹294.83 at stop ₹234.75 (-5.5%, charges ₹0.31) — the cash goes back to work at the next Friday screen
2020-12-28  BORORENEW   PYRAMID BUY ₹2,076.67 at ₹235.00 (box jump — doubling the stake with NEW capital; stop stays ₹148.20; charges ₹2.46)
2021-01-04  PILANIINVS  PYRAMID BUY ₹580.45 at ₹2,060.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,132.80; charges ₹0.69)
2021-01-04  PILANIINVS  SELL ₹1,199.96 at stop ₹2,132.80 (+2.1%, charges ₹1.24) — the cash goes back to work at the next Friday screen
2021-01-11  FILATEX     BUY ₹1,188.15 at ₹33.75 (fresh Friday signal — BUY: 7.78× weekly, month 6.75×, ladder rising; stop ₹18.65; charges ₹1.41)
2021-01-11  JSLHISAR    PYRAMID BUY ₹771.96 at ₹159.90 (box jump — doubling the stake with NEW capital; stop stays ₹129.68; charges ₹0.91)
2021-01-11  LTTS        PYRAMID BUY ₹677.44 at ₹2,482.50 (box jump — doubling the stake with NEW capital; stop stays ₹2,194.50; charges ₹0.80)
2021-01-18  FILATEX     PYRAMID BUY ₹1,128.72 at ₹32.10 (box jump — doubling the stake with NEW capital; stop stays ₹30.16; charges ₹1.34)
2021-01-18  JSLHISAR    PYRAMID BUY ₹1,458.08 at ₹151.10 (box jump — doubling the stake with NEW capital; stop stays ₹142.59; charges ₹1.73)
2021-01-18  TATASTLBSL  PYRAMID BUY ₹591.81 at ₹44.90 (box jump — doubling the stake with NEW capital; stop stays ₹40.61; charges ₹0.70)
2021-01-20  BORORENEW   SELL ₹4,368.72 at stop ₹247.59 (+38.3%, charges ₹4.53) — the cash goes back to work at the next Friday screen
2021-01-22  JSLHISAR    SELL ₹2,747.44 at stop ₹142.59 (-3.1%, charges ₹2.85) — the cash goes back to work at the next Friday screen
2021-01-22  TATASTLBSL  SELL ₹1,068.78 at stop ₹40.61 (+2.3%, charges ₹1.11) — the cash goes back to work at the next Friday screen
2021-01-25  FILATEX     SELL ₹2,117.56 at stop ₹30.16 (-8.4%, charges ₹2.20) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹1,420.94 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹1.68)
2021-01-25  HINDZINC    BUY ₹1,415.75 at ₹277.40 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 2.11×, ladder rising; stop ₹248.97; charges ₹1.68)
2021-01-25  INDIAMART   BUY ₹1,419.10 at ₹3,990.00 (fresh Friday signal — BUY: 2.37× weekly, month 1.58×, ladder rising; stop ₹3,323.19; charges ₹1.68)
2021-01-25  JUSTDIAL    PYRAMID BUY ₹417.89 at ₹672.50 (box jump — doubling the stake with NEW capital; stop stays ₹622.35; charges ₹0.50)
2021-01-25  JUSTDIAL    SELL ₹772.20 at stop ₹622.35 (-2.4%, charges ₹0.80) — the cash goes back to work at the next Friday screen
2021-01-25  MAHLOG      BUY ₹1,436.00 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹1.70)
2021-01-25  TATAELXSI   BUY ₹1,426.33 at ₹2,608.00 (fresh Friday signal — BUY: 2.95× weekly, month 2.73×, ladder rising; stop ₹1,712.61; charges ₹1.69)
2021-01-25  TATAMOTORS  BUY ₹1,435.07 at ₹296.90 (fresh Friday signal — BUY: 3.10× weekly, month 2.05×, ladder rising; stop ₹171.38; charges ₹1.70)
2021-01-27  ICIL        SELL ₹567.50 at stop ₹132.29 (+51.5%, charges ₹0.59) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹480.49 at stop ₹417.53 (-13.6%, charges ₹0.50) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹1,731.69 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹2.05)
2021-02-01  GAEL        BUY ₹1,749.81 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹2.07)
2021-02-01  INDIAMART   PYRAMID BUY ₹1,395.78 at ₹3,929.07 (box jump — doubling the stake with NEW capital; stop stays ₹3,460.38; charges ₹1.65)
2021-02-01  TATAELXSI   PYRAMID BUY ₹1,481.32 at ₹2,711.75 (box jump — doubling the stake with NEW capital; stop stays ₹2,275.70; charges ₹1.76)
2021-02-08  APTECHT     PYRAMID BUY ₹2,093.60 at ₹216.00 (box jump — doubling the stake with NEW capital; stop stays ₹163.06; charges ₹2.48)
2021-02-08  GDL         PYRAMID BUY ₹1,428.24 at ₹159.00 (box jump — doubling the stake with NEW capital; stop stays ₹141.52; charges ₹1.69)
2021-02-08  MAHLOG      PYRAMID BUY ₹1,460.76 at ₹505.00 (box jump — doubling the stake with NEW capital; stop stays ₹408.33; charges ₹1.73)
2021-02-08  TATAMOTORS  PYRAMID BUY ₹1,538.86 at ₹318.75 (box jump — doubling the stake with NEW capital; stop stays ₹239.88; charges ₹1.82)
2021-02-15  APTECHT     PYRAMID BUY ₹4,605.12 at ₹237.70 (box jump — doubling the stake with NEW capital; stop stays ₹197.36; charges ₹5.46)
2021-02-15  HINDZINC    PYRAMID BUY ₹1,529.79 at ₹300.10 (box jump — doubling the stake with NEW capital; stop stays ₹279.30; charges ₹1.81)
2021-02-15  INDIAMART   PYRAMID BUY ₹3,290.66 at ₹4,634.30 (box jump — doubling the stake with NEW capital; stop stays ₹4,137.25; charges ₹3.90)
2021-02-15  TATAELXSI   PYRAMID BUY ₹3,112.92 at ₹2,851.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,660.00; charges ₹3.69)
2021-02-15  TATAMOTORS  PYRAMID BUY ₹3,183.49 at ₹329.90 (box jump — doubling the stake with NEW capital; stop stays ₹296.97; charges ₹3.77)
2021-02-22  TATAELXSI   SELL ₹5,799.30 at stop ₹2,660.00 (-3.5%, charges ₹6.02) — the cash goes back to work at the next Friday screen
2021-02-23  GAEL        SELL ₹1,531.57 at stop ₹62.70 (-12.3%, charges ₹1.59) — the cash goes back to work at the next Friday screen
2021-03-01  MATRIMONY   BUY ₹3,848.66 at ₹1,128.00 (fresh Friday signal — BUY: 6.50× weekly, month 2.29×, ladder rising; stop ₹726.93; charges ₹4.56)
2021-03-01  RCF         BUY ₹3,998.60 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.13×, ladder rising; stop ₹50.16; charges ₹4.74)
2021-03-02  INDIAMART   SELL ₹5,865.88 at stop ₹4,137.25 (-3.7%, charges ₹6.08) — the cash goes back to work at the next Friday screen
2021-03-08  APTECHT     PYRAMID BUY ₹8,596.81 at ₹222.00 (box jump — doubling the stake with NEW capital; stop stays ₹204.25; charges ₹10.19)
2021-03-08  JSWENERGY   BUY ₹4,832.10 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹5.73)
2021-03-15  JSWENERGY   PYRAMID BUY ₹5,041.60 at ₹85.50 (box jump — doubling the stake with NEW capital; stop stays ₹76.43; charges ₹5.97)
2021-03-15  MATRIMONY   PYRAMID BUY ₹3,637.93 at ₹1,067.50 (box jump — doubling the stake with NEW capital; stop stays ₹943.21; charges ₹4.31)
2021-03-15  RCF         PYRAMID BUY ₹4,283.41 at ₹85.80 (box jump — doubling the stake with NEW capital; stop stays ₹79.16; charges ₹5.08)
2021-03-17  RCF         SELL ₹7,890.98 at stop ₹79.16 (-4.5%, charges ₹8.19) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹15,793.15 at stop ₹204.25 (-7.0%, charges ₹16.38) — the cash goes back to work at the next Friday screen
2021-03-19  HINDZINC    SELL ₹2,842.88 at stop ₹279.30 (-3.3%, charges ₹2.95) — the cash goes back to work at the next Friday screen
2021-03-19  TATAMOTORS  SELL ₹5,722.11 at stop ₹296.97 (-6.9%, charges ₹5.94) — the cash goes back to work at the next Friday screen
2021-03-22  DEEPAKFERT  BUY ₹5,845.99 at ₹237.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.87×, ladder rising; stop ₹184.78; charges ₹6.93)
2021-03-22  KEI         BUY ₹5,814.93 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹6.89)
2021-03-22  PRAKASH     BUY ₹5,846.68 at ₹67.15 (fresh Friday signal — BUY: 2.45× weekly, month 4.02×, ladder rising; stop ₹51.52; charges ₹6.93)
2021-03-22  WELSPUNIND  BUY ₹5,844.51 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.42×, ladder rising; stop ₹67.45; charges ₹6.92)
2021-03-24  MATRIMONY   SELL ₹6,418.25 at stop ₹943.21 (-14.1%, charges ₹6.66) — the cash goes back to work at the next Friday screen
2021-03-30  DEEPAKFERT  PYRAMID BUY ₹5,497.83 at ₹223.15 (box jump — doubling the stake with NEW capital; stop stays ₹209.52; charges ₹6.51)
2021-03-30  GDL         PYRAMID BUY ₹3,315.32 at ₹184.65 (box jump — doubling the stake with NEW capital; stop stays ₹157.22; charges ₹3.93)
2021-03-30  KEI         PYRAMID BUY ₹5,788.01 at ₹520.20 (box jump — doubling the stake with NEW capital; stop stays ₹471.20; charges ₹6.86)
2021-03-30  KPITTECH    BUY ₹8,194.87 at ₹182.00 (fresh Friday signal — BUY: 1.71× weekly, month 2.77×, ladder rising; stop ₹136.62; charges ₹9.71)
2021-03-30  MAHLOG      PYRAMID BUY ₹3,226.22 at ₹558.00 (box jump — doubling the stake with NEW capital; stop stays ₹473.82; charges ₹3.82)
2021-03-30  WELSPUNIND  PYRAMID BUY ₹6,020.34 at ₹84.00 (box jump — doubling the stake with NEW capital; stop stays ₹68.17; charges ₹7.13)
2021-03-31  JTEKTINDIA  SELL ₹138.57 at stop ₹83.60 (-0.3%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2021-04-01  TAX         FY2021 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹2,854.12 / LT ₹0.00)
2021-04-05  AUBANK      BUY ₹8,255.11 at ₹631.00 (fresh Friday signal — ACCUMULATE: 3.80× weekly, month 2.03×, ladder rising; stop ₹533.06; charges ₹9.78)
2021-04-12  AUBANK      SELL ₹6,958.32 at stop ₹533.06 (-15.5%, charges ₹7.22) — the cash goes back to work at the next Friday screen
2021-04-19  JSWENERGY   PYRAMID BUY ₹11,220.50 at ₹95.20 (box jump — doubling the stake with NEW capital; stop stays ₹81.99; charges ₹13.29)
2021-04-19  KPITTECH    PYRAMID BUY ₹8,533.71 at ₹189.75 (box jump — doubling the stake with NEW capital; stop stays ₹171.05; charges ₹10.11)
2021-04-19  MOREPENLAB  BUY ₹6,995.95 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹8.29)
2021-04-19  PRAKASH     PYRAMID BUY ₹6,783.33 at ₹78.00 (box jump — doubling the stake with NEW capital; stop stays ₹74.58; charges ₹8.04)
2021-04-19  PRAKASH     SELL ₹12,950.70 at stop ₹74.58 (+2.8%, charges ₹13.43) — the cash goes back to work at the next Friday screen
2021-04-26  ORIENTREF   BUY ₹11,353.04 at ₹314.95 (fresh Friday signal — BUY: 1.81× weekly, month 5.16×, ladder rising; stop ₹247.04; charges ₹13.45)
2021-05-10  KEI         PYRAMID BUY ₹11,753.76 at ₹528.50 (box jump — doubling the stake with NEW capital; stop stays ₹485.02; charges ₹13.93)
2021-05-10  ORIENTREF   PYRAMID BUY ₹11,341.39 at ₹315.00 (box jump — doubling the stake with NEW capital; stop stays ₹283.10; charges ₹13.44)
2021-05-17  GDL         PYRAMID BUY ₹8,900.21 at ₹248.00 (box jump — doubling the stake with NEW capital; stop stays ₹230.90; charges ₹10.55)
2021-05-24  DEEPAKFERT  PYRAMID BUY ₹14,773.68 at ₹300.00 (box jump — doubling the stake with NEW capital; stop stays ₹264.10; charges ₹17.50)
2021-05-31  KEI         PYRAMID BUY ₹27,738.89 at ₹624.00 (box jump — doubling the stake with NEW capital; stop stays ₹558.60; charges ₹32.87)
2021-05-31  MAHLOG      PYRAMID BUY ₹6,179.36 at ₹534.70 (box jump — doubling the stake with NEW capital; stop stays ₹494.95; charges ₹7.32)
2021-06-07  DEEPAKFERT  PYRAMID BUY ₹29,234.56 at ₹297.00 (box jump — doubling the stake with NEW capital; stop stays ₹269.80; charges ₹34.64)
2021-06-07  JSWENERGY   PYRAMID BUY ₹32,133.81 at ₹136.40 (box jump — doubling the stake with NEW capital; stop stays ₹108.49; charges ₹38.07)
2021-06-07  KPITTECH    PYRAMID BUY ₹21,835.15 at ₹242.90 (box jump — doubling the stake with NEW capital; stop stays ₹214.70; charges ₹25.87)
2021-06-07  MOREPENLAB  PYRAMID BUY ₹11,185.86 at ₹59.95 (box jump — doubling the stake with NEW capital; stop stays ₹49.83; charges ₹13.25)
2021-06-07  ORIENTREF   PYRAMID BUY ₹22,813.27 at ₹317.00 (box jump — doubling the stake with NEW capital; stop stays ₹287.19; charges ₹27.03)
2021-06-07  WELSPUNIND  PYRAMID BUY ₹13,308.54 at ₹92.90 (box jump — doubling the stake with NEW capital; stop stays ₹80.48; charges ₹15.77)
2021-06-21  MOREPENLAB  PYRAMID BUY ₹22,787.35 at ₹61.10 (box jump — doubling the stake with NEW capital; stop stays ₹56.33; charges ₹27.00)
2021-07-12  ORIENTREF   PYRAMID BUY ₹47,937.03 at ₹333.25 (box jump — doubling the stake with NEW capital; stop stays ₹301.44; charges ₹56.80)
2021-07-19  KPITTECH    PYRAMID BUY ₹47,983.72 at ₹267.05 (box jump — doubling the stake with NEW capital; stop stays ₹232.94; charges ₹56.85)
2021-07-19  WELSPUNIND  PYRAMID BUY ₹35,778.61 at ₹124.95 (box jump — doubling the stake with NEW capital; stop stays ₹97.56; charges ₹42.39)
2021-08-10  MOREPENLAB  SELL ₹41,948.34 at stop ₹56.33 (+2.6%, charges ₹43.51) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNIND  SELL ₹71,263.48 at stop ₹124.64 (+17.2%, charges ₹73.92) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹64,799.26 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹76.78)
2021-08-16  TATAINVEST  BUY ₹50,010.23 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹59.25)
2021-08-23  TATAINVEST  PYRAMID BUY ₹47,161.39 at ₹1,235.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,139.00; charges ₹55.88)
2021-08-30  BASF        PYRAMID BUY ₹61,029.66 at ₹3,469.75 (box jump — doubling the stake with NEW capital; stop stays ₹3,220.50; charges ₹72.31)
2021-09-13  TATAINVEST  PYRAMID BUY ₹98,224.58 at ₹1,286.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,183.22; charges ₹116.38)
2021-09-20  GDL         SELL ₹19,061.30 at stop ₹266.00 (+26.8%, charges ₹19.77) — the cash goes back to work at the next Friday screen
2021-09-27  TATAINVEST  PYRAMID BUY ₹2.00 lakh at ₹1,309.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,187.74; charges ₹236.62)
2021-10-22  KEI         SELL ₹75,722.84 at stop ₹853.10 (+48.5%, charges ₹78.55) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        PYRAMID BUY ₹1.18 lakh at ₹3,345.50 (box jump — doubling the stake with NEW capital; stop stays ₹3,220.59; charges ₹139.36)
2021-10-25  BASF        SELL ₹2.26 lakh at stop ₹3,220.59 (-6.9%, charges ₹234.52) — the cash goes back to work at the next Friday screen
2021-10-25  SHOPERSTOP  BUY ₹94,784.13 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹112.30)
2021-11-01  TCIEXP      BUY ₹1.06 lakh at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹125.21)
2021-11-01  TTKPRESTIG  BUY ₹1.20 lakh at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹142.67)
2021-11-08  SHOPERSTOP  PYRAMID BUY ₹1.06 lakh at ₹363.60 (box jump — doubling the stake with NEW capital; stop stays ₹319.53; charges ₹125.11)
2021-11-08  TCIEXP      PYRAMID BUY ₹1.16 lakh at ₹2,009.25 (box jump — doubling the stake with NEW capital; stop stays ₹1,651.24; charges ₹137.21)
2021-11-08  TTKPRESTIG  PYRAMID BUY ₹1.25 lakh at ₹11,451.00 (box jump — doubling the stake with NEW capital; stop stays ₹10,070.05; charges ₹147.80)
2021-11-15  SHOPERSTOP  PYRAMID BUY ₹2.21 lakh at ₹381.35 (box jump — doubling the stake with NEW capital; stop stays ₹335.82; charges ₹262.27)
2021-11-15  TCIEXP      PYRAMID BUY ₹2.30 lakh at ₹1,999.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,807.09; charges ₹272.97)
2021-11-18  DEEPAKFERT  SELL ₹72,436.73 at stop ₹368.55 (+31.2%, charges ₹75.14) — the cash goes back to work at the next Friday screen
2021-11-22  SHOPERSTOP  SELL ₹3.89 lakh at stop ₹335.82 (-7.5%, charges ₹403.75) — the cash goes back to work at the next Friday screen
2021-11-26  TATAINVEST  SELL ₹4.38 lakh at stop ₹1,436.49 (+11.0%, charges ₹453.94) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹2.19 lakh at stop ₹10,070.05 (-10.5%, charges ₹227.22) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹2.01 lakh at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹238.36)
2021-11-29  ESCORTS     BUY ₹2.02 lakh at ₹1,875.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.18×, ladder rising; stop ₹1,369.04; charges ₹238.98)
2021-11-29  RAYMOND     BUY ₹1.99 lakh at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹235.95)
2021-11-29  TVTODAY     BUY ₹2.02 lakh at ₹328.80 (fresh Friday signal — ACCUMULATE: 2.49× weekly, month 4.40×, ladder rising; stop ₹277.73; charges ₹238.79)
2021-11-30  MAHLOG      SELL ₹15,104.22 at stop ₹654.55 (+23.0%, charges ₹15.67) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹2.74 lakh at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹324.72)
2021-12-06  BSOFT       PYRAMID BUY ₹2.09 lakh at ₹485.00 (box jump — doubling the stake with NEW capital; stop stays ₹424.65; charges ₹248.21)
2021-12-06  TCIEXP      PYRAMID BUY ₹5.24 lakh at ₹2,277.25 (box jump — doubling the stake with NEW capital; stop stays ₹1,909.50; charges ₹621.32)
2021-12-13  ESCORTS     PYRAMID BUY ₹2.01 lakh at ₹1,869.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,739.73; charges ₹237.93)
2021-12-13  RAYMOND     PYRAMID BUY ₹2.21 lakh at ₹661.00 (box jump — doubling the stake with NEW capital; stop stays ₹560.88; charges ₹261.37)
2021-12-13  TVTODAY     PYRAMID BUY ₹2.10 lakh at ₹342.44 (box jump — doubling the stake with NEW capital; stop stays ₹311.68; charges ₹248.40)
2021-12-20  KPITTECH    SELL ₹1.65 lakh at stop ₹458.85 (+90.6%, charges ₹170.77) — the cash goes back to work at the next Friday screen
2021-12-21  TCIEXP      SELL ₹9.38 lakh at stop ₹2,039.74 (-3.7%, charges ₹972.87) — the cash goes back to work at the next Friday screen
2021-12-27  BSE         PYRAMID BUY ₹2.68 lakh at ₹1,850.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,634.39; charges ₹317.48)
2021-12-27  DIAMONDYD   BUY ₹3.59 lakh at ₹820.10 (fresh Friday signal — ACCUMULATE: 3.07× weekly, month 2.05×, ladder rising; stop ₹747.75; charges ₹425.33)
2021-12-27  MINDAIND    BUY ₹3.58 lakh at ₹1,180.00 (fresh Friday signal — BUY: 3.66× weekly, month 2.64×, ladder rising; stop ₹929.20; charges ₹424.30)
2021-12-27  SWANENERGY  BUY ₹3.59 lakh at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹424.80)
2022-01-03  MINDAIND    PYRAMID BUY ₹3.73 lakh at ₹1,229.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,088.41; charges ₹441.70)
2022-01-07  MINDAIND    SELL ₹6.59 lakh at stop ₹1,088.41 (-9.7%, charges ₹683.35) — the cash goes back to work at the next Friday screen
2022-01-10  EVERESTIND  BUY ₹3.39 lakh at ₹598.65 (fresh Friday signal — BUY: 3.00× weekly, month 1.77×, ladder rising; stop ₹490.96; charges ₹401.98)
2022-01-10  ZEELEARN    BUY ₹4.02 lakh at ₹17.80 (fresh Friday signal — BUY: 14.73× weekly, month 5.09×, ladder rising; stop ₹13.06; charges ₹476.50)
2022-01-17  EVERESTIND  PYRAMID BUY ₹3.36 lakh at ₹593.50 (box jump — doubling the stake with NEW capital; stop stays ₹536.75; charges ₹398.05)
2022-01-21  LTTS        SELL ₹2,646.45 at stop ₹4,856.88 (+118.7%, charges ₹2.75) — the cash goes back to work at the next Friday screen
2022-01-24  DIAMONDYD   PYRAMID BUY ₹3.85 lakh at ₹880.00 (box jump — doubling the stake with NEW capital; stop stays ₹817.00; charges ₹455.86)
2022-01-24  ESCORTS     PYRAMID BUY ₹4.02 lakh at ₹1,869.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,754.65; charges ₹475.77)
2022-01-24  EVERESTIND  SELL ₹6.07 lakh at stop ₹536.75 (-10.0%, charges ₹629.31) — the cash goes back to work at the next Friday screen
2022-01-24  SWANENERGY  PYRAMID BUY ₹4.18 lakh at ₹175.00 (box jump — doubling the stake with NEW capital; stop stays ₹162.64; charges ₹495.35)
2022-01-24  TVTODAY     SELL ₹3.81 lakh at stop ₹311.68 (-7.1%, charges ₹395.24) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹7.76 lakh at stop ₹162.64 (+0.1%, charges ₹804.77) — the cash goes back to work at the next Friday screen
2022-01-31  ANDHRSUGAR  BUY ₹5.32 lakh at ₹157.95 (fresh Friday signal — BUY: 1.89× weekly, month 1.58×, ladder rising; stop ₹119.37; charges ₹629.99)
2022-01-31  DIAMONDYD   SELL ₹7.13 lakh at stop ₹817.00 (-3.9%, charges ₹739.85) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹5.32 lakh at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹630.34)
2022-01-31  TV18BRDCST  BUY ₹5.32 lakh at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹629.85)
2022-02-07  ANDHRSUGAR  PYRAMID BUY ₹5.51 lakh at ₹163.90 (box jump — doubling the stake with NEW capital; stop stays ₹135.28; charges ₹652.94)
2022-02-07  CCL         BUY ₹8.04 lakh at ₹503.55 (fresh Friday signal — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹952.80)
2022-02-07  RAYMOND     PYRAMID BUY ₹5.19 lakh at ₹778.00 (box jump — doubling the stake with NEW capital; stop stays ₹679.35; charges ₹614.91)
2022-02-07  SHARDACROP  PYRAMID BUY ₹5.98 lakh at ₹660.10 (box jump — doubling the stake with NEW capital; stop stays ₹545.30; charges ₹708.35)
2022-02-07  TV18BRDCST  PYRAMID BUY ₹5.86 lakh at ₹65.00 (box jump — doubling the stake with NEW capital; stop stays ₹53.30; charges ₹694.26)
2022-02-07  ZEELEARN    PYRAMID BUY ₹3.52 lakh at ₹15.60 (box jump — doubling the stake with NEW capital; stop stays ₹13.28; charges ₹417.11)
2022-02-11  SHARDACROP  SELL ₹9.86 lakh at stop ₹545.30 (-12.5%, charges ₹1,022.94) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹3.66 lakh at stop ₹424.65 (-10.6%, charges ₹379.92) — the cash goes back to work at the next Friday screen
2022-02-14  CCL         PYRAMID BUY ₹7.42 lakh at ₹465.00 (box jump — doubling the stake with NEW capital; stop stays ₹441.75; charges ₹878.81)
2022-02-14  GNFC        BUY ₹8.19 lakh at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹970.86)
2022-02-15  RAYMOND     SELL ₹9.05 lakh at stop ₹679.35 (-3.4%, charges ₹938.64) — the cash goes back to work at the next Friday screen
2022-02-21  ANDHRSUGAR  SELL ₹9.08 lakh at stop ₹135.28 (-15.9%, charges ₹942.12) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹9.95 lakh at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹1,179.08)
2022-02-21  EVERESTIND  BUY ₹5.23 lakh at ₹740.00 (fresh Friday signal — BUY: 3.34× weekly, month 1.68×, ladder rising; stop ₹522.67; charges ₹619.26)
2022-02-21  GNFC        PYRAMID BUY ₹8.11 lakh at ₹548.00 (box jump — doubling the stake with NEW capital; stop stays ₹497.80; charges ₹960.94)
2022-02-21  TV18BRDCST  PYRAMID BUY ₹11.80 lakh at ₹65.50 (box jump — doubling the stake with NEW capital; stop stays ₹58.38; charges ₹1,398.36)
2022-02-22  TV18BRDCST  SELL ₹21.00 lakh at stop ₹58.38 (-8.4%, charges ₹2,178.80) — the cash goes back to work at the next Friday screen
2022-02-22  ZEELEARN    SELL ₹5.98 lakh at stop ₹13.28 (-20.5%, charges ₹620.73) — the cash goes back to work at the next Friday screen
2022-02-24  CCL         SELL ₹14.07 lakh at stop ₹441.75 (-8.8%, charges ₹1,459.47) — the cash goes back to work at the next Friday screen
2022-02-25  ESCORTS     SELL ₹7.52 lakh at stop ₹1,754.65 (-6.2%, charges ₹780.52) — the cash goes back to work at the next Friday screen
2022-03-07  EVERESTIND  PYRAMID BUY ₹4.37 lakh at ₹620.00 (box jump — doubling the stake with NEW capital; stop stays ₹526.21; charges ₹518.22)
2022-03-07  EXCELINDUS  BUY ₹10.17 lakh at ₹1,523.00 (fresh Friday signal — BUY: 6.93× weekly, month 5.51×, ladder rising; stop ₹1,016.01; charges ₹1,205.09)
2022-03-07  HDFCMFGETF  BUY ₹10.24 lakh at ₹46.90 (fresh Friday signal — BUY: 1.99× weekly, month 1.52×, ladder rising; stop ₹40.00; charges ₹1,213.56)
2022-03-14  KOTAKGOLD   BUY ₹10.95 lakh at ₹44.64 (fresh Friday signal — BUY: 1.78× weekly, month 1.90×, ladder rising; stop ₹40.55; charges ₹1,297.67)
2022-03-21  BSE         SELL ₹4.73 lakh at stop ₹1,634.39 (-12.6%, charges ₹490.31) — the cash goes back to work at the next Friday screen
2022-03-21  EXCELINDUS  PYRAMID BUY ₹11.23 lakh at ₹1,683.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,438.30; charges ₹1,330.78)
2022-03-21  HDFCMFGETF  PYRAMID BUY ₹9.99 lakh at ₹45.81 (box jump — doubling the stake with NEW capital; stop stays ₹41.99; charges ₹1,183.96)
2022-03-28  EVERESTIND  PYRAMID BUY ₹10.29 lakh at ₹730.00 (box jump — doubling the stake with NEW capital; stop stays ₹594.70; charges ₹1,219.60)
2022-03-28  KOTAKGOLD   PYRAMID BUY ₹10.83 lakh at ₹44.18 (box jump — doubling the stake with NEW capital; stop stays ₹41.14; charges ₹1,282.78)
2022-03-29  EXCELINDUS  SELL ₹19.16 lakh at stop ₹1,438.30 (-10.3%, charges ₹1,987.14) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹13.35 lakh / LT ₹0.00)
2022-04-04  INOXLEISUR  BUY ₹15.15 lakh at ₹520.85 (fresh Friday signal — ACCUMULATE: 7.27× weekly, month 3.35×, ladder rising; stop ₹470.35; charges ₹1,794.49)
2022-04-04  RCF         BUY ₹15.07 lakh at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹1,785.73)
2022-04-11  TNPL        BUY ₹15.10 lakh at ₹193.30 (fresh Friday signal — BUY: 4.95× weekly, month 4.11×, ladder rising; stop ₹157.89; charges ₹1,788.73)
2022-04-25  GNFC        PYRAMID BUY ₹25.04 lakh at ₹846.40 (box jump — doubling the stake with NEW capital; stop stays ₹792.16; charges ₹2,966.64)
2022-04-25  RCF         PYRAMID BUY ₹16.27 lakh at ₹104.20 (box jump — doubling the stake with NEW capital; stop stays ₹93.15; charges ₹1,927.93)
2022-04-25  TNPL        PYRAMID BUY ₹16.47 lakh at ₹211.10 (box jump — doubling the stake with NEW capital; stop stays ₹176.75; charges ₹1,951.13)
2022-04-27  KOTAKGOLD   SELL ₹20.13 lakh at stop ₹41.14 (-7.4%, charges ₹2,088.17) — the cash goes back to work at the next Friday screen
2022-04-28  EVERESTIND  SELL ₹16.74 lakh at stop ₹594.70 (-15.6%, charges ₹1,736.88) — the cash goes back to work at the next Friday screen
2022-05-02  RIIL        BUY ₹20.37 lakh at ₹1,100.00 (fresh Friday signal — BUY: 5.17× weekly, month 3.64×, ladder rising; stop ₹852.81; charges ₹2,413.11)
2022-05-02  VBL         BUY ₹20.39 lakh at ₹216.40 (fresh Friday signal — BUY: 3.87× weekly, month 2.06×, ladder rising; stop ₹166.33; charges ₹2,416.35)
2022-05-04  RCF         SELL ₹29.05 lakh at stop ₹93.15 (-7.1%, charges ₹3,012.87) — the cash goes back to work at the next Friday screen
2022-05-06  GNFC        SELL ₹46.79 lakh at stop ₹792.16 (+13.4%, charges ₹4,853.74) — the cash goes back to work at the next Friday screen
2022-05-06  INOXLEISUR  SELL ₹13.65 lakh at stop ₹470.35 (-9.7%, charges ₹1,415.59) — the cash goes back to work at the next Friday screen
2022-05-09  GEPIL       BUY ₹24.66 lakh at ₹182.65 (fresh Friday signal — ACCUMULATE: 1.55× weekly, month 2.61×, ladder rising; stop ₹163.45; charges ₹2,921.54)
2022-05-09  JKIL        BUY ₹24.77 lakh at ₹229.70 (fresh Friday signal — BUY: 6.96× weekly, month 3.58×, ladder rising; stop ₹192.28; charges ₹2,935.16)
2022-05-09  MRPL        BUY ₹24.80 lakh at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹2,938.25)
2022-05-09  TNPL        PYRAMID BUY ₹32.54 lakh at ₹208.70 (box jump — doubling the stake with NEW capital; stop stays ₹195.61; charges ₹3,855.61)
2022-05-09  VBL         PYRAMID BUY ₹19.96 lakh at ₹212.00 (box jump — doubling the stake with NEW capital; stop stays ₹196.27; charges ₹2,364.41)
2022-05-10  TNPL        SELL ₹60.90 lakh at stop ₹195.61 (-4.8%, charges ₹6,317.36) — the cash goes back to work at the next Friday screen
2022-05-23  ACC         BUY ₹31.79 lakh at ₹2,260.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹3,766.78)
2022-05-23  JKIL        PYRAMID BUY ₹24.78 lakh at ₹230.00 (box jump — doubling the stake with NEW capital; stop stays ₹196.02; charges ₹2,935.51)
2022-05-23  MRPL        PYRAMID BUY ₹30.10 lakh at ₹94.80 (box jump — doubling the stake with NEW capital; stop stays ₹60.81; charges ₹3,566.88)
2022-05-23  RIIL        PYRAMID BUY ₹19.23 lakh at ₹1,040.00 (box jump — doubling the stake with NEW capital; stop stays ₹863.73; charges ₹2,278.78)
2022-05-23  VADILALIND  BUY ₹31.72 lakh at ₹1,805.00 (fresh Friday signal — BUY: 1.51× weekly, month 1.94×, ladder rising; stop ₹1,567.50; charges ₹3,758.57)
2022-05-26  RIIL        SELL ₹31.89 lakh at stop ₹863.73 (-19.3%, charges ₹3,308.43) — the cash goes back to work at the next Friday screen
2022-05-31  GEPIL       SELL ₹22.02 lakh at stop ₹163.45 (-10.5%, charges ₹2,283.83) — the cash goes back to work at the next Friday screen
2022-06-06  MRPL        PYRAMID BUY ₹56.08 lakh at ₹88.35 (box jump — doubling the stake with NEW capital; stop stays ₹69.61; charges ₹6,644.45)
2022-06-06  VBL         SELL ₹36.89 lakh at stop ₹196.27 (-8.4%, charges ₹3,826.63) — the cash goes back to work at the next Friday screen
2022-06-13  JKIL        PYRAMID BUY ₹61.95 lakh at ₹287.70 (box jump — doubling the stake with NEW capital; stop stays ₹233.94; charges ₹7,339.52)
2022-06-20  APARINDS    BUY ₹40.45 lakh at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹4,792.92)
2022-06-20  JSWENERGY   SELL ₹95,016.74 at stop ₹201.99 (+78.9%, charges ₹98.56) — the cash goes back to work at the next Friday screen
2022-06-27  VADILALIND  PYRAMID BUY ₹34.67 lakh at ₹1,975.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,602.19; charges ₹4,107.69)
2022-07-04  APARINDS    PYRAMID BUY ₹41.67 lakh at ₹980.00 (box jump — doubling the stake with NEW capital; stop stays ₹844.03; charges ₹4,937.63)
2022-07-06  MRPL        SELL ₹88.23 lakh at stop ₹69.61 (-20.3%, charges ₹9,151.64) — the cash goes back to work at the next Friday screen
2022-07-11  VADILALIND  PYRAMID BUY ₹73.20 lakh at ₹2,086.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,877.25; charges ₹8,672.80)
2022-07-18  ACC         PYRAMID BUY ₹30.36 lakh at ₹2,160.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,030.06; charges ₹3,597.42)
2022-07-18  LUMAXIND    BUY ₹61.53 lakh at ₹1,483.25 (fresh Friday signal — BUY: 2.18× weekly, month 1.90×, ladder rising; stop ₹1,282.55; charges ₹7,290.33)
2022-07-25  LUMAXIND    PYRAMID BUY ₹58.55 lakh at ₹1,413.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,320.50; charges ₹6,936.81)
2022-07-25  TIINDIA     BUY ₹84.26 lakh at ₹2,135.00 (fresh Friday signal — BUY: 4.17× weekly, month 2.43×, ladder rising; stop ₹1,862.00; charges ₹9,983.78)
2022-07-25  VADILALIND  PYRAMID BUY ₹1.45 crore at ₹2,071.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,924.70; charges ₹17,209.03)
2022-08-01  JKIL        PYRAMID BUY ₹1.46 crore at ₹338.50 (box jump — doubling the stake with NEW capital; stop stays ₹308.80; charges ₹17,260.74)
2022-08-05  JKIL        SELL ₹2.65 crore at stop ₹308.80 (+3.4%, charges ₹27,526.59) — the cash goes back to work at the next Friday screen
2022-08-08  ACC         PYRAMID BUY ₹63.47 lakh at ₹2,260.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,053.90; charges ₹7,520.17)
2022-08-08  NAVNETEDUL  BUY ₹1.17 crore at ₹130.50 (fresh Friday signal — BUY: 14.73× weekly, month 3.84×, ladder rising; stop ₹88.40; charges ₹13,911.28)
2022-08-08  TIINDIA     PYRAMID BUY ₹89.57 lakh at ₹2,272.15 (box jump — doubling the stake with NEW capital; stop stays ₹1,867.30; charges ₹10,612.54)
2022-08-08  TVSSRICHAK  BUY ₹1.17 crore at ₹2,242.10 (fresh Friday signal — BUY: 10.49× weekly, month 1.64×, ladder rising; stop ₹1,791.98; charges ₹13,921.35)
2022-08-16  ACC         PYRAMID BUY ₹1.26 crore at ₹2,248.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,085.11; charges ₹14,951.62)
2022-08-22  APARINDS    PYRAMID BUY ₹1.03 crore at ₹1,208.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,095.35; charges ₹12,165.57)
2022-08-22  NAVNETEDUL  PYRAMID BUY ₹1.16 crore at ₹129.00 (box jump — doubling the stake with NEW capital; stop stays ₹116.38; charges ₹13,735.09)
2022-08-22  TVSSRICHAK  PYRAMID BUY ₹1.09 crore at ₹2,090.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,914.38; charges ₹12,961.57)
2022-09-05  NAVNETEDUL  PYRAMID BUY ₹2.49 crore at ₹138.40 (box jump — doubling the stake with NEW capital; stop stays ₹125.88; charges ₹29,454.42)
2022-09-12  APARINDS    PYRAMID BUY ₹2.09 crore at ₹1,228.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,108.54; charges ₹24,719.32)
2022-09-12  LUMAXIND    PYRAMID BUY ₹1.37 crore at ₹1,649.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,492.45; charges ₹16,181.21)
2022-09-26  NAVNETEDUL  PYRAMID BUY ₹4.83 crore at ₹134.45 (box jump — doubling the stake with NEW capital; stop stays ₹127.30; charges ₹57,193.65)
2022-09-26  NAVNETEDUL  SELL ₹9.13 crore at stop ₹127.30 (-5.2%, charges ₹94,665.12) — the cash goes back to work at the next Friday screen
2022-09-26  TIINDIA     PYRAMID BUY ₹2.16 crore at ₹2,737.75 (box jump — doubling the stake with NEW capital; stop stays ₹2,360.75; charges ₹25,559.29)
2022-09-26  TVSSRICHAK  PYRAMID BUY ₹2.65 crore at ₹2,530.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,432.24; charges ₹31,362.05)
2022-09-26  TVSSRICHAK  SELL ₹5.08 crore at stop ₹2,432.24 (+3.6%, charges ₹52,706.60) — the cash goes back to work at the next Friday screen
2022-10-03  ALLCARGO    BUY ₹3.24 crore at ₹413.00 (fresh Friday signal — ACCUMULATE: 2.01× weekly, month 3.12×, ladder rising; stop ₹336.30; charges ₹38,417.26)
2022-10-03  LIBERTSHOE  BUY ₹3.23 crore at ₹314.05 (fresh Friday signal — BUY: 10.93× weekly, month 7.97×, ladder rising; stop ₹174.37; charges ₹38,297.38)
2022-10-03  SCHNEIDER   BUY ₹3.25 crore at ₹183.85 (fresh Friday signal — BUY: 2.05× weekly, month 3.46×, ladder rising; stop ₹137.51; charges ₹38,451.07)
2022-10-03  WESTLIFE    BUY ₹3.25 crore at ₹728.00 (fresh Friday signal — ACCUMULATE: 2.19× weekly, month 1.94×, ladder rising; stop ₹633.65; charges ₹38,506.61)
2022-10-10  SCHNEIDER   PYRAMID BUY ₹3.34 crore at ₹189.20 (box jump — doubling the stake with NEW capital; stop stays ₹159.60; charges ₹39,523.10)
2022-10-20  VADILALIND  SELL ₹3.21 crore at stop ₹2,295.06 (+13.1%, charges ₹33,338.41) — the cash goes back to work at the next Friday screen
2022-10-24  GODFRYPHLP  BUY ₹3.61 crore at ₹1,451.00 (fresh Friday signal — BUY: 4.48× weekly, month 3.07×, ladder rising; stop ₹1,209.44; charges ₹42,754.42)
2022-10-31  TIINDIA     PYRAMID BUY ₹4.21 crore at ₹2,675.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,465.49; charges ₹49,917.34)
2022-11-01  LUMAXIND    SELL ₹2.47 crore at stop ₹1,492.45 (-3.6%, charges ₹25,601.46) — the cash goes back to work at the next Friday screen
2022-11-03  APARINDS    SELL ₹4.61 crore at stop ₹1,358.50 (+17.4%, charges ₹47,804.89) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹4.70 crore at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹55,632.70)
2022-11-07  LIBERTSHOE  PYRAMID BUY ₹3.02 crore at ₹293.95 (box jump — doubling the stake with NEW capital; stop stays ₹240.31; charges ₹35,803.78)
2022-11-07  RVNL        BUY ₹3.60 crore at ₹46.85 (fresh Friday signal — BUY: 4.42× weekly, month 4.42×, ladder rising; stop ₹33.77; charges ₹42,676.06)
2022-11-07  WESTLIFE    PYRAMID BUY ₹3.40 crore at ₹763.50 (box jump — doubling the stake with NEW capital; stop stays ₹671.22; charges ₹40,336.49)
2022-11-10  SCHNEIDER   SELL ₹5.62 crore at stop ₹159.60 (-14.4%, charges ₹58,282.38) — the cash goes back to work at the next Friday screen
2022-11-14  CGCL        PYRAMID BUY ₹12.20 lakh at ₹736.05 (box jump — doubling the stake with NEW capital; stop stays ₹699.20; charges ₹1,445.93)
2022-11-14  PIIND       BUY ₹5.12 crore at ₹3,443.90 (fresh Friday signal — BUY: 5.02× weekly, month 1.65×, ladder rising; stop ₹3,060.95; charges ₹60,717.43)
2022-11-14  RVNL        PYRAMID BUY ₹3.95 crore at ₹51.45 (box jump — doubling the stake with NEW capital; stop stays ₹37.29; charges ₹46,810.71)
2022-11-21  GODFRYPHLP  PYRAMID BUY ₹4.57 crore at ₹1,840.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,492.45; charges ₹54,152.26)
2022-11-21  KTKBANK     PYRAMID BUY ₹4.64 crore at ₹138.50 (box jump — doubling the stake with NEW capital; stop stays ₹123.03; charges ₹54,971.43)
2022-11-21  RVNL        PYRAMID BUY ₹9.73 crore at ₹63.40 (box jump — doubling the stake with NEW capital; stop stays ₹46.27; charges ₹1.15 lakh)
2022-11-21  WESTLIFE    PYRAMID BUY ₹6.73 crore at ₹755.15 (box jump — doubling the stake with NEW capital; stop stays ₹708.51; charges ₹79,743.43)
2022-11-28  ALLCARGO    PYRAMID BUY ₹3.66 crore at ₹466.70 (box jump — doubling the stake with NEW capital; stop stays ₹432.77; charges ₹43,361.00)
2022-11-28  PIIND       PYRAMID BUY ₹5.05 crore at ₹3,400.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,123.65; charges ₹59,872.43)
2022-11-29  ALLCARGO    SELL ₹6.78 crore at stop ₹432.77 (-1.6%, charges ₹70,289.95) — the cash goes back to work at the next Friday screen
2022-12-05  GODFRYPHLP  PYRAMID BUY ₹9.09 crore at ₹1,830.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,643.55; charges ₹1.08 lakh)
2022-12-05  HDFCMFGETF  PYRAMID BUY ₹20.51 lakh at ₹47.05 (box jump — doubling the stake with NEW capital; stop stays ₹43.56; charges ₹2,430.57)
2022-12-05  MSTCLTD     BUY ₹7.27 crore at ₹336.00 (fresh Friday signal — BUY: 11.49× weekly, month 2.93×, ladder rising; stop ₹230.96; charges ₹86,139.80)
2022-12-05  RVNL        PYRAMID BUY ₹23.29 crore at ₹75.90 (box jump — doubling the stake with NEW capital; stop stays ₹53.77; charges ₹2.76 lakh)
2022-12-12  HDFCMFGETF  PYRAMID BUY ₹41.68 lakh at ₹47.83 (box jump — doubling the stake with NEW capital; stop stays ₹44.65; charges ₹4,938.79)
2022-12-19  KTKBANK     PYRAMID BUY ₹10.27 crore at ₹153.45 (box jump — doubling the stake with NEW capital; stop stays ₹139.84; charges ₹1.22 lakh)
2022-12-19  MSTCLTD     PYRAMID BUY ₹6.89 crore at ₹318.70 (box jump — doubling the stake with NEW capital; stop stays ₹290.44; charges ₹81,607.82)
2022-12-22  MSTCLTD     SELL ₹12.53 crore at stop ₹290.44 (-11.3%, charges ₹1.30 lakh) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹2.76 crore at stop ₹2,465.16 (+10.0%, charges ₹28,662.34) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹18.70 crore at stop ₹139.84 (-4.4%, charges ₹1.94 lakh) — the cash goes back to work at the next Friday screen
2022-12-26  GODFRYPHLP  SELL ₹16.29 crore at stop ₹1,643.55 (-5.4%, charges ₹1.69 lakh) — the cash goes back to work at the next Friday screen
2022-12-26  RVNL        SELL ₹37.11 crore at stop ₹60.57 (-8.3%, charges ₹3.85 lakh) — the cash goes back to work at the next Friday screen
2023-01-02  BAJAJHIND   BUY ₹10.79 crore at ₹17.20 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 4.56×, ladder rising; stop ₹13.98; charges ₹1.28 lakh)
2023-01-02  GICRE       BUY ₹12.68 crore at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 11.18×, ladder rising; stop ₹137.57; charges ₹1.50 lakh)
2023-01-02  GSFC        BUY ₹12.80 crore at ₹140.70 (fresh Friday signal — ACCUMULATE: 2.14× weekly, month 1.67×, ladder rising; stop ₹111.58; charges ₹1.52 lakh)
2023-01-02  IOB         BUY ₹12.70 crore at ₹32.40 (fresh Friday signal — ACCUMULATE: 4.77× weekly, month 30.16×, ladder rising; stop ₹21.23; charges ₹1.51 lakh)
2023-01-02  JINDALSAW   BUY ₹12.86 crore at ₹51.98 (fresh Friday signal — ACCUMULATE: 1.95× weekly, month 2.35×, ladder rising; stop ₹42.55; charges ₹1.52 lakh)
2023-01-02  JSL         BUY ₹12.74 crore at ₹241.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.13×, ladder rising; stop ₹192.61; charges ₹1.51 lakh)
2023-01-02  YESBANK     BUY ₹12.81 crore at ₹20.85 (fresh Friday signal — ACCUMULATE: 2.12× weekly, month 4.61×, ladder rising; stop ₹15.00; charges ₹1.52 lakh)
2023-01-09  CGCL        PYRAMID BUY ₹25.02 lakh at ₹754.95 (box jump — doubling the stake with NEW capital; stop stays ₹704.95; charges ₹2,964.35)
2023-01-11  TIINDIA     SELL ₹8.17 crore at stop ₹2,598.34 (+1.0%, charges ₹84,761.41) — the cash goes back to work at the next Friday screen
2023-01-16  ANUP        BUY ₹8.17 crore at ₹476.12 (fresh Friday signal — ACCUMULATE: 4.84× weekly, month 1.56×, ladder rising; stop ₹364.75; charges ₹96,815.74)
2023-01-16  GICRE       PYRAMID BUY ₹13.22 crore at ₹187.05 (box jump — doubling the stake with NEW capital; stop stays ₹167.72; charges ₹1.57 lakh)
2023-01-16  JSL         PYRAMID BUY ₹12.61 crore at ₹238.90 (box jump — doubling the stake with NEW capital; stop stays ₹218.83; charges ₹1.49 lakh)
2023-01-16  WESTLIFE    SELL ₹12.61 crore at stop ₹708.51 (-5.6%, charges ₹1.31 lakh) — the cash goes back to work at the next Friday screen
2023-01-23  JINDALSAW   PYRAMID BUY ₹14.46 crore at ₹58.50 (box jump — doubling the stake with NEW capital; stop stays ₹51.77; charges ₹1.71 lakh)
2023-01-23  PIIND       SELL ₹9.27 crore at stop ₹3,123.65 (-8.7%, charges ₹96,157.88) — the cash goes back to work at the next Friday screen
2023-01-23  USHAMART    BUY ₹12.61 crore at ₹203.00 (fresh Friday signal — BUY: 2.91× weekly, month 3.70×, ladder rising; stop ₹166.25; charges ₹1.49 lakh)
2023-01-30  BAJAJHIND   SELL ₹8.75 crore at stop ₹13.98 (-18.7%, charges ₹90,800.43) — the cash goes back to work at the next Friday screen
2023-02-01  GICRE       SELL ₹23.67 crore at stop ₹167.72 (-8.4%, charges ₹2.46 lakh) — the cash goes back to work at the next Friday screen
2023-02-06  ANUP        PYRAMID BUY ₹9.64 crore at ₹562.10 (box jump — doubling the stake with NEW capital; stop stays ₹466.90; charges ₹1.14 lakh)
2023-02-06  EBBETF0423  BUY ₹17.19 crore at ₹1,216.48 (fresh Friday signal — ACCUMULATE: 1.85× weekly, month 2.06×, ladder rising; stop ₹1,124.88; charges ₹2.04 lakh)
2023-02-06  LIBERTSHOE  SELL ₹4.93 crore at stop ₹240.31 (-21.0%, charges ₹51,168.40) — the cash goes back to work at the next Friday screen
2023-02-06  ORIENTPPR   BUY ₹17.19 crore at ₹45.70 (fresh Friday signal — ACCUMULATE: 1.64× weekly, month 2.07×, ladder rising; stop ₹39.90; charges ₹2.04 lakh)
2023-02-13  ANUP        PYRAMID BUY ₹19.53 crore at ₹570.00 (box jump — doubling the stake with NEW capital; stop stays ₹518.77; charges ₹2.31 lakh)
2023-02-13  ORIENTPPR   SELL ₹14.97 crore at stop ₹39.90 (-12.7%, charges ₹1.55 lakh) — the cash goes back to work at the next Friday screen
2023-02-13  YESBANK     PYRAMID BUY ₹10.47 crore at ₹17.05 (box jump — doubling the stake with NEW capital; stop stays ₹15.34; charges ₹1.24 lakh)
2023-02-17  CGCL        SELL ₹46.65 lakh at stop ₹704.95 (-0.9%, charges ₹4,838.88) — the cash goes back to work at the next Friday screen
2023-02-20  ANUP        PYRAMID BUY ₹38.53 crore at ₹562.52 (box jump — doubling the stake with NEW capital; stop stays ₹527.27; charges ₹4.56 lakh)
2023-02-20  CIGNITITEC  BUY ₹24.17 crore at ₹731.95 (fresh Friday signal — BUY: 2.05× weekly, month 1.77×, ladder rising; stop ₹568.10; charges ₹2.86 lakh)
2023-02-22  USHAMART    SELL ₹10.30 crore at stop ₹166.25 (-18.1%, charges ₹1.07 lakh) — the cash goes back to work at the next Friday screen
2023-02-27  JSL         PYRAMID BUY ₹28.02 crore at ₹265.50 (box jump — doubling the stake with NEW capital; stop stays ₹235.03; charges ₹3.32 lakh)
2023-02-27  SONATSOFTW  BUY ₹13.82 crore at ₹360.00 (fresh Friday signal — BUY: 9.70× weekly, month 3.45×, ladder rising; stop ₹282.62; charges ₹1.64 lakh)
2023-03-06  CIGNITITEC  PYRAMID BUY ₹25.46 crore at ₹772.00 (box jump — doubling the stake with NEW capital; stop stays ₹659.30; charges ₹3.02 lakh)
2023-03-06  IOB         PYRAMID BUY ₹10.22 crore at ₹26.10 (box jump — doubling the stake with NEW capital; stop stays ₹22.18; charges ₹1.21 lakh)
2023-03-06  JINDALSAW   PYRAMID BUY ₹36.54 crore at ₹73.97 (box jump — doubling the stake with NEW capital; stop stays ₹67.92; charges ₹4.33 lakh)
2023-03-06  SONATSOFTW  PYRAMID BUY ₹15.37 crore at ₹400.75 (box jump — doubling the stake with NEW capital; stop stays ₹325.85; charges ₹1.82 lakh)
2023-03-10  ANUP        SELL ₹72.10 crore at stop ₹527.27 (-4.7%, charges ₹7.48 lakh) — the cash goes back to work at the next Friday screen
2023-03-13  YESBANK     SELL ₹18.80 crore at stop ₹15.34 (-19.1%, charges ₹1.95 lakh) — the cash goes back to work at the next Friday screen
2023-03-20  CIGNITITEC  PYRAMID BUY ₹50.77 crore at ₹770.05 (box jump — doubling the stake with NEW capital; stop stays ₹705.14; charges ₹6.02 lakh)
2023-03-20  IOB         SELL ₹17.35 crore at stop ₹22.18 (-24.2%, charges ₹1.80 lakh) — the cash goes back to work at the next Friday screen
2023-03-20  SONATSOFTW  PYRAMID BUY ₹30.46 crore at ₹397.50 (box jump — doubling the stake with NEW capital; stop stays ₹357.20; charges ₹3.61 lakh)
2023-03-27  JINDALSAW   SELL ₹66.99 crore at stop ₹67.92 (+5.1%, charges ₹6.95 lakh) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹48.37 crore at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹5.73 lakh)
2023-03-27  SONATSOFTW  PYRAMID BUY ₹63.37 crore at ₹413.70 (box jump — doubling the stake with NEW capital; stop stays ₹371.45; charges ₹7.51 lakh)
2023-03-29  CIGNITITEC  SELL ₹92.83 crore at stop ₹705.14 (-7.3%, charges ₹9.63 lakh) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹113.61 crore at stop ₹371.45 (-7.4%, charges ₹11.79 lakh) — the cash goes back to work at the next Friday screen
2023-04-03  CPSEETF     BUY ₹47.35 crore at ₹40.00 (fresh Friday signal — ACCUMULATE: 1.80× weekly, month 1.84×, ladder rising; stop ₹36.42; charges ₹5.61 lakh)
2023-04-03  HAL         BUY ₹47.34 crore at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹5.61 lakh)
2023-04-03  SETFGOLD    BUY ₹47.40 crore at ₹52.71 (fresh Friday signal — BUY: 3.16× weekly, month 1.65×, ladder rising; stop ₹48.56; charges ₹5.62 lakh)
2023-04-03  TAX         FY2023 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹45.71 crore / LT ₹0.00)
2023-04-10  JISLJALEQS  BUY ₹53.48 crore at ₹36.70 (fresh Friday signal — BUY: 1.61× weekly, month 2.06×, ladder rising; stop ₹27.65; charges ₹6.34 lakh)
2023-04-10  JSL         PYRAMID BUY ₹60.75 crore at ₹288.00 (box jump — doubling the stake with NEW capital; stop stays ₹256.98; charges ₹7.20 lakh)
2023-04-13  JSL         SELL ₹108.24 crore at stop ₹256.98 (-4.9%, charges ₹11.23 lakh) — the cash goes back to work at the next Friday screen
2023-04-17  SETFGOLD    PYRAMID BUY ₹47.60 crore at ₹53.00 (box jump — doubling the stake with NEW capital; stop stays ₹49.74; charges ₹5.64 lakh)
2023-04-24  ASHIANA     BUY ₹62.67 crore at ₹177.50 (fresh Friday signal — ACCUMULATE: 2.73× weekly, month 2.97×, ladder rising; stop ₹158.98; charges ₹7.42 lakh)
2023-04-24  FDC         BUY ₹62.45 crore at ₹287.20 (fresh Friday signal — BUY: 9.32× weekly, month 1.61×, ladder rising; stop ₹248.43; charges ₹7.40 lakh)
2023-04-24  JISLJALEQS  PYRAMID BUY ₹52.62 crore at ₹36.15 (box jump — doubling the stake with NEW capital; stop stays ₹32.63; charges ₹6.23 lakh)
2023-04-24  MARKSANS    BUY ₹62.60 crore at ₹78.00 (fresh Friday signal — ACCUMULATE: 1.64× weekly, month 1.51×, ladder rising; stop ₹71.87; charges ₹7.42 lakh)
2023-05-02  CPSEETF     PYRAMID BUY ₹48.98 crore at ₹41.43 (box jump — doubling the stake with NEW capital; stop stays ₹38.64; charges ₹5.80 lakh)
2023-05-02  GSFC        PYRAMID BUY ₹14.61 crore at ₹160.80 (box jump — doubling the stake with NEW capital; stop stays ₹116.04; charges ₹1.73 lakh)
2023-05-02  ICICIBANK   BUY ₹58.26 crore at ₹924.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.24×, ladder rising; stop ₹838.28; charges ₹6.90 lakh)
2023-05-02  KSB         PYRAMID BUY ₹52.41 crore at ₹453.40 (box jump — doubling the stake with NEW capital; stop stays ₹407.74; charges ₹6.21 lakh)
2023-05-08  FDC         PYRAMID BUY ₹65.04 crore at ₹299.50 (box jump — doubling the stake with NEW capital; stop stays ₹270.27; charges ₹7.71 lakh)
2023-05-15  HAL         PYRAMID BUY ₹51.18 crore at ₹1,493.47 (box jump — doubling the stake with NEW capital; stop stays ₹1,370.80; charges ₹6.06 lakh)
2023-05-15  JISLJALEQS  PYRAMID BUY ₹115.80 crore at ₹39.80 (box jump — doubling the stake with NEW capital; stop stays ₹37.15; charges ₹13.72 lakh)
2023-05-22  GSFC        PYRAMID BUY ₹30.53 crore at ₹168.05 (box jump — doubling the stake with NEW capital; stop stays ₹155.85; charges ₹3.62 lakh)
2023-05-22  JISLJALEQS  SELL ₹215.82 crore at stop ₹37.15 (-2.5%, charges ₹22.39 lakh) — the cash goes back to work at the next Friday screen
2023-05-22  MARKSANS    SELL ₹57.56 crore at stop ₹71.87 (-7.9%, charges ₹5.97 lakh) — the cash goes back to work at the next Friday screen
2023-05-29  ASHIANA     PYRAMID BUY ₹64.29 crore at ₹182.30 (box jump — doubling the stake with NEW capital; stop stays ₹165.16; charges ₹7.62 lakh)
2023-05-29  BALMLAWRIE  BUY ₹60.48 crore at ₹126.45 (fresh Friday signal — BUY: 7.38× weekly, month 1.80×, ladder rising; stop ₹116.71; charges ₹7.17 lakh)
2023-05-29  GSFC        SELL ₹56.53 crore at stop ₹155.85 (-2.2%, charges ₹5.86 lakh) — the cash goes back to work at the next Friday screen
2023-05-29  SCHNEIDER   BUY ₹106.41 crore at ₹236.80 (fresh Friday signal — BUY: 11.77× weekly, month 1.59×, ladder rising; stop ₹175.42; charges ₹12.61 lakh)
2023-05-29  THANGAMAYL  BUY ₹106.49 crore at ₹1,344.00 (fresh Friday signal — ACCUMULATE: 18.71× weekly, month 3.50×, ladder rising; stop ₹1,116.30; charges ₹12.62 lakh)
2023-06-05  BALMLAWRIE  PYRAMID BUY ₹62.96 crore at ₹131.80 (box jump — doubling the stake with NEW capital; stop stays ₹118.04; charges ₹7.46 lakh)
2023-06-05  CPSEETF     PYRAMID BUY ₹99.82 crore at ₹42.24 (box jump — doubling the stake with NEW capital; stop stays ₹39.05; charges ₹11.83 lakh)
2023-06-05  HAL         PYRAMID BUY ₹109.03 crore at ₹1,591.88 (box jump — doubling the stake with NEW capital; stop stays ₹1,415.36; charges ₹12.92 lakh)
2023-06-05  ICICIBANK   PYRAMID BUY ₹59.39 crore at ₹943.00 (box jump — doubling the stake with NEW capital; stop stays ₹886.30; charges ₹7.04 lakh)
2023-06-12  ASHIANA     PYRAMID BUY ₹135.16 crore at ₹191.75 (box jump — doubling the stake with NEW capital; stop stays ₹172.90; charges ₹16.01 lakh)
2023-06-12  THANGAMAYL  PYRAMID BUY ₹113.94 crore at ₹1,439.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,344.25; charges ₹13.50 lakh)
2023-06-19  BALMLAWRIE  PYRAMID BUY ₹131.82 crore at ₹138.05 (box jump — doubling the stake with NEW capital; stop stays ₹124.83; charges ₹15.62 lakh)
2023-06-19  HAL         PYRAMID BUY ₹266.89 crore at ₹1,949.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,723.32; charges ₹31.62 lakh)
2023-06-19  SCHNEIDER   PYRAMID BUY ₹110.86 crore at ₹247.00 (box jump — doubling the stake with NEW capital; stop stays ₹223.11; charges ₹13.13 lakh)
2023-06-26  FDC         PYRAMID BUY ₹136.80 crore at ₹315.15 (box jump — doubling the stake with NEW capital; stop stays ₹289.61; charges ₹16.21 lakh)
2023-07-03  BALMLAWRIE  PYRAMID BUY ₹261.76 crore at ₹137.15 (box jump — doubling the stake with NEW capital; stop stays ₹128.77; charges ₹31.01 lakh)
2023-07-10  ASHIANA     PYRAMID BUY ₹281.77 crore at ₹200.00 (box jump — doubling the stake with NEW capital; stop stays ₹178.84; charges ₹33.39 lakh)
2023-07-10  CPSEETF     PYRAMID BUY ₹217.28 crore at ₹46.00 (box jump — doubling the stake with NEW capital; stop stays ₹40.77; charges ₹25.74 lakh)
2023-07-10  FDC         PYRAMID BUY ₹294.48 crore at ₹339.40 (box jump — doubling the stake with NEW capital; stop stays ₹291.22; charges ₹34.89 lakh)
2023-07-10  SCHNEIDER   PYRAMID BUY ₹251.14 crore at ₹279.95 (box jump — doubling the stake with NEW capital; stop stays ₹245.91; charges ₹29.76 lakh)
2023-07-12  KSB         SELL ₹94.11 crore at stop ₹407.74 (-6.4%, charges ₹9.76 lakh) — the cash goes back to work at the next Friday screen
2023-07-17  SCHNEIDER   PYRAMID BUY ₹509.25 crore at ₹284.00 (box jump — doubling the stake with NEW capital; stop stays ₹255.17; charges ₹60.34 lakh)
2023-07-17  THANGAMAYL  SELL ₹212.42 crore at stop ₹1,344.25 (-3.4%, charges ₹22.03 lakh) — the cash goes back to work at the next Friday screen
2023-07-24  ICICIBANK   PYRAMID BUY ₹126.50 crore at ₹1,004.95 (box jump — doubling the stake with NEW capital; stop stays ₹894.19; charges ₹14.99 lakh)
2023-07-24  TFCILTD     BUY ₹363.06 crore at ₹17.11 (fresh Friday signal — BUY: 11.34× weekly, month 1.82×, ladder rising; stop ₹14.54; charges ₹43.02 lakh)
2023-07-31  CPSEETF     SELL ₹395.84 crore at stop ₹41.97 (-4.0%, charges ₹41.06 lakh) — the cash goes back to work at the next Friday screen
2023-07-31  TFCILTD     PYRAMID BUY ₹371.11 crore at ₹17.51 (box jump — doubling the stake with NEW capital; stop stays ₹15.52; charges ₹43.97 lakh)
2023-08-07  UFO         BUY ₹395.84 crore at ₹98.00 (fresh Friday signal — BUY: 9.42× weekly, month 3.46×, ladder rising; stop ₹74.53; charges ₹46.90 lakh)
2023-08-14  TFCILTD     PYRAMID BUY ₹822.27 crore at ₹19.41 (box jump — doubling the stake with NEW capital; stop stays ₹15.84; charges ₹97.42 lakh)
2023-08-14  UFO         PYRAMID BUY ₹391.33 crore at ₹97.00 (box jump — doubling the stake with NEW capital; stop stays ₹87.73; charges ₹46.37 lakh)
2023-08-21  ICICIBANK   PYRAMID BUY ₹239.20 crore at ₹950.70 (box jump — doubling the stake with NEW capital; stop stays ₹898.70; charges ₹28.34 lakh)
2023-08-28  TFCILTD     PYRAMID BUY ₹1,690.14 crore at ₹19.96 (box jump — doubling the stake with NEW capital; stop stays ₹17.98; charges ₹2.00 crore)
2023-10-03  SETFGOLD    SELL ₹89.20 crore at stop ₹49.74 (-5.9%, charges ₹9.25 lakh) — the cash goes back to work at the next Friday screen
2023-10-09  BALMLAWRIE  SELL ₹542.07 crore at stop ₹142.24 (+5.1%, charges ₹56.23 lakh) — the cash goes back to work at the next Friday screen
2023-10-16  SEQUENT     BUY ₹631.28 crore at ₹103.80 (fresh Friday signal — ACCUMULATE: 5.39× weekly, month 1.98×, ladder rising; stop ₹82.25; charges ₹74.80 lakh)
2023-10-23  FDC         SELL ₹614.98 crore at stop ₹354.97 (+10.3%, charges ₹63.79 lakh) — the cash goes back to work at the next Friday screen
2023-10-23  SCHNEIDER   SELL ₹1,129.45 crore at stop ₹315.45 (+15.8%, charges ₹1.17 crore) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹503.18 crore at stop ₹1,840.70 (+6.3%, charges ₹52.19 lakh) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹875.72 crore at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹1.04 crore)
2023-10-30  MANGLMCEM   BUY ₹877.07 crore at ₹399.95 (fresh Friday signal — BUY: 1.77× weekly, month 1.50×, ladder rising; stop ₹333.88; charges ₹1.04 crore)
2023-10-30  SEQUENT     PYRAMID BUY ₹617.77 crore at ₹101.70 (box jump — doubling the stake with NEW capital; stop stays ₹83.77; charges ₹73.20 lakh)
2023-11-06  GEOJITFSL   BUY ₹494.81 crore at ₹65.10 (fresh Friday signal — BUY: 10.04× weekly, month 6.76×, ladder rising; stop ₹47.89; charges ₹58.63 lakh)
2023-11-13  GEOJITFSL   PYRAMID BUY ₹506.75 crore at ₹66.75 (box jump — doubling the stake with NEW capital; stop stays ₹59.85; charges ₹60.04 lakh)
2023-11-20  MANGLMCEM   PYRAMID BUY ₹922.80 crore at ₹421.30 (box jump — doubling the stake with NEW capital; stop stays ₹388.55; charges ₹1.09 crore)
2023-11-28  CUPID       PYRAMID BUY ₹1,275.56 crore at ₹176.44 (box jump — doubling the stake with NEW capital; stop stays ₹158.66; charges ₹1.51 crore)
2023-12-11  GEOJITFSL   PYRAMID BUY ₹1,040.97 crore at ₹68.60 (box jump — doubling the stake with NEW capital; stop stays ₹63.22; charges ₹1.23 crore)
2023-12-18  MANGLMCEM   PYRAMID BUY ₹2,775.73 crore at ₹634.00 (box jump — doubling the stake with NEW capital; stop stays ₹464.55; charges ₹3.29 crore)
2023-12-18  UFO         PYRAMID BUY ₹914.05 crore at ₹113.35 (box jump — doubling the stake with NEW capital; stop stays ₹100.70; charges ₹1.08 crore)
2023-12-26  MANGLMCEM   PYRAMID BUY ₹6,160.74 crore at ₹704.00 (box jump — doubling the stake with NEW capital; stop stays ₹579.98; charges ₹7.30 crore)
2024-01-01  GEOJITFSL   PYRAMID BUY ₹2,387.06 crore at ₹78.70 (box jump — doubling the stake with NEW capital; stop stays ₹68.78; charges ₹2.83 crore)
2024-01-01  SEQUENT     PYRAMID BUY ₹1,387.80 crore at ₹114.30 (box jump — doubling the stake with NEW capital; stop stays ₹102.69; charges ₹1.64 crore)
2024-01-23  UFO         PYRAMID BUY ₹2,262.21 crore at ₹140.35 (box jump — doubling the stake with NEW capital; stop stays ₹120.13; charges ₹2.68 crore)
2024-01-29  SEQUENT     PYRAMID BUY ₹3,276.33 crore at ₹135.00 (box jump — doubling the stake with NEW capital; stop stays ₹120.65; charges ₹3.88 crore)
2024-03-06  SEQUENT     SELL ₹5,846.60 crore at stop ₹120.65 (-0.9%, charges ₹6.06 crore) — the cash goes back to work at the next Friday screen
2024-03-11  GEOJITFSL   SELL ₹4,167.37 crore at stop ₹68.81 (-5.7%, charges ₹4.32 crore) — the cash goes back to work at the next Friday screen
2024-03-11  SOLARINDS   BUY ₹3,831.49 crore at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹4.54 crore)
2024-03-12  UFO         SELL ₹4,049.42 crore at stop ₹125.82 (+2.4%, charges ₹4.20 crore) — the cash goes back to work at the next Friday screen
2024-03-13  ASHIANA     SELL ₹763.80 crore at stop ₹271.51 (+40.7%, charges ₹79.23 lakh) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹3,627.94 crore at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹4.30 crore)
2024-03-18  FORCEMOT    BUY ₹3,611.58 crore at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹4.28 crore)
2024-03-18  INDIGO      BUY ₹3,606.47 crore at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹4.27 crore)
2024-03-20  TFCILTD     SELL ₹5,647.16 crore at stop ₹33.40 (+74.3%, charges ₹5.86 crore) — the cash goes back to work at the next Friday screen
2024-03-26  BOSCHLTD    PYRAMID BUY ₹3,715.15 crore at ₹30,245.00 (box jump — doubling the stake with NEW capital; stop stays ₹26,710.20; charges ₹4.40 crore)
2024-03-26  SADBHAV     BUY ₹4,172.02 crore at ₹25.85 (fresh Friday signal — ACCUMULATE: 1.84× weekly, month 2.30×, ladder rising; stop ₹19.13; charges ₹4.94 crore)
2024-04-01  SOLARINDS   PYRAMID BUY ₹4,528.18 crore at ₹8,950.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,980.95; charges ₹5.37 crore)
2024-04-01  TAX         FY2024 settled: ₹517.73 crore paid (STCG ₹2,588.64 crore @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-08  BOSCHLTD    PYRAMID BUY ₹7,606.36 crore at ₹30,980.00 (box jump — doubling the stake with NEW capital; stop stays ₹28,244.40; charges ₹9.01 crore)
2024-04-15  INDIGO      PYRAMID BUY ₹4,131.61 crore at ₹3,670.30 (box jump — doubling the stake with NEW capital; stop stays ₹3,287.00; charges ₹4.90 crore)
2024-04-15  SADBHAV     PYRAMID BUY ₹5,319.68 crore at ₹33.00 (box jump — doubling the stake with NEW capital; stop stays ₹30.68; charges ₹6.30 crore)
2024-04-18  SADBHAV     SELL ₹9,875.27 crore at stop ₹30.68 (+4.3%, charges ₹10.24 crore) — the cash goes back to work at the next Friday screen
2024-04-22  GOLDSHARE   BUY ₹4,395.38 crore at ₹62.45 (fresh Friday signal — BUY: 3.30× weekly, month 7.13×, ladder rising; stop ₹53.01; charges ₹5.21 crore)
2024-04-22  JUSTDIAL    BUY ₹6,587.00 crore at ₹1,084.00 (fresh Friday signal — BUY: 11.71× weekly, month 3.19×, ladder rising; stop ₹821.08; charges ₹7.80 crore)
2024-04-29  FORCEMOT    PYRAMID BUY ₹5,547.42 crore at ₹10,100.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,483.47; charges ₹6.57 crore)
2024-04-29  GOLDSHARE   PYRAMID BUY ₹4,379.63 crore at ₹62.30 (box jump — doubling the stake with NEW capital; stop stays ₹57.09; charges ₹5.19 crore)
2024-05-06  JUSTDIAL    PYRAMID BUY ₹6,706.65 crore at ₹1,105.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,008.00; charges ₹7.95 crore)
2024-05-09  JUSTDIAL    SELL ₹12,215.93 crore at stop ₹1,008.00 (-7.9%, charges ₹12.67 crore) — the cash goes back to work at the next Friday screen
2024-05-13  CENTURYTEX  BUY ₹9,112.44 crore at ₹2,000.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 1.97×, ladder rising; stop ₹1,715.70; charges ₹10.80 crore)
2024-05-13  INDIGO      PYRAMID BUY ₹9,013.89 crore at ₹4,006.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,719.77; charges ₹10.68 crore)
2024-05-21  FORCEMOT    PYRAMID BUY ₹9,866.91 crore at ₹8,987.50 (box jump — doubling the stake with NEW capital; stop stays ₹8,083.64; charges ₹11.69 crore)
2024-05-27  BOSCHLTD    PYRAMID BUY ₹15,164.94 crore at ₹30,901.00 (box jump — doubling the stake with NEW capital; stop stays ₹29,015.09; charges ₹17.97 crore)
2024-05-28  FORCEMOT    SELL ₹17,720.32 crore at stop ₹8,083.64 (-6.7%, charges ₹18.38 crore) — the cash goes back to work at the next Friday screen
2024-06-03  JCHAC       BUY ₹9,153.83 crore at ₹1,900.00 (fresh Friday signal — BUY: 7.52× weekly, month 3.77×, ladder rising; stop ₹1,103.95; charges ₹10.85 crore)
2024-06-03  THERMAX     BUY ₹11,669.97 crore at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹13.83 crore)
2024-06-04  BOSCHLTD    SELL ₹28,432.47 crore at stop ₹29,015.09 (-5.4%, charges ₹29.49 crore) — the cash goes back to work at the next Friday screen
2024-06-04  CENTURYTEX  SELL ₹7,799.76 crore at stop ₹1,715.70 (-14.2%, charges ₹8.09 crore) — the cash goes back to work at the next Friday screen
2024-06-04  MANGLMCEM   SELL ₹13,910.74 crore at stop ₹796.10 (+29.9%, charges ₹14.43 crore) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹8,062.65 crore at stop ₹7,980.95 (-3.3%, charges ₹8.36 crore) — the cash goes back to work at the next Friday screen
2024-06-05  ICICIBANK   SELL ₹528.19 crore at stop ₹1,051.37 (+9.5%, charges ₹54.79 lakh) — the cash goes back to work at the next Friday screen
2024-06-10  BANKBEES    BUY ₹13,014.61 crore at ₹514.99 (fresh Friday signal — BUY: 4.22× weekly, month 1.96×, ladder rising; stop ₹457.43; charges ₹15.42 crore)
2024-06-10  DABUR       BUY ₹6,595.91 crore at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹7.81 crore)
2024-06-10  INDIGO      PYRAMID BUY ₹19,779.64 crore at ₹4,398.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,805.04; charges ₹23.44 crore)
2024-06-10  MATRIMONY   BUY ₹13,061.77 crore at ₹643.50 (fresh Friday signal — BUY: 5.35× weekly, month 1.60×, ladder rising; stop ₹496.18; charges ₹15.48 crore)
2024-06-10  NIFTYBEES   BUY ₹12,997.47 crore at ₹259.45 (fresh Friday signal — BUY: 4.16× weekly, month 2.61×, ladder rising; stop ₹229.24; charges ₹15.40 crore)
2024-06-10  UTINIFTETF  BUY ₹13,064.05 crore at ₹251.07 (fresh Friday signal — BUY: 10.56× weekly, month 3.19×, ladder rising; stop ₹222.42; charges ₹15.48 crore)
2024-06-18  DABUR       PYRAMID BUY ₹6,630.62 crore at ₹608.10 (box jump — doubling the stake with NEW capital; stop stays ₹552.95; charges ₹7.86 crore)
2024-06-18  NIFTYBEES   PYRAMID BUY ₹13,043.61 crore at ₹260.68 (box jump — doubling the stake with NEW capital; stop stays ₹230.02; charges ₹15.45 crore)
2024-06-18  THERMAX     PYRAMID BUY ₹11,196.10 crore at ₹5,417.40 (box jump — doubling the stake with NEW capital; stop stays ₹4,719.70; charges ₹13.27 crore)
2024-06-18  UTINIFTETF  PYRAMID BUY ₹13,102.62 crore at ₹252.11 (box jump — doubling the stake with NEW capital; stop stays ₹224.49; charges ₹15.52 crore)
2024-06-24  MATRIMONY   PYRAMID BUY ₹12,672.24 crore at ₹625.05 (box jump — doubling the stake with NEW capital; stop stays ₹564.77; charges ₹15.01 crore)
2024-07-01  JCHAC       PYRAMID BUY ₹9,571.26 crore at ₹1,989.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,710.00; charges ₹11.34 crore)
2024-07-08  BANKBEES    PYRAMID BUY ₹13,604.74 crore at ₹538.98 (box jump — doubling the stake with NEW capital; stop stays ₹507.06; charges ₹16.12 crore)
2024-07-15  NIFTYBEES   PYRAMID BUY ₹27,153.93 crore at ₹271.50 (box jump — doubling the stake with NEW capital; stop stays ₹255.69; charges ₹32.17 crore)
2024-07-22  JCHAC       PYRAMID BUY ₹18,477.12 crore at ₹1,921.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,795.83; charges ₹21.89 crore)
2024-07-23  MATRIMONY   SELL ₹22,862.97 crore at stop ₹564.77 (-11.0%, charges ₹23.72 crore) — the cash goes back to work at the next Friday screen
2024-07-29  THYROCARE   BUY ₹22,862.97 crore at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹27.09 crore)
2024-07-29  UTINIFTETF  PYRAMID BUY ₹28,328.65 crore at ₹272.70 (box jump — doubling the stake with NEW capital; stop stays ₹248.19; charges ₹33.56 crore)
2024-08-05  DABUR       PYRAMID BUY ₹13,403.76 crore at ₹615.00 (box jump — doubling the stake with NEW capital; stop stays ₹587.15; charges ₹15.88 crore)
2024-08-05  THERMAX     SELL ₹19,476.58 crore at stop ₹4,719.70 (-14.6%, charges ₹20.20 crore) — the cash goes back to work at the next Friday screen
2024-08-05  THYROCARE   PYRAMID BUY ₹23,270.79 crore at ₹799.95 (box jump — doubling the stake with NEW capital; stop stays ₹729.50; charges ₹27.57 crore)
2024-08-12  BASF        BUY ₹19,476.58 crore at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹23.08 crore)
2024-08-26  BASF        PYRAMID BUY ₹17,643.13 crore at ₹6,666.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,894.80; charges ₹20.90 crore)
2024-09-09  THYROCARE   PYRAMID BUY ₹49,148.02 crore at ₹845.25 (box jump — doubling the stake with NEW capital; stop stays ₹796.15; charges ₹58.23 crore)
2024-09-16  DABUR       PYRAMID BUY ₹28,752.01 crore at ₹660.00 (box jump — doubling the stake with NEW capital; stop stays ₹602.49; charges ₹34.07 crore)
2024-09-16  NIFTYBEES   PYRAMID BUY ₹56,674.61 crore at ₹283.50 (box jump — doubling the stake with NEW capital; stop stays ₹262.66; charges ₹67.15 crore)
2024-09-23  UTINIFTETF  PYRAMID BUY ₹58,216.35 crore at ₹280.37 (box jump — doubling the stake with NEW capital; stop stays ₹256.51; charges ₹68.98 crore)
2024-10-03  DABUR       SELL ₹52,407.86 crore at stop ₹602.49 (-5.2%, charges ₹54.36 crore) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹52,407.86 crore at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹62.09 crore)
2024-10-07  INDIGO      SELL ₹40,277.41 crore at stop ₹4,485.14 (+10.5%, charges ₹41.78 crore) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹92,435.36 crore at stop ₹796.15 (-2.8%, charges ₹95.88 crore) — the cash goes back to work at the next Friday screen
2024-10-14  BASF        PYRAMID BUY ₹43,512.99 crore at ₹8,225.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,611.30; charges ₹51.56 crore)
2024-10-14  BSE         BUY ₹63,171.22 crore at ₹4,536.00 (fresh Friday signal — BUY: 2.79× weekly, month 4.25×, ladder rising; stop ₹3,393.93; charges ₹74.85 crore)
2024-10-14  DBCORP      BUY ₹63,418.07 crore at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹75.14 crore)
2024-10-14  JCHAC       PYRAMID BUY ₹49,319.40 crore at ₹2,565.30 (box jump — doubling the stake with NEW capital; stop stays ₹2,041.43; charges ₹58.43 crore)
2024-10-22  BASF        SELL ₹80,401.52 crore at stop ₹7,611.30 (-0.1%, charges ₹83.40 crore) — the cash goes back to work at the next Friday screen
2024-10-23  JCHAC       SELL ₹90,678.81 crore at stop ₹2,362.13 (+5.0%, charges ₹94.06 crore) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹54,303.42 crore at stop ₹302.08 (-14.2%, charges ₹56.33 crore) — the cash goes back to work at the next Friday screen
2024-10-28  CARERATING  BUY ₹59,367.29 crore at ₹1,396.00 (fresh Friday signal — BUY: 7.47× weekly, month 3.86×, ladder rising; stop ₹1,066.23; charges ₹70.34 crore)
2024-10-28  CUPID       SELL ₹2,290.30 crore at stop ₹158.66 (+6.7%, charges ₹2.38 crore) — the cash goes back to work at the next Friday screen
2024-11-04  63MOONS     BUY ₹67,006.78 crore at ₹595.00 (fresh Friday signal — BUY: 2.09× weekly, month 4.03×, ladder rising; stop ₹404.18; charges ₹158.18 crore)
2024-11-04  AKZOINDIA   BUY ₹67,373.11 crore at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹159.04 crore)
2024-11-04  AXISGOLD    BUY ₹40,050.34 crore at ₹69.05 (fresh Friday signal — BUY: 2.01× weekly, month 2.88×, ladder rising; stop ₹60.85; charges ₹94.54 crore)
2024-11-04  BSE         PYRAMID BUY ₹61,816.64 crore at ₹4,444.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,694.81; charges ₹145.93 crore)
2024-11-04  GOLDSHARE   PYRAMID BUY ₹9,407.47 crore at ₹66.95 (box jump — doubling the stake with NEW capital; stop stays ₹62.46; charges ₹22.21 crore)
2024-11-11  ASTRAZEN    PYRAMID BUY ₹51,694.14 crore at ₹7,350.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,854.77; charges ₹122.03 crore)
2024-11-13  UTINIFTETF  SELL ₹1.06 lakh crore at stop ₹256.51 (-5.4%, charges ₹235.94 crore) — the cash goes back to work at the next Friday screen
2024-11-14  ASTRAZEN    SELL ₹96,094.92 crore at stop ₹6,854.77 (-7.3%, charges ₹213.44 crore) — the cash goes back to work at the next Friday screen
2024-11-14  GOLDSHARE   SELL ₹17,493.54 crore at stop ₹62.46 (-3.4%, charges ₹38.86 crore) — the cash goes back to work at the next Friday screen
2024-11-14  NIFTYBEES   SELL ₹1.05 lakh crore at stop ₹262.66 (-4.4%, charges ₹232.60 crore) — the cash goes back to work at the next Friday screen
2024-11-18  SASKEN      BUY ₹69,621.39 crore at ₹2,015.25 (fresh Friday signal — BUY: 9.07× weekly, month 2.15×, ladder rising; stop ₹1,640.65; charges ₹164.35 crore)
2024-11-25  63MOONS     PYRAMID BUY ₹67,298.01 crore at ₹599.00 (box jump — doubling the stake with NEW capital; stop stays ₹523.12; charges ₹158.87 crore)
2024-11-25  GARFIBRES   BUY ₹77,050.19 crore at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹181.89 crore)
2024-12-02  CARERATING  PYRAMID BUY ₹64,525.78 crore at ₹1,519.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,239.70; charges ₹152.32 crore)
2024-12-02  GANECOS     BUY ₹92,703.39 crore at ₹2,418.80 (fresh Friday signal — ACCUMULATE: 2.21× weekly, month 1.58×, ladder rising; stop ₹1,751.78; charges ₹218.84 crore)
2024-12-02  GARFIBRES   PYRAMID BUY ₹75,260.18 crore at ₹936.00 (box jump — doubling the stake with NEW capital; stop stays ₹829.35; charges ₹177.66 crore)
2024-12-02  SWANENERGY  BUY ₹85,160.64 crore at ₹608.00 (fresh Friday signal — BUY: 1.83× weekly, month 1.52×, ladder rising; stop ₹449.22; charges ₹201.03 crore)
2024-12-09  AKZOINDIA   PYRAMID BUY ₹55,322.92 crore at ₹3,718.70 (box jump — doubling the stake with NEW capital; stop stays ₹3,423.18; charges ₹130.60 crore)
2024-12-09  SASKEN      PYRAMID BUY ₹77,168.74 crore at ₹2,239.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,993.24; charges ₹182.17 crore)
2024-12-09  SWANENERGY  PYRAMID BUY ₹1.01 lakh crore at ₹725.95 (box jump — doubling the stake with NEW capital; stop stays ₹574.13; charges ₹239.47 crore)
2024-12-23  63MOONS     PYRAMID BUY ₹2.25 lakh crore at ₹1,002.40 (box jump — doubling the stake with NEW capital; stop stays ₹790.40; charges ₹531.08 crore)
2024-12-27  AKZOINDIA   SELL ₹1.02 lakh crore at stop ₹3,423.18 (-16.9%, charges ₹225.46 crore) — the cash goes back to work at the next Friday screen
2025-01-06  BSE         PYRAMID BUY ₹1.49 lakh crore at ₹5,350.00 (box jump — doubling the stake with NEW capital; stop stays ₹4,954.63; charges ₹350.94 crore)
2025-01-06  CAMLINFINE  BUY ₹1.02 lakh crore at ₹137.04 (fresh Friday signal — BUY: 3.44× weekly, month 1.90×, ladder rising; stop ₹109.44; charges ₹239.62 crore)
2025-01-06  SWANENERGY  PYRAMID BUY ₹2.11 lakh crore at ₹755.05 (box jump — doubling the stake with NEW capital; stop stays ₹671.32; charges ₹497.54 crore)
2025-01-08  BANKBEES    SELL ₹25,526.19 crore at stop ₹507.06 (-3.8%, charges ₹56.70 crore) — the cash goes back to work at the next Friday screen
2025-01-09  GARFIBRES   SELL ₹1.33 lakh crore at stop ₹829.35 (-12.3%, charges ₹295.23 crore) — the cash goes back to work at the next Friday screen
2025-01-09  SWANENERGY  SELL ₹3.74 lakh crore at stop ₹671.32 (-5.6%, charges ₹829.63 crore) — the cash goes back to work at the next Friday screen
2025-01-10  GANECOS     SELL ₹66,832.12 crore at stop ₹1,751.78 (-27.6%, charges ₹148.44 crore) — the cash goes back to work at the next Friday screen
2025-01-13  CAMLINFINE  PYRAMID BUY ₹92,444.43 crore at ₹125.10 (box jump — doubling the stake with NEW capital; stop stays ₹120.37; charges ₹218.23 crore)
2025-01-13  CAMLINFINE  SELL ₹1.77 lakh crore at stop ₹120.37 (-8.2%, charges ₹393.80 crore) — the cash goes back to work at the next Friday screen
2025-01-13  CARERATING  SELL ₹1.05 lakh crore at stop ₹1,239.70 (-14.9%, charges ₹233.13 crore) — the cash goes back to work at the next Friday screen
2025-01-21  SASKEN      SELL ₹1.37 lakh crore at stop ₹1,993.24 (-6.3%, charges ₹304.14 crore) — the cash goes back to work at the next Friday screen
2025-01-22  63MOONS     SELL ₹3.54 lakh crore at stop ₹790.40 (-1.1%, charges ₹785.36 crore) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹1.71 lakh crore at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹404.39 crore)
2025-02-03  ZENSARTECH  BUY ₹1.75 lakh crore at ₹947.00 (fresh Friday signal — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹412.11 crore)
2025-02-17  SETFGOLD    BUY ₹1.71 lakh crore at ₹76.80 (fresh Friday signal — BUY: 1.62× weekly, month 1.57×, ladder rising; stop ₹59.71; charges ₹403.98 crore)
2025-02-24  SETFGOLD    PYRAMID BUY ₹1.67 lakh crore at ₹74.99 (box jump — doubling the stake with NEW capital; stop stays ₹69.36; charges ₹393.53 crore)
2025-02-28  BSE         SELL ₹2.74 lakh crore at stop ₹4,954.63 (+0.7%, charges ₹609.52 crore) — the cash goes back to work at the next Friday screen
2025-03-03  AXISGOLD    PYRAMID BUY ₹41,795.91 crore at ₹72.23 (box jump — doubling the stake with NEW capital; stop stays ₹67.36; charges ₹98.67 crore)
2025-03-03  NH          BUY ₹1.85 lakh crore at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹436.40 crore)
2025-03-03  ZENSARTECH  SELL ₹1.34 lakh crore at stop ₹727.84 (-23.1%, charges ₹296.66 crore) — the cash goes back to work at the next Friday screen
2025-03-10  CREDITACC   PYRAMID BUY ₹1.95 lakh crore at ₹968.75 (box jump — doubling the stake with NEW capital; stop stays ₹837.38; charges ₹459.79 crore)
2025-03-17  AVANTIFEED  BUY ₹2.27 lakh crore at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹535.91 crore)
2025-03-17  NH          PYRAMID BUY ₹1.93 lakh crore at ₹1,521.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,436.97; charges ₹456.68 crore)
2025-04-01  TAX         FY2025 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹2.07 lakh crore / LT ₹0.00)
2025-04-07  AVANTIFEED  SELL ₹1.74 lakh crore at stop ₹648.95 (-23.0%, charges ₹386.61 crore) — the cash goes back to work at the next Friday screen
2025-04-07  GOLDBEES    BUY ₹2.27 lakh crore at ₹74.60 (fresh Friday signal — BUY: 1.78× weekly, month 1.67×, ladder rising; stop ₹68.93; charges ₹536.56 crore)
2025-04-07  SETFGOLD    SELL ₹3.07 lakh crore at stop ₹69.36 (-8.6%, charges ₹682.63 crore) — the cash goes back to work at the next Friday screen
2025-04-07  VADILALIND  BUY ₹2.26 lakh crore at ₹4,820.55 (fresh Friday signal — BUY: 9.88× weekly, month 5.69×, ladder rising; stop ₹4,255.30; charges ₹533.85 crore)
2025-04-15  AVANTIFEED  BUY ₹2.60 lakh crore at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹614.03 crore)
2025-04-15  VADILALIND  PYRAMID BUY ₹2.76 lakh crore at ₹5,898.90 (box jump — doubling the stake with NEW capital; stop stays ₹4,500.03; charges ₹651.73 crore)
2025-04-28  FORCEMOT    BUY ₹2.78 lakh crore at ₹9,275.00 (fresh Friday signal — ACCUMULATE: 2.06× weekly, month 1.62×, ladder rising; stop ₹7,647.50; charges ₹655.95 crore)
2025-04-28  WHIRLPOOL   BUY ₹2.77 lakh crore at ₹1,153.90 (fresh Friday signal — BUY: 2.21× weekly, month 1.77×, ladder rising; stop ₹1,017.54; charges ₹653.51 crore)
2025-05-12  AXISGOLD    PYRAMID BUY ₹96,717.04 crore at ₹83.67 (box jump — doubling the stake with NEW capital; stop stays ₹74.30; charges ₹228.31 crore)
2025-05-12  CREDITACC   PYRAMID BUY ₹4.61 lakh crore at ₹1,148.60 (box jump — doubling the stake with NEW capital; stop stays ₹1,019.35; charges ₹1,089.03 crore)
2025-05-12  GOLDBEES    PYRAMID BUY ₹2.41 lakh crore at ₹79.38 (box jump — doubling the stake with NEW capital; stop stays ₹73.49; charges ₹569.59 crore)
2025-05-12  NH          PYRAMID BUY ₹4.65 lakh crore at ₹1,829.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,641.69; charges ₹1,097.03 crore)
2025-05-19  FORCEMOT    PYRAMID BUY ₹3.27 lakh crore at ₹10,954.50 (box jump — doubling the stake with NEW capital; stop stays ₹8,910.52; charges ₹772.90 crore)
2025-05-19  VADILALIND  PYRAMID BUY ₹6.36 lakh crore at ₹6,805.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,401.40; charges ₹1,501.90 crore)
2025-05-19  WHIRLPOOL   PYRAMID BUY ₹3.14 lakh crore at ₹1,311.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,111.50; charges ₹740.73 crore)
2025-05-30  VADILALIND  SELL ₹10.07 lakh crore at stop ₹5,401.40 (-11.2%, charges ₹2,235.73 crore) — the cash goes back to work at the next Friday screen
2025-06-02  CREDITACC   PYRAMID BUY ₹9.15 lakh crore at ₹1,140.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,029.71; charges ₹2,159.19 crore)
2025-06-02  FORCEMOT    PYRAMID BUY ₹7.61 lakh crore at ₹12,742.00 (box jump — doubling the stake with NEW capital; stop stays ₹9,650.58; charges ₹1,795.90 crore)
2025-06-02  LUMAXIND    BUY ₹6.73 lakh crore at ₹2,989.50 (fresh Friday signal — BUY: 7.29× weekly, month 1.54×, ladder rising; stop ₹2,531.37; charges ₹1,588.77 crore)
2025-06-02  RPOWER      BUY ₹3.97 lakh crore at ₹58.64 (fresh Friday signal — BUY: 5.25× weekly, month 1.98×, ladder rising; stop ₹47.24; charges ₹937.93 crore)
2025-06-09  AXISGOLD    PYRAMID BUY ₹1.84 lakh crore at ₹79.72 (box jump — doubling the stake with NEW capital; stop stays ₹75.36; charges ₹434.56 crore)
2025-06-09  GOLDBEES    PYRAMID BUY ₹4.91 lakh crore at ₹80.82 (box jump — doubling the stake with NEW capital; stop stays ₹74.70; charges ₹1,158.48 crore)
2025-06-09  LUMAXIND    PYRAMID BUY ₹7.14 lakh crore at ₹3,180.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,614.49; charges ₹1,686.02 crore)
2025-06-23  FORCEMOT    PYRAMID BUY ₹16.91 lakh crore at ₹14,179.00 (box jump — doubling the stake with NEW capital; stop stays ₹11,433.25; charges ₹3,992.16 crore)
2025-06-23  LUMAXIND    PYRAMID BUY ₹14.20 lakh crore at ₹3,164.90 (box jump — doubling the stake with NEW capital; stop stays ₹2,954.12; charges ₹3,352.06 crore)
2025-06-23  WHIRLPOOL   PYRAMID BUY ₹6.36 lakh crore at ₹1,331.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,233.96; charges ₹1,502.28 crore)
2025-06-30  NH          PYRAMID BUY ₹11.29 lakh crore at ₹2,225.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,763.87; charges ₹2,665.94 crore)
2025-07-07  GOLDBEES    PYRAMID BUY ₹9.81 lakh crore at ₹80.90 (box jump — doubling the stake with NEW capital; stop stays ₹75.56; charges ₹2,316.51 crore)
2025-07-07  WHIRLPOOL   PYRAMID BUY ₹13.15 lakh crore at ₹1,377.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,301.97; charges ₹3,104.72 crore)
2025-07-14  LUMAXIND    PYRAMID BUY ₹31.74 lakh crore at ₹3,541.50 (box jump — doubling the stake with NEW capital; stop stays ₹3,319.20; charges ₹7,493.01 crore)
2025-08-04  NH          SELL ₹18.36 lakh crore at stop ₹1,814.78 (-6.5%, charges ₹4,077.98 crore) — the cash goes back to work at the next Friday screen
2025-08-07  WHIRLPOOL   SELL ₹24.79 lakh crore at stop ₹1,301.97 (-2.1%, charges ₹5,505.43 crore) — the cash goes back to work at the next Friday screen
2025-08-08  LUMAXIND    SELL ₹59.30 lakh crore at stop ₹3,319.20 (-0.4%, charges ₹13,170.54 crore) — the cash goes back to work at the next Friday screen
2025-08-11  BLISSGVS    BUY ₹19.52 lakh crore at ₹178.60 (fresh Friday signal — BUY: 1.52× weekly, month 1.82×, ladder rising; stop ₹143.93; charges ₹4,608.48 crore)
2025-08-11  MIRZAINT    BUY ₹19.52 lakh crore at ₹33.00 (fresh Friday signal — BUY: 4.19× weekly, month 2.46×, ladder rising; stop ₹30.59; charges ₹4,607.50 crore)
2025-08-11  PGHL        BUY ₹19.53 lakh crore at ₹6,345.00 (fresh Friday signal — BUY: 1.64× weekly, month 2.94×, ladder rising; stop ₹5,320.00; charges ₹4,610.04 crore)
2025-08-11  PRAKASH     BUY ₹19.71 lakh crore at ₹178.70 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 2.58×, ladder rising; stop ₹145.68; charges ₹4,651.94 crore)
2025-08-11  RAIN        BUY ₹19.74 lakh crore at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹4,659.46 crore)
2025-08-18  PGHL        PYRAMID BUY ₹19.68 lakh crore at ₹6,408.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,758.90; charges ₹4,644.82 crore)
2025-08-26  RAIN        SELL ₹17.61 lakh crore at stop ₹143.64 (-10.4%, charges ₹3,911.74 crore) — the cash goes back to work at the next Friday screen
2025-09-01  SHREDIGCEM  BUY ₹21.42 lakh crore at ₹97.22 (fresh Friday signal — BUY: 4.86× weekly, month 3.98×, ladder rising; stop ₹75.89; charges ₹5,056.55 crore)
2025-09-08  PGHL        PYRAMID BUY ₹39.90 lakh crore at ₹6,505.50 (box jump — doubling the stake with NEW capital; stop stays ₹5,938.45; charges ₹9,419.85 crore)
2025-09-09  RPOWER      SELL ₹3.19 lakh crore at stop ₹47.24 (-19.4%, charges ₹707.69 crore) — the cash goes back to work at the next Friday screen
2025-09-15  MIRZAINT    PYRAMID BUY ₹20.00 lakh crore at ₹33.90 (box jump — doubling the stake with NEW capital; stop stays ₹31.37; charges ₹4,721.99 crore)
2025-09-15  SHREDIGCEM  PYRAMID BUY ₹19.87 lakh crore at ₹90.40 (box jump — doubling the stake with NEW capital; stop stays ₹83.06; charges ₹4,690.73 crore)
2025-09-26  BLISSGVS    SELL ₹15.66 lakh crore at stop ₹143.93 (-19.4%, charges ₹3,478.44 crore) — the cash goes back to work at the next Friday screen
2025-09-29  SUBROS      BUY ₹19.47 lakh crore at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹4,595.41 crore)
2025-10-06  MIRZAINT    PYRAMID BUY ₹45.68 lakh crore at ₹38.75 (box jump — doubling the stake with NEW capital; stop stays ₹35.42; charges ₹10,782.36 crore)
2025-10-06  SUBROS      PYRAMID BUY ₹18.45 lakh crore at ₹1,075.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,046.90; charges ₹4,354.53 crore)
2025-10-09  FORCEMOT    SELL ₹36.49 lakh crore at stop ₹15,350.10 (+19.9%, charges ₹8,105.41 crore) — the cash goes back to work at the next Friday screen
2025-10-13  AVANTIFEED  PYRAMID BUY ₹2.09 lakh crore at ₹657.45 (box jump — doubling the stake with NEW capital; stop stays ₹511.29; charges ₹492.35 crore)
2025-10-13  SETFGOLD    BUY ₹35.38 lakh crore at ₹106.38 (fresh Friday signal — BUY: 3.03× weekly, month 4.34×, ladder rising; stop ₹90.43; charges ₹8,353.02 crore)
2025-10-14  SUBROS      SELL ₹35.80 lakh crore at stop ₹1,046.90 (-5.1%, charges ₹7,951.67 crore) — the cash goes back to work at the next Friday screen
2025-10-20  AVANTIFEED  PYRAMID BUY ₹4.36 lakh crore at ₹687.70 (box jump — doubling the stake with NEW capital; stop stays ₹600.07; charges ₹1,028.79 crore)
2025-10-20  CREDITACC   SELL ₹20.38 lakh crore at stop ₹1,274.42 (+17.5%, charges ₹4,526.89 crore) — the cash goes back to work at the next Friday screen
2025-10-20  GOLDSHARE   BUY ₹35.73 lakh crore at ₹109.00 (fresh Friday signal — BUY: 2.69× weekly, month 2.73×, ladder rising; stop ₹85.50; charges ₹8,434.41 crore)
2025-10-27  MIRZAINT    PYRAMID BUY ₹92.23 lakh crore at ₹39.17 (box jump — doubling the stake with NEW capital; stop stays ₹35.51; charges ₹21,772.73 crore)
2025-11-03  GOLDSHARE   PYRAMID BUY ₹33.32 lakh crore at ₹101.90 (box jump — doubling the stake with NEW capital; stop stays ₹91.06; charges ₹7,866.40 crore)
2025-11-03  PRAKASH     PYRAMID BUY ₹18.14 lakh crore at ₹164.85 (box jump — doubling the stake with NEW capital; stop stays ₹147.31; charges ₹4,281.27 crore)
2025-11-03  SETFGOLD    PYRAMID BUY ₹34.39 lakh crore at ₹103.63 (box jump — doubling the stake with NEW capital; stop stays ₹93.58; charges ₹8,117.88 crore)
2025-11-06  PGHL        SELL ₹72.60 lakh crore at stop ₹5,938.45 (-7.8%, charges ₹16,126.41 crore) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹51.64 lakh crore at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹12,189.87 crore)
2025-11-10  CUB         BUY ₹42.52 lakh crore at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹10,038.55 crore)
2025-11-14  PRAKASH     SELL ₹32.30 lakh crore at stop ₹147.31 (-14.2%, charges ₹7,174.92 crore) — the cash goes back to work at the next Friday screen
2025-11-17  CCL         PYRAMID BUY ₹54.08 lakh crore at ₹1,065.50 (box jump — doubling the stake with NEW capital; stop stays ₹976.41; charges ₹12,767.42 crore)
2025-11-17  CUB         PYRAMID BUY ₹45.40 lakh crore at ₹272.00 (box jump — doubling the stake with NEW capital; stop stays ₹232.87; charges ₹10,716.13 crore)
2025-11-17  PARAGMILK   BUY ₹32.30 lakh crore at ₹354.00 (fresh Friday signal — BUY: 3.48× weekly, month 2.34×, ladder rising; stop ₹293.55; charges ₹7,625.52 crore)
2025-11-24  CCL         SELL ₹98.79 lakh crore at stop ₹976.41 (-6.1%, charges ₹21,942.35 crore) — the cash goes back to work at the next Friday screen
2025-12-01  CUB         PYRAMID BUY ₹90.82 lakh crore at ₹272.40 (box jump — doubling the stake with NEW capital; stop stays ₹247.10; charges ₹21,438.44 crore)
2025-12-01  LUMAXIND    BUY ₹73.14 lakh crore at ₹5,671.00 (fresh Friday signal — BUY: 2.57× weekly, month 1.94×, ladder rising; stop ₹4,702.50; charges ₹17,265.66 crore)
2025-12-08  AVANTIFEED  PYRAMID BUY ₹10.39 lakh crore at ₹820.95 (box jump — doubling the stake with NEW capital; stop stays ₹748.60; charges ₹2,453.36 crore)
2025-12-08  LUMAXIND    PYRAMID BUY ₹72.95 lakh crore at ₹5,669.50 (box jump — doubling the stake with NEW capital; stop stays ₹5,078.70; charges ₹17,220.34 crore)
2025-12-09  PARAGMILK   SELL ₹26.66 lakh crore at stop ₹293.55 (-17.1%, charges ₹5,922.51 crore) — the cash goes back to work at the next Friday screen
2025-12-15  ESABINDIA   BUY ₹52.31 lakh crore at ₹6,203.50 (fresh Friday signal — BUY: 2.22× weekly, month 2.05×, ladder rising; stop ₹5,247.99; charges ₹12,349.16 crore)
2025-12-29  ESABINDIA   PYRAMID BUY ₹51.26 lakh crore at ₹6,093.50 (box jump — doubling the stake with NEW capital; stop stays ₹5,605.00; charges ₹12,101.55 crore)
2025-12-29  MIRZAINT    SELL ₹1.71 crore crore at stop ₹36.49 (-3.0%, charges ₹38,039.47 crore) — the cash goes back to work at the next Friday screen
2026-01-01  LUMAXIND    SELL ₹1.30 crore crore at stop ₹5,078.70 (-10.4%, charges ₹28,930.16 crore) — the cash goes back to work at the next Friday screen
2026-01-05  HINDCOPPER  BUY ₹83.90 lakh crore at ₹554.95 (fresh Friday signal — ACCUMULATE: 6.99× weekly, month 6.47×, ladder rising; stop ₹456.95; charges ₹19,805.03 crore)
2026-01-05  KIRIINDUS   BUY ₹84.40 lakh crore at ₹622.00 (fresh Friday signal — BUY: 24.50× weekly, month 6.65×, ladder rising; stop ₹525.16; charges ₹19,923.81 crore)
2026-01-08  KIRIINDUS   SELL ₹70.93 lakh crore at stop ₹525.16 (-15.6%, charges ₹15,755.48 crore) — the cash goes back to work at the next Friday screen
2026-01-12  ESABINDIA   SELL ₹93.99 lakh crore at stop ₹5,605.00 (-8.8%, charges ₹20,876.19 crore) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹88.57 lakh crore at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹20,907.41 crore)
2026-01-12  SETFGOLD    PYRAMID BUY ₹78.69 lakh crore at ₹118.70 (box jump — doubling the stake with NEW capital; stop stays ₹106.43; charges ₹18,574.84 crore)
2026-01-19  CUB         PYRAMID BUY ₹1.80 crore crore at ₹269.65 (box jump — doubling the stake with NEW capital; stop stays ₹247.95; charges ₹42,393.92 crore)
2026-01-19  HINDCOPPER  PYRAMID BUY ₹85.97 lakh crore at ₹570.00 (box jump — doubling the stake with NEW capital; stop stays ₹485.74; charges ₹20,294.11 crore)
2026-01-19  KIRIINDUS   BUY ₹1.25 crore crore at ₹530.30 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 9.46×, ladder rising; stop ₹382.56; charges ₹29,583.44 crore)
2026-01-19  NATIONALUM  PYRAMID BUY ₹91.12 lakh crore at ₹363.00 (box jump — doubling the stake with NEW capital; stop stays ₹312.41; charges ₹21,509.87 crore)
2026-01-20  SHREDIGCEM  SELL ₹36.39 lakh crore at stop ₹83.06 (-11.5%, charges ₹8,082.86 crore) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹18.89 lakh crore at stop ₹748.60 (-2.4%, charges ₹4,195.62 crore) — the cash goes back to work at the next Friday screen
2026-02-02  AXISGOLD    SELL ₹5.18 lakh crore at stop ₹112.59 (+43.6%, charges ₹1,151.02 crore) — the cash goes back to work at the next Friday screen
2026-02-02  CPSEETF     BUY ₹1.40 crore crore at ₹95.71 (fresh Friday signal — BUY: 4.29× weekly, month 2.10×, ladder rising; stop ₹85.68; charges ₹32,937.52 crore)
2026-02-02  GOLDBEES    SELL ₹27.33 lakh crore at stop ₹113.05 (+41.5%, charges ₹6,070.98 crore) — the cash goes back to work at the next Friday screen
2026-02-02  KIRIINDUS   PYRAMID BUY ₹1.09 crore crore at ₹461.25 (box jump — doubling the stake with NEW capital; stop stays ₹423.46; charges ₹25,670.66 crore)
2026-02-02  NATIONALUM  PYRAMID BUY ₹1.74 crore crore at ₹347.10 (box jump — doubling the stake with NEW capital; stop stays ₹335.49; charges ₹41,086.86 crore)
2026-02-02  SETFGOLD    PYRAMID BUY ₹1.72 crore crore at ₹130.03 (box jump — doubling the stake with NEW capital; stop stays ₹115.37; charges ₹40,647.62 crore)
2026-02-16  HINDCOPPER  PYRAMID BUY ₹1.76 crore crore at ₹585.00 (box jump — doubling the stake with NEW capital; stop stays ₹520.46; charges ₹41,607.16 crore)
2026-02-17  NATIONALUM  SELL ₹3.35 crore crore at stop ₹335.49 (-4.8%, charges ₹74,478.21 crore) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹2.25 crore crore at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.67×, ladder rising; stop ₹5,440.18; charges ₹53,079.85 crore)
2026-02-23  CPSEETF     PYRAMID BUY ₹1.48 crore crore at ₹101.63 (box jump — doubling the stake with NEW capital; stop stays ₹91.67; charges ₹34,892.26 crore)
2026-02-23  ICICIB22    BUY ₹1.43 crore crore at ₹127.18 (fresh Friday signal — BUY: 1.79× weekly, month 1.79×, ladder rising; stop ₹114.46; charges ₹33,751.25 crore)
2026-02-23  KIRIINDUS   PYRAMID BUY ₹2.15 crore crore at ₹457.15 (box jump — doubling the stake with NEW capital; stop stays ₹427.56; charges ₹50,824.89 crore)
2026-03-02  ABB         PYRAMID BUY ₹2.15 crore crore at ₹5,840.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,486.25; charges ₹50,780.72 crore)
2026-03-02  HINDCOPPER  PYRAMID BUY ₹3.39 crore crore at ₹563.50 (box jump — doubling the stake with NEW capital; stop stays ₹528.63; charges ₹80,061.41 crore)
2026-03-02  KIRIINDUS   SELL ₹4.01 crore crore at stop ₹427.56 (-10.3%, charges ₹89,148.93 crore) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹3.34 crore crore at stop ₹251.43 (-6.4%, charges ₹74,134.70 crore) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹6.34 crore crore at stop ₹528.63 (-7.0%, charges ₹1.41 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-16  APOLLOPIPE  BUY ₹2.97 crore crore at ₹407.55 (fresh Friday signal — BUY: 65.78× weekly, month 26.51×, ladder rising; stop ₹315.92; charges ₹70,042.67 crore)
2026-03-16  CPSEETF     PYRAMID BUY ₹2.97 crore crore at ₹102.23 (box jump — doubling the stake with NEW capital; stop stays ₹96.54; charges ₹70,113.66 crore)
2026-03-16  J&KBANK     BUY ₹2.96 crore crore at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹69,859.82 crore)
2026-03-16  JBCHEPHARM  BUY ₹2.96 crore crore at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹69,988.31 crore)
2026-03-23  ABB         PYRAMID BUY ₹4.61 crore crore at ₹6,264.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,854.38; charges ₹1.09 lakh crore)
2026-03-23  AVADHSUGAR  BUY ₹3.56 crore crore at ₹450.00 (fresh Friday signal — BUY: 1.74× weekly, month 5.07×, ladder rising; stop ₹369.20; charges ₹84,121.22 crore)
2026-03-23  ICICIB22    SELL ₹1.28 crore crore at stop ₹114.46 (-10.0%, charges ₹28,450.02 crore) — the cash goes back to work at the next Friday screen
2026-03-23  J&KBANK     PYRAMID BUY ₹2.82 crore crore at ₹115.68 (box jump — doubling the stake with NEW capital; stop stays ₹110.67; charges ₹66,553.63 crore)
2026-03-23  J&KBANK     SELL ₹5.38 crore crore at stop ₹110.67 (-6.5%, charges ₹1.19 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-23  SETFGOLD    SELL ₹3.05 crore crore at stop ₹115.37 (-4.6%, charges ₹67,637.22 crore) — the cash goes back to work at the next Friday screen
2026-03-30  APOLLOPIPE  PYRAMID BUY ₹3.07 crore crore at ₹423.35 (box jump — doubling the stake with NEW capital; stop stays ₹350.75; charges ₹72,586.34 crore)
2026-03-30  BAJAJHIND   BUY ₹3.91 crore crore at ₹16.42 (fresh Friday signal — ACCUMULATE: 2.06× weekly, month 1.79×, ladder rising; stop ₹13.87; charges ₹92,221.18 crore)
2026-03-30  DWARKESH    BUY ₹3.88 crore crore at ₹42.99 (fresh Friday signal — BUY: 2.17× weekly, month 2.56×, ladder rising; stop ₹34.22; charges ₹91,619.84 crore)
2026-04-01  TAX         FY2026 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹2.68 crore crore / LT ₹0.00)
2026-04-06  AVADHSUGAR  PYRAMID BUY ₹3.74 crore crore at ₹474.00 (box jump — doubling the stake with NEW capital; stop stays ₹404.27; charges ₹88,398.52 crore)
2026-04-06  CHENNPETRO  BUY ₹3.15 crore crore at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹74,421.46 crore)
2026-04-20  AVADHSUGAR  PYRAMID BUY ₹7.65 crore crore at ₹484.70 (box jump — doubling the stake with NEW capital; stop stays ₹440.85; charges ₹1.81 lakh crore)
2026-04-20  DWARKESH    PYRAMID BUY ₹4.31 crore crore at ₹47.90 (box jump — doubling the stake with NEW capital; stop stays ₹41.52; charges ₹1.02 lakh crore)
2026-05-04  BAJAJHIND   PYRAMID BUY ₹4.87 crore crore at ₹20.50 (box jump — doubling the stake with NEW capital; stop stays ₹17.96; charges ₹1.15 lakh crore)
2026-05-04  CPSEETF     PYRAMID BUY ₹6.41 crore crore at ₹110.50 (box jump — doubling the stake with NEW capital; stop stays ₹100.15; charges ₹1.51 lakh crore)
2026-05-11  APOLLOPIPE  PYRAMID BUY ₹7.18 crore crore at ₹495.00 (box jump — doubling the stake with NEW capital; stop stays ₹399.95; charges ₹1.70 lakh crore)
2026-05-14  BAJAJHIND   SELL ₹8.50 crore crore at stop ₹17.96 (-2.7%, charges ₹1.89 lakh crore) — the cash goes back to work at the next Friday screen
2026-05-18  ABB         PYRAMID BUY ₹9.28 crore crore at ₹6,310.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,862.93; charges ₹2.19 lakh crore)
2026-05-18  CHENNPETRO  PYRAMID BUY ₹3.16 crore crore at ₹995.00 (box jump — doubling the stake with NEW capital; stop stays ₹953.23; charges ₹74,696.20 crore)
2026-05-18  DWARKESH    SELL ₹7.45 crore crore at stop ₹41.52 (-8.6%, charges ₹1.66 lakh crore) — the cash goes back to work at the next Friday screen
2026-05-18  SASKEN      BUY ₹8.50 crore crore at ₹1,680.10 (fresh Friday signal — BUY: 74.07× weekly, month 16.59×, ladder rising; stop ₹1,161.09; charges ₹2.01 lakh crore)
2026-05-25  APOLLOPIPE  PYRAMID BUY ₹15.24 crore crore at ₹525.65 (box jump — doubling the stake with NEW capital; stop stays ₹439.90; charges ₹3.60 lakh crore)
2026-05-25  DHANUKA     BUY ₹7.45 crore crore at ₹1,190.10 (fresh Friday signal — BUY: 17.25× weekly, month 3.84×, ladder rising; stop ₹988.48; charges ₹1.76 lakh crore)
2026-05-25  JBCHEPHARM  PYRAMID BUY ₹3.07 crore crore at ₹2,214.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,976.47; charges ₹72,372.81 crore)
2026-05-25  SASKEN      PYRAMID BUY ₹9.39 crore crore at ₹1,862.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,551.58; charges ₹2.22 lakh crore)
2026-06-02  CPSEETF     SELL ₹11.59 crore crore at stop ₹100.15 (-5.0%, charges ₹2.57 lakh crore) — the cash goes back to work at the next Friday screen
2026-06-08  BALAMINES   BUY ₹11.59 crore crore at ₹2,029.10 (fresh Friday signal — BUY: 5.63× weekly, month 3.60×, ladder rising; stop ₹1,615.57; charges ₹2.73 lakh crore)
2026-06-08  DHANUKA     PYRAMID BUY ₹6.77 crore crore at ₹1,083.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,004.15; charges ₹1.60 lakh crore)
2026-06-08  JBCHEPHARM  PYRAMID BUY ₹5.99 crore crore at ₹2,164.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,976.86; charges ₹1.41 lakh crore)
2026-06-15  BALAMINES   PYRAMID BUY ₹12.42 crore crore at ₹2,180.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,889.93; charges ₹2.93 lakh crore)
2026-06-15  CHENNPETRO  PYRAMID BUY ₹7.36 crore crore at ₹1,158.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,075.02; charges ₹1.74 lakh crore)
2026-06-22  BALAMINES   PYRAMID BUY ₹24.66 crore crore at ₹2,167.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,931.44; charges ₹5.82 lakh crore)
2026-06-22  SASKEN      PYRAMID BUY ₹25.99 crore crore at ₹2,579.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,933.72; charges ₹6.14 lakh crore)
2026-06-29  BALAMINES   SELL ₹43.81 crore crore at stop ₹1,931.44 (-9.6%, charges ₹9.73 lakh crore) — the cash goes back to work at the next Friday screen
2026-07-06  ADFFOODS    BUY ₹19.01 crore crore at ₹321.40 (fresh Friday signal — BUY: 8.70× weekly, month 4.89×, ladder rising; stop ₹282.15; charges ₹4.49 lakh crore)
2026-07-06  TASTYBITE   BUY ₹18.92 crore crore at ₹8,674.00 (fresh Friday signal — BUY: 4.19× weekly, month 2.41×, ladder rising; stop ₹7,657.48; charges ₹4.47 lakh crore)
2026-07-08  SASKEN      SELL ₹38.85 crore crore at stop ₹1,933.72 (-11.1%, charges ₹8.63 lakh crore) — the cash goes back to work at the next Friday screen
2026-07-13  ADFFOODS    PYRAMID BUY ₹18.82 crore crore at ₹318.95 (box jump — doubling the stake with NEW capital; stop stays ₹287.38; charges ₹4.44 lakh crore)
2026-07-13  MIRZAINT    BUY ₹20.84 crore crore at ₹39.66 (fresh Friday signal — BUY: 8.80× weekly, month 1.80×, ladder rising; stop ₹32.30; charges ₹4.92 lakh crore)
2026-07-13  RITES       BUY ₹20.86 crore crore at ₹228.43 (fresh Friday signal — ACCUMULATE: 9.47× weekly, month 9.79×, ladder rising; stop ₹204.60; charges ₹4.92 lakh crore)
2026-07-20  MIRZAINT    PYRAMID BUY ₹20.16 crore crore at ₹38.45 (box jump — doubling the stake with NEW capital; stop stays ₹34.99; charges ₹4.76 lakh crore)
2026-07-20  TASTYBITE   PYRAMID BUY ₹19.04 crore crore at ₹8,746.50 (box jump — doubling the stake with NEW capital; stop stays ₹7,999.48; charges ₹4.49 lakh crore)
2026-07-22  DHANUKA     SELL ₹12.51 crore crore at stop ₹1,004.15 (-11.7%, charges ₹2.78 lakh crore) — the cash goes back to work at the next Friday screen
2026-07-24  ADFFOODS    SELL ₹33.79 crore crore at stop ₹287.38 (-10.2%, charges ₹7.51 lakh crore) — the cash goes back to work at the next Friday screen
2026-07-24  MIRZAINT    SELL ₹36.56 crore crore at stop ₹34.99 (-10.4%, charges ₹8.12 lakh crore) — the cash goes back to work at the next Friday screen
2026-07-27  ASHIANA     BUY ₹25.46 crore crore at ₹388.55 (fresh Friday signal — ACCUMULATE: 21.14× weekly, month 4.03×, ladder rising; stop ₹349.27; charges ₹6.01 lakh crore)
2026-07-27  CHENNPETRO  PYRAMID BUY ₹15.61 crore crore at ₹1,230.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,130.59; charges ₹3.68 lakh crore)
2026-07-27  MAHLOG      BUY ₹25.44 crore crore at ₹417.00 (fresh Friday signal — ACCUMULATE: 8.12× weekly, month 1.89×, ladder rising; stop ₹360.48; charges ₹6.01 lakh crore)
2026-07-27  SHALPAINTS  BUY ₹25.55 crore crore at ₹72.10 (fresh Friday signal — BUY: 24.23× weekly, month 2.36×, ladder rising; stop ₹45.48; charges ₹6.03 lakh crore)
2026-08-03  SHALPAINTS  PYRAMID BUY ₹23.93 crore crore at ₹67.68 (box jump — doubling the stake with NEW capital; stop stays ₹57.85; charges ₹5.65 lakh crore)
2026-08-10  AVADHSUGAR  PYRAMID BUY ₹19.23 crore crore at ₹610.00 (box jump — doubling the stake with NEW capital; stop stays ₹475.95; charges ₹4.54 lakh crore)
2026-08-10  MAHLOG      PYRAMID BUY ₹24.53 crore crore at ₹403.00 (box jump — doubling the stake with NEW capital; stop stays ₹380.33; charges ₹5.79 lakh crore)
2026-08-24  TASTYBITE   PYRAMID BUY ₹44.29 crore crore at ₹10,186.00 (box jump — doubling the stake with NEW capital; stop stays ₹8,558.55; charges ₹10.46 lakh crore)
2026-08-31  RITES       PYRAMID BUY ₹19.77 crore crore at ₹217.00 (box jump — doubling the stake with NEW capital; stop stays ₹204.83; charges ₹4.67 lakh crore)
2026-09-02  MAHLOG      SELL ₹46.14 crore crore at stop ₹380.33 (-7.2%, charges ₹10.25 lakh crore) — the cash goes back to work at the next Friday screen
2026-09-07  ASHIANA     SELL ₹22.78 crore crore at stop ₹349.27 (-10.1%, charges ₹5.06 lakh crore) — the cash goes back to work at the next Friday screen
2026-09-07  BODALCHEM   BUY ₹51.02 crore crore at ₹168.00 (fresh Friday signal — BUY: 23.67× weekly, month 12.34×, ladder rising; stop ₹63.20; charges ₹12.04 lakh crore)
2026-09-07  TASTYBITE   PYRAMID BUY ₹86.01 crore crore at ₹9,902.00 (box jump — doubling the stake with NEW capital; stop stays ₹9,267.25; charges ₹20.30 lakh crore)
```
