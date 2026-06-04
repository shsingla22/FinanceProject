"""
Comprehensive BS-only screen at multiple CAGR thresholds with per-company
breakdowns. Designed to answer:
  "Which balance-sheet patterns predict 20%+ stock CAGR with at least 80%
   probability?"

Honest answer (developed by this script): at the strict 20% CAGR target,
no single pattern reaches 80% hit rate — the unconditional base rate of
20%+ CAGR is only 34-44%, and the best signals get ~65-70%. To get to
80% hit rate, the CAGR target must be relaxed to ~10-12%.

This script tests both views:
  - Strict view: forward CAGR >= 20% (high bar, best hit rate ~70%)
  - Relaxed view: forward CAGR >= 15%, >= 10% (more patterns clear 80%)

Plus a comprehensive per-company scorecard counting how many qualifying
patterns each of the 500 companies matched, with realized CAGR data.

Outputs (this folder):
  v4_results_cagr20.csv       — every signal × horizon at 20% CAGR target
  v4_results_cagr15.csv       — same at 15% CAGR target
  v4_results_cagr10.csv       — same at 10% CAGR target
  v4_top_patterns.csv         — only patterns >= 80% (at any threshold)
  v4_company_pattern_hits.csv — every (signal, horizon, company, base_year)
                                 row at >= 80% hit rate patterns
  v4_company_scorecard.csv    — per company: # patterns matched, avg
                                 realized CAGR, best realized CAGR
  v4_base_rates.csv           — unconditional base rates per horizon
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
DATA_BS = HERE.parent / "BalanceSheet" / "Nifty500" / "_all_balance_sheets_long.csv"
DATA_SI = HERE.parent / "StockInfo" / "Nifty500" / "_all_stock_info_long.csv"
DATA_CON = HERE.parent / "Nifty500" / "nifty500_constituents.csv"


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


def make_signals() -> list[tuple[str, str]]:
    return [
        # Single-factor static
        ("Debt/Equity < 0.05 (debt-free)", "debt_to_equity < 0.05"),
        ("Debt/Equity < 0.10", "debt_to_equity < 0.10"),
        ("Debt/Equity < 0.30", "debt_to_equity < 0.30"),
        ("Debt/Equity < 0.50", "debt_to_equity < 0.50"),
        ("Reserves > 10x Equity Capital", "reserves_to_equity_cap > 10"),
        ("Reserves > 25x Equity Capital", "reserves_to_equity_cap > 25"),
        ("Reserves > 50x Equity Capital", "reserves_to_equity_cap > 50"),
        ("Reserves > 100x Equity Capital", "reserves_to_equity_cap > 100"),
        ("Cash+Investments > 20% of TA", "cash_plus_investments_to_assets > 0.20"),
        ("Cash+Investments > 30% of TA", "cash_plus_investments_to_assets > 0.30"),
        ("Cash+Investments > 40% of TA", "cash_plus_investments_to_assets > 0.40"),
        ("Cash > 15% of TA", "cash_to_assets > 0.15"),
        ("Cash > 20% of TA", "cash_to_assets > 0.20"),
        ("Borrowings < 10% of TA", "borrowings_to_assets < 0.10"),
        ("Borrowings < 5% of TA", "borrowings_to_assets < 0.05"),

        # Growth signals (single-factor)
        ("Reserves CAGR (3y) > 15%", "reserves_cagr3y > 15"),
        ("Reserves CAGR (3y) > 20%", "reserves_cagr3y > 20"),
        ("Reserves CAGR (3y) > 25%", "reserves_cagr3y > 25"),
        ("Reserves CAGR (3y) > 30%", "reserves_cagr3y > 30"),
        ("Reserves CAGR (5y) > 15%", "reserves_cagr5y > 15"),
        ("Reserves CAGR (5y) > 20%", "reserves_cagr5y > 20"),
        ("Reserves CAGR (5y) > 25%", "reserves_cagr5y > 25"),
        ("Fixed Assets CAGR (3y) > 15%", "fixed_assets_cagr3y > 15"),
        ("Fixed Assets CAGR (3y) > 20%", "fixed_assets_cagr3y > 20"),
        ("Fixed Assets CAGR (3y) > 25%", "fixed_assets_cagr3y > 25"),
        ("Total Assets CAGR (3y) > 15%", "total_assets_cagr3y > 15"),
        ("Total Assets CAGR (3y) > 20%", "total_assets_cagr3y > 20"),

        # Two-factor: capital efficiency
        ("Reserves CAGR > 15% AND Debt/Equity < 0.5",
            "reserves_cagr3y > 15 and debt_to_equity < 0.5"),
        ("Reserves CAGR > 15% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 15 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 20% AND Debt/Equity < 0.5",
            "reserves_cagr3y > 20 and debt_to_equity < 0.5"),
        ("Reserves CAGR > 20% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 20 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 25% AND Debt/Equity < 0.5",
            "reserves_cagr3y > 25 and debt_to_equity < 0.5"),
        ("Reserves CAGR > 25% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 25 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 25% AND Debt/Equity < 0.1",
            "reserves_cagr3y > 25 and debt_to_equity < 0.1"),
        ("Reserves CAGR > 30% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 30 and debt_to_equity < 0.3"),
        ("FA CAGR > 15% AND Debt/Equity < 0.5",
            "fixed_assets_cagr3y > 15 and debt_to_equity < 0.5"),
        ("FA CAGR > 15% AND Debt/Equity < 0.3",
            "fixed_assets_cagr3y > 15 and debt_to_equity < 0.3"),
        ("FA CAGR > 20% AND Debt/Equity < 0.3",
            "fixed_assets_cagr3y > 20 and debt_to_equity < 0.3"),
        ("FA CAGR > 25% AND Debt/Equity < 0.3",
            "fixed_assets_cagr3y > 25 and debt_to_equity < 0.3"),
        ("FA CAGR > 15% AND Reserves CAGR > 20%",
            "fixed_assets_cagr3y > 15 and reserves_cagr3y > 20"),
        ("FA CAGR > 20% AND Reserves CAGR > 25%",
            "fixed_assets_cagr3y > 20 and reserves_cagr3y > 25"),
        ("TA CAGR > 15% AND Debt/Equity < 0.5",
            "total_assets_cagr3y > 15 and debt_to_equity < 0.5"),
        ("TA CAGR > 20% AND Debt/Equity < 0.5",
            "total_assets_cagr3y > 20 and debt_to_equity < 0.5"),

        # Cash + debt screens
        ("Cash > 15% of TA AND Debt/Equity < 0.3",
            "cash_to_assets > 0.15 and debt_to_equity < 0.3"),
        ("Cash > 20% of TA AND Debt/Equity < 0.3",
            "cash_to_assets > 0.20 and debt_to_equity < 0.3"),
        ("Cash > 20% of TA AND Debt/Equity < 0.1",
            "cash_to_assets > 0.20 and debt_to_equity < 0.10"),

        # Persistence (sustained growth)
        ("Reserves > 15% YoY for 3 yrs",
            "reserves_current_yoy > 15 and reserves_lag1_yoy > 15 and reserves_lag2_yoy > 15"),
        ("Reserves > 20% YoY for 3 yrs",
            "reserves_current_yoy > 20 and reserves_lag1_yoy > 20 and reserves_lag2_yoy > 20"),
        ("Reserves > 25% YoY for 3 yrs",
            "reserves_current_yoy > 25 and reserves_lag1_yoy > 25 and reserves_lag2_yoy > 25"),
        ("FA > 15% YoY for 3 yrs (sustained capex)",
            "fixed_assets_current_yoy > 15 and fixed_assets_lag1_yoy > 15 and fixed_assets_lag2_yoy > 15"),
        ("FA > 20% YoY for 3 yrs",
            "fixed_assets_current_yoy > 20 and fixed_assets_lag1_yoy > 20 and fixed_assets_lag2_yoy > 20"),
        ("TA > 15% YoY for 3 yrs",
            "total_assets_current_yoy > 15 and total_assets_lag1_yoy > 15 and total_assets_lag2_yoy > 15"),

        # Combined persistence + leverage
        ("Reserves > 15% YoY for 3 yrs AND Debt/Equity < 0.5",
            "reserves_current_yoy > 15 and reserves_lag1_yoy > 15 and reserves_lag2_yoy > 15 and debt_to_equity < 0.5"),
        ("Reserves > 20% YoY for 3 yrs AND Debt/Equity < 0.5",
            "reserves_current_yoy > 20 and reserves_lag1_yoy > 20 and reserves_lag2_yoy > 20 and debt_to_equity < 0.5"),
        ("Reserves > 20% YoY for 3 yrs AND Debt/Equity < 0.3",
            "reserves_current_yoy > 20 and reserves_lag1_yoy > 20 and reserves_lag2_yoy > 20 and debt_to_equity < 0.3"),
        ("Reserves > 25% YoY for 3 yrs AND Debt/Equity < 0.5",
            "reserves_current_yoy > 25 and reserves_lag1_yoy > 25 and reserves_lag2_yoy > 25 and debt_to_equity < 0.5"),

        # Three-factor combined screens
        ("Reserves CAGR > 20% AND FA CAGR > 10% AND Debt/Equity < 0.5",
            "reserves_cagr3y > 20 and fixed_assets_cagr3y > 10 and debt_to_equity < 0.5"),
        ("Reserves CAGR > 20% AND FA CAGR > 10% AND Debt/Equity < 0.3",
            "reserves_cagr3y > 20 and fixed_assets_cagr3y > 10 and debt_to_equity < 0.3"),
        ("Reserves CAGR > 25% AND FA CAGR > 15% AND Debt/Equity < 0.5",
            "reserves_cagr3y > 25 and fixed_assets_cagr3y > 15 and debt_to_equity < 0.5"),
        ("Reserves CAGR > 25% AND FA CAGR > 10% AND Cash > 10% of TA",
            "reserves_cagr3y > 25 and fixed_assets_cagr3y > 10 and cash_to_assets > 0.10"),

        # Deleveraging compounders
        ("Reserves CAGR > 20% AND Borrowings CAGR < 0%",
            "reserves_cagr3y > 20 and borrowings_cagr3y < 0"),
        ("Reserves CAGR > 25% AND Borrowings CAGR < 0%",
            "reserves_cagr3y > 25 and borrowings_cagr3y < 0"),

        # 5-year sustained quality
        ("Reserves CAGR (5y) > 20% AND Debt/Equity < 0.5",
            "reserves_cagr5y > 20 and debt_to_equity < 0.5"),
        ("Reserves CAGR (5y) > 20% AND Debt/Equity < 0.3",
            "reserves_cagr5y > 20 and debt_to_equity < 0.3"),
        ("Reserves CAGR (5y) > 25% AND Debt/Equity < 0.5",
            "reserves_cagr5y > 25 and debt_to_equity < 0.5"),
    ]


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

    BS_LAGGABLE = [
        "Fixed Assets", "Investments", "Total Assets",
        "Equity Capital", "Reserves", "Borrowings",
        "Inventories", "Trade receivables", "Cash Equivalents", "Trade Payables",
    ]
    BS_LAGGABLE = [c for c in BS_LAGGABLE if c in panel.columns]

    add_cols: dict[str, pd.Series] = {}
    for col in BS_LAGGABLE:
        for ny in (1, 2, 3, 5):
            add_cols[f"{col}__lag{ny}"] = g[col].shift(ny)
    add_cols["price_fwd3"] = g["Stock Price (Rs)"].shift(-3)
    add_cols["price_fwd5"] = g["Stock Price (Rs)"].shift(-5)
    add_cols["price_fwd7"] = g["Stock Price (Rs)"].shift(-7)
    panel = pd.concat([panel, pd.DataFrame(add_cols)], axis=1)

    print("Computing derived features ...")
    panel["cagr3y_pct"] = safe_cagr(panel["price_fwd3"], panel["Stock Price (Rs)"], 3)
    panel["cagr5y_pct"] = safe_cagr(panel["price_fwd5"], panel["Stock Price (Rs)"], 5)
    panel["cagr7y_pct"] = safe_cagr(panel["price_fwd7"], panel["Stock Price (Rs)"], 7)

    derived: dict[str, pd.Series] = {}
    for col in BS_LAGGABLE:
        for ny in (1, 3, 5):
            name = col.lower().replace(" ", "_") + f"_cagr{ny}y"
            derived[name] = safe_cagr(panel[col], panel[f"{col}__lag{ny}"], ny)
        for shift_n, name in ((0, "current_yoy"), (1, "lag1_yoy"), (2, "lag2_yoy")):
            cur = g[col].shift(shift_n)
            prev = g[col].shift(shift_n + 1)
            derived[f"{col.lower().replace(' ', '_')}_{name}"] = safe_cagr(cur, prev, 1)

    equity_total = panel["Equity Capital"] + panel["Reserves"]
    derived["debt_to_equity"] = safe_div(panel["Borrowings"], equity_total)
    derived["reserves_to_equity_cap"] = safe_div(panel["Reserves"], panel["Equity Capital"])
    derived["cash_to_assets"] = safe_div(panel["Cash Equivalents"], panel["Total Assets"])
    derived["fa_to_assets"] = safe_div(panel["Fixed Assets"], panel["Total Assets"])
    derived["borrowings_to_assets"] = safe_div(panel["Borrowings"], panel["Total Assets"])
    derived["cash_plus_investments_to_assets"] = safe_div(
        panel["Cash Equivalents"] + panel["Investments"], panel["Total Assets"]
    )

    panel = pd.concat([panel, pd.DataFrame(derived)], axis=1)

    # Save base rates
    base_rates = []
    for h in ("cagr3y_pct", "cagr5y_pct", "cagr7y_pct"):
        sub = panel[panel[h].notna()]
        for threshold in (10, 15, 20, 25, 30):
            base_rates.append({
                "horizon": h,
                "cagr_threshold_pct": threshold,
                "n_total": len(sub),
                "hits": int((sub[h] >= threshold).sum()),
                "base_rate_pct": round((sub[h] >= threshold).mean() * 100, 1),
            })
    pd.DataFrame(base_rates).to_csv(HERE / "v4_base_rates.csv", index=False)
    print(f"Saved base rates: {HERE / 'v4_base_rates.csv'}")

    SIGNALS = make_signals()
    print(f"Testing {len(SIGNALS)} signals × 3 horizons × 3 CAGR thresholds ...")

    all_results = {}  # threshold -> rows
    for threshold in (10, 15, 20):
        all_results[threshold] = []

    company_rows = []  # only for hit_rate >= 80% at any threshold

    for name, expr in SIGNALS:
        try:
            mask = eval_signal(expr, panel).fillna(False)
        except Exception as e:
            print(f"  ERROR for '{name}': {e}")
            continue

        for horizon, col in (("3y", "cagr3y_pct"), ("5y", "cagr5y_pct"), ("7y", "cagr7y_pct")):
            sub = panel[mask & panel[col].notna()].copy()
            n = len(sub)
            if n < 15:
                continue

            for threshold in (10, 15, 20):
                hits = (sub[col] >= threshold).sum()
                rate = hits / n
                all_results[threshold].append({
                    "signal": name,
                    "horizon": horizon,
                    "n": n,
                    "hits": int(hits),
                    "hit_rate_pct": round(rate * 100, 1),
                    "avg_cagr_pct": round(sub[col].mean(), 1),
                    "median_cagr_pct": round(sub[col].median(), 1),
                    "min_cagr_pct": round(sub[col].min(), 1),
                    "max_cagr_pct": round(sub[col].max(), 1),
                })

                # Capture company-level matches for 80%+ patterns
                if rate >= 0.80:
                    for _, row in sub.iterrows():
                        company_rows.append({
                            "cagr_threshold_pct": threshold,
                            "signal": name,
                            "horizon": horizon,
                            "nse_symbol": row["nse_symbol"],
                            "industry": row["industry"],
                            "base_year": int(row["base_year"]),
                            "stock_price_at_base": round(row["Stock Price (Rs)"], 2) if pd.notna(row["Stock Price (Rs)"]) else None,
                            "forward_cagr_pct": round(row[col], 1),
                            "met_target": "Y" if row[col] >= threshold else "N",
                        })

    # Save per-threshold results
    for threshold, rows in all_results.items():
        df = pd.DataFrame(rows).sort_values(["hit_rate_pct", "n"], ascending=[False, False])
        df.to_csv(HERE / f"v4_results_cagr{threshold}.csv", index=False)
        print(f"  cagr>={threshold}%: {len(df)} signal/horizon rows -> v4_results_cagr{threshold}.csv")

    # Top patterns (any threshold reaching 80%)
    top_rows = []
    for threshold, rows in all_results.items():
        for r in rows:
            if r["hit_rate_pct"] >= 80:
                top_rows.append({**r, "cagr_threshold_pct": threshold})
    top_df = pd.DataFrame(top_rows).sort_values(
        ["cagr_threshold_pct", "hit_rate_pct", "n"], ascending=[False, False, False]
    )
    top_df.to_csv(HERE / "v4_top_patterns.csv", index=False)
    print(f"Top patterns (>= 80% hit rate at any threshold): {len(top_df)}")

    # Per-company breakdowns
    if company_rows:
        comp = pd.DataFrame(company_rows).sort_values(
            ["cagr_threshold_pct", "signal", "horizon", "forward_cagr_pct"],
            ascending=[False, True, True, False]
        )
        comp.to_csv(HERE / "v4_company_pattern_hits.csv", index=False)
        print(f"Company pattern hits: {len(comp):,} rows")

        # Per-company scorecard
        score = comp.groupby("nse_symbol").agg(
            industry=("industry", "first"),
            n_pattern_matches=("signal", "count"),
            n_target_hits=("met_target", lambda s: (s == "Y").sum()),
            avg_realized_cagr=("forward_cagr_pct", "mean"),
            best_realized_cagr=("forward_cagr_pct", "max"),
            worst_realized_cagr=("forward_cagr_pct", "min"),
            base_years_covered=("base_year", "nunique"),
            unique_signals_matched=("signal", "nunique"),
        ).reset_index()
        score["target_hit_rate_pct"] = round(
            (score["n_target_hits"] / score["n_pattern_matches"]) * 100, 1
        )
        score = score.sort_values("n_pattern_matches", ascending=False)
        score.to_csv(HERE / "v4_company_scorecard.csv", index=False)
        print(f"Company scorecard: {len(score)} companies")

    print("\n" + "=" * 80)
    print("PATTERNS BY CAGR THRESHOLD")
    print("=" * 80)
    for threshold in (20, 15, 10):
        rows = all_results[threshold]
        df = pd.DataFrame(rows)
        n_80 = (df["hit_rate_pct"] >= 80).sum()
        n_70 = (df["hit_rate_pct"] >= 70).sum()
        print(f"\nCAGR >= {threshold}% target:")
        print(f"  Patterns at hit rate >= 80%: {n_80}")
        print(f"  Patterns at hit rate >= 70%: {n_70}")
        print(f"  Highest hit rate achieved: {df['hit_rate_pct'].max()}%")
        if n_80 > 0:
            print("  Top 5 patterns at this threshold:")
            print(df[df["hit_rate_pct"] >= 80].head(15).to_string(index=False))


if __name__ == "__main__":
    main()
