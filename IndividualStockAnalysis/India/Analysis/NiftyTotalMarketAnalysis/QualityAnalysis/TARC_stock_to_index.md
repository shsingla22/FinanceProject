# TARC (TARC) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: LAGGED the index: the ratio fell -89% from FY2020 to FY2026.**

```
FY2020  ███████████                0.019%
FY2021  █                          0.002%  ▼ -90.6% vs prior year
FY2022  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -0.047%  ▼ -2702.2% vs prior year
FY2023  ██                         0.003%  ▲ +107.4% vs prior year
FY2024  ▒▒▒▒▒▒                     -0.011%  ▼ -406.5% vs prior year
FY2025  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒           -0.029%  ▼ -171.8% vs prior year
FY2026  █                          0.002%  ▲ +107.2% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2020 |
| last 10 years | FY2016 | FY2026 | n/a — data starts FY2020 |
| last 5 years | FY2021 | FY2026 | +16% |
| last 3 years | FY2023 | FY2026 | -40% |
| last 1 year | FY2025 | FY2026 | turned from loss to profit share |


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: FELL INTO LOSS: positive in FY2020, negative by FY2026.**

```
FY2020  █████                      0.005%
FY2021                             -0.000%  ▼ -100.0% vs prior year
FY2022  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -0.025%
FY2023  ███████████████████        0.018%  ▲ +173.1% vs prior year
FY2024  ▒▒                         -0.002%  ▼ -111.8% vs prior year
FY2025  ▒▒▒▒▒▒▒▒▒▒▒▒▒              -0.012%  ▼ -470.7% vs prior year
FY2026  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  -0.024%  ▼ -95.5% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2020 |
| last 10 years | FY2016 | FY2026 | n/a — data starts FY2020 |
| last 5 years | FY2021 | FY2026 | n/a (base year is zero) |
| last 3 years | FY2023 | FY2026 | fell from profit to loss share |
| last 1 year | FY2025 | FY2026 | -96% |


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

  +403% ┤
        │         ╔══════■═══╗                ┏━━◆
        │■════════╝┈┈┈┈┈┏┛┈┗━╚═══■══╗┏━━━◆━━━━┛╔═■┈┈
        │ ┗┓            ┃       ┗◆━━╚══╗    ╔══╝
  -431% ┤  ┃           ┏┛              ╚═■══╝
        │  ┗┓          ┃
        │   ┗┓        ┏┛
-1,265% ┤    ┃       ┏┛
        │    ┗┓     ┏┛
        │     ┗┓    ┃
-2,098% ┤      ┗┓  ┏┛
        │       ┃  ┃
        │       ┗┓┏┛
        │        ◆┛
-2,932% ┤
        └┬───────┬───────┬───────┬───────┬───────┬──
       FY21    FY22    FY23    FY24    FY25    FY26

◆      -90.6  -2702.2 +107.4  -406.5  -171.8  +107.2
■     -100.0     ·    +173.1  -111.8  -470.7   -95.5

◆ PAT ratio   ■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

Each line again on its own, for a closer read:

```
PAT RATIO — yearly change against the Nifty 50 (%)

  +332% ┤
        │┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈◆━┓┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┏━━◆┈┈
        │◆┓             ┏┛ ┗━━━━┓    ┏━━━◆━━━━┛
        │ ┗┓            ┃       ┗◆━━━┛
  -483% ┤  ┃           ┏┛
        │  ┗┓          ┃
        │   ┗┓        ┏┛
-1,297% ┤    ┃       ┏┛
        │    ┗┓     ┏┛
        │     ┗┓    ┃
-2,112% ┤      ┗┓  ┏┛
        │       ┃  ┃
        │       ┗┓┏┛
        │        ◆┛
-2,927% ┤
        └┬───────┬───────┬───────┬───────┬───────┬──
       FY21    FY22    FY23    FY24    FY25    FY26

◆      -90.6  -2702.2 +107.4  -406.5  -171.8  +107.2

◆ PAT ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

```
OPERATING-PROFIT RATIO — yearly change against the Nifty 50 (%)

  +225% ┤
        │        ■╗
        │      ╔═╝╚═╗
        │     ╔╝    ╚╗
   +38% ┼┈┈┈╔═╝┈┈┈┈┈┈╚═╗┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
        │ ╔═╝          ╚═╗
        │■╝              ■╗              ■
  -149% ┤                 ╚╗            ╔╝
        │                  ╚╗          ╔╝
        │                   ╚╗        ╔╝
  -335% ┤                    ╚═╗    ╔═╝
        │                      ╚╗  ╔╝
        │                       ╚╗╔╝
        │                        ■╝
  -522% ┤
        └┬───────┬───────┬───────┬───────┬──
       FY21    FY23    FY24    FY25    FY26

■     -100.0  +173.1  -111.8  -470.7   -95.5

■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```


**The value at every point of the graph** (also printed under each point above):

| Fiscal year | PAT ratio | Operating-profit ratio |
|---|---|---|
| FY2021 | -90.6% | -100.0% |
| FY2022 | -2702.2% | — |
| FY2023 | +107.4% | +173.1% |
| FY2024 | -406.5% | -111.8% |
| FY2025 | -171.8% | -470.7% |
| FY2026 | +107.2% | -95.5% |


The same graph in two other formats sits beside this file: [`TARC_stock_to_index.svg`](TARC_stock_to_index.svg) — a vector chart that opens in any browser — and [`TARC_stock_to_index.mmd`](TARC_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2015 | — | — | — | 239,976 | — | 362,356 |
| FY2016 | — | — | — | 252,916 | — | 381,103 |
| FY2017 | — | — | — | 268,287 | — | 384,170 |
| FY2018 | — | — | — | 260,991 | — | 381,288 |
| FY2019 | — | — | — | 281,855 | — | 476,374 |
| FY2020 | — | — | 53 | 275,997 | 25 | 491,207 |
| FY2021 | — | — | 6 | 331,853 | -0 | 542,357 |
| FY2022 | — | — | -233 | 495,232 | -184 | 730,487 |
| FY2023 | — | — | 20 | 574,328 | 164 | 890,079 |
| FY2024 | — | — | -77 | 721,343 | -22 | 1,008,599 |
| FY2025 | — | — | -231 | 796,066 | -133 | 1,068,504 |
| FY2026 | — | — | 19 | 905,734 | -264 | 1,084,854 |


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
