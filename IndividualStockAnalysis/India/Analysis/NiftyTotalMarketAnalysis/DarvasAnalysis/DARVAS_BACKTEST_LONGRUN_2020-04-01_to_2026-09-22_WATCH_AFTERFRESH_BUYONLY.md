# The Darvas screen, run for 6.5 years — 2020-04-01 → 2026-09-22

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-22, 1388 symbols, fetched once into `ROLLING_MCAP750_2019-06-01_to_2026-09-22/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **SURVIVORSHIP BIAS REMOVED — the universe is POINT-IN-TIME with a rolling radar:** membership is recomputed EVERY MONTH as the top 750 stocks by the TRAILING month's actual traded value from NSE's official bhavcopies, with hysteresis (leave only past rank 900) — companies that later died are IN while they traded, and a NEW LISTING is excluded for its FIRST THREE MONTHS, entering only once seasoned. ETFs and funds are excluded outright — stocks only. Membership gates fresh entries; a held position runs to its stop regardless (`_membership_long.csv`). Split/bonus adjustments on raw exchange data are heuristic, every one listed in `_adjustments.csv`. No costs where the gross run is shown, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹461.09** | **+26.65% a year** |
| The same system before costs and taxes | ₹608.13 | +32.19% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹289.64 | +17.87% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹5.13 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹455.96** (+26.43% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.47 years, 339 weekly screens, 434 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹19.54** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹61.17**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹43.74 | ₹0.00 | ₹8.7489 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹27.10 | ₹24.91 | ₹8.5341 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹40.03 | ₹47.08 | ₹13.8916 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹122.03 | ₹0.00 | ₹24.4060 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹0.00 | ₹15.89 | ₹1.9858 | ₹0.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹18.03 | ₹0.00 | ₹3.6056 | ₹0.00 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹25.64 | ₹0.00 | ₹5.1286 | ₹0.00 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 150.45 | +50.4% | +51.2% | +70.1% |
| 2021 (2021-12-31) | 235.12 | +56.3% | +66.4% | +26.2% |
| 2022 (2022-12-30) | 278.01 | +18.2% | +22.7% | +4.3% |
| 2023 (2023-12-29) | 410.42 | +47.6% | +56.4% | +20.0% |
| 2024 (2024-12-27) | 416.56 | +1.5% | +8.9% | +9.6% |
| 2025 (2025-12-26) | 409.84 | -1.6% | +0.5% | +9.4% |
| 2026 (2026-09-22) | 461.09 | +12.5% | +15.1% | -10.1% |

## What it took to earn it

- **Maximum drawdown: -27.5%** (peak 2024-07-05 → trough 2026-04-02, on weekly closes).
- **204 closed trades**: 94 winners (46%), average winner +34.7%, average loser -10.2%.
- Best closed trade ANANDRATHI +224.7%; worst AKZOINDIA -24.2%.
- Median holding period 66 days.
- Cash share of equity averaged 10% across all weeks (median 1%); the portfolio sat FULLY in cash for 2 of 339 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-04-30 | 100.20 | 59.96 | 4 |
| 2020-05-29 | 102.93 | 0.00 | 10 |
| 2020-06-26 | 115.37 | 0.00 | 10 |
| 2020-07-31 | 123.54 | 0.00 | 10 |
| 2020-08-28 | 126.10 | 0.00 | 10 |
| 2020-09-25 | 127.74 | 20.21 | 8 |
| 2020-10-30 | 121.92 | 0.00 | 10 |
| 2020-11-27 | 128.11 | 0.00 | 11 |
| 2020-12-24 | 150.45 | 40.47 | 8 |
| 2021-01-29 | 149.66 | 27.58 | 9 |
| 2021-02-26 | 161.46 | 19.11 | 9 |
| 2021-03-26 | 159.63 | 14.01 | 9 |
| 2021-04-30 | 163.84 | 0.00 | 10 |
| 2021-05-28 | 177.69 | 0.00 | 10 |
| 2021-06-25 | 197.86 | 0.00 | 10 |
| 2021-07-30 | 238.29 | 0.00 | 10 |
| 2021-08-27 | 231.99 | 0.00 | 10 |
| 2021-09-24 | 235.72 | 24.25 | 9 |
| 2021-10-29 | 233.59 | 43.35 | 8 |
| 2021-11-26 | 239.34 | 81.78 | 6 |
| 2021-12-31 | 235.12 | 0.00 | 9 |
| 2022-01-28 | 253.32 | 24.00 | 8 |
| 2022-02-25 | 236.31 | 78.83 | 5 |
| 2022-03-25 | 250.90 | 27.05 | 7 |
| 2022-04-29 | 250.70 | 19.96 | 7 |
| 2022-05-27 | 252.32 | 0.00 | 8 |
| 2022-06-24 | 238.12 | 35.73 | 7 |
| 2022-07-29 | 256.08 | 10.89 | 8 |
| 2022-08-26 | 267.87 | 10.89 | 8 |
| 2022-09-30 | 260.09 | 0.00 | 9 |
| 2022-10-28 | 272.69 | 0.00 | 9 |
| 2022-11-25 | 280.19 | 0.00 | 9 |
| 2022-12-30 | 278.01 | 0.00 | 10 |
| 2023-01-27 | 275.03 | 26.87 | 9 |
| 2023-02-24 | 285.42 | 0.00 | 10 |
| 2023-03-31 | 267.61 | 121.34 | 6 |
| 2023-04-28 | 274.02 | 55.15 | 8 |
| 2023-05-26 | 286.69 | 0.00 | 10 |
| 2023-06-30 | 302.54 | 0.00 | 10 |
| 2023-07-28 | 319.46 | 0.00 | 10 |
| 2023-08-25 | 346.36 | 0.00 | 10 |
| 2023-09-29 | 352.24 | 37.85 | 9 |
| 2023-10-27 | 350.18 | 92.49 | 7 |
| 2023-11-24 | 395.03 | 0.00 | 10 |
| 2023-12-29 | 410.42 | 0.00 | 10 |
| 2024-01-25 | 428.93 | 17.85 | 10 |
| 2024-02-23 | 451.90 | 0.86 | 10 |
| 2024-03-28 | 441.53 | 104.00 | 8 |
| 2024-04-26 | 453.77 | 0.00 | 10 |
| 2024-05-31 | 447.80 | 87.79 | 8 |
| 2024-06-28 | 461.84 | 0.00 | 10 |
| 2024-07-26 | 460.46 | 91.08 | 8 |
| 2024-08-30 | 455.51 | 0.23 | 10 |
| 2024-09-27 | 449.70 | 0.00 | 10 |
| 2024-10-25 | 410.93 | 172.61 | 6 |
| 2024-11-29 | 437.56 | 0.00 | 10 |
| 2024-12-27 | 416.56 | 122.49 | 7 |
| 2025-01-31 | 392.44 | 204.99 | 4 |
| 2025-02-28 | 357.03 | 209.97 | 4 |
| 2025-03-27 | 388.88 | 90.52 | 7 |
| 2025-04-25 | 396.85 | 108.23 | 6 |
| 2025-05-30 | 414.93 | 0.00 | 9 |
| 2025-06-27 | 440.07 | 0.00 | 9 |
| 2025-07-25 | 452.83 | 0.00 | 9 |
| 2025-08-29 | 458.10 | 46.28 | 8 |
| 2025-09-26 | 422.53 | 93.50 | 7 |
| 2025-10-31 | 402.98 | 67.08 | 9 |
| 2025-11-28 | 413.23 | 77.78 | 9 |
| 2025-12-26 | 409.84 | 36.36 | 10 |
| 2026-01-30 | 403.56 | 170.18 | 6 |
| 2026-02-27 | 386.24 | 52.17 | 9 |
| 2026-03-27 | 361.78 | 148.51 | 6 |
| 2026-04-30 | 401.57 | 0.00 | 10 |
| 2026-05-29 | 431.28 | 0.29 | 10 |
| 2026-06-25 | 432.84 | 0.00 | 10 |
| 2026-07-31 | 439.79 | 83.90 | 8 |
| 2026-08-28 | 463.67 | 0.00 | 10 |
| 2026-09-22 | 461.09 | 0.00 | 10 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| AVALON | 2026-09-21 | 2,550.00 | 2,468.50 | 2,032.34 | -3.2% |
| BLUESTONE | 2026-08-03 | 823.40 | 930.40 | 758.29 | +13.0% |
| CAPLIPOINT | 2026-05-18 | 1,990.00 | 2,777.30 | 2,376.52 | +39.6% |
| CHENNPETRO | 2026-04-06 | 989.00 | 1,392.00 | 1,242.60 | +40.7% |
| CRAFTSMAN | 2026-05-11 | 9,039.50 | 10,602.00 | 10,380.65 | +17.3% |
| JBCHEPHARM | 2026-03-16 | 2,136.00 | 2,408.90 | 1,976.86 | +12.8% |
| RUBICON | 2026-06-08 | 1,190.00 | 1,671.20 | 1,653.47 | +40.4% |
| STLTECH | 2026-04-13 | 224.31 | 405.15 | 250.86 | +80.6% |
| SUNDRMFAST | 2026-09-15 | 1,277.30 | 1,190.90 | 1,127.74 | -6.8% |
| TMB | 2026-08-03 | 864.90 | 883.75 | 817.00 | +2.2% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| DEEPAKNTR | 2020-04-13 | 474.55 | 2020-06-12 | 474.05 | -0.1% |
| IOLCP | 2020-05-11 | 66.18 | 2020-06-16 | 69.35 | +4.8% |
| HATHWAY | 2020-06-22 | 34.80 | 2020-06-29 | 31.40 | -9.8% |
| PANACEABIO | 2020-06-15 | 230.00 | 2020-08-20 | 184.01 | -20.0% |
| APCOTEXIND | 2020-08-24 | 164.95 | 2020-08-31 | 151.95 | -7.9% |
| APLLTD | 2020-05-11 | 774.70 | 2020-09-01 | 928.62 | +19.9% |
| CADILAHC | 2020-04-27 | 330.30 | 2020-09-08 | 364.99 | +10.5% |
| BALAJITELE | 2020-05-04 | 61.40 | 2020-09-09 | 74.07 | +20.6% |
| RCF | 2020-05-18 | 39.90 | 2020-09-09 | 45.84 | +14.9% |
| TAJGVK | 2020-04-27 | 133.40 | 2020-09-22 | 126.45 | -5.2% |
| SATIA | 2020-09-14 | 122.00 | 2020-09-22 | 102.97 | -15.6% |
| BHARATRAS | 2020-07-06 | 1,901.25 | 2020-10-09 | 2,210.00 | +16.2% |
| PRINCEPIPE | 2020-09-07 | 208.00 | 2020-10-12 | 220.88 | +6.2% |
| ALEMBICLTD | 2020-05-18 | 54.90 | 2020-11-02 | 91.41 | +66.5% |
| GLAXO | 2020-09-14 | 1,675.00 | 2020-11-02 | 1,441.55 | -13.9% |
| ADVENZYMES | 2020-05-18 | 159.95 | 2020-11-03 | 292.33 | +82.8% |
| THYROCARE | 2020-10-12 | 1,071.90 | 2020-11-12 | 1,016.50 | -5.2% |
| TATACHEM | 2020-11-09 | 318.00 | 2020-12-21 | 476.43 | +49.8% |
| SYNGENE | 2020-04-27 | 319.00 | 2020-12-22 | 562.40 | +76.3% |
| TCI | 2020-09-14 | 242.00 | 2020-12-22 | 234.75 | -3.0% |
| GODREJPROP | 2020-11-09 | 964.00 | 2021-01-18 | 1,306.25 | +35.5% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| KIRIINDUS | 2020-12-28 | 537.55 | 2021-01-21 | 478.56 | -11.0% |
| SAKSOFT | 2020-09-28 | 398.70 | 2021-01-25 | 341.10 | -14.4% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| TRENT | 2020-11-17 | 503.33 | 2021-01-29 | 417.53 | -17.0% |
| MTNL | 2020-12-28 | 14.10 | 2021-02-16 | 12.06 | -14.5% |
| TATAELXSI | 2021-01-25 | 2,608.00 | 2021-02-22 | 2,660.00 | +2.0% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| JINDWORLD | 2020-11-09 | 50.00 | 2021-03-01 | 52.12 | +4.2% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| TATAMOTORS | 2021-01-25 | 296.90 | 2021-03-19 | 296.97 | +0.0% |
| APTECHT | 2021-02-01 | 178.45 | 2021-03-19 | 204.25 | +14.5% |
| MAHINDCIE | 2021-02-22 | 188.00 | 2021-03-19 | 158.46 | -15.7% |
| BANARISUG | 2020-09-07 | 1,398.95 | 2021-03-25 | 1,586.36 | +13.4% |
| PAISALO | 2020-12-28 | 56.99 | 2021-04-12 | 72.41 | +27.1% |
| CENTRUM | 2021-03-30 | 28.40 | 2021-04-12 | 24.89 | -12.4% |
| GFLLIMITED | 2021-03-22 | 93.00 | 2021-04-13 | 74.39 | -20.0% |
| VIDHIING | 2021-03-22 | 194.70 | 2021-06-18 | 182.64 | -6.2% |
| MOREPENLAB | 2021-04-19 | 37.45 | 2021-08-10 | 56.33 | +50.4% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| GDL | 2021-01-25 | 158.00 | 2021-09-20 | 266.00 | +68.4% |
| KEI | 2021-03-22 | 522.00 | 2021-10-22 | 853.10 | +63.4% |
| BASF | 2021-08-16 | 3,679.70 | 2021-10-25 | 3,220.59 | -12.5% |
| NEOGEN | 2021-09-27 | 1,255.00 | 2021-10-25 | 1,142.85 | -8.9% |
| EMAMIPAP | 2021-04-19 | 125.00 | 2021-11-22 | 141.55 | +13.2% |
| SHOPERSTOP | 2021-10-25 | 326.00 | 2021-11-22 | 335.82 | +3.0% |
| TATAINVEST | 2021-08-16 | 1,308.05 | 2021-11-26 | 1,436.49 | +9.8% |
| TTKPRESTIG | 2021-11-01 | 11,040.00 | 2021-11-26 | 10,070.05 | -8.8% |
| SOMANYCERA | 2021-06-21 | 594.85 | 2021-11-29 | 755.11 | +26.9% |
| MAHLOG | 2021-01-25 | 495.85 | 2021-11-30 | 654.55 | +32.0% |
| RSYSTEMS | 2021-11-29 | 324.85 | 2021-12-16 | 291.18 | -10.4% |
| TCIEXP | 2021-11-01 | 1,831.25 | 2021-12-21 | 2,039.74 | +11.4% |
| LTTS | 2020-10-19 | 1,745.00 | 2022-01-21 | 4,856.88 | +178.3% |
| SWANENERGY | 2021-12-27 | 149.90 | 2022-01-25 | 162.64 | +8.5% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| BSOFT | 2021-11-29 | 465.20 | 2022-02-14 | 424.65 | -8.7% |
| RAYMOND | 2021-11-29 | 596.00 | 2022-02-15 | 679.35 | +14.0% |
| GREENLAM | 2021-12-20 | 363.58 | 2022-02-22 | 313.67 | -13.7% |
| LAXMIMACH | 2022-02-21 | 10,118.80 | 2022-02-22 | 10,169.75 | +0.5% |
| CHAMBLFERT | 2021-12-06 | 407.45 | 2022-02-24 | 353.85 | -13.2% |
| JSWISPL | 2022-01-24 | 37.50 | 2022-02-24 | 30.25 | -19.3% |
| BSE | 2021-12-06 | 1,889.95 | 2022-03-21 | 1,634.39 | -13.5% |
| RAJRATAN | 2021-03-22 | 763.95 | 2022-03-28 | 1,553.82 | +103.4% |
| GTLINFRA | 2022-03-07 | 1.70 | 2022-04-29 | 1.41 | -17.1% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
| INOXLEISUR | 2022-04-04 | 520.85 | 2022-05-06 | 470.35 | -9.7% |
| MFL | 2022-05-02 | 1,430.00 | 2022-05-11 | 1,225.50 | -14.3% |
| MOL | 2022-05-09 | 129.80 | 2022-05-11 | 113.62 | -12.5% |
| VBL | 2022-05-16 | 220.00 | 2022-06-06 | 196.27 | -10.8% |
| KRISHANA | 2022-05-16 | 67.96 | 2022-06-16 | 54.77 | -19.4% |
| JSWENERGY | 2021-03-08 | 81.85 | 2022-06-20 | 201.99 | +146.8% |
| DANGEE | 2022-02-28 | 235.00 | 2022-09-06 | 375.25 | +59.7% |
| RAJMET | 2022-05-09 | 411.30 | 2022-09-15 | 359.30 | -12.6% |
| APARINDS | 2022-06-20 | 950.15 | 2022-11-03 | 1,358.50 | +43.0% |
| ELECON | 2022-06-13 | 122.47 | 2022-12-21 | 202.49 | +65.3% |
| SHANTIGEAR | 2022-02-28 | 185.30 | 2022-12-22 | 345.56 | +86.5% |
| KTKBANK | 2022-11-07 | 140.00 | 2022-12-23 | 139.84 | -0.1% |
| 3MINDIA | 2022-07-11 | 22,701.00 | 2023-01-02 | 21,626.80 | -4.7% |
| CONCOR | 2022-09-12 | 753.00 | 2023-01-17 | 696.30 | -7.5% |
| KSL | 2022-12-26 | 330.10 | 2023-01-27 | 328.23 | -0.6% |
| GICRE | 2022-12-26 | 157.00 | 2023-02-01 | 167.72 | +6.8% |
| LSIL | 2023-01-23 | 22.40 | 2023-02-07 | 20.04 | -10.5% |
| CGCL | 2022-02-21 | 599.50 | 2023-02-17 | 704.95 | +17.6% |
| SUNFLAG | 2023-01-30 | 130.00 | 2023-02-27 | 129.20 | -0.6% |
| MAHINDCIE | 2023-02-06 | 395.20 | 2023-03-10 | 391.69 | -0.9% |
| KABRAEXTRU | 2022-12-26 | 441.95 | 2023-03-14 | 506.92 | +14.7% |
| KRISHANA | 2022-12-26 | 83.60 | 2023-03-20 | 94.40 | +12.9% |
| JINDALSAW | 2023-01-09 | 55.85 | 2023-03-27 | 67.92 | +21.6% |
| WONDERLA | 2023-03-06 | 456.00 | 2023-03-27 | 384.27 | -15.7% |
| MBAPL | 2022-02-14 | 52.00 | 2023-03-29 | 112.36 | +116.1% |
| CIGNITITEC | 2023-02-20 | 731.95 | 2023-03-29 | 705.14 | -3.7% |
| SHREECEM | 2022-09-12 | 24,599.00 | 2023-04-24 | 23,636.00 | -3.9% |
| KIRLOSBROS | 2023-04-03 | 414.00 | 2023-04-26 | 403.85 | -2.5% |
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
| JSWHL | 2022-09-19 | 4,700.00 | 2024-05-13 | 6,280.45 | +33.6% |
| FORCEMOT | 2024-03-18 | 6,567.70 | 2024-05-28 | 8,083.64 | +23.1% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| BOSCHLTD | 2024-03-18 | 29,500.05 | 2024-06-04 | 29,015.09 | -1.6% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| TDPOWERSYS | 2023-04-03 | 79.50 | 2024-07-19 | 188.72 | +137.4% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| ARE&M | 2024-06-10 | 1,450.00 | 2024-07-22 | 1,502.14 | +3.6% |
| FIEMIND | 2024-06-10 | 1,320.00 | 2024-07-23 | 1,257.56 | -4.7% |
| KIRLOSBROS | 2024-05-21 | 1,844.00 | 2024-08-05 | 1,987.46 | +7.8% |
| THERMAX | 2024-06-03 | 5,640.00 | 2024-08-05 | 4,719.70 | -16.3% |
| JWL | 2024-05-13 | 490.00 | 2024-08-06 | 552.00 | +12.7% |
| CAMPUS | 2024-06-03 | 286.00 | 2024-08-16 | 277.07 | -3.1% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| CERA | 2024-08-12 | 10,499.95 | 2024-09-19 | 8,198.93 | -21.9% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 785.00 | 2024-10-07 | 796.15 | +1.4% |
| PCBL | 2024-08-12 | 393.00 | 2024-10-18 | 476.85 | +21.3% |
| BASF | 2024-08-12 | 7,350.00 | 2024-10-22 | 7,611.30 | +3.6% |
| ALKYLAMINE | 2024-09-23 | 2,432.85 | 2024-10-22 | 2,106.24 | -13.4% |
| INDIAGLYCO | 2024-07-22 | 515.00 | 2024-10-25 | 587.91 | +14.2% |
| DBCORP | 2024-10-14 | 352.00 | 2024-10-25 | 302.08 | -14.2% |
| CUPID | 2023-10-30 | 120.99 | 2024-10-28 | 158.66 | +31.1% |
| ESABINDIA | 2024-07-22 | 6,486.15 | 2024-11-13 | 5,842.74 | -9.9% |
| ASTRAZEN | 2024-10-14 | 7,800.00 | 2024-11-14 | 6,854.77 | -12.1% |
| SUPRIYA | 2024-08-19 | 528.00 | 2024-12-17 | 717.25 | +35.8% |
| KIRLPNU | 2024-11-04 | 1,698.00 | 2024-12-23 | 1,596.00 | -6.0% |
| PRSMJOHNSN | 2024-09-16 | 214.51 | 2024-12-26 | 170.55 | -20.5% |
| AKZOINDIA | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-28 | 747.70 | 2025-01-09 | 893.05 | +19.4% |
| GARFIBRES | 2024-11-25 | 956.00 | 2025-01-09 | 829.35 | -13.2% |
| KSL | 2024-12-23 | 1,192.00 | 2025-01-09 | 1,059.30 | -11.1% |
| CARERATING | 2024-10-28 | 1,396.00 | 2025-01-13 | 1,239.70 | -11.2% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| MOTILALOFS | 2024-10-21 | 1,021.95 | 2025-01-17 | 788.79 | -22.8% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| LLOYDSME | 2025-01-06 | 1,439.00 | 2025-01-28 | 1,258.75 | -12.5% |
| JINDWORLD | 2024-12-30 | 407.65 | 2025-02-12 | 374.11 | -8.2% |
| GANESHHOUC | 2024-11-18 | 1,059.00 | 2025-02-28 | 1,090.38 | +3.0% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-03-03 | 727.84 | -23.1% |
| GRWRHITECH | 2025-03-10 | 4,219.95 | 2025-04-03 | 3,602.82 | -14.6% |
| AVANTIFEED | 2025-03-17 | 842.55 | 2025-04-07 | 648.95 | -23.0% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| JSWHL | 2024-11-11 | 15,500.00 | 2025-08-04 | 19,106.01 | +23.3% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| WHIRLPOOL | 2025-04-28 | 1,153.90 | 2025-08-07 | 1,301.97 | +12.8% |
| RAIN | 2025-08-11 | 160.25 | 2025-08-26 | 143.64 | -10.4% |
| GODFRYPHLP | 2025-02-24 | 5,780.00 | 2025-09-16 | 8,967.50 | +55.1% |
| RSYSTEMS | 2025-09-01 | 460.00 | 2025-09-24 | 423.23 | -8.0% |
| INDIASHLTR | 2025-04-15 | 865.00 | 2025-09-25 | 862.60 | -0.3% |
| KIMS | 2025-04-28 | 679.50 | 2025-10-03 | 680.34 | +0.1% |
| FORCEMOT | 2025-04-28 | 9,275.00 | 2025-10-09 | 15,350.10 | +65.5% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 850.00 | 2025-10-20 | 1,274.42 | +49.9% |
| BLACKBUCK | 2025-08-18 | 553.00 | 2025-10-28 | 642.20 | +16.1% |
| PGHL | 2025-08-11 | 6,345.00 | 2025-11-06 | 5,938.45 | -6.4% |
| FDC | 2025-09-22 | 489.55 | 2025-11-06 | 425.79 | -13.0% |
| ASTRAMICRO | 2025-10-06 | 1,119.85 | 2025-11-06 | 1,026.00 | -8.4% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| TDPOWERSYS | 2025-11-03 | 382.27 | 2025-11-24 | 357.49 | -6.5% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| RAMKY | 2025-10-13 | 622.35 | 2025-12-01 | 578.17 | -7.1% |
| SHAILY | 2025-10-13 | 2,434.00 | 2025-12-15 | 2,340.80 | -3.8% |
| HCG | 2025-10-27 | 758.60 | 2025-12-23 | 676.59 | -10.8% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.49 | -10.1% |
| KIRLOSENG | 2025-12-08 | 1,130.00 | 2026-01-12 | 1,140.95 | +1.0% |
| ASHAPURMIN | 2025-12-22 | 800.00 | 2026-01-16 | 817.00 | +2.1% |
| LGBBROSLTD | 2025-09-29 | 1,411.60 | 2026-01-20 | 1,713.80 | +21.4% |
| AVANTIFEED | 2025-04-15 | 818.00 | 2026-01-21 | 748.60 | -8.5% |
| LTF | 2025-11-10 | 304.00 | 2026-01-21 | 281.77 | -7.3% |
| SANSERA | 2025-12-01 | 1,749.60 | 2026-01-23 | 1,672.76 | -4.4% |
| NATIONALUM | 2026-01-12 | 352.00 | 2026-02-17 | 335.49 | -4.7% |
| SHRIRAMFIN | 2025-12-29 | 963.00 | 2026-03-04 | 992.37 | +3.0% |
| HAPPYFORGE | 2026-02-23 | 1,370.00 | 2026-03-04 | 1,234.05 | -9.9% |
| CUB | 2025-11-10 | 254.20 | 2026-03-09 | 251.43 | -1.1% |
| HINDCOPPER | 2026-01-12 | 532.00 | 2026-03-12 | 528.63 | -0.6% |
| RBA | 2026-01-19 | 67.50 | 2026-03-12 | 61.08 | -9.5% |
| VESUVIUS | 2026-02-23 | 535.10 | 2026-03-23 | 464.31 | -13.2% |
| J&KBANK | 2026-03-16 | 121.14 | 2026-03-23 | 110.67 | -8.6% |
| MAHABANK | 2025-11-03 | 59.70 | 2026-03-30 | 61.05 | +2.3% |
| KSB | 2026-03-02 | 738.00 | 2026-05-04 | 917.42 | +24.3% |
| INOXINDIA | 2026-04-13 | 1,299.10 | 2026-05-13 | 1,372.18 | +5.6% |
| AETHER | 2026-03-30 | 1,150.50 | 2026-05-14 | 1,125.84 | -2.1% |
| E2E | 2026-02-23 | 2,914.00 | 2026-06-05 | 2,330.72 | -20.0% |
| THERMAX | 2026-04-13 | 3,596.00 | 2026-07-29 | 4,306.64 | +19.8% |
| VTL | 2026-03-23 | 534.00 | 2026-07-31 | 592.80 | +11.0% |
| ALKYLAMINE | 2026-05-18 | 1,710.00 | 2026-09-10 | 1,920.99 | +12.3% |
| ABB | 2026-02-23 | 6,090.00 | 2026-09-15 | 7,158.25 | +17.5% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-04-01_to_2026-09-22_WATCH_AFTERFRESH_BUYONLY.csv` beside this report (17511 events in all).*

```
2020-04-13  DEEPAKNTR   BUY ₹10.00 at ₹474.55 (fresh Friday signal — ACCUMULATE: 1.76× weekly, month 2.47×, ladder rising; stop ₹240.25; charges ₹0.0118)
2020-04-27  CADILAHC    BUY ₹10.01 at ₹330.30 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 5.12×, ladder rising; stop ₹310.03; charges ₹0.0119)
2020-04-27  SYNGENE     BUY ₹10.02 at ₹319.00 (fresh Friday signal — ACCUMULATE: 2.32× weekly, month 1.94×, ladder rising; stop ₹285.95; charges ₹0.0119)
2020-04-27  TAJGVK      BUY ₹10.01 at ₹133.40 (fresh Friday signal — BUY: 6.65× weekly, month 2.23×, ladder rising; stop ₹106.49; charges ₹0.0119)
2020-05-04  BALAJITELE  BUY ₹9.94 at ₹61.40 (fresh Friday signal — BUY: surged 4.19× weekly on 2020-04-24 (month 2.47×), ladder rising NOW — promoted from the ladder watch; stop ₹48.55; charges ₹0.0118)
2020-05-11  APLLTD      BUY ₹9.93 at ₹774.70 (fresh Friday signal — ACCUMULATE: 1.70× weekly, month 6.10×, ladder rising; stop ₹694.45; charges ₹0.0118)
2020-05-11  IOLCP       BUY ₹9.93 at ₹66.18 (fresh Friday signal — BUY: 2.18× weekly, month 2.65×, ladder rising; stop ₹51.22; charges ₹0.0118)
2020-05-18  ADVENZYMES  BUY ₹10.25 at ₹159.95 (fresh Friday signal — ACCUMULATE: 3.12× weekly, month 2.00×, ladder rising; stop ₹126.20; charges ₹0.0121)
2020-05-18  ALEMBICLTD  BUY ₹10.23 at ₹54.90 (fresh Friday signal — ACCUMULATE: 2.50× weekly, month 2.01×, ladder rising; stop ₹44.84; charges ₹0.0121)
2020-05-18  RCF         BUY ₹9.68 at ₹39.90 (fresh Friday signal — ACCUMULATE: 2.16× weekly, month 2.55×, ladder rising; stop ₹35.25; charges ₹0.0115)
2020-06-12  DEEPAKNTR   SELL ₹9.97 at stop ₹474.05 (-0.1%, charges ₹0.0103) — the cash goes back to work at the next Friday screen
2020-06-15  PANACEABIO  BUY ₹9.97 at ₹230.00 (fresh Friday signal — BUY: 12.78× weekly, month 8.25×, ladder rising; stop ₹114.11; charges ₹0.0118)
2020-06-16  IOLCP       SELL ₹10.38 at stop ₹69.35 (+4.8%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2020-06-22  HATHWAY     BUY ₹10.38 at ₹34.80 (fresh Friday signal — BUY: 9.17× weekly, month 6.59×, ladder rising; stop ₹19.97; charges ₹0.0123)
2020-06-29  HATHWAY     SELL ₹9.35 at stop ₹31.40 (-9.8%, charges ₹0.0097) — the cash goes back to work at the next Friday screen
2020-07-06  BHARATRAS   BUY ₹9.35 at ₹1,901.25 (fresh Friday signal — BUY: 4.45× weekly, month 1.97×, ladder rising; stop ₹1,626.88; charges ₹0.0111)
2020-08-20  PANACEABIO  SELL ₹7.96 at stop ₹184.01 (-20.0%, charges ₹0.0083) — the cash goes back to work at the next Friday screen
2020-08-24  APCOTEXIND  BUY ₹7.96 at ₹164.95 (fresh Friday signal — BUY: 8.08× weekly, month 5.83×, ladder rising; stop ₹119.51; charges ₹0.0094)
2020-08-31  APCOTEXIND  SELL ₹7.31 at stop ₹151.95 (-7.9%, charges ₹0.0076) — the cash goes back to work at the next Friday screen
2020-09-01  APLLTD      SELL ₹11.87 at stop ₹928.62 (+19.9%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2020-09-07  BANARISUG   BUY ₹12.38 at ₹1,398.95 (fresh Friday signal — BUY: 5.36× weekly, month 3.91×, ladder rising; stop ₹1,211.25; charges ₹0.0147)
2020-09-07  PRINCEPIPE  BUY ₹6.81 at ₹208.00 (fresh Friday signal — BUY: 3.47× weekly, month 1.51×, ladder rising; stop ₹132.50; charges ₹0.0081)
2020-09-08  CADILAHC    SELL ₹11.04 at stop ₹364.99 (+10.5%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-09  BALAJITELE  SELL ₹11.96 at stop ₹74.07 (+20.6%, charges ₹0.0124) — the cash goes back to work at the next Friday screen
2020-09-09  RCF         SELL ₹11.09 at stop ₹45.84 (+14.9%, charges ₹0.0115) — the cash goes back to work at the next Friday screen
2020-09-14  GLAXO       BUY ₹8.57 at ₹1,675.00 (fresh Friday signal — BUY: 2.58× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.0102)
2020-09-14  SATIA       BUY ₹12.76 at ₹122.00 (fresh Friday signal — ACCUMULATE: 2.86× weekly, month 6.16×, ladder rising; stop ₹102.97; charges ₹0.0151)
2020-09-14  TCI         BUY ₹12.76 at ₹242.00 (fresh Friday signal — ACCUMULATE: 7.76× weekly, month 3.77×, ladder rising; stop ₹190.07; charges ₹0.0151)
2020-09-22  SATIA       SELL ₹10.75 at stop ₹102.97 (-15.6%, charges ₹0.0111) — the cash goes back to work at the next Friday screen
2020-09-22  TAJGVK      SELL ₹9.47 at stop ₹126.45 (-5.2%, charges ₹0.0098) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹7.33 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0087)
2020-09-28  SAKSOFT     BUY ₹12.88 at ₹398.70 (fresh Friday signal — ACCUMULATE: 8.71× weekly, month 12.36×, ladder rising; stop ₹303.81; charges ₹0.0153)
2020-10-09  BHARATRAS   SELL ₹10.84 at stop ₹2,210.00 (+16.2%, charges ₹0.0112) — the cash goes back to work at the next Friday screen
2020-10-12  PRINCEPIPE  SELL ₹7.21 at stop ₹220.88 (+6.2%, charges ₹0.0075) — the cash goes back to work at the next Friday screen
2020-10-12  THYROCARE   BUY ₹10.84 at ₹1,071.90 (fresh Friday signal — BUY: 8.93× weekly, month 4.49×, ladder rising; stop ₹705.09; charges ₹0.0128)
2020-10-19  LTTS        BUY ₹7.21 at ₹1,745.00 (fresh Friday signal — BUY: 4.76× weekly, month 2.59×, ladder rising; stop ₹1,482.95; charges ₹0.0085)
2020-11-02  ALEMBICLTD  SELL ₹17.00 at stop ₹91.41 (+66.5%, charges ₹0.0176) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹7.36 at stop ₹1,441.55 (-13.9%, charges ₹0.0076) — the cash goes back to work at the next Friday screen
2020-11-03  ADVENZYMES  SELL ₹18.70 at stop ₹292.33 (+82.8%, charges ₹0.0194) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹12.02 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 2.00×, ladder rising; stop ₹77.16; charges ₹0.0142)
2020-11-09  GODREJPROP  BUY ₹11.99 at ₹964.00 (fresh Friday signal — BUY: surged 4.07× weekly on 2020-10-23 (month 2.56×), ladder rising NOW — promoted from the ladder watch; stop ₹927.67; charges ₹0.0142)
2020-11-09  JINDWORLD   BUY ₹12.04 at ₹50.00 (fresh Friday signal — ACCUMULATE: 5.28× weekly, month 1.55×, ladder rising; stop ₹39.81; charges ₹0.0143)
2020-11-09  TATACHEM    BUY ₹7.01 at ₹318.00 (fresh Friday signal — BUY: surged 1.68× weekly on 2020-10-16 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹299.01; charges ₹0.0083)
2020-11-12  THYROCARE   SELL ₹10.26 at stop ₹1,016.50 (-5.2%, charges ₹0.0106) — the cash goes back to work at the next Friday screen
2020-11-17  TRENT       BUY ₹10.26 at ₹503.33 (fresh Friday signal — ACCUMULATE: 3.30× weekly, month 1.95×, ladder rising; stop ₹367.93; charges ₹0.0122)
2020-12-21  TATACHEM    SELL ₹10.49 at stop ₹476.43 (+49.8%, charges ₹0.0109) — the cash goes back to work at the next Friday screen
2020-12-22  SYNGENE     SELL ₹17.63 at stop ₹562.40 (+76.3%, charges ₹0.0183) — the cash goes back to work at the next Friday screen
2020-12-22  TCI         SELL ₹12.35 at stop ₹234.75 (-3.0%, charges ₹0.0128) — the cash goes back to work at the next Friday screen
2020-12-28  KIRIINDUS   BUY ₹9.30 at ₹537.55 (fresh Friday signal — BUY: 8.73× weekly, month 2.26×, ladder rising; stop ₹424.46; charges ₹0.0110)
2020-12-28  MTNL        BUY ₹15.65 at ₹14.10 (fresh Friday signal — BUY: 9.97× weekly, month 4.77×, ladder rising; stop ₹8.26; charges ₹0.0185)
2020-12-28  PAISALO     BUY ₹15.52 at ₹56.99 (fresh Friday signal — BUY: 32.27× weekly, month 7.43×, ladder rising; stop ₹33.56; charges ₹0.0184)
2021-01-18  GODREJPROP  SELL ₹16.21 at stop ₹1,306.25 (+35.5%, charges ₹0.0168) — the cash goes back to work at the next Friday screen
2021-01-20  BORORENEW   SELL ₹29.78 at stop ₹247.59 (+148.3%, charges ₹0.0309) — the cash goes back to work at the next Friday screen
2021-01-21  KIRIINDUS   SELL ₹8.26 at stop ₹478.56 (-11.0%, charges ₹0.0086) — the cash goes back to work at the next Friday screen
2021-01-25  GDL         BUY ₹15.26 at ₹158.00 (fresh Friday signal — BUY: 14.44× weekly, month 4.79×, ladder rising; stop ₹92.41; charges ₹0.0181)
2021-01-25  MAHLOG      BUY ₹15.42 at ₹495.85 (fresh Friday signal — BUY: 4.90× weekly, month 1.61×, ladder rising; stop ₹391.30; charges ₹0.0183)
2021-01-25  SAKSOFT     SELL ₹10.99 at stop ₹341.10 (-14.4%, charges ₹0.0114) — the cash goes back to work at the next Friday screen
2021-01-25  TATAELXSI   BUY ₹8.16 at ₹2,608.00 (fresh Friday signal — BUY: 2.95× weekly, month 2.73×, ladder rising; stop ₹1,712.61; charges ₹0.0097)
2021-01-25  TATAMOTORS  BUY ₹15.41 at ₹296.90 (fresh Friday signal — BUY: 3.10× weekly, month 2.05×, ladder rising; stop ₹171.38; charges ₹0.0183)
2021-01-29  HCLTECH     SELL ₹8.10 at stop ₹928.05 (+10.7%, charges ₹0.0084) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹8.49 at stop ₹417.53 (-17.0%, charges ₹0.0088) — the cash goes back to work at the next Friday screen
2021-02-01  APTECHT     BUY ₹15.24 at ₹178.45 (fresh Friday signal — BUY: 2.82× weekly, month 2.95×, ladder rising; stop ₹156.94; charges ₹0.0181)
2021-02-01  GAEL        BUY ₹12.35 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.71× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.0146)
2021-02-16  MTNL        SELL ₹13.36 at stop ₹12.06 (-14.5%, charges ₹0.0139) — the cash goes back to work at the next Friday screen
2021-02-22  MAHINDCIE   BUY ₹13.36 at ₹188.00 (fresh Friday signal — BUY: 22.74× weekly, month 4.25×, ladder rising; stop ₹143.79; charges ₹0.0158)
2021-02-22  TATAELXSI   SELL ₹8.31 at stop ₹2,660.00 (+2.0%, charges ₹0.0086) — the cash goes back to work at the next Friday screen
2021-02-23  GAEL        SELL ₹10.81 at stop ₹62.70 (-12.3%, charges ₹0.0112) — the cash goes back to work at the next Friday screen
2021-03-01  JINDWORLD   SELL ₹12.52 at stop ₹52.12 (+4.2%, charges ₹0.0130) — the cash goes back to work at the next Friday screen
2021-03-01  RCF         BUY ₹16.30 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.13×, ladder rising; stop ₹50.16; charges ₹0.0193)
2021-03-08  JSWENERGY   BUY ₹15.34 at ₹81.85 (fresh Friday signal — BUY: 5.17× weekly, month 2.50×, ladder rising; stop ₹65.79; charges ₹0.0182)
2021-03-17  RCF         SELL ₹16.09 at stop ₹79.16 (-1.1%, charges ₹0.0167) — the cash goes back to work at the next Friday screen
2021-03-19  APTECHT     SELL ₹17.40 at stop ₹204.25 (+14.5%, charges ₹0.0181) — the cash goes back to work at the next Friday screen
2021-03-19  MAHINDCIE   SELL ₹11.24 at stop ₹158.46 (-15.7%, charges ₹0.0117) — the cash goes back to work at the next Friday screen
2021-03-19  TATAMOTORS  SELL ₹15.38 at stop ₹296.97 (+0.0%, charges ₹0.0160) — the cash goes back to work at the next Friday screen
2021-03-22  GFLLIMITED  BUY ₹15.68 at ₹93.00 (fresh Friday signal — ACCUMULATE: 6.17× weekly, month 3.98×, ladder rising; stop ₹74.39; charges ₹0.0186)
2021-03-22  KEI         BUY ₹15.77 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0187)
2021-03-22  RAJRATAN    BUY ₹13.06 at ₹763.95 (fresh Friday signal — BUY: 4.06× weekly, month 2.74×, ladder rising; stop ₹590.19; charges ₹0.0155)
2021-03-22  VIDHIING    BUY ₹15.60 at ₹194.70 (fresh Friday signal — BUY: 7.01× weekly, month 2.56×, ladder rising; stop ₹125.41; charges ₹0.0185)
2021-03-25  BANARISUG   SELL ₹14.01 at stop ₹1,586.36 (+13.4%, charges ₹0.0145) — the cash goes back to work at the next Friday screen
2021-03-30  CENTRUM     BUY ₹14.01 at ₹28.40 (fresh Friday signal — ACCUMULATE: 1.82× weekly, month 6.70×, ladder rising; stop ₹24.89; charges ₹0.0166)
2021-04-01  CENTRUM     TRIM 5.4% (₹0.75 at ₹28.35) to pay the tax bill
2021-04-01  GDL         TRIM 5.4% (₹0.92 at ₹177.90) to pay the tax bill
2021-04-01  GFLLIMITED  TRIM 5.4% (₹0.98 at ₹108.35) to pay the tax bill
2021-04-01  JSWENERGY   TRIM 5.4% (₹0.91 at ₹90.70) to pay the tax bill
2021-04-01  KEI         TRIM 5.4% (₹0.86 at ₹528.60) to pay the tax bill
2021-04-01  LTTS        TRIM 5.4% (₹0.61 at ₹2,720.60) to pay the tax bill
2021-04-01  MAHLOG      TRIM 5.4% (₹0.96 at ₹574.75) to pay the tax bill
2021-04-01  PAISALO     TRIM 5.4% (₹1.14 at ₹78.11) to pay the tax bill
2021-04-01  RAJRATAN    TRIM 5.4% (₹0.71 at ₹771.90) to pay the tax bill
2021-04-01  TAX         FY2021 settled: ₹8.7489 paid (STCG ₹43.74 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-01  VIDHIING    TRIM 5.4% (₹0.89 at ₹207.10) to pay the tax bill
2021-04-12  CENTRUM     SELL ₹11.59 at stop ₹24.89 (-12.4%, charges ₹0.0120) — the cash goes back to work at the next Friday screen
2021-04-12  PAISALO     SELL ₹18.61 at stop ₹72.41 (+27.1%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2021-04-13  GFLLIMITED  SELL ₹11.84 at stop ₹74.39 (-20.0%, charges ₹0.0123) — the cash goes back to work at the next Friday screen
2021-04-19  EMAMIPAP    BUY ₹13.57 at ₹125.00 (fresh Friday signal — ACCUMULATE: 2.31× weekly, month 22.17×, ladder rising; stop ₹81.22; charges ₹0.0161)
2021-04-19  KPRMILL     BUY ₹14.23 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0169)
2021-04-19  MOREPENLAB  BUY ₹14.24 at ₹37.45 (fresh Friday signal — BUY: 2.45× weekly, month 2.08×, ladder rising; stop ₹28.01; charges ₹0.0169)
2021-06-18  VIDHIING    SELL ₹13.81 at stop ₹182.64 (-6.2%, charges ₹0.0143) — the cash goes back to work at the next Friday screen
2021-06-21  SOMANYCERA  BUY ₹13.81 at ₹594.85 (fresh Friday signal — BUY: 16.56× weekly, month 2.49×, ladder rising; stop ₹434.15; charges ₹0.0164)
2021-08-10  MOREPENLAB  SELL ₹21.37 at stop ₹56.33 (+50.4%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹21.20 at stop ₹352.48 (+49.4%, charges ₹0.0220) — the cash goes back to work at the next Friday screen
2021-08-16  BASF        BUY ₹23.36 at ₹3,679.70 (fresh Friday signal — BUY: 9.67× weekly, month 3.43×, ladder rising; stop ₹2,675.86; charges ₹0.0277)
2021-08-16  TATAINVEST  BUY ₹19.21 at ₹1,308.05 (fresh Friday signal — BUY: 8.45× weekly, month 4.81×, ladder rising; stop ₹1,031.13; charges ₹0.0228)
2021-09-20  GDL         SELL ₹24.25 at stop ₹266.00 (+68.4%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2021-09-27  NEOGEN      BUY ₹23.86 at ₹1,255.00 (fresh Friday signal — BUY: 4.66× weekly, month 4.51×, ladder rising; stop ₹1,035.55; charges ₹0.0283)
2021-10-22  KEI         SELL ₹24.33 at stop ₹853.10 (+63.4%, charges ₹0.0252) — the cash goes back to work at the next Friday screen
2021-10-25  BASF        SELL ₹20.40 at stop ₹3,220.59 (-12.5%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2021-10-25  NEOGEN      SELL ₹21.68 at stop ₹1,142.85 (-8.9%, charges ₹0.0225) — the cash goes back to work at the next Friday screen
2021-10-25  SHOPERSTOP  BUY ₹23.45 at ₹326.00 (fresh Friday signal — BUY: 4.86× weekly, month 2.38×, ladder rising; stop ₹254.41; charges ₹0.0278)
2021-11-01  TCIEXP      BUY ₹19.95 at ₹1,831.25 (fresh Friday signal — BUY: 6.84× weekly, month 1.90×, ladder rising; stop ₹1,384.20; charges ₹0.0236)
2021-11-01  TTKPRESTIG  BUY ₹23.40 at ₹11,040.00 (fresh Friday signal — BUY: 9.56× weekly, month 2.93×, ladder rising; stop ₹8,703.05; charges ₹0.0277)
2021-11-22  EMAMIPAP    SELL ₹15.33 at stop ₹141.55 (+13.2%, charges ₹0.0159) — the cash goes back to work at the next Friday screen
2021-11-22  SHOPERSTOP  SELL ₹24.10 at stop ₹335.82 (+3.0%, charges ₹0.0250) — the cash goes back to work at the next Friday screen
2021-11-26  TATAINVEST  SELL ₹21.05 at stop ₹1,436.49 (+9.8%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2021-11-26  TTKPRESTIG  SELL ₹21.30 at stop ₹10,070.05 (-8.8%, charges ₹0.0221) — the cash goes back to work at the next Friday screen
2021-11-29  BSOFT       BUY ₹23.66 at ₹465.20 (fresh Friday signal — BUY: 3.61× weekly, month 2.59×, ladder rising; stop ₹375.44; charges ₹0.0280)
2021-11-29  RAYMOND     BUY ₹23.42 at ₹596.00 (fresh Friday signal — BUY: 5.68× weekly, month 1.64×, ladder rising; stop ₹468.59; charges ₹0.0277)
2021-11-29  RSYSTEMS    BUY ₹23.55 at ₹324.85 (fresh Friday signal — BUY: 7.74× weekly, month 2.63×, ladder rising; stop ₹218.59; charges ₹0.0279)
2021-11-29  SOMANYCERA  SELL ₹17.50 at stop ₹755.11 (+26.9%, charges ₹0.0181) — the cash goes back to work at the next Friday screen
2021-11-30  MAHLOG      SELL ₹19.21 at stop ₹654.55 (+32.0%, charges ₹0.0199) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹23.39 at ₹1,889.95 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹1,429.61; charges ₹0.0277)
2021-12-06  CHAMBLFERT  BUY ₹23.33 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹0.0276)
2021-12-16  RSYSTEMS    SELL ₹21.06 at stop ₹291.18 (-10.4%, charges ₹0.0218) — the cash goes back to work at the next Friday screen
2021-12-20  GREENLAM    BUY ₹22.21 at ₹363.58 (fresh Friday signal — BUY: 14.43× weekly, month 5.78×, ladder rising; stop ₹274.66; charges ₹0.0263)
2021-12-21  TCIEXP      SELL ₹22.17 at stop ₹2,039.74 (+11.4%, charges ₹0.0230) — the cash goes back to work at the next Friday screen
2021-12-27  SWANENERGY  BUY ₹22.17 at ₹149.90 (fresh Friday signal — ACCUMULATE: 5.78× weekly, month 1.60×, ladder rising; stop ₹120.48; charges ₹0.0263)
2022-01-21  LTTS        SELL ₹18.95 at stop ₹4,856.88 (+178.3%, charges ₹0.0197) — the cash goes back to work at the next Friday screen
2022-01-24  JSWISPL     BUY ₹18.95 at ₹37.50 (fresh Friday signal — BUY: 5.58× weekly, month 4.04×, ladder rising; stop ₹27.79; charges ₹0.0224)
2022-01-25  SWANENERGY  SELL ₹24.00 at stop ₹162.64 (+8.5%, charges ₹0.0249) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹24.00 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0284)
2022-02-11  SHARDACROP  SELL ₹22.26 at stop ₹545.30 (-7.1%, charges ₹0.0231) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹21.55 at stop ₹424.65 (-8.7%, charges ₹0.0224) — the cash goes back to work at the next Friday screen
2022-02-14  MBAPL       BUY ₹22.26 at ₹52.00 (fresh Friday signal — BUY: 14.53× weekly, month 3.60×, ladder rising; stop ₹35.45; charges ₹0.0264)
2022-02-15  RAYMOND     SELL ₹26.63 at stop ₹679.35 (+14.0%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2022-02-21  CGCL        BUY ₹24.00 at ₹599.50 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹536.75; charges ₹0.0284)
2022-02-21  LAXMIMACH   BUY ₹23.96 at ₹10,118.80 (fresh Friday signal — BUY: surged 2.17× weekly on 2022-01-21 (month 1.69×), ladder rising NOW — promoted from the ladder watch; stop ₹10,169.75; charges ₹0.0284)
2022-02-22  GREENLAM    SELL ₹19.11 at stop ₹313.67 (-13.7%, charges ₹0.0198) — the cash goes back to work at the next Friday screen
2022-02-22  LAXMIMACH   SELL ₹24.02 at stop ₹10,169.75 (+0.5%, charges ₹0.0249) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹20.22 at stop ₹353.85 (-13.2%, charges ₹0.0210) — the cash goes back to work at the next Friday screen
2022-02-24  JSWISPL     SELL ₹15.25 at stop ₹30.25 (-19.3%, charges ₹0.0158) — the cash goes back to work at the next Friday screen
2022-02-28  DANGEE      BUY ₹23.87 at ₹235.00 (fresh Friday signal — BUY: 1.83× weekly, month 2.01×, ladder rising; stop ₹185.20; charges ₹0.0283)
2022-02-28  SHANTIGEAR  BUY ₹23.98 at ₹185.30 (fresh Friday signal — BUY: surged 3.40× weekly on 2022-02-11 (month 1.62×), ladder rising NOW — promoted from the ladder watch; stop ₹170.29; charges ₹0.0284)
2022-03-07  GTLINFRA    BUY ₹24.12 at ₹1.70 (fresh Friday signal — ACCUMULATE: 2.05× weekly, month 1.67×, ladder rising; stop ₹1.39; charges ₹0.0286)
2022-03-21  BSE         SELL ₹20.18 at stop ₹1,634.39 (-13.5%, charges ₹0.0209) — the cash goes back to work at the next Friday screen
2022-03-28  RAJRATAN    SELL ₹25.07 at stop ₹1,553.82 (+103.4%, charges ₹0.0260) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹8.5341 paid (STCG ₹27.10 @20%, LTCG ₹24.91 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  INOXLEISUR  BUY ₹21.12 at ₹520.85 (fresh Friday signal — ACCUMULATE: 7.27× weekly, month 3.35×, ladder rising; stop ₹470.35; charges ₹0.0250)
2022-04-04  RCF         BUY ₹22.46 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.0266)
2022-04-29  GTLINFRA    SELL ₹19.96 at stop ₹1.41 (-17.1%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2022-05-02  MFL         BUY ₹19.96 at ₹1,430.00 (fresh Friday signal — BUY: 14.27× weekly, month 3.71×, ladder rising; stop ₹932.71; charges ₹0.0236)
2022-05-04  RCF         SELL ₹21.65 at stop ₹93.15 (-3.4%, charges ₹0.0225) — the cash goes back to work at the next Friday screen
2022-05-06  INOXLEISUR  SELL ₹19.03 at stop ₹470.35 (-9.7%, charges ₹0.0197) — the cash goes back to work at the next Friday screen
2022-05-09  MOL         BUY ₹24.63 at ₹129.80 (fresh Friday signal — BUY: 6.75× weekly, month 2.56×, ladder rising; stop ₹113.62; charges ₹0.0292)
2022-05-09  RAJMET      BUY ₹16.06 at ₹411.30 (fresh Friday signal — BUY: 2.19× weekly, month 4.66×, ladder rising; stop ₹349.60; charges ₹0.0190)
2022-05-11  MFL         SELL ₹17.07 at stop ₹1,225.50 (-14.3%, charges ₹0.0177) — the cash goes back to work at the next Friday screen
2022-05-11  MOL         SELL ₹21.51 at stop ₹113.62 (-12.5%, charges ₹0.0223) — the cash goes back to work at the next Friday screen
2022-05-16  KRISHANA    BUY ₹14.61 at ₹67.96 (fresh Friday signal — ACCUMULATE: 1.67× weekly, month 1.86×, ladder rising; stop ₹54.77; charges ₹0.0173)
2022-05-16  VBL         BUY ₹23.96 at ₹220.00 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.88×, ladder rising; stop ₹196.27; charges ₹0.0284)
2022-06-06  VBL         SELL ₹21.33 at stop ₹196.27 (-10.8%, charges ₹0.0221) — the cash goes back to work at the next Friday screen
2022-06-13  ELECON      BUY ₹21.33 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0253)
2022-06-16  KRISHANA    SELL ₹11.75 at stop ₹54.77 (-19.4%, charges ₹0.0122) — the cash goes back to work at the next Friday screen
2022-06-20  APARINDS    BUY ₹11.75 at ₹950.15 (fresh Friday signal — BUY: 13.43× weekly, month 3.81×, ladder rising; stop ₹706.80; charges ₹0.0139)
2022-06-20  JSWENERGY   SELL ₹35.73 at stop ₹201.99 (+146.8%, charges ₹0.0371) — the cash goes back to work at the next Friday screen
2022-07-11  3MINDIA     BUY ₹24.83 at ₹22,701.00 (fresh Friday signal — BUY: surged 1.59× weekly on 2022-07-01 (month 2.11×), ladder rising NOW — promoted from the ladder watch; stop ₹20,069.75; charges ₹0.0294)
2022-09-06  DANGEE      SELL ₹38.03 at stop ₹375.25 (+59.7%, charges ₹0.0394) — the cash goes back to work at the next Friday screen
2022-09-12  CONCOR      BUY ₹22.26 at ₹753.00 (fresh Friday signal — BUY: 6.34× weekly, month 1.83×, ladder rising; stop ₹633.27; charges ₹0.0264)
2022-09-12  SHREECEM    BUY ₹26.66 at ₹24,599.00 (fresh Friday signal — BUY: 6.53× weekly, month 2.02×, ladder rising; stop ₹19,760.95; charges ₹0.0316)
2022-09-15  RAJMET      SELL ₹14.00 at stop ₹359.30 (-12.6%, charges ₹0.0145) — the cash goes back to work at the next Friday screen
2022-09-19  JSWHL       BUY ₹14.00 at ₹4,700.00 (fresh Friday signal — BUY: 55.28× weekly, month 2.87×, ladder rising; stop ₹3,335.69; charges ₹0.0166)
2022-11-03  APARINDS    SELL ₹16.76 at stop ₹1,358.50 (+43.0%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2022-11-07  KTKBANK     BUY ₹16.76 at ₹140.00 (fresh Friday signal — BUY: 12.94× weekly, month 4.92×, ladder rising; stop ₹71.72; charges ₹0.0199)
2022-12-21  ELECON      SELL ₹35.19 at stop ₹202.49 (+65.3%, charges ₹0.0365) — the cash goes back to work at the next Friday screen
2022-12-22  SHANTIGEAR  SELL ₹44.62 at stop ₹345.56 (+86.5%, charges ₹0.0463) — the cash goes back to work at the next Friday screen
2022-12-23  KTKBANK     SELL ₹16.70 at stop ₹139.84 (-0.1%, charges ₹0.0173) — the cash goes back to work at the next Friday screen
2022-12-26  GICRE       BUY ₹27.15 at ₹157.00 (fresh Friday signal — BUY: surged 4.73× weekly on 2022-12-02 (month 1.82×), ladder rising NOW — promoted from the ladder watch; stop ₹134.14; charges ₹0.0322)
2022-12-26  KABRAEXTRU  BUY ₹15.34 at ₹441.95 (fresh Friday signal — BUY: surged 4.67× weekly on 2022-11-25 (month 1.52×), ladder rising NOW — promoted from the ladder watch; stop ₹457.95; charges ₹0.0182)
2022-12-26  KRISHANA    BUY ₹26.95 at ₹83.60 (fresh Friday signal — BUY: 3.70× weekly, month 2.29×, ladder rising; stop ₹75.36; charges ₹0.0319)
2022-12-26  KSL         BUY ₹27.08 at ₹330.10 (fresh Friday signal — BUY: surged 5.50× weekly on 2022-12-09 (month 2.50×), ladder rising NOW — promoted from the ladder watch; stop ₹328.23; charges ₹0.0321)
2023-01-02  3MINDIA     SELL ₹23.61 at stop ₹21,626.80 (-4.7%, charges ₹0.0245) — the cash goes back to work at the next Friday screen
2023-01-09  JINDALSAW   BUY ₹23.61 at ₹55.85 (fresh Friday signal — BUY: 3.64× weekly, month 3.14×, ladder rising; stop ₹42.55; charges ₹0.0280)
2023-01-17  CONCOR      SELL ₹20.54 at stop ₹696.30 (-7.5%, charges ₹0.0213) — the cash goes back to work at the next Friday screen
2023-01-23  LSIL        BUY ₹20.54 at ₹22.40 (fresh Friday signal — BUY: 3.57× weekly, month 3.13×, ladder rising; stop ₹11.29; charges ₹0.0243)
2023-01-27  KSL         SELL ₹26.87 at stop ₹328.23 (-0.6%, charges ₹0.0279) — the cash goes back to work at the next Friday screen
2023-01-30  SUNFLAG     BUY ₹26.87 at ₹130.00 (fresh Friday signal — BUY: 2.23× weekly, month 3.12×, ladder rising; stop ₹105.97; charges ₹0.0318)
2023-02-01  GICRE       SELL ₹28.94 at stop ₹167.72 (+6.8%, charges ₹0.0300) — the cash goes back to work at the next Friday screen
2023-02-06  MAHINDCIE   BUY ₹27.54 at ₹395.20 (fresh Friday signal — BUY: 1.59× weekly, month 2.05×, ladder rising; stop ₹328.94; charges ₹0.0326)
2023-02-07  LSIL        SELL ₹18.34 at stop ₹20.04 (-10.5%, charges ₹0.0190) — the cash goes back to work at the next Friday screen
2023-02-17  CGCL        SELL ₹28.16 at stop ₹704.95 (+17.6%, charges ₹0.0292) — the cash goes back to work at the next Friday screen
2023-02-20  CIGNITITEC  BUY ₹19.56 at ₹731.95 (fresh Friday signal — BUY: 2.05× weekly, month 1.77×, ladder rising; stop ₹568.10; charges ₹0.0232)
2023-02-20  TIIL        BUY ₹28.32 at ₹1,116.70 (fresh Friday signal — BUY: 8.57× weekly, month 1.55×, ladder rising; stop ₹923.40; charges ₹0.0336)
2023-02-27  SUNFLAG     SELL ₹26.65 at stop ₹129.20 (-0.6%, charges ₹0.0276) — the cash goes back to work at the next Friday screen
2023-03-06  WONDERLA    BUY ₹26.65 at ₹456.00 (fresh Friday signal — BUY: 4.06× weekly, month 2.13×, ladder rising; stop ₹384.27; charges ₹0.0316)
2023-03-10  MAHINDCIE   SELL ₹27.24 at stop ₹391.69 (-0.9%, charges ₹0.0283) — the cash goes back to work at the next Friday screen
2023-03-13  KIRLOSIND   BUY ₹27.24 at ₹2,300.00 (fresh Friday signal — ACCUMULATE: 2.65× weekly, month 2.41×, ladder rising; stop ₹2,097.31; charges ₹0.0323)
2023-03-14  KABRAEXTRU  SELL ₹17.55 at stop ₹506.92 (+14.7%, charges ₹0.0182) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹17.55 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.57×, ladder rising; stop ₹691.46; charges ₹0.0208)
2023-03-20  KRISHANA    SELL ₹30.36 at stop ₹94.40 (+12.9%, charges ₹0.0315) — the cash goes back to work at the next Friday screen
2023-03-27  JINDALSAW   SELL ₹28.64 at stop ₹67.92 (+21.6%, charges ₹0.0297) — the cash goes back to work at the next Friday screen
2023-03-27  KSB         BUY ₹26.86 at ₹417.98 (fresh Friday signal — ACCUMULATE: 1.90× weekly, month 2.61×, ladder rising; stop ₹372.21; charges ₹0.0318)
2023-03-27  WONDERLA    SELL ₹22.40 at stop ₹384.27 (-15.7%, charges ₹0.0232) — the cash goes back to work at the next Friday screen
2023-03-29  CIGNITITEC  SELL ₹18.81 at stop ₹705.14 (-3.7%, charges ₹0.0195) — the cash goes back to work at the next Friday screen
2023-03-29  MBAPL       SELL ₹47.99 at stop ₹112.36 (+116.1%, charges ₹0.0498) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹25.76 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.06×, ladder rising; stop ₹1,171.71; charges ₹0.0305)
2023-04-03  INGERRAND   BUY ₹25.71 at ₹2,690.00 (fresh Friday signal — BUY: surged 2.77× weekly on 2023-03-10 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹2,170.84; charges ₹0.0305)
2023-04-03  KIRLOSBROS  BUY ₹25.67 at ₹414.00 (fresh Friday signal — BUY: surged 2.03× weekly on 2023-03-10 (month 3.71×), ladder rising NOW — promoted from the ladder watch; stop ₹357.44; charges ₹0.0304)
2023-04-03  TAX         FY2023 settled: ₹13.8916 paid (STCG ₹40.03 @20%, LTCG ₹47.08 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-03  TDPOWERSYS  BUY ₹25.70 at ₹79.50 (fresh Friday signal — BUY: surged 2.04× weekly on 2023-03-10 (month 1.65×), ladder rising NOW — promoted from the ladder watch; stop ₹64.12; charges ₹0.0304)
2023-04-24  SHREECEM    SELL ₹25.56 at stop ₹23,636.00 (-3.9%, charges ₹0.0265) — the cash goes back to work at the next Friday screen
2023-04-26  KIRLOSBROS  SELL ₹24.99 at stop ₹403.85 (-2.5%, charges ₹0.0259) — the cash goes back to work at the next Friday screen
2023-05-02  FAIRCHEMOR  BUY ₹27.21 at ₹1,272.00 (fresh Friday signal — BUY: 3.67× weekly, month 1.62×, ladder rising; stop ₹1,054.59; charges ₹0.0322)
2023-05-02  GLS         BUY ₹27.16 at ₹509.05 (fresh Friday signal — BUY: 4.14× weekly, month 2.64×, ladder rising; stop ₹351.50; charges ₹0.0322)
2023-05-19  FAIRCHEMOR  SELL ₹24.35 at stop ₹1,141.04 (-10.3%, charges ₹0.0253) — the cash goes back to work at the next Friday screen
2023-05-22  SHARDAMOTR  BUY ₹25.13 at ₹380.00 (fresh Friday signal — BUY: 9.54× weekly, month 2.31×, ladder rising; stop ₹342.95; charges ₹0.0298)
2023-07-03  ANURAS      SELL ₹23.35 at stop ₹1,007.67 (+33.3%, charges ₹0.0242) — the cash goes back to work at the next Friday screen
2023-07-10  GENUSPOWER  BUY ₹23.35 at ₹162.85 (fresh Friday signal — BUY: 13.37× weekly, month 8.48×, ladder rising; stop ₹99.51; charges ₹0.0277)
2023-07-12  KSB         SELL ₹26.15 at stop ₹407.74 (-2.4%, charges ₹0.0271) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹26.15 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0310)
2023-09-13  INGERRAND   SELL ₹28.83 at stop ₹3,022.99 (+12.4%, charges ₹0.0299) — the cash goes back to work at the next Friday screen
2023-09-18  SJVN        BUY ₹28.83 at ₹75.35 (fresh Friday signal — BUY: 5.02× weekly, month 4.67×, ladder rising; stop ₹58.28; charges ₹0.0342)
2023-09-25  KIRLOSIND   SELL ₹37.85 at stop ₹3,202.97 (+39.3%, charges ₹0.0393) — the cash goes back to work at the next Friday screen
2023-10-03  PILANIINVS  BUY ₹35.53 at ₹2,380.05 (fresh Friday signal — BUY: 3.07× weekly, month 7.66×, ladder rising; stop ₹2,018.75; charges ₹0.0421)
2023-10-23  SJVN        SELL ₹25.21 at stop ₹66.03 (-12.4%, charges ₹0.0261) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹34.28 at stop ₹1,840.70 (+33.4%, charges ₹0.0356) — the cash goes back to work at the next Friday screen
2023-10-25  SHARDAMOTR  SELL ₹30.68 at stop ₹465.07 (+22.4%, charges ₹0.0318) — the cash goes back to work at the next Friday screen
2023-10-30  CUPID       BUY ₹22.63 at ₹120.99 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹73.16; charges ₹0.0268)
2023-10-30  KKCL        BUY ₹34.95 at ₹761.80 (fresh Friday signal — ACCUMULATE: 9.21× weekly, month 1.91×, ladder rising; stop ₹674.12; charges ₹0.0414)
2023-10-30  SHAREINDIA  BUY ₹34.92 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0414)
2023-11-16  GENUSPOWER  SELL ₹33.48 at stop ₹234.03 (+43.7%, charges ₹0.0347) — the cash goes back to work at the next Friday screen
2023-11-20  ISMTLTD     BUY ₹33.48 at ₹94.60 (fresh Friday signal — BUY: 5.37× weekly, month 1.93×, ladder rising; stop ₹80.18; charges ₹0.0397)
2023-12-20  ISMTLTD     SELL ₹31.20 at stop ₹88.35 (-6.6%, charges ₹0.0324) — the cash goes back to work at the next Friday screen
2023-12-26  MMFL        BUY ₹31.20 at ₹1,023.60 (fresh Friday signal — BUY: 9.43× weekly, month 3.43×, ladder rising; stop ₹821.80; charges ₹0.0370)
2024-01-17  TIIL        SELL ₹59.15 at stop ₹2,337.00 (+109.3%, charges ₹0.0614) — the cash goes back to work at the next Friday screen
2024-01-23  GANESHHOUC  BUY ₹41.29 at ₹663.40 (fresh Friday signal — BUY: 26.04× weekly, month 5.30×, ladder rising; stop ₹354.40; charges ₹0.0489)
2024-01-30  MMFL        SELL ₹27.74 at stop ₹912.05 (-10.9%, charges ₹0.0288) — the cash goes back to work at the next Friday screen
2024-02-05  TCI         BUY ₹44.73 at ₹987.60 (fresh Friday signal — BUY: 18.34× weekly, month 4.04×, ladder rising; stop ₹790.40; charges ₹0.0530)
2024-03-05  GLS         SELL ₹41.50 at stop ₹779.48 (+53.1%, charges ₹0.0430) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹41.48 at stop ₹357.20 (+19.1%, charges ₹0.0430) — the cash goes back to work at the next Friday screen
2024-03-11  DOLLAR      BUY ₹45.33 at ₹527.95 (fresh Friday signal — BUY: 4.55× weekly, month 2.48×, ladder rising; stop ₹461.65; charges ₹0.0537)
2024-03-11  SOLARINDS   BUY ₹38.52 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0456)
2024-03-11  TCI         SELL ₹35.72 at stop ₹790.40 (-20.0%, charges ₹0.0371) — the cash goes back to work at the next Friday screen
2024-03-13  DOLLAR      SELL ₹39.55 at stop ₹461.65 (-12.6%, charges ₹0.0410) — the cash goes back to work at the next Friday screen
2024-03-13  KKCL        SELL ₹30.86 at stop ₹674.12 (-11.5%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2024-03-14  GANESHHOUC  SELL ₹41.39 at stop ₹666.47 (+0.5%, charges ₹0.0429) — the cash goes back to work at the next Friday screen
2024-03-18  BOSCHLTD    BUY ₹42.89 at ₹29,500.05 (fresh Friday signal — BUY: 1.54× weekly, month 1.81×, ladder rising; stop ₹26,525.90; charges ₹0.0508)
2024-03-18  FORCEMOT    BUY ₹42.69 at ₹6,567.70 (fresh Friday signal — ACCUMULATE: 1.91× weekly, month 1.52×, ladder rising; stop ₹5,500.61; charges ₹0.0506)
2024-03-18  INDIGO      BUY ₹42.63 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0505)
2024-03-27  ANANDRATHI  SELL ₹84.71 at stop ₹862.65 (+224.7%, charges ₹0.0879) — the cash goes back to work at the next Friday screen
2024-04-01  DMART       BUY ₹37.46 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; stop ₹3,695.50; charges ₹0.0444)
2024-04-01  SHRIRAMFIN  BUY ₹42.13 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.94× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0499)
2024-04-01  TAX         FY2024 settled: ₹24.4060 paid (STCG ₹122.03 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-05-09  PILANIINVS  SELL ₹55.27 at stop ₹3,710.37 (+55.9%, charges ₹0.0573) — the cash goes back to work at the next Friday screen
2024-05-13  JSWHL       SELL ₹18.66 at stop ₹6,280.45 (+33.6%, charges ₹0.0194) — the cash goes back to work at the next Friday screen
2024-05-13  JWL         BUY ₹43.66 at ₹490.00 (fresh Friday signal — BUY: 7.12× weekly, month 2.51×, ladder rising; stop ₹370.93; charges ₹0.0517)
2024-05-21  KIRLOSBROS  BUY ₹30.27 at ₹1,844.00 (fresh Friday signal — BUY: 5.41× weekly, month 1.62×, ladder rising; stop ₹1,221.51; charges ₹0.0359)
2024-05-28  FORCEMOT    SELL ₹52.43 at stop ₹8,083.64 (+23.1%, charges ₹0.0544) — the cash goes back to work at the next Friday screen
2024-05-31  DMART       SELL ₹35.36 at stop ₹4,322.83 (-5.4%, charges ₹0.0367) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹45.99 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0545)
2024-06-03  THERMAX     BUY ₹41.80 at ₹5,640.00 (fresh Friday signal — BUY: 8.15× weekly, month 5.82×, ladder rising; stop ₹4,642.65; charges ₹0.0495)
2024-06-04  BOSCHLTD    SELL ₹42.09 at stop ₹29,015.09 (-1.6%, charges ₹0.0437) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹39.16 at stop ₹441.77 (-6.8%, charges ₹0.0406) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹40.55 at stop ₹7,980.95 (+5.5%, charges ₹0.0421) — the cash goes back to work at the next Friday screen
2024-06-10  ARE&M       BUY ₹33.76 at ₹1,450.00 (fresh Friday signal — BUY: 3.00× weekly, month 2.35×, ladder rising; stop ₹916.60; charges ₹0.0400)
2024-06-10  FIEMIND     BUY ₹44.09 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0522)
2024-06-10  UNOMINDA    BUY ₹43.95 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.60×, ladder rising; stop ₹769.64; charges ₹0.0521)
2024-07-19  TDPOWERSYS  SELL ₹60.87 at stop ₹188.72 (+137.4%, charges ₹0.0631) — the cash goes back to work at the next Friday screen
2024-07-19  UNOMINDA    SELL ₹44.39 at stop ₹981.87 (+1.2%, charges ₹0.0460) — the cash goes back to work at the next Friday screen
2024-07-22  ARE&M       SELL ₹34.90 at stop ₹1,502.14 (+3.6%, charges ₹0.0362) — the cash goes back to work at the next Friday screen
2024-07-22  ESABINDIA   BUY ₹45.52 at ₹6,486.15 (fresh Friday signal — BUY: 2.98× weekly, month 1.72×, ladder rising; stop ₹5,682.38; charges ₹0.0539)
2024-07-22  INDIAGLYCO  BUY ₹45.47 at ₹515.00 (fresh Friday signal — BUY: 3.46× weekly, month 2.25×, ladder rising; stop ₹429.42; charges ₹0.0539)
2024-07-23  FIEMIND     SELL ₹41.91 at stop ₹1,257.56 (-4.7%, charges ₹0.0435) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹44.72 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0530)
2024-07-29  THYROCARE   BUY ₹46.36 at ₹785.00 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹589.00; charges ₹0.0549)
2024-08-05  KIRLOSBROS  SELL ₹32.55 at stop ₹1,987.46 (+7.8%, charges ₹0.0338) — the cash goes back to work at the next Friday screen
2024-08-05  THERMAX     SELL ₹34.90 at stop ₹4,719.70 (-16.3%, charges ₹0.0362) — the cash goes back to work at the next Friday screen
2024-08-06  JWL         SELL ₹49.08 at stop ₹552.00 (+12.7%, charges ₹0.0509) — the cash goes back to work at the next Friday screen
2024-08-12  BASF        BUY ₹45.07 at ₹7,350.00 (fresh Friday signal — BUY: 5.89× weekly, month 3.35×, ladder rising; stop ₹5,386.50; charges ₹0.0534)
2024-08-12  CERA        BUY ₹45.00 at ₹10,499.95 (fresh Friday signal — BUY: 4.91× weekly, month 2.08×, ladder rising; stop ₹8,198.93; charges ₹0.0533)
2024-08-12  PCBL        BUY ₹26.46 at ₹393.00 (fresh Friday signal — BUY: 4.82× weekly, month 4.03×, ladder rising; stop ₹246.00; charges ₹0.0314)
2024-08-16  CAMPUS      SELL ₹44.46 at stop ₹277.07 (-3.1%, charges ₹0.0461) — the cash goes back to work at the next Friday screen
2024-08-19  SUPRIYA     BUY ₹44.22 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.14×, ladder rising; stop ₹361.00; charges ₹0.0524)
2024-09-09  AVANTIFEED  SELL ₹41.58 at stop ₹650.13 (-6.8%, charges ₹0.0431) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹41.82 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0495)
2024-09-19  CERA        SELL ₹35.06 at stop ₹8,198.93 (-21.9%, charges ₹0.0364) — the cash goes back to work at the next Friday screen
2024-09-23  ALKYLAMINE  BUY ₹35.06 at ₹2,432.85 (fresh Friday signal — BUY: 9.32× weekly, month 3.52×, ladder rising; stop ₹2,106.24; charges ₹0.0415)
2024-10-07  INDIGO      SELL ₹59.62 at stop ₹4,485.14 (+40.2%, charges ₹0.0618) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹46.91 at stop ₹796.15 (+1.4%, charges ₹0.0487) — the cash goes back to work at the next Friday screen
2024-10-14  ASTRAZEN    BUY ₹45.07 at ₹7,800.00 (fresh Friday signal — ACCUMULATE: 3.65× weekly, month 8.83×, ladder rising; stop ₹6,768.80; charges ₹0.0534)
2024-10-14  DBCORP      BUY ₹45.25 at ₹352.00 (fresh Friday signal — ACCUMULATE: 7.16× weekly, month 1.71×, ladder rising; stop ₹302.08; charges ₹0.0536)
2024-10-18  PCBL        SELL ₹32.04 at stop ₹476.85 (+21.3%, charges ₹0.0332) — the cash goes back to work at the next Friday screen
2024-10-21  MOTILALOFS  BUY ₹43.03 at ₹1,021.95 (fresh Friday signal — BUY: 7.74× weekly, month 5.64×, ladder rising; stop ₹656.59; charges ₹0.0510)
2024-10-22  ALKYLAMINE  SELL ₹30.29 at stop ₹2,106.24 (-13.4%, charges ₹0.0314) — the cash goes back to work at the next Friday screen
2024-10-22  BASF        SELL ₹46.57 at stop ₹7,611.30 (+3.6%, charges ₹0.0483) — the cash goes back to work at the next Friday screen
2024-10-25  DBCORP      SELL ₹38.75 at stop ₹302.08 (-14.2%, charges ₹0.0402) — the cash goes back to work at the next Friday screen
2024-10-25  INDIAGLYCO  SELL ₹51.79 at stop ₹587.91 (+14.2%, charges ₹0.0537) — the cash goes back to work at the next Friday screen
2024-10-28  CARERATING  BUY ₹37.99 at ₹1,396.00 (fresh Friday signal — BUY: surged 3.30× weekly on 2024-10-11 (month 1.54×), ladder rising NOW — promoted from the ladder watch; stop ₹1,066.23; charges ₹0.0450)
2024-10-28  CUPID       SELL ₹29.61 at stop ₹158.66 (+31.1%, charges ₹0.0307) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹38.07 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.44×, ladder rising; stop ₹636.31; charges ₹0.0451)
2024-11-04  AKZOINDIA   BUY ₹42.17 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.0996)
2024-11-04  KIRLPNU     BUY ₹41.95 at ₹1,698.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.98×, ladder rising; stop ₹1,188.50; charges ₹0.0990)
2024-11-11  JSWHL       BUY ₹41.32 at ₹15,500.00 (fresh Friday signal — BUY: 8.83× weekly, month 3.54×, ladder rising; stop ₹8,434.53; charges ₹0.0975)
2024-11-13  ESABINDIA   SELL ₹40.86 at stop ₹5,842.74 (-9.9%, charges ₹0.0908) — the cash goes back to work at the next Friday screen
2024-11-14  ASTRAZEN    SELL ₹39.48 at stop ₹6,854.77 (-12.1%, charges ₹0.0877) — the cash goes back to work at the next Friday screen
2024-11-18  GANESHHOUC  BUY ₹40.65 at ₹1,059.00 (fresh Friday signal — BUY: surged 4.01× weekly on 2024-10-18 (month 1.75×), ladder rising NOW — promoted from the ladder watch; stop ₹867.10; charges ₹0.0960)
2024-11-25  GARFIBRES   BUY ₹40.41 at ₹956.00 (fresh Friday signal — BUY: 4.62× weekly, month 2.20×, ladder rising; stop ₹704.32; charges ₹0.0954)
2024-12-17  SUPRIYA     SELL ₹59.87 at stop ₹717.25 (+35.8%, charges ₹0.1330) — the cash goes back to work at the next Friday screen
2024-12-23  KIRLPNU     SELL ₹39.25 at stop ₹1,596.00 (-6.0%, charges ₹0.0872) — the cash goes back to work at the next Friday screen
2024-12-23  KSL         BUY ₹41.57 at ₹1,192.00 (fresh Friday signal — BUY: 10.78× weekly, month 1.64×, ladder rising; stop ₹858.80; charges ₹0.0981)
2024-12-26  PRSMJOHNSN  SELL ₹33.13 at stop ₹170.55 (-20.5%, charges ₹0.0736) — the cash goes back to work at the next Friday screen
2024-12-27  AKZOINDIA   SELL ₹31.81 at stop ₹3,423.18 (-24.2%, charges ₹0.0707) — the cash goes back to work at the next Friday screen
2024-12-30  JINDWORLD   BUY ₹42.12 at ₹407.65 (fresh Friday signal — ACCUMULATE: 2.82× weekly, month 2.63×, ladder rising; stop ₹362.90; charges ₹0.0994)
2024-12-30  KFINTECH    BUY ₹41.98 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.21×, ladder rising; stop ₹1,159.14; charges ₹0.0991)
2025-01-06  LLOYDSME    BUY ₹38.39 at ₹1,439.00 (fresh Friday signal — BUY: 2.97× weekly, month 1.94×, ladder rising; stop ₹1,064.09; charges ₹0.0906)
2025-01-09  GARFIBRES   SELL ₹34.89 at stop ₹829.35 (-13.2%, charges ₹0.0775) — the cash goes back to work at the next Friday screen
2025-01-09  KSL         SELL ₹36.77 at stop ₹1,059.30 (-11.1%, charges ₹0.0817) — the cash goes back to work at the next Friday screen
2025-01-09  PAYTM       SELL ₹45.31 at stop ₹893.05 (+19.4%, charges ₹0.1006) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹38.65 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 9.77×, ladder rising; stop ₹697.76; charges ₹0.0912)
2025-01-13  CARERATING  SELL ₹33.62 at stop ₹1,239.70 (-11.2%, charges ₹0.0747) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹32.05 at stop ₹1,159.14 (-23.3%, charges ₹0.0712) — the cash goes back to work at the next Friday screen
2025-01-17  MOTILALOFS  SELL ₹33.10 at stop ₹788.79 (-22.8%, charges ₹0.0735) — the cash goes back to work at the next Friday screen
2025-01-24  AEGISLOG    SELL ₹32.28 at stop ₹700.36 (-16.1%, charges ₹0.0717) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹37.82 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0893)
2025-01-28  LLOYDSME    SELL ₹33.43 at stop ₹1,258.75 (-12.5%, charges ₹0.0742) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹38.91 at ₹947.00 (fresh Friday signal — BUY: surged 9.53× weekly on 2025-01-24 (month 2.32×), ladder rising NOW — promoted from the ladder watch; stop ₹727.84; charges ₹0.0919)
2025-02-12  JINDWORLD   SELL ₹38.48 at stop ₹374.11 (-8.2%, charges ₹0.0855) — the cash goes back to work at the next Friday screen
2025-02-24  GODFRYPHLP  BUY ₹36.27 at ₹5,780.00 (fresh Friday signal — BUY: surged 12.02× weekly on 2025-02-14 (month 2.67×), ladder rising NOW — promoted from the ladder watch; stop ₹4,579.56; charges ₹0.0856)
2025-02-28  GANESHHOUC  SELL ₹41.67 at stop ₹1,090.38 (+3.0%, charges ₹0.0925) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹35.51 at ₹1,450.00 (fresh Friday signal — BUY: 4.73× weekly, month 1.68×, ladder rising; stop ₹1,235.90; charges ₹0.0838)
2025-03-03  ZENSARTECH  SELL ₹29.77 at stop ₹727.84 (-23.1%, charges ₹0.0661) — the cash goes back to work at the next Friday screen
2025-03-10  GRWRHITECH  BUY ₹36.92 at ₹4,219.95 (fresh Friday signal — BUY: surged 2.69× weekly on 2025-02-14 (month 1.89×), ladder rising NOW — promoted from the ladder watch; stop ₹3,504.00; charges ₹0.0872)
2025-03-17  AVANTIFEED  BUY ₹37.28 at ₹842.55 (fresh Friday signal — BUY: 1.75× weekly, month 1.50×, ladder rising; stop ₹648.95; charges ₹0.0880)
2025-03-24  INDIASHLTR  BUY ₹39.52 at ₹794.95 (fresh Friday signal — BUY: 5.78× weekly, month 1.76×, ladder rising; stop ₹692.55; charges ₹0.0933)
2025-04-01  TAX         FY2025 settled: ₹1.9858 paid (STCG ₹0.00 @20%, LTCG ₹15.89 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2025-04-03  GRWRHITECH  SELL ₹31.38 at stop ₹3,602.82 (-14.6%, charges ₹0.0697) — the cash goes back to work at the next Friday screen
2025-04-07  AVANTIFEED  SELL ₹28.58 at stop ₹648.95 (-23.0%, charges ₹0.0635) — the cash goes back to work at the next Friday screen
2025-04-07  INDIASHLTR  SELL ₹36.56 at stop ₹738.82 (-7.1%, charges ₹0.0812) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹38.34 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 2.02×, ladder rising; stop ₹492.75; charges ₹0.0905)
2025-04-15  INDIASHLTR  BUY ₹38.48 at ₹865.00 (fresh Friday signal — BUY: 1.60× weekly, month 2.25×, ladder rising; stop ₹738.82; charges ₹0.0908)
2025-04-28  FORCEMOT    BUY ₹39.66 at ₹9,275.00 (fresh Friday signal — ACCUMULATE: 2.06× weekly, month 1.62×, ladder rising; stop ₹7,647.50; charges ₹0.0936)
2025-04-28  KIMS        BUY ₹29.06 at ₹679.50 (fresh Friday signal — BUY: surged 1.50× weekly on 2025-03-27 (month 1.81×), ladder rising NOW — promoted from the ladder watch; stop ₹486.11; charges ₹0.0686)
2025-04-28  WHIRLPOOL   BUY ₹39.51 at ₹1,153.90 (fresh Friday signal — BUY: 2.21× weekly, month 1.77×, ladder rising; stop ₹1,017.54; charges ₹0.0933)
2025-08-04  JSWHL       SELL ₹50.70 at stop ₹19,106.01 (+23.3%, charges ₹0.1126) — the cash goes back to work at the next Friday screen
2025-08-04  NH          SELL ₹44.23 at stop ₹1,814.78 (+25.2%, charges ₹0.0983) — the cash goes back to work at the next Friday screen
2025-08-07  WHIRLPOOL   SELL ₹44.38 at stop ₹1,301.97 (+12.8%, charges ₹0.0986) — the cash goes back to work at the next Friday screen
2025-08-11  PGHL        BUY ₹43.68 at ₹6,345.00 (fresh Friday signal — BUY: 1.64× weekly, month 2.94×, ladder rising; stop ₹5,320.00; charges ₹0.1031)
2025-08-11  RAIN        BUY ₹43.75 at ₹160.25 (fresh Friday signal — BUY: 9.58× weekly, month 1.81×, ladder rising; stop ₹143.64; charges ₹0.1033)
2025-08-18  BLACKBUCK   BUY ₹44.63 at ₹553.00 (fresh Friday signal — ACCUMULATE: 3.19× weekly, month 4.96×, ladder rising; stop ₹473.20; charges ₹0.1054)
2025-08-26  RAIN        SELL ₹39.04 at stop ₹143.64 (-10.4%, charges ₹0.0867) — the cash goes back to work at the next Friday screen
2025-09-01  RSYSTEMS    BUY ₹45.13 at ₹460.00 (fresh Friday signal — BUY: surged 17.81× weekly on 2025-08-22 (month 4.67×), ladder rising NOW — promoted from the ladder watch; stop ₹394.44; charges ₹0.1065)
2025-09-16  GODFRYPHLP  SELL ₹56.01 at stop ₹8,967.50 (+55.1%, charges ₹0.1244) — the cash goes back to work at the next Friday screen
2025-09-22  FDC         BUY ₹43.20 at ₹489.55 (fresh Friday signal — ACCUMULATE: 9.75× weekly, month 1.96×, ladder rising; stop ₹425.79; charges ₹0.1020)
2025-09-24  RSYSTEMS    SELL ₹41.33 at stop ₹423.23 (-8.0%, charges ₹0.0918) — the cash goes back to work at the next Friday screen
2025-09-25  INDIASHLTR  SELL ₹38.20 at stop ₹862.60 (-0.3%, charges ₹0.0849) — the cash goes back to work at the next Friday screen
2025-09-29  LGBBROSLTD  BUY ₹42.06 at ₹1,411.60 (fresh Friday signal — BUY: 3.53× weekly, month 1.72×, ladder rising; stop ₹1,258.75; charges ₹0.0993)
2025-09-29  SUBROS      BUY ₹41.84 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.0988)
2025-10-03  KIMS        SELL ₹28.96 at stop ₹680.34 (+0.1%, charges ₹0.0643) — the cash goes back to work at the next Friday screen
2025-10-06  ASTRAMICRO  BUY ₹38.57 at ₹1,119.85 (fresh Friday signal — BUY: 3.17× weekly, month 1.83×, ladder rising; stop ₹1,026.00; charges ₹0.0910)
2025-10-09  FORCEMOT    SELL ₹65.33 at stop ₹15,350.10 (+65.5%, charges ₹0.1451) — the cash goes back to work at the next Friday screen
2025-10-13  RAMKY       BUY ₹41.48 at ₹622.35 (fresh Friday signal — BUY: 20.34× weekly, month 6.75×, ladder rising; stop ₹529.58; charges ₹0.0979)
2025-10-13  SHAILY      BUY ₹23.85 at ₹2,434.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 1.66×, ladder rising; stop ₹1,942.00; charges ₹0.0563)
2025-10-14  SUBROS      SELL ₹38.52 at stop ₹1,046.90 (-7.5%, charges ₹0.0855) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹38.52 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.32×, ladder rising; stop ₹1,311.00; charges ₹0.0909)
2025-10-20  CREDITACC   SELL ₹56.44 at stop ₹1,274.42 (+49.9%, charges ₹0.1254) — the cash goes back to work at the next Friday screen
2025-10-27  HCG         BUY ₹40.95 at ₹758.60 (fresh Friday signal — BUY: surged 2.59× weekly on 2025-10-17 (month 1.51×), ladder rising NOW — promoted from the ladder watch; stop ₹674.50; charges ₹0.0967)
2025-10-28  BLACKBUCK   SELL ₹51.59 at stop ₹642.20 (+16.1%, charges ₹0.1146) — the cash goes back to work at the next Friday screen
2025-11-03  MAHABANK    BUY ₹26.09 at ₹59.70 (fresh Friday signal — ACCUMULATE: 2.08× weekly, month 1.69×, ladder rising; stop ₹53.69; charges ₹0.0616)
2025-11-03  TDPOWERSYS  BUY ₹40.98 at ₹382.27 (fresh Friday signal — BUY: 4.87× weekly, month 1.95×, ladder rising; stop ₹276.78; charges ₹0.0967)
2025-11-06  ASTRAMICRO  SELL ₹35.17 at stop ₹1,026.00 (-8.4%, charges ₹0.0781) — the cash goes back to work at the next Friday screen
2025-11-06  FDC         SELL ₹37.40 at stop ₹425.79 (-13.0%, charges ₹0.0831) — the cash goes back to work at the next Friday screen
2025-11-06  PGHL        SELL ₹40.70 at stop ₹5,938.45 (-6.4%, charges ₹0.0904) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹41.38 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.0977)
2025-11-10  CUB         BUY ₹41.59 at ₹254.20 (fresh Friday signal — BUY: 6.02× weekly, month 1.74×, ladder rising; stop ₹213.75; charges ₹0.0982)
2025-11-10  LTF         BUY ₹30.29 at ₹304.00 (fresh Friday signal — BUY: 2.98× weekly, month 1.53×, ladder rising; stop ₹250.80; charges ₹0.0715)
2025-11-20  ANANDRATHI  SELL ₹35.31 at stop ₹1,450.17 (-7.9%, charges ₹0.0784) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹39.63 at stop ₹976.41 (-3.8%, charges ₹0.0880) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹35.31 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.39×, ladder rising; stop ₹2,956.49; charges ₹0.0834)
2025-11-24  TDPOWERSYS  SELL ₹38.15 at stop ₹357.49 (-6.5%, charges ₹0.0847) — the cash goes back to work at the next Friday screen
2025-12-01  EUREKAFORB  BUY ₹41.19 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.33×, ladder rising; stop ₹535.37; charges ₹0.0972)
2025-12-01  RAMKY       SELL ₹38.36 at stop ₹578.17 (-7.1%, charges ₹0.0852) — the cash goes back to work at the next Friday screen
2025-12-01  SANSERA     BUY ₹36.59 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.54×, ladder rising; stop ₹1,413.60; charges ₹0.0864)
2025-12-08  KIRLOSENG   BUY ₹38.36 at ₹1,130.00 (fresh Friday signal — BUY: 1.67× weekly, month 2.31×, ladder rising; stop ₹886.54; charges ₹0.0906)
2025-12-15  SHAILY      SELL ₹22.83 at stop ₹2,340.80 (-3.8%, charges ₹0.0507) — the cash goes back to work at the next Friday screen
2025-12-22  ASHAPURMIN  BUY ₹22.83 at ₹800.00 (fresh Friday signal — BUY: surged 1.56× weekly on 2025-11-21 (month 1.64×), ladder rising NOW — promoted from the ladder watch; stop ₹641.35; charges ₹0.0539)
2025-12-23  HCG         SELL ₹36.36 at stop ₹676.59 (-10.8%, charges ₹0.0808) — the cash goes back to work at the next Friday screen
2025-12-29  SHRIRAMFIN  BUY ₹36.36 at ₹963.00 (fresh Friday signal — BUY: 1.70× weekly, month 1.58×, ladder rising; stop ₹778.00; charges ₹0.0858)
2026-01-08  EUREKAFORB  SELL ₹36.38 at stop ₹589.10 (-11.3%, charges ₹0.0808) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹31.59 at stop ₹2,956.49 (-10.1%, charges ₹0.0702) — the cash goes back to work at the next Friday screen
2026-01-12  HINDCOPPER  BUY ₹27.85 at ₹532.00 (fresh Friday signal — BUY: surged 1.55× weekly on 2025-12-12 (month 1.96×), ladder rising NOW — promoted from the ladder watch; stop ₹456.95; charges ₹0.0657)
2026-01-12  KIRLOSENG   SELL ₹38.55 at stop ₹1,140.95 (+1.0%, charges ₹0.0856) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹40.12 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.56×, ladder rising; stop ₹246.34; charges ₹0.0947)
2026-01-16  ASHAPURMIN  SELL ₹23.21 at stop ₹817.00 (+2.1%, charges ₹0.0516) — the cash goes back to work at the next Friday screen
2026-01-19  RBA         BUY ₹40.11 at ₹67.50 (fresh Friday signal — BUY: surged 1.55× weekly on 2026-01-09 (month 4.51×), ladder rising NOW — promoted from the ladder watch; stop ₹61.08; charges ₹0.0947)
2026-01-20  LGBBROSLTD  SELL ₹50.83 at stop ₹1,713.80 (+21.4%, charges ₹0.1129) — the cash goes back to work at the next Friday screen
2026-01-21  AVANTIFEED  SELL ₹34.92 at stop ₹748.60 (-8.5%, charges ₹0.0776) — the cash goes back to work at the next Friday screen
2026-01-21  LTF         SELL ₹27.95 at stop ₹281.77 (-7.3%, charges ₹0.0621) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹34.82 at stop ₹1,672.76 (-4.4%, charges ₹0.0773) — the cash goes back to work at the next Friday screen
2026-02-17  NATIONALUM  SELL ₹38.07 at stop ₹335.49 (-4.7%, charges ₹0.0846) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹38.78 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.67×, ladder rising; stop ₹5,440.18; charges ₹0.0916)
2026-02-23  E2E         BUY ₹39.26 at ₹2,914.00 (fresh Friday signal — BUY: 9.16× weekly, month 3.19×, ladder rising; stop ₹2,312.68; charges ₹0.0927)
2026-02-23  HAPPYFORGE  BUY ₹38.67 at ₹1,370.00 (fresh Friday signal — BUY: surged 6.09× weekly on 2026-02-13 (month 1.85×), ladder rising NOW — promoted from the ladder watch; stop ₹1,188.64; charges ₹0.0913)
2026-02-23  VESUVIUS    BUY ₹39.37 at ₹535.10 (fresh Friday signal — BUY: 38.99× weekly, month 4.57×, ladder rising; stop ₹464.31; charges ₹0.0929)
2026-03-02  KSB         BUY ₹38.19 at ₹738.00 (fresh Friday signal — BUY: 52.86× weekly, month 4.79×, ladder rising; stop ₹658.54; charges ₹0.0901)
2026-03-04  HAPPYFORGE  SELL ₹34.67 at stop ₹1,234.05 (-9.9%, charges ₹0.0770) — the cash goes back to work at the next Friday screen
2026-03-04  SHRIRAMFIN  SELL ₹37.30 at stop ₹992.37 (+3.0%, charges ₹0.0828) — the cash goes back to work at the next Friday screen
2026-03-09  CUB         SELL ₹40.95 at stop ₹251.43 (-1.1%, charges ₹0.0910) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹27.55 at stop ₹528.63 (-0.6%, charges ₹0.0612) — the cash goes back to work at the next Friday screen
2026-03-12  RBA         SELL ₹36.13 at stop ₹61.08 (-9.5%, charges ₹0.0802) — the cash goes back to work at the next Friday screen
2026-03-16  J&KBANK     BUY ₹36.66 at ₹121.14 (fresh Friday signal — BUY: 2.61× weekly, month 2.95×, ladder rising; stop ₹103.27; charges ₹0.0865)
2026-03-16  JBCHEPHARM  BUY ₹36.73 at ₹2,136.00 (fresh Friday signal — BUY: 2.39× weekly, month 1.54×, ladder rising; stop ₹1,875.30; charges ₹0.0867)
2026-03-23  J&KBANK     SELL ₹33.34 at stop ₹110.67 (-8.6%, charges ₹0.0741) — the cash goes back to work at the next Friday screen
2026-03-23  VESUVIUS    SELL ₹34.01 at stop ₹464.31 (-13.2%, charges ₹0.0755) — the cash goes back to work at the next Friday screen
2026-03-23  VTL         BUY ₹36.02 at ₹534.00 (fresh Friday signal — BUY: surged 1.53× weekly on 2026-02-27 (month 2.21×), ladder rising NOW — promoted from the ladder watch; stop ₹485.45; charges ₹0.0850)
2026-03-30  AETHER      BUY ₹35.93 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0848)
2026-03-30  MAHABANK    SELL ₹26.56 at stop ₹61.05 (+2.3%, charges ₹0.0590) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹3.6056 paid (STCG ₹18.03 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹35.63 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.65×, ladder rising; stop ₹891.29; charges ₹0.0841)
2026-04-13  INOXINDIA   BUY ₹36.68 at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹0.0866)
2026-04-13  STLTECH     BUY ₹26.24 at ₹224.31 (fresh Friday signal — BUY: surged 1.81× weekly on 2026-03-13 (month 2.29×), ladder rising NOW — promoted from the ladder watch; stop ₹162.10; charges ₹0.0619)
2026-04-13  THERMAX     BUY ₹36.99 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.0873)
2026-05-04  KSB         SELL ₹47.25 at stop ₹917.42 (+24.3%, charges ₹0.1050) — the cash goes back to work at the next Friday screen
2026-05-11  CRAFTSMAN   BUY ₹41.00 at ₹9,039.50 (fresh Friday signal — BUY: 22.97× weekly, month 3.93×, ladder rising; stop ₹7,119.77; charges ₹0.0968)
2026-05-13  INOXINDIA   SELL ₹38.56 at stop ₹1,372.18 (+5.6%, charges ₹0.0857) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹35.00 at stop ₹1,125.84 (-2.1%, charges ₹0.0777) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹39.77 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.23×, ladder rising; stop ₹1,502.04; charges ₹0.0939)
2026-05-18  CAPLIPOINT  BUY ₹39.76 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0939)
2026-06-05  E2E         SELL ₹31.26 at stop ₹2,330.72 (-20.0%, charges ₹0.0694) — the cash goes back to work at the next Friday screen
2026-06-08  RUBICON     BUY ₹31.55 at ₹1,190.00 (fresh Friday signal — BUY: 15.02× weekly, month 1.61×, ladder rising; stop ₹872.10; charges ₹0.0745)
2026-07-29  THERMAX     SELL ₹44.09 at stop ₹4,306.64 (+19.8%, charges ₹0.0979) — the cash goes back to work at the next Friday screen
2026-07-31  VTL         SELL ₹39.80 at stop ₹592.80 (+11.0%, charges ₹0.0884) — the cash goes back to work at the next Friday screen
2026-08-03  BLUESTONE   BUY ₹39.06 at ₹823.40 (fresh Friday signal — ACCUMULATE: 5.63× weekly, month 9.43×, ladder rising; stop ₹664.75; charges ₹0.0922)
2026-08-03  TMB         BUY ₹44.84 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.56×, ladder rising; stop ₹748.60; charges ₹0.1058)
2026-09-10  ALKYLAMINE  SELL ₹44.47 at stop ₹1,920.99 (+12.3%, charges ₹0.0988) — the cash goes back to work at the next Friday screen
2026-09-15  ABB         SELL ₹45.38 at stop ₹7,158.25 (+17.5%, charges ₹0.1008) — the cash goes back to work at the next Friday screen
2026-09-15  SUNDRMFAST  BUY ₹44.47 at ₹1,277.30 (fresh Friday signal — BUY: 3.14× weekly, month 1.81×, ladder rising; stop ₹1,127.74; charges ₹0.1050)
2026-09-21  AVALON      BUY ₹45.38 at ₹2,550.00 (fresh Friday signal — BUY: 2.64× weekly, month 1.85×, ladder rising; stop ₹2,032.34; charges ₹0.1071)
```
