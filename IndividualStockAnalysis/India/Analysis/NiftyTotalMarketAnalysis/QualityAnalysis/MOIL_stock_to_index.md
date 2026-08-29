# MOIL (MOIL) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: LAGGED the index: the ratio fell -50% from FY2015 to FY2020.**

```
FY2015  ██████████████████████████ 0.178%
FY2016  ██████████                 0.068%  ▼ -61.6% vs prior year
FY2017  █████████████████          0.114%  ▲ +67.3% vs prior year
FY2018  ███████████████████████    0.160%  ▲ +39.6% vs prior year
FY2019  █████████████████████████  0.170%  ▲ +6.1% vs prior year
FY2020  █████████████              0.090%  ▼ -47.0% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2005 | FY2020 | n/a — data starts FY2015 |
| last 10 years | FY2010 | FY2020 | n/a — data starts FY2015 |
| last 5 years | FY2015 | FY2020 | -50% |
| last 3 years | FY2017 | FY2020 | -21% |
| last 1 year | FY2019 | FY2020 | -47% |


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: LAGGED the index: the ratio fell -50% from FY2015 to FY2020.**

```
FY2015  ████████████████████       0.105%
FY2016  ███                        0.018%  ▼ -82.4% vs prior year
FY2017  ███████████████            0.078%  ▲ +325.1% vs prior year
FY2018  ██████████████████████████ 0.138%  ▲ +77.3% vs prior year
FY2019  ████████████████████████   0.126%  ▼ -9.0% vs prior year
FY2020  ██████████                 0.052%  ▼ -58.6% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2005 | FY2020 | n/a — data starts FY2015 |
| last 10 years | FY2010 | FY2020 | n/a — data starts FY2015 |
| last 5 years | FY2015 | FY2020 | -50% |
| last 3 years | FY2017 | FY2020 | -33% |
| last 1 year | FY2019 | FY2020 | -59% |


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

  +358% ┤
        │        ■╗
        │       ╔╝╚╗
        │       ║  ╚╗
  +240% ┤      ╔╝   ╚═╗
        │      ║      ╚╗
        │     ╔╝       ╚╗
  +121% ┤    ╔╝         ╚╗
        │   ╔╝           ■═╗
        │   ║   ┏◆━━━━━━━◆━╚═╗
        │  ╔╝┏━━┛            ╚══╗◆━━┓
    +3% ┼┈┈║━┛┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╚■═══╗━┓┈┈┈┈
        │◆╔╝                         ╚═══■
        │■╝
  -115% ┤
        └┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20

◆      -61.6   +67.3   +39.6   +6.1    -47.0
■      -82.4  +325.1   +77.3   -9.0    -58.6

◆ PAT ratio   ■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

Each line again on its own, for a closer read:

```
PAT RATIO — yearly change against the Nifty 50 (%)

   +78% ┤
        │        ◆━┓
        │       ┏┛ ┗━━┓
        │       ┃     ┗━┓
   +40% ┤      ┏┛       ┗◆━┓
        │      ┃           ┗━┓
        │     ┏┛             ┗━━┓
    +3% ┼┈┈┈┈┏┛┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┗◆┓┈┈┈┈┈┈┈┈┈
        │   ┏┛                    ┗━┓
        │   ┃                       ┗┓
   -35% ┤  ┏┛                        ┗━┓
        │  ┃                           ┗━┓
        │ ┏┛                             ◆
        │◆┛
   -72% ┤
        └┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20

◆      -61.6   +67.3   +39.6   +6.1    -47.0

◆ PAT ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

```
OPERATING-PROFIT RATIO — yearly change against the Nifty 50 (%)

  +358% ┤
        │        ■╗
        │       ╔╝╚╗
        │       ║  ╚╗
  +240% ┤      ╔╝   ╚═╗
        │      ║      ╚╗
        │     ╔╝       ╚╗
  +121% ┤    ╔╝         ╚╗
        │   ╔╝           ■═╗
        │   ║              ╚═╗
        │  ╔╝                ╚══╗
    +3% ┼┈┈║┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╚■═══╗┈┈┈┈┈┈
        │ ╔╝                         ╚═══■
        │■╝
  -115% ┤
        └┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20

■      -82.4  +325.1   +77.3   -9.0    -58.6

■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```


**The value at every point of the graph** (also printed under each point above):

| Fiscal year | PAT ratio | Operating-profit ratio |
|---|---|---|
| FY2016 | -61.6% | -82.4% |
| FY2017 | +67.3% | +325.1% |
| FY2018 | +39.6% | +77.3% |
| FY2019 | +6.1% | -9.0% |
| FY2020 | -47.0% | -58.6% |


The same graph in two other formats sits beside this file: [`MOIL_stock_to_index.svg`](MOIL_stock_to_index.svg) — a vector chart that opens in any browser — and [`MOIL_stock_to_index.mmd`](MOIL_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2015 | — | — | 428 | 239,976 | 379 | 362,356 |
| FY2016 | — | — | 173 | 252,916 | 70 | 381,103 |
| FY2017 | — | — | 307 | 268,287 | 300 | 384,170 |
| FY2018 | — | — | 417 | 260,991 | 528 | 381,288 |
| FY2019 | — | — | 478 | 281,855 | 600 | 476,374 |
| FY2020 | — | — | 248 | 275,997 | 256 | 491,207 |
| FY2021 | — | — | — | 331,853 | — | 542,357 |
| FY2022 | — | — | — | 495,232 | — | 730,487 |
| FY2023 | — | — | — | 574,328 | — | 890,079 |
| FY2024 | — | — | — | 721,343 | — | 1,008,599 |
| FY2025 | — | — | — | 796,066 | — | 1,068,504 |
| FY2026 | — | — | — | 905,734 | — | 1,084,854 |


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
