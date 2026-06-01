"""
Plot US IPO annual statistics + size-segment indices across 2000-2025.

Reads:
  - us_ipo_data.csv (SEC DERA source)
  - sp500_data.csv, sp_midcap400_data.csv, russell2000_data.csv (Yahoo)

Renders a multi-axis line chart with:
  - Left axis (y1): IPO counts (total, corporate, SPAC, fund)
  - Right axis (y2): IPO gross proceeds in $ billions
  - Right axis 2 (y3): US index levels (S&P 500, S&P 400, Russell 2000)
  - Right axis 3 (y4): US index YoY % changes

Output: us_ipo_combined.png

Usage:
    python3 plot_us_ipo.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
OUT = HERE / "us_ipo_combined.png"


def load():
    ipo = pd.read_csv(HERE / "us_ipo_data.csv")
    for c in ["ipo_proceeds_total_usd_mn", "ipo_proceeds_corporate_usd_mn",
              "ipo_proceeds_spac_usd_mn", "ipo_proceeds_fund_usd_mn"]:
        ipo[c.replace("_mn", "_bn")] = ipo[c] / 1000

    def load_index(csv_name, prefix):
        df = pd.read_csv(HERE / csv_name)
        df = df[["calendar_year", "year_end_close"]].rename(
            columns={"year_end_close": f"{prefix}_level"})
        df[f"{prefix}_yoy"] = (df[f"{prefix}_level"].pct_change() * 100).round(2)
        return df

    sp500 = load_index("sp500_data.csv", "sp500")
    sp400 = load_index("sp_midcap400_data.csv", "sp400")
    rut   = load_index("russell2000_data.csv", "rut")
    df = ipo.merge(sp500, on="calendar_year")\
            .merge(sp400, on="calendar_year")\
            .merge(rut,   on="calendar_year")
    return df


def plot(df):
    fig, ax_count = plt.subplots(figsize=(22, 12))
    ax_amount = ax_count.twinx()
    ax_level  = ax_count.twinx()
    ax_yoy    = ax_count.twinx()

    # Spread the three right-side axes
    ax_amount.spines["right"].set_position(("outward", 0))
    ax_level.spines["right"].set_position(("outward", 80))
    ax_yoy.spines["right"].set_position(("outward", 160))

    x = df["calendar_year"]

    cnt_lines = [
        ax_count.plot(x, df["ipo_count_total"], marker="o", linewidth=2.5,
                      color="#1f77b4", label="(1) Total IPO count")[0],
        ax_count.plot(x, df["ipo_count_corporate"], marker="^", linewidth=2,
                      color="#2ca02c", label="(2) Corporate IPO count")[0],
        ax_count.plot(x, df["ipo_count_spac"], marker="s", linewidth=2,
                      color="#d62728", label="(3) SPAC IPO count")[0],
        ax_count.plot(x, df["ipo_count_fund"], marker="x", linewidth=1.5,
                      color="#8c564b", label="(4) Fund / BDC IPO count")[0],
    ]
    amt_lines = [
        ax_amount.plot(x, df["ipo_proceeds_total_usd_bn"], marker="D", linewidth=2.5,
                       color="#ff7f0e", linestyle="--",
                       label="(5) Total IPO proceeds ($ B)")[0],
        ax_amount.plot(x, df["ipo_proceeds_corporate_usd_bn"], marker="P", linewidth=2,
                       color="#17becf", linestyle="--",
                       label="(6) Corporate IPO proceeds ($ B)")[0],
        ax_amount.plot(x, df["ipo_proceeds_spac_usd_bn"], marker="*", linewidth=2,
                       color="#e377c2", linestyle="--",
                       label="(7) SPAC IPO proceeds ($ B)")[0],
    ]
    lvl_lines = [
        ax_level.plot(x, df["sp500_level"], marker="o", linewidth=2.5,
                      color="#003f5c", label="(8) S&P 500 close")[0],
        ax_level.plot(x, df["sp400_level"], marker="s", linewidth=2.5,
                      color="#bc5090", label="(9) S&P MidCap 400 close")[0],
        ax_level.plot(x, df["rut_level"], marker="^", linewidth=2.5,
                      color="#ff6361", label="(10) Russell 2000 close")[0],
    ]
    yoy_lines = [
        ax_yoy.plot(x, df["sp500_yoy"], marker=".", linewidth=1.5,
                    color="#003f5c", linestyle=":",
                    label="(11) S&P 500 YoY %")[0],
        ax_yoy.plot(x, df["sp400_yoy"], marker=".", linewidth=1.5,
                    color="#bc5090", linestyle=":",
                    label="(12) S&P MidCap 400 YoY %")[0],
        ax_yoy.plot(x, df["rut_yoy"], marker=".", linewidth=1.5,
                    color="#ff6361", linestyle=":",
                    label="(13) Russell 2000 YoY %")[0],
    ]
    ax_yoy.axhline(0, color="grey", linewidth=0.5, alpha=0.4)

    ax_count.set_xlabel("Calendar year", fontsize=12)
    ax_count.set_ylabel("Number of IPOs", color="#1f77b4", fontsize=11)
    ax_amount.set_ylabel("IPO proceeds (US$ B)", color="#ff7f0e", fontsize=11)
    ax_level.set_ylabel("Index level (price)", color="#003f5c", fontsize=11)
    ax_yoy.set_ylabel("Index YoY % change", color="#444", fontsize=11)

    ax_count.tick_params(axis="y", labelcolor="#1f77b4")
    ax_amount.tick_params(axis="y", labelcolor="#ff7f0e")
    ax_level.tick_params(axis="y", labelcolor="#003f5c")
    ax_yoy.tick_params(axis="y", labelcolor="#444")

    ax_count.set_xticks(x)
    ax_count.set_xticklabels(x, rotation=45)
    ax_count.grid(True, alpha=0.3)

    # Annotations on extreme years
    ax_count.annotate(
        "2021: SPAC mania peak\n1,078 IPOs / $303B / Russell +14%",
        xy=(2021, 1078), xytext=(2016.5, 950),
        fontsize=9.5, color="#d62728",
        arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.2),
    )
    ax_count.annotate(
        "2008: GFC freeze\nIPOs frozen + indices -35% to -38%",
        xy=(2008, 60), xytext=(2009.5, 280),
        fontsize=9.5, color="#444",
        arrowprops=dict(arrowstyle="->", color="#444", lw=1.0),
    )
    ax_count.annotate(
        "2022: Fed-hike freeze\nIPOs -93%; S&P 500 -19%; Russell -22%",
        xy=(2022, 202), xytext=(2023, 480),
        fontsize=9.5, color="#444",
        arrowprops=dict(arrowstyle="->", color="#444", lw=1.0),
    )

    fig.suptitle(
        "U.S. IPO market + size-segment indices — yearly view, CY 2000-2025\n"
        "Sources: IPO data — U.S. SEC DERA (sec-stats-ipos-20260317.xlsx); "
        "index levels — Yahoo Finance daily (^GSPC, ^MID, ^RUT)\n"
        "https://www.sec.gov/data-research/statistics-data-visualizations/initial-public-offerings-ipos",
        fontsize=12, y=0.995,
    )

    lines = cnt_lines + amt_lines + lvl_lines + yoy_lines
    labels = [ln.get_label() for ln in lines]
    ax_count.legend(lines, labels, loc="upper left", fontsize=9.5,
                    framealpha=0.92, ncol=3)

    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    plot(load())
