# The Darvas screen — 2020-03-01 → 2026-09-11

> **LONG-RUN BACKTEST.** One continuous price archive (2019-03-01 → 2026-09-11, 1971 symbols, in `ROLLING_2019-03-01_to_2026-09-13/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. The net run pays Angel One charges on every order and settles capital-gains tax every 1 April. **The universe is POINT-IN-TIME with a ROLLING radar:** membership is recomputed EVERY MONTH as the top symbols by the TRAILING month's traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — casualties are IN while they traded, new listings enter the month they earn their place; membership gates fresh entries only (`_membership_long.csv`); split/bonus adjustments are heuristic, all listed in `_adjustments.csv`. No slippage, stop exits at the stop price, fractional shares. Stored fiscal statements exist for 37% of this universe — a stock without statements cannot be blocked by the earnings gate.

## The rules — the skill, kept simple

₹100 starts ALL IN CASH and nothing is ever added: the portfolio compounds only what it makes. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. **At most 10 positions at any time**, each fresh entry one equal slice (a tenth of equity), entries at the next trading day's open, falling earnings power refused, nothing below half a slice. **Cash never sleeps:** money freed by a stop goes into that week's fresh qualifiers, and a fully-qualified signal the cash never reached climbs the funding queue each time it is starved — front of the line ahead of louder newcomers, reset once funded. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; only the stop itself exits; a stopped symbol returns only by passing the full screen again. When nothing qualifies, the cash stays cash. NO pyramiding — doubling was built, measured and retired: on every configuration tested the add-on bought the top of the newest box with the stop a whole box lower, and the marginal rupee underperformed the base system.

## The headline — IRR, since capital is added when signals call

| | Money put in | Final value | IRR (money-weighted, per year) |
|---|---:|---:|---:|
| **This system, NET of charges and capital-gains tax** | ₹438.82 (₹100 + ₹338.82 added across 64 top-ups) | **₹750.48** | **+14.46%** |
| Before charges and taxes | ₹434.80 | ₹844.83 | +18.01% |
| Nifty 50 (same window, pre-cost, pre-tax) | ₹100.00 | ₹212.91 | +12.30% |

*₹1.07 of tax has accrued on the final part-year's realised gains (due next April) — settling it today would leave ₹749.41; unrealised gains in the end book carry a further deferred liability. 6.52 years, 341 weekly screens.*

## What the frictions took (net run)

- **Transaction charges: ₹22.76** (Angel One equity delivery: STT 0.10% both sides, exchange and SEBI levies, 18% GST, stamp duty 0.015% on buys, delivery brokerage ₹0 until 31 Oct 2024 then 0.1%).
- **Capital-gains tax paid: ₹45.35** — 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward.

| Fiscal year | Settled on | STCG @20% | LTCG @12.5% | Tax paid | Losses c/f (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2020 | 2020-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹3.06 / ₹0.00 |
| FY2021 | 2021-04-01 | ₹38.59 | ₹0.00 | ₹7.72 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹58.71 | ₹1.59 | ₹11.94 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹0.00 | ₹0.00 | ₹0.00 | ₹12.17 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹95.25 | ₹4.72 | ₹19.64 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.00 | ₹52.29 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹14.75 | ₹24.80 | ₹6.05 | ₹0.00 / ₹0.00 |
| Final part-year (accrued) | — | ₹5.33 | ₹0.00 | ₹1.07 | ₹0.00 / ₹0.00 |

## Calendar-year returns (Modified Dietz — money-weighted for the top-ups, so added capital is never booked as return)

| Year (through) | Net equity | Added in year | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|---:|
| 2020 (2020-12-24) | ₹162.90 | ₹21.77 | +38.2% | +39.0% | +25.1% |
| 2021 (2021-12-31) | ₹276.44 | ₹35.74 | +42.6% | +49.7% | +26.2% |
| 2022 (2022-12-30) | ₹286.90 | ₹39.82 | -9.9% | -5.4% | +4.3% |
| 2023 (2023-12-29) | ₹459.61 | ₹72.82 | +31.1% | +32.0% | +20.0% |
| 2024 (2024-12-27) | ₹508.44 | ₹67.75 | -3.8% | +0.9% | +9.6% |
| 2025 (2025-12-26) | ₹622.13 | ₹68.23 | +8.5% | +9.9% | +9.4% |
| 2026 (2026-09-11) | ₹750.48 | ₹32.67 | +14.7% | +16.8% | -10.2% |

## What it took to earn it

- **Maximum drawdown: -25.1%** (peak 2022-01-14 → trough 2022-05-13, weekly closes).
- **209 closed trades**: 85 winners (41%), average winner +29.6%, average loser -10.3%.
- Best closed trade KPITTECH +152.1%; worst MAHABANK -27.1%.
- Median holding period 65 days.
- Cash share of equity averaged 11% (median 3%); fully in cash 5 of 341 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net run)

| Month-end screen | Equity | Cash | Positions |
|---|---:|---:|---:|
| 2020-03-27 | ₹96.87 | ₹96.87 | 0 |
| 2020-04-30 | ₹97.13 | ₹38.46 | 6 |
| 2020-05-29 | ₹103.45 | ₹0.24 | 10 |
| 2020-06-26 | ₹113.32 | ₹0.00 | 10 |
| 2020-07-31 | ₹119.13 | ₹19.42 | 8 |
| 2020-08-28 | ₹125.80 | ₹3.30 | 10 |
| 2020-09-25 | ₹124.32 | ₹30.11 | 7 |
| 2020-10-30 | ₹127.64 | ₹13.87 | 9 |
| 2020-11-27 | ₹148.69 | ₹0.00 | 10 |
| 2020-12-24 | ₹162.90 | ₹76.51 | 5 |
| 2021-01-29 | ₹170.52 | ₹70.49 | 6 |
| 2021-02-26 | ₹190.80 | ₹15.27 | 9 |
| 2021-03-26 | ₹182.17 | ₹33.72 | 8 |
| 2021-04-30 | ₹193.98 | ₹0.94 | 10 |
| 2021-05-28 | ₹222.27 | ₹0.94 | 10 |
| 2021-06-25 | ₹237.17 | ₹1.99 | 10 |
| 2021-07-30 | ₹263.07 | ₹1.99 | 10 |
| 2021-08-27 | ₹250.68 | ₹46.45 | 8 |
| 2021-09-24 | ₹265.62 | ₹0.00 | 10 |
| 2021-10-29 | ₹259.65 | ₹3.20 | 10 |
| 2021-11-26 | ₹266.89 | ₹30.07 | 9 |
| 2021-12-31 | ₹276.44 | ₹37.07 | 9 |
| 2022-01-28 | ₹269.43 | ₹55.35 | 8 |
| 2022-02-25 | ₹245.20 | ₹200.59 | 2 |
| 2022-03-25 | ₹244.61 | ₹51.72 | 8 |
| 2022-04-29 | ₹240.35 | ₹47.35 | 8 |
| 2022-05-27 | ₹220.19 | ₹38.67 | 8 |
| 2022-06-24 | ₹226.63 | ₹14.31 | 9 |
| 2022-07-29 | ₹256.51 | ₹0.00 | 10 |
| 2022-08-26 | ₹275.61 | ₹4.77 | 10 |
| 2022-09-30 | ₹275.00 | ₹0.00 | 10 |
| 2022-10-28 | ₹286.38 | ₹0.15 | 10 |
| 2022-11-25 | ₹286.70 | ₹26.03 | 9 |
| 2022-12-30 | ₹286.90 | ₹140.86 | 5 |
| 2023-01-27 | ₹279.98 | ₹0.00 | 10 |
| 2023-02-24 | ₹294.96 | ₹28.12 | 9 |
| 2023-03-31 | ₹292.23 | ₹120.24 | 6 |
| 2023-04-28 | ₹316.58 | ₹2.98 | 10 |
| 2023-05-26 | ₹325.06 | ₹29.09 | 9 |
| 2023-06-30 | ₹347.78 | ₹0.00 | 10 |
| 2023-07-28 | ₹367.91 | ₹0.00 | 10 |
| 2023-08-25 | ₹375.75 | ₹0.00 | 10 |
| 2023-09-29 | ₹392.42 | ₹35.58 | 9 |
| 2023-10-27 | ₹395.98 | ₹193.42 | 5 |
| 2023-11-24 | ₹443.34 | ₹0.00 | 10 |
| 2023-12-29 | ₹459.61 | ₹0.00 | 10 |
| 2024-01-25 | ₹486.77 | ₹46.92 | 9 |
| 2024-02-23 | ₹523.82 | ₹6.31 | 10 |
| 2024-03-28 | ₹479.31 | ₹109.41 | 8 |
| 2024-04-26 | ₹498.31 | ₹0.00 | 10 |
| 2024-05-31 | ₹477.35 | ₹147.88 | 7 |
| 2024-06-28 | ₹499.92 | ₹0.00 | 10 |
| 2024-07-26 | ₹503.67 | ₹84.84 | 8 |
| 2024-08-30 | ₹504.33 | ₹12.87 | 10 |
| 2024-09-27 | ₹512.48 | ₹1.03 | 10 |
| 2024-10-25 | ₹460.81 | ₹94.27 | 8 |
| 2024-11-29 | ₹510.38 | ₹0.00 | 10 |
| 2024-12-27 | ₹508.44 | ₹0.00 | 10 |
| 2025-01-31 | ₹484.56 | ₹184.33 | 6 |
| 2025-02-28 | ₹435.80 | ₹142.22 | 7 |
| 2025-03-27 | ₹458.63 | ₹0.99 | 10 |
| 2025-04-25 | ₹468.14 | ₹32.53 | 9 |
| 2025-05-30 | ₹474.01 | ₹43.96 | 9 |
| 2025-06-27 | ₹503.52 | ₹0.00 | 10 |
| 2025-07-25 | ₹518.76 | ₹44.56 | 9 |
| 2025-08-29 | ₹521.33 | ₹0.00 | 10 |
| 2025-09-26 | ₹536.24 | ₹86.00 | 8 |
| 2025-10-31 | ₹560.32 | ₹98.63 | 9 |
| 2025-11-28 | ₹565.62 | ₹77.74 | 9 |
| 2025-12-26 | ₹622.13 | ₹7.76 | 10 |
| 2026-01-30 | ₹741.20 | ₹0.00 | 10 |
| 2026-02-27 | ₹712.83 | ₹0.00 | 10 |
| 2026-03-27 | ₹616.75 | ₹351.10 | 5 |
| 2026-04-30 | ₹647.80 | ₹32.53 | 10 |
| 2026-05-29 | ₹656.02 | ₹27.99 | 10 |
| 2026-06-25 | ₹659.63 | ₹28.50 | 10 |
| 2026-07-31 | ₹647.43 | ₹97.15 | 9 |
| 2026-08-28 | ₹716.64 | ₹94.41 | 9 |
| 2026-09-11 | ₹750.48 | ₹20.18 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,754.90 | 2,376.52 | +38.4% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,572.90 | 1,242.60 | +59.0% |
| HBLPOWER | 2024-07-29 | 634.15 | 652.65 | 583.02 | +2.9% |
| LIQUID1 | 2026-03-30 | 1,097.40 | 1,122.52 | 1,047.51 | +2.3% |
| LIQUIDPLUS | 2026-06-15 | 1,084.28 | 1,103.07 | 1,039.82 | +1.7% |
| MANINDS | 2026-06-08 | 526.00 | 866.10 | 700.58 | +64.7% |
| ORIENTREF | 2021-04-26 | 314.95 | 322.40 | 301.44 | +2.4% |
| PREMEXPLN | 2026-06-22 | 781.05 | 668.00 | 635.06 | -14.5% |
| RATNAVEER | 2026-08-03 | 184.99 | 288.30 | 263.29 | +55.8% |
| VINDHYATEL | 2026-09-07 | 2,755.00 | 2,813.50 | 2,555.50 | +2.1% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| HDFCMFGETF | 2020-03-09 | 4,002.50 | 2020-03-13 | 3,540.65 | -11.5% |
| LALPATHLAB | 2020-03-09 | 835.00 | 2020-03-13 | 743.38 | -11.0% |
| SETFGOLD | 2020-03-09 | 3,862.80 | 2020-03-17 | 3,548.39 | -8.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| AXISGOLD | 2020-04-13 | 4,049.00 | 2020-07-23 | 3,971.05 | -1.9% |
| GSPL | 2020-06-22 | 226.80 | 2020-07-29 | 201.11 | -11.3% |
| MANGCHEFER | 2020-05-11 | 33.75 | 2020-07-31 | 33.73 | -0.1% |
| EIDPARRY | 2020-05-11 | 164.00 | 2020-08-17 | 273.03 | +66.5% |
| LINCOLN | 2020-08-24 | 248.50 | 2020-08-31 | 224.20 | -9.8% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| GOLDBEES | 2020-04-13 | 41.24 | 2020-09-04 | 41.00 | -0.6% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| KIRLOSBROS | 2020-07-27 | 122.55 | 2020-09-08 | 120.79 | -1.4% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| HDFCMFGETF | 2020-04-20 | 4,385.40 | 2020-09-23 | 4,492.07 | +2.4% |
| VSTTILLERS | 2020-09-07 | 1,838.00 | 2020-09-24 | 1,676.56 | -8.8% |
| SEQUENT | 2020-08-03 | 123.80 | 2020-10-29 | 144.64 | +16.8% |
| GLAXO | 2020-09-14 | 1,675.00 | 2020-11-02 | 1,441.55 | -13.9% |
| KPITTECH | 2020-09-28 | 113.60 | 2020-11-02 | 93.15 | -18.0% |
| MEGH | 2020-08-03 | 59.20 | 2020-11-03 | 70.16 | +18.5% |
| TATAMTRDVR | 2020-09-07 | 58.50 | 2020-12-21 | 69.87 | +19.4% |
| ADANIGAS | 2020-09-14 | 209.75 | 2020-12-21 | 332.60 | +58.6% |
| LASA | 2020-11-09 | 80.50 | 2020-12-21 | 77.95 | -3.2% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| MAJESCO | 2020-11-02 | 920.10 | 2020-12-23 | 918.70 | -0.2% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| KIRIINDUS | 2020-12-28 | 537.55 | 2021-01-21 | 478.56 | -11.0% |
| TATASTLBSL | 2020-11-17 | 30.95 | 2021-01-22 | 40.61 | +31.2% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| XCHANGING | 2020-12-28 | 88.00 | 2021-01-25 | 80.75 | -8.2% |
| HFCL | 2020-12-28 | 25.60 | 2021-01-28 | 28.12 | +9.8% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| LGBBROSLTD | 2021-02-08 | 329.70 | 2021-02-18 | 310.84 | -5.7% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| RCF | 2021-02-08 | 56.90 | 2021-03-17 | 79.16 | +39.1% |
| APTECHT | 2020-12-28 | 154.75 | 2021-03-19 | 204.25 | +32.0% |
| HINDZINC | 2021-01-25 | 277.40 | 2021-03-19 | 279.30 | +0.7% |
| MHRIL | 2021-02-01 | 224.00 | 2021-03-19 | 210.90 | -5.8% |
| MAHABANK | 2021-03-01 | 25.20 | 2021-03-19 | 18.37 | -27.1% |
| UCOBANK | 2021-02-22 | 14.50 | 2021-03-22 | 12.52 | -13.7% |
| CENTENKA | 2021-03-22 | 264.00 | 2021-03-25 | 229.90 | -12.9% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| PRAKASH | 2021-03-22 | 67.15 | 2021-04-19 | 74.58 | +11.1% |
| POLYMED | 2020-09-07 | 449.70 | 2021-06-14 | 950.00 | +111.3% |
| KESORAMIND | 2020-12-28 | 61.95 | 2021-08-10 | 85.78 | +38.5% |
| WELSPUNIND | 2021-03-22 | 81.45 | 2021-08-10 | 124.64 | +53.0% |
| TATACOFFEE | 2021-01-25 | 118.70 | 2021-08-11 | 192.49 | +62.2% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| DHANUKA | 2021-06-21 | 956.40 | 2021-08-11 | 874.86 | -8.5% |
| SWARAJENG | 2021-08-16 | 1,795.00 | 2021-08-23 | 1,639.37 | -8.7% |
| MATRIMONY | 2021-08-16 | 1,136.35 | 2021-08-27 | 986.29 | -13.2% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| INDOCO | 2021-08-16 | 484.30 | 2021-11-12 | 412.30 | -14.9% |
| DEEPAKFERT | 2021-03-22 | 237.00 | 2021-11-18 | 368.55 | +55.5% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| ALICON | 2021-08-16 | 875.75 | 2021-11-29 | 718.58 | -17.9% |
| MAHLOG | 2021-08-30 | 805.00 | 2021-11-30 | 654.55 | -18.7% |
| APOLLOPIPE | 2021-08-30 | 1,525.00 | 2021-12-02 | 1,541.52 | +1.1% |
| KPITTECH | 2021-03-30 | 182.00 | 2021-12-20 | 458.85 | +152.1% |
| SOLARINDS | 2021-12-06 | 2,751.00 | 2021-12-20 | 2,397.37 | -12.9% |
| TCIEXP | 2021-12-06 | 2,277.25 | 2021-12-21 | 2,039.74 | -10.4% |
| MINDAIND | 2021-12-27 | 1,180.00 | 2022-01-07 | 1,088.41 | -7.8% |
| LTI | 2021-10-25 | 6,555.00 | 2022-01-24 | 6,270.00 | -4.3% |
| EVERESTIND | 2022-01-10 | 598.65 | 2022-01-24 | 536.75 | -10.3% |
| GABRIEL | 2021-01-25 | 114.60 | 2022-02-14 | 125.40 | +9.4% |
| BBL | 2021-11-15 | 923.50 | 2022-02-14 | 903.76 | -2.1% |
| BSOFT | 2021-11-22 | 473.00 | 2022-02-14 | 424.65 | -10.2% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| SUZLON | 2021-12-27 | 8.40 | 2022-02-15 | 9.79 | +16.5% |
| ANDHRSUGAR | 2022-01-31 | 157.95 | 2022-02-21 | 135.28 | -14.4% |
| ABCAPITAL | 2022-01-03 | 124.70 | 2022-02-22 | 103.58 | -16.9% |
| CCL | 2022-02-07 | 503.55 | 2022-02-24 | 441.75 | -12.3% |
| BIRLACABLE | 2022-03-14 | 162.10 | 2022-04-19 | 145.40 | -10.3% |
| SFL | 2021-12-06 | 3,417.00 | 2022-04-27 | 3,519.94 | +3.0% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| SRHHYPOLTD | 2022-03-07 | 408.00 | 2022-05-05 | 431.30 | +5.7% |
| ZUARIGLOB | 2022-03-14 | 195.30 | 2022-05-06 | 165.25 | -15.4% |
| INOXLEISUR | 2022-04-04 | 520.85 | 2022-05-06 | 470.35 | -9.7% |
| TNPL | 2022-04-25 | 211.10 | 2022-05-10 | 195.61 | -7.3% |
| VALIANTORG | 2022-04-04 | 1,010.90 | 2022-05-11 | 784.63 | -22.4% |
| MOL | 2022-05-09 | 129.80 | 2022-05-11 | 113.62 | -12.5% |
| RIIL | 2022-05-02 | 1,100.00 | 2022-05-26 | 863.73 | -21.5% |
| HUHTAMAKI | 2022-05-02 | 197.75 | 2022-05-26 | 161.50 | -18.3% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| MRPL | 2022-05-09 | 78.00 | 2022-07-06 | 69.61 | -10.8% |
| JKIL | 2022-05-09 | 229.70 | 2022-08-05 | 308.80 | +34.4% |
| ICICIGOLD | 2022-03-14 | 46.20 | 2022-08-29 | 41.50 | -10.2% |
| MARATHON | 2022-07-11 | 215.00 | 2022-09-19 | 232.80 | +8.3% |
| WSTCSTPAPR | 2022-08-08 | 498.00 | 2022-09-22 | 533.28 | +7.1% |
| VADILALIND | 2022-05-23 | 1,805.00 | 2022-10-20 | 2,295.06 | +27.2% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| JAICORPLTD | 2022-09-26 | 195.20 | 2022-11-03 | 165.39 | -15.3% |
| TDPOWERSYS | 2022-09-05 | 120.00 | 2022-11-09 | 103.50 | -13.8% |
| ANANTRAJ | 2022-10-24 | 107.65 | 2022-11-23 | 99.75 | -7.3% |
| RPGLIFE | 2022-11-14 | 960.80 | 2022-12-20 | 841.65 | -12.4% |
| ELECON | 2022-06-27 | 136.70 | 2022-12-21 | 202.49 | +48.1% |
| SHANTIGEAR | 2022-06-06 | 238.05 | 2022-12-22 | 345.56 | +45.2% |
| ACC | 2022-05-23 | 2,260.00 | 2022-12-23 | 2,465.16 | +9.1% |
| DAAWAT | 2022-09-26 | 113.35 | 2022-12-23 | 109.13 | -3.7% |
| GANECOS | 2022-11-07 | 857.00 | 2023-01-02 | 837.90 | -2.2% |
| WESTLIFE | 2022-11-07 | 763.50 | 2023-01-16 | 708.51 | -7.2% |
| BAJAJHIND | 2023-01-02 | 17.20 | 2023-01-30 | 13.98 | -18.7% |
| GICRE | 2023-01-02 | 179.20 | 2023-02-01 | 167.72 | -6.4% |
| ORIENTPPR | 2023-02-06 | 45.70 | 2023-02-13 | 39.90 | -12.7% |
| CGCL | 2022-03-07 | 600.00 | 2023-02-17 | 704.95 | +17.5% |
| CENTRALBK | 2022-11-28 | 25.70 | 2023-02-22 | 25.51 | -0.7% |
| SUNFLAG | 2023-01-23 | 131.50 | 2023-02-27 | 129.20 | -1.7% |
| MAHINDCIE | 2023-02-06 | 395.20 | 2023-03-10 | 391.69 | -0.9% |
| ATULAUTO | 2023-02-20 | 387.95 | 2023-03-13 | 335.92 | -13.4% |
| JINDALSAW | 2023-01-02 | 51.98 | 2023-03-27 | 67.92 | +30.7% |
| WONDERLA | 2023-03-06 | 456.00 | 2023-03-27 | 384.27 | -15.7% |
| CIGNITITEC | 2023-02-20 | 731.95 | 2023-03-29 | 705.14 | -3.7% |
| SONATSOFTW | 2023-02-27 | 360.00 | 2023-03-29 | 371.45 | +3.2% |
| JSL | 2023-01-02 | 241.00 | 2023-04-13 | 256.98 | +6.6% |
| VSSL | 2023-03-13 | 368.90 | 2023-05-26 | 324.52 | -12.0% |
| GSFC | 2023-01-02 | 140.70 | 2023-05-29 | 155.85 | +10.8% |
| ANURAS | 2023-03-20 | 755.90 | 2023-07-03 | 1,007.67 | +33.3% |
| KSB | 2023-04-10 | 451.00 | 2023-07-12 | 407.74 | -9.6% |
| CPSEETF | 2023-04-03 | 40.00 | 2023-07-31 | 41.97 | +4.9% |
| LAXMIMACH | 2023-05-29 | 11,604.35 | 2023-08-17 | 12,863.00 | +10.8% |
| TV18BRDCST | 2023-06-05 | 40.25 | 2023-09-28 | 43.08 | +7.0% |
| SETFGOLD | 2023-04-10 | 52.60 | 2023-10-03 | 49.74 | -5.4% |
| SJVN | 2023-07-10 | 48.00 | 2023-10-23 | 66.03 | +37.6% |
| HATHWAY | 2023-10-03 | 20.00 | 2023-10-23 | 18.10 | -9.5% |
| DEN | 2023-10-09 | 50.90 | 2023-10-23 | 46.98 | -7.7% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| MANINFRA | 2023-08-07 | 145.75 | 2023-10-26 | 140.65 | -3.5% |
| SPARC | 2023-07-17 | 225.30 | 2023-12-20 | 256.55 | +13.9% |
| ANGELONE | 2023-10-30 | 253.50 | 2024-01-23 | 296.88 | +17.1% |
| SUNDRMFAST | 2023-01-09 | 992.00 | 2024-02-09 | 1,155.25 | +16.5% |
| SAKSOFT | 2023-04-17 | 159.00 | 2024-02-12 | 305.02 | +91.8% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| IBREALEST | 2023-12-26 | 89.40 | 2024-03-06 | 102.92 | +15.1% |
| BOMDYEING | 2023-08-21 | 127.40 | 2024-03-11 | 164.59 | +29.2% |
| HITECH | 2023-11-06 | 102.75 | 2024-03-11 | 126.73 | +23.3% |
| GULFOILLUB | 2023-11-06 | 622.00 | 2024-03-12 | 941.07 | +51.3% |
| SPIC | 2024-01-29 | 87.00 | 2024-03-12 | 76.38 | -12.2% |
| AEGISCHEM | 2024-02-19 | 436.55 | 2024-03-13 | 394.30 | -9.7% |
| APOLLO | 2023-11-13 | 122.90 | 2024-03-26 | 105.78 | -13.9% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| SKIPPER | 2024-03-26 | 300.20 | 2024-05-28 | 297.82 | -0.8% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| FDC | 2024-02-12 | 449.00 | 2024-06-04 | 419.95 | -6.5% |
| BOSCHLTD | 2024-03-11 | 29,819.95 | 2024-06-04 | 29,015.09 | -2.7% |
| SMSPHARMA | 2024-03-18 | 189.20 | 2024-06-04 | 181.36 | -4.1% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| NCC | 2024-06-10 | 327.60 | 2024-07-23 | 297.87 | -9.1% |
| FINPIPE | 2024-06-10 | 350.00 | 2024-07-23 | 306.66 | -12.4% |
| THERMAX | 2024-06-03 | 5,640.00 | 2024-08-05 | 4,719.70 | -16.3% |
| ENDURANCE | 2024-06-10 | 2,439.90 | 2024-08-05 | 2,429.11 | -0.4% |
| EMUDHRA | 2024-03-18 | 583.90 | 2024-08-13 | 793.11 | +35.8% |
| AVANTIFEED | 2024-08-12 | 758.00 | 2024-09-09 | 650.13 | -14.2% |
| ORIENTELEC | 2024-06-10 | 237.91 | 2024-09-19 | 245.34 | +3.1% |
| VGUARD | 2024-08-19 | 524.15 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| HINDOILEXP | 2024-07-29 | 270.00 | 2024-10-07 | 220.07 | -18.5% |
| KALYANKJIL | 2024-09-16 | 723.20 | 2024-10-22 | 668.80 | -7.5% |
| SNOWMAN | 2024-08-12 | 79.80 | 2024-10-23 | 68.37 | -14.3% |
| BLUESTARCO | 2024-06-03 | 1,625.00 | 2024-11-07 | 1,795.74 | +10.5% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| MARKSANS | 2024-09-23 | 326.00 | 2024-12-20 | 282.25 | -13.4% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| KAYNES | 2024-12-23 | 7,358.80 | 2025-01-10 | 6,670.80 | -9.3% |
| WABAG | 2024-06-03 | 1,029.05 | 2025-01-13 | 1,446.29 | +40.5% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| BFUTILITIE | 2024-10-14 | 1,068.60 | 2025-01-27 | 860.15 | -19.5% |
| FSL | 2024-11-11 | 367.05 | 2025-01-28 | 332.14 | -9.5% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| APOLLO | 2025-01-20 | 131.50 | 2025-02-17 | 110.19 | -16.2% |
| BSE | 2024-10-14 | 4,536.00 | 2025-02-28 | 4,954.63 | +9.2% |
| GANESHHOUC | 2024-11-11 | 1,119.30 | 2025-02-28 | 1,090.38 | -2.6% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| TAJGVK | 2025-02-24 | 440.40 | 2025-04-02 | 453.34 | +2.9% |
| HDFCGOLD | 2025-02-10 | 75.80 | 2025-04-07 | 71.44 | -5.8% |
| SETFGOLD | 2025-02-17 | 76.80 | 2025-04-07 | 69.36 | -9.7% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| GRMOVER | 2025-03-10 | 252.00 | 2025-05-07 | 290.80 | +15.4% |
| VADILALIND | 2025-04-15 | 5,898.90 | 2025-05-30 | 5,401.40 | -8.4% |
| VMART | 2025-05-12 | 894.50 | 2025-07-03 | 797.90 | -10.8% |
| QUICKHEAL | 2025-07-07 | 402.00 | 2025-07-21 | 354.54 | -11.8% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| TIMKEN | 2025-06-02 | 3,120.00 | 2025-08-04 | 3,114.10 | -0.2% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| BLISSGVS | 2025-08-11 | 178.60 | 2025-09-26 | 143.93 | -19.4% |
| FORCEMOT | 2025-07-28 | 17,500.00 | 2025-10-09 | 15,350.10 | -12.3% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| TFCILTD | 2025-04-28 | 37.60 | 2025-10-30 | 69.12 | +83.8% |
| PRAKASH | 2025-08-11 | 178.70 | 2025-11-14 | 147.31 | -17.6% |
| SKYGOLD | 2025-10-27 | 370.00 | 2025-11-25 | 329.13 | -11.0% |
| PARAGMILK | 2025-11-17 | 354.00 | 2025-12-09 | 293.55 | -17.1% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| GMRAIRPORT | 2025-12-15 | 103.95 | 2026-01-23 | 92.10 | -11.4% |
| GOLDBEES | 2025-04-07 | 74.60 | 2026-02-02 | 113.05 | +51.5% |
| GOLDIETF | 2025-03-10 | 74.30 | 2026-03-23 | 115.68 | +55.7% |
| HDFCSILVER | 2025-09-29 | 137.30 | 2026-03-23 | 201.50 | +46.8% |
| SILVERIETF | 2025-09-29 | 142.00 | 2026-03-23 | 208.50 | +46.8% |
| HDFCGOLD | 2025-10-13 | 106.57 | 2026-03-23 | 114.75 | +7.7% |
| SETFGOLD | 2026-01-27 | 133.33 | 2026-03-23 | 115.37 | -13.5% |
| MAHABANK | 2025-11-03 | 59.70 | 2026-03-30 | 61.05 | +2.3% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| BAJAJHIND | 2026-04-06 | 17.08 | 2026-05-14 | 17.96 | +5.2% |
| CPSEETF | 2026-02-09 | 99.82 | 2026-06-02 | 100.15 | +0.3% |
| NLCINDIA | 2026-04-20 | 303.60 | 2026-06-09 | 320.62 | +5.6% |
| GOLD1 | 2026-01-27 | 132.24 | 2026-06-10 | 121.71 | -8.0% |
| ATHERENERG | 2026-05-18 | 930.00 | 2026-06-18 | 951.09 | +2.3% |
| NRBBEARING | 2026-06-15 | 438.00 | 2026-07-22 | 391.97 | -10.5% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.64 | +19.8% |
| GABRIEL | 2026-07-27 | 1,370.10 | 2026-08-25 | 1,349.19 | -1.5% |

## The complete trade blotter

*Buys, sells and tax settlements; every stop raise, starved signal and refused signal is in `_longrun_events_2020-03-01_to_2026-09-11.csv` (6198 events in all).*

```
2020-03-09  HDFCMFGETF  BUY ₹10.01 at ₹4,002.50 (fresh Friday signal — ACCUMULATE: 2.73× weekly, month 2.32×, ladder rising; stop ₹3,540.65; charges ₹0.01)
2020-03-09  LALPATHLAB  BUY ₹9.99 at ₹835.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.75×, ladder rising; stop ₹743.38; charges ₹0.01)
2020-03-09  SETFGOLD    BUY ₹10.00 at ₹3,862.80 (fresh Friday signal — BUY: 3.14× weekly, month 2.45×, ladder rising; stop ₹3,548.39; charges ₹0.01)
2020-03-13  HDFCMFGETF  SELL ₹8.84 at stop ₹3,540.65 (-11.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-13  LALPATHLAB  SELL ₹8.88 at stop ₹743.38 (-11.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-03-17  SETFGOLD    SELL ₹9.17 at stop ₹3,548.39 (-8.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-04-01  TAX         FY2020 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹3.06 / LT ₹0.00)
2020-04-13  AXISGOLD    BUY ₹9.72 at ₹4,049.00 (fresh Friday signal — ACCUMULATE: 1.53× weekly, month 3.08×, ladder rising; stop ₹3,199.23; charges ₹0.01)
2020-04-13  GOLDBEES    BUY ₹9.69 at ₹41.24 (fresh Friday signal — ACCUMULATE: 1.55× weekly, month 9.44×, ladder rising; stop ₹31.74; charges ₹0.01)
2020-04-20  HDFCMFGETF  BUY ₹9.74 at ₹4,385.40 (fresh Friday signal — BUY: 2.66× weekly, month 4.34×, ladder rising; stop ₹3,695.50; charges ₹0.01)
2020-04-27  CADILAHC    BUY ₹9.75 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 4.52×, ladder rising; stop ₹310.03; charges ₹0.01)
2020-04-27  SYNGENE     BUY ₹9.76 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.67×, ladder rising; stop ₹285.95; charges ₹0.01)
2020-04-27  TAJGVK      BUY ₹9.75 at ₹133.40 (fresh Friday signal — BUY: 6.65× weekly, month 2.45×, ladder rising; stop ₹106.49; charges ₹0.01)
2020-04-30  AXISGOLD    RAISE STOP ₹3,199.23 → ₹3,943.45 (new box ₹4,151.00–₹4,802.10 sealed)
2020-04-30  HDFCMFGETF  RAISE STOP ₹3,695.50 → ₹4,037.50 (new box ₹4,250.00–₹4,830.70 sealed)
2020-05-11  APLLTD      BUY ₹9.53 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.70× weekly, month 6.57×, ladder rising; stop ₹694.45; charges ₹0.01)
2020-05-11  EIDPARRY    BUY ₹9.57 at ₹164.00 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 1.53×, ladder rising; stop ₹132.60; charges ₹0.01)
2020-05-11  IOLCP       BUY ₹9.54 at ₹66.18 (fresh Friday signal — BUY: 2.18× weekly, month 2.73×, ladder rising; stop ₹51.22; charges ₹0.01)
2020-05-11  MANGCHEFER  BUY ₹9.58 at ₹33.75 (fresh Friday signal — BUY: 2.54× weekly, month 2.97×, ladder rising; stop ₹29.50; charges ₹0.01)
2020-05-15  MANGCHEFER  RAISE STOP ₹29.50 → ₹30.64 (new box ₹32.25–₹36.25 sealed)
2020-05-15  TAJGVK      RAISE STOP ₹106.49 → ₹107.73 (new box ₹117.00–₹147.90 sealed)
2020-05-22  IOLCP       RAISE STOP ₹51.22 → ₹69.35 (new box ₹73.00–₹80.96 sealed)
2020-06-05  APLLTD      RAISE STOP ₹694.45 → ₹785.37 (new box ₹826.70–₹915.00 sealed)
2020-06-05  CADILAHC    RAISE STOP ₹310.03 → ₹316.35 (new box ₹333.00–₹353.00 sealed)
2020-06-05  SYNGENE     RAISE STOP ₹285.95 → ₹323.19 (new box ₹340.20–₹382.00 sealed)
2020-06-16  IOLCP       SELL ₹9.97 at stop ₹69.35 (+4.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-06-19  CADILAHC    RAISE STOP ₹316.35 → ₹338.53 (new box ₹356.35–₹383.60 sealed)
2020-06-19  EIDPARRY    RAISE STOP ₹132.60 → ₹204.49 (new box ₹215.25–₹237.80 sealed)
2020-06-19  MANGCHEFER  RAISE STOP ₹30.64 → ₹33.73 (new box ₹35.50–₹40.25 sealed)
2020-06-19  TAJGVK      RAISE STOP ₹107.73 → ₹126.45 (new box ₹137.65–₹175.00 sealed)
2020-06-22  GSPL        BUY ₹11.16 at ₹226.80 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.87× weekly, month 1.88×, ladder rising; ₹0.94 fresh capital added; stop ₹201.11; charges ₹0.01)
2020-07-03  APLLTD      RAISE STOP ₹785.37 → ₹830.30 (new box ₹874.00–₹983.15 sealed)
2020-07-03  EIDPARRY    RAISE STOP ₹204.49 → ₹249.19 (new box ₹262.30–₹279.80 sealed)
2020-07-03  SYNGENE     RAISE STOP ₹323.19 → ₹378.10 (new box ₹398.00–₹424.00 sealed)
2020-07-10  AXISGOLD    RAISE STOP ₹3,943.45 → ₹3,971.05 (new box ₹4,180.05–₹4,503.40 sealed)
2020-07-23  AXISGOLD    SELL ₹9.51 at stop ₹3,971.05 (-1.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-07-24  EIDPARRY    RAISE STOP ₹249.19 → ₹273.03 (new box ₹287.40–₹313.80 sealed)
2020-07-27  KIRLOSBROS  BUY ₹11.36 at ₹122.55 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 9.32× weekly, month 6.82×, ladder rising; ₹1.85 fresh capital added; stop ₹97.15; charges ₹0.01)
2020-07-29  GSPL        SELL ₹9.87 at stop ₹201.11 (-11.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-07-31  APLLTD      RAISE STOP ₹830.30 → ₹903.45 (new box ₹951.00–₹1,045.00 sealed)
2020-07-31  MANGCHEFER  SELL ₹9.55 at stop ₹33.73 (-0.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-08-03  MEGH        BUY ₹11.90 at ₹59.20 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.80× weekly, month 3.46×, ladder rising; ₹4.38 fresh capital added; stop ₹53.58; charges ₹0.01)
2020-08-03  SEQUENT     BUY ₹11.90 at ₹123.80 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.93× weekly, month 4.08×, ladder rising; stop ₹103.69; charges ₹0.01)
2020-08-07  HDFCMFGETF  RAISE STOP ₹4,037.50 → ₹4,492.07 (new box ₹4,728.50–₹5,338.50 sealed)
2020-08-07  KIRLOSBROS  RAISE STOP ₹97.15 → ₹119.79 (new box ₹126.10–₹137.70 sealed)
2020-08-07  MEGH        RAISE STOP ₹53.58 → ₹55.58 (new box ₹58.50–₹64.50 sealed)
2020-08-14  CADILAHC    RAISE STOP ₹338.53 → ₹364.99 (new box ₹384.20–₹411.50 sealed)
2020-08-14  MEGH        RAISE STOP ₹55.58 → ₹59.47 (new box ₹62.60–₹69.90 sealed)
2020-08-14  SYNGENE     RAISE STOP ₹378.10 → ₹434.44 (new box ₹457.30–₹504.00 sealed)
2020-08-17  EIDPARRY    SELL ₹15.90 at stop ₹273.03 (+66.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-08-21  GOLDBEES    RAISE STOP ₹31.74 → ₹41.00 (new box ₹43.16–₹49.60 sealed)
2020-08-21  KIRLOSBROS  RAISE STOP ₹119.79 → ₹120.79 (new box ₹127.15–₹147.35 sealed)
2020-08-24  LINCOLN     BUY ₹12.60 at ₹248.50 (fresh Friday signal — starved 4×, front of the queue — BUY: 4.53× weekly, month 6.98×, ladder rising; stop ₹199.55; charges ₹0.01)
2020-08-28  APLLTD      RAISE STOP ₹903.45 → ₹928.62 (new box ₹977.50–₹1,049.00 sealed)
2020-08-28  LINCOLN     RAISE STOP ₹199.55 → ₹224.20 (new box ₹236.00–₹254.50 sealed)
2020-08-28  SEQUENT     RAISE STOP ₹103.69 → ₹110.97 (new box ₹118.95–₹145.55 sealed)
2020-08-31  LINCOLN     SELL ₹11.34 at stop ₹224.20 (-9.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.40 at stop ₹928.62 (+19.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-04  GOLDBEES    SELL ₹9.61 at stop ₹41.00 (-0.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-04  MEGH        RAISE STOP ₹59.47 → ₹61.01 (new box ₹65.60–₹80.90 sealed)
2020-09-07  POLYMED     BUY ₹11.99 at ₹449.70 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.13× weekly, month 2.67×, ladder rising; stop ₹372.40; charges ₹0.01)
2020-09-07  TATAMTRDVR  BUY ₹11.95 at ₹58.50 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.04× weekly, month 2.34×, ladder rising; stop ₹47.02; charges ₹0.01)
2020-09-07  VSTTILLERS  BUY ₹12.01 at ₹1,838.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.52× weekly, month 3.94×, ladder rising; ₹0.30 fresh capital added; stop ₹1,481.95; charges ₹0.01)
2020-09-08  CADILAHC    SELL ₹10.75 at stop ₹364.99 (+10.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-08  KIRLOSBROS  SELL ₹11.17 at stop ₹120.79 (-1.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-11  POLYMED     RAISE STOP ₹372.40 → ₹408.50 (new box ₹430.00–₹497.70 sealed)
2020-09-14  ADANIGAS    BUY ₹12.72 at ₹209.75 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.79× weekly, month 1.71×, ladder rising; ₹3.47 fresh capital added; stop ₹159.58; charges ₹0.02)
2020-09-14  GLAXO       BUY ₹12.68 at ₹1,675.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.58× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.02)
2020-09-18  TATAMTRDVR  RAISE STOP ₹47.02 → ₹52.77 (new box ₹55.55–₹62.95 sealed)
2020-09-18  VSTTILLERS  RAISE STOP ₹1,481.95 → ₹1,676.56 (new box ₹1,764.80–₹1,937.95 sealed)
2020-09-22  TAJGVK      SELL ₹9.22 at stop ₹126.45 (-5.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-23  HDFCMFGETF  SELL ₹9.95 at stop ₹4,492.07 (+2.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-24  VSTTILLERS  SELL ₹10.94 at stop ₹1,676.56 (-8.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-25  MEGH        RAISE STOP ₹61.01 → ₹70.16 (new box ₹73.85–₹85.20 sealed)
2020-09-25  SEQUENT     RAISE STOP ₹110.97 → ₹120.62 (new box ₹129.20–₹157.80 sealed)
2020-09-25  SYNGENE     RAISE STOP ₹434.44 → ₹501.60 (new box ₹528.00–₹594.95 sealed)
2020-09-28  HCLTECH     BUY ₹12.75 at ₹838.40 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.02)
2020-09-28  KPITTECH    BUY ₹12.75 at ₹113.60 (fresh Friday signal — ACCUMULATE: 2.60× weekly, month 3.04×, ladder rising; ₹8.17 fresh capital added; stop ₹93.15; charges ₹0.02)
2020-09-28  SAKSOFT     BUY ₹12.78 at ₹398.70 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.02)
2020-10-01  ADANIGAS    RAISE STOP ₹159.58 → ₹162.03 (new box ₹174.25–₹215.00 sealed)
2020-10-01  GLAXO       RAISE STOP ₹1,437.44 → ₹1,441.55 (new box ₹1,526.00–₹1,807.50 sealed)
2020-10-01  POLYMED     RAISE STOP ₹408.50 → ₹420.11 (new box ₹443.00–₹519.30 sealed)
2020-10-01  TATAMTRDVR  RAISE STOP ₹52.77 → ₹53.70 (new box ₹57.00–₹68.00 sealed)
2020-10-09  HCLTECH     RAISE STOP ₹740.29 → ₹766.75 (new box ₹807.10–₹844.75 sealed)
2020-10-09  SEQUENT     RAISE STOP ₹120.62 → ₹144.64 (new box ₹152.25–₹162.75 sealed)
2020-10-23  HCLTECH     RAISE STOP ₹766.75 → ₹779.57 (new box ₹820.60–₹910.70 sealed)
2020-10-29  SEQUENT     SELL ₹13.87 at stop ₹144.64 (+16.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹10.89 at stop ₹1,441.55 (-13.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-11-02  KPITTECH    SELL ₹10.43 at stop ₹93.15 (-18.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-11-02  MAJESCO     BUY ₹12.57 at ₹920.10 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.86× weekly, month 4.93×, ladder rising; stop ₹826.60; charges ₹0.01)
2020-11-03  MEGH        SELL ₹14.07 at stop ₹70.16 (+18.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹12.86 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.02)
2020-11-09  LASA        BUY ₹12.89 at ₹80.50 (fresh Friday signal — BUY: 3.08× weekly, month 3.28×, ladder rising; stop ₹65.41; charges ₹0.02)
2020-11-13  ADANIGAS    RAISE STOP ₹162.03 → ₹219.69 (new box ₹231.25–₹247.30 sealed)
2020-11-17  TATASTLBSL  BUY ₹13.60 at ₹30.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.01× weekly, month 2.00×, ladder rising; ₹2.65 fresh capital added; stop ₹22.80; charges ₹0.02)
2020-11-20  LASA        RAISE STOP ₹65.41 → ₹71.68 (new box ₹75.45–₹83.50 sealed)
2020-11-20  MAJESCO     RAISE STOP ₹826.60 → ₹864.50 (new box ₹910.00–₹935.00 sealed)
2020-11-27  BORORENEW   RAISE STOP ₹77.16 → ₹106.40 (new box ₹112.00–₹122.00 sealed)
2020-11-27  TATAMTRDVR  RAISE STOP ₹53.70 → ₹66.88 (new box ₹70.40–₹78.20 sealed)
2020-12-04  ADANIGAS    RAISE STOP ₹219.69 → ₹295.81 (new box ₹311.95–₹365.75 sealed)
2020-12-04  LASA        RAISE STOP ₹71.68 → ₹77.95 (new box ₹82.05–₹88.50 sealed)
2020-12-11  BORORENEW   RAISE STOP ₹106.40 → ₹123.97 (new box ₹130.50–₹140.70 sealed)
2020-12-11  MAJESCO     RAISE STOP ₹864.50 → ₹918.70 (new box ₹967.05–₹986.20 sealed)
2020-12-18  ADANIGAS    RAISE STOP ₹295.81 → ₹332.60 (new box ₹350.10–₹382.65 sealed)
2020-12-18  SYNGENE     RAISE STOP ₹501.60 → ₹562.40 (new box ₹592.00–₹624.95 sealed)
2020-12-18  TATAMTRDVR  RAISE STOP ₹66.88 → ₹69.87 (new box ₹73.55–₹81.25 sealed)
2020-12-18  TATASTLBSL  RAISE STOP ₹22.80 → ₹34.30 (new box ₹36.10–₹39.45 sealed)
2020-12-21  ADANIGAS    SELL ₹20.12 at stop ₹332.60 (+58.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-12-21  LASA        SELL ₹12.45 at stop ₹77.95 (-3.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-12-21  TATAMTRDVR  SELL ₹14.24 at stop ₹69.87 (+19.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-12-22  SYNGENE     SELL ₹17.18 at stop ₹562.40 (+76.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-12-23  MAJESCO     SELL ₹12.52 at stop ₹918.70 (-0.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-12-24  BORORENEW   RAISE STOP ₹123.97 → ₹148.20 (new box ₹156.00–₹181.00 sealed)
2020-12-28  APTECHT     BUY ₹16.68 at ₹154.75 (fresh Friday signal — starved 4×, front of the queue — BUY: 3.24× weekly, month 2.88×, ladder rising; stop ₹123.03; charges ₹0.02)
2020-12-28  HFCL        BUY ₹16.74 at ₹25.60 (fresh Friday signal — starved 4×, front of the queue — BUY: 2.33× weekly, month 3.95×, ladder rising; stop ₹19.05; charges ₹0.02)
2020-12-28  KESORAMIND  BUY ₹16.77 at ₹61.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.82× weekly, month 7.26×, ladder rising; ₹7.23 fresh capital added; stop ₹46.12; charges ₹0.02)
2020-12-28  KIRIINDUS   BUY ₹16.79 at ₹537.55 (fresh Friday signal — starved 2×, front of the queue — BUY: 8.73× weekly, month 2.26×, ladder rising; stop ₹424.46; charges ₹0.02)
2020-12-28  XCHANGING   BUY ₹16.76 at ₹88.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 3.95× weekly, month 3.92×, ladder rising; stop ₹71.32; charges ₹0.02)
2021-01-01  KESORAMIND  RAISE STOP ₹46.12 → ₹49.45 (new box ₹53.50–₹67.00 sealed)
2021-01-01  KIRIINDUS   RAISE STOP ₹424.46 → ₹478.56 (new box ₹513.75–₹631.05 sealed)
2021-01-08  HFCL        RAISE STOP ₹19.05 → ₹24.13 (new box ₹25.40–₹27.25 sealed)
2021-01-15  BORORENEW   RAISE STOP ₹148.20 → ₹247.59 (new box ₹265.05–₹323.25 sealed)
2021-01-15  SAKSOFT     RAISE STOP ₹303.81 → ₹341.10 (new box ₹359.05–₹405.00 sealed)
2021-01-15  TATASTLBSL  RAISE STOP ₹34.30 → ₹40.61 (new box ₹42.75–₹45.60 sealed)
2021-01-15  XCHANGING   RAISE STOP ₹71.32 → ₹80.75 (new box ₹85.00–₹92.00 sealed)
2021-01-20  BORORENEW   SELL ₹31.87 at stop ₹247.59 (+148.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-01-21  KIRIINDUS   SELL ₹14.92 at stop ₹478.56 (-11.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-01-22  HCLTECH     RAISE STOP ₹779.57 → ₹928.05 (new box ₹976.90–₹1,067.00 sealed)
2021-01-22  HFCL        RAISE STOP ₹24.13 → ₹28.12 (new box ₹29.60–₹33.80 sealed)
2021-01-22  TATASTLBSL  SELL ₹17.80 at stop ₹40.61 (+31.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-01-25  GABRIEL     BUY ₹17.55 at ₹114.60 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.54× weekly, month 3.77×, ladder rising; stop ₹86.90; charges ₹0.02)
2021-01-25  HINDZINC    BUY ₹17.65 at ₹277.40 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 2.32× weekly, month 2.11×, ladder rising; stop ₹248.97; charges ₹0.02)
2021-01-25  SAKSOFT     SELL ₹10.91 at stop ₹341.10 (-14.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-01-25  TATACOFFEE  BUY ₹17.59 at ₹118.70 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.30× weekly, month 2.15×, ladder rising; stop ₹102.65; charges ₹0.02)
2021-01-25  XCHANGING   SELL ₹15.35 at stop ₹80.75 (-8.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-01-28  HFCL        SELL ₹18.34 at stop ₹28.12 (+9.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-01-29  APTECHT     RAISE STOP ₹123.03 → ₹156.94 (new box ₹165.20–₹191.80 sealed)
2021-01-29  HCLTECH     SELL ₹14.09 at stop ₹928.05 (+10.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-02-01  GAEL        BUY ₹17.45 at ₹71.47 (fresh Friday signal — starved 5×, front of the queue — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.02)
2021-02-01  MHRIL       BUY ₹17.43 at ₹224.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.64× weekly, month 1.67×, ladder rising; stop ₹200.74; charges ₹0.02)
2021-02-05  APTECHT     RAISE STOP ₹156.94 → ₹163.06 (new box ₹173.40–₹207.85 sealed)
2021-02-08  LGBBROSLTD  BUY ₹17.89 at ₹329.70 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.57× weekly, month 1.66×, ladder rising; ₹0.24 fresh capital added; stop ₹266.95; charges ₹0.02)
2021-02-08  RCF         BUY ₹17.96 at ₹56.90 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 1.67× weekly, month 1.90×, ladder rising; stop ₹50.16; charges ₹0.02)
2021-02-12  APTECHT     RAISE STOP ₹163.06 → ₹197.36 (new box ₹207.75–₹231.40 sealed)
2021-02-12  HINDZINC    RAISE STOP ₹248.97 → ₹279.30 (new box ₹294.00–₹306.40 sealed)
2021-02-12  LGBBROSLTD  RAISE STOP ₹266.95 → ₹310.84 (new box ₹327.20–₹349.70 sealed)
2021-02-18  LGBBROSLTD  SELL ₹16.83 at stop ₹310.84 (-5.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-02-22  UCOBANK     BUY ₹17.99 at ₹14.50 (fresh Friday signal — starved 1×, front of the queue — BUY: 13.91× weekly, month 5.44×, ladder rising; ₹1.16 fresh capital added; stop ₹11.07; charges ₹0.02)
2021-02-23  GAEL        SELL ₹15.27 at stop ₹62.70 (-12.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-02-26  KESORAMIND  RAISE STOP ₹49.45 → ₹62.23 (new box ₹65.50–₹72.85 sealed)
2021-02-26  MHRIL       RAISE STOP ₹200.74 → ₹210.90 (new box ₹222.00–₹240.00 sealed)
2021-02-26  UCOBANK     RAISE STOP ₹11.07 → ₹12.52 (new box ₹13.40–₹16.35 sealed)
2021-03-01  MAHABANK    BUY ₹20.03 at ₹25.20 (fresh Friday signal — starved 4×, front of the queue — ACCUMULATE: 3.28× weekly, month 6.37×, ladder rising; ₹4.75 fresh capital added; stop ₹18.37; charges ₹0.02)
2021-03-05  APTECHT     RAISE STOP ₹197.36 → ₹204.25 (new box ₹215.00–₹247.95 sealed)
2021-03-05  POLYMED     RAISE STOP ₹420.11 → ₹642.77 (new box ₹676.60–₹749.75 sealed)
2021-03-12  RCF         RAISE STOP ₹50.16 → ₹79.16 (new box ₹84.00–₹100.15 sealed)
2021-03-17  RCF         SELL ₹24.92 at stop ₹79.16 (+39.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹21.97 at stop ₹204.25 (+32.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-03-19  GABRIEL     RAISE STOP ₹86.90 → ₹86.92 (new box ₹98.00–₹134.95 sealed)
2021-03-19  HINDZINC    SELL ₹17.73 at stop ₹279.30 (+0.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-03-19  MAHABANK    SELL ₹14.57 at stop ₹18.37 (-27.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-03-19  MHRIL       SELL ₹16.37 at stop ₹210.90 (-5.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-03-22  CENTENKA    BUY ₹18.73 at ₹264.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.04× weekly, month 1.55×, ladder rising; stop ₹229.90; charges ₹0.02)
2021-03-22  DEEPAKFERT  BUY ₹18.73 at ₹237.00 (fresh Friday signal — starved 4×, front of the queue — BUY: 2.43× weekly, month 1.87×, ladder rising; stop ₹184.78; charges ₹0.02)
2021-03-22  KEI         BUY ₹18.70 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.02)
2021-03-22  PRAKASH     BUY ₹18.73 at ₹67.15 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.45× weekly, month 4.02×, ladder rising; stop ₹51.52; charges ₹0.02)
2021-03-22  UCOBANK     SELL ₹15.50 at stop ₹12.52 (-13.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-03-22  WELSPUNIND  BUY ₹18.72 at ₹81.45 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.57× weekly, month 2.42×, ladder rising; stop ₹67.45; charges ₹0.02)
2021-03-25  CENTENKA    SELL ₹16.27 at stop ₹229.90 (-12.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-03-26  DEEPAKFERT  RAISE STOP ₹184.78 → ₹209.52 (new box ₹220.55–₹249.45 sealed)
2021-03-26  KEI         RAISE STOP ₹436.67 → ₹471.20 (new box ₹496.00–₹558.00 sealed)
2021-03-26  POLYMED     RAISE STOP ₹642.77 → ₹719.96 (new box ₹765.55–₹917.50 sealed)
2021-03-26  WELSPUNIND  RAISE STOP ₹67.45 → ₹68.17 (new box ₹72.65–₹87.60 sealed)
2021-03-30  CENTRUM     BUY ₹18.29 at ₹28.40 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹0.02)
2021-03-30  KPITTECH    BUY ₹18.28 at ₹182.00 (fresh Friday signal — BUY: 1.71× weekly, month 2.77×, ladder rising; ₹2.85 fresh capital added; stop ₹136.62; charges ₹0.02)
2021-04-01  CENTRUM     TRIM 4.0% (₹0.73 at ₹28.35) to pay the tax bill
2021-04-01  DEEPAKFERT  TRIM 4.0% (₹0.74 at ₹234.55) to pay the tax bill
2021-04-01  GABRIEL     TRIM 4.0% (₹0.63 at ₹103.10) to pay the tax bill
2021-04-01  KEI         TRIM 4.0% (₹0.76 at ₹528.60) to pay the tax bill
2021-04-01  KESORAMIND  RAISE STOP ₹62.23 → ₹64.31 (new box ₹67.70–₹78.60 sealed)
2021-04-01  KESORAMIND  TRIM 4.0% (₹0.83 at ₹76.45) to pay the tax bill
2021-04-01  KPITTECH    TRIM 4.0% (₹0.71 at ₹175.70) to pay the tax bill
2021-04-01  POLYMED     TRIM 4.0% (₹0.89 at ₹837.20) to pay the tax bill
2021-04-01  PRAKASH     TRIM 4.0% (₹0.91 at ₹81.40) to pay the tax bill
2021-04-01  TATACOFFEE  RAISE STOP ₹102.65 → ₹108.58 (new box ₹114.30–₹128.70 sealed)
2021-04-01  TATACOFFEE  TRIM 4.0% (₹0.73 at ₹122.85) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹7.72 paid (STCG ₹38.59 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  WELSPUNIND  TRIM 4.0% (₹0.78 at ₹84.75) to pay the tax bill
2021-04-12  CENTRUM     SELL ₹15.35 at stop ₹24.89 (-12.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-04-16  KPITTECH    RAISE STOP ₹136.62 → ₹171.05 (new box ₹180.05–₹204.70 sealed)
2021-04-16  PRAKASH     RAISE STOP ₹51.52 → ₹74.58 (new box ₹78.50–₹90.85 sealed)
2021-04-19  KPRMILL     BUY ₹17.64 at ₹236.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.36× weekly, month 1.58×, ladder rising; ₹2.29 fresh capital added; stop ₹192.07; charges ₹0.02)
2021-04-19  PRAKASH     SELL ₹19.92 at stop ₹74.58 (+11.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-04-23  KPRMILL     RAISE STOP ₹192.07 → ₹221.37 (new box ₹233.02–₹255.60 sealed)
2021-04-26  ORIENTREF   BUY ₹18.98 at ₹314.95 (fresh Friday signal — BUY: 1.81× weekly, month 5.16×, ladder rising; stop ₹247.04; charges ₹0.02)
2021-05-07  KEI         RAISE STOP ₹471.20 → ₹485.02 (new box ₹510.55–₹532.45 sealed)
2021-05-07  KESORAMIND  RAISE STOP ₹64.31 → ₹66.59 (new box ₹70.10–₹79.50 sealed)
2021-05-07  ORIENTREF   RAISE STOP ₹247.04 → ₹283.10 (new box ₹298.00–₹322.30 sealed)
2021-05-14  KPRMILL     RAISE STOP ₹221.37 → ₹268.28 (new box ₹282.40–₹326.25 sealed)
2021-05-14  POLYMED     RAISE STOP ₹719.96 → ₹902.50 (new box ₹950.00–₹1,085.15 sealed)
2021-05-21  DEEPAKFERT  RAISE STOP ₹209.52 → ₹264.10 (new box ₹278.00–₹297.65 sealed)
2021-05-21  KESORAMIND  RAISE STOP ₹66.59 → ₹70.06 (new box ₹73.75–₹84.90 sealed)
2021-05-21  TATACOFFEE  RAISE STOP ₹108.58 → ₹149.67 (new box ₹157.55–₹180.90 sealed)
2021-05-28  KEI         RAISE STOP ₹485.02 → ₹558.60 (new box ₹588.00–₹638.80 sealed)
2021-05-28  TATACOFFEE  RAISE STOP ₹149.67 → ₹163.64 (new box ₹172.25–₹185.85 sealed)
2021-06-04  DEEPAKFERT  RAISE STOP ₹264.10 → ₹269.80 (new box ₹284.00–₹314.00 sealed)
2021-06-04  KESORAMIND  RAISE STOP ₹70.06 → ₹73.21 (new box ₹77.20–₹90.50 sealed)
2021-06-04  KPITTECH    RAISE STOP ₹171.05 → ₹214.70 (new box ₹226.00–₹250.60 sealed)
2021-06-04  ORIENTREF   RAISE STOP ₹283.10 → ₹287.19 (new box ₹302.30–₹337.40 sealed)
2021-06-04  POLYMED     RAISE STOP ₹902.50 → ₹950.00 (new box ₹1,000.00–₹1,165.00 sealed)
2021-06-04  WELSPUNIND  RAISE STOP ₹68.17 → ₹80.48 (new box ₹86.00–₹104.40 sealed)
2021-06-14  POLYMED     SELL ₹24.26 at stop ₹950.00 (+111.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-06-18  KEI         RAISE STOP ₹558.60 → ₹608.00 (new box ₹640.00–₹718.90 sealed)
2021-06-21  DHANUKA     BUY ₹23.20 at ₹956.40 (fresh Friday signal — starved 7×, front of the queue — BUY: 1.69× weekly, month 4.14×, ladder rising; stop ₹807.50; charges ₹0.03)
2021-06-25  DHANUKA     RAISE STOP ₹807.50 → ₹874.86 (new box ₹920.90–₹1,019.90 sealed)
2021-07-02  KESORAMIND  RAISE STOP ₹73.21 → ₹85.78 (new box ₹90.30–₹96.85 sealed)
2021-07-09  ORIENTREF   RAISE STOP ₹287.19 → ₹301.44 (new box ₹317.30–₹357.00 sealed)
2021-07-16  KPITTECH    RAISE STOP ₹214.70 → ₹232.94 (new box ₹245.20–₹274.00 sealed)
2021-07-16  KPRMILL     RAISE STOP ₹268.28 → ₹333.07 (new box ₹350.60–₹372.95 sealed)
2021-07-16  WELSPUNIND  RAISE STOP ₹80.48 → ₹97.56 (new box ₹102.70–₹109.70 sealed)
2021-07-30  WELSPUNIND  RAISE STOP ₹97.56 → ₹117.99 (new box ₹124.20–₹134.50 sealed)
2021-08-06  KPITTECH    RAISE STOP ₹232.94 → ₹266.76 (new box ₹280.80–₹315.65 sealed)
2021-08-06  KPRMILL     RAISE STOP ₹333.07 → ₹352.48 (new box ₹371.03–₹417.00 sealed)
2021-08-06  TATACOFFEE  RAISE STOP ₹163.64 → ₹192.49 (new box ₹205.00–₹246.70 sealed)
2021-08-06  WELSPUNIND  RAISE STOP ₹117.99 → ₹124.64 (new box ₹131.20–₹145.40 sealed)
2021-08-10  KESORAMIND  SELL ₹22.24 at stop ₹85.78 (+38.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNIND  SELL ₹27.44 at stop ₹124.64 (+53.0%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-08-11  DHANUKA     SELL ₹21.18 at stop ₹874.86 (-8.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹26.29 at stop ₹352.48 (+49.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-08-11  TATACOFFEE  SELL ₹27.31 at stop ₹192.49 (+62.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-08-13  GABRIEL     RAISE STOP ₹86.92 → ₹118.77 (new box ₹125.05–₹146.00 sealed)
2021-08-13  KEI         RAISE STOP ₹608.00 → ₹663.29 (new box ₹698.20–₹762.00 sealed)
2021-08-16  ALICON      BUY ₹25.98 at ₹875.75 (fresh Friday signal — BUY: 1.84× weekly, month 3.28×, ladder rising; ₹4.22 fresh capital added; stop ₹718.58; charges ₹0.03)
2021-08-16  INDOCO      BUY ₹26.22 at ₹484.30 (fresh Friday signal — starved 2×, front of the queue — BUY: 4.80× weekly, month 2.73×, ladder rising; stop ₹412.30; charges ₹0.03)
2021-08-16  MATRIMONY   BUY ₹26.11 at ₹1,136.35 (fresh Friday signal — BUY: 2.08× weekly, month 2.11×, ladder rising; stop ₹986.29; charges ₹0.03)
2021-08-16  SWARAJENG   BUY ₹26.15 at ₹1,795.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.68× weekly, month 2.90×, ladder rising; stop ₹1,639.37; charges ₹0.03)
2021-08-16  TATAINVEST  BUY ₹26.20 at ₹1,308.05 (fresh Friday signal — starved 1×, front of the queue — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.03)
2021-08-20  TATAINVEST  RAISE STOP ₹1,031.13 → ₹1,139.00 (new box ₹1,198.95–₹1,385.00 sealed)
2021-08-23  SWARAJENG   SELL ₹23.83 at stop ₹1,639.37 (-8.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-08-27  GABRIEL     RAISE STOP ₹118.77 → ₹124.06 (new box ₹133.00–₹162.80 sealed)
2021-08-27  KPITTECH    RAISE STOP ₹266.76 → ₹278.89 (new box ₹303.45–₹385.30 sealed)
2021-08-27  MATRIMONY   SELL ₹22.62 at stop ₹986.29 (-13.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-08-30  APOLLOPIPE  BUY ₹25.39 at ₹1,525.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.97× weekly, month 2.01×, ladder rising; stop ₹1,209.11; charges ₹0.03)
2021-08-30  MAHLOG      BUY ₹25.30 at ₹805.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.55× weekly, month 5.47×, ladder rising; ₹4.24 fresh capital added; stop ₹588.04; charges ₹0.03)
2021-09-09  APOLLOPIPE  RAISE STOP ₹1,209.11 → ₹1,368.00 (new box ₹1,440.00–₹1,525.00 sealed)
2021-09-09  KEI         RAISE STOP ₹663.29 → ₹718.20 (new box ₹756.00–₹792.95 sealed)
2021-09-09  TATAINVEST  RAISE STOP ₹1,139.00 → ₹1,183.22 (new box ₹1,245.50–₹1,294.50 sealed)
2021-09-17  KEI         RAISE STOP ₹718.20 → ₹737.39 (new box ₹776.20–₹841.00 sealed)
2021-09-24  APOLLOPIPE  RAISE STOP ₹1,368.00 → ₹1,417.40 (new box ₹1,492.00–₹1,619.80 sealed)
2021-09-24  DEEPAKFERT  RAISE STOP ₹269.80 → ₹368.55 (new box ₹393.00–₹474.50 sealed)
2021-09-24  TATAINVEST  RAISE STOP ₹1,183.22 → ₹1,187.74 (new box ₹1,250.25–₹1,320.00 sealed)
2021-10-01  APOLLOPIPE  RAISE STOP ₹1,417.40 → ₹1,541.52 (new box ₹1,622.65–₹1,709.95 sealed)
2021-10-08  KEI         RAISE STOP ₹737.39 → ₹853.10 (new box ₹898.00–₹997.70 sealed)
2021-10-14  TATAINVEST  RAISE STOP ₹1,187.74 → ₹1,349.09 (new box ₹1,420.10–₹1,509.00 sealed)
2021-10-22  KEI         SELL ₹29.27 at stop ₹853.10 (+63.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-10-25  LTI         BUY ₹26.07 at ₹6,555.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.63× weekly, month 1.84×, ladder rising; stop ₹5,353.77; charges ₹0.03)
2021-10-29  LTI         RAISE STOP ₹5,353.77 → ₹5,950.99 (new box ₹6,264.20–₹7,155.00 sealed)
2021-10-29  TATAINVEST  RAISE STOP ₹1,349.09 → ₹1,436.49 (new box ₹1,512.10–₹1,733.90 sealed)
2021-11-12  INDOCO      SELL ₹22.27 at stop ₹412.30 (-14.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-11-15  BBL         BUY ₹27.24 at ₹923.50 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.87× weekly, month 2.02×, ladder rising; ₹1.77 fresh capital added; stop ₹788.60; charges ₹0.03)
2021-11-18  DEEPAKFERT  SELL ₹27.89 at stop ₹368.55 (+55.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-11-22  BSOFT       BUY ₹26.54 at ₹473.00 (fresh Friday signal — BUY: 6.30× weekly, month 1.77×, ladder rising; stop ₹375.44; charges ₹0.03)
2021-11-26  KPITTECH    RAISE STOP ₹278.89 → ₹398.63 (new box ₹422.00–₹499.90 sealed)
2021-11-26  LTI         RAISE STOP ₹5,950.99 → ₹6,270.00 (new box ₹6,600.00–₹7,564.95 sealed)
2021-11-26  MAHLOG      RAISE STOP ₹588.04 → ₹654.55 (new box ₹689.00–₹778.90 sealed)
2021-11-26  TATAINVEST  SELL ₹28.71 at stop ₹1,436.49 (+9.8%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-11-29  ALICON      SELL ₹21.27 at stop ₹718.58 (-17.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-11-29  RAYMOND     BUY ₹26.20 at ₹596.00 (fresh Friday signal — starved 5×, front of the queue — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.03)
2021-11-30  MAHLOG      SELL ₹20.53 at stop ₹654.55 (-18.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-12-02  APOLLOPIPE  SELL ₹25.61 at stop ₹1,541.52 (+1.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2021-12-03  BSOFT       RAISE STOP ₹375.44 → ₹424.65 (new box ₹447.00–₹513.95 sealed)
2021-12-06  SFL         BUY ₹26.21 at ₹3,417.00 (fresh Friday signal — starved 5×, front of the queue — BUY: 2.40× weekly, month 2.05×, ladder rising; stop ₹2,838.79; charges ₹0.03)
2021-12-06  SOLARINDS   BUY ₹25.98 at ₹2,751.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.55× weekly, month 2.23×, ladder rising; ₹6.99 fresh capital added; stop ₹2,397.37; charges ₹0.03)
2021-12-06  TCIEXP      BUY ₹26.07 at ₹2,277.25 (fresh Friday signal — starved 4×, front of the queue — BUY: 1.93× weekly, month 1.55×, ladder rising; stop ₹1,909.50; charges ₹0.03)
2021-12-10  BBL         RAISE STOP ₹788.60 → ₹825.08 (new box ₹868.50–₹946.50 sealed)
2021-12-10  KPITTECH    RAISE STOP ₹398.63 → ₹458.85 (new box ₹483.00–₹531.00 sealed)
2021-12-10  RAYMOND     RAISE STOP ₹468.59 → ₹560.88 (new box ₹590.40–₹676.40 sealed)
2021-12-10  TCIEXP      RAISE STOP ₹1,909.50 → ₹2,039.74 (new box ₹2,147.10–₹2,376.85 sealed)
2021-12-20  KPITTECH    SELL ₹44.14 at stop ₹458.85 (+152.1%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2021-12-20  SOLARINDS   SELL ₹22.59 at stop ₹2,397.37 (-12.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-12-21  TCIEXP      SELL ₹23.30 at stop ₹2,039.74 (-10.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-12-27  MINDAIND    BUY ₹26.45 at ₹1,180.00 (fresh Friday signal — starved 4×, front of the queue — BUY: 3.66× weekly, month 2.64×, ladder rising; stop ₹929.20; charges ₹0.03)
2021-12-27  SUZLON      BUY ₹26.51 at ₹8.40 (fresh Friday signal — BUY: 1.64× weekly, month 1.53×, ladder rising; stop ₹6.18; charges ₹0.03)
2021-12-31  GABRIEL     RAISE STOP ₹124.06 → ₹125.40 (new box ₹132.00–₹146.30 sealed)
2021-12-31  MINDAIND    RAISE STOP ₹929.20 → ₹1,088.41 (new box ₹1,145.70–₹1,254.40 sealed)
2021-12-31  SFL         RAISE STOP ₹2,838.79 → ₹2,840.55 (new box ₹2,990.05–₹3,387.60 sealed)
2022-01-03  ABCAPITAL   BUY ₹27.98 at ₹124.70 (fresh Friday signal — ACCUMULATE: 1.52× weekly, month 1.54×, ladder rising; stop ₹101.63; charges ₹0.03)
2022-01-07  MINDAIND    SELL ₹24.34 at stop ₹1,088.41 (-7.8%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-01-10  EVERESTIND  BUY ₹28.15 at ₹598.65 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.00× weekly, month 1.77×, ladder rising; stop ₹490.96; charges ₹0.03)
2022-01-14  EVERESTIND  RAISE STOP ₹490.96 → ₹536.75 (new box ₹565.00–₹642.00 sealed)
2022-01-14  SUZLON      RAISE STOP ₹6.18 → ₹8.73 (new box ₹9.30–₹11.20 sealed)
2022-01-24  EVERESTIND  SELL ₹25.18 at stop ₹536.75 (-10.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-01-24  LTI         SELL ₹24.88 at stop ₹6,270.00 (-4.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-01-31  ANDHRSUGAR  BUY ₹27.27 at ₹157.95 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.89× weekly, month 1.58×, ladder rising; stop ₹119.37; charges ₹0.03)
2022-02-04  ABCAPITAL   RAISE STOP ₹101.63 → ₹103.58 (new box ₹111.80–₹139.20 sealed)
2022-02-04  ANDHRSUGAR  RAISE STOP ₹119.37 → ₹135.28 (new box ₹142.40–₹165.50 sealed)
2022-02-04  BBL         RAISE STOP ₹825.08 → ₹903.76 (new box ₹951.33–₹1,075.00 sealed)
2022-02-04  RAYMOND     RAISE STOP ₹560.88 → ₹679.35 (new box ₹715.10–₹800.00 sealed)
2022-02-04  SFL         RAISE STOP ₹2,840.55 → ₹2,922.75 (new box ₹3,162.00–₹3,959.50 sealed)
2022-02-04  SUZLON      RAISE STOP ₹8.73 → ₹9.79 (new box ₹10.55–₹13.10 sealed)
2022-02-07  CCL         BUY ₹27.09 at ₹503.55 (fresh Friday signal — starved 4×, front of the queue — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹0.03)
2022-02-11  CCL         RAISE STOP ₹408.60 → ₹441.75 (new box ₹465.00–₹514.95 sealed)
2022-02-14  BBL         SELL ₹26.60 at stop ₹903.76 (-2.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹23.77 at stop ₹424.65 (-10.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-02-14  GABRIEL     SELL ₹18.40 at stop ₹125.40 (+9.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-02-15  RAYMOND     SELL ₹29.80 at stop ₹679.35 (+14.0%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-02-15  SUZLON      SELL ₹30.83 at stop ₹9.79 (+16.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-02-21  ANDHRSUGAR  SELL ₹23.31 at stop ₹135.28 (-14.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-02-22  ABCAPITAL   SELL ₹23.19 at stop ₹103.58 (-16.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-02-24  CCL         SELL ₹23.71 at stop ₹441.75 (-12.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-03-04  SFL         RAISE STOP ₹2,922.75 → ₹2,993.45 (new box ₹3,151.00–₹3,300.00 sealed)
2022-03-07  CGCL        BUY ₹24.75 at ₹600.00 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 3.19×, ladder rising; stop ₹536.75; charges ₹0.03)
2022-03-07  GTLINFRA    BUY ₹24.67 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.03)
2022-03-07  SRHHYPOLTD  BUY ₹24.60 at ₹408.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 3.20×, ladder rising; stop ₹312.70; charges ₹0.03)
2022-03-14  BIRLACABLE  BUY ₹24.97 at ₹162.10 (fresh Friday signal — BUY: 3.06× weekly, month 5.33×, ladder rising; stop ₹128.30; charges ₹0.03)
2022-03-14  ICICIGOLD   BUY ₹24.99 at ₹46.20 (fresh Friday signal — starved 5×, front of the queue — BUY: 4.11× weekly, month 3.73×, ladder rising; stop ₹41.50; charges ₹0.03)
2022-03-14  ZUARIGLOB   BUY ₹24.90 at ₹195.30 (fresh Friday signal — BUY: 2.01× weekly, month 1.59×, ladder rising; stop ₹152.52; charges ₹0.03)
2022-03-25  BIRLACABLE  RAISE STOP ₹128.30 → ₹145.40 (new box ₹153.05–₹172.80 sealed)
2022-03-25  SFL         RAISE STOP ₹2,993.45 → ₹3,072.06 (new box ₹3,233.75–₹3,457.50 sealed)
2022-04-01  SRHHYPOLTD  RAISE STOP ₹312.70 → ₹431.30 (new box ₹454.00–₹523.00 sealed)
2022-04-01  TAX         FY2022 settled: ₹11.94 paid (STCG ₹58.71 @20%, LTCG ₹1.59 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  INOXLEISUR  BUY ₹23.83 at ₹520.85 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 7.27× weekly, month 3.35×, ladder rising; stop ₹470.35; charges ₹0.03)
2022-04-04  VALIANTORG  BUY ₹23.78 at ₹1,010.90 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.69× weekly, month 2.82×, ladder rising; ₹7.83 fresh capital added; stop ₹784.63; charges ₹0.03)
2022-04-08  ZUARIGLOB   RAISE STOP ₹152.52 → ₹165.25 (new box ₹173.95–₹184.45 sealed)
2022-04-19  BIRLACABLE  SELL ₹22.35 at stop ₹145.40 (-10.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-04-22  GTLINFRA    RAISE STOP ₹1.39 → ₹1.41 (new box ₹1.50–₹1.80 sealed)
2022-04-22  SFL         RAISE STOP ₹3,072.06 → ₹3,519.94 (new box ₹3,705.20–₹4,055.00 sealed)
2022-04-25  TNPL        BUY ₹24.04 at ₹211.10 (fresh Friday signal — starved 6×, front of the queue — BUY: 3.06× weekly, month 4.07×, ladder rising; ₹1.69 fresh capital added; stop ₹176.75; charges ₹0.03)
2022-04-27  SFL         SELL ₹26.94 at stop ₹3,519.94 (+3.0%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-04-29  GTLINFRA    SELL ₹20.42 at stop ₹1.41 (-17.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-02  HUHTAMAKI   BUY ₹24.21 at ₹197.75 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.89× weekly, month 2.26×, ladder rising; ₹1.03 fresh capital added; stop ₹161.50; charges ₹0.03)
2022-05-02  RIIL        BUY ₹24.17 at ₹1,100.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 5.17× weekly, month 3.64×, ladder rising; stop ₹852.81; charges ₹0.03)
2022-05-05  SRHHYPOLTD  SELL ₹25.95 at stop ₹431.30 (+5.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-05-06  INOXLEISUR  SELL ₹21.47 at stop ₹470.35 (-9.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-06  TNPL        RAISE STOP ₹176.75 → ₹195.61 (new box ₹205.90–₹226.95 sealed)
2022-05-06  ZUARIGLOB   SELL ₹21.02 at stop ₹165.25 (-15.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-09  JKIL        BUY ₹22.79 at ₹229.70 (fresh Friday signal — starved 1×, front of the queue — BUY: 6.96× weekly, month 3.58×, ladder rising; stop ₹192.28; charges ₹0.03)
2022-05-09  MOL         BUY ₹22.82 at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹0.03)
2022-05-09  MRPL        BUY ₹22.70 at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹0.03)
2022-05-10  TNPL        SELL ₹22.23 at stop ₹195.61 (-7.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-11  MOL         SELL ₹19.93 at stop ₹113.62 (-12.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-11  VALIANTORG  SELL ₹18.42 at stop ₹784.63 (-22.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹21.73 at ₹220.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.03)
2022-05-20  JKIL        RAISE STOP ₹192.28 → ₹196.02 (new box ₹208.80–₹251.40 sealed)
2022-05-20  MRPL        RAISE STOP ₹58.41 → ₹60.81 (new box ₹66.30–₹84.60 sealed)
2022-05-20  RIIL        RAISE STOP ₹852.81 → ₹863.73 (new box ₹942.00–₹1,202.90 sealed)
2022-05-23  ACC         BUY ₹22.35 at ₹2,260.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹0.03)
2022-05-23  VADILALIND  BUY ₹22.30 at ₹1,805.00 (fresh Friday signal — BUY: 1.51× weekly, month 1.94×, ladder rising; ₹5.68 fresh capital added; stop ₹1,567.50; charges ₹0.03)
2022-05-26  HUHTAMAKI   SELL ₹19.73 at stop ₹161.50 (-18.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-26  RIIL        SELL ₹18.94 at stop ₹863.73 (-21.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-06-03  MRPL        RAISE STOP ₹60.81 → ₹69.61 (new box ₹75.65–₹95.80 sealed)
2022-06-06  SHANTIGEAR  BUY ₹22.12 at ₹238.05 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.57× weekly, month 2.31×, ladder rising; stop ₹179.53; charges ₹0.03)
2022-06-06  VBL         SELL ₹19.34 at stop ₹196.27 (-10.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-06-10  JKIL        RAISE STOP ₹196.02 → ₹233.94 (new box ₹246.25–₹264.60 sealed)
2022-06-20  APARINDS    BUY ₹21.58 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.03)
2022-06-24  VADILALIND  RAISE STOP ₹1,567.50 → ₹1,602.19 (new box ₹1,726.00–₹2,138.70 sealed)
2022-06-27  ELECON      BUY ₹22.74 at ₹136.70 (fresh Friday signal — BUY: 2.35× weekly, month 2.36×, ladder rising; ₹8.43 fresh capital added; stop ₹111.01; charges ₹0.03)
2022-07-01  APARINDS    RAISE STOP ₹706.80 → ₹844.03 (new box ₹891.30–₹1,048.85 sealed)
2022-07-06  MRPL        SELL ₹20.21 at stop ₹69.61 (-10.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-07-08  ELECON      RAISE STOP ₹111.01 → ₹120.65 (new box ₹127.00–₹144.95 sealed)
2022-07-08  VADILALIND  RAISE STOP ₹1,602.19 → ₹1,877.25 (new box ₹1,976.05–₹2,165.00 sealed)
2022-07-11  MARATHON    BUY ₹24.07 at ₹215.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.48× weekly, month 6.64×, ladder rising; ₹3.86 fresh capital added; stop ₹186.25; charges ₹0.03)
2022-07-15  ACC         RAISE STOP ₹1,994.10 → ₹2,030.06 (new box ₹2,136.90–₹2,201.10 sealed)
2022-07-22  ELECON      RAISE STOP ₹120.65 → ₹142.64 (new box ₹150.15–₹162.50 sealed)
2022-07-22  MARATHON    RAISE STOP ₹186.25 → ₹188.59 (new box ₹199.25–₹234.80 sealed)
2022-07-22  VADILALIND  RAISE STOP ₹1,877.25 → ₹1,924.70 (new box ₹2,026.00–₹2,220.00 sealed)
2022-07-29  JKIL        RAISE STOP ₹233.94 → ₹308.80 (new box ₹325.05–₹349.00 sealed)
2022-08-05  ACC         RAISE STOP ₹2,030.06 → ₹2,053.90 (new box ₹2,162.00–₹2,213.00 sealed)
2022-08-05  JKIL        SELL ₹30.57 at stop ₹308.80 (+34.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-08-08  WSTCSTPAPR  BUY ₹25.80 at ₹498.00 (fresh Friday signal — starved 5×, front of the queue — ACCUMULATE: 3.90× weekly, month 2.21×, ladder rising; stop ₹443.70; charges ₹0.03)
2022-08-12  ACC         RAISE STOP ₹2,053.90 → ₹2,085.11 (new box ₹2,194.85–₹2,262.60 sealed)
2022-08-12  ELECON      RAISE STOP ₹142.64 → ₹156.67 (new box ₹165.97–₹196.97 sealed)
2022-08-12  MARATHON    RAISE STOP ₹188.59 → ₹192.48 (new box ₹204.30–₹243.70 sealed)
2022-08-12  VADILALIND  RAISE STOP ₹1,924.70 → ₹2,151.75 (new box ₹2,265.00–₹2,450.00 sealed)
2022-08-19  APARINDS    RAISE STOP ₹844.03 → ₹1,095.35 (new box ₹1,153.00–₹1,287.95 sealed)
2022-08-19  WSTCSTPAPR  RAISE STOP ₹443.70 → ₹482.12 (new box ₹507.50–₹547.80 sealed)
2022-08-26  ACC         RAISE STOP ₹2,085.11 → ₹2,151.37 (new box ₹2,264.60–₹2,367.75 sealed)
2022-08-29  ICICIGOLD   SELL ₹22.40 at stop ₹41.50 (-10.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-09-02  SHANTIGEAR  RAISE STOP ₹179.53 → ₹253.27 (new box ₹266.60–₹289.50 sealed)
2022-09-02  VADILALIND  RAISE STOP ₹2,151.75 → ₹2,270.26 (new box ₹2,389.75–₹2,648.00 sealed)
2022-09-05  TDPOWERSYS  BUY ₹27.79 at ₹120.00 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 2.31× weekly, month 1.78×, ladder rising; ₹0.62 fresh capital added; stop ₹94.46; charges ₹0.03)
2022-09-09  APARINDS    RAISE STOP ₹1,095.35 → ₹1,108.54 (new box ₹1,180.00–₹1,418.20 sealed)
2022-09-16  MARATHON    RAISE STOP ₹192.48 → ₹232.80 (new box ₹245.05–₹275.00 sealed)
2022-09-16  SHANTIGEAR  RAISE STOP ₹253.27 → ₹289.75 (new box ₹305.00–₹338.00 sealed)
2022-09-16  WSTCSTPAPR  RAISE STOP ₹482.12 → ₹533.28 (new box ₹561.35–₹650.00 sealed)
2022-09-19  MARATHON    SELL ₹26.01 at stop ₹232.80 (+8.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-09-22  WSTCSTPAPR  SELL ₹27.57 at stop ₹533.28 (+7.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-09-26  DAAWAT      BUY ₹27.13 at ₹113.35 (fresh Friday signal — starved 7×, front of the queue — BUY: 2.27× weekly, month 2.59×, ladder rising; stop ₹95.33; charges ₹0.03)
2022-09-26  JAICORPLTD  BUY ₹27.01 at ₹195.20 (fresh Friday signal — starved 6×, front of the queue — BUY: 2.80× weekly, month 3.10×, ladder rising; ₹0.56 fresh capital added; stop ₹148.34; charges ₹0.03)
2022-09-30  ACC         RAISE STOP ₹2,151.37 → ₹2,171.53 (new box ₹2,313.10–₹2,785.00 sealed)
2022-09-30  DAAWAT      RAISE STOP ₹95.33 → ₹101.08 (new box ₹106.40–₹117.70 sealed)
2022-09-30  JAICORPLTD  RAISE STOP ₹148.34 → ₹165.39 (new box ₹174.10–₹201.00 sealed)
2022-09-30  TDPOWERSYS  RAISE STOP ₹94.46 → ₹103.50 (new box ₹111.22–₹136.96 sealed)
2022-09-30  VADILALIND  RAISE STOP ₹2,270.26 → ₹2,295.06 (new box ₹2,425.20–₹2,859.00 sealed)
2022-10-07  SHANTIGEAR  RAISE STOP ₹289.75 → ₹301.39 (new box ₹317.25–₹348.00 sealed)
2022-10-14  DAAWAT      RAISE STOP ₹101.08 → ₹107.16 (new box ₹112.80–₹125.00 sealed)
2022-10-14  SHANTIGEAR  RAISE STOP ₹301.39 → ₹325.04 (new box ₹342.15–₹370.95 sealed)
2022-10-20  VADILALIND  SELL ₹28.29 at stop ₹2,295.06 (+27.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-10-21  APARINDS    RAISE STOP ₹1,108.54 → ₹1,277.75 (new box ₹1,345.00–₹1,513.95 sealed)
2022-10-24  ANANTRAJ    BUY ₹28.15 at ₹107.65 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.19× weekly, month 3.13×, ladder rising; stop ₹92.72; charges ₹0.03)
2022-10-28  APARINDS    RAISE STOP ₹1,277.75 → ₹1,358.50 (new box ₹1,430.00–₹1,557.00 sealed)
2022-11-03  APARINDS    SELL ₹30.78 at stop ₹1,358.50 (+43.0%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-11-03  JAICORPLTD  SELL ₹22.83 at stop ₹165.39 (-15.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-11-04  ANANTRAJ    RAISE STOP ₹92.72 → ₹99.75 (new box ₹105.00–₹110.90 sealed)
2022-11-04  ELECON      RAISE STOP ₹156.67 → ₹164.33 (new box ₹172.97–₹189.50 sealed)
2022-11-07  GANECOS     BUY ₹28.56 at ₹857.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 3.60× weekly, month 1.88×, ladder rising; ₹3.25 fresh capital added; stop ₹717.11; charges ₹0.03)
2022-11-07  WESTLIFE    BUY ₹28.46 at ₹763.50 (fresh Friday signal — starved 4×, front of the queue — ACCUMULATE: 2.22× weekly, month 1.72×, ladder rising; stop ₹671.22; charges ₹0.03)
2022-11-09  TDPOWERSYS  SELL ₹23.91 at stop ₹103.50 (-13.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-11-11  CGCL        RAISE STOP ₹536.75 → ₹699.20 (new box ₹736.00–₹773.60 sealed)
2022-11-11  DAAWAT      RAISE STOP ₹107.16 → ₹109.13 (new box ₹115.30–₹135.85 sealed)
2022-11-14  RPGLIFE     BUY ₹28.41 at ₹960.80 (fresh Friday signal — starved 6×, front of the queue — BUY: 1.97× weekly, month 2.37×, ladder rising; ₹4.50 fresh capital added; stop ₹774.25; charges ₹0.03)
2022-11-18  ACC         RAISE STOP ₹2,171.53 → ₹2,259.81 (new box ₹2,378.75–₹2,514.95 sealed)
2022-11-18  ELECON      RAISE STOP ₹164.33 → ₹202.49 (new box ₹213.15–₹229.40 sealed)
2022-11-18  GANECOS     RAISE STOP ₹717.11 → ₹771.40 (new box ₹812.00–₹859.00 sealed)
2022-11-18  RPGLIFE     RAISE STOP ₹774.25 → ₹816.00 (new box ₹858.95–₹905.00 sealed)
2022-11-18  SHANTIGEAR  RAISE STOP ₹325.04 → ₹345.56 (new box ₹363.75–₹399.20 sealed)
2022-11-18  WESTLIFE    RAISE STOP ₹671.22 → ₹708.51 (new box ₹745.80–₹811.85 sealed)
2022-11-23  ANANTRAJ    SELL ₹26.03 at stop ₹99.75 (-7.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-11-25  RPGLIFE     RAISE STOP ₹816.00 → ₹841.65 (new box ₹885.95–₹1,012.75 sealed)
2022-11-28  CENTRALBK   BUY ₹28.40 at ₹25.70 (fresh Friday signal — starved 5×, front of the queue — BUY: 4.21× weekly, month 4.84×, ladder rising; ₹2.37 fresh capital added; stop ₹20.95; charges ₹0.03)
2022-12-09  GANECOS     RAISE STOP ₹771.40 → ₹837.90 (new box ₹882.00–₹930.00 sealed)
2022-12-16  ACC         RAISE STOP ₹2,259.81 → ₹2,465.16 (new box ₹2,594.90–₹2,656.85 sealed)
2022-12-20  RPGLIFE     SELL ₹24.83 at stop ₹841.65 (-12.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-12-21  ELECON      SELL ₹33.61 at stop ₹202.49 (+48.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹32.04 at stop ₹345.56 (+45.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹24.33 at stop ₹2,465.16 (+9.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-12-23  DAAWAT      SELL ₹26.06 at stop ₹109.13 (-3.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2022-12-30  CENTRALBK   RAISE STOP ₹20.95 → ₹23.99 (new box ₹28.10–₹41.80 sealed)
2023-01-02  BAJAJHIND   BUY ₹28.65 at ₹17.20 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 1.76× weekly, month 4.56×, ladder rising; stop ₹13.98; charges ₹0.03)
2023-01-02  GANECOS     SELL ₹27.86 at stop ₹837.90 (-2.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-01-02  GICRE       BUY ₹28.65 at ₹179.20 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.54× weekly, month 11.18×, ladder rising; stop ₹137.57; charges ₹0.03)
2023-01-02  GSFC        BUY ₹28.93 at ₹140.70 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.14× weekly, month 1.67×, ladder rising; stop ₹111.58; charges ₹0.03)
2023-01-02  JINDALSAW   BUY ₹28.95 at ₹51.98 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.95× weekly, month 2.35×, ladder rising; ₹3.09 fresh capital added; stop ₹42.55; charges ₹0.03)
2023-01-02  JSL         BUY ₹28.78 at ₹241.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.29× weekly, month 2.13×, ladder rising; stop ₹192.61; charges ₹0.03)
2023-01-06  CGCL        RAISE STOP ₹699.20 → ₹704.95 (new box ₹742.05–₹807.95 sealed)
2023-01-09  SUNDRMFAST  BUY ₹28.72 at ₹992.00 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 3.18× weekly, month 1.85×, ladder rising; ₹0.86 fresh capital added; stop ₹844.60; charges ₹0.03)
2023-01-13  GICRE       RAISE STOP ₹137.57 → ₹167.72 (new box ₹176.55–₹204.00 sealed)
2023-01-13  JSL         RAISE STOP ₹192.61 → ₹218.83 (new box ₹230.35–₹255.00 sealed)
2023-01-16  WESTLIFE    SELL ₹26.35 at stop ₹708.51 (-7.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-01-20  JINDALSAW   RAISE STOP ₹42.55 → ₹51.77 (new box ₹54.50–₹58.38 sealed)
2023-01-23  SUNFLAG     BUY ₹28.36 at ₹131.50 (fresh Friday signal — starved 5×, front of the queue — BUY: 2.91× weekly, month 2.81×, ladder rising; ₹2.01 fresh capital added; stop ₹105.97; charges ₹0.03)
2023-01-30  BAJAJHIND   SELL ₹23.24 at stop ₹13.98 (-18.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-02-01  GICRE       SELL ₹26.75 at stop ₹167.72 (-6.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-02-03  SUNFLAG     RAISE STOP ₹105.97 → ₹121.69 (new box ₹128.10–₹139.40 sealed)
2023-02-06  MAHINDCIE   BUY ₹28.25 at ₹395.20 (fresh Friday signal — starved 8×, front of the queue — BUY: 1.59× weekly, month 2.05×, ladder rising; stop ₹328.94; charges ₹0.03)
2023-02-06  ORIENTPPR   BUY ₹28.26 at ₹45.70 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 1.64× weekly, month 2.07×, ladder rising; ₹6.52 fresh capital added; stop ₹39.90; charges ₹0.03)
2023-02-10  CENTRALBK   RAISE STOP ₹23.99 → ₹25.51 (new box ₹26.85–₹28.30 sealed)
2023-02-10  MAHINDCIE   RAISE STOP ₹328.94 → ₹368.65 (new box ₹388.05–₹418.20 sealed)
2023-02-13  ORIENTPPR   SELL ₹24.62 at stop ₹39.90 (-12.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-02-17  CGCL        SELL ₹29.01 at stop ₹704.95 (+17.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-02-17  SUNFLAG     RAISE STOP ₹121.69 → ₹129.20 (new box ₹136.00–₹149.00 sealed)
2023-02-20  ATULAUTO    BUY ₹28.88 at ₹387.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.96× weekly, month 4.05×, ladder rising; ₹4.23 fresh capital added; stop ₹335.92; charges ₹0.03)
2023-02-20  CIGNITITEC  BUY ₹28.98 at ₹731.95 (fresh Friday signal — starved 5×, front of the queue — BUY: 2.05× weekly, month 1.77×, ladder rising; stop ₹568.10; charges ₹0.03)
2023-02-22  CENTRALBK   SELL ₹28.12 at stop ₹25.51 (-0.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-02-24  JSL         RAISE STOP ₹218.83 → ₹235.03 (new box ₹247.40–₹268.95 sealed)
2023-02-24  SUNDRMFAST  RAISE STOP ₹844.60 → ₹926.11 (new box ₹974.85–₹1,033.80 sealed)
2023-02-27  SONATSOFTW  BUY ₹28.47 at ₹360.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 9.70× weekly, month 3.45×, ladder rising; ₹0.35 fresh capital added; stop ₹282.62; charges ₹0.03)
2023-02-27  SUNFLAG     SELL ₹27.81 at stop ₹129.20 (-1.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-03-03  CIGNITITEC  RAISE STOP ₹568.10 → ₹659.30 (new box ₹694.00–₹733.70 sealed)
2023-03-03  JINDALSAW   RAISE STOP ₹51.77 → ₹67.92 (new box ₹71.50–₹79.22 sealed)
2023-03-03  MAHINDCIE   RAISE STOP ₹368.65 → ₹391.69 (new box ₹412.30–₹462.40 sealed)
2023-03-03  SONATSOFTW  RAISE STOP ₹282.62 → ₹325.85 (new box ₹343.00–₹376.50 sealed)
2023-03-06  WONDERLA    BUY ₹30.12 at ₹456.00 (fresh Friday signal — starved 4×, front of the queue — BUY: 4.06× weekly, month 2.13×, ladder rising; ₹2.31 fresh capital added; stop ₹384.27; charges ₹0.04)
2023-03-10  MAHINDCIE   SELL ₹27.93 at stop ₹391.69 (-0.9%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-03-13  ATULAUTO    SELL ₹24.95 at stop ₹335.92 (-13.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-03-13  VSSL        BUY ₹29.74 at ₹368.90 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.79× weekly, month 1.86×, ladder rising; ₹1.81 fresh capital added; stop ₹286.40; charges ₹0.04)
2023-03-17  CIGNITITEC  RAISE STOP ₹659.30 → ₹705.14 (new box ₹742.25–₹797.45 sealed)
2023-03-17  SONATSOFTW  RAISE STOP ₹325.85 → ₹357.20 (new box ₹376.00–₹416.32 sealed)
2023-03-20  ANURAS      BUY ₹29.13 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.57×, ladder rising; ₹4.18 fresh capital added; stop ₹691.46; charges ₹0.03)
2023-03-24  SONATSOFTW  RAISE STOP ₹357.20 → ₹371.45 (new box ₹391.00–₹427.80 sealed)
2023-03-24  VSSL        RAISE STOP ₹286.40 → ₹324.52 (new box ₹341.60–₹380.35 sealed)
2023-03-27  JINDALSAW   SELL ₹37.75 at stop ₹67.92 (+30.7%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-03-27  WONDERLA    SELL ₹25.32 at stop ₹384.27 (-15.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-03-29  CIGNITITEC  SELL ₹27.86 at stop ₹705.14 (-3.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹29.31 at stop ₹371.45 (+3.2%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-04-03  CPSEETF     BUY ₹29.14 at ₹40.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.80× weekly, month 1.84×, ladder rising; stop ₹36.42; charges ₹0.03)
2023-04-03  HAL         BUY ₹29.20 at ₹1,380.00 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.03)
2023-04-03  TAX         FY2023 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹12.17 / LT ₹0.00)
2023-04-06  JSL         RAISE STOP ₹235.03 → ₹256.98 (new box ₹270.50–₹299.80 sealed)
2023-04-10  KSB         BUY ₹29.73 at ₹451.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.21× weekly, month 2.22×, ladder rising; stop ₹372.21; charges ₹0.04)
2023-04-10  SETFGOLD    BUY ₹29.73 at ₹52.60 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.69× weekly, month 2.06×, ladder rising; stop ₹48.56; charges ₹0.04)
2023-04-13  JSL         SELL ₹30.62 at stop ₹256.98 (+6.6%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-04-13  SETFGOLD    RAISE STOP ₹48.56 → ₹49.74 (new box ₹52.36–₹53.75 sealed)
2023-04-17  SAKSOFT     BUY ₹30.08 at ₹159.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.60× weekly, month 1.54×, ladder rising; stop ₹131.96; charges ₹0.04)
2023-04-21  SAKSOFT     RAISE STOP ₹131.96 → ₹145.68 (new box ₹153.35–₹166.65 sealed)
2023-04-21  SUNDRMFAST  RAISE STOP ₹926.11 → ₹932.66 (new box ₹981.75–₹1,006.05 sealed)
2023-04-28  ANURAS      RAISE STOP ₹691.46 → ₹946.20 (new box ₹996.00–₹1,069.75 sealed)
2023-04-28  CPSEETF     RAISE STOP ₹36.42 → ₹38.64 (new box ₹40.67–₹41.49 sealed)
2023-04-28  GSFC        RAISE STOP ₹111.58 → ₹116.04 (new box ₹122.15–₹130.60 sealed)
2023-04-28  KSB         RAISE STOP ₹372.21 → ₹407.74 (new box ₹429.20–₹459.97 sealed)
2023-04-28  SUNDRMFAST  RAISE STOP ₹932.66 → ₹944.82 (new box ₹994.55–₹1,070.00 sealed)
2023-05-12  ANURAS      RAISE STOP ₹946.20 → ₹1,007.67 (new box ₹1,060.70–₹1,224.20 sealed)
2023-05-12  HAL         RAISE STOP ₹1,171.71 → ₹1,370.80 (new box ₹1,442.95–₹1,525.00 sealed)
2023-05-12  SAKSOFT     RAISE STOP ₹145.68 → ₹154.78 (new box ₹175.60–₹245.00 sealed)
2023-05-19  GSFC        RAISE STOP ₹116.04 → ₹155.85 (new box ₹164.05–₹179.70 sealed)
2023-05-26  SUNDRMFAST  RAISE STOP ₹944.82 → ₹996.55 (new box ₹1,049.00–₹1,097.40 sealed)
2023-05-26  VSSL        SELL ₹26.10 at stop ₹324.52 (-12.0%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-05-29  GSFC        SELL ₹31.97 at stop ₹155.85 (+10.8%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-05-29  LAXMIMACH   BUY ₹32.17 at ₹11,604.35 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.50× weekly, month 1.95×, ladder rising; ₹3.09 fresh capital added; stop ₹10,279.00; charges ₹0.04)
2023-06-02  CPSEETF     RAISE STOP ₹38.64 → ₹39.05 (new box ₹41.10–₹43.50 sealed)
2023-06-02  HAL         RAISE STOP ₹1,370.80 → ₹1,415.36 (new box ₹1,489.85–₹1,584.40 sealed)
2023-06-05  TV18BRDCST  BUY ₹33.31 at ₹40.25 (fresh Friday signal — starved 5×, front of the queue — BUY: 3.05× weekly, month 1.59×, ladder rising; ₹1.35 fresh capital added; stop ₹31.78; charges ₹0.04)
2023-06-09  LAXMIMACH   RAISE STOP ₹10,279.00 → ₹10,688.45 (new box ₹11,251.00–₹11,776.00 sealed)
2023-06-09  SUNDRMFAST  RAISE STOP ₹996.55 → ₹1,055.40 (new box ₹1,110.95–₹1,172.00 sealed)
2023-06-16  HAL         RAISE STOP ₹1,415.36 → ₹1,723.32 (new box ₹1,814.03–₹1,900.00 sealed)
2023-06-16  SAKSOFT     RAISE STOP ₹154.78 → ₹243.25 (new box ₹256.05–₹294.80 sealed)
2023-06-16  TV18BRDCST  RAISE STOP ₹31.78 → ₹34.87 (new box ₹36.70–₹40.75 sealed)
2023-06-23  SAKSOFT     RAISE STOP ₹243.25 → ₹284.57 (new box ₹299.55–₹342.85 sealed)
2023-06-30  SUNDRMFAST  RAISE STOP ₹1,055.40 → ₹1,091.69 (new box ₹1,149.15–₹1,212.00 sealed)
2023-07-03  ANURAS      SELL ₹38.75 at stop ₹1,007.67 (+33.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-07-07  CPSEETF     RAISE STOP ₹39.05 → ₹40.77 (new box ₹42.92–₹44.24 sealed)
2023-07-07  LAXMIMACH   RAISE STOP ₹10,688.45 → ₹11,917.75 (new box ₹12,545.00–₹13,255.35 sealed)
2023-07-07  TV18BRDCST  RAISE STOP ₹34.87 → ₹35.20 (new box ₹37.05–₹42.45 sealed)
2023-07-10  SJVN        BUY ₹35.18 at ₹48.00 (fresh Friday signal — starved 5×, front of the queue — BUY: 3.63× weekly, month 3.61×, ladder rising; stop ₹38.24; charges ₹0.04)
2023-07-12  KSB         SELL ₹26.82 at stop ₹407.74 (-9.6%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-07-14  SAKSOFT     RAISE STOP ₹284.57 → ₹291.27 (new box ₹306.60–₹339.95 sealed)
2023-07-17  SPARC       BUY ₹35.45 at ₹225.30 (fresh Friday signal — starved 5×, front of the queue — BUY: 3.18× weekly, month 2.72×, ladder rising; ₹5.06 fresh capital added; stop ₹191.52; charges ₹0.04)
2023-07-21  CPSEETF     RAISE STOP ₹40.77 → ₹41.97 (new box ₹44.18–₹46.00 sealed)
2023-07-21  LAXMIMACH   RAISE STOP ₹11,917.75 → ₹12,737.60 (new box ₹13,408.00–₹13,923.00 sealed)
2023-07-21  SJVN        RAISE STOP ₹38.24 → ₹42.94 (new box ₹45.20–₹49.30 sealed)
2023-07-21  SUNDRMFAST  RAISE STOP ₹1,091.69 → ₹1,155.25 (new box ₹1,216.05–₹1,266.25 sealed)
2023-07-28  LAXMIMACH   RAISE STOP ₹12,737.60 → ₹12,863.00 (new box ₹13,540.00–₹14,441.50 sealed)
2023-07-28  SPARC       RAISE STOP ₹191.52 → ₹207.34 (new box ₹218.25–₹237.00 sealed)
2023-07-31  CPSEETF     SELL ₹30.51 at stop ₹41.97 (+4.9%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-08-04  TV18BRDCST  RAISE STOP ₹35.20 → ₹37.29 (new box ₹39.25–₹44.30 sealed)
2023-08-07  MANINFRA    BUY ₹36.08 at ₹145.75 (fresh Friday signal — starved 8×, front of the queue — BUY: 2.67× weekly, month 3.16×, ladder rising; ₹5.57 fresh capital added; stop ₹113.05; charges ₹0.04)
2023-08-11  HAL         RAISE STOP ₹1,723.32 → ₹1,758.24 (new box ₹1,850.78–₹1,999.45 sealed)
2023-08-11  SJVN        RAISE STOP ₹42.94 → ₹51.35 (new box ₹54.05–₹62.70 sealed)
2023-08-11  SPARC       RAISE STOP ₹207.34 → ₹212.32 (new box ₹223.50–₹246.75 sealed)
2023-08-17  LAXMIMACH   SELL ₹35.58 at stop ₹12,863.00 (+10.8%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-08-21  BOMDYEING   BUY ₹37.39 at ₹127.40 (fresh Friday signal — starved 6×, front of the queue — BUY: 1.77× weekly, month 2.13×, ladder rising; ₹1.81 fresh capital added; stop ₹102.74; charges ₹0.04)
2023-09-01  BOMDYEING   RAISE STOP ₹102.74 → ₹125.21 (new box ₹131.80–₹143.30 sealed)
2023-09-01  HAL         RAISE STOP ₹1,758.24 → ₹1,840.70 (new box ₹1,937.58–₹2,067.50 sealed)
2023-09-01  MANINFRA    RAISE STOP ₹113.05 → ₹125.80 (new box ₹132.65–₹155.50 sealed)
2023-09-01  SAKSOFT     RAISE STOP ₹291.27 → ₹295.74 (new box ₹311.30–₹327.00 sealed)
2023-09-01  TV18BRDCST  RAISE STOP ₹37.29 → ₹43.08 (new box ₹45.35–₹49.80 sealed)
2023-09-15  SAKSOFT     RAISE STOP ₹295.74 → ₹296.54 (new box ₹312.15–₹354.45 sealed)
2023-09-15  SJVN        RAISE STOP ₹51.35 → ₹58.28 (new box ₹61.35–₹67.35 sealed)
2023-09-22  SJVN        RAISE STOP ₹58.28 → ₹66.03 (new box ₹70.00–₹83.25 sealed)
2023-09-28  TV18BRDCST  SELL ₹35.58 at stop ₹43.08 (+7.0%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-10-03  HATHWAY     BUY ₹39.39 at ₹20.00 (fresh Friday signal — starved 5×, front of the queue — ACCUMULATE: 2.57× weekly, month 5.67×, ladder rising; ₹3.81 fresh capital added; stop ₹18.10; charges ₹0.05)
2023-10-03  SETFGOLD    SELL ₹28.05 at stop ₹49.74 (-5.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2023-10-09  DEN         BUY ₹39.06 at ₹50.90 (fresh Friday signal — starved 4×, front of the queue — ACCUMULATE: 1.96× weekly, month 5.99×, ladder rising; ₹11.01 fresh capital added; stop ₹46.98; charges ₹0.05)
2023-10-13  MANINFRA    RAISE STOP ₹125.80 → ₹140.65 (new box ₹148.05–₹163.80 sealed)
2023-10-23  DEN         SELL ₹35.97 at stop ₹46.98 (-7.7%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-10-23  HATHWAY     SELL ₹35.57 at stop ₹18.10 (-9.5%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-10-23  SJVN        SELL ₹48.29 at stop ₹66.03 (+37.6%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹38.86 at stop ₹1,840.70 (+33.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-10-26  MANINFRA    SELL ₹34.74 at stop ₹140.65 (-3.5%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-10-30  ANGELONE    BUY ₹40.15 at ₹253.50 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.84× weekly, month 2.75×, ladder rising; stop ₹194.37; charges ₹0.05)
2023-10-30  SHAREINDIA  BUY ₹40.19 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.05)
2023-11-03  BOMDYEING   RAISE STOP ₹125.21 → ₹129.06 (new box ₹140.10–₹176.90 sealed)
2023-11-03  SAKSOFT     RAISE STOP ₹296.54 → ₹305.02 (new box ₹327.45–₹402.20 sealed)
2023-11-06  GULFOILLUB  BUY ₹40.99 at ₹622.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.90× weekly, month 3.03×, ladder rising; stop ₹503.55; charges ₹0.05)
2023-11-06  HITECH      BUY ₹40.89 at ₹102.75 (fresh Friday signal — ACCUMULATE: 2.79× weekly, month 5.13×, ladder rising; stop ₹86.54; charges ₹0.05)
2023-11-10  ANGELONE    RAISE STOP ₹194.37 → ₹236.87 (new box ₹249.34–₹289.79 sealed)
2023-11-10  SPARC       RAISE STOP ₹212.32 → ₹222.78 (new box ₹234.50–₹247.15 sealed)
2023-11-13  APOLLO      BUY ₹42.19 at ₹122.90 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.90× weekly, month 3.87×, ladder rising; ₹10.98 fresh capital added; stop ₹88.83; charges ₹0.05)
2023-11-17  APOLLO      RAISE STOP ₹88.83 → ₹105.78 (new box ₹111.35–₹123.80 sealed)
2023-11-17  GULFOILLUB  RAISE STOP ₹503.55 → ₹570.00 (new box ₹600.00–₹638.40 sealed)
2023-11-17  SHAREINDIA  RAISE STOP ₹261.25 → ₹280.63 (new box ₹295.40–₹325.89 sealed)
2023-11-24  ANGELONE    RAISE STOP ₹236.87 → ₹274.55 (new box ₹289.00–₹309.00 sealed)
2023-11-24  SHAREINDIA  RAISE STOP ₹280.63 → ₹321.67 (new box ₹338.60–₹369.40 sealed)
2023-11-24  SPARC       RAISE STOP ₹222.78 → ₹232.18 (new box ₹244.40–₹267.30 sealed)
2023-12-08  SPARC       RAISE STOP ₹232.18 → ₹256.55 (new box ₹270.05–₹286.70 sealed)
2023-12-15  ANGELONE    RAISE STOP ₹274.55 → ₹279.31 (new box ₹294.01–₹324.50 sealed)
2023-12-15  GULFOILLUB  RAISE STOP ₹570.00 → ₹608.10 (new box ₹640.10–₹709.80 sealed)
2023-12-15  HITECH      RAISE STOP ₹86.54 → ₹96.42 (new box ₹101.50–₹112.00 sealed)
2023-12-15  SHAREINDIA  RAISE STOP ₹321.67 → ₹328.89 (new box ₹346.20–₹360.34 sealed)
2023-12-20  SPARC       SELL ₹40.28 at stop ₹256.55 (+13.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2023-12-26  IBREALEST   BUY ₹45.05 at ₹89.40 (fresh Friday signal — starved 4×, front of the queue — BUY: 2.36× weekly, month 2.30×, ladder rising; ₹4.77 fresh capital added; stop ₹80.56; charges ₹0.05)
2023-12-29  ANGELONE    RAISE STOP ₹279.31 → ₹296.88 (new box ₹312.50–₹338.50 sealed)
2023-12-29  SHAREINDIA  RAISE STOP ₹328.89 → ₹330.37 (new box ₹347.76–₹372.60 sealed)
2024-01-05  GULFOILLUB  RAISE STOP ₹608.10 → ₹675.40 (new box ₹710.95–₹749.80 sealed)
2024-01-05  HITECH      RAISE STOP ₹96.42 → ₹105.54 (new box ₹111.10–₹118.15 sealed)
2024-01-23  ANGELONE    SELL ₹46.92 at stop ₹296.88 (+17.1%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-01-25  HITECH      RAISE STOP ₹105.54 → ₹126.73 (new box ₹133.40–₹153.90 sealed)
2024-01-25  IBREALEST   RAISE STOP ₹80.56 → ₹87.97 (new box ₹92.60–₹104.55 sealed)
2024-01-29  SPIC        BUY ₹48.21 at ₹87.00 (fresh Friday signal — starved 6×, front of the queue — ACCUMULATE: 2.04× weekly, month 2.40×, ladder rising; ₹1.29 fresh capital added; stop ₹76.38; charges ₹0.06)
2024-02-09  SUNDRMFAST  SELL ₹33.38 at stop ₹1,155.25 (+16.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2024-02-12  FDC         BUY ₹46.87 at ₹449.00 (fresh Friday signal — starved 7×, front of the queue — BUY: 2.31× weekly, month 1.83×, ladder rising; ₹13.50 fresh capital added; stop ₹381.90; charges ₹0.06)
2024-02-12  SAKSOFT     SELL ₹57.58 at stop ₹305.02 (+91.8%, charges ₹0.06) — the cash goes back to work at the next Friday screen
2024-02-16  FDC         RAISE STOP ₹381.90 → ₹403.80 (new box ₹425.05–₹471.95 sealed)
2024-02-16  GULFOILLUB  RAISE STOP ₹675.40 → ₹771.40 (new box ₹812.00–₹935.00 sealed)
2024-02-16  SHAREINDIA  RAISE STOP ₹330.37 → ₹357.20 (new box ₹376.00–₹391.23 sealed)
2024-02-19  AEGISCHEM   BUY ₹51.27 at ₹436.55 (fresh Friday signal — starved 5×, front of the queue — BUY: 4.51× weekly, month 2.11×, ladder rising; stop ₹343.05; charges ₹0.06)
2024-02-23  IBREALEST   RAISE STOP ₹87.97 → ₹102.92 (new box ₹108.45–₹126.90 sealed)
2024-03-01  AEGISCHEM   RAISE STOP ₹343.05 → ₹394.30 (new box ₹415.05–₹471.90 sealed)
2024-03-01  BOMDYEING   RAISE STOP ₹129.06 → ₹164.59 (new box ₹173.25–₹183.90 sealed)
2024-03-06  IBREALEST   SELL ₹51.75 at stop ₹102.92 (+15.1%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹47.75 at stop ₹357.20 (+19.1%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-03-07  FDC         RAISE STOP ₹403.80 → ₹412.30 (new box ₹434.00–₹487.70 sealed)
2024-03-07  GULFOILLUB  RAISE STOP ₹771.40 → ₹941.07 (new box ₹990.60–₹1,075.00 sealed)
2024-03-11  BOMDYEING   SELL ₹48.20 at stop ₹164.59 (+29.2%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-03-11  BOSCHLTD    BUY ₹47.16 at ₹29,819.95 (fresh Friday signal — BUY: 1.81× weekly, month 2.03×, ladder rising; stop ₹26,525.90; charges ₹0.06)
2024-03-11  HITECH      SELL ₹50.32 at stop ₹126.73 (+23.3%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-03-12  GULFOILLUB  SELL ₹61.87 at stop ₹941.07 (+51.3%, charges ₹0.06) — the cash goes back to work at the next Friday screen
2024-03-12  SPIC        SELL ₹42.23 at stop ₹76.38 (-12.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-03-13  AEGISCHEM   SELL ₹46.21 at stop ₹394.30 (-9.7%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-03-18  EMUDHRA     BUY ₹46.88 at ₹583.90 (fresh Friday signal — BUY: 1.54× weekly, month 3.10×, ladder rising; stop ₹529.77; charges ₹0.06)
2024-03-18  FORCEMOT    BUY ₹46.60 at ₹6,567.70 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.06)
2024-03-18  INDIGO      BUY ₹46.81 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.06)
2024-03-18  SMSPHARMA   BUY ₹46.66 at ₹189.20 (fresh Friday signal — starved 7×, front of the queue — ACCUMULATE: 1.84× weekly, month 7.08×, ladder rising; stop ₹146.81; charges ₹0.06)
2024-03-22  BOSCHLTD    RAISE STOP ₹26,525.90 → ₹26,710.20 (new box ₹28,116.00–₹30,468.05 sealed)
2024-03-26  APOLLO      SELL ₹36.23 at stop ₹105.78 (-13.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-03-26  SKIPPER     BUY ₹47.35 at ₹300.20 (fresh Friday signal — BUY: 2.14× weekly, month 2.22×, ladder rising; stop ₹297.82; charges ₹0.06)
2024-04-01  DMART       BUY ₹46.38 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; ₹2.88 fresh capital added; stop ₹3,695.50; charges ₹0.05)
2024-04-01  SHRIRAMFIN  BUY ₹46.27 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.05)
2024-04-01  TAX         FY2024 settled: ₹19.64 paid (STCG ₹95.25 @20%, LTCG ₹4.72 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-05  BOSCHLTD    RAISE STOP ₹26,710.20 → ₹28,244.40 (new box ₹29,730.95–₹31,150.00 sealed)
2024-04-12  EMUDHRA     RAISE STOP ₹529.77 → ₹627.45 (new box ₹675.00–₹833.50 sealed)
2024-04-12  INDIGO      RAISE STOP ₹2,834.99 → ₹3,287.00 (new box ₹3,460.00–₹3,645.00 sealed)
2024-04-19  SMSPHARMA   RAISE STOP ₹146.81 → ₹181.36 (new box ₹190.90–₹218.00 sealed)
2024-04-26  FDC         RAISE STOP ₹412.30 → ₹419.95 (new box ₹442.05–₹460.00 sealed)
2024-04-26  FORCEMOT    RAISE STOP ₹5,500.61 → ₹7,483.47 (new box ₹7,893.85–₹9,261.80 sealed)
2024-04-26  SHRIRAMFIN  RAISE STOP ₹424.70 → ₹441.77 (new box ₹465.02–₹521.13 sealed)
2024-05-10  INDIGO      RAISE STOP ₹3,287.00 → ₹3,719.77 (new box ₹3,915.55–₹4,179.10 sealed)
2024-05-17  DMART       RAISE STOP ₹3,695.50 → ₹4,322.83 (new box ₹4,550.35–₹4,895.60 sealed)
2024-05-17  FORCEMOT    RAISE STOP ₹7,483.47 → ₹8,083.64 (new box ₹8,590.00–₹10,277.85 sealed)
2024-05-24  BOSCHLTD    RAISE STOP ₹28,244.40 → ₹29,015.09 (new box ₹30,542.20–₹32,100.00 sealed)
2024-05-28  FORCEMOT    SELL ₹57.23 at stop ₹8,083.64 (+23.1%, charges ₹0.06) — the cash goes back to work at the next Friday screen
2024-05-28  SKIPPER     SELL ₹46.87 at stop ₹297.82 (-0.8%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-05-31  DMART       SELL ₹43.77 at stop ₹4,322.83 (-5.4%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-06-03  BLUESTARCO  BUY ₹48.14 at ₹1,625.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.66× weekly, month 1.71×, ladder rising; stop ₹1,398.88; charges ₹0.06)
2024-06-03  THERMAX     BUY ₹48.13 at ₹5,640.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.06)
2024-06-03  WABAG       BUY ₹48.06 at ₹1,029.05 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.54× weekly, month 1.52×, ladder rising; stop ₹801.26; charges ₹0.06)
2024-06-04  BOSCHLTD    SELL ₹45.78 at stop ₹29,015.09 (-2.7%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-06-04  FDC         SELL ₹43.74 at stop ₹419.95 (-6.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹43.01 at stop ₹441.77 (-6.8%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-06-04  SMSPHARMA   SELL ₹44.63 at stop ₹181.36 (-4.1%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-06-07  INDIGO      RAISE STOP ₹3,719.77 → ₹3,805.04 (new box ₹4,005.30–₹4,529.00 sealed)
2024-06-10  ENDURANCE   BUY ₹47.54 at ₹2,439.90 (fresh Friday signal — starved 6×, front of the queue — BUY: 2.56× weekly, month 2.14×, ladder rising; stop ₹1,964.12; charges ₹0.06)
2024-06-10  FINPIPE     BUY ₹47.70 at ₹350.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.61× weekly, month 2.10×, ladder rising; ₹9.69 fresh capital added; stop ₹276.26; charges ₹0.06)
2024-06-10  NCC         BUY ₹47.55 at ₹327.60 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.80× weekly, month 1.63×, ladder rising; stop ₹260.92; charges ₹0.06)
2024-06-10  ORIENTELEC  BUY ₹47.62 at ₹237.91 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.28× weekly, month 1.78×, ladder rising; stop ₹195.65; charges ₹0.06)
2024-06-14  THERMAX     RAISE STOP ₹4,642.65 → ₹4,719.70 (new box ₹4,968.10–₹5,699.95 sealed)
2024-06-21  ORIENTELEC  RAISE STOP ₹195.65 → ₹225.44 (new box ₹237.31–₹247.50 sealed)
2024-06-21  WABAG       RAISE STOP ₹801.26 → ₹1,037.68 (new box ₹1,092.30–₹1,180.60 sealed)
2024-06-28  EMUDHRA     RAISE STOP ₹627.45 → ₹793.11 (new box ₹834.85–₹898.00 sealed)
2024-06-28  ENDURANCE   RAISE STOP ₹1,964.12 → ₹2,429.11 (new box ₹2,575.00–₹3,061.30 sealed)
2024-06-28  FINPIPE     RAISE STOP ₹276.26 → ₹306.66 (new box ₹322.80–₹355.90 sealed)
2024-06-28  INDIGO      RAISE STOP ₹3,805.04 → ₹3,976.70 (new box ₹4,186.00–₹4,609.80 sealed)
2024-06-28  NCC         RAISE STOP ₹260.92 → ₹297.87 (new box ₹313.55–₹336.70 sealed)
2024-07-05  BLUESTARCO  RAISE STOP ₹1,398.88 → ₹1,506.27 (new box ₹1,585.55–₹1,797.95 sealed)
2024-07-19  ORIENTELEC  RAISE STOP ₹225.44 → ₹245.34 (new box ₹258.25–₹287.05 sealed)
2024-07-23  FINPIPE     SELL ₹41.70 at stop ₹306.66 (-12.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-07-23  NCC         SELL ₹43.14 at stop ₹297.87 (-9.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-07-26  WABAG       RAISE STOP ₹1,037.68 → ₹1,125.70 (new box ₹1,184.95–₹1,379.00 sealed)
2024-07-29  HBLPOWER    BUY ₹50.15 at ₹634.15 (fresh Friday signal — starved 6×, front of the queue — ACCUMULATE: 1.86× weekly, month 1.74×, ladder rising; ₹15.53 fresh capital added; stop ₹509.61; charges ₹0.06)
2024-07-29  HINDOILEXP  BUY ₹50.22 at ₹270.00 (fresh Friday signal — starved 9×, front of the queue — BUY: 2.01× weekly, month 2.73×, ladder rising; stop ₹209.42; charges ₹0.06)
2024-08-05  ENDURANCE   SELL ₹47.23 at stop ₹2,429.11 (-0.4%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-08-05  THERMAX     SELL ₹40.19 at stop ₹4,719.70 (-16.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-08-12  AVANTIFEED  BUY ₹49.69 at ₹758.00 (fresh Friday signal — starved 4×, front of the queue — BUY: 2.64× weekly, month 5.57×, ladder rising; ₹12.12 fresh capital added; stop ₹596.83; charges ₹0.06)
2024-08-12  SNOWMAN     BUY ₹49.84 at ₹79.80 (fresh Friday signal — starved 8×, front of the queue — ACCUMULATE: 3.19× weekly, month 1.59×, ladder rising; stop ₹68.14; charges ₹0.06)
2024-08-13  EMUDHRA     SELL ₹63.53 at stop ₹793.11 (+35.8%, charges ₹0.07) — the cash goes back to work at the next Friday screen
2024-08-19  VGUARD      BUY ₹50.66 at ₹524.15 (fresh Friday signal — starved 4×, front of the queue — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.06)
2024-08-23  AVANTIFEED  RAISE STOP ₹596.83 → ₹650.13 (new box ₹684.35–₹793.00 sealed)
2024-09-06  INDIGO      RAISE STOP ₹3,976.70 → ₹4,485.14 (new box ₹4,721.20–₹4,943.80 sealed)
2024-09-06  WABAG       RAISE STOP ₹1,125.70 → ₹1,182.84 (new box ₹1,245.10–₹1,420.00 sealed)
2024-09-09  AVANTIFEED  SELL ₹42.53 at stop ₹650.13 (-14.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-09-16  KALYANKJIL  BUY ₹51.32 at ₹723.20 (fresh Friday signal — starved 8×, front of the queue — BUY: 2.49× weekly, month 3.31×, ladder rising; stop ₹601.35; charges ₹0.06)
2024-09-19  ORIENTELEC  SELL ₹48.99 at stop ₹245.34 (+3.1%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-09-20  KALYANKJIL  RAISE STOP ₹601.35 → ₹642.11 (new box ₹675.90–₹749.00 sealed)
2024-09-23  MARKSANS    BUY ₹52.04 at ₹326.00 (fresh Friday signal — starved 8×, front of the queue — BUY: 2.64× weekly, month 2.05×, ladder rising; stop ₹242.62; charges ₹0.06)
2024-09-27  BLUESTARCO  RAISE STOP ₹1,506.27 → ₹1,750.90 (new box ₹1,843.05–₹1,988.40 sealed)
2024-09-27  HINDOILEXP  RAISE STOP ₹209.42 → ₹220.07 (new box ₹231.65–₹245.50 sealed)
2024-10-04  KALYANKJIL  RAISE STOP ₹642.11 → ₹668.80 (new box ₹704.00–₹786.25 sealed)
2024-10-04  VGUARD      SELL ₹40.53 at stop ₹420.24 (-19.8%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-10-04  WABAG       RAISE STOP ₹1,182.84 → ₹1,367.05 (new box ₹1,439.00–₹1,548.00 sealed)
2024-10-07  ASTRAZEN    BUY ₹47.96 at ₹7,442.65 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; ₹6.40 fresh capital added; stop ₹6,768.80; charges ₹0.06)
2024-10-07  HINDOILEXP  SELL ₹40.84 at stop ₹220.07 (-18.5%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-10-07  INDIGO      SELL ₹65.47 at stop ₹4,485.14 (+40.2%, charges ₹0.07) — the cash goes back to work at the next Friday screen
2024-10-11  BLUESTARCO  RAISE STOP ₹1,750.90 → ₹1,795.74 (new box ₹1,890.25–₹2,199.55 sealed)
2024-10-11  MARKSANS    RAISE STOP ₹242.62 → ₹249.76 (new box ₹268.00–₹328.80 sealed)
2024-10-11  SNOWMAN     RAISE STOP ₹68.14 → ₹68.37 (new box ₹73.74–₹91.65 sealed)
2024-10-14  BFUTILITIE  BUY ₹51.03 at ₹1,068.60 (fresh Friday signal — starved 6×, front of the queue — ACCUMULATE: 2.10× weekly, month 2.20×, ladder rising; stop ₹860.15; charges ₹0.06)
2024-10-14  BSE         BUY ₹50.97 at ₹4,536.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.79× weekly, month 4.25×, ladder rising; stop ₹3,393.93; charges ₹0.06)
2024-10-22  KALYANKJIL  SELL ₹47.36 at stop ₹668.80 (-7.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-10-23  SNOWMAN     SELL ₹42.61 at stop ₹68.37 (-14.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹46.68 at ₹747.70 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.06)
2024-11-01  BSE         RAISE STOP ₹3,393.93 → ₹3,694.81 (new box ₹3,993.65–₹4,989.80 sealed)
2024-11-01  WABAG       RAISE STOP ₹1,367.05 → ₹1,446.29 (new box ₹1,552.30–₹1,905.65 sealed)
2024-11-07  BLUESTARCO  SELL ₹53.02 at stop ₹1,795.74 (+10.5%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2024-11-08  ASTRAZEN    RAISE STOP ₹6,768.80 → ₹6,854.77 (new box ₹7,215.55–₹7,695.70 sealed)
2024-11-11  FSL         BUY ₹48.60 at ₹367.05 (fresh Friday signal — starved 4×, front of the queue — BUY: 1.56× weekly, month 1.99×, ladder rising; stop ₹309.80; charges ₹0.11)
2024-11-11  GANESHHOUC  BUY ₹48.47 at ₹1,119.30 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.27× weekly, month 2.35×, ladder rising; stop ₹867.10; charges ₹0.11)
2024-11-14  ASTRAZEN    SELL ₹44.02 at stop ₹6,854.77 (-7.9%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2024-11-22  GANESHHOUC  RAISE STOP ₹867.10 → ₹967.56 (new box ₹1,020.05–₹1,195.00 sealed)
2024-11-22  PAYTM       RAISE STOP ₹636.31 → ₹712.50 (new box ₹750.00–₹855.10 sealed)
2024-11-25  GARFIBRES   BUY ₹49.13 at ₹956.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.62× weekly, month 2.20×, ladder rising; ₹1.57 fresh capital added; stop ₹704.32; charges ₹0.12)
2024-11-29  FSL         RAISE STOP ₹309.80 → ₹317.79 (new box ₹334.65–₹390.85 sealed)
2024-11-29  GARFIBRES   RAISE STOP ₹704.32 → ₹829.35 (new box ₹873.00–₹957.00 sealed)
2024-11-29  MARKSANS    RAISE STOP ₹249.76 → ₹282.25 (new box ₹297.10–₹325.00 sealed)
2024-12-06  HBLPOWER    RAISE STOP ₹509.61 → ₹583.02 (new box ₹613.70–₹641.85 sealed)
2024-12-06  PAYTM       RAISE STOP ₹712.50 → ₹838.09 (new box ₹882.20–₹952.00 sealed)
2024-12-20  MARKSANS    SELL ₹44.91 at stop ₹282.25 (-13.4%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2024-12-20  PAYTM       RAISE STOP ₹838.09 → ₹887.49 (new box ₹934.20–₹1,007.00 sealed)
2024-12-23  KAYNES      BUY ₹49.67 at ₹7,358.80 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.40× weekly, month 2.00×, ladder rising; ₹4.77 fresh capital added; stop ₹5,824.55; charges ₹0.12)
2024-12-27  KAYNES      RAISE STOP ₹5,824.55 → ₹6,670.80 (new box ₹7,021.90–₹7,780.00 sealed)
2024-12-27  PAYTM       RAISE STOP ₹887.49 → ₹893.05 (new box ₹940.05–₹1,062.95 sealed)
2025-01-03  BSE         RAISE STOP ₹3,694.81 → ₹4,954.63 (new box ₹5,215.40–₹5,837.95 sealed)
2025-01-03  GANESHHOUC  RAISE STOP ₹967.56 → ₹1,075.49 (new box ₹1,132.10–₹1,211.45 sealed)
2025-01-09  GARFIBRES   SELL ₹42.42 at stop ₹829.35 (-13.2%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹55.57 at stop ₹893.05 (+19.4%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2025-01-10  KAYNES      SELL ₹44.82 at stop ₹6,670.80 (-9.3%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹47.68 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.11)
2025-01-13  LLOYDSME    BUY ₹47.93 at ₹1,441.90 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.11)
2025-01-13  WABAG       SELL ₹67.31 at stop ₹1,446.29 (+40.5%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2025-01-17  AEGISLOG    RAISE STOP ₹697.76 → ₹700.36 (new box ₹778.05–₹1,037.00 sealed)
2025-01-17  FSL         RAISE STOP ₹317.79 → ₹332.14 (new box ₹352.95–₹422.30 sealed)
2025-01-20  APOLLO      BUY ₹49.90 at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 3.48×, ladder rising; stop ₹110.19; charges ₹0.12)
2025-01-24  AEGISLOG    SELL ₹39.83 at stop ₹700.36 (-16.1%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-01-27  BFUTILITIE  SELL ₹40.93 at stop ₹860.15 (-19.5%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹46.48 at ₹850.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.11)
2025-01-28  FSL         SELL ₹43.77 at stop ₹332.14 (-9.5%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-01-28  LLOYDSME    SELL ₹41.65 at stop ₹1,258.75 (-12.7%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-01-31  GANESHHOUC  RAISE STOP ₹1,075.49 → ₹1,090.38 (new box ₹1,181.45–₹1,485.00 sealed)
2025-02-03  ZENSARTECH  BUY ₹47.54 at ₹947.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹0.11)
2025-02-10  HDFCGOLD    BUY ₹48.14 at ₹75.80 (fresh Friday signal — BUY: 2.22× weekly, month 1.58×, ladder rising; stop ₹64.93; charges ₹0.11)
2025-02-17  APOLLO      SELL ₹41.62 at stop ₹110.19 (-16.2%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-02-17  SETFGOLD    BUY ₹45.82 at ₹76.80 (fresh Friday signal — BUY: 1.62× weekly, month 1.57×, ladder rising; stop ₹59.71; charges ₹0.11)
2025-02-21  HDFCGOLD    RAISE STOP ₹64.93 → ₹70.20 (new box ₹73.89–₹76.80 sealed)
2025-02-21  SETFGOLD    RAISE STOP ₹59.71 → ₹69.36 (new box ₹73.01–₹76.80 sealed)
2025-02-24  TAJGVK      BUY ₹44.73 at ₹440.40 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.16× weekly, month 2.07×, ladder rising; stop ₹349.09; charges ₹0.11)
2025-02-28  BSE         SELL ₹55.49 at stop ₹4,954.63 (+9.2%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2025-02-28  GANESHHOUC  SELL ₹47.01 at stop ₹1,090.38 (-2.6%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-02-28  TAJGVK      RAISE STOP ₹349.09 → ₹412.59 (new box ₹434.30–₹498.25 sealed)
2025-03-03  NH          BUY ₹43.35 at ₹1,450.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.10)
2025-03-03  ZENSARTECH  SELL ₹36.37 at stop ₹727.84 (-23.1%, charges ₹0.08) — the cash goes back to work at the next Friday screen
2025-03-07  CREDITACC   RAISE STOP ₹825.52 → ₹837.38 (new box ₹882.15–₹1,031.40 sealed)
2025-03-10  GOLDIETF    BUY ₹44.64 at ₹74.30 (fresh Friday signal — ACCUMULATE: 1.51× weekly, month 1.95×, ladder rising; stop ₹69.50; charges ₹0.11)
2025-03-10  GRMOVER     BUY ₹44.44 at ₹252.00 (fresh Friday signal — BUY: 1.55× weekly, month 1.68×, ladder rising; stop ₹203.86; charges ₹0.10)
2025-03-13  NH          RAISE STOP ₹1,235.90 → ₹1,436.97 (new box ₹1,512.60–₹1,692.50 sealed)
2025-03-17  AVANTIFEED  BUY ₹45.16 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.11)
2025-03-21  TAJGVK      RAISE STOP ₹412.59 → ₹453.34 (new box ₹477.20–₹518.85 sealed)
2025-04-01  TAX         FY2025 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹52.29 / LT ₹0.00)
2025-04-02  TAJGVK      SELL ₹45.83 at stop ₹453.34 (+2.9%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-04-04  GRMOVER     RAISE STOP ₹203.86 → ₹248.00 (new box ₹261.05–₹288.67 sealed)
2025-04-04  HDFCGOLD    RAISE STOP ₹70.20 → ₹71.44 (new box ₹75.20–₹78.55 sealed)
2025-04-07  AVANTIFEED  SELL ₹34.63 at stop ₹648.95 (-23.0%, charges ₹0.08) — the cash goes back to work at the next Friday screen
2025-04-07  GOLDBEES    BUY ₹44.86 at ₹74.60 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.78× weekly, month 1.67×, ladder rising; stop ₹68.93; charges ₹0.11)
2025-04-07  HDFCGOLD    SELL ₹45.16 at stop ₹71.44 (-5.8%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-04-07  SETFGOLD    SELL ₹41.20 at stop ₹69.36 (-9.7%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-04-15  INDIASHLTR  BUY ₹45.12 at ₹865.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.11)
2025-04-15  VADILALIND  BUY ₹45.29 at ₹5,898.90 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.25× weekly, month 6.19×, ladder rising; stop ₹4,500.03; charges ₹0.11)
2025-04-25  GRMOVER     RAISE STOP ₹248.00 → ₹290.80 (new box ₹306.10–₹329.95 sealed)
2025-04-28  TFCILTD     BUY ₹46.67 at ₹37.60 (fresh Friday signal — starved 6×, front of the queue — BUY: 1.96× weekly, month 2.55×, ladder rising; ₹14.14 fresh capital added; stop ₹30.97; charges ₹0.11)
2025-05-02  TFCILTD     RAISE STOP ₹30.97 → ₹34.39 (new box ₹36.20–₹38.94 sealed)
2025-05-07  GRMOVER     SELL ₹51.05 at stop ₹290.80 (+15.4%, charges ₹0.11) — the cash goes back to work at the next Friday screen
2025-05-09  CREDITACC   RAISE STOP ₹837.38 → ₹1,019.35 (new box ₹1,073.00–₹1,179.20 sealed)
2025-05-09  GOLDBEES    RAISE STOP ₹68.93 → ₹73.49 (new box ₹77.36–₹83.56 sealed)
2025-05-09  GOLDIETF    RAISE STOP ₹69.50 → ₹75.63 (new box ₹79.61–₹87.91 sealed)
2025-05-09  INDIASHLTR  RAISE STOP ₹738.82 → ₹804.65 (new box ₹847.00–₹915.00 sealed)
2025-05-09  NH          RAISE STOP ₹1,436.97 → ₹1,641.69 (new box ₹1,728.10–₹1,871.60 sealed)
2025-05-12  VMART       BUY ₹48.37 at ₹894.50 (fresh Friday signal — ACCUMULATE: 3.73× weekly, month 1.96×, ladder rising; stop ₹725.56; charges ₹0.11)
2025-05-16  TFCILTD     RAISE STOP ₹34.39 → ₹35.21 (new box ₹37.06–₹42.52 sealed)
2025-05-16  VADILALIND  RAISE STOP ₹4,500.03 → ₹5,401.40 (new box ₹5,858.00–₹7,380.00 sealed)
2025-05-23  VMART       RAISE STOP ₹725.56 → ₹797.90 (new box ₹839.90–₹899.27 sealed)
2025-05-30  CREDITACC   RAISE STOP ₹1,019.35 → ₹1,029.71 (new box ₹1,083.90–₹1,225.60 sealed)
2025-05-30  VADILALIND  SELL ₹41.28 at stop ₹5,401.40 (-8.4%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-06-02  TIMKEN      BUY ₹47.58 at ₹3,120.00 (fresh Friday signal — starved 5×, front of the queue — ACCUMULATE: 1.84× weekly, month 3.36×, ladder rising; ₹3.61 fresh capital added; stop ₹2,785.11; charges ₹0.11)
2025-06-06  GOLDBEES    RAISE STOP ₹73.49 → ₹74.70 (new box ₹78.63–₹81.95 sealed)
2025-06-20  TFCILTD     RAISE STOP ₹35.21 → ₹36.66 (new box ₹39.15–₹47.48 sealed)
2025-06-20  TIMKEN      RAISE STOP ₹2,785.11 → ₹3,002.09 (new box ₹3,160.10–₹3,467.30 sealed)
2025-06-27  NH          RAISE STOP ₹1,641.69 → ₹1,763.87 (new box ₹1,856.70–₹1,957.00 sealed)
2025-07-03  VMART       SELL ₹42.94 at stop ₹797.90 (-10.8%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-07-04  GOLDBEES    RAISE STOP ₹74.70 → ₹75.56 (new box ₹79.54–₹85.00 sealed)
2025-07-07  QUICKHEAL   BUY ₹50.75 at ₹402.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 4.50× weekly, month 2.43×, ladder rising; ₹7.81 fresh capital added; stop ₹326.90; charges ₹0.12)
2025-07-11  CREDITACC   RAISE STOP ₹1,029.71 → ₹1,193.20 (new box ₹1,256.00–₹1,354.80 sealed)
2025-07-11  TIMKEN      RAISE STOP ₹3,002.09 → ₹3,114.10 (new box ₹3,278.00–₹3,531.80 sealed)
2025-07-18  QUICKHEAL   RAISE STOP ₹326.90 → ₹354.54 (new box ₹373.20–₹416.70 sealed)
2025-07-21  QUICKHEAL   SELL ₹44.56 at stop ₹354.54 (-11.8%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-07-25  NH          RAISE STOP ₹1,763.87 → ₹1,814.78 (new box ₹1,910.30–₹2,045.00 sealed)
2025-07-28  FORCEMOT    BUY ₹51.28 at ₹17,500.00 (fresh Friday signal — starved 5×, front of the queue — BUY: 3.26× weekly, month 3.99×, ladder rising; ₹6.73 fresh capital added; stop ₹15,350.10; charges ₹0.12)
2025-08-01  INDIASHLTR  RAISE STOP ₹804.65 → ₹853.86 (new box ₹898.80–₹1,011.75 sealed)
2025-08-01  TFCILTD     RAISE STOP ₹36.66 → ₹51.02 (new box ₹53.71–₹58.85 sealed)
2025-08-04  NH          SELL ₹54.01 at stop ₹1,814.78 (+25.2%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2025-08-04  TIMKEN      SELL ₹47.27 at stop ₹3,114.10 (-0.2%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-08-11  BLISSGVS    BUY ₹51.37 at ₹178.60 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.52× weekly, month 1.82×, ladder rising; stop ₹143.93; charges ₹0.12)
2025-08-11  PRAKASH     BUY ₹51.21 at ₹178.70 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 7.16× weekly, month 2.58×, ladder rising; ₹1.30 fresh capital added; stop ₹145.68; charges ₹0.12)
2025-08-14  INDIASHLTR  RAISE STOP ₹853.86 → ₹862.60 (new box ₹908.00–₹975.00 sealed)
2025-09-05  CREDITACC   RAISE STOP ₹1,193.20 → ₹1,256.94 (new box ₹1,323.10–₹1,409.00 sealed)
2025-09-05  TFCILTD     RAISE STOP ₹51.02 → ₹56.58 (new box ₹59.56–₹63.20 sealed)
2025-09-19  GOLDBEES    RAISE STOP ₹75.56 → ₹85.42 (new box ₹89.92–₹92.90 sealed)
2025-09-25  INDIASHLTR  SELL ₹44.79 at stop ₹862.60 (-0.3%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-09-26  BLISSGVS    SELL ₹41.21 at stop ₹143.93 (-19.4%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-09-26  CREDITACC   RAISE STOP ₹1,256.94 → ₹1,274.42 (new box ₹1,341.50–₹1,400.00 sealed)
2025-09-26  GOLDIETF    RAISE STOP ₹75.63 → ₹89.02 (new box ₹93.70–₹97.50 sealed)
2025-09-26  TFCILTD     RAISE STOP ₹56.58 → ₹67.97 (new box ₹71.55–₹72.98 sealed)
2025-09-29  HDFCSILVER  BUY ₹53.35 at ₹137.30 (fresh Friday signal — starved 4×, front of the queue — BUY: 2.55× weekly, month 4.63×, ladder rising; stop ₹112.21; charges ₹0.13)
2025-09-29  SILVERIETF  BUY ₹53.44 at ₹142.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.78× weekly, month 3.67×, ladder rising; ₹20.78 fresh capital added; stop ₹119.33; charges ₹0.13)
2025-10-03  GOLDBEES    RAISE STOP ₹85.42 → ₹88.72 (new box ₹93.39–₹97.50 sealed)
2025-10-03  GOLDIETF    RAISE STOP ₹89.02 → ₹91.66 (new box ₹96.48–₹102.50 sealed)
2025-10-09  FORCEMOT    SELL ₹44.78 at stop ₹15,350.10 (-12.3%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-10-10  HDFCSILVER  RAISE STOP ₹112.21 → ₹129.39 (new box ₹136.20–₹142.70 sealed)
2025-10-13  HDFCGOLD    BUY ₹58.64 at ₹106.57 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.68× weekly, month 3.27×, ladder rising; ₹13.87 fresh capital added; stop ₹91.67; charges ₹0.14)
2025-10-17  TFCILTD     RAISE STOP ₹67.97 → ₹69.12 (new box ₹72.76–₹75.90 sealed)
2025-10-20  CREDITACC   SELL ₹69.36 at stop ₹1,274.42 (+49.9%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2025-10-27  SKYGOLD     BUY ₹56.13 at ₹370.00 (fresh Friday signal — BUY: 1.65× weekly, month 2.25×, ladder rising; stop ₹304.38; charges ₹0.13)
2025-10-30  TFCILTD     SELL ₹85.40 at stop ₹69.12 (+83.8%, charges ₹0.19) — the cash goes back to work at the next Friday screen
2025-10-31  GOLDBEES    RAISE STOP ₹88.72 → ₹90.77 (new box ₹95.55–₹108.69 sealed)
2025-10-31  PRAKASH     RAISE STOP ₹145.68 → ₹147.31 (new box ₹155.06–₹167.99 sealed)
2025-10-31  SILVERIETF  RAISE STOP ₹119.33 → ₹123.06 (new box ₹138.51–₹190.00 sealed)
2025-11-03  MAHABANK    BUY ₹56.14 at ₹59.70 (fresh Friday signal — starved 7×, front of the queue — ACCUMULATE: 2.08× weekly, month 1.69×, ladder rising; stop ₹53.69; charges ₹0.13)
2025-11-07  SKYGOLD     RAISE STOP ₹304.38 → ₹329.13 (new box ₹346.45–₹375.45 sealed)
2025-11-14  PRAKASH     SELL ₹42.02 at stop ₹147.31 (-17.6%, charges ₹0.09) — the cash goes back to work at the next Friday screen
2025-11-17  PARAGMILK   BUY ₹56.48 at ₹354.00 (fresh Friday signal — starved 7×, front of the queue — BUY: 3.48× weekly, month 2.34×, ladder rising; stop ₹293.55; charges ₹0.13)
2025-11-25  SKYGOLD     SELL ₹49.70 at stop ₹329.13 (-11.0%, charges ₹0.11) — the cash goes back to work at the next Friday screen
2025-12-01  SANSERA     BUY ₹57.68 at ₹1,749.60 (fresh Friday signal — starved 4×, front of the queue — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.14)
2025-12-09  PARAGMILK   SELL ₹46.62 at stop ₹293.55 (-17.1%, charges ₹0.10) — the cash goes back to work at the next Friday screen
2025-12-12  SANSERA     RAISE STOP ₹1,413.60 → ₹1,517.72 (new box ₹1,597.60–₹1,770.00 sealed)
2025-12-15  GMRAIRPORT  BUY ₹58.92 at ₹103.95 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.56× weekly, month 2.60×, ladder rising; stop ₹89.73; charges ₹0.14)
2025-12-19  GMRAIRPORT  RAISE STOP ₹89.73 → ₹92.10 (new box ₹96.95–₹110.36 sealed)
2025-12-19  GOLDIETF    RAISE STOP ₹91.66 → ₹107.32 (new box ₹112.97–₹116.21 sealed)
2025-12-26  GOLDBEES    RAISE STOP ₹90.77 → ₹103.85 (new box ₹109.32–₹111.77 sealed)
2025-12-26  HDFCGOLD    RAISE STOP ₹91.67 → ₹106.71 (new box ₹112.33–₹115.92 sealed)
2026-01-02  HDFCSILVER  RAISE STOP ₹129.39 → ₹201.50 (new box ₹212.10–₹243.45 sealed)
2026-01-09  GOLDBEES    RAISE STOP ₹103.85 → ₹104.22 (new box ₹109.70–₹117.00 sealed)
2026-01-09  HDFCGOLD    RAISE STOP ₹106.71 → ₹107.66 (new box ₹113.33–₹120.90 sealed)
2026-01-09  SILVERIETF  RAISE STOP ₹123.06 → ₹208.50 (new box ₹219.47–₹251.35 sealed)
2026-01-16  MAHABANK    RAISE STOP ₹53.69 → ₹58.71 (new box ₹61.80–₹65.97 sealed)
2026-01-16  SANSERA     RAISE STOP ₹1,517.72 → ₹1,672.76 (new box ₹1,760.80–₹1,958.30 sealed)
2026-01-23  GMRAIRPORT  SELL ₹51.97 at stop ₹92.10 (-11.4%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹54.89 at stop ₹1,672.76 (-4.4%, charges ₹0.12) — the cash goes back to work at the next Friday screen
2026-01-27  GOLD1       BUY ₹73.17 at ₹132.24 (fresh Friday signal — starved 6×, front of the queue — BUY: 4.68× weekly, month 3.28×, ladder rising; stop ₹103.55; charges ₹0.17)
2026-01-27  SETFGOLD    BUY ₹73.16 at ₹133.33 (fresh Friday signal — starved 5×, front of the queue — BUY: 3.60× weekly, month 3.02×, ladder rising; ₹31.72 fresh capital added; stop ₹106.43; charges ₹0.17)
2026-01-30  GOLDBEES    RAISE STOP ₹104.22 → ₹113.05 (new box ₹119.00–₹135.90 sealed)
2026-01-30  GOLDIETF    RAISE STOP ₹107.32 → ₹115.68 (new box ₹121.77–₹139.00 sealed)
2026-01-30  HDFCGOLD    RAISE STOP ₹107.66 → ₹114.75 (new box ₹121.50–₹144.00 sealed)
2026-01-30  MAHABANK    RAISE STOP ₹58.71 → ₹59.76 (new box ₹62.91–₹67.59 sealed)
2026-01-30  SETFGOLD    RAISE STOP ₹106.43 → ₹115.37 (new box ₹121.57–₹142.22 sealed)
2026-02-02  GOLDBEES    SELL ₹67.67 at stop ₹113.05 (+51.5%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2026-02-09  CPSEETF     BUY ₹68.62 at ₹99.82 (fresh Friday signal — starved 6×, front of the queue — BUY: 2.11× weekly, month 2.09×, ladder rising; ₹0.95 fresh capital added; stop ₹85.68; charges ₹0.16)
2026-02-20  CPSEETF     RAISE STOP ₹85.68 → ₹91.67 (new box ₹96.50–₹102.40 sealed)
2026-02-20  MAHABANK    RAISE STOP ₹59.76 → ₹61.05 (new box ₹64.26–₹67.70 sealed)
2026-03-13  CPSEETF     RAISE STOP ₹91.67 → ₹96.54 (new box ₹101.62–₹106.26 sealed)
2026-03-23  GOLDIETF    SELL ₹69.18 at stop ₹115.68 (+55.7%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2026-03-23  HDFCGOLD    SELL ₹62.86 at stop ₹114.75 (+7.7%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2026-03-23  HDFCSILVER  SELL ₹77.93 at stop ₹201.50 (+46.8%, charges ₹0.17) — the cash goes back to work at the next Friday screen
2026-03-23  SETFGOLD    SELL ₹63.02 at stop ₹115.37 (-13.5%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2026-03-23  SILVERIETF  SELL ₹78.11 at stop ₹208.50 (+46.8%, charges ₹0.17) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹61.55 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.15)
2026-03-30  LIQUID1     BUY ₹61.56 at ₹1,097.40 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 2.24× weekly, month 1.82×, ladder rising; stop ₹1,039.97; charges ₹0.15)
2026-03-30  MAHABANK    SELL ₹57.14 at stop ₹61.05 (+2.3%, charges ₹0.13) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹6.05 paid (STCG ₹14.75 @20%, LTCG ₹24.80 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2026-04-06  BAJAJHIND   BUY ₹60.85 at ₹17.08 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 2.33× weekly, month 1.97×, ladder rising; stop ₹13.87; charges ₹0.14)
2026-04-06  CHENNPETRO  BUY ₹60.93 at ₹989.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.14)
2026-04-10  AETHER      RAISE STOP ₹928.15 → ₹1,010.28 (new box ₹1,065.60–₹1,250.00 sealed)
2026-04-10  GOLD1       RAISE STOP ₹103.55 → ₹113.80 (new box ₹119.79–₹125.94 sealed)
2026-04-13  THERMAX     BUY ₹61.50 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.15)
2026-04-20  NLCINDIA    BUY ₹63.27 at ₹303.60 (fresh Friday signal — starved 3×, front of the queue — BUY: 5.54× weekly, month 2.41×, ladder rising; stop ₹248.05; charges ₹0.15)
2026-04-24  LIQUID1     RAISE STOP ₹1,039.97 → ₹1,041.83 (new box ₹1,096.66–₹1,102.30 sealed)
2026-04-30  BAJAJHIND   RAISE STOP ₹13.87 → ₹17.96 (new box ₹18.91–₹20.30 sealed)
2026-04-30  CPSEETF     RAISE STOP ₹96.54 → ₹100.15 (new box ₹105.42–₹107.84 sealed)
2026-04-30  NLCINDIA    RAISE STOP ₹248.05 → ₹278.49 (new box ₹293.15–₹318.55 sealed)
2026-05-08  AETHER      RAISE STOP ₹1,010.28 → ₹1,125.84 (new box ₹1,185.10–₹1,275.10 sealed)
2026-05-08  GOLD1       RAISE STOP ₹113.80 → ₹114.47 (new box ₹120.50–₹127.90 sealed)
2026-05-08  LIQUID1     RAISE STOP ₹1,041.83 → ₹1,047.51 (new box ₹1,102.64–₹1,103.15 sealed)
2026-05-08  THERMAX     RAISE STOP ₹2,897.50 → ₹3,726.38 (new box ₹3,922.50–₹4,305.00 sealed)
2026-05-14  AETHER      SELL ₹59.95 at stop ₹1,125.84 (-2.1%, charges ₹0.13) — the cash goes back to work at the next Friday screen
2026-05-14  BAJAJHIND   SELL ₹63.70 at stop ₹17.96 (+5.2%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2026-05-15  CHENNPETRO  RAISE STOP ₹891.29 → ₹953.23 (new box ₹1,003.40–₹1,159.70 sealed)
2026-05-15  THERMAX     RAISE STOP ₹3,726.38 → ₹4,181.80 (new box ₹4,401.90–₹4,880.00 sealed)
2026-05-18  ATHERENERG  BUY ₹64.08 at ₹930.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.71× weekly, month 1.86×, ladder rising; stop ₹793.87; charges ₹0.15)
2026-05-18  CAPLIPOINT  BUY ₹64.11 at ₹1,990.00 (fresh Friday signal — starved 6×, front of the queue — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.15)
2026-05-22  CAPLIPOINT  RAISE STOP ₹1,711.52 → ₹1,851.17 (new box ₹1,948.60–₹2,060.00 sealed)
2026-05-22  NLCINDIA    RAISE STOP ₹278.49 → ₹320.62 (new box ₹337.50–₹387.80 sealed)
2026-05-29  ATHERENERG  RAISE STOP ₹793.87 → ₹829.92 (new box ₹873.60–₹989.40 sealed)
2026-05-29  GOLD1       RAISE STOP ₹114.47 → ₹121.71 (new box ₹128.12–₹135.00 sealed)
2026-06-02  CPSEETF     SELL ₹68.54 at stop ₹100.15 (+0.3%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2026-06-08  MANINDS     BUY ₹65.84 at ₹526.00 (fresh Friday signal — starved 5×, front of the queue — ACCUMULATE: 2.51× weekly, month 1.68×, ladder rising; stop ₹442.27; charges ₹0.16)
2026-06-09  NLCINDIA    SELL ₹66.51 at stop ₹320.62 (+5.6%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2026-06-10  GOLD1       SELL ₹67.04 at stop ₹121.71 (-8.0%, charges ₹0.15) — the cash goes back to work at the next Friday screen
2026-06-12  ATHERENERG  RAISE STOP ₹829.92 → ₹951.09 (new box ₹1,001.15–₹1,069.00 sealed)
2026-06-12  CAPLIPOINT  RAISE STOP ₹1,851.17 → ₹1,852.50 (new box ₹1,950.00–₹2,099.00 sealed)
2026-06-12  CHENNPETRO  RAISE STOP ₹953.23 → ₹1,075.02 (new box ₹1,131.60–₹1,225.00 sealed)
2026-06-15  LIQUIDPLUS  BUY ₹66.94 at ₹1,084.28 (fresh Friday signal — starved 4×, front of the queue — BUY: 2.46× weekly, month 1.67×, ladder rising; stop ₹1,022.02; charges ₹0.16)
2026-06-15  NRBBEARING  BUY ₹67.07 at ₹438.00 (fresh Friday signal — starved 6×, front of the queue — BUY: 10.53× weekly, month 6.95×, ladder rising; stop ₹331.98; charges ₹0.16)
2026-06-18  ATHERENERG  SELL ₹65.24 at stop ₹951.09 (+2.3%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2026-06-19  THERMAX     RAISE STOP ₹4,181.80 → ₹4,306.64 (new box ₹4,533.30–₹5,075.00 sealed)
2026-06-22  PREMEXPLN   BUY ₹66.95 at ₹781.05 (fresh Friday signal — starved 4×, front of the queue — ACCUMULATE: 2.49× weekly, month 3.44×, ladder rising; stop ₹585.15; charges ₹0.16)
2026-06-25  CAPLIPOINT  RAISE STOP ₹1,852.50 → ₹2,209.13 (new box ₹2,325.40–₹2,447.30 sealed)
2026-06-25  NRBBEARING  RAISE STOP ₹331.98 → ₹391.97 (new box ₹412.60–₹455.80 sealed)
2026-07-10  LIQUIDPLUS  RAISE STOP ₹1,022.02 → ₹1,036.02 (new box ₹1,090.55–₹1,094.25 sealed)
2026-07-10  PREMEXPLN   RAISE STOP ₹585.15 → ₹635.06 (new box ₹680.00–₹829.80 sealed)
2026-07-17  CAPLIPOINT  RAISE STOP ₹2,209.13 → ₹2,376.52 (new box ₹2,501.60–₹2,675.00 sealed)
2026-07-22  NRBBEARING  SELL ₹59.75 at stop ₹391.97 (-10.5%, charges ₹0.13) — the cash goes back to work at the next Friday screen
2026-07-24  CHENNPETRO  RAISE STOP ₹1,075.02 → ₹1,130.59 (new box ₹1,190.10–₹1,279.70 sealed)
2026-07-24  LIQUIDPLUS  RAISE STOP ₹1,036.02 → ₹1,039.82 (new box ₹1,094.55–₹1,127.08 sealed)
2026-07-27  GABRIEL     BUY ₹64.43 at ₹1,370.10 (fresh Friday signal — starved 4×, front of the queue — BUY: 4.50× weekly, month 1.84×, ladder rising; stop ₹1,154.25; charges ₹0.15)
2026-07-29  THERMAX     SELL ₹73.32 at stop ₹4,306.64 (+19.8%, charges ₹0.16) — the cash goes back to work at the next Friday screen
2026-07-31  GABRIEL     RAISE STOP ₹1,154.25 → ₹1,268.34 (new box ₹1,335.10–₹1,519.90 sealed)
2026-08-03  RATNAVEER   BUY ₹65.89 at ₹184.99 (fresh Friday signal — starved 3×, front of the queue — BUY: 9.23× weekly, month 4.03×, ladder rising; stop ₹162.56; charges ₹0.16)
2026-08-07  RATNAVEER   RAISE STOP ₹162.56 → ₹165.36 (new box ₹175.15–₹207.79 sealed)
2026-08-14  RATNAVEER   RAISE STOP ₹165.36 → ₹194.19 (new box ₹204.41–₹218.49 sealed)
2026-08-21  CHENNPETRO  RAISE STOP ₹1,130.59 → ₹1,242.60 (new box ₹1,308.00–₹1,449.00 sealed)
2026-08-21  GABRIEL     RAISE STOP ₹1,268.34 → ₹1,349.19 (new box ₹1,420.20–₹1,600.00 sealed)
2026-08-25  GABRIEL     SELL ₹63.15 at stop ₹1,349.19 (-1.5%, charges ₹0.14) — the cash goes back to work at the next Friday screen
2026-09-04  MANINDS     RAISE STOP ₹442.27 → ₹700.58 (new box ₹737.45–₹783.40 sealed)
2026-09-04  RATNAVEER   RAISE STOP ₹194.19 → ₹263.29 (new box ₹277.15–₹314.90 sealed)
2026-09-07  VINDHYATEL  BUY ₹74.23 at ₹2,755.00 (fresh Friday signal — starved 4×, front of the queue — BUY: 1.68× weekly, month 1.98×, ladder rising; stop ₹2,256.25; charges ₹0.18)
2026-09-11  VINDHYATEL  RAISE STOP ₹2,256.25 → ₹2,555.50 (new box ₹2,690.00–₹2,952.60 sealed)
```
