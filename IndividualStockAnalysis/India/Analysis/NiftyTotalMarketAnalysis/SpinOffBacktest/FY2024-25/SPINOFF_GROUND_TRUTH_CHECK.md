# Demerger list checked against NSE's register

*Skill run 2025-03-31 · register from the daily bhavcopy bundles' corporate-actions file and NSE's corporate-actions API · 5 universe demerger record dates in the window.*

| | Count |
|---|---:|
| Demergers in NSE's register (universe) | 5 |
| …captured by the skill as demergers | 5 |
| …MISSED | 0 |
| Confirmed demergers in the skill | 21 |
| …verified by a register record date | 20 |
| …pending (no record date yet, not verifiable) | 1 |
| …FALSE POSITIVES | 0 |

## Recall — every register demerger, and what the skill holds

| Parent | Record date(s) | Purpose | Skill kind | Confidence | Stage | Resulting company read | Resulting company listed (NSE equity list) | Verdict |
|---|---|---|---|---|---|---|---|---|
| **CCAVENUE** | 2024-09-11 | Demerger | demerger/merger/slump_sale | confirmed | record_date | Odigma Consultancy Solutions Limited |  | captured |
| **ITC** | 2025-01-06 | DEMERGER; Demerger | capital_reduction/demerger/slump_sale | confirmed | record_date | ITC Hotels Limited | ITCHOTELS (2025-01-29) | captured |
| **RAYMOND** | 2024-07-11 | DEMERGER; Demerger | demerger/merger | confirmed | record_date | Raymond Lifestyle Limited | RAYMONDLSL (2024-09-05) | captured |
| **SANOFI** | 2024-06-13 | DEMERGER; Demerger | demerger/preferential_issue/rights_issue | confirmed | record_date | Sanofi Consumer Healthcare India Limited |  | captured |
| **STAR** | 2024-12-06 | DEMERGER; Demerger | demerger/merger/preferential_issue/rights_issue/slump_sale | confirmed | listed | OneSource Specialty Pharma Limited | ONESOURCE (2025-01-24) | captured |

## Precision — every confirmed demerger in the skill

| Company | Stage | Listed on | Register date(s) | What is spun (judge) | Verdict |
|---|---|---|---|---|---|
| **ABFRL** | effective |  | 2025-05-22 | Madura Fashion & Lifestyle (MFL) western wear brands business, demerged into Adi | verified by a later record date (2025-05-22) |
| **ADANIENT** | announced |  |  | Food FMCG division — trading and supply of edible oil and allied commodities, pl | pending — not yet verifiable (no record date yet) |
| **CCAVENUE** | record_date | 2024-09-11 | 2024-09-11 | Global Top Level Domain (GTLD) Undertaking — the dot-triple-O top-level domain a | verified by the register |
| **DBREALTY** | nclt_sanction |  | 2025-07-18 | The hospitality business — operating and under-construction luxury/upscale hotel | verified by a later record date (2025-07-18) |
| **HEGAM** | announced |  | 2026-09-07 | Graphite Business — graphite electrode manufacturing plus 76.5 MW captive power  | verified by a later record date (2026-09-07) |
| **HINDUNILVR** | announced |  | 2025-12-05 | HUL's Ice Cream Business Undertaking, including brands Kwality Wall's, Cornetto  | verified by a later record date (2025-12-05) |
| **INDIAGLYCO** | announced |  | 2026-09-02 | Biopharma Undertaking into Ennature Bio Pharma Limited, and Spirits and Biofuel  | verified by a later record date (2026-09-02) |
| **INOXGREEN** | announced |  | 2026-08-01 | Power Evacuation Business of Inox Green, with associated activities, assets and  | verified by a later record date (2026-08-01) |
| **ITC** | record_date | 2025-01-06 | 2025-01-06 | The Hotels Business of ITC Limited, demerged into ITC Hotels Limited on a going  | verified by the register |
| **NUVAMA** | listed | 2023-09-26 |  | Wealth Management Business Undertaking (including merchant banking business) of  | verified by NSE's equity list — this company is the listed resulting company (listed 2023-09-26) |
| **QUESS** | record_date |  | 2025-04-15 | Quess's Global Technology Solutions platform — BPM services, customer lifecycle  | verified by the register |
| **RAYMOND** | record_date | 2024-07-11 | 2024-07-11; 2025-05-14 | Raymond's lifestyle business undertaking — branded fabric, shirting, branded rea | verified by the register |
| **SANOFI** | record_date | 2024-06-13 | 2024-06-13 | The Consumer Healthcare business (Demerged Undertaking) of Sanofi India, transfe | verified by the register |
| **SANOFICONR** | listed | 2024-09-13 |  | The Consumer Healthcare business of Sanofi India Limited, demerged into wholly o | verified by NSE's equity list — this company is the listed resulting company (listed 2024-09-13) |
| **SIEMENS** | record_date |  | 2025-04-07 | Siemens Limited's Energy Business — products, solutions and services across the  | verified by the register |
| **SKFINDIA** | exchange_noc |  | 2025-10-15 | SKF India's Industrial Business — rolling bearings, seals, rotating shaft servic | verified by a later record date (2025-10-15) |
| **STAR** | listed | 2024-12-11 | 2024-12-06 | Identified CDMO and Soft Gelatin (softgel/oral technologies) businesses of Strid | verified by the register |
| **STLTECH** | record_date |  | 2025-04-24 | Global Services Business — fibre roll-out, end-to-end system integration and net | verified by the register |
| **TMPV** | effective |  | 2025-10-14 | Tata Motors' Commercial Vehicles Business, with its related investments, demerge | verified by a later record date (2025-10-14) |
| **TRIVENI** | announced |  | 2026-07-22 | Power Transmission Business (gears and defence segments) transferred and vested  | verified by a later record date (2026-07-22) |
| **VEDL** | nclt_sanction |  | 2026-05-01 | Aluminium, merchant power, oil & gas and iron ore undertakings of Vedanta Limite | verified by a later record date (2026-05-01) |

## Reading the result

- A register demerger the skill lacks is a miss in CAPTURE; one held as merger or other is a miss in CLASSIFICATION.
- A confirmed demerger with a record date the register does not know is a false positive; one the judge reads as an amalgamation is too.
- Confirmed demergers still before their record date cannot be verified against the register; they are listed as pending, and the register will settle them as it fills.
- A company in NSE's equity list that LISTED within 75 days after the record date, named like the parent or the resulting company read from the scheme, shows the resulting company arriving.
