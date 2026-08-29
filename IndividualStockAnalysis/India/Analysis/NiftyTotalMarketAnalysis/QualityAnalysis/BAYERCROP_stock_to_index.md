# Bayer Crop Sci. (BAYERCROP) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: LAGGED the index: the ratio fell -52% from FY2015 to FY2026.**

```
FY2015  ██████████████████████     406.172
FY2016  ██████████████████████████ 483.267  ▲ +19.0% vs prior year
FY2017  ██████████████████████     408.016  ▼ -15.6% vs prior year
FY2018  █████████████████████      393.799  ▼ -3.5% vs prior year
FY2019  ████████████████████       370.220  ▼ -6.0% vs prior year
FY2020  ███████████████████        350.506  ▼ -5.3% vs prior year
FY2021  ████████████████████       365.106  ▲ +4.2% vs prior year
FY2022  ████████████████           290.562  ▼ -20.4% vs prior year
FY2023  ████████████               225.721  ▼ -22.3% vs prior year
FY2024  █████████████              232.443  ▲ +3.0% vs prior year
FY2025  ███████████                201.757  ▼ -13.2% vs prior year
FY2026  ██████████                 193.586  ▼ -4.0% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2015 |
| last 10 years | FY2016 | FY2026 | -60% |
| last 5 years | FY2021 | FY2026 | -47% |
| last 3 years | FY2023 | FY2026 | -14% |
| last 1 year | FY2025 | FY2026 | -4% |


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

   +22% ┤
        │●╮
        │ ╰╮
        │  │
   +10% ┤  ╰╮
        │   ╰╮                                  ╭●╮
        │    ╰╮                              ╭──╯ ╰╮                     ●─╮
    -2% ┼┈┈┈┈┈╰╮┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╭─╯┈┈┈┈┈╰╮┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╭╯┈╰╮┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
        │      ╰╮       ╭●───────●───────●─╯        ╰─╮                ╭╯   ╰──╮       ╭─●
        │       │     ╭─╯                             ╰╮              ╭╯       ╰╮   ╭──╯
   -14% ┤       ╰╮ ╭──╯                                ╰╮           ╭─╯         ╰●──╯
        │        ●─╯                                    ╰╮         ╭╯
        │                                                ●────╮   ╭╯
        │                                                     ╰──●╯
   -26% ┤
        └┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20    FY21    FY22    FY23    FY24    FY25    FY26

●      +19.0   -15.6   -3.5    -6.0    -5.3    +4.2    -20.4   -22.3   +3.0    -13.2   -4.0

● Price ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

**The value at every point of the graph** (also printed under each point above):

| Fiscal year | Price ratio |
|---|---|
| FY2016 | +19.0% |
| FY2017 | -15.6% |
| FY2018 | -3.5% |
| FY2019 | -6.0% |
| FY2020 | -5.3% |
| FY2021 | +4.2% |
| FY2022 | -20.4% |
| FY2023 | -22.3% |
| FY2024 | +3.0% |
| FY2025 | -13.2% |
| FY2026 | -4.0% |


The same graph in two other formats sits beside this file: [`BAYERCROP_stock_to_index.svg`](BAYERCROP_stock_to_index.svg) — a vector chart that opens in any browser — and [`BAYERCROP_stock_to_index.mmd`](BAYERCROP_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2006 | — | — | 38 | — | 57 | — |
| FY2007 | — | — | 55 | — | 35 | — |
| FY2015 | 3,323.10 | 8,181.50 | — | 239,976 | — | 362,356 |
| FY2016 | 3,793.55 | 7,849.80 | — | 252,916 | — | 381,103 |
| FY2017 | 3,796.20 | 9,304.05 | — | 268,287 | — | 384,170 |
| FY2018 | 4,229.15 | 10,739.35 | — | 260,991 | — | 381,288 |
| FY2019 | 4,349.40 | 11,748.15 | — | 281,855 | — | 476,374 |
| FY2020 | 3,455.95 | 9,859.90 | — | 275,997 | — | 491,207 |
| FY2021 | 5,341.90 | 14,631.10 | — | 331,853 | — | 542,357 |
| FY2022 | 4,969.35 | 17,102.55 | — | 495,232 | — | 730,487 |
| FY2023 | 4,077.65 | 18,065.00 | — | 574,328 | — | 890,079 |
| FY2024 | 5,254.35 | 22,604.85 | — | 721,343 | — | 1,008,599 |
| FY2025 | 4,909.60 | 24,334.20 | — | 796,066 | — | 1,068,504 |
| FY2026 | 4,645.60 | 23,997.55 | — | 905,734 | — | 1,084,854 |


## Years the stored data could not cover

- Mar 2015: company Net Profit not in stored data
- Mar 2016: company Net Profit not in stored data
- Mar 2017: company Net Profit not in stored data
- Mar 2018: company Net Profit not in stored data
- Mar 2019: company Net Profit not in stored data
- Mar 2020: company Net Profit not in stored data
- Mar 2021: company Net Profit not in stored data
- Mar 2022: company Net Profit not in stored data
- Mar 2023: company Net Profit not in stored data
- Mar 2024: company Net Profit not in stored data
- Mar 2025: company Net Profit not in stored data
- Mar 2026: company Net Profit not in stored data


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
