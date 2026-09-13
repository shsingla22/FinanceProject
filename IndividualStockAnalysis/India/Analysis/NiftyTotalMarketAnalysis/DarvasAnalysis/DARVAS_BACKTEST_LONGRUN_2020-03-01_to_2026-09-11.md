# The Darvas screen — 2020-03-01 → 2026-09-11

> **LONG-RUN BACKTEST, TWO ENGINES.** One continuous price archive (2019-03-01 → 2026-09-11, 1971 symbols, in `ROLLING_2019-03-01_to_2026-09-13/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. Both engines pay Angel One charges on every order and settle capital-gains tax every 1 April in their net runs. **The universe is POINT-IN-TIME with a ROLLING radar:** membership is recomputed EVERY MONTH as the top symbols by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and new listings or emerging names ENTER the month they earn their place, so neither survivorship bias nor an emergence blind spot remains. Membership gates fresh entries only; a held position runs to its stop regardless (`_membership_long.csv`). Raw exchange data means heuristic split/bonus adjustment, every one listed in `_adjustments.csv`. No slippage, stop exits at the stop price, fractional shares. Stored fiscal statements exist for 37% of this universe — a stock without statements cannot be blocked by the earnings gate (only a FALLING verdict blocks), which loosens that gate for the rest.

## The two engines

**Common rules.** ₹100 starts all in cash. Every Friday after the close the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. Entries into NEW stocks use ONLY the original capital and money freed by sales — **never more than one tenth of total capital per first entry** (sell a stock worth 40% of the book and it takes four fresh names to redeploy it), best volume reaction first, at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily, ratcheted up weekly, and only the stop itself exits. When nothing qualifies, the cash stays cash.

**Engine A — no doubling.** Exactly the rules above, nothing else.

**Engine B — doubling with NEW capital, 3× cap.** On EVERY box jump upward (each weekly stop ratchet), the stake is doubled with FRESH MONEY from outside the portfolio, equal to the position's market value, at the next day's open — but AT MOST THREE TIMES per position (8× the first slice), so the capital the rule demands stays realistic. The new money never touches the portfolio's cash — fresh entries are never starved — and every injection is dated and logged, so the honest yardstick is the money-weighted return (XIRR), not a naive multiple. Each add-on is its own tax lot on its own holding clock; the ratcheted stop covers the whole enlarged position; a jump past the cap is logged, never doubled.

## The headline — XIRR is the honest yardstick

| Engine | Money put in | Final value | XIRR (per year) |
|---|---:|---:|---:|
| **B: doubling, NET of charges and tax** | ₹3,872.38 crore crore (₹100 + ₹3,872.38 crore crore injected) | **₹4,356.62 crore crore** | **+111.06%** |
| B: doubling, before charges and tax | ₹4,370.59 crore crore | ₹4,932.75 crore crore | +115.58% |
| **A: no doubling, NET of charges and tax** | ₹100.00 | **₹204.17** | **+11.58%** |
| A: no doubling, before charges and tax | ₹100.00 | ₹250.18 | +15.11% |
| Nifty 50 (pre-cost, pre-tax) | ₹100.00 | ₹212.91 | +12.30% |

*With a single starting flow (engine A, the Nifty) the XIRR IS the CAGR. Engine B's XIRR weighs every injection by how long it was invested. Tax accrued on the final part-year, due next April and not yet paid: engine B ₹0.00, engine A ₹0.00; unrealised gains in both end books carry further deferred liabilities.*

6.52 years, 341 weekly screens. Engine B injected new capital 401 times (gross run: 402); the complete dated injection list is in the blotter and the events CSV.

## The radar, measured — an honest negative result

This run uses ROLLING monthly membership; the same window was also run
on a FIXED start-month cohort (in this repository's history). Side by
side:

| Engine A (₹100 →) | Fixed cohort | Rolling radar (this run) |
|---|---:|---:|
| A: no doubling, net | ₹276.43 (+16.89%/yr) | ₹204.17 (+11.58%/yr) |
| A: no doubling, gross | ₹348.47 (+21.12%/yr) | ₹250.18 (+15.11%/yr) |
| Nifty 50 | ₹212.91 (+12.30%/yr) | ₹212.91 (+12.30%/yr) |

The radar was built to catch emerging stocks — and it does (the IPO
entries are in `_membership_long.csv`) — but on this window it COST
money, and the ledger says why: cohort trades averaged **+6.5%** (134 closed) while radar-admitted trades averaged **−0.1%** (77 closed). A stock typically enters
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
| Transaction charges | ₹9.74 | ₹12.51 crore crore |
| Capital-gains tax paid | ₹22.60 | ₹0.00 |
| Tax accrued, final part-year | ₹0.00 | ₹0.00 |

*Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024, then 0.1% (the ₹20/order cap never binds at this scale). Tax: 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward; flat DP/minimum charges cannot scale to a normalised ₹100 and are excluded (under 0.03% of a trade on a ₹1-lakh+ account).*

### Tax ledger — Engine B (doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹11.59 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹1,983.92 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹9.32 lakh / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹43.01 crore / ₹0.00 |
| FY2024 | 2024-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹5,710.60 crore / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹6.35 lakh crore / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹15.73 crore crore / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹55.95 crore crore / ₹0.00 |

### Tax ledger — Engine A (no doubling)

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹11.59 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹0.62 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹43.14 | ₹0.00 | ₹8.63 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹1.06 | ₹0.00 | ₹0.21 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹68.05 | ₹0.00 | ₹13.61 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹1.19 | ₹0.15 | ₹0.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹19.81 / ₹0.00 |
| Final part-year (accrued) | — | ₹0.00 | ₹0.00 | ₹0.00 | ₹21.96 / ₹0.00 |

## Calendar-year returns (net runs)

*Engine B's yearly figure is Modified Dietz — money-weighted for the injections, so new capital is never booked as 'return'. Engine A's is the plain yearly return (no injections).*

| Year (through) | A equity (₹) | A return | B equity (₹) | B injected in year | B return (Dietz) | Nifty 50 |
|---|---:|---:|---:|---:|---:|---:|
| 2020 (2020-12-24) | ₹103.57 | +3.6% | ₹4,826.05 | ₹4,585.85 | +14.1% | +25.1% |
| 2021 (2021-12-31) | ₹156.78 | +51.4% | ₹21.55 lakh | ₹20.68 lakh | +25.4% | +26.2% |
| 2022 (2022-12-30) | ₹151.20 | -3.6% | ₹103.31 crore | ₹109.73 crore | -38.3% | +4.3% |
| 2023 (2023-12-29) | ₹214.88 | +42.1% | ₹19,734.52 crore | ₹18,209.44 crore | +39.3% | +20.0% |
| 2024 (2024-12-27) | ₹215.36 | +0.2% | ₹26.12 lakh crore | ₹27.18 lakh crore | -23.0% | +9.6% |
| 2025 (2025-12-26) | ₹186.16 | -13.6% | ₹37.42 crore crore | ₹34.81 crore crore | +35.1% | +9.4% |
| 2026 (2026-09-11) | ₹204.17 | +9.7% | ₹4,356.62 crore crore | ₹3,837.29 crore crore | +60.1% | -10.2% |

## What it took to earn it (engine B net; A in brackets)

- Maximum drawdown **-11.7%** (A: -33.0%), on weekly closes — B's is softened by injections landing mid-decline, so read it with care.
- **226 closed trades**: 44 winners (19%), average winner +15.9%, average loser -10.6% (returns per blended entry price).
- Best closed trade LTTS +118.7%; worst BCG -59.0%.
- Median holding period 66 days.
- Cash share of equity averaged 11%; fully in cash 5 of 341 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net runs)

| Month-end screen | B equity | B injected so far | B cash | B positions | A equity |
|---|---:|---:|---:|---:|---:|
| 2020-03-27 | ₹88.29 | ₹0.00 | ₹88.29 | 0 | ₹88.29 |
| 2020-04-30 | ₹89.10 | ₹0.00 | ₹26.28 | 7 | ₹89.10 |
| 2020-05-29 | ₹140.03 | ₹46.97 | ₹5.15 | 9 | ₹93.67 |
| 2020-06-26 | ₹254.84 | ₹147.60 | ₹6.21 | 9 | ₹100.04 |
| 2020-07-31 | ₹429.25 | ₹315.14 | ₹42.11 | 8 | ₹103.92 |
| 2020-08-28 | ₹735.03 | ₹654.75 | ₹0.00 | 10 | ₹101.63 |
| 2020-09-25 | ₹1,177.12 | ₹1,094.44 | ₹194.89 | 7 | ₹103.47 |
| 2020-10-30 | ₹2,103.15 | ₹1,993.25 | ₹0.00 | 10 | ₹105.76 |
| 2020-11-27 | ₹3,082.55 | ₹3,024.07 | ₹0.00 | 12 | ₹104.11 |
| 2020-12-24 | ₹4,826.05 | ₹4,585.85 | ₹968.75 | 8 | ₹103.57 |
| 2021-01-29 | ₹10,950.00 | ₹11,384.71 | ₹1,590.19 | 8 | ₹99.09 |
| 2021-02-26 | ₹26,836.42 | ₹25,442.04 | ₹478.43 | 9 | ₹112.08 |
| 2021-03-26 | ₹33,533.73 | ₹34,260.33 | ₹2,729.68 | 11 | ₹112.27 |
| 2021-04-30 | ₹61,374.04 | ₹57,081.22 | ₹0.00 | 12 | ₹126.15 |
| 2021-05-28 | ₹1.09 lakh | ₹96,585.20 | ₹0.00 | 12 | ₹136.43 |
| 2021-06-25 | ₹2.28 lakh | ₹1.90 lakh | ₹0.00 | 11 | ₹140.82 |
| 2021-07-30 | ₹2.78 lakh | ₹2.27 lakh | ₹0.00 | 11 | ₹150.91 |
| 2021-08-27 | ₹2.93 lakh | ₹2.52 lakh | ₹0.00 | 12 | ₹145.65 |
| 2021-09-24 | ₹3.76 lakh | ₹3.31 lakh | ₹15,087.88 | 11 | ₹150.11 |
| 2021-10-29 | ₹6.00 lakh | ₹5.30 lakh | ₹94,192.61 | 10 | ₹151.74 |
| 2021-11-26 | ₹10.63 lakh | ₹10.26 lakh | ₹6.32 lakh | 7 | ₹151.68 |
| 2021-12-31 | ₹21.55 lakh | ₹20.73 lakh | ₹1.05 lakh | 11 | ₹156.78 |
| 2022-01-28 | ₹32.95 lakh | ₹33.26 lakh | ₹12.35 lakh | 10 | ₹155.36 |
| 2022-02-25 | ₹58.58 lakh | ₹66.93 lakh | ₹37.21 lakh | 7 | ₹140.66 |
| 2022-03-25 | ₹77.09 lakh | ₹79.17 lakh | ₹2.34 lakh | 12 | ₹144.83 |
| 2022-04-29 | ₹1.52 crore | ₹1.61 crore | ₹30.46 lakh | 10 | ₹139.51 |
| 2022-05-27 | ₹1.87 crore | ₹2.23 crore | ₹26.47 lakh | 12 | ₹122.43 |
| 2022-06-24 | ₹3.12 crore | ₹3.45 crore | ₹78,013.31 | 11 | ₹124.61 |
| 2022-07-29 | ₹8.78 crore | ₹8.31 crore | ₹5.81 lakh | 11 | ₹135.02 |
| 2022-08-26 | ₹15.28 crore | ₹13.91 crore | ₹0.00 | 12 | ₹144.71 |
| 2022-09-30 | ₹26.63 crore | ₹26.44 crore | ₹7.77 crore | 11 | ₹143.56 |
| 2022-10-28 | ₹32.82 crore | ₹32.49 crore | ₹1.14 crore | 13 | ₹147.33 |
| 2022-11-25 | ₹64.09 crore | ₹58.01 crore | ₹1.36 crore | 13 | ₹158.26 |
| 2022-12-30 | ₹103.31 crore | ₹109.94 crore | ₹80.32 crore | 6 | ₹151.20 |
| 2023-01-27 | ₹133.63 crore | ₹149.17 crore | ₹7.41 crore | 13 | ₹142.09 |
| 2023-02-24 | ₹202.14 crore | ₹219.23 crore | ₹23.74 crore | 11 | ₹140.25 |
| 2023-03-31 | ₹527.70 crore | ₹547.21 crore | ₹250.71 crore | 8 | ₹144.82 |
| 2023-04-28 | ₹824.76 crore | ₹801.15 crore | ₹0.00 | 13 | ₹157.23 |
| 2023-05-26 | ₹1,493.55 crore | ₹1,333.18 crore | ₹0.00 | 13 | ₹170.69 |
| 2023-06-30 | ₹2,492.11 crore | ₹2,244.69 crore | ₹45.91 crore | 12 | ₹179.48 |
| 2023-07-28 | ₹3,404.72 crore | ₹3,102.16 crore | ₹40.19 crore | 10 | ₹180.27 |
| 2023-08-25 | ₹5,025.71 crore | ₹4,067.87 crore | ₹77.59 crore | 10 | ₹203.19 |
| 2023-09-29 | ₹7,018.84 crore | ₹5,857.48 crore | ₹77.59 crore | 10 | ₹208.14 |
| 2023-10-27 | ₹7,420.41 crore | ₹6,212.07 crore | ₹745.62 crore | 8 | ₹204.23 |
| 2023-11-24 | ₹8,265.12 crore | ₹7,089.97 crore | ₹0.00 | 12 | ₹208.97 |
| 2023-12-29 | ₹19,734.52 crore | ₹18,319.37 crore | ₹0.00 | 12 | ₹214.88 |
| 2024-01-25 | ₹28,334.71 crore | ₹26,972.86 crore | ₹0.00 | 11 | ₹218.56 |
| 2024-02-23 | ₹47,552.07 crore | ₹47,653.49 crore | ₹0.00 | 12 | ₹226.65 |
| 2024-03-28 | ₹68,922.65 crore | ₹71,310.81 crore | ₹0.00 | 13 | ₹227.32 |
| 2024-04-26 | ₹1.11 lakh crore | ₹1.07 lakh crore | ₹0.00 | 13 | ₹229.17 |
| 2024-05-31 | ₹1.70 lakh crore | ₹1.71 lakh crore | ₹32,070.13 crore | 11 | ₹229.40 |
| 2024-06-28 | ₹3.02 lakh crore | ₹3.04 lakh crore | ₹0.00 | 12 | ₹236.39 |
| 2024-07-26 | ₹4.35 lakh crore | ₹4.41 lakh crore | ₹4,898.69 crore | 13 | ₹236.76 |
| 2024-08-30 | ₹6.39 lakh crore | ₹6.56 lakh crore | ₹0.00 | 13 | ₹227.19 |
| 2024-09-27 | ₹8.32 lakh crore | ₹8.17 lakh crore | ₹0.00 | 13 | ₹237.15 |
| 2024-10-25 | ₹9.03 lakh crore | ₹10.18 lakh crore | ₹2.74 lakh crore | 10 | ₹211.30 |
| 2024-11-29 | ₹14.03 lakh crore | ₹15.55 lakh crore | ₹0.00 | 13 | ₹213.27 |
| 2024-12-27 | ₹26.12 lakh crore | ₹27.36 lakh crore | ₹3.38 lakh crore | 11 | ₹215.36 |
| 2025-01-31 | ₹29.51 lakh crore | ₹34.16 lakh crore | ₹12.03 lakh crore | 9 | ₹196.82 |
| 2025-02-28 | ₹40.93 lakh crore | ₹48.75 lakh crore | ₹5.09 lakh crore | 11 | ₹180.24 |
| 2025-03-27 | ₹68.25 lakh crore | ₹71.82 lakh crore | ₹0.00 | 12 | ₹196.87 |
| 2025-04-25 | ₹99.17 lakh crore | ₹96.74 lakh crore | ₹13.39 lakh crore | 11 | ₹207.10 |
| 2025-05-30 | ₹1.68 crore crore | ₹1.80 crore crore | ₹38.67 lakh crore | 11 | ₹196.66 |
| 2025-06-27 | ₹2.24 crore crore | ₹2.19 crore crore | ₹2.08 lakh crore | 13 | ₹206.84 |
| 2025-07-25 | ₹3.80 crore crore | ₹3.84 crore crore | ₹77.10 lakh crore | 12 | ₹204.12 |
| 2025-08-29 | ₹4.79 crore crore | ₹5.16 crore crore | ₹36.49 lakh crore | 14 | ₹186.87 |
| 2025-09-26 | ₹8.35 crore crore | ₹8.94 crore crore | ₹4.57 crore crore | 10 | ₹188.63 |
| 2025-10-31 | ₹14.64 crore crore | ₹15.50 crore crore | ₹0.00 | 15 | ₹189.40 |
| 2025-11-28 | ₹23.21 crore crore | ₹23.87 crore crore | ₹2.32 crore crore | 13 | ₹185.08 |
| 2025-12-26 | ₹37.42 crore crore | ₹35.08 crore crore | ₹56.34 lakh crore | 13 | ₹186.16 |
| 2026-01-30 | ₹63.51 crore crore | ₹58.83 crore crore | ₹2.17 crore crore | 11 | ₹183.62 |
| 2026-02-27 | ₹109.91 crore crore | ₹114.17 crore crore | ₹30.76 crore crore | 11 | ₹175.40 |
| 2026-03-27 | ₹164.21 crore crore | ₹179.44 crore crore | ₹68.84 crore crore | 9 | ₹164.14 |
| 2026-04-30 | ₹240.89 crore crore | ₹240.92 crore crore | ₹0.00 | 12 | ₹172.59 |
| 2026-05-29 | ₹655.58 crore crore | ₹655.84 crore crore | ₹9.25 crore crore | 12 | ₹177.34 |
| 2026-06-25 | ₹1,040.41 crore crore | ₹1,017.37 crore crore | ₹0.00 | 12 | ₹176.77 |
| 2026-07-31 | ₹1,979.65 crore crore | ₹1,955.76 crore crore | ₹139.75 crore crore | 11 | ₹179.24 |
| 2026-08-28 | ₹3,059.21 crore crore | ₹2,619.39 crore crore | ₹0.00 | 12 | ₹199.48 |
| 2026-09-11 | ₹4,356.62 crore crore | ₹3,872.38 crore crore | ₹0.00 | 12 | ₹204.17 |

## Engine B — still held at the end

| Stock | First entry | Blended entry ₹ | Lots | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|---:|
| ABB | 2026-03-02 | 6,642.56 | 4 | 7,274.00 | 7,158.25 | +9.5% |
| APOLLOPIPE | 2026-03-16 | 490.37 | 4 | 554.90 | 440.44 | +13.2% |
| BLUESTONE | 2026-07-27 | 826.57 | 3 | 890.35 | 747.41 | +7.7% |
| CAPLIPOINT | 2026-05-18 | 2,367.83 | 4 | 2,754.90 | 2,376.52 | +16.3% |
| CHENNPETRO | 2026-04-06 | 1,152.36 | 4 | 1,572.90 | 1,242.60 | +36.5% |
| JTLINFRA | 2022-10-24 | 292.00 | 1 | 295.80 | 217.12 | +1.3% |
| LIQUID1 | 2026-03-30 | 1,100.91 | 3 | 1,122.52 | 1,047.51 | +2.0% |
| LIQUIDPLUS | 2026-02-09 | 1,085.23 | 4 | 1,103.07 | 1,039.82 | +1.6% |
| ORIENTREF | 2021-04-26 | 324.61 | 4 | 322.40 | 301.44 | -0.7% |
| RATNAVEER | 2026-08-03 | 260.32 | 4 | 288.30 | 263.29 | +10.7% |
| RUBICON | 2026-06-08 | 1,442.40 | 4 | 1,835.40 | 1,653.47 | +27.2% |
| SUBEX | 2020-10-19 | 15.55 | 1 | 16.95 | 11.11 | +9.0% |

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
| DYNPRO | 2020-08-03 | 203.35 | 2 | 2020-08-31 | 186.68 | -8.2% |
| APCOTEXIND | 2020-08-24 | 161.23 | 2 | 2020-08-31 | 151.95 | -5.8% |
| GOLDBEES | 2020-04-13 | 43.84 | 2 | 2020-09-04 | 41.00 | -6.5% |
| CADILAHC | 2020-04-27 | 377.33 | 4 | 2020-09-08 | 364.99 | -3.3% |
| KIRLOSBROS | 2020-07-27 | 132.77 | 3 | 2020-09-08 | 120.79 | -9.0% |
| TAJGVK | 2020-04-27 | 142.96 | 3 | 2020-09-22 | 126.45 | -11.5% |
| SATIA | 2020-09-14 | 122.00 | 1 | 2020-09-22 | 102.97 | -15.6% |
| HDFCMFGETF | 2020-04-20 | 4,685.38 | 3 | 2020-09-23 | 4,492.07 | -4.1% |
| AARTIDRUGS | 2020-08-24 | 3,064.61 | 2 | 2020-09-30 | 2,264.30 | -26.1% |
| PRINCEPIPE | 2020-09-07 | 225.49 | 3 | 2020-10-12 | 220.88 | -2.0% |
| INDIAMART | 2020-09-07 | 2,421.33 | 3 | 2020-10-19 | 2,315.62 | -4.4% |
| THYROCARE | 2020-08-24 | 1,020.49 | 4 | 2020-11-12 | 1,016.50 | -0.4% |
| VIDHIING | 2020-09-28 | 120.59 | 2 | 2020-12-02 | 115.50 | -4.2% |
| ESTER | 2020-10-26 | 119.40 | 2 | 2020-12-21 | 101.25 | -15.2% |
| SYNGENE | 2020-04-27 | 442.96 | 4 | 2020-12-22 | 562.40 | +27.0% |
| TCI | 2020-09-14 | 248.49 | 3 | 2020-12-22 | 234.75 | -5.5% |
| ITDC | 2020-12-28 | 344.15 | 2 | 2021-01-18 | 304.38 | -11.6% |
| JSLHISAR | 2020-11-17 | 147.20 | 4 | 2021-01-22 | 142.59 | -3.1% |
| TATASTLBSL | 2020-11-17 | 39.71 | 3 | 2021-01-22 | 40.61 | +2.3% |
| SAKSOFT | 2020-09-28 | 382.48 | 2 | 2021-01-25 | 341.10 | -10.8% |
| JUSTDIAL | 2020-10-26 | 637.80 | 3 | 2021-01-25 | 622.35 | -2.4% |
| TRENT | 2020-11-17 | 483.35 | 2 | 2021-01-29 | 417.53 | -13.6% |
| DCW | 2021-01-25 | 25.82 | 3 | 2021-03-18 | 25.79 | -0.1% |
| TATAMOTORS | 2021-01-25 | 318.85 | 3 | 2021-03-19 | 296.97 | -6.9% |
| APTECHT | 2021-02-01 | 219.72 | 4 | 2021-03-19 | 204.25 | -7.0% |
| CENTENKA | 2021-03-22 | 264.00 | 1 | 2021-03-25 | 229.90 | -12.9% |
| PAISALO | 2020-12-28 | 73.50 | 4 | 2021-04-12 | 72.41 | -1.5% |
| CENTRUM | 2021-03-30 | 28.40 | 1 | 2021-04-12 | 24.89 | -12.4% |
| PRAKASH | 2021-03-22 | 72.57 | 2 | 2021-04-19 | 74.58 | +2.8% |
| POLYMED | 2020-09-07 | 593.42 | 4 | 2021-06-14 | 950.00 | +60.1% |
| VIDHIING | 2021-03-22 | 201.70 | 3 | 2021-06-18 | 182.64 | -9.4% |
| WELSPUNIND | 2021-03-22 | 106.37 | 4 | 2021-08-10 | 124.64 | +17.2% |
| MOREPENLAB | 2021-04-19 | 54.89 | 3 | 2021-08-10 | 56.33 | +2.6% |
| SUPPETRO | 2021-04-26 | 733.36 | 3 | 2021-09-13 | 703.10 | -4.1% |
| GDL | 2021-01-25 | 209.76 | 4 | 2021-09-20 | 266.00 | +26.8% |
| KEI | 2021-03-22 | 574.37 | 4 | 2021-10-22 | 853.10 | +48.5% |
| BASF | 2021-08-16 | 3,460.21 | 3 | 2021-10-25 | 3,220.59 | -6.9% |
| INDOCO | 2021-08-16 | 484.30 | 1 | 2021-11-12 | 412.30 | -14.9% |
| DEEPAKFERT | 2021-03-22 | 281.00 | 4 | 2021-11-18 | 368.55 | +31.2% |
| HATSUN | 2021-09-20 | 1,406.99 | 2 | 2021-11-22 | 1,255.19 | -10.8% |
| SHOPERSTOP | 2021-10-25 | 363.06 | 3 | 2021-11-22 | 335.82 | -7.5% |
| TATAINVEST | 2021-08-16 | 1,294.09 | 4 | 2021-11-26 | 1,436.49 | +11.0% |
| TTKPRESTIG | 2021-11-01 | 11,245.38 | 2 | 2021-11-26 | 10,070.05 | -10.5% |
| SOMANYCERA | 2021-06-21 | 815.79 | 4 | 2021-11-29 | 755.11 | -7.4% |
| MAHLOG | 2021-01-25 | 531.95 | 4 | 2021-11-30 | 654.55 | +23.0% |
| SUPRAJIT | 2021-11-22 | 447.50 | 2 | 2021-12-13 | 391.40 | -12.5% |
| TCIEXP | 2021-11-01 | 2,118.52 | 4 | 2021-12-21 | 2,039.74 | -3.7% |
| MINDAIND | 2021-12-20 | 1,166.36 | 3 | 2022-01-07 | 1,088.41 | -6.7% |
| LTTS | 2020-10-19 | 2,220.53 | 4 | 2022-01-21 | 4,856.88 | +118.7% |
| MIRZAINT | 2021-12-06 | 134.19 | 3 | 2022-01-24 | 143.07 | +6.6% |
| SWANENERGY | 2022-01-10 | 169.65 | 2 | 2022-01-25 | 162.64 | -4.1% |
| SHARDACROP | 2022-01-31 | 623.38 | 2 | 2022-02-11 | 545.30 | -12.5% |
| BSOFT | 2021-11-29 | 475.09 | 2 | 2022-02-14 | 424.65 | -10.6% |
| RAYMOND | 2021-11-29 | 703.20 | 3 | 2022-02-15 | 679.35 | -3.4% |
| ANDHRSUGAR | 2022-01-31 | 160.92 | 2 | 2022-02-21 | 135.28 | -15.9% |
| OMAXE | 2022-02-14 | 97.75 | 2 | 2022-02-21 | 89.39 | -8.6% |
| ZEELEARN | 2022-01-10 | 16.70 | 2 | 2022-02-22 | 13.28 | -20.5% |
| TV18BRDCST | 2022-01-31 | 63.72 | 3 | 2022-02-22 | 58.38 | -8.4% |
| COMPINFO | 2022-01-10 | 44.00 | 2 | 2022-02-24 | 29.08 | -33.9% |
| ESCORTS | 2021-11-29 | 1,870.85 | 3 | 2022-02-25 | 1,754.65 | -6.2% |
| BSE | 2021-12-06 | 1,869.99 | 2 | 2022-03-21 | 1,634.39 | -12.6% |
| EXCELINDUS | 2022-03-07 | 1,603.38 | 2 | 2022-03-29 | 1,438.30 | -10.3% |
| STEELXIND | 2021-12-27 | 20.90 | 2 | 2022-04-20 | 21.56 | +3.2% |
| EVERESTIND | 2022-02-21 | 705.00 | 3 | 2022-04-28 | 594.70 | -15.6% |
| GTLINFRA | 2022-03-07 | 1.63 | 2 | 2022-04-29 | 1.41 | -13.2% |
| RCF | 2022-04-04 | 100.30 | 2 | 2022-05-04 | 93.15 | -7.1% |
| SRHHYPOLTD | 2022-03-07 | 433.98 | 2 | 2022-05-05 | 431.30 | -0.6% |
| GNFC | 2022-02-14 | 698.36 | 3 | 2022-05-06 | 792.16 | +13.4% |
| MAWANASUG | 2022-03-07 | 149.05 | 3 | 2022-05-09 | 135.09 | -9.4% |
| MANALIPETC | 2022-04-25 | 139.80 | 1 | 2022-05-11 | 99.75 | -28.6% |
| MFL | 2022-05-02 | 1,369.04 | 2 | 2022-05-11 | 1,225.50 | -10.5% |
| MOL | 2022-05-09 | 129.80 | 1 | 2022-05-11 | 113.62 | -12.5% |
| RIIL | 2022-05-02 | 1,070.02 | 2 | 2022-05-26 | 863.73 | -19.3% |
| GEPIL | 2022-05-09 | 182.65 | 1 | 2022-05-31 | 163.45 | -10.5% |
| BCG | 2021-11-29 | 134.10 | 1 | 2022-06-06 | 55.00 | -59.0% |
| VBL | 2022-05-16 | 220.00 | 1 | 2022-06-06 | 196.27 | -10.8% |
| GRAUWEIL | 2022-05-23 | 76.53 | 2 | 2022-06-13 | 61.82 | -19.2% |
| MRPL | 2022-05-09 | 87.37 | 3 | 2022-07-06 | 69.61 | -20.3% |
| JKIL | 2022-05-09 | 298.61 | 4 | 2022-08-05 | 308.80 | +3.4% |
| ICICIGOLD | 2022-03-14 | 46.20 | 1 | 2022-08-29 | 41.50 | -10.2% |
| MARATHON | 2022-07-11 | 235.21 | 4 | 2022-09-19 | 232.80 | -1.0% |
| WSTCSTPAPR | 2022-08-08 | 545.49 | 3 | 2022-09-22 | 533.28 | -2.2% |
| NAVNETEDUL | 2022-08-08 | 134.26 | 4 | 2022-09-26 | 127.30 | -5.2% |
| CENTRALBK | 2022-09-26 | 20.45 | 1 | 2022-10-17 | 18.95 | -7.3% |
| VADILALIND | 2022-05-23 | 2,029.48 | 4 | 2022-10-20 | 2,295.06 | +13.1% |
| APARINDS | 2022-06-20 | 1,157.19 | 4 | 2022-11-03 | 1,358.50 | +17.4% |
| CHEMCON | 2022-10-03 | 437.98 | 2 | 2022-11-04 | 394.35 | -10.0% |
| SCHNEIDER | 2022-09-26 | 183.10 | 2 | 2022-11-10 | 159.60 | -12.8% |
| ALLCARGO | 2022-10-03 | 439.83 | 2 | 2022-11-29 | 432.77 | -1.6% |
| ELECON | 2022-06-13 | 151.43 | 4 | 2022-12-21 | 202.49 | +33.7% |
| HEIDELBERG | 2022-09-26 | 203.98 | 3 | 2022-12-21 | 190.00 | -6.9% |
| LIKHITHA | 2022-12-05 | 248.23 | 2 | 2022-12-21 | 210.50 | -15.2% |
| SHANTIGEAR | 2022-06-06 | 314.55 | 4 | 2022-12-22 | 345.56 | +9.9% |
| ACC | 2022-05-23 | 2,241.61 | 4 | 2022-12-23 | 2,465.16 | +10.0% |
| KTKBANK | 2022-11-07 | 146.35 | 3 | 2022-12-23 | 139.84 | -4.4% |
| RVNL | 2022-11-07 | 66.08 | 4 | 2022-12-26 | 60.57 | -8.3% |
| WESTLIFE | 2022-10-03 | 750.44 | 3 | 2023-01-16 | 708.51 | -5.6% |
| PIIND | 2022-11-14 | 3,421.96 | 2 | 2023-01-23 | 3,123.65 | -8.7% |
| GICRE | 2023-01-02 | 183.12 | 2 | 2023-02-01 | 167.72 | -8.4% |
| LSIL | 2023-01-30 | 22.53 | 2 | 2023-02-07 | 20.04 | -11.0% |
| SPECIALITY | 2023-01-23 | 276.85 | 1 | 2023-02-14 | 221.73 | -19.9% |
| CGCL | 2022-03-07 | 711.44 | 3 | 2023-02-17 | 704.95 | -0.9% |
| SPIC | 2023-01-02 | 83.38 | 2 | 2023-02-23 | 65.74 | -21.2% |
| AXITA | 2023-02-13 | 67.00 | 1 | 2023-02-28 | 53.77 | -19.7% |
| YESBANK | 2023-01-02 | 18.95 | 2 | 2023-03-13 | 15.34 | -19.1% |
| IOB | 2023-01-02 | 29.25 | 2 | 2023-03-20 | 22.18 | -24.2% |
| JINDALSAW | 2023-01-02 | 64.60 | 3 | 2023-03-27 | 67.92 | +5.1% |
| SONATSOFTW | 2023-02-27 | 401.31 | 4 | 2023-03-29 | 371.45 | -7.4% |
| JSL | 2023-01-02 | 270.35 | 4 | 2023-04-13 | 256.98 | -4.9% |
| GSFC | 2023-01-02 | 159.39 | 3 | 2023-05-29 | 155.85 | -2.2% |
| MOLDTECH | 2023-02-06 | 255.82 | 4 | 2023-07-03 | 292.84 | +14.5% |
| ANURAS | 2023-03-20 | 1,058.50 | 3 | 2023-07-03 | 1,007.67 | -4.8% |
| HARIOMPIPE | 2023-01-02 | 433.91 | 4 | 2023-07-10 | 603.25 | +39.0% |
| KSB | 2023-04-10 | 452.20 | 2 | 2023-07-12 | 407.74 | -9.8% |
| CPSEETF | 2023-04-03 | 43.74 | 4 | 2023-07-31 | 41.97 | -4.0% |
| SETFGOLD | 2023-04-10 | 52.80 | 2 | 2023-10-03 | 49.74 | -5.8% |
| HAL | 2023-04-03 | 1,731.74 | 4 | 2023-10-25 | 1,840.70 | +6.3% |
| GENUSPOWER | 2023-07-10 | 207.87 | 4 | 2023-11-16 | 234.03 | +12.6% |
| BIRLAMONEY | 2023-11-20 | 113.83 | 2 | 2023-11-30 | 103.60 | -9.0% |
| DBL | 2023-08-07 | 353.59 | 3 | 2023-12-20 | 370.74 | +4.9% |
| TIIL | 2023-04-17 | 1,909.71 | 4 | 2024-01-17 | 2,337.00 | +22.4% |
| HIMATSEIDE | 2023-11-20 | 169.48 | 2 | 2024-01-18 | 156.75 | -7.5% |
| SAKSOFT | 2023-04-17 | 242.45 | 4 | 2024-02-12 | 305.02 | +25.8% |
| BALMLAWRIE | 2023-12-26 | 270.73 | 4 | 2024-02-12 | 240.49 | -11.2% |
| RVNL | 2024-01-23 | 313.49 | 2 | 2024-02-12 | 241.04 | -23.1% |
| SHAREINDIA | 2023-10-30 | 351.44 | 4 | 2024-03-06 | 357.20 | +1.6% |
| GEPIL | 2023-11-20 | 282.02 | 4 | 2024-03-06 | 273.88 | -2.9% |
| KCP | 2024-02-19 | 216.95 | 1 | 2024-03-12 | 167.91 | -22.6% |
| AEGISCHEM | 2024-02-19 | 438.47 | 2 | 2024-03-13 | 394.30 | -10.1% |
| RAIN | 2024-02-19 | 203.50 | 1 | 2024-03-13 | 154.40 | -24.1% |
| ZENTEC | 2023-07-17 | 749.95 | 4 | 2024-05-09 | 896.89 | +19.6% |
| FORCEMOT | 2024-03-18 | 8,659.96 | 3 | 2024-05-28 | 8,083.64 | -6.7% |
| SOLARINDS | 2023-11-20 | 7,936.88 | 3 | 2024-06-04 | 7,980.95 | +0.6% |
| TATAMTRDVR | 2023-12-04 | 572.65 | 4 | 2024-06-04 | 591.85 | +3.4% |
| SMSPHARMA | 2024-03-11 | 196.17 | 3 | 2024-06-04 | 181.36 | -7.5% |
| BHEL | 2024-03-11 | 285.48 | 2 | 2024-06-04 | 251.68 | -11.8% |
| BOSCHLTD | 2024-03-11 | 30,703.33 | 4 | 2024-06-04 | 29,015.09 | -5.5% |
| UNOMINDA | 2024-06-10 | 1,093.79 | 3 | 2024-07-19 | 981.87 | -10.2% |
| THERMAX | 2024-06-03 | 5,528.77 | 2 | 2024-08-05 | 4,719.70 | -14.6% |
| EMUDHRA | 2024-03-18 | 761.91 | 3 | 2024-08-13 | 793.11 | +4.1% |
| CAMPUS | 2024-06-03 | 289.67 | 3 | 2024-08-16 | 277.07 | -4.4% |
| DABUR | 2024-06-10 | 635.27 | 4 | 2024-10-03 | 602.49 | -5.2% |
| VGUARD | 2024-08-19 | 524.15 | 1 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 4,058.99 | 4 | 2024-10-07 | 4,485.14 | +10.5% |
| GEOJITFSL | 2024-07-22 | 136.23 | 3 | 2024-10-07 | 138.18 | +1.4% |
| EVEREADY | 2024-08-19 | 479.35 | 2 | 2024-10-07 | 423.27 | -11.7% |
| KIOCL | 2024-02-19 | 403.72 | 4 | 2024-10-22 | 342.29 | -15.2% |
| BASF | 2024-08-12 | 7,616.24 | 3 | 2024-10-22 | 7,611.30 | -0.1% |
| SUNTECK | 2024-07-22 | 592.92 | 2 | 2024-10-25 | 531.30 | -10.4% |
| NIFTYBEES | 2024-06-10 | 274.63 | 4 | 2024-11-14 | 262.66 | -4.4% |
| ASTRAZEN | 2024-10-07 | 7,396.38 | 2 | 2024-11-14 | 6,854.77 | -7.3% |
| PRECWIRE | 2024-10-14 | 205.18 | 2 | 2024-12-26 | 164.78 | -19.7% |
| AKZOINDIA | 2024-11-04 | 4,118.82 | 2 | 2024-12-27 | 3,423.18 | -16.9% |
| BANKBEES | 2024-06-10 | 526.98 | 2 | 2025-01-08 | 507.06 | -3.8% |
| PAYTM | 2024-10-28 | 936.85 | 4 | 2025-01-09 | 893.05 | -4.7% |
| GARFIBRES | 2024-11-25 | 946.01 | 2 | 2025-01-09 | 829.35 | -12.3% |
| SKIPPER | 2024-10-14 | 553.34 | 3 | 2025-01-10 | 477.28 | -13.7% |
| NSIL | 2024-11-25 | 8,837.95 | 2 | 2025-01-13 | 6,818.32 | -22.9% |
| KFINTECH | 2024-12-30 | 1,511.45 | 1 | 2025-01-15 | 1,159.14 | -23.3% |
| AEGISLOG | 2025-01-13 | 819.14 | 2 | 2025-01-24 | 700.36 | -14.5% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 1 | 2025-01-28 | 1,258.75 | -12.7% |
| APOLLO | 2025-01-20 | 131.50 | 1 | 2025-02-17 | 110.19 | -16.2% |
| BSE | 2024-10-14 | 4,919.52 | 3 | 2025-02-28 | 4,954.63 | +0.7% |
| ZENSARTECH | 2025-02-03 | 947.00 | 1 | 2025-03-03 | 727.84 | -23.1% |
| TAJGVK | 2025-02-24 | 481.17 | 3 | 2025-04-02 | 453.34 | -5.8% |
| BAJAJHCARE | 2025-01-20 | 649.82 | 3 | 2025-04-07 | 521.14 | -19.8% |
| HDFCGOLD | 2025-02-10 | 76.10 | 3 | 2025-04-07 | 71.44 | -6.1% |
| SETFGOLD | 2025-02-17 | 75.90 | 2 | 2025-04-07 | 69.36 | -8.6% |
| ITDCEM | 2024-10-07 | 554.03 | 4 | 2025-04-11 | 524.92 | -5.3% |
| GRMOVER | 2025-03-10 | 281.85 | 3 | 2025-05-07 | 290.80 | +3.2% |
| VADILALIND | 2025-04-07 | 6,081.19 | 3 | 2025-05-30 | 5,401.40 | -11.2% |
| TECHNOE | 2025-06-02 | 1,554.45 | 3 | 2025-07-24 | 1,467.84 | -5.6% |
| KPRMILL | 2025-05-12 | 1,205.40 | 3 | 2025-08-01 | 1,108.74 | -8.0% |
| JSWHL | 2024-11-18 | 21,485.12 | 3 | 2025-08-04 | 19,106.01 | -11.1% |
| NH | 2025-03-03 | 1,940.68 | 4 | 2025-08-04 | 1,814.78 | -6.5% |
| WHIRLPOOL | 2025-04-28 | 1,329.25 | 4 | 2025-08-07 | 1,301.97 | -2.1% |
| PUNJABCHEM | 2025-08-04 | 1,403.00 | 1 | 2025-08-18 | 1,208.88 | -13.8% |
| RAIN | 2025-08-11 | 160.25 | 1 | 2025-08-26 | 143.64 | -10.4% |
| RPOWER | 2025-06-02 | 58.64 | 1 | 2025-09-09 | 47.24 | -19.4% |
| SPIC | 2025-08-25 | 114.00 | 2 | 2025-09-23 | 97.50 | -14.5% |
| INDIASHLTR | 2025-04-15 | 915.18 | 4 | 2025-09-25 | 862.60 | -5.7% |
| BOMDYEING | 2025-07-28 | 181.54 | 4 | 2025-09-25 | 172.67 | -4.9% |
| BLISSGVS | 2025-08-11 | 178.60 | 1 | 2025-09-26 | 143.93 | -19.4% |
| OLECTRA | 2025-07-28 | 1,481.17 | 3 | 2025-10-14 | 1,416.64 | -4.4% |
| SUBROS | 2025-09-29 | 1,103.63 | 2 | 2025-10-14 | 1,046.90 | -5.1% |
| CREDITACC | 2025-01-27 | 1,084.34 | 4 | 2025-10-20 | 1,274.42 | +17.5% |
| NETWEB | 2025-09-08 | 3,637.45 | 3 | 2025-11-06 | 3,515.95 | -3.3% |
| PRAKASH | 2025-08-11 | 171.78 | 2 | 2025-11-14 | 147.31 | -14.2% |
| ANANDRATHI | 2025-10-20 | 1,570.73 | 2 | 2025-11-20 | 1,450.17 | -7.7% |
| SKYGOLD | 2025-10-27 | 363.51 | 2 | 2025-11-25 | 329.13 | -9.5% |
| SIRCA | 2025-08-11 | 499.33 | 4 | 2025-12-08 | 485.64 | -2.7% |
| NACLIND | 2025-04-07 | 160.03 | 2 | 2025-12-17 | 164.20 | +2.6% |
| TATSILV | 2025-10-20 | 19.92 | 2 | 2025-12-29 | 18.35 | -7.9% |
| KIRIINDUS | 2026-01-05 | 622.00 | 1 | 2026-01-08 | 525.16 | -15.6% |
| RADICO | 2025-11-24 | 3,289.40 | 1 | 2026-01-09 | 2,956.49 | -10.1% |
| AVANTIFEED | 2025-04-15 | 766.81 | 4 | 2026-01-21 | 748.60 | -2.4% |
| SANSERA | 2025-12-01 | 1,786.59 | 3 | 2026-01-23 | 1,672.76 | -6.4% |
| GMRAIRPORT | 2025-12-15 | 103.00 | 2 | 2026-01-23 | 92.10 | -10.6% |
| TATSILV | 2026-01-27 | 29.76 | 2 | 2026-02-02 | 23.03 | -22.6% |
| GROWWSLVR | 2026-01-27 | 27.64 | 2 | 2026-02-02 | 22.32 | -19.2% |
| APEX | 2026-02-09 | 420.94 | 3 | 2026-02-27 | 389.22 | -7.5% |
| CUB | 2025-11-10 | 268.69 | 4 | 2026-03-09 | 251.43 | -6.4% |
| SETFGOLD | 2025-09-29 | 110.51 | 4 | 2026-03-23 | 115.37 | +4.4% |
| GOLDIETF | 2025-09-29 | 119.63 | 4 | 2026-03-23 | 115.68 | -3.3% |
| SILVERIETF | 2025-09-29 | 194.11 | 3 | 2026-03-23 | 208.50 | +7.4% |
| HDFCSILVER | 2025-09-29 | 186.62 | 3 | 2026-03-23 | 201.50 | +8.0% |
| J&KBANK | 2026-03-02 | 117.18 | 3 | 2026-03-23 | 110.67 | -5.6% |
| AGIIL | 2026-01-12 | 300.29 | 2 | 2026-03-30 | 271.80 | -9.5% |
| TORNTPOWER | 2026-03-02 | 1,491.00 | 1 | 2026-03-30 | 1,315.84 | -11.7% |
| AETHER | 2026-03-30 | 1,186.79 | 3 | 2026-05-14 | 1,125.84 | -5.1% |
| BAJAJHIND | 2026-04-06 | 18.79 | 2 | 2026-05-14 | 17.96 | -4.4% |
| CPSEETF | 2026-02-09 | 105.98 | 4 | 2026-06-02 | 100.15 | -5.5% |
| NLCINDIA | 2026-05-18 | 349.83 | 2 | 2026-06-09 | 320.62 | -8.3% |
| NRBBEARING | 2026-06-15 | 435.00 | 2 | 2026-07-22 | 391.97 | -9.9% |
| THERMAX | 2026-04-13 | 4,508.08 | 4 | 2026-07-29 | 4,306.64 | -4.5% |

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
2020-06-12  DEEPAKNTR   SELL ₹17.59 at stop ₹474.05 (-4.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-06-15  PANACEABIO  BUY ₹16.52 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.27×, ladder rising; stop ₹114.11; charges ₹0.02)
2020-06-22  CADILAHC    PYRAMID BUY ₹19.68 at ₹365.95 (box jump — doubling the stake with NEW capital; stop stays ₹338.53; charges ₹0.02)
2020-06-22  EIDPARRY    PYRAMID BUY ₹17.21 at ₹267.45 (box jump — doubling the stake with NEW capital; stop stays ₹204.49; charges ₹0.02)
2020-06-22  MANGCHEFER  PYRAMID BUY ₹22.89 at ₹36.60 (box jump — doubling the stake with NEW capital; stop stays ₹33.73; charges ₹0.03)
2020-06-22  TAJGVK      PYRAMID BUY ₹20.74 at ₹155.70 (box jump — doubling the stake with NEW capital; stop stays ₹126.45; charges ₹0.02)
2020-06-29  PANACEABIO  PYRAMID BUY ₹14.64 at ₹204.00 (box jump — doubling the stake with NEW capital; stop stays ₹169.29; charges ₹0.02)
2020-07-06  EIDPARRY    PYRAMID BUY ₹34.21 at ₹266.00 (box jump — doubling the stake with NEW capital; stop stays ₹249.19; charges ₹0.04)
2020-07-06  SYNGENE     PYRAMID BUY ₹24.42 at ₹438.00 (box jump — doubling the stake with NEW capital; stop stays ₹378.10; charges ₹0.03)
2020-07-13  AXISGOLD    PYRAMID BUY ₹18.68 at ₹4,295.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,971.05; charges ₹0.02)
2020-07-23  AXISGOLD    SELL ₹34.49 at stop ₹3,971.05 (-6.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2020-07-27  EIDPARRY    PYRAMID BUY ₹75.59 at ₹294.00 (box jump — doubling the stake with NEW capital; stop stays ₹273.03; charges ₹0.09)
2020-07-27  KIRLOSBROS  BUY ₹40.71 at ₹122.55 (fresh Friday signal — ACCUMULATE: 9.32× weekly, month 6.82×, ladder rising; stop ₹97.15; charges ₹0.05)
2020-07-31  MANGCHEFER  SELL ₹42.11 at stop ₹33.73 (-4.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2020-08-03  DYNPRO      BUY ₹42.11 at ₹200.00 (fresh Friday signal — BUY: 6.82× weekly, month 11.46×, ladder rising; stop ₹156.56; charges ₹0.05)
2020-08-03  PANACEABIO  PYRAMID BUY ₹32.69 at ₹227.95 (box jump — doubling the stake with NEW capital; stop stays ₹184.01; charges ₹0.04)
2020-08-10  DYNPRO      PYRAMID BUY ₹43.47 at ₹206.70 (box jump — doubling the stake with NEW capital; stop stays ₹186.68; charges ₹0.05)
2020-08-10  HDFCMFGETF  PYRAMID BUY ₹20.10 at ₹4,989.95 (box jump — doubling the stake with NEW capital; stop stays ₹4,492.07; charges ₹0.02)
2020-08-10  KIRLOSBROS  PYRAMID BUY ₹47.93 at ₹144.45 (box jump — doubling the stake with NEW capital; stop stays ₹119.79; charges ₹0.06)
2020-08-17  CADILAHC    PYRAMID BUY ₹42.92 at ₹399.15 (box jump — doubling the stake with NEW capital; stop stays ₹364.99; charges ₹0.05)
2020-08-17  EIDPARRY    SELL ₹140.17 at stop ₹273.03 (+2.1%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2020-08-17  SYNGENE     PYRAMID BUY ₹55.02 at ₹493.80 (box jump — doubling the stake with NEW capital; stop stays ₹434.44; charges ₹0.07)
2020-08-20  PANACEABIO  SELL ₹52.69 at stop ₹184.01 (-17.3%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2020-08-24  AARTIDRUGS  BUY ₹44.47 at ₹3,250.00 (fresh Friday signal — BUY: 5.29× weekly, month 7.63×, ladder rising; stop ₹1,888.30; charges ₹0.05)
2020-08-24  APCOTEXIND  BUY ₹74.10 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.09)
2020-08-24  GOLDBEES    PYRAMID BUY ₹9.90 at ₹46.45 (box jump — doubling the stake with NEW capital; stop stays ₹41.00; charges ₹0.01)
2020-08-24  KIRLOSBROS  PYRAMID BUY ₹87.57 at ₹132.05 (box jump — doubling the stake with NEW capital; stop stays ₹120.79; charges ₹0.10)
2020-08-24  THYROCARE   BUY ₹74.30 at ₹790.05 (fresh Friday signal — BUY: 7.11× weekly, month 4.47×, ladder rising; stop ₹599.31; charges ₹0.09)
2020-08-31  APCOTEXIND  PYRAMID BUY ₹70.67 at ₹157.50 (box jump — doubling the stake with NEW capital; stop stays ₹151.95; charges ₹0.08)
2020-08-31  APCOTEXIND  SELL ₹136.13 at stop ₹151.95 (-5.8%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2020-08-31  DYNPRO      SELL ₹78.40 at stop ₹186.68 (-8.2%, charges ₹0.08) — the cash goes back to work at the next Friday screen
2020-09-04  GOLDBEES    SELL ₹17.44 at stop ₹41.00 (-6.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-09-07  AARTIDRUGS  PYRAMID BUY ₹39.34 at ₹2,879.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,264.30; charges ₹0.05)
2020-09-07  INDIAMART   BUY ₹87.01 at ₹2,124.50 (fresh Friday signal — BUY: 2.47× weekly, month 1.96×, ladder rising; stop ₹1,655.61; charges ₹0.10)
2020-09-07  POLYMED     BUY ₹57.82 at ₹449.70 (fresh Friday signal — BUY: 2.13× weekly, month 2.67×, ladder rising; stop ₹372.40; charges ₹0.07)
2020-09-07  PRINCEPIPE  BUY ₹87.14 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.10)
2020-09-07  THYROCARE   PYRAMID BUY ₹70.92 at ₹755.00 (box jump — doubling the stake with NEW capital; stop stays ₹705.09; charges ₹0.08)
2020-09-08  CADILAHC    SELL ₹78.36 at stop ₹364.99 (-3.3%, charges ₹0.08) — the cash goes back to work at the next Friday screen
2020-09-08  KIRLOSBROS  SELL ₹159.95 at stop ₹120.79 (-9.0%, charges ₹0.17) — the cash goes back to work at the next Friday screen
2020-09-14  POLYMED     PYRAMID BUY ₹61.90 at ₹481.95 (box jump — doubling the stake with NEW capital; stop stays ₹408.50; charges ₹0.07)
2020-09-14  SATIA       BUY ₹97.74 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.16×, ladder rising; stop ₹102.97; charges ₹0.12)
2020-09-14  TCI         BUY ₹97.75 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.76× weekly, month 3.77×, ladder rising; stop ₹190.07; charges ₹0.12)
2020-09-21  INDIAMART   PYRAMID BUY ₹103.14 at ₹2,521.28 (box jump — doubling the stake with NEW capital; stop stays ₹2,099.50; charges ₹0.12)
2020-09-21  PRINCEPIPE  PYRAMID BUY ₹93.73 at ₹224.00 (box jump — doubling the stake with NEW capital; stop stays ₹178.66; charges ₹0.11)
2020-09-22  SATIA       SELL ₹82.31 at stop ₹102.97 (-15.6%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹33.63 at stop ₹126.45 (-11.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2020-09-23  HDFCMFGETF  SELL ₹36.14 at stop ₹4,492.07 (-4.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2020-09-28  SAKSOFT     BUY ₹118.28 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.14)
2020-09-28  VIDHIING    BUY ₹76.61 at ₹111.70 (fresh Friday signal — BUY: 4.70× weekly, month 4.56×, ladder rising; stop ₹77.90; charges ₹0.09)
2020-09-30  AARTIDRUGS  SELL ₹61.79 at stop ₹2,264.30 (-26.1%, charges ₹0.06) — the cash goes back to work at the next Friday screen
2020-10-05  POLYMED     PYRAMID BUY ₹120.74 at ₹470.35 (box jump — doubling the stake with NEW capital; stop stays ₹420.11; charges ₹0.14)
2020-10-05  TCI         PYRAMID BUY ₹92.55 at ₹229.40 (box jump — doubling the stake with NEW capital; stop stays ₹202.40; charges ₹0.11)
2020-10-12  INDIAMART   PYRAMID BUY ₹206.05 at ₹2,520.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,315.62; charges ₹0.24)
2020-10-12  PRINCEPIPE  PYRAMID BUY ₹196.55 at ₹235.00 (box jump — doubling the stake with NEW capital; stop stays ₹220.88; charges ₹0.23)
2020-10-12  PRINCEPIPE  SELL ₹368.87 at stop ₹220.88 (-2.0%, charges ₹0.38) — the cash goes back to work at the next Friday screen
2020-10-19  INDIAMART   SELL ₹378.06 at stop ₹2,315.62 (-4.4%, charges ₹0.39) — the cash goes back to work at the next Friday screen
2020-10-19  LTTS        BUY ₹207.95 at ₹1,745.00 (fresh Friday signal — BUY: 4.76× weekly, month 2.59×, ladder rising; stop ₹1,482.95; charges ₹0.25)
2020-10-19  SUBEX       BUY ₹207.78 at ₹15.55 (fresh Friday signal — BUY: 6.85× weekly, month 4.86×, ladder rising; stop ₹11.11; charges ₹0.25)
2020-10-19  THYROCARE   PYRAMID BUY ₹194.21 at ₹1,034.45 (box jump — doubling the stake with NEW capital; stop stays ₹933.42; charges ₹0.23)
2020-10-19  VIDHIING    PYRAMID BUY ₹88.71 at ₹129.50 (box jump — doubling the stake with NEW capital; stop stays ₹115.50; charges ₹0.11)
2020-10-26  ESTER       BUY ₹182.66 at ₹119.90 (fresh Friday signal — BUY: 4.14× weekly, month 4.67×, ladder rising; stop ₹83.98; charges ₹0.22)
2020-10-26  JUSTDIAL    BUY ₹210.32 at ₹584.00 (fresh Friday signal — BUY: 4.99× weekly, month 1.82×, ladder rising; stop ₹383.80; charges ₹0.25)
2020-11-09  ESTER       PYRAMID BUY ₹180.92 at ₹118.90 (box jump — doubling the stake with NEW capital; stop stays ₹101.25; charges ₹0.21)
2020-11-09  THYROCARE   PYRAMID BUY ₹426.94 at ₹1,137.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,016.50; charges ₹0.51)
2020-11-12  THYROCARE   SELL ₹761.68 at stop ₹1,016.50 (-0.4%, charges ₹0.79) — the cash goes back to work at the next Friday screen
2020-11-17  JSLHISAR    BUY ₹262.13 at ₹119.70 (fresh Friday signal — BUY: 2.03× weekly, month 1.66×, ladder rising; stop ₹89.02; charges ₹0.31)
2020-11-17  TATASTLBSL  BUY ₹237.01 at ₹30.95 (fresh Friday signal — BUY: 2.01× weekly, month 2.00×, ladder rising; stop ₹22.80; charges ₹0.28)
2020-11-17  TRENT       BUY ₹262.55 at ₹503.33 (fresh Friday signal — ACCUMULATE: 3.30× weekly, month 1.95×, ladder rising; stop ₹367.93; charges ₹0.31)
2020-11-23  JUSTDIAL    PYRAMID BUY ₹223.85 at ₹622.30 (box jump — doubling the stake with NEW capital; stop stays ₹523.11; charges ₹0.27)
2020-11-23  LTTS        PYRAMID BUY ₹199.11 at ₹1,672.75 (box jump — doubling the stake with NEW capital; stop stays ₹1,545.70; charges ₹0.24)
2020-12-02  VIDHIING    SELL ₹157.99 at stop ₹115.50 (-4.2%, charges ₹0.16) — the cash goes back to work at the next Friday screen
2020-12-07  TCI         PYRAMID BUY ₹210.72 at ₹261.30 (box jump — doubling the stake with NEW capital; stop stays ₹234.75; charges ₹0.25)
2020-12-14  JSLHISAR    PYRAMID BUY ₹292.65 at ₹133.80 (box jump — doubling the stake with NEW capital; stop stays ₹106.69; charges ₹0.35)
2020-12-14  TRENT       PYRAMID BUY ₹241.40 at ₹463.33 (box jump — doubling the stake with NEW capital; stop stays ₹417.53; charges ₹0.29)
2020-12-21  ESTER       SELL ₹307.63 at stop ₹101.25 (-15.2%, charges ₹0.32) — the cash goes back to work at the next Friday screen
2020-12-21  LTTS        PYRAMID BUY ₹525.60 at ₹2,209.15 (box jump — doubling the stake with NEW capital; stop stays ₹1,712.85; charges ₹0.62)
2020-12-21  TATASTLBSL  PYRAMID BUY ₹291.41 at ₹38.10 (box jump — doubling the stake with NEW capital; stop stays ₹34.30; charges ₹0.35)
2020-12-22  SYNGENE     SELL ₹125.13 at stop ₹562.40 (+27.0%, charges ₹0.13) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹377.99 at stop ₹234.75 (-5.5%, charges ₹0.39) — the cash goes back to work at the next Friday screen
2020-12-28  ITDC        BUY ₹479.14 at ₹338.55 (fresh Friday signal — BUY: 10.22× weekly, month 4.03×, ladder rising; stop ₹247.29; charges ₹0.57)
2020-12-28  PAISALO     BUY ₹489.61 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.58)
2021-01-04  ITDC        PYRAMID BUY ₹494.40 at ₹349.75 (box jump — doubling the stake with NEW capital; stop stays ₹304.38; charges ₹0.59)
2021-01-04  PAISALO     PYRAMID BUY ₹617.40 at ₹71.95 (box jump — doubling the stake with NEW capital; stop stays ₹36.33; charges ₹0.73)
2021-01-11  JSLHISAR    PYRAMID BUY ₹699.07 at ₹159.90 (box jump — doubling the stake with NEW capital; stop stays ₹129.68; charges ₹0.83)
2021-01-11  LTTS        PYRAMID BUY ₹1,180.57 at ₹2,482.50 (box jump — doubling the stake with NEW capital; stop stays ₹2,194.50; charges ₹1.40)
2021-01-11  PAISALO     PYRAMID BUY ₹1,208.51 at ₹70.46 (box jump — doubling the stake with NEW capital; stop stays ₹62.70; charges ₹1.43)
2021-01-18  ITDC        SELL ₹859.14 at stop ₹304.38 (-11.6%, charges ₹0.89) — the cash goes back to work at the next Friday screen
2021-01-18  JSLHISAR    PYRAMID BUY ₹1,320.41 at ₹151.10 (box jump — doubling the stake with NEW capital; stop stays ₹142.59; charges ₹1.56)
2021-01-18  SAKSOFT     PYRAMID BUY ₹108.52 at ₹366.25 (box jump — doubling the stake with NEW capital; stop stays ₹341.10; charges ₹0.13)
2021-01-18  TATASTLBSL  PYRAMID BUY ₹686.44 at ₹44.90 (box jump — doubling the stake with NEW capital; stop stays ₹40.61; charges ₹0.81)
2021-01-22  JSLHISAR    SELL ₹2,488.03 at stop ₹142.59 (-3.1%, charges ₹2.58) — the cash goes back to work at the next Friday screen
2021-01-22  TATASTLBSL  SELL ₹1,239.68 at stop ₹40.61 (+2.3%, charges ₹1.29) — the cash goes back to work at the next Friday screen
2021-01-25  DCW         BUY ₹1,129.01 at ₹23.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.83×, ladder rising; stop ₹16.00; charges ₹1.34)
2021-01-25  GDL         BUY ₹1,124.74 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹1.33)
2021-01-25  JUSTDIAL    PYRAMID BUY ₹483.53 at ₹672.50 (box jump — doubling the stake with NEW capital; stop stays ₹622.35; charges ₹0.57)
2021-01-25  JUSTDIAL    SELL ₹893.49 at stop ₹622.35 (-2.4%, charges ₹0.93) — the cash goes back to work at the next Friday screen
2021-01-25  MAHLOG      BUY ₹1,136.66 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹1.35)
2021-01-25  SAKSOFT     SELL ₹201.81 at stop ₹341.10 (-10.8%, charges ₹0.21) — the cash goes back to work at the next Friday screen
2021-01-25  TATAMOTORS  BUY ₹1,135.93 at ₹296.90 (fresh Friday signal — BUY: 3.10× weekly, month 2.05×, ladder rising; stop ₹171.38; charges ₹1.35)
2021-01-29  TRENT       SELL ₹434.36 at stop ₹417.53 (-13.6%, charges ₹0.45) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹1,111.76 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹1.32)
2021-02-08  APTECHT     PYRAMID BUY ₹1,344.10 at ₹216.00 (box jump — doubling the stake with NEW capital; stop stays ₹163.06; charges ₹1.59)
2021-02-08  DCW         PYRAMID BUY ₹1,005.10 at ₹20.50 (box jump — doubling the stake with NEW capital; stop stays ₹18.09; charges ₹1.19)
2021-02-08  GDL         PYRAMID BUY ₹1,130.51 at ₹159.00 (box jump — doubling the stake with NEW capital; stop stays ₹141.52; charges ₹1.34)
2021-02-08  MAHLOG      PYRAMID BUY ₹1,156.26 at ₹505.00 (box jump — doubling the stake with NEW capital; stop stays ₹408.33; charges ₹1.37)
2021-02-08  TATAMOTORS  PYRAMID BUY ₹1,218.08 at ₹318.75 (box jump — doubling the stake with NEW capital; stop stays ₹239.88; charges ₹1.44)
2021-02-15  APTECHT     PYRAMID BUY ₹2,956.52 at ₹237.70 (box jump — doubling the stake with NEW capital; stop stays ₹197.36; charges ₹3.50)
2021-02-15  PAISALO     PYRAMID BUY ₹2,726.88 at ₹79.54 (box jump — doubling the stake with NEW capital; stop stays ₹72.41; charges ₹3.23)
2021-02-15  TATAMOTORS  PYRAMID BUY ₹2,519.88 at ₹329.90 (box jump — doubling the stake with NEW capital; stop stays ₹296.97; charges ₹2.99)
2021-03-08  APTECHT     PYRAMID BUY ₹5,519.21 at ₹222.00 (box jump — doubling the stake with NEW capital; stop stays ₹204.25; charges ₹6.54)
2021-03-08  POLYMED     PYRAMID BUY ₹368.87 at ₹718.90 (box jump — doubling the stake with NEW capital; stop stays ₹642.77; charges ₹0.44)
2021-03-15  DCW         PYRAMID BUY ₹2,930.21 at ₹29.90 (box jump — doubling the stake with NEW capital; stop stays ₹25.79; charges ₹3.47)
2021-03-18  DCW         SELL ₹5,046.62 at stop ₹25.79 (-0.1%, charges ₹5.23) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹10,139.32 at stop ₹204.25 (-7.0%, charges ₹10.52) — the cash goes back to work at the next Friday screen
2021-03-19  TATAMOTORS  SELL ₹4,529.31 at stop ₹296.97 (-6.9%, charges ₹4.70) — the cash goes back to work at the next Friday screen
2021-03-22  CENTENKA    BUY ₹3,141.53 at ₹264.00 (fresh Friday signal — BUY: 2.04× weekly, month 1.55×, ladder rising; stop ₹229.90; charges ₹3.72)
2021-03-22  DEEPAKFERT  BUY ₹3,421.27 at ₹237.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.87×, ladder rising; stop ₹184.78; charges ₹4.05)
2021-03-22  KEI         BUY ₹3,403.10 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹4.03)
2021-03-22  PRAKASH     BUY ₹3,421.68 at ₹67.15 (fresh Friday signal — BUY: 2.45× weekly, month 4.02×, ladder rising; stop ₹51.52; charges ₹4.05)
2021-03-22  VIDHIING    BUY ₹3,385.70 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹4.01)
2021-03-22  WELSPUNIND  BUY ₹3,420.41 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.42×, ladder rising; stop ₹67.45; charges ₹4.05)
2021-03-25  CENTENKA    SELL ₹2,729.68 at stop ₹229.90 (-12.9%, charges ₹2.83) — the cash goes back to work at the next Friday screen
2021-03-30  CENTRUM     BUY ₹2,729.68 at ₹28.40 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹3.23)
2021-03-30  DEEPAKFERT  PYRAMID BUY ₹3,217.52 at ₹223.15 (box jump — doubling the stake with NEW capital; stop stays ₹209.52; charges ₹3.81)
2021-03-30  GDL         PYRAMID BUY ₹2,624.22 at ₹184.65 (box jump — doubling the stake with NEW capital; stop stays ₹157.22; charges ₹3.11)
2021-03-30  KEI         PYRAMID BUY ₹3,387.34 at ₹520.20 (box jump — doubling the stake with NEW capital; stop stays ₹471.20; charges ₹4.01)
2021-03-30  MAHLOG      PYRAMID BUY ₹2,553.70 at ₹558.00 (box jump — doubling the stake with NEW capital; stop stays ₹473.82; charges ₹3.03)
2021-03-30  WELSPUNIND  PYRAMID BUY ₹3,523.31 at ₹84.00 (box jump — doubling the stake with NEW capital; stop stays ₹68.17; charges ₹4.17)
2021-04-01  TAX         FY2021 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹1,983.92 / LT ₹0.00)
2021-04-05  VIDHIING    PYRAMID BUY ₹3,544.95 at ₹204.10 (box jump — doubling the stake with NEW capital; stop stays ₹168.12; charges ₹4.20)
2021-04-12  CENTRUM     SELL ₹2,387.00 at stop ₹24.89 (-12.4%, charges ₹2.48) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹4,956.80 at stop ₹72.41 (-1.5%, charges ₹5.14) — the cash goes back to work at the next Friday screen
2021-04-19  MOREPENLAB  BUY ₹5,418.19 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹6.42)
2021-04-19  PRAKASH     PYRAMID BUY ₹3,969.84 at ₹78.00 (box jump — doubling the stake with NEW capital; stop stays ₹74.58; charges ₹4.70)
2021-04-19  PRAKASH     SELL ₹7,579.19 at stop ₹74.58 (+2.8%, charges ₹7.86) — the cash goes back to work at the next Friday screen
2021-04-26  ORIENTREF   BUY ₹3,814.60 at ₹314.95 (fresh Friday signal — BUY: 1.81× weekly, month 5.16×, ladder rising; stop ₹247.04; charges ₹4.52)
2021-04-26  SUPPETRO    BUY ₹5,690.21 at ₹670.90 (fresh Friday signal — BUY: 6.51× weekly, month 2.36×, ladder rising; stop ₹453.05; charges ₹6.74)
2021-05-10  KEI         PYRAMID BUY ₹6,878.70 at ₹528.50 (box jump — doubling the stake with NEW capital; stop stays ₹485.02; charges ₹8.15)
2021-05-10  ORIENTREF   PYRAMID BUY ₹3,810.68 at ₹315.00 (box jump — doubling the stake with NEW capital; stop stays ₹283.10; charges ₹4.51)
2021-05-10  SUPPETRO    PYRAMID BUY ₹6,041.38 at ₹713.15 (box jump — doubling the stake with NEW capital; stop stays ₹653.60; charges ₹7.16)
2021-05-17  GDL         PYRAMID BUY ₹7,044.92 at ₹248.00 (box jump — doubling the stake with NEW capital; stop stays ₹230.90; charges ₹8.35)
2021-05-24  DEEPAKFERT  PYRAMID BUY ₹8,646.06 at ₹300.00 (box jump — doubling the stake with NEW capital; stop stays ₹264.10; charges ₹10.24)
2021-05-24  VIDHIING    PYRAMID BUY ₹7,082.23 at ₹204.00 (box jump — doubling the stake with NEW capital; stop stays ₹182.64; charges ₹8.39)
2021-05-31  KEI         PYRAMID BUY ₹16,233.75 at ₹624.00 (box jump — doubling the stake with NEW capital; stop stays ₹558.60; charges ₹19.23)
2021-05-31  MAHLOG      PYRAMID BUY ₹4,891.24 at ₹534.70 (box jump — doubling the stake with NEW capital; stop stays ₹494.95; charges ₹5.80)
2021-06-07  DEEPAKFERT  PYRAMID BUY ₹17,109.06 at ₹297.00 (box jump — doubling the stake with NEW capital; stop stays ₹269.80; charges ₹20.27)
2021-06-07  MOREPENLAB  PYRAMID BUY ₹8,663.17 at ₹59.95 (box jump — doubling the stake with NEW capital; stop stays ₹49.83; charges ₹10.26)
2021-06-07  ORIENTREF   PYRAMID BUY ₹7,665.22 at ₹317.00 (box jump — doubling the stake with NEW capital; stop stays ₹287.19; charges ₹9.08)
2021-06-07  SUPPETRO    PYRAMID BUY ₹13,118.66 at ₹774.75 (box jump — doubling the stake with NEW capital; stop stays ₹703.10; charges ₹15.54)
2021-06-07  WELSPUNIND  PYRAMID BUY ₹7,788.61 at ₹92.90 (box jump — doubling the stake with NEW capital; stop stays ₹80.48; charges ₹9.23)
2021-06-14  POLYMED     SELL ₹973.30 at stop ₹950.00 (+60.1%, charges ₹1.01) — the cash goes back to work at the next Friday screen
2021-06-18  VIDHIING    SELL ₹12,660.71 at stop ₹182.64 (-9.4%, charges ₹13.13) — the cash goes back to work at the next Friday screen
2021-06-21  MOREPENLAB  PYRAMID BUY ₹17,648.25 at ₹61.10 (box jump — doubling the stake with NEW capital; stop stays ₹56.33; charges ₹20.91)
2021-06-21  SOMANYCERA  BUY ₹13,634.01 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹16.15)
2021-07-12  ORIENTREF   PYRAMID BUY ₹16,106.75 at ₹333.25 (box jump — doubling the stake with NEW capital; stop stays ₹301.44; charges ₹19.08)
2021-07-19  WELSPUNIND  PYRAMID BUY ₹20,938.87 at ₹124.95 (box jump — doubling the stake with NEW capital; stop stays ₹97.56; charges ₹24.81)
2021-08-10  MOREPENLAB  SELL ₹32,487.97 at stop ₹56.33 (+2.6%, charges ₹33.70) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNIND  SELL ₹41,705.82 at stop ₹124.64 (+17.2%, charges ₹43.26) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹26,996.89 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹31.99)
2021-08-16  INDOCO      BUY ₹20,224.14 at ₹484.30 (fresh Friday signal — BUY: 4.80× weekly, month 2.73×, ladder rising; stop ₹412.30; charges ₹23.96)
2021-08-16  TATAINVEST  BUY ₹26,972.77 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹31.96)
2021-08-23  TATAINVEST  PYRAMID BUY ₹25,436.26 at ₹1,235.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,139.00; charges ₹30.14)
2021-08-30  BASF        PYRAMID BUY ₹25,426.38 at ₹3,469.75 (box jump — doubling the stake with NEW capital; stop stays ₹3,220.50; charges ₹30.13)
2021-09-13  SUPPETRO    SELL ₹23,772.10 at stop ₹703.10 (-4.1%, charges ₹24.66) — the cash goes back to work at the next Friday screen
2021-09-13  TATAINVEST  PYRAMID BUY ₹52,976.94 at ₹1,286.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,183.22; charges ₹62.77)
2021-09-20  GDL         SELL ₹15,087.88 at stop ₹266.00 (+26.8%, charges ₹15.65) — the cash goes back to work at the next Friday screen
2021-09-20  HATSUN      BUY ₹23,772.10 at ₹1,390.00 (fresh Friday signal — BUY: 6.62× weekly, month 6.95×, ladder rising; stop ₹994.17; charges ₹28.17)
2021-09-27  HATSUN      PYRAMID BUY ₹24,324.72 at ₹1,424.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,255.19; charges ₹28.82)
2021-09-27  TATAINVEST  PYRAMID BUY ₹1.08 lakh at ₹1,309.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,187.74; charges ₹127.62)
2021-10-04  SOMANYCERA  PYRAMID BUY ₹18,360.13 at ₹802.00 (box jump — doubling the stake with NEW capital; stop stays ₹560.50; charges ₹21.75)
2021-10-22  KEI         SELL ₹44,315.59 at stop ₹853.10 (+48.5%, charges ₹45.97) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        PYRAMID BUY ₹49,002.71 at ₹3,345.50 (box jump — doubling the stake with NEW capital; stop stays ₹3,220.59; charges ₹58.06)
2021-10-25  BASF        SELL ₹94,192.61 at stop ₹3,220.59 (-6.9%, charges ₹97.71) — the cash goes back to work at the next Friday screen
2021-10-25  SHOPERSTOP  BUY ₹59,403.47 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹70.38)
2021-11-01  TCIEXP      BUY ₹34,173.46 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹40.49)
2021-11-01  TTKPRESTIG  BUY ₹60,019.15 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹71.11)
2021-11-08  SHOPERSTOP  PYRAMID BUY ₹66,176.42 at ₹363.60 (box jump — doubling the stake with NEW capital; stop stays ₹319.53; charges ₹78.41)
2021-11-08  SOMANYCERA  PYRAMID BUY ₹38,391.57 at ₹839.00 (box jump — doubling the stake with NEW capital; stop stays ₹685.75; charges ₹45.49)
2021-11-08  TCIEXP      PYRAMID BUY ₹37,450.75 at ₹2,009.25 (box jump — doubling the stake with NEW capital; stop stays ₹1,651.24; charges ₹44.37)
2021-11-08  TTKPRESTIG  PYRAMID BUY ₹62,179.80 at ₹11,451.00 (box jump — doubling the stake with NEW capital; stop stays ₹10,070.05; charges ₹73.67)
2021-11-12  INDOCO      SELL ₹17,179.23 at stop ₹412.30 (-14.9%, charges ₹17.82) — the cash goes back to work at the next Friday screen
2021-11-15  SHOPERSTOP  PYRAMID BUY ₹1.39 lakh at ₹381.35 (box jump — doubling the stake with NEW capital; stop stays ₹335.82; charges ₹164.37)
2021-11-15  TCIEXP      PYRAMID BUY ₹74,505.05 at ₹1,999.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,807.09; charges ₹88.28)
2021-11-18  DEEPAKFERT  SELL ₹42,392.45 at stop ₹368.55 (+31.2%, charges ₹43.97) — the cash goes back to work at the next Friday screen
2021-11-22  HATSUN      SELL ₹42,812.41 at stop ₹1,255.19 (-10.8%, charges ₹44.41) — the cash goes back to work at the next Friday screen
2021-11-22  SHOPERSTOP  SELL ₹2.44 lakh at stop ₹335.82 (-7.5%, charges ₹253.04) — the cash goes back to work at the next Friday screen
2021-11-22  SOMANYCERA  PYRAMID BUY ₹78,932.78 at ₹863.00 (box jump — doubling the stake with NEW capital; stop stays ₹755.11; charges ₹93.52)
2021-11-22  SUPRAJIT    BUY ₹59,571.68 at ₹454.00 (fresh Friday signal — BUY: 10.19× weekly, month 1.96×, ladder rising; stop ₹309.33; charges ₹70.58)
2021-11-26  TATAINVEST  SELL ₹2.36 lakh at stop ₹1,436.49 (+11.0%, charges ₹244.83) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹1.09 lakh at stop ₹10,070.05 (-10.5%, charges ₹113.26) — the cash goes back to work at the next Friday screen
2021-11-29  BCG         BUY ₹1.11 lakh at ₹134.10 (fresh Friday signal — BUY: 1.94× weekly, month 1.58×, ladder rising; stop ₹55.00; charges ₹131.75)
2021-11-29  BSOFT       BUY ₹1.11 lakh at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹131.52)
2021-11-29  ESCORTS     BUY ₹1.11 lakh at ₹1,875.00 (fresh Friday signal — BUY: 1.78× weekly, month 2.18×, ladder rising; stop ₹1,369.04; charges ₹131.43)
2021-11-29  RAYMOND     BUY ₹1.10 lakh at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹130.19)
2021-11-29  SOMANYCERA  SELL ₹1.38 lakh at stop ₹755.11 (-7.4%, charges ₹143.05) — the cash goes back to work at the next Friday screen
2021-11-29  SUPRAJIT    PYRAMID BUY ₹57,797.33 at ₹441.00 (box jump — doubling the stake with NEW capital; stop stays ₹391.40; charges ₹68.48)
2021-11-30  MAHLOG      SELL ₹11,955.67 at stop ₹654.55 (+23.0%, charges ₹12.40) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹1.36 lakh at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹161.04)
2021-12-06  BSOFT       PYRAMID BUY ₹1.16 lakh at ₹485.00 (box jump — doubling the stake with NEW capital; stop stays ₹424.65; charges ₹136.95)
2021-12-06  MIRZAINT    BUY ₹1.36 lakh at ₹107.00 (fresh Friday signal — BUY: 3.65× weekly, month 3.62×, ladder rising; stop ₹73.21; charges ₹160.67)
2021-12-06  TCIEXP      PYRAMID BUY ₹1.70 lakh at ₹2,277.25 (box jump — doubling the stake with NEW capital; stop stays ₹1,909.50; charges ₹200.93)
2021-12-13  ESCORTS     PYRAMID BUY ₹1.10 lakh at ₹1,869.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,739.73; charges ₹130.85)
2021-12-13  RAYMOND     PYRAMID BUY ₹1.22 lakh at ₹661.00 (box jump — doubling the stake with NEW capital; stop stays ₹560.88; charges ₹144.21)
2021-12-13  SUPRAJIT    SELL ₹1.02 lakh at stop ₹391.40 (-12.5%, charges ₹106.25) — the cash goes back to work at the next Friday screen
2021-12-20  MINDAIND    BUY ₹1.56 lakh at ₹1,026.00 (fresh Friday signal — BUY: 5.05× weekly, month 1.81×, ladder rising; stop ₹787.66; charges ₹185.19)
2021-12-21  TCIEXP      SELL ₹3.03 lakh at stop ₹2,039.74 (-3.7%, charges ₹314.61) — the cash goes back to work at the next Friday screen
2021-12-27  BSE         PYRAMID BUY ₹1.33 lakh at ₹1,850.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,634.39; charges ₹157.45)
2021-12-27  MINDAIND    PYRAMID BUY ₹1.80 lakh at ₹1,180.00 (box jump — doubling the stake with NEW capital; stop stays ₹929.20; charges ₹212.74)
2021-12-27  MIRZAINT    PYRAMID BUY ₹1.59 lakh at ₹125.40 (box jump — doubling the stake with NEW capital; stop stays ₹95.34; charges ₹188.07)
2021-12-27  STEELXIND   BUY ₹2.12 lakh at ₹16.40 (fresh Friday signal — BUY: 3.12× weekly, month 3.27×, ladder rising; stop ₹7.36; charges ₹250.61)
2022-01-03  MINDAIND    PYRAMID BUY ₹3.74 lakh at ₹1,229.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,088.41; charges ₹443.18)
2022-01-07  MINDAIND    SELL ₹6.61 lakh at stop ₹1,088.41 (-6.7%, charges ₹685.64) — the cash goes back to work at the next Friday screen
2022-01-10  COMPINFO    BUY ₹2.52 lakh at ₹45.00 (fresh Friday signal — BUY: 4.39× weekly, month 5.27×, ladder rising; stop ₹25.44; charges ₹298.89)
2022-01-10  SWANENERGY  BUY ₹2.57 lakh at ₹164.30 (fresh Friday signal — BUY: 6.30× weekly, month 2.85×, ladder rising; stop ₹120.48; charges ₹304.43)
2022-01-10  ZEELEARN    BUY ₹2.57 lakh at ₹17.80 (fresh Friday signal — BUY: 14.73× weekly, month 5.09×, ladder rising; stop ₹13.06; charges ₹304.46)
2022-01-17  MIRZAINT    PYRAMID BUY ₹3.85 lakh at ₹152.20 (box jump — doubling the stake with NEW capital; stop stays ₹143.07; charges ₹456.27)
2022-01-21  LTTS        SELL ₹4,611.94 at stop ₹4,856.88 (+118.7%, charges ₹4.78) — the cash goes back to work at the next Friday screen
2022-01-24  ESCORTS     PYRAMID BUY ₹2.21 lakh at ₹1,869.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,754.65; charges ₹261.65)
2022-01-24  MIRZAINT    SELL ₹7.23 lakh at stop ₹143.07 (+6.6%, charges ₹749.77) — the cash goes back to work at the next Friday screen
2022-01-24  SWANENERGY  PYRAMID BUY ₹2.73 lakh at ₹175.00 (box jump — doubling the stake with NEW capital; stop stays ₹162.64; charges ₹323.87)
2022-01-25  SWANENERGY  SELL ₹5.07 lakh at stop ₹162.64 (-4.1%, charges ₹526.18) — the cash goes back to work at the next Friday screen
2022-01-31  ANDHRSUGAR  BUY ₹3.29 lakh at ₹157.95 (fresh Friday signal — BUY: 1.89× weekly, month 1.58×, ladder rising; stop ₹119.37; charges ₹389.76)
2022-01-31  SHARDACROP  BUY ₹3.29 lakh at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹389.97)
2022-01-31  TV18BRDCST  BUY ₹3.29 lakh at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹389.67)
2022-02-07  ANDHRSUGAR  PYRAMID BUY ₹3.41 lakh at ₹163.90 (box jump — doubling the stake with NEW capital; stop stays ₹135.28; charges ₹403.96)
2022-02-07  COMPINFO    PYRAMID BUY ₹2.41 lakh at ₹43.00 (box jump — doubling the stake with NEW capital; stop stays ₹29.08; charges ₹285.27)
2022-02-07  RAYMOND     PYRAMID BUY ₹2.86 lakh at ₹778.00 (box jump — doubling the stake with NEW capital; stop stays ₹679.35; charges ₹339.28)
2022-02-07  SHARDACROP  PYRAMID BUY ₹3.70 lakh at ₹660.10 (box jump — doubling the stake with NEW capital; stop stays ₹545.30; charges ₹438.24)
2022-02-07  TV18BRDCST  PYRAMID BUY ₹3.63 lakh at ₹65.00 (box jump — doubling the stake with NEW capital; stop stays ₹53.30; charges ₹429.52)
2022-02-07  ZEELEARN    PYRAMID BUY ₹2.25 lakh at ₹15.60 (box jump — doubling the stake with NEW capital; stop stays ₹13.28; charges ₹266.52)
2022-02-11  SHARDACROP  SELL ₹6.10 lakh at stop ₹545.30 (-12.5%, charges ₹632.87) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹2.02 lakh at stop ₹424.65 (-10.6%, charges ₹209.62) — the cash goes back to work at the next Friday screen
2022-02-14  GNFC        BUY ₹4.79 lakh at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹567.30)
2022-02-14  OMAXE       BUY ₹3.79 lakh at ₹103.30 (fresh Friday signal — BUY: 7.36× weekly, month 4.44×, ladder rising; stop ₹84.88; charges ₹449.03)
2022-02-15  RAYMOND     SELL ₹4.99 lakh at stop ₹679.35 (-3.4%, charges ₹517.90) — the cash goes back to work at the next Friday screen
2022-02-21  ANDHRSUGAR  SELL ₹5.62 lakh at stop ₹135.28 (-15.9%, charges ₹582.87) — the cash goes back to work at the next Friday screen
2022-02-21  EVERESTIND  BUY ₹6.18 lakh at ₹740.00 (fresh Friday signal — BUY: 3.34× weekly, month 1.68×, ladder rising; stop ₹522.67; charges ₹731.75)
2022-02-21  GNFC        PYRAMID BUY ₹4.74 lakh at ₹548.00 (box jump — doubling the stake with NEW capital; stop stays ₹497.80; charges ₹561.50)
2022-02-21  OMAXE       PYRAMID BUY ₹3.38 lakh at ₹92.20 (box jump — doubling the stake with NEW capital; stop stays ₹89.39; charges ₹400.31)
2022-02-21  OMAXE       SELL ₹6.54 lakh at stop ₹89.39 (-8.6%, charges ₹678.47) — the cash goes back to work at the next Friday screen
2022-02-21  TV18BRDCST  PYRAMID BUY ₹7.30 lakh at ₹65.50 (box jump — doubling the stake with NEW capital; stop stays ₹58.38; charges ₹865.13)
2022-02-22  TV18BRDCST  SELL ₹12.99 lakh at stop ₹58.38 (-8.4%, charges ₹1,347.97) — the cash goes back to work at the next Friday screen
2022-02-22  ZEELEARN    SELL ₹3.82 lakh at stop ₹13.28 (-20.5%, charges ₹396.62) — the cash goes back to work at the next Friday screen
2022-02-24  COMPINFO    SELL ₹3.25 lakh at stop ₹29.08 (-33.9%, charges ₹337.25) — the cash goes back to work at the next Friday screen
2022-02-25  ESCORTS     SELL ₹4.14 lakh at stop ₹1,754.65 (-6.2%, charges ₹429.25) — the cash goes back to work at the next Friday screen
2022-03-07  CGCL        BUY ₹6.47 lakh at ₹600.00 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 3.19×, ladder rising; stop ₹536.75; charges ₹766.78)
2022-03-07  EVERESTIND  PYRAMID BUY ₹5.17 lakh at ₹620.00 (box jump — doubling the stake with NEW capital; stop stays ₹526.21; charges ₹612.36)
2022-03-07  EXCELINDUS  BUY ₹6.40 lakh at ₹1,523.00 (fresh Friday signal — BUY: 6.93× weekly, month 5.51×, ladder rising; stop ₹1,016.01; charges ₹758.62)
2022-03-07  GTLINFRA    BUY ₹6.45 lakh at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹764.57)
2022-03-07  MAWANASUG   BUY ₹6.45 lakh at ₹115.00 (fresh Friday signal — ACCUMULATE: 2.21× weekly, month 7.30×, ladder rising; stop ₹84.08; charges ₹763.96)
2022-03-07  SRHHYPOLTD  BUY ₹6.43 lakh at ₹408.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 3.20×, ladder rising; stop ₹312.70; charges ₹762.23)
2022-03-14  ICICIGOLD   BUY ₹5.00 lakh at ₹46.20 (fresh Friday signal — BUY: 4.11× weekly, month 3.73×, ladder rising; stop ₹41.50; charges ₹591.99)
2022-03-21  BSE         SELL ₹2.34 lakh at stop ₹1,634.39 (-12.6%, charges ₹243.17) — the cash goes back to work at the next Friday screen
2022-03-21  EXCELINDUS  PYRAMID BUY ₹7.07 lakh at ₹1,683.85 (box jump — doubling the stake with NEW capital; stop stays ₹1,438.30; charges ₹837.75)
2022-03-28  EVERESTIND  PYRAMID BUY ₹12.16 lakh at ₹730.00 (box jump — doubling the stake with NEW capital; stop stays ₹594.70; charges ₹1,441.16)
2022-03-29  EXCELINDUS  SELL ₹12.06 lakh at stop ₹1,438.30 (-10.3%, charges ₹1,250.93) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹9.32 lakh / LT ₹0.00)
2022-04-04  MAWANASUG   PYRAMID BUY ₹7.76 lakh at ₹138.55 (box jump — doubling the stake with NEW capital; stop stays ₹122.26; charges ₹919.31)
2022-04-04  RCF         BUY ₹10.60 lakh at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹1,256.41)
2022-04-04  SRHHYPOLTD  PYRAMID BUY ₹7.24 lakh at ₹460.00 (box jump — doubling the stake with NEW capital; stop stays ₹431.30; charges ₹858.36)
2022-04-11  STEELXIND   PYRAMID BUY ₹3.27 lakh at ₹25.40 (box jump — doubling the stake with NEW capital; stop stays ₹21.56; charges ₹387.69)
2022-04-20  STEELXIND   SELL ₹5.55 lakh at stop ₹21.56 (+3.2%, charges ₹575.27) — the cash goes back to work at the next Friday screen
2022-04-25  GNFC        PYRAMID BUY ₹14.63 lakh at ₹846.40 (box jump — doubling the stake with NEW capital; stop stays ₹792.16; charges ₹1,733.49)
2022-04-25  GTLINFRA    PYRAMID BUY ₹5.88 lakh at ₹1.55 (box jump — doubling the stake with NEW capital; stop stays ₹1.41; charges ₹696.28)
2022-04-25  MANALIPETC  BUY ₹9.35 lakh at ₹139.80 (fresh Friday signal — BUY: 10.53× weekly, month 1.74×, ladder rising; stop ₹99.75; charges ₹1,107.25)
2022-04-25  MAWANASUG   PYRAMID BUY ₹19.18 lakh at ₹171.35 (box jump — doubling the stake with NEW capital; stop stays ₹135.09; charges ₹2,272.54)
2022-04-25  RCF         PYRAMID BUY ₹11.45 lakh at ₹104.20 (box jump — doubling the stake with NEW capital; stop stays ₹93.15; charges ₹1,356.46)
2022-04-28  EVERESTIND  SELL ₹19.79 lakh at stop ₹594.70 (-15.6%, charges ₹2,052.40) — the cash goes back to work at the next Friday screen
2022-04-29  GTLINFRA    SELL ₹10.67 lakh at stop ₹1.41 (-13.2%, charges ₹1,107.25) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹15.15 lakh at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹1,794.49)
2022-05-02  RIIL        BUY ₹15.10 lakh at ₹1,100.00 (fresh Friday signal — BUY: 5.17× weekly, month 3.64×, ladder rising; stop ₹852.81; charges ₹1,788.86)
2022-05-04  RCF         SELL ₹20.44 lakh at stop ₹93.15 (-7.1%, charges ₹2,119.81) — the cash goes back to work at the next Friday screen
2022-05-05  SRHHYPOLTD  SELL ₹13.56 lakh at stop ₹431.30 (-0.6%, charges ₹1,406.91) — the cash goes back to work at the next Friday screen
2022-05-06  GNFC        SELL ₹27.34 lakh at stop ₹792.16 (+13.4%, charges ₹2,836.17) — the cash goes back to work at the next Friday screen
2022-05-09  GEPIL       BUY ₹15.27 lakh at ₹182.65 (fresh Friday signal — ACCUMULATE: 1.55× weekly, month 2.61×, ladder rising; stop ₹163.45; charges ₹1,809.54)
2022-05-09  JKIL        BUY ₹15.42 lakh at ₹229.70 (fresh Friday signal — BUY: 6.96× weekly, month 3.58×, ladder rising; stop ₹192.28; charges ₹1,827.33)
2022-05-09  MAWANASUG   SELL ₹30.19 lakh at stop ₹135.09 (-9.4%, charges ₹3,132.03) — the cash goes back to work at the next Friday screen
2022-05-09  MFL         PYRAMID BUY ₹13.84 lakh at ₹1,308.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,225.50; charges ₹1,639.45)
2022-05-09  MOL         BUY ₹15.44 lakh at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹1,829.26)
2022-05-09  MRPL        BUY ₹15.36 lakh at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹1,819.89)
2022-05-11  MANALIPETC  SELL ₹6.65 lakh at stop ₹99.75 (-28.6%, charges ₹690.14) — the cash goes back to work at the next Friday screen
2022-05-11  MFL         SELL ₹25.89 lakh at stop ₹1,225.50 (-10.5%, charges ₹2,685.21) — the cash goes back to work at the next Friday screen
2022-05-11  MOL         SELL ₹13.48 lakh at stop ₹113.62 (-12.5%, charges ₹1,398.75) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹14.70 lakh at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹1,741.34)
2022-05-23  ACC         BUY ₹19.55 lakh at ₹2,260.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹2,316.83)
2022-05-23  GRAUWEIL    BUY ₹19.69 lakh at ₹82.70 (fresh Friday signal — BUY: 5.06× weekly, month 7.54×, ladder rising; stop ₹56.42; charges ₹2,333.31)
2022-05-23  JKIL        PYRAMID BUY ₹15.42 lakh at ₹230.00 (box jump — doubling the stake with NEW capital; stop stays ₹196.02; charges ₹1,827.55)
2022-05-23  MRPL        PYRAMID BUY ₹18.65 lakh at ₹94.80 (box jump — doubling the stake with NEW capital; stop stays ₹60.81; charges ₹2,209.25)
2022-05-23  RIIL        PYRAMID BUY ₹14.26 lakh at ₹1,040.00 (box jump — doubling the stake with NEW capital; stop stays ₹863.73; charges ₹1,689.28)
2022-05-23  VADILALIND  BUY ₹19.51 lakh at ₹1,805.00 (fresh Friday signal — BUY: 1.51× weekly, month 1.94×, ladder rising; stop ₹1,567.50; charges ₹2,311.78)
2022-05-26  RIIL        SELL ₹23.64 lakh at stop ₹863.73 (-19.3%, charges ₹2,452.57) — the cash goes back to work at the next Friday screen
2022-05-31  GEPIL       SELL ₹13.64 lakh at stop ₹163.45 (-10.5%, charges ₹1,414.55) — the cash goes back to work at the next Friday screen
2022-06-06  BCG         SELL ₹45,507.35 at stop ₹55.00 (-59.0%, charges ₹47.20) — the cash goes back to work at the next Friday screen
2022-06-06  GRAUWEIL    PYRAMID BUY ₹16.73 lakh at ₹70.35 (box jump — doubling the stake with NEW capital; stop stays ₹61.82; charges ₹1,982.51)
2022-06-06  MRPL        PYRAMID BUY ₹34.73 lakh at ₹88.35 (box jump — doubling the stake with NEW capital; stop stays ₹69.61; charges ₹4,115.43)
2022-06-06  SHANTIGEAR  BUY ₹23.98 lakh at ₹238.05 (fresh Friday signal — BUY: 1.57× weekly, month 2.31×, ladder rising; stop ₹179.53; charges ₹2,841.03)
2022-06-06  VBL         SELL ₹13.08 lakh at stop ₹196.27 (-10.8%, charges ₹1,357.07) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹29.66 lakh at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹3,514.72)
2022-06-13  GRAUWEIL    SELL ₹29.36 lakh at stop ₹61.82 (-19.2%, charges ₹3,045.48) — the cash goes back to work at the next Friday screen
2022-06-13  JKIL        PYRAMID BUY ₹38.57 lakh at ₹287.70 (box jump — doubling the stake with NEW capital; stop stays ₹233.94; charges ₹4,569.33)
2022-06-20  APARINDS    BUY ₹28.58 lakh at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹3,386.16)
2022-06-20  ELECON      PYRAMID BUY ₹31.75 lakh at ₹131.25 (box jump — doubling the stake with NEW capital; stop stays ₹111.01; charges ₹3,762.08)
2022-06-27  VADILALIND  PYRAMID BUY ₹21.32 lakh at ₹1,975.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,602.19; charges ₹2,526.52)
2022-07-04  APARINDS    PYRAMID BUY ₹29.44 lakh at ₹980.00 (box jump — doubling the stake with NEW capital; stop stays ₹844.03; charges ₹3,488.40)
2022-07-06  MRPL        SELL ₹54.64 lakh at stop ₹69.61 (-20.3%, charges ₹5,668.32) — the cash goes back to work at the next Friday screen
2022-07-11  ELECON      PYRAMID BUY ₹71.08 lakh at ₹147.00 (box jump — doubling the stake with NEW capital; stop stays ₹120.65; charges ₹8,422.07)
2022-07-11  MARATHON    BUY ₹49.61 lakh at ₹215.00 (fresh Friday signal — BUY: 2.48× weekly, month 6.64×, ladder rising; stop ₹186.25; charges ₹5,878.13)
2022-07-11  VADILALIND  PYRAMID BUY ₹45.02 lakh at ₹2,086.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,877.25; charges ₹5,334.38)
2022-07-18  ACC         PYRAMID BUY ₹18.68 lakh at ₹2,160.95 (box jump — doubling the stake with NEW capital; stop stays ₹2,030.06; charges ₹2,212.66)
2022-07-25  ELECON      PYRAMID BUY ₹1.60 crore at ₹165.95 (box jump — doubling the stake with NEW capital; stop stays ₹142.64; charges ₹19,004.27)
2022-07-25  MARATHON    PYRAMID BUY ₹50.69 lakh at ₹219.95 (box jump — doubling the stake with NEW capital; stop stays ₹188.59; charges ₹6,006.34)
2022-07-25  VADILALIND  PYRAMID BUY ₹89.34 lakh at ₹2,071.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,924.70; charges ₹10,584.75)
2022-08-01  JKIL        PYRAMID BUY ₹90.70 lakh at ₹338.50 (box jump — doubling the stake with NEW capital; stop stays ₹308.80; charges ₹10,745.94)
2022-08-05  JKIL        SELL ₹1.65 crore at stop ₹308.80 (+3.4%, charges ₹17,137.11) — the cash goes back to work at the next Friday screen
2022-08-08  ACC         PYRAMID BUY ₹39.04 lakh at ₹2,260.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,053.90; charges ₹4,625.43)
2022-08-08  NAVNETEDUL  BUY ₹100.00 lakh at ₹130.50 (fresh Friday signal — BUY: 14.73× weekly, month 3.84×, ladder rising; stop ₹88.40; charges ₹11,848.00)
2022-08-08  WSTCSTPAPR  BUY ₹71.02 lakh at ₹498.00 (fresh Friday signal — ACCUMULATE: 3.90× weekly, month 2.21×, ladder rising; stop ₹443.70; charges ₹8,415.00)
2022-08-16  ACC         PYRAMID BUY ₹77.62 lakh at ₹2,248.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,085.11; charges ₹9,196.28)
2022-08-16  MARATHON    PYRAMID BUY ₹1.03 crore at ₹223.10 (box jump — doubling the stake with NEW capital; stop stays ₹192.48; charges ₹12,177.50)
2022-08-22  APARINDS    PYRAMID BUY ₹72.54 lakh at ₹1,208.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,095.35; charges ₹8,594.88)
2022-08-22  NAVNETEDUL  PYRAMID BUY ₹98.73 lakh at ₹129.00 (box jump — doubling the stake with NEW capital; stop stays ₹116.38; charges ₹11,697.94)
2022-08-22  WSTCSTPAPR  PYRAMID BUY ₹78.92 lakh at ₹554.05 (box jump — doubling the stake with NEW capital; stop stays ₹482.12; charges ₹9,351.02)
2022-08-29  ICICIGOLD   SELL ₹4.48 lakh at stop ₹41.50 (-10.2%, charges ₹464.52) — the cash goes back to work at the next Friday screen
2022-09-05  NAVNETEDUL  PYRAMID BUY ₹2.12 crore at ₹138.40 (box jump — doubling the stake with NEW capital; stop stays ₹125.88; charges ₹25,085.82)
2022-09-05  SHANTIGEAR  PYRAMID BUY ₹28.77 lakh at ₹286.00 (box jump — doubling the stake with NEW capital; stop stays ₹253.27; charges ₹3,409.24)
2022-09-12  APARINDS    PYRAMID BUY ₹1.47 crore at ₹1,228.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,108.54; charges ₹17,464.01)
2022-09-19  MARATHON    PYRAMID BUY ₹2.30 crore at ₹250.15 (box jump — doubling the stake with NEW capital; stop stays ₹232.80; charges ₹27,291.78)
2022-09-19  MARATHON    SELL ₹4.28 crore at stop ₹232.80 (-1.0%, charges ₹44,400.60) — the cash goes back to work at the next Friday screen
2022-09-19  SHANTIGEAR  PYRAMID BUY ₹62.74 lakh at ₹312.00 (box jump — doubling the stake with NEW capital; stop stays ₹289.75; charges ₹7,433.95)
2022-09-19  WSTCSTPAPR  PYRAMID BUY ₹1.61 crore at ₹565.00 (box jump — doubling the stake with NEW capital; stop stays ₹533.28; charges ₹19,060.37)
2022-09-22  WSTCSTPAPR  SELL ₹3.03 crore at stop ₹533.28 (-2.2%, charges ₹31,449.42) — the cash goes back to work at the next Friday screen
2022-09-26  CENTRALBK   BUY ₹2.65 crore at ₹20.45 (fresh Friday signal — BUY: 5.35× weekly, month 2.44×, ladder rising; stop ₹18.95; charges ₹31,453.10)
2022-09-26  HEIDELBERG  BUY ₹2.66 crore at ₹205.20 (fresh Friday signal — BUY: 9.09× weekly, month 6.26×, ladder rising; stop ₹180.55; charges ₹31,575.18)
2022-09-26  NAVNETEDUL  PYRAMID BUY ₹4.11 crore at ₹134.45 (box jump — doubling the stake with NEW capital; stop stays ₹127.30; charges ₹48,710.84)
2022-09-26  NAVNETEDUL  SELL ₹7.77 crore at stop ₹127.30 (-5.2%, charges ₹80,624.64) — the cash goes back to work at the next Friday screen
2022-09-26  SCHNEIDER   BUY ₹2.04 crore at ₹177.00 (fresh Friday signal — BUY: 5.21× weekly, month 3.37×, ladder rising; stop ₹137.51; charges ₹24,139.33)
2022-10-03  ALLCARGO    BUY ₹2.52 crore at ₹413.00 (fresh Friday signal — ACCUMULATE: 2.01× weekly, month 3.12×, ladder rising; stop ₹336.30; charges ₹29,887.62)
2022-10-03  CHEMCON     BUY ₹2.62 crore at ₹447.95 (fresh Friday signal — ACCUMULATE: 2.09× weekly, month 2.31×, ladder rising; stop ₹390.07; charges ₹31,079.07)
2022-10-03  WESTLIFE    BUY ₹2.63 crore at ₹728.00 (fresh Friday signal — ACCUMULATE: 2.19× weekly, month 1.94×, ladder rising; stop ₹633.65; charges ₹31,123.97)
2022-10-10  SCHNEIDER   PYRAMID BUY ₹2.18 crore at ₹189.20 (box jump — doubling the stake with NEW capital; stop stays ₹159.60; charges ₹25,772.60)
2022-10-10  SHANTIGEAR  PYRAMID BUY ₹1.38 crore at ₹342.15 (box jump — doubling the stake with NEW capital; stop stays ₹301.39; charges ₹16,294.98)
2022-10-17  CENTRALBK   SELL ₹2.45 crore at stop ₹18.95 (-7.3%, charges ₹25,460.47) — the cash goes back to work at the next Friday screen
2022-10-20  VADILALIND  SELL ₹1.98 crore at stop ₹2,295.06 (+13.1%, charges ₹20,505.43) — the cash goes back to work at the next Friday screen
2022-10-24  CHEMCON     PYRAMID BUY ₹2.50 crore at ₹428.00 (box jump — doubling the stake with NEW capital; stop stays ₹394.35; charges ₹29,659.75)
2022-10-24  JTLINFRA    BUY ₹3.29 crore at ₹292.00 (fresh Friday signal — ACCUMULATE: 5.50× weekly, month 7.34×, ladder rising; stop ₹217.12; charges ₹38,952.69)
2022-11-03  APARINDS    SELL ₹3.26 crore at stop ₹1,358.50 (+17.4%, charges ₹33,773.80) — the cash goes back to work at the next Friday screen
2022-11-04  CHEMCON     SELL ₹4.61 crore at stop ₹394.35 (-10.0%, charges ₹47,772.73) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹3.61 crore at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹42,759.33)
2022-11-07  RVNL        BUY ₹3.60 crore at ₹46.85 (fresh Friday signal — BUY: 4.42× weekly, month 4.42×, ladder rising; stop ₹33.77; charges ₹42,664.27)
2022-11-07  WESTLIFE    PYRAMID BUY ₹2.75 crore at ₹763.50 (box jump — doubling the stake with NEW capital; stop stays ₹671.22; charges ₹32,603.01)
2022-11-10  SCHNEIDER   SELL ₹3.66 crore at stop ₹159.60 (-12.8%, charges ₹38,005.33) — the cash goes back to work at the next Friday screen
2022-11-14  CGCL        PYRAMID BUY ₹7.93 lakh at ₹736.05 (box jump — doubling the stake with NEW capital; stop stays ₹699.20; charges ₹939.54)
2022-11-14  PIIND       BUY ₹4.10 crore at ₹3,443.90 (fresh Friday signal — BUY: 5.02× weekly, month 1.65×, ladder rising; stop ₹3,060.95; charges ₹48,540.75)
2022-11-14  RVNL        PYRAMID BUY ₹3.95 crore at ₹51.45 (box jump — doubling the stake with NEW capital; stop stays ₹37.29; charges ₹46,797.77)
2022-11-21  KTKBANK     PYRAMID BUY ₹3.57 crore at ₹138.50 (box jump — doubling the stake with NEW capital; stop stays ₹123.03; charges ₹42,251.07)
2022-11-21  RVNL        PYRAMID BUY ₹9.73 crore at ₹63.40 (box jump — doubling the stake with NEW capital; stop stays ₹46.27; charges ₹1.15 lakh)
2022-11-21  WESTLIFE    PYRAMID BUY ₹5.44 crore at ₹755.15 (box jump — doubling the stake with NEW capital; stop stays ₹708.51; charges ₹64,454.70)
2022-11-28  ALLCARGO    PYRAMID BUY ₹2.85 crore at ₹466.70 (box jump — doubling the stake with NEW capital; stop stays ₹432.77; charges ₹33,733.72)
2022-11-28  PIIND       PYRAMID BUY ₹4.04 crore at ₹3,400.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,123.65; charges ₹47,865.21)
2022-11-29  ALLCARGO    SELL ₹5.27 crore at stop ₹432.77 (-1.6%, charges ₹54,683.73) — the cash goes back to work at the next Friday screen
2022-12-05  HEIDELBERG  PYRAMID BUY ₹2.70 crore at ₹208.00 (box jump — doubling the stake with NEW capital; stop stays ₹184.82; charges ₹31,968.11)
2022-12-05  LIKHITHA    BUY ₹6.63 crore at ₹261.70 (fresh Friday signal — BUY: 16.49× weekly, month 7.66×, ladder rising; stop ₹179.07; charges ₹78,600.39)
2022-12-05  RVNL        PYRAMID BUY ₹23.28 crore at ₹75.90 (box jump — doubling the stake with NEW capital; stop stays ₹53.77; charges ₹2.76 lakh)
2022-12-19  HEIDELBERG  PYRAMID BUY ₹5.22 crore at ₹201.35 (box jump — doubling the stake with NEW capital; stop stays ₹190.00; charges ₹61,855.44)
2022-12-19  KTKBANK     PYRAMID BUY ₹7.90 crore at ₹153.45 (box jump — doubling the stake with NEW capital; stop stays ₹139.84; charges ₹93,568.03)
2022-12-19  LIKHITHA    PYRAMID BUY ₹5.94 crore at ₹234.75 (box jump — doubling the stake with NEW capital; stop stays ₹210.50; charges ₹70,422.55)
2022-12-21  ELECON      SELL ₹3.91 crore at stop ₹202.49 (+33.7%, charges ₹40,537.04) — the cash goes back to work at the next Friday screen
2022-12-21  HEIDELBERG  SELL ₹9.84 crore at stop ₹190.00 (-6.9%, charges ₹1.02 lakh) — the cash goes back to work at the next Friday screen
2022-12-21  LIKHITHA    SELL ₹10.64 crore at stop ₹210.50 (-15.2%, charges ₹1.10 lakh) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹2.77 crore at stop ₹345.56 (+9.9%, charges ₹28,769.71) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹1.70 crore at stop ₹2,465.16 (+10.0%, charges ₹17,629.33) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹14.37 crore at stop ₹139.84 (-4.4%, charges ₹1.49 lakh) — the cash goes back to work at the next Friday screen
2022-12-26  RVNL        SELL ₹37.09 crore at stop ₹60.57 (-8.3%, charges ₹3.85 lakh) — the cash goes back to work at the next Friday screen
2023-01-02  GICRE       BUY ₹10.30 crore at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 11.18×, ladder rising; stop ₹137.57; charges ₹1.22 lakh)
2023-01-02  GSFC        BUY ₹10.40 crore at ₹140.70 (fresh Friday signal — ACCUMULATE: 2.14× weekly, month 1.67×, ladder rising; stop ₹111.58; charges ₹1.23 lakh)
2023-01-02  HARIOMPIPE  BUY ₹10.31 crore at ₹363.95 (fresh Friday signal — ACCUMULATE: 5.91× weekly, month 2.06×, ladder rising; stop ₹264.86; charges ₹1.22 lakh)
2023-01-02  IOB         BUY ₹10.32 crore at ₹32.40 (fresh Friday signal — ACCUMULATE: 4.77× weekly, month 30.16×, ladder rising; stop ₹21.23; charges ₹1.22 lakh)
2023-01-02  JINDALSAW   BUY ₹7.96 crore at ₹51.98 (fresh Friday signal — ACCUMULATE: 1.95× weekly, month 2.35×, ladder rising; stop ₹42.55; charges ₹94,334.10)
2023-01-02  JSL         BUY ₹10.35 crore at ₹241.00 (fresh Friday signal — BUY: 2.29× weekly, month 2.13×, ladder rising; stop ₹192.61; charges ₹1.23 lakh)
2023-01-02  SPIC        BUY ₹10.29 crore at ₹88.25 (fresh Friday signal — BUY: 4.81× weekly, month 3.70×, ladder rising; stop ₹54.66; charges ₹1.22 lakh)
2023-01-02  YESBANK     BUY ₹10.41 crore at ₹20.85 (fresh Friday signal — ACCUMULATE: 2.12× weekly, month 4.61×, ladder rising; stop ₹15.00; charges ₹1.23 lakh)
2023-01-09  CGCL        PYRAMID BUY ₹16.26 lakh at ₹754.95 (box jump — doubling the stake with NEW capital; stop stays ₹704.95; charges ₹1,926.19)
2023-01-16  GICRE       PYRAMID BUY ₹10.74 crore at ₹187.05 (box jump — doubling the stake with NEW capital; stop stays ₹167.72; charges ₹1.27 lakh)
2023-01-16  JSL         PYRAMID BUY ₹10.24 crore at ₹238.90 (box jump — doubling the stake with NEW capital; stop stays ₹218.83; charges ₹1.21 lakh)
2023-01-16  WESTLIFE    SELL ₹10.19 crore at stop ₹708.51 (-5.6%, charges ₹1.06 lakh) — the cash goes back to work at the next Friday screen
2023-01-23  JINDALSAW   PYRAMID BUY ₹8.95 crore at ₹58.50 (box jump — doubling the stake with NEW capital; stop stays ₹51.77; charges ₹1.06 lakh)
2023-01-23  PIIND       SELL ₹7.41 crore at stop ₹3,123.65 (-8.7%, charges ₹76,873.73) — the cash goes back to work at the next Friday screen
2023-01-23  SPECIALITY  BUY ₹10.19 crore at ₹276.85 (fresh Friday signal — BUY: 6.67× weekly, month 2.61×, ladder rising; stop ₹221.73; charges ₹1.21 lakh)
2023-01-23  SPIC        PYRAMID BUY ₹9.14 crore at ₹78.50 (box jump — doubling the stake with NEW capital; stop stays ₹65.74; charges ₹1.08 lakh)
2023-01-30  LSIL        BUY ₹7.41 crore at ₹23.20 (fresh Friday signal — BUY: 2.28× weekly, month 3.56×, ladder rising; stop ₹11.29; charges ₹87,806.32)
2023-02-01  GICRE       SELL ₹19.22 crore at stop ₹167.72 (-8.4%, charges ₹1.99 lakh) — the cash goes back to work at the next Friday screen
2023-02-06  LSIL        PYRAMID BUY ₹6.97 crore at ₹21.85 (box jump — doubling the stake with NEW capital; stop stays ₹20.04; charges ₹82,598.92)
2023-02-06  MOLDTECH    BUY ₹14.24 crore at ₹189.00 (fresh Friday signal — BUY: 3.10× weekly, month 4.84×, ladder rising; stop ₹142.35; charges ₹1.69 lakh)
2023-02-07  LSIL        SELL ₹12.77 crore at stop ₹20.04 (-11.0%, charges ₹1.32 lakh) — the cash goes back to work at the next Friday screen
2023-02-13  AXITA       BUY ₹17.75 crore at ₹67.00 (fresh Friday signal — BUY: 1.99× weekly, month 1.70×, ladder rising; stop ₹53.77; charges ₹2.10 lakh)
2023-02-13  HARIOMPIPE  PYRAMID BUY ₹12.02 crore at ₹425.00 (box jump — doubling the stake with NEW capital; stop stays ₹370.12; charges ₹1.42 lakh)
2023-02-13  MOLDTECH    PYRAMID BUY ₹18.75 crore at ₹249.15 (box jump — doubling the stake with NEW capital; stop stays ₹188.72; charges ₹2.22 lakh)
2023-02-13  YESBANK     PYRAMID BUY ₹8.50 crore at ₹17.05 (box jump — doubling the stake with NEW capital; stop stays ₹15.34; charges ₹1.01 lakh)
2023-02-14  SPECIALITY  SELL ₹8.14 crore at stop ₹221.73 (-19.9%, charges ₹84,480.54) — the cash goes back to work at the next Friday screen
2023-02-17  CGCL        SELL ₹30.31 lakh at stop ₹704.95 (-0.9%, charges ₹3,144.22) — the cash goes back to work at the next Friday screen
2023-02-20  HARIOMPIPE  PYRAMID BUY ₹23.81 crore at ₹421.25 (box jump — doubling the stake with NEW capital; stop stays ₹386.32; charges ₹2.82 lakh)
2023-02-23  SPIC        SELL ₹15.29 crore at stop ₹65.74 (-21.2%, charges ₹1.59 lakh) — the cash goes back to work at the next Friday screen
2023-02-27  JSL         PYRAMID BUY ₹22.76 crore at ₹265.50 (box jump — doubling the stake with NEW capital; stop stays ₹235.03; charges ₹2.70 lakh)
2023-02-27  MOLDTECH    PYRAMID BUY ₹34.76 crore at ₹231.00 (box jump — doubling the stake with NEW capital; stop stays ₹196.50; charges ₹4.12 lakh)
2023-02-27  SONATSOFTW  BUY ₹23.74 crore at ₹360.00 (fresh Friday signal — BUY: 9.70× weekly, month 3.45×, ladder rising; stop ₹282.62; charges ₹2.81 lakh)
2023-02-28  AXITA       SELL ₹14.21 crore at stop ₹53.77 (-19.7%, charges ₹1.47 lakh) — the cash goes back to work at the next Friday screen
2023-03-06  IOB         PYRAMID BUY ₹8.30 crore at ₹26.10 (box jump — doubling the stake with NEW capital; stop stays ₹22.18; charges ₹98,365.58)
2023-03-06  JINDALSAW   PYRAMID BUY ₹22.62 crore at ₹73.97 (box jump — doubling the stake with NEW capital; stop stays ₹67.92; charges ₹2.68 lakh)
2023-03-06  SONATSOFTW  PYRAMID BUY ₹26.39 crore at ₹400.75 (box jump — doubling the stake with NEW capital; stop stays ₹325.85; charges ₹3.13 lakh)
2023-03-13  YESBANK     SELL ₹15.27 crore at stop ₹15.34 (-19.1%, charges ₹1.58 lakh) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹29.48 crore at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.57×, ladder rising; stop ₹691.46; charges ₹3.49 lakh)
2023-03-20  HARIOMPIPE  PYRAMID BUY ₹51.98 crore at ₹460.00 (box jump — doubling the stake with NEW capital; stop stays ₹399.00; charges ₹6.16 lakh)
2023-03-20  IOB         SELL ₹14.09 crore at stop ₹22.18 (-24.2%, charges ₹1.46 lakh) — the cash goes back to work at the next Friday screen
2023-03-20  SONATSOFTW  PYRAMID BUY ₹52.32 crore at ₹397.50 (box jump — doubling the stake with NEW capital; stop stays ₹357.20; charges ₹6.20 lakh)
2023-03-27  JINDALSAW   SELL ₹41.48 crore at stop ₹67.92 (+5.1%, charges ₹4.30 lakh) — the cash goes back to work at the next Friday screen
2023-03-27  SONATSOFTW  PYRAMID BUY ₹108.85 crore at ₹413.70 (box jump — doubling the stake with NEW capital; stop stays ₹371.45; charges ₹12.90 lakh)
2023-03-29  SONATSOFTW  SELL ₹195.14 crore at stop ₹371.45 (-7.4%, charges ₹20.24 lakh) — the cash goes back to work at the next Friday screen
2023-04-03  CPSEETF     BUY ₹52.44 crore at ₹40.00 (fresh Friday signal — ACCUMULATE: 1.80× weekly, month 1.84×, ladder rising; stop ₹36.42; charges ₹6.21 lakh)
2023-04-03  HAL         BUY ₹52.44 crore at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹6.21 lakh)
2023-04-03  TAX         FY2023 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹43.01 crore / LT ₹0.00)
2023-04-10  JSL         PYRAMID BUY ₹49.34 crore at ₹288.00 (box jump — doubling the stake with NEW capital; stop stays ₹256.98; charges ₹5.85 lakh)
2023-04-10  KSB         BUY ₹58.73 crore at ₹451.00 (fresh Friday signal — BUY: 2.21× weekly, month 2.22×, ladder rising; stop ₹372.21; charges ₹6.96 lakh)
2023-04-10  SETFGOLD    BUY ₹58.71 crore at ₹52.60 (fresh Friday signal — BUY: 2.69× weekly, month 2.06×, ladder rising; stop ₹48.56; charges ₹6.96 lakh)
2023-04-13  JSL         SELL ₹87.91 crore at stop ₹256.98 (-4.9%, charges ₹9.12 lakh) — the cash goes back to work at the next Friday screen
2023-04-17  SAKSOFT     BUY ₹50.67 crore at ₹159.00 (fresh Friday signal — BUY: 1.60× weekly, month 1.54×, ladder rising; stop ₹131.96; charges ₹6.00 lakh)
2023-04-17  SETFGOLD    PYRAMID BUY ₹59.09 crore at ₹53.00 (box jump — doubling the stake with NEW capital; stop stays ₹49.74; charges ₹7.00 lakh)
2023-04-17  TIIL        BUY ₹65.62 crore at ₹1,495.35 (fresh Friday signal — BUY: 3.27× weekly, month 2.15×, ladder rising; stop ₹1,036.90; charges ₹7.77 lakh)
2023-04-24  MOLDTECH    PYRAMID BUY ₹86.21 crore at ₹286.65 (box jump — doubling the stake with NEW capital; stop stays ₹249.42; charges ₹10.21 lakh)
2023-04-24  SAKSOFT     PYRAMID BUY ₹59.30 crore at ₹186.30 (box jump — doubling the stake with NEW capital; stop stays ₹145.68; charges ₹7.03 lakh)
2023-05-02  ANURAS      PYRAMID BUY ₹44.37 crore at ₹1,139.00 (box jump — doubling the stake with NEW capital; stop stays ₹946.20; charges ₹5.26 lakh)
2023-05-02  CPSEETF     PYRAMID BUY ₹54.25 crore at ₹41.43 (box jump — doubling the stake with NEW capital; stop stays ₹38.64; charges ₹6.43 lakh)
2023-05-02  GSFC        PYRAMID BUY ₹11.87 crore at ₹160.80 (box jump — doubling the stake with NEW capital; stop stays ₹116.04; charges ₹1.41 lakh)
2023-05-02  KSB         PYRAMID BUY ₹58.97 crore at ₹453.40 (box jump — doubling the stake with NEW capital; stop stays ₹407.74; charges ₹6.99 lakh)
2023-05-02  TIIL        PYRAMID BUY ₹67.54 crore at ₹1,540.95 (box jump — doubling the stake with NEW capital; stop stays ₹1,373.70; charges ₹8.00 lakh)
2023-05-15  ANURAS      PYRAMID BUY ₹91.08 crore at ₹1,169.80 (box jump — doubling the stake with NEW capital; stop stays ₹1,007.67; charges ₹10.79 lakh)
2023-05-15  HAL         PYRAMID BUY ₹56.68 crore at ₹1,493.47 (box jump — doubling the stake with NEW capital; stop stays ₹1,370.80; charges ₹6.72 lakh)
2023-05-15  SAKSOFT     PYRAMID BUY ₹122.48 crore at ₹192.50 (box jump — doubling the stake with NEW capital; stop stays ₹154.78; charges ₹14.51 lakh)
2023-05-22  GSFC        PYRAMID BUY ₹24.79 crore at ₹168.05 (box jump — doubling the stake with NEW capital; stop stays ₹155.85; charges ₹2.94 lakh)
2023-05-29  GSFC        SELL ₹45.91 crore at stop ₹155.85 (-2.2%, charges ₹4.76 lakh) — the cash goes back to work at the next Friday screen
2023-06-05  CPSEETF     PYRAMID BUY ₹110.55 crore at ₹42.24 (box jump — doubling the stake with NEW capital; stop stays ₹39.05; charges ₹13.10 lakh)
2023-06-05  HAL         PYRAMID BUY ₹120.76 crore at ₹1,591.88 (box jump — doubling the stake with NEW capital; stop stays ₹1,415.36; charges ₹14.31 lakh)
2023-06-19  HAL         PYRAMID BUY ₹295.60 crore at ₹1,949.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,723.32; charges ₹35.02 lakh)
2023-06-19  SAKSOFT     PYRAMID BUY ₹384.59 crore at ₹302.40 (box jump — doubling the stake with NEW capital; stop stays ₹243.25; charges ₹45.57 lakh)
2023-07-03  ANURAS      SELL ₹156.66 crore at stop ₹1,007.67 (-4.8%, charges ₹16.25 lakh) — the cash goes back to work at the next Friday screen
2023-07-03  MOLDTECH    SELL ₹175.85 crore at stop ₹292.84 (+14.5%, charges ₹18.24 lakh) — the cash goes back to work at the next Friday screen
2023-07-10  CPSEETF     PYRAMID BUY ₹240.65 crore at ₹46.00 (box jump — doubling the stake with NEW capital; stop stays ₹40.77; charges ₹28.51 lakh)
2023-07-10  GENUSPOWER  BUY ₹271.41 crore at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹32.16 lakh)
2023-07-10  HARIOMPIPE  SELL ₹136.11 crore at stop ₹603.25 (+39.0%, charges ₹14.12 lakh) — the cash goes back to work at the next Friday screen
2023-07-12  KSB         SELL ₹105.90 crore at stop ₹407.74 (-9.8%, charges ₹10.98 lakh) — the cash goes back to work at the next Friday screen
2023-07-17  GENUSPOWER  PYRAMID BUY ₹298.72 crore at ₹179.45 (box jump — doubling the stake with NEW capital; stop stays ₹142.36; charges ₹35.39 lakh)
2023-07-17  ZENTEC      BUY ₹308.83 crore at ₹595.40 (fresh Friday signal — BUY: 8.06× weekly, month 3.59×, ladder rising; stop ₹364.54; charges ₹36.59 lakh)
2023-07-24  ZENTEC      PYRAMID BUY ₹318.10 crore at ₹614.00 (box jump — doubling the stake with NEW capital; stop stays ₹544.87; charges ₹37.69 lakh)
2023-07-31  CPSEETF     SELL ₹438.41 crore at stop ₹41.97 (-4.0%, charges ₹45.48 lakh) — the cash goes back to work at the next Friday screen
2023-07-31  GENUSPOWER  PYRAMID BUY ₹588.28 crore at ₹176.80 (box jump — doubling the stake with NEW capital; stop stays ₹163.02; charges ₹69.70 lakh)
2023-08-07  DBL         BUY ₹401.01 crore at ₹318.10 (fresh Friday signal — BUY: 6.63× weekly, month 4.65×, ladder rising; stop ₹225.25; charges ₹47.51 lakh)
2023-08-14  DBL         PYRAMID BUY ₹377.43 crore at ₹299.75 (box jump — doubling the stake with NEW capital; stop stays ₹271.17; charges ₹44.72 lakh)
2023-08-28  GENUSPOWER  PYRAMID BUY ₹1,608.15 crore at ₹241.80 (box jump — doubling the stake with NEW capital; stop stays ₹199.74; charges ₹1.91 crore)
2023-09-04  TIIL        PYRAMID BUY ₹181.45 crore at ₹2,071.30 (box jump — doubling the stake with NEW capital; stop stays ₹1,862.00; charges ₹21.50 lakh)
2023-10-03  SETFGOLD    SELL ₹110.73 crore at stop ₹49.74 (-5.8%, charges ₹11.49 lakh) — the cash goes back to work at the next Friday screen
2023-10-03  TIIL        PYRAMID BUY ₹354.59 crore at ₹2,025.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,878.24; charges ₹42.01 lakh)
2023-10-25  HAL         SELL ₹557.30 crore at stop ₹1,840.70 (+6.3%, charges ₹57.81 lakh) — the cash goes back to work at the next Friday screen
2023-10-30  SHAREINDIA  BUY ₹740.68 crore at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹87.76 lakh)
2023-11-16  GENUSPOWER  SELL ₹3,107.89 crore at stop ₹234.03 (+12.6%, charges ₹3.22 crore) — the cash goes back to work at the next Friday screen
2023-11-20  BIRLAMONEY  BUY ₹637.29 crore at ₹116.15 (fresh Friday signal — BUY: 2.25× weekly, month 4.02×, ladder rising; stop ₹101.46; charges ₹75.51 lakh)
2023-11-20  GEPIL       BUY ₹824.87 crore at ₹218.00 (fresh Friday signal — BUY: 4.38× weekly, month 2.06×, ladder rising; stop ₹158.46; charges ₹97.73 lakh)
2023-11-20  HIMATSEIDE  BUY ₹822.29 crore at ₹172.95 (fresh Friday signal — BUY: 2.60× weekly, month 2.69×, ladder rising; stop ₹134.86; charges ₹97.43 lakh)
2023-11-20  SHAREINDIA  PYRAMID BUY ₹877.90 crore at ₹356.00 (box jump — doubling the stake with NEW capital; stop stays ₹280.63; charges ₹1.04 crore)
2023-11-20  SOLARINDS   BUY ₹828.38 crore at ₹7,500.00 (fresh Friday signal — BUY: 3.85× weekly, month 2.17×, ladder rising; stop ₹4,746.06; charges ₹98.15 lakh)
2023-11-28  BIRLAMONEY  PYRAMID BUY ₹611.05 crore at ₹111.50 (box jump — doubling the stake with NEW capital; stop stays ₹103.60; charges ₹72.40 lakh)
2023-11-28  SHAREINDIA  PYRAMID BUY ₹1,688.76 crore at ₹342.61 (box jump — doubling the stake with NEW capital; stop stays ₹321.67; charges ₹2.00 crore)
2023-11-28  ZENTEC      PYRAMID BUY ₹802.08 crore at ₹774.55 (box jump — doubling the stake with NEW capital; stop stays ₹682.08; charges ₹95.03 lakh)
2023-11-30  BIRLAMONEY  SELL ₹1,133.67 crore at stop ₹103.60 (-9.0%, charges ₹1.18 crore) — the cash goes back to work at the next Friday screen
2023-12-04  HIMATSEIDE  PYRAMID BUY ₹788.31 crore at ₹166.00 (box jump — doubling the stake with NEW capital; stop stays ₹156.75; charges ₹93.40 lakh)
2023-12-04  TATAMTRDVR  BUY ₹1,133.67 crore at ₹485.45 (fresh Friday signal — BUY: 7.29× weekly, month 2.48×, ladder rising; stop ₹432.39; charges ₹1.34 crore)
2023-12-11  DBL         PYRAMID BUY ₹1,002.46 crore at ₹398.30 (box jump — doubling the stake with NEW capital; stop stays ₹370.74; charges ₹1.19 crore)
2023-12-11  SOLARINDS   PYRAMID BUY ₹700.45 crore at ₹6,349.25 (box jump — doubling the stake with NEW capital; stop stays ₹5,332.29; charges ₹82.99 lakh)
2023-12-11  TATAMTRDVR  PYRAMID BUY ₹1,122.65 crore at ₹481.30 (box jump — doubling the stake with NEW capital; stop stays ₹450.92; charges ₹1.33 crore)
2023-12-18  GEPIL       PYRAMID BUY ₹891.92 crore at ₹236.00 (box jump — doubling the stake with NEW capital; stop stays ₹206.25; charges ₹1.06 crore)
2023-12-18  SHAREINDIA  PYRAMID BUY ₹3,621.73 crore at ₹367.60 (box jump — doubling the stake with NEW capital; stop stays ₹328.89; charges ₹4.29 crore)
2023-12-20  DBL         SELL ₹1,863.14 crore at stop ₹370.74 (+4.9%, charges ₹1.93 crore) — the cash goes back to work at the next Friday screen
2023-12-26  BALMLAWRIE  BUY ₹1,863.14 crore at ₹238.25 (fresh Friday signal — BUY: 6.98× weekly, month 5.17×, ladder rising; stop ₹158.70; charges ₹2.21 crore)
2024-01-08  BALMLAWRIE  PYRAMID BUY ₹1,746.90 crore at ₹223.65 (box jump — doubling the stake with NEW capital; stop stays ₹204.77; charges ₹2.07 crore)
2024-01-15  TATAMTRDVR  PYRAMID BUY ₹2,557.74 crore at ₹548.60 (box jump — doubling the stake with NEW capital; stop stays ₹489.30; charges ₹3.03 crore)
2024-01-17  TIIL        SELL ₹817.10 crore at stop ₹2,337.00 (+22.4%, charges ₹84.76 lakh) — the cash goes back to work at the next Friday screen
2024-01-18  HIMATSEIDE  SELL ₹1,486.34 crore at stop ₹156.75 (-7.5%, charges ₹1.54 crore) — the cash goes back to work at the next Friday screen
2024-01-23  BALMLAWRIE  PYRAMID BUY ₹4,348.85 crore at ₹278.55 (box jump — doubling the stake with NEW capital; stop stays ₹231.75; charges ₹5.15 crore)
2024-01-23  RVNL        BUY ₹2,303.44 crore at ₹332.00 (fresh Friday signal — BUY: 6.89× weekly, month 1.60×, ladder rising; stop ₹157.32; charges ₹2.73 crore)
2024-02-05  BALMLAWRIE  PYRAMID BUY ₹8,948.44 crore at ₹286.75 (box jump — doubling the stake with NEW capital; stop stays ₹240.49; charges ₹10.60 crore)
2024-02-05  GEPIL       PYRAMID BUY ₹2,145.38 crore at ₹284.00 (box jump — doubling the stake with NEW capital; stop stays ₹220.03; charges ₹2.54 crore)
2024-02-05  RVNL        PYRAMID BUY ₹2,043.96 crore at ₹294.95 (box jump — doubling the stake with NEW capital; stop stays ₹241.04; charges ₹2.42 crore)
2024-02-05  TATAMTRDVR  PYRAMID BUY ₹5,865.43 crore at ₹629.40 (box jump — doubling the stake with NEW capital; stop stays ₹492.53; charges ₹6.95 crore)
2024-02-12  BALMLAWRIE  SELL ₹14,985.23 crore at stop ₹240.49 (-11.2%, charges ₹15.54 crore) — the cash goes back to work at the next Friday screen
2024-02-12  RVNL        SELL ₹3,335.31 crore at stop ₹241.04 (-23.1%, charges ₹3.46 crore) — the cash goes back to work at the next Friday screen
2024-02-12  SAKSOFT     SELL ₹774.58 crore at stop ₹305.02 (+25.8%, charges ₹80.35 lakh) — the cash goes back to work at the next Friday screen
2024-02-19  AEGISCHEM   BUY ₹4,722.32 crore at ₹436.55 (fresh Friday signal — BUY: 4.51× weekly, month 2.11×, ladder rising; stop ₹343.05; charges ₹5.60 crore)
2024-02-19  KCP         BUY ₹4,814.98 crore at ₹216.95 (fresh Friday signal — BUY: 3.57× weekly, month 4.05×, ladder rising; stop ₹167.91; charges ₹5.70 crore)
2024-02-19  KIOCL       BUY ₹4,755.96 crore at ₹491.55 (fresh Friday signal — BUY: 4.30× weekly, month 2.57×, ladder rising; stop ₹318.79; charges ₹5.63 crore)
2024-02-19  RAIN        BUY ₹4,801.86 crore at ₹203.50 (fresh Friday signal — BUY: 3.51× weekly, month 5.93×, ladder rising; stop ₹154.40; charges ₹5.69 crore)
2024-02-19  ZENTEC      PYRAMID BUY ₹1,677.41 crore at ₹810.40 (box jump — doubling the stake with NEW capital; stop stays ₹738.15; charges ₹1.99 crore)
2024-03-04  AEGISCHEM   PYRAMID BUY ₹4,758.33 crore at ₹440.40 (box jump — doubling the stake with NEW capital; stop stays ₹394.30; charges ₹5.64 crore)
2024-03-04  GEPIL       PYRAMID BUY ₹4,659.67 crore at ₹308.60 (box jump — doubling the stake with NEW capital; stop stays ₹273.88; charges ₹5.52 crore)
2024-03-06  GEPIL       SELL ₹8,257.37 crore at stop ₹273.88 (-2.9%, charges ₹8.57 crore) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹7,027.07 crore at stop ₹357.20 (+1.6%, charges ₹7.29 crore) — the cash goes back to work at the next Friday screen
2024-03-11  BHEL        BUY ₹5,368.24 crore at ₹259.10 (fresh Friday signal — BUY: 3.01× weekly, month 1.67×, ladder rising; stop ₹188.78; charges ₹6.36 crore)
2024-03-11  BOSCHLTD    BUY ₹4,492.54 crore at ₹29,819.95 (fresh Friday signal — BUY: 1.81× weekly, month 2.03×, ladder rising; stop ₹26,525.90; charges ₹5.32 crore)
2024-03-11  SMSPHARMA   BUY ₹5,423.66 crore at ₹179.00 (fresh Friday signal — BUY: 8.20× weekly, month 12.63×, ladder rising; stop ₹132.95; charges ₹6.43 crore)
2024-03-12  KCP         SELL ₹3,718.31 crore at stop ₹167.91 (-22.6%, charges ₹3.86 crore) — the cash goes back to work at the next Friday screen
2024-03-13  AEGISCHEM   SELL ₹8,506.60 crore at stop ₹394.30 (-10.1%, charges ₹8.82 crore) — the cash goes back to work at the next Friday screen
2024-03-13  RAIN        SELL ₹3,635.19 crore at stop ₹154.40 (-24.1%, charges ₹3.77 crore) — the cash goes back to work at the next Friday screen
2024-03-18  EMUDHRA     BUY ₹4,306.81 crore at ₹583.90 (fresh Friday signal — BUY: 1.54× weekly, month 3.10×, ladder rising; stop ₹529.77; charges ₹5.10 crore)
2024-03-18  FORCEMOT    BUY ₹5,780.73 crore at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹6.85 crore)
2024-03-18  INDIGO      BUY ₹5,772.55 crore at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹6.84 crore)
2024-03-18  SMSPHARMA   PYRAMID BUY ₹5,725.93 crore at ₹189.20 (box jump — doubling the stake with NEW capital; stop stays ₹146.81; charges ₹6.78 crore)
2024-03-26  BOSCHLTD    PYRAMID BUY ₹4,551.18 crore at ₹30,245.00 (box jump — doubling the stake with NEW capital; stop stays ₹26,710.20; charges ₹5.39 crore)
2024-03-26  KIOCL       PYRAMID BUY ₹3,962.23 crore at ₹410.00 (box jump — doubling the stake with NEW capital; stop stays ₹321.93; charges ₹4.69 crore)
2024-04-01  SOLARINDS   PYRAMID BUY ₹1,973.56 crore at ₹8,950.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,980.95; charges ₹2.34 crore)
2024-04-01  TAX         FY2024 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹5,710.60 crore / LT ₹0.00)
2024-04-08  BOSCHLTD    PYRAMID BUY ₹9,318.03 crore at ₹30,980.00 (box jump — doubling the stake with NEW capital; stop stays ₹28,244.40; charges ₹11.04 crore)
2024-04-15  EMUDHRA     PYRAMID BUY ₹5,149.68 crore at ₹699.00 (box jump — doubling the stake with NEW capital; stop stays ₹627.45; charges ₹6.10 crore)
2024-04-15  INDIGO      PYRAMID BUY ₹6,613.09 crore at ₹3,670.30 (box jump — doubling the stake with NEW capital; stop stays ₹3,287.00; charges ₹7.84 crore)
2024-04-22  SMSPHARMA   PYRAMID BUY ₹12,597.45 crore at ₹208.25 (box jump — doubling the stake with NEW capital; stop stays ₹181.36; charges ₹14.93 crore)
2024-04-29  FORCEMOT    PYRAMID BUY ₹8,879.25 crore at ₹10,100.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,483.47; charges ₹10.52 crore)
2024-05-09  ZENTEC      SELL ₹3,706.82 crore at stop ₹896.89 (+19.6%, charges ₹3.85 crore) — the cash goes back to work at the next Friday screen
2024-05-13  INDIGO      PYRAMID BUY ₹14,427.71 crore at ₹4,006.10 (box jump — doubling the stake with NEW capital; stop stays ₹3,719.77; charges ₹17.09 crore)
2024-05-21  BHEL        PYRAMID BUY ₹6,454.54 crore at ₹311.90 (box jump — doubling the stake with NEW capital; stop stays ₹251.68; charges ₹7.65 crore)
2024-05-21  FORCEMOT    PYRAMID BUY ₹15,793.06 crore at ₹8,987.50 (box jump — doubling the stake with NEW capital; stop stays ₹8,083.64; charges ₹18.71 crore)
2024-05-27  BOSCHLTD    PYRAMID BUY ₹18,577.52 crore at ₹30,901.00 (box jump — doubling the stake with NEW capital; stop stays ₹29,015.09; charges ₹22.01 crore)
2024-05-28  FORCEMOT    SELL ₹28,363.30 crore at stop ₹8,083.64 (-6.7%, charges ₹29.42 crore) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹17,140.13 crore at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹20.31 crore)
2024-06-03  THERMAX     BUY ₹14,930.00 crore at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹17.69 crore)
2024-06-04  BHEL        SELL ₹10,399.70 crore at stop ₹251.68 (-11.8%, charges ₹10.79 crore) — the cash goes back to work at the next Friday screen
2024-06-04  BOSCHLTD    SELL ₹34,830.65 crore at stop ₹29,015.09 (-5.5%, charges ₹36.13 crore) — the cash goes back to work at the next Friday screen
2024-06-04  SMSPHARMA   SELL ₹21,905.91 crore at stop ₹181.36 (-7.5%, charges ₹22.72 crore) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹3,514.01 crore at stop ₹7,980.95 (+0.6%, charges ₹3.65 crore) — the cash goes back to work at the next Friday screen
2024-06-04  TATAMTRDVR  SELL ₹11,013.04 crore at stop ₹591.85 (+3.4%, charges ₹11.42 crore) — the cash goes back to work at the next Friday screen
2024-06-10  BANKBEES    BUY ₹22,329.25 crore at ₹514.99 (fresh Friday signal — BUY: 4.22× weekly, month 1.96×, ladder rising; stop ₹457.43; charges ₹26.46 crore)
2024-06-10  CAMPUS      PYRAMID BUY ₹17,299.40 crore at ₹289.00 (box jump — doubling the stake with NEW capital; stop stays ₹248.05; charges ₹20.50 crore)
2024-06-10  DABUR       BUY ₹14,650.13 crore at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹17.36 crore)
2024-06-10  INDIGO      PYRAMID BUY ₹31,659.47 crore at ₹4,398.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,805.04; charges ₹37.51 crore)
2024-06-10  KIOCL       PYRAMID BUY ₹8,306.09 crore at ₹430.00 (box jump — doubling the stake with NEW capital; stop stays ₹330.30; charges ₹9.84 crore)
2024-06-10  NIFTYBEES   BUY ₹22,299.84 crore at ₹259.45 (fresh Friday signal — BUY: 4.16× weekly, month 2.61×, ladder rising; stop ₹229.24; charges ₹26.42 crore)
2024-06-10  UNOMINDA    BUY ₹22,384.10 crore at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹26.52 crore)
2024-06-18  DABUR       PYRAMID BUY ₹14,727.23 crore at ₹608.10 (box jump — doubling the stake with NEW capital; stop stays ₹552.95; charges ₹17.45 crore)
2024-06-18  NIFTYBEES   PYRAMID BUY ₹22,379.01 crore at ₹260.68 (box jump — doubling the stake with NEW capital; stop stays ₹230.02; charges ₹26.52 crore)
2024-06-18  THERMAX     PYRAMID BUY ₹14,323.75 crore at ₹5,417.40 (box jump — doubling the stake with NEW capital; stop stays ₹4,719.70; charges ₹16.97 crore)
2024-06-18  UNOMINDA    PYRAMID BUY ₹24,353.63 crore at ₹1,056.60 (box jump — doubling the stake with NEW capital; stop stays ₹895.00; charges ₹28.85 crore)
2024-07-01  EMUDHRA     PYRAMID BUY ₹12,996.15 crore at ₹882.55 (box jump — doubling the stake with NEW capital; stop stays ₹793.11; charges ₹15.40 crore)
2024-07-08  BANKBEES    PYRAMID BUY ₹23,341.73 crore at ₹538.98 (box jump — doubling the stake with NEW capital; stop stays ₹507.06; charges ₹27.66 crore)
2024-07-08  UNOMINDA    PYRAMID BUY ₹54,105.55 crore at ₹1,174.40 (box jump — doubling the stake with NEW capital; stop stays ₹981.87; charges ₹64.11 crore)
2024-07-15  NIFTYBEES   PYRAMID BUY ₹46,588.17 crore at ₹271.50 (box jump — doubling the stake with NEW capital; stop stays ₹255.69; charges ₹55.20 crore)
2024-07-19  UNOMINDA    SELL ₹90,323.78 crore at stop ₹981.87 (-10.2%, charges ₹93.69 crore) — the cash goes back to work at the next Friday screen
2024-07-22  GEOJITFSL   BUY ₹42,716.80 crore at ₹111.55 (fresh Friday signal — BUY: 3.55× weekly, month 1.64×, ladder rising; stop ₹90.61; charges ₹50.61 crore)
2024-07-22  SUNTECK     BUY ₹42,708.30 crore at ₹590.05 (fresh Friday signal — BUY: 3.28× weekly, month 1.60×, ladder rising; stop ₹487.06; charges ₹50.60 crore)
2024-07-29  GEOJITFSL   PYRAMID BUY ₹45,381.83 crore at ₹118.65 (box jump — doubling the stake with NEW capital; stop stays ₹95.03; charges ₹53.77 crore)
2024-07-29  SUNTECK     PYRAMID BUY ₹43,073.39 crore at ₹595.80 (box jump — doubling the stake with NEW capital; stop stays ₹531.30; charges ₹51.03 crore)
2024-08-05  DABUR       PYRAMID BUY ₹29,771.02 crore at ₹615.00 (box jump — doubling the stake with NEW capital; stop stays ₹587.15; charges ₹35.27 crore)
2024-08-05  THERMAX     SELL ₹24,917.39 crore at stop ₹4,719.70 (-14.6%, charges ₹25.85 crore) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹29,816.08 crore at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹35.33 crore)
2024-08-12  CAMPUS      PYRAMID BUY ₹34,919.29 crore at ₹291.85 (box jump — doubling the stake with NEW capital; stop stays ₹277.07; charges ₹41.37 crore)
2024-08-13  EMUDHRA     SELL ₹23,320.14 crore at stop ₹793.11 (+4.1%, charges ₹24.19 crore) — the cash goes back to work at the next Friday screen
2024-08-16  CAMPUS      SELL ₹66,193.85 crore at stop ₹277.07 (-4.4%, charges ₹68.66 crore) — the cash goes back to work at the next Friday screen
2024-08-19  EVEREADY    BUY ₹33,889.18 crore at ₹473.80 (fresh Friday signal — BUY: 2.51× weekly, month 3.62×, ladder rising; stop ₹372.97; charges ₹40.15 crore)
2024-08-19  VGUARD      BUY ₹55,624.81 crore at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹65.91 crore)
2024-08-26  BASF        PYRAMID BUY ₹27,009.32 crore at ₹6,666.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,894.80; charges ₹32.00 crore)
2024-08-26  EVEREADY    PYRAMID BUY ₹34,642.03 crore at ₹484.90 (box jump — doubling the stake with NEW capital; stop stays ₹423.27; charges ₹41.04 crore)
2024-09-16  DABUR       PYRAMID BUY ₹63,860.92 crore at ₹660.00 (box jump — doubling the stake with NEW capital; stop stays ₹602.49; charges ₹75.66 crore)
2024-09-16  NIFTYBEES   PYRAMID BUY ₹97,236.98 crore at ₹283.50 (box jump — doubling the stake with NEW capital; stop stays ₹262.66; charges ₹115.21 crore)
2024-09-30  GEOJITFSL   PYRAMID BUY ₹1.20 lakh crore at ₹157.39 (box jump — doubling the stake with NEW capital; stop stays ₹138.18; charges ₹142.57 crore)
2024-10-03  DABUR       SELL ₹1.16 lakh crore at stop ₹602.49 (-5.2%, charges ₹120.74 crore) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹44,498.48 crore at stop ₹420.24 (-19.8%, charges ₹46.16 crore) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹88,543.74 crore at ₹7,442.65 (fresh Friday signal — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹104.91 crore)
2024-10-07  EVEREADY    SELL ₹60,379.71 crore at stop ₹423.27 (-11.7%, charges ₹62.63 crore) — the cash goes back to work at the next Friday screen
2024-10-07  GEOJITFSL   SELL ₹2.11 lakh crore at stop ₹138.18 (+1.4%, charges ₹218.81 crore) — the cash goes back to work at the next Friday screen
2024-10-07  INDIGO      SELL ₹64,468.38 crore at stop ₹4,485.14 (+10.5%, charges ₹66.87 crore) — the cash goes back to work at the next Friday screen
2024-10-07  ITDCEM      BUY ₹72,357.55 crore at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹85.73 crore)
2024-10-14  BASF        PYRAMID BUY ₹66,612.68 crore at ₹8,225.00 (box jump — doubling the stake with NEW capital; stop stays ₹7,611.30; charges ₹78.92 crore)
2024-10-14  BSE         BUY ₹96,097.43 crore at ₹4,536.00 (fresh Friday signal — BUY: 2.79× weekly, month 4.25×, ladder rising; stop ₹3,393.93; charges ₹113.86 crore)
2024-10-14  PRECWIRE    BUY ₹96,664.78 crore at ₹213.35 (fresh Friday signal — BUY: 2.45× weekly, month 1.94×, ladder rising; stop ₹161.43; charges ₹114.53 crore)
2024-10-14  SKIPPER     BUY ₹95,607.12 crore at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹113.28 crore)
2024-10-21  KIOCL       PYRAMID BUY ₹14,169.91 crore at ₹367.00 (box jump — doubling the stake with NEW capital; stop stays ₹342.29; charges ₹16.79 crore)
2024-10-22  BASF        SELL ₹1.23 lakh crore at stop ₹7,611.30 (-0.1%, charges ₹127.68 crore) — the cash goes back to work at the next Friday screen
2024-10-22  KIOCL       SELL ₹26,388.67 crore at stop ₹342.29 (-15.2%, charges ₹27.37 crore) — the cash goes back to work at the next Friday screen
2024-10-25  SUNTECK     SELL ₹76,695.66 crore at stop ₹531.30 (-10.4%, charges ₹79.56 crore) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹91,132.64 crore at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹107.98 crore)
2024-11-04  AKZOINDIA   BUY ₹1.26 lakh crore at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹296.34 crore)
2024-11-04  BSE         PYRAMID BUY ₹94,036.82 crore at ₹4,444.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,694.81; charges ₹221.99 crore)
2024-11-04  ITDCEM      PYRAMID BUY ₹60,367.19 crore at ₹547.15 (box jump — doubling the stake with NEW capital; stop stays ₹430.14; charges ₹142.51 crore)
2024-11-04  PRECWIRE    PYRAMID BUY ₹89,146.63 crore at ₹196.99 (box jump — doubling the stake with NEW capital; stop stays ₹164.78; charges ₹210.44 crore)
2024-11-04  SKIPPER     PYRAMID BUY ₹94,310.96 crore at ₹546.15 (box jump — doubling the stake with NEW capital; stop stays ₹448.15; charges ₹222.63 crore)
2024-11-11  ASTRAZEN    PYRAMID BUY ₹87,337.90 crore at ₹7,350.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,854.77; charges ₹206.17 crore)
2024-11-14  ASTRAZEN    SELL ₹1.62 lakh crore at stop ₹6,854.77 (-7.3%, charges ₹360.61 crore) — the cash goes back to work at the next Friday screen
2024-11-14  NIFTYBEES   SELL ₹1.80 lakh crore at stop ₹262.66 (-4.4%, charges ₹399.08 crore) — the cash goes back to work at the next Friday screen
2024-11-18  JSWHL       BUY ₹1.29 lakh crore at ₹19,990.00 (fresh Friday signal — BUY: 3.46× weekly, month 4.62×, ladder rising; stop ₹8,434.53; charges ₹304.73 crore)
2024-11-25  GARFIBRES   BUY ₹1.40 lakh crore at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹329.50 crore)
2024-11-25  NSIL        BUY ₹1.30 lakh crore at ₹9,200.05 (fresh Friday signal — BUY: 2.68× weekly, month 7.14×, ladder rising; stop ₹5,674.36; charges ₹307.53 crore)
2024-11-25  PAYTM       PYRAMID BUY ₹1.11 lakh crore at ₹913.80 (box jump — doubling the stake with NEW capital; stop stays ₹712.50; charges ₹262.61 crore)
2024-12-02  GARFIBRES   PYRAMID BUY ₹1.36 lakh crore at ₹936.00 (box jump — doubling the stake with NEW capital; stop stays ₹829.35; charges ₹321.85 crore)
2024-12-09  AKZOINDIA   PYRAMID BUY ₹1.03 lakh crore at ₹3,718.70 (box jump — doubling the stake with NEW capital; stop stays ₹3,423.18; charges ₹243.33 crore)
2024-12-09  PAYTM       PYRAMID BUY ₹2.43 lakh crore at ₹997.45 (box jump — doubling the stake with NEW capital; stop stays ₹838.09; charges ₹572.62 crore)
2024-12-16  ITDCEM      PYRAMID BUY ₹1.13 lakh crore at ₹514.85 (box jump — doubling the stake with NEW capital; stop stays ₹477.71; charges ₹267.87 crore)
2024-12-16  NSIL        PYRAMID BUY ₹1.20 lakh crore at ₹8,475.00 (box jump — doubling the stake with NEW capital; stop stays ₹6,818.32; charges ₹282.63 crore)
2024-12-23  PAYTM       PYRAMID BUY ₹4.66 lakh crore at ₹959.80 (box jump — doubling the stake with NEW capital; stop stays ₹887.49; charges ₹1,100.72 crore)
2024-12-26  PRECWIRE    SELL ₹1.49 lakh crore at stop ₹164.78 (-19.7%, charges ₹330.14 crore) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹1.89 lakh crore at stop ₹3,423.18 (-16.9%, charges ₹420.09 crore) — the cash goes back to work at the next Friday screen
2024-12-30  KFINTECH    BUY ₹2.61 lakh crore at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹616.35 crore)
2025-01-06  BSE         PYRAMID BUY ₹2.26 lakh crore at ₹5,350.00 (box jump — doubling the stake with NEW capital; stop stays ₹4,954.63; charges ₹533.86 crore)
2025-01-06  SKIPPER     PYRAMID BUY ₹1.92 lakh crore at ₹557.10 (box jump — doubling the stake with NEW capital; stop stays ₹477.28; charges ₹453.66 crore)
2025-01-08  BANKBEES    SELL ₹43,795.43 crore at stop ₹507.06 (-3.8%, charges ₹97.28 crore) — the cash goes back to work at the next Friday screen
2025-01-09  GARFIBRES   SELL ₹2.41 lakh crore at stop ₹829.35 (-12.3%, charges ₹534.83 crore) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹8.65 lakh crore at stop ₹893.05 (-4.7%, charges ₹1,920.76 crore) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹3.28 lakh crore at stop ₹477.28 (-13.7%, charges ₹728.91 crore) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹2.73 lakh crore at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹643.63 crore)
2025-01-13  LLOYDSME    BUY ₹2.72 lakh crore at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹641.94 crore)
2025-01-13  NSIL        SELL ₹1.92 lakh crore at stop ₹6,818.32 (-22.9%, charges ₹426.44 crore) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹1.99 lakh crore at stop ₹1,159.14 (-23.3%, charges ₹442.72 crore) — the cash goes back to work at the next Friday screen
2025-01-20  AEGISLOG    PYRAMID BUY ₹2.62 lakh crore at ₹803.60 (box jump — doubling the stake with NEW capital; stop stays ₹700.36; charges ₹618.22 crore)
2025-01-20  APOLLO      BUY ₹3.02 lakh crore at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 3.48×, ladder rising; stop ₹110.19; charges ₹713.61 crore)
2025-01-20  BAJAJHCARE  BUY ₹3.07 lakh crore at ₹690.00 (fresh Friday signal — BUY: 1.75× weekly, month 4.12×, ladder rising; stop ₹451.06; charges ₹724.15 crore)
2025-01-24  AEGISLOG    SELL ₹4.55 lakh crore at stop ₹700.36 (-14.5%, charges ₹1,010.48 crore) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹2.80 lakh crore at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹660.70 crore)
2025-01-28  LLOYDSME    SELL ₹2.36 lakh crore at stop ₹1,258.75 (-12.7%, charges ₹524.87 crore) — the cash goes back to work at the next Friday screen
2025-02-03  BAJAJHCARE  PYRAMID BUY ₹3.02 lakh crore at ₹680.00 (box jump — doubling the stake with NEW capital; stop stays ₹455.35; charges ₹711.97 crore)
2025-02-03  ZENSARTECH  BUY ₹3.21 lakh crore at ₹947.00 (fresh Friday signal — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹757.47 crore)
2025-02-10  HDFCGOLD    BUY ₹3.19 lakh crore at ₹75.80 (fresh Friday signal — BUY: 2.22× weekly, month 1.58×, ladder rising; stop ₹64.93; charges ₹753.82 crore)
2025-02-17  APOLLO      SELL ₹2.52 lakh crore at stop ₹110.19 (-16.2%, charges ₹560.06 crore) — the cash goes back to work at the next Friday screen
2025-02-17  SETFGOLD    BUY ₹3.07 lakh crore at ₹76.80 (fresh Friday signal — BUY: 1.62× weekly, month 1.57×, ladder rising; stop ₹59.71; charges ₹724.20 crore)
2025-02-24  BAJAJHCARE  PYRAMID BUY ₹5.45 lakh crore at ₹614.55 (box jump — doubling the stake with NEW capital; stop stays ₹521.14; charges ₹1,285.37 crore)
2025-02-24  HDFCGOLD    PYRAMID BUY ₹3.14 lakh crore at ₹74.60 (box jump — doubling the stake with NEW capital; stop stays ₹70.20; charges ₹740.13 crore)
2025-02-24  SETFGOLD    PYRAMID BUY ₹2.99 lakh crore at ₹74.99 (box jump — doubling the stake with NEW capital; stop stays ₹69.36; charges ₹705.47 crore)
2025-02-24  TAJGVK      BUY ₹4.17 lakh crore at ₹440.40 (fresh Friday signal — BUY: 2.16× weekly, month 2.07×, ladder rising; stop ₹349.09; charges ₹984.17 crore)
2025-02-28  BSE         SELL ₹4.17 lakh crore at stop ₹4,954.63 (+0.7%, charges ₹927.22 crore) — the cash goes back to work at the next Friday screen
2025-03-03  JSWHL       PYRAMID BUY ₹1.07 lakh crore at ₹16,599.95 (box jump — doubling the stake with NEW capital; stop stays ₹13,741.44; charges ₹252.46 crore)
2025-03-03  NH          BUY ₹4.60 lakh crore at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹1,086.46 crore)
2025-03-03  TAJGVK      PYRAMID BUY ₹4.29 lakh crore at ₹454.45 (box jump — doubling the stake with NEW capital; stop stays ₹412.59; charges ₹1,013.17 crore)
2025-03-03  ZENSARTECH  SELL ₹2.45 lakh crore at stop ₹727.84 (-23.1%, charges ₹545.27 crore) — the cash goes back to work at the next Friday screen
2025-03-10  CREDITACC   PYRAMID BUY ₹3.18 lakh crore at ₹968.75 (box jump — doubling the stake with NEW capital; stop stays ₹837.38; charges ₹751.22 crore)
2025-03-10  GRMOVER     BUY ₹2.94 lakh crore at ₹252.00 (fresh Friday signal — BUY: 1.55× weekly, month 1.68×, ladder rising; stop ₹203.86; charges ₹694.43 crore)
2025-03-17  NH          PYRAMID BUY ₹4.82 lakh crore at ₹1,521.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,436.97; charges ₹1,136.97 crore)
2025-03-24  TAJGVK      PYRAMID BUY ₹9.72 lakh crore at ₹515.00 (box jump — doubling the stake with NEW capital; stop stays ₹453.34; charges ₹2,293.61 crore)
2025-04-01  TAX         FY2025 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹6.35 lakh crore / LT ₹0.00)
2025-04-02  TAJGVK      SELL ₹17.05 lakh crore at stop ₹453.34 (-5.8%, charges ₹3,786.50 crore) — the cash goes back to work at the next Friday screen
2025-04-07  BAJAJHCARE  SELL ₹9.20 lakh crore at stop ₹521.14 (-19.8%, charges ₹2,044.22 crore) — the cash goes back to work at the next Friday screen
2025-04-07  GRMOVER     PYRAMID BUY ₹2.98 lakh crore at ₹255.55 (box jump — doubling the stake with NEW capital; stop stays ₹248.00; charges ₹702.55 crore)
2025-04-07  HDFCGOLD    PYRAMID BUY ₹6.46 lakh crore at ₹77.00 (box jump — doubling the stake with NEW capital; stop stays ₹71.44; charges ₹1,526.09 crore)
2025-04-07  HDFCGOLD    SELL ₹11.96 lakh crore at stop ₹71.44 (-6.1%, charges ₹2,655.41 crore) — the cash goes back to work at the next Friday screen
2025-04-07  ITDCEM      PYRAMID BUY ₹2.42 lakh crore at ₹550.00 (box jump — doubling the stake with NEW capital; stop stays ₹524.92; charges ₹571.64 crore)
2025-04-07  JSWHL       PYRAMID BUY ₹3.18 lakh crore at ₹24,680.80 (box jump — doubling the stake with NEW capital; stop stays ₹19,106.01; charges ₹749.82 crore)
2025-04-07  NACLIND     BUY ₹8.13 lakh crore at ₹128.14 (fresh Friday signal — BUY: 3.19× weekly, month 13.92×, ladder rising; stop ₹89.22; charges ₹1,919.03 crore)
2025-04-07  SETFGOLD    SELL ₹5.51 lakh crore at stop ₹69.36 (-8.6%, charges ₹1,223.73 crore) — the cash goes back to work at the next Friday screen
2025-04-07  VADILALIND  BUY ₹8.09 lakh crore at ₹4,820.55 (fresh Friday signal — BUY: 9.88× weekly, month 5.69×, ladder rising; stop ₹4,255.30; charges ₹1,909.34 crore)
2025-04-11  ITDCEM      SELL ₹4.61 lakh crore at stop ₹524.92 (-5.3%, charges ₹1,023.18 crore) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹9.34 lakh crore at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹2,204.13 crore)
2025-04-15  INDIASHLTR  BUY ₹9.37 lakh crore at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹2,212.63 crore)
2025-04-15  VADILALIND  PYRAMID BUY ₹9.87 lakh crore at ₹5,898.90 (box jump — doubling the stake with NEW capital; stop stays ₹4,500.03; charges ₹2,330.94 crore)
2025-04-28  GRMOVER     PYRAMID BUY ₹7.21 lakh crore at ₹310.00 (box jump — doubling the stake with NEW capital; stop stays ₹290.80; charges ₹1,702.47 crore)
2025-04-28  WHIRLPOOL   BUY ₹10.66 lakh crore at ₹1,153.90 (fresh Friday signal — BUY: 2.21× weekly, month 1.77×, ladder rising; stop ₹1,017.54; charges ₹2,516.74 crore)
2025-05-07  GRMOVER     SELL ₹13.48 lakh crore at stop ₹290.80 (+3.2%, charges ₹2,995.12 crore) — the cash goes back to work at the next Friday screen
2025-05-12  CREDITACC   PYRAMID BUY ₹7.54 lakh crore at ₹1,148.60 (box jump — doubling the stake with NEW capital; stop stays ₹1,019.35; charges ₹1,779.28 crore)
2025-05-12  INDIASHLTR  PYRAMID BUY ₹10.03 lakh crore at ₹927.70 (box jump — doubling the stake with NEW capital; stop stays ₹804.65; charges ₹2,367.41 crore)
2025-05-12  KPRMILL     BUY ₹13.55 lakh crore at ₹1,302.00 (fresh Friday signal — BUY: 15.99× weekly, month 3.16×, ladder rising; stop ₹938.50; charges ₹3,198.40 crore)
2025-05-12  NH          PYRAMID BUY ₹11.57 lakh crore at ₹1,829.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,641.69; charges ₹2,731.17 crore)
2025-05-19  VADILALIND  PYRAMID BUY ₹22.75 lakh crore at ₹6,805.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,401.40; charges ₹5,371.62 crore)
2025-05-19  WHIRLPOOL   PYRAMID BUY ₹12.08 lakh crore at ₹1,311.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,111.50; charges ₹2,852.64 crore)
2025-05-26  KPRMILL     PYRAMID BUY ₹11.83 lakh crore at ₹1,139.95 (box jump — doubling the stake with NEW capital; stop stays ₹1,043.59; charges ₹2,793.71 crore)
2025-05-30  VADILALIND  SELL ₹36.00 lakh crore at stop ₹5,401.40 (-11.2%, charges ₹7,996.22 crore) — the cash goes back to work at the next Friday screen
2025-06-02  CREDITACC   PYRAMID BUY ₹14.94 lakh crore at ₹1,140.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,029.71; charges ₹3,527.74 crore)
2025-06-02  RPOWER      BUY ₹18.31 lakh crore at ₹58.64 (fresh Friday signal — BUY: 5.25× weekly, month 1.98×, ladder rising; stop ₹47.24; charges ₹4,321.31 crore)
2025-06-02  TECHNOE     BUY ₹18.28 lakh crore at ₹1,421.00 (fresh Friday signal — BUY: 6.29× weekly, month 1.64×, ladder rising; stop ₹1,150.36; charges ₹4,315.96 crore)
2025-06-23  WHIRLPOOL   PYRAMID BUY ₹24.51 lakh crore at ₹1,331.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,233.96; charges ₹5,785.48 crore)
2025-06-30  NH          PYRAMID BUY ₹28.12 lakh crore at ₹2,225.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,763.87; charges ₹6,637.17 crore)
2025-06-30  TECHNOE     PYRAMID BUY ₹20.78 lakh crore at ₹1,619.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,384.15; charges ₹4,905.73 crore)
2025-07-07  WHIRLPOOL   PYRAMID BUY ₹50.65 lakh crore at ₹1,377.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,301.97; charges ₹11,956.73 crore)
2025-07-14  TECHNOE     PYRAMID BUY ₹40.75 lakh crore at ₹1,589.10 (box jump — doubling the stake with NEW capital; stop stays ₹1,467.84; charges ₹9,618.90 crore)
2025-07-21  KPRMILL     PYRAMID BUY ₹24.67 lakh crore at ₹1,189.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,108.74; charges ₹5,824.39 crore)
2025-07-24  TECHNOE     SELL ₹75.02 lakh crore at stop ₹1,467.84 (-5.6%, charges ₹16,663.04 crore) — the cash goes back to work at the next Friday screen
2025-07-28  BOMDYEING   BUY ₹37.64 lakh crore at ₹181.45 (fresh Friday signal — BUY: 21.87× weekly, month 4.30×, ladder rising; stop ₹148.64; charges ₹8,885.33 crore)
2025-07-28  OLECTRA     BUY ₹37.44 lakh crore at ₹1,475.00 (fresh Friday signal — BUY: 7.37× weekly, month 1.99×, ladder rising; stop ₹1,185.79; charges ₹8,839.36 crore)
2025-08-01  KPRMILL     SELL ₹45.83 lakh crore at stop ₹1,108.74 (-8.0%, charges ₹10,179.91 crore) — the cash goes back to work at the next Friday screen
2025-08-04  INDIASHLTR  PYRAMID BUY ₹19.49 lakh crore at ₹902.50 (box jump — doubling the stake with NEW capital; stop stays ₹853.86; charges ₹4,600.76 crore)
2025-08-04  JSWHL       SELL ₹4.90 lakh crore at stop ₹19,106.01 (-11.1%, charges ₹1,088.60 crore) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹45.71 lakh crore at stop ₹1,814.78 (-6.5%, charges ₹10,152.62 crore) — the cash goes back to work at the next Friday screen
2025-08-04  PUNJABCHEM  BUY ₹38.12 lakh crore at ₹1,403.00 (fresh Friday signal — BUY: 43.22× weekly, month 11.54×, ladder rising; stop ₹1,208.88; charges ₹8,998.57 crore)
2025-08-07  WHIRLPOOL   SELL ₹95.46 lakh crore at stop ₹1,301.97 (-2.1%, charges ₹21,202.19 crore) — the cash goes back to work at the next Friday screen
2025-08-11  BLISSGVS    BUY ₹33.64 lakh crore at ₹178.60 (fresh Friday signal — BUY: 1.52× weekly, month 1.82×, ladder rising; stop ₹143.93; charges ₹7,942.01 crore)
2025-08-11  OLECTRA     PYRAMID BUY ₹35.23 lakh crore at ₹1,391.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,311.47; charges ₹8,316.29 crore)
2025-08-11  PRAKASH     BUY ₹40.83 lakh crore at ₹178.70 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 2.58×, ladder rising; stop ₹145.68; charges ₹9,637.34 crore)
2025-08-11  RAIN        BUY ₹40.89 lakh crore at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹9,652.90 crore)
2025-08-11  SIRCA       BUY ₹40.44 lakh crore at ₹458.80 (fresh Friday signal — BUY: 2.96× weekly, month 3.38×, ladder rising; stop ₹388.17; charges ₹9,545.27 crore)
2025-08-18  INDIASHLTR  PYRAMID BUY ₹40.16 lakh crore at ₹931.00 (box jump — doubling the stake with NEW capital; stop stays ₹862.60; charges ₹9,480.89 crore)
2025-08-18  PUNJABCHEM  SELL ₹32.69 lakh crore at stop ₹1,208.88 (-13.8%, charges ₹7,262.01 crore) — the cash goes back to work at the next Friday screen
2025-08-25  BOMDYEING   PYRAMID BUY ₹37.15 lakh crore at ₹179.50 (box jump — doubling the stake with NEW capital; stop stays ₹157.01; charges ₹8,769.09 crore)
2025-08-25  SPIC        BUY ₹32.69 lakh crore at ₹111.40 (fresh Friday signal — BUY: 8.68× weekly, month 5.72×, ladder rising; stop ₹77.81; charges ₹7,718.08 crore)
2025-08-26  RAIN        SELL ₹36.49 lakh crore at stop ₹143.64 (-10.4%, charges ₹8,103.88 crore) — the cash goes back to work at the next Friday screen
2025-09-01  SIRCA       PYRAMID BUY ₹40.84 lakh crore at ₹464.50 (box jump — doubling the stake with NEW capital; stop stays ₹424.18; charges ₹9,641.05 crore)
2025-09-08  BOMDYEING   PYRAMID BUY ₹73.46 lakh crore at ₹177.70 (box jump — doubling the stake with NEW capital; stop stays ₹160.12; charges ₹17,341.81 crore)
2025-09-08  NETWEB      BUY ₹36.49 lakh crore at ₹3,135.50 (fresh Friday signal — BUY: 6.14× weekly, month 4.02×, ladder rising; stop ₹2,081.16; charges ₹8,612.82 crore)
2025-09-08  OLECTRA     PYRAMID BUY ₹77.38 lakh crore at ₹1,529.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,416.64; charges ₹18,265.87 crore)
2025-09-08  SPIC        PYRAMID BUY ₹34.14 lakh crore at ₹116.60 (box jump — doubling the stake with NEW capital; stop stays ₹97.50; charges ₹8,059.28 crore)
2025-09-09  RPOWER      SELL ₹14.68 lakh crore at stop ₹47.24 (-19.4%, charges ₹3,260.54 crore) — the cash goes back to work at the next Friday screen
2025-09-22  BOMDYEING   PYRAMID BUY ₹1.52 crore crore at ₹184.00 (box jump — doubling the stake with NEW capital; stop stays ₹172.67; charges ₹35,870.87 crore)
2025-09-23  SPIC        SELL ₹56.90 lakh crore at stop ₹97.50 (-14.5%, charges ₹12,638.73 crore) — the cash goes back to work at the next Friday screen
2025-09-25  BOMDYEING   SELL ₹2.84 crore crore at stop ₹172.67 (-4.9%, charges ₹63,130.95 crore) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹74.17 lakh crore at stop ₹862.60 (-5.7%, charges ₹16,474.43 crore) — the cash goes back to work at the next Friday screen
2025-09-26  BLISSGVS    SELL ₹26.99 lakh crore at stop ₹143.93 (-19.4%, charges ₹5,994.57 crore) — the cash goes back to work at the next Friday screen
2025-09-29  GOLDIETF    BUY ₹87.85 lakh crore at ₹97.96 (fresh Friday signal — BUY: 2.84× weekly, month 2.11×, ladder rising; stop ₹89.02; charges ₹20,737.51 crore)
2025-09-29  HDFCSILVER  BUY ₹88.09 lakh crore at ₹137.30 (fresh Friday signal — BUY: 2.55× weekly, month 4.63×, ladder rising; stop ₹112.21; charges ₹20,795.86 crore)
2025-09-29  NETWEB      PYRAMID BUY ₹42.95 lakh crore at ₹3,700.00 (box jump — doubling the stake with NEW capital; stop stays ₹2,674.79; charges ₹10,139.44 crore)
2025-09-29  SETFGOLD    BUY ₹87.92 lakh crore at ₹99.53 (fresh Friday signal — BUY: 3.36× weekly, month 2.81×, ladder rising; stop ₹76.99; charges ₹20,753.85 crore)
2025-09-29  SILVERIETF  BUY ₹87.98 lakh crore at ₹142.00 (fresh Friday signal — BUY: 2.78× weekly, month 3.67×, ladder rising; stop ₹119.33; charges ₹20,768.52 crore)
2025-09-29  SUBROS      BUY ₹87.46 lakh crore at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹20,645.55 crore)
2025-10-06  GOLDIETF    PYRAMID BUY ₹91.52 lakh crore at ₹102.30 (box jump — doubling the stake with NEW capital; stop stays ₹91.66; charges ₹21,605.14 crore)
2025-10-06  SETFGOLD    PYRAMID BUY ₹90.41 lakh crore at ₹102.60 (box jump — doubling the stake with NEW capital; stop stays ₹90.43; charges ₹21,343.50 crore)
2025-10-06  SIRCA       PYRAMID BUY ₹86.75 lakh crore at ₹493.90 (box jump — doubling the stake with NEW capital; stop stays ₹446.36; charges ₹20,478.33 crore)
2025-10-06  SUBROS      PYRAMID BUY ₹82.87 lakh crore at ₹1,075.20 (box jump — doubling the stake with NEW capital; stop stays ₹1,046.90; charges ₹19,563.33 crore)
2025-10-13  AVANTIFEED  PYRAMID BUY ₹7.49 lakh crore at ₹657.45 (box jump — doubling the stake with NEW capital; stop stays ₹511.29; charges ₹1,767.34 crore)
2025-10-13  HDFCSILVER  PYRAMID BUY ₹1.03 crore crore at ₹161.11 (box jump — doubling the stake with NEW capital; stop stays ₹129.39; charges ₹24,344.59 crore)
2025-10-14  OLECTRA     SELL ₹1.43 crore crore at stop ₹1,416.64 (-4.4%, charges ₹31,730.74 crore) — the cash goes back to work at the next Friday screen
2025-10-14  SUBROS      SELL ₹1.61 crore crore at stop ₹1,046.90 (-5.1%, charges ₹35,724.00 crore) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹1.37 crore crore at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹32,260.03 crore)
2025-10-20  AVANTIFEED  PYRAMID BUY ₹15.64 lakh crore at ₹687.70 (box jump — doubling the stake with NEW capital; stop stays ₹600.07; charges ₹3,692.95 crore)
2025-10-20  CREDITACC   SELL ₹33.30 lakh crore at stop ₹1,274.42 (+17.5%, charges ₹7,396.15 crore) — the cash goes back to work at the next Friday screen
2025-10-20  TATSILV     BUY ₹1.37 crore crore at ₹16.34 (fresh Friday signal — BUY: 7.63× weekly, month 21.45×, ladder rising; stop ₹13.06; charges ₹32,306.89 crore)
2025-10-27  ANANDRATHI  PYRAMID BUY ₹1.36 crore crore at ₹1,566.95 (box jump — doubling the stake with NEW capital; stop stays ₹1,450.17; charges ₹32,029.55 crore)
2025-10-27  SKYGOLD     BUY ₹81.15 lakh crore at ₹370.00 (fresh Friday signal — BUY: 1.65× weekly, month 2.25×, ladder rising; stop ₹304.38; charges ₹19,156.97 crore)
2025-11-03  NETWEB      PYRAMID BUY ₹89.47 lakh crore at ₹3,858.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,515.95; charges ₹21,119.88 crore)
2025-11-03  PRAKASH     PYRAMID BUY ₹37.57 lakh crore at ₹164.85 (box jump — doubling the stake with NEW capital; stop stays ₹147.31; charges ₹8,869.42 crore)
2025-11-03  SETFGOLD    PYRAMID BUY ₹1.82 crore crore at ₹103.63 (box jump — doubling the stake with NEW capital; stop stays ₹93.58; charges ₹43,064.64 crore)
2025-11-03  SILVERIETF  PYRAMID BUY ₹92.38 lakh crore at ₹149.46 (box jump — doubling the stake with NEW capital; stop stays ₹123.06; charges ₹21,807.99 crore)
2025-11-06  NETWEB      SELL ₹1.63 crore crore at stop ₹3,515.95 (-3.3%, charges ₹36,097.18 crore) — the cash goes back to work at the next Friday screen
2025-11-10  CUB         BUY ₹1.63 crore crore at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹38,364.14 crore)
2025-11-10  SKYGOLD     PYRAMID BUY ₹78.12 lakh crore at ₹357.00 (box jump — doubling the stake with NEW capital; stop stays ₹329.13; charges ₹18,440.25 crore)
2025-11-14  PRAKASH     SELL ₹66.92 lakh crore at stop ₹147.31 (-14.2%, charges ₹14,864.15 crore) — the cash goes back to work at the next Friday screen
2025-11-17  CUB         PYRAMID BUY ₹1.73 crore crore at ₹272.00 (box jump — doubling the stake with NEW capital; stop stays ₹232.87; charges ₹40,953.63 crore)
2025-11-17  SIRCA       PYRAMID BUY ₹1.83 crore crore at ₹520.95 (box jump — doubling the stake with NEW capital; stop stays ₹475.57; charges ₹43,148.80 crore)
2025-11-20  ANANDRATHI  SELL ₹2.50 crore crore at stop ₹1,450.17 (-7.7%, charges ₹55,592.47 crore) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹2.29 crore crore at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹53,961.21 crore)
2025-11-25  SKYGOLD     SELL ₹1.44 crore crore at stop ₹329.13 (-9.5%, charges ₹31,883.60 crore) — the cash goes back to work at the next Friday screen
2025-12-01  CUB         PYRAMID BUY ₹3.47 crore crore at ₹272.40 (box jump — doubling the stake with NEW capital; stop stays ₹247.10; charges ₹81,930.89 crore)
2025-12-01  NACLIND     PYRAMID BUY ₹12.15 lakh crore at ₹191.99 (box jump — doubling the stake with NEW capital; stop stays ₹164.20; charges ₹2,868.47 crore)
2025-12-01  SANSERA     BUY ₹2.32 crore crore at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹54,806.13 crore)
2025-12-08  AVANTIFEED  PYRAMID BUY ₹37.31 lakh crore at ₹820.95 (box jump — doubling the stake with NEW capital; stop stays ₹748.60; charges ₹8,806.59 crore)
2025-12-08  SIRCA       SELL ₹3.40 crore crore at stop ₹485.64 (-2.7%, charges ₹75,437.70 crore) — the cash goes back to work at the next Friday screen
2025-12-15  GMRAIRPORT  BUY ₹3.04 crore crore at ₹103.95 (fresh Friday signal — BUY: 1.56× weekly, month 2.60×, ladder rising; stop ₹89.73; charges ₹71,765.21 crore)
2025-12-15  SANSERA     PYRAMID BUY ₹2.26 crore crore at ₹1,705.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,517.72; charges ₹53,282.96 crore)
2025-12-17  NACLIND     SELL ₹20.71 lakh crore at stop ₹164.20 (+2.6%, charges ₹4,600.93 crore) — the cash goes back to work at the next Friday screen
2025-12-22  GMRAIRPORT  PYRAMID BUY ₹2.98 crore crore at ₹102.05 (box jump — doubling the stake with NEW capital; stop stays ₹92.10; charges ₹70,287.17 crore)
2025-12-22  GOLDIETF    PYRAMID BUY ₹2.02 crore crore at ₹112.84 (box jump — doubling the stake with NEW capital; stop stays ₹107.32; charges ₹47,605.98 crore)
2025-12-29  TATSILV     PYRAMID BUY ₹1.96 crore crore at ₹23.50 (box jump — doubling the stake with NEW capital; stop stays ₹18.35; charges ₹46,353.71 crore)
2025-12-29  TATSILV     SELL ₹3.06 crore crore at stop ₹18.35 (-7.9%, charges ₹67,881.91 crore) — the cash goes back to work at the next Friday screen
2026-01-05  HDFCSILVER  PYRAMID BUY ₹2.87 crore crore at ₹224.14 (box jump — doubling the stake with NEW capital; stop stays ₹201.50; charges ₹67,657.57 crore)
2026-01-05  KIRIINDUS   BUY ₹3.62 crore crore at ₹622.00 (fresh Friday signal — BUY: 24.50× weekly, month 6.65×, ladder rising; stop ₹525.16; charges ₹85,444.98 crore)
2026-01-08  KIRIINDUS   SELL ₹3.04 crore crore at stop ₹525.16 (-15.6%, charges ₹67,568.71 crore) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹2.05 crore crore at stop ₹2,956.49 (-10.1%, charges ₹45,425.45 crore) — the cash goes back to work at the next Friday screen
2026-01-12  AGIIL       BUY ₹4.85 crore crore at ₹295.60 (fresh Friday signal — ACCUMULATE: 5.45× weekly, month 2.03×, ladder rising; stop ₹202.47; charges ₹1.15 lakh crore)
2026-01-12  SETFGOLD    PYRAMID BUY ₹4.17 crore crore at ₹118.70 (box jump — doubling the stake with NEW capital; stop stays ₹106.43; charges ₹98,537.86 crore)
2026-01-12  SILVERIETF  PYRAMID BUY ₹3.00 crore crore at ₹242.60 (box jump — doubling the stake with NEW capital; stop stays ₹208.50; charges ₹70,712.89 crore)
2026-01-19  CUB         PYRAMID BUY ₹6.86 crore crore at ₹269.65 (box jump — doubling the stake with NEW capital; stop stays ₹247.95; charges ₹1.62 lakh crore)
2026-01-19  SANSERA     PYRAMID BUY ₹4.88 crore crore at ₹1,846.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,672.76; charges ₹1.15 lakh crore)
2026-01-21  AVANTIFEED  SELL ₹67.81 lakh crore at stop ₹748.60 (-2.4%, charges ₹15,060.60 crore) — the cash goes back to work at the next Friday screen
2026-01-23  GMRAIRPORT  SELL ₹5.36 crore crore at stop ₹92.10 (-10.6%, charges ₹1.19 lakh crore) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹8.82 crore crore at stop ₹1,672.76 (-6.4%, charges ₹1.96 lakh crore) — the cash goes back to work at the next Friday screen
2026-01-27  GROWWSLVR   BUY ₹6.47 crore crore at ₹31.00 (fresh Friday signal — BUY: 5.65× weekly, month 5.51×, ladder rising; stop ₹19.45; charges ₹1.53 lakh crore)
2026-01-27  TATSILV     BUY ₹6.46 crore crore at ₹32.00 (fresh Friday signal — BUY: 9.86× weekly, month 21.32×, ladder rising; stop ₹19.90; charges ₹1.52 lakh crore)
2026-02-02  GOLDIETF    PYRAMID BUY ₹4.74 crore crore at ₹132.82 (box jump — doubling the stake with NEW capital; stop stays ₹115.68; charges ₹1.12 lakh crore)
2026-02-02  GROWWSLVR   PYRAMID BUY ₹5.05 crore crore at ₹24.27 (box jump — doubling the stake with NEW capital; stop stays ₹22.32; charges ₹1.19 lakh crore)
2026-02-02  GROWWSLVR   SELL ₹9.26 crore crore at stop ₹22.32 (-19.2%, charges ₹2.06 lakh crore) — the cash goes back to work at the next Friday screen
2026-02-02  TATSILV     PYRAMID BUY ₹5.54 crore crore at ₹27.52 (box jump — doubling the stake with NEW capital; stop stays ₹23.03; charges ₹1.31 lakh crore)
2026-02-02  TATSILV     SELL ₹9.24 crore crore at stop ₹23.03 (-22.6%, charges ₹2.05 lakh crore) — the cash goes back to work at the next Friday screen
2026-02-09  APEX        BUY ₹7.06 crore crore at ₹355.00 (fresh Friday signal — BUY: 2.98× weekly, month 4.24×, ladder rising; stop ₹221.66; charges ₹1.67 lakh crore)
2026-02-09  CPSEETF     BUY ₹7.11 crore crore at ₹99.82 (fresh Friday signal — BUY: 2.11× weekly, month 2.09×, ladder rising; stop ₹85.68; charges ₹1.68 lakh crore)
2026-02-09  LIQUIDPLUS  BUY ₹6.48 crore crore at ₹1,075.80 (fresh Friday signal — BUY: 1.56× weekly, month 3.05×, ladder rising; stop ₹1,009.92; charges ₹1.53 lakh crore)
2026-02-16  APEX        PYRAMID BUY ₹8.44 crore crore at ₹425.00 (box jump — doubling the stake with NEW capital; stop stays ₹327.85; charges ₹1.99 lakh crore)
2026-02-16  LIQUIDPLUS  PYRAMID BUY ₹6.42 crore crore at ₹1,068.50 (box jump — doubling the stake with NEW capital; stop stays ₹1,012.68; charges ₹1.52 lakh crore)
2026-02-23  APEX        PYRAMID BUY ₹17.92 crore crore at ₹452.00 (box jump — doubling the stake with NEW capital; stop stays ₹389.22; charges ₹4.23 lakh crore)
2026-02-23  CPSEETF     PYRAMID BUY ₹7.23 crore crore at ₹101.63 (box jump — doubling the stake with NEW capital; stop stays ₹91.67; charges ₹1.71 lakh crore)
2026-02-27  APEX        SELL ₹30.76 crore crore at stop ₹389.22 (-7.5%, charges ₹6.83 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-02  ABB         BUY ₹11.20 crore crore at ₹5,840.00 (fresh Friday signal — ACCUMULATE: 2.01× weekly, month 1.63×, ladder rising; stop ₹5,486.25; charges ₹2.64 lakh crore)
2026-03-02  J&KBANK     BUY ₹11.17 crore crore at ₹116.20 (fresh Friday signal — BUY: 8.67× weekly, month 1.90×, ladder rising; stop ₹96.50; charges ₹2.64 lakh crore)
2026-03-02  TORNTPOWER  BUY ₹8.40 crore crore at ₹1,491.00 (fresh Friday signal — BUY: 1.57× weekly, month 1.69×, ladder rising; stop ₹1,315.84; charges ₹1.98 lakh crore)
2026-03-09  CUB         SELL ₹12.76 crore crore at stop ₹251.43 (-6.4%, charges ₹2.83 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-16  AGIIL       PYRAMID BUY ₹4.99 crore crore at ₹305.00 (box jump — doubling the stake with NEW capital; stop stays ₹271.80; charges ₹1.18 lakh crore)
2026-03-16  APOLLOPIPE  BUY ₹12.76 crore crore at ₹407.55 (fresh Friday signal — BUY: 65.78× weekly, month 26.51×, ladder rising; stop ₹315.92; charges ₹3.01 lakh crore)
2026-03-16  CPSEETF     PYRAMID BUY ₹14.52 crore crore at ₹102.23 (box jump — doubling the stake with NEW capital; stop stays ₹96.54; charges ₹3.43 lakh crore)
2026-03-16  J&KBANK     PYRAMID BUY ₹11.62 crore crore at ₹121.14 (box jump — doubling the stake with NEW capital; stop stays ₹103.27; charges ₹2.74 lakh crore)
2026-03-23  ABB         PYRAMID BUY ₹11.99 crore crore at ₹6,264.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,854.38; charges ₹2.83 lakh crore)
2026-03-23  GOLDIETF    SELL ₹8.23 crore crore at stop ₹115.68 (-3.3%, charges ₹1.83 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-23  HDFCSILVER  SELL ₹5.14 crore crore at stop ₹201.50 (+8.0%, charges ₹1.14 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-23  J&KBANK     PYRAMID BUY ₹22.16 crore crore at ₹115.68 (box jump — doubling the stake with NEW capital; stop stays ₹110.67; charges ₹5.23 lakh crore)
2026-03-23  J&KBANK     SELL ₹42.25 crore crore at stop ₹110.67 (-5.6%, charges ₹9.38 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-23  SETFGOLD    SELL ₹8.09 crore crore at stop ₹115.37 (+4.4%, charges ₹1.80 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-23  SILVERIETF  SELL ₹5.13 crore crore at stop ₹208.50 (+7.4%, charges ₹1.14 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹17.53 crore crore at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹4.14 lakh crore)
2026-03-30  AGIIL       SELL ₹8.87 crore crore at stop ₹271.80 (-9.5%, charges ₹1.97 lakh crore) — the cash goes back to work at the next Friday screen
2026-03-30  APOLLOPIPE  PYRAMID BUY ₹13.22 crore crore at ₹423.35 (box jump — doubling the stake with NEW capital; stop stays ₹350.75; charges ₹3.12 lakh crore)
2026-03-30  LIQUID1     BUY ₹17.44 crore crore at ₹1,097.40 (fresh Friday signal — ACCUMULATE: 2.24× weekly, month 1.82×, ladder rising; stop ₹1,039.97; charges ₹4.12 lakh crore)
2026-03-30  TORNTPOWER  SELL ₹7.38 crore crore at stop ₹1,315.84 (-11.7%, charges ₹1.64 lakh crore) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹15.73 crore crore / LT ₹0.00)
2026-04-06  BAJAJHIND   BUY ₹17.70 crore crore at ₹17.08 (fresh Friday signal — ACCUMULATE: 2.33× weekly, month 1.97×, ladder rising; stop ₹13.87; charges ₹4.18 lakh crore)
2026-04-06  CHENNPETRO  BUY ₹17.72 crore crore at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹4.18 lakh crore)
2026-04-13  AETHER      PYRAMID BUY ₹17.78 crore crore at ₹1,170.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,010.28; charges ₹4.20 lakh crore)
2026-04-13  LIQUIDPLUS  PYRAMID BUY ₹12.98 crore crore at ₹1,080.91 (box jump — doubling the stake with NEW capital; stop stays ₹1,022.02; charges ₹3.06 lakh crore)
2026-04-13  THERMAX     BUY ₹14.70 crore crore at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹3.47 lakh crore)
2026-04-27  LIQUID1     PYRAMID BUY ₹17.49 crore crore at ₹1,103.44 (box jump — doubling the stake with NEW capital; stop stays ₹1,041.83; charges ₹4.13 lakh crore)
2026-05-04  BAJAJHIND   PYRAMID BUY ₹21.19 crore crore at ₹20.50 (box jump — doubling the stake with NEW capital; stop stays ₹17.96; charges ₹5.00 lakh crore)
2026-05-04  CPSEETF     PYRAMID BUY ₹31.35 crore crore at ₹110.50 (box jump — doubling the stake with NEW capital; stop stays ₹100.15; charges ₹7.40 lakh crore)
2026-05-11  AETHER      PYRAMID BUY ₹36.84 crore crore at ₹1,213.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,125.84; charges ₹8.70 lakh crore)
2026-05-11  APOLLOPIPE  PYRAMID BUY ₹30.88 crore crore at ₹495.00 (box jump — doubling the stake with NEW capital; stop stays ₹399.95; charges ₹7.29 lakh crore)
2026-05-11  LIQUID1     PYRAMID BUY ₹34.88 crore crore at ₹1,101.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,047.51; charges ₹8.23 lakh crore)
2026-05-11  THERMAX     PYRAMID BUY ₹19.20 crore crore at ₹4,707.00 (box jump — doubling the stake with NEW capital; stop stays ₹3,726.38; charges ₹4.53 lakh crore)
2026-05-14  AETHER      SELL ₹68.13 crore crore at stop ₹1,125.84 (-5.1%, charges ₹15.13 lakh crore) — the cash goes back to work at the next Friday screen
2026-05-14  BAJAJHIND   SELL ₹37.00 crore crore at stop ₹17.96 (-4.4%, charges ₹8.22 lakh crore) — the cash goes back to work at the next Friday screen
2026-05-18  ABB         PYRAMID BUY ₹24.12 crore crore at ₹6,310.00 (box jump — doubling the stake with NEW capital; stop stays ₹5,862.93; charges ₹5.69 lakh crore)
2026-05-18  CAPLIPOINT  BUY ₹47.95 crore crore at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹11.32 lakh crore)
2026-05-18  CHENNPETRO  PYRAMID BUY ₹17.79 crore crore at ₹995.00 (box jump — doubling the stake with NEW capital; stop stays ₹953.23; charges ₹4.20 lakh crore)
2026-05-18  NLCINDIA    BUY ₹47.93 crore crore at ₹351.55 (fresh Friday signal — BUY: 5.83× weekly, month 6.05×, ladder rising; stop ₹278.49; charges ₹11.31 lakh crore)
2026-05-18  THERMAX     PYRAMID BUY ₹36.34 crore crore at ₹4,458.60 (box jump — doubling the stake with NEW capital; stop stays ₹4,181.80; charges ₹8.58 lakh crore)
2026-05-25  APOLLOPIPE  PYRAMID BUY ₹65.50 crore crore at ₹525.65 (box jump — doubling the stake with NEW capital; stop stays ₹439.90; charges ₹15.46 lakh crore)
2026-05-25  CAPLIPOINT  PYRAMID BUY ₹49.51 crore crore at ₹2,059.40 (box jump — doubling the stake with NEW capital; stop stays ₹1,851.17; charges ₹11.69 lakh crore)
2026-05-25  NLCINDIA    PYRAMID BUY ₹47.35 crore crore at ₹348.10 (box jump — doubling the stake with NEW capital; stop stays ₹320.62; charges ₹11.18 lakh crore)
2026-06-02  CPSEETF     SELL ₹56.64 crore crore at stop ₹100.15 (-5.5%, charges ₹12.58 lakh crore) — the cash goes back to work at the next Friday screen
2026-06-08  ABB         PYRAMID BUY ₹54.26 crore crore at ₹7,105.50 (box jump — doubling the stake with NEW capital; stop stays ₹6,609.15; charges ₹12.81 lakh crore)
2026-06-08  RUBICON     BUY ₹65.88 crore crore at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹15.55 lakh crore)
2026-06-09  NLCINDIA    SELL ₹86.92 crore crore at stop ₹320.62 (-8.3%, charges ₹19.31 lakh crore) — the cash goes back to work at the next Friday screen
2026-06-15  CAPLIPOINT  PYRAMID BUY ₹116.93 crore crore at ₹2,435.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,852.50; charges ₹27.60 lakh crore)
2026-06-15  CHENNPETRO  PYRAMID BUY ₹41.35 crore crore at ₹1,158.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,075.02; charges ₹9.76 lakh crore)
2026-06-15  NRBBEARING  BUY ₹86.92 crore crore at ₹438.00 (fresh Friday signal — BUY: 10.53× weekly, month 6.95×, ladder rising; stop ₹331.98; charges ₹20.52 lakh crore)
2026-06-15  RUBICON     PYRAMID BUY ₹72.29 crore crore at ₹1,308.70 (box jump — doubling the stake with NEW capital; stop stays ₹1,042.53; charges ₹17.06 lakh crore)
2026-06-22  THERMAX     PYRAMID BUY ₹76.71 crore crore at ₹4,712.10 (box jump — doubling the stake with NEW capital; stop stays ₹4,306.64; charges ₹18.11 lakh crore)
2026-06-29  CAPLIPOINT  PYRAMID BUY ₹240.43 crore crore at ₹2,506.40 (box jump — doubling the stake with NEW capital; stop stays ₹2,209.13; charges ₹56.76 lakh crore)
2026-06-29  NRBBEARING  PYRAMID BUY ₹85.53 crore crore at ₹432.00 (box jump — doubling the stake with NEW capital; stop stays ₹391.97; charges ₹20.19 lakh crore)
2026-07-13  LIQUIDPLUS  PYRAMID BUY ₹26.25 crore crore at ₹1,093.96 (box jump — doubling the stake with NEW capital; stop stays ₹1,036.02; charges ₹6.20 lakh crore)
2026-07-13  RUBICON     PYRAMID BUY ₹157.89 crore crore at ₹1,431.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,221.98; charges ₹37.27 lakh crore)
2026-07-22  NRBBEARING  SELL ₹154.68 crore crore at stop ₹391.97 (-9.9%, charges ₹34.36 lakh crore) — the cash goes back to work at the next Friday screen
2026-07-27  BLUESTONE   BUY ₹154.68 crore crore at ₹793.00 (fresh Friday signal — BUY: 47.94× weekly, month 6.10×, ladder rising; stop ₹559.17; charges ₹36.51 lakh crore)
2026-07-27  CHENNPETRO  PYRAMID BUY ₹87.74 crore crore at ₹1,230.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,130.59; charges ₹20.71 lakh crore)
2026-07-27  RUBICON     PYRAMID BUY ₹340.54 crore crore at ₹1,545.00 (box jump — doubling the stake with NEW capital; stop stays ₹1,320.78; charges ₹80.39 lakh crore)
2026-07-29  THERMAX     SELL ₹139.75 crore crore at stop ₹4,306.64 (-4.5%, charges ₹31.04 lakh crore) — the cash goes back to work at the next Friday screen
2026-08-03  BLUESTONE   PYRAMID BUY ₹160.23 crore crore at ₹823.40 (box jump — doubling the stake with NEW capital; stop stays ₹664.75; charges ₹37.83 lakh crore)
2026-08-03  RATNAVEER   BUY ₹139.75 crore crore at ₹184.99 (fresh Friday signal — BUY: 9.23× weekly, month 4.03×, ladder rising; stop ₹162.56; charges ₹32.99 lakh crore)
2026-08-10  RATNAVEER   PYRAMID BUY ₹156.29 crore crore at ₹207.38 (box jump — doubling the stake with NEW capital; stop stays ₹165.36; charges ₹36.89 lakh crore)
2026-08-17  RATNAVEER   PYRAMID BUY ₹347.11 crore crore at ₹230.56 (box jump — doubling the stake with NEW capital; stop stays ₹194.19; charges ₹81.94 lakh crore)
2026-09-07  BLUESTONE   PYRAMID BUY ₹328.48 crore crore at ₹845.00 (box jump — doubling the stake with NEW capital; stop stays ₹747.41; charges ₹77.54 lakh crore)
2026-09-07  RATNAVEER   PYRAMID BUY ₹924.50 crore crore at ₹307.40 (box jump — doubling the stake with NEW capital; stop stays ₹263.29; charges ₹2.18 crore crore)
```
