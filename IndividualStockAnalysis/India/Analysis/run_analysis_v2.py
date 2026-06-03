"""
Detailed balance-sheet → forward stock-CAGR analysis.

Stricter test than `run_analysis.py`:
  - Outcome = forward stock-price CAGR >= 20% (not just positive returns)
  - Coverage: ALL 500 companies × ALL years × {3y, 5y, 7y} horizons
  - Signals: 60+ balance-sheet-only definitions (no P&L)
  - Threshold: hit rate >= 80%, n >= 20
  - Report: for each qualifying pattern, lists every (company, base_year)
    instance with its realized CAGR

Forward CAGR thresholds:
  3-year CAGR >= 20%  =>  total return >= 72.8%
  5-year CAGR >= 20%  =>  total return >= 148.8%
  7-year CAGR >= 20%  =>  total return >= 258.3%

Outputs (this folder):
  cagr_pattern_results.csv        — every signal × horizon row
  cagr_top_patterns_80pct.csv     — only signals with hit_rate >= 80%
  cagr_pattern_companies.csv      — per-pattern company list (long)
  panel_with_cagr.csv             — full feature + outcome panel

Usage:
  python3 run_analysis_v2.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
DATA_BS = HERE.parent / "BalanceSheet" / "_all_balance_sheets_long.csv"
DATA_SI = HERE.parent / "StockInfo" / "_all_stock_info_long.csv"
DATA_CON = HERE.parent / "Nifty500" / "nifty500_constituents.csv"

OUT_RESULTS = HERE / "cagr_pattern_results.csv"
OUT_TOP = HERE / "cagr_top_patterns_80pct.csv"
OUT_COMPANIES = HERE / "cagr_pattern_companies.csv"
OUT_PANEL = HERE / "panel_with_cagr.csv"

CAGR_THRESHOLD = 20.0  # %
MIN_N = 20


def load_wide_bs(long_csv: Path) -> pd.DataFrame:
    df = pd.read_csv(long_csv)
    if "parent_line_item" in df.columns:
        df["_p"] = df["parent_line_item"].fillna("").astype(str).str.len()
        df = df.sort_values("_p").drop_duplicates(
            subset=["nse_symbol", "year", "line_item"], keep="first"
        ).drop(columns=["_p"])
    return df.pivot_table(
        index=["nse_symbol", "year"], columns="line_item",
        values="value_rs_cr", aggfunc="first"
    )


def load_wide_si(long_csv: Path) -> pd.DataFrame:
    df = pd.read_csv(long_csv)
    return df.pivot_table(
        index=["nse_symbol", "year"], columns="metric",
        values="value", aggfunc="first"
    )


def year_to_int(y: str) -> int | None:
    parts = str(y).split()
    if len(parts) == 2 and parts[0] == "Mar":
        try:
            return int(parts[1])
        except ValueError:
            return None
    return None


def safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    out = pd.Series(np.nan, index=a.index, dtype=float)
    mask = a.notna() & b.notna() & (b != 0)
    out[mask] = a[mask] / b[mask]
    return out


def safe_cagr(end: pd.Series, start: pd.Series, years: int) -> pd.Series:
    out = pd.Series(np.nan, index=end.index, dtype=float)
    mask = end.notna() & start.notna() & (start > 0) & (end > 0)
    out[mask] = ((end[mask] / start[mask]) ** (1 / years) - 1) * 100
    return out


def main() -> None:
    print("Loading data ...")
    bs = load_wide_bs(DATA_BS)
    si = load_wide_si(DATA_SI)
    const = pd.read_csv(DATA_CON)
    print(f"  BS: {bs.shape}, SI: {si.shape}")

    # Merge; index = (symbol, year). bs has BS line items, si has stock info.
    panel = bs.join(si, how="outer").reset_index()
    panel["base_year"] = panel["year"].apply(year_to_int)
    panel = panel.dropna(subset=["base_year"]).copy()
    panel["base_year"] = panel["base_year"].astype(int)

    panel["industry"] = panel["nse_symbol"].map(
        dict(zip(const["nse_symbol"], const["industry"]))
    )

    panel = panel.sort_values(["nse_symbol", "base_year"]).reset_index(drop=True)
    g = panel.groupby("nse_symbol", group_keys=False)

    # Lagged values for CAGR computation
    BS_LAGGABLE = [
        "Fixed Assets", "CWIP", "Investments", "Total Assets",
        "Equity Capital", "Reserves", "Borrowings", "Total Liabilities",
        "Inventories", "Trade receivables", "Cash Equivalents", "Trade Payables",
    ]
    for col in BS_LAGGABLE:
        if col in panel.columns:
            panel[f"{col}__lag1"] = g[col].shift(1)
            panel[f"{col}__lag2"] = g[col].shift(2)
            panel[f"{col}__lag3"] = g[col].shift(3)
            panel[f"{col}__lag5"] = g[col].shift(5)

    # Forward price
    if "Stock Price (Rs)" not in panel.columns:
        raise RuntimeError("Stock Price (Rs) column missing")
    panel["price_fwd3"] = g["Stock Price (Rs)"].shift(-3)
    panel["price_fwd5"] = g["Stock Price (Rs)"].shift(-5)
    panel["price_fwd7"] = g["Stock Price (Rs)"].shift(-7)

    # Forward CAGRs
    panel["cagr3y_pct"] = safe_cagr(panel["price_fwd3"], panel["Stock Price (Rs)"], 3)
    panel["cagr5y_pct"] = safe_cagr(panel["price_fwd5"], panel["Stock Price (Rs)"], 5)
    panel["cagr7y_pct"] = safe_cagr(panel["price_fwd7"], panel["Stock Price (Rs)"], 7)

    print("Computing derived BS-only features ...")

    # ---- Derived features ----
    # 1y, 3y, 5y CAGRs for key items
    for col in BS_LAGGABLE:
        if col in panel.columns:
            for ny in (1, 3, 5):
                lag = panel.get(f"{col}__lag{ny}")
                if lag is not None:
                    name = col.lower().replace(" ", "_") + f"_cagr{ny}y"
                    panel[name] = safe_cagr(panel[col], lag, ny)

    # Balance-sheet ratios
    equity_total = panel["Equity Capital"] + panel["Reserves"]
    panel["debt_to_equity"] = safe_div(panel["Borrowings"], equity_total)
    panel["reserves_to_equity_cap"] = safe_div(panel["Reserves"], panel["Equity Capital"])
    panel["cash_to_assets"] = safe_div(panel["Cash Equivalents"], panel["Total Assets"])
    panel["fa_to_assets"] = safe_div(panel["Fixed Assets"], panel["Total Assets"])
    panel["inv_to_assets"] = safe_div(panel["Inventories"], panel["Total Assets"])
    panel["rec_to_assets"] = safe_div(panel["Trade receivables"], panel["Total Assets"])
    panel["pay_to_assets"] = safe_div(panel["Trade Payables"], panel["Total Assets"])
    panel["cwip_to_fa"] = safe_div(panel["CWIP"], panel["Fixed Assets"])
    panel["borrowings_to_assets"] = safe_div(panel["Borrowings"], panel["Total Assets"])
    panel["investments_to_assets"] = safe_div(panel["Investments"], panel["Total Assets"])

    # Change in ratios (yoy)
    for col in ("debt_to_equity", "fa_to_assets", "cash_to_assets", "cwip_to_fa"):
        if col in panel.columns:
            panel[f"{col}__lag3"] = g[col].shift(3)

    # Save panel
    keep = ["nse_symbol", "base_year", "industry", "Stock Price (Rs)",
            "Market Cap (Rs Cr)", "cagr3y_pct", "cagr5y_pct", "cagr7y_pct"]
    derived_cols = [c for c in panel.columns if any(
        c.endswith(s) for s in ("_cagr1y", "_cagr3y", "_cagr5y", "_to_assets", "_to_equity", "_to_fa", "_to_equity_cap")
    ) or c == "debt_to_equity"]
    keep_full = list(set(keep + derived_cols))
    panel[keep_full].to_csv(OUT_PANEL, index=False)
    print(f"Saved panel: {OUT_PANEL} ({len(panel):,} rows)")

    # ---- Signal definitions (BS-only) ----
    SIGNALS: list[tuple[str, str]] = [
        # Single-factor: balance-sheet growth signals (3-year)
        ("Reserves CAGR (3y) > 20% (strong retained earnings)", "reserves_cagr3y > 20"),
        ("Reserves CAGR (3y) > 25%", "reserves_cagr3y > 25"),
        ("Reserves CAGR (3y) > 30%", "reserves_cagr3y > 30"),
        ("Total Assets CAGR (3y) > 15%", "total_assets_cagr3y > 15"),
        ("Total Assets CAGR (3y) > 20%", "total_assets_cagr3y > 20"),
        ("Fixed Assets CAGR (3y) > 15%", "fixed_assets_cagr3y > 15"),
        ("Fixed Assets CAGR (3y) > 20%", "fixed_assets_cagr3y > 20"),
        ("Fixed Assets CAGR (3y) > 25%", "fixed_assets_cagr3y > 25"),
        ("FA CAGR (3y) between 10-25%", "fixed_assets_cagr3y.between(10, 25)"),
        ("Fixed Assets shrinking 3y (CAGR < 0%)", "fixed_assets_cagr3y < 0"),
        ("Borrowings shrinking 3y (CAGR < 0%)", "borrowings_cagr3y < 0"),
        ("Cash Equivalents CAGR (3y) > 20%", "cash_equivalents_cagr3y > 20"),
        ("Investments CAGR (3y) > 20%", "investments_cagr3y > 20"),

        # 5-year history
        ("Reserves CAGR (5y) > 20%", "reserves_cagr5y > 20"),
        ("Reserves CAGR (5y) > 25%", "reserves_cagr5y > 25"),
        ("Total Assets CAGR (5y) > 15%", "total_assets_cagr5y > 15"),
        ("Total Assets CAGR (5y) > 20%", "total_assets_cagr5y > 20"),
        ("Fixed Assets CAGR (5y) > 15%", "fixed_assets_cagr5y > 15"),
        ("Fixed Assets CAGR (5y) > 20%", "fixed_assets_cagr5y > 20"),

        # Static balance-sheet ratios
        ("Debt/Equity < 0.3 (low leverage)", "debt_to_equity < 0.3"),
        ("Debt/Equity < 0.5", "debt_to_equity < 0.5"),
        ("Debt/Equity < 0.1 (near zero debt)", "debt_to_equity < 0.1"),
        ("Reserves > 10x Equity Capital (mature compounder)", "reserves_to_equity_cap > 10"),
        ("Reserves > 20x Equity Capital", "reserves_to_equity_cap > 20"),
        ("Reserves > 50x Equity Capital", "reserves_to_equity_cap > 50"),
        ("Cash > 10% of Total Assets", "cash_to_assets > 0.1"),
        ("Cash > 20% of Total Assets", "cash_to_assets > 0.2"),
        ("CWIP > 15% of Fixed Assets (heavy pipeline)", "cwip_to_fa > 0.15"),
        ("CWIP > 25% of Fixed Assets", "cwip_to_fa > 0.25"),
        ("CWIP > 40% of Fixed Assets (very heavy pipeline)", "cwip_to_fa > 0.4"),
        ("Borrowings < 10% of Total Assets (low debt)", "borrowings_to_assets < 0.1"),
        ("Borrowings < 5% of Total Assets (very low debt)", "borrowings_to_assets < 0.05"),
        ("Investments > 20% of Total Assets (holding co. style)", "investments_to_assets > 0.2"),

        # Combined high-quality signals (BS-only)
        ("Reserves CAGR > 20% AND Debt/Equity < 0.5",
            "reserves_cagr3y > 20 and debt_to_equity < 0.5"),
        ("Reserves CAGR > 20% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 20 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 25% AND Debt/Equity < 0.5",
            "reserves_cagr3y > 25 and debt_to_equity < 0.5"),
        ("Reserves CAGR > 30% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 30 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 20% AND Cash CAGR > 15%",
            "reserves_cagr3y > 20 and cash_equivalents_cagr3y > 15"),
        ("FA CAGR > 15% AND Debt/Equity < 0.5 (low-debt capex)",
            "fixed_assets_cagr3y > 15 and debt_to_equity < 0.5"),
        ("FA CAGR > 15% AND Reserves CAGR > 20% (profitable expansion)",
            "fixed_assets_cagr3y > 15 and reserves_cagr3y > 20"),
        ("FA CAGR > 20% AND Reserves CAGR > 25%",
            "fixed_assets_cagr3y > 20 and reserves_cagr3y > 25"),
        ("FA CAGR > 25% AND Reserves CAGR > 25% (aggressive growth + retained)",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25"),
        ("Total Assets CAGR > 15% AND Debt/Equity < 0.5",
            "total_assets_cagr3y > 15 and debt_to_equity < 0.5"),
        ("Total Assets CAGR > 20% AND Debt/Equity < 0.3",
            "total_assets_cagr3y > 20 and debt_to_equity < 0.3"),
        ("CWIP/FA > 25% AND Debt/Equity < 0.5 (low-debt heavy capex)",
            "cwip_to_fa > 0.25 and debt_to_equity < 0.5"),
        ("Cash > 20% of TA AND Reserves CAGR > 20%",
            "cash_to_assets > 0.2 and reserves_cagr3y > 20"),
        ("Cash > 10% of TA AND Debt/Equity < 0.3",
            "cash_to_assets > 0.1 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 25% AND FA CAGR < 25% (capital-efficient compounding)",
            "reserves_cagr3y > 25 and fixed_assets_cagr3y < 25"),
        ("Reserves CAGR > 15% AND Borrowings CAGR < 0% (deleveraging compounder)",
            "reserves_cagr3y > 15 and borrowings_cagr3y < 0"),

        # 5-year history-based screens
        ("Reserves CAGR (5y) > 20% AND Debt/Equity < 0.5",
            "reserves_cagr5y > 20 and debt_to_equity < 0.5"),
        ("FA CAGR (5y) > 15% AND Reserves CAGR (5y) > 20%",
            "fixed_assets_cagr5y > 15 and reserves_cagr5y > 20"),
        ("Total Assets CAGR (5y) > 15% AND Reserves CAGR (5y) > 20%",
            "total_assets_cagr5y > 15 and reserves_cagr5y > 20"),

        # Triple-screen highest quality
        ("Reserves CAGR > 20% AND Debt/Equity < 0.3 AND FA CAGR > 10%",
            "reserves_cagr3y > 20 and debt_to_equity < 0.3 and fixed_assets_cagr3y > 10"),
        ("Reserves CAGR > 25% AND Cash > 10% of TA AND Debt/Equity < 0.5",
            "reserves_cagr3y > 25 and cash_to_assets > 0.1 and debt_to_equity < 0.5"),
    ]

    feat = panel.copy()

    def eval_signal(expr: str, df: pd.DataFrame) -> pd.Series:
        try:
            return df.eval(expr)
        except Exception:
            # Parse 'X and Y and Z' manually
            parts = [p.strip() for p in expr.split(" and ")]
            masks = []
            for p in parts:
                if ".between(" in p:
                    col_part, between_part = p.split(".between(")
                    a, b = between_part.rstrip(")").split(",")
                    masks.append(df[col_part.strip()].between(float(a), float(b)))
                    continue
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
                        masks.append(m)
                        break
            final = masks[0]
            for m in masks[1:]:
                final = final & m
            return final

    # ---- Run all signal × horizon tests ----
    print(f"\nTesting {len(SIGNALS)} signals × 3 horizons ...")
    results = []
    company_rows: list[dict] = []

    for name, expr in SIGNALS:
        try:
            mask = eval_signal(expr, feat).fillna(False)
        except Exception as e:
            print(f"  ERROR for '{name}': {e}")
            continue

        for horizon, col in (("3y", "cagr3y_pct"), ("5y", "cagr5y_pct"), ("7y", "cagr7y_pct")):
            sub = feat[mask & feat[col].notna()].copy()
            n = len(sub)
            if n < MIN_N:
                continue
            hits = (sub[col] >= CAGR_THRESHOLD).sum()
            rate = hits / n
            avg = sub[col].mean()
            median = sub[col].median()
            results.append({
                "signal": name,
                "horizon": horizon,
                "n": n,
                "hits_cagr_geq_20pct": int(hits),
                "hit_rate_pct": round(rate * 100, 1),
                "avg_cagr_pct": round(avg, 1),
                "median_cagr_pct": round(median, 1),
            })

            # For patterns at >= 80%, record the company instances
            if rate >= 0.80:
                for _, row in sub.iterrows():
                    company_rows.append({
                        "signal": name,
                        "horizon": horizon,
                        "nse_symbol": row["nse_symbol"],
                        "industry": row["industry"],
                        "base_year": int(row["base_year"]),
                        "stock_price_at_base": round(row["Stock Price (Rs)"], 2) if pd.notna(row["Stock Price (Rs)"]) else None,
                        "forward_cagr_pct": round(row[col], 1),
                        "met_20pct_cagr": "Y" if row[col] >= CAGR_THRESHOLD else "N",
                    })

    results_df = pd.DataFrame(results).sort_values(
        ["hit_rate_pct", "n"], ascending=[False, False]
    )
    results_df.to_csv(OUT_RESULTS, index=False)
    print(f"\nAll results: {OUT_RESULTS} ({len(results_df)} rows)")

    top = results_df[results_df["hit_rate_pct"] >= 80].copy()
    top.to_csv(OUT_TOP, index=False)
    print(f"Top patterns (>= 80% hit rate, n >= {MIN_N}): {OUT_TOP} ({len(top)} rows)")

    companies_df = pd.DataFrame(company_rows).sort_values(
        ["signal", "horizon", "forward_cagr_pct"], ascending=[True, True, False]
    )
    companies_df.to_csv(OUT_COMPANIES, index=False)
    print(f"Per-pattern company list: {OUT_COMPANIES} ({len(companies_df):,} rows)")

    print()
    print("=== TOP PATTERNS (>= 80% hit rate for CAGR >= 20%, n >= 20) ===")
    print(top.to_string(index=False))


if __name__ == "__main__":
    main()
