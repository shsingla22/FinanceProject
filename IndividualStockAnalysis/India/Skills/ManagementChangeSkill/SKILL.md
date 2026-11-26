---
name: management-change
description: Find every NiftyTotalMarket company going through a management change — the promoters / owners changing, or the CEO / MD or CFO changing — from the text of exchange filings, NSE's shareholding and takeover registers, bulk and block deals and the stored conference calls; then give each company's last three years of financials and the track record of the outgoing and the incoming management. Use when asked which companies have a new owner, a new promoter, an open offer, a new CEO, MD or CFO, or to analyse a company after such a change.
---

# ManagementChangeSkill

Two kinds of management change, for every company in the NiftyTotalMarket:

1. **Ownership** — the promoters or owners of the company changing: a change
   of control (completed or in progress), a large stake change under the same
   controller, a hand-over inside the promoter family.
2. **The seat** — the chief executive (CEO, Managing Director, MD & CEO,
   Chairman & Managing Director, an Executive Chairman who is the chief
   executive) or the CFO (or Director (Finance) of a public-sector company)
   changing.

The output is the list of companies first, then for each company: what is
changing (with the documents' words and links), the last three years of
financials, the track record of the outgoing management, the track record of
the incoming management, and what was said on the calls.

## The rule the skill is built on

**A headline decides nothing.** "…has informed the Exchange about change in
Management" is the headline of a new head of internal audit and of a new CEO
alike. Every filing's TEXT is read; the exchange's own registers are read
beside it; a reading model then reads each candidate company's complete
documents and decides; and every name and quote it gives is checked against
the documents before it is reported.

## Sources

| Source | What it shows | Where it is kept |
|---|---|---|
| NSE filings in the management, board and takeover categories — Change in Management, Appointment, Change in Director(s), Resignation, Resignation of Director/KMP/SMP, Cessation, Retirement, Disclosure under SEBI Takeover Regulations, open-offer categories | Read in full (15 pages): PDFs through `pdftotext`, then PyPDF2; a `.zip` is opened and its structured XML read (NSE files resignations as XBRL: `TypeOfChange`, `DesignationOfDesignatedPerson`, `NameOfDesignatedPerson`, `ReasonOfResignationInBrief`); a scanned letter goes through OCR when `rapidocr-onnxruntime` is installed | `ManagementChange/NiftyTotalMarket/_filings.csv.gz`, `text/` |
| Every other material filing — board outcomes, press releases, updates, acquisitions, agreements, schemes, news verification | The first pages the all-filings store already keeps | `Announcements/NiftyTotalMarket/_all_filings.csv.gz` |
| NSE shareholding register | Promoter-and-group % quarter by quarter, with the company's notes | `_shareholding.csv` |
| NSE Regulation 29 feed | Every acquisition or sale disclosed under the takeover code: who, promoter or not, the holding after | `_sast_reg29.csv` |
| NSE bulk and block deals | A client selling or buying a large slice | `_deals.csv` |
| Stored conference calls | What management said; and the transcript's own list of who the CEO / MD / CFO is | `ConferenceCalls/NiftyTotalMarket/` |
| Statements (screener.in, consolidated), annual-report management history, bhavcopy closes | Financials and track records | `ProfitStatement/`, `BalanceSheet/`, `CashFlow/`, `WorkingCapital/`, `ManagementInfo/`, `Announcements/_bhav_bundles/` |

BSE's announcement API and SEBI's site refuse this environment; every
universe company is NSE-listed and Regulation 30 / SAST disclosures go to
both exchanges, so the NSE record is the complete one.

## Steps

1. **Collect** — `ManagementChange/fetch_management_change.py` refreshes the
   all-filings store to today, reads every management / takeover filing of
   the window in full, and pulls the Reg 29 feed, the deals and the
   shareholding register for every member. Re-runs read only what is new;
   `--retry no-text,skipped,failed,zip,short` re-reads what gave no text.
2. **Mechanical read, for recall** (`scripts/mgmt.py`).
   - *The seat*: every mention of a CEO / MD / CFO seat with an appointment
     word or a cessation word inside the same two sentences. A
     re-appointment is recognised and not counted. SEBI's table labels
     ("Reason for change viz. appointment, re-appointment, resignation,
     removal, death or otherwise") are blanked first — they print every event
     word in every filing. A deputy seat, the seat of a division ("CEO –
     Emerging Business"), and a letter addressed to the MD are marked and not
     counted. In a category that is not about management the mention must be
     in the opening of the document.
   - *Ownership*: the promoter holding moved five points, or crossed 50%,
     25% or nil (register); promoters sold 5% or an outsider reached 25%
     (Reg 29); one client sold 5% net (deals); an open-offer filing; or text
     that speaks of control, an open offer or a promoter reclassification
     WITH THIS COMPANY AS THE TARGET (a company buying another is not
     changing hands). Two smaller signs together also qualify.
   - *Calls*: "our new CFO", "taken over as", "stepping down", "open
     offer", "new promoter"; and the roster — a seat whose listed holder
     differs between the first and the last call of the window.
3. **The judge, for precision** (`scripts/analyze.py`, `scripts/judge.py`).
   One forced-choice question per candidate company and kind over its
   COMPLETE documents (all of them when they fit; otherwise every filing's
   opening pages first, then whole filings shortest first).
   - Seat: one entry per seat — outgoing (name, last day, reason, in their
     words, since when), incoming (name, effective date, interim or not,
     internal / external / promoter family, age, qualifications, experience,
     every earlier role with employer and years, the filing's own profile),
     status, the verbatim sentence. Re-appointments, title changes, division
     heads, deputies and other senior management are returned as "not a
     change" with the reason, so the reader sees they were read.
   - Ownership: one of change of control · control change in progress ·
     stake change, same controller · within the promoter family · dilution
     only · none — with the outgoing and incoming owner, stakes, price, mode,
     the open offer, the dates, what changes on the board, and what the
     documents say about the buyer.
   The model is `MGMT_JUDGE_MODEL`, else `ANALYST_MODEL`, else
   `claude-opus-5`, through the `claude` CLI. Answers are cached by the
   documents' content (`.judge_cache.json`).
4. **Check** — a change is reported only when it is a change, falls in the
   window, and the people named are in the documents. Each carries
   `verified` (names and an eight-word run of the quote found in the text);
   an unverified one is printed with a warning.
5. **Analyse each company with a change** (`scripts/track.py`).
   - *Financials*: the last three fiscal years — revenue, operating profit,
     PAT with growth and margins, cash from operations, free cash flow, ROCE,
     ROE, borrowings, debt / equity, working-capital days — computed here
     from the stored statements (lenders use Revenue / Financing profit).
     The share price from the close before the announcement to the latest
     close, beside the Nifty 500; not compared across a split, bonus or
     demerger.
   - *Outgoing*: the company's results while the person held the seat — from
     the fiscal year before they took it to the last full year they held it:
     sales, operating profit and PAT growth a year, margin, ROCE, ROE and
     borrowings start to end. The start comes from the filing, else from the
     annual reports on file (a floor). When neither says, the last five years
     are shown as context only and said to be so. It is the record of the
     company under them, not a claim about what one person caused.
   - *Incoming*: the filing's own profile, age, qualifications, experience
     and earlier roles; seats the annual reports on file show them in at any
     universe company; and — where an earlier TOP seat was at a universe
     company — that company's results in those years. For a new owner: what
     the documents say about the buyer, and its own three years when it is a
     universe company.
   - *Calls*: every question about the change with every answer to it, uncut.
6. **Report** — `MANAGEMENT_CHANGE_REPORT.md`: the counts; List 1 ownership,
   List 2 chief executives, List 3 CFOs; what was read and set aside; then
   each company in five parts. `companies/<SYMBOL>.md` carries the call
   passages in full.
7. **Evaluate** — `scripts/evaluate.py` (below). Run it after every run.

## Run

```bash
cd IndividualStockAnalysis/India
python3 ManagementChange/fetch_management_change.py            # collect (365 days)
python3 ManagementChange/fetch_management_change.py --only filings --no-refresh --retry no-text,skipped,failed,zip,short
cd Skills/ManagementChangeSkill/scripts
python3 analyze.py run --workers 6                             # last 365 days
python3 analyze.py run --only RBLBANK,EPL                      # some companies
python3 analyze.py run --quick                                 # no judge
python3 analyze.py render                                      # re-render the saved run
python3 evaluate.py                                            # the evaluation
python3 -m pytest -q test_skill.py                             # offline tests
```

Optional, for scanned letters: `python3 -m pip install rapidocr-onnxruntime`
(with poppler's `pdftoppm`). Without it a scan is recorded as `no-text` and
shows in the evaluation.

## Outputs — `Analysis/NiftyTotalMarketAnalysis/ManagementChangeAnalysis/`

| File | What |
|---|---|
| `MANAGEMENT_CHANGE_REPORT.md` | The three lists, what was set aside, then each company in five parts |
| `MANAGEMENT_CHANGE_EVAL.md` | The evaluation of that run |
| `companies/<SYMBOL>.md` | One company, with the call passages in full |
| `_seat_changes.csv`, `_ownership_changes.csv` | One row per change |
| `_candidates.csv` | Every company put to the judge, and what became of it |
| `management_change_latest.json`, `_eval.json` | The run and its evaluation |

## Tests and evaluation

`scripts/test_skill.py` — offline: the seat detector (appointment, cessation,
re-appointment, table labels, divisions, deputies, addressees), ownership
language with the company as target, the register / Reg 29 / deals
summaries, the call roster, financials for companies and lenders, tenure
records, name matching, the judge cache and retry, the name-and-quote check,
the window, the document budget, an end-to-end run with a fake judge.

`scripts/evaluate.py` — eight checks of a real run against things its own
detector did not decide:

| | Check | Fails hard when |
|---|---|---|
| E1 | Coverage: every management / takeover filing read, or why not | a filing was never attempted |
| E2 | Ownership vs NSE's shareholding register: every five-point move or threshold crossing carries a verdict | one has no verdict |
| E3 | Every open-offer filing is read as a change of control | — (listed for review) |
| E4 | Call rosters: a seat whose listed holder changed is a reported change | — (listed for review) |
| E5 | A headline that names a CEO / MD / CFO coming or going has a reported change or a recorded reason | — (listed for review) |
| E6 | Management filings whose PDF gave no text | — (listed) |
| E7 | A hand-labelled set of filings (`evals/labelled_filings.csv`): recall and precision of the mechanical flag, recall of the final list | — |
| E8 | Names and quotes of every reported change found in the documents | under 90%, or a judge failure |

An exception a person has read is recorded in
`evals/reviewed_exceptions.csv` (`check,symbol,note`) and shown with its note.

## Limits, stated

- Disclosure is the source: a change a company has not yet told the exchange
  about, or said only in a newspaper, is not here.
- A tenure's start comes from the filing or the annual reports on file (about
  five years back); statements on file start in FY2015.
- An incoming person's record outside the universe is the filing's profile
  only — nothing is added from memory.
- Scanned takeover disclosures are not put through OCR: the same disclosures
  arrive structured in the Reg 29 feed.
- Prices are unadjusted closes.
