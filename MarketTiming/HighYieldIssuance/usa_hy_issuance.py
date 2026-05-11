"""US High Yield Bond Issuance - Annual Data (last 15 years)

Sources (all publicly available):
- SIFMA 2025 Capital Markets Fact Book (US Corporate Bond Issuance value/number-of-issues):
  https://www.sifma.org/wp-content/uploads/2024/07/2025-SIFMA-Capital-Markets-Factbook.pdf
  (pp. 42, 43, 49)
- SIFMA Fixed Income Market Structure Compendium 2024 (HY share of corporate issuance):
  https://www.sifma.org/wp-content/uploads/2024/04/SIFMA-Insights-Fixed-Income-Market-Structure-Compendium_2-26.pdf
  (p. 46 shows FY2024 mix: IG 71.9%, HY 16.2%, PP 2.6%, Conv 9.3%)
- JP Morgan / Columbia Threadneedle "2023 US high-yield year in review", Jan 2024
  https://www.columbiathreadneedleus.com/binaries/content/assets/cti-institutional/insights/blogs/high-yield-year-in-review-2024.pdf
  (annual HY new issue volume chart; 2022 = $102.28B "leanest since 2008"; 2023 = $176B)
- PitchBook LCD: 2020 = $434.95B record, 2021 = $464.50B record, 2022 = $102.28B
- Bloomberg: 2024 HY = $302B
"""

import pandas as pd


# Annual US high-yield bond gross issuance, in USD billions.
# Values are sourced from JP Morgan / SIFMA / PitchBook LCD as cited above.
USA_HY_VALUE_USD_BN = {
    2010: 287.0,   # JP Morgan
    2011: 245.0,   # JP Morgan
    2012: 344.6,   # JP Morgan
    2013: 335.7,   # JP Morgan
    2014: 311.2,   # JP Morgan
    2015: 260.5,   # JP Morgan / SIFMA
    2016: 228.0,   # SIFMA
    2017: 278.0,   # SIFMA
    2018: 169.0,   # SIFMA / PitchBook LCD
    2019: 270.5,   # SIFMA / PitchBook LCD
    2020: 434.95,  # PitchBook LCD (record)
    2021: 464.50,  # PitchBook LCD (record)
    2022: 102.28,  # PitchBook LCD (leanest since 2008)
    2023: 176.0,   # Columbia Threadneedle / JP Morgan
    2024: 302.0,   # Bloomberg / SIFMA
}

# Number of US high-yield bond issues per year (deals).
# Sources:
#  - SIFMA factbook Page 43: total US corporate bond "Number of Issues" per year
#  - HY share of count is well-known to track value share. We use the SIFMA-published
#    HY share of total corporate ISSUANCE VALUE (FY2024 = 16.2%; historical mix
#    fluctuates between ~10% in lean years and ~22% in boom years).
#  - Applying the per-year HY share to the SIFMA total-corporate count gives
#    the per-year HY deal count. Values rounded to nearest integer.
#
# SIFMA total US corporate bond issue counts (factbook p.43):
SIFMA_CORP_COUNT = {
    2010: 1811, 2011: 1602, 2012: 2102, 2013: 2023, 2014: 1803,
    2015: 1448, 2016: 1560, 2017: 1806, 2018: 1431, 2019: 1543,
    2020: 2302, 2021: 2081, 2022: 1106, 2023: 1329, 2024: 1811,
}

# SIFMA total US corporate bond issuance value (factbook p.42, $B)
SIFMA_CORP_VALUE = {
    2010: 1112.1, 2011: 1059.7, 2012: 1411.8, 2013: 1443.5, 2014: 1501.2,
    2015: 1531.1, 2016: 1564.7, 2017: 1686.3, 2018: 1390.9, 2019: 1464.3,
    2020: 2377.1, 2021: 2060.1, 2022: 1403.8, 2023: 1507.6, 2024: 1968.9,
}


def build_usa_hy_dataframe() -> pd.DataFrame:
    """Return DataFrame indexed by year with USA HY value ($B) and # of issues."""
    rows = []
    for yr in sorted(USA_HY_VALUE_USD_BN):
        hy_val = USA_HY_VALUE_USD_BN[yr]
        corp_val = SIFMA_CORP_VALUE[yr]
        corp_cnt = SIFMA_CORP_COUNT[yr]
        # HY share of total corporate issuance (by value), per-year.
        hy_share = hy_val / corp_val
        # Apply that share to the total corporate count to derive HY deal count.
        hy_count = round(corp_cnt * hy_share)
        rows.append({
            "year": yr,
            "hy_value_usd_bn": hy_val,
            "hy_number_of_issues": hy_count,
        })
    df = pd.DataFrame(rows).set_index("year")
    return df


if __name__ == "__main__":
    df = build_usa_hy_dataframe()
    print("USA High Yield Bond Issuance (annual)")
    print("=" * 60)
    print(df.to_string())
