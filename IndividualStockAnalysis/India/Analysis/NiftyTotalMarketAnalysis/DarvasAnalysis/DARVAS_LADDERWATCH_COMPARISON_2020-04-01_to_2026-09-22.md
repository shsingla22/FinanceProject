# The ladder watch, measured — April 2020 → September 2026

Four replays of the identical engine on the identical archive: the top 750
NSE companies by market capitalisation, membership rolled monthly with no
lookahead (`VolumeAndPricingBacktest/ROLLING_MCAP750_2019-06-01_to_2026-09-22/`),
₹100 starting all in cash on 2020-04-01, ten equal slices, daily stops,
weekly ratchets, Angel One charges on every order and capital-gains tax
settled every 1 April. Every number below is NET of those costs and taxes;
the gross figure is the same simulation without them. The Nifty 50 made
₹289.64 (+17.87% a year) over the same 6.47 years, itself pre-cost and
pre-tax.

## The four rules

| Rule | ₹100 became (net) | CAGR (net) | Gross | Max drawdown | Buys | of which promoted |
|---|---:|---:|---:|---:|---:|---:|
| **A. Old rules** — a surge that fails the ladder is dropped | ₹342.79 | +20.98% | ₹415.96 | −27.1% | 212 | — |
| **B. Ladder watch as first specified** — watched 30 days; promoted on BUY *or* ACCUMULATE; promoted and fresh signals ranked together by surge size | ₹200.80 | +11.38% | ₹242.92 | −42.8% | 245 | 163 |
| **C. Watch, fresh signals funded first** — as B, but the week's fresh full qualifiers take the cash before any promoted name | ₹388.18 | +23.32% | ₹488.27 | −36.6% | 213 | 51 |
| **D. Watch, fresh first, promoted on a BREAKOUT only** — as C, but a watched stock is promoted only when its ladder rises *and* it closes above its box top (BUY); ACCUMULATE keeps it on watch | **₹461.09** | **+26.65%** | ₹608.13 | −27.5% | 214 | 26 |

Rule D is now the skill's default, live and in the backtest engine. The
two toggles that produced B and C remain in `longrun.py`
(`--watch-promote both`, `--watch-priority surge`) so any of these can be
replayed.

## What the promoted trades did

| Rule | Promoted trades closed | Mean return | Median | Win rate | All trades: mean / win rate |
|---|---:|---:|---:|---:|---|
| B | 156 | +4.3% | −6.0% | 39% | +4.8% / 36% |
| C | 51 | +5.2% | −4.3% | 37% | +10.6% / 41% |
| D | 25 | +13.6% | +0.5% | 56% | +10.5% / 46% |
| A (no watch) | — | — | — | — | +7.7% / 42% |

## Why the first version lost money

- **Volume of watch entries.** Over the window 5,473 surges passed both
  volume gates but failed the ladder — about 16 a week. Most were stocks
  that had been *falling* and then spiked (their last three box
  midpoints step down). With ACCUMULATE counting as a promotion, any such
  stock that sealed one higher box got promoted, so 163 of the 245 buys
  were promoted names and they carried their large surge multiples to the
  front of the queue.
- **Crowding out.** Fresh, fully-qualified signals — the rule that made
  ₹343 on its own — were funded only 82 times instead of 212, because the
  ten slots were full of promoted names. That is the whole loss: the
  promoted trades were not disastrous (+4.3% mean), they simply displaced
  better ones and doubled the drawdown.
- **Funding fresh first (C)** removed the displacement and lifted the
  result above the old rules.
- **Breakout-only promotion (D)** cut the promoted entries to 26 and
  turned them into the best-performing group in the book (+13.6% mean,
  56% winners): a stock that surged, then built a rising ladder, then
  broke out of its box is exactly what Darvas waited for. Drawdown came
  back to the old rules' level.

## Reports

- Rule D (the skill as it now runs): `DARVAS_BACKTEST_LONGRUN_2020-04-01_to_2026-09-22_WATCH_AFTERFRESH_BUYONLY.md`
- Rule A: `…_BASELINE.md` · Rule B: `…_LADDERWATCH.md` · Rule C: `…_WATCH_AFTERFRESH.md`
- Every event of every run (buys, sells, stop raises, watch starts,
  promotions, expiries, refusals) in the matching `_longrun_events_…csv`.

The same caveats as every long run here: point-in-time membership from
bhavcopies with market caps reconstructed before February 2024, corporate
actions detected from the price series, statements cut at each screen's
fiscal year, and the conference-call read excluded from the backtest.
