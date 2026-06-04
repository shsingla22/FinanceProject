"""
Re-run the v4 analysis to capture (company, year) matches for ALL
patterns at hit_rate >= 65% (not just >= 80%), then emit a
comprehensive readable MD file listing every company that triggered
each pattern, with its realized forward CAGR.

This is the user's requested 'list the companies and the years that
satisfied the criteria' output.

Output:
  pattern_companies_full.csv  — every (pattern, company, year) match
                                for patterns at hit_rate >= 65%
  COMPANIES_BY_PATTERN.md     — human-readable listing organized by
                                pattern, then by realized CAGR
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
DATA_BS = HERE.parent / "BalanceSheet" / "Nifty500" / "_all_balance_sheets_long.csv"
DATA_SI = HERE.parent / "StockInfo" / "Nifty500" / "_all_stock_info_long.csv"
DATA_CON = HERE.parent / "Nifty500" / "nifty500_constituents.csv"

OUT_CSV = HERE / "pattern_companies_full.csv"
OUT_MD = HERE / "COMPANIES_BY_PATTERN.md"

# Match the v4 script's settings
MIN_HIT_RATE = 65.0  # Capture patterns at >= 65% to get a broader list


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


# Curated list of the top patterns we want to detail.
# Each entry is (signal_name, expression, horizon_col, horizon_label, cagr_threshold)
PATTERNS_TO_DETAIL = [
    # =========== >= 80% hit rate at 10% CAGR target (the 5 from v4) ===========
    ("FA > 20% YoY for 3 yrs",
     "fixed_assets_current_yoy > 20 and fixed_assets_lag1_yoy > 20 and fixed_assets_lag2_yoy > 20",
     "cagr7y_pct", "7y", 10),
    ("Reserves CAGR > 25% AND FA CAGR > 15% AND Debt/Equity < 0.5",
     "reserves_cagr3y > 25 and fixed_assets_cagr3y > 15 and debt_to_equity < 0.5",
     "cagr7y_pct", "7y", 10),
    ("Reserves > 20% YoY for 3 yrs AND Debt/Equity < 0.5",
     "reserves_current_yoy > 20 and reserves_lag1_yoy > 20 and reserves_lag2_yoy > 20 and debt_to_equity < 0.5",
     "cagr7y_pct", "7y", 10),
    ("Reserves CAGR > 25% AND Borrowings CAGR < 0%",
     "reserves_cagr3y > 25 and borrowings_cagr3y < 0",
     "cagr7y_pct", "7y", 10),
    ("Reserves CAGR > 20% AND FA CAGR > 10% AND Debt/Equity < 0.3",
     "reserves_cagr3y > 20 and fixed_assets_cagr3y > 10 and debt_to_equity < 0.3",
     "cagr7y_pct", "7y", 10),

    # =========== High hit rates at 15% CAGR target ===========
    ("FA > 20% YoY for 3 yrs (15% target)",
     "fixed_assets_current_yoy > 20 and fixed_assets_lag1_yoy > 20 and fixed_assets_lag2_yoy > 20",
     "cagr5y_pct", "5y", 15),
    ("Reserves CAGR > 25% AND FA CAGR > 15% AND Debt/Equity < 0.5 (15% target)",
     "reserves_cagr3y > 25 and fixed_assets_cagr3y > 15 and debt_to_equity < 0.5",
     "cagr7y_pct", "7y", 15),

    # =========== Highest hit rates at the strict 20% CAGR target ===========
    ("FA > 20% YoY for 3 yrs (20% target, 5y) - BEST AT STRICT TARGET",
     "fixed_assets_current_yoy > 20 and fixed_assets_lag1_yoy > 20 and fixed_assets_lag2_yoy > 20",
     "cagr5y_pct", "5y", 20),
    ("Reserves CAGR > 25% AND Borrowings CAGR < 0% (20% target, 5y)",
     "reserves_cagr3y > 25 and borrowings_cagr3y < 0",
     "cagr5y_pct", "5y", 20),
    ("Reserves CAGR > 20% AND Borrowings CAGR < 0% (20% target, 5y)",
     "reserves_cagr3y > 20 and borrowings_cagr3y < 0",
     "cagr5y_pct", "5y", 20),
]


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

    BS_LAGGABLE = [
        "Fixed Assets", "Investments", "Total Assets",
        "Equity Capital", "Reserves", "Borrowings",
        "Inventories", "Trade receivables", "Cash Equivalents", "Trade Payables",
    ]
    BS_LAGGABLE = [c for c in BS_LAGGABLE if c in panel.columns]

    add_cols = {}
    for col in BS_LAGGABLE:
        for ny in (1, 2, 3, 5):
            add_cols[f"{col}__lag{ny}"] = g[col].shift(ny)
    add_cols["price_fwd3"] = g["Stock Price (Rs)"].shift(-3)
    add_cols["price_fwd5"] = g["Stock Price (Rs)"].shift(-5)
    add_cols["price_fwd7"] = g["Stock Price (Rs)"].shift(-7)
    panel = pd.concat([panel, pd.DataFrame(add_cols)], axis=1)

    panel["cagr3y_pct"] = safe_cagr(panel["price_fwd3"], panel["Stock Price (Rs)"], 3)
    panel["cagr5y_pct"] = safe_cagr(panel["price_fwd5"], panel["Stock Price (Rs)"], 5)
    panel["cagr7y_pct"] = safe_cagr(panel["price_fwd7"], panel["Stock Price (Rs)"], 7)

    derived = {}
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

    panel = pd.concat([panel, pd.DataFrame(derived)], axis=1)

    # Build per-pattern company lists
    all_rows = []
    pattern_metadata = []
    for sig_name, expr, horizon_col, horizon_label, cagr_thr in PATTERNS_TO_DETAIL:
        try:
            mask = eval_signal(expr, panel).fillna(False)
        except Exception as e:
            print(f"  ERROR for '{sig_name}': {e}")
            continue
        sub = panel[mask & panel[horizon_col].notna()].copy()
        n = len(sub)
        if n < 5:
            continue
        hits = (sub[horizon_col] >= cagr_thr).sum()
        rate = hits / n
        pattern_metadata.append({
            "pattern": sig_name,
            "horizon": horizon_label,
            "cagr_threshold_pct": cagr_thr,
            "n": n,
            "hits": int(hits),
            "hit_rate_pct": round(rate * 100, 1),
            "avg_realized_cagr_pct": round(sub[horizon_col].mean(), 1),
        })
        for _, row in sub.iterrows():
            all_rows.append({
                "pattern": sig_name,
                "horizon": horizon_label,
                "cagr_threshold_pct": cagr_thr,
                "nse_symbol": row["nse_symbol"],
                "industry": row["industry"] if pd.notna(row["industry"]) else "",
                "base_year_T": int(row["base_year"]),
                "fy_label": f"Mar {int(row['base_year'])}",
                "stock_price_at_T": round(row["Stock Price (Rs)"], 2)
                if pd.notna(row["Stock Price (Rs)"]) else None,
                "forward_cagr_pct": round(row[horizon_col], 1),
                "met_target": "Y" if row[horizon_col] >= cagr_thr else "N",
            })

    companies_df = pd.DataFrame(all_rows).sort_values(
        ["pattern", "forward_cagr_pct"], ascending=[True, False]
    )
    companies_df.to_csv(OUT_CSV, index=False)
    print(f"Saved {len(companies_df):,} (pattern, company, year) rows -> {OUT_CSV}")

    # ---- Build readable MD file ----
    metadata_df = pd.DataFrame(pattern_metadata)
    print("\nPattern metadata:")
    print(metadata_df.to_string(index=False))

    lines = []
    lines.append("# Companies and Years Satisfying Each Balance-Sheet Pattern")
    lines.append("")
    lines.append("**Universe:** Nifty 500 (all 500 constituents)")
    lines.append("**Period:** FY 2015 → FY 2026")
    lines.append("**Methodology:** for each pattern, lists every (company, base year T)")
    lines.append("observation that matched the BS criteria evaluated using data through")
    lines.append("year T, along with the *realized* forward stock-price CAGR over the")
    lines.append("subsequent N years (where N = pattern's horizon).")
    lines.append("")
    lines.append("**'Met target'**: Y = the company's actual forward CAGR met or exceeded")
    lines.append("the CAGR threshold of the pattern (success); N = it fell short (failure).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Group by pattern
    for sig_name, expr, horizon_col, horizon_label, cagr_thr in PATTERNS_TO_DETAIL:
        meta = next(
            (m for m in pattern_metadata
             if m["pattern"] == sig_name and m["horizon"] == horizon_label
             and m["cagr_threshold_pct"] == cagr_thr),
            None
        )
        if meta is None:
            continue
        lines.append(f"## Pattern: {sig_name}")
        lines.append("")
        lines.append(f"- **Forward horizon**: {horizon_label}")
        lines.append(f"- **CAGR target**: ≥ {cagr_thr}%")
        lines.append(f"- **Sample size (n)**: {meta['n']}")
        lines.append(f"- **Hit rate**: {meta['hit_rate_pct']}% ({meta['hits']} of {meta['n']} met target)")
        lines.append(f"- **Average realized CAGR across all matches**: {meta['avg_realized_cagr_pct']}%")
        lines.append("")
        lines.append("### Companies that matched this pattern")
        lines.append("")
        lines.append("| Rank | NSE Symbol | Industry | Base Year (T) | Forward CAGR | Met Target? |")
        lines.append("|-----:|-----------|----------|---------------|-------------:|:------------|")

        sub = companies_df[
            (companies_df["pattern"] == sig_name)
            & (companies_df["horizon"] == horizon_label)
            & (companies_df["cagr_threshold_pct"] == cagr_thr)
        ].copy().sort_values("forward_cagr_pct", ascending=False).reset_index(drop=True)

        for i, row in sub.iterrows():
            ind = row["industry"] if row["industry"] else "(uncl.)"
            mark = "✅" if row["met_target"] == "Y" else "❌"
            lines.append(
                f"| {i+1} | {row['nse_symbol']} | {ind} | {row['fy_label']} | "
                f"{row['forward_cagr_pct']:+.1f}% | {mark} {row['met_target']} |"
            )

        lines.append("")
        lines.append("---")
        lines.append("")

    OUT_MD.write_text("\n".join(lines))
    print(f"\nWrote {OUT_MD} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
