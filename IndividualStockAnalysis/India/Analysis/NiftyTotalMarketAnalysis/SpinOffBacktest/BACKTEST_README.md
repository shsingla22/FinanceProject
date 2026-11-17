# Backtests of the demerger skill and its ground truth

Two backtests of the SpinOffSkill, each run AS OF a past date over a past window and
checked against NSE's own corporate-actions register for that window. Each folder holds
the run (`SPINOFF_REPORT.md`, `spinoff_latest.json`, `_situations.csv`), the register
check (`SPINOFF_GROUND_TRUTH_CHECK.md`, `_ground_truth_check.csv`) and a one-page
`BACKTEST_SUMMARY.md`.

| Folder | Filings window | As of | Run |
|---|---|---|---|
| `FY2024-25/` | 2024-04-01 → 2025-03-31 | 2025-03-31 | list-only (judge classification and listing status) |
| `2024-04_to_today/` | 2024-04-01 → 2026-11-16 | 2026-11-16 | list-only |

## How a backtest is run

`Skills/SpinOffSkill/scripts/backtest.py --from 2024-04-01 --to 2025-03-31 --label FY2024-25`

- The filings store was first extended back to April 2024 (`Announcements/fetch_announcements.py --days 960`):
  every NSE filing of the universe for 2.6 years (217,524), the first six pages of every
  material one read (95,708), 9,630 restructuring filings across 677 companies with full text.
- The register was built for the same span (`Announcements/demerger_ground_truth.py --days 960`):
  647 daily bhavcopy bundles' corporate-actions files plus the corporate-actions API, 83 demerger
  record dates, 18 of them for universe companies.
- An as-of run sees only filings dated inside its window, calls up to its month, register record
  dates up to its date plus the announced weeks ahead, and NSE's equity list. Nothing later.
- Two parents that left the index after their demerger — Raymond Ltd and Sanofi India — were added
  as extra members (`Announcements/NiftyTotalMarket/_extra_members.csv`), otherwise a backtest over
  FY2024-25 would be judged against record dates for companies it was never shown.

## The ground truth

NSE's corporate-actions register: every record date whose purpose is "Demerger", for a
universe company, inside the window. This is the exchange's own record and the only
independent source: a demerger exists here once it has a record date, so announced
schemes before their record date cannot be tested against it.

| Window | Register demergers | Companies |
|---|---:|---|
| FY2024-25 | 5 | Sanofi India (2024-06-13), Raymond (2024-07-11), CCAvenue (2024-09-11), Strides (2024-12-06), ITC (2025-01-06) |
| April 2024 → today | 18 | the five above, then Siemens (2025-04-07), Quess (2025-04-15), Sterlite Technologies (2025-04-24), Raymond again (2025-05-14, Raymond Realty), Aditya Birla Fashion (2025-05-22), DB Realty (2025-07-18), Tata Motors (2025-10-14), SKF India (2025-10-15), Hindustan Unilever (2025-12-05), Vedanta (2026-05-01), Triveni Engineering (2026-07-22), Inox Green (2026-08-01), India Glycols (2026-09-02), HEG (2026-09-07) |

## The skill's results

| | FY2024-25 as of 2025-03-31 | April 2024 → today as of 2026-11-16 |
|---|---:|---:|
| Register demergers in the window | 5 | 18 |
| Captured as confirmed / probable demergers | 5 | 18 |
| Missed (absent, or held as merger / other) | 0 | 0 |
| Confirmed demergers in the skill | 20 | 39 |
| …verified by a register record date or the company's own listing | 10 | 21 |
| …verified by a record date that came AFTER the as-of date | 9 | — |
| …pending (no record date to date) | 1 | 18 |
| False positives | 0 | 0 |
| Situations in all | 1,380 | 2,182 |

Demergers whose record date is more than two years before the run (Sanofi India and Raymond
Lifestyle in the long window) are marked mature and counted as captured, not confirmed: the
notes' second year is over.

The FY2024-25 run is the stronger test: of 20 demergers it called confirmed on 31 March 2025,
19 have since reached a record date or a listing, and the one that has not — Adani Enterprises'
food-FMCG demerger into Adani Wilmar — was a real scheme on the exchange record that the
company later withdrew (no withdrawal filing fell inside the window).

The production run of 2026-11-16 (400-day window, full report) ends the same way: 8 of 8
register demergers captured, 0 missed, 0 false positives, 32 confirmed demergers.

The 18 pending as of today are mostly schemes in flight with a stated listing: UPL, Astra
Microwave, Lemon Tree (Fleur), Natco (crop health), Apollo Hospitals (Healthtech), Refex,
Religare (Finvest), Anant Raj, Pricol, TVS Motor, Piccadily, Thomas Cook (Sterling), Lloyds
Enterprises, Mahindra Seamless. Four are doubtful and left for the next pass: SCI (land assets
already moved in 2024), M&M (last-mile mobility into an unlisted subsidiary), Texmaco Rail and
Nykaa (internal moves whose listing the documents do not state).

## Partial spin-offs (subsidiary IPOs), added 2026-11-17

Filings flagged as a subsidiary listing are now resolved with one forced-choice question of the
complete documents. A subsidiary, associate or JV listed, or being listed, by IPO is a partial
spin-off and sits in the confirmed list below the demergers; everything else leaves both the
confirmed and the probable lists.

| | FY2024-25 as of 2025-03-31 | April 2024 → today |
|---|---:|---:|
| Partial spin-offs | 11 | 21 |
| …already listed | 4 | 10 |
| …IPO in motion | 7 | 11 |
| Flagged as a subsidiary listing, found not to be one | 12 | 35 |

The FY2024-25 run tests the "IPO in motion" calls: of the seven flagged on 31 March 2025, five
have since listed (Aegis Vopak Terminals, Brigade Hotel Ventures, Canara HSBC Life, EAAA India
Alternatives, HDB Financial Services), one was shelved (Greaves Electric Mobility) and one is
still pending (Belstar Microfinance). The register check is unchanged in both windows: every
register demerger captured, no false positives.

The backtests also showed a subsidiary IPO hiding behind a demerger mention (HDFC Bank's HDB
Financial, Amber's IL JIN): a company is one situation and a demerger tag outranked a listing tag.
The listing question is now asked there too.

## What the backtests taught, now in the skill

Every change below came from a named case in one of the two windows; each has a test.

1. **The exchange's record date rules.** When the register has the company, its record date
   sets the stage and the listing date (ITC's filings yielded a June 2024 dividend record date
   for a demerger whose record date was 6 January 2025), the register is read up to 45 days
   ahead because the file shows announced dates (Siemens, 7 April 2025 was in the file in
   March), and no judge-based rule may demote a company the register says demerged (CCAvenue).
2. **SEBI's own listing answer.** The Regulation 30 disclosure line "Whether listing would be
   sought for the resulting entity" is parsed filing by filing; a "No" or "Not applicable" from
   every answering filing, and no "Yes", means a reorganisation inside the group (Deepak
   Fertilisers, Motherson). A "Yes" anywhere keeps the demerger (Raymond's May 2024 "No" was
   about another scheme).
3. **Direction by every name and in the filing's own voice.** A renamed company's filings carry
   the old name in the headline (Adani Wilmar, now AWL Agri Business); role aliases inside the
   parenthesis are read (Kitex: "(“KGL” or “Resulting Company”)"); "shares issued by the Company
   to the shareholders of …" is inbound (Cello).
4. **The judge's words.** A slump sale or a move to a wholly-owned subsidiary with no listing
   stated (Tata Communications), "no listed-shareholder spin-off" (DLF), a separation the judge
   dates two years before the filings (GMR's 2022 demerger), a listing question answered "No new
   listing" (GMR), a scheme the judge says was withdrawn (Astral), "not stated … no demerger"
   (Adani Enterprises today), and a read opening "Not stated — the documents describe an
   amalgamation" (Viyash) each move the situation off the confirmed list — while "No listing
   date stated" is read as silence, not a no.
5. **A news headline is not a scheme.** The exchange asking about a news item that says
   "demerge" never puts a scheme on the record (Amber).
6. **A resulting company already listed before the filings**, with nothing expected, is history
   the filings still mention (SCI's land company), unless the documents say when the shares
   will list (Adani Enterprises' holders receiving listed Adani Wilmar shares).

## Caveats

- The universe is today's NiftyTotalMarket (plus the two extra parents); a company that was a
  member in 2024 and is not today is outside both the register and the skill.
- Record dates verify completed demergers; the pending lists rest on scheme filings alone.
- Both runs are list-only; the production report adds rationale, numbers and documents.
