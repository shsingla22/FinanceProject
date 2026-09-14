# The Darvas screen — 2020-03-01 → 2026-09-11

> **LONG-RUN BACKTEST.** One continuous price archive (2019-03-01 → 2026-09-11, 1971 symbols, in `ROLLING_2019-03-01_to_2026-09-13/`); every Friday screen sees only bars up to its own Friday; the earnings gate reads only fiscal years ended on or before the last 31 March at each screen date; the conference-call read is excluded. The net run pays Angel One charges on every order and settles capital-gains tax every 1 April. **The universe is POINT-IN-TIME with a ROLLING radar:** membership is recomputed EVERY MONTH as the top symbols by the TRAILING month's traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — casualties are IN while they traded, new listings enter the month they earn their place; membership gates fresh entries only (`_membership_long.csv`); split/bonus adjustments are heuristic, all listed in `_adjustments.csv`. No slippage, stop exits at the stop price, fractional shares. Stored fiscal statements exist for 37% of this universe — a stock without statements cannot be blocked by the earnings gate.

## The rules — the skill, kept simple

₹100 starts ALL IN CASH and nothing is ever added: the portfolio compounds only what it makes. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; ≥3 boxes with the last 3 midpoints rising) runs over the whole universe. **At most 10 positions at any time**, each fresh entry one equal slice (a tenth of equity), entries at the next trading day's open, falling earnings power refused, nothing below half a slice. **Cash never sleeps:** money freed by a stop goes into that week's fresh qualifiers, and a fully-qualified signal the cash never reached climbs the funding queue each time it is starved — front of the line ahead of louder newcomers, reset once funded. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; only the stop itself exits; a stopped symbol returns only by passing the full screen again. When nothing qualifies, the cash stays cash. NO pyramiding — doubling was built, measured and retired: on every configuration tested the add-on bought the top of the newest box with the stop a whole box lower, and the marginal rupee underperformed the base system.

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of charges and capital-gains tax** | **₹234.07** | **+13.94% a year** |
| Before charges and taxes | ₹328.43 | +20.02% a year |
| Nifty 50 (same window, pre-cost, pre-tax) | ₹212.91 | +12.30% a year |

*₹1.71 of tax has accrued on the final part-year's realised gains (due next April) — settling it today would leave ₹232.36 (+13.81% a year); unrealised gains in the end book carry a further deferred liability. 6.52 years, 341 weekly screens.*

## What the frictions took (net run)

- **Transaction charges: ₹10.77** (Angel One equity delivery: STT 0.10% both sides, exchange and SEBI levies, 18% GST, stamp duty 0.015% on buys, delivery brokerage ₹0 until 31 Oct 2024 then 0.1%).
- **Capital-gains tax paid: ₹22.77** — 20% short-term (≤365 days), 12.5% long-term, settled each 1 April with lawful set-off and loss carry-forward.

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

## Calendar-year returns

| Year (through) | Net equity | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | ₹112.96 | +13.0% | +13.7% | +25.1% |
| 2021 (2021-12-31) | ₹153.67 | +36.0% | +38.8% | +26.2% |
| 2022 (2022-12-30) | ₹133.86 | -12.9% | -5.8% | +4.3% |
| 2023 (2023-12-29) | ₹215.64 | +61.1% | +57.1% | +20.0% |
| 2024 (2024-12-27) | ₹224.29 | +4.0% | +10.6% | +9.6% |
| 2025 (2025-12-26) | ₹212.51 | -5.3% | +6.4% | +9.4% |
| 2026 (2026-09-11) | ₹234.07 | +10.1% | +19.6% | -10.2% |

## What it took to earn it

- **Maximum drawdown: -31.6%** (peak 2021-07-30 → trough 2022-06-17, weekly closes).
- **230 closed trades**: 96 winners (42%), average winner +28.6%, average loser -12.0%.
- Best closed trade BORORENEW +148.3%; worst BCG -59.0%.
- Median holding period 63 days.
- Cash share of equity averaged 11% (median 3%); fully in cash 5 of 341 weeks — when nothing qualifies, the money waits.

## Monthly equity curve (net run)

| Month-end screen | Equity | Cash | Positions |
|---|---:|---:|---:|
| 2020-03-27 | ₹88.29 | ₹88.29 | 0 |
| 2020-04-30 | ₹89.10 | ₹26.28 | 7 |
| 2020-05-29 | ₹93.67 | ₹0.00 | 10 |
| 2020-06-26 | ₹100.04 | ₹0.00 | 10 |
| 2020-07-31 | ₹103.92 | ₹8.78 | 9 |
| 2020-08-28 | ₹100.59 | ₹1.17 | 10 |
| 2020-09-25 | ₹104.20 | ₹25.58 | 7 |
| 2020-10-30 | ₹96.43 | ₹9.48 | 8 |
| 2020-11-27 | ₹103.55 | ₹3.16 | 9 |
| 2020-12-24 | ₹112.96 | ₹46.02 | 5 |
| 2021-01-29 | ₹110.63 | ₹31.93 | 7 |
| 2021-02-26 | ₹123.67 | ₹21.89 | 8 |
| 2021-03-26 | ₹113.63 | ₹10.13 | 9 |
| 2021-04-30 | ₹123.82 | ₹1.08 | 10 |
| 2021-05-28 | ₹141.80 | ₹1.08 | 10 |
| 2021-06-25 | ₹150.98 | ₹2.21 | 10 |
| 2021-07-30 | ₹165.69 | ₹2.21 | 10 |
| 2021-08-27 | ₹153.55 | ₹6.06 | 9 |
| 2021-09-24 | ₹154.97 | ₹24.68 | 8 |
| 2021-10-29 | ₹154.45 | ₹27.71 | 8 |
| 2021-11-26 | ₹150.37 | ₹65.71 | 6 |
| 2021-12-31 | ₹153.67 | ₹0.00 | 10 |
| 2022-01-28 | ₹151.02 | ₹14.85 | 9 |
| 2022-02-25 | ₹135.46 | ₹82.57 | 4 |
| 2022-03-25 | ₹134.84 | ₹14.39 | 9 |
| 2022-04-29 | ₹132.23 | ₹22.36 | 8 |
| 2022-05-27 | ₹113.61 | ₹13.74 | 9 |
| 2022-06-24 | ₹115.15 | ₹5.21 | 9 |
| 2022-07-29 | ₹125.44 | ₹0.37 | 9 |
| 2022-08-26 | ₹131.75 | ₹4.34 | 9 |
| 2022-09-30 | ₹132.06 | ₹16.43 | 8 |
| 2022-10-28 | ₹134.99 | ₹14.65 | 8 |
| 2022-11-25 | ₹143.20 | ₹0.68 | 9 |
| 2022-12-30 | ₹133.86 | ₹90.35 | 3 |
| 2023-01-27 | ₹121.67 | ₹0.00 | 10 |
| 2023-02-24 | ₹119.18 | ₹23.44 | 8 |
| 2023-03-31 | ₹122.10 | ₹41.73 | 6 |
| 2023-04-28 | ₹130.46 | ₹17.67 | 8 |
| 2023-05-26 | ₹145.86 | ₹4.31 | 9 |
| 2023-06-30 | ₹153.21 | ₹3.50 | 9 |
| 2023-07-28 | ₹154.66 | ₹10.35 | 9 |
| 2023-08-25 | ₹167.37 | ₹0.00 | 10 |
| 2023-09-29 | ₹177.97 | ₹0.00 | 10 |
| 2023-10-27 | ₹181.85 | ₹59.74 | 6 |
| 2023-11-24 | ₹201.49 | ₹4.70 | 9 |
| 2023-12-29 | ₹215.64 | ₹4.70 | 9 |
| 2024-01-25 | ₹215.12 | ₹26.13 | 8 |
| 2024-02-23 | ₹215.72 | ₹27.31 | 8 |
| 2024-03-28 | ₹218.12 | ₹0.00 | 9 |
| 2024-04-26 | ₹221.25 | ₹0.00 | 10 |
| 2024-05-31 | ₹218.51 | ₹16.67 | 9 |
| 2024-06-28 | ₹216.33 | ₹5.75 | 9 |
| 2024-07-26 | ₹208.66 | ₹39.50 | 7 |
| 2024-08-30 | ₹225.92 | ₹0.00 | 9 |
| 2024-09-27 | ₹240.92 | ₹0.00 | 9 |
| 2024-10-25 | ₹221.41 | ₹88.48 | 6 |
| 2024-11-29 | ₹218.35 | ₹0.00 | 11 |
| 2024-12-27 | ₹224.29 | ₹37.20 | 9 |
| 2025-01-31 | ₹199.27 | ₹78.04 | 7 |
| 2025-02-28 | ₹187.24 | ₹36.31 | 9 |
| 2025-03-27 | ₹204.63 | ₹0.00 | 11 |
| 2025-04-25 | ₹206.56 | ₹25.50 | 9 |
| 2025-05-30 | ₹207.36 | ₹22.11 | 9 |
| 2025-06-27 | ₹213.79 | ₹1.42 | 10 |
| 2025-07-25 | ₹214.19 | ₹2.78 | 10 |
| 2025-08-29 | ₹203.05 | ₹20.80 | 9 |
| 2025-09-26 | ₹207.49 | ₹19.79 | 9 |
| 2025-10-31 | ₹206.02 | ₹44.14 | 9 |
| 2025-11-28 | ₹202.90 | ₹37.45 | 9 |
| 2025-12-26 | ₹212.51 | ₹0.00 | 11 |
| 2026-01-30 | ₹225.82 | ₹0.00 | 10 |
| 2026-02-27 | ₹211.49 | ₹15.47 | 9 |
| 2026-03-27 | ₹184.29 | ₹110.61 | 4 |
| 2026-04-30 | ₹194.60 | ₹1.09 | 10 |
| 2026-05-29 | ₹199.65 | ₹0.00 | 10 |
| 2026-06-25 | ₹209.01 | ₹0.00 | 10 |
| 2026-07-31 | ₹201.28 | ₹22.96 | 9 |
| 2026-08-28 | ₹228.10 | ₹22.12 | 9 |
| 2026-09-11 | ₹234.07 | ₹0.00 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,754.90 | 2,376.52 | +38.4% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,572.90 | 1,242.60 | +59.0% |
| DYCL | 2026-07-27 | 406.00 | 455.45 | 357.26 | +12.2% |
| FLUOROCHEM | 2026-07-27 | 4,653.20 | 4,773.20 | 4,327.53 | +2.6% |
| LIQUID1 | 2024-11-25 | 1,020.63 | 1,122.52 | 1,047.51 | +10.0% |
| MANINDS | 2026-06-08 | 526.00 | 866.10 | 700.58 | +64.7% |
| OMAXE | 2026-08-31 | 131.50 | 123.98 | 89.02 | -5.7% |
| RATNAVEER | 2026-08-03 | 184.99 | 288.30 | 263.29 | +55.8% |
| SWANENERGY | 2025-07-21 | 506.70 | 460.90 | 391.40 | -9.0% |
| TRENT | 2026-04-27 | 2,890.67 | 2,802.40 | 2,668.19 | -3.1% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| HDFCMFGETF | 2020-03-09 | 4,002.50 | 2020-03-13 | 3,540.65 | -11.5% |
| INDOCO | 2020-03-09 | 228.20 | 2020-03-13 | 164.08 | -28.1% |
| LALPATHLAB | 2020-03-09 | 835.00 | 2020-03-13 | 743.38 | -11.0% |
| SETFGOLD | 2020-03-09 | 3,862.80 | 2020-03-17 | 3,548.39 | -8.1% |
| DEEPAKNTR | 2020-03-09 | 508.80 | 2020-03-19 | 356.25 | -30.0% |
| IOLCP | 2020-03-09 | 51.20 | 2020-03-19 | 36.91 | -27.9% |
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| AXISGOLD | 2020-04-13 | 4,049.00 | 2020-07-23 | 3,971.05 | -1.9% |
| MANGCHEFER | 2020-05-11 | 33.75 | 2020-07-31 | 33.73 | -0.1% |
| EIDPARRY | 2020-05-11 | 164.00 | 2020-08-17 | 273.03 | +66.5% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| GOLDBEES | 2020-04-13 | 41.24 | 2020-09-04 | 41.00 | -0.6% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| KIRLOSBROS | 2020-07-27 | 122.55 | 2020-09-08 | 120.79 | -1.4% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| DEEPAKFERT | 2020-08-03 | 166.45 | 2020-09-22 | 154.26 | -7.3% |
| HDFCMFGETF | 2020-04-20 | 4,385.40 | 2020-09-23 | 4,492.07 | +2.4% |
| AARTIDRUGS | 2020-08-24 | 3,250.00 | 2020-09-30 | 2,264.30 | -30.3% |
| PRINCEPIPE | 2020-09-28 | 246.95 | 2020-10-12 | 220.88 | -10.6% |
| GLOBUSSPR | 2020-09-14 | 255.55 | 2020-10-30 | 287.85 | +12.6% |
| ALEMBICLTD | 2020-06-22 | 81.65 | 2020-11-02 | 91.41 | +12.0% |
| ADVENZYMES | 2020-08-24 | 241.50 | 2020-11-03 | 292.33 | +21.0% |
| VIDHIING | 2020-10-05 | 137.00 | 2020-12-02 | 115.50 | -15.7% |
| TATAMTRDVR | 2020-09-14 | 61.20 | 2020-12-21 | 69.87 | +14.2% |
| ESTER | 2020-11-02 | 121.85 | 2020-12-21 | 101.25 | -16.9% |
| LASA | 2020-11-09 | 80.50 | 2020-12-21 | 77.95 | -3.2% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| KIRIINDUS | 2020-12-28 | 537.55 | 2021-01-21 | 478.56 | -11.0% |
| PANACEABIO | 2020-12-07 | 214.50 | 2021-01-22 | 197.40 | -8.0% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| XCHANGING | 2020-12-28 | 88.00 | 2021-01-25 | 80.75 | -8.2% |
| HFCL | 2020-12-28 | 25.60 | 2021-01-28 | 28.12 | +9.8% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| LTI | 2020-10-19 | 3,090.35 | 2021-02-25 | 3,676.50 | +19.0% |
| INDIAMART | 2021-01-25 | 3,990.00 | 2021-03-02 | 4,137.25 | +3.7% |
| DCW | 2021-01-25 | 23.00 | 2021-03-18 | 25.79 | +12.1% |
| RAYMOND | 2021-03-08 | 390.90 | 2021-03-18 | 349.65 | -10.6% |
| APTECHT | 2020-12-28 | 154.75 | 2021-03-19 | 204.25 | +32.0% |
| HINDZINC | 2021-01-25 | 277.40 | 2021-03-19 | 279.30 | +0.7% |
| MHRIL | 2021-02-01 | 224.00 | 2021-03-19 | 210.90 | -5.8% |
| MAHABANK | 2021-03-01 | 25.20 | 2021-03-19 | 18.37 | -27.1% |
| MANALIPETC | 2021-03-01 | 67.00 | 2021-03-19 | 58.28 | -13.0% |
| CENTENKA | 2021-03-22 | 264.00 | 2021-03-25 | 229.90 | -12.9% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| PRAKASH | 2021-03-22 | 67.15 | 2021-04-19 | 74.58 | +11.1% |
| POLYMED | 2020-09-07 | 449.70 | 2021-06-14 | 950.00 | +111.3% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| WELSPUNIND | 2021-03-22 | 81.45 | 2021-08-10 | 124.64 | +53.0% |
| MOREPENLAB | 2021-04-26 | 50.90 | 2021-08-10 | 56.33 | +10.7% |
| TATACOFFEE | 2021-01-25 | 118.70 | 2021-08-11 | 192.49 | +62.2% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| SCHAND | 2021-03-22 | 123.00 | 2021-08-17 | 115.06 | -6.5% |
| GDL | 2021-02-01 | 159.15 | 2021-09-20 | 266.00 | +67.1% |
| INSECTICID | 2021-06-21 | 750.00 | 2021-10-20 | 673.55 | -10.2% |
| FDC | 2021-06-21 | 342.00 | 2021-10-21 | 328.04 | -4.1% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| RPGLIFE | 2021-09-27 | 700.00 | 2021-10-29 | 628.09 | -10.3% |
| DEEPAKFERT | 2021-03-22 | 237.00 | 2021-11-18 | 368.55 | +55.5% |
| SHOPERSTOP | 2021-10-25 | 326.00 | 2021-11-22 | 335.82 | +3.0% |
| POKARNA | 2021-08-16 | 497.00 | 2021-11-26 | 574.75 | +15.6% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| NHPC | 2021-10-25 | 32.90 | 2021-11-29 | 30.11 | -8.5% |
| DELTACORP | 2021-09-27 | 242.50 | 2021-12-01 | 244.67 | +0.9% |
| SUPRAJIT | 2021-11-22 | 454.00 | 2021-12-13 | 391.40 | -13.8% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| MINDAIND | 2021-12-20 | 1,026.00 | 2022-01-07 | 1,088.41 | +6.1% |
| LTI | 2021-10-25 | 6,555.00 | 2022-01-24 | 6,270.00 | -4.3% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| GABRIEL | 2021-08-16 | 149.30 | 2022-02-14 | 125.40 | -16.0% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| SUZLON | 2022-01-10 | 11.15 | 2022-02-15 | 9.79 | -12.2% |
| RAJESHEXPO | 2021-12-06 | 751.80 | 2022-02-24 | 748.32 | -0.5% |
| SIS | 2022-02-14 | 532.95 | 2022-02-24 | 470.91 | -11.6% |
| ESCORTS | 2021-11-29 | 1,875.00 | 2022-02-25 | 1,754.65 | -6.4% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| EXCELINDUS | 2022-03-07 | 1,523.00 | 2022-03-29 | 1,438.30 | -5.6% |
| EVERESTIND | 2022-02-21 | 740.00 | 2022-04-28 | 594.70 | -19.6% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
| SRHHYPOLTD | 2022-03-07 | 408.00 | 2022-05-05 | 431.30 | +5.7% |
| INOXLEISUR | 2022-04-04 | 520.85 | 2022-05-06 | 470.35 | -9.7% |
| MAWANASUG | 2022-03-07 | 115.00 | 2022-05-09 | 135.09 | +17.5% |
| ORISSAMINE | 2022-05-02 | 3,379.00 | 2022-05-11 | 2,898.50 | -14.2% |
| MFL | 2022-05-02 | 1,430.00 | 2022-05-11 | 1,225.50 | -14.3% |
| MOL | 2022-05-09 | 129.80 | 2022-05-11 | 113.62 | -12.5% |
| RIIL | 2021-12-27 | 845.00 | 2022-05-26 | 863.73 | +2.2% |
| BCG | 2021-11-29 | 134.10 | 2022-06-06 | 55.00 | -59.0% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| GRAUWEIL | 2022-05-23 | 82.70 | 2022-06-13 | 61.82 | -25.2% |
| MRPL | 2022-05-09 | 78.00 | 2022-07-06 | 69.61 | -10.8% |
| JKIL | 2022-05-09 | 229.70 | 2022-08-05 | 308.80 | +34.4% |
| ICICIGOLD | 2022-03-14 | 46.20 | 2022-08-29 | 41.50 | -10.2% |
| MARATHON | 2022-07-11 | 215.00 | 2022-09-19 | 232.80 | +8.3% |
| BFUTILITIE | 2022-09-26 | 439.65 | 2022-09-27 | 412.40 | -6.2% |
| VADILALIND | 2022-05-23 | 1,805.00 | 2022-10-20 | 2,295.06 | +27.2% |
| MANGCHEFER | 2022-08-08 | 125.00 | 2022-10-27 | 117.89 | -5.7% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| TDPOWERSYS | 2022-09-05 | 120.00 | 2022-11-09 | 103.50 | -13.8% |
| ALLCARGO | 2022-10-03 | 413.00 | 2022-11-29 | 432.77 | +4.8% |
| SATIA | 2022-10-31 | 161.25 | 2022-12-05 | 138.51 | -14.1% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-06-06 | 238.05 | 2022-12-22 | 345.56 | +45.2% |
| BESTAGRO | 2022-10-24 | 1,607.00 | 2022-12-22 | 1,453.50 | -9.6% |
| RICOAUTO | 2022-12-05 | 77.50 | 2022-12-22 | 75.43 | -2.7% |
| ACC | 2022-05-23 | 2,260.00 | 2022-12-23 | 2,465.16 | +9.1% |
| RVNL | 2022-11-14 | 51.45 | 2022-12-26 | 60.57 | +17.7% |
| WESTLIFE | 2022-11-07 | 763.50 | 2023-01-16 | 708.51 | -7.2% |
| BAJAJHIND | 2022-12-12 | 15.75 | 2023-01-30 | 13.98 | -11.2% |
| GICRE | 2023-01-02 | 179.20 | 2023-02-01 | 167.72 | -6.4% |
| CGCL | 2022-03-07 | 600.00 | 2023-02-17 | 704.95 | +17.5% |
| PSB | 2023-01-02 | 33.70 | 2023-02-21 | 25.55 | -24.2% |
| SPIC | 2023-01-02 | 88.25 | 2023-02-23 | 65.74 | -25.5% |
| IOB | 2023-01-02 | 32.40 | 2023-03-20 | 22.18 | -31.5% |
| UCOBANK | 2023-01-02 | 31.80 | 2023-03-27 | 23.46 | -26.2% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| CIGNITITEC | 2023-02-20 | 731.95 | 2023-03-29 | 705.14 | -3.7% |
| SONATSOFTW | 2023-02-27 | 360.00 | 2023-03-29 | 371.45 | +3.2% |
| JSL | 2023-01-02 | 241.00 | 2023-04-13 | 256.98 | +6.6% |
| CERA | 2023-02-27 | 6,150.00 | 2023-04-26 | 6,037.30 | -1.8% |
| NUCLEUS | 2023-03-27 | 641.00 | 2023-06-23 | 1,020.80 | +59.3% |
| MOLDTECH | 2023-02-06 | 189.00 | 2023-07-03 | 292.84 | +54.9% |
| ANURAS | 2023-04-17 | 995.20 | 2023-07-03 | 1,007.67 | +1.3% |
| HARIOMPIPE | 2023-01-02 | 363.95 | 2023-07-10 | 603.25 | +65.8% |
| DISHTV | 2023-07-17 | 19.55 | 2023-07-28 | 17.29 | -11.6% |
| CPSEETF | 2023-04-03 | 40.00 | 2023-07-31 | 41.97 | +4.9% |
| DHAMPURSUG | 2023-06-26 | 286.80 | 2023-08-18 | 253.65 | -11.6% |
| JAICORPLTD | 2023-08-21 | 213.05 | 2023-09-12 | 207.10 | -2.8% |
| SETFGOLD | 2023-04-10 | 52.60 | 2023-10-03 | 49.74 | -5.4% |
| SJVN | 2023-07-10 | 48.00 | 2023-10-23 | 66.03 | +37.6% |
| DEN | 2023-10-09 | 50.90 | 2023-10-23 | 46.98 | -7.7% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| MANINFRA | 2023-07-31 | 122.95 | 2023-10-26 | 140.65 | +14.4% |
| ANGELONE | 2023-10-30 | 253.50 | 2024-01-23 | 296.88 | +17.1% |
| KECL | 2023-01-23 | 86.55 | 2024-02-12 | 133.00 | +53.7% |
| SAKSOFT | 2023-05-02 | 200.25 | 2024-02-12 | 305.02 | +52.3% |
| ASHAPURMIN | 2023-08-07 | 193.45 | 2024-02-19 | 389.50 | +101.3% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| BOMDYEING | 2023-09-18 | 153.70 | 2024-03-11 | 164.59 | +7.1% |
| KCP | 2024-02-19 | 216.95 | 2024-03-12 | 167.91 | -22.6% |
| GSPL | 2024-01-29 | 360.00 | 2024-03-14 | 331.55 | -7.9% |
| KALYANKJIL | 2023-07-10 | 163.75 | 2024-04-18 | 401.04 | +144.9% |
| ZENTEC | 2023-07-17 | 595.40 | 2024-05-09 | 896.89 | +50.6% |
| SUNDARMFIN | 2024-02-26 | 4,223.15 | 2024-05-09 | 4,431.80 | +4.9% |
| JUSTDIAL | 2024-04-22 | 1,084.00 | 2024-05-09 | 1,008.00 | -7.0% |
| SURYODAY | 2024-04-22 | 213.80 | 2024-05-22 | 193.85 | -9.3% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| SMSPHARMA | 2024-03-11 | 179.00 | 2024-06-04 | 181.36 | +1.3% |
| SOLARINDS | 2024-03-18 | 8,900.05 | 2024-06-04 | 7,980.95 | -10.3% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| CENTURYTEX | 2024-05-13 | 2,000.00 | 2024-06-04 | 1,715.70 | -14.2% |
| PGEL | 2024-05-27 | 262.00 | 2024-06-04 | 237.50 | -9.4% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| HINDMOTORS | 2024-05-13 | 42.00 | 2024-07-23 | 29.67 | -29.4% |
| NCC | 2024-06-10 | 327.60 | 2024-07-23 | 297.87 | -9.1% |
| THERMAX | 2024-06-03 | 5,640.00 | 2024-08-05 | 4,719.70 | -16.3% |
| ENDURANCE | 2024-06-10 | 2,439.90 | 2024-08-05 | 2,429.11 | -0.4% |
| JWL | 2024-05-13 | 490.00 | 2024-08-06 | 552.00 | +12.7% |
| PANAMAPET | 2024-06-10 | 383.00 | 2024-10-03 | 384.27 | +0.3% |
| HINDOILEXP | 2024-07-29 | 270.00 | 2024-10-07 | 220.07 | -18.5% |
| CEATLTD | 2024-07-22 | 2,645.95 | 2024-10-18 | 2,745.55 | +3.8% |
| GODFRYPHLP | 2024-02-19 | 2,547.70 | 2024-10-22 | 6,258.93 | +145.7% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| GENESYS | 2024-07-29 | 488.67 | 2024-10-25 | 451.09 | -7.7% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| TBZ | 2024-08-12 | 161.01 | 2024-11-13 | 236.93 | +47.2% |
| ASTRAZEN | 2024-10-07 | 7,442.65 | 2024-11-14 | 6,854.77 | -7.9% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| HIMATSEIDE | 2024-10-21 | 164.15 | 2025-01-13 | 174.80 | +6.5% |
| CARERATING | 2024-11-04 | 1,510.00 | 2025-01-13 | 1,239.70 | -17.9% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| 63MOONS | 2024-11-04 | 595.00 | 2025-01-22 | 790.40 | +32.8% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| APOLLO | 2025-01-20 | 131.50 | 2025-02-17 | 110.19 | -16.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| TAJGVK | 2025-01-06 | 446.90 | 2025-04-02 | 453.34 | +1.4% |
| BAJAJHCARE | 2025-01-20 | 690.00 | 2025-04-07 | 521.14 | -24.5% |
| HDFCGOLD | 2025-02-10 | 75.80 | 2025-04-07 | 71.44 | -5.8% |
| SETFGOLD | 2025-02-17 | 76.80 | 2025-04-07 | 69.36 | -9.7% |
| ITDCEM | 2024-08-12 | 561.45 | 2025-04-11 | 524.92 | -6.5% |
| GRMOVER | 2025-03-10 | 252.00 | 2025-05-07 | 290.80 | +15.4% |
| VADILALIND | 2025-04-07 | 4,820.55 | 2025-05-30 | 5,401.40 | +12.0% |
| PREMEXPLN | 2025-05-12 | 483.95 | 2025-07-14 | 537.70 | +11.1% |
| MIDHANI | 2025-06-02 | 423.80 | 2025-08-01 | 393.30 | -7.2% |
| JSWHL | 2024-11-18 | 19,990.00 | 2025-08-04 | 19,106.01 | -4.4% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| THYROCARE | 2025-08-04 | 1,324.90 | 2025-09-15 | 1,184.93 | -10.6% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| EVEREADY | 2025-09-08 | 467.15 | 2025-10-06 | 373.49 | -20.0% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| TFCILTD | 2025-04-28 | 37.60 | 2025-10-30 | 69.12 | +83.8% |
| NETWEB | 2025-09-29 | 3,700.00 | 2025-11-06 | 3,515.95 | -5.0% |
| PRAKASH | 2025-08-11 | 178.70 | 2025-11-14 | 147.31 | -17.6% |
| TDPOWERSYS | 2025-11-03 | 764.55 | 2025-11-24 | 714.97 | -6.5% |
| SKYGOLD | 2025-10-27 | 370.00 | 2025-11-25 | 329.13 | -11.0% |
| PARAGMILK | 2025-11-17 | 354.00 | 2025-12-09 | 293.55 | -17.1% |
| LUMAXIND | 2025-12-01 | 5,671.00 | 2026-01-01 | 5,078.70 | -10.4% |
| SJS | 2025-11-10 | 1,695.00 | 2026-01-20 | 1,596.00 | -5.8% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| GMRAIRPORT | 2025-12-15 | 103.95 | 2026-01-23 | 92.10 | -11.4% |
| GOLDBEES | 2025-10-13 | 102.60 | 2026-02-02 | 113.05 | +10.2% |
| TATSILV | 2026-01-27 | 32.00 | 2026-02-02 | 23.03 | -28.0% |
| APEX | 2026-02-09 | 355.00 | 2026-02-27 | 389.22 | +9.6% |
| GOLDIETF | 2025-03-10 | 74.30 | 2026-03-23 | 115.68 | +55.7% |
| HDFCSILVER | 2025-09-22 | 127.30 | 2026-03-23 | 201.50 | +58.3% |
| SILVERBEES | 2026-01-05 | 222.90 | 2026-03-23 | 196.78 | -11.7% |
| SILVERIETF | 2026-01-27 | 335.00 | 2026-03-23 | 208.50 | -37.8% |
| HDFCGOLD | 2026-01-27 | 135.17 | 2026-03-23 | 114.75 | -15.1% |
| J&KBANK | 2026-03-02 | 116.20 | 2026-03-23 | 110.67 | -4.8% |
| MAHABANK | 2025-11-03 | 59.70 | 2026-03-30 | 61.05 | +2.3% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| BAJAJHIND | 2026-04-06 | 17.08 | 2026-05-14 | 17.96 | +5.2% |
| CPSEETF | 2026-02-09 | 99.82 | 2026-06-02 | 100.15 | +0.3% |
| NLCINDIA | 2026-04-20 | 303.60 | 2026-06-09 | 320.62 | +5.6% |
| MARKSANS | 2026-05-18 | 209.56 | 2026-07-22 | 244.62 | +16.7% |
| NRBBEARING | 2026-06-15 | 438.00 | 2026-07-22 | 391.97 | -10.5% |
| OFSS | 2026-04-27 | 9,050.00 | 2026-07-23 | 10,241.00 | +13.2% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.64 | +19.8% |
| GABRIEL | 2026-07-27 | 1,370.10 | 2026-08-25 | 1,349.19 | -1.5% |

## The complete trade blotter

*Buys, sells and tax settlements; every stop raise, starved signal and refused signal is in `_longrun_events_2020-03-01_to_2026-09-11.csv` (2533 events in all).*

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
2020-05-11  EIDPARRY    BUY ₹8.80 at ₹164.00 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 1.53×, ladder rising; stop ₹132.60; charges ₹0.01)
2020-05-11  IOLCP       BUY ₹8.67 at ₹66.18 (fresh Friday signal — BUY: 2.18× weekly, month 2.73×, ladder rising; stop ₹51.22; charges ₹0.01)
2020-05-11  MANGCHEFER  BUY ₹8.81 at ₹33.75 (fresh Friday signal — BUY: 2.54× weekly, month 2.97×, ladder rising; stop ₹29.50; charges ₹0.01)
2020-06-12  DEEPAKNTR   SELL ₹8.80 at stop ₹474.05 (-0.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-06-15  PANACEABIO  BUY ₹8.80 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.27×, ladder rising; stop ₹114.11; charges ₹0.01)
2020-06-16  IOLCP       SELL ₹9.07 at stop ₹69.35 (+4.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-06-22  ALEMBICLTD  BUY ₹9.07 at ₹81.65 (fresh Friday signal — starved 1×, front of the queue — BUY: 11.73× weekly, month 8.56×, ladder rising; stop ₹44.84; charges ₹0.01)
2020-07-23  AXISGOLD    SELL ₹8.63 at stop ₹3,971.05 (-1.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-07-27  KIRLOSBROS  BUY ₹8.63 at ₹122.55 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 9.32× weekly, month 6.82×, ladder rising; stop ₹97.15; charges ₹0.01)
2020-07-31  MANGCHEFER  SELL ₹8.78 at stop ₹33.73 (-0.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-08-03  DEEPAKFERT  BUY ₹8.78 at ₹166.45 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.28× weekly, month 3.19×, ladder rising; stop ₹106.88; charges ₹0.01)
2020-08-17  EIDPARRY    SELL ₹14.62 at stop ₹273.03 (+66.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-08-20  PANACEABIO  SELL ₹7.02 at stop ₹184.01 (-20.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-08-24  AARTIDRUGS  BUY ₹10.21 at ₹3,250.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 5.29× weekly, month 7.63×, ladder rising; stop ₹1,888.30; charges ₹0.01)
2020-08-24  ADVENZYMES  BUY ₹10.27 at ₹241.50 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.06× weekly, month 7.95×, ladder rising; stop ₹194.75; charges ₹0.01)
2020-09-04  GOLDBEES    SELL ₹8.73 at stop ₹41.00 (-0.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-07  POLYMED     BUY ₹9.86 at ₹449.70 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.13× weekly, month 2.67×, ladder rising; stop ₹372.40; charges ₹0.01)
2020-09-08  CADILAHC    SELL ₹9.81 at stop ₹364.99 (+10.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-08  KIRLOSBROS  SELL ₹8.49 at stop ₹120.79 (-1.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-14  GLOBUSSPR   BUY ₹8.03 at ₹255.55 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.82× weekly, month 2.49×, ladder rising; stop ₹163.88; charges ₹0.01)
2020-09-14  TATAMTRDVR  BUY ₹10.31 at ₹61.20 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.20× weekly, month 2.63×, ladder rising; stop ₹47.02; charges ₹0.01)
2020-09-22  DEEPAKFERT  SELL ₹8.12 at stop ₹154.26 (-7.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹8.42 at stop ₹126.45 (-5.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-23  HDFCMFGETF  SELL ₹9.05 at stop ₹4,492.07 (+2.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-09-28  PRINCEPIPE  BUY ₹10.53 at ₹246.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.56× weekly, month 1.74×, ladder rising; stop ₹178.66; charges ₹0.01)
2020-09-28  SAKSOFT     BUY ₹10.55 at ₹398.70 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.01)
2020-09-30  AARTIDRUGS  SELL ₹7.10 at stop ₹2,264.30 (-30.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-10-05  VIDHIING    BUY ₹10.43 at ₹137.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.31× weekly, month 5.81×, ladder rising; stop ₹77.90; charges ₹0.01)
2020-10-12  PRINCEPIPE  SELL ₹9.40 at stop ₹220.88 (-10.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-10-19  LTI         BUY ₹10.11 at ₹3,090.35 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.35× weekly, month 3.38×, ladder rising; stop ₹2,166.78; charges ₹0.01)
2020-10-30  GLOBUSSPR   SELL ₹9.02 at stop ₹287.85 (+12.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-11-02  ALEMBICLTD  SELL ₹10.13 at stop ₹91.41 (+12.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-11-02  ESTER       BUY ₹9.48 at ₹121.85 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.41× weekly, month 6.14×, ladder rising; stop ₹83.98; charges ₹0.01)
2020-11-03  ADVENZYMES  SELL ₹12.40 at stop ₹292.33 (+21.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹9.67 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.01)
2020-11-09  LASA        BUY ₹9.70 at ₹80.50 (fresh Friday signal — BUY: 3.08× weekly, month 3.28×, ladder rising; stop ₹65.41; charges ₹0.01)
2020-12-02  VIDHIING    SELL ₹8.77 at stop ₹115.50 (-15.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-12-07  PANACEABIO  BUY ₹10.56 at ₹214.50 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.55× weekly, month 1.90×, ladder rising; stop ₹183.35; charges ₹0.01)
2020-12-21  ESTER       SELL ₹7.86 at stop ₹101.25 (-16.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-12-21  LASA        SELL ₹9.37 at stop ₹77.95 (-3.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-12-21  TATAMTRDVR  SELL ₹11.75 at stop ₹69.87 (+14.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2020-12-22  SYNGENE     SELL ₹15.67 at stop ₹562.40 (+76.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2020-12-28  APTECHT     BUY ₹11.58 at ₹154.75 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.24× weekly, month 2.88×, ladder rising; stop ₹123.03; charges ₹0.01)
2020-12-28  HFCL        BUY ₹11.23 at ₹25.60 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.33× weekly, month 3.95×, ladder rising; stop ₹19.05; charges ₹0.01)
2020-12-28  KIRIINDUS   BUY ₹11.62 at ₹537.55 (fresh Friday signal — starved 1×, front of the queue — BUY: 8.73× weekly, month 2.26×, ladder rising; stop ₹424.46; charges ₹0.01)
2020-12-28  XCHANGING   BUY ₹11.59 at ₹88.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 3.95× weekly, month 3.92×, ladder rising; stop ₹71.32; charges ₹0.01)
2021-01-20  BORORENEW   SELL ₹23.97 at stop ₹247.59 (+148.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-01-21  KIRIINDUS   SELL ₹10.32 at stop ₹478.56 (-11.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-01-22  PANACEABIO  SELL ₹9.70 at stop ₹197.40 (-8.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-01-25  DCW         BUY ₹11.54 at ₹23.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.09× weekly, month 1.83×, ladder rising; stop ₹16.00; charges ₹0.01)
2021-01-25  HINDZINC    BUY ₹11.58 at ₹277.40 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.32× weekly, month 2.11×, ladder rising; stop ₹248.97; charges ₹0.01)
2021-01-25  INDIAMART   BUY ₹11.45 at ₹3,990.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.37× weekly, month 1.58×, ladder rising; stop ₹3,323.19; charges ₹0.01)
2021-01-25  SAKSOFT     SELL ₹9.01 at stop ₹341.10 (-14.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-01-25  TATACOFFEE  BUY ₹9.42 at ₹118.70 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.30× weekly, month 2.15×, ladder rising; stop ₹102.65; charges ₹0.01)
2021-01-25  XCHANGING   SELL ₹10.62 at stop ₹80.75 (-8.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-01-28  HFCL        SELL ₹12.31 at stop ₹28.12 (+9.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-02-01  GAEL        BUY ₹11.30 at ₹71.47 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.01)
2021-02-01  GDL         BUY ₹11.29 at ₹159.15 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.82× weekly, month 6.27×, ladder rising; stop ₹92.41; charges ₹0.01)
2021-02-01  MHRIL       BUY ₹9.34 at ₹224.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.64× weekly, month 1.67×, ladder rising; stop ₹200.74; charges ₹0.01)
2021-02-23  GAEL        SELL ₹9.89 at stop ₹62.70 (-12.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-02-25  LTI         SELL ₹12.00 at stop ₹3,676.50 (+19.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-01  MAHABANK    BUY ₹12.66 at ₹25.20 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 3.28× weekly, month 6.37×, ladder rising; stop ₹18.37; charges ₹0.01)
2021-03-01  MANALIPETC  BUY ₹9.23 at ₹67.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.27× weekly, month 4.11×, ladder rising; stop ₹44.17; charges ₹0.01)
2021-03-02  INDIAMART   SELL ₹11.84 at stop ₹4,137.25 (+3.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-08  RAYMOND     BUY ₹11.84 at ₹390.90 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.51× weekly, month 2.21×, ladder rising; stop ₹349.65; charges ₹0.01)
2021-03-18  DCW         SELL ₹12.91 at stop ₹25.79 (+12.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-18  RAYMOND     SELL ₹10.57 at stop ₹349.65 (-10.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹15.25 at stop ₹204.25 (+32.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-03-19  HINDZINC    SELL ₹11.64 at stop ₹279.30 (+0.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-19  MAHABANK    SELL ₹9.21 at stop ₹18.37 (-27.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-19  MANALIPETC  SELL ₹8.01 at stop ₹58.28 (-13.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-19  MHRIL       SELL ₹8.78 at stop ₹210.90 (-5.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-22  CENTENKA    BUY ₹11.66 at ₹264.00 (fresh Friday signal — BUY: 2.04× weekly, month 1.55×, ladder rising; stop ₹229.90; charges ₹0.01)
2021-03-22  DEEPAKFERT  BUY ₹11.66 at ₹237.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.87×, ladder rising; stop ₹184.78; charges ₹0.01)
2021-03-22  KEI         BUY ₹11.60 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.01)
2021-03-22  PRAKASH     BUY ₹11.67 at ₹67.15 (fresh Friday signal — BUY: 2.45× weekly, month 4.02×, ladder rising; stop ₹51.52; charges ₹0.01)
2021-03-22  SCHAND      BUY ₹6.56 at ₹123.00 (fresh Friday signal — BUY: 1.71× weekly, month 8.03×, ladder rising; stop ₹87.12; charges ₹0.01)
2021-03-22  VIDHIING    BUY ₹11.54 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.01)
2021-03-22  WELSPUNIND  BUY ₹11.66 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.42×, ladder rising; stop ₹67.45; charges ₹0.01)
2021-03-25  CENTENKA    SELL ₹10.13 at stop ₹229.90 (-12.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-03-30  CENTRUM     BUY ₹10.13 at ₹28.40 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹0.01)
2021-04-01  CENTRUM     TRIM 1.1% (₹0.11 at ₹28.35) to pay the tax bill
2021-04-01  DEEPAKFERT  TRIM 1.1% (₹0.12 at ₹234.55) to pay the tax bill
2021-04-01  GDL         TRIM 1.1% (₹0.14 at ₹177.90) to pay the tax bill
2021-04-01  KEI         TRIM 1.1% (₹0.13 at ₹528.60) to pay the tax bill
2021-04-01  POLYMED     TRIM 1.1% (₹0.20 at ₹837.20) to pay the tax bill
2021-04-01  PRAKASH     TRIM 1.1% (₹0.15 at ₹81.40) to pay the tax bill
2021-04-01  SCHAND      TRIM 1.1% (₹0.06 at ₹112.50) to pay the tax bill
2021-04-01  TATACOFFEE  TRIM 1.1% (₹0.11 at ₹122.85) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹1.28 paid (STCG ₹6.40 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 1.1% (₹0.13 at ₹207.10) to pay the tax bill
2021-04-01  WELSPUNIND  TRIM 1.1% (₹0.13 at ₹84.75) to pay the tax bill
2021-04-12  CENTRUM     SELL ₹8.77 at stop ₹24.89 (-12.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-04-19  KPRMILL     BUY ₹8.77 at ₹236.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.01)
2021-04-19  PRAKASH     SELL ₹12.79 at stop ₹74.58 (+11.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-04-26  MOREPENLAB  BUY ₹11.71 at ₹50.90 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.98× weekly, month 4.00×, ladder rising; stop ₹28.01; charges ₹0.01)
2021-06-14  POLYMED     SELL ₹20.56 at stop ₹950.00 (+111.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-06-18  VIDHIING    SELL ₹10.69 at stop ₹182.64 (-6.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-06-21  FDC         BUY ₹15.01 at ₹342.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 7.58× weekly, month 2.52×, ladder rising; stop ₹306.90; charges ₹0.02)
2021-06-21  INSECTICID  BUY ₹15.10 at ₹750.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 6.66× weekly, month 2.93×, ladder rising; stop ₹570.00; charges ₹0.02)
2021-08-10  MOREPENLAB  SELL ₹12.93 at stop ₹56.33 (+10.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNIND  SELL ₹17.61 at stop ₹124.64 (+53.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹13.06 at stop ₹352.48 (+49.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-08-11  TATACOFFEE  SELL ₹15.07 at stop ₹192.49 (+62.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹15.84 at ₹3,679.70 (fresh Friday signal — starved 1×, front of the queue — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.02)
2021-08-16  GABRIEL     BUY ₹15.77 at ₹149.30 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.50× weekly, month 3.57×, ladder rising; stop ₹118.77; charges ₹0.02)
2021-08-16  POKARNA     BUY ₹15.83 at ₹497.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.52× weekly, month 1.80×, ladder rising; stop ₹286.08; charges ₹0.02)
2021-08-16  TATAINVEST  BUY ₹13.44 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.02)
2021-08-17  SCHAND      SELL ₹6.06 at stop ₹115.06 (-6.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-09-20  GDL         SELL ₹18.62 at stop ₹266.00 (+67.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-09-27  DELTACORP   BUY ₹9.28 at ₹242.50 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.64× weekly, month 3.63×, ladder rising; stop ₹209.09; charges ₹0.01)
2021-09-27  RPGLIFE     BUY ₹15.40 at ₹700.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.62× weekly, month 4.04×, ladder rising; stop ₹571.90; charges ₹0.02)
2021-10-20  INSECTICID  SELL ₹13.53 at stop ₹673.55 (-10.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-10-21  FDC         SELL ₹14.37 at stop ₹328.04 (-4.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-10-22  KEI         SELL ₹18.72 at stop ₹853.10 (+63.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹13.84 at stop ₹3,220.59 (-12.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-10-25  LTI         BUY ₹15.56 at ₹6,555.00 (fresh Friday signal — BUY: 4.63× weekly, month 1.84×, ladder rising; stop ₹5,353.77; charges ₹0.02)
2021-10-25  NHPC        BUY ₹15.53 at ₹32.90 (fresh Friday signal — BUY: 3.94× weekly, month 2.28×, ladder rising; stop ₹27.60; charges ₹0.02)
2021-10-25  SHOPERSTOP  BUY ₹15.43 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹0.02)
2021-10-29  RPGLIFE     SELL ₹13.79 at stop ₹628.09 (-10.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-11-01  TCIEXP      BUY ₹12.12 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.01)
2021-11-01  TTKPRESTIG  BUY ₹15.59 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.02)
2021-11-18  DEEPAKFERT  SELL ₹17.90 at stop ₹368.55 (+55.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-11-22  SHOPERSTOP  SELL ₹15.86 at stop ₹335.82 (+3.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-11-22  SUPRAJIT    BUY ₹15.24 at ₹454.00 (fresh Friday signal — BUY: 10.19× weekly, month 1.96×, ladder rising; stop ₹309.33; charges ₹0.02)
2021-11-26  POKARNA     SELL ₹18.26 at stop ₹574.75 (+15.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-11-26  TATAINVEST  SELL ₹14.73 at stop ₹1,436.49 (+9.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹14.19 at stop ₹10,070.05 (-8.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-11-29  BCG         BUY ₹14.81 at ₹134.10 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.94× weekly, month 1.58×, ladder rising; stop ₹55.00; charges ₹0.02)
2021-11-29  BSOFT       BUY ₹14.78 at ₹465.20 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.02)
2021-11-29  ESCORTS     BUY ₹14.77 at ₹1,875.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.78× weekly, month 2.18×, ladder rising; stop ₹1,369.04; charges ₹0.02)
2021-11-29  NHPC        SELL ₹14.18 at stop ₹30.11 (-8.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-11-29  RAYMOND     BUY ₹14.76 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.02)
2021-12-01  DELTACORP   SELL ₹9.34 at stop ₹244.67 (+0.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹14.68 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.02)
2021-12-06  RAJESHEXPO  BUY ₹14.68 at ₹751.80 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.81× weekly, month 2.30×, ladder rising; stop ₹662.77; charges ₹0.02)
2021-12-13  SUPRAJIT    SELL ₹13.11 at stop ₹391.40 (-13.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-12-20  MINDAIND    BUY ₹13.86 at ₹1,026.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.05× weekly, month 1.81×, ladder rising; stop ₹787.66; charges ₹0.02)
2021-12-21  TCIEXP      SELL ₹13.47 at stop ₹2,039.74 (+11.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2021-12-27  RIIL        BUY ₹13.47 at ₹845.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.93× weekly, month 4.04×, ladder rising; stop ₹552.18; charges ₹0.02)
2022-01-07  MINDAIND    SELL ₹14.67 at stop ₹1,088.41 (+6.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-01-10  SUZLON      BUY ₹14.67 at ₹11.15 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.86× weekly, month 2.04×, ladder rising; stop ₹6.18; charges ₹0.02)
2022-01-24  LTI         SELL ₹14.85 at stop ₹6,270.00 (-4.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹14.85 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.02)
2022-02-11  SHARDACROP  SELL ₹13.78 at stop ₹545.30 (-7.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹13.46 at stop ₹424.65 (-8.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-02-14  GABRIEL     SELL ₹13.22 at stop ₹125.40 (-16.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-02-14  SIS         BUY ₹13.78 at ₹532.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.96× weekly, month 1.55×, ladder rising; stop ₹470.91; charges ₹0.02)
2022-02-15  RAYMOND     SELL ₹16.79 at stop ₹679.35 (+14.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-02-15  SUZLON      SELL ₹12.85 at stop ₹9.79 (-12.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-02-21  EVERESTIND  BUY ₹14.26 at ₹740.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.34× weekly, month 1.68×, ladder rising; stop ₹522.67; charges ₹0.02)
2022-02-24  RAJESHEXPO  SELL ₹14.58 at stop ₹748.32 (-0.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-02-24  SIS         SELL ₹12.15 at stop ₹470.91 (-11.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-02-25  ESCORTS     SELL ₹13.79 at stop ₹1,754.65 (-6.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-03-07  CGCL        BUY ₹13.24 at ₹600.00 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 3.19×, ladder rising; stop ₹536.75; charges ₹0.02)
2022-03-07  EXCELINDUS  BUY ₹13.10 at ₹1,523.00 (fresh Friday signal — BUY: 6.93× weekly, month 5.51×, ladder rising; stop ₹1,016.01; charges ₹0.02)
2022-03-07  GTLINFRA    BUY ₹13.21 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.02)
2022-03-07  MAWANASUG   BUY ₹13.20 at ₹115.00 (fresh Friday signal — ACCUMULATE: 2.21× weekly, month 7.30×, ladder rising; stop ₹84.08; charges ₹0.02)
2022-03-07  SRHHYPOLTD  BUY ₹13.17 at ₹408.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 3.20×, ladder rising; stop ₹312.70; charges ₹0.02)
2022-03-14  ICICIGOLD   BUY ₹14.94 at ₹46.20 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.11× weekly, month 3.73×, ladder rising; stop ₹41.50; charges ₹0.02)
2022-03-21  BSE         SELL ₹12.67 at stop ₹1,634.39 (-13.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-03-29  EXCELINDUS  SELL ₹12.35 at stop ₹1,438.30 (-5.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹6.80 paid (STCG ₹34.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  INOXLEISUR  BUY ₹7.16 at ₹520.85 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 7.27× weekly, month 3.35×, ladder rising; stop ₹470.35; charges ₹0.01)
2022-04-04  RCF         BUY ₹12.78 at ₹96.40 (fresh Friday signal — starved 2×, front of the queue — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.02)
2022-04-28  EVERESTIND  SELL ₹11.43 at stop ₹594.70 (-19.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-04-29  GTLINFRA    SELL ₹10.93 at stop ₹1.41 (-17.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹9.14 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.01)
2022-05-02  ORISSAMINE  BUY ₹13.22 at ₹3,379.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.63× weekly, month 1.78×, ladder rising; stop ₹2,898.50; charges ₹0.02)
2022-05-04  RCF         SELL ₹12.32 at stop ₹93.15 (-3.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-05-05  SRHHYPOLTD  SELL ₹13.89 at stop ₹431.30 (+5.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-05-06  INOXLEISUR  SELL ₹6.45 at stop ₹470.35 (-9.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-05-09  JKIL        BUY ₹12.35 at ₹229.70 (fresh Friday signal — BUY: 6.96× weekly, month 3.58×, ladder rising; stop ₹192.28; charges ₹0.01)
2022-05-09  MAWANASUG   SELL ₹15.47 at stop ₹135.09 (+17.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-05-09  MOL         BUY ₹12.37 at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹0.01)
2022-05-09  MRPL        BUY ₹7.94 at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹0.01)
2022-05-11  MFL         SELL ₹7.82 at stop ₹1,225.50 (-14.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-05-11  MOL         SELL ₹10.80 at stop ₹113.62 (-12.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-05-11  ORISSAMINE  SELL ₹11.32 at stop ₹2,898.50 (-14.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹11.61 at ₹220.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.01)
2022-05-23  ACC         BUY ₹11.82 at ₹2,260.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹0.01)
2022-05-23  GRAUWEIL    BUY ₹11.79 at ₹82.70 (fresh Friday signal — BUY: 5.06× weekly, month 7.54×, ladder rising; stop ₹56.42; charges ₹0.01)
2022-05-23  VADILALIND  BUY ₹10.18 at ₹1,805.00 (fresh Friday signal — BUY: 1.51× weekly, month 1.94×, ladder rising; stop ₹1,567.50; charges ₹0.01)
2022-05-26  RIIL        SELL ₹13.74 at stop ₹863.73 (+2.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-06-06  BCG         SELL ₹6.06 at stop ₹55.00 (-59.0%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-06-06  SHANTIGEAR  BUY ₹11.16 at ₹238.05 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.57× weekly, month 2.31×, ladder rising; stop ₹179.53; charges ₹0.01)
2022-06-06  VBL         SELL ₹10.34 at stop ₹196.27 (-10.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹11.68 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.01)
2022-06-13  GRAUWEIL    SELL ₹8.80 at stop ₹61.82 (-25.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹10.88 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.01)
2022-07-06  MRPL        SELL ₹7.07 at stop ₹69.61 (-10.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-07-11  MARATHON    BUY ₹11.91 at ₹215.00 (fresh Friday signal — BUY: 2.48× weekly, month 6.64×, ladder rising; stop ₹186.25; charges ₹0.01)
2022-08-05  JKIL        SELL ₹16.57 at stop ₹308.80 (+34.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-08-08  MANGCHEFER  BUY ₹12.60 at ₹125.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.24× weekly, month 1.91×, ladder rising; stop ₹108.58; charges ₹0.01)
2022-08-29  ICICIGOLD   SELL ₹13.39 at stop ₹41.50 (-10.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-09-05  TDPOWERSYS  BUY ₹13.32 at ₹120.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.31× weekly, month 1.78×, ladder rising; stop ₹94.46; charges ₹0.02)
2022-09-19  MARATHON    SELL ₹12.87 at stop ₹232.80 (+8.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-09-26  BFUTILITIE  BUY ₹13.09 at ₹439.65 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.67× weekly, month 4.24×, ladder rising; stop ₹412.40; charges ₹0.02)
2022-09-27  BFUTILITIE  SELL ₹12.25 at stop ₹412.40 (-6.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-10-03  ALLCARGO    BUY ₹13.02 at ₹413.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.01× weekly, month 3.12×, ladder rising; stop ₹336.30; charges ₹0.02)
2022-10-20  VADILALIND  SELL ₹12.91 at stop ₹2,295.06 (+27.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-10-24  BESTAGRO    BUY ₹13.53 at ₹1,607.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.00× weekly, month 2.64×, ladder rising; stop ₹1,207.45; charges ₹0.02)
2022-10-27  MANGCHEFER  SELL ₹11.86 at stop ₹117.89 (-5.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-10-31  SATIA       BUY ₹13.75 at ₹161.25 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.04× weekly, month 1.72×, ladder rising; stop ₹127.06; charges ₹0.02)
2022-11-03  APARINDS    SELL ₹15.52 at stop ₹1,358.50 (+43.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-11-07  WESTLIFE    BUY ₹13.58 at ₹763.50 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.22× weekly, month 1.72×, ladder rising; stop ₹671.22; charges ₹0.02)
2022-11-09  TDPOWERSYS  SELL ₹11.47 at stop ₹103.50 (-13.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-11-14  RVNL        BUY ₹13.62 at ₹51.45 (fresh Friday signal — starved 2×, front of the queue — BUY: 5.86× weekly, month 6.47×, ladder rising; stop ₹37.29; charges ₹0.02)
2022-11-29  ALLCARGO    SELL ₹13.61 at stop ₹432.77 (+4.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-12-05  RICOAUTO    BUY ₹14.25 at ₹77.50 (fresh Friday signal — starved 2×, front of the queue — BUY: 6.07× weekly, month 2.84×, ladder rising; stop ₹48.41; charges ₹0.02)
2022-12-05  SATIA       SELL ₹11.79 at stop ₹138.51 (-14.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-12-12  BAJAJHIND   BUY ₹11.83 at ₹15.75 (fresh Friday signal — starved 3×, front of the queue — BUY: 14.16× weekly, month 2.35×, ladder rising; stop ₹9.93; charges ₹0.01)
2022-12-21  ELECON      SELL ₹19.26 at stop ₹202.49 (+65.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-12-22  BESTAGRO    SELL ₹12.21 at stop ₹1,453.50 (-9.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-12-22  RICOAUTO    SELL ₹13.84 at stop ₹75.43 (-2.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹16.17 at stop ₹345.56 (+45.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹12.86 at stop ₹2,465.16 (+9.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2022-12-26  RVNL        SELL ₹16.00 at stop ₹60.57 (+17.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-01-02  GICRE       BUY ₹10.08 at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 11.18×, ladder rising; stop ₹137.57; charges ₹0.01)
2023-01-02  HARIOMPIPE  BUY ₹13.35 at ₹363.95 (fresh Friday signal — ACCUMULATE: 5.91× weekly, month 2.06×, ladder rising; stop ₹264.86; charges ₹0.02)
2023-01-02  IOB         BUY ₹13.39 at ₹32.40 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 4.77× weekly, month 30.16×, ladder rising; stop ₹21.23; charges ₹0.02)
2023-01-02  JSL         BUY ₹13.37 at ₹241.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.29× weekly, month 2.13×, ladder rising; stop ₹192.61; charges ₹0.02)
2023-01-02  PSB         BUY ₹13.43 at ₹33.70 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.91× weekly, month 32.41×, ladder rising; stop ₹25.45; charges ₹0.02)
2023-01-02  SPIC        BUY ₹13.36 at ₹88.25 (fresh Friday signal — starved 2×, front of the queue — BUY: 4.81× weekly, month 3.70×, ladder rising; stop ₹54.66; charges ₹0.02)
2023-01-02  UCOBANK     BUY ₹13.37 at ₹31.80 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.50× weekly, month 20.22×, ladder rising; stop ₹23.46; charges ₹0.02)
2023-01-16  WESTLIFE    SELL ₹12.57 at stop ₹708.51 (-7.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-01-23  KECL        BUY ₹12.57 at ₹86.55 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.26× weekly, month 2.07×, ladder rising; stop ₹51.00; charges ₹0.01)
2023-01-30  BAJAJHIND   SELL ₹10.48 at stop ₹13.98 (-11.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-02-01  GICRE       SELL ₹9.41 at stop ₹167.72 (-6.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-02-06  JINDALSAW   BUY ₹7.77 at ₹65.22 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.72× weekly, month 3.57×, ladder rising; stop ₹51.25; charges ₹0.01)
2023-02-06  MOLDTECH    BUY ₹12.12 at ₹189.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.10× weekly, month 4.84×, ladder rising; stop ₹142.35; charges ₹0.01)
2023-02-17  CGCL        SELL ₹15.53 at stop ₹704.95 (+17.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-02-20  CIGNITITEC  BUY ₹12.18 at ₹731.95 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.05× weekly, month 1.77×, ladder rising; stop ₹568.10; charges ₹0.01)
2023-02-21  PSB         SELL ₹10.16 at stop ₹25.55 (-24.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-02-23  SPIC        SELL ₹9.93 at stop ₹65.74 (-25.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-02-27  CERA        BUY ₹11.68 at ₹6,150.00 (fresh Friday signal — BUY: 5.94× weekly, month 1.75×, ladder rising; stop ₹5,579.40; charges ₹0.01)
2023-02-27  SONATSOFTW  BUY ₹11.76 at ₹360.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 9.70× weekly, month 3.45×, ladder rising; stop ₹282.62; charges ₹0.01)
2023-03-20  IOB         SELL ₹9.15 at stop ₹22.18 (-31.5%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-03-27  JINDALSAW   SELL ₹8.07 at stop ₹67.92 (+4.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-03-27  NUCLEUS     BUY ₹9.15 at ₹641.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.55× weekly, month 5.08×, ladder rising; stop ₹510.71; charges ₹0.01)
2023-03-27  UCOBANK     SELL ₹9.84 at stop ₹23.46 (-26.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-03-29  CIGNITITEC  SELL ₹11.71 at stop ₹705.14 (-3.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹12.11 at stop ₹371.45 (+3.2%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-04-03  CPSEETF     BUY ₹12.28 at ₹40.00 (fresh Friday signal — ACCUMULATE: 1.80× weekly, month 1.84×, ladder rising; stop ₹36.42; charges ₹0.01)
2023-04-03  HAL         BUY ₹12.28 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.01)
2023-04-03  TAX         FY2023 settled: ₹0.00 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹15.16 / LT ₹0.00)
2023-04-10  SETFGOLD    BUY ₹12.51 at ₹52.60 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.69× weekly, month 2.06×, ladder rising; stop ₹48.56; charges ₹0.01)
2023-04-13  JSL         SELL ₹14.22 at stop ₹256.98 (+6.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-04-17  ANURAS      BUY ₹12.65 at ₹995.20 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.48× weekly, month 5.24×, ladder rising; stop ₹691.46; charges ₹0.01)
2023-04-26  CERA        SELL ₹11.44 at stop ₹6,037.30 (-1.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-05-02  SAKSOFT     BUY ₹13.36 at ₹200.25 (fresh Friday signal — starved 2×, front of the queue — BUY: 5.05× weekly, month 3.30×, ladder rising; stop ₹145.68; charges ₹0.02)
2023-06-23  NUCLEUS     SELL ₹14.54 at stop ₹1,020.80 (+59.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-06-26  DHAMPURSUG  BUY ₹15.34 at ₹286.80 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.56× weekly, month 1.63×, ladder rising; stop ₹253.65; charges ₹0.02)
2023-07-03  ANURAS      SELL ₹12.78 at stop ₹1,007.67 (+1.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-07-03  MOLDTECH    SELL ₹18.74 at stop ₹292.84 (+54.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-07-10  HARIOMPIPE  SELL ₹22.08 at stop ₹603.25 (+65.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-07-10  KALYANKJIL  BUY ₹15.05 at ₹163.75 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.19× weekly, month 2.67×, ladder rising; stop ₹115.42; charges ₹0.02)
2023-07-10  SJVN        BUY ₹15.08 at ₹48.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.63× weekly, month 3.61×, ladder rising; stop ₹38.24; charges ₹0.02)
2023-07-17  DISHTV      BUY ₹11.73 at ₹19.55 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.03× weekly, month 3.10×, ladder rising; stop ₹15.86; charges ₹0.01)
2023-07-17  ZENTEC      BUY ₹15.24 at ₹595.40 (fresh Friday signal — starved 2×, front of the queue — BUY: 8.06× weekly, month 3.59×, ladder rising; stop ₹364.54; charges ₹0.02)
2023-07-28  DISHTV      SELL ₹10.35 at stop ₹17.29 (-11.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-07-31  CPSEETF     SELL ₹12.86 at stop ₹41.97 (+4.9%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-07-31  MANINFRA    BUY ₹10.35 at ₹122.95 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.59× weekly, month 2.10×, ladder rising; stop ₹107.63; charges ₹0.01)
2023-08-07  ASHAPURMIN  BUY ₹12.86 at ₹193.45 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.87× weekly, month 2.42×, ladder rising; stop ₹110.83; charges ₹0.02)
2023-08-18  DHAMPURSUG  SELL ₹13.54 at stop ₹253.65 (-11.6%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-08-21  JAICORPLTD  BUY ₹13.54 at ₹213.05 (fresh Friday signal — starved 2×, front of the queue — BUY: 3.46× weekly, month 1.53×, ladder rising; stop ₹166.82; charges ₹0.02)
2023-09-12  JAICORPLTD  SELL ₹13.13 at stop ₹207.10 (-2.8%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-09-18  BOMDYEING   BUY ₹13.13 at ₹153.70 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 3.03× weekly, month 3.44×, ladder rising; stop ₹117.23; charges ₹0.02)
2023-10-03  SETFGOLD    SELL ₹11.80 at stop ₹49.74 (-5.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-10-09  DEN         BUY ₹11.80 at ₹50.90 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.96× weekly, month 5.99×, ladder rising; stop ₹46.98; charges ₹0.01)
2023-10-23  DEN         SELL ₹10.87 at stop ₹46.98 (-7.7%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-10-23  SJVN        SELL ₹20.70 at stop ₹66.03 (+37.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹16.34 at stop ₹1,840.70 (+33.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2023-10-26  MANINFRA    SELL ₹11.82 at stop ₹140.65 (+14.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2023-10-30  ANGELONE    BUY ₹18.35 at ₹253.50 (fresh Friday signal — BUY: 1.84× weekly, month 2.75×, ladder rising; stop ₹194.37; charges ₹0.02)
2023-10-30  CUPID       BUY ₹18.33 at ₹120.99 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.02)
2023-10-30  SHAREINDIA  BUY ₹18.36 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.02)
2024-01-23  ANGELONE    SELL ₹21.44 at stop ₹296.88 (+17.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-01-29  GSPL        BUY ₹21.60 at ₹360.00 (fresh Friday signal — starved 3×, front of the queue — BUY: 3.79× weekly, month 2.77×, ladder rising; stop ₹296.21; charges ₹0.03)
2024-02-12  KECL        SELL ₹19.28 at stop ₹133.00 (+53.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-02-12  SAKSOFT     SELL ₹20.30 at stop ₹305.02 (+52.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-02-19  ASHAPURMIN  SELL ₹25.83 at stop ₹389.50 (+101.3%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2024-02-19  GODFRYPHLP  BUY ₹21.26 at ₹2,547.70 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 2.18× weekly, month 2.13×, ladder rising; stop ₹2,170.75; charges ₹0.03)
2024-02-19  KCP         BUY ₹21.37 at ₹216.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.57× weekly, month 4.05×, ladder rising; stop ₹167.91; charges ₹0.03)
2024-02-26  SUNDARMFIN  BUY ₹21.60 at ₹4,223.15 (fresh Friday signal — starved 2×, front of the queue — BUY: 5.66× weekly, month 3.04×, ladder rising; stop ₹3,460.23; charges ₹0.03)
2024-03-06  SHAREINDIA  SELL ₹21.81 at stop ₹357.20 (+19.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-03-11  BOMDYEING   SELL ₹14.03 at stop ₹164.59 (+7.1%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2024-03-11  SMSPHARMA   BUY ₹21.91 at ₹179.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 8.20× weekly, month 12.63×, ladder rising; stop ₹132.95; charges ₹0.03)
2024-03-12  KCP         SELL ₹16.50 at stop ₹167.91 (-22.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-03-14  GSPL        SELL ₹19.85 at stop ₹331.55 (-7.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹20.92 at ₹29,500.05 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.02)
2024-03-18  FORCEMOT    BUY ₹14.06 at ₹6,567.70 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.02)
2024-03-18  SOLARINDS   BUY ₹21.01 at ₹8,900.05 (fresh Friday signal — starved 2×, front of the queue — BUY: 4.28× weekly, month 2.84×, ladder rising; stop ₹5,332.29; charges ₹0.02)
2024-04-01  BOSCHLTD    TRIM 3.5% (₹0.75 at ₹30,282.30) to pay the tax bill
2024-04-01  CUPID       TRIM 3.5% (₹0.99 at ₹186.62) to pay the tax bill
2024-04-01  FORCEMOT    TRIM 3.5% (₹0.57 at ₹7,540.95) to pay the tax bill
2024-04-01  GODFRYPHLP  TRIM 3.5% (₹0.91 at ₹3,098.85) to pay the tax bill
2024-04-01  KALYANKJIL  TRIM 3.5% (₹1.37 at ₹425.90) to pay the tax bill
2024-04-01  SMSPHARMA   TRIM 3.5% (₹0.80 at ₹186.05) to pay the tax bill
2024-04-01  SOLARINDS   TRIM 3.5% (₹0.72 at ₹8,726.05) to pay the tax bill
2024-04-01  SUNDARMFIN  TRIM 3.5% (₹0.74 at ₹4,136.60) to pay the tax bill
2024-04-01  TAX         FY2024 settled: ₹7.70 paid (STCG ₹34.29 @20%, LTCG ₹6.74 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-01  ZENTEC      TRIM 3.5% (₹0.85 at ₹945.60) to pay the tax bill
2024-04-18  KALYANKJIL  SELL ₹35.48 at stop ₹401.04 (+144.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-04-22  JUSTDIAL    BUY ₹21.98 at ₹1,084.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 11.71× weekly, month 3.19×, ladder rising; stop ₹821.08; charges ₹0.03)
2024-04-22  SURYODAY    BUY ₹13.50 at ₹213.80 (fresh Friday signal — BUY: 2.34× weekly, month 1.68×, ladder rising; stop ₹127.50; charges ₹0.02)
2024-05-09  JUSTDIAL    SELL ₹20.40 at stop ₹1,008.00 (-7.0%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-05-09  SUNDARMFIN  SELL ₹21.82 at stop ₹4,431.80 (+4.9%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-05-09  ZENTEC      SELL ₹22.10 at stop ₹896.89 (+50.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-05-13  CENTURYTEX  BUY ₹21.31 at ₹2,000.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 3.44× weekly, month 1.97×, ladder rising; stop ₹1,715.70; charges ₹0.03)
2024-05-13  HINDMOTORS  BUY ₹21.27 at ₹42.00 (fresh Friday signal — BUY: 3.62× weekly, month 10.84×, ladder rising; stop ₹26.37; charges ₹0.03)
2024-05-13  JWL         BUY ₹21.34 at ₹490.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 7.12× weekly, month 2.51×, ladder rising; stop ₹370.93; charges ₹0.03)
2024-05-22  SURYODAY    SELL ₹12.22 at stop ₹193.85 (-9.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2024-05-27  PGEL        BUY ₹12.62 at ₹262.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 5.36× weekly, month 2.63×, ladder rising; stop ₹185.72; charges ₹0.01)
2024-05-28  FORCEMOT    SELL ₹16.67 at stop ₹8,083.64 (+23.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-06-03  THERMAX     BUY ₹16.67 at ₹5,640.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.02)
2024-06-04  BOSCHLTD    SELL ₹19.81 at stop ₹29,015.09 (-1.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-06-04  CENTURYTEX  SELL ₹18.24 at stop ₹1,715.70 (-14.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-06-04  PGEL        SELL ₹11.41 at stop ₹237.50 (-9.4%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2024-06-04  SMSPHARMA   SELL ₹21.37 at stop ₹181.36 (+1.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹18.13 at stop ₹7,980.95 (-10.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-06-10  ENDURANCE   BUY ₹20.82 at ₹2,439.90 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.56× weekly, month 2.14×, ladder rising; stop ₹1,964.12; charges ₹0.02)
2024-06-10  NCC         BUY ₹20.76 at ₹327.60 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.80× weekly, month 1.63×, ladder rising; stop ₹260.92; charges ₹0.02)
2024-06-10  PANAMAPET   BUY ₹20.83 at ₹383.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.07× weekly, month 2.01×, ladder rising; stop ₹261.85; charges ₹0.02)
2024-06-10  UNOMINDA    BUY ₹20.81 at ₹970.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.02)
2024-07-19  UNOMINDA    SELL ₹21.01 at stop ₹981.87 (+1.2%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-07-22  CEATLTD     BUY ₹21.09 at ₹2,645.95 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 2.91× weekly, month 1.90×, ladder rising; stop ₹2,479.17; charges ₹0.02)
2024-07-23  HINDMOTORS  SELL ₹14.99 at stop ₹29.67 (-29.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-07-23  NCC         SELL ₹18.83 at stop ₹297.87 (-9.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-07-29  GENESYS     BUY ₹18.48 at ₹488.67 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.61× weekly, month 1.91×, ladder rising; stop ₹384.07; charges ₹0.02)
2024-07-29  HINDOILEXP  BUY ₹21.02 at ₹270.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.01× weekly, month 2.73×, ladder rising; stop ₹209.42; charges ₹0.02)
2024-08-05  ENDURANCE   SELL ₹20.69 at stop ₹2,429.11 (-0.4%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-08-05  THERMAX     SELL ₹13.92 at stop ₹4,719.70 (-16.3%, charges ₹0.01) — the cash goes back to work at the next Friday screen
2024-08-06  JWL         SELL ₹23.99 at stop ₹552.00 (+12.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹20.48 at ₹7,350.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.02)
2024-08-12  ITDCEM      BUY ₹17.65 at ₹561.45 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 3.20× weekly, month 1.67×, ladder rising; stop ₹402.23; charges ₹0.02)
2024-08-12  TBZ         BUY ₹20.45 at ₹161.01 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.88× weekly, month 4.43×, ladder rising; stop ₹124.78; charges ₹0.02)
2024-10-03  PANAMAPET   SELL ₹20.85 at stop ₹384.27 (+0.3%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-10-07  ASTRAZEN    BUY ₹20.85 at ₹7,442.65 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 5.46× weekly, month 6.63×, ladder rising; stop ₹6,768.80; charges ₹0.02)
2024-10-07  HINDOILEXP  SELL ₹17.09 at stop ₹220.07 (-18.5%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-10-14  SKIPPER     BUY ₹17.09 at ₹553.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.85× weekly, month 1.81×, ladder rising; stop ₹418.00; charges ₹0.02)
2024-10-18  CEATLTD     SELL ₹21.84 at stop ₹2,745.55 (+3.8%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-10-21  HIMATSEIDE  BUY ₹21.84 at ₹164.15 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.81× weekly, month 2.25×, ladder rising; stop ₹118.10; charges ₹0.03)
2024-10-22  BASF        SELL ₹21.17 at stop ₹7,611.30 (+3.6%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-10-22  GODFRYPHLP  SELL ₹50.29 at stop ₹6,258.93 (+145.7%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-10-25  GENESYS     SELL ₹17.02 at stop ₹451.09 (-7.7%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-10-28  CUPID       SELL ₹23.14 at stop ₹158.66 (+31.1%, charges ₹0.02) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹19.97 at ₹747.70 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.02)
2024-11-04  63MOONS     BUY ₹21.84 at ₹595.00 (fresh Friday signal — BUY: 2.09× weekly, month 4.03×, ladder rising; stop ₹404.18; charges ₹0.05)
2024-11-04  AKZOINDIA   BUY ₹22.08 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.05)
2024-11-04  CARERATING  BUY ₹22.09 at ₹1,510.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 1.80× weekly, month 4.48×, ladder rising; stop ₹1,066.23; charges ₹0.05)
2024-11-04  KIRLPNU     BUY ₹21.96 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.05)
2024-11-13  TBZ         SELL ₹30.00 at stop ₹236.93 (+47.2%, charges ₹0.07) — the cash goes back to work at the next Friday screen
2024-11-14  ASTRAZEN    SELL ₹19.14 at stop ₹6,854.77 (-7.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-11-18  JSWHL       BUY ₹20.66 at ₹19,990.00 (fresh Friday signal — BUY: 3.46× weekly, month 4.62×, ladder rising; stop ₹8,434.53; charges ₹0.05)
2024-11-25  GARFIBRES   BUY ₹20.96 at ₹956.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.05)
2024-11-25  LIQUID1     BUY ₹11.20 at ₹1,020.63 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.75× weekly, month 2.54×, ladder rising; stop ₹955.12; charges ₹0.03)
2024-12-23  KIRLPNU     SELL ₹20.55 at stop ₹1,596.00 (-6.0%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹16.65 at stop ₹3,423.18 (-24.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2024-12-30  KFINTECH    BUY ₹22.20 at ₹1,511.45 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.05)
2025-01-06  TAJGVK      BUY ₹15.00 at ₹446.90 (fresh Friday signal — starved 1×, front of the queue — BUY: 4.69× weekly, month 2.27×, ladder rising; stop ₹325.01; charges ₹0.04)
2025-01-09  GARFIBRES   SELL ₹18.10 at stop ₹829.35 (-13.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹23.77 at stop ₹893.05 (+19.4%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹14.70 at stop ₹477.28 (-13.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹20.18 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.05)
2025-01-13  CARERATING  SELL ₹18.05 at stop ₹1,239.70 (-17.9%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-01-13  HIMATSEIDE  SELL ₹23.17 at stop ₹174.80 (+6.5%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹20.28 at ₹1,441.90 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.05)
2025-01-15  KFINTECH    SELL ₹16.95 at stop ₹1,159.14 (-23.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-01-20  APOLLO      BUY ₹20.25 at ₹131.50 (fresh Friday signal — starved 3×, front of the queue — ACCUMULATE: 1.93× weekly, month 3.48×, ladder rising; stop ₹110.19; charges ₹0.05)
2025-01-20  BAJAJHCARE  BUY ₹20.55 at ₹690.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.75× weekly, month 4.12×, ladder rising; stop ₹451.06; charges ₹0.05)
2025-01-22  63MOONS     SELL ₹28.88 at stop ₹790.40 (+32.8%, charges ₹0.06) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹16.85 at stop ₹700.36 (-16.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹18.81 at ₹850.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.04)
2025-01-28  LLOYDSME    SELL ₹17.62 at stop ₹1,258.75 (-12.7%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹19.79 at ₹947.00 (fresh Friday signal — BUY: 2.25× weekly, month 2.40×, ladder rising; stop ₹727.84; charges ₹0.05)
2025-02-10  HDFCGOLD    BUY ₹19.71 at ₹75.80 (fresh Friday signal — BUY: 2.22× weekly, month 1.58×, ladder rising; stop ₹64.93; charges ₹0.05)
2025-02-17  APOLLO      SELL ₹16.89 at stop ₹110.19 (-16.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-02-17  SETFGOLD    BUY ₹19.12 at ₹76.80 (fresh Friday signal — BUY: 1.62× weekly, month 1.57×, ladder rising; stop ₹59.71; charges ₹0.05)
2025-03-03  NH          BUY ₹18.61 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.04)
2025-03-03  ZENSARTECH  SELL ₹15.14 at stop ₹727.84 (-23.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2025-03-10  GOLDIETF    BUY ₹13.33 at ₹74.30 (fresh Friday signal — ACCUMULATE: 1.51× weekly, month 1.95×, ladder rising; stop ₹69.50; charges ₹0.03)
2025-03-10  GRMOVER     BUY ₹19.51 at ₹252.00 (fresh Friday signal — BUY: 1.55× weekly, month 1.68×, ladder rising; stop ₹203.86; charges ₹0.05)
2025-04-01  BAJAJHCARE  TRIM 3.4% (₹0.67 at ₹672.90) to pay the tax bill
2025-04-01  CREDITACC   TRIM 3.4% (₹0.72 at ₹966.65) to pay the tax bill
2025-04-01  GOLDIETF    TRIM 3.4% (₹0.47 at ₹78.72) to pay the tax bill
2025-04-01  GRMOVER     TRIM 3.4% (₹0.73 at ₹282.75) to pay the tax bill
2025-04-01  HDFCGOLD    TRIM 3.4% (₹0.69 at ₹78.84) to pay the tax bill
2025-04-01  ITDCEM      TRIM 3.4% (₹0.59 at ₹555.70) to pay the tax bill
2025-04-01  JSWHL       TRIM 3.4% (₹0.81 at ₹23,376.25) to pay the tax bill
2025-04-01  LIQUID1     TRIM 3.4% (₹0.38 at ₹1,043.01) to pay the tax bill
2025-04-01  NH          TRIM 3.4% (₹0.72 at ₹1,676.80) to pay the tax bill
2025-04-01  SETFGOLD    TRIM 3.4% (₹0.65 at ₹78.29) to pay the tax bill
2025-04-01  TAJGVK      TRIM 3.4% (₹0.52 at ₹458.15) to pay the tax bill
2025-04-01  TAX         FY2025 settled: ₹6.96 paid (STCG ₹34.81 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2025-04-02  TAJGVK      SELL ₹14.64 at stop ₹453.34 (+1.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2025-04-07  BAJAJHCARE  SELL ₹14.93 at stop ₹521.14 (-24.5%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2025-04-07  HDFCGOLD    SELL ₹17.87 at stop ₹71.44 (-5.8%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-04-07  SETFGOLD    SELL ₹16.61 at stop ₹69.36 (-9.7%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-04-07  VADILALIND  BUY ₹14.64 at ₹4,820.55 (fresh Friday signal — starved 1×, front of the queue — BUY: 9.88× weekly, month 5.69×, ladder rising; stop ₹4,255.30; charges ₹0.03)
2025-04-11  ITDCEM      SELL ₹15.89 at stop ₹524.92 (-6.5%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹19.86 at ₹818.00 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.05)
2025-04-15  INDIASHLTR  BUY ₹19.93 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.05)
2025-04-28  TFCILTD     BUY ₹20.61 at ₹37.60 (fresh Friday signal — starved 4×, front of the queue — BUY: 1.96× weekly, month 2.55×, ladder rising; stop ₹30.97; charges ₹0.05)
2025-05-07  GRMOVER     SELL ₹21.65 at stop ₹290.80 (+15.4%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2025-05-12  PREMEXPLN   BUY ₹20.77 at ₹483.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.96× weekly, month 5.61×, ladder rising; stop ₹355.08; charges ₹0.05)
2025-05-30  VADILALIND  SELL ₹16.32 at stop ₹5,401.40 (+12.0%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-06-02  MIDHANI     BUY ₹20.69 at ₹423.80 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.22× weekly, month 2.43×, ladder rising; stop ₹370.79; charges ₹0.05)
2025-07-14  PREMEXPLN   SELL ₹22.97 at stop ₹537.70 (+11.1%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2025-07-21  SWANENERGY  BUY ₹21.61 at ₹506.70 (fresh Friday signal — starved 3×, front of the queue — BUY: 6.35× weekly, month 1.78×, ladder rising; stop ₹391.40; charges ₹0.05)
2025-08-01  MIDHANI     SELL ₹19.11 at stop ₹393.30 (-7.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-08-04  JSWHL       SELL ₹18.99 at stop ₹19,106.01 (-4.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹22.41 at stop ₹1,814.78 (+25.2%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2025-08-04  THYROCARE   BUY ₹20.16 at ₹1,324.90 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 1.76× weekly, month 2.24×, ladder rising; stop ₹1,171.92; charges ₹0.05)
2025-08-11  PRAKASH     BUY ₹20.15 at ₹178.70 (fresh Friday signal — starved 2×, front of the queue — ACCUMULATE: 7.16× weekly, month 2.58×, ladder rising; stop ₹145.68; charges ₹0.05)
2025-08-11  RAIN        BUY ₹20.18 at ₹160.25 (fresh Friday signal — starved 3×, front of the queue — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.05)
2025-08-26  RAIN        SELL ₹18.00 at stop ₹143.64 (-10.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-09-08  EVEREADY    BUY ₹20.80 at ₹467.15 (fresh Friday signal — starved 3×, front of the queue — BUY: 1.97× weekly, month 3.01×, ladder rising; stop ₹373.49; charges ₹0.05)
2025-09-15  THYROCARE   SELL ₹17.95 at stop ₹1,184.93 (-10.6%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-09-22  HDFCSILVER  BUY ₹17.95 at ₹127.30 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.93× weekly, month 3.66×, ladder rising; stop ₹112.21; charges ₹0.04)
2025-09-25  INDIASHLTR  SELL ₹19.79 at stop ₹862.60 (-0.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-09-29  NETWEB      BUY ₹19.79 at ₹3,700.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.97× weekly, month 7.27×, ladder rising; stop ₹2,674.79; charges ₹0.05)
2025-10-06  EVEREADY    SELL ₹16.56 at stop ₹373.49 (-20.0%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-10-13  GOLDBEES    BUY ₹16.56 at ₹102.60 (fresh Friday signal — starved 3×, front of the queue — BUY: 3.01× weekly, month 2.39×, ladder rising; stop ₹88.72; charges ₹0.04)
2025-10-20  CREDITACC   SELL ₹27.12 at stop ₹1,274.42 (+49.9%, charges ₹0.06) — the cash goes back to work at the next Friday screen
2025-10-27  SKYGOLD     BUY ₹20.70 at ₹370.00 (fresh Friday signal — BUY: 1.65× weekly, month 2.25×, ladder rising; stop ₹304.38; charges ₹0.05)
2025-10-30  TFCILTD     SELL ₹37.71 at stop ₹69.12 (+83.8%, charges ₹0.08) — the cash goes back to work at the next Friday screen
2025-11-03  MAHABANK    BUY ₹20.54 at ₹59.70 (fresh Friday signal — starved 4×, front of the queue — ACCUMULATE: 2.08× weekly, month 1.69×, ladder rising; stop ₹53.69; charges ₹0.05)
2025-11-03  TDPOWERSYS  BUY ₹20.54 at ₹764.55 (fresh Friday signal — starved 2×, front of the queue — BUY: 4.87× weekly, month 1.95×, ladder rising; stop ₹553.57; charges ₹0.05)
2025-11-06  NETWEB      SELL ₹18.72 at stop ₹3,515.95 (-5.0%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-11-10  SJS         BUY ₹20.30 at ₹1,695.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 4.19× weekly, month 1.96×, ladder rising; stop ₹1,347.19; charges ₹0.05)
2025-11-14  PRAKASH     SELL ₹16.53 at stop ₹147.31 (-17.6%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-11-17  PARAGMILK   BUY ₹18.01 at ₹354.00 (fresh Friday signal — starved 4×, front of the queue — BUY: 3.48× weekly, month 2.34×, ladder rising; stop ₹293.55; charges ₹0.04)
2025-11-24  TDPOWERSYS  SELL ₹19.12 at stop ₹714.97 (-6.5%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-11-25  SKYGOLD     SELL ₹18.33 at stop ₹329.13 (-11.0%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2025-12-01  LUMAXIND    BUY ₹17.01 at ₹5,671.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.57× weekly, month 1.94×, ladder rising; stop ₹4,702.50; charges ₹0.04)
2025-12-01  SANSERA     BUY ₹20.44 at ₹1,749.60 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.05)
2025-12-09  PARAGMILK   SELL ₹14.86 at stop ₹293.55 (-17.1%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2025-12-15  GMRAIRPORT  BUY ₹14.86 at ₹103.95 (fresh Friday signal — starved 1×, front of the queue — BUY: 1.56× weekly, month 2.60×, ladder rising; stop ₹89.73; charges ₹0.04)
2026-01-01  LUMAXIND    SELL ₹15.16 at stop ₹5,078.70 (-10.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2026-01-05  SILVERBEES  BUY ₹15.16 at ₹222.90 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.57× weekly, month 3.68×, ladder rising; stop ₹118.89; charges ₹0.04)
2026-01-20  SJS         SELL ₹19.03 at stop ₹1,596.00 (-5.8%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹18.09 at stop ₹748.60 (-8.5%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-01-23  GMRAIRPORT  SELL ₹13.11 at stop ₹92.10 (-11.4%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹19.46 at stop ₹1,672.76 (-4.4%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-01-27  HDFCGOLD    BUY ₹23.46 at ₹135.17 (fresh Friday signal — starved 3×, front of the queue — BUY: 4.38× weekly, month 2.90×, ladder rising; stop ₹107.66; charges ₹0.06)
2026-01-27  SILVERIETF  BUY ₹23.48 at ₹335.00 (fresh Friday signal — starved 4×, front of the queue — BUY: 3.77× weekly, month 4.93×, ladder rising; stop ₹208.50; charges ₹0.06)
2026-01-27  TATSILV     BUY ₹22.74 at ₹32.00 (fresh Friday signal — starved 2×, front of the queue — BUY: 9.86× weekly, month 21.32×, ladder rising; stop ₹19.90; charges ₹0.05)
2026-02-02  GOLDBEES    SELL ₹18.16 at stop ₹113.05 (+10.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-02-02  TATSILV     SELL ₹16.29 at stop ₹23.03 (-28.0%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-02-09  APEX        BUY ₹14.18 at ₹355.00 (fresh Friday signal — BUY: 2.98× weekly, month 4.24×, ladder rising; stop ₹221.66; charges ₹0.03)
2026-02-09  CPSEETF     BUY ₹20.27 at ₹99.82 (fresh Friday signal — starved 2×, front of the queue — BUY: 2.11× weekly, month 2.09×, ladder rising; stop ₹85.68; charges ₹0.05)
2026-02-27  APEX        SELL ₹15.47 at stop ₹389.22 (+9.6%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2026-03-02  J&KBANK     BUY ₹15.47 at ₹116.20 (fresh Friday signal — starved 2×, front of the queue — BUY: 8.67× weekly, month 1.90×, ladder rising; stop ₹96.50; charges ₹0.04)
2026-03-23  GOLDIETF    SELL ₹19.96 at stop ₹115.68 (+55.7%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-03-23  HDFCGOLD    SELL ₹19.83 at stop ₹114.75 (-15.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-03-23  HDFCSILVER  SELL ₹28.28 at stop ₹201.50 (+58.3%, charges ₹0.06) — the cash goes back to work at the next Friday screen
2026-03-23  J&KBANK     SELL ₹14.67 at stop ₹110.67 (-4.8%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2026-03-23  SILVERBEES  SELL ₹13.32 at stop ₹196.78 (-11.7%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2026-03-23  SILVERIETF  SELL ₹14.55 at stop ₹208.50 (-37.8%, charges ₹0.03) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹18.31 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.04)
2026-03-30  MAHABANK    SELL ₹20.91 at stop ₹61.05 (+2.3%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.03 paid (STCG ₹0.00 @20%, LTCG ₹0.23 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2026-04-06  BAJAJHIND   BUY ₹18.25 at ₹17.08 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.33× weekly, month 1.97×, ladder rising; stop ₹13.87; charges ₹0.04)
2026-04-06  CHENNPETRO  BUY ₹18.27 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.04)
2026-04-13  THERMAX     BUY ₹18.43 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.04)
2026-04-20  NLCINDIA    BUY ₹18.94 at ₹303.60 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.54× weekly, month 2.41×, ladder rising; stop ₹248.05; charges ₹0.04)
2026-04-27  OFSS        BUY ₹19.06 at ₹9,050.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 5.35× weekly, month 2.36×, ladder rising; stop ₹6,723.15; charges ₹0.04)
2026-04-27  TRENT       BUY ₹19.12 at ₹2,890.67 (fresh Friday signal — BUY: 2.90× weekly, month 1.69×, ladder rising; stop ₹2,414.90; charges ₹0.05)
2026-05-14  AETHER      SELL ₹17.84 at stop ₹1,125.84 (-2.1%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-05-14  BAJAJHIND   SELL ₹19.10 at stop ₹17.96 (+5.2%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-05-18  CAPLIPOINT  BUY ₹18.99 at ₹1,990.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.04)
2026-05-18  MARKSANS    BUY ₹19.04 at ₹209.56 (fresh Friday signal — starved 3×, front of the queue — BUY: 2.70× weekly, month 1.65×, ladder rising; stop ₹171.95; charges ₹0.04)
2026-06-02  CPSEETF     SELL ₹20.25 at stop ₹100.15 (+0.3%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-06-08  MANINDS     BUY ₹19.84 at ₹526.00 (fresh Friday signal — starved 1×, front of the queue — ACCUMULATE: 2.51× weekly, month 1.68×, ladder rising; stop ₹442.27; charges ₹0.05)
2026-06-09  NLCINDIA    SELL ₹19.91 at stop ₹320.62 (+5.6%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-06-15  NRBBEARING  BUY ₹20.31 at ₹438.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 10.53× weekly, month 6.95×, ladder rising; stop ₹331.98; charges ₹0.05)
2026-07-22  MARKSANS    SELL ₹22.12 at stop ₹244.62 (+16.7%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2026-07-22  NRBBEARING  SELL ₹18.10 at stop ₹391.97 (-10.5%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-07-23  OFSS        SELL ₹21.47 at stop ₹10,241.00 (+13.2%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2026-07-27  DYCL        BUY ₹20.25 at ₹406.00 (fresh Friday signal — starved 1×, front of the queue — BUY: 10.52× weekly, month 7.30×, ladder rising; stop ₹233.64; charges ₹0.05)
2026-07-27  FLUOROCHEM  BUY ₹20.29 at ₹4,653.20 (fresh Friday signal — starved 1×, front of the queue — BUY: 2.43× weekly, month 1.76×, ladder rising; stop ₹3,623.49; charges ₹0.05)
2026-07-27  GABRIEL     BUY ₹20.16 at ₹1,370.10 (fresh Friday signal — starved 3×, front of the queue — BUY: 4.50× weekly, month 1.84×, ladder rising; stop ₹1,154.25; charges ₹0.05)
2026-07-29  THERMAX     SELL ₹21.97 at stop ₹4,306.64 (+19.8%, charges ₹0.05) — the cash goes back to work at the next Friday screen
2026-08-03  RATNAVEER   BUY ₹20.60 at ₹184.99 (fresh Friday signal — starved 2×, front of the queue — BUY: 9.23× weekly, month 4.03×, ladder rising; stop ₹162.56; charges ₹0.05)
2026-08-25  GABRIEL     SELL ₹19.76 at stop ₹1,349.19 (-1.5%, charges ₹0.04) — the cash goes back to work at the next Friday screen
2026-08-31  OMAXE       BUY ₹22.12 at ₹131.50 (fresh Friday signal — starved 1×, front of the queue — BUY: 3.94× weekly, month 5.41×, ladder rising; stop ₹89.02; charges ₹0.05)
```
