# GSFC (GSFC) — Stock vs Nifty 50: price and earnings ratios

Every chart divides the company by the **Nifty 50** index, one point per fiscal year, up to the last 15 fiscal years. A **rising** line means the company outgrew the index on that measure; a **falling** line means it lagged. Index prices are real ^NSEI closes; index PAT and operating profit are the summed figures of the current 50 constituents from the stored statements (Mar 2015..Mar 2026) — today's membership, so older years carry a survivorship caveat.

## 1. Price ratio — company share price ÷ Nifty 50 (×1000 for readability)

**Verdict: too little overlapping data to call a trend.**

*(no overlapping years in the stored data)*


**Change over the standard windows**

*(too little data for window trends)*


## 2. PAT ratio — company net profit ÷ index net profit (% of index)

**Verdict: LAGGED the index: the ratio fell -56% from FY2015 to FY2026.**

```
FY2015  ████████████████████       0.170%
FY2016  ███████████████████        0.164%  ▼ -3.5% vs prior year
FY2017  ███████████████████        0.158%  ▼ -3.9% vs prior year
FY2018  █████████████████████      0.182%  ▲ +14.9% vs prior year
FY2019  █████████████████████      0.175%  ▼ -3.7% vs prior year
FY2020  █████                      0.040%  ▼ -77.2% vs prior year
FY2021  ████████████████           0.136%  ▲ +240.2% vs prior year
FY2022  █████████████████████      0.182%  ▲ +33.9% vs prior year
FY2023  ██████████████████████████ 0.220%  ▲ +21.4% vs prior year
FY2024  █████████                  0.078%  ▼ -64.5% vs prior year
FY2025  █████████                  0.074%  ▼ -5.0% vs prior year
FY2026  █████████                  0.074%  ▬ +0.1% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2015 |
| last 10 years | FY2016 | FY2026 | -55% |
| last 5 years | FY2021 | FY2026 | -45% |
| last 3 years | FY2023 | FY2026 | -66% |
| last 1 year | FY2025 | FY2026 | +0% |


## 3. Operating-profit ratio — company operating profit ÷ index operating profit (% of index)

**Verdict: LAGGED the index: the ratio fell -55% from FY2015 to FY2026.**

```
FY2015  ███████████████████████    0.163%
FY2016  █████████████████████████  0.172%  ▲ +5.5% vs prior year
FY2017  ██████████████████         0.127%  ▼ -26.2% vs prior year
FY2018  █████████████████████      0.148%  ▲ +16.4% vs prior year
FY2019  ███████████████████████    0.157%  ▲ +6.1% vs prior year
FY2020  █████████                  0.065%  ▼ -58.4% vs prior year
FY2021  ███████████████            0.105%  ▲ +61.1% vs prior year
FY2022  ██████████████████████████ 0.181%  ▲ +71.8% vs prior year
FY2023  ██████████████████████████ 0.178%  ▼ -1.3% vs prior year
FY2024  ███████                    0.051%  ▼ -71.4% vs prior year
FY2025  █████████                  0.060%  ▲ +16.8% vs prior year
FY2026  ██████████                 0.073%  ▲ +22.3% vs prior year
```


**Change over the standard windows**

| Window | From | To | Ratio change |
|---|---|---|---|
| last 15 years | FY2011 | FY2026 | n/a — data starts FY2015 |
| last 10 years | FY2016 | FY2026 | -58% |
| last 5 years | FY2021 | FY2026 | -31% |
| last 3 years | FY2023 | FY2026 | -59% |
| last 1 year | FY2025 | FY2026 | +22% |


## 4. Yearly change of all three ratios — line graph

One line per ratio, one point per fiscal year: how much the company gained (+) or lost (−) on the index that year.

```
ALL THREE RATIOS — yearly change against the Nifty 50 (%)

  +266% ┤
        │                                        ◆┓
        │                                       ┏┛┗┓
        │                                       ┃  ┗┓
  +174% ┤                                      ┏┛   ┗┓
        │                                      ┃     ┗┓
        │                                     ┏┛      ┗┓
   +82% ┤                                    ┏┛       ╔══■═╗
        │                                   ┏┛  ╔■════╝ ┗┓ ╚══╗
        │               ╔■═══╗              ┃  ╔╝        ◆━━━━╚═╗◆┓              ■═══════■
   -11% ┼■════╗━━◆━╔════╝◆━━━╚═══■══╗┈┈┈┈┈┈┏╔══╝┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╚■═╗━┓┈┈┈┈┈┈┈┈╔══◆━━━━━━━◆┈┈
        │     ╚══■═╝               ┗╚══╗   ╔╝                      ╚═╗┓      ╔╝━┛
        │                            ┗━╚═■═╝                         ╚══╗┓╔══╝┛
        │                               ┗◆┛                             ╚■╝┛
  -103% ┤
        └┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20    FY21    FY22    FY23    FY24    FY25    FY26

◆      -3.5    -3.9    +14.9   -3.7    -77.2  +240.2   +33.9   +21.4   -64.5   -5.0    +0.1
■      +5.5    -26.2   +16.4   +6.1    -58.4   +61.1   +71.8   -1.3    -71.4   +16.8   +22.3

◆ PAT ratio   ■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

Each line again on its own, for a closer read:

```
PAT RATIO — yearly change against the Nifty 50 (%)

  +266% ┤
        │                                        ◆┓
        │                                       ┏┛┗┓
        │                                       ┃  ┗┓
  +174% ┤                                      ┏┛   ┗┓
        │                                      ┃     ┗┓
        │                                     ┏┛      ┗┓
   +82% ┤                                    ┏┛        ┗┓
        │                                   ┏┛          ┗┓
        │                                   ┃            ◆━━━━━━━◆┓
   -11% ┼◆━━━━━━━◆━━━━━━━◆━━━━━━━◆━┓┈┈┈┈┈┈┈┏┛┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┗━━┓┈┈┈┈┈┈┈┈┈┈┏◆━━━━━━━◆┈┈
        │                          ┗━┓     ┃                         ┗┓       ┏━┛
        │                            ┗━━┓ ┏┛                          ┗━━┓ ┏━━┛
        │                               ┗◆┛                              ◆━┛
  -103% ┤
        └┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20    FY21    FY22    FY23    FY24    FY25    FY26

◆      -3.5    -3.9    +14.9   -3.7    -77.2  +240.2   +33.9   +21.4   -64.5   -5.0    +0.1

◆ PAT ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```

```
OPERATING-PROFIT RATIO — yearly change against the Nifty 50 (%)

   +83% ┤
        │                                             ╔══■╗
        │                                        ■════╝   ╚═╗
        │                                       ╔╝          ╚╗
   +42% ┤                                      ╔╝            ╚╗
        │                                      ║              ╚╗                      ╔══■
        │               ╔■═══════■╗           ╔╝               ╚═╗               ■════╝
    +0% ┼■═╗┈┈┈┈┈┈┈┈┈┈╔═╝┈┈┈┈┈┈┈┈┈╚╗┈┈┈┈┈┈┈┈┈╔╝┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈■╗┈┈┈┈┈┈┈┈┈┈┈┈┈╔╝┈┈┈┈┈┈┈┈┈┈
        │  ╚════╗  ╔══╝            ╚═╗      ╔╝                    ╚═╗          ╔╝
        │       ╚■═╝                 ╚╗     ║                       ╚╗        ╔╝
   -41% ┤                             ╚═╗  ╔╝                        ╚╗     ╔═╝
        │                               ╚╗╔╝                          ╚╗   ╔╝
        │                                ■╝                            ╚═╗╔╝
        │                                                                ■╝
   -83% ┤
        └┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬──
       FY16    FY17    FY18    FY19    FY20    FY21    FY22    FY23    FY24    FY25    FY26

■      +5.5    -26.2   +16.4   +6.1    -58.4   +61.1   +71.8   -1.3    -71.4   +16.8   +22.3

■ Operating-profit ratio
┈ the 0% line — above it the company gained on the index that year, below it the company lagged
```


**The value at every point of the graph** (also printed under each point above):

| Fiscal year | PAT ratio | Operating-profit ratio |
|---|---|---|
| FY2016 | -3.5% | +5.5% |
| FY2017 | -3.9% | -26.2% |
| FY2018 | +14.9% | +16.4% |
| FY2019 | -3.7% | +6.1% |
| FY2020 | -77.2% | -58.4% |
| FY2021 | +240.2% | +61.1% |
| FY2022 | +33.9% | +71.8% |
| FY2023 | +21.4% | -1.3% |
| FY2024 | -64.5% | -71.4% |
| FY2025 | -5.0% | +16.8% |
| FY2026 | +0.1% | +22.3% |


The same graph in two other formats sits beside this file: [`GSFC_stock_to_index.svg`](GSFC_stock_to_index.svg) — a vector chart that opens in any browser — and [`GSFC_stock_to_index.mmd`](GSFC_stock_to_index.mmd) — Mermaid source, which draws itself when pasted into GitHub.


## 5. The raw yearly values behind every ratio

Company prices in rupees; profits in Rs crore. The index close is the March close unless the company closes its books in another month (shown in brackets). '—' = not in the stored data.

| Fiscal year | Company price (Rs) | Nifty 50 close | Company PAT (Rs cr) | Index PAT (Rs cr) | Company OP (Rs cr) | Index OP (Rs cr) |
|---|---|---|---|---|---|---|
| FY2015 | — | — | 409 | 239,976 | 592 | 362,356 |
| FY2016 | — | — | 416 | 252,916 | 657 | 381,103 |
| FY2017 | — | — | 424 | 268,287 | 489 | 384,170 |
| FY2018 | — | — | 474 | 260,991 | 565 | 381,288 |
| FY2019 | — | — | 493 | 281,855 | 749 | 476,374 |
| FY2020 | — | — | 110 | 275,997 | 321 | 491,207 |
| FY2021 | — | — | 450 | 331,853 | 571 | 542,357 |
| FY2022 | — | — | 899 | 495,232 | 1,321 | 730,487 |
| FY2023 | — | — | 1,266 | 574,328 | 1,588 | 890,079 |
| FY2024 | — | — | 564 | 721,343 | 514 | 1,008,599 |
| FY2025 | — | — | 591 | 796,066 | 636 | 1,068,504 |
| FY2026 | — | — | 673 | 905,734 | 790 | 1,084,854 |


---
*Generated by the StockToIndexPriceEarningsRatio skill. Research tooling — not investment advice.*
