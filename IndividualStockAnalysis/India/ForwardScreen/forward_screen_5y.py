"""
Forward 5-year Screen — apply the v7 winning patterns to the latest
3 years of available data (Mar 2024, Mar 2025, Mar 2026) to find
Nifty 500 companies likely to deliver >= 20% CAGR over the next
5 years.

Patterns applied (from ../Analysis/ALL_PATTERNS_20PCT_CAGR.md):

  PRIMARY (the strongest historical signal — 88.9% hit rate at 5y):
    FA > 20% YoY for 3 yrs
    AND Sales CAGR > 20% (last 3 yrs)
    AND ROCE > 20% at T

  SECONDARY (broader, value-anchored — 81.1% hit rate at 5y, n=90):
    P/E < 15 AND Sales CAGR > 15% (last 3 yrs)

For each match we produce a per-company explanation citing the
specific BS/P&L/valuation numbers that triggered the screen.

Outputs (this folder):
  - forward_screen_results.csv     full per-company computation
  - CANDIDATES_5Y_20PCT_CAGR.md    human-readable candidate list with reasoning
"""

from __future__ import annotations
import math
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent

BS_FILE = DATA / "BalanceSheet" / "_all_balance_sheets_long.csv"
PL_FILE = DATA / "ProfitStatement" / "_all_profit_loss_long.csv"
SI_FILE = DATA / "StockInfo" / "_all_stock_info_long.csv"
N500    = DATA / "Nifty500" / "nifty500_constituents.csv"

# We anchor T = Mar 2026 (the latest fiscal year-end with full data).
T  = "Mar 2026"
T1 = "Mar 2025"
T2 = "Mar 2024"
T3 = "Mar 2023"  # used as base for 3-yr Sales CAGR


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


def load_panel() -> pd.DataFrame:
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

    # Restrict to Mar fiscal year companies (the only consistent reporting set
    # that aligns with our stock-price year-ends).
    panel = panel[panel["year"].astype(str).str.startswith("Mar")].copy()
    panel["industry"] = ""

    # Optional industry tag
    if N500.exists():
        n500 = pd.read_csv(N500)
        sym_col = next((c for c in n500.columns if c.lower() in
                        {"symbol", "nse_symbol", "ticker"}), None)
        ind_col = next((c for c in n500.columns if "industry" in c.lower()), None)
        if sym_col and ind_col:
            ind_map = dict(zip(n500[sym_col].astype(str),
                               n500[ind_col].astype(str)))
            panel["industry"] = panel["nse_symbol"].map(ind_map).fillna("")

    return panel


# ---------- screen ----------------------------------------------------------

def yoy(curr, prev):
    if curr is None or prev is None:
        return None
    if pd.isna(curr) or pd.isna(prev) or prev <= 0:
        return None
    return curr / prev - 1.0


def cagr(end, start, years):
    if end is None or start is None:
        return None
    if pd.isna(end) or pd.isna(start) or start <= 0 or end <= 0:
        return None
    return (end / start) ** (1.0 / years) - 1.0


def safe(d: dict, k: str):
    v = d.get(k)
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return None
    return v


def get_row(panel: pd.DataFrame, sym: str, year: str) -> dict:
    sub = panel[(panel["nse_symbol"] == sym) & (panel["year"] == year)]
    if sub.empty:
        return {}
    return sub.iloc[0].to_dict()


def screen(panel: pd.DataFrame) -> pd.DataFrame:
    rows = []
    syms = panel["nse_symbol"].unique()
    for sym in syms:
        rT  = get_row(panel, sym, T)
        rT1 = get_row(panel, sym, T1)
        rT2 = get_row(panel, sym, T2)
        rT3 = get_row(panel, sym, T3)
        if not rT or not rT1 or not rT2 or not rT3:
            continue

        fa_T  = safe(rT,  "Fixed Assets")
        fa_T1 = safe(rT1, "Fixed Assets")
        fa_T2 = safe(rT2, "Fixed Assets")
        fa_T3 = safe(rT3, "Fixed Assets")

        sales_T  = safe(rT,  "Sales")
        sales_T3 = safe(rT3, "Sales")

        op_T  = safe(rT, "Operating Profit")
        eq_T  = safe(rT, "Equity Capital")
        res_T = safe(rT, "Reserves")
        bor_T = safe(rT, "Borrowings")
        np_T  = safe(rT, "Net Profit")
        np_T3 = safe(rT3, "Net Profit")

        pe   = safe(rT, "P/E ratio")
        px   = safe(rT, "Stock Price (Rs)")
        mcap = safe(rT, "Market Cap (Rs Cr)")
        opm  = safe(rT, "OPM %")

        fa_yoy_1 = yoy(fa_T,  fa_T1)
        fa_yoy_2 = yoy(fa_T1, fa_T2)
        fa_yoy_3 = yoy(fa_T2, fa_T3)
        sales_cagr_3y = cagr(sales_T, sales_T3, 3)
        np_cagr_3y    = cagr(np_T, np_T3, 3)

        cap_base = None
        if eq_T is not None and res_T is not None and bor_T is not None:
            denom = eq_T + res_T + bor_T
            if denom and denom > 0 and op_T is not None:
                cap_base = denom
                roce = op_T / denom
            else:
                roce = None
        else:
            roce = None

        ind = ""
        ind_series = panel.loc[panel["nse_symbol"] == sym, "industry"]
        if len(ind_series):
            ind = str(ind_series.iloc[0])

        # PRIMARY screen
        primary = (
            fa_yoy_1 is not None and fa_yoy_1 > 0.20
            and fa_yoy_2 is not None and fa_yoy_2 > 0.20
            and fa_yoy_3 is not None and fa_yoy_3 > 0.20
            and sales_cagr_3y is not None and sales_cagr_3y > 0.20
            and roce is not None and roce > 0.20
        )

        # SECONDARY screen — value-anchored
        secondary = (
            pe is not None and 0 < pe < 15
            and sales_cagr_3y is not None and sales_cagr_3y > 0.15
        )

        rows.append({
            "nse_symbol": sym,
            "industry": ind,
            "Stock Price (Rs)": px,
            "Market Cap (Rs Cr)": mcap,
            "P/E ratio": pe,
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
            "OPM % T": opm,
            "PRIMARY_match": primary,
            "SECONDARY_match": secondary,
        })

    out = pd.DataFrame(rows)
    return out


# ---------- formatting -------------------------------------------------------

def pct(x):
    if x is None or (isinstance(x, float) and (math.isnan(x))):
        return "n/a"
    return f"{x * 100:.1f}%"


def num(x, fmt="{:,.0f}"):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    return fmt.format(x)


def rupees(x):
    return f"₹{num(x)}"


def explanation_primary(r: dict) -> str:
    parts = []
    parts.append(
        f"- **Sustained capex**: Fixed Assets compounded at >20% YoY for "
        f"three consecutive years — {pct(r['FA YoY (T-2)'])} (FY24), "
        f"{pct(r['FA YoY (T-1)'])} (FY25), {pct(r['FA YoY (T)'])} (FY26). "
        f"FA grew from {rupees(r['FA T-3'])} Cr to {rupees(r['FA T'])} Cr."
    )
    parts.append(
        f"- **Top-line scaling with capex**: Sales grew from "
        f"{rupees(r['Sales T-3'])} Cr (FY23) to {rupees(r['Sales T'])} Cr (FY26), "
        f"a 3-year CAGR of **{pct(r['Sales 3y CAGR'])}** — confirming the "
        f"capex is translating into revenue, not just idle assets."
    )
    parts.append(
        f"- **High capital efficiency (ROCE {pct(r['ROCE T'])})**: Operating "
        f"profit of {rupees(r['Op Profit T'])} Cr on a capital base "
        f"(equity + reserves + borrowings) of {rupees(r['Capital Base T'])} Cr. "
        f"A >20% ROCE means the new capex is earning more than its cost of capital."
    )
    if r["NP 3y CAGR"] is not None:
        parts.append(
            f"- **Profit follows sales**: Net profit 3-yr CAGR of "
            f"{pct(r['NP 3y CAGR'])} (FY23 {rupees(r['NP T-3'])} Cr "
            f"→ FY26 {rupees(r['NP T'])} Cr)."
        )
    if r["P/E ratio"] is not None and not math.isnan(r["P/E ratio"]):
        parts.append(
            f"- **Entry P/E {r['P/E ratio']:.1f}x** "
            f"({'rich — valuation risk if multiple compresses' if r['P/E ratio'] > 50 else 'reasonable for the growth profile'})."
        )
    return "\n".join(parts)


def explanation_secondary(r: dict) -> str:
    parts = []
    parts.append(
        f"- **Cheap valuation**: trading at **{r['P/E ratio']:.1f}x P/E** — "
        f"below 15x bar."
    )
    parts.append(
        f"- **Real top-line growth**: Sales 3-yr CAGR of "
        f"**{pct(r['Sales 3y CAGR'])}** ({rupees(r['Sales T-3'])} Cr "
        f"FY23 → {rupees(r['Sales T'])} Cr FY26)."
    )
    if r["ROCE T"] is not None:
        parts.append(f"- ROCE FY26: {pct(r['ROCE T'])}.")
    if r["NP 3y CAGR"] is not None:
        parts.append(f"- Net profit 3-yr CAGR: {pct(r['NP 3y CAGR'])}.")
    if r["OPM % T"] is not None and not math.isnan(r["OPM % T"]):
        parts.append(f"- Operating margin FY26: {r['OPM % T']:.1f}%.")
    parts.append(
        "- Cheap-and-growing combinations historically converted to >=20% "
        "5-year CAGR 81% of the time in our v7 backtest."
    )
    return "\n".join(parts)


# ---------- main -------------------------------------------------------------

def main():
    panel = load_panel()
    print(f"Loaded panel: {panel.shape}")
    out = screen(panel)

    out.sort_values(
        ["PRIMARY_match", "SECONDARY_match", "Sales 3y CAGR"],
        ascending=[False, False, False],
        inplace=True,
    )

    out_csv = HERE / "forward_screen_results.csv"
    out.to_csv(out_csv, index=False)
    print(f"Wrote {out_csv} ({len(out)} rows)")

    primary  = out[out["PRIMARY_match"]].copy().sort_values("Sales 3y CAGR", ascending=False)
    secondary = out[
        out["SECONDARY_match"] & ~out["PRIMARY_match"]
    ].copy().sort_values("Sales 3y CAGR", ascending=False)
    print(f"PRIMARY matches: {len(primary)}")
    print(f"SECONDARY-only matches: {len(secondary)}")

    md_lines = []
    md_lines.append(
        "# Nifty 500 — 5-Year Forward Candidates for >=20% CAGR\n"
    )
    md_lines.append(
        "**As of:** FY26 reported data (year-end Mar 2026)\n"
    )
    md_lines.append(
        "**Method:** apply the patterns identified in\n"
        "`../Analysis/ALL_PATTERNS_20PCT_CAGR.md` to the latest 3 fiscal\n"
        "years (FY24, FY25, FY26) for each Nifty 500 constituent.\n"
    )
    md_lines.append(
        "**Historical base rates** (from the v7 backtest):\n"
        "- PRIMARY screen — `FA YoY >20% x 3 yrs AND Sales 3y CAGR >20% AND ROCE >20%`:\n"
        "  **88.9% hit rate** at 5y, avg realized CAGR **+42.1%**\n"
        "- SECONDARY screen — `P/E <15 AND Sales 3y CAGR >15%`:\n"
        "  **81.1% hit rate** at 5y, avg realized CAGR **+38.4%** (n=90 historical)\n"
    )
    md_lines.append("---\n")

    md_lines.append("## A. PRIMARY screen winners — high-conviction candidates\n")
    md_lines.append(
        "Companies that simultaneously satisfy all three conditions of\n"
        "the strongest historical signal. Historically 8 of 9 such "
        "companies (88.9%) delivered >=20% 5-year stock CAGR.\n"
    )

    if primary.empty:
        md_lines.append("*No companies in the Nifty 500 currently satisfy all three PRIMARY conditions.*\n")
    else:
        md_lines.append(
            "| # | Symbol | Industry | Price | Mcap (Cr) | P/E | Sales 3y CAGR | ROCE FY26 |\n"
            "|--:|--------|----------|------:|----------:|----:|--------------:|----------:|"
        )
        for i, (_, r) in enumerate(primary.iterrows(), 1):
            pe_val = r["P/E ratio"]
            pe_str = "n/a" if pe_val is None or (isinstance(pe_val, float) and math.isnan(pe_val)) else f"{pe_val:.1f}"
            md_lines.append(
                f"| {i} | **{r['nse_symbol']}** | {r['industry'] or '(uncl.)'} | "
                f"{rupees(r['Stock Price (Rs)'])} | {num(r['Market Cap (Rs Cr)'])} | "
                f"{pe_str} | "
                f"{pct(r['Sales 3y CAGR'])} | {pct(r['ROCE T'])} |"
            )
        md_lines.append("")

        for i, (_, r) in enumerate(primary.iterrows(), 1):
            md_lines.append(f"### {i}. {r['nse_symbol']} — why it should deliver >=20% CAGR\n")
            md_lines.append(
                f"*Industry: {r['industry'] or '(uncl.)'}  |  "
                f"Price (Mar 2026): {rupees(r['Stock Price (Rs)'])}  |  "
                f"Market cap: Rs {num(r['Market Cap (Rs Cr)'])} Cr*\n"
            )
            md_lines.append(explanation_primary(r.to_dict()))
            md_lines.append("")

    md_lines.append("---\n")
    md_lines.append("## B. SECONDARY screen winners — value + growth candidates\n")
    md_lines.append(
        "Companies that don't meet the strict PRIMARY screen but satisfy\n"
        "the broader value-anchored signal. Historical base rate 81.1%\n"
        "at the 5-year horizon.\n"
    )

    if secondary.empty:
        md_lines.append("*No additional secondary matches.*\n")
    else:
        md_lines.append(
            "| # | Symbol | Industry | Price | Mcap (Cr) | P/E | Sales 3y CAGR | ROCE FY26 |\n"
            "|--:|--------|----------|------:|----------:|----:|--------------:|----------:|"
        )
        for i, (_, r) in enumerate(secondary.iterrows(), 1):
            md_lines.append(
                f"| {i} | **{r['nse_symbol']}** | {r['industry'] or '(uncl.)'} | "
                f"{rupees(r['Stock Price (Rs)'])} | {num(r['Market Cap (Rs Cr)'])} | "
                f"{r['P/E ratio']:.1f} | "
                f"{pct(r['Sales 3y CAGR'])} | "
                f"{pct(r['ROCE T']) if r['ROCE T'] is not None else 'n/a'} |"
            )
        md_lines.append("")

        for i, (_, r) in enumerate(secondary.iterrows(), 1):
            md_lines.append(f"### {i}. {r['nse_symbol']} — why it qualifies\n")
            md_lines.append(
                f"*Industry: {r['industry'] or '(uncl.)'}  |  "
                f"Price (Mar 2026): {rupees(r['Stock Price (Rs)'])}  |  "
                f"Market cap: Rs {num(r['Market Cap (Rs Cr)'])} Cr*\n"
            )
            md_lines.append(explanation_secondary(r.to_dict()))
            md_lines.append("")

    md_lines.append("---\n")
    md_lines.append("## How to read this list\n")
    md_lines.append(
        "These names are *statistical candidates* — companies whose\n"
        "current fundamentals match historical patterns that delivered\n"
        ">=20% 5-year CAGR with high probability. They are NOT individual\n"
        "buy recommendations. In particular:\n\n"
        "1. **Valuation overlay matters.** The single biggest historical\n"
        "   failure in PRIMARY-screen matches (AFFLE) was a P/E >100x\n"
        "   company where multiple compression dragged 5-yr returns to\n"
        "   +5.8%, far below the +42% peer average. PRIMARY candidates\n"
        "   trading above ~75x P/E deserve extra scrutiny.\n\n"
        "2. **Diversify across sectors.** The historical winners cluster\n"
        "   in capex-heavy domestic-consumption businesses. Concentration\n"
        "   in a single sector raises factor risk.\n\n"
        "3. **Re-screen annually.** A company that satisfies the screen\n"
        "   today may not next year as its capex cycle matures.\n\n"
        "4. **Cross-check with cash flow.** The screen trusts reported P&L\n"
        "   and BS numbers. For any candidate, verify operating cash flow\n"
        "   tracks reported net profit (no receivables/inventory bloat).\n"
    )

    md = "\n".join(md_lines)
    md_path = HERE / "CANDIDATES_5Y_20PCT_CAGR.md"
    md_path.write_text(md)
    print(f"Wrote {md_path} ({md.count(chr(10))} lines)")


if __name__ == "__main__":
    main()
