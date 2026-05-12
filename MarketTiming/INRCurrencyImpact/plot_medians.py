"""Chart 3: Median year-end closing price of constituent companies for
Nifty 50, Nifty Midcap 100 and Nifty Smallcap 100 (last 25 years).

For each calendar year, the median is taken across all current constituents
of each index that have price data for that year (constituents that hadn't
IPO'd yet are excluded for that year).

Source: Yahoo Finance, one .NS ticker per constituent. The constituent
universe is the current published membership of each index (see
constituents.py).
"""

from __future__ import annotations
import os
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

from constituents import NIFTY_50, NIFTY_MIDCAP_100, NIFTY_SMALLCAP_100
from data_fetcher import (
    fetch_constituent_prices, yearly_median_of_constituents,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(HERE, "constituent_medians.png")
OUT_CSV = os.path.join(HERE, "constituent_medians.csv")
YEARS_BACK = 25


def build_dataset(years_back: int = YEARS_BACK) -> pd.DataFrame:
    end_year = datetime.today().year
    start_year = end_year - years_back
    start = f"{start_year}-01-01"
    end = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    p50 = fetch_constituent_prices(NIFTY_50, start, end)
    pmid = fetch_constituent_prices(NIFTY_MIDCAP_100, start, end)
    psmall = fetch_constituent_prices(NIFTY_SMALLCAP_100, start, end)

    med = pd.concat({
        "nifty50_median":   yearly_median_of_constituents(p50),
        "midcap_median":    yearly_median_of_constituents(pmid),
        "smallcap_median":  yearly_median_of_constituents(psmall),
    }, axis=1)
    med = med[(med.index >= start_year) & (med.index <= end_year)]
    med.index.name = "year"
    return med


def plot(df: pd.DataFrame, out_path: str = OUT_PNG) -> None:
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df.index, df["nifty50_median"],
            color="#1f77b4", marker="o", linewidth=2,
            label="Nifty 50 — median constituent close")
    ax.plot(df.index, df["midcap_median"],
            color="#2ca02c", marker="s", linewidth=2,
            label="Nifty Midcap 100 — median constituent close")
    ax.plot(df.index, df["smallcap_median"],
            color="#ff7f0e", marker="^", linewidth=2,
            label="Nifty Smallcap 100 — median constituent close")
    ax.set_xlabel("Year")
    ax.set_ylabel("Median constituent close (INR)")
    ax.set_title(f"Median Year-End Constituent Price: Nifty 50 / Midcap / "
                 f"Smallcap (last {YEARS_BACK} years)")
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
