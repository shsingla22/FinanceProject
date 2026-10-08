# The month-vs-year gate, swept — April 2020 → September 2026

Seven replays of the identical engine (ladder watch on, promotion on a
breakout only, fresh signals funded first — the skill as it runs today) on
the identical archive: the top 750 NSE companies by market capitalisation,
membership rolled monthly with no lookahead, ₹100 starting all in cash on
2020-04-01, ten equal slices, Angel One charges on every order and
capital-gains tax settled every 1 April. The only thing that changes from
row to row is the month-vs-year volume threshold: the last 21 trading
days' average daily volume must be at least this multiple of the eleven
months before them. The Nifty 50 made ₹289.64 (+17.87% a year) over the
same window, pre-cost and pre-tax.

**The skill itself has not been changed; its gate stays at 1.5×.**

## The sweep

| Gate | ₹100 became (net) | CAGR (net) | Gross | Max drawdown | Buys | Mean trade | Winners | Signals not funded |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **1.5× (current)** | **₹461.09** | **+26.65%** | ₹608.13 | −27.5% | 214 | +10.5% | 46% | 4,149 |
| 1.4× | ₹399.97 | +23.90% | ₹581.74 | −34.9% | 217 | +9.7% | 45% | 4,483 |
| 1.3× | ₹446.91 | +26.04% | ₹576.16 | −30.7% | 213 | +10.5% | 45% | 4,914 |
| 1.25× | ₹437.88 | +25.64% | ₹583.15 | −28.1% | 212 | +10.0% | 45% | 5,135 |
| 1.2× | ₹418.92 | +24.78% | ₹575.15 | −31.0% | 215 | +9.6% | 44% | 5,386 |
| 1.1× | ₹503.96 | +28.40% | ₹677.54 | −29.9% | 226 | +12.1% | 47% | 5,848 |
| 1.0× (month merely ≥ year) | ₹430.01 | +25.29% | ₹554.03 | −34.0% | 218 | +11.1% | 44% | 6,361 |

## Calendar years, net — the current gate against the only one that beat it

| Year | 1.5× (current) | 1.1× | Nifty 50 |
|---|---:|---:|---:|
| 2020 (from April) | +50.4% | +42.9% | +70.1% |
| 2021 | +56.3% | **+124.4%** | +26.2% |
| 2022 | +18.2% | +23.5% | +4.3% |
| 2023 | +47.6% | +39.0% | +20.0% |
| 2024 | +1.5% | +1.2% | +9.6% |
| 2025 | −1.6% | −7.7% | +9.4% |
| 2026 to 22 Sep | +12.5% | −2.0% | −10.1% |

## What the sweep says

- **There is no threshold that is reliably better than 1.5×.** Six of the
  seven settings land within ₹400–₹504 net, and the ordering is not
  monotonic: 1.4× is the worst, 1.1× the best, and 1.3× sits back near
  the current figure. That shape is the signature of noise, not of a
  better rule. Loosening the gate by a notch changes *which* ten stocks
  fill the book in a given week, and the six-year path then diverges on
  a handful of trades.
- **The book, not the gate, is the constraint.** Every setting made
  212–226 buys. Loosening the gate from 1.5× to 1.0× added roughly 2,200
  more qualifying signals over the window, and almost all of them went
  unfunded (4,149 → 6,361 "not funded" lines): the ten slots were
  already full. A looser gate therefore mostly reshuffles the queue.
- **1.1× wins on one year.** Its whole advantage is 2021 (+124% against
  +56%). It trailed the current gate in 2020, 2023, 2025 and 2026, and
  its drawdown is slightly deeper. A rule that wins on one year out of
  seven and loses on four is not one to adopt on this evidence.
- **The gate is still doing its job.** Even at 1.0× the drawdown widens
  to −34% and the gross return is the lowest of the sweep; the
  month-vs-year test is what keeps single-week spikes in otherwise
  sleepy names out of the book.
- **The cases that prompted this** (CarTrade 31 Jul at 1.44×, Jyoti CNC
  at 1.46× and 1.25×, Macpower 31 Jul at 1.25×) would have been let
  through at 1.4×, 1.25× and 1.2× respectively — and those three
  settings all did *worse* than 1.5× across the six years. Individual
  misses are real; the rule that would have caught them cost more than
  it made.

## Recommendation

Keep 1.5×. If anything is changed later, the honest next experiment is
not the threshold but the book: the sweep shows thousands of qualifying
signals going unfunded every setting, so slot count and slice size
decide the outcome far more than another notch on the gate.

## Files

Each replay's report and complete event log sit beside this note as
`DARVAS_BACKTEST_LONGRUN_2020-04-01_to_2026-09-22_MONTH_<gate>.md` and
`_longrun_events_2020-04-01_to_2026-09-22_MONTH_<gate>.csv`; the 1.5×
row is the `…_WATCH_AFTERFRESH_BUYONLY` pair. Replay any setting with
`longrun.py --month-multiple <gate>`; the flag affects that replay only.
