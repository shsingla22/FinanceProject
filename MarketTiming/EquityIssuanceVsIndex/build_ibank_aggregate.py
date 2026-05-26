"""
Compute per-company YoY % change for each listed Indian I-banking stock
and the equal-weighted basket average across all available companies in
each year.

Reads investment_banks_data.csv (year-end closing prices) and writes a
new derived file investment_banks_yoy.csv plus the basket-average
series. Re-run after appending new years or new companies to the
source CSV.

Usage:
    python3 build_ibank_aggregate.py
"""

from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
SRC = HERE / "investment_banks_data.csv"
OUT = HERE / "investment_banks_yoy.csv"


def load() -> pd.DataFrame:
    df = pd.read_csv(SRC)
    df = df.sort_values("calendar_year").reset_index(drop=True)
    # Strip the price columns (everything after year_end_date)
    return df


def compute() -> pd.DataFrame:
    df = load()
    company_cols = [c for c in df.columns if c not in ("calendar_year", "year_end_date")]

    # YoY % for each company
    yoy = pd.DataFrame({"calendar_year": df["calendar_year"],
                        "year_end_date": df["year_end_date"]})
    for c in company_cols:
        yoy[f"{c} — YoY %"] = (df[c].astype(float).pct_change() * 100).round(2)

    # Equal-weighted basket average across companies that have a YoY% in that year
    yoy_only = yoy.drop(columns=["calendar_year", "year_end_date"])
    yoy["I-banking basket YoY % (equal-weight, avg of available)"] = (
        yoy_only.mean(axis=1, skipna=True).round(2)
    )
    yoy["Number of companies in basket this year"] = yoy_only.notna().sum(axis=1)

    return yoy


def main() -> None:
    yoy = compute()
    yoy.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")
    print(yoy.to_string(index=False))


if __name__ == "__main__":
    main()
