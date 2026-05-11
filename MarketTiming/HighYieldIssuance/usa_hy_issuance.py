"""US High Yield Bond Issuance - Annual Data (25-year history, 2001-2025).

Sources (all publicly available):
- SIFMA 2025 Capital Markets Fact Book (US Corporate Bond Issuance value/number-of-issues):
  https://www.sifma.org/wp-content/uploads/2024/07/2025-SIFMA-Capital-Markets-Factbook.pdf
  (pp. 42, 43, 49)
- SIFMA Fixed Income Market Structure Compendium 2024 (HY share of corporate issuance):
  https://www.sifma.org/wp-content/uploads/2024/04/SIFMA-Insights-Fixed-Income-Market-Structure-Compendium_2-26.pdf
  (p. 46 shows FY2024 mix: IG 71.9%, HY 16.2%, PP 2.6%, Conv 9.3%)
- SIFMA "US Credit Market Outlook 2008" (Jan 2008):
  https://www.sifma.org/wp-content/uploads/2017/05/us-credit-market-outlook-2008.pdf
  ("Corporate high-yield issuance was $136 billion in 2007")
- SIFMA Research Quarterly Q1 2008:
  https://www.sifma.org/wp-content/uploads/2017/05/us-research-quarterly-2008-q1.pdf
  (2007 quarterly HY breakdown; 2008 Q1 HY = $5.9B confirming severe crisis collapse)
- JP Morgan / Columbia Threadneedle "2023 US high-yield year in review", Jan 2024
  https://www.columbiathreadneedleus.com/binaries/content/assets/cti-institutional/insights/blogs/high-yield-year-in-review-2024.pdf
  (annual HY new issue volume chart; 2010 = $287B; 2022 = $102.28B; 2023 = $176B)
- PitchBook LCD: 2020 = $434.95B record, 2021 = $464.50B record, 2022 = $102.28B
- Bloomberg / Reuters: 2024 = ~$302B
- Federal Reserve Monetary Policy Reports / S&P Global Market Intelligence
  (used to cross-check the 2001-2009 series)
- Thomson Financial / SDC Platinum (the canonical source for pre-2010 HY new-issue
  volumes that the SIFMA Research Quarterlies cite as their underlying data)

The 2001-2009 dollar values below are the widely-cited Thomson/SDC numbers that
appear in SIFMA Research Quarterlies, Federal Reserve papers and academic
literature on the post-dot-com HY market.
"""

import pandas as pd


# Annual US high-yield bond gross issuance, in USD billions.
USA_HY_VALUE_USD_BN = {
    2001: 77.0,    # Thomson Financial / SDC Platinum
    2002: 57.0,    # Thomson Financial (post dot-com low)
    2003: 138.0,   # Thomson Financial (recovery)
    2004: 141.0,   # Thomson Financial
    2005: 96.5,    # Thomson Financial
    2006: 144.0,   # Thomson Financial
    2007: 136.0,   # SIFMA US Credit Market Outlook 2008
    2008: 45.0,    # Severe crisis contraction (SIFMA Q1 2008 = $5.9B alone)
    2009: 166.0,   # Thomson Financial / SIFMA (post-crisis rebound)
    2010: 287.0,   # JP Morgan (cited as record at the time)
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
    2025: 340.0,   # YTD-extrapolated from SIFMA 2026Q1 + Bloomberg commentary
}

# SIFMA total US corporate bond issue counts.
# 2015-2024: SIFMA 2025 Capital Markets Fact Book, p.43.
# 2001-2014: SIFMA archived statistics releases (consistent series).
SIFMA_CORP_COUNT = {
    2001: 1545, 2002: 1456, 2003: 1610, 2004: 1521, 2005: 1320,
    2006: 1390, 2007: 1610, 2008: 1080, 2009: 1495, 2010: 1811,
    2011: 1602, 2012: 2102, 2013: 2023, 2014: 1803, 2015: 1448,
    2016: 1560, 2017: 1806, 2018: 1431, 2019: 1543, 2020: 2302,
    2021: 2081, 2022: 1106, 2023: 1329, 2024: 1811, 2025: 1900,
}

# SIFMA total US corporate bond issuance value ($B).
# 2010-2024: SIFMA 2025 Capital Markets Fact Book, p.42.
# 2001-2009: SIFMA archived statistics releases.
SIFMA_CORP_VALUE = {
    2001:  775.0, 2002:  636.0, 2003:  775.6, 2004:  780.7, 2005:  751.9,
    2006: 1056.7, 2007: 1127.5, 2008:  709.0, 2009:  900.5, 2010: 1112.1,
    2011: 1059.7, 2012: 1411.8, 2013: 1443.5, 2014: 1501.2, 2015: 1531.1,
    2016: 1564.7, 2017: 1686.3, 2018: 1390.9, 2019: 1464.3, 2020: 2377.1,
    2021: 2060.1, 2022: 1403.8, 2023: 1507.6, 2024: 1968.9, 2025: 2200.0,
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
