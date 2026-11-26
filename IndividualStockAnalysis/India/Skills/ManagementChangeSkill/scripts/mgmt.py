"""
mgmt.py — the mechanical read of the ManagementChangeSkill.

Two kinds of management change, each found from several independent
sources, none of them a headline:

  A. OWNERSHIP — the promoters / owners of the company changing.
     * the exchange's quarterly shareholding register (promoter-and-group %),
     * NSE's Regulation 29 takeover disclosures (who bought or sold, promoter
       or not, the holding after),
     * bulk and block deals (a seller parting with a large slice),
     * the TEXT of open-offer, takeover, acquisition, agreement, board-outcome,
       press-release and update filings,
     * the stored conference calls.

  B. CEO / MD / CFO — the chief executive, managing director or chief
     financial officer changing: the TEXT of every filing in the management
     and board categories, of board outcomes, press releases and updates,
     and the calls. An appointment or a cessation counts; a re-appointment,
     a director who is not the MD, a company secretary, a head of internal
     audit do not.

This module only finds CANDIDATES and the evidence lines for them — it is
built for recall. `analyze.py` then reads the complete documents with the
judge, company by company, and decides.
"""

from __future__ import annotations

import csv
import datetime as dt
import gzip
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
sys.path.insert(0, str(INDIA / "Announcements"))
sys.path.insert(0, str(INDIA / "ManagementChange"))

import fetch_announcements as FA        # noqa: E402
import deep_read as DR                  # noqa: E402
import fetch_management_change as MF    # noqa: E402

DATA = MF.OUT_DIR
CONCALLS = INDIA / "ConferenceCalls" / "NiftyTotalMarket"
CALL_CACHE = CONCALLS / ".text_cache"
BUNDLES = INDIA / "Announcements" / "_bhav_bundles"

WINDOW_DAYS = 365

# ------------------------------------------------------------------ roles
# The three seats. Longest alternatives first so 'Managing Director & CEO'
# is one mention, not two.
_CEO = r"chief\s+executive\s+officer|\bC\.?E\.?O\.?(?![A-Za-z])|chief\s+executive(?!\s+officer)"
_MD = (r"chairman\s*(?:and|&|cum|-)\s*managing\s+director|\bC\.?M\.?D\.?(?![A-Za-z])|"
       r"(?<!deputy )(?<!dy\. )(?<!dy )managing\s+director|(?<![A-Za-z.])M\.?D\.?(?=\s*(?:&|and|cum)\s*C\.?E\.?O)")
_CFO = (r"chief\s+financ(?:ial|e)\s+officer|\bC\.?F\.?O\.?(?![A-Za-z])|director\s*[\(\-–,]?\s*\(?finance\)?(?!\s*(?:committee|department))|"
        r"finance\s+director|whole[\s-]?time\s+director\s*(?:and|&|cum)\s*c\.?f\.?o")
ROLE_RX = re.compile(rf"(?P<ceo>{_CEO})|(?P<md>{_MD})|(?P<cfo>{_CFO})", re.I)
# a seat that is not the company's own top seat
LOWER_RX = re.compile(r"\b(?:deputy|dy\.?|assistant|asst\.?|associate|vice|regional|zonal|circle|divisional|"
                      r"business unit|unit|plant|country|joint\s+c\.?f\.?o)\s*$", re.I)
UNIT_AFTER_RX = re.compile(r"^\s*(?:[-–—,(]\s*|of\s+(?!the\s+(?:company|bank|corporation)\b)(?:the\s+|its\s+|our\s+)?)"
                           r"(?!the\s+company|and\b|&|kmp\b|key\b|w\.?e\.?f|with\b|for\s+a\b|designate)"
                           r"[A-Za-z][\w&.' -]{2,60}?(?:business|division|vertical|segment|subsidiar|region|operations|"
                           r"limited|ltd|llc|inc\b|gmbh|pte)", re.I)

# 'Chief Executive Officer — Cable Solutions', 'CEO- Emerging Business': a dash and a name is a unit's seat
UNIT_DASH_RX = re.compile(r"^\s*[-–—]\s*(?!designate|elect|kmp|key\b|and\b)[A-Z]")

# ----------------------------------------------------------------- events
APPOINT_RX = re.compile(
    r"(?<!re-)(?<!re)(?<!re )\bappoint(?:ed|ment|s|ing)?\b|\belevat(?:ed|ion|es|ing)\b|"
    r"\b(?:has|have|had|will|shall|to)\s+(?:be\s+)?(?:take|taken|taking|took)\s+(?:over|charge)\b|\bassum(?:e|ed|es|ing)\s+(?:the\s+)?(?:charge|office|role)\b|"
    r"\bjoin(?:ed|s|ing)?\s+(?:the\s+(?:company|bank)\s+)?as\b|\bsucceed(?:s|ed|ing)?\b|\bsuccessor\b|\bnamed\s+as\b|"
    r"\bre-?designat(?:ed|ion|es|ing)\b|\bdesignat(?:ed|ion)\s+as\b|\binduct(?:ed|ion)\b|\bpromot(?:ed|ion)\s+(?:as|to)\b|"
    r"\badditional\s+charge\b|\binterim\b|\bofficiating\b|\bin-?charge\b", re.I)
CEASE_RX = re.compile(
    r"\bresign(?:ed|ation|s|ing)?\b|\bcessation\b|\bceas(?:e|ed|es|ing)\b|\bstep(?:ped|s|ping)?\s+down\b|"
    r"\bretir(?:e|ed|es|ing|ement)\b|\bsuperannuat(?:e|ed|ion|ing)\b|\bdemise\b|\bpassed\s+away\b|\bsad\s+demise\b|"
    r"\brelinquish(?:ed|es|ing|ment)?\b|\bdemit(?:s|ted|ting)?\b|\bremov(?:al|ed)\b|\bterminat(?:ed|ion)\b|"
    r"\bcompletion\s+of\s+(?:his|her|the|their)?\s*(?:tenure|term)\b|\b(?:tenure|term)\s+(?:ends|ended|expires|expired|expiry|completes|completed|concludes)\b|"
    r"\brelieved\b|\bvacat(?:e|ed|ion|ing)\b|\bexit(?:s|ed|ing)?\b|\bmov(?:e|es|ed|ing)\s+on\b|\bleav(?:e|es|ing)\s+the\s+(?:company|bank|organi[sz]ation)\b|"
    r"\bpursue\s+(?:other\s+)?(?:opportunit|career|interest)\w*\b|\bearly\s+release\b|\brepatriat\w+\b", re.I)
REAPPOINT_RX = re.compile(r"\bre[\s-]?appoint(?:ed|ment|s|ing)?\b|\bcontinuation\b|\bextension\s+of\s+(?:the\s+)?(?:tenure|term)\b|"
                          r"\bextend(?:ed|ing)?\s+(?:the\s+)?(?:tenure|term)\b|\brenewal\s+of\s+(?:the\s+)?(?:tenure|term)\b|"
                          r"\bfurther\s+(?:period|term)\b", re.I)
PERSON_RX = re.compile(r"\b(?:Mr|Ms|Mrs|Shri|Smt|Dr|Sri|Prof|CA|CS)\.?\s+((?:[A-Z][A-Za-z.'-]*\.?\s+){0,4}[A-Z][A-Za-z'-]+)")
WINDOW = 260            # characters either side of a role mention that an event must fall in

SEAT = {"ceo": "CEO", "md": "MD", "cfo": "CFO"}


# SEBI's disclosure table prints every event word in its row labels ("Reason for change viz.
# appointment, re-appointment, resignation, removal, death or otherwise") — in every filing,
# whatever happened. The labels are dropped before any event word is looked for.
BOILER_RX = re.compile(
    r"appointment\W+(?:re-?\s?appointment\W+)?resignation\W+(?:cessation\W+)?removal\W+death\W+(?:or\W+)?otherwise|"
    r"appointment\s*/\s*(?:re-?\s?appointment\s*/\s*)?(?:resignation\s*/\s*)?cessation(?:\s*/\s*resignation)?|"
    r"terms?\s+of\s+(?:re-?\s?)?appointment(?:\s*/\s*re-?\s?appointment)?|"
    r"\(\s*in\s+case\s+of\s+(?:appointment|resignation)[^)]{0,80}\)|in\s+case\s+of\s+appointment(?:\s+of\s+(?:a\s+)?director)?|"
    r"reasons?\s+for\s+change\s*(?:viz\.?|i\.e\.?|such\s+as)?", re.I)
ADDRESSEE_RX = re.compile(r"\bTo,?\s+(?:The\s+)?(?:Board\s+of\s+Directors|Chairman|Chairperson)?[\s,/&and]*(?:The\s+)?$", re.I)


def squash(text: str) -> str:
    return re.sub(r"[ \t\r\f\v]+", " ", re.sub(r"\s*\n\s*", " ", text or ""))


def strip_labels(text: str) -> str:
    """The text with the disclosure table's row labels blanked (same
    length, so positions still point into the original)."""
    return BOILER_RX.sub(lambda m: " " * len(m.group(0)), text)


def _sentence_window(t: str, a: int, b: int, w: int = WINDOW) -> tuple[int, int]:
    """The window around t[a:b]: up to `w` characters each side, but not past
    a paragraph of unrelated business (two sentence ends away)."""
    lo, hi = max(0, a - w), min(len(t), b + w)
    left = [m.end() for m in re.finditer(r"[.;:]\s+(?=[A-Z0-9])", t[lo:a])]
    if len(left) >= 2:
        lo = lo + left[-2]
    right = [m.start() for m in re.finditer(r"[.;]\s+(?=[A-Z0-9])", t[b:hi])]
    if len(right) >= 2:
        hi = b + right[1] + 1
    return lo, hi


def kmp_hits(text: str, max_hits: int = 40) -> list[dict]:
    """Every mention of a CEO / MD / CFO seat with an appointment or a
    cessation beside it: [{seat, role_text, event, event_text, lower,
    unit, person, snippet, pos}]. `event` is 'appointment', 'cessation' or
    'reappointment' (the nearest event word decides; a re-appointment is
    reported, never counted as a change). `lower` marks a deputy / regional
    seat, `unit` a seat of a division or another company."""
    raw = squash(text)
    t = strip_labels(raw)
    out, seen = [], set()
    for m in ROLE_RX.finditer(t):
        seat = SEAT[m.lastgroup]
        if ADDRESSEE_RX.search(t[max(0, m.start() - 40):m.start()]):       # 'To, The Managing Director' on a letter
            continue
        lo, hi = _sentence_window(t, m.start(), m.end())
        win = t[lo:hi]
        rel = m.start() - lo
        best = None
        for kind, rx in (("reappointment", REAPPOINT_RX), ("appointment", APPOINT_RX), ("cessation", CEASE_RX)):
            for e in rx.finditer(win):
                d = min(abs(e.start() - rel), abs(e.end() - rel))
                # a re-appointment word contains 'appoint': the longer match at the same place wins
                rank = (d, 0 if kind == "reappointment" else 1)
                if best is None or rank < best[0]:
                    best = (rank, kind, e.group(0))
        if best is None:
            continue
        lower = bool(LOWER_RX.search(t[max(0, m.start() - 22):m.start()]))
        after = t[m.end():m.end() + 90]
        unit = bool(UNIT_AFTER_RX.match(after) or UNIT_DASH_RX.match(after))
        people = [(abs(p.start() - rel), p.group(1).strip()) for p in PERSON_RX.finditer(win)]
        person = min(people)[1] if people else ""
        key = (seat, best[1], person, lower, unit)
        if key in seen:
            continue
        seen.add(key)
        out.append({"seat": seat, "role_text": m.group(0), "event": best[1], "event_text": best[2],
                    "lower": lower, "unit": unit, "person": person,
                    "snippet": raw[lo:hi].strip()[:520], "pos": m.start()})
        if len(out) >= max_hits:
            break
    return out


def kmp_flags(text: str) -> set[tuple[str, str]]:
    """{(seat, event)} for the company's own top seats: appointment or
    cessation only — the candidates a judge must read."""
    return {(h["seat"], h["event"]) for h in kmp_hits(text)
            if h["event"] in ("appointment", "cessation") and not h["lower"] and not h["unit"]}


# -------------------------------------------------------------- ownership
OWN_RULES = {
    "open_offer": re.compile(
        r"\bopen\s+offer\b|\bpublic\s+announcement\b.{0,160}\b(?:acqui|takeover|regulation\s+3|regulation\s+4)|"
        r"\bdetailed\s+public\s+statement\b|\bletter\s+of\s+offer\b.{0,200}\b(?:acquirer|takeover|sast)|"
        r"\bregulations?\s+3\s*\(\s*1\s*\)\s*(?:and|&|read with)\s*(?:regulation\s+)?4\b", re.I | re.S),
    "change_of_control": re.compile(
        r"\bchange\s+(?:in|of)\s+(?:the\s+)?(?:control|management\s+control|ownership|promoters?)\b|\bacqui\w+\s+(?:of\s+)?(?:sole\s+|joint\s+)?control\b|"
        r"\b(?:controlling|majority)\s+(?:stake|interest|shareholding)\b.{0,80}\b(?:in|of)\s+the\s+company\b|"
        r"\bnew\s+promoters?\b|\bincoming\s+promoters?\b|\bclassified\s+as\s+(?:a\s+)?promoters?\b|\bbecome\s+(?:a\s+|the\s+)?promoters?\b", re.I | re.S),
    "promoter_sale": re.compile(
        r"\bpromoters?\b.{0,140}\b(?:sale|sell|sold|divest\w*|dispos\w*|exit\w*|offload\w*|transfer\w*)\b.{0,140}\b(?:stake|shares?|shareholding|holding)\b|"
        r"\b(?:sale|sell|sold|divest\w*|dispos\w*|transfer\w*)\b.{0,100}\b(?:stake|shares?|shareholding)\b.{0,100}\bby\s+(?:the\s+)?promoters?\b|"
        r"\bshare\s+purchase\s+agreement\b.{0,300}\bpromoters?\b|\bpromoters?\b.{0,300}\bshare\s+purchase\s+agreement\b", re.I | re.S),
    "reclassification": re.compile(
        r"\bre-?classif\w+\b.{0,160}\bpromoters?\b|\bpromoters?\b.{0,160}\bre-?classif\w+\b|\bregulation\s+31A\b|"
        r"\bceas\w+\s+to\s+be\s+(?:a\s+|the\s+)?promoters?\b", re.I | re.S),
    "disinvestment": re.compile(r"\bstrategic\s+disinvestment\b|\bdisinvestment\s+of\s+(?:the\s+)?(?:government|goi)\b|"
                                r"\boffer\s+for\s+sale\b.{0,160}\b(?:promoter|president\s+of\s+india|government)", re.I | re.S),
    "insolvency": re.compile(r"\bresolution\s+plan\b.{0,200}\b(?:approved|successful\s+resolution\s+applicant)\b|"
                             r"\bsuccessful\s+resolution\s+applicant\b", re.I | re.S),
    "family": re.compile(r"\bfamily\s+(?:settlement|arrangement|separation|realignment)\b|\binter[\s-]se\s+transfer\b|"
                         r"\bby\s+way\s+of\s+gift\b|\btransmission\s+of\s+shares\b|\bsuccession\b.{0,80}\bpromoter", re.I | re.S),
}
# the company as the TARGET, not as the buyer of something else
TARGET_RX = re.compile(r"\b(?:of|in)\s+(?:the\s+)?(?:target\s+)?company\b|\btarget\s+company\b|\bequity\s+(?:share\s+)?capital\s+of\s+the\s+company\b|"
                       r"\bpromoters?\s+(?:and\s+promoter\s+group\s+)?of\s+the\s+company\b|\bthe\s+company'?s\s+promoters?\b|"
                       r"\bour\s+promoters?\b|\bpublic\s+shareholders\b", re.I)
OWN_STRONG = ("open_offer", "change_of_control", "reclassification", "disinvestment", "insolvency")


def ownership_hits(text: str, max_per_rule: int = 3) -> list[dict]:
    """[{rule, target, snippet}] — ownership language in a filing's text.
    `target` says the sentence speaks of THIS company's own shares or
    promoters (a company announcing that it is buying control of another
    is not changing hands itself)."""
    t = squash(text)
    out = []
    for rule, rx in OWN_RULES.items():
        n = 0
        for m in rx.finditer(t):
            lo, hi = max(0, m.start() - 240), min(len(t), m.end() + 240)
            win = t[lo:hi]
            out.append({"rule": rule, "target": bool(TARGET_RX.search(win)), "snippet": win.strip()[:560],
                        "pos": m.start()})
            n += 1
            if n >= max_per_rule:
                break
    return out


def ownership_flags(text: str) -> set[str]:
    """Rules that fire with this company as the target (a strong rule needs
    one such sentence, the softer ones two)."""
    by: dict[str, int] = {}
    for h in ownership_hits(text, max_per_rule=6):
        if h["target"]:
            by[h["rule"]] = by.get(h["rule"], 0) + 1
    return {r for r, n in by.items() if n >= (1 if r in OWN_STRONG else 2)}


# -------------------------------------------------------------- the store

def _f(x) -> float | None:
    try:
        return float(str(x).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def window(today: dt.date, days: int = WINDOW_DAYS) -> tuple[str, str]:
    return (today - dt.timedelta(days=days)).isoformat(), today.isoformat()


def load_filings(today: dt.date, days: int = WINDOW_DAYS) -> list[dict]:
    """Every filing of the window that has text on file, from both stores:
    the management / takeover filings read in full for this skill, and the
    first pages the all-filings store keeps for every other material
    category. Each row: date, symbol, company, category, headline,
    attachment, ann_id, text_path, origin."""
    start, end = window(today, days)
    out, seen = [], set()
    for r in MF.read_csv(MF.FILINGS):
        if not (start <= r["date"] <= end) or r.get("read_status") != "read":
            continue
        seen.add(r["ann_id"])
        # a large board outcome or press release read here is still a general filing: only its opening counts for a seat
        origin = "store" if r["category"] in MF.BIG_CATEGORIES else "mgmt"
        out.append({**{k: r[k] for k in ("date", "symbol", "company", "category", "headline", "attachment", "ann_id")},
                    "text_path": str(DATA / r["text_file"]), "origin": origin})
    for r in DR.load_all().values():
        if not (start <= r["date"] <= end) or r["ann_id"] in seen:
            continue
        if r.get("read_status") != "read" or not r.get("first_text"):
            continue
        out.append({**{k: r[k] for k in ("date", "symbol", "company", "category", "headline", "attachment", "ann_id")},
                    "text_path": str(FA.OUT_DIR / r["first_text"]), "origin": "store"})
    out.sort(key=lambda r: (r["symbol"], r["date"], r["ann_id"]))
    return out


def text_of(row: dict) -> str:
    p = Path(row.get("text_path") or "")
    try:
        return p.read_text(errors="replace") if p.is_file() else ""
    except OSError:
        return ""


# categories whose text can announce a change of seat; a results PDF or an
# order win mentions the CFO only as a signatory
KMP_SCAN_SKIP = {"Loss of Share Certificates", "Issue of Duplicate Share Certificate", "Record Date",
                 "Allotment of Securities", "Incorporation", "Product launch", "Awarding of order(s)/contract(s)",
                 "Registrar & Share Transfer Agent Update", "Address Change", "Buyback", "Bonus", "Stock split",
                 "Disclosure under SEBI Takeover Regulations", "Trading Plan under PIT"}
# in a category that is not about management, the mention must be the news, not a passing line:
# it has to sit in the opening of the document
KMP_OPENING_CHARS = 6000


def scan_filing(row: dict, text: str | None = None) -> dict:
    """The mechanical read of one filing: its KMP hits and ownership hits."""
    text = text_of(row) if text is None else text
    kmp, own = [], []
    if row["category"] not in KMP_SCAN_SKIP:
        body = text if row.get("origin") == "mgmt" else text[:KMP_OPENING_CHARS]
        kmp = [h for h in kmp_hits(body) if h["event"] in ("appointment", "cessation")]
    own = [h for h in ownership_hits(text) if h["target"]]
    flags = ownership_flags(text)
    return {"kmp": kmp, "kmp_flags": sorted({(h["seat"], h["event"]) for h in kmp if not h["lower"] and not h["unit"]}),
            "own": own, "own_flags": sorted(flags), "chars": len(text)}


# --------------------------------------------------- shareholding register

def shareholding_moves(rows: list[dict], today: dt.date, days: int = WINDOW_DAYS) -> dict[str, dict]:
    """Per symbol, the promoter-and-group holding over the window from the
    exchange's quarterly register: the quarter end at or before the window
    opened (the base), every quarter since, the change, the largest single
    quarter's change and the thresholds crossed (50%, 25%, nil)."""
    start, end = window(today, days)
    by: dict[str, list[tuple[str, float]]] = {}
    for r in rows:
        v = _f(r.get("promoter_pct"))
        if v is None or not r.get("as_of") or r["as_of"] > end:
            continue
        by.setdefault(r["symbol"], []).append((r["as_of"], v))
    out = {}
    for sym, ser in by.items():
        ser = sorted(set(ser))
        before = [x for x in ser if x[0] <= start]
        base = before[-1] if before else ser[0]
        path = [base] + [x for x in ser if x[0] > base[0]]
        if len(path) < 2:
            out[sym] = {"series": path, "base": base, "latest": base, "change": 0.0, "max_step": 0.0,
                        "crossed": [], "level": "none"}
            continue
        steps = [(b[0], round(b[1] - a[1], 2)) for a, b in zip(path, path[1:])]
        change = round(path[-1][1] - base[1], 2)
        big = max(steps, key=lambda s: abs(s[1]))
        crossed = []
        for th, name in ((50.0, "50%"), (25.0, "25%")):
            if (base[1] >= th) != (path[-1][1] >= th):
                crossed.append(("below " if path[-1][1] < th else "above ") + name)
        if (base[1] > 0) != (path[-1][1] > 0):
            crossed.append("to nil" if path[-1][1] == 0 else "from nil")
        mag = max(abs(change), abs(big[1]))
        level = "major" if (mag >= 5 or crossed) else ("minor" if mag >= 2 else "none")
        out[sym] = {"series": path, "base": base, "latest": path[-1], "change": change,
                    "max_step": big[1], "max_step_quarter": big[0], "crossed": crossed, "level": level}
    return out


# ----------------------------------------------------- Reg 29 disclosures

def sast_summary(rows: list[dict], today: dt.date, days: int = WINDOW_DAYS) -> dict[str, dict]:
    """Per symbol over the window: what promoters sold and bought (% of
    capital, summed over their Reg 29 disclosures), and every outside
    acquirer whose holding after the trade is 10% or more."""
    start, end = window(today, days)
    out: dict[str, dict] = {}
    for r in rows:
        if not (start <= (r.get("date") or "") <= end):
            continue
        s = out.setdefault(r["symbol"], {"promoter_sold": 0.0, "promoter_bought": 0.0, "outsiders": [], "rows": []})
        sold, got, after = _f(r.get("pct_sold")) or 0.0, _f(r.get("pct_acquired")) or 0.0, _f(r.get("pct_after"))
        prom = (r.get("promoter") or "").upper().startswith("Y")
        if prom:
            s["promoter_sold"] = round(s["promoter_sold"] + sold, 2)
            s["promoter_bought"] = round(s["promoter_bought"] + got, 2)
        elif after is not None and after >= 10 and got > 0:
            s["outsiders"].append({"acquirer": r["acquirer"], "pct_after": after, "pct_acquired": got, "date": r["date"],
                                   "mode": r.get("mode", "")})
        s["rows"].append(r)
    for s in out.values():
        s["level"] = ("major" if (s["promoter_sold"] >= 5 or any(o["pct_after"] >= 25 for o in s["outsiders"]))
                      else "minor" if (s["promoter_sold"] >= 2 or s["promoter_bought"] >= 5 or s["outsiders"]) else "none")
    return out


# ---------------------------------------------------- bulk and block deals

def shares_outstanding(as_of: dt.date | None = None) -> dict[str, float]:
    """Shares outstanding per symbol from the newest bhavcopy bundle's
    market-cap file (market cap / close)."""
    import io, zipfile                                # noqa: PLC0415, E401
    files = sorted(BUNDLES.glob("PR*.zip"), key=lambda p: (p.name[6:8], p.name[4:6], p.name[2:4]), reverse=True)
    for p in files:
        d = dt.date(2000 + int(p.name[6:8]), int(p.name[4:6]), int(p.name[2:4]))
        if as_of and d > as_of:
            continue
        try:
            with zipfile.ZipFile(p) as z:
                name = next((n for n in z.namelist() if n.lower().startswith("mcap")), None)
                if not name:
                    continue
                rd = csv.DictReader(io.StringIO(z.read(name).decode("utf-8", "replace")))
                out = {}
                for r in rd:
                    r = {(k or "").strip(): (v or "").strip() for k, v in r.items() if k}
                    sym = r.get("Symbol") or r.get("SYMBOL")
                    n = _f(r.get("Issue Size") or r.get("ISSUE SIZE") or r.get("Issue Size(No. of Shares)"))
                    if n is None:
                        cap, px = _f(r.get("Market Cap(Rs.)") or r.get("Market Cap")), _f(r.get("Close Price/Paid up value(Rs.)") or r.get("Close Price"))
                        n = cap / px if cap and px else None
                    if sym and n:
                        out[sym] = n
                if out:
                    return out
        except (zipfile.BadZipFile, OSError, StopIteration):
            continue
    return {}


def deals_summary(rows: list[dict], today: dt.date, shares: dict[str, float], days: int = WINDOW_DAYS) -> dict[str, dict]:
    """Per symbol over the window: each client's net selling and buying in
    bulk / block deals as % of the shares outstanding; `level` major when one
    client sold 5% or more."""
    start, end = window(today, days)
    acc: dict[str, dict[tuple[str, str], float]] = {}
    for r in rows:
        if not (start <= (r.get("date") or "") <= end):
            continue
        q = _f(r.get("quantity"))
        if not q:
            continue
        key = (re.sub(r"[^A-Z0-9 ]", "", (r.get("client") or "").upper()).strip(), (r.get("side") or "").upper())
        acc.setdefault(r["symbol"], {})
        acc[r["symbol"]][key] = acc[r["symbol"]].get(key, 0.0) + q
    out = {}
    for sym, d in acc.items():
        n = shares.get(sym)
        clients = {}
        for (client, side), q in d.items():
            c = clients.setdefault(client, {"client": client, "sold": 0.0, "bought": 0.0})
            c["sold" if side.startswith("S") else "bought"] += q
        rows_ = []
        for c in clients.values():
            c["sold_pct"] = round(100 * c["sold"] / n, 2) if n else None
            c["bought_pct"] = round(100 * c["bought"] / n, 2) if n else None
            # a broker crossing both sides the same day is not a holder changing
            net = (c["sold_pct"] or 0) - (c["bought_pct"] or 0)
            c["net_sold_pct"] = round(net, 2)
            rows_.append(c)
        rows_.sort(key=lambda c: -abs(c["net_sold_pct"]))
        top_sell = max((c["net_sold_pct"] for c in rows_), default=0)
        top_buy = max((-c["net_sold_pct"] for c in rows_), default=0)
        out[sym] = {"clients": rows_[:8], "top_seller_pct": top_sell, "top_buyer_pct": top_buy,
                    "level": "major" if top_sell >= 5 or top_buy >= 10 else ("minor" if top_sell >= 2 or top_buy >= 5 else "none")}
    return out


# ------------------------------------------------------------------ calls
CALL_KMP_RX = re.compile(
    r"\bnew\s+(?:c\.?e\.?o|c\.?f\.?o|m\.?d\b|managing\s+director|chief\s+(?:executive|financial)\s+officer)|"
    r"\b(?:joined|joining|taken\s+over|took\s+over|appointed|taking\s+over|assumed\s+charge)\s+(?:us\s+)?as\s+(?:the\s+|our\s+)?(?:new\s+|group\s+)?"
    r"(?:c\.?e\.?o|c\.?f\.?o|m\.?d\b|managing\s+director|chief\s+(?:executive|financial)\s+officer)|"
    r"\b(?:my|his|her)\s+(?:first|last|final)\s+(?:earnings\s+|conference\s+|investor\s+)?call\b|"
    r"\b(?:c\.?e\.?o|c\.?f\.?o|managing\s+director|chief\s+(?:executive|financial)\s+officer)\s+(?:designate|elect)\b|"
    r"\b(?:stepping|stepped|step)\s+down\s+(?:as|from)\b|\bsuccession\s+plan\w*\b|\b(?:c\.?e\.?o|c\.?f\.?o|leadership|management)\s+(?:transition|succession|change)\b|"
    r"\bwelcome\b.{0,80}\b(?:c\.?e\.?o|c\.?f\.?o|managing\s+director|chief\s+(?:executive|financial)\s+officer)\b|"
    r"\bsearch\s+for\s+(?:a\s+)?(?:new\s+)?(?:c\.?e\.?o|c\.?f\.?o|managing\s+director)", re.I | re.S)
CALL_OWN_RX = re.compile(
    r"\bopen\s+offer\b|\bnew\s+promoters?\b|\bchange\s+(?:in|of)\s+(?:control|ownership|promoters?)\b|"
    r"\bpromoters?\b.{0,80}\b(?:stake\s+sale|selling|sold|exit\w*|divest\w*|offload\w*)\b|"
    r"\b(?:stake\s+sale|sale\s+of\s+stake)\b.{0,60}\bpromoters?\b|\b(?:controlling|majority)\s+stake\b.{0,60}\b(?:in\s+(?:us|the\s+company|our\s+company)|acquired\s+by)\b|"
    r"\bstrategic\s+(?:investor|partner)\b.{0,80}\b(?:control|majority|promoter)\b|\bnew\s+(?:owner|parent|shareholder)s?\b", re.I | re.S)


def call_text(symbol: str) -> str:
    """The stored transcripts' text for a company, cached as text beside
    the PDFs (extraction is slow; the cache follows the PDF's mtime)."""
    pdf = CONCALLS / f"{symbol}.pdf"
    if not pdf.exists():
        return ""
    CALL_CACHE.mkdir(parents=True, exist_ok=True)
    cache = CALL_CACHE / f"{symbol.replace('&', '_')}.txt"
    if cache.exists() and cache.stat().st_mtime >= pdf.stat().st_mtime:
        return cache.read_text(errors="replace")
    text = ""
    import shutil, subprocess                            # noqa: PLC0415, E401
    exe = shutil.which("pdftotext")
    if exe:                                              # poppler: seconds, where PyPDF2 takes minutes
        try:
            out = subprocess.run([exe, "-q", str(pdf), "-"], capture_output=True, timeout=300).stdout
            text = DR.clean_text(out.decode("utf-8", "replace").replace("\f", "\n"))
        except (subprocess.SubprocessError, OSError):
            text = ""
    if "Call: " not in text:
        try:
            import PyPDF2                                # noqa: PLC0415
            reader = PyPDF2.PdfReader(str(pdf), strict=False)
            text = DR.clean_text("\n".join((pg.extract_text() or "") for pg in reader.pages))
        except Exception:                                # noqa: BLE001
            pass
    cache.write_text(text, encoding="utf-8")
    return text


_MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


def call_sections(text: str) -> list[tuple[str, dt.date, str]]:
    """[(label 'MMM YYYY', first of that month, section text)] oldest first."""
    parts = re.split(r"Call: (\w{3} \d{4})", text or "")
    out = []
    for i in range(1, len(parts) - 1, 2):
        m = re.match(r"(\w{3}) (\d{4})", parts[i])
        if m and m.group(1) in _MONTHS:
            out.append((parts[i], dt.date(int(m.group(2)), _MONTHS[m.group(1)], 1), parts[i + 1]))
    return sorted(out, key=lambda x: x[1])


def call_hits(symbol: str, today: dt.date, months: int = 13, text: str | None = None) -> list[dict]:
    """Management-change language in the calls of the last `months` months:
    [{call, kind 'kmp'|'ownership', term, snippet}]."""
    text = call_text(symbol) if text is None else text
    cutoff = dt.date(today.year, today.month, 1) - dt.timedelta(days=months * 31)
    out = []
    for label, d, body in call_sections(text):
        if d < cutoff or d > today:
            continue
        t = squash(body)
        for kind, rx in (("kmp", CALL_KMP_RX), ("ownership", CALL_OWN_RX)):
            n = 0
            for m in rx.finditer(t):
                lo, hi = max(0, m.start() - 260), min(len(t), m.end() + 320)
                out.append({"call": label, "date": d.isoformat(), "kind": kind, "term": re.sub(r"\s+", " ", m.group(0))[:60],
                            "snippet": t[lo:hi].strip()})
                n += 1
                if n >= 4:
                    break
    return out


# roster: who the transcript lists as management, with the seat
_TITLE = r"(?:Mr|Ms|Mrs|Shri|Smt|Dr|Sri|Prof|CA)\.?\s+"
_NAME = r"[A-Z][A-Za-z.'’-]*(?:\s+[A-Z][A-Za-z.'’-]*){1,4}"
ROSTER_INLINE_RX = re.compile(
    r"(?:" + _TITLE + r")(" + _NAME + r")\s*[-–—:,]\s*(?P<rest>[^\n;]{0,110})", re.I)
ROSTER_NAME_LINE_RX = re.compile(r"^(?:" + _TITLE + r")?(" + _NAME + r")$")
ROSTER_PLAIN_RX = re.compile(r"^(?:" + _TITLE + r")?(" + _NAME + r")\s*[-–—:,]\s*(?P<rest>.{3,110})$")
ROSTER_UNIT_RX = re.compile(r"\b(?:business|division|vertical|segment|region|subsidiar\w*|operations|international|india\s+business)\b", re.I)
_NOT_A_NAME = re.compile(r"\b(?:limited|ltd|management|participants?|moderator|analyst|conference|call|officer|director|"
                         r"chairman|president|head|secretary|bank|capital|securities|research|investor|relations)\b", re.I)


def _seats_in(role_text: str, company: str = "") -> set[str]:
    """The top seats a designation names ('Managing Director & CEO' → MD
    and CEO); nothing for a deputy seat or the seat of a business unit."""
    out = set()
    co = {w for w in re.findall(r"[a-z]{4,}", (company or "").lower())} - {"limited", "india", "company", "corporation"}
    last = 0
    for m in ROLE_RX.finditer(role_text):
        gap, last = role_text[last:m.start()], m.end()
        if len(gap.split()) > 5:                      # a sentence a speaker said, not a designation
            break
        if LOWER_RX.search(role_text[max(0, m.start() - 22):m.start()]):
            continue
        after = role_text[m.end():m.end() + 70]
        tail = re.match(r"\s*(?:[-–—,(]|of\b)\s*(.+)", after)
        if tail and not re.match(r"\s*(?:&|and|cum)\b", after):
            words = set(re.findall(r"[a-z]{4,}", tail.group(1).lower()))
            if ROSTER_UNIT_RX.search(tail.group(1)) and not (words & co):
                continue                              # 'CEO – Emerging Business'; 'CFO – Coromandel International' is the company
        out.add(SEAT[m.lastgroup])
    return out


def roster(section: str, company: str = "", head_chars: int = 6000) -> dict[str, set[str]]:
    """{seat: {names}} from the participants block at the top of one call's
    transcript, in the three ways transcripts print it: 'Mr. A B – Chief
    Financial Officer' on one line, 'A B – CFO' without a title, and the
    name on one line with the designation on the next."""
    head = section[:head_chars]
    out: dict[str, set[str]] = {}

    def add(name: str, role_text: str) -> None:
        if _NOT_A_NAME.search(name) or len(norm_name(name).split()) < 2:
            return
        for seat in _seats_in(role_text, company):
            out.setdefault(seat, set()).add(norm_name(name))

    for m in ROSTER_INLINE_RX.finditer(head):
        add(m.group(1), m.group("rest"))
    lines = [re.sub(r"\s+", " ", x).strip() for x in head.splitlines()]
    lines = [x for x in lines if x]
    for i, line in enumerate(lines):
        if len(line) > 130:
            continue
        m = ROSTER_PLAIN_RX.match(line)
        if m and ROLE_RX.search(m.group("rest")):
            add(m.group(1), m.group("rest"))
        elif i and ROLE_RX.search(line) and len(line) <= 90 and not ROSTER_NAME_LINE_RX.match(line):
            prev = ROSTER_NAME_LINE_RX.match(lines[i - 1])
            if prev and not ROLE_RX.search(lines[i - 1]):
                add(prev.group(1), line)
    return out


def norm_name(name: str) -> str:
    """A person's name for comparison: titles and initials' dots dropped,
    lower case, single spaces."""
    n = re.sub(r"\b(?:Mr|Ms|Mrs|Shri|Smt|Dr|Sri|Prof|CA|CS)\.?\s+", "", name or "", flags=re.I)
    n = re.sub(r"[^A-Za-z ]", " ", n).lower()
    return re.sub(r"\s+", " ", n).strip()


def same_person(a: str, b: str) -> bool:
    """Two spellings of one person: the same surname and a first name that
    agrees (in full or by initial); or one name's words contained in the
    other's."""
    x, y = norm_name(a).split(), norm_name(b).split()
    if not x or not y:
        return False
    if set(x) <= set(y) or set(y) <= set(x):
        return len(set(x) & set(y)) >= 1 and (len(x) > 1 or len(y) > 1 or x == y)
    if x[-1] != y[-1]:
        return False
    return x[0] == y[0] or x[0][0] == y[0][0] and (len(x[0]) == 1 or len(y[0]) == 1)


def roster_changes(symbol: str, today: dt.date, text: str | None = None, months: int = 14, company: str = "") -> list[dict]:
    """An independent check on the filings: for each seat, the names the
    earliest and the latest call of the window list. A seat whose names do
    not overlap changed hands in between."""
    text = call_text(symbol) if text is None else text
    cutoff = dt.date(today.year, today.month, 1) - dt.timedelta(days=months * 31)
    secs = [(label, d, roster(body, company)) for label, d, body in call_sections(text) if cutoff <= d <= today]
    out = []
    for seat in ("CEO", "MD", "CFO"):
        have = [(label, d, r[seat]) for label, d, r in secs if r.get(seat)]
        if len(have) < 2:
            continue
        first, last = have[0], have[-1]
        if not any(same_person(a, b) for a in first[2] for b in last[2]):
            out.append({"seat": seat, "from_call": first[0], "to_call": last[0],
                        "before": sorted(first[2]), "after": sorted(last[2])})
    return out
