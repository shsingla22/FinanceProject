# The Darvas screen — 2020-03-01 → 2026-09-11

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2019-03-01 → 2026-09-11, 1971 symbols, in `ROLLING_2019-03-01_to_2026-09-13/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **The universe is POINT-IN-TIME with a ROLLING radar:** membership is recomputed EVERY MONTH as the top symbols by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and new listings or emerging names ENTER the month they earn their place, so neither survivorship bias nor an emergence blind spot remains. Membership gates fresh entries only; a held position runs to its stop regardless (`_membership_long.csv`). Raw exchange data means heuristic split/bonus adjustment, every one listed in `_adjustments.csv`. No slippage, stop exits at the stop price, fractional shares. Stored fiscal statements exist for 37% of this universe — a stock without statements cannot be blocked by the earnings gate (only a FALLING verdict blocks), which loosens that gate for the rest.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), at the next trading day's open, falling earnings power refused, nothing below half a slice. **Funding order:** a fully-qualified signal the cash never reached climbs the queue each time it is starved and goes to the FRONT ahead of louder newcomers, resetting to normal once funded — so a steady climber flagged week after week can no longer be outbid forever by one-week volume spikes; fresh names rank by volume reaction. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with a RECYCLING POCKET, 3× cap.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled at the next day's open — at most THREE times per position (8× the first slice). The doubling money lives in its own POCKET, outside the trading book: when a doubled position sells, the pyramid lots' capital AND their returns go OUT to the pocket (only the initial slice and its returns stay in the portfolio, so the trading book can never balloon), and later doubles draw the pocket FIRST — fresh outside money enters only for the shortfall, each such injection dated and logged, so the honest yardstick is the money-weighted return (XIRR) and the capital requirement stays bounded. Each add-on is its own tax lot on its own holding clock (the pocket pays tax on its own gains); the ratcheted stop covers the whole enlarged position; a jump past the cap is logged, never doubled.

## The headline — XIRR is the honest yardstick

| Engine | Money put in | Final value | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | ₹964.07 (₹100 + ₹864.07 injected) | **₹906.88** | **-1.12%** |
| B: doubling, before charges and tax | ₹1,052.36 | ₹1,087.11 | +0.61% |
| **A: no doubling, NET of charges and tax** | ₹100.00 | **₹234.07** | **+13.94%** |
| A: no doubling, before charges and tax | ₹100.00 | ₹328.43 | +20.02% |
| Nifty 50 (pre-cost, pre-tax) | ₹100.00 | ₹212.91 | +12.30% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹1.71; unrealised gains in both end books carry further deferred liabilities.*

6.52 years, 341 weekly screens. Engine B's total doubling spend was ₹7,374.26: the pocket recycled ₹6,510.19 of it, and only ₹864.07 was fresh outside money across 26 dated injections (all in the blotter and events CSV). The pocket holds ₹530.72 at the end, counted in the final value.

## What the frictions took (net runs)

| | Engine A: no doubling | Engine B: doubling |
|---|---:|---:|
| Transaction charges | ₹10.77 | ₹6.53 |
| Capital-gains tax paid | ₹22.77 | ₹11.54 |
| Tax accrued, final part-year | ₹1.71 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling) — portfolio book

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹11.59 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹1.15 | ₹0.00 | ₹0.23 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹55.77 | ₹0.00 | ₹11.15 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹11.01 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹0.79 | ₹0.00 | ₹0.16 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹7.16 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹34.28 / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹35.44 / ₹0.00 |

### Tax ledger — Engine B — the doubling pocket's own book

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹0.00 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹43.20 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹33.45 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹24.34 | ₹0.00 | ₹4.87 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹17.71 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹35.96 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹78.39 / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹88.05 / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹11.59 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹6.40 | ₹0.00 | ₹1.28 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹34.00 | ₹0.00 | ₹6.80 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹15.16 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹34.29 | ₹6.74 | ₹7.70 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹34.81 | ₹0.00 | ₹6.96 | ₹0.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.23 | ₹0.03 | ₹0.00 / ₹0.00 |
| Final part-year (accrued) | — | ₹8.55 | ₹0.00 | ₹1.71 | ₹0.00 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2020 (2020-12-24) | ₹112.96 | +13.0% | ₹492.24 | ₹392.28 | -0.0% | +25.1% |
| 2021 (2021-12-31) | ₹153.67 | +36.0% | ₹806.83 | ₹236.72 | +12.5% | +26.2% |
| 2022 (2022-12-30) | ₹133.86 | -12.9% | ₹1,028.71 | ₹235.07 | -1.5% | +4.3% |
| 2023 (2023-12-29) | ₹215.64 | +61.1% | ₹1,075.12 | ₹0.00 | +4.5% | +20.0% |
| 2024 (2024-12-27) | ₹224.29 | +4.0% | ₹1,006.67 | ₹0.00 | -6.4% | +9.6% |
| 2025 (2025-12-26) | ₹212.51 | -5.3% | ₹950.08 | ₹0.00 | -5.6% | +9.4% |
| 2026 (2026-09-11) | ₹234.07 | +10.1% | ₹906.88 | ₹0.00 | -4.5% | -10.2% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-40.0%** (A: -31.6%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **117 closed trades**: 18 winners (15%), average winner +15.7%, average loser -10.9% (returns per blended entry price).
- Best closed trade POLYMED +60.1%; worst BCG -59.0%.
- Median holding period 53 days.
- Cash share of equity averaged 4%; fully in cash 5 of 341 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

*B equity counts the whole system — trading book plus the idle doubling pocket (shown separately).*

| Month-end screen | B equity | B pocket | B injected so far | B cash | B positions | A equity |
|---|---:|---:|---:|---:|---:|---:|
| 2020-03-27 | ₹88.29 | ₹0.00 | ₹0.00 | ₹88.29 | 0 | ₹88.29 |
| 2020-04-30 | ₹89.10 | ₹0.00 | ₹0.00 | ₹26.28 | 7 | ₹89.10 |
| 2020-05-29 | ₹140.03 | ₹0.00 | ₹46.97 | ₹5.15 | 9 | ₹93.67 |
| 2020-06-26 | ₹246.34 | ₹0.00 | ₹138.81 | ₹0.00 | 9 | ₹100.04 |
| 2020-07-31 | ₹389.59 | ₹31.57 | ₹278.21 | ₹19.17 | 7 | ₹103.92 |
| 2020-08-28 | ₹479.38 | ₹146.06 | ₹392.28 | ₹14.42 | 6 | ₹100.59 |
| 2020-09-25 | ₹499.46 | ₹215.88 | ₹392.28 | ₹27.27 | 3 | ₹104.20 |
| 2020-10-30 | ₹495.05 | ₹80.36 | ₹392.28 | ₹0.00 | 4 | ₹96.43 |
| 2020-11-27 | ₹496.89 | ₹173.81 | ₹392.28 | ₹11.95 | 4 | ₹103.55 |
| 2020-12-24 | ₹492.24 | ₹305.35 | ₹392.28 | ₹55.10 | 2 | ₹112.96 |
| 2021-01-29 | ₹475.93 | ₹296.79 | ₹392.28 | ₹39.15 | 3 | ₹110.63 |
| 2021-02-26 | ₹516.38 | ₹128.98 | ₹392.28 | ₹16.42 | 4 | ₹123.67 |
| 2021-03-26 | ₹580.92 | ₹177.11 | ₹443.30 | ₹0.00 | 3 | ₹113.63 |
| 2021-04-30 | ₹658.33 | ₹105.81 | ₹443.30 | ₹0.00 | 3 | ₹123.82 |
| 2021-05-28 | ₹717.02 | ₹26.87 | ₹443.30 | ₹0.00 | 3 | ₹141.80 |
| 2021-06-25 | ₹894.85 | ₹446.41 | ₹527.33 | ₹0.00 | 3 | ₹150.98 |
| 2021-07-30 | ₹1,089.71 | ₹0.00 | ₹549.84 | ₹0.00 | 3 | ₹165.69 |
| 2021-08-27 | ₹1,137.76 | ₹0.00 | ₹629.00 | ₹44.01 | 2 | ₹153.55 |
| 2021-09-24 | ₹1,141.66 | ₹0.00 | ₹629.00 | ₹44.01 | 2 | ₹154.97 |
| 2021-10-29 | ₹819.84 | ₹448.04 | ₹629.00 | ₹0.00 | 4 | ₹154.45 |
| 2021-11-26 | ₹791.32 | ₹551.75 | ₹629.00 | ₹85.96 | 2 | ₹150.37 |
| 2021-12-31 | ₹806.83 | ₹458.86 | ₹629.00 | ₹10.72 | 5 | ₹153.67 |
| 2022-01-28 | ₹786.62 | ₹527.48 | ₹629.00 | ₹42.93 | 4 | ₹151.02 |
| 2022-02-25 | ₹746.02 | ₹487.46 | ₹629.00 | ₹47.50 | 4 | ₹135.46 |
| 2022-03-25 | ₹766.65 | ₹301.86 | ₹629.00 | ₹6.27 | 5 | ₹134.84 |
| 2022-04-29 | ₹738.21 | ₹451.99 | ₹629.00 | ₹55.09 | 3 | ₹132.23 |
| 2022-05-27 | ₹702.14 | ₹554.87 | ₹629.00 | ₹22.46 | 7 | ₹113.61 |
| 2022-06-24 | ₹697.87 | ₹476.14 | ₹629.00 | ₹0.00 | 7 | ₹115.15 |
| 2022-07-29 | ₹739.86 | ₹217.34 | ₹629.00 | ₹11.84 | 6 | ₹125.44 |
| 2022-08-26 | ₹778.53 | ₹92.46 | ₹629.00 | ₹0.00 | 6 | ₹131.75 |
| 2022-09-30 | ₹1,008.21 | ₹202.21 | ₹864.07 | ₹28.95 | 5 | ₹132.06 |
| 2022-10-28 | ₹1,039.96 | ₹276.44 | ₹864.07 | ₹0.00 | 5 | ₹134.99 |
| 2022-11-25 | ₹1,078.03 | ₹410.62 | ₹864.07 | ₹19.21 | 4 | ₹143.20 |
| 2022-12-30 | ₹1,028.71 | ₹885.61 | ₹864.07 | ₹87.20 | 1 | ₹133.86 |
| 2023-01-27 | ₹1,021.54 | ₹843.76 | ₹864.07 | ₹1.12 | 7 | ₹121.67 |
| 2023-02-24 | ₹1,021.24 | ₹817.83 | ₹864.07 | ₹10.64 | 6 | ₹119.18 |
| 2023-03-31 | ₹1,031.61 | ₹710.74 | ₹864.07 | ₹33.33 | 4 | ₹122.10 |
| 2023-04-28 | ₹1,036.40 | ₹744.14 | ₹864.07 | ₹0.00 | 5 | ₹130.46 |
| 2023-05-26 | ₹1,067.17 | ₹602.18 | ₹864.07 | ₹0.00 | 5 | ₹145.86 |
| 2023-06-30 | ₹1,072.09 | ₹582.49 | ₹864.07 | ₹15.96 | 4 | ₹153.21 |
| 2023-07-28 | ₹1,064.01 | ₹594.58 | ₹864.07 | ₹0.00 | 4 | ₹154.66 |
| 2023-08-25 | ₹1,053.76 | ₹824.79 | ₹864.07 | ₹19.61 | 4 | ₹167.37 |
| 2023-09-29 | ₹1,049.94 | ₹747.06 | ₹864.07 | ₹0.54 | 4 | ₹177.97 |
| 2023-10-27 | ₹1,060.91 | ₹817.98 | ₹864.07 | ₹34.70 | 3 | ₹181.85 |
| 2023-11-24 | ₹1,064.90 | ₹817.98 | ₹864.07 | ₹10.40 | 4 | ₹201.49 |
| 2023-12-29 | ₹1,075.12 | ₹720.97 | ₹864.07 | ₹10.40 | 4 | ₹215.64 |
| 2024-01-25 | ₹1,065.06 | ₹720.97 | ₹864.07 | ₹10.40 | 4 | ₹215.12 |
| 2024-02-23 | ₹1,056.34 | ₹500.20 | ₹864.07 | ₹10.40 | 4 | ₹215.72 |
| 2024-03-28 | ₹1,077.69 | ₹603.81 | ₹864.07 | ₹0.00 | 4 | ₹218.12 |
| 2024-04-26 | ₹1,095.92 | ₹563.97 | ₹864.07 | ₹0.00 | 4 | ₹221.25 |
| 2024-05-31 | ₹1,062.94 | ₹813.04 | ₹864.07 | ₹11.30 | 4 | ₹218.51 |
| 2024-06-28 | ₹1,054.00 | ₹848.49 | ₹864.07 | ₹8.19 | 5 | ₹216.33 |
| 2024-07-26 | ₹1,050.21 | ₹802.90 | ₹864.07 | ₹31.57 | 4 | ₹208.66 |
| 2024-08-30 | ₹1,051.14 | ₹732.52 | ₹864.07 | ₹0.00 | 5 | ₹225.92 |
| 2024-09-27 | ₹1,045.19 | ₹647.27 | ₹864.07 | ₹0.00 | 5 | ₹240.92 |
| 2024-10-25 | ₹1,023.58 | ₹823.74 | ₹864.07 | ₹50.15 | 3 | ₹221.41 |
| 2024-11-29 | ₹1,009.11 | ₹822.67 | ₹864.07 | ₹8.03 | 7 | ₹218.35 |
| 2024-12-27 | ₹1,006.67 | ₹716.67 | ₹864.07 | ₹34.38 | 5 | ₹224.29 |
| 2025-01-31 | ₹975.03 | ₹833.30 | ₹864.07 | ₹24.17 | 5 | ₹199.27 |
| 2025-02-28 | ₹962.01 | ₹780.90 | ₹864.07 | ₹0.00 | 7 | ₹187.24 |
| 2025-03-27 | ₹980.96 | ₹708.17 | ₹864.07 | ₹0.00 | 7 | ₹204.63 |
| 2025-04-25 | ₹968.81 | ₹750.53 | ₹864.07 | ₹2.30 | 5 | ₹206.56 |
| 2025-05-30 | ₹958.00 | ₹709.36 | ₹864.07 | ₹21.54 | 4 | ₹207.36 |
| 2025-06-27 | ₹963.28 | ₹616.63 | ₹864.07 | ₹0.00 | 5 | ₹213.79 |
| 2025-07-25 | ₹966.35 | ₹616.63 | ₹864.07 | ₹0.00 | 5 | ₹214.19 |
| 2025-08-29 | ₹961.68 | ₹682.06 | ₹864.07 | ₹0.00 | 5 | ₹203.05 |
| 2025-09-26 | ₹956.74 | ₹664.50 | ₹864.07 | ₹14.43 | 4 | ₹207.49 |
| 2025-10-31 | ₹949.24 | ₹718.36 | ₹864.07 | ₹11.18 | 4 | ₹206.02 |
| 2025-11-28 | ₹956.59 | ₹646.15 | ₹864.07 | ₹31.76 | 3 | ₹202.90 |
| 2025-12-26 | ₹950.08 | ₹629.51 | ₹864.07 | ₹0.00 | 4 | ₹212.51 |
| 2026-01-30 | ₹919.65 | ₹801.32 | ₹864.07 | ₹3.84 | 6 | ₹225.82 |
| 2026-02-27 | ₹901.11 | ₹755.52 | ₹864.07 | ₹17.32 | 4 | ₹211.49 |
| 2026-03-27 | ₹892.92 | ₹738.31 | ₹864.07 | ₹26.66 | 3 | ₹184.29 |
| 2026-04-30 | ₹897.09 | ₹687.35 | ₹864.07 | ₹0.00 | 5 | ₹194.60 |
| 2026-05-29 | ₹886.03 | ₹608.99 | ₹864.07 | ₹0.00 | 5 | ₹199.65 |
| 2026-06-25 | ₹891.68 | ₹643.71 | ₹864.07 | ₹0.00 | 5 | ₹209.01 |
| 2026-07-31 | ₹891.78 | ₹530.72 | ₹864.07 | ₹11.07 | 4 | ₹201.28 |
| 2026-08-28 | ₹892.33 | ₹530.72 | ₹864.07 | ₹11.07 | 4 | ₹228.10 |
| 2026-09-11 | ₹906.88 | ₹530.72 | ₹864.07 | ₹11.07 | 4 | ₹234.07 |

## Engine B — still held at the end

| Stock | First entry | Blended entry ₹ | Lots | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|---:|
| CAPLIPOINT | 2026-05-18 | 2,367.83 | 4 | 2,754.90 | 2,376.52 | +16.3% |
| JTLINFRA | 2022-10-24 | 292.00 | 1 | 295.80 | 217.12 | +1.3% |
| LIQUID1 | 2026-03-30 | 1,100.91 | 3 | 1,122.52 | 1,047.51 | +2.0% |
| LIQUIDPLUS | 2026-02-09 | 1,085.23 | 4 | 1,103.07 | 1,039.82 | +1.6% |

## Engine B — every closed trade

*Returns are on the blended entry price across lots.*

| Stock | First entry | Blended ₹ | Lots | Exit | Exit ₹ | Return |
|---|---|---:|---:|---|---:|---:|
| HDFCMFGETF | 2020-03-09 | 4,002.50 | 1 | 2020-03-13 | 3,540.65 | -11.5% |
| INDOCO | 2020-03-09 | 228.20 | 1 | 2020-03-13 | 164.08 | -28.1% |
| LALPATHLAB | 2020-03-09 | 835.00 | 1 | 2020-03-13 | 743.38 | -11.0% |
| SETFGOLD | 2020-03-09 | 3,862.80 | 1 | 2020-03-17 | 3,548.39 | -8.1% |
| DEEPAKNTR | 2020-03-09 | 508.80 | 1 | 2020-03-19 | 356.25 | -30.0% |
| IOLCP | 2020-03-09 | 51.20 | 1 | 2020-03-19 | 36.91 | -27.9% |
| DEEPAKNTR | 2020-04-13 | 498.24 | 2 | 2020-06-12 | 474.05 | -4.9% |
| AXISGOLD | 2020-04-13 | 4,227.60 | 3 | 2020-07-23 | 3,971.05 | -6.1% |
| MANGCHEFER | 2020-05-11 | 35.27 | 3 | 2020-07-31 | 33.73 | -4.4% |
| EIDPARRY | 2020-05-11 | 267.40 | 4 | 2020-08-17 | 273.03 | +2.1% |
| PANACEABIO | 2020-06-15 | 222.48 | 3 | 2020-08-20 | 184.01 | -17.3% |
| GOLDBEES | 2020-04-13 | 43.84 | 2 | 2020-09-04 | 41.00 | -6.5% |
| CADILAHC | 2020-04-27 | 377.33 | 4 | 2020-09-08 | 364.99 | -3.3% |
| TAJGVK | 2020-04-27 | 142.96 | 3 | 2020-09-22 | 126.45 | -11.5% |
| HDFCMFGETF | 2020-04-20 | 4,685.38 | 3 | 2020-09-23 | 4,492.07 | -4.1% |
| ADVENZYMES | 2020-08-24 | 281.27 | 3 | 2020-11-03 | 292.33 | +3.9% |
| LASA | 2020-11-09 | 82.32 | 3 | 2020-12-21 | 77.95 | -5.3% |
| SYNGENE | 2020-04-27 | 442.96 | 4 | 2020-12-22 | 562.40 | +27.0% |
| BORORENEW | 2020-12-28 | 254.99 | 2 | 2021-01-20 | 247.59 | -2.9% |
| KIRIINDUS | 2020-12-28 | 538.77 | 2 | 2021-01-21 | 478.56 | -11.2% |
| SAKSOFT | 2020-09-28 | 382.48 | 2 | 2021-01-25 | 341.10 | -10.8% |
| XCHANGING | 2020-12-28 | 90.25 | 2 | 2021-01-25 | 80.75 | -10.5% |
| GAEL | 2021-02-01 | 71.47 | 1 | 2021-02-23 | 62.70 | -12.3% |
| INDIAMART | 2021-01-25 | 4,296.73 | 3 | 2021-03-02 | 4,137.25 | -3.7% |
| HINDZINC | 2021-01-25 | 288.74 | 2 | 2021-03-19 | 279.30 | -3.3% |
| APTECHT | 2021-02-01 | 219.72 | 4 | 2021-03-19 | 204.25 | -7.0% |
| POLYMED | 2020-09-07 | 593.42 | 4 | 2021-06-14 | 950.00 | +60.1% |
| VIDHIING | 2021-03-22 | 201.70 | 3 | 2021-06-18 | 182.64 | -9.4% |
| KESORAMIND | 2021-06-21 | 86.97 | 2 | 2021-08-10 | 85.78 | -1.4% |
| BAJAJHIND | 2021-03-08 | 13.76 | 4 | 2021-10-19 | 13.96 | +1.5% |
| DECCANCE | 2021-06-21 | 696.27 | 3 | 2021-11-22 | 620.61 | -10.9% |
| TATAMTRDVR | 2021-10-25 | 268.98 | 3 | 2021-11-22 | 265.05 | -1.5% |
| NETWORK18 | 2021-10-18 | 79.45 | 2 | 2021-11-29 | 72.52 | -8.7% |
| LTI | 2021-10-25 | 6,583.76 | 3 | 2022-01-24 | 6,270.00 | -4.8% |
| SHARDACROP | 2022-01-31 | 623.38 | 2 | 2022-02-11 | 545.30 | -12.5% |
| BSOFT | 2021-11-29 | 475.09 | 2 | 2022-02-14 | 424.65 | -10.6% |
| RAYMOND | 2021-11-29 | 703.20 | 3 | 2022-02-15 | 679.35 | -3.4% |
| TV18BRDCST | 2022-01-31 | 63.72 | 3 | 2022-02-22 | 58.38 | -8.4% |
| EXCELINDUS | 2022-03-07 | 1,603.38 | 2 | 2022-03-29 | 1,438.30 | -10.3% |
| SFL | 2021-12-06 | 3,348.75 | 4 | 2022-04-27 | 3,519.94 | +5.1% |
| EVERESTIND | 2022-02-21 | 705.00 | 3 | 2022-04-28 | 594.70 | -15.6% |
| RCF | 2022-04-04 | 100.30 | 2 | 2022-05-04 | 93.15 | -7.1% |
| GNFC | 2022-02-14 | 698.36 | 3 | 2022-05-06 | 792.16 | +13.4% |
| ORISSAMINE | 2022-05-02 | 3,379.00 | 1 | 2022-05-11 | 2,898.50 | -14.2% |
| MOL | 2022-05-09 | 129.80 | 1 | 2022-05-11 | 113.62 | -12.5% |
| RIIL | 2022-05-02 | 1,070.02 | 2 | 2022-05-26 | 863.73 | -19.3% |
| GEPIL | 2022-05-09 | 182.65 | 1 | 2022-05-31 | 163.45 | -10.5% |
| BCG | 2021-11-29 | 134.10 | 1 | 2022-06-06 | 55.00 | -59.0% |
| VBL | 2022-05-16 | 220.00 | 1 | 2022-06-06 | 196.27 | -10.8% |
| GRAUWEIL | 2022-05-23 | 76.53 | 2 | 2022-06-13 | 61.82 | -19.2% |
| MRPL | 2022-05-09 | 87.37 | 3 | 2022-07-06 | 69.61 | -20.3% |
| JKIL | 2022-05-09 | 298.61 | 4 | 2022-08-05 | 308.80 | +3.4% |
| NAVNETEDUL | 2022-08-08 | 134.26 | 4 | 2022-09-26 | 127.30 | -5.2% |
| VADILALIND | 2022-06-13 | 2,065.03 | 4 | 2022-10-20 | 2,295.06 | +11.1% |
| APARINDS | 2022-06-20 | 1,157.19 | 4 | 2022-11-03 | 1,358.50 | +17.4% |
| ELECON | 2022-06-13 | 151.43 | 4 | 2022-12-21 | 202.49 | +33.7% |
| SHANTIGEAR | 2022-06-06 | 314.55 | 4 | 2022-12-22 | 345.56 | +9.9% |
| ACC | 2022-05-23 | 2,241.61 | 4 | 2022-12-23 | 2,465.16 | +10.0% |
| GICRE | 2023-01-02 | 183.12 | 2 | 2023-02-01 | 167.72 | -8.4% |
| SPIC | 2023-01-02 | 83.38 | 2 | 2023-02-23 | 65.74 | -21.2% |
| IOB | 2023-01-02 | 29.25 | 2 | 2023-03-20 | 22.18 | -24.2% |
| JINDALSAW | 2023-02-06 | 69.60 | 2 | 2023-03-27 | 67.92 | -2.4% |
| SONATSOFTW | 2023-03-27 | 413.70 | 1 | 2023-03-29 | 371.45 | -10.2% |
| JSL | 2023-01-02 | 270.35 | 4 | 2023-04-13 | 256.98 | -4.9% |
| GSFC | 2023-01-02 | 159.39 | 3 | 2023-05-29 | 155.85 | -2.2% |
| ANURAS | 2023-04-17 | 1,118.40 | 3 | 2023-07-03 | 1,007.67 | -9.9% |
| HARIOMPIPE | 2023-01-02 | 433.91 | 4 | 2023-07-10 | 603.25 | +39.0% |
| CPSEETF | 2023-04-03 | 43.74 | 4 | 2023-07-31 | 41.97 | -4.0% |
| KIRLOSBROS | 2023-08-07 | 886.95 | 2 | 2023-08-21 | 771.68 | -13.0% |
| WELSPUNIND | 2023-08-07 | 122.17 | 3 | 2023-09-12 | 114.00 | -6.7% |
| GABRIEL | 2023-08-28 | 313.77 | 2 | 2023-09-12 | 295.45 | -5.8% |
| FDC | 2023-07-10 | 359.85 | 3 | 2023-10-23 | 354.97 | -1.4% |
| PRAKASH | 2023-09-18 | 174.23 | 3 | 2024-02-28 | 168.62 | -3.2% |
| PAISALO | 2024-03-04 | 191.33 | 2 | 2024-03-12 | 161.88 | -15.4% |
| ZENTEC | 2023-07-17 | 749.95 | 4 | 2024-05-09 | 896.89 | +19.6% |
| SOLARINDS | 2024-03-18 | 8,925.01 | 2 | 2024-06-04 | 7,980.95 | -10.6% |
| CENTURYTEX | 2024-05-13 | 2,000.00 | 1 | 2024-06-04 | 1,715.70 | -14.2% |
| PGEL | 2024-06-10 | 331.98 | 2 | 2024-07-23 | 338.30 | +1.9% |
| ENDURANCE | 2024-06-10 | 2,565.48 | 2 | 2024-08-05 | 2,429.11 | -5.3% |
| PANAMAPET | 2024-06-10 | 406.47 | 4 | 2024-10-03 | 384.27 | -5.5% |
| BASF | 2024-08-12 | 7,616.24 | 3 | 2024-10-22 | 7,611.30 | -0.1% |
| GENESYS | 2024-07-29 | 504.11 | 3 | 2024-10-25 | 451.09 | -10.5% |
| CUPID | 2023-10-30 | 148.70 | 2 | 2024-10-28 | 158.66 | +6.7% |
| ASTRAZEN | 2024-10-07 | 7,396.38 | 2 | 2024-11-14 | 6,854.77 | -7.3% |
| KIRLPNU | 2024-11-04 | 1,693.95 | 3 | 2024-12-23 | 1,596.00 | -5.8% |
| AKZOINDIA | 2024-11-04 | 4,118.82 | 2 | 2024-12-27 | 3,423.18 | -16.9% |
| PAYTM | 2024-10-28 | 936.85 | 4 | 2025-01-09 | 893.05 | -4.7% |
| CARERATING | 2024-11-04 | 1,514.54 | 2 | 2025-01-13 | 1,239.70 | -18.1% |
| HIMATSEIDE | 2024-11-04 | 186.30 | 2 | 2025-01-13 | 174.80 | -6.2% |
| KFINTECH | 2024-12-30 | 1,511.45 | 1 | 2025-01-15 | 1,159.14 | -23.3% |
| AEGISLOG | 2025-01-13 | 819.14 | 2 | 2025-01-24 | 700.36 | -14.5% |
| APOLLO | 2025-01-20 | 131.50 | 1 | 2025-02-17 | 110.19 | -16.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 1 | 2025-03-03 | 727.84 | -23.1% |
| TAJGVK | 2025-02-24 | 481.17 | 3 | 2025-04-02 | 453.34 | -5.8% |
| BAJAJHCARE | 2025-01-20 | 649.82 | 3 | 2025-04-07 | 521.14 | -19.8% |
| HDFCGOLD | 2025-02-10 | 76.10 | 3 | 2025-04-07 | 71.44 | -6.1% |
| SETFGOLD | 2025-03-10 | 74.79 | 1 | 2025-04-07 | 69.36 | -7.3% |
| VADILALIND | 2025-04-15 | 6,351.41 | 2 | 2025-05-30 | 5,401.40 | -15.0% |
| TDPOWERSYS | 2025-06-02 | 514.75 | 2 | 2025-07-28 | 457.00 | -11.2% |
| JSWHL | 2024-11-18 | 21,485.12 | 3 | 2025-08-04 | 19,106.01 | -11.1% |
| SHARDACROP | 2025-08-04 | 1,029.39 | 2 | 2025-09-24 | 848.33 | -17.6% |
| CREDITACC | 2025-01-27 | 1,084.34 | 4 | 2025-10-20 | 1,274.42 | +17.5% |
| SKYGOLD | 2025-10-27 | 363.51 | 2 | 2025-11-25 | 329.13 | -9.5% |
| SIRCA | 2025-08-11 | 499.33 | 4 | 2025-12-08 | 485.64 | -2.7% |
| AVANTIFEED | 2025-04-15 | 766.81 | 4 | 2026-01-21 | 748.60 | -2.4% |
| SANSERA | 2025-12-01 | 1,786.59 | 3 | 2026-01-23 | 1,672.76 | -6.4% |
| GMRAIRPORT | 2025-12-15 | 103.00 | 2 | 2026-01-23 | 92.10 | -10.6% |
| GOLDBEES | 2026-01-27 | 126.28 | 2 | 2026-02-02 | 113.05 | -10.5% |
| TATSILV | 2026-01-27 | 29.76 | 2 | 2026-02-02 | 23.03 | -22.6% |
| GROWWSLVR | 2026-01-27 | 27.64 | 2 | 2026-02-02 | 22.32 | -19.2% |
| SILVER | 2026-01-27 | 289.14 | 2 | 2026-02-02 | 234.68 | -18.8% |
| APEX | 2026-02-09 | 420.94 | 3 | 2026-02-27 | 389.22 | -7.5% |
| GOLDIETF | 2026-01-27 | 134.61 | 2 | 2026-03-23 | 115.68 | -14.1% |
| J&KBANK | 2026-03-02 | 117.18 | 3 | 2026-03-23 | 110.67 | -5.6% |
| AETHER | 2026-03-30 | 1,186.79 | 3 | 2026-05-14 | 1,125.84 | -5.1% |
| CPSEETF | 2026-02-09 | 105.98 | 4 | 2026-06-02 | 100.15 | -5.5% |
| MIDHANI | 2026-06-08 | 434.84 | 2 | 2026-07-23 | 399.19 | -8.2% |

## Engine B — the complete trade blotter

*Buys, pyramid injections, sells and tax settlements; every stop raise and refused signal is in `_longrun_events_2020-03-01_to_2026-09-11.csv`, and engine A's full ledger in `_longrun_events_2020-03-01_to_2026-09-11_no_doubling.csv`.*

```
2020-03-09  DEEPAKNTR   BUY ₹10.01 at ₹508.80 (fresh Friday signal — BUY: 2.89× weekly, month 3.33×, ladder rising; stop ₹356.25; charges ₹0.01)
2020-03-09  HDFCMFGETF  BUY ₹9.98 at ₹4,002.50 (fresh Friday signal — ACCUMULATE: 2.73× weekly, month 2.32×, ladder rising; stop ₹3,540.65; charges ₹0.01)
2020-03-09  INDOCO      BUY ₹9.96 at ₹228.20 (fresh Friday signal — ACCUMULATE: 2.23× weekly, month 2.79×, ladder rising; stop ₹164.08; charges ₹0.01)
2020-03-09  IOLCP       BUY ₹9.87 at ₹51.20 (fresh Friday signal — ACCUMULATE: 2.04× weekly, month 9.15×, ladder rising; stop ₹36.91; charges ₹0.01)
2020-03-09  LALPATHLAB  BUY ₹9.89 at ₹835.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.75×, ladder rising; stop ₹743.38; charges ₹0.01)
2020-03-09  SETFGOLD    BUY ₹10.00 at ₹3,862.80 (fresh Friday signal — BUY: 3.14× weekly, month 2.45×, ladder rising; stop ₹3,548.39; charges ₹0.01)
2020-03-13  HDFCMFGETF  SELL ₹8.81 at stop ₹3,540.65 (-11.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-13  INDOCO      SELL ₹7.14 at stop ₹164.08 (-28.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-13  LALPATHLAB  SELL ₹8.79 at stop ₹743.38 (-11.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-17  SETFGOLD    SELL ₹9.17 at stop ₹3,548.39 (-8.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-19  DEEPAKNTR   SELL ₹7.00 at stop ₹356.25 (-30.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-19  IOLCP       SELL ₹7.10 at stop ₹36.91 (-27.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-04-01  TAX         FY2020 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹11.59 / LT ₹0.00)
2020-04-13  AXISGOLD    BUY ₹8.82 at ₹4,049.00 (fresh Friday signal — ACCUMULATE: 1.53× weekly, month 3.08×, ladder rising; stop ₹3,199.23; charges ₹0.01)
2020-04-13  DEEPAKNTR   BUY ₹8.83 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.54×, ladder rising; stop ₹240.25; charges ₹0.01)
2020-04-13  GOLDBEES    BUY ₹8.80 at ₹41.24 (fresh Friday signal — ACCUMULATE: 1.55× weekly, month 9.44×, ladder rising; stop ₹31.74; charges ₹0.01)
2020-04-20  HDFCMFGETF  BUY ₹8.85 at ₹4,385.40 (fresh Friday signal — BUY: 2.66× weekly, month 4.34×, ladder rising; stop ₹3,695.50; charges ₹0.01)
2020-04-27  CADILAHC    BUY ₹8.90 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 4.52×, ladder rising; stop ₹310.03; charges ₹0.01)
2020-04-27  SYNGENE     BUY ₹8.91 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.67×, ladder rising; stop ₹285.95; charges ₹0.01)
2020-04-27  TAJGVK      BUY ₹8.90 at ₹133.40 (fresh Friday signal — BUY: 6.65× weekly, month 2.45×, ladder rising; stop ₹106.49; charges ₹0.01)
2020-05-04  AXISGOLD    PYRAMID BUY ₹9.30 at ₹4,271.70 (box jump — doubling the stake with NEW capital; stop stays ₹3,943.45; charges ₹0.01)
2020-05-04  HDFCMFGETF  PYRAMID BUY ₹8.82 at ₹4,376.95 (box jump — doubling the stake with NEW capital; stop stays ₹4,037.50; charges ₹0.01)
2020-05-11  EIDPARRY    BUY ₹10.57 at ₹164.00 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 1.53×, ladder rising; stop ₹132.60; charges ₹0.01)
2020-05-11  MANGCHEFER  BUY ₹10.57 at ₹33.75 (fresh Friday signal — BUY: 2.54× weekly, month 2.97×, ladder rising; stop ₹29.50; charges ₹0.01)
2020-05-18  DEEPAKNTR   PYRAMID BUY ₹9.70 at ₹521.95 (box jump — doubling the stake with NEW capital; stop stays ₹474.05; charges ₹0.01)
2020-05-18  MANGCHEFER  PYRAMID BUY ₹10.68 at ₹34.15 (box jump — doubling the stake with NEW capital; stop stays ₹30.64; charges ₹0.01)
2020-05-18  TAJGVK      PYRAMID BUY ₹8.47 at ₹127.05 (box jump — doubling the stake with NEW capital; stop stays ₹107.73; charges ₹0.01)
2020-06-08  CADILAHC    PYRAMID BUY ₹9.69 at ₹360.00 (box jump — doubling the stake with NEW capital; stop stays ₹316.35; charges ₹0.01)
2020-06-08  SYNGENE     PYRAMID BUY ₹10.43 at ₹373.90 (box jump — doubling the stake with NEW capital; stop stays ₹323.19; charges ₹0.01)
2020-06-12  DEEPAKNTR   SELL ₹17.59 at stop ₹474.05 (-4.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.79 of doubled capital and its returns OUT to the pocket
2020-06-15  PANACEABIO  BUY ₹13.95 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.27×, ladder rising; stop ₹114.11; charges ₹0.02)
2020-06-22  CADILAHC    PYRAMID BUY ₹19.68 at ₹365.95 (box jump — doubling the stake with NEW capital; stop stays ₹338.53; charges ₹0.02)
2020-06-22  EIDPARRY    PYRAMID BUY ₹17.21 at ₹267.45 (box jump — doubling the stake with NEW capital; stop stays ₹204.49; charges ₹0.02)
2020-06-22  MANGCHEFER  PYRAMID BUY ₹22.89 at ₹36.60 (box jump — doubling the stake with NEW capital; stop stays ₹33.73; charges ₹0.03)
2020-06-22  TAJGVK      PYRAMID BUY ₹20.74 at ₹155.70 (box jump — doubling the stake with NEW capital; stop stays ₹126.45; funded ₹8.79 from the pocket + ₹11.95 fresh; charges ₹0.02)
2020-06-29  PANACEABIO  PYRAMID BUY ₹12.36 at ₹204.00 (box jump — doubling the stake with NEW capital; stop stays ₹169.29; charges ₹0.01)
2020-07-06  EIDPARRY    PYRAMID BUY ₹34.21 at ₹266.00 (box jump — doubling the stake with NEW capital; stop stays ₹249.19; charges ₹0.04)
2020-07-06  SYNGENE     PYRAMID BUY ₹24.42 at ₹438.00 (box jump — doubling the stake with NEW capital; stop stays ₹378.10; charges ₹0.03)
2020-07-13  AXISGOLD    PYRAMID BUY ₹18.68 at ₹4,295.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,971.05; charges ₹0.02)
2020-07-23  AXISGOLD    SELL ₹34.49 at stop ₹3,971.05 (-6.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹25.86 of doubled capital and its returns OUT to the pocket
2020-07-27  EIDPARRY    PYRAMID BUY ₹75.59 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹273.03; funded ₹25.86 from the pocket + ₹49.73 fresh; charges ₹0.09)
2020-07-31  MANGCHEFER  SELL ₹42.11 at stop ₹33.73 (-4.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹31.57 of doubled capital and its returns OUT to the pocket
2020-08-03  PANACEABIO  PYRAMID BUY ₹27.60 at ₹227.95 (box jump — doubling the stake with NEW capital; stop stays ₹184.01; funded ₹27.60 from the pocket + ₹0.00 fresh; charges ₹0.03)
2020-08-10  HDFCMFGETF  PYRAMID BUY ₹20.10 at ₹4,989.95 (box jump — doubling the stake with NEW capital; stop stays ₹4,492.07; funded ₹3.98 from the pocket + ₹16.13 fresh; charges ₹0.02)
2020-08-17  CADILAHC    PYRAMID BUY ₹42.92 at ₹399.15 (box jump — doubling the stake with NEW capital; stop stays ₹364.99; charges ₹0.05)
2020-08-17  EIDPARRY    SELL ₹140.17 at stop ₹273.03 (+2.1%, charges ₹0.15) — the cash goes back to work at the next Friday screen; ₹122.61 of doubled capital and its returns OUT to the pocket
2020-08-17  SYNGENE     PYRAMID BUY ₹55.02 at ₹493.80 (box jump — doubling the stake with NEW capital; stop stays ₹434.44; charges ₹0.07)
2020-08-20  PANACEABIO  SELL ₹44.48 at stop ₹184.01 (-17.3%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹33.35 of doubled capital and its returns OUT to the pocket
2020-08-24  ADVENZYMES  BUY ₹33.44 at ₹241.50 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.06× weekly, month 7.95×, ladder rising; stop ₹194.75; charges ₹0.04)
2020-08-24  GOLDBEES    PYRAMID BUY ₹9.90 at ₹46.45 (box jump — doubling the stake with NEW capital; stop stays ₹41.00; funded ₹9.90 from the pocket + ₹0.00 fresh; charges ₹0.01)
2020-09-04  GOLDBEES    SELL ₹17.44 at stop ₹41.00 (-6.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹8.72 of doubled capital and its returns OUT to the pocket
2020-09-07  POLYMED     BUY ₹23.14 at ₹449.70 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.13× weekly, month 2.67×, ladder rising; stop ₹372.40; charges ₹0.03)
2020-09-08  CADILAHC    SELL ₹78.36 at stop ₹364.99 (-3.3%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹68.55 of doubled capital and its returns OUT to the pocket
2020-09-14  POLYMED     PYRAMID BUY ₹24.77 at ₹481.95 (box jump — doubling the stake with NEW capital; stop stays ₹408.50; funded ₹24.77 from the pocket + ₹0.00 fresh; charges ₹0.03)
2020-09-21  ADVENZYMES  PYRAMID BUY ₹34.97 at ₹252.85 (box jump — doubling the stake with NEW capital; stop stays ₹212.37; funded ₹34.97 from the pocket + ₹0.00 fresh; charges ₹0.04)
2020-09-22  TAJGVK      SELL ₹33.63 at stop ₹126.45 (-11.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹25.21 of doubled capital and its returns OUT to the pocket
2020-09-23  HDFCMFGETF  SELL ₹36.14 at stop ₹4,492.07 (-4.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹27.09 of doubled capital and its returns OUT to the pocket
2020-09-28  SAKSOFT     BUY ₹27.27 at ₹398.70 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.03)
2020-10-05  POLYMED     PYRAMID BUY ₹48.33 at ₹470.35 (box jump — doubling the stake with NEW capital; stop stays ₹420.11; funded ₹48.33 from the pocket + ₹0.00 fresh; charges ₹0.06)
2020-10-26  ADVENZYMES  PYRAMID BUY ₹87.20 at ₹315.40 (box jump — doubling the stake with NEW capital; stop stays ₹292.33; funded ₹87.20 from the pocket + ₹0.00 fresh; charges ₹0.10)
2020-11-03  ADVENZYMES  SELL ₹161.37 at stop ₹292.33 (+3.9%, charges ₹0.17) — the cash goes back to work at the next Friday screen; ₹120.98 of doubled capital and its returns OUT to the pocket
2020-11-09  LASA        BUY ₹28.44 at ₹80.50 (fresh Friday signal — BUY: 3.08× weekly, month 3.28×, ladder rising; stop ₹65.41; charges ₹0.03)
2020-11-23  LASA        PYRAMID BUY ₹27.53 at ₹78.00 (box jump — doubling the stake with NEW capital; stop stays ₹71.68; funded ₹27.53 from the pocket + ₹0.00 fresh; charges ₹0.03)
2020-12-07  LASA        PYRAMID BUY ₹60.24 at ₹85.40 (box jump — doubling the stake with NEW capital; stop stays ₹77.95; funded ₹60.24 from the pocket + ₹0.00 fresh; charges ₹0.07)
2020-12-21  LASA        SELL ₹109.79 at stop ₹77.95 (-5.3%, charges ₹0.11) — the cash goes back to work at the next Friday screen; ₹82.31 of doubled capital and its returns OUT to the pocket
2020-12-22  SYNGENE     SELL ₹125.13 at stop ₹562.40 (+27.0%, charges ₹0.13) — the cash goes back to work at the next Friday screen; ₹109.46 of doubled capital and its returns OUT to the pocket
2020-12-28  BORORENEW   BUY ₹18.87 at ₹235.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.97× weekly, month 3.28×, ladder rising; stop ₹148.20; charges ₹0.02)
2020-12-28  KIRIINDUS   BUY ₹18.90 at ₹537.55 (fresh Friday signal — starved 1×, front of the queue — BUY: 8.73× weekly, month 2.26×, ladder rising; stop ₹424.46; charges ₹0.02)
2020-12-28  XCHANGING   BUY ₹17.33 at ₹88.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 3.95× weekly, month 3.92×, ladder rising; stop ₹71.32; charges ₹0.02)
2021-01-04  KIRIINDUS   PYRAMID BUY ₹18.97 at ₹540.00 (box jump — doubling the stake with NEW capital; stop stays ₹478.56; funded ₹18.97 from the pocket + ₹0.00 fresh; charges ₹0.02)
2021-01-18  BORORENEW   PYRAMID BUY ₹22.05 at ₹275.00 (box jump — doubling the stake with NEW capital; stop stays ₹247.59; funded ₹22.05 from the pocket + ₹0.00 fresh; charges ₹0.03)
2021-01-18  SAKSOFT     PYRAMID BUY ₹25.02 at ₹366.25 (box jump — doubling the stake with NEW capital; stop stays ₹341.10; funded ₹25.02 from the pocket + ₹0.00 fresh; charges ₹0.03)
2021-01-18  XCHANGING   PYRAMID BUY ₹18.19 at ₹92.50 (box jump — doubling the stake with NEW capital; stop stays ₹80.75; funded ₹18.19 from the pocket + ₹0.00 fresh; charges ₹0.02)
2021-01-20  BORORENEW   SELL ₹39.64 at stop ₹247.59 (-2.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹19.81 of doubled capital and its returns OUT to the pocket
2021-01-21  KIRIINDUS   SELL ₹33.56 at stop ₹478.56 (-11.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹16.77 of doubled capital and its returns OUT to the pocket
2021-01-25  HINDZINC    BUY ₹14.40 at ₹277.40 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.32× weekly, month 2.11×, ladder rising; stop ₹248.97; charges ₹0.02)
2021-01-25  INDIAMART   BUY ₹22.22 at ₹3,990.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.37× weekly, month 1.58×, ladder rising; stop ₹3,323.19; charges ₹0.03)
2021-01-25  SAKSOFT     SELL ₹46.54 at stop ₹341.10 (-10.8%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹23.25 of doubled capital and its returns OUT to the pocket
2021-01-25  XCHANGING   SELL ₹31.71 at stop ₹80.75 (-10.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹15.85 of doubled capital and its returns OUT to the pocket
2021-02-01  APTECHT     BUY ₹20.39 at ₹178.45 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.02)
2021-02-01  GAEL        BUY ₹18.76 at ₹71.47 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.02)
2021-02-01  INDIAMART   PYRAMID BUY ₹21.86 at ₹3,929.07 (box jump — doubling the stake with NEW capital; stop stays ₹3,460.38; funded ₹21.86 from the pocket + ₹0.00 fresh; charges ₹0.03)
2021-02-08  APTECHT     PYRAMID BUY ₹24.65 at ₹216.00 (box jump — doubling the stake with NEW capital; stop stays ₹163.06; funded ₹24.65 from the pocket + ₹0.00 fresh; charges ₹0.03)
2021-02-15  APTECHT     PYRAMID BUY ₹54.22 at ₹237.70 (box jump — doubling the stake with NEW capital; stop stays ₹197.36; funded ₹54.22 from the pocket + ₹0.00 fresh; charges ₹0.06)
2021-02-15  HINDZINC    PYRAMID BUY ₹15.56 at ₹300.10 (box jump — doubling the stake with NEW capital; stop stays ₹279.30; funded ₹15.56 from the pocket + ₹0.00 fresh; charges ₹0.02)
2021-02-15  INDIAMART   PYRAMID BUY ₹51.53 at ₹4,634.30 (box jump — doubling the stake with NEW capital; stop stays ₹4,137.25; funded ₹51.53 from the pocket + ₹0.00 fresh; charges ₹0.06)
2021-02-23  GAEL        SELL ₹16.42 at stop ₹62.70 (-12.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-03-02  INDIAMART   SELL ₹91.85 at stop ₹4,137.25 (-3.7%, charges ₹0.10) — the cash goes back to work at the next Friday screen; ₹68.86 of doubled capital and its returns OUT to the pocket
2021-03-08  APTECHT     PYRAMID BUY ₹101.22 at ₹222.00 (box jump — doubling the stake with NEW capital; stop stays ₹204.25; funded ₹50.20 from the pocket + ₹51.02 fresh; charges ₹0.12)
2021-03-08  BAJAJHIND   BUY ₹39.41 at ₹7.80 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.45× weekly, month 2.79×, ladder rising; stop ₹4.40; charges ₹0.05)
2021-03-08  POLYMED     PYRAMID BUY ₹147.64 at ₹718.90 (box jump — doubling the stake with NEW capital; stop stays ₹642.77; funded ₹147.64 from the pocket + ₹0.00 fresh; charges ₹0.17)
2021-03-19  APTECHT     SELL ₹185.94 at stop ₹204.25 (-7.0%, charges ₹0.19) — the cash goes back to work at the next Friday screen; ₹162.66 of doubled capital and its returns OUT to the pocket
2021-03-19  HINDZINC    SELL ₹28.92 at stop ₹279.30 (-3.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹14.45 of doubled capital and its returns OUT to the pocket
2021-03-22  VIDHIING    BUY ₹37.75 at ₹194.70 (fresh Friday signal — starved 1×, front of the queue — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.04)
2021-03-30  BAJAJHIND   PYRAMID BUY ₹31.79 at ₹6.30 (box jump — doubling the stake with NEW capital; stop stays ₹5.51; funded ₹31.79 from the pocket + ₹0.00 fresh; charges ₹0.04)
2021-04-01  BAJAJHIND   TRIM 0.1% (₹0.03 at ₹6.40) to pay the tax bill
2021-04-01  POLYMED     TRIM 0.1% (₹0.18 at ₹837.20) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹0.23 paid (STCG ₹1.15 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 0.1% (₹0.02 at ₹207.10) to pay the tax bill
2021-04-05  VIDHIING    PYRAMID BUY ₹39.51 at ₹204.10 (box jump — doubling the stake with NEW capital; stop stays ₹168.12; funded ₹39.51 from the pocket + ₹0.00 fresh; charges ₹0.05)
2021-05-24  VIDHIING    PYRAMID BUY ₹78.93 at ₹204.00 (box jump — doubling the stake with NEW capital; stop stays ₹182.64; funded ₹78.93 from the pocket + ₹0.00 fresh; charges ₹0.09)
2021-05-31  BAJAJHIND   PYRAMID BUY ₹110.90 at ₹11.00 (box jump — doubling the stake with NEW capital; stop stays ₹9.54; funded ₹26.87 from the pocket + ₹84.03 fresh; charges ₹0.13)
2021-06-14  POLYMED     SELL ₹389.38 at stop ₹950.00 (+60.1%, charges ₹0.40) — the cash goes back to work at the next Friday screen; ₹340.62 of doubled capital and its returns OUT to the pocket
2021-06-18  VIDHIING    SELL ₹141.11 at stop ₹182.64 (-9.4%, charges ₹0.15) — the cash goes back to work at the next Friday screen; ₹105.79 of doubled capital and its returns OUT to the pocket
2021-06-21  DECCANCE    BUY ₹42.01 at ₹546.40 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.95× weekly, month 1.68×, ladder rising; stop ₹497.80; charges ₹0.05)
2021-06-21  KESORAMIND  BUY ₹42.06 at ₹81.80 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.61× weekly, month 2.62×, ladder rising; stop ₹73.21; charges ₹0.05)
2021-06-28  BAJAJHIND   PYRAMID BUY ₹372.82 at ₹18.50 (box jump — doubling the stake with NEW capital; stop stays ₹13.96; funded ₹372.82 from the pocket + ₹0.00 fresh; charges ₹0.44)
2021-07-05  KESORAMIND  PYRAMID BUY ₹47.33 at ₹92.15 (box jump — doubling the stake with NEW capital; stop stays ₹85.78; funded ₹47.33 from the pocket + ₹0.00 fresh; charges ₹0.06)
2021-07-12  DECCANCE    PYRAMID BUY ₹48.77 at ₹635.00 (box jump — doubling the stake with NEW capital; stop stays ₹548.20; funded ₹26.26 from the pocket + ₹22.51 fresh; charges ₹0.06)
2021-08-10  KESORAMIND  SELL ₹87.97 at stop ₹85.78 (-1.4%, charges ₹0.09) — the cash goes back to work at the next Friday screen; ₹43.96 of doubled capital and its returns OUT to the pocket
2021-08-16  DECCANCE    PYRAMID BUY ₹123.12 at ₹802.00 (box jump — doubling the stake with NEW capital; stop stays ₹620.61; funded ₹43.96 from the pocket + ₹79.16 fresh; charges ₹0.15)
2021-10-18  NETWORK18   BUY ₹44.01 at ₹80.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.54× weekly, month 2.23×, ladder rising; stop ₹55.91; charges ₹0.05)
2021-10-19  BAJAJHIND   SELL ₹561.74 at stop ₹13.96 (+1.5%, charges ₹0.58) — the cash goes back to work at the next Friday screen; ₹491.40 of doubled capital and its returns OUT to the pocket
2021-10-25  LTI         BUY ₹33.74 at ₹6,555.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.63× weekly, month 1.84×, ladder rising; stop ₹5,353.77; charges ₹0.04)
2021-10-25  NETWORK18   PYRAMID BUY ₹43.35 at ₹78.90 (box jump — doubling the stake with NEW capital; stop stays ₹72.52; funded ₹43.35 from the pocket + ₹0.00 fresh; charges ₹0.05)
2021-10-25  TATAMTRDVR  BUY ₹36.60 at ₹252.40 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.45× weekly, month 2.17×, ladder rising; stop ₹169.19; charges ₹0.04)
2021-11-01  LTI         PYRAMID BUY ₹34.55 at ₹6,720.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,950.99; funded ₹34.55 from the pocket + ₹0.00 fresh; charges ₹0.04)
2021-11-01  TATAMTRDVR  PYRAMID BUY ₹36.17 at ₹249.75 (box jump — doubling the stake with NEW capital; stop stays ₹204.73; funded ₹36.17 from the pocket + ₹0.00 fresh; charges ₹0.04)
2021-11-22  DECCANCE    SELL ₹190.23 at stop ₹620.61 (-10.9%, charges ₹0.20) — the cash goes back to work at the next Friday screen; ₹142.62 of doubled capital and its returns OUT to the pocket
2021-11-22  TATAMTRDVR  PYRAMID BUY ₹83.06 at ₹286.90 (box jump — doubling the stake with NEW capital; stop stays ₹265.05; funded ₹83.06 from the pocket + ₹0.00 fresh; charges ₹0.10)
2021-11-22  TATAMTRDVR  SELL ₹153.22 at stop ₹265.05 (-1.5%, charges ₹0.16) — the cash goes back to work at the next Friday screen; ₹114.87 of doubled capital and its returns OUT to the pocket
2021-11-29  BCG         BUY ₹24.96 at ₹134.10 (fresh Friday signal — BUY: 1.94× weekly, month 1.58×, ladder rising; stop ₹55.00; charges ₹0.03)
2021-11-29  BSOFT       BUY ₹30.66 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.04)
2021-11-29  LTI         PYRAMID BUY ₹67.11 at ₹6,530.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,270.00; funded ₹67.11 from the pocket + ₹0.00 fresh; charges ₹0.08)
2021-11-29  NETWORK18   SELL ₹79.57 at stop ₹72.52 (-8.7%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹39.76 of doubled capital and its returns OUT to the pocket
2021-11-29  RAYMOND     BUY ₹30.34 at ₹596.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.04)
2021-12-06  BSOFT       PYRAMID BUY ₹31.92 at ₹485.00 (box jump — doubling the stake with NEW capital; stop stays ₹424.65; funded ₹31.92 from the pocket + ₹0.00 fresh; charges ₹0.04)
2021-12-06  SFL         BUY ₹29.08 at ₹3,417.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.40× weekly, month 2.05×, ladder rising; stop ₹2,838.79; charges ₹0.03)
2021-12-13  RAYMOND     PYRAMID BUY ₹33.61 at ₹661.00 (box jump — doubling the stake with NEW capital; stop stays ₹560.88; funded ₹33.61 from the pocket + ₹0.00 fresh; charges ₹0.04)
2022-01-03  SFL         PYRAMID BUY ₹27.84 at ₹3,274.90 (box jump — doubling the stake with NEW capital; stop stays ₹2,840.55; funded ₹27.84 from the pocket + ₹0.00 fresh; charges ₹0.03)
2022-01-24  LTI         SELL ₹128.66 at stop ₹6,270.00 (-4.8%, charges ₹0.13) — the cash goes back to work at the next Friday screen; ₹96.46 of doubled capital and its returns OUT to the pocket
2022-01-31  SHARDACROP  BUY ₹26.26 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.03)
2022-01-31  TV18BRDCST  BUY ₹16.67 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.02)
2022-02-07  RAYMOND     PYRAMID BUY ₹79.08 at ₹778.00 (box jump — doubling the stake with NEW capital; stop stays ₹679.35; funded ₹79.08 from the pocket + ₹0.00 fresh; charges ₹0.09)
2022-02-07  SFL         PYRAMID BUY ₹56.91 at ₹3,349.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,922.75; funded ₹56.91 from the pocket + ₹0.00 fresh; charges ₹0.07)
2022-02-07  SHARDACROP  PYRAMID BUY ₹29.51 at ₹660.10 (box jump — doubling the stake with NEW capital; stop stays ₹545.30; funded ₹29.51 from the pocket + ₹0.00 fresh; charges ₹0.03)
2022-02-07  TV18BRDCST  PYRAMID BUY ₹18.38 at ₹65.00 (box jump — doubling the stake with NEW capital; stop stays ₹53.30; funded ₹18.38 from the pocket + ₹0.00 fresh; charges ₹0.02)
2022-02-11  SHARDACROP  SELL ₹48.67 at stop ₹545.30 (-12.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹24.32 of doubled capital and its returns OUT to the pocket
2022-02-14  BSOFT       SELL ₹55.81 at stop ₹424.65 (-10.6%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹27.89 of doubled capital and its returns OUT to the pocket
2022-02-14  GNFC        BUY ₹24.35 at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹0.03)
2022-02-15  RAYMOND     SELL ₹137.88 at stop ₹679.35 (-3.4%, charges ₹0.14) — the cash goes back to work at the next Friday screen; ₹103.37 of doubled capital and its returns OUT to the pocket
2022-02-21  EVERESTIND  BUY ₹31.42 at ₹740.00 (fresh Friday signal — BUY: 3.34× weekly, month 1.68×, ladder rising; stop ₹522.67; charges ₹0.04)
2022-02-21  GNFC        PYRAMID BUY ₹24.10 at ₹548.00 (box jump — doubling the stake with NEW capital; stop stays ₹497.80; funded ₹24.10 from the pocket + ₹0.00 fresh; charges ₹0.03)
2022-02-21  TV18BRDCST  PYRAMID BUY ₹37.01 at ₹65.50 (box jump — doubling the stake with NEW capital; stop stays ₹58.38; funded ₹37.01 from the pocket + ₹0.00 fresh; charges ₹0.04)
2022-02-22  TV18BRDCST  SELL ₹65.87 at stop ₹58.38 (-8.4%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹49.38 of doubled capital and its returns OUT to the pocket
2022-03-07  EVERESTIND  PYRAMID BUY ₹26.29 at ₹620.00 (box jump — doubling the stake with NEW capital; stop stays ₹526.21; funded ₹26.29 from the pocket + ₹0.00 fresh; charges ₹0.03)
2022-03-07  EXCELINDUS  BUY ₹41.23 at ₹1,523.00 (fresh Friday signal — BUY: 6.93× weekly, month 5.51×, ladder rising; stop ₹1,016.01; charges ₹0.05)
2022-03-07  SFL         PYRAMID BUY ₹113.78 at ₹3,350.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,993.45; funded ₹113.78 from the pocket + ₹0.00 fresh; charges ₹0.13)
2022-03-21  EXCELINDUS  PYRAMID BUY ₹45.53 at ₹1,683.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,438.30; funded ₹45.53 from the pocket + ₹0.00 fresh; charges ₹0.05)
2022-03-28  EVERESTIND  PYRAMID BUY ₹61.88 at ₹730.00 (box jump — doubling the stake with NEW capital; stop stays ₹594.70; funded ₹61.88 from the pocket + ₹0.00 fresh; charges ₹0.07)
2022-03-29  EXCELINDUS  SELL ₹77.66 at stop ₹1,438.30 (-10.3%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹38.81 of doubled capital and its returns OUT to the pocket
2022-04-01  TAX         FY2022 settled: ₹11.15 paid (STCG ₹55.77 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  RCF         BUY ₹33.97 at ₹96.40 (fresh Friday signal — starved 1×, front of the queue — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.04)
2022-04-25  GNFC        PYRAMID BUY ₹74.41 at ₹846.40 (box jump — doubling the stake with NEW capital; stop stays ₹792.16; funded ₹74.41 from the pocket + ₹0.00 fresh; charges ₹0.09)
2022-04-25  RCF         PYRAMID BUY ₹36.67 at ₹104.20 (box jump — doubling the stake with NEW capital; stop stays ₹93.15; funded ₹36.67 from the pocket + ₹0.00 fresh; charges ₹0.04)
2022-04-27  SFL         SELL ₹238.71 at stop ₹3,519.94 (+5.1%, charges ₹0.25) — the cash goes back to work at the next Friday screen; ₹208.82 of doubled capital and its returns OUT to the pocket
2022-04-28  EVERESTIND  SELL ₹100.65 at stop ₹594.70 (-15.6%, charges ₹0.10) — the cash goes back to work at the next Friday screen; ₹75.46 of doubled capital and its returns OUT to the pocket
2022-05-02  ORISSAMINE  BUY ₹26.69 at ₹3,379.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.63× weekly, month 1.78×, ladder rising; stop ₹2,898.50; charges ₹0.03)
2022-05-02  RIIL        BUY ₹28.40 at ₹1,100.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.17× weekly, month 3.64×, ladder rising; stop ₹852.81; charges ₹0.03)
2022-05-04  RCF         SELL ₹65.46 at stop ₹93.15 (-7.1%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹32.71 of doubled capital and its returns OUT to the pocket
2022-05-06  GNFC        SELL ₹139.05 at stop ₹792.16 (+13.4%, charges ₹0.14) — the cash goes back to work at the next Friday screen; ₹104.25 of doubled capital and its returns OUT to the pocket
2022-05-09  GEPIL       BUY ₹13.22 at ₹182.65 (fresh Friday signal — ACCUMULATE: 1.55× weekly, month 2.61×, ladder rising; stop ₹163.45; charges ₹0.02)
2022-05-09  JKIL        BUY ₹13.35 at ₹229.70 (fresh Friday signal — BUY: 6.96× weekly, month 3.58×, ladder rising; stop ₹192.28; charges ₹0.02)
2022-05-09  MOL         BUY ₹13.36 at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹0.02)
2022-05-09  MRPL        BUY ₹13.29 at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹0.02)
2022-05-11  MOL         SELL ₹11.67 at stop ₹113.62 (-12.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-05-11  ORISSAMINE  SELL ₹22.84 at stop ₹2,898.50 (-14.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹12.49 at ₹220.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.01)
2022-05-23  ACC         BUY ₹18.09 at ₹2,260.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹0.02)
2022-05-23  GRAUWEIL    BUY ₹18.05 at ₹82.70 (fresh Friday signal — BUY: 5.06× weekly, month 7.54×, ladder rising; stop ₹56.42; charges ₹0.02)
2022-05-23  JKIL        PYRAMID BUY ₹13.35 at ₹230.00 (box jump — doubling the stake with NEW capital; stop stays ₹196.02; funded ₹13.35 from the pocket + ₹0.00 fresh; charges ₹0.02)
2022-05-23  MRPL        PYRAMID BUY ₹16.14 at ₹94.80 (box jump — doubling the stake with NEW capital; stop stays ₹60.81; funded ₹16.14 from the pocket + ₹0.00 fresh; charges ₹0.02)
2022-05-23  RIIL        PYRAMID BUY ₹26.82 at ₹1,040.00 (box jump — doubling the stake with NEW capital; stop stays ₹863.73; funded ₹26.82 from the pocket + ₹0.00 fresh; charges ₹0.03)
2022-05-26  RIIL        SELL ₹44.47 at stop ₹863.73 (-19.3%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹22.22 of doubled capital and its returns OUT to the pocket
2022-05-31  GEPIL       SELL ₹11.80 at stop ₹163.45 (-10.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-06-06  BCG         SELL ₹10.22 at stop ₹55.00 (-59.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-06-06  GRAUWEIL    PYRAMID BUY ₹15.34 at ₹70.35 (box jump — doubling the stake with NEW capital; stop stays ₹61.82; funded ₹15.34 from the pocket + ₹0.00 fresh; charges ₹0.02)
2022-06-06  MRPL        PYRAMID BUY ₹30.06 at ₹88.35 (box jump — doubling the stake with NEW capital; stop stays ₹69.61; funded ₹30.06 from the pocket + ₹0.00 fresh; charges ₹0.04)
2022-06-06  SHANTIGEAR  BUY ₹19.09 at ₹238.05 (fresh Friday signal — BUY: 1.57× weekly, month 2.31×, ladder rising; stop ₹179.53; charges ₹0.02)
2022-06-06  VBL         SELL ₹11.12 at stop ₹196.27 (-10.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹12.52 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.01)
2022-06-13  GRAUWEIL    SELL ₹26.91 at stop ₹61.82 (-19.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹13.45 of doubled capital and its returns OUT to the pocket
2022-06-13  JKIL        PYRAMID BUY ₹33.37 at ₹287.70 (box jump — doubling the stake with NEW capital; stop stays ₹233.94; funded ₹33.37 from the pocket + ₹0.00 fresh; charges ₹0.04)
2022-06-13  VADILALIND  BUY ₹23.99 at ₹2,088.90 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.72× weekly, month 1.81×, ladder rising; stop ₹1,466.28; charges ₹0.03)
2022-06-20  APARINDS    BUY ₹13.46 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.02)
2022-06-20  ELECON      PYRAMID BUY ₹13.40 at ₹131.25 (box jump — doubling the stake with NEW capital; stop stays ₹111.01; funded ₹13.40 from the pocket + ₹0.00 fresh; charges ₹0.02)
2022-06-27  VADILALIND  PYRAMID BUY ₹22.65 at ₹1,975.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,602.19; funded ₹22.65 from the pocket + ₹0.00 fresh; charges ₹0.03)
2022-07-04  APARINDS    PYRAMID BUY ₹13.87 at ₹980.00 (box jump — doubling the stake with NEW capital; stop stays ₹844.03; funded ₹13.87 from the pocket + ₹0.00 fresh; charges ₹0.02)
2022-07-06  MRPL        SELL ₹47.29 at stop ₹69.61 (-20.3%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹35.45 of doubled capital and its returns OUT to the pocket
2022-07-11  ELECON      PYRAMID BUY ₹30.00 at ₹147.00 (box jump — doubling the stake with NEW capital; stop stays ₹120.65; funded ₹30.00 from the pocket + ₹0.00 fresh; charges ₹0.04)
2022-07-11  VADILALIND  PYRAMID BUY ₹47.83 at ₹2,086.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,877.25; funded ₹47.83 from the pocket + ₹0.00 fresh; charges ₹0.06)
2022-07-18  ACC         PYRAMID BUY ₹17.28 at ₹2,160.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,030.06; funded ₹17.28 from the pocket + ₹0.00 fresh; charges ₹0.02)
2022-07-25  ELECON      PYRAMID BUY ₹67.71 at ₹165.95 (box jump — doubling the stake with NEW capital; stop stays ₹142.64; funded ₹67.71 from the pocket + ₹0.00 fresh; charges ₹0.08)
2022-07-25  VADILALIND  PYRAMID BUY ₹94.91 at ₹2,071.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,924.70; funded ₹94.91 from the pocket + ₹0.00 fresh; charges ₹0.11)
2022-08-01  JKIL        PYRAMID BUY ₹78.49 at ₹338.50 (box jump — doubling the stake with NEW capital; stop stays ₹308.80; funded ₹78.49 from the pocket + ₹0.00 fresh; charges ₹0.09)
2022-08-05  JKIL        SELL ₹142.97 at stop ₹308.80 (+3.4%, charges ₹0.15) — the cash goes back to work at the next Friday screen; ₹125.07 of doubled capital and its returns OUT to the pocket
2022-08-08  ACC         PYRAMID BUY ₹36.12 at ₹2,260.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,053.90; funded ₹36.12 from the pocket + ₹0.00 fresh; charges ₹0.04)
2022-08-08  NAVNETEDUL  BUY ₹29.74 at ₹130.50 (fresh Friday signal — BUY: 14.73× weekly, month 3.84×, ladder rising; stop ₹88.40; charges ₹0.04)
2022-08-16  ACC         PYRAMID BUY ₹71.81 at ₹2,248.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,085.11; funded ₹71.81 from the pocket + ₹0.00 fresh; charges ₹0.09)
2022-08-22  APARINDS    PYRAMID BUY ₹34.17 at ₹1,208.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,095.35; funded ₹34.17 from the pocket + ₹0.00 fresh; charges ₹0.04)
2022-08-22  NAVNETEDUL  PYRAMID BUY ₹29.36 at ₹129.00 (box jump — doubling the stake with NEW capital; stop stays ₹116.38; funded ₹29.36 from the pocket + ₹0.00 fresh; charges ₹0.03)
2022-09-05  NAVNETEDUL  PYRAMID BUY ₹62.97 at ₹138.40 (box jump — doubling the stake with NEW capital; stop stays ₹125.88; funded ₹62.97 from the pocket + ₹0.00 fresh; charges ₹0.07)
2022-09-05  SHANTIGEAR  PYRAMID BUY ₹22.91 at ₹286.00 (box jump — doubling the stake with NEW capital; stop stays ₹253.27; funded ₹22.91 from the pocket + ₹0.00 fresh; charges ₹0.03)
2022-09-12  APARINDS    PYRAMID BUY ₹69.44 at ₹1,228.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,108.54; funded ₹6.58 from the pocket + ₹62.86 fresh; charges ₹0.08)
2022-09-19  SHANTIGEAR  PYRAMID BUY ₹49.95 at ₹312.00 (box jump — doubling the stake with NEW capital; stop stays ₹289.75; charges ₹0.06)
2022-09-26  NAVNETEDUL  PYRAMID BUY ₹122.27 at ₹134.45 (box jump — doubling the stake with NEW capital; stop stays ₹127.30; charges ₹0.14)
2022-09-26  NAVNETEDUL  SELL ₹231.16 at stop ₹127.30 (-5.2%, charges ₹0.24) — the cash goes back to work at the next Friday screen; ₹202.21 of doubled capital and its returns OUT to the pocket
2022-10-10  SHANTIGEAR  PYRAMID BUY ₹109.48 at ₹342.15 (box jump — doubling the stake with NEW capital; stop stays ₹301.39; funded ₹109.48 from the pocket + ₹0.00 fresh; charges ₹0.13)
2022-10-20  VADILALIND  SELL ₹210.01 at stop ₹2,295.06 (+11.1%, charges ₹0.22) — the cash goes back to work at the next Friday screen; ₹183.71 of doubled capital and its returns OUT to the pocket
2022-10-24  JTLINFRA    BUY ₹55.24 at ₹292.00 (fresh Friday signal — ACCUMULATE: 5.50× weekly, month 7.34×, ladder rising; stop ₹217.12; charges ₹0.07)
2022-11-03  APARINDS    SELL ₹153.39 at stop ₹1,358.50 (+17.4%, charges ₹0.16) — the cash goes back to work at the next Friday screen; ₹134.18 of doubled capital and its returns OUT to the pocket
2022-12-21  ELECON      SELL ₹164.96 at stop ₹202.49 (+33.7%, charges ₹0.17) — the cash goes back to work at the next Friday screen; ₹144.30 of doubled capital and its returns OUT to the pocket
2022-12-22  SHANTIGEAR  SELL ₹220.79 at stop ₹345.56 (+9.9%, charges ₹0.23) — the cash goes back to work at the next Friday screen; ₹193.14 of doubled capital and its returns OUT to the pocket
2022-12-23  ACC         SELL ₹157.24 at stop ₹2,465.16 (+10.0%, charges ₹0.16) — the cash goes back to work at the next Friday screen; ₹137.55 of doubled capital and its returns OUT to the pocket
2023-01-02  GICRE       BUY ₹14.30 at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 11.18×, ladder rising; stop ₹137.57; charges ₹0.02)
2023-01-02  GSFC        BUY ₹14.44 at ₹140.70 (fresh Friday signal — ACCUMULATE: 2.14× weekly, month 1.67×, ladder rising; stop ₹111.58; charges ₹0.02)
2023-01-02  HARIOMPIPE  BUY ₹14.35 at ₹363.95 (fresh Friday signal — ACCUMULATE: 5.91× weekly, month 2.06×, ladder rising; stop ₹264.86; charges ₹0.02)
2023-01-02  IOB         BUY ₹14.33 at ₹32.40 (fresh Friday signal — ACCUMULATE: 4.77× weekly, month 30.16×, ladder rising; stop ₹21.23; charges ₹0.02)
2023-01-02  JSL         BUY ₹14.37 at ₹241.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.13×, ladder rising; stop ₹192.61; charges ₹0.02)
2023-01-02  SPIC        BUY ₹14.31 at ₹88.25 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.81× weekly, month 3.70×, ladder rising; stop ₹54.66; charges ₹0.02)
2023-01-16  GICRE       PYRAMID BUY ₹14.91 at ₹187.05 (box jump — doubling the stake with NEW capital; stop stays ₹167.72; funded ₹14.91 from the pocket + ₹0.00 fresh; charges ₹0.02)
2023-01-16  JSL         PYRAMID BUY ₹14.22 at ₹238.90 (box jump — doubling the stake with NEW capital; stop stays ₹218.83; funded ₹14.22 from the pocket + ₹0.00 fresh; charges ₹0.02)
2023-01-23  SPIC        PYRAMID BUY ₹12.71 at ₹78.50 (box jump — doubling the stake with NEW capital; stop stays ₹65.74; funded ₹12.71 from the pocket + ₹0.00 fresh; charges ₹0.02)
2023-02-01  GICRE       SELL ₹26.69 at stop ₹167.72 (-8.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹13.34 of doubled capital and its returns OUT to the pocket
2023-02-06  JINDALSAW   BUY ₹14.47 at ₹65.22 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.72× weekly, month 3.57×, ladder rising; stop ₹51.25; charges ₹0.02)
2023-02-13  HARIOMPIPE  PYRAMID BUY ₹16.74 at ₹425.00 (box jump — doubling the stake with NEW capital; stop stays ₹370.12; funded ₹16.74 from the pocket + ₹0.00 fresh; charges ₹0.02)
2023-02-20  HARIOMPIPE  PYRAMID BUY ₹33.16 at ₹421.25 (box jump — doubling the stake with NEW capital; stop stays ₹386.32; funded ₹33.16 from the pocket + ₹0.00 fresh; charges ₹0.04)
2023-02-23  SPIC        SELL ₹21.26 at stop ₹65.74 (-21.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹10.62 of doubled capital and its returns OUT to the pocket
2023-02-27  JSL         PYRAMID BUY ₹31.60 at ₹265.50 (box jump — doubling the stake with NEW capital; stop stays ₹235.03; funded ₹31.60 from the pocket + ₹0.00 fresh; charges ₹0.04)
2023-03-06  IOB         PYRAMID BUY ₹11.53 at ₹26.10 (box jump — doubling the stake with NEW capital; stop stays ₹22.18; funded ₹11.53 from the pocket + ₹0.00 fresh; charges ₹0.01)
2023-03-06  JINDALSAW   PYRAMID BUY ₹16.39 at ₹73.97 (box jump — doubling the stake with NEW capital; stop stays ₹67.92; funded ₹16.39 from the pocket + ₹0.00 fresh; charges ₹0.02)
2023-03-20  HARIOMPIPE  PYRAMID BUY ₹72.37 at ₹460.00 (box jump — doubling the stake with NEW capital; stop stays ₹399.00; funded ₹72.37 from the pocket + ₹0.00 fresh; charges ₹0.09)
2023-03-20  IOB         SELL ₹19.56 at stop ₹22.18 (-24.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen; ₹9.77 of doubled capital and its returns OUT to the pocket
2023-03-27  JINDALSAW   SELL ₹30.05 at stop ₹67.92 (-2.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen; ₹15.01 of doubled capital and its returns OUT to the pocket
2023-03-27  SONATSOFTW  BUY ₹20.42 at ₹413.70 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.76× weekly, month 4.94×, ladder rising; stop ₹371.45; charges ₹0.02)
2023-03-29  SONATSOFTW  SELL ₹18.30 at stop ₹371.45 (-10.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-04-03  CPSEETF     BUY ₹32.01 at ₹40.00 (fresh Friday signal — ACCUMULATE: 1.80× weekly, month 1.84×, ladder rising; stop ₹36.42; charges ₹0.04)
2023-04-03  TAX         FY2023 pocket settled: ₹4.87 paid from the doubling pocket (STCG ₹24.34 @20%, LTCG ₹0.00 @12.5%)
2023-04-03  TAX         FY2023 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹11.01 / LT ₹0.00)
2023-04-10  JSL         PYRAMID BUY ₹68.51 at ₹288.00 (box jump — doubling the stake with NEW capital; stop stays ₹256.98; funded ₹68.51 from the pocket + ₹0.00 fresh; charges ₹0.08)
2023-04-13  JSL         SELL ₹122.05 at stop ₹256.98 (-4.9%, charges ₹0.13) — the cash goes back to work at the next Friday screen; ₹106.77 of doubled capital and its returns OUT to the pocket
2023-04-17  ANURAS      BUY ₹16.60 at ₹995.20 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.48× weekly, month 5.24×, ladder rising; stop ₹691.46; charges ₹0.02)
2023-05-02  ANURAS      PYRAMID BUY ₹18.98 at ₹1,139.00 (box jump — doubling the stake with NEW capital; stop stays ₹946.20; funded ₹18.98 from the pocket + ₹0.00 fresh; charges ₹0.02)
2023-05-02  CPSEETF     PYRAMID BUY ₹33.12 at ₹41.43 (box jump — doubling the stake with NEW capital; stop stays ₹38.64; funded ₹33.12 from the pocket + ₹0.00 fresh; charges ₹0.04)
2023-05-02  GSFC        PYRAMID BUY ₹16.48 at ₹160.80 (box jump — doubling the stake with NEW capital; stop stays ₹116.04; funded ₹16.48 from the pocket + ₹0.00 fresh; charges ₹0.02)
2023-05-15  ANURAS      PYRAMID BUY ₹38.96 at ₹1,169.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,007.67; funded ₹38.96 from the pocket + ₹0.00 fresh; charges ₹0.05)
2023-05-22  GSFC        PYRAMID BUY ₹34.43 at ₹168.05 (box jump — doubling the stake with NEW capital; stop stays ₹155.85; funded ₹34.43 from the pocket + ₹0.00 fresh; charges ₹0.04)
2023-05-29  GSFC        SELL ₹63.75 at stop ₹155.85 (-2.2%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹47.79 of doubled capital and its returns OUT to the pocket
2023-06-05  CPSEETF     PYRAMID BUY ₹67.49 at ₹42.24 (box jump — doubling the stake with NEW capital; stop stays ₹39.05; funded ₹67.49 from the pocket + ₹0.00 fresh; charges ₹0.08)
2023-07-03  ANURAS      SELL ₹67.00 at stop ₹1,007.67 (-9.9%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹50.23 of doubled capital and its returns OUT to the pocket
2023-07-10  CPSEETF     PYRAMID BUY ₹146.91 at ₹46.00 (box jump — doubling the stake with NEW capital; stop stays ₹40.77; funded ₹146.91 from the pocket + ₹0.00 fresh; charges ₹0.17)
2023-07-10  FDC         BUY ₹32.73 at ₹339.40 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.96× weekly, month 5.06×, ladder rising; stop ₹291.22; charges ₹0.04)
2023-07-10  HARIOMPIPE  SELL ₹189.50 at stop ₹603.25 (+39.0%, charges ₹0.20) — the cash goes back to work at the next Friday screen; ₹165.77 of doubled capital and its returns OUT to the pocket
2023-07-17  ZENTEC      BUY ₹23.73 at ₹595.40 (fresh Friday signal — starved 2×, front of the queue — BUY: 8.06× weekly, month 3.59×, ladder rising; stop ₹364.54; charges ₹0.03)
2023-07-24  FDC         PYRAMID BUY ₹32.56 at ₹338.05 (box jump — doubling the stake with NEW capital; stop stays ₹305.00; funded ₹32.56 from the pocket + ₹0.00 fresh; charges ₹0.04)
2023-07-24  ZENTEC      PYRAMID BUY ₹24.44 at ₹614.00 (box jump — doubling the stake with NEW capital; stop stays ₹544.87; funded ₹24.44 from the pocket + ₹0.00 fresh; charges ₹0.03)
2023-07-31  CPSEETF     SELL ₹267.64 at stop ₹41.97 (-4.0%, charges ₹0.28) — the cash goes back to work at the next Friday screen; ₹234.12 of doubled capital and its returns OUT to the pocket
2023-08-07  KIRLOSBROS  BUY ₹21.65 at ₹850.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.05× weekly, month 2.14×, ladder rising; stop ₹647.33; charges ₹0.03)
2023-08-07  WELSPUNIND  BUY ₹11.86 at ₹116.70 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.13× weekly, month 3.60×, ladder rising; stop ₹86.36; charges ₹0.01)
2023-08-14  KIRLOSBROS  PYRAMID BUY ₹23.51 at ₹923.95 (box jump — doubling the stake with NEW capital; stop stays ₹771.68; funded ₹23.51 from the pocket + ₹0.00 fresh; charges ₹0.03)
2023-08-21  KIRLOSBROS  SELL ₹39.20 at stop ₹771.68 (-13.0%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹19.59 of doubled capital and its returns OUT to the pocket
2023-08-28  GABRIEL     BUY ₹19.61 at ₹312.55 (fresh Friday signal — starved 2×, front of the queue — BUY: 8.46× weekly, month 3.60×, ladder rising; stop ₹205.20; charges ₹0.02)
2023-08-28  WELSPUNIND  PYRAMID BUY ₹12.45 at ₹122.60 (box jump — doubling the stake with NEW capital; stop stays ₹107.11; funded ₹12.45 from the pocket + ₹0.00 fresh; charges ₹0.01)
2023-09-04  FDC         PYRAMID BUY ₹73.35 at ₹381.00 (box jump — doubling the stake with NEW capital; stop stays ₹354.97; funded ₹73.35 from the pocket + ₹0.00 fresh; charges ₹0.09)
2023-09-04  WELSPUNIND  PYRAMID BUY ₹25.31 at ₹124.70 (box jump — doubling the stake with NEW capital; stop stays ₹114.00; funded ₹25.31 from the pocket + ₹0.00 fresh; charges ₹0.03)
2023-09-11  GABRIEL     PYRAMID BUY ₹19.74 at ₹315.00 (box jump — doubling the stake with NEW capital; stop stays ₹295.45; funded ₹19.74 from the pocket + ₹0.00 fresh; charges ₹0.02)
2023-09-12  GABRIEL     SELL ₹36.98 at stop ₹295.45 (-5.8%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹18.48 of doubled capital and its returns OUT to the pocket
2023-09-12  WELSPUNIND  SELL ₹46.19 at stop ₹114.00 (-6.7%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹34.63 of doubled capital and its returns OUT to the pocket
2023-09-18  PRAKASH     BUY ₹29.52 at ₹134.50 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.62× weekly, month 3.50×, ladder rising; stop ₹117.33; charges ₹0.03)
2023-10-03  PRAKASH     PYRAMID BUY ₹31.37 at ₹143.10 (box jump — doubling the stake with NEW capital; stop stays ₹126.87; funded ₹31.37 from the pocket + ₹0.00 fresh; charges ₹0.04)
2023-10-23  FDC         SELL ₹136.45 at stop ₹354.97 (-1.4%, charges ₹0.14) — the cash goes back to work at the next Friday screen; ₹102.29 of doubled capital and its returns OUT to the pocket
2023-10-30  CUPID       BUY ₹24.29 at ₹120.99 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.03)
2023-11-28  CUPID       PYRAMID BUY ₹35.38 at ₹176.44 (box jump — doubling the stake with NEW capital; stop stays ₹158.66; funded ₹35.38 from the pocket + ₹0.00 fresh; charges ₹0.04)
2023-11-28  ZENTEC      PYRAMID BUY ₹61.63 at ₹774.55 (box jump — doubling the stake with NEW capital; stop stays ₹682.08; funded ₹61.63 from the pocket + ₹0.00 fresh; charges ₹0.07)
2024-01-29  PRAKASH     PYRAMID BUY ₹91.88 at ₹209.70 (box jump — doubling the stake with NEW capital; stop stays ₹168.62; funded ₹91.88 from the pocket + ₹0.00 fresh; charges ₹0.11)
2024-02-19  ZENTEC      PYRAMID BUY ₹128.89 at ₹810.40 (box jump — doubling the stake with NEW capital; stop stays ₹738.15; funded ₹128.89 from the pocket + ₹0.00 fresh; charges ₹0.15)
2024-02-28  PRAKASH     SELL ₹147.52 at stop ₹168.62 (-3.2%, charges ₹0.15) — the cash goes back to work at the next Friday screen; ₹110.59 of doubled capital and its returns OUT to the pocket
2024-03-04  PAISALO     BUY ₹47.33 at ₹192.65 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.76× weekly, month 2.54×, ladder rising; stop ₹141.55; charges ₹0.06)
2024-03-11  PAISALO     PYRAMID BUY ₹46.62 at ₹190.00 (box jump — doubling the stake with NEW capital; stop stays ₹161.88; funded ₹46.62 from the pocket + ₹0.00 fresh; charges ₹0.06)
2024-03-12  PAISALO     SELL ₹79.31 at stop ₹161.88 (-15.4%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹39.63 of doubled capital and its returns OUT to the pocket
2024-03-18  SOLARINDS   BUY ₹39.68 at ₹8,900.05 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.28× weekly, month 2.84×, ladder rising; stop ₹5,332.29; charges ₹0.05)
2024-04-01  CUPID       TRIM 0.0% (₹0.03 at ₹186.62) to pay the tax bill
2024-04-01  JTLINFRA    TRIM 0.0% (₹0.02 at ₹295.80) to pay the tax bill
2024-04-01  SOLARINDS   PYRAMID BUY ₹39.84 at ₹8,950.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,980.95; funded ₹39.84 from the pocket + ₹0.00 fresh; charges ₹0.05)
2024-04-01  SOLARINDS   TRIM 0.0% (₹0.01 at ₹8,726.05) to pay the tax bill
2024-04-01  TAX         FY2024 settled: ₹0.16 paid (STCG ₹0.79 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-01  ZENTEC      TRIM 0.0% (₹0.10 at ₹945.60) to pay the tax bill
2024-05-09  ZENTEC      SELL ₹284.73 at stop ₹896.89 (+19.6%, charges ₹0.30) — the cash goes back to work at the next Friday screen; ₹249.08 of doubled capital and its returns OUT to the pocket
2024-05-13  CENTURYTEX  BUY ₹24.35 at ₹2,000.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 3.44× weekly, month 1.97×, ladder rising; stop ₹1,715.70; charges ₹0.03)
2024-06-04  CENTURYTEX  SELL ₹20.84 at stop ₹1,715.70 (-14.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹70.94 at stop ₹7,980.95 (-10.6%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹35.45 of doubled capital and its returns OUT to the pocket
2024-06-10  ENDURANCE   BUY ₹19.81 at ₹2,439.90 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.56× weekly, month 2.14×, ladder rising; stop ₹1,964.12; charges ₹0.02)
2024-06-10  PANAMAPET   BUY ₹19.83 at ₹383.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.07× weekly, month 2.01×, ladder rising; stop ₹261.85; charges ₹0.02)
2024-06-10  PGEL        BUY ₹19.81 at ₹286.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.35× weekly, month 3.10×, ladder rising; stop ₹237.50; charges ₹0.02)
2024-07-01  ENDURANCE   PYRAMID BUY ₹21.82 at ₹2,691.20 (box jump — doubling the stake with NEW capital; stop stays ₹2,429.11; funded ₹21.82 from the pocket + ₹0.00 fresh; charges ₹0.03)
2024-07-08  PANAMAPET   PYRAMID BUY ₹20.97 at ₹405.45 (box jump — doubling the stake with NEW capital; stop stays ₹370.60; funded ₹20.97 from the pocket + ₹0.00 fresh; charges ₹0.02)
2024-07-15  PGEL        PYRAMID BUY ₹26.15 at ₹378.00 (box jump — doubling the stake with NEW capital; stop stays ₹338.30; funded ₹26.15 from the pocket + ₹0.00 fresh; charges ₹0.03)
2024-07-23  PGEL        SELL ₹46.74 at stop ₹338.30 (+1.9%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹23.36 of doubled capital and its returns OUT to the pocket
2024-07-29  GENESYS     BUY ₹24.92 at ₹488.67 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.61× weekly, month 1.91×, ladder rising; stop ₹384.07; charges ₹0.03)
2024-08-05  ENDURANCE   SELL ₹39.33 at stop ₹2,429.11 (-5.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹19.65 of doubled capital and its returns OUT to the pocket
2024-08-12  BASF        BUY ₹26.32 at ₹7,350.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.03)
2024-08-12  PANAMAPET   PYRAMID BUY ₹42.02 at ₹406.50 (box jump — doubling the stake with NEW capital; stop stays ₹375.25; funded ₹42.02 from the pocket + ₹0.00 fresh; charges ₹0.05)
2024-08-19  GENESYS     PYRAMID BUY ₹24.17 at ₹474.50 (box jump — doubling the stake with NEW capital; stop stays ₹398.41; funded ₹24.17 from the pocket + ₹0.00 fresh; charges ₹0.03)
2024-08-26  BASF        PYRAMID BUY ₹23.84 at ₹6,666.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,894.80; funded ₹23.84 from the pocket + ₹0.00 fresh; charges ₹0.03)
2024-09-16  PANAMAPET   PYRAMID BUY ₹85.25 at ₹412.60 (box jump — doubling the stake with NEW capital; stop stays ₹384.27; funded ₹85.25 from the pocket + ₹0.00 fresh; charges ₹0.10)
2024-10-03  PANAMAPET   SELL ₹158.53 at stop ₹384.27 (-5.5%, charges ₹0.16) — the cash goes back to work at the next Friday screen; ₹138.68 of doubled capital and its returns OUT to the pocket
2024-10-07  ASTRAZEN    BUY ₹19.85 at ₹7,442.65 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.02)
2024-10-14  BASF        PYRAMID BUY ₹58.81 at ₹8,225.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,611.30; funded ₹58.81 from the pocket + ₹0.00 fresh; charges ₹0.07)
2024-10-14  GENESYS     PYRAMID BUY ₹53.63 at ₹526.67 (box jump — doubling the stake with NEW capital; stop stays ₹451.09; funded ₹53.63 from the pocket + ₹0.00 fresh; charges ₹0.06)
2024-10-22  BASF        SELL ₹108.66 at stop ₹7,611.30 (-0.1%, charges ₹0.11) — the cash goes back to work at the next Friday screen; ₹81.46 of doubled capital and its returns OUT to the pocket
2024-10-25  GENESYS     SELL ₹91.72 at stop ₹451.09 (-10.5%, charges ₹0.10) — the cash goes back to work at the next Friday screen; ₹68.76 of doubled capital and its returns OUT to the pocket
2024-10-28  CUPID       SELL ₹63.51 at stop ₹158.66 (+6.7%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹31.74 of doubled capital and its returns OUT to the pocket
2024-10-28  PAYTM       BUY ₹13.08 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.02)
2024-11-04  AKZOINDIA   BUY ₹15.64 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.04)
2024-11-04  CARERATING  BUY ₹15.74 at ₹1,510.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.80× weekly, month 4.48×, ladder rising; stop ₹1,066.23; charges ₹0.04)
2024-11-04  HIMATSEIDE  BUY ₹15.74 at ₹170.83 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.72× weekly, month 2.78×, ladder rising; stop ₹118.10; charges ₹0.04)
2024-11-04  KIRLPNU     BUY ₹15.55 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.04)
2024-11-11  ASTRAZEN    PYRAMID BUY ₹19.58 at ₹7,350.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,854.77; funded ₹19.58 from the pocket + ₹0.00 fresh; charges ₹0.05)
2024-11-11  KIRLPNU     PYRAMID BUY ₹15.44 at ₹1,690.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,504.85; funded ₹15.44 from the pocket + ₹0.00 fresh; charges ₹0.04)
2024-11-14  ASTRAZEN    SELL ₹36.40 at stop ₹6,854.77 (-7.3%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹18.18 of doubled capital and its returns OUT to the pocket
2024-11-18  JSWHL       BUY ₹16.36 at ₹19,990.00 (fresh Friday signal — BUY: 3.46× weekly, month 4.62×, ladder rising; stop ₹8,434.53; charges ₹0.04)
2024-11-25  PAYTM       PYRAMID BUY ₹15.96 at ₹913.80 (box jump — doubling the stake with NEW capital; stop stays ₹712.50; funded ₹15.96 from the pocket + ₹0.00 fresh; charges ₹0.04)
2024-12-02  CARERATING  PYRAMID BUY ₹15.80 at ₹1,519.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,239.70; funded ₹15.80 from the pocket + ₹0.00 fresh; charges ₹0.04)
2024-12-09  AKZOINDIA   PYRAMID BUY ₹12.84 at ₹3,718.70 (box jump — doubling the stake with NEW capital; stop stays ₹3,423.18; funded ₹12.84 from the pocket + ₹0.00 fresh; charges ₹0.03)
2024-12-09  PAYTM       PYRAMID BUY ₹34.81 at ₹997.45 (box jump — doubling the stake with NEW capital; stop stays ₹838.09; funded ₹34.81 from the pocket + ₹0.00 fresh; charges ₹0.08)
2024-12-16  KIRLPNU     PYRAMID BUY ₹30.92 at ₹1,693.90 (box jump — doubling the stake with NEW capital; stop stays ₹1,596.00; funded ₹30.92 from the pocket + ₹0.00 fresh; charges ₹0.07)
2024-12-23  KIRLPNU     SELL ₹58.07 at stop ₹1,596.00 (-5.8%, charges ₹0.13) — the cash goes back to work at the next Friday screen; ₹43.52 of doubled capital and its returns OUT to the pocket
2024-12-23  PAYTM       PYRAMID BUY ₹66.91 at ₹959.80 (box jump — doubling the stake with NEW capital; stop stays ₹887.49; funded ₹66.91 from the pocket + ₹0.00 fresh; charges ₹0.16)
2024-12-27  AKZOINDIA   SELL ₹23.56 at stop ₹3,423.18 (-16.9%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹11.77 of doubled capital and its returns OUT to the pocket
2024-12-30  KFINTECH    BUY ₹29.05 at ₹1,511.45 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.07)
2025-01-06  HIMATSEIDE  PYRAMID BUY ₹18.55 at ₹201.80 (box jump — doubling the stake with NEW capital; stop stays ₹174.80; funded ₹18.55 from the pocket + ₹0.00 fresh; charges ₹0.04)
2025-01-09  PAYTM       SELL ₹124.10 at stop ₹893.05 (-4.7%, charges ₹0.28) — the cash goes back to work at the next Friday screen; ₹108.53 of doubled capital and its returns OUT to the pocket
2025-01-13  AEGISLOG    BUY ₹17.12 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.04)
2025-01-13  CARERATING  SELL ₹25.70 at stop ₹1,239.70 (-18.1%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹12.84 of doubled capital and its returns OUT to the pocket
2025-01-13  HIMATSEIDE  SELL ₹32.03 at stop ₹174.80 (-6.2%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹15.99 of doubled capital and its returns OUT to the pocket
2025-01-15  KFINTECH    SELL ₹22.18 at stop ₹1,159.14 (-23.3%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2025-01-20  AEGISLOG    PYRAMID BUY ₹16.44 at ₹803.60 (box jump — doubling the stake with NEW capital; stop stays ₹700.36; funded ₹16.44 from the pocket + ₹0.00 fresh; charges ₹0.04)
2025-01-20  APOLLO      BUY ₹15.68 at ₹131.50 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.93× weekly, month 3.48×, ladder rising; stop ₹110.19; charges ₹0.04)
2025-01-20  BAJAJHCARE  BUY ₹15.91 at ₹690.00 (fresh Friday signal — BUY: 1.75× weekly, month 4.12×, ladder rising; stop ₹451.06; charges ₹0.04)
2025-01-24  AEGISLOG    SELL ₹28.56 at stop ₹700.36 (-14.5%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹14.26 of doubled capital and its returns OUT to the pocket
2025-01-27  CREDITACC   BUY ₹13.39 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.03)
2025-02-03  BAJAJHCARE  PYRAMID BUY ₹15.64 at ₹680.00 (box jump — doubling the stake with NEW capital; stop stays ₹455.35; funded ₹15.64 from the pocket + ₹0.00 fresh; charges ₹0.04)
2025-02-03  ZENSARTECH  BUY ₹15.50 at ₹947.00 (fresh Friday signal — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹0.04)
2025-02-10  HDFCGOLD    BUY ₹8.67 at ₹75.80 (fresh Friday signal — BUY: 2.22× weekly, month 1.58×, ladder rising; stop ₹64.93; charges ₹0.02)
2025-02-17  APOLLO      SELL ₹13.08 at stop ₹110.19 (-16.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2025-02-24  BAJAJHCARE  PYRAMID BUY ₹28.24 at ₹614.55 (box jump — doubling the stake with NEW capital; stop stays ₹521.14; funded ₹28.24 from the pocket + ₹0.00 fresh; charges ₹0.07)
2025-02-24  HDFCGOLD    PYRAMID BUY ₹8.52 at ₹74.60 (box jump — doubling the stake with NEW capital; stop stays ₹70.20; funded ₹8.52 from the pocket + ₹0.00 fresh; charges ₹0.02)
2025-02-24  TAJGVK      BUY ₹13.08 at ₹440.40 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.16× weekly, month 2.07×, ladder rising; stop ₹349.09; charges ₹0.03)
2025-03-03  JSWHL       PYRAMID BUY ₹13.56 at ₹16,599.95 (box jump — doubling the stake with NEW capital; stop stays ₹13,741.44; funded ₹13.56 from the pocket + ₹0.00 fresh; charges ₹0.03)
2025-03-03  TAJGVK      PYRAMID BUY ₹13.46 at ₹454.45 (box jump — doubling the stake with NEW capital; stop stays ₹412.59; funded ₹13.46 from the pocket + ₹0.00 fresh; charges ₹0.03)
2025-03-03  ZENSARTECH  SELL ₹11.86 at stop ₹727.84 (-23.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2025-03-10  CREDITACC   PYRAMID BUY ₹15.23 at ₹968.75 (box jump — doubling the stake with NEW capital; stop stays ₹837.38; funded ₹15.23 from the pocket + ₹0.00 fresh; charges ₹0.04)
2025-03-10  SETFGOLD    BUY ₹11.86 at ₹74.79 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.20× weekly, month 2.11×, ladder rising; stop ₹69.36; charges ₹0.03)
2025-03-24  TAJGVK      PYRAMID BUY ₹30.48 at ₹515.00 (box jump — doubling the stake with NEW capital; stop stays ₹453.34; funded ₹30.48 from the pocket + ₹0.00 fresh; charges ₹0.07)
2025-04-01  TAX         FY2025 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹7.16 / LT ₹0.00)
2025-04-02  TAJGVK      SELL ₹53.48 at stop ₹453.34 (-5.8%, charges ₹0.12) — the cash goes back to work at the next Friday screen; ₹40.07 of doubled capital and its returns OUT to the pocket
2025-04-07  BAJAJHCARE  SELL ₹47.73 at stop ₹521.14 (-19.8%, charges ₹0.11) — the cash goes back to work at the next Friday screen; ₹35.77 of doubled capital and its returns OUT to the pocket
2025-04-07  HDFCGOLD    PYRAMID BUY ₹17.56 at ₹77.00 (box jump — doubling the stake with NEW capital; stop stays ₹71.44; funded ₹17.56 from the pocket + ₹0.00 fresh; charges ₹0.04)
2025-04-07  HDFCGOLD    SELL ₹32.47 at stop ₹71.44 (-6.1%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹24.33 of doubled capital and its returns OUT to the pocket
2025-04-07  JSWHL       PYRAMID BUY ₹40.26 at ₹24,680.80 (box jump — doubling the stake with NEW capital; stop stays ₹19,106.01; funded ₹40.26 from the pocket + ₹0.00 fresh; charges ₹0.10)
2025-04-07  SETFGOLD    SELL ₹10.95 at stop ₹69.36 (-7.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹21.03 at ₹818.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.05)
2025-04-15  VADILALIND  BUY ₹21.11 at ₹5,898.90 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.25× weekly, month 6.19×, ladder rising; stop ₹4,500.03; charges ₹0.05)
2025-05-12  CREDITACC   PYRAMID BUY ₹36.07 at ₹1,148.60 (box jump — doubling the stake with NEW capital; stop stays ₹1,019.35; funded ₹36.07 from the pocket + ₹0.00 fresh; charges ₹0.09)
2025-05-19  VADILALIND  PYRAMID BUY ₹24.30 at ₹6,805.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,401.40; funded ₹24.30 from the pocket + ₹0.00 fresh; charges ₹0.06)
2025-05-30  VADILALIND  SELL ₹38.44 at stop ₹5,401.40 (-15.0%, charges ₹0.09) — the cash goes back to work at the next Friday screen; ₹19.20 of doubled capital and its returns OUT to the pocket
2025-06-02  CREDITACC   PYRAMID BUY ₹71.52 at ₹1,140.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,029.71; funded ₹71.52 from the pocket + ₹0.00 fresh; charges ₹0.17)
2025-06-02  TDPOWERSYS  BUY ₹21.54 at ₹518.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.60× weekly, month 2.44×, ladder rising; stop ₹432.25; charges ₹0.05)
2025-06-23  TDPOWERSYS  PYRAMID BUY ₹21.22 at ₹511.50 (box jump — doubling the stake with NEW capital; stop stays ₹457.00; funded ₹21.22 from the pocket + ₹0.00 fresh; charges ₹0.05)
2025-07-28  TDPOWERSYS  SELL ₹37.79 at stop ₹457.00 (-11.2%, charges ₹0.08) — the cash goes back to work at the next Friday screen; ₹18.87 of doubled capital and its returns OUT to the pocket
2025-08-04  JSWHL       SELL ₹62.12 at stop ₹19,106.01 (-11.1%, charges ₹0.14) — the cash goes back to work at the next Friday screen; ₹46.55 of doubled capital and its returns OUT to the pocket
2025-08-04  SHARDACROP  BUY ₹18.92 at ₹1,107.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.38× weekly, month 3.43×, ladder rising; stop ₹729.83; charges ₹0.04)
2025-08-11  SIRCA       BUY ₹15.57 at ₹458.80 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.96× weekly, month 3.38×, ladder rising; stop ₹388.17; charges ₹0.04)
2025-09-01  SHARDACROP  PYRAMID BUY ₹16.22 at ₹951.60 (box jump — doubling the stake with NEW capital; stop stays ₹848.33; funded ₹16.22 from the pocket + ₹0.00 fresh; charges ₹0.04)
2025-09-01  SIRCA       PYRAMID BUY ₹15.72 at ₹464.50 (box jump — doubling the stake with NEW capital; stop stays ₹424.18; funded ₹15.72 from the pocket + ₹0.00 fresh; charges ₹0.04)
2025-09-24  SHARDACROP  SELL ₹28.83 at stop ₹848.33 (-17.6%, charges ₹0.06) — the cash goes back to work at the next Friday screen; ₹14.40 of doubled capital and its returns OUT to the pocket
2025-10-06  SIRCA       PYRAMID BUY ₹33.40 at ₹493.90 (box jump — doubling the stake with NEW capital; stop stays ₹446.36; funded ₹33.40 from the pocket + ₹0.00 fresh; charges ₹0.08)
2025-10-13  AVANTIFEED  PYRAMID BUY ₹16.87 at ₹657.45 (box jump — doubling the stake with NEW capital; stop stays ₹511.29; funded ₹16.87 from the pocket + ₹0.00 fresh; charges ₹0.04)
2025-10-20  AVANTIFEED  PYRAMID BUY ₹35.24 at ₹687.70 (box jump — doubling the stake with NEW capital; stop stays ₹600.07; funded ₹35.24 from the pocket + ₹0.00 fresh; charges ₹0.08)
2025-10-20  CREDITACC   SELL ₹159.36 at stop ₹1,274.42 (+17.5%, charges ₹0.35) — the cash goes back to work at the next Friday screen; ₹139.37 of doubled capital and its returns OUT to the pocket
2025-10-27  SKYGOLD     BUY ₹23.24 at ₹370.00 (fresh Friday signal — BUY: 1.65× weekly, month 2.25×, ladder rising; stop ₹304.38; charges ₹0.05)
2025-11-10  SKYGOLD     PYRAMID BUY ₹22.37 at ₹357.00 (box jump — doubling the stake with NEW capital; stop stays ₹329.13; funded ₹22.37 from the pocket + ₹0.00 fresh; charges ₹0.05)
2025-11-17  SIRCA       PYRAMID BUY ₹70.37 at ₹520.95 (box jump — doubling the stake with NEW capital; stop stays ₹475.57; funded ₹70.37 from the pocket + ₹0.00 fresh; charges ₹0.17)
2025-11-25  SKYGOLD     SELL ₹41.12 at stop ₹329.13 (-9.5%, charges ₹0.09) — the cash goes back to work at the next Friday screen; ₹20.53 of doubled capital and its returns OUT to the pocket
2025-12-01  SANSERA     BUY ₹30.48 at ₹1,749.60 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.07)
2025-12-08  AVANTIFEED  PYRAMID BUY ₹84.04 at ₹820.95 (box jump — doubling the stake with NEW capital; stop stays ₹748.60; funded ₹84.04 from the pocket + ₹0.00 fresh; charges ₹0.20)
2025-12-08  SIRCA       SELL ₹130.76 at stop ₹485.64 (-2.7%, charges ₹0.29) — the cash goes back to work at the next Friday screen; ₹114.35 of doubled capital and its returns OUT to the pocket
2025-12-15  GMRAIRPORT  BUY ₹17.69 at ₹103.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.56× weekly, month 2.60×, ladder rising; stop ₹89.73; charges ₹0.04)
2025-12-15  SANSERA     PYRAMID BUY ₹29.63 at ₹1,705.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,517.72; funded ₹29.63 from the pocket + ₹0.00 fresh; charges ₹0.07)
2025-12-22  GMRAIRPORT  PYRAMID BUY ₹17.32 at ₹102.05 (box jump — doubling the stake with NEW capital; stop stays ₹92.10; funded ₹17.32 from the pocket + ₹0.00 fresh; charges ₹0.04)
2026-01-19  SANSERA     PYRAMID BUY ₹64.08 at ₹1,846.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,672.76; funded ₹64.08 from the pocket + ₹0.00 fresh; charges ₹0.15)
2026-01-21  AVANTIFEED  SELL ₹152.75 at stop ₹748.60 (-2.4%, charges ₹0.34) — the cash goes back to work at the next Friday screen; ₹133.59 of doubled capital and its returns OUT to the pocket
2026-01-23  GMRAIRPORT  SELL ₹31.16 at stop ₹92.10 (-10.6%, charges ₹0.07) — the cash goes back to work at the next Friday screen; ₹15.56 of doubled capital and its returns OUT to the pocket
2026-01-23  SANSERA     SELL ₹115.74 at stop ₹1,672.76 (-6.4%, charges ₹0.26) — the cash goes back to work at the next Friday screen; ₹86.74 of doubled capital and its returns OUT to the pocket
2026-01-27  GOLDBEES    BUY ₹11.96 at ₹130.55 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.08× weekly, month 3.47×, ladder rising; stop ₹104.22; charges ₹0.03)
2026-01-27  GOLDIETF    BUY ₹11.97 at ₹136.40 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.40× weekly, month 3.35×, ladder rising; stop ₹106.77; charges ₹0.03)
2026-01-27  GROWWSLVR   BUY ₹11.98 at ₹31.00 (fresh Friday signal — BUY: 5.65× weekly, month 5.51×, ladder rising; stop ₹19.45; charges ₹0.03)
2026-01-27  SILVER      BUY ₹12.04 at ₹315.00 (fresh Friday signal — BUY: 5.32× weekly, month 6.78×, ladder rising; stop ₹208.79; charges ₹0.03)
2026-01-27  TATSILV     BUY ₹11.97 at ₹32.00 (fresh Friday signal — BUY: 9.86× weekly, month 21.32×, ladder rising; stop ₹19.90; charges ₹0.03)
2026-02-02  GOLDBEES    PYRAMID BUY ₹11.15 at ₹121.99 (box jump — doubling the stake with NEW capital; stop stays ₹113.05; funded ₹11.15 from the pocket + ₹0.00 fresh; charges ₹0.03)
2026-02-02  GOLDBEES    SELL ₹20.60 at stop ₹113.05 (-10.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹10.29 of doubled capital and its returns OUT to the pocket
2026-02-02  GOLDIETF    PYRAMID BUY ₹11.63 at ₹132.82 (box jump — doubling the stake with NEW capital; stop stays ₹115.68; funded ₹11.63 from the pocket + ₹0.00 fresh; charges ₹0.03)
2026-02-02  GROWWSLVR   PYRAMID BUY ₹9.36 at ₹24.27 (box jump — doubling the stake with NEW capital; stop stays ₹22.32; funded ₹9.36 from the pocket + ₹0.00 fresh; charges ₹0.02)
2026-02-02  GROWWSLVR   SELL ₹17.16 at stop ₹22.32 (-19.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹8.57 of doubled capital and its returns OUT to the pocket
2026-02-02  SILVER      PYRAMID BUY ₹10.04 at ₹263.22 (box jump — doubling the stake with NEW capital; stop stays ₹234.68; funded ₹10.04 from the pocket + ₹0.00 fresh; charges ₹0.02)
2026-02-02  SILVER      SELL ₹17.84 at stop ₹234.68 (-18.8%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹8.91 of doubled capital and its returns OUT to the pocket
2026-02-02  TATSILV     PYRAMID BUY ₹10.27 at ₹27.52 (box jump — doubling the stake with NEW capital; stop stays ₹23.03; funded ₹10.27 from the pocket + ₹0.00 fresh; charges ₹0.02)
2026-02-02  TATSILV     SELL ₹17.12 at stop ₹23.03 (-22.6%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹8.55 of doubled capital and its returns OUT to the pocket
2026-02-09  APEX        BUY ₹11.93 at ₹355.00 (fresh Friday signal — BUY: 2.98× weekly, month 4.24×, ladder rising; stop ₹221.66; charges ₹0.03)
2026-02-09  CPSEETF     BUY ₹12.01 at ₹99.82 (fresh Friday signal — BUY: 2.11× weekly, month 2.09×, ladder rising; stop ₹85.68; charges ₹0.03)
2026-02-09  LIQUIDPLUS  BUY ₹12.01 at ₹1,075.80 (fresh Friday signal — BUY: 1.56× weekly, month 3.05×, ladder rising; stop ₹1,009.92; charges ₹0.03)
2026-02-16  APEX        PYRAMID BUY ₹14.24 at ₹425.00 (box jump — doubling the stake with NEW capital; stop stays ₹327.85; funded ₹14.24 from the pocket + ₹0.00 fresh; charges ₹0.03)
2026-02-16  LIQUIDPLUS  PYRAMID BUY ₹11.90 at ₹1,068.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,012.68; funded ₹11.90 from the pocket + ₹0.00 fresh; charges ₹0.03)
2026-02-23  APEX        PYRAMID BUY ₹30.26 at ₹452.00 (box jump — doubling the stake with NEW capital; stop stays ₹389.22; funded ₹30.26 from the pocket + ₹0.00 fresh; charges ₹0.07)
2026-02-23  CPSEETF     PYRAMID BUY ₹12.20 at ₹101.63 (box jump — doubling the stake with NEW capital; stop stays ₹91.67; funded ₹12.20 from the pocket + ₹0.00 fresh; charges ₹0.03)
2026-02-27  APEX        SELL ₹51.94 at stop ₹389.22 (-7.5%, charges ₹0.12) — the cash goes back to work at the next Friday screen; ₹38.92 of doubled capital and its returns OUT to the pocket
2026-03-02  J&KBANK     BUY ₹14.67 at ₹116.20 (fresh Friday signal — starved 1×, front of the queue — BUY: 8.67× weekly, month 1.90×, ladder rising; stop ₹96.50; charges ₹0.03)
2026-03-16  CPSEETF     PYRAMID BUY ₹24.51 at ₹102.23 (box jump — doubling the stake with NEW capital; stop stays ₹96.54; funded ₹24.51 from the pocket + ₹0.00 fresh; charges ₹0.06)
2026-03-16  J&KBANK     PYRAMID BUY ₹15.26 at ₹121.14 (box jump — doubling the stake with NEW capital; stop stays ₹103.27; funded ₹15.26 from the pocket + ₹0.00 fresh; charges ₹0.04)
2026-03-23  GOLDIETF    SELL ₹20.19 at stop ₹115.68 (-14.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen; ₹10.08 of doubled capital and its returns OUT to the pocket
2026-03-23  J&KBANK     PYRAMID BUY ₹29.11 at ₹115.68 (box jump — doubling the stake with NEW capital; stop stays ₹110.67; funded ₹29.11 from the pocket + ₹0.00 fresh; charges ₹0.07)
2026-03-23  J&KBANK     SELL ₹55.52 at stop ₹110.67 (-5.6%, charges ₹0.12) — the cash goes back to work at the next Friday screen; ₹41.60 of doubled capital and its returns OUT to the pocket
2026-03-30  AETHER      BUY ₹15.44 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.04)
2026-03-30  LIQUID1     BUY ₹11.22 at ₹1,097.40 (fresh Friday signal — ACCUMULATE: 2.24× weekly, month 1.82×, ladder rising; stop ₹1,039.97; charges ₹0.03)
2026-04-01  TAX         FY2026 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹34.28 / LT ₹0.00)
2026-04-13  AETHER      PYRAMID BUY ₹15.67 at ₹1,170.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,010.28; funded ₹15.67 from the pocket + ₹0.00 fresh; charges ₹0.04)
2026-04-13  LIQUIDPLUS  PYRAMID BUY ₹24.04 at ₹1,080.91 (box jump — doubling the stake with NEW capital; stop stays ₹1,022.02; funded ₹24.04 from the pocket + ₹0.00 fresh; charges ₹0.06)
2026-04-27  LIQUID1     PYRAMID BUY ₹11.25 at ₹1,103.44 (box jump — doubling the stake with NEW capital; stop stays ₹1,041.83; funded ₹11.25 from the pocket + ₹0.00 fresh; charges ₹0.03)
2026-05-04  CPSEETF     PYRAMID BUY ₹52.93 at ₹110.50 (box jump — doubling the stake with NEW capital; stop stays ₹100.15; funded ₹52.93 from the pocket + ₹0.00 fresh; charges ₹0.12)
2026-05-11  AETHER      PYRAMID BUY ₹32.46 at ₹1,213.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,125.84; funded ₹32.46 from the pocket + ₹0.00 fresh; charges ₹0.08)
2026-05-11  LIQUID1     PYRAMID BUY ₹22.43 at ₹1,101.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,047.51; funded ₹22.43 from the pocket + ₹0.00 fresh; charges ₹0.05)
2026-05-14  AETHER      SELL ₹60.03 at stop ₹1,125.84 (-5.1%, charges ₹0.13) — the cash goes back to work at the next Friday screen; ₹44.99 of doubled capital and its returns OUT to the pocket
2026-05-18  CAPLIPOINT  BUY ₹15.04 at ₹1,990.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.04)
2026-05-25  CAPLIPOINT  PYRAMID BUY ₹15.53 at ₹2,059.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,851.17; funded ₹15.53 from the pocket + ₹0.00 fresh; charges ₹0.04)
2026-06-02  CPSEETF     SELL ₹95.61 at stop ₹100.15 (-5.5%, charges ₹0.21) — the cash goes back to work at the next Friday screen; ₹83.62 of doubled capital and its returns OUT to the pocket
2026-06-08  MIDHANI     BUY ₹11.99 at ₹430.50 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.42× weekly, month 1.62×, ladder rising; stop ₹368.08; charges ₹0.03)
2026-06-15  CAPLIPOINT  PYRAMID BUY ₹36.69 at ₹2,435.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,852.50; funded ₹36.69 from the pocket + ₹0.00 fresh; charges ₹0.09)
2026-06-22  MIDHANI     PYRAMID BUY ₹12.21 at ₹439.20 (box jump — doubling the stake with NEW capital; stop stays ₹399.19; funded ₹12.21 from the pocket + ₹0.00 fresh; charges ₹0.03)
2026-06-29  CAPLIPOINT  PYRAMID BUY ₹75.43 at ₹2,506.40 (box jump — doubling the stake with NEW capital; stop stays ₹2,209.13; funded ₹75.43 from the pocket + ₹0.00 fresh; charges ₹0.18)
2026-07-13  LIQUIDPLUS  PYRAMID BUY ₹48.61 at ₹1,093.96 (box jump — doubling the stake with NEW capital; stop stays ₹1,036.02; funded ₹48.61 from the pocket + ₹0.00 fresh; charges ₹0.11)
2026-07-23  MIDHANI     SELL ₹22.12 at stop ₹399.19 (-8.2%, charges ₹0.05) — the cash goes back to work at the next Friday screen; ₹11.04 of doubled capital and its returns OUT to the pocket
```
