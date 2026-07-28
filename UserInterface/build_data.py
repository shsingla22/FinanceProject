"""
build_data.py — shared scoring library for the Business Analysis UI backend.

server.py imports score_params / series_for_chart / clean from here to run
the BusinessAnalysis skill (quant engine + scoring) at request time. The
main() entry point can still emit a full JSON snapshot to data/ if you ever
want an offline export:

    python3 UserInterface/build_data.py
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import pandas as pd
import yaml

REPO = Path(__file__).resolve().parent.parent
INDIA = REPO / "IndividualStockAnalysis" / "India"
SKILL = INDIA / "Skills" / "BusinessAnalysis"
OUT = Path(__file__).resolve().parent / "data"
UNIVERSE = "NiftyTotalMarket"

sys.path.insert(0, str(SKILL / "scripts"))
import quant_signals as Q  # noqa: E402
import scoring as S        # noqa: E402
import framework as F      # noqa: E402

# ---- cache the long-CSV loads so 742 compute() calls read each file once
_load_cache: dict = {}
_orig_load = Q.load_statement


def _cached_load(base, statement_dir, universe, fname, value_col, item_col="line_item"):
    key = (str(base), statement_dir, universe, fname)
    if key not in _load_cache:
        _load_cache[key] = _orig_load(base, statement_dir, universe, fname,
                                      value_col, item_col)
    return _load_cache[key]


Q.load_statement = _cached_load

# ---- quantitative -> score thresholds (reference/scoring_rubric.md)
TH = {
    "croci":      {"dir": "maximize", "strong": 0.25, "good": 0.15, "bad": 0.08, "weak": 0.04},
    "asset_turn": {"dir": "maximize", "strong": 1.5,  "good": 1.0,  "bad": 0.5,  "weak": 0.3},
    "opm_level":  {"dir": "maximize", "strong": 25,   "good": 15,   "bad": 8,    "weak": 3},
    "opm_std":    {"dir": "minimize", "strong": 2,    "good": 4,    "bad": 8,    "weak": 12},
    "ccc":        {"dir": "minimize", "strong": 0,    "good": 30,   "bad": 90,   "weak": 150},
    "yoy_std":    {"dir": "minimize", "strong": 0.05, "good": 0.10, "bad": 0.25, "weak": 0.40},
    "gm_proxy":   {"dir": "maximize", "strong": 60,   "good": 40,   "bad": 20,   "weak": 10},
}


def tmap(key, value):
    t = TH[key]
    return S.quant_to_score(value, t["dir"], t)


def score_params(sig: dict, fw) -> list:
    """Map the quant signals of one company to ParamScore objects for the
    quantitatively-scorable parameters. Every OTHER framework parameter is
    appended with score=None so module/overall coverage is honest (the
    qualitative playbook cannot run in a static build)."""
    ps = []

    def add(pid, module, nature, score, rationale, evidence, avail):
        ps.append(S.ParamScore(id=pid, module=module, nature=nature,
                               score=score, rationale=rationale,
                               evidence=evidence, sources=[],
                               quant_available=avail))

    # ROC.headline <- CROCI proxy (fallback ROCE proxy)
    v = sig["ROC.headline"]
    val = None
    if v["data_available"] and isinstance(v["value"], dict):
        val = v["value"].get("croci_proxy") or v["value"].get("roce_proxy")
    sc = tmap("croci", val)
    add("ROC.headline", "ROC", "quantitative", sc,
        (f"For every ₹100 of capital in the business (shareholders' funds + "
         f"borrowings), it generated ₹{val*100:.0f} of operating cash this "
         f"year — a {val:.0%} cash return on capital."
         if val is not None else
         "Not enough data to work out the cash return on capital."),
        v["evidence"] if v["data_available"] else {}, val is not None)

    # ROC.asset_turn
    v = sig["ROC.asset_turn"]
    val = v["value"] if v["data_available"] else None
    add("ROC.asset_turn", "ROC", "hybrid", tmap("asset_turn", val),
        (f"Every ₹1 of assets produces ₹{val:.2f} of sales — "
         + ("an asset-light business." if val >= 1.0 else
            "a fairly asset-heavy business." if val < 0.5 else
            "a moderate asset intensity.")
         if val is not None else "No data on asset intensity."),
        v["evidence"], val is not None)

    # ROC.profit_margin — mean of level score and stability score
    v = sig["ROC.profit_margin"]
    sc = None
    rat = "no P&L data"
    if v["data_available"] and isinstance(v["value"], dict):
        lvl = tmap("opm_level", v["value"].get("opm_latest"))
        stb = tmap("opm_std", v["value"].get("opm_std"))
        parts = [x for x in (lvl, stb) if x is not None]
        if parts:
            sc = S.clamp(round(sum(parts) / len(parts)))
            opm_now = v['value'].get('opm_latest')
            swing = round(v['value'].get('opm_std') or 0, 1)
            lvl_txt = (f"Out of every ₹100 of sales, ₹{opm_now:.0f} is "
                       f"operating profit. " if opm_now is not None else "")
            rat = (lvl_txt + f"Margins have moved about ±{swing} points a year "
                   + ("— very steady, a sign costs are under control."
                      if swing <= 4 else
                      "— sizeable swings, suggesting key costs are outside "
                      "management's control."))
    add("ROC.profit_margin", "ROC", "quantitative", sc, rat,
        v["evidence"] if v["data_available"] else {}, sc is not None)

    # CAP.working_capital_cost <- CCC latest
    v = sig["CAP.working_capital_cost"]
    val = None
    if v["data_available"] and isinstance(v["value"], dict):
        val = v["value"].get("ccc_latest")
    add("CAP.working_capital_cost", "CAP", "quantitative", tmap("ccc", val),
        ((f"Cash comes back {abs(val):.0f} "
          f"day{'s' if round(abs(val)) != 1 else ''} BEFORE suppliers need "
          f"to be paid — customers effectively fund the business (negative "
          f"working capital, a rare strength)." if val <= 0 else
          f"About {val:.0f} day{'s' if round(val) != 1 else ''} of cash "
          f"stays stuck between paying suppliers and collecting from customers"
          + (" — a short, healthy cycle." if val <= 30 else
             " — a long cycle that ties up capital."))
         if val is not None else "No working-capital data."),
        v["evidence"] if v["data_available"] else {}, val is not None)

    # GRW.persistence — stability score + band bonus
    v = sig["GRW.persistence"]
    sc = None
    rat = "insufficient history (<4y)"
    if v["data_available"] and isinstance(v["value"], dict):
        base = tmap("yoy_std", v["value"].get("yoy_std"))
        if base is not None:
            sc = base
            cagr = v["value"].get("sales_cagr")
            ystd = v["value"].get("yoy_std")
            if v["value"].get("in_10_15_band"):
                sc = S.clamp(sc + 1)
            rat = (f"Sales have grown about {cagr:.0%} a year on average"
                   if cagr is not None else "Average sales growth unavailable")
            if ystd is not None:
                rat += (", with very consistent year-to-year growth"
                        if ystd <= 0.10 else
                        ", but the growth is lumpy from year to year")
            if v["value"].get("in_10_15_band"):
                rat += (" — right inside the steady 10–15% band the framework "
                        "prizes most")
            rat += "."
    add("GRW.persistence", "GRW", "quantitative", sc, rat,
        v["evidence"] if v["data_available"] else {}, sc is not None)

    # IND.barriers_entry_rationality <- margin stability proxy
    v = sig["IND.barriers_entry_rationality"]
    val = None
    if v["data_available"] and isinstance(v["value"], dict):
        val = v["value"].get("opm_std")
    add("IND.barriers_entry_rationality", "IND", "hybrid", tmap("opm_std", val),
        ((f"Profit margins have barely moved over the years (±{val:.1f} points) "
          f"— consistent with rational pricing and few new competitors."
          if val <= 4 else
          f"Profit margins swing by ±{val:.1f} points — a hint of price wars, "
          f"cost shocks, or new entrants disturbing the industry.")
         if val is not None else "No margin history to judge industry stability."),
        v["evidence"] if v["data_available"] else {}, val is not None)

    # CUS.intangible_benefits <- gross-margin proxy
    v = sig["CUS.intangible_benefits"]
    val = None
    if v["data_available"] and isinstance(v["value"], dict):
        val = v["value"].get("gross_margin_proxy")
    add("CUS.intangible_benefits", "CUS", "hybrid", tmap("gm_proxy", val),
        ((f"The product has essentially no direct input costs — nearly all "
          f"of every ₹100 of sales is available for people, marketing and "
          f"profit (typical of software / internet platforms)."
          if val >= 95 else
          f"After direct input costs, the company keeps ₹{val:.0f} of every "
          f"₹100 of sales"
          + (" — pricing power customers are happy to pay for." if val >= 40 else
             " — thin pricing power; customers likely buy on price."))
         if val is not None else "No input-cost data to judge pricing power."),
        v["evidence"] if v["data_available"] else {}, val is not None)

    # Every remaining framework parameter -> unassessed (qualitative playbook
    # required); keeps coverage honest at N-assessed / 34.
    done = {p.id for p in ps}
    for p in fw.parameters:
        if p.id not in done:
            add(p.id, p.module, p.nature, None,
                "Needs a judgement call from the conference calls or annual "
                "reports — the numbers alone can't answer this.", {}, False)

    return ps


def clean(o):
    """JSON-safe: replace NaN with None recursively."""
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    return o


def series_for_chart(sig: dict) -> dict:
    out = {}
    pm = sig.get("ROC.profit_margin", {})
    if pm.get("data_available"):
        out["opm"] = pm["evidence"].get("opm_series")
    gp = sig.get("GRW.persistence", {})
    if gp.get("data_available"):
        out["sales"] = gp["evidence"].get("sales_series")
    wc = sig.get("CAP.working_capital_cost", {})
    if wc.get("data_available"):
        out["ccc"] = wc["evidence"].get("ccc_series")
    return out


def main() -> int:
    OUT.mkdir(exist_ok=True)

    # -------- framework.json
    fw = F.load_framework()
    problems = F.validate(fw)
    if problems:
        print("Skill framework invalid, aborting:", problems)
        return 1
    fw_json = {
        "version": fw.version,
        "modules": [{"id": m.id, "order": m.order, "name": m.name,
                     "guidance": m.guidance} for m in fw.modules],
        "parameters": [{"id": p.id, "module": p.module, "name": p.name,
                        "nature": p.nature, "signal": p.signal,
                        "direction": p.direction,
                        "description": " ".join(p.description.split()),
                        "cautions": p.cautions} for p in fw.parameters],
    }
    (OUT / "framework.json").write_text(json.dumps(fw_json))
    print(f"framework.json: {len(fw.parameters)} parameters")

    # -------- inputs
    const = pd.read_csv(INDIA / "NiftyTotalMarket" / "niftytotalmarket_constituents.csv")
    live = pd.read_csv(INDIA / "StockInfo" / "Nifty500" / "live_market_data.csv")
    live_map = live.set_index("nse_symbol").to_dict("index")

    cc_log_path = INDIA / "ConferenceCalls" / "NiftyTotalMarket" / "_fetch_log.csv"
    cc_map = {}
    if cc_log_path.exists():
        for _, r in pd.read_csv(cc_log_path).iterrows():
            s = str(r["status"])
            n = 0
            if s.startswith("ok"):
                for part in s.split(":"):
                    if part.startswith("text_ok="):
                        n = int(part.split("=")[1])
            cc_map[r["nse_symbol"]] = n

    mgmt_dir = INDIA / "ManagementInfo" / "NiftyTotalMarket"

    module_ids = [m.id for m in fw.modules]
    companies = {}
    n_total = len(const)

    for i, row in enumerate(const.itertuples(), 1):
        sym = str(row.nse_symbol)
        sig = Q.compute(sym, base=INDIA, universe=UNIVERSE)
        pscores = score_params(sig, fw)
        agg = S.aggregate(pscores, module_ids)

        mgmt = []
        mfile = mgmt_dir / f"{sym.replace('&', '_AND_')}.csv"
        if mfile.exists():
            try:
                mdf = pd.read_csv(mfile)
                cur = mdf[mdf["status"] == "current"]
                mgmt = [{"role": r2["role"], "name": r2["name"]}
                        for _, r2 in cur.head(6).iterrows()]
            except Exception:
                pass

        lv = live_map.get(sym, {})
        companies[sym] = clean({
            "name": row.company_name,
            "industry": (row.industry if isinstance(row.industry, str) else "") or "",
            "mcap": lv.get("market_cap_rs_cr"),
            "pe": lv.get("stock_pe"),
            "price": lv.get("current_price_rs"),
            "overall": agg["overall_score"],
            "coverage": agg["overall_coverage"],
            "modules": {m: {"score": agg["modules"][m]["module_score"],
                            "assessed": agg["modules"][m]["n_assessed"],
                            "total": agg["modules"][m]["n_total"]}
                        for m in module_ids},
            # Only assessed params are shipped; the UI derives unassessed ones
            # from framework.json (they all share the same "needs qualitative
            # analysis" status), keeping the payload small.
            "params": {p.id: {"score": p.score, "rationale": p.rationale,
                              "nature": p.nature}
                       for p in pscores if p.score is not None},
            "series": series_for_chart(sig),
            "mgmt": mgmt,
            "concalls": cc_map.get(sym, 0),
        })
        if i % 100 == 0 or i == n_total:
            print(f"  [{i}/{n_total}] {sym}")

    payload = {"universe": UNIVERSE, "framework_version": fw.version,
               "n": len(companies), "companies": companies}
    out_path = OUT / "companies.json"
    out_path.write_text(json.dumps(payload))
    print(f"companies.json: {len(companies)} companies, "
          f"{out_path.stat().st_size / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
