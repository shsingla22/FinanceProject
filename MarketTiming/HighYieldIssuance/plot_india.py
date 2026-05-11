"""India chart: number of HY issues, value of HY issuance, Nifty 50, Nifty
Midcap and Nifty/BSE Smallcap on a single line chart over the last 25 years.

Renders to ./india_high_yield_vs_indices.png and writes the joined dataset
to ./india_chart_data.csv for transparency.
"""

from __future__ import annotations
import os
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

from india_hy_issuance import build_india_hy_dataframe
from index_data import fetch_index, fetch_nifty50_with_sensex_backfill

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(HERE, "india_high_yield_vs_indices.png")
OUT_CSV = os.path.join(HERE, "india_chart_data.csv")
YEARS_BACK = 25


def annual_year_end_from_series(s: pd.Series, name: str) -> pd.Series:
    out = s.resample("YE").last()
    out.index = out.index.year
    out.name = name
    return out


def build_dataset(years_back: int = YEARS_BACK) -> pd.DataFrame:
    end_year = datetime.today().year
    start_year = end_year - years_back
    start_str = f"{start_year}-01-01"
    end_str = f"{end_year + 1}-01-01"

    hy = build_india_hy_dataframe()
    hy = hy[(hy.index >= start_year) & (hy.index <= end_year)]

    nifty50_daily = fetch_nifty50_with_sensex_backfill(start_str, end_str)
    nifty50 = annual_year_end_from_series(nifty50_daily, "nifty50")

    midcap_daily = fetch_index("NIFTY_MIDCAP_100.NS", start_str, end_str)
    midcap = annual_year_end_from_series(midcap_daily, "nifty_midcap")

    smallcap_daily = fetch_index("BSE-SMLCAP.BO", start_str, end_str)
    smallcap = annual_year_end_from_series(smallcap_daily, "nifty_smallcap")

    sensex_daily = fetch_index("^BSESN", start_str, end_str)
    sensex = annual_year_end_from_series(sensex_daily, "sensex")

    df = hy.join([nifty50, midcap, smallcap, sensex], how="outer")
    df.index.name = "year"
    return df


def plot(df: pd.DataFrame, out_path: str = OUT_PNG) -> None:
    fig, ax1 = plt.subplots(figsize=(17, 8.5))

    # Axis 1: HY issuance value (INR crore)
    color_val = "#1f77b4"
    l1 = ax1.plot(df.index, df["hy_value_inr_crore"],
                  color=color_val, marker="o", linewidth=2,
                  label="HY issuance value (INR cr)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("HY issuance value (INR crore)", color=color_val)
    ax1.tick_params(axis="y", labelcolor=color_val)

    # Axis 2: HY number of issues
    ax2 = ax1.twinx()
    color_cnt = "#2ca02c"
    l2 = ax2.plot(df.index, df["hy_number_of_issues"],
                  color=color_cnt, marker="s", linewidth=2,
                  label="HY number of issues")
    ax2.set_ylabel("Number of HY issues", color=color_cnt)
    ax2.tick_params(axis="y", labelcolor=color_cnt)

    # Axis 3: Index levels (shared scale, far right)
    ax3 = ax1.twinx()
    ax3.spines["right"].set_position(("axes", 1.08))
    l3 = ax3.plot(df.index, df["nifty50"],
                  color="#d62728", marker="^", linewidth=2,
                  label="Nifty 50 (year-end close)")
    l4 = ax3.plot(df.index, df["nifty_midcap"],
                  color="#9467bd", marker="v", linewidth=2,
                  label="Nifty Midcap 100 (year-end close)")
    l5 = ax3.plot(df.index, df["nifty_smallcap"],
                  color="#ff7f0e", marker="D", linewidth=2,
                  label="Nifty/BSE Smallcap (year-end close)")
    ax3.set_ylabel("Index level (year-end close)", color="#444444")
    ax3.tick_params(axis="y", labelcolor="#444444")

    lines = l1 + l2 + l3 + l4 + l5
    labels = [ln.get_label() for ln in lines]
    ax1.legend(lines, labels, loc="upper left", framealpha=0.9)

    plt.title(f"India: High-Yield Bond Issuance vs. Nifty 50 / Midcap / "
              f"Smallcap (last {YEARS_BACK} years)")
    ax1.grid(True, alpha=0.3)
    ax1.set_xticks(df.index)
    ax1.set_xticklabels([str(y) for y in df.index], rotation=45)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    df = build_dataset(years_back=YEARS_BACK)
    df.to_csv(OUT_CSV)
    print(df.to_string())
    print(f"\nWrote: {OUT_CSV}")
    plot(df)
