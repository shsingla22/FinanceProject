# The Darvas screen, run for six years — 2020-06-01 → 2026-09-11

> **LONG-RUN BACKTEST.** One continuous price archive (2019-06-01 → 2026-09-11, 741 symbols, fetched once into `2019-06-01_to_2026-09-13/`) so every Friday screen has its full year of volume baseline and six months of boxes. Every screen sees only bars up to its own Friday. The earnings gate reads only fiscal years ended on or before the last 31 March at each screen date — the cut rolls forward with the replay — and the conference-call read is excluded. **Two limits that cannot be engineered away:** the universe is TODAY'S NiftyTotalMarket constituents (survivorship bias — companies that later failed or left the index are missing from the early years, which flatters results), and Yahoo serves split-adjusted history as it stands today. No costs, no slippage, stop exits at the stop price, fractional shares.

## The rules, exactly as the live skill prescribes

₹100 starts ALL IN CASH. Every Friday after the close, the full three-gate screen (weekly volume ≥1.5× the 12-week average WITH a rising price; last month's volume ≥1.5× the year's norm; at least 3 boxes with the last 3 midpoints rising) runs over the whole universe. Fresh BUY/ACCUMULATE signals are funded from cash — equal slices of one tenth of equity, best volume reaction first, entries at the next trading day's open, falling earnings power refused, nothing below half a slice. Stops (box bottom − max(0.3×height, 5% of bottom)) are checked daily and ratcheted up weekly; the stabilisation grace applies — only the stop itself exits. **Pyramiding:** on every 2nd consecutive box jump upward without the stop being hit, the stake is DOUBLED — new capital equal to the position's market value goes in at the next day's open, from cash only (partial when cash runs short, never borrowed), each add-on a separate tax lot on its own holding clock, the ratcheted stop covering the whole enlarged position. A stopped symbol returns only by passing the full screen again. **When nothing qualifies, the cash stays cash.**

## The headline

| | ₹100 became | CAGR |
|---|---:|---:|
| **This system, NET of Angel One charges and capital-gains tax** | **₹447.36** | **+27.01% a year** |
| The same system before costs and taxes | ₹651.14 | +34.85% a year |
| Nifty 50 (same window, itself pre-cost, pre-tax) | ₹230.70 | +14.27% a year |

*The net run is a full separate simulation, not a discount applied afterwards: charges shrink every position as it is opened, tax leaves the portfolio every 1 April, and the smaller cash pile funds fewer fresh signals along the way. ₹2.39 of tax has additionally accrued on the final part-year's realised gains (due next April, not yet paid) — settling it today would leave **₹444.97** (+26.90% a year). Gains still unrealised in the end book carry a further deferred liability when eventually sold.*

6.27 years, 328 weekly screens, 415 dated entries (buys, sells, tax settlements) in the blotter below.


## What the frictions took

- **Transaction charges: ₹21.70** across every order of the whole run (Angel One equity delivery: STT 0.10% both sides, NSE transaction charge 0.00297%, SEBI fee 0.0001%, 18% GST on brokerage+levies, stamp duty 0.015% on buys; delivery brokerage ₹0 until 31 Oct 2024 and min(0.1%, ₹20)/order from 1 Nov 2024 — at this normalised scale the ₹20 cap never binds, so 0.1% applies). Flat charges that cannot scale to a normalised ₹100 — the ~₹20+GST DP charge per sell and the ₹2 brokerage minimum — are excluded; on a ₹1-lakh+ account they are under 0.03% of a trade.
- **Capital-gains tax paid: ₹71.64**, settled out of the portfolio on the first trading day of each April — 20% short-term (held ≤ 365 days), 12.5% long-term (> 365 days), with lawful set-off: short-term losses absorb short- then long-term gains, long-term losses only long-term gains, unabsorbed losses carried forward. Gains are computed on execution prices (charges not added to basis) and the LTCG exemption slab is ignored — both simplifications overstate the tax slightly, never understate it.

| Fiscal year | Settled on | STCG taxed @20% | LTCG taxed @12.5% | Tax paid | Losses carried fwd (ST / LT) |
|---|---|---:|---:|---:|---:|
| FY2021 | 2021-04-01 | ₹41.01 | ₹0.00 | ₹8.2011 | ₹0.00 / ₹0.00 |
| FY2022 | 2022-04-01 | ₹53.23 | ₹0.00 | ₹10.6462 | ₹0.00 / ₹0.00 |
| FY2023 | 2023-04-03 | ₹45.04 | ₹3.27 | ₹9.4155 | ₹0.00 / ₹0.00 |
| FY2024 | 2024-04-01 | ₹177.57 | ₹0.00 | ₹35.5148 | ₹0.00 / ₹0.00 |
| FY2025 | 2025-04-01 | ₹35.63 | ₹0.00 | ₹7.1252 | ₹0.00 / ₹0.00 |
| FY2026 | 2026-04-01 | ₹3.68 | ₹0.00 | ₹0.7357 | ₹0.00 / ₹0.00 |
| FY2027 (accrued, due next April) | — | ₹11.96 | ₹0.00 | ₹2.3921 | ₹0.00 / ₹0.00 |

## Calendar-year equity — net of costs and taxes

| Year (through) | Net equity (₹) | Net return | Gross return | Nifty 50 |
|---|---:|---:|---:|---:|
| 2020 (2020-12-24) | 145.67 | +45.7% | +46.5% | +35.6% |
| 2021 (2021-12-31) | 216.85 | +48.9% | +59.2% | +26.2% |
| 2022 (2022-12-30) | 254.44 | +17.3% | +29.4% | +4.3% |
| 2023 (2023-12-29) | 382.50 | +50.3% | +56.0% | +20.0% |
| 2024 (2024-12-27) | 441.06 | +15.3% | +30.4% | +9.6% |
| 2025 (2025-12-26) | 437.95 | -0.7% | +2.4% | +9.4% |
| 2026 (2026-09-11) | 447.36 | +2.1% | +3.6% | -10.2% |

## What pyramiding changed — an honest negative result

This run adds the pyramiding rule (double the stake on every 2nd
consecutive box jump). The previous run of the SAME window, identical
in every other rule, is in this repository's history — side by side:

| | Gross ₹100 → | Gross CAGR | Net ₹100 → | Net CAGR |
|---|---:|---:|---:|---:|
| Without pyramiding (previous run) | ₹1,050.49 | +45.54% | ₹788.82 | +39.04% |
| **With pyramiding (this run)** | **₹651.14** | **+34.85%** | **₹447.36** | **+27.01%** |

Pyramiding still beat the index comfortably — but it gave away roughly
a third of the compounding, and the ledger says exactly why:

- **The add-on buys near the top and its stop sits a whole box lower.**
  72 pyramids executed in the net run; **42 of the 72 positions later
  stopped out BELOW the add-on price**, so the doubled lot lost money
  outright while fattening the position exactly when the risk to the
  stop was widest.
- **Doubling starves the pipeline that actually made the money.** The
  add-ons consumed the cash that used to fund fresh Friday qualifiers:
  fresh entries fell from 214 to 171, and 86 further pyramid calls went
  unfunded for lack of cash. The no-pyramid run's compounding came from
  a steady stream of NEW breakouts, not from concentration.
- **Concentration also cut the winners early.** With more capital in
  fewer names, single stop-outs took bigger bites of equity — every
  calendar year's return is lower than the no-pyramid run's, and 2026
  fell from +21.6% net to +2.1%.

The rule is implemented, tested and stays available in the engine —
but on this window the evidence says Darvas's original sizing (equal
slices, let the RATCHET do the concentrating by simply not selling
winners) beats doubling into strength.

## What it took to earn it

- **Maximum drawdown: -34.3%** (peak 2024-03-01 → trough 2026-04-02, on weekly closes).
- **166 closed trades**: 71 winners (43%), average winner +29.1%, average loser -10.2%.
- Best closed trade ADANIPOWER +153.0%; worst IOB -31.5%.
- Median holding period 70 days.
- Cash share of equity averaged 14% across all weeks (median 4%); the portfolio sat FULLY in cash for 1 of 328 weeks — rule 3: when nothing qualifies, the money waits.

## Monthly equity curve

| Month-end screen | Equity (₹) | Cash (₹) | Positions |
|---|---:|---:|---:|
| 2020-06-26 | 104.31 | 0.61 | 10 |
| 2020-07-31 | 109.48 | 16.12 | 7 |
| 2020-08-28 | 122.70 | 0.71 | 7 |
| 2020-09-25 | 120.09 | 11.81 | 7 |
| 2020-10-30 | 117.75 | 25.43 | 6 |
| 2020-11-27 | 132.52 | 2.60 | 8 |
| 2020-12-24 | 145.67 | 53.36 | 6 |
| 2021-01-29 | 148.43 | 86.87 | 4 |
| 2021-02-26 | 155.95 | 56.88 | 5 |
| 2021-03-26 | 145.87 | 56.30 | 6 |
| 2021-04-30 | 148.59 | 19.49 | 6 |
| 2021-05-28 | 166.07 | 0.00 | 7 |
| 2021-06-25 | 174.44 | 7.08 | 7 |
| 2021-07-30 | 192.48 | 0.00 | 7 |
| 2021-08-27 | 187.72 | 25.75 | 6 |
| 2021-09-24 | 212.42 | 0.00 | 7 |
| 2021-10-29 | 202.91 | 26.23 | 7 |
| 2021-11-26 | 205.46 | 59.38 | 5 |
| 2021-12-31 | 216.85 | 17.23 | 7 |
| 2022-01-28 | 194.55 | 99.58 | 4 |
| 2022-02-25 | 182.50 | 106.40 | 4 |
| 2022-03-25 | 201.34 | 106.40 | 4 |
| 2022-04-29 | 218.52 | 0.00 | 9 |
| 2022-05-27 | 207.59 | 56.00 | 6 |
| 2022-06-24 | 202.22 | 0.00 | 7 |
| 2022-07-29 | 228.22 | 11.03 | 6 |
| 2022-08-26 | 237.97 | 75.11 | 4 |
| 2022-09-30 | 238.21 | 0.00 | 5 |
| 2022-10-28 | 239.64 | 0.00 | 5 |
| 2022-11-25 | 252.37 | 78.26 | 4 |
| 2022-12-30 | 254.44 | 165.47 | 3 |
| 2023-01-27 | 247.46 | 0.11 | 8 |
| 2023-02-24 | 232.60 | 31.40 | 7 |
| 2023-03-31 | 228.15 | 99.90 | 3 |
| 2023-04-28 | 229.40 | 54.40 | 6 |
| 2023-05-26 | 238.97 | 20.94 | 7 |
| 2023-06-30 | 250.00 | 0.00 | 7 |
| 2023-07-28 | 282.11 | 0.00 | 7 |
| 2023-08-25 | 270.43 | 0.00 | 5 |
| 2023-09-29 | 286.39 | 0.00 | 5 |
| 2023-10-27 | 289.71 | 137.19 | 3 |
| 2023-11-24 | 360.66 | 0.00 | 8 |
| 2023-12-29 | 382.50 | 0.00 | 7 |
| 2024-01-25 | 450.57 | 34.10 | 6 |
| 2024-02-23 | 534.72 | 0.00 | 6 |
| 2024-03-28 | 520.90 | 178.38 | 5 |
| 2024-04-26 | 481.85 | 0.00 | 8 |
| 2024-05-31 | 490.57 | 45.51 | 7 |
| 2024-06-28 | 460.00 | 0.00 | 10 |
| 2024-07-26 | 462.20 | 129.84 | 7 |
| 2024-08-30 | 483.60 | 0.00 | 10 |
| 2024-09-27 | 490.21 | 0.00 | 10 |
| 2024-10-25 | 429.65 | 159.49 | 7 |
| 2024-11-29 | 457.70 | 0.00 | 8 |
| 2024-12-27 | 441.06 | 156.72 | 6 |
| 2025-01-24 | 404.54 | 168.12 | 4 |
| 2025-02-28 | 375.08 | 295.51 | 2 |
| 2025-03-28 | 385.67 | 219.64 | 4 |
| 2025-04-25 | 384.38 | 170.37 | 5 |
| 2025-05-30 | 410.10 | 0.00 | 9 |
| 2025-06-27 | 444.36 | 0.00 | 9 |
| 2025-07-25 | 506.74 | 0.00 | 9 |
| 2025-08-29 | 514.22 | 0.43 | 6 |
| 2025-09-26 | 460.80 | 222.81 | 4 |
| 2025-10-31 | 434.30 | 203.19 | 5 |
| 2025-11-28 | 435.59 | 120.61 | 7 |
| 2025-12-26 | 437.95 | 0.00 | 9 |
| 2026-01-30 | 415.82 | 184.72 | 4 |
| 2026-02-27 | 415.78 | 35.14 | 4 |
| 2026-03-27 | 373.04 | 196.80 | 2 |
| 2026-04-24 | 391.99 | 56.76 | 7 |
| 2026-05-29 | 405.26 | 0.00 | 7 |
| 2026-06-26 | 404.85 | 0.00 | 6 |
| 2026-07-31 | 411.25 | 90.36 | 5 |
| 2026-08-28 | 431.06 | 0.00 | 6 |
| 2026-09-11 | 447.36 | 84.56 | 5 |

## Still held at the end

| Stock | Entry | Entry ₹ | Mark ₹ | Stop | Return |
|---|---|---:|---:|---:|---:|
| ABB | 2026-02-23 | 6,176.90 | 7,274.00 | 7,158.25 | +17.8% |
| CAPLIPOINT | 2026-05-18 | 2,010.00 | 2,754.90 | 2,376.52 | +37.1% |
| CHENNPETRO | 2026-04-06 | 1,098.46 | 1,572.90 | 1,242.60 | +43.2% |
| TIPSMUSIC | 2026-04-27 | 670.00 | 661.55 | 608.52 | -1.3% |
| TMB | 2026-08-03 | 864.90 | 910.90 | 796.29 | +5.3% |

## Every closed trade

| Stock | Entry | Entry ₹ | Exit | Exit ₹ | Return |
|---|---|---:|---|---:|---:|
| IGL | 2020-06-08 | 247.75 | 2020-07-07 | 208.81 | -15.7% |
| RELAXO | 2020-06-08 | 759.45 | 2020-07-28 | 603.77 | -20.5% |
| LLOYDSENGG | 2020-06-08 | 0.87 | 2020-07-31 | 0.71 | -18.0% |
| EIDPARRY | 2020-06-08 | 221.48 | 2020-08-17 | 273.03 | +23.3% |
| GRANULES | 2020-06-15 | 227.67 | 2020-08-31 | 286.95 | +26.0% |
| ZENTEC | 2020-08-03 | 58.80 | 2020-08-31 | 80.56 | +37.0% |
| KIRLOSBROS | 2020-06-08 | 119.27 | 2020-09-08 | 120.79 | +1.3% |
| RCF | 2020-06-08 | 47.11 | 2020-09-09 | 45.84 | -2.7% |
| SCHAEFFLER | 2020-09-14 | 814.00 | 2020-09-23 | 724.67 | -11.0% |
| INDIAMART | 2020-09-07 | 2,124.50 | 2020-10-19 | 2,315.62 | +9.0% |
| CAPLIPOINT | 2020-06-15 | 492.84 | 2020-10-30 | 498.06 | +1.1% |
| GLAXO | 2020-09-14 | 1,675.00 | 2020-11-02 | 1,441.55 | -13.9% |
| ADVENZYMES | 2020-06-15 | 231.60 | 2020-11-03 | 292.33 | +26.2% |
| ATGL | 2020-09-14 | 227.99 | 2020-12-21 | 332.60 | +45.9% |
| SYNGENE | 2020-06-08 | 373.90 | 2020-12-22 | 562.40 | +50.4% |
| BORORENEW | 2020-11-09 | 99.70 | 2021-01-20 | 247.59 | +148.3% |
| JUSTDIAL | 2020-11-02 | 654.24 | 2021-01-25 | 622.35 | -4.9% |
| HFCL | 2020-12-28 | 28.32 | 2021-01-28 | 28.12 | -0.7% |
| HCLTECH | 2020-09-28 | 838.40 | 2021-01-29 | 928.05 | +10.7% |
| TRENT | 2020-11-17 | 755.00 | 2021-01-29 | 626.30 | -17.0% |
| JKCEMENT | 2020-12-28 | 1,913.20 | 2021-01-29 | 2,061.50 | +7.8% |
| GAEL | 2021-02-01 | 71.47 | 2021-02-23 | 62.70 | -12.3% |
| KPRMILL | 2020-11-02 | 167.53 | 2021-02-24 | 166.62 | -0.5% |
| ITC | 2021-02-08 | 228.69 | 2021-02-26 | 197.41 | -13.7% |
| GRAVITA | 2020-12-28 | 69.65 | 2021-03-17 | 96.13 | +38.0% |
| RCF | 2021-03-01 | 80.00 | 2021-03-17 | 79.16 | -1.1% |
| UJJIVANSFB | 2021-02-08 | 37.15 | 2021-03-18 | 32.12 | -13.5% |
| MAHABANK | 2021-02-08 | 20.82 | 2021-03-19 | 18.37 | -11.8% |
| HONAUT | 2020-12-28 | 40,442.45 | 2021-03-22 | 41,911.15 | +3.6% |
| GESHIP | 2021-03-01 | 315.90 | 2021-04-12 | 290.70 | -8.0% |
| AUBANK | 2021-04-05 | 631.00 | 2021-04-12 | 533.06 | -15.5% |
| IOB | 2021-03-01 | 18.90 | 2021-04-28 | 14.82 | -21.6% |
| POLYMED | 2020-09-07 | 632.47 | 2021-06-14 | 950.00 | +50.2% |
| WELSPUNLIV | 2021-03-22 | 81.45 | 2021-08-10 | 124.64 | +53.0% |
| MARKSANS | 2021-05-03 | 75.51 | 2021-08-10 | 77.14 | +2.2% |
| KPRMILL | 2021-04-19 | 236.00 | 2021-08-11 | 352.48 | +49.4% |
| JWL | 2021-06-21 | 30.80 | 2021-08-23 | 30.42 | -1.2% |
| KEI | 2021-03-22 | 622.46 | 2021-10-22 | 853.10 | +37.1% |
| DEEPAKFERT | 2021-03-22 | 237.00 | 2021-11-11 | 385.70 | +62.7% |
| GRAVITA | 2021-08-23 | 204.19 | 2021-11-22 | 197.03 | -3.5% |
| TATAINVEST | 2021-08-16 | 130.81 | 2021-11-26 | 143.65 | +9.8% |
| NHPC | 2021-09-06 | 30.79 | 2021-11-29 | 30.11 | -2.2% |
| KPITTECH | 2021-03-30 | 318.42 | 2021-12-20 | 458.85 | +44.1% |
| UNOMINDA | 2021-12-27 | 590.00 | 2022-01-07 | 544.21 | -7.8% |
| LTM | 2021-10-25 | 6,542.51 | 2022-01-24 | 6,270.00 | -4.2% |
| PERSISTENT | 2021-11-01 | 2,144.23 | 2022-01-24 | 2,067.34 | -3.6% |
| AFFLE | 2022-01-10 | 1,307.00 | 2022-01-25 | 1,206.50 | -7.7% |
| SHARDACROP | 2022-01-31 | 586.70 | 2022-02-11 | 545.30 | -7.1% |
| GABRIEL | 2021-08-16 | 144.78 | 2022-02-14 | 125.40 | -13.4% |
| BSOFT | 2021-12-27 | 529.00 | 2022-02-14 | 424.65 | -19.7% |
| CHAMBLFERT | 2021-12-06 | 407.45 | 2022-02-24 | 353.85 | -13.2% |
| CCL | 2022-02-07 | 503.55 | 2022-02-24 | 441.75 | -12.3% |
| RCF | 2022-04-04 | 96.40 | 2022-05-04 | 93.15 | -3.4% |
| GNFC | 2022-02-14 | 553.00 | 2022-05-06 | 792.16 | +43.2% |
| BSE | 2021-12-06 | 209.99 | 2022-05-10 | 255.87 | +21.8% |
| MINDACORP | 2022-04-11 | 230.05 | 2022-05-11 | 186.63 | -18.9% |
| LTFOODS | 2022-04-18 | 91.70 | 2022-05-11 | 73.86 | -19.5% |
| SPLPETRO | 2022-04-04 | 475.00 | 2022-05-24 | 424.27 | -10.7% |
| MRPL | 2022-05-09 | 83.17 | 2022-07-06 | 69.61 | -16.3% |
| VBL | 2022-05-16 | 146.67 | 2022-08-22 | 188.52 | +28.5% |
| BLS | 2022-04-11 | 95.37 | 2022-08-23 | 110.67 | +16.0% |
| HOMEFIRST | 2022-08-29 | 944.95 | 2022-09-14 | 849.35 | -10.1% |
| ADANIPOWER | 2022-02-21 | 26.40 | 2022-10-14 | 66.80 | +153.0% |
| KALYANKJIL | 2022-08-29 | 90.75 | 2022-11-22 | 94.53 | +4.2% |
| ELECON | 2022-06-13 | 134.73 | 2022-12-21 | 202.49 | +50.3% |
| ACC | 2022-05-23 | 2,267.00 | 2022-12-23 | 2,465.15 | +8.7% |
| IRFC | 2022-11-28 | 32.00 | 2022-12-23 | 28.20 | -11.9% |
| APOLLO | 2022-10-17 | 24.16 | 2022-12-26 | 24.42 | +1.1% |
| GICRE | 2023-01-02 | 179.20 | 2023-02-01 | 167.72 | -6.4% |
| LLOYDSENGG | 2023-01-02 | 15.63 | 2023-02-07 | 19.27 | +23.3% |
| CGCL | 2022-02-21 | 567.08 | 2023-03-08 | 666.82 | +17.6% |
| YESBANK | 2023-01-02 | 20.85 | 2023-03-13 | 15.34 | -26.4% |
| IOB | 2023-01-02 | 32.40 | 2023-03-20 | 22.18 | -31.5% |
| UCOBANK | 2022-11-28 | 26.42 | 2023-03-27 | 23.46 | -11.2% |
| JINDALSAW | 2023-02-06 | 65.22 | 2023-03-27 | 67.92 | +4.1% |
| SONATSOFTW | 2023-03-20 | 397.50 | 2023-03-29 | 371.45 | -6.6% |
| JSL | 2023-01-02 | 253.24 | 2023-04-13 | 256.98 | +1.5% |
| KIRLOSBROS | 2023-04-10 | 425.00 | 2023-04-26 | 403.85 | -5.0% |
| MARKSANS | 2023-04-24 | 78.00 | 2023-05-22 | 71.87 | -7.9% |
| ASHAPURMIN | 2023-05-02 | 136.50 | 2023-05-29 | 134.24 | -1.7% |
| MAHABANK | 2022-11-28 | 26.20 | 2023-06-15 | 27.79 | +6.1% |
| ANURAS | 2023-03-20 | 834.32 | 2023-07-03 | 1,007.67 | +20.8% |
| KSB | 2023-04-10 | 451.00 | 2023-07-12 | 407.74 | -9.6% |
| REFEX | 2023-05-02 | 78.25 | 2023-08-11 | 121.69 | +55.5% |
| CEATLTD | 2023-07-10 | 2,408.00 | 2023-08-14 | 2,244.85 | -6.8% |
| HEG | 2023-06-19 | 317.84 | 2023-10-23 | 328.78 | +3.4% |
| HAL | 2023-04-03 | 1,689.03 | 2023-10-25 | 1,840.70 | +9.0% |
| TSFINV | 2023-11-06 | 144.75 | 2023-12-20 | 145.40 | +0.4% |
| ANGELONE | 2023-10-30 | 253.50 | 2024-01-23 | 296.88 | +17.1% |
| ZFCVINDIA | 2023-04-24 | 1,750.90 | 2024-02-02 | 2,473.96 | +41.3% |
| APOLLO | 2023-11-06 | 95.90 | 2024-02-13 | 112.10 | +16.9% |
| MEDANTA | 2023-06-19 | 663.97 | 2024-03-06 | 1,225.50 | +84.6% |
| SHAREINDIA | 2023-10-30 | 300.00 | 2024-03-06 | 357.20 | +19.1% |
| RITES | 2024-01-29 | 342.50 | 2024-03-13 | 314.37 | -8.2% |
| ANANDRATHI | 2023-07-17 | 417.31 | 2024-03-27 | 862.65 | +106.7% |
| DMART | 2024-04-01 | 4,570.00 | 2024-05-31 | 4,322.83 | -5.4% |
| CUPID | 2023-10-30 | 7.03 | 2024-06-04 | 17.77 | +152.8% |
| SOLARINDS | 2024-03-11 | 7,564.00 | 2024-06-04 | 7,980.95 | +5.5% |
| BHEL | 2024-03-11 | 259.10 | 2024-06-04 | 251.68 | -2.9% |
| SHRIRAMFIN | 2024-04-01 | 474.20 | 2024-06-04 | 441.77 | -6.8% |
| HGINFRA | 2024-04-08 | 1,097.70 | 2024-06-04 | 1,274.90 | +16.1% |
| UNOMINDA | 2024-06-10 | 970.00 | 2024-07-19 | 981.87 | +1.2% |
| FIEMIND | 2024-06-10 | 1,309.51 | 2024-07-23 | 1,257.56 | -4.0% |
| NCC | 2024-06-10 | 327.60 | 2024-07-23 | 297.87 | -9.1% |
| ENDURANCE | 2024-06-10 | 2,439.90 | 2024-08-05 | 2,429.11 | -0.4% |
| ADANIPOWER | 2024-06-10 | 156.60 | 2024-08-12 | 126.55 | -19.2% |
| CAMPUS | 2024-06-03 | 288.62 | 2024-08-16 | 277.07 | -4.0% |
| AVANTIFEED | 2024-07-29 | 697.65 | 2024-09-09 | 650.13 | -6.8% |
| KSCL | 2024-07-29 | 1,068.40 | 2024-09-30 | 973.63 | -8.9% |
| DABUR | 2024-06-10 | 604.20 | 2024-10-03 | 602.49 | -0.3% |
| VGUARD | 2024-08-19 | 524.15 | 2024-10-04 | 420.24 | -19.8% |
| INDIGO | 2024-03-18 | 3,200.00 | 2024-10-07 | 4,485.14 | +40.2% |
| THYROCARE | 2024-07-29 | 261.67 | 2024-10-07 | 265.38 | +1.4% |
| GODFRYPHLP | 2024-02-05 | 848.30 | 2024-10-22 | 2,086.31 | +145.9% |
| HINDUNILVR | 2024-06-10 | 2,579.00 | 2024-10-23 | 2,667.03 | +3.4% |
| INOXWIND | 2024-08-19 | 215.70 | 2024-11-13 | 193.99 | -10.1% |
| INDIAGLYCO | 2024-10-14 | 739.40 | 2024-11-13 | 566.76 | -23.3% |
| SUPRIYA | 2024-08-19 | 653.28 | 2024-12-17 | 717.25 | +9.8% |
| KIRLPNU | 2024-11-04 | 849.00 | 2024-12-23 | 798.00 | -6.0% |
| PRSMJOHNSN | 2024-09-16 | 202.76 | 2024-12-26 | 170.55 | -15.9% |
| JSWDULUX | 2024-11-04 | 4,518.00 | 2024-12-27 | 3,423.18 | -24.2% |
| PAYTM | 2024-10-28 | 882.19 | 2025-01-09 | 893.05 | +1.2% |
| SKIPPER | 2024-10-14 | 553.00 | 2025-01-10 | 477.28 | -13.7% |
| KAYNES | 2024-12-23 | 7,358.80 | 2025-01-10 | 6,670.80 | -9.3% |
| ZENTEC | 2024-12-23 | 2,555.00 | 2025-01-13 | 2,213.55 | -13.4% |
| KFINTECH | 2024-12-30 | 1,511.45 | 2025-01-15 | 1,159.14 | -23.3% |
| AEGISLOG | 2025-01-13 | 834.65 | 2025-01-24 | 700.36 | -16.1% |
| LLOYDSME | 2025-01-13 | 1,441.90 | 2025-01-28 | 1,258.75 | -12.7% |
| APOLLO | 2025-01-20 | 131.50 | 2025-02-17 | 110.19 | -16.2% |
| ZENSARTECH | 2025-02-03 | 947.00 | 2025-02-17 | 814.20 | -14.0% |
| BSE | 2024-10-07 | 1,582.41 | 2025-02-28 | 1,651.54 | +4.4% |
| INDIASHLTR | 2025-03-24 | 794.95 | 2025-04-07 | 738.82 | -7.1% |
| CEMPRO | 2024-10-07 | 655.05 | 2025-04-11 | 524.92 | -19.9% |
| PARAS | 2025-05-05 | 686.10 | 2025-07-28 | 708.99 | +3.3% |
| NH | 2025-03-03 | 1,450.00 | 2025-08-04 | 1,814.78 | +25.2% |
| WHIRLPOOL | 2025-04-28 | 1,153.90 | 2025-08-07 | 1,301.97 | +12.8% |
| INDIASHLTR | 2025-04-15 | 883.73 | 2025-09-25 | 862.60 | -2.4% |
| SMLMAH | 2025-04-28 | 2,812.66 | 2025-09-26 | 3,255.67 | +15.8% |
| FORCEMOT | 2025-04-28 | 9,275.00 | 2025-10-09 | 15,350.10 | +65.5% |
| SUBROS | 2025-09-29 | 1,132.00 | 2025-10-14 | 1,046.90 | -7.5% |
| CREDITACC | 2025-01-27 | 1,148.30 | 2025-10-20 | 1,274.42 | +11.0% |
| GALLANTT | 2025-04-21 | 474.75 | 2025-10-20 | 616.41 | +29.8% |
| NETWEB | 2025-09-29 | 3,700.00 | 2025-11-06 | 3,515.95 | -5.0% |
| ANANDRATHI | 2025-10-20 | 1,574.50 | 2025-11-20 | 1,450.17 | -7.9% |
| NLCINDIA | 2025-09-29 | 280.30 | 2025-11-24 | 241.39 | -13.9% |
| TDPOWERSYS | 2025-11-03 | 382.27 | 2025-11-24 | 357.49 | -6.5% |
| CCL | 2025-11-10 | 1,014.90 | 2025-11-24 | 976.41 | -3.8% |
| SHAILY | 2025-10-13 | 2,434.00 | 2025-12-15 | 2,340.80 | -3.8% |
| EUREKAFORB | 2025-12-01 | 664.00 | 2026-01-08 | 589.10 | -11.3% |
| GRAVITA | 2025-11-10 | 1,711.00 | 2026-01-09 | 1,678.56 | -1.9% |
| RADICO | 2025-11-24 | 3,289.40 | 2026-01-09 | 2,956.50 | -10.1% |
| KIRLOSENG | 2025-12-22 | 1,258.30 | 2026-01-12 | 1,140.95 | -9.3% |
| AVANTIFEED | 2025-04-15 | 737.82 | 2026-01-21 | 748.60 | +1.5% |
| LTF | 2025-11-10 | 304.00 | 2026-01-21 | 281.77 | -7.3% |
| SANSERA | 2025-12-01 | 1,797.74 | 2026-01-23 | 1,672.76 | -7.0% |
| HINDZINC | 2026-01-27 | 733.00 | 2026-02-02 | 602.35 | -17.8% |
| NATIONALUM | 2026-01-12 | 349.55 | 2026-02-17 | 335.49 | -4.0% |
| CUB | 2025-11-10 | 204.36 | 2026-03-09 | 188.57 | -7.7% |
| HINDCOPPER | 2026-02-02 | 577.51 | 2026-03-12 | 528.63 | -8.5% |
| MAHABANK | 2025-11-03 | 60.09 | 2026-03-30 | 61.05 | +1.6% |
| INOXINDIA | 2026-04-13 | 1,299.10 | 2026-05-13 | 1,372.18 | +5.6% |
| AETHER | 2026-03-30 | 1,169.62 | 2026-05-14 | 1,125.84 | -3.7% |
| GALLANTT | 2026-04-20 | 862.10 | 2026-05-14 | 783.75 | -9.1% |
| NLCINDIA | 2026-04-20 | 307.11 | 2026-06-09 | 320.62 | +4.4% |
| THERMAX | 2026-04-13 | 4,026.79 | 2026-07-29 | 4,306.63 | +6.9% |
| ALKYLAMINE | 2026-05-18 | 1,747.91 | 2026-09-10 | 1,920.99 | +9.9% |

## The complete trade blotter

*Buys and sells only; every stop raise, refused signal and unfunded signal is in `_longrun_events_2020-06-01_to_2026-09-11.csv` beside this report (1897 events in all).*

```
2020-06-08  EIDPARRY    BUY ₹10.00 at ₹219.00 (fresh Friday signal — BUY: 4.34× weekly, month 3.59×, ladder rising; stop ₹132.60; charges ₹0.0118)
2020-06-08  IGL         BUY ₹9.95 at ₹247.75 (fresh Friday signal — BUY: 1.53× weekly, month 1.89×, ladder rising; stop ₹208.81; charges ₹0.0118)
2020-06-08  KIRLOSBROS  BUY ₹9.96 at ₹106.50 (fresh Friday signal — ACCUMULATE: 2.95× weekly, month 1.69×, ladder rising; stop ₹91.63; charges ₹0.0118)
2020-06-08  LLOYDSENGG  BUY ₹10.00 at ₹0.87 (fresh Friday signal — BUY: 4.83× weekly, month 4.76×, ladder rising; stop ₹0.46; charges ₹0.0118)
2020-06-08  RCF         BUY ₹10.02 at ₹45.20 (fresh Friday signal — BUY: 2.38× weekly, month 2.29×, ladder rising; stop ₹35.25; charges ₹0.0119)
2020-06-08  RELAXO      BUY ₹10.00 at ₹759.45 (fresh Friday signal — BUY: 1.89× weekly, month 1.81×, ladder rising; stop ₹603.77; charges ₹0.0118)
2020-06-08  SYNGENE     BUY ₹9.95 at ₹373.90 (fresh Friday signal — ACCUMULATE: 1.59× weekly, month 2.27×, ladder rising; stop ₹323.19; charges ₹0.0118)
2020-06-15  ADVENZYMES  BUY ₹9.87 at ₹172.70 (fresh Friday signal — BUY: 4.13× weekly, month 2.92×, ladder rising; stop ₹126.20; charges ₹0.0117)
2020-06-15  CAPLIPOINT  BUY ₹9.82 at ₹383.80 (fresh Friday signal — BUY: 5.39× weekly, month 2.09×, ladder rising; stop ₹291.46; charges ₹0.0116)
2020-06-15  GRANULES    BUY ₹9.82 at ₹216.75 (fresh Friday signal — BUY: 3.46× weekly, month 2.65×, ladder rising; stop ₹170.34; charges ₹0.0116)
2020-06-29  EIDPARRY    PYRAMID BUY ₹0.61 at ₹272.00 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹0.61 of ₹12.40); stop stays ₹249.19; charges ₹0.0007)
2020-07-07  IGL         SELL ₹8.36 at stop ₹208.81 (-15.7%, charges ₹0.0087) — the cash goes back to work at the next Friday screen
2020-07-13  GRANULES    PYRAMID BUY ₹8.36 at ₹236.20 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹8.36 of ₹10.69); stop stays ₹194.80; charges ₹0.0099)
2020-07-28  RELAXO      SELL ₹7.93 at stop ₹603.77 (-20.5%, charges ₹0.0082) — the cash goes back to work at the next Friday screen
2020-07-31  LLOYDSENGG  SELL ₹8.18 at stop ₹0.71 (-18.0%, charges ₹0.0085) — the cash goes back to work at the next Friday screen
2020-08-03  ZENTEC      BUY ₹11.38 at ₹58.80 (fresh Friday signal — ACCUMULATE: 4.33× weekly, month 4.91×, ladder rising; stop ₹42.67; charges ₹0.0135)
2020-08-10  RCF         PYRAMID BUY ₹4.74 at ₹51.75 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹4.74 of ₹11.46); stop stays ₹43.89; charges ₹0.0056)
2020-08-17  EIDPARRY    SELL ₹13.05 at stop ₹273.03 (+23.3%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2020-08-24  KIRLOSBROS  PYRAMID BUY ₹12.34 at ₹132.05 (2nd consecutive box jump — doubling the stake; stop stays ₹120.79; charges ₹0.0146)
2020-08-31  GRANULES    PYRAMID BUY ₹0.71 at ₹312.05 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹0.71 of ₹25.16); stop stays ₹286.95; charges ₹0.0008)
2020-08-31  GRANULES    SELL ₹23.77 at stop ₹286.95 (+26.0%, charges ₹0.0247) — the cash goes back to work at the next Friday screen
2020-08-31  ZENTEC      SELL ₹15.56 at stop ₹80.56 (+37.0%, charges ₹0.0161) — the cash goes back to work at the next Friday screen
2020-09-07  INDIAMART   BUY ₹11.65 at ₹2,124.50 (fresh Friday signal — BUY: 2.46× weekly, month 1.96×, ladder rising; stop ₹1,655.61; charges ₹0.0138)
2020-09-07  POLYMED     BUY ₹11.72 at ₹449.70 (fresh Friday signal — BUY: 2.13× weekly, month 2.66×, ladder rising; stop ₹372.40; charges ₹0.0139)
2020-09-08  KIRLOSBROS  SELL ₹22.53 at stop ₹120.79 (+1.3%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2020-09-09  RCF         SELL ₹14.32 at stop ₹45.84 (-2.7%, charges ₹0.0149) — the cash goes back to work at the next Friday screen
2020-09-14  ATGL        BUY ₹12.15 at ₹209.75 (fresh Friday signal — BUY: 1.66× weekly, month 1.67×, ladder rising; stop ₹159.58; charges ₹0.0144)
2020-09-14  GLAXO       BUY ₹12.10 at ₹1,675.00 (fresh Friday signal — BUY: 2.55× weekly, month 2.05×, ladder rising; stop ₹1,437.44; charges ₹0.0143)
2020-09-14  SCHAEFFLER  BUY ₹12.14 at ₹814.00 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 1.89×, ladder rising; stop ₹724.67; charges ₹0.0144)
2020-09-21  CAPLIPOINT  PYRAMID BUY ₹15.39 at ₹602.00 (2nd consecutive box jump — doubling the stake; stop stays ₹486.88; charges ₹0.0182)
2020-09-23  SCHAEFFLER  SELL ₹10.78 at stop ₹724.67 (-11.0%, charges ₹0.0112) — the cash goes back to work at the next Friday screen
2020-09-28  HCLTECH     BUY ₹11.81 at ₹838.40 (fresh Friday signal — BUY: 2.61× weekly, month 2.34×, ladder rising; stop ₹740.29; charges ₹0.0140)
2020-10-19  INDIAMART   SELL ₹12.67 at stop ₹2,315.62 (+9.0%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2020-10-26  ADVENZYMES  PYRAMID BUY ₹12.67 at ₹315.40 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹12.67 of ₹18.00); stop stays ₹292.33; charges ₹0.0150)
2020-10-30  CAPLIPOINT  SELL ₹25.43 at stop ₹498.06 (+1.1%, charges ₹0.0264) — the cash goes back to work at the next Friday screen
2020-11-02  GLAXO       SELL ₹10.39 at stop ₹1,441.55 (-13.9%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2020-11-02  JUSTDIAL    BUY ₹11.57 at ₹636.00 (fresh Friday signal — BUY: 2.86× weekly, month 2.30×, ladder rising; stop ₹383.80; charges ₹0.0137)
2020-11-02  KPRMILL     BUY ₹11.50 at ₹151.00 (fresh Friday signal — BUY: 2.37× weekly, month 3.11×, ladder rising; stop ₹108.58; charges ₹0.0136)
2020-11-03  ADVENZYMES  SELL ₹28.39 at stop ₹292.33 (+26.2%, charges ₹0.0294) — the cash goes back to work at the next Friday screen
2020-11-09  BORORENEW   BUY ₹11.70 at ₹99.70 (fresh Friday signal — ACCUMULATE: 1.74× weekly, month 1.65×, ladder rising; stop ₹77.16; charges ₹0.0139)
2020-11-17  ATGL        PYRAMID BUY ₹14.25 at ₹246.25 (2nd consecutive box jump — doubling the stake; stop stays ₹219.69; charges ₹0.0169)
2020-11-17  TRENT       BUY ₹12.57 at ₹755.00 (fresh Friday signal — ACCUMULATE: 3.32× weekly, month 1.93×, ladder rising; stop ₹551.90; charges ₹0.0149)
2020-12-01  KPRMILL     PYRAMID BUY ₹2.60 at ₹157.41 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹2.60 of ₹11.98); stop stays ₹148.69; charges ₹0.0031)
2020-12-21  ATGL        SELL ₹38.43 at stop ₹332.60 (+45.9%, charges ₹0.0399) — the cash goes back to work at the next Friday screen
2020-12-22  SYNGENE     SELL ₹14.93 at stop ₹562.40 (+50.4%, charges ₹0.0155) — the cash goes back to work at the next Friday screen
2020-12-28  GRAVITA     BUY ₹14.81 at ₹69.65 (fresh Friday signal — BUY: 2.45× weekly, month 4.29×, ladder rising; stop ₹46.41; charges ₹0.0175)
2020-12-28  HFCL        BUY ₹14.80 at ₹25.60 (fresh Friday signal — BUY: 2.33× weekly, month 3.93×, ladder rising; stop ₹19.05; charges ₹0.0175)
2020-12-28  HONAUT      BUY ₹14.87 at ₹38,887.75 (fresh Friday signal — BUY: 5.49× weekly, month 1.69×, ladder rising; stop ₹29,024.49; charges ₹0.0176)
2020-12-28  JKCEMENT    BUY ₹8.88 at ₹1,913.20 (fresh Friday signal — ACCUMULATE: 2.08× weekly, month 1.76×, ladder rising; stop ₹1,734.50; charges ₹0.0105)
2021-01-20  BORORENEW   SELL ₹29.00 at stop ₹247.59 (+148.3%, charges ₹0.0301) — the cash goes back to work at the next Friday screen
2021-01-25  HFCL        PYRAMID BUY ₹16.78 at ₹31.25 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹16.78 of ₹18.04); stop stays ₹28.12; charges ₹0.0199)
2021-01-25  JUSTDIAL    PYRAMID BUY ₹12.22 at ₹672.50 (2nd consecutive box jump — doubling the stake; stop stays ₹622.35; charges ₹0.0145)
2021-01-25  JUSTDIAL    SELL ₹22.59 at stop ₹622.35 (-4.9%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2021-01-28  HFCL        SELL ₹31.28 at stop ₹28.12 (-0.7%, charges ₹0.0324) — the cash goes back to work at the next Friday screen
2021-01-29  HCLTECH     SELL ₹13.04 at stop ₹928.05 (+10.7%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2021-01-29  JKCEMENT    SELL ₹9.55 at stop ₹2,061.50 (+7.8%, charges ₹0.0099) — the cash goes back to work at the next Friday screen
2021-01-29  TRENT       SELL ₹10.41 at stop ₹626.30 (-17.0%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2021-02-01  GAEL        BUY ₹15.01 at ₹71.47 (fresh Friday signal — ACCUMULATE: 2.70× weekly, month 3.63×, ladder rising; stop ₹62.70; charges ₹0.0178)
2021-02-01  KPRMILL     PYRAMID BUY ₹16.94 at ₹182.93 (2nd consecutive box jump — doubling the stake; stop stays ₹166.62; charges ₹0.0201)
2021-02-08  HONAUT      PYRAMID BUY ₹16.04 at ₹41,999.00 (2nd consecutive box jump — doubling the stake; stop stays ₹35,971.61; charges ₹0.0190)
2021-02-08  ITC         BUY ₹15.01 at ₹228.69 (fresh Friday signal — BUY: 2.38× weekly, month 1.68×, ladder rising; stop ₹184.60; charges ₹0.0178)
2021-02-08  MAHABANK    BUY ₹8.81 at ₹16.45 (fresh Friday signal — BUY: 2.17× weekly, month 3.37×, ladder rising; stop ₹9.50; charges ₹0.0104)
2021-02-08  UJJIVANSFB  BUY ₹15.05 at ₹37.15 (fresh Friday signal — ACCUMULATE: 2.60× weekly, month 2.19×, ladder rising; stop ₹32.12; charges ₹0.0178)
2021-02-23  GAEL        SELL ₹13.14 at stop ₹62.70 (-12.3%, charges ₹0.0136) — the cash goes back to work at the next Friday screen
2021-02-24  KPRMILL     SELL ₹30.81 at stop ₹166.62 (-0.5%, charges ₹0.0320) — the cash goes back to work at the next Friday screen
2021-02-26  ITC         SELL ₹12.93 at stop ₹197.41 (-13.7%, charges ₹0.0134) — the cash goes back to work at the next Friday screen
2021-03-01  GESHIP      BUY ₹11.34 at ₹315.90 (fresh Friday signal — BUY: 2.93× weekly, month 1.80×, ladder rising; stop ₹219.84; charges ₹0.0134)
2021-03-01  IOB         BUY ₹16.14 at ₹18.90 (fresh Friday signal — ACCUMULATE: 3.52× weekly, month 9.60×, ladder rising; stop ₹13.70; charges ₹0.0191)
2021-03-01  MAHABANK    PYRAMID BUY ₹13.48 at ₹25.20 (2nd consecutive box jump — doubling the stake; stop stays ₹18.37; charges ₹0.0160)
2021-03-01  RCF         BUY ₹15.92 at ₹80.00 (fresh Friday signal — BUY: 7.15× weekly, month 3.12×, ladder rising; stop ₹50.16; charges ₹0.0189)
2021-03-17  GRAVITA     SELL ₹20.39 at stop ₹96.13 (+38.0%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2021-03-17  RCF         SELL ₹15.72 at stop ₹79.16 (-1.1%, charges ₹0.0163) — the cash goes back to work at the next Friday screen
2021-03-18  UJJIVANSFB  SELL ₹12.98 at stop ₹32.12 (-13.5%, charges ₹0.0135) — the cash goes back to work at the next Friday screen
2021-03-19  MAHABANK    SELL ₹19.62 at stop ₹18.37 (-11.8%, charges ₹0.0204) — the cash goes back to work at the next Friday screen
2021-03-22  DEEPAKFERT  BUY ₹14.82 at ₹237.00 (fresh Friday signal — BUY: 2.43× weekly, month 1.82×, ladder rising; stop ₹184.78; charges ₹0.0176)
2021-03-22  HONAUT      SELL ₹31.96 at stop ₹41,911.15 (+3.6%, charges ₹0.0332) — the cash goes back to work at the next Friday screen
2021-03-22  KEI         BUY ₹14.74 at ₹522.00 (fresh Friday signal — BUY: 5.22× weekly, month 1.54×, ladder rising; stop ₹436.67; charges ₹0.0175)
2021-03-22  WELSPUNLIV  BUY ₹14.82 at ₹81.45 (fresh Friday signal — BUY: 3.57× weekly, month 2.45×, ladder rising; stop ₹67.45; charges ₹0.0176)
2021-03-30  KPITTECH    BUY ₹14.68 at ₹182.00 (fresh Friday signal — BUY: 1.71× weekly, month 2.75×, ladder rising; stop ₹136.62; charges ₹0.0174)
2021-03-30  POLYMED     PYRAMID BUY ₹21.23 at ₹815.45 (2nd consecutive box jump — doubling the stake; stop stays ₹719.96; charges ₹0.0252)
2021-04-01  TAX         FY2021 settled: ₹8.2011 paid (STCG ₹41.01 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2021-04-05  AUBANK      BUY ₹12.19 at ₹631.00 (fresh Friday signal — ACCUMULATE: 3.80× weekly, month 2.02×, ladder rising; stop ₹533.06; charges ₹0.0144)
2021-04-12  AUBANK      SELL ₹10.28 at stop ₹533.06 (-15.5%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2021-04-12  GESHIP      SELL ₹10.41 at stop ₹290.70 (-8.0%, charges ₹0.0108) — the cash goes back to work at the next Friday screen
2021-04-19  KPRMILL     BUY ₹13.82 at ₹236.00 (fresh Friday signal — BUY: 2.36× weekly, month 1.58×, ladder rising; stop ₹192.07; charges ₹0.0164)
2021-04-28  IOB         SELL ₹12.62 at stop ₹14.82 (-21.6%, charges ₹0.0131) — the cash goes back to work at the next Friday screen
2021-05-03  MARKSANS    BUY ₹15.09 at ₹70.95 (fresh Friday signal — ACCUMULATE: 3.13× weekly, month 3.97×, ladder rising; stop ₹64.12; charges ₹0.0179)
2021-05-10  KEI         PYRAMID BUY ₹4.40 at ₹528.50 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹4.40 of ₹14.91); stop stays ₹485.02; charges ₹0.0052)
2021-06-14  POLYMED     SELL ₹49.39 at stop ₹950.00 (+50.2%, charges ₹0.0512) — the cash goes back to work at the next Friday screen
2021-06-21  JWL         BUY ₹17.39 at ₹30.80 (fresh Friday signal — BUY: 6.73× weekly, month 3.20×, ladder rising; stop ₹18.23; charges ₹0.0206)
2021-06-21  KEI         PYRAMID BUY ₹24.92 at ₹682.20 (2nd consecutive box jump — doubling the stake; stop stays ₹608.00; charges ₹0.0295)
2021-06-28  MARKSANS    PYRAMID BUY ₹7.08 at ₹87.50 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹7.08 of ₹18.59); stop stays ₹76.87; charges ₹0.0084)
2021-08-10  MARKSANS    SELL ₹22.60 at stop ₹77.14 (+2.2%, charges ₹0.0234) — the cash goes back to work at the next Friday screen
2021-08-10  WELSPUNLIV  SELL ₹22.62 at stop ₹124.64 (+53.0%, charges ₹0.0235) — the cash goes back to work at the next Friday screen
2021-08-11  KPRMILL     SELL ₹20.59 at stop ₹352.48 (+49.4%, charges ₹0.0214) — the cash goes back to work at the next Friday screen
2021-08-16  GABRIEL     BUY ₹19.46 at ₹149.30 (fresh Friday signal — BUY: 2.50× weekly, month 3.57×, ladder rising; stop ₹118.77; charges ₹0.0231)
2021-08-16  TATAINVEST  BUY ₹19.50 at ₹130.81 (fresh Friday signal — BUY: 8.45× weekly, month 4.82×, ladder rising; stop ₹103.11; charges ₹0.0231)
2021-08-23  GRAVITA     BUY ₹18.24 at ₹188.60 (fresh Friday signal — BUY: 2.16× weekly, month 1.88×, ladder rising; stop ₹151.95; charges ₹0.0216)
2021-08-23  JWL         SELL ₹17.14 at stop ₹30.42 (-1.2%, charges ₹0.0178) — the cash goes back to work at the next Friday screen
2021-09-06  NHPC        BUY ₹19.17 at ₹27.90 (fresh Friday signal — BUY: 5.07× weekly, month 1.59×, ladder rising; stop ₹24.13; charges ₹0.0227)
2021-09-13  KEI         PYRAMID BUY ₹6.57 at ₹796.70 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹6.57 of ₹58.17); stop stays ₹718.20; charges ₹0.0078)
2021-10-22  KEI         SELL ₹69.24 at stop ₹853.10 (+37.1%, charges ₹0.0718) — the cash goes back to work at the next Friday screen
2021-10-25  LTM         BUY ₹20.43 at ₹6,555.00 (fresh Friday signal — BUY: 4.63× weekly, month 1.86×, ladder rising; stop ₹5,353.77; charges ₹0.0242)
2021-10-25  NHPC        PYRAMID BUY ₹22.58 at ₹32.90 (2nd consecutive box jump — doubling the stake; stop stays ₹27.60; charges ₹0.0268)
2021-11-01  PERSISTENT  BUY ₹20.55 at ₹1,977.15 (fresh Friday signal — ACCUMULATE: 1.71× weekly, month 2.09×, ladder rising; stop ₹1,728.75; charges ₹0.0243)
2021-11-11  DEEPAKFERT  SELL ₹24.07 at stop ₹385.70 (+62.7%, charges ₹0.0250) — the cash goes back to work at the next Friday screen
2021-11-15  GRAVITA     PYRAMID BUY ₹21.23 at ₹219.80 (2nd consecutive box jump — doubling the stake; stop stays ₹197.03; charges ₹0.0252)
2021-11-22  GRAVITA     SELL ₹38.01 at stop ₹197.03 (-3.5%, charges ₹0.0394) — the cash goes back to work at the next Friday screen
2021-11-22  NHPC        PYRAMID BUY ₹8.51 at ₹32.90 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹8.51 of ₹45.14); stop stays ₹30.11; charges ₹0.0101)
2021-11-26  TATAINVEST  SELL ₹21.37 at stop ₹143.65 (+9.8%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2021-11-29  KPITTECH    PYRAMID BUY ₹36.65 at ₹455.00 (2nd consecutive box jump — doubling the stake; stop stays ₹398.63; charges ₹0.0434)
2021-11-29  LTM         PYRAMID BUY ₹20.33 at ₹6,530.00 (2nd consecutive box jump — doubling the stake; stop stays ₹6,270.00; charges ₹0.0241)
2021-11-29  NHPC        SELL ₹49.04 at stop ₹30.11 (-2.2%, charges ₹0.0509) — the cash goes back to work at the next Friday screen
2021-12-06  BSE         BUY ₹21.06 at ₹209.99 (fresh Friday signal — BUY: 4.20× weekly, month 1.77×, ladder rising; stop ₹158.85; charges ₹0.0250)
2021-12-06  CHAMBLFERT  BUY ₹21.01 at ₹407.45 (fresh Friday signal — ACCUMULATE: 3.11× weekly, month 1.86×, ladder rising; stop ₹274.46; charges ₹0.0249)
2021-12-20  KPITTECH    SELL ₹73.80 at stop ₹458.85 (+44.1%, charges ₹0.0766) — the cash goes back to work at the next Friday screen
2021-12-27  BSOFT       BUY ₹20.99 at ₹529.00 (fresh Friday signal — BUY: 2.23× weekly, month 2.14×, ladder rising; stop ₹424.65; charges ₹0.0249)
2021-12-27  PERSISTENT  PYRAMID BUY ₹24.00 at ₹2,311.50 (2nd consecutive box jump — doubling the stake; stop stays ₹2,067.34; charges ₹0.0284)
2021-12-27  UNOMINDA    BUY ₹20.94 at ₹590.00 (fresh Friday signal — BUY: 3.66× weekly, month 2.64×, ladder rising; stop ₹464.60; charges ₹0.0248)
2022-01-03  GABRIEL     PYRAMID BUY ₹17.23 at ₹140.00 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹17.23 of ₹18.23); stop stays ₹125.40; charges ₹0.0204)
2022-01-07  UNOMINDA    SELL ₹19.27 at stop ₹544.21 (-7.8%, charges ₹0.0200) — the cash goes back to work at the next Friday screen
2022-01-10  AFFLE       BUY ₹19.27 at ₹1,307.00 (fresh Friday signal — BUY: 4.57× weekly, month 1.57×, ladder rising; stop ₹955.80; charges ₹0.0228)
2022-01-24  LTM         SELL ₹38.98 at stop ₹6,270.00 (-4.2%, charges ₹0.0404) — the cash goes back to work at the next Friday screen
2022-01-24  PERSISTENT  SELL ₹42.85 at stop ₹2,067.34 (-3.6%, charges ₹0.0445) — the cash goes back to work at the next Friday screen
2022-01-25  AFFLE       SELL ₹17.75 at stop ₹1,206.50 (-7.7%, charges ₹0.0184) — the cash goes back to work at the next Friday screen
2022-01-31  SHARDACROP  BUY ₹19.60 at ₹586.70 (fresh Friday signal — BUY: 19.48× weekly, month 6.26×, ladder rising; stop ₹342.00; charges ₹0.0232)
2022-02-07  CCL         BUY ₹19.72 at ₹503.55 (fresh Friday signal — BUY: 4.07× weekly, month 1.58×, ladder rising; stop ₹408.60; charges ₹0.0234)
2022-02-11  SHARDACROP  SELL ₹18.17 at stop ₹545.30 (-7.1%, charges ₹0.0189) — the cash goes back to work at the next Friday screen
2022-02-14  BSOFT       SELL ₹16.81 at stop ₹424.65 (-19.7%, charges ₹0.0174) — the cash goes back to work at the next Friday screen
2022-02-14  GABRIEL     SELL ₹31.71 at stop ₹125.40 (-13.4%, charges ₹0.0329) — the cash goes back to work at the next Friday screen
2022-02-14  GNFC        BUY ₹18.68 at ₹553.00 (fresh Friday signal — BUY: 7.50× weekly, month 2.65×, ladder rising; stop ₹414.87; charges ₹0.0221)
2022-02-21  ADANIPOWER  BUY ₹18.77 at ₹26.40 (fresh Friday signal — BUY: 8.22× weekly, month 2.70×, ladder rising; stop ₹18.02; charges ₹0.0222)
2022-02-21  CGCL        BUY ₹18.60 at ₹567.08 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.06×, ladder rising; stop ₹507.72; charges ₹0.0220)
2022-02-24  CCL         SELL ₹17.26 at stop ₹441.75 (-12.3%, charges ₹0.0179) — the cash goes back to work at the next Friday screen
2022-02-24  CHAMBLFERT  SELL ₹18.21 at stop ₹353.85 (-13.2%, charges ₹0.0189) — the cash goes back to work at the next Friday screen
2022-04-01  TAX         FY2022 settled: ₹10.6462 paid (STCG ₹53.23 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2022-04-04  RCF         BUY ₹20.54 at ₹96.40 (fresh Friday signal — BUY: 8.32× weekly, month 2.52×, ladder rising; stop ₹74.19; charges ₹0.0243)
2022-04-04  SPLPETRO    BUY ₹20.64 at ₹475.00 (fresh Friday signal — BUY: 4.41× weekly, month 2.84×, ladder rising; stop ₹398.29; charges ₹0.0245)
2022-04-11  BLS         BUY ₹20.90 at ₹82.50 (fresh Friday signal — BUY: 8.78× weekly, month 1.73×, ladder rising; stop ₹54.82; charges ₹0.0248)
2022-04-11  MINDACORP   BUY ₹20.88 at ₹230.05 (fresh Friday signal — BUY: 2.10× weekly, month 1.60×, ladder rising; stop ₹186.63; charges ₹0.0247)
2022-04-18  LTFOODS     BUY ₹12.79 at ₹91.70 (fresh Friday signal — BUY: 12.80× weekly, month 1.79×, ladder rising; stop ₹73.86; charges ₹0.0152)
2022-05-04  RCF         SELL ₹19.80 at stop ₹93.15 (-3.4%, charges ₹0.0205) — the cash goes back to work at the next Friday screen
2022-05-06  GNFC        SELL ₹26.69 at stop ₹792.16 (+43.2%, charges ₹0.0277) — the cash goes back to work at the next Friday screen
2022-05-09  MRPL        BUY ₹20.67 at ₹78.00 (fresh Friday signal — BUY: 2.47× weekly, month 7.89×, ladder rising; stop ₹58.41; charges ₹0.0245)
2022-05-10  BSE         SELL ₹25.61 at stop ₹255.87 (+21.8%, charges ₹0.0266) — the cash goes back to work at the next Friday screen
2022-05-11  LTFOODS     SELL ₹10.28 at stop ₹73.86 (-19.5%, charges ₹0.0107) — the cash goes back to work at the next Friday screen
2022-05-11  MINDACORP   SELL ₹16.90 at stop ₹186.63 (-18.9%, charges ₹0.0175) — the cash goes back to work at the next Friday screen
2022-05-16  VBL         BUY ₹19.69 at ₹146.67 (fresh Friday signal — ACCUMULATE: 1.77× weekly, month 2.79×, ladder rising; stop ₹130.85; charges ₹0.0233)
2022-05-23  ACC         BUY ₹21.32 at ₹2,260.00 (fresh Friday signal — ACCUMULATE: 2.13× weekly, month 1.55×, ladder rising; stop ₹1,994.10; charges ₹0.0253)
2022-05-24  SPLPETRO    SELL ₹18.40 at stop ₹424.27 (-10.7%, charges ₹0.0191) — the cash goes back to work at the next Friday screen
2022-06-06  MRPL        PYRAMID BUY ₹23.38 at ₹88.35 (2nd consecutive box jump — doubling the stake; stop stays ₹69.61; charges ₹0.0277)
2022-06-13  ELECON      BUY ₹21.49 at ₹122.47 (fresh Friday signal — BUY: 4.00× weekly, month 1.65×, ladder rising; stop ₹85.59; charges ₹0.0255)
2022-06-20  BLS         PYRAMID BUY ₹11.13 at ₹106.12 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹11.13 of ₹26.86); stop stays ₹83.17; charges ₹0.0132)
2022-07-06  MRPL        SELL ₹36.79 at stop ₹69.61 (-16.3%, charges ₹0.0382) — the cash goes back to work at the next Friday screen
2022-07-11  ELECON      PYRAMID BUY ₹25.76 at ₹147.00 (2nd consecutive box jump — doubling the stake; stop stays ₹120.65; charges ₹0.0305)
2022-08-08  BLS         PYRAMID BUY ₹11.03 at ₹118.25 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹11.03 of ₹42.31); stop stays ₹110.67; charges ₹0.0131)
2022-08-22  VBL         SELL ₹25.25 at stop ₹188.52 (+28.5%, charges ₹0.0262) — the cash goes back to work at the next Friday screen
2022-08-23  BLS         SELL ₹49.86 at stop ₹110.67 (+16.0%, charges ₹0.0517) — the cash goes back to work at the next Friday screen
2022-08-29  ACC         PYRAMID BUY ₹21.43 at ₹2,274.00 (2nd consecutive box jump — doubling the stake; stop stays ₹2,151.37; charges ₹0.0254)
2022-08-29  HOMEFIRST   BUY ₹23.88 at ₹944.95 (fresh Friday signal — ACCUMULATE: 3.67× weekly, month 2.49×, ladder rising; stop ₹849.35; charges ₹0.0283)
2022-08-29  KALYANKJIL  BUY ₹23.91 at ₹78.10 (fresh Friday signal — BUY: 9.54× weekly, month 2.93×, ladder rising; stop ₹65.55; charges ₹0.0283)
2022-09-14  HOMEFIRST   SELL ₹21.42 at stop ₹849.35 (-10.1%, charges ₹0.0222) — the cash goes back to work at the next Friday screen
2022-09-19  KALYANKJIL  PYRAMID BUY ₹27.31 at ₹95.10 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹27.31 of ₹29.08); stop stays ₹76.00; charges ₹0.0324)
2022-10-14  ADANIPOWER  SELL ₹47.38 at stop ₹66.80 (+153.0%, charges ₹0.0491) — the cash goes back to work at the next Friday screen
2022-10-17  APOLLO      BUY ₹23.30 at ₹24.00 (fresh Friday signal — BUY: 6.98× weekly, month 4.78×, ladder rising; stop ₹14.17; charges ₹0.0276)
2022-10-24  KALYANKJIL  PYRAMID BUY ₹24.07 at ₹101.85 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹24.07 of ₹60.36); stop stays ₹89.78; charges ₹0.0285)
2022-11-22  KALYANKJIL  SELL ₹78.26 at stop ₹94.53 (+4.2%, charges ₹0.0812) — the cash goes back to work at the next Friday screen
2022-11-28  IRFC        BUY ₹25.16 at ₹32.00 (fresh Friday signal — BUY: 9.02× weekly, month 13.28×, ladder rising; stop ₹23.09; charges ₹0.0298)
2022-11-28  MAHABANK    BUY ₹25.28 at ₹27.60 (fresh Friday signal — BUY: 8.71× weekly, month 8.20×, ladder rising; stop ₹21.47; charges ₹0.0300)
2022-11-28  UCOBANK     BUY ₹25.21 at ₹21.05 (fresh Friday signal — BUY: 13.59× weekly, month 16.04×, ladder rising; stop ₹13.59; charges ₹0.0299)
2022-12-12  APOLLO      PYRAMID BUY ₹2.60 at ₹25.80 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹2.60 of ₹25.03); stop stays ₹24.42; charges ₹0.0031)
2022-12-21  ELECON      SELL ₹70.84 at stop ₹202.49 (+50.3%, charges ₹0.0735) — the cash goes back to work at the next Friday screen
2022-12-23  ACC         SELL ₹46.38 at stop ₹2,465.15 (+8.7%, charges ₹0.0481) — the cash goes back to work at the next Friday screen
2022-12-23  IRFC        SELL ₹22.13 at stop ₹28.20 (-11.9%, charges ₹0.0230) — the cash goes back to work at the next Friday screen
2022-12-26  APOLLO      SELL ₹26.12 at stop ₹24.42 (+1.1%, charges ₹0.0271) — the cash goes back to work at the next Friday screen
2023-01-02  GICRE       BUY ₹25.40 at ₹179.20 (fresh Friday signal — ACCUMULATE: 2.52× weekly, month 11.13×, ladder rising; stop ₹137.57; charges ₹0.0301)
2023-01-02  IOB         BUY ₹25.36 at ₹32.40 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 28.89×, ladder rising; stop ₹21.23; charges ₹0.0300)
2023-01-02  JSL         BUY ₹25.72 at ₹241.00 (fresh Friday signal — BUY: 2.24× weekly, month 2.14×, ladder rising; stop ₹192.61; charges ₹0.0305)
2023-01-02  LLOYDSENGG  BUY ₹25.52 at ₹15.63 (fresh Friday signal — ACCUMULATE: 2.36× weekly, month 2.74×, ladder rising; stop ₹10.86; charges ₹0.0302)
2023-01-02  UCOBANK     PYRAMID BUY ₹38.04 at ₹31.80 (2nd consecutive box jump — doubling the stake; stop stays ₹23.46; charges ₹0.0451)
2023-01-02  YESBANK     BUY ₹25.31 at ₹20.85 (fresh Friday signal — ACCUMULATE: 2.89× weekly, month 3.19×, ladder rising; stop ₹15.00; charges ₹0.0300)
2023-02-01  GICRE       SELL ₹23.72 at stop ₹167.72 (-6.4%, charges ₹0.0246) — the cash goes back to work at the next Friday screen
2023-02-06  JINDALSAW   BUY ₹23.84 at ₹65.22 (fresh Friday signal — BUY: 2.71× weekly, month 3.60×, ladder rising; stop ₹51.25; charges ₹0.0282)
2023-02-07  LLOYDSENGG  SELL ₹31.40 at stop ₹19.27 (+23.3%, charges ₹0.0326) — the cash goes back to work at the next Friday screen
2023-02-27  JSL         PYRAMID BUY ₹28.31 at ₹265.50 (2nd consecutive box jump — doubling the stake; stop stays ₹235.03; charges ₹0.0335)
2023-03-08  CGCL        SELL ₹21.82 at stop ₹666.82 (+17.6%, charges ₹0.0226) — the cash goes back to work at the next Friday screen
2023-03-13  YESBANK     SELL ₹18.58 at stop ₹15.34 (-26.4%, charges ₹0.0193) — the cash goes back to work at the next Friday screen
2023-03-20  ANURAS      BUY ₹22.99 at ₹755.90 (fresh Friday signal — ACCUMULATE: 3.74× weekly, month 2.60×, ladder rising; stop ₹691.46; charges ₹0.0272)
2023-03-20  IOB         SELL ₹17.32 at stop ₹22.18 (-31.5%, charges ₹0.0180) — the cash goes back to work at the next Friday screen
2023-03-20  SONATSOFTW  BUY ₹20.49 at ₹397.50 (fresh Friday signal — BUY: 2.89× weekly, month 5.76×, ladder rising; stop ₹357.20; charges ₹0.0243)
2023-03-27  JINDALSAW   SELL ₹24.77 at stop ₹67.92 (+4.1%, charges ₹0.0257) — the cash goes back to work at the next Friday screen
2023-03-27  MAHABANK    PYRAMID BUY ₹17.32 at ₹24.40 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹17.32 of ₹22.32); stop stays ₹22.36; charges ₹0.0205)
2023-03-27  UCOBANK     SELL ₹56.03 at stop ₹23.46 (-11.2%, charges ₹0.0581) — the cash goes back to work at the next Friday screen
2023-03-29  SONATSOFTW  SELL ₹19.11 at stop ₹371.45 (-6.6%, charges ₹0.0198) — the cash goes back to work at the next Friday screen
2023-04-03  HAL         BUY ₹21.96 at ₹1,380.00 (fresh Friday signal — ACCUMULATE: 1.57× weekly, month 2.04×, ladder rising; stop ₹1,171.71; charges ₹0.0260)
2023-04-03  TAX         FY2023 settled: ₹9.4155 paid (STCG ₹45.04 @20%, LTCG ₹3.27 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2023-04-10  KIRLOSBROS  BUY ₹22.09 at ₹425.00 (fresh Friday signal — BUY: 1.86× weekly, month 2.34×, ladder rising; stop ₹357.44; charges ₹0.0262)
2023-04-10  KSB         BUY ₹22.16 at ₹451.00 (fresh Friday signal — BUY: 2.21× weekly, month 2.24×, ladder rising; stop ₹372.21; charges ₹0.0263)
2023-04-13  JSL         SELL ₹54.71 at stop ₹256.98 (+1.5%, charges ₹0.0567) — the cash goes back to work at the next Friday screen
2023-04-24  MARKSANS    BUY ₹22.77 at ₹78.00 (fresh Friday signal — ACCUMULATE: 1.64× weekly, month 1.51×, ladder rising; stop ₹71.87; charges ₹0.0270)
2023-04-24  ZFCVINDIA   BUY ₹22.76 at ₹1,697.50 (fresh Friday signal — ACCUMULATE: 7.38× weekly, month 1.55×, ladder rising; stop ₹1,561.17; charges ₹0.0270)
2023-04-26  KIRLOSBROS  SELL ₹20.95 at stop ₹403.85 (-5.0%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2023-05-02  ASHAPURMIN  BUY ₹23.00 at ₹143.10 (fresh Friday signal — BUY: 2.05× weekly, month 2.10×, ladder rising; stop ₹123.50; charges ₹0.0273)
2023-05-02  REFEX       BUY ₹23.08 at ₹65.32 (fresh Friday signal — BUY: 4.73× weekly, month 1.57×, ladder rising; stop ₹54.53; charges ₹0.0274)
2023-05-15  ANURAS      PYRAMID BUY ₹8.32 at ₹1,169.80 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹8.32 of ₹35.54); stop stays ₹1,007.67; charges ₹0.0099)
2023-05-22  MARKSANS    SELL ₹20.94 at stop ₹71.87 (-7.9%, charges ₹0.0217) — the cash goes back to work at the next Friday screen
2023-05-29  ASHAPURMIN  PYRAMID BUY ₹20.85 at ₹129.90 (2nd consecutive box jump — doubling the stake; stop stays ₹134.24; charges ₹0.0247)
2023-05-29  ASHAPURMIN  SELL ₹43.03 at stop ₹134.24 (-1.7%, charges ₹0.0446) — the cash goes back to work at the next Friday screen
2023-06-05  HAL         PYRAMID BUY ₹25.30 at ₹1,591.88 (2nd consecutive box jump — doubling the stake; stop stays ₹1,415.36; charges ₹0.0300)
2023-06-05  REFEX       PYRAMID BUY ₹17.81 at ₹105.24 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹17.81 of ₹37.15); stop stays ₹87.60; charges ₹0.0211)
2023-06-15  MAHABANK    SELL ₹45.09 at stop ₹27.79 (+6.1%, charges ₹0.0468) — the cash goes back to work at the next Friday screen
2023-06-19  HEG         BUY ₹19.78 at ₹317.84 (fresh Friday signal — BUY: 5.90× weekly, month 3.83×, ladder rising; stop ₹211.53; charges ₹0.0234)
2023-06-19  MEDANTA     BUY ₹25.31 at ₹651.00 (fresh Friday signal — BUY: 6.42× weekly, month 1.67×, ladder rising; stop ₹548.15; charges ₹0.0300)
2023-07-03  ANURAS      SELL ₹37.74 at stop ₹1,007.67 (+20.8%, charges ₹0.0391) — the cash goes back to work at the next Friday screen
2023-07-10  CEATLTD     BUY ₹25.44 at ₹2,408.00 (fresh Friday signal — BUY: 4.55× weekly, month 2.41×, ladder rising; stop ₹1,892.78; charges ₹0.0301)
2023-07-12  KSB         SELL ₹19.99 at stop ₹407.74 (-9.6%, charges ₹0.0207) — the cash goes back to work at the next Friday screen
2023-07-17  ANANDRATHI  BUY ₹26.63 at ₹265.70 (fresh Friday signal — BUY: 14.43× weekly, month 2.32×, ladder rising; stop ₹199.61; charges ₹0.0315)
2023-07-24  MEDANTA     PYRAMID BUY ₹5.66 at ₹728.95 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹5.66 of ₹28.30); stop stays ₹647.28; charges ₹0.0067)
2023-08-11  REFEX       SELL ₹63.46 at stop ₹121.69 (+55.5%, charges ₹0.0658) — the cash goes back to work at the next Friday screen
2023-08-14  CEATLTD     SELL ₹23.66 at stop ₹2,244.85 (-6.8%, charges ₹0.0245) — the cash goes back to work at the next Friday screen
2023-08-14  HAL         PYRAMID BUY ₹60.13 at ₹1,892.42 (2nd consecutive box jump — doubling the stake; stop stays ₹1,758.24; charges ₹0.0712)
2023-08-14  ZFCVINDIA   PYRAMID BUY ₹3.33 at ₹2,230.00 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹3.33 of ₹29.86); stop stays ₹2,046.36; charges ₹0.0039)
2023-08-21  ANANDRATHI  PYRAMID BUY ₹23.66 at ₹347.99 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹23.66 of ₹34.83); stop stays ₹305.19; charges ₹0.0280)
2023-10-23  HEG         SELL ₹20.41 at stop ₹328.78 (+3.4%, charges ₹0.0212) — the cash goes back to work at the next Friday screen
2023-10-25  HAL         SELL ₹116.77 at stop ₹1,840.70 (+9.0%, charges ₹0.1211) — the cash goes back to work at the next Friday screen
2023-10-30  ANGELONE    BUY ₹29.18 at ₹253.50 (fresh Friday signal — BUY: 1.84× weekly, month 2.75×, ladder rising; stop ₹194.37; charges ₹0.0346)
2023-10-30  CUPID       BUY ₹29.14 at ₹6.05 (fresh Friday signal — BUY: 1.86× weekly, month 5.68×, ladder rising; stop ₹3.66; charges ₹0.0345)
2023-10-30  SHAREINDIA  BUY ₹29.16 at ₹300.00 (fresh Friday signal — BUY: 3.44× weekly, month 2.62×, ladder rising; stop ₹261.25; charges ₹0.0346)
2023-11-06  APOLLO      BUY ₹31.04 at ₹95.90 (fresh Friday signal — BUY: 5.38× weekly, month 5.92×, ladder rising; stop ₹60.83; charges ₹0.0368)
2023-11-06  TSFINV      BUY ₹18.66 at ₹144.75 (fresh Friday signal — BUY: 3.35× weekly, month 1.95×, ladder rising; stop ₹109.72; charges ₹0.0221)
2023-12-20  TSFINV      SELL ₹18.71 at stop ₹145.40 (+0.4%, charges ₹0.0194) — the cash goes back to work at the next Friday screen
2023-12-26  CUPID       PYRAMID BUY ₹18.71 at ₹9.40 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹18.71 of ₹45.22); stop stays ₹8.10; charges ₹0.0222)
2024-01-23  ANGELONE    SELL ₹34.10 at stop ₹296.88 (+17.1%, charges ₹0.0354) — the cash goes back to work at the next Friday screen
2024-01-29  RITES       BUY ₹34.10 at ₹342.50 (fresh Friday signal — BUY: 11.32× weekly, month 2.99×, ladder rising; stop ₹240.21; charges ₹0.0404)
2024-02-02  ZFCVINDIA   SELL ₹36.78 at stop ₹2,473.96 (+41.3%, charges ₹0.0382) — the cash goes back to work at the next Friday screen
2024-02-05  GODFRYPHLP  BUY ₹36.78 at ₹848.30 (fresh Friday signal — BUY: 10.17× weekly, month 1.74×, ladder rising; stop ₹653.92; charges ₹0.0436)
2024-02-13  APOLLO      SELL ₹36.20 at stop ₹112.10 (+16.9%, charges ₹0.0375) — the cash goes back to work at the next Friday screen
2024-02-19  ANANDRATHI  PYRAMID BUY ₹36.20 at ₹927.25 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹36.20 of ₹155.79); stop stays ₹770.07; charges ₹0.0429)
2024-03-06  MEDANTA     SELL ₹57.02 at stop ₹1,225.50 (+84.6%, charges ₹0.0592) — the cash goes back to work at the next Friday screen
2024-03-06  SHAREINDIA  SELL ₹34.65 at stop ₹357.20 (+19.1%, charges ₹0.0359) — the cash goes back to work at the next Friday screen
2024-03-11  BHEL        BUY ₹37.46 at ₹259.10 (fresh Friday signal — BUY: 3.01× weekly, month 1.67×, ladder rising; stop ₹188.78; charges ₹0.0444)
2024-03-11  SOLARINDS   BUY ₹54.21 at ₹7,564.00 (fresh Friday signal — ACCUMULATE: 4.35× weekly, month 1.71×, ladder rising; stop ₹5,332.29; charges ₹0.0642)
2024-03-13  RITES       SELL ₹31.23 at stop ₹314.37 (-8.2%, charges ₹0.0324) — the cash goes back to work at the next Friday screen
2024-03-18  INDIGO      BUY ₹31.23 at ₹3,200.00 (fresh Friday signal — ACCUMULATE: 4.67× weekly, month 1.67×, ladder rising; stop ₹2,834.99; charges ₹0.0370)
2024-03-27  ANANDRATHI  SELL ₹178.38 at stop ₹862.65 (+106.7%, charges ₹0.1850) — the cash goes back to work at the next Friday screen
2024-04-01  DMART       BUY ₹48.22 at ₹4,570.00 (fresh Friday signal — BUY: 3.09× weekly, month 1.56×, ladder rising; stop ₹3,695.50; charges ₹0.0571)
2024-04-01  SHRIRAMFIN  BUY ₹48.11 at ₹474.20 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 1.95×, ladder rising; stop ₹424.70; charges ₹0.0570)
2024-04-01  TAX         FY2024 settled: ₹35.5148 paid (STCG ₹177.57 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2024-04-08  HGINFRA     BUY ₹46.54 at ₹1,097.70 (fresh Friday signal — BUY: 4.70× weekly, month 2.03×, ladder rising; stop ₹812.30; charges ₹0.0551)
2024-05-31  DMART       SELL ₹45.51 at stop ₹4,322.83 (-5.4%, charges ₹0.0472) — the cash goes back to work at the next Friday screen
2024-06-03  CAMPUS      BUY ₹45.51 at ₹286.00 (fresh Friday signal — BUY: 10.34× weekly, month 2.79×, ladder rising; stop ₹236.55; charges ₹0.0539)
2024-06-04  BHEL        SELL ₹36.31 at stop ₹251.68 (-2.9%, charges ₹0.0377) — the cash goes back to work at the next Friday screen
2024-06-04  CUPID       SELL ₹120.69 at stop ₹17.77 (+152.8%, charges ₹0.1252) — the cash goes back to work at the next Friday screen
2024-06-04  HGINFRA     SELL ₹53.93 at stop ₹1,274.90 (+16.1%, charges ₹0.0559) — the cash goes back to work at the next Friday screen
2024-06-04  SHRIRAMFIN  SELL ₹44.72 at stop ₹441.77 (-6.8%, charges ₹0.0464) — the cash goes back to work at the next Friday screen
2024-06-04  SOLARINDS   SELL ₹57.07 at stop ₹7,980.95 (+5.5%, charges ₹0.0592) — the cash goes back to work at the next Friday screen
2024-06-10  ADANIPOWER  BUY ₹45.82 at ₹156.60 (fresh Friday signal — BUY: 7.81× weekly, month 1.77×, ladder rising; stop ₹126.55; charges ₹0.0543)
2024-06-10  DABUR       BUY ₹45.62 at ₹604.20 (fresh Friday signal — BUY: 3.89× weekly, month 2.59×, ladder rising; stop ₹509.91; charges ₹0.0541)
2024-06-10  ENDURANCE   BUY ₹38.04 at ₹2,439.90 (fresh Friday signal — BUY: 2.56× weekly, month 2.14×, ladder rising; stop ₹1,964.12; charges ₹0.0451)
2024-06-10  FIEMIND     BUY ₹45.97 at ₹1,320.00 (fresh Friday signal — BUY: 11.07× weekly, month 1.60×, ladder rising; stop ₹1,064.00; charges ₹0.0545)
2024-06-10  HINDUNILVR  BUY ₹45.80 at ₹2,579.00 (fresh Friday signal — BUY: 2.72× weekly, month 1.58×, ladder rising; stop ₹2,201.72; charges ₹0.0543)
2024-06-10  NCC         BUY ₹45.74 at ₹327.60 (fresh Friday signal — BUY: 2.80× weekly, month 1.63×, ladder rising; stop ₹260.92; charges ₹0.0542)
2024-06-10  UNOMINDA    BUY ₹45.74 at ₹970.00 (fresh Friday signal — BUY: 4.24× weekly, month 2.61×, ladder rising; stop ₹769.64; charges ₹0.0542)
2024-07-19  UNOMINDA    SELL ₹46.19 at stop ₹981.87 (+1.2%, charges ₹0.0479) — the cash goes back to work at the next Friday screen
2024-07-22  FIEMIND     PYRAMID BUY ₹45.18 at ₹1,299.00 (2nd consecutive box jump — doubling the stake; stop stays ₹1,257.56; charges ₹0.0535)
2024-07-23  FIEMIND     SELL ₹87.34 at stop ₹1,257.56 (-4.0%, charges ₹0.0906) — the cash goes back to work at the next Friday screen
2024-07-23  NCC         SELL ₹41.49 at stop ₹297.87 (-9.1%, charges ₹0.0430) — the cash goes back to work at the next Friday screen
2024-07-29  AVANTIFEED  BUY ₹46.17 at ₹697.65 (fresh Friday signal — BUY: 9.75× weekly, month 3.97×, ladder rising; stop ₹558.65; charges ₹0.0547)
2024-07-29  KSCL        BUY ₹37.45 at ₹1,068.40 (fresh Friday signal — BUY: 5.64× weekly, month 1.78×, ladder rising; stop ₹875.38; charges ₹0.0444)
2024-07-29  THYROCARE   BUY ₹46.22 at ₹261.67 (fresh Friday signal — BUY: 11.18× weekly, month 3.35×, ladder rising; stop ₹196.33; charges ₹0.0548)
2024-08-05  ENDURANCE   SELL ₹37.79 at stop ₹2,429.11 (-0.4%, charges ₹0.0392) — the cash goes back to work at the next Friday screen
2024-08-12  ADANIPOWER  SELL ₹36.94 at stop ₹126.55 (-19.2%, charges ₹0.0383) — the cash goes back to work at the next Friday screen
2024-08-12  CAMPUS      PYRAMID BUY ₹37.79 at ₹291.85 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹37.79 of ₹46.39); stop stays ₹277.07; charges ₹0.0448)
2024-08-16  CAMPUS      SELL ₹79.79 at stop ₹277.07 (-4.0%, charges ₹0.0828) — the cash goes back to work at the next Friday screen
2024-08-19  INOXWIND    BUY ₹23.77 at ₹215.70 (fresh Friday signal — BUY: 3.38× weekly, month 2.37×, ladder rising; stop ₹155.87; charges ₹0.0282)
2024-08-19  SUPRIYA     BUY ₹46.46 at ₹528.00 (fresh Friday signal — BUY: 6.86× weekly, month 2.15×, ladder rising; stop ₹361.00; charges ₹0.0550)
2024-08-19  VGUARD      BUY ₹46.51 at ₹524.15 (fresh Friday signal — ACCUMULATE: 3.48× weekly, month 1.72×, ladder rising; stop ₹420.24; charges ₹0.0551)
2024-09-09  AVANTIFEED  SELL ₹42.93 at stop ₹650.13 (-6.8%, charges ₹0.0445) — the cash goes back to work at the next Friday screen
2024-09-16  PRSMJOHNSN  BUY ₹42.93 at ₹214.51 (fresh Friday signal — BUY: 34.86× weekly, month 11.66×, ladder rising; stop ₹154.99; charges ₹0.0509)
2024-09-30  KSCL        SELL ₹34.06 at stop ₹973.63 (-8.9%, charges ₹0.0353) — the cash goes back to work at the next Friday screen
2024-10-03  DABUR       SELL ₹45.39 at stop ₹602.49 (-0.3%, charges ₹0.0471) — the cash goes back to work at the next Friday screen
2024-10-04  VGUARD      SELL ₹37.21 at stop ₹420.24 (-19.8%, charges ₹0.0386) — the cash goes back to work at the next Friday screen
2024-10-07  BSE         BUY ₹45.34 at ₹1,396.67 (fresh Friday signal — ACCUMULATE: 2.88× weekly, month 3.26×, ladder rising; stop ₹1,131.31; charges ₹0.0537)
2024-10-07  CEMPRO      BUY ₹45.66 at ₹655.05 (fresh Friday signal — BUY: 3.08× weekly, month 2.56×, ladder rising; stop ₹402.23; charges ₹0.0541)
2024-10-07  INDIGO      SELL ₹43.68 at stop ₹4,485.14 (+40.2%, charges ₹0.0453) — the cash goes back to work at the next Friday screen
2024-10-07  THYROCARE   SELL ₹46.77 at stop ₹265.38 (+1.4%, charges ₹0.0485) — the cash goes back to work at the next Friday screen
2024-10-14  INDIAGLYCO  BUY ₹47.18 at ₹739.40 (fresh Friday signal — BUY: 1.95× weekly, month 1.86×, ladder rising; stop ₹566.76; charges ₹0.0559)
2024-10-14  SKIPPER     BUY ₹46.94 at ₹553.00 (fresh Friday signal — BUY: 2.85× weekly, month 1.80×, ladder rising; stop ₹418.00; charges ₹0.0556)
2024-10-22  GODFRYPHLP  SELL ₹90.25 at stop ₹2,086.31 (+145.9%, charges ₹0.0936) — the cash goes back to work at the next Friday screen
2024-10-23  HINDUNILVR  SELL ₹47.26 at stop ₹2,667.03 (+3.4%, charges ₹0.0490) — the cash goes back to work at the next Friday screen
2024-10-28  PAYTM       BUY ₹43.39 at ₹747.70 (fresh Friday signal — ACCUMULATE: 2.07× weekly, month 2.45×, ladder rising; stop ₹636.31; charges ₹0.0514)
2024-10-28  PRSMJOHNSN  PYRAMID BUY ₹38.18 at ₹191.00 (2nd consecutive box jump — doubling the stake; stop stays ₹170.55; charges ₹0.0452)
2024-11-04  JSWDULUX    BUY ₹44.69 at ₹4,518.00 (fresh Friday signal — ACCUMULATE: 4.97× weekly, month 2.52×, ladder rising; stop ₹3,311.30; charges ₹0.1055)
2024-11-04  KIRLPNU     BUY ₹33.23 at ₹849.00 (fresh Friday signal — BUY: 4.25× weekly, month 1.99×, ladder rising; stop ₹594.25; charges ₹0.0784)
2024-11-13  INDIAGLYCO  SELL ₹36.04 at stop ₹566.76 (-23.3%, charges ₹0.0800) — the cash goes back to work at the next Friday screen
2024-11-13  INOXWIND    SELL ₹21.30 at stop ₹193.99 (-10.1%, charges ₹0.0473) — the cash goes back to work at the next Friday screen
2024-11-25  SUPRIYA     PYRAMID BUY ₹57.34 at ₹809.00 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹57.34 of ₹71.10); stop stays ₹574.32; charges ₹0.1354)
2024-12-17  SUPRIYA     SELL ₹113.51 at stop ₹717.25 (+9.8%, charges ₹0.2521) — the cash goes back to work at the next Friday screen
2024-12-23  KAYNES      BUY ₹44.80 at ₹7,358.80 (fresh Friday signal — BUY: 3.40× weekly, month 2.00×, ladder rising; stop ₹5,824.55; charges ₹0.1058)
2024-12-23  KIRLPNU     SELL ₹31.09 at stop ₹798.00 (-6.0%, charges ₹0.0691) — the cash goes back to work at the next Friday screen
2024-12-23  ZENTEC      BUY ₹44.78 at ₹2,555.00 (fresh Friday signal — BUY: 3.53× weekly, month 2.25×, ladder rising; stop ₹1,537.95; charges ₹0.1057)
2024-12-26  PRSMJOHNSN  SELL ₹68.00 at stop ₹170.55 (-15.9%, charges ₹0.1510) — the cash goes back to work at the next Friday screen
2024-12-27  JSWDULUX    SELL ₹33.71 at stop ₹3,423.18 (-24.2%, charges ₹0.0749) — the cash goes back to work at the next Friday screen
2024-12-30  KFINTECH    BUY ₹44.18 at ₹1,511.45 (fresh Friday signal — BUY: 2.78× weekly, month 2.22×, ladder rising; stop ₹1,159.14; charges ₹0.1043)
2024-12-30  PAYTM       PYRAMID BUY ₹58.95 at ₹1,017.00 (2nd consecutive box jump — doubling the stake; stop stays ₹893.05; charges ₹0.1392)
2025-01-06  BSE         PYRAMID BUY ₹53.59 at ₹1,783.33 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹53.59 of ₹57.83); stop stays ₹1,651.54; charges ₹0.1265)
2025-01-09  PAYTM       SELL ₹103.18 at stop ₹893.05 (+1.2%, charges ₹0.2292) — the cash goes back to work at the next Friday screen
2025-01-10  KAYNES      SELL ₹40.43 at stop ₹6,670.80 (-9.3%, charges ₹0.0898) — the cash goes back to work at the next Friday screen
2025-01-10  SKIPPER     SELL ₹40.37 at stop ₹477.28 (-13.7%, charges ₹0.0897) — the cash goes back to work at the next Friday screen
2025-01-13  AEGISLOG    BUY ₹40.30 at ₹834.65 (fresh Friday signal — BUY: 27.32× weekly, month 4.81×, ladder rising; stop ₹697.76; charges ₹0.0951)
2025-01-13  LLOYDSME    BUY ₹40.19 at ₹1,441.90 (fresh Friday signal — ACCUMULATE: 1.65× weekly, month 1.99×, ladder rising; stop ₹1,258.75; charges ₹0.0949)
2025-01-13  ZENTEC      SELL ₹38.61 at stop ₹2,213.55 (-13.4%, charges ₹0.0858) — the cash goes back to work at the next Friday screen
2025-01-15  KFINTECH    SELL ₹33.73 at stop ₹1,159.14 (-23.3%, charges ₹0.0749) — the cash goes back to work at the next Friday screen
2025-01-20  APOLLO      BUY ₹41.37 at ₹131.50 (fresh Friday signal — ACCUMULATE: 1.93× weekly, month 5.79×, ladder rising; stop ₹110.19; charges ₹0.0977)
2025-01-24  AEGISLOG    SELL ₹33.66 at stop ₹700.36 (-16.1%, charges ₹0.0748) — the cash goes back to work at the next Friday screen
2025-01-27  CREDITACC   BUY ₹39.14 at ₹850.00 (fresh Friday signal — ACCUMULATE: 3.44× weekly, month 9.52×, ladder rising; stop ₹825.52; charges ₹0.0924)
2025-01-28  LLOYDSME    SELL ₹34.93 at stop ₹1,258.75 (-12.7%, charges ₹0.0776) — the cash goes back to work at the next Friday screen
2025-02-03  ZENSARTECH  BUY ₹39.84 at ₹947.00 (fresh Friday signal — BUY: 4.92× weekly, month 3.02×, ladder rising; stop ₹727.84; charges ₹0.0941)
2025-02-17  APOLLO      SELL ₹34.51 at stop ₹110.19 (-16.2%, charges ₹0.0766) — the cash goes back to work at the next Friday screen
2025-02-17  ZENSARTECH  SELL ₹34.10 at stop ₹814.20 (-14.0%, charges ₹0.0757) — the cash goes back to work at the next Friday screen
2025-02-28  BSE         SELL ₹102.83 at stop ₹1,651.54 (+4.4%, charges ₹0.2284) — the cash goes back to work at the next Friday screen
2025-03-03  NH          BUY ₹37.33 at ₹1,450.00 (fresh Friday signal — BUY: 4.67× weekly, month 1.70×, ladder rising; stop ₹1,235.90; charges ₹0.0881)
2025-03-24  INDIASHLTR  BUY ₹38.54 at ₹794.95 (fresh Friday signal — BUY: 4.59× weekly, month 1.56×, ladder rising; stop ₹692.55; charges ₹0.0910)
2025-04-01  TAX         FY2025 settled: ₹7.1252 paid (STCG ₹35.63 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2025-04-07  INDIASHLTR  SELL ₹35.65 at stop ₹738.82 (-7.1%, charges ₹0.0792) — the cash goes back to work at the next Friday screen
2025-04-11  CEMPRO      SELL ₹36.47 at stop ₹524.92 (-19.9%, charges ₹0.0810) — the cash goes back to work at the next Friday screen
2025-04-15  AVANTIFEED  BUY ₹37.82 at ₹818.00 (fresh Friday signal — ACCUMULATE: 1.61× weekly, month 1.63×, ladder rising; stop ₹492.75; charges ₹0.0893)
2025-04-15  INDIASHLTR  BUY ₹37.75 at ₹865.00 (fresh Friday signal — BUY: 1.66× weekly, month 2.04×, ladder rising; stop ₹738.82; charges ₹0.0891)
2025-04-21  GALLANTT    BUY ₹38.69 at ₹474.75 (fresh Friday signal — BUY: 3.71× weekly, month 3.71×, ladder rising; stop ₹328.99; charges ₹0.0913)
2025-04-28  FORCEMOT    BUY ₹38.40 at ₹9,275.00 (fresh Friday signal — ACCUMULATE: 1.94× weekly, month 1.70×, ladder rising; stop ₹7,633.31; charges ₹0.0906)
2025-04-28  SMLMAH      BUY ₹38.28 at ₹1,680.00 (fresh Friday signal — BUY: 1.70× weekly, month 3.85×, ladder rising; stop ₹1,419.23; charges ₹0.0904)
2025-04-28  WHIRLPOOL   BUY ₹38.26 at ₹1,153.90 (fresh Friday signal — BUY: 2.17× weekly, month 1.78×, ladder rising; stop ₹1,017.54; charges ₹0.0903)
2025-05-05  PARAS       BUY ₹38.89 at ₹686.10 (fresh Friday signal — BUY: 25.11× weekly, month 4.49×, ladder rising; stop ₹486.64; charges ₹0.0918)
2025-05-12  CREDITACC   PYRAMID BUY ₹16.54 at ₹1,148.60 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹16.54 of ₹52.76); stop stays ₹1,019.35; charges ₹0.0390)
2025-07-28  PARAS       SELL ₹40.00 at stop ₹708.99 (+3.3%, charges ₹0.0888) — the cash goes back to work at the next Friday screen
2025-08-04  INDIASHLTR  PYRAMID BUY ₹39.30 at ₹902.50 (2nd consecutive box jump — doubling the stake; stop stays ₹853.86; charges ₹0.0928)
2025-08-04  NH          SELL ₹46.51 at stop ₹1,814.78 (+25.2%, charges ₹0.1033) — the cash goes back to work at the next Friday screen
2025-08-07  WHIRLPOOL   SELL ₹42.97 at stop ₹1,301.97 (+12.8%, charges ₹0.0954) — the cash goes back to work at the next Friday screen
2025-08-11  SMLMAH      PYRAMID BUY ₹89.75 at ₹3,948.00 (2nd consecutive box jump — doubling the stake; stop stays ₹2,878.57; charges ₹0.2119)
2025-09-25  INDIASHLTR  SELL ₹74.86 at stop ₹862.60 (-2.4%, charges ₹0.1663) — the cash goes back to work at the next Friday screen
2025-09-26  SMLMAH      SELL ₹147.52 at stop ₹3,255.67 (+15.8%, charges ₹0.3277) — the cash goes back to work at the next Friday screen
2025-09-29  CREDITACC   PYRAMID BUY ₹82.98 at ₹1,376.00 (2nd consecutive box jump — doubling the stake; stop stays ₹1,274.42; charges ₹0.1959)
2025-09-29  NETWEB      BUY ₹45.72 at ₹3,700.00 (fresh Friday signal — BUY: 2.97× weekly, month 7.29×, ladder rising; stop ₹2,674.79; charges ₹0.1079)
2025-09-29  NLCINDIA    BUY ₹45.66 at ₹280.30 (fresh Friday signal — BUY: 4.24× weekly, month 1.86×, ladder rising; stop ₹241.39; charges ₹0.1078)
2025-09-29  SUBROS      BUY ₹45.42 at ₹1,132.00 (fresh Friday signal — BUY: 8.21× weekly, month 2.64×, ladder rising; stop ₹865.50; charges ₹0.1072)
2025-10-09  FORCEMOT    SELL ₹63.26 at stop ₹15,350.10 (+65.5%, charges ₹0.1405) — the cash goes back to work at the next Friday screen
2025-10-13  AVANTIFEED  PYRAMID BUY ₹30.33 at ₹657.45 (2nd consecutive box jump — doubling the stake; stop stays ₹511.29; charges ₹0.0716)
2025-10-13  SHAILY      BUY ₹35.97 at ₹2,434.00 (fresh Friday signal — ACCUMULATE: 4.03× weekly, month 1.99×, ladder rising; stop ₹1,942.00; charges ₹0.0849)
2025-10-14  SUBROS      SELL ₹41.81 at stop ₹1,046.90 (-7.5%, charges ₹0.0929) — the cash goes back to work at the next Friday screen
2025-10-20  ANANDRATHI  BUY ₹41.81 at ₹1,574.50 (fresh Friday signal — BUY: 12.88× weekly, month 2.36×, ladder rising; stop ₹1,311.00; charges ₹0.0987)
2025-10-20  CREDITACC   SELL ₹153.18 at stop ₹1,274.42 (+11.0%, charges ₹0.3402) — the cash goes back to work at the next Friday screen
2025-10-20  GALLANTT    SELL ₹50.01 at stop ₹616.41 (+29.8%, charges ₹0.1111) — the cash goes back to work at the next Friday screen
2025-11-03  MAHABANK    BUY ₹43.49 at ₹59.70 (fresh Friday signal — ACCUMULATE: 2.08× weekly, month 1.71×, ladder rising; stop ₹53.69; charges ₹0.1027)
2025-11-03  TDPOWERSYS  BUY ₹43.20 at ₹382.27 (fresh Friday signal — BUY: 4.87× weekly, month 1.96×, ladder rising; stop ₹276.78; charges ₹0.1020)
2025-11-06  NETWEB      SELL ₹43.25 at stop ₹3,515.95 (-5.0%, charges ₹0.0961) — the cash goes back to work at the next Friday screen
2025-11-10  CCL         BUY ₹43.08 at ₹1,014.90 (fresh Friday signal — BUY: 23.71× weekly, month 1.53×, ladder rising; stop ₹780.14; charges ₹0.1017)
2025-11-10  CUB         BUY ₹43.29 at ₹190.65 (fresh Friday signal — BUY: 6.02× weekly, month 1.75×, ladder rising; stop ₹160.31; charges ₹0.1022)
2025-11-10  GRAVITA     BUY ₹30.10 at ₹1,711.00 (fresh Friday signal — BUY: 2.50× weekly, month 1.59×, ladder rising; stop ₹1,544.13; charges ₹0.0710)
2025-11-10  LTF         BUY ₹43.28 at ₹304.00 (fresh Friday signal — BUY: 2.98× weekly, month 1.55×, ladder rising; stop ₹250.80; charges ₹0.1022)
2025-11-20  ANANDRATHI  SELL ₹38.34 at stop ₹1,450.17 (-7.9%, charges ₹0.0851) — the cash goes back to work at the next Friday screen
2025-11-24  CCL         SELL ₹41.25 at stop ₹976.41 (-3.8%, charges ₹0.0916) — the cash goes back to work at the next Friday screen
2025-11-24  NLCINDIA    SELL ₹39.14 at stop ₹241.39 (-13.9%, charges ₹0.0869) — the cash goes back to work at the next Friday screen
2025-11-24  RADICO      BUY ₹38.34 at ₹3,289.40 (fresh Friday signal — ACCUMULATE: 5.90× weekly, month 2.37×, ladder rising; stop ₹2,956.50; charges ₹0.0905)
2025-11-24  TDPOWERSYS  SELL ₹40.22 at stop ₹357.49 (-6.5%, charges ₹0.0893) — the cash goes back to work at the next Friday screen
2025-12-01  CUB         PYRAMID BUY ₹46.28 at ₹204.30 (2nd consecutive box jump — doubling the stake; stop stays ₹185.32; charges ₹0.1093)
2025-12-01  EUREKAFORB  BUY ₹43.67 at ₹664.00 (fresh Friday signal — BUY: 6.94× weekly, month 2.35×, ladder rising; stop ₹535.37; charges ₹0.1031)
2025-12-01  SANSERA     BUY ₹30.66 at ₹1,749.60 (fresh Friday signal — BUY: 2.73× weekly, month 1.61×, ladder rising; stop ₹1,413.60; charges ₹0.0724)
2025-12-15  SHAILY      SELL ₹34.44 at stop ₹2,340.80 (-3.8%, charges ₹0.0765) — the cash goes back to work at the next Friday screen
2025-12-22  KIRLOSENG   BUY ₹34.44 at ₹1,258.30 (fresh Friday signal — BUY: 4.09× weekly, month 1.72×, ladder rising; stop ₹1,014.88; charges ₹0.0813)
2026-01-08  EUREKAFORB  SELL ₹38.57 at stop ₹589.10 (-11.3%, charges ₹0.0857) — the cash goes back to work at the next Friday screen
2026-01-09  GRAVITA     SELL ₹29.39 at stop ₹1,678.56 (-1.9%, charges ₹0.0653) — the cash goes back to work at the next Friday screen
2026-01-09  RADICO      SELL ₹34.30 at stop ₹2,956.50 (-10.1%, charges ₹0.0762) — the cash goes back to work at the next Friday screen
2026-01-12  KIRLOSENG   SELL ₹31.08 at stop ₹1,140.95 (-9.3%, charges ₹0.0690) — the cash goes back to work at the next Friday screen
2026-01-12  NATIONALUM  BUY ₹41.84 at ₹352.00 (fresh Friday signal — BUY: 2.49× weekly, month 1.57×, ladder rising; stop ₹246.34; charges ₹0.0988)
2026-01-19  SANSERA     PYRAMID BUY ₹32.27 at ₹1,846.00 (2nd consecutive box jump — doubling the stake; stop stays ₹1,672.76; charges ₹0.0762)
2026-01-21  AVANTIFEED  SELL ₹68.83 at stop ₹748.60 (+1.5%, charges ₹0.1529) — the cash goes back to work at the next Friday screen
2026-01-21  LTF         SELL ₹39.93 at stop ₹281.77 (-7.3%, charges ₹0.0887) — the cash goes back to work at the next Friday screen
2026-01-23  SANSERA     SELL ₹58.29 at stop ₹1,672.76 (-7.0%, charges ₹0.1295) — the cash goes back to work at the next Friday screen
2026-01-27  HINDZINC    BUY ₹41.56 at ₹733.00 (fresh Friday signal — BUY: 3.59× weekly, month 3.42×, ladder rising; stop ₹602.35; charges ₹0.0981)
2026-02-02  HINDCOPPER  BUY ₹40.76 at ₹590.15 (fresh Friday signal — BUY: 2.81× weekly, month 4.41×, ladder rising; stop ₹485.74; charges ₹0.0962)
2026-02-02  HINDZINC    SELL ₹34.00 at stop ₹602.35 (-17.8%, charges ₹0.0755) — the cash goes back to work at the next Friday screen
2026-02-02  MAHABANK    PYRAMID BUY ₹43.95 at ₹60.48 (2nd consecutive box jump — doubling the stake; stop stays ₹59.76; charges ₹0.1038)
2026-02-02  NATIONALUM  PYRAMID BUY ₹41.16 at ₹347.10 (2nd consecutive box jump — doubling the stake; stop stays ₹335.49; charges ₹0.0972)
2026-02-17  NATIONALUM  SELL ₹79.29 at stop ₹335.49 (-4.0%, charges ₹0.1761) — the cash goes back to work at the next Friday screen
2026-02-23  ABB         BUY ₹41.38 at ₹6,090.00 (fresh Friday signal — BUY: 4.16× weekly, month 1.69×, ladder rising; stop ₹5,440.18; charges ₹0.0977)
2026-02-23  CUB         PYRAMID BUY ₹95.62 at ₹211.28 (2nd consecutive box jump — doubling the stake; stop stays ₹188.57; charges ₹0.2257)
2026-03-02  HINDCOPPER  PYRAMID BUY ₹35.14 at ₹563.50 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹35.14 of ₹38.83); stop stays ₹528.63; charges ₹0.0829)
2026-03-09  CUB         SELL ₹170.10 at stop ₹188.57 (-7.7%, charges ₹0.3778) — the cash goes back to work at the next Friday screen
2026-03-12  HINDCOPPER  SELL ₹69.16 at stop ₹528.63 (-8.5%, charges ₹0.1536) — the cash goes back to work at the next Friday screen
2026-03-23  ABB         PYRAMID BUY ₹42.46 at ₹6,264.00 (2nd consecutive box jump — doubling the stake; stop stays ₹5,854.38; charges ₹0.1002)
2026-03-30  AETHER      BUY ₹36.63 at ₹1,150.50 (fresh Friday signal — BUY: 2.85× weekly, month 2.04×, ladder rising; stop ₹928.15; charges ₹0.0865)
2026-03-30  MAHABANK    SELL ₹88.43 at stop ₹61.05 (+1.6%, charges ₹0.1964) — the cash goes back to work at the next Friday screen
2026-04-01  TAX         FY2026 settled: ₹0.7357 paid (STCG ₹3.68 @20%, LTCG ₹0.00 @12.5%; losses carried forward ST ₹0.00 / LT ₹0.00)
2026-04-06  CHENNPETRO  BUY ₹36.67 at ₹989.00 (fresh Friday signal — ACCUMULATE: 1.63× weekly, month 1.66×, ladder rising; stop ₹891.29; charges ₹0.0866)
2026-04-13  INOXINDIA   BUY ₹37.63 at ₹1,299.10 (fresh Friday signal — BUY: 4.08× weekly, month 2.14×, ladder rising; stop ₹1,091.46; charges ₹0.0888)
2026-04-13  THERMAX     BUY ₹37.94 at ₹3,596.00 (fresh Friday signal — BUY: 2.05× weekly, month 1.52×, ladder rising; stop ₹2,897.50; charges ₹0.0896)
2026-04-20  GALLANTT    BUY ₹39.42 at ₹862.10 (fresh Friday signal — BUY: 15.07× weekly, month 24.00×, ladder rising; stop ₹612.75; charges ₹0.0931)
2026-04-20  NLCINDIA    BUY ₹39.44 at ₹303.60 (fresh Friday signal — BUY: 5.54× weekly, month 2.42×, ladder rising; stop ₹248.05; charges ₹0.0931)
2026-04-27  TIPSMUSIC   BUY ₹39.89 at ₹670.00 (fresh Friday signal — BUY: 20.24× weekly, month 2.80×, ladder rising; stop ₹495.00; charges ₹0.0942)
2026-05-11  AETHER      PYRAMID BUY ₹16.88 at ₹1,213.40 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹16.88 of ₹38.54); stop stays ₹1,125.84; charges ₹0.0398)
2026-05-13  INOXINDIA   SELL ₹39.56 at stop ₹1,372.18 (+5.6%, charges ₹0.0879) — the cash goes back to work at the next Friday screen
2026-05-14  AETHER      SELL ₹51.27 at stop ₹1,125.84 (-3.7%, charges ₹0.1139) — the cash goes back to work at the next Friday screen
2026-05-14  GALLANTT    SELL ₹35.67 at stop ₹783.75 (-9.1%, charges ₹0.0792) — the cash goes back to work at the next Friday screen
2026-05-18  ALKYLAMINE  BUY ₹37.85 at ₹1,710.00 (fresh Friday signal — ACCUMULATE: 9.48× weekly, month 4.24×, ladder rising; stop ₹1,502.04; charges ₹0.0894)
2026-05-18  CAPLIPOINT  BUY ₹37.85 at ₹1,990.00 (fresh Friday signal — BUY: 7.92× weekly, month 2.28×, ladder rising; stop ₹1,711.52; charges ₹0.0893)
2026-05-18  THERMAX     PYRAMID BUY ₹46.93 at ₹4,458.60 (2nd consecutive box jump — doubling the stake; stop stays ₹4,181.80; charges ₹0.1108)
2026-05-25  NLCINDIA    PYRAMID BUY ₹3.87 at ₹348.10 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹3.87 of ₹45.12); stop stays ₹320.62; charges ₹0.0091)
2026-06-09  NLCINDIA    SELL ₹45.01 at stop ₹320.62 (+4.4%, charges ₹0.1000) — the cash goes back to work at the next Friday screen
2026-06-15  CAPLIPOINT  PYRAMID BUY ₹2.18 at ₹2,435.00 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹2.18 of ₹46.20); stop stays ₹1,852.50; charges ₹0.0051)
2026-06-15  CHENNPETRO  PYRAMID BUY ₹42.83 at ₹1,158.00 (2nd consecutive box jump — doubling the stake; stop stays ₹1,075.02; charges ₹0.1011)
2026-07-29  THERMAX     SELL ₹90.36 at stop ₹4,306.63 (+6.9%, charges ₹0.2007) — the cash goes back to work at the next Friday screen
2026-08-03  ALKYLAMINE  PYRAMID BUY ₹39.44 at ₹1,785.90 (2nd consecutive box jump — doubling the stake; stop stays ₹1,676.66; charges ₹0.0931)
2026-08-03  TMB         BUY ₹42.41 at ₹864.90 (fresh Friday signal — BUY: 8.04× weekly, month 2.57×, ladder rising; stop ₹748.60; charges ₹0.1001)
2026-08-24  CHENNPETRO  PYRAMID BUY ₹8.51 at ₹1,405.00 (2nd consecutive box jump — doubling the stake (partial: cash covered ₹8.51 of ₹103.82); stop stays ₹1,242.60; charges ₹0.0201)
2026-09-10  ALKYLAMINE  SELL ₹84.56 at stop ₹1,920.99 (+9.9%, charges ₹0.1878) — the cash goes back to work at the next Friday screen
```
