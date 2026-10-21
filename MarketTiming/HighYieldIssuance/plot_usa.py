"""USA chart: number of HY issues, $ value of HY issuance, and S&P 500
movement on a single line chart over the last 25 years.

Renders to ./usa_high_yield_vs_sp500.png and writes the underlying joined
dataset to ./usa_chart_data.csv for transparency.
"""

from __future__ import annotations
import os
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

from usa_hy_issuance import build_usa_hy_dataframe
from index_data import fetch_index

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(HERE, "usa_high_yield_vs_sp500.png")
OUT_CSV = os.path.join(HERE, "usa_chart_data.csv")
YEARS_BACK = 25


def build_dataset(years_back: int = YEARS_BACK) -> pd.DataFrame:
    end_year = datetime.today().year
    start_year = end_year - years_back

    hy = build_usa_hy_dataframe()
    hy = hy[(hy.index >= start_year) & (hy.index <= end_year)]

    sp = fetch_index("^GSPC", start=f"{start_year}-01-01",
                     end=f"{end_year + 1}-01-01")
    sp_annual = sp.resample("YE").last()
    sp_annual.index = sp_annual.index.year
    sp_annual.name = "sp500_year_end"

    df = hy.join(sp_annual, how="outer")
    df.index.name = "year"
    return df


def plot(df: pd.DataFrame, out_path: str = OUT_PNG) -> None:
    fig, ax1 = plt.subplots(figsize=(16, 8))

    # Primary axis: HY issuance value ($B)
    color_val = "#1f77b4"
    line_val = ax1.plot(df.index, df["hy_value_usd_bn"],
                        color=color_val, marker="o", linewidth=2,
                        label="HY issuance value ($B)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("HY issuance value (USD billions)", color=color_val)
    ax1.tick_params(axis="y", labelcolor=color_val)

    # Right axis #1: number of HY issues
    ax2 = ax1.twinx()
    color_cnt = "#2ca02c"
    line_cnt = ax2.plot(df.index, df["hy_number_of_issues"],
                        color=color_cnt, marker="s", linewidth=2,
                        label="HY number of issues")
    ax2.set_ylabel("Number of HY issues", color=color_cnt)
    ax2.tick_params(axis="y", labelcolor=color_cnt)

    # Right axis #2: S&P 500 year-end close (offset to the right)
    ax3 = ax1.twinx()
    ax3.spines["right"].set_position(("axes", 1.08))
    color_sp = "#d62728"
    line_sp = ax3.plot(df.index, df["sp500_year_end"],
                       color=color_sp, marker="^", linewidth=2,
                       label="S&P 500 (year-end close)")
    ax3.set_ylabel("S&P 500 year-end close", color=color_sp)
    ax3.tick_params(axis="y", labelcolor=color_sp)

    lines = line_val + line_cnt + line_sp
    labels = [ln.get_label() for ln in lines]
    ax1.legend(lines, labels, loc="upper left", framealpha=0.9)

    plt.title(f"USA: High-Yield Bond Issuance vs. S&P 500 "
              f"(last {YEARS_BACK} years)")
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
