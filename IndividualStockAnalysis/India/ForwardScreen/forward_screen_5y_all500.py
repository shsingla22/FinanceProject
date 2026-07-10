"""
Forward 5-year Screen v2 — apply the v7 winning patterns to every
Nifty 500 company, using each company's OWN fiscal calendar (Mar / Dec
/ Jun / Sep / Nov). This closes the gap that v1 left by anchoring on
Mar only.

Patterns applied (from ../Analysis/ALL_PATTERNS_20PCT_CAGR.md):

  PRIMARY (88.9% historical hit rate at 5y):
    FA > 20% YoY for 3 yrs
    AND Sales 3y CAGR > 20%
    AND ROCE > 20% at T

  SECONDARY (81.1% historical hit rate at 5y):
    P/E < 15 AND Sales 3y CAGR > 15%

For each of the 500 Nifty 500 constituents the script:
  1. Detects the company's fiscal year-end month from its BS data
  2. Picks the most recent 4 year-ends in that calendar (T-3, T-2, T-1, T)
  3. Applies both screens
  4. Records a coverage status (evaluated / insufficient_data)

Outputs (this folder):
  - forward_screen_results_all500.csv  full per-company status
  - CANDIDATES_5Y_20PCT_CAGR.md         human-readable candidate list
                                       (overwrites v1)
"""

from __future__ import annotations
import math
import re
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent

BS_FILE = DATA / "BalanceSheet" / "Nifty500" / "_all_balance_sheets_long.csv"
PL_FILE = DATA / "ProfitStatement" / "Nifty500" / "_all_profit_loss_long.csv"
SI_FILE = DATA / "StockInfo" / "Nifty500" / "_all_stock_info_long.csv"
N500    = DATA / "Nifty500" / "nifty500_constituents.csv"

MONTH_ORDER = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
               "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}

def parse_year(y: str):
    m = re.match(r"([A-Za-z]{3})\s+(\d{4})", str(y))
    if not m:
        return None
    return (int(m.group(2)), MONTH_ORDER.get(m.group(1), 0), m.group(1))


# ---------- load & pivot ----------------------------------------------------

def pivot(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    return (
        df.pivot_table(
            index=["nse_symbol", "year"],
            columns="line_item",
            values=value_col,
            aggfunc="first",
        )
        .reset_index()
    )


def load_panel():
    bs = pd.read_csv(BS_FILE)
    pl = pd.read_csv(PL_FILE)
    si = pd.read_csv(SI_FILE)

    bs_w = pivot(bs, "value_rs_cr")
    pl_w = pivot(pl, "value")
    si_w = (
        si.pivot_table(
            index=["nse_symbol", "year"],
            columns="metric",
            values="value",
            aggfunc="first",
        )
        .reset_index()
    )
    panel = bs_w.merge(pl_w, on=["nse_symbol", "year"], how="outer",
                       suffixes=("_bs", "_pl"))
    panel = panel.merge(si_w, on=["nse_symbol", "year"], how="left")

    n500 = pd.read_csv(N500)
    ind_map = dict(zip(n500["nse_symbol"].astype(str),
                       n500["industry"].astype(str)))
    name_map = dict(zip(n500["nse_symbol"].astype(str),
                        n500["company_name"].astype(str)))
    panel["industry"] = panel["nse_symbol"].map(ind_map).fillna("")
    return panel, n500, ind_map, name_map


def detect_fiscal_month(sub: pd.DataFrame) -> str | None:
    """The fiscal month is the modal month of available year-end records."""
    months = [parse_year(y)[2] for y in sub["year"] if parse_year(y)]
    if not months:
        return None
    return pd.Series(months).mode().iloc[0]


def latest_n_years(sub: pd.DataFrame, fiscal_month: str, n: int = 4):
    rows = []
    for y in sub["year"]:
        p = parse_year(y)
        if p and p[2] == fiscal_month:
            rows.append((p[0], y))
    rows.sort(reverse=True)
    return [y for _, y in rows[:n]]


def safe(d: dict, k: str):
    v = d.get(k)
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return None
    return v


def yoy(curr, prev):
    if curr is None or prev is None or prev <= 0:
        return None
    return curr / prev - 1.0


def cagr(end, start, years):
    if end is None or start is None or start <= 0 or end <= 0:
        return None
    return (end / start) ** (1.0 / years) - 1.0


def screen(panel: pd.DataFrame, all_syms: list[str]) -> pd.DataFrame:
    rows = []
    for sym in all_syms:
        sub = panel[panel["nse_symbol"] == sym]
        if sub.empty:
            rows.append({"nse_symbol": sym, "status": "no_data"})
            continue

        fm = detect_fiscal_month(sub)
        if fm is None:
            rows.append({"nse_symbol": sym, "status": "no_data"})
            continue

        years = latest_n_years(sub, fm, n=4)  # [T, T-1, T-2, T-3]
        if len(years) < 4:
            rows.append({
                "nse_symbol": sym, "status": "insufficient_years",
                "fiscal_month": fm,
                "available_years": ",".join(years),
            })
            continue

        T, T1, T2, T3 = years
        def row_for(y):
            r = sub[sub["year"] == y]
            return r.iloc[0].to_dict() if not r.empty else {}
        rT, rT1, rT2, rT3 = row_for(T), row_for(T1), row_for(T2), row_for(T3)

        fa_T  = safe(rT,  "Fixed Assets")
        fa_T1 = safe(rT1, "Fixed Assets")
        fa_T2 = safe(rT2, "Fixed Assets")
        fa_T3 = safe(rT3, "Fixed Assets")

        sales_T  = safe(rT,  "Sales")
        sales_T3 = safe(rT3, "Sales")
        np_T     = safe(rT,  "Net Profit")
        np_T3    = safe(rT3, "Net Profit")

        op_T  = safe(rT, "Operating Profit")
        eq_T  = safe(rT, "Equity Capital")
        res_T = safe(rT, "Reserves")
        bor_T = safe(rT, "Borrowings")

        pe   = safe(rT, "P/E ratio")
        px   = safe(rT, "Stock Price (Rs)")
        mcap = safe(rT, "Market Cap (Rs Cr)")
        opm  = safe(rT, "OPM %")

        fa_yoy_1 = yoy(fa_T,  fa_T1)
        fa_yoy_2 = yoy(fa_T1, fa_T2)
        fa_yoy_3 = yoy(fa_T2, fa_T3)
        sales_cagr_3y = cagr(sales_T, sales_T3, 3)
        np_cagr_3y    = cagr(np_T, np_T3, 3)
        roce = None
        cap_base = None
        if eq_T is not None and res_T is not None and bor_T is not None:
            denom = eq_T + res_T + bor_T
            if denom and denom > 0 and op_T is not None:
                cap_base = denom
                roce = op_T / denom

        primary = (
            fa_yoy_1 is not None and fa_yoy_1 > 0.20
            and fa_yoy_2 is not None and fa_yoy_2 > 0.20
            and fa_yoy_3 is not None and fa_yoy_3 > 0.20
            and sales_cagr_3y is not None and sales_cagr_3y > 0.20
            and roce is not None and roce > 0.20
        )
        secondary = (
            pe is not None and 0 < pe < 15
            and sales_cagr_3y is not None and sales_cagr_3y > 0.15
        )

        ind = ""
        ind_series = sub["industry"]
        if len(ind_series):
            ind = str(ind_series.iloc[0])

        rows.append({
            "nse_symbol": sym,
            "status": "evaluated",
            "industry": ind,
            "fiscal_month": fm,
            "year_T": T,
            "year_T-3": T3,
            "Stock Price (Rs)": px,
            "Market Cap (Rs Cr)": mcap,
            "P/E ratio": pe,
            "OPM % T": opm,
            "FA T": fa_T,
            "FA T-1": fa_T1,
            "FA T-2": fa_T2,
            "FA T-3": fa_T3,
            "FA YoY (T)": fa_yoy_1,
            "FA YoY (T-1)": fa_yoy_2,
            "FA YoY (T-2)": fa_yoy_3,
            "Sales T": sales_T,
            "Sales T-3": sales_T3,
            "Sales 3y CAGR": sales_cagr_3y,
            "NP T": np_T,
            "NP T-3": np_T3,
            "NP 3y CAGR": np_cagr_3y,
            "Op Profit T": op_T,
            "Capital Base T": cap_base,
            "ROCE T": roce,
            "PRIMARY_match": primary,
            "SECONDARY_match": secondary,
        })
    return pd.DataFrame(rows)


# ---------- formatting -------------------------------------------------------

def pct(x):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    return f"{x * 100:.1f}%"


def num(x, fmt="{:,.0f}"):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    return fmt.format(x)


def rupees(x):
    return f"₹{num(x)}"


def fy_label(year_str: str) -> str:
    p = parse_year(year_str)
    if not p:
        return year_str
    return f"FY{str(p[0])[-2:]}"


def explanation_primary(r: dict) -> str:
    yT  = fy_label(r["year_T"])
    yT3 = fy_label(r["year_T-3"])
    # YoY labels: oldest -> newest
    yT2_lbl = fy_label(r["year_T-3"])  # FA YoY(T-2) covers T-3 -> T-2
    parts = []
    parts.append(
        f"- **Sustained capex**: Fixed Assets grew >20% YoY for three "
        f"consecutive years — {pct(r['FA YoY (T-2)'])}, "
        f"{pct(r['FA YoY (T-1)'])}, {pct(r['FA YoY (T)'])} "
        f"({yT3} → {yT}). FA went from {rupees(r['FA T-3'])} Cr to "
        f"{rupees(r['FA T'])} Cr."
    )
    parts.append(
        f"- **Top-line scaling with capex**: Sales {rupees(r['Sales T-3'])} Cr "
        f"({yT3}) → {rupees(r['Sales T'])} Cr ({yT}); 3-yr CAGR "
        f"**{pct(r['Sales 3y CAGR'])}** — the new assets are generating revenue."
    )
    parts.append(
        f"- **High capital efficiency (ROCE {pct(r['ROCE T'])})**: Operating "
        f"profit {rupees(r['Op Profit T'])} Cr on a capital base of "
        f"{rupees(r['Capital Base T'])} Cr — the capex is earning well above "
        f"its cost of capital."
    )
    if r["NP 3y CAGR"] is not None:
        parts.append(
            f"- **Profit follows sales**: Net profit 3-yr CAGR "
            f"{pct(r['NP 3y CAGR'])} ({yT3} {rupees(r['NP T-3'])} Cr → "
            f"{yT} {rupees(r['NP T'])} Cr)."
        )
    if r["P/E ratio"] is not None and not (isinstance(r["P/E ratio"], float) and math.isnan(r["P/E ratio"])):
        flag = ("rich — valuation risk if multiple compresses"
                if r["P/E ratio"] > 50 else "reasonable for the growth profile")
        parts.append(f"- **Entry P/E {r['P/E ratio']:.1f}x** ({flag}).")
    return "\n".join(parts)


def explanation_secondary(r: dict) -> str:
    yT  = fy_label(r["year_T"])
    yT3 = fy_label(r["year_T-3"])
    parts = [
        f"- **Cheap valuation**: trading at **{r['P/E ratio']:.1f}x P/E** (below 15x bar).",
        f"- **Real top-line growth**: Sales 3-yr CAGR "
        f"**{pct(r['Sales 3y CAGR'])}** ({rupees(r['Sales T-3'])} Cr {yT3} "
        f"→ {rupees(r['Sales T'])} Cr {yT}).",
    ]
    if r["ROCE T"] is not None:
        flag = ""
        if r["ROCE T"] < 0.05:
            flag = " ⚠️ weak capital efficiency"
        parts.append(f"- ROCE {yT}: {pct(r['ROCE T'])}.{flag}")
    if r["NP 3y CAGR"] is not None:
        parts.append(f"- Net profit 3-yr CAGR: {pct(r['NP 3y CAGR'])}.")
    if r["OPM % T"] is not None and not (isinstance(r["OPM % T"], float) and math.isnan(r["OPM % T"])):
        parts.append(f"- Operating margin {yT}: {r['OPM % T']:.1f}%.")
    parts.append(
        "- Historically cheap-and-growing combinations delivered ≥20% "
        "5-yr CAGR 81% of the time (n=90 backtest)."
    )
    return "\n".join(parts)


def write_md(out: pd.DataFrame, n500_total: int):
    evaluated = out[out["status"] == "evaluated"]
    primary  = evaluated[evaluated["PRIMARY_match"] == True].sort_values("Sales 3y CAGR", ascending=False)
    secondary = evaluated[
        (evaluated["SECONDARY_match"] == True) & (evaluated["PRIMARY_match"] == False)
    ].sort_values("Sales 3y CAGR", ascending=False)

    md = []
    md.append("# Nifty 500 — 5-Year Forward Candidates for ≥20% CAGR\n")
    md.append(f"**Universe:** all {n500_total} Nifty 500 constituents\n")
    md.append(
        "**Method:** for each company, auto-detect its fiscal calendar "
        "(Mar / Dec / Jun / Sep / Nov), then apply the v7 patterns to its "
        "most recent 4 fiscal year-ends (T, T-1, T-2, T-3).\n"
    )

    n_eval = len(evaluated)
    n_no = (out["status"] == "no_data").sum()
    n_short = (out["status"] == "insufficient_years").sum()
    md.append(
        f"**Coverage:** {n_eval} / {n500_total} cos evaluated. "
        f"{n_short} cos had <4 fiscal year-ends of data "
        f"(typically recent IPOs); {n_no} had no usable data.\n"
    )
    md.append(
        "**Historical base rates** (from the v7 backtest):\n"
        "- PRIMARY screen — `FA YoY >20% × 3 yrs AND Sales 3y CAGR >20% AND ROCE >20%`: "
        "**88.9% hit rate** at 5y, avg realized CAGR **+42.1%**\n"
        "- SECONDARY screen — `P/E <15 AND Sales 3y CAGR >15%`: "
        "**81.1% hit rate** at 5y, avg realized CAGR **+38.4%**\n"
    )
    md.append("---\n")

    # PRIMARY
    md.append("## A. PRIMARY screen winners — high-conviction\n")
    md.append(
        "Companies satisfying ALL three conditions of the strongest historical "
        "signal (88.9% historical hit rate at 5y).\n"
    )
    if primary.empty:
        md.append("*No Nifty 500 companies currently satisfy all three PRIMARY conditions.*\n")
    else:
        md.append(
            "| # | Symbol | Industry | Fiscal | Price | Mcap (Cr) | P/E | Sales 3y CAGR | ROCE |\n"
            "|--:|--------|----------|:------:|------:|----------:|----:|--------------:|-----:|"
        )
        for i, (_, r) in enumerate(primary.iterrows(), 1):
            pe_val = r["P/E ratio"]
            pe_str = "n/a" if pe_val is None or (isinstance(pe_val, float) and math.isnan(pe_val)) else f"{pe_val:.1f}"
            md.append(
                f"| {i} | **{r['nse_symbol']}** | {r['industry'] or '(uncl.)'} | "
                f"{r['fiscal_month']} | {rupees(r['Stock Price (Rs)'])} | "
                f"{num(r['Market Cap (Rs Cr)'])} | {pe_str} | "
                f"{pct(r['Sales 3y CAGR'])} | {pct(r['ROCE T'])} |"
            )
        md.append("")
        for i, (_, r) in enumerate(primary.iterrows(), 1):
            md.append(f"### {i}. {r['nse_symbol']} — why it should deliver ≥20% CAGR\n")
            md.append(
                f"*Industry: {r['industry'] or '(uncl.)'}  |  Fiscal year-end: "
                f"{r['fiscal_month']}  |  Anchor T = {r['year_T']}  |  "
                f"Price: {rupees(r['Stock Price (Rs)'])}  |  Market cap: "
                f"Rs {num(r['Market Cap (Rs Cr)'])} Cr*\n"
            )
            md.append(explanation_primary(r.to_dict()))
            md.append("")

    md.append("---\n")

    # SECONDARY
    md.append("## B. SECONDARY screen winners — value + growth\n")
    md.append(
        "Companies not in PRIMARY but satisfying the broader value-anchored "
        "signal (81.1% historical hit rate at 5y).\n"
    )
    if secondary.empty:
        md.append("*No additional secondary matches.*\n")
    else:
        md.append(
            "| # | Symbol | Industry | Fiscal | Price | Mcap (Cr) | P/E | Sales 3y CAGR | ROCE |\n"
            "|--:|--------|----------|:------:|------:|----------:|----:|--------------:|-----:|"
        )
        for i, (_, r) in enumerate(secondary.iterrows(), 1):
            md.append(
                f"| {i} | **{r['nse_symbol']}** | {r['industry'] or '(uncl.)'} | "
                f"{r['fiscal_month']} | {rupees(r['Stock Price (Rs)'])} | "
                f"{num(r['Market Cap (Rs Cr)'])} | {r['P/E ratio']:.1f} | "
                f"{pct(r['Sales 3y CAGR'])} | "
                f"{pct(r['ROCE T']) if r['ROCE T'] is not None else 'n/a'} |"
            )
        md.append("")
        for i, (_, r) in enumerate(secondary.iterrows(), 1):
            md.append(f"### {i}. {r['nse_symbol']} — why it qualifies\n")
            md.append(
                f"*Industry: {r['industry'] or '(uncl.)'}  |  Fiscal year-end: "
                f"{r['fiscal_month']}  |  Anchor T = {r['year_T']}  |  "
                f"Price: {rupees(r['Stock Price (Rs)'])}  |  Market cap: "
                f"Rs {num(r['Market Cap (Rs Cr)'])} Cr*\n"
            )
            md.append(explanation_secondary(r.to_dict()))
            md.append("")

    md.append("---\n")

    # Cos not evaluated
    skipped = out[out["status"] != "evaluated"][["nse_symbol", "status", "fiscal_month", "available_years"]] if "available_years" in out.columns else out[out["status"] != "evaluated"][["nse_symbol", "status"]]
    md.append("## C. Cos not evaluable by this screen\n")
    md.append(
        f"{len(skipped)} of {n500_total} cos could not be evaluated. "
        "Most are recent IPOs (don't yet have 4 fiscal years of history). "
        "These are listed for completeness — they aren't ruled out, just "
        "data-insufficient to test the pattern against today.\n"
    )
    if len(skipped):
        md.append("| Symbol | Status | Notes |")
        md.append("|--------|--------|-------|")
        for _, r in skipped.iterrows():
            notes = []
            if "fiscal_month" in r and isinstance(r.get("fiscal_month"), str):
                notes.append(f"fiscal: {r['fiscal_month']}")
            if "available_years" in r and isinstance(r.get("available_years"), str):
                notes.append(f"have: {r['available_years']}")
            md.append(f"| {r['nse_symbol']} | {r['status']} | {' / '.join(notes)} |")
        md.append("")

    md.append("---\n")
    md.append("## How to read this list\n")
    md.append(
        "1. **Valuation overlay matters.** The single biggest historical "
        "failure in PRIMARY matches (AFFLE) was a P/E >100x stock where "
        "multiple compression dragged 5-yr returns to +5.8%. Treat "
        "extreme-P/E candidates with extra scrutiny.\n\n"
        "2. **Diversify across sectors.** The historical winners cluster in "
        "capex-heavy domestic-consumption businesses.\n\n"
        "3. **Re-screen annually.** A company that satisfies the screen today "
        "may not next year as its capex cycle matures.\n\n"
        "4. **Cross-check with cash flow.** The screen trusts reported P&L "
        "and BS numbers. For any candidate, verify operating cash flow "
        "tracks reported net profit.\n"
    )

    text = "\n".join(md)
    path = HERE / "CANDIDATES_5Y_20PCT_CAGR.md"
    path.write_text(text)
    return path, len(primary), len(secondary), n_eval, n_short, n_no


def main():
    panel, n500, _, _ = load_panel()
    all_syms = list(n500["nse_symbol"].astype(str).unique())
    print(f"Nifty 500 universe size: {len(all_syms)}")
    out = screen(panel, all_syms)
    out_csv = HERE / "forward_screen_results_all500.csv"
    out.to_csv(out_csv, index=False)
    print(f"Wrote {out_csv} ({len(out)} rows)")
    path, n_p, n_s, n_eval, n_short, n_no = write_md(out, len(all_syms))
    print(f"Evaluated: {n_eval}, Insufficient: {n_short}, No data: {n_no}")
    print(f"PRIMARY matches: {n_p}")
    print(f"SECONDARY-only matches: {n_s}")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
