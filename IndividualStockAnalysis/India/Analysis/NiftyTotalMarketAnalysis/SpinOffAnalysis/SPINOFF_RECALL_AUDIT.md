# Recall audit — did the skill miss demergers? (window 2025-10-08 → 2026-10-12)

The question asked: are demergers being missed, and can more be captured
without adding noise? Three independent ground truths were built and the
skill's situation list compared against each, before and after the changes
below. Everything here is re-runnable: the raw NSE year sits in the fetcher's
monthly pulls, the corporate-actions and board-meeting feeds are public NSE
endpoints, and the classifier is `Announcements/fetch_announcements.py`.

## 1. Ground truth A — demergers that reached a record date

NSE's corporate-actions feed lists every record date with its purpose. In the
window it carries **8 demerger record dates for universe companies**.

| Record date | Company | In the skill before | After |
|---|---|---|---|
| 2025-10-14 | TMPV (Tata Motors CV) | yes (probable: scheme, nature unclear) | yes |
| 2025-10-15 | SKFINDIA | yes (confirmed) | yes |
| 2025-12-05 | HINDUNILVR | yes (confirmed) | yes |
| 2026-05-01 | VEDL | yes (confirmed) | yes |
| 2026-07-22 | TRIVENI | yes (confirmed) | yes |
| 2026-08-01 | INOXGREEN | yes (confirmed) | yes |
| 2026-09-02 | INDIAGLYCO | yes (confirmed) | yes |
| 2026-09-07 | HEGAM | yes (confirmed) | yes |

**Recall on completed demergers: 8 of 8, before and after.** The skill never
missed a demerger that actually happened. The misses were earlier in the
cycle — schemes announced but not yet at a record date.

## 2. Ground truth B — board-meeting purposes

NSE publishes the stated purpose of every board meeting. Filtering the
universe's 23,185 intimations for demerger / scheme / subsidiary-listing
language gives **9 meetings at 6 companies**. Before the change the skill
had three of them only as other restructurings or not at all:

| Company | Purpose, as filed | Before | After |
|---|---|---|---|
| MTARTECH | "…financial results…, Scheme of Arrangement and other business matters" (Nov 2025) | **missing** | probable (scheme) |
| NATCOPHARM | "To consider Scheme of arrangement (demerger)" (Mar 2026) | other (its rights issue only) | **confirmed demerger** |
| PFC | "to consider Scheme of arrangement" (Jun 2026) | other | probable (scheme) |
| CELLO | board meeting on its composite scheme (May 2026) | dropped by a count rule | **confirmed demerger** |
| THOMASCOOK, ASTRAMICRO | scheme meetings | confirmed | confirmed |

The board-meeting feed is now a source in its own right (`source` = NSE-BM):
66 restructuring purposes in the window.

## 3. Ground truth C — a wide-net scan of the raw year

Every one of the universe's **82,055 filings** was re-read with a deliberately
loose pattern (demerger, spin-off, hive-off, carve-out, scheme of arrangement,
composite scheme, resulting / demerged company, slump sale, business transfer,
subsidiary IPO / DRHP / listing): 349 rows at 111 companies. The classifier had
kept all but 28 of them:

| Dropped rows | Why | Verdict |
|---|---|---|
| 9 | "Copy of Newspaper Publication" — a reprint of a filing already kept | noise, correctly dropped |
| 9 | generic Regulation 30 subsidiary updates (incorporations, name changes, credit ratings) | noise, correctly dropped |
| 2 | COALINDIA "Listing of South Eastern Coalfields / Bharat Coking Coal, a subsidiary" | **miss** — pattern widened |
| 1 | HEGAM record date "in consultation with the Resulting Company" | **miss** — pattern widened |
| 7 | other subsidiary-related updates | noise |

Only two patterns were actually too narrow. The headline read is close to
complete — **for filings whose headline says anything at all.**

## 4. The real blind spot — headlines that say nothing

**1,184 of the universe's 4,770 "Outcome of Board Meeting" filings** carry a
bare headline ("X Ltd has informed the Exchange about Outcome of Board
Meeting"). Only the attachment says what the board approved. The fetcher now
reads the first four pages of every such PDF (`source` = NSE-deep):

- 1,184 PDFs read → **156 were restructuring filings** (demerger 15, scheme 10,
  subsidiary listing 1, merger 54, slump sale 24, rights 69-including-prefs,
  capital action 49).
- **12 companies entered the demerger / scheme list only through this scan:**
  NATCOPHARM, ERIS, LENSKART, BAJAJELEC, AEGISLOG, VIJAYA, CYIENT (subsidiary
  listing), CRAFTSMAN, MANKIND, DIACABS, MTARTECH (with the board feed), PFC.

## 5. Noise taken out at the same time

- **Bare "NCLT" no longer makes a scheme.** Insolvency petitions, resolution
  plans and liquidation orders all cite the tribunal; they were landing as
  "scheme (nature unclear)". A scheme now needs the word scheme beside the
  tribunal.
- **The judge demotes amalgamations.** When the judge, having read the scheme,
  says nothing is separated — amalgamation into the parent, liquidation of a
  subsidiary, an insolvency matter, a reserves reclassification — the situation
  is a merger whatever the keyword count said. Demoted in this window: DABUR
  (Sesa Care amalgamation), AMBUJACEM (Sanghi amalgamation), GODIGIT, SFL
  (Kurlon amalgamation), VIYASH, AGARWALEYE, SUZLON (reserves), LALPATHLAB,
  MAXHEALTH (internal mergers / liquidations), POLYCAB, LICHSGFIN, JPPOWER,
  VIKRAMSOLR, DIACABS-insolvency rows (insolvency matters).
- **Composite schemes stay demergers.** The stricter count rule that fixed
  Dabur had also turned Cello's composite scheme (which demerges *and*
  amalgamates) into a merger; the count rule is permissive again and the
  judge's read, not the count, decides.
- **A subsidiary listing is never an amalgamation.** Prestige's withdrawn
  DRHP had been demoted by an over-broad "not … separation" pattern. The
  demotion now needs explicit amalgamation / liquidation / insolvency words,
  and a withdrawn proposal is its own stage (WITHDRAWN) rather than a loss.
- **Resulting-company names must look like company names** (two capitalised
  words before "Limited", never the parent itself), so fragments like
  "Public Limited" no longer appear in the table.

## 6. Preferential issues and warrants (added on request)

The headline read had dropped **256 filings at 85 universe companies** about
preferential allotments and warrants — Affle 3i's June 2026 warrant allotment
among them. They are now a kind of their own (`preferential_issue`, conversions
included): **241 rows at 80 companies** kept (the rest are monitoring-agency
reports, which are noise). Each offering's text is read for instrument, count,
price and amount, and the judge names every buyer with its category. Affle:
74,00,000 warrants at ₹1,487, 100% to Affle Holdings Pte. Ltd., the promoter.

## 7. Before and after

| | Before | After |
|---|---:|---:|
| Filings kept for the universe | 1,023 | 1,494 |
| Companies with a restructuring filing | 256 | 343 |
| Confirmed demergers | 34 | **42** |
| Probable (schemes of unsettled nature, subsidiary listings) | 22 | 27 |
| Indicated (rumour, denial, withdrawn) | 3 | 4 |
| Rights / preferential offerings with buyers named | 0 | 164 (113 with promoters among the buyers) |
| Record-date demergers captured | 8 / 8 | 8 / 8 |
| Board-meeting-purpose schemes captured | 3 / 6 companies | 6 / 6 |

Companies that entered the spin-off list in this pass: AEGISLOG, BAJAJ-AUTO,
BAJAJELEC, CELLO, CRAFTSMAN, CYIENT, DIACABS, ERIS, LENSKART, MANKIND,
MTARTECH, NATCOPHARM, PFOCUS, PRESTIGE (withdrawn), VIYASH. One left:
SAPPHIRE, whose scheme is its merger with Devyani, now classified as such.

## 8. What still cannot be seen

- A demerger first discussed only inside a quarterly results presentation or
  an annual report, with no exchange filing yet, is caught only if management
  also says it on a call (the "indicated on the calls" list) — 12 companies
  this run.
- Filings whose attachment is a scanned image yield no text; the deep scan
  cannot read them. The fetch log records every PDF without extractable text.
- BSE-only filings before the first run cannot be back-filled from this
  environment; every universe company is NSE-listed, so the NSE record is the
  complete one for Regulation 30 disclosures.
