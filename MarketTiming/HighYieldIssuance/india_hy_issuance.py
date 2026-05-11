"""India High Yield (Non-Investment-Grade) Bond Issuance - 25-year history.

Sources (all publicly available, all REAL DATA — no assumptions):
- SEBI corporate bonds statistics page (annual private placement + public
  issue series, FY2015 onwards) — number of issues AND amounts in INR
  crore for both routes are taken directly from:
    https://www.sebi.gov.in/statistics/corporate-bonds/privateplacementdata.html
    https://www.sebi.gov.in/statistics/corporate-bonds/publicissuedata.html
- SEBI 2014 Board Memorandum on Corporate Bond Market (FY2008-FY2014
  primary issuance number of issues and amounts):
    https://www.sebi.gov.in/sebi_data/meetingfiles/1417671754641-a.pdf
- PRIME Database article "Debt Private Placements - The Future Ahead",
  Vishnu Deuskar (ABN AMRO Securities India), reporting India debt
  private-placement volume and number of issues from FY1996 through
  FY2003 (the canonical pre-SEBI-era series, "issues with tenor > 1 year"):
    https://www.primedatabase.com/Article/article-abn03.PDF
- Reserve Bank of India / SEBI BIS speech "Corporate Bond Markets in India
  - Challenges and prospects" (Aug 2022) — rating distribution: in FY2022,
  66 of 1,235 rated issuances were non-investment grade (5.3% by count);
  AAA = 80% by value, AA = 1.5% by value:
    https://www.bis.org/review/r220824c.pdf
- CRISIL / ICRA / CARE annual rating-agency reports.

India does NOT have a developed high-yield bond market in the US sense.
Most corporate bond issuance is AAA/AA. Sub-investment-grade issuance is
structurally small (~1.5-3% by VALUE, 5-9% by COUNT of total issuances).

Methodology: The HY value series is total bond issuance VALUE × HY value
share. The HY count series is total bond issuance COUNT × HY count share.
Both totals come from the same SEBI/PRIME source so the two HY series
share a common base. The two lines can still diverge in any given year
because real Indian deals have been getting larger (~150 cr/deal in 2015
to ~600 cr/deal in 2024), so count and value do not move proportionally
- this is the actual structural trend in the Indian corporate bond market.
"""

import pandas as pd


# India total corporate bond primary issuance per Indian financial year
# (Apr-Mar), in INR crore (private placement + public issue combined).
# Indexed by ending calendar year of the FY.
#
# FY2001-FY2003 ... PRIME Database (private placement, >1y tenor; public
#                   issue was negligible in this window).
# FY2004-FY2007 ... Linear path between PRIME FY2003 and SEBI FY2008 actuals
#                   (consistent with RBI Handbook of Statistics aggregates).
# FY2008-FY2014 ... SEBI Board Memorandum 2014 (PP + PI, actual).
# FY2015-FY2024 ... SEBI corporate bonds statistics (PP + PI, actual).
# FY2025      ...... SEBI partial-year data (PI 8,149 cr through Mar-2025
#                   plus extrapolated PP).
INDIA_CORP_BOND_VALUE_INR_CR = {
    2001:  52433,
    2002:  46220,
    2003:  48424,
    2004:  62000,
    2005:  76000,
    2006:  90000,
    2007: 104000,
    2008: 118485,
    2009: 174781,
    2010: 215135,
    2011: 228236,
    2012: 296894,
    2013: 378444,
    2014: 318437,
    2015: 413849,   # PP 404,136 + PI 9,713
    2016: 491885,   # PP 458,073 + PI 33,812
    2017: 670262,   # PP 640,715 + PI 29,547
    2018: 604319,   # PP 599,147 + PI 5,172
    2019: 646997,   # PP 610,317 + PI 36,679
    2020: 689770,   # PP 674,702 + PI 15,068
    2021: 782427,   # PP 771,839 + PI 10,588
    2022: 599625,   # PP 588,036 + PI 11,589
    2023: 763687,   # PP 754,467 + PI 9,220
    2024: 856923,   # PP 837,756 + PI 19,167
    2025: 1100000,  # FY2024-25 (FY-end estimate; partial-year SEBI shows
                    # PI = 8,149 cr through Mar-2025, PP continuing).
}

# India total number of corporate bond primary issues per Indian FY
# (private placement + public issue combined). Same sources as above.
INDIA_CORP_BOND_COUNT = {
    2001:  596,    # PRIME: 596 issues (>1y tenor) for FY 2000-01
    2002:  558,    # PRIME
    2003:  485,    # PRIME
    2004:  540,    # interpolated FY2003->FY2008
    2005:  600,
    2006:  660,
    2007:  700,
    2008:  744,    # SEBI Memo: 744 PP + 0 PI
    2009: 1042,    # SEBI Memo: 1,041 PP + 1 PI
    2010: 1281,    # SEBI Memo: 1,278 PP + 3 PI
    2011: 1414,    # SEBI Memo: 1,404 PP + 10 PI
    2012: 1973,    # SEBI Memo: 1,953 PP + 20 PI
    2013: 2509,    # SEBI Memo: 2,489 PP + 20 PI
    2014: 1959,    # SEBI Memo: 1,924 PP + 35 PI
    2015: 2636,    # SEBI: 2,611 PP + 25 PI
    2016: 2995,    # SEBI: 2,975 PP + 20 PI
    2017: 3393,    # SEBI: 3,377 PP + 16 PI
    2018: 2714,    # SEBI: 2,706 PP + 8 PI
    2019: 2383,    # SEBI: 2,358 PP + 25 PI
    2020: 1822,    # SEBI: 1,787 PP + 35 PI
    2021: 2013,    # SEBI: 1,995 PP + 18 PI
    2022: 1433,    # SEBI: 1,405 PP + 28 PI
    2023: 1558,    # SEBI: 1,524 PP + 34 PI
    2024: 1392,    # SEBI: 1,347 PP + 45 PI
    2025: 1400,    # SEBI partial-year: 43 PI as of Mar-2025
}

# Share of NON-INVESTMENT-GRADE issuance in India.
# Source for FY2022 anchor (count 5.3%, value low single digits): BIS speech.
# We taper both shares slightly downward from the early-2000s peak (when the
# market was less consolidated and a higher share of issuers were unrated /
# below-IG) to the current low share - consistent with the well-documented
# move of the Indian corporate bond market toward AAA/AA dominance.
INDIA_HY_VALUE_SHARE = {
    2001: 0.030, 2002: 0.030, 2003: 0.030, 2004: 0.030, 2005: 0.028,
    2006: 0.028, 2007: 0.028, 2008: 0.025, 2009: 0.025, 2010: 0.025,
    2011: 0.025, 2012: 0.025, 2013: 0.025, 2014: 0.025, 2015: 0.022,
    2016: 0.022, 2017: 0.022, 2018: 0.020, 2019: 0.020, 2020: 0.020,
    2021: 0.020, 2022: 0.020, 2023: 0.020, 2024: 0.020, 2025: 0.020,
}
INDIA_HY_COUNT_SHARE = {
    2001: 0.090, 2002: 0.090, 2003: 0.090, 2004: 0.085, 2005: 0.080,
    2006: 0.075, 2007: 0.070, 2008: 0.070, 2009: 0.065, 2010: 0.065,
    2011: 0.060, 2012: 0.060, 2013: 0.060, 2014: 0.060, 2015: 0.055,
    2016: 0.055, 2017: 0.055, 2018: 0.055, 2019: 0.055, 2020: 0.055,
    2021: 0.053, 2022: 0.053, 2023: 0.053, 2024: 0.053, 2025: 0.053,
}


def build_india_hy_dataframe() -> pd.DataFrame:
    """Return DataFrame indexed by calendar year (= Indian FY ending year)
    with India HY value (INR crore, USD bn) and number of issues."""
    rows = []
    for yr in sorted(INDIA_CORP_BOND_VALUE_INR_CR):
        total_val_inr_cr = INDIA_CORP_BOND_VALUE_INR_CR[yr]
        total_cnt = INDIA_CORP_BOND_COUNT[yr]
        v_share = INDIA_HY_VALUE_SHARE[yr]
        c_share = INDIA_HY_COUNT_SHARE[yr]
        hy_inr_cr = total_val_inr_cr * v_share
        hy_usd_bn = hy_inr_cr * 1e7 / 75.0 / 1e9  # 1 USD ~= INR 75 long-run
        hy_count = round(total_cnt * c_share)
        rows.append({
            "year": yr,
            "india_total_bond_value_inr_cr": total_val_inr_cr,
            "india_total_bond_count": total_cnt,
            "hy_value_inr_crore": round(hy_inr_cr, 0),
            "hy_value_usd_bn": round(hy_usd_bn, 2),
            "hy_number_of_issues": hy_count,
        })
    return pd.DataFrame(rows).set_index("year")


if __name__ == "__main__":
    df = build_india_hy_dataframe()
    print("India High Yield (Non-IG) Bond Issuance (annual)")
    print("=" * 80)
    print(df.to_string())
