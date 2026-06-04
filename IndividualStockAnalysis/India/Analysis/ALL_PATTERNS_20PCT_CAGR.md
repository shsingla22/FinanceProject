# Comprehensive Patterns for ≥ 20% Stock CAGR — Multi-Factor (BS + P&L + P/E)

**Universe:** Nifty 500 (all 500 constituents)
**CAGR target:** ≥ 20% forward stock-price compound annual growth
**Horizons:** 3 years, 5 years, 7 years
**Predictor framing:** signals are computed using BS + P&L + P/E
data through fiscal year-end T. The forward CAGR is then measured
from T → T+horizon using year-end stock prices.

**Met target**: ✅ Y = forward CAGR ≥ 20%; ❌ N = forward CAGR < 20%.

---

## Summary of all patterns at ≥ 80% hit rate

| Horizon | Signal | n | Hits ≥ 20% | Hit Rate | Avg CAGR |
|---------|--------|--:|-----------:|---------:|---------:|
| 3y | FA > 20% YoY 3yrs AND Sales CAGR > 20% AND ROCE > 20% | 13 | 11 | **84.6%** | 44.6% |
| 5y | FA > 20% YoY 3yrs AND Sales CAGR > 20% AND ROCE > 20% | 9 | 8 | **88.9%** | 42.1% |
| 5y | FA > 30% YoY for 3 yrs AND Sales CAGR > 15% | 7 | 6 | **85.7%** | 36.8% |
| 5y | FA > 20% YoY 3yrs AND Sales CAGR > 20% AND ROCE > 25% | 7 | 6 | **85.7%** | 29.6% |
| 5y | FA > 30% YoY for 3 yrs (the v6 winner; pure BS) | 11 | 9 | **81.8%** | 34.2% |
| 5y | P/E < 15 AND Sales CAGR > 15% | 90 | 73 | **81.1%** | 38.4% |
| 5y | FA > 20% YoY 3yrs AND Sales CAGR > 20% AND NP CAGR > 20% | 10 | 8 | **80.0%** | 31.5% |
| 5y | FA > 30% YoY for 3 yrs AND NP CAGR > 20% | 5 | 4 | **80.0%** | 32.2% |

---

## Horizon: 3y forward

### Pattern: FA > 20% YoY 3yrs AND Sales CAGR > 20% AND ROCE > 20%

- **Horizon**: 3y
- **CAGR target**: ≥ 20%
- **Sample size**: 13
- **Hit rate**: **84.6%** (11 of 13)
- **Avg realized CAGR**: 44.6%

| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |
|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|
| 1 | GRAVITA | (uncl.) | Mar 2020 | ₹33 | 7.0 | +143.8% | ✅ Y |
| 2 | UNOMINDA | (uncl.) | Mar 2020 | ₹120 | 42.0 | +59.0% | ✅ Y |
| 3 | DIXON | CONSUMER GOODS | Mar 2020 | ₹716 | 34.4 | +58.7% | ✅ Y |
| 4 | LAURUSLABS | PHARMA | Mar 2023 | ₹293 | 20.0 | +50.2% | ✅ Y |
| 5 | DIXON | CONSUMER GOODS | Mar 2023 | ₹2,861 | 66.7 | +50.1% | ✅ Y |
| 6 | DIXON | CONSUMER GOODS | Mar 2022 | ₹4,309 | 134.4 | +45.2% | ✅ Y |
| 7 | UNOMINDA | (uncl.) | Mar 2019 | ₹167 | 31.8 | +40.8% | ✅ Y |
| 8 | DMART | CONSUMER GOODS | Mar 2019 | ₹1,472 | 101.8 | +39.6% | ✅ Y |
| 9 | DMART | CONSUMER GOODS | Mar 2018 | ₹1,325 | 102.5 | +29.2% | ✅ Y |
| 10 | DIXON | CONSUMER GOODS | Mar 2021 | ₹3,672 | 134.6 | +26.8% | ✅ Y |
| 11 | COHANCE | (uncl.) | Mar 2022 | ₹618 | 38.3 | +23.0% | ✅ Y |
| 12 | UNOMINDA | (uncl.) | Mar 2018 | ₹177 | 30.9 | +15.3% | ❌ N |
| 13 | AFFLE | (uncl.) | Mar 2021 | ₹1,092 | 103.3 | -1.5% | ❌ N |

---

## Horizon: 5y forward

### Pattern: FA > 20% YoY 3yrs AND Sales CAGR > 20% AND ROCE > 20%

- **Horizon**: 5y
- **CAGR target**: ≥ 20%
- **Sample size**: 9
- **Hit rate**: **88.9%** (8 of 9)
- **Avg realized CAGR**: 42.1%

| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |
|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|
| 1 | GRAVITA | (uncl.) | Mar 2020 | ₹33 | 7.0 | +122.7% | ✅ Y |
| 2 | DIXON | CONSUMER GOODS | Mar 2020 | ₹716 | 34.4 | +79.1% | ✅ Y |
| 3 | UNOMINDA | (uncl.) | Mar 2020 | ₹120 | 42.0 | +48.9% | ✅ Y |
| 4 | UNOMINDA | (uncl.) | Mar 2019 | ₹167 | 31.8 | +32.6% | ✅ Y |
| 5 | DMART | CONSUMER GOODS | Mar 2019 | ₹1,472 | 101.8 | +25.2% | ✅ Y |
| 6 | UNOMINDA | (uncl.) | Mar 2018 | ₹177 | 30.9 | +22.1% | ✅ Y |
| 7 | DIXON | CONSUMER GOODS | Mar 2021 | ₹3,672 | 134.6 | +21.4% | ✅ Y |
| 8 | DMART | CONSUMER GOODS | Mar 2018 | ₹1,325 | 102.5 | +20.8% | ✅ Y |
| 9 | AFFLE | (uncl.) | Mar 2021 | ₹1,092 | 103.3 | +5.8% | ❌ N |

### Pattern: FA > 20% YoY 3yrs AND Sales CAGR > 20% AND ROCE > 25%

- **Horizon**: 5y
- **CAGR target**: ≥ 20%
- **Sample size**: 7
- **Hit rate**: **85.7%** (6 of 7)
- **Avg realized CAGR**: 29.6%

| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |
|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|
| 1 | DIXON | CONSUMER GOODS | Mar 2020 | ₹716 | 34.4 | +79.1% | ✅ Y |
| 2 | UNOMINDA | (uncl.) | Mar 2019 | ₹167 | 31.8 | +32.6% | ✅ Y |
| 3 | DMART | CONSUMER GOODS | Mar 2019 | ₹1,472 | 101.8 | +25.2% | ✅ Y |
| 4 | UNOMINDA | (uncl.) | Mar 2018 | ₹177 | 30.9 | +22.1% | ✅ Y |
| 5 | DIXON | CONSUMER GOODS | Mar 2021 | ₹3,672 | 134.6 | +21.4% | ✅ Y |
| 6 | DMART | CONSUMER GOODS | Mar 2018 | ₹1,325 | 102.5 | +20.8% | ✅ Y |
| 7 | AFFLE | (uncl.) | Mar 2021 | ₹1,092 | 103.3 | +5.8% | ❌ N |

### Pattern: FA > 30% YoY for 3 yrs AND Sales CAGR > 15%

- **Horizon**: 5y
- **CAGR target**: ≥ 20%
- **Sample size**: 7
- **Hit rate**: **85.7%** (6 of 7)
- **Avg realized CAGR**: 36.8%

| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |
|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|
| 1 | DIXON | CONSUMER GOODS | Mar 2020 | ₹716 | 34.4 | +79.1% | ✅ Y |
| 2 | UNOMINDA | (uncl.) | Mar 2020 | ₹120 | 42.0 | +48.9% | ✅ Y |
| 3 | PRESTIGE | CONSTRUCTION | Mar 2020 | ₹168 | 16.7 | +47.8% | ✅ Y |
| 4 | UNOMINDA | (uncl.) | Mar 2019 | ₹167 | 31.8 | +32.6% | ✅ Y |
| 5 | UNOMINDA | (uncl.) | Mar 2018 | ₹177 | 30.9 | +22.1% | ✅ Y |
| 6 | DIXON | CONSUMER GOODS | Mar 2021 | ₹3,672 | 134.6 | +21.4% | ✅ Y |
| 7 | AFFLE | (uncl.) | Mar 2021 | ₹1,092 | 103.3 | +5.8% | ❌ N |

### Pattern: FA > 30% YoY for 3 yrs (the v6 winner; pure BS)

- **Horizon**: 5y
- **CAGR target**: ≥ 20%
- **Sample size**: 11
- **Hit rate**: **81.8%** (9 of 11)
- **Avg realized CAGR**: 34.2%

| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |
|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|
| 1 | DIXON | CONSUMER GOODS | Mar 2020 | ₹716 | 34.4 | +79.1% | ✅ Y |
| 2 | ZENSARTECH | IT | Mar 2020 | ₹88 | 7.5 | +51.4% | ✅ Y |
| 3 | UNOMINDA | (uncl.) | Mar 2020 | ₹120 | 42.0 | +48.9% | ✅ Y |
| 4 | PRESTIGE | CONSTRUCTION | Mar 2020 | ₹168 | 16.7 | +47.8% | ✅ Y |
| 5 | PRESTIGE | CONSTRUCTION | Mar 2019 | ₹251 | 22.6 | +36.1% | ✅ Y |
| 6 | UNOMINDA | (uncl.) | Mar 2019 | ₹167 | 31.8 | +32.6% | ✅ Y |
| 7 | 360ONE | (uncl.) | Mar 2021 | ₹310 | 16.8 | +25.1% | ✅ Y |
| 8 | UNOMINDA | (uncl.) | Mar 2018 | ₹177 | 30.9 | +22.1% | ✅ Y |
| 9 | DIXON | CONSUMER GOODS | Mar 2021 | ₹3,672 | 134.6 | +21.4% | ✅ Y |
| 10 | AFFLE | (uncl.) | Mar 2021 | ₹1,092 | 103.3 | +5.8% | ❌ N |
| 11 | AJANTPHARM | PHARMA | Mar 2018 | ₹927 | 26.1 | +5.5% | ❌ N |

### Pattern: P/E < 15 AND Sales CAGR > 15%

- **Horizon**: 5y
- **CAGR target**: ≥ 20%
- **Sample size**: 90
- **Hit rate**: **81.1%** (73 of 90)
- **Avg realized CAGR**: 38.4%

| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |
|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|
| 1 | ZENTEC | (uncl.) | Mar 2020 | ₹23 | 3.0 | +130.4% | ✅ Y |
| 2 | GRAVITA | (uncl.) | Mar 2020 | ₹33 | 7.0 | +122.7% | ✅ Y |
| 3 | ACE | (uncl.) | Mar 2020 | ₹34 | 7.4 | +105.6% | ✅ Y |
| 4 | RVNL | (uncl.) | Mar 2020 | ₹13 | 3.5 | +94.0% | ✅ Y |
| 5 | SAREGAMA | (uncl.) | Mar 2020 | ₹19 | 7.5 | +93.3% | ✅ Y |
| 6 | APARINDS | (uncl.) | Mar 2020 | ₹288 | 8.2 | +80.6% | ✅ Y |
| 7 | NEWGEN | (uncl.) | Mar 2020 | ₹53 | 10.2 | +79.8% | ✅ Y |
| 8 | JSL | METALS | Mar 2019 | ₹39 | 13.2 | +77.7% | ✅ Y |
| 9 | ADANIENT | (uncl.) | Mar 2020 | ₹138 | 14.9 | +75.9% | ✅ Y |
| 10 | WELCORP | METALS | Mar 2020 | ₹62 | 2.5 | +69.6% | ✅ Y |
| 11 | PCBL | (uncl.) | Mar 2020 | ₹31 | 3.8 | +68.3% | ✅ Y |
| 12 | TITAGARH | (uncl.) | Mar 2019 | ₹70 | -28.4 | +67.3% | ✅ Y |
| 13 | APLAPOLLO | METALS | Mar 2020 | ₹125 | 13.0 | +65.0% | ✅ Y |
| 14 | JINDALSAW | METALS | Mar 2020 | ₹23 | 2.6 | +63.8% | ✅ Y |
| 15 | JINDALSTEL | METALS | Mar 2020 | ₹82 | -76.8 | +61.8% | ✅ Y |
| 16 | BLS | (uncl.) | Mar 2019 | ₹29 | 11.3 | +61.0% | ✅ Y |
| 17 | KEI | INDUSTRIAL MANUFACTURING | Mar 2020 | ₹268 | 9.4 | +60.9% | ✅ Y |
| 18 | SOBHA | CONSTRUCTION | Mar 2020 | ₹134 | 5.1 | +55.7% | ✅ Y |
| 19 | HFCL | TELECOM | Mar 2020 | ₹9 | 5.1 | +54.3% | ✅ Y |
| 20 | RVNL | (uncl.) | Mar 2021 | ₹29 | 6.1 | +53.7% | ✅ Y |
| 21 | ANGELONE | (uncl.) | Mar 2021 | ₹29 | 8.0 | +50.9% | ✅ Y |
| 22 | OLECTRA | (uncl.) | Mar 2019 | ₹253 | -127.4 | +49.4% | ✅ Y |
| 23 | CAPLIPOINT | PHARMA | Mar 2020 | ₹282 | 12.1 | +47.9% | ✅ Y |
| 24 | OIL | ENERGY | Mar 2020 | ₹55 | 1.9 | +47.7% | ✅ Y |
| 25 | POLYCAB | (uncl.) | Mar 2020 | ₹742 | 14.6 | +47.3% | ✅ Y |
| 26 | GPIL | (uncl.) | Mar 2020 | ₹26 | 11.0 | +47.1% | ✅ Y |
| 27 | SARDAEN | (uncl.) | Mar 2019 | ₹30 | 5.2 | +46.9% | ✅ Y |
| 28 | BEL | INDUSTRIAL MANUFACTURING | Mar 2019 | ₹31 | 11.9 | +45.6% | ✅ Y |
| 29 | RKFORGE | INDUSTRIAL MANUFACTURING | Mar 2019 | ₹107 | 14.6 | +45.2% | ✅ Y |
| 30 | SWANCORP | (uncl.) | Mar 2019 | ₹108 | -490.4 | +44.1% | ✅ Y |
| 31 | ADANIGREEN | ENERGY | Mar 2020 | ₹153 | -50.6 | +44.0% | ✅ Y |
| 32 | LEMONTREE | SERVICES | Mar 2020 | ₹22 | -183.3 | +42.3% | ✅ Y |
| 33 | OIL | ENERGY | Mar 2021 | ₹82 | 3.8 | +42.2% | ✅ Y |
| 34 | CHAMBLFERT | FERTILISERS & PESTICIDES | Mar 2020 | ₹108 | 3.7 | +42.0% | ✅ Y |
| 35 | SONATSOFTW | IT | Mar 2019 | ₹126 | 14.1 | +41.9% | ✅ Y |
| 36 | BLS | (uncl.) | Mar 2018 | ₹29 | 12.3 | +41.7% | ✅ Y |
| 37 | SONATSOFTW | IT | Mar 2020 | ₹62 | 6.2 | +41.2% | ✅ Y |
| 38 | IRCON | CONSTRUCTION | Mar 2019 | ₹40 | 8.3 | +40.8% | ✅ Y |
| 39 | GRASIM | CEMENT & CEMENT PRODUCTS | Mar 2020 | ₹474 | 7.3 | +40.7% | ✅ Y |
| 40 | KPIL | (uncl.) | Mar 2020 | ₹183 | 7.2 | +39.8% | ✅ Y |
| 41 | DEEPAKNTR | CHEMICALS | Mar 2020 | ₹385 | 8.6 | +38.8% | ✅ Y |
| 42 | JINDALSTEL | METALS | Mar 2019 | ₹165 | -9.7 | +38.8% | ✅ Y |
| 43 | JINDALSAW | METALS | Mar 2019 | ₹43 | 3.2 | +38.4% | ✅ Y |
| 44 | INDIGO | SERVICES | Mar 2020 | ₹1,066 | -175.6 | +36.8% | ✅ Y |
| 45 | INOXWIND | INDUSTRIAL MANUFACTURING | Mar 2021 | ₹17 | -5.4 | +34.0% | ✅ Y |
| 46 | MMTC | SERVICES | Mar 2020 | ₹12 | -6.3 | +33.5% | ✅ Y |
| 47 | GMDCLTD | METALS | Mar 2019 | ₹81 | 11.8 | +33.4% | ✅ Y |
| 48 | TECHNOE | (uncl.) | Mar 2020 | ₹238 | 14.6 | +33.3% | ✅ Y |
| 49 | IRCON | CONSTRUCTION | Mar 2020 | ₹38 | 7.4 | +32.6% | ✅ Y |
| 50 | GICRE | FINANCIAL SERVICES | Mar 2020 | ₹105 | -99.2 | +32.0% | ✅ Y |
| 51 | HFCL | TELECOM | Mar 2019 | ₹23 | 13.3 | +32.0% | ✅ Y |
| 52 | GALLANTT | (uncl.) | Mar 2019 | ₹49 | 3.8 | +31.5% | ✅ Y |
| 53 | LTTS | IT | Mar 2020 | ₹1,161 | 14.8 | +31.1% | ✅ Y |
| 54 | CAPLIPOINT | PHARMA | Mar 2021 | ₹403 | 14.2 | +30.1% | ✅ Y |
| 55 | GRANULES | PHARMA | Mar 2019 | ₹117 | 12.5 | +29.8% | ✅ Y |
| 56 | JSL | METALS | Mar 2018 | ₹79 | 11.0 | +29.8% | ✅ Y |
| 57 | HCLTECH | IT | Mar 2020 | ₹436 | 11.7 | +29.6% | ✅ Y |
| 58 | CHENNPETRO | ENERGY | Mar 2019 | ₹265 | -19.2 | +27.9% | ✅ Y |
| 59 | GRANULES | PHARMA | Mar 2020 | ₹144 | 10.9 | +27.6% | ✅ Y |
| 60 | RITES | CONSTRUCTION | Mar 2019 | ₹103 | 10.9 | +26.5% | ✅ Y |
| 61 | TATASTEEL | METALS | Mar 2019 | ₹51 | 5.6 | +25.2% | ✅ Y |
| 62 | PCBL | (uncl.) | Mar 2019 | ₹89 | 8.0 | +24.7% | ✅ Y |
| 63 | TECHNOE | (uncl.) | Mar 2019 | ₹256 | 14.9 | +24.7% | ✅ Y |
| 64 | JSWSTEEL | METALS | Mar 2019 | ₹288 | 9.1 | +23.6% | ✅ Y |
| 65 | NATIONALUM | METALS | Mar 2019 | ₹53 | 5.7 | +23.5% | ✅ Y |
| 66 | AUROPHARMA | PHARMA | Mar 2020 | ₹413 | 8.5 | +22.9% | ✅ Y |
| 67 | BALRAMCHIN | CONSUMER GOODS | Mar 2019 | ₹135 | 5.4 | +21.8% | ✅ Y |
| 68 | ENGINERSIN | CONSTRUCTION | Mar 2020 | ₹60 | 8.9 | +21.7% | ✅ Y |
| 69 | SAIL | METALS | Mar 2019 | ₹51 | 8.9 | +21.5% | ✅ Y |
| 70 | CHALET | (uncl.) | Mar 2019 | ₹339 | -915.7 | +21.1% | ✅ Y |
| 71 | HSCL | CHEMICALS | Mar 2019 | ₹116 | 15.0 | +21.1% | ✅ Y |
| 72 | NMDC | METALS | Mar 2019 | ₹26 | 5.2 | +21.0% | ✅ Y |
| 73 | JINDALSTEL | METALS | Mar 2018 | ₹219 | -15.1 | +20.0% | ✅ Y |
| 74 | POWERGRID | ENERGY | Mar 2019 | ₹112 | 10.3 | +19.9% | ❌ N |
| 75 | TITAGARH | (uncl.) | Mar 2018 | ₹110 | -8.8 | +19.1% | ❌ N |
| 76 | GRANULES | PHARMA | Mar 2021 | ₹303 | 13.7 | +15.4% | ❌ N |
| 77 | ASHOKLEY | AUTOMOBILE | Mar 2019 | ₹44 | 12.5 | +14.1% | ❌ N |
| 78 | CHAMBLFERT | FERTILISERS & PESTICIDES | Mar 2021 | ₹229 | 5.8 | +13.3% | ❌ N |
| 79 | RITES | CONSTRUCTION | Mar 2020 | ₹123 | 10.0 | +12.7% | ❌ N |
| 80 | HINDPETRO | ENERGY | Mar 2019 | ₹182 | 6.2 | +11.8% | ❌ N |
| 81 | BPCL | ENERGY | Mar 2019 | ₹193 | 10.7 | +9.3% | ❌ N |
| 82 | POWERGRID | ENERGY | Mar 2018 | ₹109 | 12.3 | +9.3% | ❌ N |
| 83 | GRAPHITE | INDUSTRIAL MANUFACTURING | Mar 2019 | ₹444 | 2.6 | +6.3% | ❌ N |
| 84 | MMTC | SERVICES | Mar 2021 | ₹42 | -8.1 | +4.2% | ❌ N |
| 85 | JUBLPHARMA | (uncl.) | Mar 2019 | ₹491 | 13.6 | +3.0% | ❌ N |
| 86 | HEG | INDUSTRIAL MANUFACTURING | Mar 2019 | ₹424 | 2.7 | -2.7% | ❌ N |
| 87 | JMFINANCIL | FINANCIAL SERVICES | Mar 2019 | ₹94 | 13.8 | -4.5% | ❌ N |
| 88 | ADANIGREEN | ENERGY | Mar 2021 | ₹1,105 | -7365.7 | -6.1% | ❌ N |
| 89 | GRAPHITE | INDUSTRIAL MANUFACTURING | Mar 2018 | ₹726 | 13.8 | -18.4% | ❌ N |
| 90 | HEG | INDUSTRIAL MANUFACTURING | Mar 2018 | ₹637 | 11.6 | -22.0% | ❌ N |

### Pattern: FA > 20% YoY 3yrs AND Sales CAGR > 20% AND NP CAGR > 20%

- **Horizon**: 5y
- **CAGR target**: ≥ 20%
- **Sample size**: 10
- **Hit rate**: **80.0%** (8 of 10)
- **Avg realized CAGR**: 31.5%

| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |
|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|
| 1 | DIXON | CONSUMER GOODS | Mar 2020 | ₹716 | 34.4 | +79.1% | ✅ Y |
| 2 | GRAVITA | (uncl.) | Mar 2019 | ₹82 | 36.4 | +64.9% | ✅ Y |
| 3 | UNOMINDA | (uncl.) | Mar 2019 | ₹167 | 31.8 | +32.6% | ✅ Y |
| 4 | HCLTECH | IT | Mar 2020 | ₹436 | 11.7 | +29.6% | ✅ Y |
| 5 | DMART | CONSUMER GOODS | Mar 2019 | ₹1,472 | 101.8 | +25.2% | ✅ Y |
| 6 | UNOMINDA | (uncl.) | Mar 2018 | ₹177 | 30.9 | +22.1% | ✅ Y |
| 7 | DIXON | CONSUMER GOODS | Mar 2021 | ₹3,672 | 134.6 | +21.4% | ✅ Y |
| 8 | DMART | CONSUMER GOODS | Mar 2018 | ₹1,325 | 102.5 | +20.8% | ✅ Y |
| 9 | DMART | CONSUMER GOODS | Mar 2020 | ₹2,188 | 108.9 | +13.3% | ❌ N |
| 10 | AFFLE | (uncl.) | Mar 2021 | ₹1,092 | 103.3 | +5.8% | ❌ N |

### Pattern: FA > 30% YoY for 3 yrs AND NP CAGR > 20%

- **Horizon**: 5y
- **CAGR target**: ≥ 20%
- **Sample size**: 5
- **Hit rate**: **80.0%** (4 of 5)
- **Avg realized CAGR**: 32.2%

| # | NSE Symbol | Industry | Base Year (T) | Price | P/E | Forward CAGR | Met ≥20%? |
|--:|-----------|----------|---------------|------:|----:|-------------:|:----------|
| 1 | DIXON | CONSUMER GOODS | Mar 2020 | ₹716 | 34.4 | +79.1% | ✅ Y |
| 2 | UNOMINDA | (uncl.) | Mar 2019 | ₹167 | 31.8 | +32.6% | ✅ Y |
| 3 | UNOMINDA | (uncl.) | Mar 2018 | ₹177 | 30.9 | +22.1% | ✅ Y |
| 4 | DIXON | CONSUMER GOODS | Mar 2021 | ₹3,672 | 134.6 | +21.4% | ✅ Y |
| 5 | AFFLE | (uncl.) | Mar 2021 | ₹1,092 | 103.3 | +5.8% | ❌ N |

---

## Key insights from this analysis

### 1. The winning multi-factor signal

**`FA > 20% YoY for 3 yrs AND Sales CAGR > 20% AND ROCE > 20%`** is the
single best signal found in this study:

- **5y horizon: 88.9% hit rate** (8 of 9) at CAGR ≥ 20%, avg realized 42.1%
- **3y horizon: 84.6% hit rate** (11 of 13) at CAGR ≥ 20%, avg realized 44.6%

Adding the P&L overlay (Sales CAGR > 20%) and quality overlay (ROCE > 20%)
to the v6 pure-BS winner (FA > 30% YoY × 3 yrs) lifts the hit rate from
**81.8% → 88.9%** on the 5y horizon — a meaningful improvement.

### 2. The biggest, simplest signal — valuation + sales growth

**`P/E < 15 AND Sales CAGR > 15%`** at the 5y horizon has the largest
sample (n = 90) at 81.1% hit rate.

### 3. Horizon

| Horizon | # patterns at ≥ 80% hit rate |
|---------|---------------------------:|
| 3y | 1 |
| 5y | 7 |
| 7y | 0 |

The **5-year horizon is the sweet spot**.

---

## Reproducibility

Re-run with: `python3 run_analysis_v7_multi_factor.py`

Inputs (under each domain's `Nifty500/` subfolder):
- `../BalanceSheet/Nifty500/_all_balance_sheets_long.csv`
- `../ProfitStatement/Nifty500/_all_profit_loss_long.csv`
- `../StockInfo/Nifty500/_all_stock_info_long.csv`

