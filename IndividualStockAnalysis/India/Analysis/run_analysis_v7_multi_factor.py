"""
Comprehensive multi-factor analysis combining:
  - Balance Sheet features (Fixed Assets, Reserves, Borrowings, etc.)
  - Profit & Loss features (Sales, Net Profit, Operating Profit, OPM, EPS)
  - Stock Info features (P/E ratio, Stock Price)

Tests ~100 signal definitions across 3y, 5y, 7y forward horizons at the
strict CAGR >= 20% target. Reports any pattern at >= 80% hit rate.

The user's question: 'find all the patterns which lead to around 20%
CAGR in 3, 5 or 7 years' using BS + P&L + P/E together.

Predictor framing (unchanged from v5/v6):
  - Features computed using BS, P&L, and stock info data through
    fiscal year-end T
  - Forward CAGR measured from T -> T+horizon using year-end stock prices

Outputs:
  v7_results.csv               — every signal × horizon row
  v7_top_patterns.csv          — patterns at >= 80% hit rate
  v7_company_matches.csv       — (pattern, company, year) rows for
                                  qualifying patterns
  ALL_PATTERNS_20PCT_CAGR.md   — comprehensive readable report
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

CAGR_TARGET = 20.0
HIT_RATE_THRESHOLD = 80.0
MIN_N = 5


def load_wide_with_dedup(long_csv, value_col):
    df = pd.read_csv(long_csv)
    if "parent_line_item" in df.columns:
        df["_p"] = df["parent_line_item"].fillna("").astype(str).str.len()
        df = df.sort_values("_p").drop_duplicates(
            subset=["nse_symbol", "year", "line_item"], keep="first"
        ).drop(columns=["_p"])
    cols = [c for c in df.columns if c == "nse_symbol" or c == "year" or c == "line_item" or c == value_col]
    return df[cols].pivot_table(
        index=["nse_symbol", "year"], columns="line_item",
        values=value_col, aggfunc="first"
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
    bs = load_wide_with_dedup(DATA_BS, "value_rs_cr")
    pl = load_wide_with_dedup(DATA_PL, "value")
    si = load_wide_si(DATA_SI)
    const = pd.read_csv(DATA_CON)

    print(f"  BS: {bs.shape}")
    print(f"  PL: {pl.shape}")
    print(f"  SI: {si.shape}")

    # Combine all three into one panel
    panel = bs.join(pl, how="outer", rsuffix="_pl").join(si, how="outer", rsuffix="_si").reset_index()
    panel["base_year"] = panel["year"].apply(year_to_int)
    panel = panel.dropna(subset=["base_year"]).copy()
    panel["base_year"] = panel["base_year"].astype(int)
    panel["industry"] = panel["nse_symbol"].map(
        dict(zip(const["nse_symbol"], const["industry"]))
    )
    panel = panel.sort_values(["nse_symbol", "base_year"]).reset_index(drop=True)
    g = panel.groupby("nse_symbol", group_keys=False)

    # Items we want to compute lagged values + CAGRs for
    BS_ITEMS = [
        "Fixed Assets", "Total Assets", "Equity Capital", "Reserves",
        "Borrowings", "Cash Equivalents", "Inventories", "Trade receivables",
        "Trade Payables", "Investments", "CWIP",
    ]
    PL_ITEMS = [
        "Sales", "Net Profit", "Operating Profit", "OPM %",
        "Other Income", "Interest", "Depreciation", "EPS in Rs",
        "Profit before tax",
    ]
    ALL_LAGGABLE = BS_ITEMS + PL_ITEMS
    ALL_LAGGABLE = [c for c in ALL_LAGGABLE if c in panel.columns]

    add = {}
    for col in ALL_LAGGABLE:
        for n in (1, 2, 3, 4, 5):
            add[f"{col}__lag{n}"] = g[col].shift(n)
    add["price_fwd3"] = g["Stock Price (Rs)"].shift(-3)
    add["price_fwd5"] = g["Stock Price (Rs)"].shift(-5)
    add["price_fwd7"] = g["Stock Price (Rs)"].shift(-7)
    panel = pd.concat([panel, pd.DataFrame(add)], axis=1)

    panel["cagr3y_pct"] = safe_cagr(panel["price_fwd3"], panel["Stock Price (Rs)"], 3)
    panel["cagr5y_pct"] = safe_cagr(panel["price_fwd5"], panel["Stock Price (Rs)"], 5)
    panel["cagr7y_pct"] = safe_cagr(panel["price_fwd7"], panel["Stock Price (Rs)"], 7)

    print("Computing derived features ...")
    derived = {}
    for col in ALL_LAGGABLE:
        for n in (1, 3, 5):
            name = col.lower().replace(" ", "_").replace("%", "pct") + f"_cagr{n}y"
            derived[name] = safe_cagr(panel[col], panel[f"{col}__lag{n}"], n)
        # YoY for each of the last 4 years (shift 0-3)
        for shift_n, lbl in ((0, "yoy0"), (1, "yoy1"), (2, "yoy2"), (3, "yoy3")):
            cur = g[col].shift(shift_n)
            prev = g[col].shift(shift_n + 1)
            derived[f"{col.lower().replace(' ', '_').replace('%', 'pct')}_{lbl}"] = safe_cagr(cur, prev, 1)

    # BS ratios
    equity_total = panel["Equity Capital"] + panel["Reserves"]
    derived["debt_to_equity"] = safe_div(panel["Borrowings"], equity_total)
    derived["cash_to_assets"] = safe_div(panel["Cash Equivalents"], panel["Total Assets"])
    derived["fa_to_assets"] = safe_div(panel["Fixed Assets"], panel["Total Assets"])
    # P&L ratios already exist as "OPM %" — convert to numeric
    derived["opm_pct"] = panel["OPM %"]
    derived["opm_pct_lag3"] = g["OPM %"].shift(3)
    derived["opm_change_3y"] = panel["OPM %"] - g["OPM %"].shift(3)
    # ROE/ROCE proxies
    derived["roe_proxy_pct"] = safe_div(panel["Net Profit"], equity_total) * 100
    derived["roce_proxy_pct"] = safe_div(panel["Operating Profit"], equity_total + panel["Borrowings"]) * 100
    # Asset turnover
    derived["asset_turnover"] = safe_div(panel["Sales"], panel["Total Assets"])
    # Margin levels
    derived["np_to_sales_pct"] = safe_div(panel["Net Profit"], panel["Sales"]) * 100

    panel = pd.concat([panel, pd.DataFrame(derived)], axis=1)

    SIGNALS = [
        # ============== PURE P&L SIGNALS ==============
        # Sales growth
        ("Sales CAGR (3y) > 20%", "sales_cagr3y > 20"),
        ("Sales CAGR (3y) > 25%", "sales_cagr3y > 25"),
        ("Sales CAGR (3y) > 30%", "sales_cagr3y > 30"),
        ("Sales CAGR (5y) > 20%", "sales_cagr5y > 20"),
        ("Sales CAGR (5y) > 25%", "sales_cagr5y > 25"),
        ("Sales > 20% YoY for 3 yrs",
            "sales_yoy0 > 20 and sales_yoy1 > 20 and sales_yoy2 > 20"),
        ("Sales > 25% YoY for 3 yrs",
            "sales_yoy0 > 25 and sales_yoy1 > 25 and sales_yoy2 > 25"),
        ("Sales > 30% YoY for 3 yrs",
            "sales_yoy0 > 30 and sales_yoy1 > 30 and sales_yoy2 > 30"),
        ("Sales > 20% YoY for 4 yrs",
            "sales_yoy0 > 20 and sales_yoy1 > 20 and sales_yoy2 > 20 and sales_yoy3 > 20"),

        # Net Profit growth
        ("Net Profit CAGR (3y) > 20%", "net_profit_cagr3y > 20"),
        ("Net Profit CAGR (3y) > 25%", "net_profit_cagr3y > 25"),
        ("Net Profit CAGR (3y) > 30%", "net_profit_cagr3y > 30"),
        ("Net Profit > 25% YoY for 3 yrs",
            "net_profit_yoy0 > 25 and net_profit_yoy1 > 25 and net_profit_yoy2 > 25"),
        ("Net Profit > 30% YoY for 3 yrs",
            "net_profit_yoy0 > 30 and net_profit_yoy1 > 30 and net_profit_yoy2 > 30"),

        # Operating Profit growth
        ("Operating Profit CAGR (3y) > 25%", "operating_profit_cagr3y > 25"),
        ("Operating Profit CAGR (3y) > 30%", "operating_profit_cagr3y > 30"),
        ("Operating Profit > 25% YoY for 3 yrs",
            "operating_profit_yoy0 > 25 and operating_profit_yoy1 > 25 and operating_profit_yoy2 > 25"),

        # OPM levels and expansion
        ("OPM > 20% (high margin)", "opm_pct > 20"),
        ("OPM > 25%", "opm_pct > 25"),
        ("OPM > 30%", "opm_pct > 30"),
        ("OPM expanded 3y (current > 3y ago)", "opm_change_3y > 0"),
        ("OPM expanded 5pp over 3y", "opm_change_3y > 5"),
        ("OPM > 20% AND OPM expanded 3y", "opm_pct > 20 and opm_change_3y > 0"),
        ("OPM > 25% AND OPM expanded 3y", "opm_pct > 25 and opm_change_3y > 0"),

        # ============== COMBINED P&L SIGNALS ==============
        ("Sales CAGR > 20% AND Net Profit CAGR > 20%",
            "sales_cagr3y > 20 and net_profit_cagr3y > 20"),
        ("Sales CAGR > 25% AND Net Profit CAGR > 25%",
            "sales_cagr3y > 25 and net_profit_cagr3y > 25"),
        ("Sales CAGR > 20% AND Net Profit CAGR > 25% (operating leverage)",
            "sales_cagr3y > 20 and net_profit_cagr3y > 25"),
        ("Net Profit CAGR > Sales CAGR (margin expanding)",
            "net_profit_cagr3y > sales_cagr3y and sales_cagr3y > 10"),
        ("Op Profit CAGR > Sales CAGR (margin expanding)",
            "operating_profit_cagr3y > sales_cagr3y and sales_cagr3y > 10"),
        ("Sales CAGR > 20% AND OPM expanded",
            "sales_cagr3y > 20 and opm_change_3y > 0"),
        ("Sales CAGR > 25% AND OPM expanded",
            "sales_cagr3y > 25 and opm_change_3y > 0"),

        # ============== P&L + Quality (ROCE/ROE) ==============
        ("Sales CAGR > 20% AND ROCE > 20%",
            "sales_cagr3y > 20 and roce_proxy_pct > 20"),
        ("Sales CAGR > 20% AND ROCE > 25%",
            "sales_cagr3y > 20 and roce_proxy_pct > 25"),
        ("Sales CAGR > 25% AND ROCE > 25%",
            "sales_cagr3y > 25 and roce_proxy_pct > 25"),
        ("Net Profit CAGR > 25% AND ROE > 20%",
            "net_profit_cagr3y > 25 and roe_proxy_pct > 20"),
        ("Net Profit CAGR > 25% AND ROCE > 25%",
            "net_profit_cagr3y > 25 and roce_proxy_pct > 25"),

        # ============== P&L + Balance Sheet ==============
        ("Sales CAGR > 20% AND Reserves CAGR > 25%",
            "sales_cagr3y > 20 and reserves_cagr3y > 25"),
        ("Sales CAGR > 25% AND Reserves CAGR > 25%",
            "sales_cagr3y > 25 and reserves_cagr3y > 25"),
        ("NP CAGR > 25% AND Reserves CAGR > 25%",
            "net_profit_cagr3y > 25 and reserves_cagr3y > 25"),
        ("Sales CAGR > 25% AND FA CAGR > 25%",
            "sales_cagr3y > 25 and fixed_assets_cagr3y > 25"),
        ("Sales CAGR > 25% AND FA CAGR > 25% AND D/E < 0.5",
            "sales_cagr3y > 25 and fixed_assets_cagr3y > 25 and debt_to_equity < 0.5"),
        ("Sales CAGR > 20% AND FA CAGR > 20% AND D/E < 0.5",
            "sales_cagr3y > 20 and fixed_assets_cagr3y > 20 and debt_to_equity < 0.5"),

        # ============== P&L + Valuation (P/E) ==============
        ("P/E < 15 AND Sales CAGR > 15%",
            "ratio < 15 and sales_cagr3y > 15"),
        ("P/E < 20 AND Sales CAGR > 20%",
            "ratio < 20 and sales_cagr3y > 20"),
        ("P/E < 30 AND Sales CAGR > 25%",
            "ratio < 30 and sales_cagr3y > 25"),
        ("P/E < 25 AND Net Profit CAGR > 20%",
            "ratio < 25 and net_profit_cagr3y > 20"),
        ("P/E < 30 AND Net Profit CAGR > 25%",
            "ratio < 30 and net_profit_cagr3y > 25"),
        # PEG-style screens
        ("P/E < 30 AND Sales CAGR > 20% AND ROCE > 20%",
            "ratio < 30 and sales_cagr3y > 20 and roce_proxy_pct > 20"),

        # ============== Triple-factor combined ==============
        ("Sales CAGR > 20% AND NP CAGR > 25% AND D/E < 0.5",
            "sales_cagr3y > 20 and net_profit_cagr3y > 25 and debt_to_equity < 0.5"),
        ("Sales CAGR > 25% AND NP CAGR > 25% AND D/E < 0.5",
            "sales_cagr3y > 25 and net_profit_cagr3y > 25 and debt_to_equity < 0.5"),
        ("Sales CAGR > 20% AND OPM > 20% AND D/E < 0.5",
            "sales_cagr3y > 20 and opm_pct > 20 and debt_to_equity < 0.5"),
        ("FA CAGR > 25% AND Sales CAGR > 20% AND NP CAGR > 20%",
            "fixed_assets_cagr3y > 25 and sales_cagr3y > 20 and net_profit_cagr3y > 20"),

        # ============== v5/v6 BS winners with P&L overlay ==============
        ("FA > 30% YoY for 3 yrs (the v6 winner; pure BS)",
            "fixed_assets_yoy0 > 30 and fixed_assets_yoy1 > 30 and fixed_assets_yoy2 > 30"),
        ("FA > 30% YoY for 3 yrs AND Sales CAGR > 15%",
            "fixed_assets_yoy0 > 30 and fixed_assets_yoy1 > 30 and fixed_assets_yoy2 > 30 and sales_cagr3y > 15"),
        ("FA > 30% YoY for 3 yrs AND NP CAGR > 20%",
            "fixed_assets_yoy0 > 30 and fixed_assets_yoy1 > 30 and fixed_assets_yoy2 > 30 and net_profit_cagr3y > 20"),
        ("FA & Reserves both > 20% YoY for 3 yrs (v5 winner)",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20"),
        ("FA & Reserves > 20% YoY 3yrs AND Sales CAGR > 15%",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20 and sales_cagr3y > 15"),
        ("FA & Reserves > 20% YoY 3yrs AND NP CAGR > 20%",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20 and net_profit_cagr3y > 20"),
        ("FA & Reserves > 20% YoY 3yrs AND Sales CAGR > 20%",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20 and sales_cagr3y > 20"),
        ("FA & Reserves > 20% YoY 3yrs AND ROCE > 20%",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and reserves_yoy0 > 20 and reserves_yoy1 > 20 and reserves_yoy2 > 20 and roce_proxy_pct > 20"),

        # ============== Holy grail — multi-factor BS + P&L + Valuation ==============
        ("FA > 20% YoY 3yrs AND Sales CAGR > 20% AND NP CAGR > 20%",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and sales_cagr3y > 20 and net_profit_cagr3y > 20"),
        ("FA > 20% YoY 3yrs AND Sales CAGR > 20% AND NP CAGR > 20% AND D/E < 0.5",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and sales_cagr3y > 20 and net_profit_cagr3y > 20 and debt_to_equity < 0.5"),
        ("FA > 20% YoY 3yrs AND Sales CAGR > 20% AND ROCE > 20%",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and sales_cagr3y > 20 and roce_proxy_pct > 20"),
        ("FA > 20% YoY 3yrs AND Sales CAGR > 20% AND ROCE > 25%",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and sales_cagr3y > 20 and roce_proxy_pct > 25"),
        ("FA > 20% YoY 3yrs AND OPM > 20% AND D/E < 0.5",
            "fixed_assets_yoy0 > 20 and fixed_assets_yoy1 > 20 and fixed_assets_yoy2 > 20 and opm_pct > 20 and debt_to_equity < 0.5"),
    ]

    print(f"\nLoaded {len(panel):,} panel rows")
    print(f"Testing {len(SIGNALS)} signals × 3 horizons at CAGR >= {CAGR_TARGET}% target ...")

    all_results = []
    company_rows = []

    # Note: 'ratio' may not be in the panel — that's the P/E ratio column
    # name from StockInfo (since it's the column name from screener.in's
    # 'P/E ratio' metric). Let me alias it.
    if "P/E ratio" in panel.columns and "ratio" not in panel.columns:
        panel["ratio"] = panel["P/E ratio"]

    for sig_name, expr in SIGNALS:
        try:
            mask = eval_signal(expr, panel).fillna(False)
        except Exception as e:
            print(f"  SKIP '{sig_name[:50]}': {str(e)[:50]}")
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
            if rate * 100 >= HIT_RATE_THRESHOLD:
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
                        "pe_at_T": round(row["P/E ratio"], 2) if "P/E ratio" in panel.columns and pd.notna(row["P/E ratio"]) else None,
                        "forward_cagr_pct": round(row[col], 1),
                        "met_target": "Y" if row[col] >= CAGR_TARGET else "N",
                    })

    results = pd.DataFrame(all_results).sort_values(
        ["hit_rate_pct", "n"], ascending=[False, False]
    )
    results.to_csv(HERE / "v7_results.csv", index=False)
    print(f"\nAll results: v7_results.csv ({len(results)} rows)")

    top = results[results["hit_rate_pct"] >= HIT_RATE_THRESHOLD].copy()
    top.to_csv(HERE / "v7_top_patterns.csv", index=False)
    print(f">= 80% hit rate patterns: {len(top)}")
    if len(top):
        print(top.to_string(index=False))

    if company_rows:
        comp = pd.DataFrame(company_rows).sort_values(
            ["horizon", "hit_rate_pct", "signal", "forward_cagr_pct"],
            ascending=[True, False, True, False]
        )
        comp.to_csv(HERE / "v7_company_matches.csv", index=False)
        print(f"\nCompany matches (>= 80% patterns): {len(comp):,} rows")

        # Generate readable MD
        lines = [
            "# Comprehensive Patterns for ≥ 20% Stock CAGR — Multi-Factor (BS + P&L + P/E)",
            "",
            "**Universe:** Nifty 500 (all 500 constituents)",
            "**CAGR target:** ≥ 20% forward stock-price compound annual growth",
            "**Horizons:** 3 years, 5 years, 7 years",
            "**Predictor framing:** signals are computed using BS + P&L + P/E",
            "data through fiscal year-end T. The forward CAGR is then measured",
            "from T → T+horizon using year-end stock prices.",
            "",
            "**Met target**: ✅ Y = forward CAGR ≥ 20%; ❌ N = forward CAGR < 20%.",
            "",
            "---",
            "",
            "## Summary of all patterns at ≥ 80% hit rate",
            "",
            "| Horizon | Signal | n | Hits ≥ 20% | Hit Rate | Avg CAGR |",
            "|---------|--------|--:|-----------:|---------:|---------:|",
        ]
        for _, row in top.sort_values(["horizon", "hit_rate_pct", "n"], ascending=[True, False, False]).iterrows():
            lines.append(
                f"| {row['horizon']} | {row['signal']} | {row['n']} | {row['hits_cagr_ge_20pct']} | "
                f"**{row['hit_rate_pct']:.1f}%** | {row['avg_cagr_pct']:.1f}% |"
            )
        lines.append("")
        lines.append("---")
        lines.append("")

        # Group by horizon → signal
        for horizon_label in ("3y", "5y", "7y"):
            comp_h = comp[comp["horizon"] == horizon_label]
            if len(comp_h) == 0:
                continue
            lines.append(f"## Horizon: {horizon_label} forward")
            lines.append("")
            for sig in comp_h["signal"].unique():
                sub = comp_h[comp_h["signal"] == sig].sort_values("forward_cagr_pct", ascending=False)
                hr = sub["hit_rate_pct"].iloc[0]
                n_total = len(sub)
                n_hits = (sub["met_target"] == "Y").sum()
                lines.append(f"### Pattern: {sig}")
                lines.append("")
                lines.append(f"- **Horizon**: {horizon_label}")
                lines.append(f"- **CAGR target**: ≥ {CAGR_TARGET:.0f}%")
                lines.append(f"- **Sample size**: {n_total}")
                lines.append(f"- **Hit rate**: **{hr:.1f}%** ({n_hits} of {n_total})")
                lines.append(f"- **Avg realized CAGR**: {sub['forward_cagr_pct'].mean():.1f}%")
                lines.append("")
                lines.append("| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |")
                lines.append("|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|")
                for i, (_, row) in enumerate(sub.iterrows(), 1):
                    ind = row["industry"] or "(uncl.)"
                    mark = "✅" if row["met_target"] == "Y" else "❌"
                    price = row["stock_price_at_T"]
                    price_str = f"₹{price:,.0f}" if price is not None else "n/a"
                    pe = row["pe_at_T"]
                    pe_str = f"{pe:.1f}" if pe is not None else "n/a"
                    lines.append(
                        f"| {i} | {row['nse_symbol']} | {ind} | {row['fy_label']} | "
                        f"{price_str} | {pe_str} | {row['forward_cagr_pct']:+.1f}% | {mark} {row['met_target']} |"
                    )
                lines.append("")
            lines.append("---")
            lines.append("")

        (HERE / "ALL_PATTERNS_20PCT_CAGR.md").write_text("\n".join(lines))
        print(f"Wrote ALL_PATTERNS_20PCT_CAGR.md ({len(lines)} lines)")


if __name__ == "__main__":
    main()
