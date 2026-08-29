# Alembic Pharma (APLLTD) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: LAGGED the index: the ratio fell -37% from FY2015 to FY2026.**

```
FY2015  █████████                  0.118%
FY2016  █████████████████████      0.285%  ▲ +141.4% vs prior year
FY2017  ███████████                0.150%  ▼ -47.2% vs prior year
FY2018  ████████████               0.158%  ▲ +5.3% vs prior year
FY2019  ████████████████           0.207%  ▲ +30.7% vs prior year
FY2020  ██████████████████████     0.290%  ▲ +40.3% vs prior year
FY2021  ██████████████████████████ 0.345%  ▲ +19.0% vs prior year
FY2022  ████████                   0.105%  ▼ -69.5% vs prior year
FY2023  ████                       0.060%  ▼ -43.4% vs prior year
FY2024  ██████                     0.085%  ▲ +43.4% vs prior year
FY2025  ██████                     0.073%  ▼ -14.4% vs prior year
FY2026  ██████                     0.074%  ▲ +1.3% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2015 |
| last 10 years | FY2016 | FY2026 | -74% |
| last 5 years | FY2021 | FY2026 | -79% |
| last 3 years | FY2023 | FY2026 | +24% |
| last 1 year | FY2025 | FY2026 | +1% |


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: MOVED WITH the index: the ratio changed only -7% across the window.**

```
FY2015  ███████████                0.111%
FY2016  █████████████████████████  0.264%  ▲ +137.6% vs prior year
FY2017  ███████████████            0.160%  ▼ -39.4% vs prior year
FY2018  ████████████████           0.169%  ▲ +5.3% vs prior year
FY2019  █████████████████          0.183%  ▲ +8.8% vs prior year
FY2020  ████████████████████████   0.249%  ▲ +35.7% vs prior year
FY2021  ██████████████████████████ 0.273%  ▲ +9.6% vs prior year
FY2022  ███████████                0.120%  ▼ -56.2% vs prior year
FY2023  ███████                    0.077%  ▼ -36.0% vs prior year
FY2024  █████████                  0.092%  ▲ +20.6% vs prior year
FY2025  █████████                  0.094%  ▲ +2.1% vs prior year
FY2026  ██████████                 0.103%  ▲ +9.5% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2015 |
| last 10 years | FY2016 | FY2026 | -61% |
| last 5 years | FY2021 | FY2026 | -62% |
| last 3 years | FY2023 | FY2026 | +35% |
| last 1 year | FY2025 | FY2026 | +10% |


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

  +158% ┤
        │■╗
        │ ╚╗
   +97% ┤  ║
        │  ╚╗
        │   ╚╗
        │    ╚╗
   +36% ┤     ╚╗                ┏◆━━━━━━╔■═╗━┓                           ◆━┓
        │     ┗╚╗          ┏━━━━┛  ╔════╝  ╚════╗◆┓                    ┏╔■════╗
        │┈┈┈┈┈┈┗║┈┈┈┈┈┈┈╔■═══════■═╝┈┈┈┈┈┈┈┈┈┈┈┈╚■═╗┓┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╔═╝┈┈┈┈┈╚══■═══════■┈┈
   -25% ┤       ╚╗ ╔════╝                          ╚══╗            ╔══╝         ┗◆━━━━┛
        │       ┗■═╝━┛                                ╚═╗     ╔══■═╝┛
        │        ◆━┛                                   ┗╚■════╝━━◆┛
        │                                                ◆━━━┛
   -86% ┤
        └┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20    FY21    FY22    FY23    FY24    FY25    FY26

◆     +141.4   -47.2   +5.3    +30.7   +40.3   +19.0   -69.5   -43.4   +43.4   -14.4   +1.3
■     +137.6   -39.4   +5.3    +8.8    +35.7   +9.6    -56.2   -36.0   +20.6   +2.1    +9.5

◆ PAT ratio   ■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

Each line again on its own, for a closer read:

```
PAT RATIO — yearly change against the Nifty 50 (%)

  +158% ┤
        │◆┓
        │ ┗┓
   +97% ┤  ┃
        │  ┗┓
        │   ┗┓
        │    ┗┓
   +36% ┤     ┃                 ┏◆━━━━━━━◆━━━┓                           ◆━┓
        │     ┗┓           ┏━━━━┛            ┗━━━◆┓                    ┏━┛ ┗━━┓
        │┈┈┈┈┈┈┗┓┈┈┈┈┈┈┈┏◆━┛┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┗━┓┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┏┛┈┈┈┈┈┈┗━┓┈┈┈┈┈┏━━◆┈┈
   -25% ┤       ┃    ┏━━┛                           ┗━┓             ┏━┛         ┗◆━━━━┛
        │       ┗┓ ┏━┛                                ┗┓          ┏━┛
        │        ◆━┛                                   ┗━┓   ┏━━━◆┛
        │                                                ◆━━━┛
   -86% ┤
        └┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20    FY21    FY22    FY23    FY24    FY25    FY26

◆     +141.4   -47.2   +5.3    +30.7   +40.3   +19.0   -69.5   -43.4   +43.4   -14.4   +1.3

◆ PAT ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

```
OPERATING-PROFIT RATIO — yearly change against the Nifty 50 (%)

  +153% ┤
        │■╗
        │ ╚╗
        │  ║
   +97% ┤  ╚╗
        │   ╚╗
        │    ╚╗
   +41% ┤     ║                         ╔■═╗
        │     ╚╗                   ╔════╝  ╚════╗                       ╔■════╗
        │      ╚╗       ╔■═══════■═╝            ╚■╗                    ╔╝     ╚══■═══════■
        │┈┈┈┈┈┈┈║┈┈┈┈╔══╝┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╚══╗┈┈┈┈┈┈┈┈┈┈┈┈┈┈╔══╝┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
   -15% ┤       ╚╗ ╔═╝                               ╚╗            ╔╝
        │        ■═╝                                  ╚══╗   ╔═══■═╝
        │                                                ■═══╝
   -72% ┤
        └┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20    FY21    FY22    FY23    FY24    FY25    FY26

■     +137.6   -39.4   +5.3    +8.8    +35.7   +9.6    -56.2   -36.0   +20.6   +2.1    +9.5

■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```


**The value at every point of the graph** (also printed under each point above):

| Fiscal year | PAT ratio | Operating-profit ratio |
|---|---|---|
| FY2016 | +141.4% | +137.6% |
| FY2017 | -47.2% | -39.4% |
| FY2018 | +5.3% | +5.3% |
| FY2019 | +30.7% | +8.8% |
| FY2020 | +40.3% | +35.7% |
| FY2021 | +19.0% | +9.6% |
| FY2022 | -69.5% | -56.2% |
| FY2023 | -43.4% | -36.0% |
| FY2024 | +43.4% | +20.6% |
| FY2025 | -14.4% | +2.1% |
| FY2026 | +1.3% | +9.5% |


The same graph in two other formats sits beside this file: [`APLLTD_stock_to_index.svg`](APLLTD_stock_to_index.svg) — a vector chart that opens in any browser — and [`APLLTD_stock_to_index.mmd`](APLLTD_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2015 | — | — | 283 | 239,976 | 403 | 362,356 |
| FY2016 | — | — | 720 | 252,916 | 1,007 | 381,103 |
| FY2017 | — | — | 403 | 268,287 | 615 | 384,170 |
| FY2018 | — | — | 413 | 260,991 | 643 | 381,288 |
| FY2019 | — | — | 583 | 281,855 | 874 | 476,374 |
| FY2020 | — | — | 801 | 275,997 | 1,223 | 491,207 |
| FY2021 | — | — | 1,146 | 331,853 | 1,480 | 542,357 |
| FY2022 | — | — | 521 | 495,232 | 874 | 730,487 |
| FY2023 | — | — | 342 | 574,328 | 682 | 890,079 |
| FY2024 | — | — | 616 | 721,343 | 932 | 1,008,599 |
| FY2025 | — | — | 582 | 796,066 | 1,008 | 1,068,504 |
| FY2026 | — | — | 671 | 905,734 | 1,121 | 1,084,854 |


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
