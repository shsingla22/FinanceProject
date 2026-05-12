"""Chart 1: INR vs USD yearly value (last 25 years), single line graph.

Source: Yahoo Finance INR=X (rupees per US dollar). Yahoo's series starts
December 2003, so years 2001-2003 appear as missing.
"""

from __future__ import annotations
import os
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

from data_fetcher import fetch_inr_usd, annual_year_end

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(HERE, "inr_vs_usd.png")
OUT_CSV = os.path.join(HERE, "inr_vs_usd.csv")
YEARS_BACK = 25


def build_dataset(years_back: int = YEARS_BACK) -> pd.DataFrame:
    end_year = datetime.today().year
    start_year = end_year - years_back
    start = f"{start_year}-01-01"
    end = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    daily = fetch_inr_usd(start, end)
    yearly = annual_year_end(daily)
    df = yearly.to_frame()
    df = df[(df.index >= start_year) & (df.index <= end_year)]
    df.index.name = "year"
    return df


def plot(df: pd.DataFrame, out_path: str = OUT_PNG) -> None:
    fig, ax = plt.subplots(figsize=(13, 6))
    ax.plot(df.index, df["inr_per_usd"],
            color="#d62728", marker="o", linewidth=2,
            label="INR per 1 USD (year-end)")
    ax.set_xlabel("Year")
    ax.set_ylabel("INR per 1 USD")
    ax.set_title(f"Indian Rupee vs US Dollar (last {YEARS_BACK} years, "
                 f"year-end close)")
    ax.grid(True, alpha=0.3)
    ax.set_xticks(df.index)
    ax.set_xticklabels([str(y) for y in df.index], rotation=45)
    ax.legend(loc="upper left", framealpha=0.9)
    fig.tight_layout()
    fig.savefig(out_path, dpi=140)
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    df = build_dataset()
    df.to_csv(OUT_CSV)
    print(df.to_string())
    plot(df)
