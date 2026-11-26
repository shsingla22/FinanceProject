"""Offline tests of the ManagementChangeSkill — no network, no judge.

Run:  python3 -m pytest -q test_skill.py
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import json
import sys
import zipfile
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mgmt as M            # noqa: E402
import judge as J           # noqa: E402
import track as T           # noqa: E402
import analyze as AZ        # noqa: E402
import evaluate as EV       # noqa: E402

MF = M.MF
TODAY = dt.date(2026, 11, 26)


def flags(text):
    return sorted(M.kmp_flags(text))


# ------------------------------------------------------- the text, not the headline

def test_an_appointment_or_a_cessation_beside_a_top_seat_is_a_candidate():
    assert flags("Mr. Ravi Kumar has been appointed as Chief Financial Officer and KMP of the Company with effect from 1 June 2026.") == [("CFO", "appointment")]
    assert flags("Ms. Asha Rao, Chief Financial Officer, has tendered her resignation to pursue other opportunities.") == [("CFO", "cessation")]
    assert flags("Shri R K Sharma assumed charge as Director (Finance) of the Company today.") == [("CFO", "appointment")]
    assert ("MD", "cessation") in flags("Completion of Tenure of Shri K. Satyanarayana Raju as MD & CEO of the Bank on 31.12.2025.")
    assert ("CEO", "cessation") in flags("Completion of Tenure of Shri K. Satyanarayana Raju as MD & CEO of the Bank on 31.12.2025.")
    assert flags("The Board noted the sad demise of Mr. A B Shah, Chairman and Managing Director of the Company.") == [("MD", "cessation")]
    assert flags("Mr. P Nair will step down as Chief Executive Officer on 31 March 2026 and Ms. L Iyer will succeed him.") == [("CEO", "appointment")] \
        or ("CEO", "cessation") in flags("Mr. P Nair will step down as Chief Executive Officer on 31 March 2026 and Ms. L Iyer will succeed him.")


def test_a_reappointment_is_read_but_is_not_a_change():
    t = "The Board approved the re-appointment of Mr. P Q Rao as Managing Director & CEO for a further period of three years."
    assert flags(t) == []
    assert {(h["seat"], h["event"]) for h in M.kmp_hits(t)} == {("MD", "reappointment"), ("CEO", "reappointment")}
    assert flags("Extension of tenure of Shri A Kumar, Chairman & Managing Director, by one year.") == []


def test_the_disclosure_table_labels_are_not_events():
    """SEBI's table prints 'appointment, re-appointment, resignation, removal,
    death or otherwise' in every filing; that row label is not news."""
    t = ("Sr. Particulars Details 1 Reason for change viz. appointment, re-appointment, resignation, removal, death or otherwise "
         "Re-appointment of Mr. A B, Managing Director 2 Date of appointment/re-appointment/cessation (as applicable) & term of appointment "
         "1 April 2026, five years 3 Brief profile (in case of appointment) Enclosed")
    assert flags(t) == []
    t2 = ("Reason for change viz. appointment, resignation, removal, death or otherwise: Appointment of Mr. C D as Independent Director. "
          "This letter is signed by E F, Company Secretary. Copy to the Managing Director.")
    assert flags(t2) == []


def test_a_division_a_deputy_and_an_addressee_are_not_the_seat():
    assert flags("Mr. Chandrashekhar Shrotri has been appointed as Chief Executive Officer — Cable Solutions in the category of Senior Management.") == []
    assert flags("Mr. Supratik Roy has been appointed as CEO- Emerging Business of the Company w.e.f. December 01, 2025.") == []
    assert flags("Mr. S T Rao, Deputy Managing Director, retired from the services of the Bank.") == []
    assert flags("To, The Managing Director, Shree Cement Limited. I hereby tender my resignation from the position of Head - Marketing.") == []
    assert flags("I will be stepping down from my position as Chief Financial Officer of Cement Business of the group.") == []
    hits = M.kmp_hits("Mr. Vivek Abrol, Chief Executive Officer – FMEG Business, has tendered his resignation.")
    assert hits and all(h["unit"] for h in hits)


def test_the_person_nearest_the_seat_is_read():
    h = M.kmp_hits("Took note of the resignation of Mr. Anish Mathew, Chief Financial Officer, with effect from December 01, 2025.")
    assert h[0]["person"] == "Anish Mathew" and h[0]["event"] == "cessation" and "Anish Mathew" in h[0]["snippet"]


def test_a_headline_alone_decides_nothing():
    """'change in Management' is the headline of a new head of internal audit
    and of a new CEO alike: only the text separates them."""
    audit = "the Board approved the appointment of Mr. Chander Kant as EVP & Head-Internal Audit of the Company for a period of 3 years."
    row = {"category": "Change in Management", "headline": "has informed the Exchange about change in Management", "origin": "mgmt"}
    assert M.scan_filing(row, audit)["kmp_flags"] == []
    ceo = "the Board approved the appointment of Ms. Anita Rao as Managing Director & Chief Executive Officer of the Company."
    assert ("CEO", "appointment") in M.scan_filing(row, ceo)["kmp_flags"]
    # in a category that is not about management the mention must be in the opening of the document
    late = "x" * (M.KMP_OPENING_CHARS + 50) + " " + ceo
    assert M.scan_filing({**row, "category": "Press Release", "origin": "store"}, late)["kmp_flags"] == []
    assert M.scan_filing({**row, "category": "Press Release", "origin": "store"}, ceo)["kmp_flags"]


# ------------------------------------------------------------------ ownership

def test_ownership_language_counts_only_with_this_company_as_the_target():
    target = ("Open offer for acquisition of up to 26% of the equity share capital of the Company (Target Company) from the public shareholders "
              "by the Acquirer, pursuant to the share purchase agreement with the promoters of the Company.")
    assert "open_offer" in M.ownership_flags(target)
    buyer = "The Company has signed an agreement for acquisition of control of XYZ Private Limited, a maker of valves, for Rs. 200 crore."
    assert M.ownership_flags(buyer) == set()
    assert "reclassification" in M.ownership_flags("Application for re-classification of the outgoing promoters of the Company to public category under Regulation 31A.")
    assert "change_of_control" in M.ownership_flags("ABC Holdings will become the promoter of the Company and acquire control; change in control of the Company is subject to approvals.")


def test_the_shareholding_register_shows_a_change_of_hands():
    rows = [{"symbol": "RBL", "as_of": d, "promoter_pct": v} for d, v in
            (("2025-06-30", "0"), ("2025-09-30", "0"), ("2025-12-31", "0"), ("2026-06-30", "60.0"), ("2026-09-30", "59.88"))]
    rows += [{"symbol": "QIP", "as_of": d, "promoter_pct": v} for d, v in (("2025-09-30", "52.1"), ("2026-09-30", "49.2"))]
    rows += [{"symbol": "FLAT", "as_of": d, "promoter_pct": v} for d, v in (("2025-09-30", "61.2"), ("2026-09-30", "61.0"))]
    rows += [{"symbol": "SELL", "as_of": d, "promoter_pct": v} for d, v in (("2025-09-30", "40.0"), ("2026-03-31", "37.5"), ("2026-09-30", "37.4"))]
    rows += [{"symbol": "LATER", "as_of": "2027-03-31", "promoter_pct": "5"}]
    mv = M.shareholding_moves(rows, TODAY)
    assert mv["RBL"]["base"] == ("2025-09-30", 0.0) and mv["RBL"]["latest"][1] == 59.88 and mv["RBL"]["level"] == "major"
    assert set(mv["RBL"]["crossed"]) == {"above 50%", "above 25%", "from nil"}
    assert mv["QIP"]["level"] == "major" and mv["QIP"]["crossed"] == ["below 50%"]        # a small move that crosses a threshold
    assert mv["FLAT"]["level"] == "none" and mv["SELL"]["level"] == "minor" and mv["SELL"]["change"] == -2.6
    assert "LATER" not in mv                                                               # nothing after the run date


def test_reg29_disclosures_and_deals_are_summed_per_company():
    sast = [{"symbol": "A", "date": "2026-03-01", "acquirer": "Promoter One", "promoter": "Y", "pct_sold": "3.5", "pct_acquired": "", "pct_after": "40"},
            {"symbol": "A", "date": "2026-04-01", "acquirer": "Promoter One", "promoter": "Y", "pct_sold": "2.0", "pct_acquired": "", "pct_after": "38"},
            {"symbol": "A", "date": "2024-04-01", "acquirer": "Promoter One", "promoter": "Y", "pct_sold": "9.0", "pct_acquired": "", "pct_after": "49"},
            {"symbol": "B", "date": "2026-05-01", "acquirer": "Big Fund", "promoter": "N", "pct_sold": "", "pct_acquired": "6", "pct_after": "26.1"},
            {"symbol": "C", "date": "2026-05-01", "acquirer": "Small Fund", "promoter": "N", "pct_sold": "", "pct_acquired": "1", "pct_after": "5.2"}]
    s = M.sast_summary(sast, TODAY)
    assert s["A"]["promoter_sold"] == 5.5 and s["A"]["level"] == "major"                   # the 2024 row is outside the window
    assert s["B"]["level"] == "major" and s["B"]["outsiders"][0]["acquirer"] == "Big Fund" and s["C"]["level"] == "none"
    deals = [{"symbol": "E", "date": "2026-09-01", "client": "EPSILON BIDCO PTE LTD", "side": "SELL", "quantity": "2600"},
             {"symbol": "E", "date": "2026-09-01", "client": "Broker X", "side": "BUY", "quantity": "900"},
             {"symbol": "E", "date": "2026-09-01", "client": "Broker X", "side": "SELL", "quantity": "900"}]
    d = M.deals_summary(deals, TODAY, {"E": 10000.0})
    assert d["E"]["top_seller_pct"] == 26.0 and d["E"]["level"] == "major"
    assert next(c for c in d["E"]["clients"] if c["client"] == "BROKER X")["net_sold_pct"] == 0.0   # a broker crossing both sides


# ---------------------------------------------------------------------- calls

CALLS = ("Call: Nov 2025\nManagement: Mr. Anil Mehta – Managing Director & CEO; Mr. Ravi Shah – Chief Financial Officer\n"
         "Moderator: Welcome.\nAnil Mehta: Good quarter.\n"
         "Call: Aug 2026\nManagement: Mr. Anil Mehta – Managing Director & CEO; Ms. Priya Nair – Chief Financial Officer\n"
         "Anil Mehta: I would like to welcome Priya Nair who has joined us as our new CFO. Ravi has moved on.\n"
         "Analyst: Is there any change in control or open offer expected after the promoters sold their stake?\n")


def test_the_calls_roster_and_the_calls_words():
    secs = M.call_sections(CALLS)
    assert [s[0] for s in secs] == ["Nov 2025", "Aug 2026"]
    r = M.roster(secs[0][2])
    assert r["CFO"] == {"ravi shah"} and r["MD"] == {"anil mehta"} and r["CEO"] == {"anil mehta"}
    ch = M.roster_changes("X", TODAY, text=CALLS)
    assert [(c["seat"], c["before"], c["after"]) for c in ch] == [("CFO", ["ravi shah"], ["priya nair"])]
    hits = M.call_hits("X", TODAY, text=CALLS)
    assert {h["kind"] for h in hits} == {"kmp", "ownership"} and all(h["call"] == "Aug 2026" for h in hits)
    assert M.same_person("R. Shah", "Ravi Shah") and not M.same_person("Ravi Shah", "Priya Nair")


# ---------------------------------------------------------------- the numbers

def _write(path: Path, header: list[str], rows: list[list]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


@pytest.fixture
def statements(tmp_path, monkeypatch):
    ys = ["Mar 2021", "Mar 2022", "Mar 2023", "Mar 2024", "Mar 2025", "Mar 2026"]
    for name in ("PNL", "BS", "CASH", "WC", "MGMT_INFO"):
        monkeypatch.setattr(T, name, tmp_path / name)
    _write(tmp_path / "PNL" / "CO.csv", ["", "parent_line_item"] + ys,
           [["Sales", ""] + [100, 110, 121, 133.1, 146.4, 161.1], ["Operating Profit", ""] + [10, 12, 15, 18, 22, 26],
            ["Net Profit", ""] + [5, 6, 8, 10, 12, 15], ["EPS in Rs", ""] + [1, 1.2, 1.6, 2, 2.4, 3]])
    _write(tmp_path / "BS" / "CO.csv", ["", "parent_line_item"] + ys,
           [["Equity Capital", ""] + [10] * 6, ["Reserves", ""] + [40, 45, 52, 60, 70, 82], ["Borrowings", ""] + [30, 28, 25, 20, 15, 10]])
    _write(tmp_path / "CASH" / "CO.csv", ["", "parent_line_item"] + ys,
           [["Cash from Operating Activity", ""] + [8, 9, 11, 13, 16, 19], ["Free Cash Flow", ""] + [3, 4, 5, 6, 8, 10]])
    _write(tmp_path / "WC" / "CO.csv", ["metric"] + ys, [["ROCE %"] + [12, 14, 16, 18, 20, 22], ["Working Capital Days"] + [60, 58, 55, 50, 48, 45]])
    _write(tmp_path / "PNL" / "BANK.csv", ["", "parent_line_item"] + ys,
           [["Revenue", ""] + [50, 55, 60, 70, 80, 90], ["Financing Profit", ""] + [5, 6, 7, 9, 10, 12], ["Net Profit", ""] + [4, 5, 6, 7, 8, 9]])
    _write(tmp_path / "MGMT_INFO" / "CO.csv", ["role", "name", "qualification", "experience", "years_present", "status", "first_seen_in_ar"],
           [["CFO", "Ravi  Shah", "", "", "FY2022–FY2025", "current", ""], ["Managing Director", "Anil Mehta-", "", "", "FY2021–FY2025", "current", ""]])
    _write(tmp_path / "MGMT_INFO" / "OTHER.csv", ["role", "name", "qualification", "experience", "years_present", "status", "first_seen_in_ar"],
           [["CFO", "Priya Nair", "", "", "FY2022–FY2024", "exited", ""]])
    _write(tmp_path / "PNL" / "OTHER.csv", ["", "parent_line_item"] + ys,
           [["Sales", ""] + [200, 220, 260, 300, 310, 320], ["Operating Profit", ""] + [20, 24, 30, 36, 37, 38], ["Net Profit", ""] + [10, 12, 16, 20, 20, 21]])
    monkeypatch.setattr(T, "_INFO", None)
    return tmp_path


def test_three_years_of_financials_computed_here(statements):
    f = T.financials("CO")
    rows = {r["metric"]: r["values"] for r in f["rows"]}
    assert f["years"] == ["Mar 2024", "Mar 2025", "Mar 2026"]
    assert rows["Sales (₹ cr)"] == [133.1, 146.4, 161.1] and rows["Sales growth (%)"] == [10.0, 10.0, 10.0]
    assert rows["Operating profit margin (%)"] == [13.5, 15.0, 16.1] and rows["ROCE (%)"] == [18.0, 20.0, 22.0]
    assert rows["ROE (%)"] == [14.3, 15.0, 16.3] and rows["Debt / equity (x)"] == [0.29, 0.19, 0.11]
    b = T.financials("BANK")                                  # a lender's statement uses other line names
    assert b["lender"] and [r["metric"] for r in b["rows"]][:3] == ["Revenue (₹ cr)", "Revenue growth (%)", "Financing profit (₹ cr)"]
    assert not T.financials("NOPE")["available"]


def test_a_tenure_record_runs_from_the_year_before_to_the_last_full_year(statements):
    rec = T.tenure_record("CO", 2023, 2026)                   # took the seat in FY2023; base is FY2022
    assert (rec["from"], rec["to"], rec["years"]) == ("Mar 2022", "Mar 2026", 4)
    rows = {r["metric"]: r for r in rec["rows"]}
    assert rows["Sales (₹ cr)"]["change"] == "+10.0% a year over 4 years" and rows["ROCE (%)"]["change"] == "+8.0 pts"
    assert rows["Borrowings (₹ cr)"]["change"] == "-18"
    assert T.tenure_record("CO", 2015, 2026)["clipped"]       # the statements on file start later than the tenure
    assert not T.tenure_record("CO", None, 2026)["available"] and not T.tenure_record("CO", 2027, 2026)["available"]
    assert T.tenure_record("CO", 2026, 2026)["years"] == 1
    assert (T.fy_of("2019-07-01"), T.fy_of("2019-02-15"), T.fy_of("2019"), T.fy_of("FY2021"), T.fy_of("April 2022"), T.fy_of("not stated")) == (2020, 2019, 2020, 2021, 2023, None)


def test_people_are_matched_across_spellings_never_on_one_word(statements):
    assert T.same_person("K. Krithivasan Iyer", "K Krithivasan Iyer") and T.same_person("Sandeep Tandon", "Sandeep Kumar Tandon")
    assert not T.same_person("Amit Shah", "Anil Shah") and not T.same_person("Shah", "Ravi Shah")
    assert T.seat_since("CO", "Ravi Shah", "CFO") == 2022 and T.seat_since("CO", "Anil Mehta", "MD") == 2021
    assert [(s["symbol"], s["role"], s["first_fy"], s["last_fy"]) for s in T.seats_held("Priya Nair", exclude_symbol="CO")] == [("OTHER", "CFO", 2022, 2024)]


def test_track_records_of_outgoing_and_incoming(statements):
    ch = {"group": "CFO", "seat": "CFO", "announced_on": "2026-06-10",
          "outgoing": {"name": "Ravi Shah", "last_day": "2026-06-30", "in_seat_since": "not stated"},
          "incoming": {"name": "Priya Nair", "from_where": "external", "experience_years": "22 years", "profile": "A chartered accountant.",
                       "previous_roles": [{"company": "Other Limited", "role": "Chief Financial Officer", "from": "2021", "to": "2024"},
                                          {"company": "Other Limited", "role": "Deputy CFO", "from": "2018", "to": "2021"}]}}
    out = AZ.outgoing_record("CO", ch)
    assert out["since_fy"] == 2022 and "annual reports" in out["since_basis"] and (out["from"], out["to"]) == ("Mar 2021", "Mar 2026")
    inc = AZ.incoming_record("CO", ch, {"CO": "Co Ltd.", "OTHER": "Other Ltd."})
    assert inc["previous_roles"][0]["symbol"] == "OTHER" and len(inc["records"]) == 1          # the deputy seat draws no record
    assert inc["records"][0]["company"] == "Other Limited" and inc["records"][0]["from"] == "Mar 2021"
    # nothing on file about when they took the seat: the last five years, marked as context only
    ch2 = {**ch, "outgoing": {"name": "Unknown Person", "last_day": "2026-06-30", "in_seat_since": ""}}
    ctx = AZ.outgoing_record("CO", ch2)
    assert ctx["context_only"] and ctx["since_fy"] is None and ctx["years"] == 5
    assert not AZ.incoming_record("CO", {**ch, "incoming": {"name": ""}}, {})["available"]


def test_a_price_across_a_split_or_demerger_is_not_compared(monkeypatch):
    monkeypatch.setattr(T, "price_since", lambda s, a, t: {"available": True, "before": ("2026-04-17", 787.5), "latest": ("2026-11-13", 259.7), "change_pct": -67.0})
    p = AZ.price_block("VEDL", "2026-04-20", TODAY, {"VEDL": [("2026-05-01", "Demerger")]})
    assert "Demerger on 2026-05-01" in p["not_comparable"]
    monkeypatch.setattr(T, "price_since", lambda s, a, t: {"available": True, "before": ("2026-04-17", 100.0), "latest": ("2026-11-13", 112.0), "change_pct": 12.0})
    assert "not_comparable" not in AZ.price_block("X", "2026-04-20", TODAY, {})


# ------------------------------------------------------------------ the judge

def test_the_judge_is_cached_and_a_bad_answer_is_asked_again(tmp_path, monkeypatch):
    monkeypatch.setattr(J, "CACHE", tmp_path / "cache.json")
    monkeypatch.setattr(J, "_MEM", None)
    calls = []
    def runner(q):
        calls.append(q)
        return "not json" if len(calls) == 1 else 'Here: ```json\n{"changes": [], "read": "nothing",}\n```'
    a = J.ask("K::seat", "s1", "prompt", runner=runner)
    assert a["status"] == "judged" and a["read"] == "nothing" and len(calls) == 2 and "previous answer was not valid JSON" in calls[1]
    assert J.ask("K::seat", "s1", "prompt", runner=runner)["status"] == "cached" and len(calls) == 2
    assert J.ask("K::seat", "s2", "prompt", allow_ai=False)["status"] == "not assessed"          # a new stamp is a new question
    assert J.ask("Z", "s", "p", runner=lambda q: "no braces at all")["status"].startswith("judge failed")
    assert json.loads((tmp_path / "cache.json").read_text())["K::seat"]["stamp"] == "s1"


def _cand(tmp_path, texts: dict[str, str], own: bool = False):
    rows = []
    for i, (date, text) in enumerate(texts.items()):
        p = tmp_path / f"f{i}.txt"
        p.write_text(text)
        rows.append({"date": date, "symbol": "CO", "company": "Co Ltd.", "category": "Change in Management", "headline": "change in Management",
                     "attachment": f"https://x/{i}.pdf", "ann_id": str(i), "text_path": str(p), "origin": "mgmt", "flags": [], "hits": []})
    return {"symbol": "CO", "company": "Co Ltd.",
            "seat": {"candidate": True, "why": ["x"], "filings": [] if own else rows, "calls": [], "roster": []},
            "own": {"candidate": own, "why": [], "filings": rows if own else [], "calls": [], "shareholding": {}, "sast": {}, "sast_rows": [],
                    "deals": {}, "notes": [], "minor": []}}


def test_every_name_and_quote_must_be_in_the_documents(tmp_path):
    c = _cand(tmp_path, {"2026-06-10": "The Board took note of the resignation of Mr. Ravi  Shah, Chief Financial\nOfficer of the Company, "
                                       "with effect from June 30, 2026, and approved the appointment of Ms. Priya Nair as Chief Financial Officer."})
    res = {"status": "judged", "changes": [
        {"seat": "CFO", "designation_as_written": "Chief Financial Officer", "is_change": True,
         "outgoing": {"name": "Ravi Shah", "last_day": "2026-06-30", "reason": "resignation"},
         "incoming": {"name": "Priya Nair", "effective": "2026-07-01"}, "status": "announced, not yet effective", "announced_on": "2026-06-10",
         "quote": "took note of the resignation of Mr. Ravi Shah, Chief Financial Officer of the Company, with effect from June 30, 2026"},
        {"seat": "CEO", "is_change": True, "outgoing": {"name": "Invented Person"}, "incoming": {"name": ""}, "announced_on": "2026-06-10", "quote": "made up"},
        {"seat": "MD", "is_change": False, "not_a_change_because": "re-appointment", "outgoing": {"name": "Anil Mehta"}, "incoming": {}},
        {"seat": "CFO", "is_change": True, "outgoing": {"name": "Ravi Shah"}, "incoming": {"name": "Priya Nair"}, "announced_on": "2026-06-10", "quote": "x"}]}
    out = AZ.settle_seat(c, res, "2025-11-26", "2026-11-26")
    kept = [ch for ch in out if not ch.get("dropped")]
    assert len(kept) == 1 and kept[0]["verified"] and kept[0]["group"] == "CFO" and kept[0]["sources"][0]["attachment"] == "https://x/0.pdf"
    assert {ch["dropped"] for ch in out if ch.get("dropped")} == {"a name the judge gave is not in the documents", "not a change: re-appointment"}
    assert len(out) == 3                                                          # the repeated CFO entry is one change
    assert AZ.settle_seat(c, {"status": "judge failed: x"}, "2025-11-26", "2026-11-26") == []


def test_a_change_outside_the_window_is_dropped(tmp_path):
    c = _cand(tmp_path, {"2026-01-05": "Mr. Old Timer retired as Managing Director on 30 June 2024. Ms. New Chief was appointed Managing Director."})
    res = {"status": "judged", "changes": [{"seat": "MD", "is_change": True, "outgoing": {"name": "Old Timer", "last_day": "2024-06-30"},
                                            "incoming": {"name": "New Chief", "effective": "2024-07-01"}, "announced_on": "2024-06-01",
                                            "quote": "Mr. Old Timer retired as Managing Director on 30 June 2024"}]}
    out = AZ.settle_seat(c, res, "2025-11-26", "2026-11-26")
    assert out[0]["dropped"].startswith("before the window")
    assert AZ.seat_group("MD & CEO", "Managing Director & CEO") == "CEO/MD" and AZ.seat_group("CFO", "Whole-time Director & CFO") == "CFO"
    assert AZ.seat_group("CMD", "Chairman and Managing Director (also Director Finance)") == "CEO/MD"


def test_ownership_verdicts_are_kept_or_set_aside(tmp_path):
    c = _cand(tmp_path, {"2026-06-19": "Pursuant to the Open Offer and the Preferential Issue, the Acquirer Emirates NBD Bank has acquired control over the "
                                       "Target Company and has become the promoter of the Target Company."}, own=True)
    res = {"status": "judged", "verdict": "change_of_control", "what_happened": "Emirates NBD took 60%.", "outgoing_owner": {"name": "not stated"},
           "incoming_owner": {"name": "Emirates NBD Bank (P.J.S.C.)", "stake_after": "60%"}, "mode": "preferential issue", "control_changes": True,
           "dates": [{"event": "completion", "date": "2026-06-18"}, {"event": "bad", "date": "soon"}], "announced_on": "2025-10-18",
           "quote": "the Acquirer Emirates NBD Bank has acquired control over the Target Company and has become the promoter"}
    o = AZ.settle_own(c, res)
    assert o["keep"] and o["verified"] and o["label"].startswith("Change of control") and len(o["dates"]) == 1 and o["outgoing_owner"]["name"] == ""
    assert not AZ.settle_own(c, {**res, "verdict": "dilution_only"})["keep"]
    assert not AZ.settle_own(c, {**res, "incoming_owner": {"name": "Zebra Capital Partners"}})["verified"]
    assert AZ.settle_own(c, {"status": "not assessed"}) == {}


def test_documents_fit_the_budget_without_losing_a_filing(tmp_path):
    c = _cand(tmp_path, {"2026-03-01": "OLD " + "o" * 500, "2026-06-01": "MID " + "m" * 9000, "2026-09-01": "NEW " + "n" * 9000})
    full = AZ.docs_text(c["seat"]["filings"], budget=50_000)
    assert full.index("NEW ") < full.index("MID ") < full.index("OLD ") and "characters]" not in full
    tight = AZ.docs_text(c["seat"]["filings"], budget=7_000)
    assert all(k in tight for k in ("NEW ", "MID ", "OLD ")) and "characters]" in tight and len(tight) < 7_400


# -------------------------------------------------------------- end to end

def test_run_end_to_end_with_a_fake_judge(tmp_path, monkeypatch, statements):
    data = tmp_path / "data"
    texts = {
        "1": ("CO", "2026-06-10", "Change in Management", "The Board took note of the resignation of Mr. Ravi Shah, Chief Financial Officer of the Company, "
              "with effect from June 30, 2026 and approved the appointment of Ms. Priya Nair as Chief Financial Officer."),
        "2": ("CO", "2026-02-01", "Appointment", "The Board approved the re-appointment of Mr. Anil Mehta as Managing Director for five years."),
        "3": ("OTHER", "2026-03-03", "Change in Management", "Appointment of Mr. Chander Kant as Head-Internal Audit of the Company."),
        "4": ("OTHER", "2026-07-07", "Updates", "Open offer for acquisition of up to 26% of the equity share capital of the Company (Target Company) by "
              "Big Buyer Limited. Big Buyer Limited will acquire control and become the promoter of the Company."),
    }
    rows = []
    for aid, (sym, date, cat, text) in texts.items():
        p = data / f"{aid}.txt"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        rows.append({"date": date, "symbol": sym, "company": f"{sym.title()} Ltd.", "category": cat, "headline": "has informed the Exchange",
                     "attachment": f"https://x/{aid}.pdf", "ann_id": aid, "text_path": str(p), "origin": "mgmt"})
    monkeypatch.setattr(M, "load_filings", lambda today, days=365: list(rows))
    monkeypatch.setattr(M.FA, "universe", lambda: {"CO": "Co Ltd.", "OTHER": "Other Ltd.", "QUIET": "Quiet Ltd."})
    monkeypatch.setattr(AZ, "SCAN_CACHE", tmp_path / "scan.json.gz")
    monkeypatch.setattr(M, "call_text", lambda s: CALLS if s == "CO" else "")
    monkeypatch.setattr(AZ, "warm_calls", lambda syms, workers=6: None)
    monkeypatch.setattr(AZ, "scan_all", lambda filings, workers=6: {r["ann_id"]: AZ._scan_job(r)[1] for r in filings})
    shp = [{"symbol": "OTHER", "as_of": "2025-09-30", "promoter_pct": "55", "notes": ""}, {"symbol": "OTHER", "as_of": "2026-09-30", "promoter_pct": "0", "notes": ""},
           {"symbol": "QUIET", "as_of": "2025-09-30", "promoter_pct": "60", "notes": ""}, {"symbol": "QUIET", "as_of": "2026-09-30", "promoter_pct": "60", "notes": ""}]
    monkeypatch.setattr(M.MF, "read_csv", lambda path: shp if path == M.MF.SHP else [])
    monkeypatch.setattr(M, "shares_outstanding", lambda as_of=None: {})
    monkeypatch.setattr(AZ, "corporate_actions", lambda today, days: {})
    monkeypatch.setattr(T, "price_since", lambda s, a, t: {"available": False})
    monkeypatch.setattr(J, "CACHE", tmp_path / "cache.json")
    monkeypatch.setattr(J, "_MEM", None)
    AZ.set_out_dir(tmp_path / "out")
    asked = []
    def runner(q):
        asked.append(q)
        if "PROMOTERS / OWNERS" in q:
            return json.dumps({"verdict": "change_of_control", "what_happened": "Big Buyer took control.",
                               "outgoing_owner": {"name": "", "stake_before": "55%", "stake_after": "0%"},
                               "incoming_owner": {"name": "Big Buyer Limited", "kind": "strategic buyer", "who_they_are": "a buyer"},
                               "mode": "open offer", "open_offer": {"made": True, "price": "100", "size": "26%", "status": "announced"},
                               "control_changes": True, "dates": [], "announced_on": "2026-07-07",
                               "quote": "Big Buyer Limited will acquire control and become the promoter of the Company"})
        return json.dumps({"changes": [
            {"seat": "CFO", "designation_as_written": "Chief Financial Officer", "is_change": True,
             "outgoing": {"name": "Ravi Shah", "last_day": "2026-06-30", "reason": "resignation", "in_seat_since": "not stated"},
             "incoming": {"name": "Priya Nair", "effective": "2026-07-01", "from_where": "external",
                          "previous_roles": [{"company": "Other Limited", "role": "Chief Financial Officer", "from": "2021", "to": "2024"}]},
             "status": "announced, not yet effective", "announced_on": "2026-06-10",
             "quote": "took note of the resignation of Mr. Ravi Shah, Chief Financial Officer of the Company"},
            {"seat": "MD", "is_change": False, "not_a_change_because": "re-appointment", "outgoing": {"name": "Anil Mehta"}, "incoming": {}}]})
    class A:                                   # noqa: D401
        as_of, days, only, quick, workers, out = "2026-11-26", 365, "", False, 2, None
    rec = AZ.cmd_run(A, runner=runner)
    cos = {c["symbol"]: c for c in rec["companies"]}
    # the head of internal audit was never put to the judge; the CFO and the open offer were
    assert len(asked) == 2 and not cos["OTHER"]["seat"]["candidate"] and cos["OTHER"]["own"]["candidate"] and not cos["QUIET"]["has_change"]
    assert cos["CO"]["has_change"] and cos["OTHER"]["ownership"]["verdict"] == "change_of_control"
    md = (tmp_path / "out" / "MANAGEMENT_CHANGE_REPORT.md").read_text()
    for part in ("## List 1 — the promoters / owners changing", "## List 3 — the CFO changing", "### 1. What is changing",
                 "### 2. Financials — the last three years", "### 3. Track record — the outgoing management",
                 "### 4. Track record — the incoming management", "### 5. On the calls"):
        assert part in md, part
    assert "Ravi Shah (resignation; last day 2026-06-30)" in md and "Big Buyer Limited" in md and "Mar 2024 | Mar 2025 | Mar 2026" in md
    assert "Results of **Other Limited** while they were Chief Financial Officer there" in md
    assert (tmp_path / "out" / "companies" / "CO.md").exists() and not (tmp_path / "out" / "companies" / "QUIET.md").exists()
    assert rec["meta"]["counts"] == {"cfo_changes": 1, "cfo_companies": 1, "change_of_control": 1}
    # the evaluation: the register's major move carries a verdict, the roster's CFO change is reported, the quotes are verified
    monkeypatch.setattr(EV, "LABELS", tmp_path / "none.csv")
    monkeypatch.setattr(EV, "REVIEWED", tmp_path / "none2.csv")
    monkeypatch.setattr(M.MF, "read_csv", lambda path: shp if path == M.MF.SHP else [])
    ev = EV.evaluate(json.loads((tmp_path / "out" / "management_change_latest.json").read_text()))
    assert ev["E2"]["major_moves"] == 1 and ev["E2"]["no_verdict"] == [] and ev["E4"]["not_reported"] == [] and ev["E8"]["verified_pct"] == 100.0
    assert "E2 — every major move" in EV.render(ev)
    # a second run asks nothing new
    AZ.cmd_run(A, runner=runner)
    assert len(asked) == 2
    AZ.set_out_dir(AZ.INDIA / "Analysis" / "NiftyTotalMarketAnalysis" / "ManagementChangeAnalysis")


# ---------------------------------------------------------------- evaluation and fetch

def test_a_headline_that_names_a_seat_is_an_independent_check():
    assert EV.seat_of_headline("Appointment of Mr X as Chief Financial Officer") == "CFO"
    assert EV.seat_of_headline("Resignation of Managing Director & CEO") == "CEO/MD"
    assert EV.seat_of_headline("Re-appointment of Managing Director") == "" and EV.seat_of_headline("Appointment of Independent Director") == ""
    assert EV.seat_of_headline("has informed the Exchange about change in Management") == ""


def test_the_fetcher_reads_dates_zips_and_the_register(monkeypatch):
    assert (MF.iso("12-NOV-2026 to 13-NOV-2026"), MF.iso("26-Nov-2026 12:48"), MF.iso("30-SEP-2026"), MF.iso("soon")) == ("2026-11-12", "2026-11-26", "2026-09-30", "")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("letter.txt", "not a pdf")
    assert MF.text_of(buf.getvalue()) == ("", 0) and MF.text_of(b"<html>") == ("", 0)
    monkeypatch.setattr(MF, "get_json", lambda url, timeout=60: [
        {"date": "30-SEP-2026", "pr_and_prgrp": "54.72", "public_val": "45.12", "submissionDate": "16-OCT-2026", "remarksWeb": "a  note"},
        {"date": "30-SEP-2026", "pr_and_prgrp": "54.70", "public_val": "45.14", "submissionDate": "10-OCT-2026"},
        {"date": "30-JUN-2026", "pr_and_prgrp": "56.38", "public_val": "43.47", "submissionDate": "15-JUL-2026"}, {"date": "bad"}])
    rows = sorted(MF.shareholding_of("VEDL"), key=lambda r: r["as_of"])
    assert [(r["as_of"], r["promoter_pct"]) for r in rows] == [("2026-06-30", "56.38"), ("2026-09-30", "54.72")]   # the later filing of a quarter wins
    assert rows[1]["notes"] == "a note"
