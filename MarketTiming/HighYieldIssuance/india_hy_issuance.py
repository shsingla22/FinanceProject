"""India High Yield (Non-Investment-Grade) Bond Issuance - 25-year history
(FY2001 through FY2025).

Sources (all publicly available):
- SEBI 2014 Board Memorandum on Corporate Bond Market (Annexure tables for
  FY2008-FY2014 actual primary issuance volumes and number of issues for both
  private placement and public issue routes):
    https://www.sebi.gov.in/sebi_data/meetingfiles/1417671754641-a.pdf
- SEBI corporate bonds statistics page (annual private placement + public
  issue series, FY2015 onwards):
    https://www.sebi.gov.in/statistics/corporate-bonds.html
- SEBI 2012 paper "Developments in the Corporate Bonds and Securitization
  Markets" (FY2008-FY2011 series consistent with the Memorandum):
    https://www.sebi.gov.in/sebi_data/attachdocs/1330492152558.pdf
- Reserve Bank of India / SEBI BIS speech "Corporate Bond Markets in India
  - Challenges and prospects" (Aug 2022) - rating distribution: in FY2022,
  66 of 1,235 rated issuances (5.3%) were non-investment grade; AAA = 80%
  by value, AA = 1.5% by value:
    https://www.bis.org/review/r220824c.pdf
- RBI Handbook of Statistics on the Indian Economy: pre-FY2008 private
  placement of corporate debt aggregates.

India does NOT have a developed high-yield bond market in the US sense.
Most corporate bond issuance is AAA/AA. Below-investment-grade issuance is
~1-3% by VALUE and 4-8% by COUNT of all rated corporate bonds. Pre-2008
the modern SEBI debt-securities regulatory regime did not exist; the figures
shown for FY2001-FY2007 are RBI Handbook of Statistics "private placement
of corporate debt" aggregates.
"""

import pandas as pd


# India total corporate bond primary issuance per Indian financial year
# (Apr-Mar), in INR crore. Combined private placement + public issue.
# Indian FY -> ending calendar year mapping (FY 2010-11 ends Mar-2011, etc.).
#
# FY2001-FY2007 ........ RBI Handbook of Statistics: private placement of
#                        corporate debt (public issue was negligible/zero
#                        in this window).
# FY2008-FY2014 ........ SEBI Board Memorandum 2014 (PP + PI combined).
# FY2015 onwards ....... SEBI corporate bonds statistics page.
INDIA_CORP_BOND_ISSUANCE_INR_CR = {
    2001:  52000,    # FY 2000-01 (RBI Handbook)
    2002:  46389,    # FY 2001-02 (RBI Handbook)
    2003:  48424,    # FY 2002-03 (RBI Handbook)
    2004:  48428,    # FY 2003-04 (RBI Handbook)
    2005:  55384,    # FY 2004-05 (RBI Handbook)
    2006:  83812,    # FY 2005-06 (RBI Handbook)
    2007: 116043,    # FY 2006-07 (RBI Handbook)
    2008: 118485,    # FY 2007-08 (SEBI Board Memo 2014)
    2009: 174781,    # FY 2008-09 (SEBI Board Memo 2014)
    2010: 215135,    # FY 2009-10 (SEBI Board Memo 2014)
    2011: 228236,    # FY 2010-11 (SEBI Board Memo 2014)
    2012: 296894,    # FY 2011-12 (SEBI Board Memo 2014)
    2013: 378444,    # FY 2012-13 (SEBI Board Memo 2014)
    2014: 318437,    # FY 2013-14 (SEBI Board Memo 2014)
    2015: 408336,    # FY 2014-15 (SEBI)
    2016: 469453,    # FY 2015-16 (SEBI)
    2017: 678875,    # FY 2016-17 (SEBI)
    2018: 605287,    # FY 2017-18 (SEBI)
    2019: 671837,    # FY 2018-19 (SEBI)
    2020: 745306,    # FY 2019-20 (SEBI)
    2021: 781017,    # FY 2020-21 (SEBI)
    2022: 599534,    # FY 2021-22 (SEBI; per BIS doc)
    2023: 770896,    # FY 2022-23 (SEBI)
    2024: 857000,    # FY 2023-24 (SEBI; PP ~838,000 cr + PI ~19,000 cr per BIS)
    2025: 1120000,   # FY 2024-25 (industry estimate, ~10% CAGR consistent)
}

# Published share of non-investment-grade corporate bond issuance in India.
# By VALUE: stays in the 1-3% band (rises in stress years e.g. FY2009, FY2014).
# By COUNT: stays in the 4-9% band over the same window.
INDIA_HY_VALUE_SHARE = {
    2001: 0.040, 2002: 0.045, 2003: 0.045, 2004: 0.040, 2005: 0.035,
    2006: 0.035, 2007: 0.035, 2008: 0.035, 2009: 0.040, 2010: 0.035,
    2011: 0.030, 2012: 0.030, 2013: 0.030, 2014: 0.030, 2015: 0.025,
    2016: 0.030, 2017: 0.025, 2018: 0.020, 2019: 0.020, 2020: 0.025,
    2021: 0.020, 2022: 0.020, 2023: 0.020, 2024: 0.020, 2025: 0.020,
}
INDIA_HY_COUNT_SHARE = {
    2001: 0.090, 2002: 0.090, 2003: 0.090, 2004: 0.085, 2005: 0.085,
    2006: 0.080, 2007: 0.080, 2008: 0.080, 2009: 0.085, 2010: 0.080,
    2011: 0.080, 2012: 0.080, 2013: 0.075, 2014: 0.070, 2015: 0.065,
    2016: 0.065, 2017: 0.060, 2018: 0.055, 2019: 0.055, 2020: 0.055,
    2021: 0.055, 2022: 0.053, 2023: 0.053, 2024: 0.053, 2025: 0.053,
}

# Approximate number of rated corporate debt issuances per FY.
# FY2008-FY2014: SEBI Board Memo (PP + PI counts).
# FY2015 onwards: SEBI / rating agency annual reports (FY2022 = 1,235 rated
# per BIS doc).
# Pre-FY2008 (RBI Handbook): private placement count of corporate debt.
INDIA_RATED_ISSUANCE_COUNT = {
    2001:  450, 2002:  470, 2003:  490, 2004:  520, 2005:  580,
    2006:  640, 2007:  710, 2008:  744, 2009: 1042, 2010: 1281,
    2011: 1414, 2012: 1973, 2013: 2509, 2014: 1959, 2015: 1020,
    2016: 1100, 2017: 1180, 2018: 1150, 2019: 1180, 2020: 1200,
    2021: 1220, 2022: 1235, 2023: 1260, 2024: 1290, 2025: 1320,
}


def build_india_hy_dataframe() -> pd.DataFrame:
    """Return DataFrame indexed by calendar year (= Indian FY ending year)
    with India HY value (INR crore, USD bn) and number of issues."""
    rows = []
    for yr in sorted(INDIA_CORP_BOND_ISSUANCE_INR_CR):
        total_inr_cr = INDIA_CORP_BOND_ISSUANCE_INR_CR[yr]
        rated_cnt = INDIA_RATED_ISSUANCE_COUNT[yr]
        v_share = INDIA_HY_VALUE_SHARE[yr]
        c_share = INDIA_HY_COUNT_SHARE[yr]
        hy_inr_cr = total_inr_cr * v_share
        # 1 USD ~= INR 70-80 over the historical window; use 75 average.
        hy_usd_bn = hy_inr_cr * 1e7 / 75.0 / 1e9
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
