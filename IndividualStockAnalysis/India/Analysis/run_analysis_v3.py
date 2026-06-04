"""
Detailed BS-only screen for patterns that predict forward stock CAGR >= 20%
with the highest achievable hit rate. Covers ALL 500 companies × ALL years
× {3y, 5y, 7y} horizons.

Strategy:
  - Test ~90 signal definitions (BS-only): single conditions, two-factor
    combinations, three-factor combinations, persistence (multi-year)
    signals, and ratio-improvement signals.
  - For each signal × horizon, compute:
      n = sample size
      hits = # of cases with forward CAGR >= 20%
      hit_rate_pct = hits / n
      avg_cagr_pct = mean forward CAGR
  - Report patterns where hit_rate_pct >= 80% AND n >= 15.
  - If no pattern hits 80%, report the best achievable (hit_rate_pct >= 70%)
    plus the per-company list to make findings actionable.

Outputs:
  cagr_v3_pattern_results.csv
  cagr_v3_top_patterns.csv             — best patterns (>= 70% hit rate)
  cagr_v3_pattern_companies.csv        — every (pattern, company, base_year)
                                          row for >=70% patterns
  cagr_v3_company_scorecard.csv        — per company, which qualifying
                                          patterns it has matched over its
                                          history with the realized CAGR
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
DATA_BS = HERE.parent / "BalanceSheet" / "Nifty500" / "_all_balance_sheets_long.csv"
DATA_SI = HERE.parent / "StockInfo" / "Nifty500" / "_all_stock_info_long.csv"
DATA_CON = HERE.parent / "Nifty500" / "nifty500_constituents.csv"

OUT_RESULTS = HERE / "cagr_v3_pattern_results.csv"
OUT_TOP = HERE / "cagr_v3_top_patterns.csv"
OUT_COMPANIES = HERE / "cagr_v3_pattern_companies.csv"
OUT_SCORECARD = HERE / "cagr_v3_company_scorecard.csv"

CAGR_THRESHOLD = 20.0
MIN_N = 15
REPORT_HIT_RATE = 70.0  # we'll dump everything >= 70% for analysis


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


def safe_div(a, b):
    out = pd.Series(np.nan, index=a.index, dtype=float)
    mask = a.notna() & b.notna() & (b != 0)
    out[mask] = a[mask] / b[mask]
    return out


def safe_cagr(end, start, years):
    out = pd.Series(np.nan, index=end.index, dtype=float)
    mask = end.notna() & start.notna() & (start > 0) & (end > 0)
    out[mask] = ((end[mask] / start[mask]) ** (1 / years) - 1) * 100
    return out


def main() -> None:
    print("Loading data ...")
    bs = load_wide_bs(DATA_BS)
    si = load_wide_si(DATA_SI)
    const = pd.read_csv(DATA_CON)

    panel = bs.join(si, how="outer").reset_index()
    panel["base_year"] = panel["year"].apply(year_to_int)
    panel = panel.dropna(subset=["base_year"]).copy()
    panel["base_year"] = panel["base_year"].astype(int)
    panel["industry"] = panel["nse_symbol"].map(
        dict(zip(const["nse_symbol"], const["industry"]))
    )
    panel = panel.sort_values(["nse_symbol", "base_year"]).reset_index(drop=True)
    g = panel.groupby("nse_symbol", group_keys=False)

    # Lagged values for CAGR calcs
    BS_LAGGABLE = [
        "Fixed Assets", "CWIP", "Investments", "Total Assets",
        "Equity Capital", "Reserves", "Borrowings", "Total Liabilities",
        "Inventories", "Trade receivables", "Cash Equivalents", "Trade Payables",
        "Long term Borrowings", "Short term Borrowings",
    ]
    BS_LAGGABLE = [c for c in BS_LAGGABLE if c in panel.columns]

    add_cols: dict[str, pd.Series] = {}
    for col in BS_LAGGABLE:
        for ny in (1, 2, 3, 5):
            add_cols[f"{col}__lag{ny}"] = g[col].shift(ny)

    # Forward price
    add_cols["price_fwd3"] = g["Stock Price (Rs)"].shift(-3)
    add_cols["price_fwd5"] = g["Stock Price (Rs)"].shift(-5)
    add_cols["price_fwd7"] = g["Stock Price (Rs)"].shift(-7)

    panel = pd.concat([panel, pd.DataFrame(add_cols)], axis=1)

    print("Computing derived BS-only features ...")

    # Forward CAGRs
    panel["cagr3y_pct"] = safe_cagr(panel["price_fwd3"], panel["Stock Price (Rs)"], 3)
    panel["cagr5y_pct"] = safe_cagr(panel["price_fwd5"], panel["Stock Price (Rs)"], 5)
    panel["cagr7y_pct"] = safe_cagr(panel["price_fwd7"], panel["Stock Price (Rs)"], 7)

    derived: dict[str, pd.Series] = {}
    # CAGRs over 1y, 3y, 5y
    for col in BS_LAGGABLE:
        for ny in (1, 3, 5):
            lag = panel[f"{col}__lag{ny}"]
            name = col.lower().replace(" ", "_") + f"_cagr{ny}y"
            derived[name] = safe_cagr(panel[col], lag, ny)
    # YoY changes for each year (for persistence checks)
    for col in BS_LAGGABLE:
        for ny in (1, 2, 3):
            lag = panel[f"{col}__lag{ny}"]
            name = col.lower().replace(" ", "_") + f"_yoy{ny}y"
            derived[name] = safe_cagr(panel[col], lag, 1) if ny == 1 else None  # placeholder
    # Actually let me explicitly compute YoY growth for persistence
    for col in BS_LAGGABLE:
        # YoY this year, 1 year ago, 2 years ago
        for shift_n, name in ((0, "current_yoy"), (1, "lag1_yoy"), (2, "lag2_yoy")):
            shifted = g[col].shift(shift_n)
            shifted_lag = g[col].shift(shift_n + 1)
            yoy = safe_cagr(shifted, shifted_lag, 1)
            derived[f"{col.lower().replace(' ', '_')}_{name}"] = yoy
    # Ratios
    equity_total = panel["Equity Capital"] + panel["Reserves"]
    derived["debt_to_equity"] = safe_div(panel["Borrowings"], equity_total)
    derived["reserves_to_equity_cap"] = safe_div(panel["Reserves"], panel["Equity Capital"])
    derived["cash_to_assets"] = safe_div(panel["Cash Equivalents"], panel["Total Assets"])
    derived["fa_to_assets"] = safe_div(panel["Fixed Assets"], panel["Total Assets"])
    derived["inv_to_assets"] = safe_div(panel["Inventories"], panel["Total Assets"])
    derived["rec_to_assets"] = safe_div(panel["Trade receivables"], panel["Total Assets"])
    derived["cwip_to_fa"] = safe_div(panel["CWIP"], panel["Fixed Assets"])
    derived["borrowings_to_assets"] = safe_div(panel["Borrowings"], panel["Total Assets"])
    derived["cash_plus_investments_to_assets"] = safe_div(
        panel["Cash Equivalents"] + panel["Investments"], panel["Total Assets"]
    )
    derived["total_capital_employed"] = equity_total + panel["Borrowings"]

    # Filter out None placeholders
    derived = {k: v for k, v in derived.items() if v is not None}

    panel = pd.concat([panel, pd.DataFrame(derived)], axis=1)

    # ---- Build SIGNAL definitions ----
    SIGNALS: list[tuple[str, str]] = [
        # ===== Single-factor static screens (very tight) =====
        ("Debt/Equity < 0.05 (debt-free)", "debt_to_equity < 0.05"),
        ("Debt/Equity < 0.10", "debt_to_equity < 0.10"),
        ("Reserves > 100x Equity Capital (mature compounder)", "reserves_to_equity_cap > 100"),
        ("Reserves > 50x Equity Capital", "reserves_to_equity_cap > 50"),
        ("Cash+Investments > 30% of Total Assets", "cash_plus_investments_to_assets > 0.30"),
        ("Cash+Investments > 40% of Total Assets", "cash_plus_investments_to_assets > 0.40"),

        # ===== Growth signals (single) =====
        ("Reserves CAGR (3y) > 25%", "reserves_cagr3y > 25"),
        ("Reserves CAGR (3y) > 30%", "reserves_cagr3y > 30"),
        ("Reserves CAGR (5y) > 25%", "reserves_cagr5y > 25"),
        ("Fixed Assets CAGR (3y) > 25%", "fixed_assets_cagr3y > 25"),
        ("Fixed Assets CAGR (3y) > 30%", "fixed_assets_cagr3y > 30"),
        ("Total Assets CAGR (3y) > 20%", "total_assets_cagr3y > 20"),

        # ===== Two-factor: capital efficiency =====
        ("Reserves CAGR > 25% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 25 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 25% AND Debt/Equity < 0.1",
            "reserves_cagr3y > 25 and debt_to_equity < 0.1"),
        ("Reserves CAGR > 30% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 30 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 30% AND Debt/Equity < 0.1",
            "reserves_cagr3y > 30 and debt_to_equity < 0.1"),
        ("FA CAGR > 20% AND Debt/Equity < 0.3",
            "fixed_assets_cagr3y > 20 and debt_to_equity < 0.3"),
        ("FA CAGR > 25% AND Debt/Equity < 0.3",
            "fixed_assets_cagr3y > 25 and debt_to_equity < 0.3"),
        ("FA CAGR > 25% AND Debt/Equity < 0.1",
            "fixed_assets_cagr3y > 25 and debt_to_equity < 0.1"),
        ("FA CAGR > 20% AND Reserves CAGR > 25%",
            "fixed_assets_cagr3y > 20 and reserves_cagr3y > 25"),
        ("FA CAGR > 25% AND Reserves CAGR > 25%",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25"),
        ("FA CAGR > 25% AND Reserves CAGR > 30%",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 30"),

        # ===== Two-factor: working capital quality =====
        ("Reserves CAGR > 25% AND Cash CAGR > 20%",
            "reserves_cagr3y > 25 and cash_equivalents_cagr3y > 20"),
        ("Reserves CAGR > 25% AND Cash > 15% of TA",
            "reserves_cagr3y > 25 and cash_to_assets > 0.15"),
        ("Reserves CAGR > 30% AND Cash > 10% of TA",
            "reserves_cagr3y > 30 and cash_to_assets > 0.10"),
        ("Cash > 20% of TA AND Debt/Equity < 0.1",
            "cash_to_assets > 0.20 and debt_to_equity < 0.10"),
        ("Cash > 25% of TA AND Debt/Equity < 0.1",
            "cash_to_assets > 0.25 and debt_to_equity < 0.10"),

        # ===== Three-factor: comprehensive high-quality screen =====
        ("Reserves CAGR > 25% AND Debt/Equity < 0.3 AND FA CAGR > 15%",
            "reserves_cagr3y > 25 and debt_to_equity < 0.3 and fixed_assets_cagr3y > 15"),
        ("Reserves CAGR > 25% AND Debt/Equity < 0.5 AND FA CAGR > 10%",
            "reserves_cagr3y > 25 and debt_to_equity < 0.5 and fixed_assets_cagr3y > 10"),
        ("Reserves CAGR > 30% AND Debt/Equity < 0.5 AND FA CAGR > 15%",
            "reserves_cagr3y > 30 and debt_to_equity < 0.5 and fixed_assets_cagr3y > 15"),
        ("Reserves CAGR > 25% AND Cash > 15% of TA AND Debt/Equity < 0.3",
            "reserves_cagr3y > 25 and cash_to_assets > 0.15 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 25% AND TA CAGR > 15% AND Debt/Equity < 0.5",
            "reserves_cagr3y > 25 and total_assets_cagr3y > 15 and debt_to_equity < 0.5"),
        ("FA CAGR > 25% AND Reserves CAGR > 25% AND Debt/Equity < 0.5",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25 and debt_to_equity < 0.5"),
        ("FA CAGR > 25% AND Reserves CAGR > 25% AND Debt/Equity < 0.3",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25 and debt_to_equity < 0.3"),

        # ===== Persistence signals (multi-year growth) =====
        ("Reserves grew > 20% YoY in each of last 3 years",
            "reserves_current_yoy > 20 and reserves_lag1_yoy > 20 and reserves_lag2_yoy > 20"),
        ("Reserves grew > 25% YoY in each of last 3 years",
            "reserves_current_yoy > 25 and reserves_lag1_yoy > 25 and reserves_lag2_yoy > 25"),
        ("Reserves grew > 15% YoY in each of last 3 years",
            "reserves_current_yoy > 15 and reserves_lag1_yoy > 15 and reserves_lag2_yoy > 15"),
        ("Fixed Assets grew > 15% YoY in each of last 3 years (sustained capex)",
            "fixed_assets_current_yoy > 15 and fixed_assets_lag1_yoy > 15 and fixed_assets_lag2_yoy > 15"),
        ("Total Assets grew > 15% YoY in each of last 3 years",
            "total_assets_current_yoy > 15 and total_assets_lag1_yoy > 15 and total_assets_lag2_yoy > 15"),

        # ===== Combined persistence + low-debt =====
        ("Reserves > 20% YoY for 3 yrs AND Debt/Equity < 0.3",
            "reserves_current_yoy > 20 and reserves_lag1_yoy > 20 and reserves_lag2_yoy > 20 and debt_to_equity < 0.3"),
        ("Reserves > 25% YoY for 3 yrs AND Debt/Equity < 0.5",
            "reserves_current_yoy > 25 and reserves_lag1_yoy > 25 and reserves_lag2_yoy > 25 and debt_to_equity < 0.5"),
        ("Reserves > 25% YoY for 3 yrs AND Debt/Equity < 0.3",
            "reserves_current_yoy > 25 and reserves_lag1_yoy > 25 and reserves_lag2_yoy > 25 and debt_to_equity < 0.3"),

        # ===== Persistence + growth =====
        ("Reserves & FA both > 20% YoY for 3 yrs",
            "reserves_current_yoy > 20 and reserves_lag1_yoy > 20 and reserves_lag2_yoy > 20 and fixed_assets_current_yoy > 20 and fixed_assets_lag1_yoy > 20 and fixed_assets_lag2_yoy > 20"),
        ("Reserves & FA both > 15% YoY for 3 yrs",
            "reserves_current_yoy > 15 and reserves_lag1_yoy > 15 and reserves_lag2_yoy > 15 and fixed_assets_current_yoy > 15 and fixed_assets_lag1_yoy > 15 and fixed_assets_lag2_yoy > 15"),

        # ===== Deleveraging compounders =====
        ("Reserves CAGR > 20% AND Borrowings CAGR < -10% (deleveraging)",
            "reserves_cagr3y > 20 and borrowings_cagr3y < -10"),
        ("Reserves CAGR > 25% AND Borrowings CAGR < 0%",
            "reserves_cagr3y > 25 and borrowings_cagr3y < 0"),
        ("Reserves CAGR > 30% AND Borrowings CAGR < 0%",
            "reserves_cagr3y > 30 and borrowings_cagr3y < 0"),
        ("Reserves CAGR > 30% AND Borrowings CAGR < -10%",
            "reserves_cagr3y > 30 and borrowings_cagr3y < -10"),

        # ===== 5-year sustained quality =====
        ("Reserves CAGR (5y) > 20% AND Debt/Equity < 0.3",
            "reserves_cagr5y > 20 and debt_to_equity < 0.3"),
        ("Reserves CAGR (5y) > 25% AND Debt/Equity < 0.3",
            "reserves_cagr5y > 25 and debt_to_equity < 0.3"),
        ("Reserves CAGR (5y) > 25% AND Debt/Equity < 0.5",
            "reserves_cagr5y > 25 and debt_to_equity < 0.5"),
        ("Reserves CAGR (5y) > 20% AND FA CAGR (5y) > 15% AND Debt/Equity < 0.5",
            "reserves_cagr5y > 20 and fixed_assets_cagr5y > 15 and debt_to_equity < 0.5"),
        ("Reserves CAGR (5y) > 25% AND FA CAGR (5y) > 15% AND Debt/Equity < 0.5",
            "reserves_cagr5y > 25 and fixed_assets_cagr5y > 15 and debt_to_equity < 0.5"),
    ]

    def eval_signal(expr: str, df: pd.DataFrame) -> pd.Series:
        try:
            return df.eval(expr)
        except Exception:
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
                            masks.append(lvals > rvals)
                        elif op_sym == "<":
                            masks.append(lvals < rvals)
                        elif op_sym == ">=":
                            masks.append(lvals >= rvals)
                        elif op_sym == "<=":
                            masks.append(lvals <= rvals)
                        else:
                            masks.append(lvals == rvals)
                        break
            final = masks[0]
            for m in masks[1:]:
                final = final & m
            return final

    # ---- Run tests ----
    print(f"\nTesting {len(SIGNALS)} signals × 3 horizons ...")
    results = []
    company_rows = []

    for name, expr in SIGNALS:
        try:
            mask = eval_signal(expr, panel).fillna(False)
        except Exception as e:
            print(f"  ERROR for '{name}': {e}")
            continue

        for horizon, col in (("3y", "cagr3y_pct"), ("5y", "cagr5y_pct"), ("7y", "cagr7y_pct")):
            sub = panel[mask & panel[col].notna()].copy()
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
                "hits": int(hits),
                "hit_rate_pct": round(rate * 100, 1),
                "avg_cagr_pct": round(avg, 1),
                "median_cagr_pct": round(median, 1),
                "min_cagr_pct": round(sub[col].min(), 1),
                "max_cagr_pct": round(sub[col].max(), 1),
            })

            # Capture company rows for >= 70% hit rate (for analysis)
            if rate >= REPORT_HIT_RATE / 100:
                for _, row in sub.iterrows():
                    company_rows.append({
                        "signal": name,
                        "horizon": horizon,
                        "nse_symbol": row["nse_symbol"],
                        "industry": row["industry"],
                        "base_year": int(row["base_year"]),
                        "stock_price_at_base": round(row["Stock Price (Rs)"], 2) if pd.notna(row["Stock Price (Rs)"]) else None,
                        "forward_cagr_pct": round(row[col], 1),
                        "met_20pct_target": "Y" if row[col] >= CAGR_THRESHOLD else "N",
                    })

    results_df = pd.DataFrame(results).sort_values(
        ["hit_rate_pct", "n"], ascending=[False, False]
    )
    results_df.to_csv(OUT_RESULTS, index=False)
    print(f"All results: {OUT_RESULTS} ({len(results_df)} rows)")

    top = results_df[results_df["hit_rate_pct"] >= REPORT_HIT_RATE].copy()
    top.to_csv(OUT_TOP, index=False)
    print(f"Top patterns (>= {REPORT_HIT_RATE}% hit rate): {OUT_TOP} ({len(top)} rows)")

    if company_rows:
        comp = pd.DataFrame(company_rows).sort_values(
            ["signal", "horizon", "forward_cagr_pct"], ascending=[True, True, False]
        )
        comp.to_csv(OUT_COMPANIES, index=False)
        print(f"Per-pattern company list: {OUT_COMPANIES} ({len(comp):,} rows)")

        # Build per-company scorecard: count of >=70% patterns matched + avg realized CAGR
        score = comp.groupby("nse_symbol").agg(
            n_pattern_matches=("signal", "count"),
            n_20pct_target_hits=("met_20pct_target", lambda s: (s == "Y").sum()),
            avg_realized_cagr=("forward_cagr_pct", "mean"),
            best_realized_cagr=("forward_cagr_pct", "max"),
            base_years_with_match=("base_year", "nunique"),
            industry=("industry", "first"),
        ).reset_index()
        score["target_hit_rate_pct"] = round(
            (score["n_20pct_target_hits"] / score["n_pattern_matches"]) * 100, 1
        )
        score = score.sort_values("n_pattern_matches", ascending=False)
        score.to_csv(OUT_SCORECARD, index=False)
        print(f"Company scorecard: {OUT_SCORECARD} ({len(score)} rows)")

    print()
    print("=" * 80)
    print(f"TOP PATTERNS (hit rate >= {REPORT_HIT_RATE}%, n >= {MIN_N})")
    print(f"Outcome: forward stock-price CAGR >= {CAGR_THRESHOLD}%")
    print("=" * 80)
    print(top.head(40).to_string(index=False))

    # Also report the absolute top patterns (any hit rate >= 80% if exist)
    perfect = results_df[results_df["hit_rate_pct"] >= 80].copy()
    print()
    print("=" * 80)
    print(f"PATTERNS HITTING 80% threshold: {len(perfect)}")
    print("=" * 80)
    if len(perfect):
        print(perfect.to_string(index=False))


if __name__ == "__main__":
    main()
