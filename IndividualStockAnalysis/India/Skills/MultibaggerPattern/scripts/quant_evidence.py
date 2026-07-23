"""
quant_evidence.py — computable evidence checks for the multibagger patterns.

Reads the NiftyTotalMarket long-format CSVs (balance sheet, P&L, cash flow,
working capital) and computes, per company, every check listed in
reference/checklist.yaml. Each check returns:

    {passed: bool|None, value, explanation}

The explanation is templated from the SAME numbers that decided the check —
explainability is captured at compute time, never narrated afterwards.
`passed=None` means the data needed for the check was unavailable (honest
abstention, not a fail).

Pure functions over pandas frames; data location discovered via base+universe.
"""

from __future__ import annotations

import math
import re
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


def _cagr(xs, min_years=4):
    c = _clean(xs)
    if len(c) < min_years or c[0] <= 0 or c[-1] <= 0:
        return None
    return (c[-1] / c[0]) ** (1 / (len(c) - 1)) - 1


def _std(xs):
    c = _clean(xs)
    if len(c) < 3:
        return None
    mu = sum(c) / len(c)
    return (sum((x - mu) ** 2 for x in c) / (len(c) - 1)) ** 0.5


def gather(sym: str, base: Path = INDIA, universe: str = UNIVERSE) -> dict:
    """All raw series a company's checks need, loaded once."""
    f = _load(base, universe)
    gm = []
    mat = _series(f["pl"], sym, "Material Cost %", "value")
    for m in mat:
        gm.append(100 - m if m is not None else None)
    return {
        "sales": _series(f["pl"], sym, "Sales", "value"),
        "opm": _series(f["pl"], sym, "OPM %", "value"),
        "gm": gm,
        "op": _series(f["pl"], sym, "Operating Profit", "value"),
        "cfo": _series(f["cf"], sym, "Cash from Operating Activity", "value_rs_cr"),
        "capex": _series(f["cf"], sym, "Fixed assets purchased", "value_rs_cr"),
        "wcd": _series(f["wc"], sym, "Working Capital Days", "value", "metric"),
        "ccc": _series(f["wc"], sym, "Cash Conversion Cycle", "value", "metric"),
        "roce": _series(f["wc"], sym, "ROCE %", "value", "metric"),
        "advances": _series(f["bs"], sym, "Advance from Customers", "value_rs_cr"),
        "total_assets": _series(f["bs"], sym, "Total Assets", "value_rs_cr"),
    }


def _check(passed, value, explanation):
    return {"passed": passed, "value": value, "explanation": explanation}


def compute_checks(sym: str, base: Path = INDIA, universe: str = UNIVERSE) -> dict:
    """Every core + pattern quant check for one company."""
    g = gather(sym, base, universe)
    out: dict = {}

    # ---------------- core principle gate
    cfo = _clean(g["cfo"])
    if len(cfo) >= 5:
        pos = sum(1 for x in cfo if x > 0)
        frac = pos / len(cfo)
        op = _clean(g["op"])
        conv = None
        if len(op) >= 5 and sum(op[-5:]) > 0 and len(cfo) >= 5:
            conv = sum(cfo[-5:]) / sum(op[-5:])
        expl = (f"Generated positive operating cash in {pos} of the last "
                f"{len(cfo)} years"
                + (f", converting about {conv:.0%} of operating profit into "
                   f"cash over the last five" if conv is not None else "") + ".")
        out["core_cash_generation"] = _check(frac >= 0.8 and (conv is None or conv >= 0.6),
                                             {"positive_years": pos, "of": len(cfo),
                                              "cash_conversion": conv}, expl)
    else:
        out["core_cash_generation"] = _check(None, None,
                                             "Not enough cash-flow history to judge.")

    roce = _clean(g["roce"])
    if len(roce) >= 4:
        med = sorted(roce)[len(roce) // 2]
        out["core_return_on_capital"] = _check(
            med >= 15, {"median_roce": med},
            f"Median return on capital employed of {med:.0f}% across "
            f"{len(roce)} years" + (" — comfortably above the 15% quality bar."
                                    if med >= 15 else
                                    " — below the 15% quality bar."))
    else:
        out["core_return_on_capital"] = _check(None, None,
                                               "Not enough return-on-capital history.")

    scagr = _cagr(g["sales"])
    if scagr is not None:
        out["core_growth"] = _check(
            scagr >= 0.08, {"sales_cagr": scagr},
            f"Sales grew about {scagr:.0%} a year over the period"
            + (" — a healthy growth runway." if scagr >= 0.08 else
               " — modest growth."))
    else:
        out["core_growth"] = _check(None, None, "Not enough sales history.")

    # ---------------- pattern checks
    ccc = _clean(g["ccc"])
    wcd = _clean(g["wcd"])
    if ccc or wcd:
        latest = (ccc or wcd)[-1]
        neg = latest <= 0
        near = latest <= 15
        out["negative_working_capital"] = _check(
            neg or near, {"cycle_days": latest},
            (f"Customers effectively fund the business — cash arrives "
             f"{abs(latest):.0f} days before suppliers are paid."
             if neg else
             f"Only about {latest:.0f} days of cash is tied up in the trade "
             f"cycle." if near else
             f"About {latest:.0f} days of cash is tied up in the trade cycle "
             f"— customers are not funding the business."))
    else:
        out["negative_working_capital"] = _check(None, None,
                                                 "No working-capital data.")

    capex = _clean(g["capex"])
    sales = _clean(g["sales"])
    if capex and sales and sales[-1] > 0:
        intensity = abs(capex[-1]) / sales[-1]
        out["low_capex_intensity"] = _check(
            intensity <= 0.06, {"capex_to_sales": intensity},
            f"Capital spending is about {intensity:.0%} of sales"
            + (" — growth needs little capital." if intensity <= 0.06 else
               " — growth is capital-hungry."))
    else:
        out["low_capex_intensity"] = _check(None, None, "No capital-spending data.")

    if len(cfo) >= 5:
        pos = sum(1 for x in cfo if x > 0)
        out["cash_conversion_strength"] = _check(
            pos / len(cfo) >= 0.9, {"positive_years": pos, "of": len(cfo)},
            f"Operating cash was positive in {pos} of {len(cfo)} years — "
            + ("the reliable cash engine recurring-revenue businesses show."
               if pos / len(cfo) >= 0.9 else "not fully consistent."))
    else:
        out["cash_conversion_strength"] = _check(None, None,
                                                 "Not enough cash-flow history.")

    opm = _clean(g["opm"])
    opm_std = _std(g["opm"])
    if opm and opm_std is not None:
        lvl = opm[-1]
        out["high_stable_margins"] = _check(
            lvl >= 18 and opm_std <= 5,
            {"operating_margin": lvl, "swing": opm_std},
            f"Operating margin of {lvl:.0f}% moving only ±{opm_std:.1f} points "
            f"a year" + (" — the steady, protected profitability these "
                         "patterns produce." if lvl >= 18 and opm_std <= 5 else
                         " — either too thin or too volatile for a protected "
                         "franchise."))
    else:
        out["high_stable_margins"] = _check(None, None, "No margin history.")

    if len(opm) >= 6:
        early = sum(opm[:3]) / 3
        late = sum(opm[-3:]) / 3
        delta = late - early
        out["rising_margins"] = _check(
            delta >= 2, {"early_avg": early, "late_avg": late, "change": delta},
            f"Operating margin moved from about {early:.0f}% (early years) to "
            f"{late:.0f}% (recent years)"
            + (" — the widening-profitability signature of pricing power / "
               "lock-in." if delta >= 2 else
               " — no widening trend." if delta > -2 else
               " — margins are ERODING, the opposite of pricing power."))
    else:
        out["rising_margins"] = _check(None, None, "Not enough margin history.")

    if roce and opm and opm_std is not None:
        med_roce = sorted(roce)[len(roce) // 2]
        ok = opm[-1] >= 22 and opm_std <= 4 and med_roce >= 25
        out["tollroad_economics"] = _check(
            ok, {"operating_margin": opm[-1], "swing": opm_std,
                 "median_roce": med_roce},
            f"Operating margin {opm[-1]:.0f}%, swings of ±{opm_std:.1f} points, "
            f"median return on capital {med_roce:.0f}%"
            + (" — the fat, calm, high-return economics of a business "
               "customers cannot skip." if ok else
               " — good but not the near-monopoly profile of a toll road."))
    else:
        out["tollroad_economics"] = _check(None, None, "Insufficient data.")

    gm = _clean(g["gm"])
    ta = _clean(g["total_assets"])
    if gm and sales and ta and ta[-1] > 0:
        turns = sales[-1] / ta[-1]
        med_roce = sorted(roce)[len(roce) // 2] if roce else None
        ok = gm[-1] <= 35 and turns >= 1.2 and (med_roce or 0) >= 15
        out["lowprice_economics"] = _check(
            ok, {"gross_margin": gm[-1], "asset_turns": turns,
                 "median_roce": med_roce},
            f"Keeps ₹{gm[-1]:.0f} of every ₹100 of sales after input costs, "
            f"but turns its assets {turns:.1f}× a year"
            + (f" with {med_roce:.0f}% returns on capital — thin margins made "
               f"up on volume, the low-price-winner profile." if ok else
               " — not the high-turnover, low-margin machine this pattern "
               "needs."))
    else:
        out["lowprice_economics"] = _check(None, None, "Insufficient data.")

    if gm:
        gm_now = gm[-1]
        out["high_gross_margin"] = _check(
            gm_now >= 45, {"gross_margin": gm_now},
            f"Keeps ₹{gm_now:.0f} of every ₹100 of sales after direct input "
            f"costs" + (" — room to fund brand, R&D and price leadership."
                        if gm_now >= 45 else " — limited pricing headroom."))
    else:
        out["high_gross_margin"] = _check(None, None, "No input-cost data.")

    if gm and scagr is not None:
        ok = gm[-1] >= 45 and scagr >= 0.08
        out["margin_funded_growth"] = _check(
            ok, {"gross_margin": gm[-1], "sales_cagr": scagr},
            f"High retained margin (₹{gm[-1]:.0f}/₹100) alongside {scagr:.0%} "
            f"yearly growth"
            + (" — the profitable-innovation flywheel: margins fund the "
               "spending that drives the growth." if ok else
               " — the flywheel is incomplete."))
    else:
        out["margin_funded_growth"] = _check(None, None, "Insufficient data.")

    if scagr is not None and len(opm) >= 6:
        early = sum(opm[:3]) / 3
        late = sum(opm[-3:]) / 3
        ok = scagr >= 0.12 and late >= early - 1
        if ok:
            expl = (f"Sales compounding at {scagr:.0%} while margins held or "
                    f"improved ({early:.0f}% → {late:.0f}%) — growth that was "
                    f"WON, not bought with price cuts.")
        elif scagr >= 0.12:
            expl = (f"Sales compounding at {scagr:.0%} but margins fell "
                    f"({early:.0f}% → {late:.0f}%) — growth may be bought with "
                    f"profitability, this pattern's red flag.")
        else:
            expl = (f"Sales compounding at {scagr:.0%} a year — below the "
                    f"12% pace the share-gainer pattern looks for.")
        out["growth_with_margins"] = _check(
            ok, {"sales_cagr": scagr, "margin_change": late - early}, expl)
    else:
        out["growth_with_margins"] = _check(None, None, "Insufficient data.")

    return out
