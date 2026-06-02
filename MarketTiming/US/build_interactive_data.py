"""
Build the inlined JSON payload used by us_ipo_interactive.html.

Reads us_ipo_data.csv and prints a JSON object that gets pasted inline
into the HTML <script> block as `const DATA = ...`.

Why the JSON is inlined into the HTML instead of fetched at runtime:
- file:// URLs in Safari + Chrome block fetch() from disk for security.
- An inlined payload means the HTML works equally well opened directly
  from disk (no web server needed) and served from any origin.

Usage:
    python3 build_interactive_data.py > /tmp/us_ipo_data.json
    # then update the DATA = {...} block in us_ipo_interactive.html
"""

import json
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent


def main() -> None:
    df = pd.read_csv(HERE / "us_ipo_data.csv")
    payload = {
        "years":               df["calendar_year"].astype(int).tolist(),
        "count_total":         df["ipo_count_total"].tolist(),
        "count_corporate":     df["ipo_count_corporate"].tolist(),
        "count_spac":          df["ipo_count_spac"].tolist(),
        "count_fund":          df["ipo_count_fund"].tolist(),
        "count_us":            df["ipo_count_us_issuers"].tolist(),
        "count_non_us":        df["ipo_count_non_us_issuers"].tolist(),
        "proceeds_total":      df["ipo_proceeds_total_usd_mn"].tolist(),
        "proceeds_corporate":  df["ipo_proceeds_corporate_usd_mn"].tolist(),
        "proceeds_spac":       df["ipo_proceeds_spac_usd_mn"].tolist(),
        "proceeds_fund":       df["ipo_proceeds_fund_usd_mn"].tolist(),
        "avg_proceeds":        df["ipo_avg_proceeds_usd_mn"].tolist(),
        "median_proceeds":     df["ipo_median_proceeds_usd_mn"].tolist(),
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
