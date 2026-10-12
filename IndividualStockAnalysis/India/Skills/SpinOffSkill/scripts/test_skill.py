"""
SpinOffSkill tests.

  cd IndividualStockAnalysis/India/Skills/SpinOffSkill
  python3 -m pytest scripts/test_skill.py -q

Every test is offline: the fetcher's parsers run on captured fixtures,
the analysis on synthetic filings and texts, the CLI on a temporary
output folder with the judge stubbed. The arithmetic of the notes
(Sears' stub, Host Marriott's leverage) is checked against the notes'
own numbers.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent.parent / "Announcements"))

import fetch_announcements as FA     # noqa: E402
import spinoff as SO                 # noqa: E402
import analyze as AZ                 # noqa: E402
import financials as FN              # noqa: E402

TODAY = dt.date(2026, 10, 8)


# ================================================================ fetcher

def test_classify_reads_category_and_headline():
    assert FA.classify("Scheme of Arrangement", "Approval of Composite Scheme by NCLT") \
        == ("scheme_other", ["scheme_other"])
    k, tags = FA.classify("Updates", "Demerger of Commercial Vehicles business of Tata Motors")
    assert k == "demerger" and "demerger" in tags
    k, tags = FA.classify("Amalgamation/Merger", "Scheme of Amalgamation of a WOS")
    assert k == "merger" and "merger" in tags
    # a scheme that demerges is a demerger even if it also merges parts
    k, _ = FA.classify("Scheme of Arrangement",
                       "Composite scheme: demerger of the energy business and amalgamation of X")
    assert k == "demerger"
    assert FA.classify("Rights Issue", "Letter of offer") == ("rights_issue", ["rights_issue"])
    k, _ = FA.classify("Updates", "Board approved the IPO of its material subsidiary")
    assert k == "subsidiary_listing"
    k, _ = FA.classify("Updates", "Slump sale of the motors business to Innomotics")
    assert k == "slump_sale"
    assert FA.classify("Updates", "Appointment of CFO") == ("", [])
    assert FA.classify("Demerger", "anything") == ("demerger", ["demerger"])


def test_classify_ignores_noise_categories_whatever_they_say():
    noisy = "Certificate under SEBI (Depositories and Participants) Regulations, 2018"
    assert FA.classify(noisy, "demerged shares credited") == ("", [])
    assert FA.classify("Issue of Duplicate Share Certificate(s)", "pursuant to merger") == ("", [])
    assert FA.classify("Copy of Newspaper Publication", "notice of demerger meeting") == ("", [])


def test_nse_rows_keep_only_universe_restructuring_filings():
    feed = [
        {"symbol": "TMPV", "an_dt": "03-Oct-2025 18:02:11", "desc": "Updates",
         "attchmntText": "Demerger of Commercial Vehicles business", "seq_id": "1",
         "attchmntFile": "https://nsearchives.nseindia.com/corporate/a.pdf", "attFileSize": "1.2 MB"},
        {"symbol": "TMPV", "an_dt": "03-Oct-2025 18:02:12", "desc": "Appointment",
         "attchmntText": "Appointment of director", "seq_id": "2", "attchmntFile": ""},
        {"symbol": "NOTINIDX", "an_dt": "03-Oct-2025 18:02:13", "desc": "Demerger",
         "attchmntText": "Demerger", "seq_id": "3", "attchmntFile": ""},
    ]
    rows = FA.nse_rows(feed, {"TMPV": "Tata Motors Passenger Vehicles Ltd."})
    assert [r["ann_id"] for r in rows] == ["1"]
    r = rows[0]
    assert r["date"] == "2025-10-03" and r["source"] == "NSE" and r["kind"] == "demerger"
    assert r["company"].startswith("Tata Motors") and r["file_size"] == "1.2 MB"
    assert set(r) == set(FA.FIELDS)


def test_month_windows_cover_the_lookback_in_month_sized_pieces():
    w = FA.month_windows(dt.date(2026, 10, 8), 365)
    assert w[0][0] == dt.date(2025, 10, 8) and w[-1][1] == dt.date(2026, 10, 8)
    for (a, b), (c, _) in zip(w, w[1:]):
        assert c == b + dt.timedelta(days=1) and (b - a).days <= 31
        assert a.month == b.month


def test_bse_rss_parses_items_with_scrip_codes_and_dates():
    xml = """<rss><channel><item><title>Persistent Systems Ltd (533179)</title>
    <link>https://www.bseindia.com/xml-data/corpfiling/AttachLive/779e.pdf</link>
    <scripcode>533179</scripcode><description>Intimation of   demerger</description>
    <pubDate>08-Oct-2026 09:50:18</pubDate></item></channel></rss>"""
    rows = FA.parse_bse_rss(xml)
    assert rows == [{"bse_code": "533179", "company": "Persistent Systems Ltd",
                     "headline": "Intimation of demerger",
                     "link": "https://www.bseindia.com/xml-data/corpfiling/AttachLive/779e.pdf",
                     "date": "2026-10-08"}]


def test_screener_company_page_yields_ids_and_announcements_parse():
    html = ('<div data-company-id="3245"></div> <a href="https://www.bseindia.com/'
            'stock-share-price/sun-pharmaceutical-industries-ltd/sunpharma/524715/">BSE</a>')
    assert FA.parse_screener_company(html) == {"screener_id": "3245", "bse_code": "524715"}
    li = ('<ul><li><a href="https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=abc.pdf">'
          ' Scheme of Arrangement <div class="ink-600 smaller"><time datetime="2026-10-07T20:39:11'
          '+05:30">7 Oct</time> - Approval of demerger by NCLT &amp; listing</div></a></li>'
          '<li><a href="https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=def.pdf">'
          ' Newspaper Publication <span><time>12 Oct 2025</time></span></a></li></ul>')
    rows = FA.parse_screener_announcements(li, 2026)
    assert rows[0]["date"] == "2026-10-07" and rows[0]["headline"].startswith("Scheme of Arrangement")
    assert "demerger by NCLT & listing" in rows[0]["note"]
    assert rows[1]["date"] == "2025-10-12"
    assert FA.bse_pdf_url(rows[0]["link"]).endswith("/AttachLive/abc.pdf")


def test_merge_rows_adds_never_duplicates_and_keeps_text_files():
    old = [{"source": "NSE", "ann_id": "1", "date": "2026-01-01", "symbol": "A", "text_file": "text/A_1.txt"}]
    new = [{"source": "NSE", "ann_id": "1", "date": "2026-01-01", "symbol": "A", "text_file": ""},
           {"source": "NSE", "ann_id": "2", "date": "2026-01-02", "symbol": "A", "text_file": ""}]
    m = FA.merge_rows(old, new)
    assert [r["ann_id"] for r in m] == ["1", "2"]
    assert m[0]["text_file"] == "text/A_1.txt"


def test_universe_is_the_official_index_list_only():
    u = FA.universe()
    assert 700 <= len(u) <= 800, len(u)
    assert "SUNPHARMA" in u and "RELIANCE" in u


# =============================================================== analysis

SCHEME = """
SCHEME OF ARRANGEMENT between Alpha Industries Limited ("Demerged Company") and
Alpha Energy Limited ("Resulting Company") and their respective shareholders.
RATIONALE: The demerger will unlock value for shareholders and allow focused
management of two distinct businesses with different risk profiles, each
attracting a distinct set of investors. The Energy business is capital intensive.
"Demerged Undertaking" means the Energy business of the Demerged Company
comprising all assets and liabilities pertaining to the energy segment.
The Energy business contributed 18% of the consolidated revenue in FY25.
Share Entitlement Ratio: 1 (One) fully paid-up equity share of Rs. 2 each of the
Resulting Company for every 1 (One) fully paid-up equity share of Rs. 2 each held
in the Demerged Company. Appointed Date: 1st April 2025. Record Date for the
purpose of the Scheme shall be 15th September 2026.
Pro forma financial statements of the Resulting Company are annexed.
The promoters shall continue to hold the same percentage shareholding in the
Resulting Company. Stock options granted under the ESOP 2020 shall be adjusted
and the exercise price determined on the record date.
"""


def test_facts_in_reads_ratio_entities_dates_and_incentives():
    f = SO.facts_in(SCHEME)
    assert f["entitlement_ratio"] == "1 for every 1"
    assert f["resulting_company"] == "Alpha Energy Limited"
    assert f["demerged_undertaking"].startswith("the Energy business")
    assert f["record_date"] == "2026-09-15" and f["appointed_date"] == "2025-04-01"
    assert f["pro_forma"] is True
    assert "exercise price" in f["esop_pricing"]
    assert "promoters shall continue" in f["insider_continuity"]
    assert f["small_share"] == "18% of revenue"
    # the other drafting order is read too
    g = SO.facts_in('between X Ltd ("Demerged Company") and the Resulting Company, i.e. Beta Power Limited')
    assert g["resulting_company"] == "Beta Power Limited"


def test_reasons_are_classified_into_the_notes_five_with_quotes():
    rs = {r["reason"]: r["quote"] for r in SO.reasons_in(SCHEME)}
    assert "unrelated businesses separated" in rs
    assert "value unlocking for shareholders" in rs
    assert "a weak or capital-heavy business carved away" in rs
    assert "attracting different investors / capital" in rs
    assert "unlock value" in rs["value unlocking for shareholders"]
    # Regulation 30 boilerplate is not a regulatory reason
    assert SO.reasons_in("Disclosure pursuant to Regulation 30 of SEBI (Listing Obligations "
                         "and Disclosure Requirements) Regulations, 2015") == []


def test_stage_of_reaches_the_furthest_stage_named():
    assert SO.stage_of("Board approved the proposed demerger") == "announced"
    assert SO.stage_of("Receipt of No Objection letter from the exchange") == "exchange_noc"
    assert SO.stage_of("NCLT convened meeting of equity shareholders") == "meetings"
    assert SO.stage_of("Approval of Composite Scheme of Arrangement by NCLT") == "nclt_sanction"
    assert SO.stage_of("Record date for the purpose of the scheme") == "record_date"
    assert SO.stage_of("Listing and commencement of trading of equity shares of the "
                       "resulting company") == "listed"
    assert SO.stage_of("Appointment of director") is None


def test_refine_kind_reads_the_scheme_text():
    row = {"kind": "scheme_other"}
    assert SO.refine_kind(row, SCHEME + " demerger demerger") == "demerger"
    assert SO.refine_kind(row, "amalgamation of the WOS; merger; amalgamation; amalgamation") == "merger"
    assert SO.refine_kind(row, "") == "scheme_other"
    assert SO.refine_kind({"kind": "rights_issue"}, SCHEME) == "rights_issue"


def _rows():
    mk = lambda i, d, cat, head, kind, tags=None: {        # noqa: E731
        "date": d, "symbol": "ALPHA", "company": "Alpha Industries Ltd.", "source": "NSE",
        "category": cat, "kind": kind, "tags": tags or kind, "headline": head,
        "attachment": f"https://x/{i}.pdf", "ann_id": str(i), "file_size": "1 MB", "text_file": ""}
    return [
        mk(1, "2026-01-10", "Outcome of Board Meeting", "Board approved the proposed demerger of the Energy business", "demerger"),
        mk(2, "2026-03-02", "Scheme of Arrangement", "Receipt of No Objection letter from NSE on the Scheme", "scheme_other"),
        mk(3, "2026-06-20", "Scheme of Arrangement", "Approval of the Scheme of Arrangement by NCLT", "scheme_other"),
        mk(4, "2026-09-01", "Record Date", "Record date for the demerger fixed as 15 September 2026", "demerger"),
        mk(5, "2026-02-01", "Amalgamation/Merger", "Amalgamation of a wholly owned subsidiary", "merger"),
    ]


def test_build_situations_groups_walks_stages_and_gathers_facts():
    texts = {"3": SCHEME}
    sits = SO.build_situations(_rows(), texts, TODAY)
    assert [s["kind"] for s in sits] == ["demerger", "merger"]      # spin-offs first
    s = sits[0]
    assert s["n_filings"] == 4 and s["first_filing"] == "2026-01-10"
    assert list(s["stage_dates"]) == ["announced", "exchange_noc", "nclt_sanction", "record_date"]
    assert s["stage"] == "record_date" and s["listed_on"] == "2026-09-15"   # the record date itself
    assert s["facts"]["resulting_company"] == "Alpha Energy Limited"
    assert s["facts"]["entitlement_ratio"] == "1 for every 1"
    assert {r["reason"] for r in s["reasons"]} >= {"value unlocking for shareholders"}
    assert s["days_since_first"] == (TODAY - dt.date(2026, 1, 10)).days
    # the bare 'Scheme of Arrangement' row was re-read as a demerger from its text
    assert [h["kind"] for h in s["headlines"] if h["date"] == "2026-06-20"] == ["demerger"]


def test_checklist_and_verdict_follow_the_notes():
    sits = SO.build_situations(_rows(), {"3": SCHEME}, TODAY)
    s = sits[0]
    fin = {"industry": "Capital Goods", "borrowings_cr": 500.0, "borrowings_year": "Mar 2026",
           "market_cap_cr": 10000.0, "debt_to_market_cap": 0.05, "net_profit_cr": 1000.0,
           "net_profit_cr_year": "Mar 2026", "pe_on_latest_profit": 10.0,
           "industry_median_pe": 30.0, "industry_peers": 20}
    mentions = [{"call": "May 2026", "term": "demerger", "quote": "the demerger is on track"}]
    items = {i["item"]: i for i in SO.checklist(s, fin, mentions, TODAY)}
    assert items["Why the spin-off"]["status"] == "yes"
    assert items["Institutional selling likely (small / different business)"]["status"] == "yes"
    assert items["Insider ownership and incentives aligned"]["status"] == "partly"
    assert items["A hidden value revealed (pro-forma, leverage, comparables)"]["status"] == "yes"
    assert items["Parent before the spin (clean parent, takeover prelude)"]["status"] == "no"
    assert items["Timing (first year sells, second year gains)"]["status"] == "partly"
    assert items["Management discussing it on the calls"]["status"] == "yes"
    v = SO.verdict(s, list(items.values()))
    assert v["label"].startswith("SPINNING") and 7 <= v["score"] <= 10   # record date 23 days ago
    later = dt.date(2026, 11, 1)
    s2 = SO.build_situations(_rows(), {"3": SCHEME}, later)[0]
    assert SO.verdict(s2, SO.checklist(s2, fin, mentions, later))["label"].startswith("LISTED <1Y")
    # a pre-spin situation points at the parent
    pre = SO.build_situations(_rows()[:2], {}, TODAY)[0]
    assert pre["stage"] == "exchange_noc"
    assert SO.verdict(pre, SO.checklist(pre, {}, [], TODAY))["label"].startswith("PRE-SPIN")
    # a merger is named for what it is
    m = sits[1]
    assert SO.verdict(m, SO.checklist(m, {}, [], TODAY))["label"].startswith("MERGER")


def test_timing_moves_from_first_year_to_second_year_to_mature():
    rows = _rows()[:4]
    for today, expect in ((dt.date(2026, 12, 1), "LISTED <1Y"), (dt.date(2027, 12, 1), "LISTED 1–2Y"),
                          (dt.date(2029, 1, 1), "MATURE")):
        s = SO.build_situations(rows, {}, today)[0]
        assert SO.verdict(s, SO.checklist(s, {}, [], today))["label"].startswith(expect)


def test_sears_stub_and_host_marriott_leverage_match_the_notes():
    # Sears $54; Dean Witter 136m sh at $37 → $15; Allstate 340m at $29 → $29; stub ≈ $10
    r = SO.stub_value(54, 340e6, [(37, 136e6), (29, 340e6)])
    assert r["stake_values_per_parent_share"] == pytest.approx([14.8, 29.0], abs=0.05)
    assert r["stub_per_share"] == pytest.approx(10.2, abs=0.05)
    # Host: stock $3–5, debt ~$25/share: a ~15% rise in assets doubles the stock
    h = SO.leverage_doubling(4, 25)
    assert h["asset_rise_to_double_equity_pct"] == pytest.approx(13.8, abs=0.1)
    assert SO.leverage_doubling(0, 25) == {}


CALLS = """Alpha Industries Ltd. (ALPHA)
Conference call transcripts, oldest-first.
Call: Feb 2025
We have no plans to restructure. Demerger is not on the table.
Call: Nov 2025
On the demerger of the energy business: the scheme has been filed with the exchanges,
and we expect value unlocking for shareholders.
Call: May 2026
The spin-off is on track; record date will be announced. Separate listing targeted for Q3.
"""


def test_concall_mentions_window_the_last_twelve_months_with_quotes():
    secs = SO.concall_sections(CALLS)
    assert [l for l, _ in secs] == ["Call: Feb 2025", "Call: Nov 2025", "Call: May 2026"]
    ms = SO.concall_mentions(CALLS, today=TODAY)
    calls = {m["call"] for m in ms}
    assert calls == {"Nov 2025", "May 2026"}                 # Feb 2025 is outside the year
    terms = {m["term"].lower() for m in ms}
    assert "demerger" in terms and "spin-off" in terms and "separate listing" in terms
    assert all(m["quote"] for m in ms)
    assert SO.concall_mentions("no sections here", today=TODAY) == []


def test_financial_picture_reads_the_stored_statements_and_market_file():
    live = {"X": {"market_cap_rs_cr": "1000", "current_price_rs": "100", "stock_pe": "20", "fetched_at": "2026-08-02"},
            "P1": {"stock_pe": "30"}, "P2": {"stock_pe": "10"}, "P3": {"stock_pe": "40"}}
    ind = {"X": "Tools", "P1": "Tools", "P2": "Tools", "P3": "Tools"}
    f = SO.financial_picture("X", live, ind)
    assert f["market_cap_cr"] == 1000 and f["industry_median_pe"] == 30 and f["industry_peers"] == 3
    # a real company on file: numbers carry their year and source
    g = SO.financial_picture("SIEMENS")
    assert g["industry"] and g.get("borrowings_year") and g.get("net_profit_cr_year")


# ==================================================================== CLI

def test_judge_is_cached_by_document_and_abstains_without_a_runner(tmp_path, monkeypatch):
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    sit = {"symbol": "ALPHA", "company": "Alpha", "kind": "demerger", "stage": "listed",
           "first_filing": "2026-01-10", "facts": {}}
    calls = []
    def runner(prompt):
        calls.append(prompt)
        assert "Alpha" in prompt and "STRICT JSON" in prompt
        return 'preamble {"what_is_spun": "Energy", "reason": "focus", "reason_class": "unrelated", "quote": "q"} tail'
    j = AZ.judge(sit, SCHEME, [], allow_ai=True, runner=runner)
    assert j["status"] == "judged" and j["what_is_spun"] == "Energy"
    j2 = AZ.judge(sit, SCHEME, [], allow_ai=True, runner=runner)
    assert j2["status"] == "cached" and len(calls) == 1
    # a changed document re-judges; --quick abstains honestly
    AZ.judge(sit, SCHEME + " changed", [], allow_ai=True, runner=runner)
    assert len(calls) == 2
    assert AZ.judge({**sit, "symbol": "BETA"}, SCHEME, [], allow_ai=False)["status"] == "not assessed"
    assert AZ.judge({**sit, "symbol": "BETA"}, SCHEME, [], runner=lambda p: "garbage")["status"].startswith("judge failed")


def test_run_writes_report_record_csvs_and_snapshot(tmp_path, monkeypatch):
    rows = _rows()
    texts = {"3": SCHEME}
    out = tmp_path / "out"
    monkeypatch.setattr(AZ, "OUT_DIR", out)
    monkeypatch.setattr(AZ, "REPORT", out / "SPINOFF_REPORT.md")
    monkeypatch.setattr(AZ, "LATEST", out / "spinoff_latest.json")
    monkeypatch.setattr(AZ, "SITUATIONS", out / "_situations.csv")
    monkeypatch.setattr(AZ, "MENTIONS", out / "_concall_mentions.csv")
    monkeypatch.setattr(AZ, "HISTORY", out / "history")
    monkeypatch.setattr(AZ, "COVERAGE", out / "_coverage.csv")
    monkeypatch.setattr(AZ, "CACHE", tmp_path / "cache.json")
    monkeypatch.setattr(SO, "load_filings", lambda path=None: rows)
    monkeypatch.setattr(SO, "load_text", lambda r: texts.get(r["ann_id"], ""))
    monkeypatch.setattr(SO, "concall_text", lambda sym: CALLS if sym == "ALPHA" else "")
    monkeypatch.setattr(FA, "universe", lambda: {"ALPHA": "Alpha Industries Ltd.", "BETA": "Beta"})
    monkeypatch.setattr(AZ, "_ai_available", lambda: False)

    monkeypatch.setattr(FN, "PNL", tmp_path / "pnl")
    monkeypatch.setattr(FN, "CASH", tmp_path / "cash")
    monkeypatch.setattr(FN, "PPT_DIR", tmp_path / "ppt")
    monkeypatch.setattr(FN, "AR_DIR", tmp_path / "ar")
    monkeypatch.setattr(FN, "LINKS", tmp_path / "ppt" / "_concall_links.csv")
    monkeypatch.setattr(FN, "CONCALLS", tmp_path / "cc")
    _write_pnl(tmp_path / "pnl" / "ALPHA.csv")

    class A:
        refresh = False; days = 365; no_bse = True; quick = True; no_calls = False; only = ""
        fetch_docs = False
    AZ.cmd_run(A())
    md = (out / "SPINOFF_REPORT.md").read_text()
    assert "# Spin-offs and demergers" in md
    assert "## Confirmed demergers" in md and "| **ALPHA** | Alpha Energy Limited | record_date | RECORD DATE 2026-09-15" in md
    assert "> **Listing:** RECORD DATE 2026-09-15; Alpha Energy Limited not yet listed" in md
    assert "### The parent, last three fiscal years" in md and "| Sales (₹ cr) | 100 | 120 | 150 |" in md
    assert "| Sales growth (%) | +25.0% | +20.0% | +25.0% |" in md and "```mermaid" in md
    assert "**P/E:**" in md and "### The business being separated" in md
    assert "Alpha Energy Limited" in md and "1 for every 1" in md
    assert "SPINNING" in md and "On the calls" in md
    assert "Other restructurings on file" in md and "| ALPHA | merger |" in md
    assert "mechanical read only" in md
    rec = json.loads((out / "spinoff_latest.json").read_text())
    assert rec["meta"]["filings"] == 5 and rec["situations"][0]["judge"]["status"] == "not assessed"
    assert rec["situations"][0]["confidence"][0] == "confirmed"
    sits = list(csv.DictReader(open(out / "_situations.csv")))
    assert [s["kind"] for s in sits] == ["demerger", "merger"]
    assert sits[0]["resulting_company"] == "Alpha Energy Limited" and sits[0]["listing"] == "pending_record_date_set"
    cov = list(csv.DictReader(open(out / "_coverage.csv")))
    assert cov[0]["symbol"] == "ALPHA" and cov[0]["parent_pnl"] == "yes" and cov[0]["cash_flow"] == "no"
    ms = list(csv.DictReader(open(out / "_concall_mentions.csv")))
    assert {m["symbol"] for m in ms} == {"ALPHA"} and all(m["quote"] for m in ms)
    snap = out / "history" / dt.date.today().isoformat()
    assert (snap / "run.json").exists() and (snap / "SPINOFF_REPORT.md").exists()


def test_call_only_scan_finds_indications_without_filings(monkeypatch):
    monkeypatch.setattr(SO, "concall_text", lambda sym: CALLS if sym == "GAMMA" else "")
    c = AZ.call_only_scan(["GAMMA", "DELTA"], exclude=set(), today=TODAY)
    assert [x["symbol"] for x in c] == ["GAMMA"] and c[0]["n"] >= 2
    assert c[0]["latest"] == "May 2026" and c[0]["example"] and c[0]["forward"] >= 1
    assert AZ.call_only_scan(["GAMMA"], exclude={"GAMMA"}, today=TODAY) == []
    # a company only describing a past demerger, or denying one, is not an indication
    past = "Call: May 2026\nOne year post our demerger we completed the integration. We have no plan to demerge further."
    monkeypatch.setattr(SO, "concall_text", lambda sym: past)
    assert AZ.call_only_scan(["OLD"], exclude=set(), today=TODAY) == []


def test_tone_separates_plans_from_history_and_denials():
    assert SO.tone("we are evaluating a demerger of the energy business; the board will consider it next quarter") == "forward"
    assert SO.tone("one year post our demerger, the integration was completed") == "backward"
    assert SO.tone("there is no plan to demerge, as you said, at the moment") == "backward"
    ms = SO.concall_mentions(CALLS, today=TODAY)
    assert all("tone" in m for m in ms) and any(m["tone"] == "forward" for m in ms)


def test_boilerplate_does_not_read_as_stages_facts_or_reasons():
    boiler = ("Disclosure under Regulation 30 of SEBI (Listing Obligations and Disclosure "
              "Requirements) Regulations, 2015 — Listing Regulations. The scheme is subject to "
              "receipt of regulatory approvals. Details of pending actions against the Company, "
              "its promoters: nil. Pursuant to the above, equity shares were credited. Announcement.")
    assert SO.stage_of(boiler) is None
    f = SO.facts_in(boiler)
    assert "esop_pricing" not in f and "insider_continuity" not in f
    assert "insider_oversubscribe" not in SO.facts_in(boiler, rights=False)
    assert SO.reasons_in(boiler) == []
    assert SO.stage_of("Listing and commencement of trading of the equity shares of SKF "
                       "Industrial Limited (resulting company)") == "listed"
    assert SO.stage_of("Board approved the Scheme of Arrangement for demerger") == "announced"
    # a scheme's text that PROMISES a listing is not a listing event: stages come from headlines
    row = {"date": "2026-02-20", "symbol": "U", "company": "U", "source": "NSE", "category": "Scheme of Arrangement",
           "kind": "demerger", "tags": "demerger", "headline": "UPL has informed the Exchange about Scheme of Arrangement",
           "attachment": "", "ann_id": "77", "file_size": "", "text_file": ""}
    s = SO.build_situations([row], {"77": "the equity shares of the Resulting Company shall be listed on the stock exchanges"}, TODAY)[0]
    assert s["stage"] == "announced" and "listed" not in s["stage_dates"]
    g = SO.facts_in('between Alpha Ltd and JSW Energy Limited ("Resulting Company")')
    assert g["resulting_company"] == "JSW Energy Limited"
    assert "demerged_undertaking" not in SO.facts_in('"Demerged Undertaking" as defined in the Scheme;')


def test_news_only_filings_are_a_rumoured_situation():
    rows = [{"date": "2026-09-30", "symbol": "SUNTV", "company": "Sun TV", "source": "NSE",
             "category": "News Verification", "kind": "demerger", "tags": "demerger",
             "headline": "The Exchange has sought clarification w.r.t. news item captioned "
                         "Possible sports division demerger", "attachment": "", "ann_id": "9",
             "file_size": "", "text_file": ""},
            {**{"date": "2026-09-30", "symbol": "SUNTV", "company": "Sun TV", "source": "NSE",
                "category": "Clarification", "kind": "demerger", "tags": "demerger",
                "headline": "Sun TV denies CNBC-TV18 rumor of possible sports division demerger",
                "attachment": "", "ann_id": "10", "file_size": "", "text_file": ""}}]
    s = SO.build_situations(rows, {}, TODAY)[0]
    assert s["stage"] == "rumoured" and s["facts"].get("news_only") is True
    assert SO.verdict(s, SO.checklist(s, {}, [], TODAY))["label"].startswith("RUMOURED")



# ============================================================= financials

def _write_pnl(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(",parent_line_item,Mar 2023,Mar 2024,Mar 2025,Mar 2026\n"
                    "Sales,,80,100,120,150\nOperating Profit,,8,12,18,30\nOPM %,,10,12,15,20\n"
                    "Net Profit,,4,5,9,15\nEPS in Rs,,2,2.5,4.5,7.5\n")


def test_parent_financials_three_years_with_growth_and_margins(tmp_path, monkeypatch):
    monkeypatch.setattr(FN, "PNL", tmp_path)
    _write_pnl(tmp_path / "X.csv")
    f = FN.parent_financials("X")
    assert f["available"] and f["years"] == ["Mar 2024", "Mar 2025", "Mar 2026"]
    rows = {r["metric"]: r["values"] for r in f["rows"]}
    assert rows["Sales (₹ cr)"] == [100, 120, 150]
    assert rows["Sales growth (%)"] == [25.0, 20.0, 25.0]          # 80→100 uses the fourth year
    assert rows["Operating margin (%)"] == [12.0, 15.0, 20.0]
    assert rows["PAT growth (%)"] == [25.0, 80.0, 66.7] and rows["PAT margin (%)"] == [5.0, 7.5, 10.0]
    assert not FN.parent_financials("NOPE")["available"]
    charts = FN.charts_for(f)
    assert len(charts) == 2 and 'x-axis ["Mar 2024", "Mar 2025", "Mar 2026"]' in charts[0]
    assert "bar [100, 120, 150]" in charts[0] and "line [12, 15, 20]" in charts[1]


def test_mermaid_chart_leaves_out_series_with_gaps():
    c = FN.mermaid_chart("t", ["a", "b"], {"ok": [1, 2], "gap": [1, None]}, "y")
    assert "bar [1, 2]" in c and "gap" in c and "Not plotted" in c
    assert FN.mermaid_chart("t", ["a", "b"], {"gap": [1, None]}, "y") == ""


def test_cash_flows_and_pe_fallback(tmp_path, monkeypatch):
    monkeypatch.setattr(FN, "CASH", tmp_path)
    (tmp_path / "X.csv").write_text(",parent_line_item,Mar 2024,Mar 2025,Mar 2026\n"
                                    "Cash from Operating Activity,,10,20,30\nFree Cash Flow,,5,8,12\n")
    cf = FN.cash_flows("X")
    assert cf["available"] and cf["years"] == ["Mar 2024", "Mar 2025", "Mar 2026"]
    assert {r["metric"]: r["values"] for r in cf["rows"]}["Free cash flow (₹ cr)"] == [5, 8, 12]
    # P/E: live file first, else close ÷ EPS with the method stated
    assert FN.pe_ratio("X", {"X": {"stock_pe": "22.5", "current_price_rs": "100", "fetched_at": "2026-08-02"}})["pe"] == 22.5
    monkeypatch.setattr(FN, "PNL", tmp_path)
    _write_pnl(tmp_path / "X.csv")
    monkeypatch.setattr(FN, "_CLOSE_CACHE", {"X": ("2026-10-01", 150.0)})
    pe = FN.pe_ratio("X", {})
    assert pe["pe"] == 20.0 and "EPS 7.5" in pe["method"] and pe["as_of"] == "2026-10-01"
    assert FN.pe_ratio("NONE", {})["pe"] is None


def test_segment_excerpts_pick_number_dense_pages_with_the_business_name(tmp_path, monkeypatch):
    monkeypatch.setattr(FN, "AR_DIR", tmp_path / "ar")
    monkeypatch.setattr(FN, "PPT_DIR", tmp_path / "ppt")
    monkeypatch.setattr(FN, "LINKS", tmp_path / "ppt" / "_concall_links.csv")
    d = tmp_path / "ar" / "X"; d.mkdir(parents=True)
    (d / "_index.csv").write_text("symbol,kind,label,url,file,text_file,pages,status,fetched\n"
                                  "X,annual_report,Annual Report 2026,https://b/ar.pdf,a.pdf,a.txt,3,ok,2026-10-12\n")
    (d / "a.txt").write_text("\n=== page 1 ===\nSterling is our hospitality arm. Segment information follows later.\n"
                             "\n=== page 2 ===\nSegment revenue: Travel 5,000 Sterling 450 Forex 1,200; Segment results Sterling 85\n"
                             "\n=== page 3 ===\nNothing here\n")
    ex = FN.segment_excerpts("X", ["Sterling Holiday Resorts Limited"])
    # page 3 rides along as the continuation of the segment table on page 2
    assert [e["page"] for e in ex] == [1, 2, 3] and ex[1]["numbers"] > ex[0]["numbers"]
    # the segment note is wanted even when it never names the brand
    (d / "a.txt").write_text("\n=== page 1 ===\nSegment revenue " + " ".join(f"{i*113:,}" for i in range(30)) + "\n")
    assert [e["page"] for e in FN.segment_excerpts("X", ["Sterling"])] == [1]
    assert ex[0]["doc"] == "Annual Report 2026" and ex[0]["url"] == "https://b/ar.pdf"
    assert FN.pages_of("\n=== page 7 ===\nabc") == [(7, "abc")]
    assert FN.segment_excerpts("X", []) == []


def test_segment_table_computes_growth_from_extracted_numbers():
    seg = {"unit": "₹ crore", "years": [
        {"fy": "FY2024", "revenue": 400, "operating_profit": 80, "pat": None, "source": "AR 2024 — page 150"},
        {"fy": "FY2025", "revenue": 450, "operating_profit": 90, "pat": 40, "source": "AR 2025 — page 161"},
        {"fy": "FY2026", "revenue": 540, "operating_profit": 99, "pat": 50, "source": "AR 2026 — page 170"}]}
    st = AZ.segment_table(seg)
    rows = {r["metric"]: r["values"] for r in st["rows"]}
    assert st["available"] and st["years"] == ["FY2024", "FY2025", "FY2026"]
    assert rows["Revenue growth (%)"] == [None, 12.5, 20.0] and rows["Operating margin (%)"] == [20.0, 20.0, 18.3]
    assert rows["PAT growth (%)"] == [None, None, 25.0] and st["found_numbers"] == 8
    assert not AZ.segment_table({"years": []})["available"]


def test_confidence_and_listing_status_follow_the_record():
    sits = SO.build_situations(_rows(), {"3": SCHEME}, TODAY)
    s = sits[0]
    assert SO.confidence(s) == ("confirmed", "a demerger scheme is on the exchange record")
    L = SO.listing_status(s, {}, TODAY)
    assert L["state"] == "pending_record_date_set" and "RECORD DATE 2026-09-15" in L["text"]
    later = SO.build_situations(_rows(), {"3": SCHEME}, dt.date(2026, 11, 20))[0]
    assert SO.listing_status(later, {}, dt.date(2026, 11, 20))["state"] == "listed"
    pre = SO.build_situations(_rows()[:2], {}, TODAY)[0]
    L = SO.listing_status(pre, {"listing_timeline": "listing expected by Q4 FY27 (Feb 2026 call)"}, TODAY)
    assert L["state"] == "not_yet" and "Q4 FY27" in L["text"]
    assert SO.listing_status(sits[1], {}, TODAY)["state"] == "not_a_spin"
    rum = {**pre, "stage": "rumoured", "facts": {"news_only": True}, "headlines": []}
    assert SO.confidence(rum)[0] == "indicated" and SO.listing_status(rum, {}, TODAY)["state"] == "no_scheme"
    ipo = {**pre, "kind": "subsidiary_listing"}
    assert SO.confidence(ipo)[0] == "probable" and SO.listing_status(ipo, {}, TODAY)["state"] == "subsidiary_ipo"



def test_resulting_company_never_the_parent_and_listing_has_a_short_form():
    rows = _rows()[:1]
    s = SO.build_situations(rows, {"1": 'Alpha Industries Limited ("Resulting Company")'}, TODAY)[0]
    assert "resulting_company" not in s["facts"]                     # the parent itself
    s = SO.build_situations(rows, {"1": 'In the case of Alpha Energy Limited ("Resulting Company")'}, TODAY)[0]
    assert s["facts"]["resulting_company"] == "Alpha Energy Limited"
    L = SO.listing_status(s, {}, TODAY)
    assert L["short"].startswith("NOT YET (announced)")
    full = SO.build_situations(_rows()[:4], {"3": SCHEME}, TODAY)[0]
    assert SO.listing_status(full, {}, TODAY)["short"] == "RECORD DATE 2026-09-15; listing pending"
    assert AZ.entity_cell({"facts": {}, "judge": {"what_is_spun": "the ice-cream business"}}) == "the ice-cream business"
    assert AZ.entity_cell({"facts": {}, "judge": {"what_is_spun": "not stated"}}) == "—"



def test_an_amalgamation_order_is_not_a_demerger_and_the_judge_can_demote():
    text = "amalgamation amalgamation amalgamation merger of Sesa into Dabur; " + "demerger " * 3
    assert SO.refine_kind({"kind": "merger"}, text) == "merger"
    assert SO.refine_kind({"kind": "scheme_other"}, "demerger " * 6 + "amalgamation " * 2) == "demerger"
    sit = {"kind": "demerger", "stage": "exchange_noc", "facts": {}, "days_since_first": 10,
           "listed_on": None, "days_since_listing": None, "reasons": [], "headlines": []}
    j = {"status": "judged", "what_is_spun": "Nothing; documents describe amalgamation of Sesa Care "
         "Private Limited into Dabur India, not a demerger", "parent_or_spin": "neither",
         "selling_pressure": "unlikely", "reason": "brand acquisition"}
    assert SO.judge_override(sit, j) == "merger"
    j2 = {"status": "judged", "what_is_spun": "Ice cream business demerged into Kwality Wall's",
          "parent_or_spin": "spin", "selling_pressure": "likely", "reason": "focus"}
    assert SO.judge_override(sit, j2) is None
    assert "demerged_undertaking" not in SO.facts_in('"Demerged Undertaking" means with the total revenue and net.')



def test_resulting_company_must_look_like_a_company_name():
    good = 'the Resulting Company, i.e. Talwandi Sabo Power Limited'
    assert SO.facts_in(good)["resulting_company"] == "Talwandi Sabo Power Limited"
    assert SO.facts_in('Sriam Labs Private Limited ("Resulting Company")')["resulting_company"] == "Sriam Labs Private Limited"
    for bad in ('No. 1 is a public limited ("Resulting Company")', 'Essentials Limited ("Resulting Company")',
                'the Resulting Company, i.e. Public Limited', 'Investments Limited ("Resulting Company")'):
        assert "resulting_company" not in SO.facts_in(bad), bad
