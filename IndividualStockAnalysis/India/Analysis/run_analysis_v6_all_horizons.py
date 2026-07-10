"""
Comprehensive 3y, 5y, 7y horizon analysis at the strict 20% CAGR target.

Question (from user): "What balance-sheet patterns predict forward
stock CAGR >= 20% with hit rate >= 80%, across 3-year, 5-year, and
7-year horizons?"

Approach: test ~50 tight balance-sheet signals (from v5_3y) on each
of the 3 horizons, at the strict 20% CAGR target. Report:
  - Any pattern at >= 80% hit rate
  - Best patterns at 70-80% (fallback)
  - Best patterns at 60-70% (broader context)

Outputs:
  v6_3y_results.csv, v6_5y_results.csv, v6_7y_results.csv
  v6_top_patterns_20pct.csv  — best patterns per horizon at 20% target
  v6_company_matches.csv     — per-pattern company-year list for
                                the qualifying high-hit-rate patterns
  COMPANIES_BY_PATTERN_ALL_HORIZONS_20pct.md — readable report
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
DATA_BS = HERE.parent / "BalanceSheet" / "Nifty500" / "_all_balance_sheets_long.csv"
DATA_SI = HERE.parent / "StockInfo" / "Nifty500" / "_all_stock_info_long.csv"
DATA_CON = HERE.parent / "Nifty500" / "nifty500_constituents.csv"

CAGR_TARGET = 20.0  # the user's strict target
HIT_RATE_THRESHOLD = 80.0  # for "winning" patterns
FALLBACK_HIT_RATE = 60.0   # also capture these for context
MIN_N = 5  # tight signals -> small samples; n>=5 to be reportable


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
    add["price_fwd5"] = g["Stock Price (Rs)"].shift(-5)
    add["price_fwd7"] = g["Stock Price (Rs)"].shift(-7)
    panel = pd.concat([panel, pd.DataFrame(add)], axis=1)

    panel["cagr3y_pct"] = safe_cagr(panel["price_fwd3"], panel["Stock Price (Rs)"], 3)
    panel["cagr5y_pct"] = safe_cagr(panel["price_fwd5"], panel["Stock Price (Rs)"], 5)
    panel["cagr7y_pct"] = safe_cagr(panel["price_fwd7"], panel["Stock Price (Rs)"], 7)

    derived = {}
    for col in BS_LAGGABLE:
        for n in (1, 3, 5):
            name = col.lower().replace(" ", "_") + f"_cagr{n}y"
            derived[name] = safe_cagr(panel[col], panel[f"{col}__lag{n}"], n)
        for shift_n, lbl in ((0, "yoy0"), (1, "yoy1"), (2, "yoy2"), (3, "yoy3")):
            cur = g[col].shift(shift_n)
            prev = g[col].shift(shift_n + 1)
            derived[f"{col.lower().replace(' ', '_')}_{lbl}"] = safe_cagr(cur, prev, 1)

    equity_total = panel["Equity Capital"] + panel["Reserves"]
    derived["debt_to_equity"] = safe_div(panel["Borrowings"], equity_total)
    derived["cash_to_assets"] = safe_div(panel["Cash Equivalents"], panel["Total Assets"])
    derived["borrowings_to_assets"] = safe_div(panel["Borrowings"], panel["Total Assets"])

    panel = pd.concat([panel, pd.DataFrame(derived)], axis=1)

    # The same tight signals from v5
    SIGNALS = [
        # Single ultra-tight
        ("FA CAGR (3y) > 30%", "fixed_assets_cagr3y > 30"),
        ("FA CAGR (3y) > 35%", "fixed_assets_cagr3y > 35"),
        ("FA CAGR (3y) > 40%", "fixed_assets_cagr3y > 40"),
        ("Reserves CAGR (3y) > 30%", "reserves_cagr3y > 30"),
        ("Reserves CAGR (3y) > 35%", "reserves_cagr3y > 35"),
        ("Reserves CAGR (3y) > 40%", "reserves_cagr3y > 40"),
        ("Reserves CAGR (5y) > 25%", "reserves_cagr5y > 25"),
        ("Reserves CAGR (5y) > 30%", "reserves_cagr5y > 30"),
        ("Reserves CAGR (5y) > 35%", "reserves_cagr5y > 35"),

        # Persistence
        ("FA > 25% YoY for 3 yrs",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25"),
        ("FA > 30% YoY for 3 yrs",
            "fixed_assets_yoy0 > 30 and fixed_assets_yoy1 > 30 and fixed_assets_yoy2 > 30"),
        ("FA > 20% YoY for 4 yrs",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and fixed_assets_yoy3 > 20"),
        ("Reserves > 25% YoY for 3 yrs",
            "reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25"),
        ("Reserves > 30% YoY for 3 yrs",
            "reserves_yoy0 > 30 and reserves_yoy1 > 30 and reserves_yoy2 > 30"),
        ("Reserves > 25% YoY for 4 yrs",
            "reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25 and reserves_yoy3 > 25"),

        # FA + Reserves both persistent (v5 winner)
        ("FA & Reserves both > 20% YoY for 3 yrs",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20"),
        ("FA & Reserves both > 25% YoY for 3 yrs",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25"),

        # Persistence + low-leverage
        ("FA > 20% YoY for 3 yrs AND D/E < 0.3",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and debt_to_equity < 0.3"),
        ("FA > 25% YoY for 3 yrs AND D/E < 0.3",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and debt_to_equity < 0.3"),
        ("FA > 25% YoY for 3 yrs AND D/E < 0.5",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and debt_to_equity < 0.5"),
        ("Reserves > 25% YoY for 3 yrs AND D/E < 0.3",
            "reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25 and debt_to_equity < 0.3"),
        ("Reserves > 25% YoY for 3 yrs AND D/E < 0.5",
            "reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25 and debt_to_equity < 0.5"),
        ("Reserves > 30% YoY for 3 yrs AND D/E < 0.5",
            "reserves_yoy0 > 30 and reserves_yoy1 > 30 and reserves_yoy2 > 30 and debt_to_equity < 0.5"),

        # 3-condition combined
        ("FA CAGR > 25% AND Reserves CAGR > 25% AND D/E < 0.5",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25 and debt_to_equity < 0.5"),
        ("FA CAGR > 25% AND Reserves CAGR > 25% AND D/E < 0.3",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 25 and debt_to_equity < 0.3"),
        ("FA CAGR > 25% AND Reserves CAGR > 30% AND D/E < 0.3",
            "fixed_assets_cagr3y > 25 and reserves_cagr3y > 30 and debt_to_equity < 0.3"),
        ("FA CAGR > 30% AND Reserves CAGR > 30% AND D/E < 0.5",
            "fixed_assets_cagr3y > 30 and reserves_cagr3y > 30 and debt_to_equity < 0.5"),
        ("Reserves CAGR > 25% AND Borrowings CAGR < -10%",
            "reserves_cagr3y > 25 and borrowings_cagr3y < -10"),
        ("Reserves CAGR > 30% AND Borrowings CAGR < -10%",
            "reserves_cagr3y > 30 and borrowings_cagr3y < -10"),
        ("Reserves CAGR > 30% AND Borrowings CAGR < 0%",
            "reserves_cagr3y > 30 and borrowings_cagr3y < 0"),

        # FA & Reserves persistent + leverage (the strongest combo)
        ("FA & Reserves both > 20% YoY for 3 yrs AND D/E < 0.5",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20 and debt_to_equity < 0.5"),
        ("FA & Reserves both > 20% YoY for 3 yrs AND D/E < 0.3",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20 and debt_to_equity < 0.3"),
        ("FA & Reserves both > 25% YoY for 3 yrs AND D/E < 0.5",
            "fixed_assets_yoy0 > 25 and fixed_assets_yoy1 > 25 and fixed_assets_yoy2 > 25 and reserves_yoy0 > 25 and reserves_yoy1 > 25 and reserves_yoy2 > 25 and debt_to_equity < 0.5"),

        # Cash-rich + growth
        ("Cash > 20% TA AND Reserves CAGR > 25%",
            "cash_to_assets > 0.20 and reserves_cagr3y > 25"),
        ("Cash > 25% TA AND Reserves CAGR > 25%",
            "cash_to_assets > 0.25 and reserves_cagr3y > 25"),
    ]

    print(f"Loaded {len(panel):,} panel rows")
    print(f"Testing {len(SIGNALS)} signals × 3 horizons at CAGR >= {CAGR_TARGET}% target ...")

    all_results = []
    company_rows = []

    for sig_name, expr in SIGNALS:
        try:
            mask = eval_signal(expr, panel).fillna(False)
        except Exception as e:
            print(f"  ERROR for '{sig_name}': {e}")
            continue
        for horizon_label, col in (("3y", "cagr3y_pct"), ("5y", "cagr5y_pct"), ("7y", "cagr7y_pct")):
            sub = panel[mask & panel[col].notna()].copy()
            n = len(sub)
            if n < MIN_N:
                continue
            hits = (sub[col] >= CAGR_TARGET).sum()
            rate = hits / n
            all_results.append({
                "signal": sig_name,
                "horizon": horizon_label,
                "n": n,
                "hits_cagr_ge_20pct": int(hits),
                "hit_rate_pct": round(rate * 100, 1),
                "avg_cagr_pct": round(sub[col].mean(), 1),
                "median_cagr_pct": round(sub[col].median(), 1),
                "min_cagr_pct": round(sub[col].min(), 1),
                "max_cagr_pct": round(sub[col].max(), 1),
            })
            if rate * 100 >= FALLBACK_HIT_RATE:
                for _, row in sub.iterrows():
                    company_rows.append({
                        "horizon": horizon_label,
                        "signal": sig_name,
                        "hit_rate_pct": round(rate * 100, 1),
                        "nse_symbol": row["nse_symbol"],
                        "industry": row["industry"] if pd.notna(row["industry"]) else "",
                        "base_year_T": int(row["base_year"]),
                        "fy_label": f"Mar {int(row['base_year'])}",
                        "stock_price_at_T": round(row["Stock Price (Rs)"], 2) if pd.notna(row["Stock Price (Rs)"]) else None,
                        "forward_cagr_pct": round(row[col], 1),
                        "met_target": "Y" if row[col] >= CAGR_TARGET else "N",
                    })

    results = pd.DataFrame(all_results).sort_values(
        ["hit_rate_pct", "n"], ascending=[False, False]
    )
    results.to_csv(HERE / "v6_all_horizons_results.csv", index=False)

    for hor in ("3y", "5y", "7y"):
        results[results["horizon"] == hor].to_csv(HERE / f"v6_{hor}_results.csv", index=False)
    print(f"\nSaved all-horizons results: v6_all_horizons_results.csv ({len(results)} rows)")

    # >= 80% hit rate patterns
    top = results[results["hit_rate_pct"] >= HIT_RATE_THRESHOLD].copy()
    top.to_csv(HERE / "v6_top_patterns_20pct.csv", index=False)
    print(f">= 80% hit rate patterns (CAGR>=20% target): {len(top)}")
    if len(top):
        print(top.to_string(index=False))

    # >= 70% for broader context
    top70 = results[results["hit_rate_pct"] >= 70].copy()
    print(f"\n>= 70% hit rate patterns: {len(top70)}")
    print(top70.head(20).to_string(index=False))

    if company_rows:
        comp = pd.DataFrame(company_rows).sort_values(
            ["horizon", "signal", "forward_cagr_pct"],
            ascending=[True, True, False]
        )
        comp.to_csv(HERE / "v6_company_matches.csv", index=False)
        print(f"\nCompany matches (>= {FALLBACK_HIT_RATE}% patterns): {len(comp):,} rows")

        # Build per-horizon readable MD
        lines = [
            "# 20% CAGR Patterns Across 3y, 5y, and 7y Horizons — Companies & Years",
            "",
            "**Universe:** Nifty 500 (all 500 constituents)",
            f"**CAGR target:** ≥ {CAGR_TARGET:.0f}% forward stock-price compound annual growth",
            "**Horizons evaluated:** 3 years, 5 years, 7 years (forward from base year T)",
            "**Predictor framing:** signals are computed using ONLY the balance sheet data",
            "through fiscal year-end T. The forward CAGR is then measured from T → T+horizon",
            "using the year-end stock prices.",
            "",
            "**'Met target'**: Y = forward CAGR ≥ 20%; N = forward CAGR < 20%.",
            "",
            "---",
            "",
            "## Summary table of all patterns at >= 70% hit rate for the 20% CAGR target",
            "",
            "| Horizon | Signal | n | Hits ≥ 20% CAGR | Hit Rate | Avg CAGR |",
            "|---------|--------|--:|--:|---:|---:|",
        ]
        for _, row in top70.sort_values(["horizon", "hit_rate_pct", "n"], ascending=[True, False, False]).iterrows():
            lines.append(
                f"| {row['horizon']} | {row['signal']} | {row['n']} | {row['hits_cagr_ge_20pct']} | "
                f"**{row['hit_rate_pct']:.1f}%** | {row['avg_cagr_pct']:.1f}% |"
            )
        lines.append("")
        lines.append("---")
        lines.append("")

        # Group by horizon + signal + (only keep patterns at >= 70% hit rate to make this readable)
        comp_filtered = comp[comp["hit_rate_pct"] >= 70].copy()
        for horizon_label in ("3y", "5y", "7y"):
            comp_h = comp_filtered[comp_filtered["horizon"] == horizon_label]
            if len(comp_h) == 0:
                continue
            lines.append(f"## Horizon: {horizon_label} forward")
            lines.append("")
            for sig in sorted(comp_h["signal"].unique()):
                sub = comp_h[comp_h["signal"] == sig].sort_values("forward_cagr_pct", ascending=False)
                hr = sub["hit_rate_pct"].iloc[0]
                n_total = len(sub)
                n_hits = (sub["met_target"] == "Y").sum()
                lines.append(f"### Pattern: {sig}")
                lines.append("")
                lines.append(f"- **Horizon**: {horizon_label}")
                lines.append(f"- **CAGR target**: ≥ {CAGR_TARGET:.0f}%")
                lines.append(f"- **Sample size**: {n_total}")
                lines.append(f"- **Hit rate**: **{hr:.1f}%** ({n_hits} of {n_total} met target)")
                lines.append(f"- **Avg realized CAGR**: {sub['forward_cagr_pct'].mean():.1f}%")
                lines.append("")
                lines.append("| # | NSE Symbol | Industry | Base Year (T) | Stock Price at T | Forward CAGR | Met ≥20%? |")
                lines.append("|--:|-----------|----------|---------------|-----------------:|-------------:|:----------|")
                for i, (_, row) in enumerate(sub.iterrows(), 1):
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

        (HERE / "COMPANIES_BY_PATTERN_ALL_HORIZONS_20pct.md").write_text("\n".join(lines))
        print(f"Wrote COMPANIES_BY_PATTERN_ALL_HORIZONS_20pct.md ({len(lines)} lines)")


if __name__ == "__main__":
    main()
