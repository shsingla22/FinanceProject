"""
quant_signals.py — compute the QUANTITATIVE parameter signals for a company
from the repo's long-format financial CSVs.

Covers the computable side of every quantitative / hybrid parameter in
parameters.yaml. For parameters whose data is not separable in the source
(R&D, A&P, growth-vs-maintenance capex split), the engine returns
`data_available: False` so the qualitative layer knows to take over.

Design notes:
- Pure functions over pandas frames; the loaders are the only I/O.
- Data location is DISCOVERED (base path + universe), never hard-coded, so the
  same skill works for Nifty500, NiftyTotalMarket, or any same-layout universe.
- Every returned signal carries `evidence` (the raw numbers used) so the
  explainability layer can cite them — nothing is a bare score.

Returns, per company, a dict keyed by parameter id -> {value, direction,
data_available, evidence, note}. Scoring lives in scoring.py (kept separate so
signals stay auditable and testable independently).
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import pandas as pd

SKILL_ROOT = Path(__file__).resolve().parent.parent
# India/ is three levels up from scripts/: BusinessAnalysis -> Skills -> India
INDIA_ROOT = SKILL_ROOT.parent.parent

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


# ----------------------------------------------------------------- loaders
def _long_path(base: Path, statement_dir: str, universe: str, fname: str) -> Path:
    return base / statement_dir / universe / fname


def load_statement(base: Path, statement_dir: str, universe: str, fname: str,
                   value_col: str, item_col: str = "line_item") -> pd.DataFrame:
    """Load a long CSV and pivot to symbol x year x item. Missing file -> empty."""
    path = _long_path(base, statement_dir, universe, fname)
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_csv(path)
    if df.empty:
        return df
    return df


def _pivot_symbol(df: pd.DataFrame, sym: str, item_col: str, value_col: str) -> pd.DataFrame:
    sub = df[df["nse_symbol"] == sym]
    if sub.empty:
        return pd.DataFrame()
    piv = sub.pivot_table(index="year", columns=item_col, values=value_col,
                          aggfunc="first")
    return piv


def _year_key(y: str):
    try:
        m, yr = str(y).split()
        return int(yr) * 100 + MONTHS.get(m, 0)
    except Exception:
        return 0


def _ordered_years(piv: pd.DataFrame) -> list:
    return sorted(piv.index, key=_year_key)


def _num(piv: pd.DataFrame, year, item):
    if piv.empty or item not in piv.columns or year not in piv.index:
        return None
    v = piv.at[year, item]
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _cagr(end, start, years):
    if end is None or start is None or start <= 0 or end <= 0 or years <= 0:
        return None
    return (end / start) ** (1.0 / years) - 1.0


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def _std(xs):
    xs = [x for x in xs if x is not None]
    if len(xs) < 2:
        return None
    mu = sum(xs) / len(xs)
    return (sum((x - mu) ** 2 for x in xs) / (len(xs) - 1)) ** 0.5


# ----------------------------------------------------------------- engine
def compute(sym: str, base: Path = INDIA_ROOT,
            universe: str = "NiftyTotalMarket") -> dict:
    bs = load_statement(base, "BalanceSheet", universe,
                        "_all_balance_sheets_long.csv", "value_rs_cr")
    pl = load_statement(base, "ProfitStatement", universe,
                        "_all_profit_loss_long.csv", "value")
    cf = load_statement(base, "CashFlow", universe,
                        "_all_cash_flow_long.csv", "value_rs_cr")
    wc = load_statement(base, "WorkingCapital", universe,
                        "_all_working_capital_long.csv", "value", "metric")

    bsp = _pivot_symbol(bs, sym, "line_item", "value_rs_cr") if not bs.empty else pd.DataFrame()
    plp = _pivot_symbol(pl, sym, "line_item", "value") if not pl.empty else pd.DataFrame()
    cfp = _pivot_symbol(cf, sym, "line_item", "value_rs_cr") if not cf.empty else pd.DataFrame()
    wcp = _pivot_symbol(wc, sym, "metric", "value") if not wc.empty else pd.DataFrame()

    out: dict = {}

    def sig(pid, value, direction, evidence, available=True, note=""):
        out[pid] = {"value": value, "direction": direction,
                    "data_available": available, "evidence": evidence, "note": note}

    # ---- shared references
    pl_years = _ordered_years(plp)
    bs_years = _ordered_years(bsp)
    latest_pl = pl_years[-1] if pl_years else None
    latest_bs = bs_years[-1] if bs_years else None

    # ============================ ROC.profit_margin
    if plp.empty:
        sig("ROC.profit_margin", None, "maximize", {}, available=False,
            note="no P&L data")
    else:
        opm_series = [_num(plp, y, "OPM %") for y in pl_years]
        gm_series = []
        for y in pl_years:
            mat = _num(plp, y, "Material Cost %")
            gm_series.append(100 - mat if mat is not None else None)
        opm_latest = _num(plp, latest_pl, "OPM %")
        sig("ROC.profit_margin",
            {"opm_latest": opm_latest, "opm_mean": _mean(opm_series),
             "opm_std": _std(opm_series), "gross_margin_proxy_latest": gm_series[-1] if gm_series else None},
            "maximize",
            {"opm_series": opm_series, "gross_margin_proxy_series": gm_series},
            note="GM proxied as 100 - Material Cost %; low opm_std is better (stable margins)")

    # ============================ ROC.asset_turn
    sales_latest = _num(plp, latest_pl, "Sales")
    ta_latest = _num(bsp, latest_bs, "Total Assets")
    at = (sales_latest / ta_latest) if (sales_latest and ta_latest) else None
    sig("ROC.asset_turn", at, "maximize",
        {"sales_latest": sales_latest, "total_assets_latest": ta_latest},
        available=at is not None,
        note="Sales / Total Assets; asset-light (high) preferred, needs a moat too")

    # ============================ ROC.headline (return on capital / CROCI proxy)
    op_latest = _num(plp, latest_pl, "Operating Profit")
    eq = _num(bsp, latest_bs, "Equity Capital")
    res = _num(bsp, latest_bs, "Reserves")
    bor = _num(bsp, latest_bs, "Borrowings")
    cfo_years = _ordered_years(cfp)
    cfo_latest = _num(cfp, cfo_years[-1], "Cash from Operating Activity") if cfo_years else None
    cap_base = None
    roce_proxy = None
    croci_proxy = None
    if None not in (eq, res, bor) and (eq + res + bor) > 0:
        cap_base = eq + res + bor
        if op_latest is not None:
            roce_proxy = op_latest / cap_base
        if cfo_latest is not None:
            croci_proxy = cfo_latest / cap_base  # cash return on capital, pre-goodwill-adj
    roce_pct_reported = _num(wcp, _ordered_years(wcp)[-1], "ROCE %") if not wcp.empty and _ordered_years(wcp) else None
    sig("ROC.headline",
        {"roce_proxy": roce_proxy, "croci_proxy": croci_proxy,
         "roce_pct_reported": roce_pct_reported},
        "maximize",
        {"operating_profit": op_latest, "cfo_latest": cfo_latest,
         "capital_base": cap_base},
        available=(roce_proxy is not None or croci_proxy is not None),
        note="CROCI proxy = CFO / (Equity+Reserves+Borrowings); goodwill adj not applied (flag)")

    # ============================ CAP.working_capital_cost
    if wcp.empty:
        sig("CAP.working_capital_cost", None, "minimize", {}, available=False,
            note="no working-capital data")
    else:
        wy = _ordered_years(wcp)
        ccc_series = [_num(wcp, y, "Cash Conversion Cycle") for y in wy]
        wcd_series = [_num(wcp, y, "Working Capital Days") for y in wy]
        ccc_latest = ccc_series[-1] if ccc_series else None
        ccc_trend = None
        if len(ccc_series) >= 4 and ccc_series[-1] is not None and ccc_series[-4] is not None:
            ccc_trend = ccc_series[-1] - ccc_series[-4]  # +ve = deteriorating
        sig("CAP.working_capital_cost",
            {"ccc_latest": ccc_latest, "ccc_3y_change": ccc_trend,
             "working_capital_days_latest": wcd_series[-1] if wcd_series else None},
            "minimize",
            {"ccc_series": ccc_series, "wcd_series": wcd_series},
            note="Low/negative CCC & WC days preferred; +ve 3y change = deteriorating")

    # ============================ CAP.growth_capex (total capex intensity anchor)
    if cfp.empty or plp.empty:
        sig("CAP.growth_capex", None, "maximize", {}, available=False,
            note="capex split needs mgmt commentary; total capex needs CF+P&L")
    else:
        cy = _ordered_years(cfp)
        capex_series = [_num(cfp, y, "Fixed assets purchased") for y in cy]
        capex_latest = capex_series[-1] if capex_series else None
        # capex intensity = |capex| / sales
        capex_int = None
        if capex_latest is not None and sales_latest:
            capex_int = abs(capex_latest) / sales_latest
        sig("CAP.growth_capex",
            {"capex_intensity_latest": capex_int, "capex_latest_rs_cr": capex_latest},
            "maximize",
            {"capex_series": capex_series, "sales_latest": sales_latest},
            note="Total capex intensity only; GROWTH-vs-maintenance split is qualitative")

    # ============================ CAP.mergers_acquisitions (cash outflow proxy)
    if cfp.empty:
        sig("CAP.mergers_acquisitions", None, "context", {}, available=False,
            note="M&A intent + OPM-post-deal are qualitative; CF gives net investment only")
    else:
        cy = _ordered_years(cfp)
        inv_purchased = [_num(cfp, y, "Investments purchased") for y in cy]
        inv_sold = [_num(cfp, y, "Investments sold") for y in cy]
        sig("CAP.mergers_acquisitions",
            {"net_investment_latest": (
                (inv_purchased[-1] or 0) + (inv_sold[-1] or 0)) if cy else None},
            "context",
            {"investments_purchased": inv_purchased, "investments_sold": inv_sold},
            note="Proxy only; true bolt-on vs transformational + acquiree OPM are qualitative")

    # ============================ CAP.shareholder_distribution
    if cfp.empty:
        sig("CAP.shareholder_distribution", None, "context", {}, available=False,
            note="no cash-flow data")
    else:
        cy = _ordered_years(cfp)
        div = [_num(cfp, y, "Dividends paid") for y in cy]
        shares = [_num(cfp, y, "Proceeds from shares") for y in cy]  # -ve => buyback
        buyback_latest = shares[-1] if shares else None
        sig("CAP.shareholder_distribution",
            {"dividends_paid_latest": div[-1] if div else None,
             "share_proceeds_latest": buyback_latest,
             "buyback_indicated": (buyback_latest is not None and buyback_latest < 0)},
            "context",
            {"dividends_series": div, "share_proceeds_series": shares},
            note="Buyback indicated when Proceeds from shares is negative; valuation-timing is qualitative")

    # ============================ CAP.advertising_promotion (not separable)
    sig("CAP.advertising_promotion", None, "context", {}, available=False,
        note="A&P not separable in standard P&L; extract from annual report / concalls")

    # ============================ CAP.research_development (not separable)
    sig("CAP.research_development", None, "context", {}, available=False,
        note="R&D not separable in standard P&L; extract from annual report / concalls")

    # ============================ GRW.persistence (growth consistency)
    if plp.empty or len(pl_years) < 4:
        sig("GRW.persistence", None, "stable", {}, available=False,
            note="need >=4 years of Sales/Net Profit")
    else:
        sales = [_num(plp, y, "Sales") for y in pl_years]
        yoy = []
        for i in range(1, len(sales)):
            if sales[i] and sales[i - 1] and sales[i - 1] > 0:
                yoy.append(sales[i] / sales[i - 1] - 1.0)
            else:
                yoy.append(None)
        n = len(sales)
        sales_cagr = _cagr(sales[-1], sales[0], n - 1)
        sig("GRW.persistence",
            {"sales_cagr": sales_cagr, "yoy_mean": _mean(yoy),
             "yoy_std": _std(yoy),
             "in_10_15_band": (sales_cagr is not None and 0.10 <= sales_cagr <= 0.15)},
            "stable",
            {"sales_series": sales, "yoy_series": yoy},
            note="Consistent ~10-15% with LOW yoy_std is the target; level alone is not enough")

    # ============================ GRW.pricing_mix_volume (margin-vs-volume decomposition hint)
    if plp.empty or len(pl_years) < 4:
        sig("GRW.pricing_mix_volume", None, "context", {}, available=False,
            note="pricing/mix vs volume split needs mgmt commentary")
    else:
        sales = [_num(plp, y, "Sales") for y in pl_years]
        opm = [_num(plp, y, "OPM %") for y in pl_years]
        sales_cagr = _cagr(sales[-1], sales[0], len(sales) - 1)
        opm_delta = (opm[-1] - opm[0]) if (opm[-1] is not None and opm[0] is not None) else None
        sig("GRW.pricing_mix_volume",
            {"sales_cagr": sales_cagr, "opm_change_over_window": opm_delta},
            "context",
            {"sales_series": sales, "opm_series": opm},
            note="Rising OPM alongside growth hints price/mix (good) vs flat OPM hints volume-led")

    # ============================ GRW.market_share_gain (growth vs a market anchor -> qualitative)
    sig("GRW.market_share_gain", None, "context", {}, available=False,
        note="requires market-size / peer data; assess qualitatively from concalls")

    # ============================ IND.barriers_entry_rationality (pricing rationality proxy)
    if plp.empty:
        sig("IND.barriers_entry_rationality", None, "maximize", {}, available=False)
    else:
        opm = [_num(plp, y, "OPM %") for y in pl_years]
        sig("IND.barriers_entry_rationality",
            {"opm_std": _std(opm)},
            "maximize",
            {"opm_series": opm},
            note="Stable margins (low opm_std) are consistent with rational pricing / few entrants")

    # ============================ CUS.intangible_benefits (gross-margin power proxy)
    if plp.empty:
        sig("CUS.intangible_benefits", None, "maximize", {}, available=False)
    else:
        mat = _num(plp, latest_pl, "Material Cost %")
        gm = (100 - mat) if mat is not None else None
        sig("CUS.intangible_benefits", {"gross_margin_proxy": gm}, "maximize",
            {"material_cost_pct": mat},
            available=gm is not None,
            note="High GM proxy is consistent with intangible-driven pricing power")

    # ============================ MOAT.technology (R&D intensity -> not separable)
    sig("MOAT.technology", None, "maximize", {}, available=False,
        note="R&D % not separable in standard P&L; extract from annual report / concalls")

    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("symbol")
    ap.add_argument("--universe", default="NiftyTotalMarket")
    ap.add_argument("--base", default=str(INDIA_ROOT))
    args = ap.parse_args()
    res = compute(args.symbol, base=Path(args.base), universe=args.universe)
    import json
    print(json.dumps(res, indent=2, default=str))
    avail = sum(1 for v in res.values() if v["data_available"])
    print(f"\n# {args.symbol}: {avail}/{len(res)} quantitative signals had data",
          flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
