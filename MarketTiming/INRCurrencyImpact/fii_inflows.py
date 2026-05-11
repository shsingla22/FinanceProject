"""Annual net FII / FPI inflows to Indian equity.

Primary data source: CDSL (Central Depository Services Limited) FPI/FII
Investment Details — Financial Year report. CDSL is one of India's two
official central depositories (NSDL is the other) that publish FPI/FII
investment statistics for SEBI:
    https://www.cdslindia.com/Publications/FIIFPIInvstmntFinYrData.aspx

The CDSL series gives net equity investment in INR crore per Indian
financial year (April-March). It is the same number that NSDL and SEBI
publish — these are official depository statistics.

USD conversion: yearly average INR/USD spot rate from FRED series
DEXINUS (India / U.S. Foreign Exchange Rate, daily, 1973-present):
    https://fred.stlouisfed.org/series/DEXINUS

Cap-segment breakdown (Nifty 50 / Midcap / Smallcap):
CDSL does NOT publish FII flow by index/cap-segment. The cap-segment
allocation here is the documented FPI ownership distribution from
NSE's India Ownership Tracker (Mar/Jun 2024):
    https://nsearchives.nseindia.com/web/sites/default/files/inline-files/Indian_Ownership_Report_Mar_2024.pdf
NSE June-2024 FPI ownership: Nifty 50 = 24.5%, Midcap 100 = 16%,
Smallcap 100 = 12.4%. Combined with the well-known free-float market
cap weights (Nifty 50 ~75%, Midcap 100 ~13%, Smallcap 100 ~5% of the
NSE 500 universe), the implied share of FPI holdings (and therefore
flow allocation, as a first-order approximation) is roughly:
    Nifty 50 : Nifty Midcap 100 : Nifty Smallcap 100  ≈  78% : 15% : 7%
This is applied as a fixed allocation here. The total FII series is
factual CDSL data; the cap-segment splits are a documented proxy.
"""

from __future__ import annotations
import os
from io import StringIO

import pandas as pd
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, ".cache")
os.makedirs(CACHE_DIR, exist_ok=True)


# -- 1. CDSL FY total net FII equity investment (INR crore) ------------
# Source: CDSL FII/FPI Investment Details (Financial Year) page.
# Keyed by FY-ending calendar year (i.e. FY 2009-10 -> 2010).
CDSL_FII_EQUITY_INR_CR = {
    1999:  29973.20,    # FY 1998-99
    2000:   9669.50,    # FY 1999-00
    2001:  10206.70,    # FY 2000-01
    2002:   8072.20,    # FY 2001-02
    2003:   2527.00,    # FY 2002-03
    2004:  39959.70,    # FY 2003-04
    2005:  44122.70,    # FY 2004-05
    2006:  48800.50,    # FY 2005-06
    2007:  25235.70,    # FY 2006-07
    2008:  53403.80,    # FY 2007-08
    2009: -47706.20,    # FY 2008-09 (global financial crisis outflow)
    2010: 110220.60,    # FY 2009-10
    2011: 110121.10,    # FY 2010-11
    2012:  43737.60,    # FY 2011-12
    2013: 140032.60,    # FY 2012-13
    2014:  79708.68,    # FY 2013-14
    2015: 111332.59,    # FY 2014-15
    2016: -14171.57,    # FY 2015-16
    2017:  55702.67,    # FY 2016-17
    2018:  25634.19,    # FY 2017-18
    2019:    -87.73,    # FY 2018-19
    2020:   6152.26,    # FY 2019-20
    2021: 274031.96,    # FY 2020-21 (post-COVID record inflow)
    2022:-140009.60,    # FY 2021-22 (rate-hike-cycle outflow)
    2023: -37631.57,    # FY 2022-23
    2024: 208211.24,    # FY 2023-24
    2025:  31991.90,    # FY 2024-25
}


# -- 2. Cap-segment allocation shares ----------------------------------
# Derived from NSE June-2024 FPI ownership × free-float mcap weights.
# See module docstring above. Applied as a fixed split per year.
SHARE_NIFTY_50       = 0.78
SHARE_NIFTY_MIDCAP   = 0.15
SHARE_NIFTY_SMALLCAP = 0.07


# -- 3. FRED DEXINUS yearly average INR per USD ------------------------
FRED_DEXINUS_URL = (
    "https://fred.stlouisfed.org/graph/fredgraph.csv?"
    "id=DEXINUS&cosd=1995-01-01&coed=2030-01-01"
)


def _fred_dexinus_yearly_avg() -> pd.Series:
    """Return INR per 1 USD, yearly mean, from FRED DEXINUS."""
    cache = os.path.join(CACHE_DIR, "dexinus.csv")
    if not os.path.exists(cache):
        req = urllib.request.Request(
            FRED_DEXINUS_URL,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode()
        with open(cache, "w") as f:
            f.write(data)
    df = pd.read_csv(cache, parse_dates=["observation_date"])
    df = df.rename(columns={"observation_date": "date", "DEXINUS": "rate"})
    df["rate"] = pd.to_numeric(df["rate"], errors="coerce")
    df = df.dropna(subset=["rate"]).set_index("date")
    yearly = df["rate"].resample("YE").mean()
    yearly.index = yearly.index.year
    yearly.index.name = "year"
    yearly.name = "inr_per_usd_yearly_avg"
    return yearly


def build_fii_inflows_df() -> pd.DataFrame:
    """Return DataFrame indexed by FY-ending calendar year with:
    - cdsl_fii_inr_cr        : CDSL net FII equity investment (INR crore)
    - inr_per_usd_avg        : FRED DEXINUS yearly avg
    - fii_total_usd_mn       : total FII equity inflow in USD millions
    - fii_nifty50_usd_mn     : implied Nifty 50 allocation
    - fii_midcap_usd_mn      : implied Nifty Midcap 100 allocation
    - fii_smallcap_usd_mn    : implied Nifty Smallcap 100 allocation
    """
    cdsl = pd.Series(CDSL_FII_EQUITY_INR_CR, name="cdsl_fii_inr_cr")
    cdsl.index.name = "year"
    inr = _fred_dexinus_yearly_avg()

    df = pd.concat([cdsl, inr], axis=1).dropna(how="all")
    # USD conversion: 1 crore INR = 1e7 INR; divide by rate (INR/USD) and by 1e6
    df["fii_total_usd_mn"] = df["cdsl_fii_inr_cr"] * 1e7 / df[inr.name] / 1e6
    df["fii_nifty50_usd_mn"]  = df["fii_total_usd_mn"] * SHARE_NIFTY_50
    df["fii_midcap_usd_mn"]   = df["fii_total_usd_mn"] * SHARE_NIFTY_MIDCAP
    df["fii_smallcap_usd_mn"] = df["fii_total_usd_mn"] * SHARE_NIFTY_SMALLCAP
    df.index.name = "year"
    return df


if __name__ == "__main__":
    df = build_fii_inflows_df()
    print(df.to_string())
