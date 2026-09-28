# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 2272 symbols, fetched once into `ROLLING_MCAP1250_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹442.01** | **+25.82% a year** |
| The same system before costs and taxes | ₹609.38 | +32.23% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹288.59 | +17.80% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹0.00 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹442.01** (+25.82% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 466 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹23.60** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹72.21**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹36.05 | ₹0.00 | ₹7.2094 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹93.40 | ₹14.78 | ₹20.5274 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹40.06 | ₹50.64 | ₹14.3410 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹150.66 | ₹0.00 | ₹30.1324 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹17.92 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹0.00 | ₹0.00 | ₹0.0000 | ₹64.26 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹0.00 | ₹0.00 | ₹0.0000 | ₹12.93 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 142.75 | +42.8% | +43.4% | +70.1% |
| 2021 (2021-12-31) | 283.72 | +98.8% | +110.4% | +26.2% |
| 2022 (2022-12-30) | 329.92 | +16.3% | +21.4% | +4.3% |
| 2023 (2023-12-29) | 481.77 | +46.0% | +57.9% | +20.0% |
| 2024 (2024-12-27) | 461.27 | -4.3% | +4.8% | +9.6% |
| 2025 (2025-12-26) | 386.83 | -16.1% | -13.2% | +9.4% |
| 2026 (2026-09-22) | 442.01 | +14.3% | +15.8% | -10.4% |

## What it took to earn it

- **Maximum drawdown: -41.8%** (peak 2024-07-05 → trough 2026-03-27, on weekly closes).
- **220 closed trades**: 95 winners (43%), average winner +36.8%, average loser -10.9%.
- Best closed trade BIGBLOC +258.3%; worst MRPL -40.3%.
- Median holding period 60 days.
- Cash share of equity averaged 9% across all weeks (median 3%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.20 | 59.96 | 4 |
| 2020-05-29 | 104.53 | 0.00 | 10 |
| 2020-06-26 | 114.63 | 0.00 | 10 |
| 2020-07-31 | 123.94 | 9.95 | 9 |
| 2020-08-28 | 126.70 | 0.00 | 10 |
| 2020-09-25 | 130.52 | 25.81 | 7 |
| 2020-10-30 | 124.30 | 6.42 | 8 |
| 2020-11-27 | 123.44 | 0.00 | 10 |
| 2020-12-24 | 142.75 | 30.14 | 8 |
| 2021-01-29 | 143.12 | 33.37 | 8 |
| 2021-02-26 | 154.27 | 14.48 | 9 |
| 2021-03-26 | 150.37 | 14.19 | 9 |
| 2021-04-30 | 164.00 | 1.63 | 10 |
| 2021-05-28 | 179.97 | 1.63 | 10 |
| 2021-06-25 | 195.96 | 0.00 | 10 |
| 2021-07-30 | 237.23 | 0.00 | 10 |
| 2021-08-27 | 227.67 | 0.00 | 10 |
| 2021-09-24 | 232.08 | 23.47 | 9 |
| 2021-10-29 | 232.37 | 41.30 | 8 |
| 2021-11-26 | 284.05 | 82.97 | 8 |
| 2021-12-31 | 283.72 | 0.00 | 10 |
| 2022-01-28 | 298.86 | 67.59 | 7 |
| 2022-02-25 | 279.11 | 83.77 | 6 |
| 2022-03-25 | 301.29 | 23.81 | 8 |
| 2022-04-29 | 291.97 | 8.51 | 8 |
| 2022-05-27 | 298.59 | 0.72 | 8 |
| 2022-06-24 | 281.54 | 28.09 | 7 |
| 2022-07-29 | 299.76 | 9.35 | 7 |
| 2022-08-26 | 311.86 | 3.93 | 7 |
| 2022-09-30 | 305.30 | 27.81 | 7 |
| 2022-10-28 | 317.03 | 0.00 | 8 |
| 2022-11-25 | 336.86 | 0.00 | 8 |
| 2022-12-30 | 329.92 | 29.12 | 8 |
| 2023-01-27 | 325.86 | 48.48 | 7 |
| 2023-02-24 | 327.41 | 0.97 | 9 |
| 2023-03-31 | 314.13 | 128.53 | 6 |
| 2023-04-28 | 322.79 | 52.66 | 8 |
| 2023-05-26 | 337.26 | 10.58 | 9 |
| 2023-06-30 | 347.73 | 10.58 | 9 |
| 2023-07-28 | 368.03 | 12.39 | 9 |
| 2023-08-25 | 403.53 | 12.39 | 9 |
| 2023-09-29 | 412.22 | 30.79 | 8 |
| 2023-10-27 | 410.96 | 116.31 | 6 |
| 2023-11-24 | 466.22 | 4.78 | 9 |
| 2023-12-29 | 481.77 | 0.00 | 9 |
| 2024-01-25 | 505.14 | 19.51 | 9 |
| 2024-02-23 | 529.83 | 8.48 | 9 |
| 2024-03-28 | 514.92 | 138.68 | 7 |
| 2024-04-26 | 526.54 | 10.53 | 9 |
| 2024-05-31 | 525.43 | 115.27 | 7 |
| 2024-06-28 | 534.16 | 4.31 | 9 |
| 2024-07-26 | 528.67 | 125.26 | 7 |
| 2024-08-30 | 519.78 | 18.15 | 9 |
| 2024-09-27 | 505.86 | 4.21 | 9 |
| 2024-10-25 | 471.09 | 202.16 | 6 |
| 2024-11-29 | 488.47 | 19.49 | 10 |
| 2024-12-27 | 461.27 | 122.39 | 8 |
| 2025-01-31 | 425.80 | 106.66 | 7 |
| 2025-02-28 | 370.99 | 79.91 | 8 |
| 2025-03-28 | 412.06 | 36.78 | 9 |
| 2025-04-25 | 445.69 | 3.88 | 9 |
| 2025-05-30 | 442.64 | 0.00 | 9 |
| 2025-06-27 | 456.58 | 0.00 | 9 |
| 2025-07-25 | 442.44 | 2.11 | 9 |
| 2025-08-29 | 433.89 | 41.92 | 8 |
| 2025-09-26 | 412.82 | 98.22 | 7 |
| 2025-10-31 | 403.83 | 0.00 | 10 |
| 2025-11-28 | 394.03 | 101.78 | 7 |
| 2025-12-26 | 386.83 | 49.62 | 9 |
| 2026-01-30 | 368.91 | 66.36 | 8 |
| 2026-02-27 | 349.79 | 33.56 | 9 |
| 2026-03-27 | 325.92 | 61.29 | 8 |
| 2026-04-30 | 382.44 | 6.14 | 10 |
| 2026-05-29 | 409.52 | 1.50 | 10 |
| 2026-06-25 | 416.21 | 0.00 | 10 |
| 2026-07-31 | 409.71 | 33.06 | 10 |
| 2026-08-28 | 451.63 | 0.00 | 11 |
| 2026-09-22 | 442.01 | 11.11 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| ACMESOLAR | 2026-09-21 | 439.00 | 458.65 | 370.12 | +4.5% |
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| CRAFTSMAN | 2026-05-11 | 9,039.50 | 10,602.00 | 10,380.65 | +17.3% |
| DEEDEV | 2026-03-16 | 303.25 | 691.80 | 537.94 | +128.1% |
| GANESHHOU | 2026-07-13 | 860.50 | 736.80 | 712.60 | -14.4% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,671.20 | 1,653.47 | +40.4% |
| SUNDRMFAST | 2026-09-15 | 1,277.30 | 1,190.90 | 1,127.74 | -6.8% |
| TMB | 2026-08-03 | 864.90 | 883.75 | 817.00 | +2.2% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| MANGCHEFER | 2020-05-11 | 33.75 | 2020-07-31 | 33.73 | -0.1% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| APCOTEXIND | 2020-08-24 | 164.95 | 2020-08-31 | 151.95 | -7.9% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| KIRLOSBROS | 2020-08-03 | 130.00 | 2020-09-08 | 120.79 | -7.1% |
| RCF | 2020-05-18 | 39.90 | 2020-09-09 | 45.84 | +14.9% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| SATIA | 2020-09-14 | 122.00 | 2020-09-22 | 102.97 | -15.6% |
| PRINCEPIPE | 2020-09-07 | 208.00 | 2020-10-12 | 220.88 | +6.2% |
| EXPLEOSOL | 2020-10-19 | 582.00 | 2020-10-29 | 527.39 | -9.4% |
| ALEMBICLTD | 2020-05-18 | 54.90 | 2020-11-02 | 91.41 | +66.5% |
| ADVENZYMES | 2020-05-18 | 159.95 | 2020-11-03 | 292.33 | +82.8% |
| HATHWAY | 2020-06-22 | 34.80 | 2020-11-09 | 28.34 | -18.6% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| GODREJPROP | 2020-11-09 | 964.00 | 2021-01-18 | 1,306.25 | +35.5% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| TRENT | 2020-11-17 | 503.33 | 2021-01-29 | 417.53 | -17.0% |
| MTNL | 2020-12-28 | 14.10 | 2021-02-16 | 12.06 | -14.5% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| TATAMOTORS | 2021-01-25 | 296.90 | 2021-03-19 | 296.97 | +0.0% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| MAHINDCIE | 2021-02-22 | 188.00 | 2021-03-19 | 158.46 | -15.7% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| KIRLFER | 2020-11-02 | 94.05 | 2021-08-10 | 279.49 | +197.2% |
| WELSPUNIND | 2021-03-22 | 81.45 | 2021-08-10 | 124.64 | +53.0% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| GDL | 2021-01-25 | 158.00 | 2021-09-20 | 266.00 | +68.4% |
| SAKSOFT | 2021-08-23 | 798.90 | 2021-10-20 | 1,002.30 | +25.5% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| INDOCO | 2021-08-16 | 484.30 | 2021-11-12 | 412.30 | -14.9% |
| BIGBLOC | 2021-11-15 | 39.80 | 2021-11-16 | 142.59 | +258.3% |
| SHOPERSTOP | 2021-10-25 | 326.00 | 2021-11-22 | 335.82 | +3.0% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| MAHLOG | 2021-01-25 | 495.85 | 2021-11-30 | 654.55 | +32.0% |
| SUPRAJIT | 2021-11-22 | 454.00 | 2021-12-13 | 391.40 | -13.8% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| MINDAIND | 2021-12-20 | 1,026.00 | 2022-01-07 | 1,088.41 | +6.1% |
| LTI | 2021-10-25 | 6,555.00 | 2022-01-24 | 6,270.00 | -4.3% |
| TVTODAY | 2021-11-22 | 320.24 | 2022-01-24 | 311.68 | -2.7% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| SUZLON | 2022-01-10 | 11.15 | 2022-02-15 | 9.79 | -12.2% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| TV18BRDCST | 2022-01-31 | 58.90 | 2022-02-22 | 58.38 | -0.9% |
| LAXMIMACH | 2022-02-21 | 10,118.80 | 2022-02-22 | 10,169.75 | +0.5% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| RAJRATAN | 2021-03-22 | 763.95 | 2022-03-28 | 1,553.82 | +103.4% |
| ANMOL | 2022-02-28 | 210.00 | 2022-05-09 | 194.51 | -7.4% |
| KAMATHOTEL | 2022-03-28 | 71.45 | 2022-05-10 | 72.91 | +2.0% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| ADVANIHOTR | 2022-02-21 | 101.85 | 2022-06-09 | 64.65 | -36.5% |
| KRISHANA | 2022-05-16 | 67.96 | 2022-06-16 | 54.77 | -19.4% |
| JSWENERGY | 2021-03-08 | 81.85 | 2022-06-20 | 201.99 | +146.8% |
| MRPL | 2022-06-13 | 116.65 | 2022-07-06 | 69.61 | -40.3% |
| STERTOOLS | 2022-06-27 | 277.80 | 2022-08-12 | 239.05 | -13.9% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| MOLDTKPAC | 2022-08-16 | 927.00 | 2022-09-29 | 874.43 | -5.7% |
| SUNDARMHLD | 2022-10-03 | 103.50 | 2022-10-11 | 92.20 | -10.9% |
| FAIRCHEMOR | 2022-10-17 | 2,240.00 | 2022-11-01 | 1,790.15 | -20.1% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| RVNL | 2022-11-07 | 46.85 | 2022-12-26 | 60.57 | +29.3% |
| CONCOR | 2022-09-12 | 753.00 | 2023-01-17 | 696.30 | -7.5% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| LSIL | 2023-01-30 | 23.20 | 2023-02-07 | 20.04 | -13.6% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| MAHINDCIE | 2023-02-06 | 395.20 | 2023-03-10 | 391.69 | -0.9% |
| KABRAEXTRU | 2022-12-26 | 441.95 | 2023-03-14 | 506.92 | +14.7% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| UNIENTER | 2023-02-13 | 179.30 | 2023-03-27 | 138.28 | -22.9% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| KIRLOSBROS | 2023-04-03 | 414.00 | 2023-04-26 | 403.85 | -2.5% |
| MUKANDLTD | 2023-01-02 | 136.70 | 2023-05-17 | 116.23 | -15.0% |
| FAIRCHEMOR | 2023-05-02 | 1,272.00 | 2023-05-19 | 1,141.04 | -10.3% |
| ANURAS | 2023-03-20 | 755.90 | 2023-07-03 | 1,007.67 | +33.3% |
| KSB | 2023-03-27 | 417.98 | 2023-07-12 | 407.74 | -2.4% |
| INGERRAND | 2023-04-03 | 2,690.00 | 2023-09-13 | 3,022.99 | +12.4% |
| KIRLOSIND | 2023-03-13 | 2,300.00 | 2023-09-25 | 3,202.97 | +39.3% |
| SJVN | 2023-09-18 | 75.35 | 2023-10-23 | 66.03 | -12.4% |
| HAL | 2023-04-03 | 1,380.00 | 2023-10-25 | 1,840.70 | +33.4% |
| SHARDAMOTR | 2023-05-22 | 380.00 | 2023-10-25 | 465.07 | +22.4% |
| GENUSPOWER | 2023-07-10 | 162.85 | 2023-11-16 | 234.03 | +43.7% |
| ISMTLTD | 2023-11-20 | 94.60 | 2023-12-20 | 88.35 | -6.6% |
| TIIL | 2023-02-20 | 1,116.70 | 2024-01-17 | 2,337.00 | +109.3% |
| MMFL | 2023-12-26 | 1,023.60 | 2024-01-30 | 912.05 | -10.9% |
| GLS | 2023-05-02 | 509.05 | 2024-03-05 | 779.48 | +53.1% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| TCI | 2024-02-05 | 987.60 | 2024-03-11 | 790.40 | -20.0% |
| KKCL | 2023-10-30 | 761.80 | 2024-03-13 | 674.12 | -11.5% |
| DOLLAR | 2024-03-11 | 527.95 | 2024-03-13 | 461.65 | -12.6% |
| GANESHHOUC | 2024-01-23 | 663.40 | 2024-03-14 | 666.47 | +0.5% |
| ANANDRATHI | 2023-07-17 | 265.70 | 2024-03-27 | 862.65 | +224.7% |
| PILANIINVS | 2023-10-03 | 2,380.05 | 2024-05-09 | 3,710.37 | +55.9% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| TDPOWERSYS | 2023-04-03 | 79.50 | 2024-07-19 | 188.72 | +137.4% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| ARE&M | 2024-06-10 | 1,450.00 | 2024-07-22 | 1,502.14 | +3.6% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| THERMAX | 2024-06-03 | 5,640.00 | 2024-08-05 | 4,719.70 | -16.3% |
| JWL | 2024-05-13 | 490.00 | 2024-08-06 | 552.00 | +12.7% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| CERA | 2024-08-12 | 10,499.95 | 2024-09-19 | 8,198.93 | -21.9% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| ALKYLAMINE | 2024-09-23 | 2,432.85 | 2024-10-22 | 2,106.24 | -13.4% |
| INDIAGLYCO | 2024-07-22 | 515.00 | 2024-10-25 | 587.91 | +14.2% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| VISHNU | 2024-10-28 | 511.90 | 2024-11-12 | 470.30 | -8.1% |
| ESABINDIA | 2024-07-22 | 6,486.15 | 2024-11-13 | 5,842.74 | -9.9% |
| ASTRAZEN | 2024-10-14 | 7,800.00 | 2024-11-14 | 6,854.77 | -12.1% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| EMSLIMITED | 2024-12-23 | 916.85 | 2025-01-10 | 802.65 | -12.5% |
| CARERATING | 2024-10-28 | 1,396.00 | 2025-01-13 | 1,239.70 | -11.2% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| MOTILALOFS | 2024-10-21 | 1,021.95 | 2025-01-17 | 788.79 | -22.8% |
| SASKEN | 2024-11-18 | 2,015.25 | 2025-01-21 | 1,993.24 | -1.1% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| NACLIND | 2024-12-30 | 67.60 | 2025-01-27 | 61.28 | -9.3% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| ZOTA | 2025-01-13 | 965.00 | 2025-01-28 | 863.60 | -10.5% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| APOLLO | 2025-01-20 | 131.50 | 2025-02-17 | 110.19 | -16.2% |
| MPSLTD | 2025-02-24 | 2,648.95 | 2025-02-25 | 2,360.51 | -10.9% |
| GANESHHOUC | 2024-11-18 | 1,059.00 | 2025-02-28 | 1,090.38 | +3.0% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| MBAPL | 2025-01-27 | 58.20 | 2025-03-27 | 53.39 | -8.3% |
| TAJGVK | 2025-02-24 | 440.40 | 2025-04-02 | 453.34 | +2.9% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| BAJAJHCARE | 2025-01-20 | 690.00 | 2025-04-07 | 521.14 | -24.5% |
| TCPLPACK | 2025-02-24 | 3,997.25 | 2025-04-07 | 4,002.68 | +0.1% |
| ROHLTD | 2025-04-07 | 341.50 | 2025-04-30 | 366.23 | +7.2% |
| GRMOVER | 2025-03-10 | 252.00 | 2025-05-07 | 290.80 | +15.4% |
| PARAS | 2025-05-05 | 1,372.20 | 2025-07-04 | 1,417.98 | +3.3% |
| KPRMILL | 2025-05-12 | 1,302.00 | 2025-08-01 | 1,108.74 | -14.8% |
| JSWHL | 2024-11-18 | 19,990.00 | 2025-08-04 | 19,106.01 | -4.4% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| RSYSTEMS | 2025-09-01 | 460.00 | 2025-09-24 | 423.23 | -8.0% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-26 | 857.85 | -0.8% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| PGHL | 2025-08-04 | 6,440.00 | 2025-11-06 | 5,938.45 | -7.8% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| PRAKASH | 2025-08-11 | 178.70 | 2025-11-14 | 147.31 | -17.6% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| NLCINDIA | 2025-09-29 | 280.30 | 2025-11-24 | 241.39 | -13.9% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| SKYGOLD | 2025-10-27 | 370.00 | 2025-11-25 | 329.13 | -11.0% |
| ASTERDM | 2025-07-07 | 633.90 | 2025-12-05 | 643.62 | +1.5% |
| PGIL | 2025-11-17 | 844.05 | 2025-12-09 | 765.71 | -9.3% |
| NACLIND | 2025-04-07 | 128.14 | 2025-12-17 | 164.20 | +28.1% |
| HCG | 2025-10-27 | 758.60 | 2025-12-23 | 676.59 | -10.8% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| KIRLOSENG | 2025-12-08 | 1,130.00 | 2026-01-12 | 1,140.95 | +1.0% |
| ESABINDIA | 2025-12-15 | 6,203.50 | 2026-01-12 | 5,605.00 | -9.6% |
| ASHAPURMIN | 2025-12-22 | 800.00 | 2026-01-16 | 817.00 | +2.1% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| GMRAIRPORT | 2025-12-01 | 108.90 | 2026-01-23 | 92.10 | -15.4% |
| JAYBARMARU | 2026-01-27 | 84.25 | 2026-01-28 | 85.51 | +1.5% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| NITCO | 2026-01-19 | 89.00 | 2026-02-19 | 75.12 | -15.6% |
| INFOBEAN | 2026-01-27 | 813.10 | 2026-02-27 | 770.07 | -5.3% |
| KIRIINDUS | 2026-01-19 | 530.30 | 2026-03-02 | 427.56 | -19.4% |
| SHRIRAMFIN | 2025-12-29 | 963.00 | 2026-03-04 | 992.37 | +3.0% |
| AWHCL | 2026-02-02 | 520.05 | 2026-03-04 | 467.40 | -10.1% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-19 | 67.50 | 2026-03-12 | 61.08 | -9.5% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| AGIIL | 2026-02-02 | 249.80 | 2026-03-30 | 271.80 | +8.8% |
| KSB | 2026-03-02 | 738.00 | 2026-05-04 | 917.42 | +24.3% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| PRECWIRE | 2026-03-09 | 328.00 | 2026-07-07 | 376.20 | +14.7% |
| AEROFLEX | 2026-03-09 | 215.00 | 2026-07-07 | 427.69 | +98.9% |
| VTL | 2026-03-30 | 520.95 | 2026-07-31 | 592.80 | +13.8% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-03-16 | 6,400.00 | 2026-09-15 | 7,158.25 | +11.8% |
| SGMART | 2026-07-13 | 646.30 | 2026-09-15 | 746.03 | +15.4% |
| RITES | 2026-07-13 | 228.43 | 2026-09-16 | 204.83 | -10.3% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_MCAP1250_CORE750.csv` beside this report (32297 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.81× weekly, month 2.50×, ladder rising; stop ₹241.64; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹10.01 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.54× weekly, month 5.13×, ladder rising; stop ₹310.03; charges ₹0.0119)
2020-04-27  SYNGENE     BUY ₹10.02 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.37× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.01 at ₹133.40 (fresh Friday signal — BUY: 6.67× weekly, month 2.22×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-11  APLLTD      BUY ₹9.98 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.72× weekly, month 6.13×, ladder rising; stop ₹694.45; charges ₹0.0118)
2020-05-11  IOLCP       BUY ₹9.98 at ₹66.18 (fresh Friday signal — BUY: 2.24× weekly, month 2.69×, ladder rising; stop ₹51.22; charges ₹0.0118)
2020-05-11  MANGCHEFER  BUY ₹9.98 at ₹33.75 (fresh Friday signal — BUY: surged 2.89× weekly on 2020-04-30 (month 2.29×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹29.50; charges ₹0.0118)
2020-05-18  ADVENZYMES  BUY ₹10.20 at ₹159.95 (fresh Friday signal — ACCUMULATE: 3.14× weekly, month 1.99×, ladder rising; stop ₹126.20; charges ₹0.0121)
2020-05-18  ALEMBICLTD  BUY ₹10.18 at ₹54.90 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 2.01×, ladder rising; stop ₹44.84; charges ₹0.0121)
2020-05-18  RCF         BUY ₹9.64 at ₹39.90 (fresh Friday signal — ACCUMULATE: 2.17× weekly, month 2.55×, ladder rising; stop ₹35.25; charges ₹0.0114)
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  PANACEABIO  BUY ₹9.97 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.25×, ladder rising; stop ₹114.11; charges ₹0.0118)
2020-06-16  IOLCP       SELL ₹10.43 at stop ₹69.35 (+4.8%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2020-06-22  HATHWAY     BUY ₹10.43 at ₹34.80 (fresh Friday signal — BUY: 9.17× weekly, month 6.59×, ladder rising; stop ₹19.97; charges ₹0.0124)
2020-07-31  MANGCHEFER  SELL ₹9.95 at stop ₹33.73 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-08-03  KIRLOSBROS  BUY ₹9.95 at ₹130.00 (fresh Friday signal — BUY: 4.32× weekly, month 10.28×, ladder rising; stop ₹97.15; charges ₹0.0118)
2020-08-20  PANACEABIO  SELL ₹7.96 at stop ₹184.01 (-20.0%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹7.96 at ₹164.95 (fresh Friday signal — BUY: 8.03× weekly, month 5.84×, ladder rising; stop ₹119.51; charges ₹0.0094)
2020-08-31  APCOTEXIND  SELL ₹7.31 at stop ₹151.95 (-7.9%, charges ₹0.0076) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.93 at stop ₹928.62 (+19.9%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹12.54 at ₹1,398.95 (fresh Friday signal — BUY: 5.23× weekly, month 3.88×, ladder rising; stop ₹1,211.25; charges ₹0.0149)
2020-09-07  PRINCEPIPE  BUY ₹6.70 at ₹208.00 (fresh Friday signal — BUY: 3.44× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.0079)
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-08  KIRLOSBROS  SELL ₹9.23 at stop ₹120.79 (-7.1%, charges ₹0.0096) — the cash goes back to work at the next Friday screen
2020-09-09  RCF         SELL ₹11.05 at stop ₹45.84 (+14.9%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-14  SATIA       BUY ₹12.93 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.17×, ladder rising; stop ₹102.97; charges ₹0.0153)
2020-09-14  TCI         BUY ₹12.93 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.71× weekly, month 3.76×, ladder rising; stop ₹190.07; charges ₹0.0153)
2020-09-22  SATIA       SELL ₹10.89 at stop ₹102.97 (-15.6%, charges ₹0.0113) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹12.70 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0150)
2020-09-28  SAKSOFT     BUY ₹13.11 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.34×, ladder rising; stop ₹303.81; charges ₹0.0155)
2020-10-12  PRINCEPIPE  SELL ₹7.10 at stop ₹220.88 (+6.2%, charges ₹0.0074) — the cash goes back to work at the next Friday screen
2020-10-19  EXPLEOSOL   BUY ₹7.10 at ₹582.00 (fresh Friday signal — BUY: 2.57× weekly, month 2.87×, ladder rising; stop ₹443.75; charges ₹0.0084)
2020-10-29  EXPLEOSOL   SELL ₹6.42 at stop ₹527.39 (-9.4%, charges ₹0.0067) — the cash goes back to work at the next Friday screen
2020-11-02  ALEMBICLTD  SELL ₹16.92 at stop ₹91.41 (+66.5%, charges ₹0.0175) — the cash goes back to work at the next Friday screen
2020-11-02  KIRLFER     BUY ₹6.42 at ₹94.05 (fresh Friday signal — ACCUMULATE: 3.57× weekly, month 2.76×, ladder rising; stop ₹75.88; charges ₹0.0076)
2020-11-03  ADVENZYMES  SELL ₹18.61 at stop ₹292.33 (+82.8%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹11.50 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.75× weekly, month 1.95×, ladder rising; stop ₹77.16; charges ₹0.0136)
2020-11-09  GODREJPROP  BUY ₹11.47 at ₹964.00 (fresh Friday signal — BUY: surged 4.12× weekly on 2020-10-23 (month 2.57×), ladder rising NOW — promoted from the ladder watch; stop ₹927.67; charges ₹0.0136)
2020-11-09  HATHWAY     SELL ₹8.48 at stop ₹28.34 (-18.6%, charges ₹0.0088) — the cash goes back to work at the next Friday screen
2020-11-09  JINDWORLD   BUY ₹11.51 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.34× weekly, month 1.54×, ladder rising; stop ₹39.81; charges ₹0.0136)
2020-11-17  TRENT       BUY ₹9.53 at ₹503.33 (fresh Friday signal — ACCUMULATE: 3.36× weekly, month 1.95×, ladder rising; stop ₹367.93; charges ₹0.0113)
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.51 at stop ₹234.75 (-3.0%, charges ₹0.0130) — the cash goes back to work at the next Friday screen
2020-12-28  MTNL        BUY ₹14.86 at ₹14.10 (fresh Friday signal — BUY: 9.99× weekly, month 4.75×, ladder rising; stop ₹8.26; charges ₹0.0176)
2020-12-28  PAISALO     BUY ₹14.72 at ₹56.99 (fresh Friday signal — BUY: 32.49× weekly, month 7.40×, ladder rising; stop ₹33.56; charges ₹0.0174)
2021-01-18  GODREJPROP  SELL ₹15.51 at stop ₹1,306.25 (+35.5%, charges ₹0.0161) — the cash goes back to work at the next Friday screen
2021-01-20  BORORENEW   SELL ₹28.48 at stop ₹247.59 (+148.3%, charges ₹0.0295) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹14.66 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.80×, ladder rising; stop ₹92.41; charges ₹0.0174)
2021-01-25  MAHLOG      BUY ₹14.82 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹0.0176)
2021-01-25  SAKSOFT     SELL ₹11.19 at stop ₹341.10 (-14.4%, charges ₹0.0116) — the cash goes back to work at the next Friday screen
2021-01-25  TATAMOTORS  BUY ₹14.81 at ₹296.90 (fresh Friday signal — BUY: 3.10× weekly, month 2.06×, ladder rising; stop ₹171.38; charges ₹0.0175)
2021-01-29  HCLTECH     SELL ₹14.02 at stop ₹928.05 (+10.7%, charges ₹0.0145) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹7.88 at stop ₹417.53 (-17.0%, charges ₹0.0082) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹14.51 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.92×, ladder rising; stop ₹156.94; charges ₹0.0172)
2021-02-01  GAEL        BUY ₹14.66 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.71× weekly, month 3.64×, ladder rising; stop ₹62.70; charges ₹0.0174)
2021-02-16  MTNL        SELL ₹12.68 at stop ₹12.06 (-14.5%, charges ₹0.0132) — the cash goes back to work at the next Friday screen
2021-02-22  MAHINDCIE   BUY ₹15.23 at ₹188.00 (fresh Friday signal — BUY: 22.74× weekly, month 4.25×, ladder rising; stop ₹143.79; charges ₹0.0180)
2021-02-23  GAEL        SELL ₹12.83 at stop ₹62.70 (-12.3%, charges ₹0.0133) — the cash goes back to work at the next Friday screen
2021-03-01  JINDWORLD   SELL ₹11.97 at stop ₹52.12 (+4.2%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2021-03-01  RCF         BUY ₹14.48 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.12×, ladder rising; stop ₹50.16; charges ₹0.0172)
2021-03-08  JSWENERGY   BUY ₹11.97 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.49×, ladder rising; stop ₹65.79; charges ₹0.0142)
2021-03-17  RCF         SELL ₹14.30 at stop ₹79.16 (-1.1%, charges ₹0.0148) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹16.57 at stop ₹204.25 (+14.5%, charges ₹0.0172) — the cash goes back to work at the next Friday screen
2021-03-19  MAHINDCIE   SELL ₹12.81 at stop ₹158.46 (-15.7%, charges ₹0.0133) — the cash goes back to work at the next Friday screen
2021-03-19  TATAMOTORS  SELL ₹14.78 at stop ₹296.97 (+0.0%, charges ₹0.0153) — the cash goes back to work at the next Friday screen
2021-03-22  KEI         BUY ₹14.94 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.53×, ladder rising; stop ₹436.67; charges ₹0.0177)
2021-03-22  RAJRATAN    BUY ₹15.02 at ₹763.95 (fresh Friday signal — BUY: 4.06× weekly, month 2.74×, ladder rising; stop ₹590.19; charges ₹0.0178)
2021-03-22  VIDHIING    BUY ₹14.86 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0176)
2021-03-22  WELSPUNIND  BUY ₹13.63 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.42×, ladder rising; stop ₹67.45; charges ₹0.0161)
2021-03-25  BANARISUG   SELL ₹14.19 at stop ₹1,586.36 (+13.4%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2021-03-30  CENTRUM     BUY ₹14.19 at ₹28.40 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 6.71×, ladder rising; stop ₹24.89; charges ₹0.0168)
2021-04-01  CENTRUM     TRIM 4.7% (₹0.67 at ₹28.35) to pay the tax bill
2021-04-01  GDL         TRIM 4.7% (₹0.78 at ₹177.90) to pay the tax bill
2021-04-01  JSWENERGY   TRIM 4.7% (₹0.62 at ₹90.70) to pay the tax bill
2021-04-01  KEI         TRIM 4.7% (₹0.71 at ₹528.60) to pay the tax bill
2021-04-01  KIRLFER     TRIM 4.7% (₹0.56 at ₹173.50) to pay the tax bill
2021-04-01  MAHLOG      TRIM 4.7% (₹0.81 at ₹574.75) to pay the tax bill
2021-04-01  PAISALO     TRIM 4.7% (₹0.95 at ₹78.11) to pay the tax bill
2021-04-01  RAJRATAN    TRIM 4.7% (₹0.71 at ₹771.90) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹7.2094 paid (STCG ₹36.05 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 4.7% (₹0.74 at ₹207.10) to pay the tax bill
2021-04-01  WELSPUNIND  TRIM 4.7% (₹0.67 at ₹84.75) to pay the tax bill
2021-04-12  CENTRUM     SELL ₹11.82 at stop ₹24.89 (-12.4%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹17.79 at stop ₹72.41 (+27.1%, charges ₹0.0185) — the cash goes back to work at the next Friday screen
2021-04-19  KPRMILL     BUY ₹13.98 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.60×, ladder rising; stop ₹192.07; charges ₹0.0166)
2021-04-19  MOREPENLAB  BUY ₹14.00 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.06×, ladder rising; stop ₹28.01; charges ₹0.0166)
2021-06-18  VIDHIING    SELL ₹13.26 at stop ₹182.64 (-6.2%, charges ₹0.0138) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹14.89 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0176)
2021-08-10  KIRLFER     SELL ₹18.15 at stop ₹279.49 (+197.2%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2021-08-10  MOREPENLAB  SELL ₹21.01 at stop ₹56.33 (+50.4%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNIND  SELL ₹19.83 at stop ₹124.64 (+53.0%, charges ₹0.0206) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹20.84 at stop ₹352.48 (+49.4%, charges ₹0.0216) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹22.88 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.42×, ladder rising; stop ₹2,675.86; charges ₹0.0271)
2021-08-16  INDOCO      BUY ₹22.81 at ₹484.30 (fresh Friday signal — BUY: 4.80× weekly, month 2.73×, ladder rising; stop ₹412.30; charges ₹0.0270)
2021-08-16  TATAINVEST  BUY ₹22.85 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0271)
2021-08-23  SAKSOFT     BUY ₹11.28 at ₹798.90 (fresh Friday signal — BUY: 4.51× weekly, month 1.59×, ladder rising; stop ₹601.49; charges ₹0.0134)
2021-09-20  GDL         SELL ₹23.47 at stop ₹266.00 (+68.4%, charges ₹0.0243) — the cash goes back to work at the next Friday screen
2021-09-27  NEOGEN      BUY ₹23.47 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0278)
2021-10-20  SAKSOFT     SELL ₹14.13 at stop ₹1,002.30 (+25.5%, charges ₹0.0147) — the cash goes back to work at the next Friday screen
2021-10-22  KEI         SELL ₹23.22 at stop ₹853.10 (+63.4%, charges ₹0.0241) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹19.98 at stop ₹3,220.59 (-12.5%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2021-10-25  LTI         BUY ₹13.98 at ₹6,555.00 (fresh Friday signal — BUY: 4.63× weekly, month 1.84×, ladder rising; stop ₹5,353.77; charges ₹0.0166)
2021-10-25  NEOGEN      SELL ₹21.32 at stop ₹1,142.85 (-8.9%, charges ₹0.0221) — the cash goes back to work at the next Friday screen
2021-10-25  SHOPERSTOP  BUY ₹23.36 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹0.0277)
2021-11-01  TCIEXP      BUY ₹18.03 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0214)
2021-11-01  TTKPRESTIG  BUY ₹23.27 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0276)
2021-11-12  INDOCO      SELL ₹19.37 at stop ₹412.30 (-14.9%, charges ₹0.0201) — the cash goes back to work at the next Friday screen
2021-11-15  BIGBLOC     BUY ₹19.37 at ₹39.80 (fresh Friday signal — BUY: 6.89× weekly, month 3.99×, ladder rising; stop ₹142.59; charges ₹0.0230)
2021-11-16  BIGBLOC     SELL ₹69.25 at stop ₹142.59 (+258.3%, charges ₹0.0718) — the cash goes back to work at the next Friday screen
2021-11-22  SHOPERSTOP  SELL ₹24.01 at stop ₹335.82 (+3.0%, charges ₹0.0249) — the cash goes back to work at the next Friday screen
2021-11-22  SUPRAJIT    BUY ₹28.16 at ₹454.00 (fresh Friday signal — BUY: 10.19× weekly, month 1.96×, ladder rising; stop ₹309.33; charges ₹0.0334)
2021-11-22  TVTODAY     BUY ₹28.36 at ₹320.24 (fresh Friday signal — BUY: 15.58× weekly, month 3.55×, ladder rising; stop ₹253.08; charges ₹0.0336)
2021-11-26  TATAINVEST  SELL ₹25.04 at stop ₹1,436.49 (+9.8%, charges ₹0.0260) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹21.18 at stop ₹10,070.05 (-8.8%, charges ₹0.0220) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹27.17 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0322)
2021-11-29  RAYMOND     BUY ₹27.82 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0330)
2021-11-29  RSYSTEMS    BUY ₹27.98 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0331)
2021-11-29  SOMANYCERA  SELL ₹18.86 at stop ₹755.11 (+26.9%, charges ₹0.0196) — the cash goes back to work at the next Friday screen
2021-11-30  MAHLOG      SELL ₹18.60 at stop ₹654.55 (+32.0%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹27.59 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0327)
2021-12-13  SUPRAJIT    SELL ₹24.22 at stop ₹391.40 (-13.8%, charges ₹0.0251) — the cash goes back to work at the next Friday screen
2021-12-16  RSYSTEMS    SELL ₹25.02 at stop ₹291.18 (-10.4%, charges ₹0.0260) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹27.33 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0324)
2021-12-20  MINDAIND    BUY ₹27.15 at ₹1,026.00 (fresh Friday signal — BUY: 5.05× weekly, month 1.81×, ladder rising; stop ₹787.66; charges ₹0.0322)
2021-12-21  TCIEXP      SELL ₹20.03 at stop ₹2,039.74 (+11.4%, charges ₹0.0208) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹24.67 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0292)
2022-01-07  MINDAIND    SELL ₹28.74 at stop ₹1,088.41 (+6.1%, charges ₹0.0298) — the cash goes back to work at the next Friday screen
2022-01-10  SUZLON      BUY ₹28.74 at ₹11.15 (fresh Friday signal — BUY: 2.86× weekly, month 2.04×, ladder rising; stop ₹6.18; charges ₹0.0340)
2022-01-24  LTI         SELL ₹13.34 at stop ₹6,270.00 (-4.3%, charges ₹0.0138) — the cash goes back to work at the next Friday screen
2022-01-24  TVTODAY     SELL ₹27.54 at stop ₹311.68 (-2.7%, charges ₹0.0286) — the cash goes back to work at the next Friday screen
2022-01-25  SWANENERGY  SELL ₹26.70 at stop ₹162.64 (+8.5%, charges ₹0.0277) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹30.42 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0360)
2022-01-31  TV18BRDCST  BUY ₹30.39 at ₹58.90 (fresh Friday signal — BUY: 2.12× weekly, month 1.51×, ladder rising; stop ₹39.10; charges ₹0.0360)
2022-02-11  SHARDACROP  SELL ₹28.21 at stop ₹545.30 (-7.1%, charges ₹0.0293) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹24.75 at stop ₹424.65 (-8.7%, charges ₹0.0257) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹29.25 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0347)
2022-02-15  RAYMOND     SELL ₹31.64 at stop ₹679.35 (+14.0%, charges ₹0.0328) — the cash goes back to work at the next Friday screen
2022-02-15  SUZLON      SELL ₹25.17 at stop ₹9.79 (-12.2%, charges ₹0.0261) — the cash goes back to work at the next Friday screen
2022-02-21  ADVANIHOTR  BUY ₹28.57 at ₹101.85 (fresh Friday signal — ACCUMULATE: 8.91× weekly, month 7.66×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹64.65; charges ₹0.0338)
2022-02-21  CGCL        BUY ₹28.63 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0339)
2022-02-21  LAXMIMACH   BUY ₹28.58 at ₹10,118.80 (fresh Friday signal — BUY: surged 2.17× weekly on 2022-01-21 (month 1.69×), ladder rising NOW — promoted from the ladder watch; stop ₹10,169.75; charges ₹0.0339)
2022-02-22  GREENLAM    SELL ₹23.53 at stop ₹313.67 (-13.7%, charges ₹0.0244) — the cash goes back to work at the next Friday screen
2022-02-22  LAXMIMACH   SELL ₹28.66 at stop ₹10,169.75 (+0.5%, charges ₹0.0297) — the cash goes back to work at the next Friday screen
2022-02-22  TV18BRDCST  SELL ₹30.06 at stop ₹58.38 (-0.9%, charges ₹0.0312) — the cash goes back to work at the next Friday screen
2022-02-28  ANMOL       BUY ₹27.04 at ₹210.00 (fresh Friday signal — BUY: surged 3.78× weekly on 2022-02-04 (month 1.71×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹194.51; charges ₹0.0320)
2022-02-28  DANGEE      BUY ₹28.30 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0335)
2022-02-28  SHANTIGEAR  BUY ₹28.43 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0337)
2022-03-21  BSE         SELL ₹23.81 at stop ₹1,634.39 (-13.5%, charges ₹0.0247) — the cash goes back to work at the next Friday screen
2022-03-28  KAMATHOTEL  BUY ₹23.81 at ₹71.45 (fresh Friday signal — BUY: 3.56× weekly, month 2.29×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹44.72; charges ₹0.0282)
2022-03-28  RAJRATAN    SELL ₹29.04 at stop ₹1,553.82 (+103.4%, charges ₹0.0301) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹20.5274 paid (STCG ₹93.40 @20%, LTCG ₹14.78 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-05-09  ANMOL       SELL ₹24.99 at stop ₹194.51 (-7.4%, charges ₹0.0259) — the cash goes back to work at the next Friday screen
2022-05-10  KAMATHOTEL  SELL ₹24.24 at stop ₹72.91 (+2.0%, charges ₹0.0251) — the cash goes back to work at the next Friday screen
2022-05-16  KRISHANA    BUY ₹28.51 at ₹67.96 (fresh Friday signal — ACCUMULATE: 1.67× weekly, month 1.86×, ladder rising; stop ₹54.77; charges ₹0.0338)
2022-05-16  VBL         BUY ₹28.51 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0338)
2022-06-06  VBL         SELL ₹25.38 at stop ₹196.27 (-10.8%, charges ₹0.0263) — the cash goes back to work at the next Friday screen
2022-06-09  ADVANIHOTR  SELL ₹18.09 at stop ₹64.65 (-36.5%, charges ₹0.0188) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹28.48 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0337)
2022-06-13  MRPL        BUY ₹15.71 at ₹116.65 (fresh Friday signal — BUY: 3.64× weekly, month 4.35×, ladder rising; stop ₹69.61; charges ₹0.0186)
2022-06-16  KRISHANA    SELL ₹22.93 at stop ₹54.77 (-19.4%, charges ₹0.0238) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹22.93 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.0272)
2022-06-20  JSWENERGY   SELL ₹28.09 at stop ₹201.99 (+146.8%, charges ₹0.0291) — the cash goes back to work at the next Friday screen
2022-06-27  STERTOOLS   BUY ₹28.09 at ₹277.80 (fresh Friday signal — BUY: surged 2.43× weekly on 2022-06-10 (month 1.67×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹188.68; charges ₹0.0333)
2022-07-06  MRPL        SELL ₹9.35 at stop ₹69.61 (-40.3%, charges ₹0.0097) — the cash goes back to work at the next Friday screen
2022-08-12  STERTOOLS   SELL ₹24.12 at stop ₹239.05 (-13.9%, charges ₹0.0250) — the cash goes back to work at the next Friday screen
2022-08-16  MOLDTKPAC   BUY ₹29.55 at ₹927.00 (fresh Friday signal — BUY: 2.90× weekly, month 2.47×, ladder rising; stop ₹758.20; charges ₹0.0350)
2022-09-06  DANGEE      SELL ₹45.09 at stop ₹375.25 (+59.7%, charges ₹0.0468) — the cash goes back to work at the next Friday screen
2022-09-12  CONCOR      BUY ₹17.76 at ₹753.00 (fresh Friday signal — BUY: 6.34× weekly, month 1.83×, ladder rising; stop ₹633.27; charges ₹0.0210)
2022-09-12  SHREECEM    BUY ₹31.25 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0370)
2022-09-29  MOLDTKPAC   SELL ₹27.81 at stop ₹874.43 (-5.7%, charges ₹0.0288) — the cash goes back to work at the next Friday screen
2022-10-03  SUNDARMHLD  BUY ₹27.81 at ₹103.50 (fresh Friday signal — BUY: 7.17× weekly, month 4.00×, ladder rising; stop ₹79.04; charges ₹0.0329)
2022-10-11  SUNDARMHLD  SELL ₹24.72 at stop ₹92.20 (-10.9%, charges ₹0.0256) — the cash goes back to work at the next Friday screen
2022-10-17  FAIRCHEMOR  BUY ₹24.72 at ₹2,240.00 (fresh Friday signal — ACCUMULATE: 2.93× weekly, month 2.97×, ladder rising; stop ₹1,790.15; charges ₹0.0293)
2022-11-01  FAIRCHEMOR  SELL ₹19.71 at stop ₹1,790.15 (-20.1%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2022-11-03  APARINDS    SELL ₹32.71 at stop ₹1,358.50 (+43.0%, charges ₹0.0339) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹32.19 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0381)
2022-11-07  RVNL        BUY ₹20.23 at ₹46.85 (fresh Friday signal — BUY: 4.42× weekly, month 4.42×, ladder rising; stop ₹33.77; charges ₹0.0240)
2022-12-21  ELECON      SELL ₹46.97 at stop ₹202.49 (+65.3%, charges ₹0.0487) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹52.91 at stop ₹345.56 (+86.5%, charges ₹0.0549) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹32.08 at stop ₹139.84 (-0.1%, charges ₹0.0333) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹32.42 at ₹157.00 (fresh Friday signal — BUY: surged 4.56× weekly on 2022-12-02 (month 1.88×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0384)
2022-12-26  KABRAEXTRU  BUY ₹32.17 at ₹441.95 (fresh Friday signal — BUY: surged 6.03× weekly on 2022-11-25 (month 1.74×), ladder rising NOW — promoted from the ladder watch; stop ₹457.95; charges ₹0.0381)
2022-12-26  KRISHANA    BUY ₹32.01 at ₹83.60 (fresh Friday signal — BUY: 3.61× weekly, month 2.28×, ladder rising; stop ₹75.36; charges ₹0.0379)
2022-12-26  KSL         BUY ₹32.34 at ₹330.10 (fresh Friday signal — BUY: surged 5.37× weekly on 2022-12-09 (month 2.54×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0383)
2022-12-26  RVNL        SELL ₹26.10 at stop ₹60.57 (+29.3%, charges ₹0.0271) — the cash goes back to work at the next Friday screen
2023-01-02  MUKANDLTD   BUY ₹29.12 at ₹136.70 (fresh Friday signal — BUY: 6.77× weekly, month 2.54×, ladder rising; stop ₹103.76; charges ₹0.0345)
2023-01-17  CONCOR      SELL ₹16.39 at stop ₹696.30 (-7.5%, charges ₹0.0170) — the cash goes back to work at the next Friday screen
2023-01-27  KSL         SELL ₹32.09 at stop ₹328.23 (-0.6%, charges ₹0.0333) — the cash goes back to work at the next Friday screen
2023-01-30  LSIL        BUY ₹33.01 at ₹23.20 (fresh Friday signal — BUY: 2.27× weekly, month 3.60×, ladder rising; stop ₹11.29; charges ₹0.0391)
2023-02-01  GICRE       SELL ₹34.55 at stop ₹167.72 (+6.8%, charges ₹0.0358) — the cash goes back to work at the next Friday screen
2023-02-06  JINDALSAW   BUY ₹32.16 at ₹65.22 (fresh Friday signal — BUY: 2.71× weekly, month 3.60×, ladder rising; stop ₹51.25; charges ₹0.0381)
2023-02-06  MAHINDCIE   BUY ₹17.86 at ₹395.20 (fresh Friday signal — BUY: 1.58× weekly, month 2.05×, ladder rising; stop ₹328.94; charges ₹0.0212)
2023-02-07  LSIL        SELL ₹28.45 at stop ₹20.04 (-13.6%, charges ₹0.0295) — the cash goes back to work at the next Friday screen
2023-02-13  UNIENTER    BUY ₹28.45 at ₹179.30 (fresh Friday signal — BUY: 19.11× weekly, month 5.40×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹119.20; charges ₹0.0337)
2023-02-17  CGCL        SELL ₹33.59 at stop ₹704.95 (+17.6%, charges ₹0.0348) — the cash goes back to work at the next Friday screen
2023-02-20  TIIL        BUY ₹32.62 at ₹1,116.70 (fresh Friday signal — BUY: 8.50× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0386)
2023-03-10  MAHINDCIE   SELL ₹17.66 at stop ₹391.69 (-0.9%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2023-03-13  KIRLOSIND   BUY ₹18.63 at ₹2,300.00 (fresh Friday signal — ACCUMULATE: 2.65× weekly, month 2.39×, ladder rising; stop ₹2,097.31; charges ₹0.0221)
2023-03-14  KABRAEXTRU  SELL ₹36.82 at stop ₹506.92 (+14.7%, charges ₹0.0382) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹31.25 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.60×, ladder rising; stop ₹691.46; charges ₹0.0370)
2023-03-20  KRISHANA    SELL ₹36.06 at stop ₹94.40 (+12.9%, charges ₹0.0374) — the cash goes back to work at the next Friday screen
2023-03-27  JINDALSAW   SELL ₹33.42 at stop ₹67.92 (+4.1%, charges ₹0.0347) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹31.46 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.85×, ladder rising; stop ₹372.21; charges ₹0.0373)
2023-03-27  UNIENTER    SELL ₹21.89 at stop ₹138.28 (-22.9%, charges ₹0.0227) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹63.06 at stop ₹112.36 (+116.1%, charges ₹0.0654) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹30.33 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.04×, ladder rising; stop ₹1,171.71; charges ₹0.0359)
2023-04-03  INGERRAND   BUY ₹30.28 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.53×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0359)
2023-04-03  KIRLOSBROS  BUY ₹23.32 at ₹414.00 (fresh Friday signal — BUY: surged 2.03× weekly on 2023-03-10 (month 3.68×), ladder rising NOW — promoted from the ladder watch; stop ₹357.44; charges ₹0.0276)
2023-04-03  TAX         FY2023 settled: ₹14.3410 paid (STCG ₹40.06 @20%, LTCG ₹50.64 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-03  TDPOWERSYS  BUY ₹30.26 at ₹79.50 (fresh Friday signal — BUY: surged 2.04× weekly on 2023-03-10 (month 1.65×), ladder rising NOW — promoted from the ladder watch; stop ₹64.12; charges ₹0.0359)
2023-04-24  SHREECEM    SELL ₹29.96 at stop ₹23,636.00 (-3.9%, charges ₹0.0311) — the cash goes back to work at the next Friday screen
2023-04-26  KIRLOSBROS  SELL ₹22.70 at stop ₹403.85 (-2.5%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2023-05-02  FAIRCHEMOR  BUY ₹20.54 at ₹1,272.00 (fresh Friday signal — BUY: 3.67× weekly, month 1.62×, ladder rising; stop ₹1,054.59; charges ₹0.0243)
2023-05-02  GLS         BUY ₹32.12 at ₹509.05 (fresh Friday signal — BUY: 4.14× weekly, month 2.66×, ladder rising; stop ₹351.50; charges ₹0.0381)
2023-05-17  MUKANDLTD   SELL ₹24.71 at stop ₹116.23 (-15.0%, charges ₹0.0256) — the cash goes back to work at the next Friday screen
2023-05-19  FAIRCHEMOR  SELL ₹18.39 at stop ₹1,141.04 (-10.3%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2023-05-22  SHARDAMOTR  BUY ₹32.52 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0385)
2023-07-03  ANURAS      SELL ₹41.57 at stop ₹1,007.67 (+33.3%, charges ₹0.0431) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹34.72 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.44×, ladder rising; stop ₹99.51; charges ₹0.0411)
2023-07-12  KSB         SELL ₹30.62 at stop ₹407.74 (-2.4%, charges ₹0.0318) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹35.67 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0423)
2023-09-13  INGERRAND   SELL ₹33.95 at stop ₹3,022.99 (+12.4%, charges ₹0.0352) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹41.43 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.66×, ladder rising; stop ₹58.28; charges ₹0.0491)
2023-09-25  KIRLOSIND   SELL ₹25.89 at stop ₹3,202.97 (+39.3%, charges ₹0.0269) — the cash goes back to work at the next Friday screen
2023-10-03  PILANIINVS  BUY ₹30.79 at ₹2,380.05 (fresh Friday signal — BUY: 3.07× weekly, month 7.69×, ladder rising; stop ₹2,018.75; charges ₹0.0365)
2023-10-23  SJVN        SELL ₹36.23 at stop ₹66.03 (-12.4%, charges ₹0.0376) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹40.37 at stop ₹1,840.70 (+33.4%, charges ₹0.0419) — the cash goes back to work at the next Friday screen
2023-10-25  SHARDAMOTR  SELL ₹39.71 at stop ₹465.07 (+22.4%, charges ₹0.0412) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹34.23 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0406)
2023-10-30  KKCL        BUY ₹41.06 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.93×, ladder rising; stop ₹674.12; charges ₹0.0486)
2023-10-30  SHAREINDIA  BUY ₹41.02 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.63×, ladder rising; stop ₹261.25; charges ₹0.0486)
2023-11-16  GENUSPOWER  SELL ₹49.78 at stop ₹234.03 (+43.7%, charges ₹0.0516) — the cash goes back to work at the next Friday screen
2023-11-20  ISMTLTD     BUY ₹45.00 at ₹94.60 (fresh Friday signal — BUY: 5.37× weekly, month 1.92×, ladder rising; stop ₹80.18; charges ₹0.0533)
2023-12-20  ISMTLTD     SELL ₹41.93 at stop ₹88.35 (-6.6%, charges ₹0.0435) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹46.71 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0553)
2024-01-17  TIIL        SELL ₹68.11 at stop ₹2,337.00 (+109.3%, charges ₹0.0706) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹48.60 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0576)
2024-01-30  MMFL        SELL ₹41.53 at stop ₹912.05 (-10.9%, charges ₹0.0431) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹52.56 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0623)
2024-03-05  GLS         SELL ₹49.07 at stop ₹779.48 (+53.1%, charges ₹0.0509) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹48.74 at stop ₹357.20 (+19.1%, charges ₹0.0506) — the cash goes back to work at the next Friday screen
2024-03-11  DOLLAR      BUY ₹52.94 at ₹527.95 (fresh Friday signal — BUY: 4.55× weekly, month 2.48×, ladder rising; stop ₹461.65; charges ₹0.0627)
2024-03-11  SOLARINDS   BUY ₹52.83 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0626)
2024-03-11  TCI         SELL ₹41.97 at stop ₹790.40 (-20.0%, charges ₹0.0435) — the cash goes back to work at the next Friday screen
2024-03-13  DOLLAR      SELL ₹46.19 at stop ₹461.65 (-12.6%, charges ₹0.0479) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹36.25 at stop ₹674.12 (-11.5%, charges ₹0.0376) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹48.71 at stop ₹666.47 (+0.5%, charges ₹0.0505) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹50.35 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0597)
2024-03-18  FORCEMOT    BUY ₹50.12 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.51×, ladder rising; stop ₹5,500.61; charges ₹0.0594)
2024-03-18  INDIGO      BUY ₹50.05 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0593)
2024-03-27  ANANDRATHI  SELL ₹115.55 at stop ₹862.65 (+224.7%, charges ₹0.1199) — the cash goes back to work at the next Friday screen
2024-04-01  DMART       BUY ₹49.07 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; stop ₹3,695.50; charges ₹0.0581)
2024-04-01  SHRIRAMFIN  BUY ₹48.95 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0580)
2024-04-01  TAX         FY2024 settled: ₹30.1324 paid (STCG ₹150.66 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-09  PILANIINVS  SELL ₹47.90 at stop ₹3,710.37 (+55.9%, charges ₹0.0497) — the cash goes back to work at the next Friday screen
2024-05-13  JWL         BUY ₹51.02 at ₹490.00 (fresh Friday signal — BUY: 7.12× weekly, month 2.51×, ladder rising; stop ₹370.93; charges ₹0.0604)
2024-05-28  FORCEMOT    SELL ₹61.55 at stop ₹8,083.64 (+23.1%, charges ₹0.0638) — the cash goes back to work at the next Friday screen
2024-05-31  DMART       SELL ₹46.31 at stop ₹4,322.83 (-5.4%, charges ₹0.0480) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹53.90 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0639)
2024-06-03  THERMAX     BUY ₹53.69 at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.0636)
2024-06-04  BOSCHLTD    SELL ₹49.41 at stop ₹29,015.09 (-1.6%, charges ₹0.0513) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹45.50 at stop ₹441.77 (-6.8%, charges ₹0.0472) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹55.62 at stop ₹7,980.95 (+5.5%, charges ₹0.0577) — the cash goes back to work at the next Friday screen
2024-06-10  ARE&M       BUY ₹51.16 at ₹1,450.00 (fresh Friday signal — BUY: 3.00× weekly, month 2.35×, ladder rising; stop ₹916.60; charges ₹0.0606)
2024-06-10  FIEMIND     BUY ₹51.45 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0610)
2024-06-10  UNOMINDA    BUY ₹51.29 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0608)
2024-07-19  TDPOWERSYS  SELL ₹71.68 at stop ₹188.72 (+137.4%, charges ₹0.0743) — the cash goes back to work at the next Friday screen
2024-07-19  UNOMINDA    SELL ₹51.80 at stop ₹981.87 (+1.2%, charges ₹0.0537) — the cash goes back to work at the next Friday screen
2024-07-22  ARE&M       SELL ₹52.88 at stop ₹1,502.14 (+3.6%, charges ₹0.0549) — the cash goes back to work at the next Friday screen
2024-07-22  ESABINDIA   BUY ₹52.18 at ₹6,486.15 (fresh Friday signal — BUY: 2.98× weekly, month 1.72×, ladder rising; stop ₹5,682.38; charges ₹0.0618)
2024-07-22  INDIAGLYCO  BUY ₹52.13 at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹0.0618)
2024-07-23  FIEMIND     SELL ₹48.91 at stop ₹1,257.56 (-4.7%, charges ₹0.0507) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹53.04 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0628)
2024-07-29  THYROCARE   BUY ₹53.09 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0629)
2024-08-05  THERMAX     SELL ₹44.83 at stop ₹4,719.70 (-16.3%, charges ₹0.0465) — the cash goes back to work at the next Friday screen
2024-08-06  JWL         SELL ₹57.34 at stop ₹552.00 (+12.7%, charges ₹0.0595) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹52.17 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0618)
2024-08-12  CERA        BUY ₹52.09 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹0.0617)
2024-08-16  CAMPUS      SELL ₹52.10 at stop ₹277.07 (-3.1%, charges ₹0.0540) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹51.00 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0604)
2024-09-09  AVANTIFEED  SELL ₹49.32 at stop ₹650.13 (-6.8%, charges ₹0.0512) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹51.96 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0616)
2024-09-19  CERA        SELL ₹40.59 at stop ₹8,198.93 (-21.9%, charges ₹0.0421) — the cash goes back to work at the next Friday screen
2024-09-23  ALKYLAMINE  BUY ₹51.88 at ₹2,432.85 (fresh Friday signal — BUY: 9.32× weekly, month 3.52×, ladder rising; stop ₹2,106.24; charges ₹0.0615)
2024-10-07  INDIGO      SELL ₹69.99 at stop ₹4,485.14 (+40.2%, charges ₹0.0726) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹53.72 at stop ₹796.15 (+1.4%, charges ₹0.0557) — the cash goes back to work at the next Friday screen
2024-10-14  ASTRAZEN    BUY ₹51.26 at ₹7,800.00 (fresh Friday signal — ACCUMULATE: 3.65× weekly, month 8.83×, ladder rising; stop ₹6,768.80; charges ₹0.0607)
2024-10-14  DBCORP      BUY ₹51.46 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0610)
2024-10-21  MOTILALOFS  BUY ₹25.21 at ₹1,021.95 (fresh Friday signal — BUY: 7.74× weekly, month 5.64×, ladder rising; stop ₹656.59; charges ₹0.0299)
2024-10-22  ALKYLAMINE  SELL ₹44.82 at stop ₹2,106.24 (-13.4%, charges ₹0.0465) — the cash goes back to work at the next Friday screen
2024-10-22  BASF        SELL ₹53.90 at stop ₹7,611.30 (+3.6%, charges ₹0.0559) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹44.06 at stop ₹302.08 (-14.2%, charges ₹0.0457) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹59.38 at stop ₹587.91 (+14.2%, charges ₹0.0616) — the cash goes back to work at the next Friday screen
2024-10-28  CARERATING  BUY ₹42.27 at ₹1,396.00 (fresh Friday signal — BUY: surged 3.30× weekly on 2024-10-11 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹1,066.23; charges ₹0.0501)
2024-10-28  CUPID       SELL ₹44.78 at stop ₹158.66 (+31.1%, charges ₹0.0465) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹42.36 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.0502)
2024-10-28  VISHNU      BUY ₹42.42 at ₹511.90 (fresh Friday signal — BUY: 4.02× weekly, month 1.75×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹399.95; charges ₹0.0503)
2024-11-04  AKZOINDIA   BUY ₹48.21 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.1138)
2024-11-04  KIRLPNU     BUY ₹47.95 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.1132)
2024-11-12  VISHNU      SELL ₹38.84 at stop ₹470.30 (-8.1%, charges ₹0.0863) — the cash goes back to work at the next Friday screen
2024-11-13  ESABINDIA   SELL ₹46.85 at stop ₹5,842.74 (-9.9%, charges ₹0.1041) — the cash goes back to work at the next Friday screen
2024-11-14  ASTRAZEN    SELL ₹44.89 at stop ₹6,854.77 (-12.1%, charges ₹0.0997) — the cash goes back to work at the next Friday screen
2024-11-18  GANESHHOUC  BUY ₹44.76 at ₹1,059.00 (fresh Friday signal — BUY: surged 4.01× weekly on 2024-10-18 (month 1.75×), ladder rising NOW — promoted from the ladder watch; stop ₹867.10; charges ₹0.1057)
2024-11-18  JSWHL       BUY ₹45.12 at ₹19,990.00 (fresh Friday signal — BUY: 3.46× weekly, month 4.62×, ladder rising; stop ₹8,434.53; charges ₹0.1065)
2024-11-18  SASKEN      BUY ₹44.95 at ₹2,015.25 (fresh Friday signal — BUY: 9.07× weekly, month 2.15×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹1,640.65; charges ₹0.1061)
2024-12-17  SUPRIYA     SELL ₹69.04 at stop ₹717.25 (+35.8%, charges ₹0.1533) — the cash goes back to work at the next Friday screen
2024-12-23  EMSLIMITED  BUY ₹42.10 at ₹916.85 (fresh Friday signal — BUY: 5.57× weekly, month 2.01×, ladder rising; stop ₹802.65; charges ₹0.0994)
2024-12-23  KIRLPNU     SELL ₹44.86 at stop ₹1,596.00 (-6.0%, charges ₹0.0996) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹46.43 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.1096)
2024-12-26  PRSMJOHNSN  SELL ₹41.17 at stop ₹170.55 (-20.5%, charges ₹0.0914) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹36.36 at stop ₹3,423.18 (-24.2%, charges ₹0.0808) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹46.31 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.1093)
2024-12-30  KFINTECH    BUY ₹46.15 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.1089)
2024-12-30  NACLIND     BUY ₹29.94 at ₹67.60 (fresh Friday signal — BUY: 1.75× weekly, month 2.31×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹53.45; charges ₹0.0707)
2025-01-09  KSL         SELL ₹41.07 at stop ₹1,059.30 (-11.1%, charges ₹0.0912) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹50.42 at stop ₹893.05 (+19.4%, charges ₹0.1120) — the cash goes back to work at the next Friday screen
2025-01-10  EMSLIMITED  SELL ₹36.69 at stop ₹802.65 (-12.5%, charges ₹0.0815) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹42.89 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.1013)
2025-01-13  CARERATING  SELL ₹37.41 at stop ₹1,239.70 (-11.2%, charges ₹0.0831) — the cash goes back to work at the next Friday screen
2025-01-13  LLOYDSME    BUY ₹42.78 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.98×, ladder rising; stop ₹1,258.75; charges ₹0.1010)
2025-01-13  ZOTA        BUY ₹42.51 at ₹965.00 (fresh Friday signal — BUY: surged 1.85× weekly on 2024-12-27 (month 1.96×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹736.25; charges ₹0.1003)
2025-01-15  KFINTECH    SELL ₹35.23 at stop ₹1,159.14 (-23.3%, charges ₹0.0782) — the cash goes back to work at the next Friday screen
2025-01-17  MOTILALOFS  SELL ₹19.39 at stop ₹788.79 (-22.8%, charges ₹0.0431) — the cash goes back to work at the next Friday screen
2025-01-20  APOLLO      BUY ₹43.33 at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 3.48×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹110.19; charges ₹0.1023)
2025-01-20  BAJAJHCARE  BUY ₹43.97 at ₹690.00 (fresh Friday signal — BUY: 1.75× weekly, month 4.12×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹451.06; charges ₹0.1038)
2025-01-21  SASKEN      SELL ₹44.25 at stop ₹1,993.24 (-1.1%, charges ₹0.0983) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹35.83 at stop ₹700.36 (-16.1%, charges ₹0.0796) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹39.94 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0943)
2025-01-27  MBAPL       BUY ₹40.27 at ₹58.20 (fresh Friday signal — ACCUMULATE: 3.22× weekly, month 3.87×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹50.92; charges ₹0.0951)
2025-01-27  NACLIND     SELL ₹27.02 at stop ₹61.28 (-9.3%, charges ₹0.0600) — the cash goes back to work at the next Friday screen
2025-01-28  LLOYDSME    SELL ₹37.17 at stop ₹1,258.75 (-12.7%, charges ₹0.0826) — the cash goes back to work at the next Friday screen
2025-01-28  ZOTA        SELL ₹37.87 at stop ₹863.60 (-10.5%, charges ₹0.0841) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹41.83 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.0987)
2025-02-12  JINDWORLD   SELL ₹42.30 at stop ₹374.11 (-8.2%, charges ₹0.0940) — the cash goes back to work at the next Friday screen
2025-02-17  APOLLO      SELL ₹36.14 at stop ₹110.19 (-16.2%, charges ₹0.0803) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹38.50 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0909)
2025-02-24  MPSLTD      BUY ₹38.36 at ₹2,648.95 (fresh Friday signal — BUY: surged 3.92× weekly on 2025-01-31 (month 3.29×), ladder rising NOW — promoted from the ladder watch; stop ₹2,360.51; charges ₹0.0906)
2025-02-24  TAJGVK      BUY ₹28.13 at ₹440.40 (fresh Friday signal — BUY: 2.16× weekly, month 2.07×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹349.09; charges ₹0.0664)
2025-02-24  TCPLPACK    BUY ₹38.29 at ₹3,997.25 (fresh Friday signal — BUY: 8.08× weekly, month 1.73×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹2,770.57; charges ₹0.0904)
2025-02-25  MPSLTD      SELL ₹34.03 at stop ₹2,360.51 (-10.9%, charges ₹0.0756) — the cash goes back to work at the next Friday screen
2025-02-28  GANESHHOUC  SELL ₹45.88 at stop ₹1,090.38 (+3.0%, charges ₹0.1019) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹37.12 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0876)
2025-03-03  ZENSARTECH  SELL ₹32.00 at stop ₹727.84 (-23.1%, charges ₹0.0711) — the cash goes back to work at the next Friday screen
2025-03-10  GRMOVER     BUY ₹35.49 at ₹252.00 (fresh Friday signal — BUY: surged 3.52× weekly on 2025-02-07 (month 1.72×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹203.86; charges ₹0.0838)
2025-03-10  GRWRHITECH  BUY ₹39.30 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.0928)
2025-03-27  MBAPL       SELL ₹36.78 at stop ₹53.39 (-8.3%, charges ₹0.0817) — the cash goes back to work at the next Friday screen
2025-04-01  TAX         FY2025 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹17.92 / LT ₹0.00)
2025-04-02  TAJGVK      SELL ₹28.83 at stop ₹453.34 (+2.9%, charges ₹0.0640) — the cash goes back to work at the next Friday screen
2025-04-03  GRWRHITECH  SELL ₹33.40 at stop ₹3,602.82 (-14.6%, charges ₹0.0742) — the cash goes back to work at the next Friday screen
2025-04-07  BAJAJHCARE  SELL ₹33.06 at stop ₹521.14 (-24.5%, charges ₹0.0734) — the cash goes back to work at the next Friday screen
2025-04-07  NACLIND     BUY ₹40.26 at ₹128.14 (fresh Friday signal — BUY: surged 9.31× weekly on 2025-03-21 (month 10.01×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹89.22; charges ₹0.0950)
2025-04-07  ROHLTD      BUY ₹40.03 at ₹341.50 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 1.60×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹359.48; charges ₹0.0945)
2025-04-07  TCPLPACK    SELL ₹38.16 at stop ₹4,002.68 (+0.1%, charges ₹0.0848) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹42.94 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.62× weekly, month 1.80×, ladder rising; stop ₹492.75; charges ₹0.1014)
2025-04-15  INDIASHLTR  BUY ₹43.11 at ₹865.00 (fresh Friday signal — BUY: 1.57× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.1018)
2025-04-30  ROHLTD      SELL ₹42.74 at stop ₹366.23 (+7.2%, charges ₹0.0949) — the cash goes back to work at the next Friday screen
2025-05-05  PARAS       BUY ₹44.82 at ₹1,372.20 (fresh Friday signal — BUY: 25.15× weekly, month 2.24×, ladder rising; stop ₹973.27; charges ₹0.1058)
2025-05-07  GRMOVER     SELL ₹40.77 at stop ₹290.80 (+15.4%, charges ₹0.0906) — the cash goes back to work at the next Friday screen
2025-05-12  KPRMILL     BUY ₹42.57 at ₹1,302.00 (fresh Friday signal — BUY: 15.89× weekly, month 3.16×, ladder rising; stop ₹938.50; charges ₹0.1005)
2025-07-04  PARAS       SELL ₹46.10 at stop ₹1,417.98 (+3.3%, charges ₹0.1024) — the cash goes back to work at the next Friday screen
2025-07-07  ASTERDM     BUY ₹43.99 at ₹633.90 (fresh Friday signal — BUY: 6.11× weekly, month 1.59×, ladder rising; stop ₹509.77; charges ₹0.1038)
2025-08-01  KPRMILL     SELL ₹36.08 at stop ₹1,108.74 (-14.8%, charges ₹0.0801) — the cash goes back to work at the next Friday screen
2025-08-04  JSWHL       SELL ₹42.93 at stop ₹19,106.01 (-4.4%, charges ₹0.0954) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹46.24 at stop ₹1,814.78 (+25.2%, charges ₹0.1027) — the cash goes back to work at the next Friday screen
2025-08-04  PGHL        BUY ₹38.19 at ₹6,440.00 (fresh Friday signal — BUY: 6.30× weekly, month 2.58×, ladder rising; stop ₹5,320.00; charges ₹0.0902)
2025-08-11  PRAKASH     BUY ₹42.64 at ₹178.70 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 2.59×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹145.68; charges ₹0.1007)
2025-08-11  RAIN        BUY ₹42.71 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.1008)
2025-08-26  RAIN        SELL ₹38.11 at stop ₹143.64 (-10.4%, charges ₹0.0847) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹41.92 at ₹460.00 (fresh Friday signal — BUY: 3.51× weekly, month 6.62×, ladder rising; stop ₹394.44; charges ₹0.0990)
2025-09-16  GODFRYPHLP  SELL ₹59.45 at stop ₹8,967.50 (+55.1%, charges ₹0.1321) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹42.19 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.81× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.0996)
2025-09-24  RSYSTEMS    SELL ₹38.40 at stop ₹423.23 (-8.0%, charges ₹0.0853) — the cash goes back to work at the next Friday screen
2025-09-26  INDIASHLTR  SELL ₹42.56 at stop ₹857.85 (-0.8%, charges ₹0.0945) — the cash goes back to work at the next Friday screen
2025-09-29  NLCINDIA    BUY ₹41.09 at ₹280.30 (fresh Friday signal — BUY: 4.26× weekly, month 1.81×, ladder rising; stop ₹241.39; charges ₹0.0970)
2025-09-29  SUBROS      BUY ₹40.88 at ₹1,132.00 (fresh Friday signal — BUY: 8.24× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0965)
2025-10-14  SUBROS      SELL ₹37.63 at stop ₹1,046.90 (-7.5%, charges ₹0.0836) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹40.70 at ₹1,574.50 (fresh Friday signal — BUY: 13.09× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0961)
2025-10-20  CREDITACC   SELL ₹59.61 at stop ₹1,274.42 (+49.9%, charges ₹0.1324) — the cash goes back to work at the next Friday screen
2025-10-27  HCG         BUY ₹40.75 at ₹758.60 (fresh Friday signal — BUY: surged 2.61× weekly on 2025-10-17 (month 1.50×), ladder rising NOW — promoted from the ladder watch; stop ₹674.50; charges ₹0.0962)
2025-10-27  SKYGOLD     BUY ₹32.03 at ₹370.00 (fresh Friday signal — BUY: surged 2.31× weekly on 2025-10-10 (month 1.67×), ladder rising NOW — promoted from the ladder watch; stop ₹304.38; charges ₹0.0756)
2025-11-06  FDC         SELL ₹36.53 at stop ₹425.79 (-13.0%, charges ₹0.0811) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹35.06 at stop ₹5,938.45 (-7.8%, charges ₹0.0779) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹39.88 at ₹1,014.90 (fresh Friday signal — BUY: 23.91× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0941)
2025-11-10  CUB         BUY ₹31.71 at ₹254.20 (fresh Friday signal — BUY: 6.08× weekly, month 1.73×, ladder rising; stop ₹213.75; charges ₹0.0748)
2025-11-14  PRAKASH     SELL ₹34.99 at stop ₹147.31 (-17.6%, charges ₹0.0777) — the cash goes back to work at the next Friday screen
2025-11-17  PGIL        BUY ₹34.99 at ₹844.05 (fresh Friday signal — BUY: 19.68× weekly, month 3.52×, ladder rising; stop ₹612.56; charges ₹0.0826)
2025-11-20  ANANDRATHI  SELL ₹37.32 at stop ₹1,450.17 (-7.9%, charges ₹0.0829) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹38.19 at stop ₹976.41 (-3.8%, charges ₹0.0848) — the cash goes back to work at the next Friday screen
2025-11-24  NLCINDIA    SELL ₹35.23 at stop ₹241.39 (-13.9%, charges ₹0.0782) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹37.32 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0881)
2025-11-25  SKYGOLD     SELL ₹28.37 at stop ₹329.13 (-11.0%, charges ₹0.0630) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹39.49 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.34×, ladder rising; stop ₹535.37; charges ₹0.0932)
2025-12-01  GMRAIRPORT  BUY ₹22.88 at ₹108.90 (fresh Friday signal — BUY: 1.69× weekly, month 1.85×, ladder rising; stop ₹89.73; charges ₹0.0540)
2025-12-01  SANSERA     BUY ₹39.42 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.55×, ladder rising; stop ₹1,413.60; charges ₹0.0930)
2025-12-05  ASTERDM     SELL ₹44.46 at stop ₹643.62 (+1.5%, charges ₹0.0988) — the cash goes back to work at the next Friday screen
2025-12-08  KIRLOSENG   BUY ₹37.55 at ₹1,130.00 (fresh Friday signal — BUY: 1.67× weekly, month 2.31×, ladder rising; stop ₹886.54; charges ₹0.0886)
2025-12-09  PGIL        SELL ₹31.60 at stop ₹765.71 (-9.3%, charges ₹0.0702) — the cash goes back to work at the next Friday screen
2025-12-15  ESABINDIA   BUY ₹37.92 at ₹6,203.50 (fresh Friday signal — BUY: surged 27.55× weekly on 2025-11-14 (month 4.45×), ladder rising NOW — promoted from the ladder watch; stop ₹5,247.99; charges ₹0.0895)
2025-12-17  NACLIND     SELL ₹51.35 at stop ₹164.20 (+28.1%, charges ₹0.1141) — the cash goes back to work at the next Friday screen
2025-12-22  ASHAPURMIN  BUY ₹38.49 at ₹800.00 (fresh Friday signal — BUY: surged 1.56× weekly on 2025-11-21 (month 1.64×), ladder rising NOW — promoted from the ladder watch; stop ₹641.35; charges ₹0.0909)
2025-12-23  HCG         SELL ₹36.18 at stop ₹676.59 (-10.8%, charges ₹0.0804) — the cash goes back to work at the next Friday screen
2025-12-29  SHRIRAMFIN  BUY ₹38.36 at ₹963.00 (fresh Friday signal — BUY: 1.70× weekly, month 1.58×, ladder rising; stop ₹778.00; charges ₹0.0905)
2026-01-08  EUREKAFORB  SELL ₹34.88 at stop ₹589.10 (-11.3%, charges ₹0.0775) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹33.39 at stop ₹2,956.49 (-10.1%, charges ₹0.0742) — the cash goes back to work at the next Friday screen
2026-01-12  ESABINDIA   SELL ₹34.11 at stop ₹5,605.00 (-9.6%, charges ₹0.0758) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹36.98 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.95×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.0873)
2026-01-12  KIRLOSENG   SELL ₹37.74 at stop ₹1,140.95 (+1.0%, charges ₹0.0838) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹37.01 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0874)
2026-01-16  ASHAPURMIN  SELL ₹39.13 at stop ₹817.00 (+2.1%, charges ₹0.0869) — the cash goes back to work at the next Friday screen
2026-01-19  KIRIINDUS   BUY ₹36.87 at ₹530.30 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 9.40×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹382.56; charges ₹0.0870)
2026-01-19  NITCO       BUY ₹36.95 at ₹89.00 (fresh Friday signal — ACCUMULATE: 5.88× weekly, month 2.19×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹75.12; charges ₹0.0872)
2026-01-19  RBA         BUY ₹36.99 at ₹67.50 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.49×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0873)
2026-01-21  AVANTIFEED  SELL ₹39.12 at stop ₹748.60 (-8.5%, charges ₹0.0869) — the cash goes back to work at the next Friday screen
2026-01-23  GMRAIRPORT  SELL ₹19.26 at stop ₹92.10 (-15.4%, charges ₹0.0428) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹37.51 at stop ₹1,672.76 (-4.4%, charges ₹0.0833) — the cash goes back to work at the next Friday screen
2026-01-27  INFOBEAN    BUY ₹35.60 at ₹813.10 (fresh Friday signal — ACCUMULATE: 3.29× weekly, month 6.84×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹683.81; charges ₹0.0840)
2026-01-27  JAYBARMARU  BUY ₹35.27 at ₹84.25 (fresh Friday signal — BUY: surged 4.48× weekly on 2026-01-02 (month 2.25×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹85.51; charges ₹0.0833)
2026-01-28  JAYBARMARU  SELL ₹35.64 at stop ₹85.51 (+1.5%, charges ₹0.0792) — the cash goes back to work at the next Friday screen
2026-02-02  AGIIL       BUY ₹35.81 at ₹249.80 (fresh Friday signal — ACCUMULATE: 1.51× weekly, month 2.66×, ladder rising; outside the top 750 by size — funded after the large names; stop ₹202.47; charges ₹0.0845)
2026-02-02  AWHCL       BUY ₹30.55 at ₹520.05 (fresh Friday signal — BUY: surged 3.63× weekly on 2026-01-23 (month 4.12×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹467.40; charges ₹0.0721)
2026-02-17  NATIONALUM  SELL ₹35.11 at stop ₹335.49 (-4.7%, charges ₹0.0780) — the cash goes back to work at the next Friday screen
2026-02-19  NITCO       SELL ₹31.04 at stop ₹75.12 (-15.6%, charges ₹0.0690) — the cash goes back to work at the next Friday screen
2026-02-23  E2E         BUY ₹30.41 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0718)
2026-02-23  VESUVIUS    BUY ₹35.74 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.56×, ladder rising; stop ₹464.31; charges ₹0.0844)
2026-02-27  INFOBEAN    SELL ₹33.56 at stop ₹770.07 (-5.3%, charges ₹0.0746) — the cash goes back to work at the next Friday screen
2026-03-02  KIRIINDUS   SELL ₹29.59 at stop ₹427.56 (-19.4%, charges ₹0.0657) — the cash goes back to work at the next Friday screen
2026-03-02  KSB         BUY ₹33.56 at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.75×, ladder rising; stop ₹658.54; charges ₹0.0792)
2026-03-04  AWHCL       SELL ₹27.33 at stop ₹467.40 (-10.1%, charges ₹0.0607) — the cash goes back to work at the next Friday screen
2026-03-04  SHRIRAMFIN  SELL ₹39.34 at stop ₹992.37 (+3.0%, charges ₹0.0874) — the cash goes back to work at the next Friday screen
2026-03-09  AEROFLEX    BUY ₹33.68 at ₹215.00 (fresh Friday signal — BUY: surged 4.38× weekly on 2026-02-20 (month 2.07×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹202.35; charges ₹0.0795)
2026-03-09  CUB         SELL ₹31.22 at stop ₹251.43 (-1.1%, charges ₹0.0693) — the cash goes back to work at the next Friday screen
2026-03-09  PRECWIRE    BUY ₹33.63 at ₹328.00 (fresh Friday signal — BUY: surged 8.31× weekly on 2026-02-20 (month 3.38×), ladder rising NOW — promoted from the ladder watch; stop ₹268.96; charges ₹0.0794)
2026-03-12  HINDCOPPER  SELL ₹36.58 at stop ₹528.63 (-0.6%, charges ₹0.0812) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹33.32 at stop ₹61.08 (-9.5%, charges ₹0.0740) — the cash goes back to work at the next Friday screen
2026-03-16  ABB         BUY ₹33.44 at ₹6,400.00 (fresh Friday signal — BUY: 1.80× weekly, month 1.91×, ladder rising; stop ₹5,486.25; charges ₹0.0789)
2026-03-16  DEEDEV      BUY ₹29.66 at ₹303.25 (fresh Friday signal — BUY: surged 106.37× weekly on 2026-02-27 (month 37.11×), ladder rising NOW — promoted from the ladder watch; outside the top 750 by size — funded after the large names; stop ₹241.30; charges ₹0.0700)
2026-03-16  J&KBANK     BUY ₹33.45 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.94×, ladder rising; stop ₹103.27; charges ₹0.0790)
2026-03-16  JBCHEPHARM  BUY ₹33.52 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0791)
2026-03-23  J&KBANK     SELL ₹30.42 at stop ₹110.67 (-8.6%, charges ₹0.0676) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹30.87 at stop ₹464.31 (-13.2%, charges ₹0.0686) — the cash goes back to work at the next Friday screen
2026-03-30  AETHER      BUY ₹32.10 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0758)
2026-03-30  AGIIL       SELL ₹38.79 at stop ₹271.80 (+8.8%, charges ₹0.0861) — the cash goes back to work at the next Friday screen
2026-03-30  VTL         BUY ₹29.19 at ₹520.95 (fresh Friday signal — BUY: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0689)
2026-04-01  TAX         FY2026 settled: ₹0.0000 paid (STCG ₹0.00 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹64.26 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹32.65 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.64×, ladder rising; stop ₹891.29; charges ₹0.0771)
2026-05-04  KSB         SELL ₹41.53 at stop ₹917.42 (+24.3%, charges ₹0.0923) — the cash goes back to work at the next Friday screen
2026-05-11  CRAFTSMAN   BUY ₹39.66 at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹0.0936)
2026-05-14  AETHER      SELL ₹31.27 at stop ₹1,125.84 (-2.1%, charges ₹0.0695) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹37.78 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.24×, ladder rising; stop ₹1,502.04; charges ₹0.0892)
2026-06-05  E2E         SELL ₹24.21 at stop ₹2,330.72 (-20.0%, charges ₹0.0538) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹25.72 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0607)
2026-07-07  AEROFLEX    SELL ₹66.70 at stop ₹427.69 (+98.9%, charges ₹0.1482) — the cash goes back to work at the next Friday screen
2026-07-07  PRECWIRE    SELL ₹38.40 at stop ₹376.20 (+14.7%, charges ₹0.0853) — the cash goes back to work at the next Friday screen
2026-07-13  GANESHHOU   BUY ₹41.39 at ₹860.50 (fresh Friday signal — BUY: 9.80× weekly, month 2.00×, ladder rising; stop ₹712.60; charges ₹0.0977)
2026-07-13  RITES       BUY ₹41.44 at ₹228.43 (fresh Friday signal — ACCUMULATE: 9.47× weekly, month 9.78×, ladder rising; stop ₹204.60; charges ₹0.0978)
2026-07-13  SGMART      BUY ₹22.27 at ₹646.30 (fresh Friday signal — BUY: 7.16× weekly, month 1.85×, ladder rising; stop ₹532.24; charges ₹0.0526)
2026-07-31  VTL         SELL ₹33.06 at stop ₹592.80 (+13.8%, charges ₹0.0734) — the cash goes back to work at the next Friday screen
2026-08-03  TMB         BUY ₹33.06 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.0780)
2026-09-10  ALKYLAMINE  SELL ₹42.25 at stop ₹1,920.99 (+12.3%, charges ₹0.0938) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹37.23 at stop ₹7,158.25 (+11.8%, charges ₹0.0827) — the cash goes back to work at the next Friday screen
2026-09-15  SGMART      SELL ₹25.59 at stop ₹746.03 (+15.4%, charges ₹0.0568) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹42.25 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.0997)
2026-09-16  RITES       SELL ₹36.99 at stop ₹204.83 (-10.3%, charges ₹0.0822) — the cash goes back to work at the next Friday screen
2026-09-21  ACMESOLAR   BUY ₹44.29 at ₹439.00 (fresh Friday signal — BUY: 1.96× weekly, month 1.82×, ladder rising; stop ₹370.12; charges ₹0.1045)
2026-09-21  AVALON      BUY ₹44.41 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.1048)
```
