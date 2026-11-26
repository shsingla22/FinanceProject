# Management change — evaluation

*Run 2026-11-26 · window 2025-11-26 → 2026-11-26.* Each check compares the skill's list with something its own detector did not decide. An exception a person has read and explained (`evals/reviewed_exceptions.csv`) is shown with the note.

| Check | Result |
|---|---|
| E1 Coverage — management / takeover filings read | 8,102 of 8,493 (95.4%) |
| E2 Ownership vs NSE shareholding register | 64 major promoter moves; 64 carry a verdict; 0 read as no change (0 not yet reviewed) |
| E3 Open-offer filings | 7 companies; 7 read as a change of control; 0 others not yet reviewed |
| E4 Call rosters | 109 seats whose listed holder changed; 78 reported; 31 not (31 not yet reviewed) |
| E5 Headlines naming a CEO / MD / CFO | 261 company-seats; 222 reported; 39 not (39 not yet reviewed) |
| E6 Management filings whose PDF gave no text | 30 at 27 companies; 1 name a seat in the headline (covered by E5) |
| E7 Hand-labelled filings (48) | mechanical flag: recall 100.0%, precision 45.8% (tp 11, fp 13, fn 0, tn 24); final list: 11 of 11 labelled changes found |
| E8 Names and quotes found in the documents | 387 of 399 seat changes, 107 of 110 ownership changes (97.1%); 0 judge failures |

**Hard failures:** none.

## E1 — coverage by category

| Category | Read | No text | Failed | Skipped (size) | Other |
|---|---:|---:|---:|---:|---:|
| Acquisition | 1 | 0 | 0 | 0 | 0 |
| Agreements | 1 | 0 | 0 | 0 | 0 |
| Allotment of Securities | 1 | 0 | 0 | 0 | 0 |
| Appointment | 1394 | 2 | 0 | 0 | 0 |
| Awarding of order(s)/contract(s) | 1 | 0 | 0 | 0 | 0 |
| Cessation | 470 | 0 | 0 | 0 | 0 |
| Change in Company Secretary/Compliance Officer | 5 | 0 | 0 | 0 | 0 |
| Change in Director(s) | 782 | 0 | 0 | 0 | 0 |
| Change in Management | 1382 | 1 | 0 | 0 | 0 |
| Corporate Insolvency Resolution Process | 1 | 0 | 0 | 0 | 0 |
| Disclosure under SEBI Takeover Regulations | 1085 | 361 | 0 | 0 | 0 |
| General Updates | 336 | 2 | 5 | 2 | 0 |
| Incorporation | 1 | 0 | 0 | 0 | 0 |
| Issue of Securities | 2 | 0 | 0 | 0 | 0 |
| Offer for sale | 3 | 0 | 0 | 0 | 0 |
| Open Offer | 2 | 0 | 0 | 1 | 0 |
| Outcome of Board Meeting | 1110 | 8 | 1 | 1 | 0 |
| Press Release | 67 | 0 | 2 | 0 | 0 |
| Public Announcement-Open Offer | 7 | 0 | 0 | 0 | 0 |
| Record Date | 2 | 0 | 0 | 0 | 0 |
| Resignation | 510 | 0 | 0 | 0 | 0 |
| Resignation of Director/KMP/SMP | 556 | 0 | 1 | 0 | 0 |
| Resignation of Independent director | 33 | 0 | 0 | 0 | 0 |
| Retirement | 119 | 0 | 0 | 0 | 0 |
| Shareholders meeting | 10 | 0 | 0 | 0 | 0 |
| Updates | 221 | 3 | 1 | 0 | 0 |

## E2 — every major move in the promoter holding

| Company | Promoter holding | Change | Crossed | Verdict | What the skill read | Reviewed |
|---|---|---:|---|---|---|---|
| **RBLBANK** | 0.0% (2025-09-30) → 59.88% (2026-09-30) | +59.88 | above 50%, above 25%, from nil | change_of_control | Emirates NBD Bank (P.J.S.C.) subscribed to 92,91,34,820 new shares at INR 280 (INR 26,015.77 crore) on 18 June 2026, taking 60% of RBL Bank's expanded capital, and compl… | — |
| **SAMMAANCAP** | 0.0% (2025-09-30) → 33.32% (2026-10-30) | +33.32 | above 25%, from nil | change_of_control | Avenir Investment RSC Ltd, owned and controlled by International Holding Company PJSC (IHC), Abu Dhabi, subscribed to a Rs 8,850 crore preferential issue of shares and w… | — |
| **RBA** | 11.27% (2025-09-30) → 41.73% (2026-09-30) | +30.46 | above 25% | change_of_control | Inspira Global (Agrawal family), through Lenexis Foodworks and affiliates, acquired control of Restaurant Brands Asia: ₹900 crore preferential equity plus ₹600 crore war… | — |
| **EPL** | 26.4% (2025-09-30) → 0.0% (2026-09-30) | -26.40 | below 25%, to nil | change_of_control | Promoter Epsilon Bidco Pte. Ltd. (Blackstone vehicle, ultimate beneficial owner Sun Yiming) sold its entire 26.37% holding in EPL on 1 September 2026 through on-market/b… | — |
| **THYROCARE** | 71.06% (2025-09-30) → 51.02% (2026-09-30) | -20.04 | — | stake_change_no_control_change | The promoter group (API Holdings / Docon Technologies) sold down roughly 20% of Thyrocare in two large blocks, reportedly to repay group debt, falling from 71.06% to 51.… | — |
| **SAGILITY** | 67.38% (2025-09-30) → 50.95% (2026-09-30) | -16.43 | — | stake_change_no_control_change | Promoter Sagility B.V. sold down in the open market. Promoter-group holding fell from 67.38% (Sep 2025) to 50.95% (Dec 2025), and a further 11.96% sale on 2026-11-19 lef… | — |
| **TENNIND** | 74.79% (2025-11-18) → 59.79% (2026-09-30) | -15.00 | — | stake_change_no_control_change | Promoter entities Tenneco Mauritius Holdings Ltd and Tenneco (Mauritius) Ltd sold about 15% of capital in open-market/block sales disclosed 2026-08-18. Promoter-group ho… | — |
| **VMM** | 54.11% (2025-09-30) → 40.02% (2026-09-30) | -14.09 | below 50% | stake_change_no_control_change | Promoter entity Samayat Services LLP sold 13.97% of VMM's capital on 2026-03-02, cutting promoter-group holding from 54.09% to 40.12%. Institutions such as HDFC Mutual F… | — |
| **ASTERDM** | 40.39% (2025-09-30) → 53.79% (2026-09-30) | +13.40 | above 50% | change_of_control | The scheme of amalgamation of Quality Care India Limited into Aster DM Healthcare became effective 1 July 2026. Shares issued under the scheme made BCP Asia II Topco IV… | — |
| **AXISCADES** | 58.08% (2025-09-30) → 44.82% (2026-09-30) | -13.26 | below 50% | stake_change_no_control_change | Promoter holding company Jupiter Capital Private Limited sold large blocks of AXISCADES shares — 2.35% disclosed 2026-07-08 (leaving 50.15%) and 10.86% disclosed 2026-10… | — |
| **ACMESOLAR** | 83.41% (2025-09-30) → 71.4% (2026-09-30) | -12.01 | — | dilution_only | Promoter-and-group holding fell from 83.29% to 71.48% between the March 2026 and the off-cycle 4 June 2026 shareholding pattern, with no filing text showing any sale, ag… | — |
| **BELRISE** | 73.01% (2025-09-30) → 61.15% (2026-09-30) | -11.86 | — | stake_change_no_control_change | Sumedh Tools Private Limited, a promoter group entity, sold 5,83,43,040 shares (6.56% of capital) through a block deal on 23 December 2025, cutting its stake to nil. The… | — |
| **GABRIEL** | 55.0% (2025-09-30) → 66.29% (2026-09-30) | +11.29 | — | dilution_only | Promoter holding rose from 55% to 66.29% purely through fresh share issues to the promoters: shares allotted under the NCLT-approved composite scheme (Asia Investments'… | — |
| **WHIRLPOOL** | 51.0% (2025-09-30) → 39.76% (2026-09-30) | -11.24 | below 50% | stake_change_no_control_change | Promoter Whirlpool Mauritius Limited sold 11.24% of the capital in the open market on 2025-12-08, cutting promoter-and-group holding from 51.0% to 39.76%. No new promote… | — |
| **AADHARHFC** | 75.32% (2025-09-30) → 64.51% (2026-09-30) | -10.81 | — | change_of_control | Blackstone-affiliated promoter BCP Topco VII Pte. Ltd. sold its entire 75.19% stake — 28,20,52,121 shares to BCP Asia II Holdco VII Pte. Ltd. at ₹425 and 4,41,39,236 sha… | — |
| **DIACABS** | 84.02% (2025-09-30) → 74.03% (2026-09-30) | -9.99 | — | dilution_only | The Company completed a Qualified Institutions Placement raising Rs.1,613.97 crore by allotting equity shares to qualified institutional buyers. Promoter holding fell fr… | — |
| **BIOCON** | 54.45% (2025-09-30) → 44.68% (2026-09-30) | -9.77 | below 50% | dilution_only | Promoter-and-group holding fell from 54.45% to 44.68% only because the company issued fresh shares — a preferential allotment in January 2026 (6.88% to Mylan Inc) and a… | — |
| **JSWINFRA** | 83.62% (2025-09-30) → 73.93% (2026-09-30) | -9.69 | — | stake_change_no_control_change | JSW Infrastructure raised capital through a qualified institutions placement combined with an offer for sale by Sajjan Jindal Family Trust, the promoter selling sharehol… | — |
| **MPHASIS** | 40.1% (2025-09-30) → 30.53% (2026-09-30) | -9.57 | — | stake_change_no_control_change | The promoter block held by BCP Topco IX Pte. Ltd. (Blackstone) was sold down by about 9.5% of capital around 18 December 2025, taking promoter-and-group holding from 40.… | — |
| **PRIVISCL** | 69.89% (2025-09-30) → 60.6% (2026-09-30) | -9.29 | — | stake_change_no_control_change | Promoter entity Vivira Investment & Trading Private Limited sold a 9.29% block in the open market in early January 2026, cutting its holding to 29.74% and total promoter… | — |
| **LLOYDSENGG** | 49.26% (2025-09-30) → 40.0% (2026-09-30) | -9.26 | — | stake_change_no_control_change | Promoter entities (Aeon Trading LLP, Lloyds Metals & Minerals Trading LLP, Lloyds Enterprises Limited) sold about 7.15% of capital in the open market, largely picked up… | — |
| **KFINTECH** | 22.89% (2025-09-30) → 14.06% (2026-09-30) | -8.83 | — | stake_change_no_control_change | General Atlantic Singapore Fund Pte Ltd, the private-equity promoter, sold 8.76% of KFin Technologies in one transaction on 2026-08-25, cutting promoter-group holding fr… | — |
| **RUBICON** | 59.99% (2025-10-15) → 51.25% (2026-09-30) | -8.74 | — | stake_change_no_control_change | General Atlantic Singapore RR Pte. Ltd., a promoter-classified financial sponsor, sold about 8.45% of Rubicon Research's capital on 2026-09-01, cutting its holding to 27… | — |
| **JSWDULUX** | 69.76% (2025-09-30) → 61.2% (2026-09-30) | -8.56 | — | change_of_control | JSW Paints Limited completed its acquisition of 60.76% of Akzo Nobel India under a share purchase agreement on 10 December 2025, after an open offer, taking 61.2%. The A… | — |
| **ELECTCAST** | 46.21% (2025-09-30) → 54.53% (2026-09-30) | +8.32 | above 50% | stake_change_no_control_change | Existing promoter entities raised their stake from 46.21% to 54.53% by buying 8.32% in open-market/block purchases — Electrosteel Thermal Coal Ltd bought 3.32% (March 20… | — |
| **CENTRALBK** | 89.27% (2025-09-30) → 81.19% (2026-09-30) | -8.08 | — | stake_change_no_control_change | The President of India, through the Department of Financial Services, Ministry of Finance, sold about 8.08% of the bank's capital, cutting promoter holding from 89.27% t… | — |
| **TEGA** | 74.8% (2025-09-30) → 67.08% (2026-10-15) | -7.72 | — | within_promoter_family | Promoter Manish Mohanka gifted 72,78,925 equity shares (9.69% of capital) off-market to MM Business Trust, a promoter-group trust with Mehul Mohanka as trustee, under a… | — |
| **TORNTPHARM** | 68.31% (2025-09-30) → 60.78% (2026-09-30) | -7.53 | — | dilution_only | No change of control. The promoter group stayed at 68.31% through June 2026, then eased to 60.78% in an off-cycle 20 July 2026 shareholding pattern filed after a capital… | — |
| **VIPIND** | 49.73% (2025-09-30) → 42.35% (2026-09-30) | -7.38 | — | change_of_control | The Piramal-family promoter entities sold down ~26% of VIP Industries through open-market/block transactions in late December 2025, and Multiples Private Equity Fund IV… | — |
| **AWL** | 63.94% (2025-09-30) → 56.94% (2026-09-30) | -7.00 | — | change_of_control | Adani group exited as promoter: Adani Commodities LLP sold its remaining stake (7% then 13%) and the Adani entities applied on 27 November 2025 to be reclassified from p… | — |
| **DOMS** | 70.39% (2025-09-30) → 63.39% (2026-09-30) | -7.00 | — | stake_change_no_control_change | Promoter F.I.L.A. Fabbrica Italiana Lapis Ed Affini S.p.A. sold 7% of DOMS' capital on 2026-06-22, cutting its holding to 19.01%. Total promoter-group holding fell from… | — |
| **NETWEB** | 71.0% (2025-09-30) → 64.16% (2026-09-30) | -6.84 | — | stake_change_no_control_change | In February 2026 the Lodha promoter family sold about 3.65% of the capital in the open market, taking promoter-group holding from 71.0% to 66.98%. The same family contin… | — |
| **BLUEJET** | 79.81% (2025-09-30) → 73.15% (2026-09-30) | -6.66 | — | stake_change_no_control_change | Exchange shareholding register shows promoter-and-group holding flat at 79.81% through 2026-06-30, then 73.15% at an interim 2026-07-09 pattern and unchanged at 2026-09-… | — |
| **LICI** | 96.5% (2025-09-30) → 90.0% (2026-09-30) | -6.50 | — | stake_change_no_control_change | The President of India, acting through the Ministry of Finance (promoter), sold 6.5% of Life Insurance Corporation of India's capital, cutting the promoter-and-group hol… | — |
| **PNGJL** | 83.11% (2025-09-30) → 76.62% (2026-09-30) | -6.49 | — | dilution_only | Promoter and group holding fell from 83.11% to 76.62% as of an off-quarter 04-Aug-2026 shareholding filing, consistent with fresh share issuance to meet SEBI's minimum p… | — |
| **MANAPPURAM** | 35.25% (2025-09-30) → 41.66% (2026-09-30) | +6.41 | — | change_of_control | Bain Capital affiliates BC Asia Investments XXV and XIV subscribed to a ~Rs 4,385 crore preferential issue of shares and warrants at Rs 236, and after a mandatory open o… | — |
| **CRAFTSMAN** | 48.7% (2025-09-30) → 42.41% (2026-09-30) | -6.29 | — | stake_change_no_control_change | Promoter, Chairman and Managing Director Srinivasan Ravi sold 5,25,000 shares (2.01% of capital) in the open market on 23 June 2026, cutting his holding from 40.15% to 3… | — |
| **GLAND** | 51.83% (2025-09-30) → 45.75% (2026-09-30) | -6.08 | below 50% | stake_change_no_control_change | Promoter Fosun Pharma Industrial Pte. Ltd. sold 6% of Gland Pharma's capital in the open market in September 2026, cutting its holding to 45.76%; promoter-and-group hold… | — |
| **NHPC** | 67.4% (2025-09-30) → 61.39% (2026-09-30) | -6.01 | — | stake_change_no_control_change | The President of India (Ministry of Power), NHPC's promoter, sold about 6.01% of the capital in June 2026. Promoter-and-group holding fell from 67.4% to 61.39%. The Gove… | — |
| **HINDCOPPER** | 66.14% (2025-09-30) → 60.14% (2026-09-30) | -6.00 | — | stake_change_no_control_change | Promoter-and-group holding (Government of India) stayed 66.14% through 2026-06-30, then fell to 60.14% at 2026-09-30, a 6 percentage-point drop. No filing explains it; R… | — |
| **MAHABANK** | 79.6% (2025-09-30) → 73.6% (2026-09-30) | -6.00 | — | stake_change_no_control_change | The President of India, acting through the Department of Financial Services, Ministry of Finance, sold 6% of Bank of Maharashtra's capital, cutting the government promot… | — |
| **YATHARTH** | 61.64% (2025-09-30) → 55.8% (2026-09-30) | -5.84 | — | stake_change_no_control_change | Promoter Dr. Neena Tyagi sold 5.85% of the capital in the open market, cutting her holding to 0.62%. Total promoter-and-group holding fell from 61.64% to 55.8%, where it… | — |
| **PREMIERENE** | 63.94% (2025-09-30) → 58.49% (2026-09-30) | -5.45 | — | stake_change_no_control_change | Promoter Surenderpal Singh Saluja sold 5.33% of the capital in the open market in May 2026. Promoter-and-group holding fell from 63.94% to 58.49%, still a clear majority… | — |
| **RELIGARE** | 25.83% (2025-09-30) → 31.26% (2026-09-30) | +5.43 | — | stake_change_no_control_change | The Burman family, already classified as promoters after the open offer completed in February 2025, kept raising its holding — converting preferential warrants at Rs.235… | — |
| **HOMEFIRST** | 12.39% (2025-09-30) → 6.97% (2026-09-30) | -5.42 | — | stake_change_no_control_change | Promoter private-equity sponsors True North Fund V LLP and Aether (Mauritius) Ltd sold 5.34% of capital in open-market sales disclosed 2026-03-04, cutting promoter-and-g… | — |
| **CPPLUS** | 77.12% (2025-09-30) → 71.8% (2026-09-30) | -5.32 | — | within_promoter_family | Promoter Aditya Khemka transferred 13.62% of capital by inter-se transfer on 2026-04-01 to the Aditya Khemka Business Family Trust (13.62%, holding 14.15% after) and to… | — |
| **IIFLCAPS** | 30.98% (2025-09-30) → 25.8% (2026-11-04) | -5.18 | — | change_of_control | Fairfax's FIH Mauritius Investments Ltd subscribed to a ₹2,000 crore preferential issue at ₹350/share and completed a 26% open offer plus secondary purchases from the ex… | — |
| **JAMNAAUTO** | 49.94% (2025-09-30) → 44.81% (2026-09-30) | -5.13 | — | stake_change_no_control_change | Two promoter family members, Ranadeep Singh Jauhar and Pradeep Singh Jauhar, each sold 2.49% of capital on 2026-09-25 (4.98% combined). Promoter-group holding fell from… | — |
| **KRN** | 70.79% (2025-09-30) → 65.69% (2026-09-30) | -5.10 | — | stake_change_no_control_change | Promoters (Santosh Kumar Yadav, Anju Devi, Manohar Lal and promoter group) gave prior intimation of intent to sell up to 10,00,000 shares for personal and financial reas… | — |
| **SHRIRAMFIN** | 25.39% (2025-09-30) → 20.3% (2026-09-30) | -5.09 | below 25% | dilution_only | Shriram Finance issued fresh shares by preferential allotment to MUFG Bank, Ltd (Mitsubishi UFJ Financial Group), which took 20.02% of the enlarged capital. Promoters so… | — |
| **BHEL** | 63.17% (2025-09-30) → 58.17% (2026-09-30) | -5.00 | — | stake_change_no_control_change | The Government of India, BHEL's promoter, sold 5% of the capital, cutting promoter-and-group holding from 63.17% to 58.17% by the 2026-03-31 quarter. The President of In… | — |
| **GICRE** | 82.4% (2025-09-30) → 77.4% (2026-09-30) | -5.00 | — | stake_change_no_control_change | The President of India, acting through the Ministry of Finance, sold 5% of GIC Re's capital, cutting promoter holding from 82.4% to 77.4%. The Government of India remain… | — |
| **JSFB** | 21.87% (2025-09-30) → 16.87% (2026-09-30) | -5.00 | — | stake_change_no_control_change | Jana Holdings Limited, a promoter of Jana Small Finance Bank, signed a Share Purchase Agreement on 18 May 2026 to sell 5,160,903 shares (~4.9% of paid-up capital) to TVS… | — |
| **SKIPPER** | 66.48% (2025-09-30) → 61.48% (2026-09-30) | -5.00 | — | dilution_only | Promoter-and-group holding fell from 66.5% to 61.48% between June and July 2026 solely because the company allotted 92,23,402 new shares on a preferential basis to non-p… | — |
| **CAPILLARY** | 52.16% (2025-11-20) → 47.23% (2026-09-30) | -4.93 | below 50% | stake_change_no_control_change | Promoter Capillary Technologies International Pte Ltd sold about 4.14% of capital (disclosed 2026-08-17), cutting its holding to 44.78%. Total promoter-and-group holding… | — |
| **GODREJPROP** | 47.05% (2025-09-30) → 51.66% (2026-09-30) | +4.61 | above 50% | stake_change_no_control_change | Promoter and group holding rose from 47.05% to 51.66% over the window, with promoter entity Anamudi Real Estates LLP buying 0.31% in the open market (to 3.36%) and no pr… | — |
| **GMRP&UI** | 50.56% (2025-09-30) → 46.53% (2026-09-30) | -4.03 | below 50% | within_promoter_family | Promoter group holding fell from 50.56% to 46.28% after a preferential allotment to a non-promoter (Synergy Industrial, Metals and Power Holdings, 4.77%, 12.74% after).… | — |
| **JIOFIN** | 47.12% (2025-09-30) → 50.98% (2026-10-30) | +3.86 | above 50% | stake_change_no_control_change | Existing promoter-group entities Jamnagar Utilities & Power and Sikka Ports & Terminals acquired shares, including via preferential allotment, lifting promoter-and-group… | — |
| **JKPAPER** | 49.63% (2025-09-30) → 52.94% (2026-09-30) | +3.31 | above 50% | within_promoter_family | No outside buyer. Singhania promoter group entities (YPL Enterprises 6.95%, JK Credit 5.54%, Accurate Finman 1.03%) acquired 13.52% of capital, while two Singhania HUFs… | — |
| **VIYASH** | 52.33% (2025-09-30) → 49.24% (2026-09-30) | -3.09 | below 50% | stake_change_no_control_change | Promoter holding rose to 61.43% in December 2025 when the Company allotted shares under the NCLT-sanctioned amalgamation of Viyash Life Sciences and others, then fell to… | — |
| **NEOGEN** | 51.23% (2025-09-30) → 48.31% (2026-09-30) | -2.92 | below 50% | within_promoter_family | On December 31, 2025 founder Haridas T. Kanani gifted 21.90% and Beena Kanani 10% of capital to their respective Kanani family trusts (managing trustee Dr. Harin Kanani)… | — |
| **APOLLO** | 52.41% (2025-11-26) → 49.98% (2026-09-30) | -2.43 | below 50% | dilution_only | No change in Apollo's own ownership. Promoter-group holding slipped from 52.41% to 49.98% purely because the company issued shares — warrant conversions and preferential… | — |
| **BLACKBUCK** | 27.19% (2025-09-30) → 24.99% (2026-09-30) | -2.20 | below 25% | stake_change_no_control_change | Promoter founders Rajesh Kumar Naidu Yabaji and Ramasubramanian Balasubramaniam sold about 1.55% of capital in open-market sales disclosed 2025-12-18; aggregate promoter… | — |
| **ALKEM** | 51.2% (2025-09-30) → 49.7% (2026-09-30) | -1.50 | below 50% | stake_change_no_control_change | Promoter-group entities (Samprada & Nanhamati Singh Family Trust and Jayanti Sinha) sold about 2% of the capital in block deals, taking promoter-and-group holding from 5… | — |

## E3 — open-offer filings not read as a change of control

None.

## E4 — a seat whose holder differs between the calls, not reported

| Company | Seat | Earlier call lists | Later call lists | Calls | The skill | Reviewed |
|---|---|---|---|---|---|---|
| **ACC** | CFO | rakesh tiwary | rohit soni | Nov 2025 → May 2026 | judge read, no change | — |
| **AMBUJACEM** | CFO | rakesh tiwary | rohit soni | Nov 2025 → May 2026 | judge read, no change | — |
| **AVALON** | MD | kunhamed bicha | bicha for the initial remarks | Nov 2025 → May 2026 | dropped: not a change: re-appointment | — |
| **AXISCADES** | MD | s rn | sampath ravinarayanan | Jun 2026 → Jun 2026 | judge read, no change | — |
| **DELHIVERY** | CFO | amit agarwal | vivek pabari | Nov 2025 → May 2026 | dropped: before the window (2025-11-01) | — |
| **EXIDEIND** | CEO | pravin saraf | from exide industries, manoj kumar agarwal | Feb 2026 → May 2026 | dropped: not a change: division or subsidiary seat | — |
| **EXIDEIND** | MD | pravin saraf | from exide industries, manoj kumar agarwal | Feb 2026 → May 2026 | dropped: not a change: division or subsidiary seat | — |
| **FORTIS** | CEO | anand k, ashutosh raghuvanshi | from agilus, vivek goyal from agilus | Nov 2025 → May 2026 | dropped: not a change: re-appointment | — |
| **FORTIS** | MD | ashutosh raghuvanshi | anand k | Nov 2025 → May 2026 | dropped: not a change: re-appointment | — |
| **HEROMOTOCO** | CEO | v s ka sbeka r, vikram kasbekar | harshavardhan chitale | Nov 2025 → May 2026 | dropped: before the window (2025-11-01) | — |
| **IDEA** | CEO | akshaya moondra | abhijit kishore | Sep 2025 → May 2026 | dropped: no date in the documents (the change may predate the window) | — |
| **INOXGREEN** | CFO | akhil jindal | inoxgfl group | Sep 2025 → Jun 2026 | judge read, no change | — |
| **INOXWIND** | CFO | akhil jindal | inoxgfl group | Sep 2025 → Jun 2026 | judge read, no change | — |
| **KIMS** | CEO | d r nitish shetty, hospital d r nitish shetty, nitish shetty | abhinay bollineni | Feb 2026 → May 2026 | dropped: not a change: re-appointment | — |
| **LEMONTREE** | CFO | kapil sharma | mayank sharma | Jan 2026 → Jun 2026 | judge read, no change | — |
| **LODHA** | CEO | abhishek lodha, sanjay chauhan, tikam jain | prashant bindal | Nov 2025 → Jul 2026 | judge read, no change | — |
| **LOTUSDEV** | CFO | rakesh gupta | sanjay kumar jain | Sep 2025 → May 2026 | judge read, no change | — |
| **NH** | MD | anesh shetty | emmanuel rupert | Nov 2025 → Feb 2026 | dropped: not a change: other: the AGM notice only seeks approval to revise the remuneration of the incumbent Dr. Emmanuel Rupert for the remaining tenure of his existing appointment (upto February 10, 2028); no appointment, cessation or vacancy of the seat is stated | — |
| **PARADEEP** | CFO | bijay kumar biswal | bijoy biswal | Nov 2025 → May 2026 | judge read, no change | — |
| **PPLPHARMA** | CEO | jagdeep mallareddy, jairam sridharan, yesh nadkarni | peter deyoung | Oct 2025 → Jul 2026 | dropped: not a change: not this company — the passage discusses AUM, ROAUM and a lending book ('double our AUM to more than 1.5 lakh crores'), not Piramal Pharma's pharmaceuticals business, and the remark pre-dates the 2025-11-26 to 2026-11-26 window | — |
| **PPLPHARMA** | CFO | vikash singh la | vivek valsaraj | Oct 2025 → Jul 2026 | judge read, no change | — |
| **PRAJIND** | MD | ashish gaikwad | sachin raole | Mar 2026 → Jun 2026 | judge read, no change | — |
| **REDINGTON** | CEO | v s hariharan | cem borhan, ramesh natarajan | Nov 2025 → Jun 2026 | judge read, no change | — |
| **SONATSOFTW** | CFO | samir dhir | jagannathan cn | Nov 2025 → May 2026 | judge read, no change | — |
| **SUBROS** | CEO | from sub | parmod kumar duggal | Nov 2025 → May 2026 | judge read, no change | — |
| **SUNPHARMA** | MD | dilip shanghvi | kirti ganorkar | Sep 2025 → May 2026 | judge read, no change | — |
| **SUPRIYA** | CFO | saloni wagh | krishna raghunathan | Nov 2025 → May 2026 | judge read, no change | — |
| **TBOTEK** | MD | gaurav bhatnagar | ankush nijhawan | Sep 2025 → Jun 2026 | judge read, no change | — |
| **TEGA** | CEO | mehul mohanka | m r sourav sen, sourav sen | Sep 2025 → Jun 2026 | judge read, no change | — |
| **TRIVENI** | CEO | rajiv rajpal | sameer sinha, suresh taneja | Nov 2025 → Jun 2026 | dropped: not a change: other: the cessation was only as Key Managerial Personnel under Section 203; he continues to hold the chief executive seat of the Company, and the Board merely revised his remuneration | — |
| **UCOBANK** | CFO | corporate general managers | kamble and also our cro | Jan 2026 → May 2026 | judge read, no change | — |

## E5 — a headline names a seat, no change reported

| Company | Seat | Date | Headline | The skill | Reviewed |
|---|---|---|---|---|---|
| **ABFRL** | CEO/MD | 2026-03-24 | [Aditya Birla Fashion and Retail Limited has informed the Exchange regarding Appointment of Mr Suraj Bahirwani as CEO (D…](https://nsearchives.nseindia.com/corporate/ABFRL_24032026131435_ABFRL_SE_Change_in_Management.pdf) | CEO: not a change: division or subsidiary seat | — |
| **AFFLE** | CEO/MD | 2026-01-02 | [Affle 3i Limited has informed the Exchange regarding Appointment of Mr Sameer Sondhi as as Chief Executive Officer, Nor…](https://nsearchives.nseindia.com/corporate/AFFLE_02012026110310_Appointment_as_senior_management_Sameer_Sondhi.pdf) | CEO: not a change: division or subsidiary seat | — |
| **APARINDS** | CEO/MD | 2025-12-15 | [Apar Industries Limited has informed the Exchange regarding Resignation of Mr. Shashi Amin, as Chief Executive Officer…](https://nsearchives.nseindia.com/corporate/APARINDS_15122025125716_FinalIntimationwithresignationletter.pdf) | CEO: not a change: division or subsidiary seat; MD & CEO: not a change: other: appointment is to a Non-Executive Independent Director seat, not the c… | — |
| **ASHAPURMIN** | CEO/MD | 2026-02-05 | [Ashapura Minechem Limited has informed the Exchange regarding Appointment of Mr HEMUL SHAH as Executive Director & CEO…](https://nsearchives.nseindia.com/corporate/ASHAPURMIN_05022026203138_Outcome05022026.pdf) | CEO: not a change: re-appointment; MD: not a change: division or subsidiary seat | — |
| **BAJAJELEC** | CEO/MD | 2026-10-28 | [Bajaj Electricals Limited has informed the Exchange regarding Appointment of Mr. Sanjay Sachdeva as Managing Director &…](https://nsearchives.nseindia.com/corporate/BAJAJELEC_28102026145908_SEIntimationOutcome.pdf) | Executive Chairman: not a change: other: the Executive Chairman is not the Company's chief executive — the documents state the Company is led by Mana… | — |
| **BERGEPAINT** | CEO/MD | 2026-08-12 | [Berger Paints (I) Limited has informed the Exchange regarding Appointment of Mr Abhijit Roy as Managing Director & CEO…](https://nsearchives.nseindia.com/corporate/PAINTBERGE_12082026201424_Re-appointmentofMrRoy.pdf) | MD & CEO: not a change: re-appointment | — |
| **BLS** | CEO/MD | 2026-08-07 | [BLS International Services Limited has informed the Exchange regarding Appointment of Mr Shikhar Aggarwal as Managing D…](https://nsearchives.nseindia.com/corporate/BLS_07082026195810_Final_Outcome_07082026_signed.pdf) | MD: not a change: deputy or joint seat | — |
| **CAMS** | CEO/MD | 2026-02-25 | [Computer Age Management Services Limited has informed the Exchange regarding a press release dated February 25, 2026, t…](https://nsearchives.nseindia.com/corporate/Jaiganesh_25022026164318_CAMS_Press_Release.pdf) | CEO: not a change: division or subsidiary seat; CEO: not a change: not this company; MD: not a change: re-appointment | — |
| **CRISIL** | CEO/MD | 2026-02-13 | [CRISIL Limited has informed the Exchange regarding Appointment of Mr. Amish Mehta as Managing Director of the company w…](https://nsearchives.nseindia.com/corporate/CRISIL_13022026184248_SignedBSENSE_V1.pdf) | MD & CEO: not a change: re-appointment | — |
| **EICHERMOT** | CEO/MD | 2026-03-10 | [Eicher Motors Limited has informed the Exchange about General Updates on VE Commercial Vehicles Ltd appoints B Srinivas…](https://nsearchives.nseindia.com/corporate/rahulrathore_royalenfield_com_10032026181624_EML_VECV_Intimation_Final_Signed.pdf) | Executive Chairman: not a change: deputy or joint seat; MD & CEO: not a change: division or subsidiary seat | — |
| **FORTIS** | CEO/MD | 2026-07-08 | [Fortis Healthcare Limited has informed the Exchange regarding Appointment of Dr. Ashutosh Raghuvanshi as Managing Direc…](https://nsearchives.nseindia.com/corporate/FORTIS_08072026144456_OUTCOMEOFBM.pdf) | MD & CEO: not a change: division or subsidiary seat; MD & CEO: not a change: re-appointment | — |
| **GRASIM** | CEO/MD | 2026-01-16 | [Appointment of Mr. Sachin Sahay as Chief Executive Officer of Birla Opus Paints, and as Senior Management Personnel of…](https://nsearchives.nseindia.com/corporate/GRASIM_16012026112645_SEIntimation_ChangeinSMP_16012026.pdf) | CEO: not a change: division or subsidiary seat | — |
| **HDFCLIFE** | CEO/MD | 2026-04-21 | [HDFC Life Insurance Company Limited has informed the Exchange regarding Appointment of Ms Vibha Padalkar as Managing Di…](https://nsearchives.nseindia.com/corporate/PRASAD_21042026195755_BMoutcome.pdf) | MD & CEO: not a change: re-appointment | — |
| **JUBLPHARMA** | CEO/MD | 2026-05-22 | [Jubilant Pharmova Limited has informed the Exchange regarding Appointment of Mr. Priyavrat Bhartia as Managing Director…](https://nsearchives.nseindia.com/corporate/JUBLPHARMA_22052026145717_MDJMDSIGNED.pdf) | MD: not a change: deputy or joint seat; MD: not a change: re-appointment | — |
| **KFINTECH** | CEO/MD | 2026-02-25 | [KFin Technologies Limited has informed the Exchange regarding a press release dated February 25, 2026, titled "MF Centr…](https://nsearchives.nseindia.com/corporate/KFINTECHNSE_25022026160728_Intimation.pdf) | CEO: not a change: not this company; MD & CEO: not a change: other: only a revision in remuneration of the same incumbent, approved by members; he co… | — |
| **LATENTVIEW** | CFO | 2026-01-14 | [With reference to the announcement made on November 05, 2025, regarding the resignation of Mr. Rajan Bala Venkatesan, C…](https://nsearchives.nseindia.com/corporate/LATENTVIEW_14012026120322_SEintimationwithdrawalSigned.pdf) | CFO: not a change: other: the Chief Financial Officer withdrew his earlier resignation without a break in service and continues in the seat — the Com… | — |
| **LICI** | CEO/MD | 2025-12-01 | [Life Insurance Corporation of India has informed the Exchange regarding Appointment of Mr Ramakrishnan Chander as Manag…](https://nsearchives.nseindia.com/corporate/LIC_BOARD_01122025214032_Intimation_MDRC_01122025.pdf) | MD: not a change: other: one of several Managing Directors who is not the Corporation's chief executive — the chief executive seat is held throughout… | — |
| **LTTS** | CFO | 2026-04-22 | [L&T Technology Services Limited has informed the Exchange regarding Appointment of Mr Rajeev Gupta (DIN: 06782710) as E…](https://nsearchives.nseindia.com/corporate/LTTS_22042026195759_LTTSBMOutcome22042026.pdf) | CFO: not a change: same person, new title | — |
| **MANYAVAR** | CEO/MD | 2026-07-25 | [Vedant Fashions Limited has informed the Exchange regarding Appointment of Mr. Ravi Modi as Chairman & Managing Directo…](https://nsearchives.nseindia.com/corporate/MANYAVAR_25072026190133_OutcomeofBM25072026FinalSigned.pdf) | CMD: not a change: re-appointment | — |
| **OSWALPUMPS** | CEO/MD | 2026-08-08 | [Oswal Pumps Limited has informed the Exchange regarding Appointment of Mr Vivek Gupta as Chairman & Managing Director o…](https://nsearchives.nseindia.com/corporate/OSWALPUMPS_08082026194624_SELetterReAppVGAppCFOOPL08082026.pdf) | CMD: not a change: re-appointment | — |
| **PARADEEP** | CEO/MD | 2026-02-02 | [Paradeep Phosphates Limited has informed the Exchange regarding Appointment of Mr N Suresh Krishnan as Managing Directo…](https://nsearchives.nseindia.com/corporate/PPLTD_02022026190907_Outcome02022026.pdf) | MD: not a change: deputy or joint seat; MD: not a change: re-appointment | — |
| **PRICOLLTD** | CEO/MD | 2026-05-14 | [Pricol Limited has informed the Exchange regarding Appointment of Mr.Vikram Mohan as Chairman & Managing Director of th…](https://nsearchives.nseindia.com/corporate/PRICOLLTD_14052026201017_sedisclosure.pdf) | CMD: not a change: same person, new title; Executive Chairman: not a change: other: Mrs.Vanitha Mohan was Chairman of the Board and a Director, not t… | — |
| **PRSMJOHNSN** | CEO/MD | 2026-03-02 | [Prism Johnson Limited has informed the Exchange regarding appointment of Mr. Sanjaykumar Shivajee Roy as an Additional…](https://nsearchives.nseindia.com/corporate/PRSMJOHNSN_02032026082607_SEIntimationApptOfSanjayRoy.pdf) | CEO: not a change: division or subsidiary seat | — |
| **PURVA** | CEO/MD | 2026-02-12 | [Puravankara Limited has informed the Exchange regarding Appointment of Mr Ashish Ravi Puravankara as Managing Director…](https://nsearchives.nseindia.com/corporate/PURVA_12022026183646_SEINTIMATIONsd.pdf) | MD: not a change: re-appointment | — |
| **PURVA** | CFO | 2026-05-18 | [Puravankara Limited has informed the Exchange regarding Outcome of Board Meeting held on May 18, 2026 for appointment o…](https://nsearchives.nseindia.com/corporate/PURVA_18052026204512_SEintimation.pdf) | MD: not a change: re-appointment | — |
| **RATEGAIN** | CEO/MD | 2026-07-31 | [Rategain Travel Technologies Limited has informed the Exchange regarding Appointment of Mr. Bhanu Chopra as Chairman &…](https://nsearchives.nseindia.com/corporate/RATEGAIN_31072026112239_RG_Outcome_Reappointment.pdf) | judge read, no change | — |
| **RAYMOND** | CEO/MD | 2026-07-06 | [Raymond Limited has informed the Exchange regarding a press release dated July 06, 2026, titled "Raymond Limited Appoin…](https://nsearchives.nseindia.in/corporate/RAYMOND_06072026113315_RLSEintimationPRsigned.pdf) | CEO: not a change: division or subsidiary seat | — |
| **RCF** | CFO | 2026-11-12 | [Rashtriya Chemicals and Fertilizers Limited has informed the Exchange regarding Appointment of Ms Nazhat J Shaikh as Ch…](https://nsearchives.nseindia.in/corporate/RCF_12112026161158_OutcomeDirectorfinance.pdf) | CFO: not a change: re-appointment | — |
| **RELIGARE** | CEO/MD | 2026-08-12 | [Religare Enterprises Limited has informed the Exchange regarding Appointment of Mr Arjun Lamba as Managing Director of…](https://nsearchives.nseindia.com/corporate/RELIGARE_12082026202225_RELOUTCOME120820260.pdf) | CFO: not a change: division or subsidiary seat; MD & CEO: not a change: division or subsidiary seat; MD: not a change: division or subsidiary seat; M… | — |
| **RKFORGE** | CEO/MD | 2026-05-01 | [Ramkrishna Forgings Limited has informed the Exchange regarding Appointment of Mr Mr. Naresh Jalan as Managing Director…](https://nsearchives.nseindia.com/corporate/RKFORGE_01052026175232_BMOutcom1May26.pdf) | MD & CEO: not a change: not this company; MD: not a change: deputy or joint seat; MD: not a change: re-appointment | — |
| **SAFARI** | CEO/MD | 2026-02-10 | [Safari Industries (India) Limited has informed the Exchange regarding Appointment of Mr. Sudhir Jatia as Chairman & Man…](https://nsearchives.nseindia.com/corporate/SAFARI_10022026143542_BMOUTCOMEOTHERMATTERS.pdf) | MD: not a change: re-appointment | — |
| **SANOFI** | CEO/MD | 2026-04-02 | [Sanofi India Limited has informed the Exchange regarding 'Intimation Regarding Receipt Of Central Government Approval F…](https://nsearchives.nseindia.in/corporate/COSECSANOFI_02042026195933_Intimation_-Approval_Signed.pdf) | MD: not a change: other: in-period filing only reports receipt of Central Government approval on 1st April 2026 for an appointment already effective… | — |
| **SOBHA** | CEO/MD | 2026-05-04 | [Sobha Limited has informed the Exchange regarding Appointment of Mr. Jagadish Nangineni as Managing Director of the com…](https://nsearchives.nseindia.com/corporate/SOBHA_04052026175724_SOBHA_Outcome_of_BM_Q4_FY2026.pdf) | MD: not a change: re-appointment | — |
| **STLTECH** | CEO/MD | 2026-04-29 | [Sterlite Technologies Limited has informed the Exchange regarding Appointment of Mr Ankit Agarwal as Managing Director…](https://nsearchives.nseindia.com/corporate/STLTECH_29042026140807_SEintimationAppointmentsigned.pdf) | MD: not a change: re-appointment | — |
| **UNOMINDA** | CEO/MD | 2026-04-19 | [UNO Minda Limited has informed the Exchange regarding Appointment of Mr Vivek Shripad Joshi as CEO-LPS Domain of the co…](https://nsearchives.nseindia.com/corporate/MINDAIND1_19042026150053_Outcome_SMP_App_VivekJoshi.pdf) | CEO: not a change: division or subsidiary seat; CFO: not a change: other: Mr. Sunil Bohra appears only as the CFO quoted in the Q1 FY27 press release… | — |
| **V2RETAIL** | CEO/MD | 2026-05-28 | [V2 Retail Limited has informed the Exchange regarding Appointment of Mr Ram Chandra Agarwal as Chairman & Managing Dire…](https://nsearchives.nseindia.com/corporate/V2RETAIL_28052026190338_Covering_MD_Appointment.pdf) | CEO: not a change: other: no appointment, cessation or vacancy of the CEO seat is stated; the seat is only mentioned in a relationship disclosure, an… | — |
| **VGUARD** | CEO/MD | 2026-07-29 | [V-Guard Industries Limited has informed the Exchange regarding Appointment of Mr Mithun K Chittilappilly as Chairman &…](https://nsearchives.nseindia.com/corporate/VGUARD4321_29072026133228_OutcomeIntimation.pdf) | Executive Chairman: not a change: other: non-executive Independent Director chairperson, not the company's chief executive (the Managing Director is)… | — |
| **WELENT** | CEO/MD | 2026-05-14 | [Welspun Enterprises Limited has informed the Exchange regarding Appointment of Mr Sandeep Garg as Managing Director of…](https://nsearchives.nseindia.com/corporate/WELENT_14052026204256_Upload.pdf) | CEO: not a change: division or subsidiary seat; CFO: not a change: division or subsidiary seat; MD: not a change: division or subsidiary seat; MD: no… | — |
| **WIPRO** | CEO/MD | 2026-04-01 | [Wipro Limited has informed the Exchange regarding Resignation of Ms Suzanne Dann as Chief Executive Officer for America…](https://nsearchives.nseindia.com/corporate/Wipro_Secretarial_01042026174222_Reg30SEIntimation.pdf) | CEO: not a change: division or subsidiary seat | — |

## E8 — reported changes whose name or quote was not matched

| Company | Seat | Names in documents | Quote in documents | Quote |
|---|---|---|---|---|
| **IGL** | MD | True | True | This is inform that Shri Kumar Shanker (DIN: 09533240) has been nominated by Promoter Company i.e. GAIL (India) Limited (GAIL) as Managing… |
| **KOTAKBANK** | MD & CEO | True | True | We wish to inform you that Mr. Ashok Vaswani, Managing Director & CEO of the Bank, has informed the Board of the Bank that, for personal re… |
| **LICI** | CFO | True | True | Ms. Sonija M. S., Chief (I/C), Finance & Accounts as Chief Financial Officer of the Corporation w.e.f. November 26, 2026. |
| **MANAPPURAM** | CFO | True | True | Mr. Buvanesh Tharashankar with effect from May 5, 2026 will be the Chief Financial Officer of the Company and will continue as the Group Ch… |
| **RALLIS** | CFO | True | True | Pursuant to Regulation 30 of the SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015 ('SEBI Listing Regulations'), we… |
| **SHRIRAMFIN** | CFO | True | True | Mr. Sunder Subramanian Joint Managing Director & Chief Financial Officer |
| **SKFINDUS** | MD | True | True | we wish to inform change in designation of Mr. Sujeeth Pai (DIN: 07763929) from Whole-Time Director to Managing Director of the Company wit… |
| **STARCEMENT** | MD & CEO | True | True | In terms of recommendation of the Nomination & Remuneration Committee, the Board of Directors of the Company, has approved the change in de… |
| **SUMICHEM** | MD | True | True | At the Meeting of the Board of Directors of the Company held today i.e. on 26th May, 2026, the Board has decided to promote Dr. Suresh Rama… |
| **TMPV** | CFO | True | True | Today we have with us Mr. P B Balaji, Group CFO , Tata Motors Passenger Vehicles Group; Mr. Shailesh Chandra, MD and CEO Tata Motors Passen… |
| **TVSSCS** | CEO | True | True | Accordingly, Mr. Vikas Chadha is no longer the Global Chief Executive Officer of the Company. |
| **VEDL** | CEO | True | True | The Board of Directors, on recommendation of Nomination and Remuneration Committee of the Company, on July 30, 2026, have considered and ap… |
| **BLUEJET** | ownership | False | None |  |
| **JPPOWER** | ownership | True | False | 24% voting right earlier held by JAL shall stand transferred to APL. |
| **MTARTECH** | ownership | False | None |  |
