"""
Cross-sectional analysis: do balance-sheet patterns predict forward
stock returns (3y / 5y / 7y) for Nifty 500 companies?

For each (company, base_year) pair, computes derived signals from
balance sheet + P&L + stock info, then computes forward stock returns
from base_year to base_year+3, +5, +7. Filters to signals with hit
rate (% of cases delivering positive returns) >= 80%.

Inputs (relative to this script):
  ../BalanceSheet/_all_balance_sheets_long.csv
  ../ProfitStatement/_all_profit_loss_long.csv
  ../StockInfo/_all_stock_info_long.csv
  ../Nifty500/nifty500_constituents.csv

Outputs (this folder):
  pattern_results.csv       — every signal × horizon combination
  top_patterns_80pct.csv    — signals with hit rate >= 80%, n >= 30
  feature_panel.csv         — per (company, base_year) computed features
                              + forward returns (for further analysis)
  README_analysis.md        — narrative writeup (separate file)

Usage:
  python3 run_analysis.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
DATA_BS = HERE.parent / "BalanceSheet" / "_all_balance_sheets_long.csv"
DATA_PL = HERE.parent / "ProfitStatement" / "_all_profit_loss_long.csv"
DATA_SI = HERE.parent / "StockInfo" / "_all_stock_info_long.csv"
DATA_CON = HERE.parent / "Nifty500" / "nifty500_constituents.csv"

OUT_RESULTS = HERE / "pattern_results.csv"
OUT_TOP = HERE / "top_patterns_80pct.csv"
OUT_PANEL = HERE / "feature_panel.csv"


def load_wide(long_csv: Path, value_col: str = "value_rs_cr") -> pd.DataFrame:
    """Convert one long-format CSV into a wide table indexed by (nse_symbol, year)
    with one column per line_item. If the same line_item label appears under
    multiple parent_line_items, the headline (empty parent) is preferred."""
    df = pd.read_csv(long_csv)
    # Find the actual value column
    if value_col not in df.columns:
        for c in ("value", "value_rs_cr"):
            if c in df.columns:
                value_col = c
                break
    # If duplicates by (sym, year, line_item), prefer rows with empty parent
    if "parent_line_item" in df.columns:
        df["_parent_priority"] = df["parent_line_item"].fillna("").astype(str).str.len()
        df = df.sort_values("_parent_priority").drop_duplicates(
            subset=["nse_symbol", "year", "line_item"], keep="first"
        )
        df = df.drop(columns=["_parent_priority"])
    elif "metric" in df.columns:
        df = df.rename(columns={"metric": "line_item"})
    wide = df.pivot_table(
        index=["nse_symbol", "year"],
        columns="line_item",
        values=value_col,
        aggfunc="first",
    )
    return wide


def year_to_int(y: str) -> int | None:
    """'Mar 2015' -> 2015. Returns None for non-March year labels (we ignore those)."""
    try:
        parts = str(y).split()
        if len(parts) == 2 and parts[0] == "Mar":
            return int(parts[1])
    except Exception:
        pass
    return None


def cagr(end: float | None, start: float | None, years: int) -> float | None:
    if end is None or start is None or years <= 0:
        return None
    try:
        if pd.isna(end) or pd.isna(start) or start <= 0 or end <= 0:
            return None
        return float((end / start) ** (1 / years) - 1) * 100
    except Exception:
        return None


def main() -> None:
    print("Loading data ...")
    bs = load_wide(DATA_BS)
    pl = load_wide(DATA_PL)
    si = load_wide(DATA_SI)
    constituents = pd.read_csv(DATA_CON)

    print(f"  Balance sheet wide table: {bs.shape}")
    print(f"  P&L          wide table: {pl.shape}")
    print(f"  Stock info   wide table: {si.shape}")

    # Combine all three into one panel
    panel = bs.join(pl, how="outer", rsuffix="_pl").join(si, how="outer", rsuffix="_si")
    panel = panel.reset_index()
    panel["base_year"] = panel["year"].apply(year_to_int)
    panel = panel.dropna(subset=["base_year"])
    panel["base_year"] = panel["base_year"].astype(int)

    # Map to industry
    industry_map = dict(zip(constituents["nse_symbol"], constituents["industry"]))
    panel["industry"] = panel["nse_symbol"].map(industry_map)

    # Required line items for our features. If any is missing in a row, we
    # skip that row's affected features.
    REQUIRED = [
        "Fixed Assets", "CWIP", "Investments", "Total Assets",
        "Equity Capital", "Reserves", "Borrowings", "Total Liabilities",
        "Inventories", "Trade receivables", "Cash Equivalents", "Trade Payables",
        "Sales", "Net Profit", "Operating Profit", "Interest", "Depreciation",
        "EPS in Rs", "Stock Price (Rs)", "Market Cap (Rs Cr)",
    ]
    have_cols = [c for c in REQUIRED if c in panel.columns]
    print(f"  Required cols present: {len(have_cols)}/{len(REQUIRED)}: {have_cols}")

    # Compute per-(symbol, base_year) features. To compute trailing CAGRs we
    # need to look 3 years back; the stock-return forward horizons need 3/5/7
    # years forward.
    panel = panel.sort_values(["nse_symbol", "base_year"])

    # Pre-compute lagged values per symbol via groupby + shift
    g = panel.groupby("nse_symbol", group_keys=False)

    # 3-year lagged values for CAGR computation
    for col in ("Fixed Assets", "Inventories", "Trade receivables",
                "Trade Payables", "Total Assets", "Sales", "Net Profit"):
        if col in panel.columns:
            panel[f"{col}__lag3"] = g[col].shift(3)

    # Forward stock price for 3/5/7-year returns
    if "Stock Price (Rs)" in panel.columns:
        panel["price_fwd3"] = g["Stock Price (Rs)"].shift(-3)
        panel["price_fwd5"] = g["Stock Price (Rs)"].shift(-5)
        panel["price_fwd7"] = g["Stock Price (Rs)"].shift(-7)

    # Derived features
    print("Computing derived features ...")

    def safe_div(a, b):
        out = pd.Series(np.nan, index=a.index, dtype=float)
        mask = b.notna() & (b != 0) & a.notna()
        out[mask] = a[mask] / b[mask]
        return out

    def safe_cagr_col(end_col: str, start_col: str, years: int = 3) -> pd.Series:
        e = panel[end_col]
        s = panel[start_col]
        out = pd.Series(np.nan, index=panel.index, dtype=float)
        mask = e.notna() & s.notna() & (e > 0) & (s > 0)
        out[mask] = ((e[mask] / s[mask]) ** (1 / years) - 1) * 100
        return out

    panel["fa_cagr3"] = safe_cagr_col("Fixed Assets", "Fixed Assets__lag3")
    panel["inv_cagr3"] = safe_cagr_col("Inventories", "Inventories__lag3")
    panel["rec_cagr3"] = safe_cagr_col("Trade receivables", "Trade receivables__lag3")
    panel["pay_cagr3"] = safe_cagr_col("Trade Payables", "Trade Payables__lag3")
    panel["assets_cagr3"] = safe_cagr_col("Total Assets", "Total Assets__lag3")
    panel["sales_cagr3"] = safe_cagr_col("Sales", "Sales__lag3")
    panel["profit_cagr3"] = safe_cagr_col("Net Profit", "Net Profit__lag3")

    # Ratios
    panel["debt_to_equity"] = safe_div(
        panel["Borrowings"], panel["Equity Capital"] + panel["Reserves"]
    )
    panel["roe_pct"] = safe_div(
        panel["Net Profit"], panel["Equity Capital"] + panel["Reserves"]
    ) * 100
    # ROCE = PBIT / Capital Employed. PBIT ≈ Operating Profit (operating profit
    # already excludes interest and tax). Capital Employed ≈ Equity + Borrowings.
    capital_employed = panel["Equity Capital"] + panel["Reserves"] + panel["Borrowings"]
    pbit = panel.get("Operating Profit", pd.Series(np.nan, index=panel.index))
    panel["roce_pct"] = safe_div(pbit, capital_employed) * 100
    panel["asset_turnover"] = safe_div(panel["Sales"], panel["Total Assets"])

    # Capital expenditure intensity: CWIP / Fixed Assets
    panel["cwip_to_fa"] = safe_div(panel["CWIP"], panel["Fixed Assets"])
    panel["sales_to_assets"] = safe_div(panel["Sales"], panel["Total Assets"])

    # Working capital cycle days (approximations using year-end balance):
    # Inventory days = Inventories / Sales * 365
    panel["inv_days"] = safe_div(panel["Inventories"], panel["Sales"]) * 365
    panel["rec_days"] = safe_div(panel["Trade receivables"], panel["Sales"]) * 365
    # Payables days = Trade Payables / Sales * 365 (rough proxy)
    panel["pay_days"] = safe_div(panel["Trade Payables"], panel["Sales"]) * 365
    panel["ccc_days"] = panel["inv_days"] + panel["rec_days"] - panel["pay_days"]

    # Forward returns
    panel["ret3y_pct"] = safe_div(panel["price_fwd3"], panel["Stock Price (Rs)"]) - 1
    panel["ret5y_pct"] = safe_div(panel["price_fwd5"], panel["Stock Price (Rs)"]) - 1
    panel["ret7y_pct"] = safe_div(panel["price_fwd7"], panel["Stock Price (Rs)"]) - 1
    for c in ("ret3y_pct", "ret5y_pct", "ret7y_pct"):
        panel[c] = panel[c] * 100

    # Save feature panel
    keep_cols = [
        "nse_symbol", "base_year", "industry",
        "Stock Price (Rs)", "Market Cap (Rs Cr)", "P/E ratio",
        "fa_cagr3", "inv_cagr3", "rec_cagr3", "pay_cagr3",
        "assets_cagr3", "sales_cagr3", "profit_cagr3",
        "debt_to_equity", "roe_pct", "roce_pct",
        "asset_turnover", "cwip_to_fa",
        "inv_days", "rec_days", "pay_days", "ccc_days",
        "ret3y_pct", "ret5y_pct", "ret7y_pct",
    ]
    keep_cols = [c for c in keep_cols if c in panel.columns]
    feat = panel[keep_cols].copy()
    feat.to_csv(OUT_PANEL, index=False)
    print(f"Saved feature panel: {OUT_PANEL} ({len(feat):,} rows)")

    # ---------- Pattern testing ----------
    print("\nTesting signal patterns ...")

    SIGNALS: list[tuple[str, str]] = [
        # Capex / fixed-asset signals
        ("FA CAGR > 15% (heavy capex)", "fa_cagr3 > 15"),
        ("FA CAGR > 20%",               "fa_cagr3 > 20"),
        ("FA CAGR > 25%",               "fa_cagr3 > 25"),
        ("FA CAGR between 10% and 20% (steady capex)", "fa_cagr3.between(10, 20)"),
        ("FA CAGR < Sales CAGR (capital-efficient growth)",
                "fa_cagr3 < sales_cagr3 and sales_cagr3 > 10"),
        ("FA shrinking (CAGR < 0%)",    "fa_cagr3 < 0"),
        ("CWIP / FA > 25% (heavy investment pipeline)", "cwip_to_fa > 0.25"),

        # Working capital efficiency
        ("Inventory CAGR < Sales CAGR", "inv_cagr3 < sales_cagr3 and sales_cagr3 > 0"),
        ("Inventory days improving 3y", None),  # special pattern below
        ("Receivables CAGR < Sales CAGR (collections improving)",
                "rec_cagr3 < sales_cagr3 and sales_cagr3 > 0"),
        ("Receivables days < 30",        "rec_days < 30"),
        ("Receivables days < 60",        "rec_days < 60"),
        ("Payables CAGR > 0 (better supplier terms)", "pay_cagr3 > 0"),
        ("CCC days < 30 (efficient working capital)",  "ccc_days < 30"),
        ("CCC days < 60",                "ccc_days < 60"),

        # Return on capital signals
        ("ROCE > 15%",                  "roce_pct > 15"),
        ("ROCE > 20%",                  "roce_pct > 20"),
        ("ROCE > 25%",                  "roce_pct > 25"),
        ("ROCE > 30% (very high return)", "roce_pct > 30"),
        ("ROE > 15%",                   "roe_pct > 15"),
        ("ROE > 20%",                   "roe_pct > 20"),
        ("ROE > 25%",                   "roe_pct > 25"),

        # Leverage
        ("Debt/Equity < 0.3 (low leverage)", "debt_to_equity < 0.3"),
        ("Debt/Equity < 0.5",               "debt_to_equity < 0.5"),
        ("Debt/Equity > 1.0 (high leverage)","debt_to_equity > 1.0"),

        # Growth
        ("Sales CAGR > 15%",            "sales_cagr3 > 15"),
        ("Sales CAGR > 20%",            "sales_cagr3 > 20"),
        ("Profit CAGR > 15%",           "profit_cagr3 > 15"),
        ("Profit CAGR > 20%",           "profit_cagr3 > 20"),
        ("Profit CAGR > Sales CAGR (margin expanding)", "profit_cagr3 > sales_cagr3"),

        # Combined high-quality signals
        ("ROCE > 20% AND Sales CAGR > 15%", "roce_pct > 20 and sales_cagr3 > 15"),
        ("ROCE > 20% AND Debt/Equity < 0.3", "roce_pct > 20 and debt_to_equity < 0.3"),
        ("ROCE > 20% AND FA CAGR > 10% (profitable expansion)", "roce_pct > 20 and fa_cagr3 > 10"),
        ("ROE > 20% AND Sales CAGR > 15%",  "roe_pct > 20 and sales_cagr3 > 15"),
        ("ROCE > 25% AND ROE > 25% (super-quality)", "roce_pct > 25 and roe_pct > 25"),

        # Valuation crossed with quality
        # (P/E will be tested later as an overlay)
    ]

    def eval_signal(expr: str | None, df: pd.DataFrame) -> pd.Series:
        if expr is None:
            return pd.Series(False, index=df.index)
        # Build mask using pandas eval — fallback to manual eval if needed
        try:
            return df.eval(expr)
        except Exception:
            # Manual: walk the expression
            try:
                # For the 'and' compound exprs
                parts = [p.strip() for p in expr.split(" and ")]
                masks = []
                for p in parts:
                    if ".between(" in p:
                        # Handle e.g. fa_cagr3.between(10, 20)
                        col_part, between_part = p.split(".between(")
                        a, b = between_part.rstrip(")").split(",")
                        m = df[col_part.strip()].between(float(a), float(b))
                    else:
                        # Compare two columns or column-vs-number
                        for op_sym in (">=", "<=", ">", "<", "=="):
                            if op_sym in p:
                                left, right = [x.strip() for x in p.split(op_sym, 1)]
                                lvals = df[left] if left in df.columns else float(left)
                                rvals = df[right] if right in df.columns else float(right)
                                if op_sym == ">":
                                    m = lvals > rvals
                                elif op_sym == "<":
                                    m = lvals < rvals
                                elif op_sym == ">=":
                                    m = lvals >= rvals
                                elif op_sym == "<=":
                                    m = lvals <= rvals
                                else:
                                    m = lvals == rvals
                                break
                    masks.append(m)
                if len(masks) == 1:
                    return masks[0]
                # Combine with AND
                final = masks[0]
                for m in masks[1:]:
                    final = final & m
                return final
            except Exception as e:
                print(f"  ERROR evaluating {expr!r}: {e}")
                return pd.Series(False, index=df.index)

    # For each signal × horizon, compute hit rate, mean return, count
    rows = []
    for name, expr in SIGNALS:
        for horizon, col in (("3y", "ret3y_pct"), ("5y", "ret5y_pct"), ("7y", "ret7y_pct")):
            if col not in feat.columns:
                continue
            mask = eval_signal(expr, feat)
            sub = feat[mask & feat[col].notna()]
            n = len(sub)
            if n < 10:
                continue
            hits = (sub[col] > 0).sum()
            rate = hits / n if n > 0 else 0
            avg = sub[col].mean()
            median = sub[col].median()
            rows.append({
                "signal": name,
                "horizon": horizon,
                "n": n,
                "hits_positive": int(hits),
                "hit_rate_pct": round(rate * 100, 1),
                "avg_return_pct": round(avg, 1),
                "median_return_pct": round(median, 1),
            })

    results = pd.DataFrame(rows).sort_values(["hit_rate_pct", "n"], ascending=[False, False])
    results.to_csv(OUT_RESULTS, index=False)
    print(f"\nAll patterns: {OUT_RESULTS} ({len(results)} rows)")

    # Top patterns (>= 80% hit rate, n >= 30)
    top = results[(results["hit_rate_pct"] >= 80) & (results["n"] >= 30)].copy()
    top.to_csv(OUT_TOP, index=False)
    print(f"Top patterns (>= 80%, n >= 30): {OUT_TOP} ({len(top)} rows)")
    print()
    print(top.to_string(index=False))


if __name__ == "__main__":
    main()
