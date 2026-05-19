"""
Combined chart of all 12 requested series on a single figure with
multiple y-axes. Reads only the CSV files committed to this folder.

Series (year on x-axis = calendar year for indices, fiscal-year-end
calendar year for IPO/FPO+Rights — both labeled with the year):

  Counts (left y-axis)
    1. Yearly number of IPOs (mainboard + SME) — ipo_data.csv
    4. Yearly number of FPO + Rights issues — fpo_rights_data.csv

  Amounts in INR crore (second y-axis)
    2. Yearly IPO amount raised — ipo_data.csv
    5. Yearly FPO + Rights amount raised — fpo_rights_data.csv

  Index levels (third y-axis)
    7. Nifty Smallcap 100 year-end close — nifty_smallcap100_data.csv
    9. Nifty 50 year-end close — nifty50_data.csv
   11. Nifty Midcap 100 year-end close — nifty_midcap100_data.csv

  YoY % change (fourth y-axis)
    3. IPO amount YoY %
    6. FPO+Rights amount YoY %
    8. Nifty Smallcap 100 YoY %
   10. Nifty 50 YoY %
   12. Nifty Midcap 100 YoY %

Coverage starts at 2000 (Nifty 50 only) and most series populate from
2001-02 (IPO/FPO+Rights) or 2006/2010/2012 (indices). Missing cells
are left blank by NaN — matplotlib renders them as line breaks.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
OUT = HERE / "all_series_combined.png"


def load() -> pd.DataFrame:
    ipo = pd.read_csv(HERE / "ipo_data.csv").rename(columns={"year_label": "year"})
    fpo = pd.read_csv(HERE / "fpo_rights_data.csv").rename(columns={"year_label": "year"})
    n50 = pd.read_csv(HERE / "nifty50_data.csv").rename(columns={"calendar_year": "year"})
    nsm = pd.read_csv(HERE / "nifty_smallcap100_data.csv").rename(columns={"calendar_year": "year"})
    nmd = pd.read_csv(HERE / "nifty_midcap100_data.csv").rename(columns={"calendar_year": "year"})

    years = pd.Index(range(2000, 2026), name="year")
    df = pd.DataFrame(index=years)
    df["ipo_count"] = ipo.set_index("year")["ipo_count_total"]
    df["ipo_amount_cr"] = ipo.set_index("year")["ipo_amount_cr_total"]
    df["fpor_count"] = fpo.set_index("year")["fpo_rights_count"]
    df["fpor_amount_cr"] = fpo.set_index("year")["fpo_rights_amount_cr"]
    df["nifty50"] = n50.set_index("year")["year_end_close"]
    df["smallcap100"] = nsm.set_index("year")["year_end_close"]
    df["midcap100"] = nmd.set_index("year")["year_end_close"]

    df["ipo_amount_yoy"] = df["ipo_amount_cr"].pct_change() * 100
    df["fpor_amount_yoy"] = df["fpor_amount_cr"].pct_change() * 100
    df["nifty50_yoy"] = df["nifty50"].pct_change() * 100
    df["smallcap100_yoy"] = df["smallcap100"].pct_change() * 100
    df["midcap100_yoy"] = df["midcap100"].pct_change() * 100
    return df.reset_index()


def plot(df: pd.DataFrame) -> None:
    fig, ax_count = plt.subplots(figsize=(22, 12))
    ax_amount = ax_count.twinx()
    ax_index = ax_count.twinx()
    ax_pct = ax_count.twinx()

    ax_amount.spines["right"].set_position(("outward", 0))
    ax_index.spines["right"].set_position(("outward", 80))
    ax_pct.spines["right"].set_position(("outward", 160))

    x = df["year"]

    cnt_lines = [
        ax_count.plot(x, df["ipo_count"], marker="^", linewidth=2,
                      color="#ff7f0e", label="(1) IPO count")[0],
        ax_count.plot(x, df["fpor_count"], marker="v", linewidth=2,
                      color="#d62728", label="(4) FPO+Rights count")[0],
    ]

    amt_lines = [
        ax_amount.plot(x, df["ipo_amount_cr"], marker="o", linewidth=2,
                       color="#1f77b4", label="(2) IPO amount raised (₹ cr)")[0],
        ax_amount.plot(x, df["fpor_amount_cr"], marker="s", linewidth=2,
                       color="#17becf", label="(5) FPO+Rights amount raised (₹ cr)")[0],
    ]

    idx_lines = [
        ax_index.plot(x, df["smallcap100"], marker="X", linewidth=2,
                      color="#8c564b", label="(7) Nifty Smallcap 100")[0],
        ax_index.plot(x, df["nifty50"], marker="D", linewidth=2,
                      color="#2ca02c", label="(9) Nifty 50")[0],
        ax_index.plot(x, df["midcap100"], marker="P", linewidth=2,
                      color="#9467bd", label="(11) Nifty Midcap 100")[0],
    ]

    pct_lines = [
        ax_pct.plot(x, df["ipo_amount_yoy"], marker=".", linewidth=1.2,
                    linestyle="--", color="#aec7e8",
                    label="(3) IPO amount YoY %")[0],
        ax_pct.plot(x, df["fpor_amount_yoy"], marker=".", linewidth=1.2,
                    linestyle="--", color="#9edae5",
                    label="(6) FPO+Rights amount YoY %")[0],
        ax_pct.plot(x, df["smallcap100_yoy"], marker=".", linewidth=1.2,
                    linestyle="--", color="#c49c94",
                    label="(8) Nifty Smallcap 100 YoY %")[0],
        ax_pct.plot(x, df["nifty50_yoy"], marker=".", linewidth=1.2,
                    linestyle="--", color="#98df8a",
                    label="(10) Nifty 50 YoY %")[0],
        ax_pct.plot(x, df["midcap100_yoy"], marker=".", linewidth=1.2,
                    linestyle="--", color="#c5b0d5",
                    label="(12) Nifty Midcap 100 YoY %")[0],
    ]
    ax_pct.axhline(0, color="grey", linewidth=0.5, alpha=0.4)

    ax_count.set_xlabel("Year")
    ax_count.set_ylabel("Number of issues", color="#d62728")
    ax_amount.set_ylabel("Amount raised (INR crore)", color="#1f77b4")
    ax_index.set_ylabel("Index level", color="#2ca02c")
    ax_pct.set_ylabel("YoY % change", color="grey")

    ax_count.tick_params(axis="y", labelcolor="#d62728")
    ax_amount.tick_params(axis="y", labelcolor="#1f77b4")
    ax_index.tick_params(axis="y", labelcolor="#2ca02c")
    ax_pct.tick_params(axis="y", labelcolor="grey")

    ax_count.set_xticks(x)
    ax_count.set_xticklabels(x, rotation=45)
    ax_count.grid(True, alpha=0.3)

    fig.suptitle(
        "Indian equity issuance, broad-market indices, and YoY % changes — 12-series combined view\n"
        "CY 2000-2025 (IPO/FPO+Rights data on fiscal-year basis, mapped to FY-ending calendar year)\n"
        "Source: SEBI Handbooks + SEBI Bulletin Annexures + NSE archives end-of-day index bhavcopy + Wikipedia (Nifty 50 pre-2010 only)",
        fontsize=12, y=0.995,
    )

    lines = cnt_lines + amt_lines + idx_lines + pct_lines
    labels = [ln.get_label() for ln in lines]
    ax_count.legend(lines, labels, loc="upper left", fontsize=8.5,
                    framealpha=0.92, ncol=2)

    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    plot(load())
