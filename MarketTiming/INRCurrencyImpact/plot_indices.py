"""Chart 2: Nifty 50, Nifty Midcap 100 and Nifty Smallcap (BSE Smallcap
proxy) yearly close prices on one line graph (last 25 years).

Source: Yahoo Finance (^NSEI, NIFTY_MIDCAP_100.NS, BSE-SMLCAP.BO).
"""

from __future__ import annotations
import os
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

from data_fetcher import fetch_indices, annual_year_end

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(HERE, "nifty_indices.png")
OUT_CSV = os.path.join(HERE, "nifty_indices.csv")
YEARS_BACK = 25


def build_dataset(years_back: int = YEARS_BACK) -> pd.DataFrame:
    end_year = datetime.today().year
    start_year = end_year - years_back
    start = f"{start_year}-01-01"
    end = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    daily = fetch_indices(start, end)
    yearly = annual_year_end(daily)
    yearly = yearly[(yearly.index >= start_year) & (yearly.index <= end_year)]
    yearly.index.name = "year"
    return yearly


def plot(df: pd.DataFrame, out_path: str = OUT_PNG) -> None:
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df.index, df["nifty50"],
            color="#1f77b4", marker="o", linewidth=2,
            label="Nifty 50")
    ax.plot(df.index, df["nifty_midcap"],
            color="#2ca02c", marker="s", linewidth=2,
            label="Nifty Midcap 100")
    ax.plot(df.index, df["nifty_smallcap"],
            color="#ff7f0e", marker="^", linewidth=2,
            label="Nifty/BSE Smallcap")
    ax.set_xlabel("Year")
    ax.set_ylabel("Index level (year-end close)")
    ax.set_title(f"Nifty 50 / Midcap 100 / Smallcap Yearly Close "
                 f"(last {YEARS_BACK} years)")
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
