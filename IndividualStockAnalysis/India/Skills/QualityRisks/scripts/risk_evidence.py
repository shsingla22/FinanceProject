"""
risk_evidence.py — computable risk fingerprints for the QualityRisks skill.

Reads the NiftyTotalMarket long-format CSVs (balance sheet, P&L, cash flow,
working capital) and computes, per company, every check listed in
reference/checklist.yaml. Each check returns:

    {flagged: bool|None, value, explanation}

flagged=True means the risk's numeric fingerprint IS PRESENT (this is a
risk skill — a "pass" is bad news). flagged=None means the data needed was
unavailable (honest abstention). The explanation is templated from the SAME
numbers that decided the check — explainability captured at compute time.
"""

from __future__ import annotations

import math
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent          # .../India
UNIVERSE = "NiftyTotalMarket"

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

_frames: dict = {}


def _load(base: Path, universe: str):
    key = (str(base), universe)
    if key in _frames:
        return _frames[key]
    def rd(sub, fname):
        p = base / sub / universe / fname
        return pd.read_csv(p) if p.exists() else pd.DataFrame()
    frames = {
        "bs": rd("BalanceSheet", "_all_balance_sheets_long.csv"),
        "pl": rd("ProfitStatement", "_all_profit_loss_long.csv"),
        "cf": rd("CashFlow", "_all_cash_flow_long.csv"),
        "wc": rd("WorkingCapital", "_all_working_capital_long.csv"),
    }
    _frames[key] = frames
    return frames


def _year_key(y):
    try:
        m, yr = str(y).split()
        return int(yr) * 100 + MONTHS.get(m, 0)
    except Exception:
        return 0


def _series(df, sym, item, value_col, item_col="line_item"):
    if df.empty:
        return []
    sub = df[(df["nse_symbol"] == sym) & (df[item_col] == item)]
    if sub.empty:
        return []
    sub = sub.sort_values("year", key=lambda s: s.map(_year_key))
    out = []
    for _, r in sub.iterrows():
        v = r[value_col]
        out.append(None if (v is None or (isinstance(v, float) and math.isnan(v)))
                   else float(v))
    return out


def _clean(xs):
    return [x for x in xs if x is not None]


def _cagr(xs):
    c = _clean(xs)
    if len(c) < 3 or c[0] <= 0 or c[-1] <= 0:
        return None
    return (c[-1] / c[0]) ** (1 / (len(c) - 1)) - 1


def _std(xs):
    c = _clean(xs)
    if len(c) < 3:
        return None
    mu = sum(c) / len(c)
    return (sum((x - mu) ** 2 for x in c) / (len(c) - 1)) ** 0.5


def gather(sym: str, base: Path = INDIA, universe: str = UNIVERSE) -> dict:
    """All raw series a company's risk checks need, loaded once."""
    f = _load(base, universe)
    gm = []
    for m in _series(f["pl"], sym, "Material Cost %", "value"):
        gm.append(100 - m if m is not None else None)
    return {
        "sales": _series(f["pl"], sym, "Sales", "value"),
        "opm": _series(f["pl"], sym, "OPM %", "value"),
        "gm": gm,
        "op": _series(f["pl"], sym, "Operating Profit", "value"),
        "cfo": _series(f["cf"], sym, "Cash from Operating Activity", "value_rs_cr"),
        "capex": _series(f["cf"], sym, "Fixed assets purchased", "value_rs_cr"),
        "debtor_days": _series(f["wc"], sym, "Debtor Days", "value", "metric"),
        "roce": _series(f["wc"], sym, "ROCE %", "value", "metric"),
        "borrowing": _series(f["bs"], sym, "Borrowings", "value_rs_cr"),
        "equity": _series(f["bs"], sym, "Equity Capital", "value_rs_cr"),
        "reserves": _series(f["bs"], sym, "Reserves", "value_rs_cr"),
    }


def _check(flagged, value, explanation):
    return {"flagged": flagged, "value": value, "explanation": explanation}


def _yoy(xs):
    c = _clean(xs)
    out = []
    for a, b in zip(c, c[1:]):
        if a and a > 0:
            out.append((b - a) / a)
    return out


def compute_checks(sym: str, base: Path = INDIA, universe: str = UNIVERSE) -> dict:
    """Every risk fingerprint + fragility check for one company."""
    g = gather(sym, base, universe)
    out: dict = {}

    sales = _clean(g["sales"])
    opm = _clean(g["opm"])
    gm = _clean(g["gm"])

    # ---------------- cyclicality fingerprints
    yoy = _yoy(g["sales"])
    if len(yoy) >= 4:
        neg = sum(1 for x in yoy if x < -0.02)
        swing = _std([x * 100 for x in yoy])
        flagged = neg >= 4 or (swing is not None and swing >= 40)
        if flagged and neg >= 4:
            expl = (f"Sales actually FELL in {neg} of the last {len(yoy)} "
                    f"years — revenue moves in cycles, it does not compound "
                    f"steadily.")
        elif flagged:
            expl = (f"Year-to-year sales growth swings by ±{swing:.0f} "
                    f"percentage points — boom-and-bust revenue, not a "
                    f"steady compounder.")
        else:
            expl = (f"Sales fell in only {neg} of the last {len(yoy)} years "
                    f"with swings of ±{swing:.0f} points — no pronounced "
                    f"boom-and-bust signature in revenue."
                    if swing is not None else
                    f"Sales fell in only {neg} of the last {len(yoy)} years "
                    f"— no pronounced boom-and-bust signature in revenue.")
        out["sales_swings"] = _check(flagged, {"neg_years": neg,
                                               "yoy_swing": swing}, expl)
    else:
        out["sales_swings"] = _check(None, None, "Not enough sales history.")

    opm_std = _std(g["opm"])
    if opm and opm_std is not None:
        flagged = opm_std >= 8
        lo, hi = min(opm), max(opm)
        if flagged:
            expl = (f"Operating margin has ranged from {lo:.0f}% to {hi:.0f}% "
                    f"(swinging ±{opm_std:.1f} points a year) — margins "
                    f"fluctuate a lot, the signature of a cyclical business.")
        else:
            expl = (f"Operating margin stayed between {lo:.0f}% and {hi:.0f}% "
                    f"(±{opm_std:.1f} points a year) — swings within the "
                    f"normal range, no extreme boom-and-bust profile.")
        out["margin_swings"] = _check(flagged, {"opm_low": lo, "opm_high": hi,
                                                "swing": opm_std}, expl)
    else:
        out["margin_swings"] = _check(None, None, "No margin history.")

    capex = [abs(x) for x in _clean(g["capex"])]
    if len(capex) >= 5 and len(sales) >= 5:
        n = min(len(capex), len(sales))
        ratio = [c / s for c, s in zip(capex[-n:], sales[-n:]) if s > 0]
        if len(ratio) >= 5:
            med = sorted(ratio)[len(ratio) // 2]
            peak = max(ratio)
            flagged = med > 0 and peak >= max(2.5 * med, 0.10) and peak >= 0.10
            if flagged:
                expl = (f"Capital spending spiked to {peak:.0%} of sales in "
                        f"its heaviest year, versus a normal {med:.0%} — the "
                        f"over-investment-in-the-expansion pattern that "
                        f"starves future returns.")
            else:
                expl = (f"Capital spending stayed near {med:.0%} of sales "
                        f"with no runaway expansion year (peak {peak:.0%}).")
            out["capex_burst"] = _check(flagged, {"median": med, "peak": peak},
                                        expl)
        else:
            out["capex_burst"] = _check(None, None, "Insufficient capex data.")
    else:
        out["capex_burst"] = _check(None, None, "Insufficient capex data.")

    # ---------------- competitive-erosion fingerprints
    if len(opm) >= 6:
        peak = max(opm)
        latest = opm[-1]
        flagged = peak >= 10 and latest <= 0.6 * peak
        if flagged:
            expl = (f"Operating margin has collapsed from a peak of "
                    f"{peak:.0f}% to {latest:.0f}% — the Nobel-Biocare-style "
                    f"fingerprint of a premium being competed away.")
        else:
            expl = (f"Operating margin ({latest:.0f}%) remains near its "
                    f"historical peak ({peak:.0f}%) — no collapse in the "
                    f"premium.")
        out["margin_collapse"] = _check(flagged, {"peak": peak,
                                                  "latest": latest}, expl)
    else:
        out["margin_collapse"] = _check(None, None, "Not enough margin history.")

    if len(gm) >= 6:
        early = sum(gm[:3]) / 3
        late = sum(gm[-3:]) / 3
        flagged = late - early <= -3
        if flagged:
            expl = (f"The share of each sale kept after direct input costs "
                    f"fell from about {early:.0f}% to {late:.0f}% — pricing "
                    f"is being competed away at the gross level.")
        else:
            expl = (f"The share of each sale kept after direct input costs "
                    f"held near {late:.0f}% (was {early:.0f}%) — no gross-"
                    f"level price erosion.")
        out["gross_margin_erosion"] = _check(flagged, {"early": early,
                                                       "late": late}, expl)
    else:
        out["gross_margin_erosion"] = _check(None, None, "No input-cost data.")

    if len(opm) >= 6:
        early = sum(opm[:3]) / 3
        late = sum(opm[-3:]) / 3
        flagged = late - early <= -3
        if flagged:
            expl = (f"Operating margin drifted down from about {early:.0f}% "
                    f"to {late:.0f}% — steady profit erosion, the mark of "
                    f"rising competitive pressure.")
        else:
            expl = (f"Operating margin held (about {early:.0f}% then "
                    f"{late:.0f}%) — no drift down under competition.")
        out["pricing_pressure"] = _check(flagged, {"early": early,
                                                   "late": late}, expl)
    else:
        out["pricing_pressure"] = _check(None, None, "Not enough margin history.")

    if len(sales) >= 8:
        half = len(sales) // 2
        first = _cagr(sales[:half + 1])
        second = _cagr(sales[half:])
        if first is not None and second is not None:
            flagged = first > 0.08 and second < min(0.08, first / 2)
            if flagged:
                expl = (f"Growth has stalled: sales compounded at "
                        f"{first:.0%} a year in the first half of the record "
                        f"but only {second:.0%} recently — demand may be "
                        f"structurally fading.")
            else:
                expl = (f"Growth is holding up: {first:.0%} a year earlier, "
                        f"{second:.0%} recently — no structural stall.")
            out["growth_deceleration"] = _check(flagged, {"first": first,
                                                          "second": second},
                                                expl)
        else:
            out["growth_deceleration"] = _check(None, None,
                                                "Insufficient sales history.")
    else:
        out["growth_deceleration"] = _check(None, None,
                                            "Insufficient sales history.")

    dd = _clean(g["debtor_days"])
    if len(dd) >= 6:
        early = sum(dd[:3]) / 3
        late = sum(dd[-3:]) / 3
        flagged = late - early >= 15 and late >= 45
        day = lambda n: f"{n:.0f} day" + ("" if round(n) == 1 else "s")
        if flagged:
            expl = (f"Customers now take about {day(late)} to pay, up "
                    f"from {early:.0f} — lengthening collection terms are "
                    f"how weak bargaining power against concentrated "
                    f"customers shows up in the numbers.")
        else:
            expl = (f"Customers pay in about {day(late)} (was "
                    f"{early:.0f}) — no sign of weakening bargaining power "
                    f"in collection terms.")
        out["receivables_creep"] = _check(flagged, {"early": early,
                                                    "late": late}, expl)
    else:
        out["receivables_creep"] = _check(None, None,
                                          "No receivables history.")

    # ---------------- fragility checks (cross-cutting)
    borrow = _clean(g["borrowing"])
    eq = _clean(g["equity"])
    res = _clean(g["reserves"])
    if borrow and eq and res:
        worth_now = eq[-1] + res[-1]
        worth_early = (eq[0] + res[0]) if (eq[0] + res[0]) > 0 else None
        if worth_now > 0:
            lev_now = borrow[-1] / worth_now
            lev_early = (borrow[0] / worth_early) if worth_early else None
            flagged = lev_now >= 1.0 and (lev_early is None or
                                          lev_now - lev_early >= 0.3)
            if flagged:
                expl = (f"Borrowings are now {lev_now:.1f}× shareholders' "
                        f"funds"
                        + (f" (up from {lev_early:.1f}×)" if lev_early
                           is not None else "")
                        + " — a leveraged balance sheet leaves little room "
                          "when any of the risks above bites.")
            else:
                expl = (f"Borrowings are {lev_now:.1f}× shareholders' funds "
                        f"— the balance sheet is not the problem.")
            out["leverage_rise"] = _check(flagged, {"now": lev_now,
                                                    "early": lev_early}, expl)
        else:
            out["leverage_rise"] = _check(None, None, "No net-worth data.")
    else:
        out["leverage_rise"] = _check(None, None, "No borrowing data.")

    cfo = _clean(g["cfo"])
    op = _clean(g["op"])
    if len(cfo) >= 6 and len(op) >= 6:
        n = min(len(cfo), len(op))
        cfo_n, op_n = cfo[-n:], op[-n:]
        def conv(cs, os):
            pairs = [(c, o) for c, o in zip(cs, os) if o > 0]
            return (sum(c for c, _ in pairs) / sum(o for _, o in pairs)
                    if pairs else None)
        early_c = conv(cfo_n[:3], op_n[:3])
        late_c = conv(cfo_n[-3:], op_n[-3:])
        if early_c is not None and late_c is not None:
            flagged = late_c <= 0.5 and late_c <= early_c - 0.2
            if flagged:
                expl = (f"Only about {late_c:.0%} of recent operating profit "
                        f"became cash (was {early_c:.0%}) — profits are "
                        f"getting stuck in paper, an early stress signal.")
            else:
                expl = (f"About {late_c:.0%} of recent operating profit "
                        f"became cash — earnings are still backed by cash.")
            out["cash_conversion_slippage"] = _check(
                flagged, {"early": early_c, "late": late_c}, expl)
        else:
            out["cash_conversion_slippage"] = _check(None, None,
                                                     "No profitable years to compare.")
    else:
        out["cash_conversion_slippage"] = _check(None, None,
                                                 "Insufficient cash-flow history.")

    roce = _clean(g["roce"])
    if len(roce) >= 6:
        early = sum(roce[:3]) / 3
        late = sum(roce[-3:]) / 3
        flagged = late - early <= -5 and late < 15
        if flagged:
            expl = (f"Returns on capital slid from about {early:.0f}% to "
                    f"{late:.0f}% — the business is earning less and less on "
                    f"the money invested in it.")
        elif late - early >= 2:
            expl = (f"Returns on capital improved from about {early:.0f}% "
                    f"to {late:.0f}% — the business is earning more on its "
                    f"capital, not less.")
        elif late - early <= -2:
            expl = (f"Returns on capital moderated from about {early:.0f}% "
                    f"to {late:.0f}% — lower, but still well clear of the "
                    f"deep slide this check looks for.")
        else:
            expl = (f"Returns on capital held near {late:.0f}% (was about "
                    f"{early:.0f}%) — no slide in what the business earns "
                    f"on its capital.")
        out["roce_slide"] = _check(flagged, {"early": early, "late": late},
                                   expl)
    else:
        out["roce_slide"] = _check(None, None, "No return-on-capital history.")

    return out
