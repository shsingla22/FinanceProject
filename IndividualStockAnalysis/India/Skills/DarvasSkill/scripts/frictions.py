"""
frictions.py — what the real world charges: Angel One transaction costs
on every order, and capital-gains tax settled every 1 April.

TRANSACTION COSTS (equity delivery on Angel One, ad-valorem components):

  both sides   STT 0.10% · NSE transaction charge 0.00297% ·
               SEBI turnover fee 0.0001% · 18% GST on (brokerage +
               transaction charge + SEBI fee)
  buy only     stamp duty 0.015%
  brokerage    ₹0 on delivery until 31 Oct 2024; from 1 Nov 2024 Angel
               One charges min(0.1% of turnover, ₹20) per order — at a
               normalised ₹100 portfolio the ₹20 cap never binds, so
               0.1% applies (stated in the report)

  Flat charges that cannot scale to a normalised ₹100 — the ₹20+GST DP
  charge per sell and the ₹2 brokerage minimum — are excluded and
  disclosed: on a realistic account (₹1 lakh+) they are under 0.03%
  of a trade.

CAPITAL GAINS TAX, settled on the first trading day of each April for
the fiscal year just ended, paid OUT OF THE PORTFOLIO:

  short-term (held ≤ 365 days)  20%
  long-term  (held  > 365 days) 12.5%

  Set-off follows the Income-tax Act: a short-term loss offsets
  short-term then long-term gains; a long-term loss offsets ONLY
  long-term gains; unabsorbed losses carry forward to later years.
  Gains are computed on execution prices (buy/sell charges not added
  to basis — a slightly conservative simplification, stated in the
  report). The LTCG exemption slab is ignored (it cannot scale to a
  normalised ₹100) — also conservative.
"""

from __future__ import annotations

import datetime as dt
from collections import defaultdict

STT = 0.0010                 # both sides, delivery
TXN = 0.0000297              # NSE transaction charge
SEBI = 0.000001              # ₹10 per crore
GST = 0.18                   # on brokerage + TXN + SEBI
STAMP = 0.00015              # buy side only
BROKERAGE = 0.0010           # min(0.1%, ₹20)/order; cap never binds here
BROKERAGE_FROM = "2024-11-01"     # ₹0 on delivery before this date

STCG_RATE = 0.20             # held ≤ 365 days
LTCG_RATE = 0.125            # held > 365 days
LT_DAYS = 365


def fy_label(date_iso: str) -> str:
    """The fiscal year a date falls in, named by its ending March."""
    d = dt.date.fromisoformat(date_iso)
    return f"FY{d.year + 1}" if d.month >= 4 else f"FY{d.year}"


def next_april_first(date_iso: str) -> str:
    d = dt.date.fromisoformat(date_iso)
    year = d.year + 1 if (d.month, d.day) >= (4, 1) else d.year
    return dt.date(year, 4, 1).isoformat()


def offset_and_tax(st: float, lt: float,
                   cf_st: float, cf_lt: float) -> dict:
    """One fiscal year's tax under the set-off rules. st/lt are the
    year's NET realised short- and long-term results (either sign);
    cf_st/cf_lt are brought-forward losses (positive numbers).
    Returns the tax and the losses carried onward."""
    if st < 0 and lt > 0:                     # ST loss absorbs LT gain
        x = min(-st, lt)
        st += x
        lt -= x
    # an LT loss never touches an ST gain — it only carries forward
    if cf_st > 0 and st > 0:
        x = min(cf_st, st)
        st -= x
        cf_st -= x
    if cf_st > 0 and lt > 0:
        x = min(cf_st, lt)
        lt -= x
        cf_st -= x
    if cf_lt > 0 and lt > 0:
        x = min(cf_lt, lt)
        lt -= x
        cf_lt -= x
    tax = STCG_RATE * max(st, 0.0) + LTCG_RATE * max(lt, 0.0)
    return {"tax": tax,
            "st_taxable": max(st, 0.0), "lt_taxable": max(lt, 0.0),
            "cf_st": cf_st + max(-st, 0.0), "cf_lt": cf_lt + max(-lt, 0.0)}


class AngelOneFrictions:
    """Cost rates by date, realised-gain buckets by fiscal year, and the
    running tallies the report prints."""

    def __init__(self):
        self.st_by_fy: dict[str, float] = defaultdict(float)
        self.lt_by_fy: dict[str, float] = defaultdict(float)
        self.cf_st = 0.0
        self.cf_lt = 0.0
        self.total_costs = 0.0
        self.total_tax = 0.0
        self.tax_rows: list[dict] = []

    # ------------------------------------------------------------ costs

    def buy_rate(self, date_iso: str) -> float:
        b = BROKERAGE if date_iso >= BROKERAGE_FROM else 0.0
        return STT + TXN + SEBI + STAMP + b + GST * (b + TXN + SEBI)

    def sell_rate(self, date_iso: str) -> float:
        b = BROKERAGE if date_iso >= BROKERAGE_FROM else 0.0
        return STT + TXN + SEBI + b + GST * (b + TXN + SEBI)

    def buy_split(self, amount: float, date_iso: str) -> tuple[float, float]:
        """Of the cash allocated, what buys shares and what the charges
        eat: notional + charges = amount."""
        notional = amount / (1 + self.buy_rate(date_iso))
        cost = amount - notional
        self.total_costs += cost
        return notional, cost

    def sell_split(self, gross: float, date_iso: str) -> tuple[float, float]:
        """Net proceeds and charges on a sale of `gross` value."""
        cost = gross * self.sell_rate(date_iso)
        self.total_costs += cost
        return gross - cost, cost

    # ------------------------------------------------------------- tax

    def on_sale(self, entry_date: str, exit_date: str,
                entry_px: float, exit_px: float, shares: float) -> None:
        gain = (exit_px - entry_px) * shares
        held = (dt.date.fromisoformat(exit_date)
                - dt.date.fromisoformat(entry_date)).days
        fy = fy_label(exit_date)
        if held > LT_DAYS:
            self.lt_by_fy[fy] += gain
        else:
            self.st_by_fy[fy] += gain

    def settle_fy(self, fy: str, paid_on: str) -> dict:
        r = offset_and_tax(self.st_by_fy.pop(fy, 0.0),
                           self.lt_by_fy.pop(fy, 0.0),
                           self.cf_st, self.cf_lt)
        self.cf_st, self.cf_lt = r["cf_st"], r["cf_lt"]
        self.total_tax += r["tax"]
        self.tax_rows.append({"fy": fy, "paid_on": paid_on, **r})
        return r

    def accrued(self) -> dict:
        """Tax that WOULD be due on fiscal years not yet settled —
        the final partial year's liability, reported, never hidden."""
        st = sum(self.st_by_fy.values())
        lt = sum(self.lt_by_fy.values())
        return offset_and_tax(st, lt, self.cf_st, self.cf_lt)
