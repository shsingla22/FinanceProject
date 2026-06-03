"""
3-YEAR HORIZON ONLY analysis with very tight balance-sheet screens to
find patterns that achieve >= 80% probability for forward stock CAGR
at the highest possible threshold.

Approach: stack more conditions (4+), tighten thresholds, and test
multi-year persistence (e.g., 4 consecutive years of growth) to push
the conditional probability up. Sample sizes will be small but
selectivity is the point.

Reports the 80% threshold at three CAGR levels:
  - CAGR >= 10% (base rate 60% at 3y)
  - CAGR >= 15% (base rate 52% at 3y)
  - CAGR >= 20% (base rate 44% at 3y)

Per the user's framing: 3 years of BS history (years T-3 through T)
predicts forward stock-price CAGR over years T -> T+3.

Outputs (this folder):
  v5_3y_results.csv               — every signal × CAGR threshold
  v5_3y_80pct_patterns.csv        — only patterns at >= 80% hit rate
  v5_3y_company_matches.csv       — every (pattern, company, year) row
                                     for >= 80% patterns
  COMPANIES_BY_PATTERN_3Y.md      — human-readable per-pattern listing
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
DATA_BS = HERE.parent / "BalanceSheet" / "_all_balance_sheets_long.csv"
DATA_SI = HERE.parent / "StockInfo" / "_all_stock_info_long.csv"
DATA_CON = HERE.parent / "Nifty500" / "nifty500_constituents.csv"


def load_wide_bs(long_csv):
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


def load_wide_si(long_csv):
    df = pd.read_csv(long_csv)
    return df.pivot_table(
        index=["nse_symbol", "year"], columns="metric",
        values="value", aggfunc="first"
    )


def year_to_int(y):
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


def eval_signal(expr, df):
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


def main():
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

    # Lagged + forward
    BS_LAGGABLE = [
        "Fixed Assets", "Total Assets", "Equity Capital", "Reserves",
        "Borrowings", "Cash Equivalents", "Inventories", "Trade receivables",
        "Trade Payables", "Investments",
    ]
    BS_LAGGABLE = [c for c in BS_LAGGABLE if c in panel.columns]

    add = {}
    for col in BS_LAGGABLE:
        for n in (1, 2, 3, 4, 5):
            add[f"{col}__lag{n}"] = g[col].shift(n)
    add["price_fwd3"] = g["Stock Price (Rs)"].shift(-3)
    panel = pd.concat([panel, pd.DataFrame(add)], axis=1)

    panel["cagr3y_pct"] = safe_cagr(panel["price_fwd3"], panel["Stock Price (Rs)"], 3)

    derived = {}
    for col in BS_LAGGABLE:
        for n in (1, 3, 5):
            name = col.lower().replace(" ", "_") + f"_cagr{n}y"
            derived[name] = safe_cagr(panel[col], panel[f"{col}__lag{n}"], n)
        # YoY for each of the last 4 years (shift 0,1,2,3)
        for shift_n, lbl in ((0, "yoy0"), (1, "yoy1"), (2, "yoy2"), (3, "yoy3")):
            cur = g[col].shift(shift_n)
            prev = g[col].shift(shift_n + 1)
            derived[f"{col.lower().replace(' ', '_')}_{lbl}"] = safe_cagr(cur, prev, 1)

    equity_total = panel["Equity Capital"] + panel["Reserves"]
    derived["debt_to_equity"] = safe_div(panel["Borrowings"], equity_total)
    derived["cash_to_assets"] = safe_div(panel["Cash Equivalents"], panel["Total Assets"])
    derived["borrowings_to_assets"] = safe_div(panel["Borrowings"], panel["Total Assets"])
    derived["fa_to_assets"] = safe_div(panel["Fixed Assets"], panel["Total Assets"])
    derived["cash_plus_inv_to_assets"] = safe_div(
        panel["Cash Equivalents"] + panel["Investments"], panel["Total Assets"]
    )

    panel = pd.concat([panel, pd.DataFrame(derived)], axis=1)

    # ============= SIGNAL DEFINITIONS (tightening the screws) =============
    SIGNALS = [
        # === Single ultra-tight thresholds ===
        ("FA CAGR (3y) > 35%", "fixed_assets_cagr3y > 35"),
        ("FA CAGR (3y) > 40%", "fixed_assets_cagr3y > 40"),
        ("Reserves CAGR (3y) > 40%", "reserves_cagr3y > 40"),
        ("Reserves CAGR (3y) > 50%", "reserves_cagr3y > 50"),
        ("Reserves CAGR (5y) > 35%", "reserves_cagr5y > 35"),

        # === FA growth persistence (3-year and 4-year) ===
        ("FA > 25% YoY for 3 yrs",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25"),
        ("FA > 30% YoY for 3 yrs",
            "fixed_assets_yoy0 > 30 and fixed_assets_yoy1 > 30 and fixed_assets_yoy2 > 30"),
        ("FA > 20% YoY for 4 yrs (4-year sustained capex)",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and fixed_assets_yoy3 > 20"),
        ("FA > 25% YoY for 4 yrs",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and fixed_assets_yoy3 > 25"),
        ("FA > 15% YoY for 4 yrs",
            "fixed_assets_yoy0 > 15 and fixed_assets_yoy1 > 15 and fixed_assets_yoy2 > 15 and fixed_assets_yoy3 > 15"),

        # === Reserves growth persistence ===
        ("Reserves > 25% YoY for 3 yrs",
            "reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25"),
        ("Reserves > 30% YoY for 3 yrs",
            "reserves_yoy0 > 30 and reserves_yoy1 > 30 and reserves_yoy2 > 30"),
        ("Reserves > 20% YoY for 4 yrs",
            "reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20 and reserves_yoy3 > 20"),
        ("Reserves > 25% YoY for 4 yrs",
            "reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25 and reserves_yoy3 > 25"),

        # === FA + Reserves both persistent ===
        ("FA & Reserves both > 20% YoY for 3 yrs",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20"),
        ("FA & Reserves both > 25% YoY for 3 yrs",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25"),

        # === Tight 3-condition stacking ===
        ("FA CAGR > 25% AND Reserves CAGR > 30% AND D/E < 0.3",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 30 and debt_to_equity < 0.3"),
        ("FA CAGR > 30% AND Reserves CAGR > 30% AND D/E < 0.5",
            "fixed_assets_cagr3y > 30 and reserves_cagr3y > 30 and debt_to_equity < 0.5"),
        ("FA CAGR > 25% AND Reserves CAGR > 25% AND D/E < 0.1",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25 and debt_to_equity < 0.1"),
        ("FA CAGR > 20% AND Reserves CAGR > 25% AND Borrowings CAGR < 0%",
            "fixed_assets_cagr3y > 20 and reserves_cagr3y > 25 and borrowings_cagr3y < 0"),
        ("FA CAGR > 25% AND Reserves CAGR > 25% AND Cash > 15% of TA",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25 and cash_to_assets > 0.15"),

        # === Persistence + leverage ===
        ("FA > 25% YoY for 3 yrs AND D/E < 0.3",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and debt_to_equity < 0.3"),
        ("FA > 25% YoY for 3 yrs AND D/E < 0.5",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and debt_to_equity < 0.5"),
        ("FA > 20% YoY for 4 yrs AND D/E < 0.5",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and fixed_assets_yoy3 > 20 and debt_to_equity < 0.5"),
        ("Reserves > 25% YoY for 3 yrs AND D/E < 0.3",
            "reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25 and debt_to_equity < 0.3"),
        ("Reserves > 25% YoY for 3 yrs AND D/E < 0.5",
            "reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25 and debt_to_equity < 0.5"),
        ("Reserves > 30% YoY for 3 yrs AND D/E < 0.5",
            "reserves_yoy0 > 30 and reserves_yoy1 > 30 and reserves_yoy2 > 30 and debt_to_equity < 0.5"),

        # === 4-factor stacking ===
        ("FA CAGR > 25% AND Reserves CAGR > 25% AND D/E < 0.3 AND Cash > 10% TA",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25 and debt_to_equity < 0.3 and cash_to_assets > 0.10"),
        ("FA > 20% YoY for 3 yrs AND Reserves CAGR > 25% AND D/E < 0.3",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_cagr3y > 25 and debt_to_equity < 0.3"),
        ("FA > 25% YoY for 3 yrs AND Reserves CAGR > 25% AND D/E < 0.5",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and reserves_cagr3y > 25 and debt_to_equity < 0.5"),

        # === Deleveraging compounders, tighter ===
        ("Reserves CAGR > 25% AND Borrowings CAGR < -15%",
            "reserves_cagr3y > 25 and borrowings_cagr3y < -15"),
        ("Reserves CAGR > 30% AND Borrowings CAGR < -15%",
            "reserves_cagr3y > 30 and borrowings_cagr3y < -15"),

        # === Cash-rich growers ===
        ("Cash > 25% of TA AND Reserves CAGR > 20% AND D/E < 0.1",
            "cash_to_assets > 0.25 and reserves_cagr3y > 20 and debt_to_equity < 0.1"),
        ("Cash > 30% of TA AND Reserves CAGR > 20%",
            "cash_to_assets > 0.30 and reserves_cagr3y > 20"),

        # === Existing winners from v4 (3y horizon) for cross-reference ===
        ("FA > 20% YoY for 3 yrs (cross-ref)",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20"),
        ("Reserves CAGR > 25% AND Borrowings CAGR < 0% (cross-ref)",
            "reserves_cagr3y > 25 and borrowings_cagr3y < 0"),
    ]

    print(f"Loaded {len(panel):,} (company, year) panel rows")
    print(f"Testing {len(SIGNALS)} signals × 3 CAGR thresholds at 3y horizon ...")

    results = []
    company_rows = []

    MIN_N = 5  # tight signals have small samples; we report n>=5 for completeness

    for name, expr in SIGNALS:
        try:
            mask = eval_signal(expr, panel).fillna(False)
        except Exception as e:
            print(f"  ERROR for '{name}': {e}")
            continue

        sub = panel[mask & panel["cagr3y_pct"].notna()].copy()
        n = len(sub)
        if n < MIN_N:
            continue

        for threshold in (10, 15, 20):
            hits = (sub["cagr3y_pct"] >= threshold).sum()
            rate = hits / n if n > 0 else 0
            results.append({
                "signal": name,
                "cagr_threshold_pct": threshold,
                "n": n,
                "hits": int(hits),
                "hit_rate_pct": round(rate * 100, 1),
                "avg_cagr_pct": round(sub["cagr3y_pct"].mean(), 1),
                "median_cagr_pct": round(sub["cagr3y_pct"].median(), 1),
                "min_cagr_pct": round(sub["cagr3y_pct"].min(), 1),
                "max_cagr_pct": round(sub["cagr3y_pct"].max(), 1),
            })

            if rate >= 0.80 and n >= 5:
                for _, row in sub.iterrows():
                    company_rows.append({
                        "cagr_threshold_pct": threshold,
                        "signal": name,
                        "nse_symbol": row["nse_symbol"],
                        "industry": row["industry"] if pd.notna(row["industry"]) else "",
                        "base_year_T": int(row["base_year"]),
                        "fy_label": f"Mar {int(row['base_year'])}",
                        "stock_price_at_T": round(row["Stock Price (Rs)"], 2)
                            if pd.notna(row["Stock Price (Rs)"]) else None,
                        "forward_cagr_pct": round(row["cagr3y_pct"], 1),
                        "met_target": "Y" if row["cagr3y_pct"] >= threshold else "N",
                    })

    results_df = pd.DataFrame(results).sort_values(
        ["cagr_threshold_pct", "hit_rate_pct", "n"], ascending=[False, False, False]
    )
    results_df.to_csv(HERE / "v5_3y_results.csv", index=False)
    print(f"\nAll results: v5_3y_results.csv ({len(results_df)} rows)")

    top = results_df[results_df["hit_rate_pct"] >= 80].copy()
    top.to_csv(HERE / "v5_3y_80pct_patterns.csv", index=False)
    print(f">= 80% hit rate patterns: {len(top)}")
    print()
    if len(top):
        print(top.to_string(index=False))
    else:
        print("None at 80%. Top 15 results:")
        print(results_df.head(15).to_string(index=False))

    if company_rows:
        comp = pd.DataFrame(company_rows).sort_values(
            ["cagr_threshold_pct", "signal", "forward_cagr_pct"],
            ascending=[False, True, False]
        )
        comp.to_csv(HERE / "v5_3y_company_matches.csv", index=False)
        print(f"\nCompany matches (>=80% patterns): {len(comp):,} rows")

        # Generate readable MD
        lines = [
            "# 3-Year Forward CAGR — Companies & Years Satisfying >= 80% Hit Rate Patterns",
            "",
            "**Universe:** Nifty 500 (all 500 constituents)",
            "**Horizon:** 3-year forward stock-price CAGR ONLY",
            "**Methodology:** for each pattern that achieves >= 80% probability,",
            "lists every (company, base year T) match with its realized 3-year",
            "forward CAGR.",
            "",
            "**Predictor framing:** signals are computed using ONLY the balance",
            "sheet data through fiscal-year-end T. The forward CAGR is then",
            "measured from T -> T+3 using the year-end stock prices.",
            "",
            "---",
            "",
        ]
        # Group by (signal, cagr_threshold)
        grouped = comp.groupby(["signal", "cagr_threshold_pct"])
        for (sig, thr), sub in grouped:
            n_total = len(sub)
            n_hits = (sub["met_target"] == "Y").sum()
            rate = round(n_hits / n_total * 100, 1)
            lines.append(f"## Pattern: {sig}")
            lines.append("")
            lines.append(f"- **Forward horizon**: 3y")
            lines.append(f"- **CAGR target**: ≥ {thr}%")
            lines.append(f"- **Sample size**: {n_total}")
            lines.append(f"- **Hit rate**: {rate}% ({n_hits} of {n_total} met target)")
            lines.append(f"- **Avg realized CAGR**: {sub['forward_cagr_pct'].mean():.1f}%")
            lines.append("")
            lines.append("### Companies (ranked by realized CAGR)")
            lines.append("")
            lines.append("| # | NSE Symbol | Industry | Base Year (T) | Stock Price at T | 3y Forward CAGR | Met Target? |")
            lines.append("|--:|-----------|----------|--------------|-----------------:|----------------:|:------------|")
            for i, (_, row) in enumerate(
                sub.sort_values("forward_cagr_pct", ascending=False).iterrows(), 1
            ):
                ind = row["industry"] or "(uncl.)"
                mark = "✅" if row["met_target"] == "Y" else "❌"
                price = row["stock_price_at_T"]
                price_str = f"₹{price:,.2f}" if price is not None else "n/a"
                lines.append(
                    f"| {i} | {row['nse_symbol']} | {ind} | {row['fy_label']} | "
                    f"{price_str} | {row['forward_cagr_pct']:+.1f}% | {mark} {row['met_target']} |"
                )
            lines.append("")
            lines.append("---")
            lines.append("")

        (HERE / "COMPANIES_BY_PATTERN_3Y.md").write_text("\n".join(lines))
        print(f"Wrote COMPANIES_BY_PATTERN_3Y.md ({len(lines)} lines)")


if __name__ == "__main__":
    main()
