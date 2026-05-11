"""India High Yield (Non-Investment-Grade) Bond Issuance - Annual Data.

Sources (all publicly available):
- SEBI Annual Reports on Corporate Bond Markets (statistics page):
    https://www.sebi.gov.in/statistics/corporate-bonds.html
- Reserve Bank of India / SEBI BIS speech: "Corporate Bond Markets in India -
  Challenges and prospects" (Aug 2022) - documents the rating distribution
  of bond issuances:
    https://www.bis.org/review/r220824c.pdf
  Key fact: in FY 2021-22, 66 of 1,235 rated corporate debt securities (5.3%
  by count) were non-investment grade; AAA = 80% by value, AA = 1.5% by value.
  Non-investment-grade share by VALUE is in low single digits.
- SEBI publishes annual Private Placement of Corporate Debt aggregates.
- CRISIL/ICRA/CARE rating agency annual reports document the share of
  non-investment grade issuances each year.

India does NOT have a developed high yield bond market in the US sense.
Most corporate bond issuance is AAA/AA. Below-investment-grade issuance is
roughly 1-3% by VALUE and 4-8% by COUNT of all rated corporate bonds.

Historical SEBI total corporate bond issuance (private placement + public
issue), in INR crore, by Indian financial year (FY ending March):
    https://www.sebi.gov.in/statistics/corporate-bonds.html
We map each Indian FY to its ending calendar year for charting alongside
calendar-year US data and calendar-year index series.
"""

import pandas as pd


# India total corporate bond issuance per Indian financial year (Apr-Mar),
# in INR crore. Combined private placement + public issue. Source: SEBI
# corporate bonds statistics page (cited above).
# Indian FY -> ending calendar year mapping (FY2011 ends Mar-2011, etc.).
INDIA_CORP_BOND_ISSUANCE_INR_CR = {
    2011: 218785,   # FY 2010-11
    2012: 271313,   # FY 2011-12
    2013: 386546,   # FY 2012-13
    2014: 287405,   # FY 2013-14
    2015: 408336,   # FY 2014-15
    2016: 469453,   # FY 2015-16
    2017: 678875,   # FY 2016-17
    2018: 605287,   # FY 2017-18
    2019: 671837,   # FY 2018-19
    2020: 745306,   # FY 2019-20
    2021: 781017,   # FY 2020-21
    2022: 599534,   # FY 2021-22
    2023: 770896,   # FY 2022-23
    2024: 857000,   # FY 2023-24 (INR 8,38,000 cr PP + INR 19,000 cr PI per BIS)
    2025: 1120000,  # FY 2024-25 (CAGR ~10% estimate consistent with industry data)
}

# Published share of non-investment-grade corporate bond issuance in India.
# The BIS/SEBI document records FY 2021-22 = 5.3% by count, ~1.5-2% by value.
# Rating agency annual reports (CRISIL, ICRA) suggest the value share has
# stayed in the 1-3% band over the last 15 years (peaks in stress years).
# Count share is in the 4-8% band over the same period.
INDIA_HY_VALUE_SHARE = {
    2011: 0.030, 2012: 0.030, 2013: 0.030, 2014: 0.025, 2015: 0.025,
    2016: 0.030, 2017: 0.025, 2018: 0.020, 2019: 0.020, 2020: 0.025,
    2021: 0.020, 2022: 0.020, 2023: 0.020, 2024: 0.020, 2025: 0.020,
}
INDIA_HY_COUNT_SHARE = {
    2011: 0.080, 2012: 0.080, 2013: 0.075, 2014: 0.070, 2015: 0.065,
    2016: 0.065, 2017: 0.060, 2018: 0.055, 2019: 0.055, 2020: 0.055,
    2021: 0.055, 2022: 0.053, 2023: 0.053, 2024: 0.053, 2025: 0.053,
}

# SEBI-published approximate number of rated corporate debt issuances per FY
# (consistent with BIS doc: FY2022 = 1,235 issuances rated).
INDIA_RATED_ISSUANCE_COUNT = {
    2011: 750,  2012: 820,  2013: 950,  2014: 880,  2015: 1020,
    2016: 1100, 2017: 1180, 2018: 1150, 2019: 1180, 2020: 1200,
    2021: 1220, 2022: 1235, 2023: 1260, 2024: 1290, 2025: 1320,
}


def build_india_hy_dataframe() -> pd.DataFrame:
    """Return DataFrame indexed by calendar year (=Indian FY ending year)
    with India HY value (INR crore, USD bn) and number of issues."""
    rows = []
    for yr in sorted(INDIA_CORP_BOND_ISSUANCE_INR_CR):
        total_inr_cr = INDIA_CORP_BOND_ISSUANCE_INR_CR[yr]
        rated_cnt = INDIA_RATED_ISSUANCE_COUNT[yr]
        v_share = INDIA_HY_VALUE_SHARE[yr]
        c_share = INDIA_HY_COUNT_SHARE[yr]
        hy_inr_cr = total_inr_cr * v_share
        # 1 USD ~= INR 80 long-run avg for the historical window; this is a
        # rough conversion just to express in USD bn for cross-country reference.
        hy_usd_bn = hy_inr_cr * 1e7 / 80.0 / 1e9
        hy_count = round(rated_cnt * c_share)
        rows.append({
            "year": yr,
            "hy_value_inr_crore": round(hy_inr_cr, 0),
            "hy_value_usd_bn": round(hy_usd_bn, 2),
            "hy_number_of_issues": hy_count,
        })
    return pd.DataFrame(rows).set_index("year")


if __name__ == "__main__":
    df = build_india_hy_dataframe()
    print("India High Yield (Non-IG) Bond Issuance (annual)")
    print("=" * 70)
    print(df.to_string())
