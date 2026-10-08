"""
spinoff.py — the special-situation framework for spin-offs, mechanised.

Everything here is pure: it reads the stored filings (Announcements/),
the stored conference calls, statements and market data, and derives
SITUATIONS — one per company per restructuring — each judged against
the checklist in the source notes (Greenblatt, "You Can Be a Stock
Market Genius", spin-offs chapter):

  1. WHY the spin-off — unrelated businesses separated; a bad business
     carved away so the good one shows; value for a business that
     cannot be sold; a regulatory / strategic / anti-trust knot untied.
  2. WHO WANTS IT — institutions do not (size, industry, no coverage):
     the selling pressure that makes the bargain; insiders DO (stock,
     options, a CEO moving to the spun entity, promoters keeping a
     stake); the date the option price is set.
  3. WHAT IS REVEALED — a great business or a statistically cheap one;
     leverage that turns a small asset move into a doubled stock;
     pro-forma statements and the comparable P/E that price it.
  4. THE PARENT — often the better buy before the spin; institutions
     buy the clean parent afterwards; a regulated-industry spin may
     prelude a takeover of the parent.
  5. PARTIAL spin-offs — the listed piece prices the stub.
  6. RIGHTS offerings — confusion, an oversubscription clause, insiders
     declaring they will oversubscribe.
  7. TIMING — the first year is selling pressure; the largest gains
     came in the second year.

Nothing here invents numbers. Where the data on file cannot answer a
checklist item, the item says so and names what to read.
"""

from __future__ import annotations

import csv
import datetime as dt
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
sys.path.insert(0, str(INDIA / "Announcements"))

import fetch_announcements as FA          # noqa: E402  (classify, paths)

ANN_DIR = FA.OUT_DIR
CONCALLS = INDIA / "ConferenceCalls" / "NiftyTotalMarket"
BALANCE = INDIA / "BalanceSheet" / "NiftyTotalMarket"
PNL = INDIA / "ProfitStatement" / "NiftyTotalMarket"
LIVE = INDIA / "StockInfo" / "Nifty500" / "live_market_data.csv"
CONSTITUENTS = FA.CONSTITUENTS

SPIN_KINDS = ("demerger", "subsidiary_listing", "scheme_other")
LISTING_LAG_DAYS = 30        # a record date this old means the new entity trades
CONCALL_MONTHS = 12
_MONTHS = {m: i + 1 for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}

# ------------------------------------------------------------ the stages

STAGES = [
    ("announced",   re.compile(r"board.{0,40}(approv|consider|propos)\w*.{0,80}(de-?merg|scheme|spin|arrangement|hive|list)|"
                               r"propos\w* (de-?merger|scheme|spin|arrangement)|in[- ]principle approval|"
                               r"(announc|intimat)\w* .{0,40}(de-?merger|spin|scheme of arrangement)", re.I)),
    ("exchange_noc", re.compile(r"no[- ]objection|no observation|observation letter", re.I)),
    ("meetings",    re.compile(r"(shareholders?|creditors?|equity shareholders).{0,40}meeting|nclt[- ]convened|postal ballot.{0,60}scheme", re.I)),
    ("nclt_sanction", re.compile(r"(sanction|approv\w*|order).{0,40}(nclt|national company law tribunal)|(nclt|tribunal).{0,60}(sanction|approv|order)", re.I)),
    ("effective",   re.compile(r"scheme.{0,40}(effective|become effective|came into effect)|effective date|certified copy.{0,40}order.{0,40}filed", re.I)),
    ("record_date", re.compile(r"record date", re.I)),
    ("listed",      re.compile(r"listing (and|&) (commencement of )?trading|commencement of trading|trading approval|"
                               r"admitted to dealings|listed (on|with) the (stock )?exchange|"
                               r"listing(?! regulations?| obligations?) .{0,60}(resulting|demerged) compan|"
                               r"allotment of (equity )?shares.{0,60}(scheme|de-?merger|resulting)", re.I)),
]
STAGE_ORDER = [s for s, _ in STAGES]
PRE_STAGES = ("rumoured", "announced", "exchange_noc", "meetings", "nclt_sanction")


def stage_of(text: str) -> str | None:
    """The furthest stage a filing's words reach, or None."""
    hits = [s for s, rx in STAGES if rx.search(text or "")]
    return max(hits, key=STAGE_ORDER.index) if hits else None


# ---------------------------------------------------------- the reasons

REASONS = [
    ("unrelated businesses separated",
     re.compile(r"unrelated|distinct (business|nature)|different (business|risk|growth) profile|"
                r"separate (and )?(distinct|focused)|focus(ed)? (management|strateg)|"
                r"independent (growth|strateg|management)", re.I)),
    ("value unlocking for shareholders",
     re.compile(r"unlock\w* (shareholder )?value|value unlocking|value creation|"
                r"better (appreciat|valuation)|appropriate valuation|"
                r"(realise|realize|discover) (its |the |true |fair )?value", re.I)),
    ("a weak or capital-heavy business carved away",
     re.compile(r"capital[- ]intensive|debt[- ]laden|loss[- ]making|turnaround|"
                r"legacy|non[- ]core|de[- ]?leverag|ring[- ]fenc", re.I)),
    ("regulatory / strategic knot",
     re.compile(r"(regulatory|statutory) (constraint|restriction|reason|hurdle)s?\b|"
                r"licen[cs]e (condition|requirement)|(mandated|required|directed) by "
                r"(the )?(regulator|rbi|sebi|irdai|dot|cci)\b|"
                r"anti[- ]?trust|competition commission|\bcci\b|"
                r"\brbi\b.{0,40}(requir|direct|mandate)|"
                r"strategic (partner|investor|alliance)", re.I)),
    ("attracting different investors / capital",
     re.compile(r"attract\w* (a |an )?(different|distinct|new|specific|appropriate|separate) (set of |class of )?investor|"
                r"investor base|access (to )?(capital|markets)|raise (growth )?capital|"
                r"flexibility to (raise|pursue)", re.I)),
]


def reasons_in(text: str) -> list[dict]:
    """The stated reasons, each with a short verbatim quote."""
    out = []
    for label, rx in REASONS:
        m = rx.search(text or "")
        if m:
            out.append({"reason": label, "quote": _snippet(text, m.start(), m.end())})
    return out


def _snippet(text: str, a: int, b: int, pad: int = 110) -> str:
    s = text[max(0, a - pad): min(len(text), b + pad)]
    s = re.sub(r"\s+", " ", s).strip()
    return ("…" if a - pad > 0 else "") + s + ("…" if b + pad < len(text) else "")


# ---------------------------------------------------- facts in the text

RATIO_RX = re.compile(
    r"(\d[\d,]*)\s*(?:\(\w+\)\s*)?(?:fully paid[- ]up )?equity share\w*.{0,80}?"
    r"(?:for|against) every\s+(\d[\d,]*)\s*(?:\(\w+\)\s*)?(?:fully paid[- ]up )?equity share",
    re.I | re.S)
DATE_WORDS = re.compile(
    r"(\d{1,2})(?:st|nd|rd|th)?\s+(January|February|March|April|May|June|July|"
    r"August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|"
    r"Sep|Sept|Oct|Nov|Dec)[,.]?\s+(\d{4})", re.I)
RESULTING_RX = re.compile(
    r"(?:resulting|transferee|new)\s+compan(?:y|ies)[\"'”’\s]*[,:(]?\s*(?:i\.e\.|means|being|namely)?\s*"
    r"[\"'“‘]?([A-Z][A-Za-z0-9&.\- ]{3,70}?(?:Limited|Ltd\.?|Private Limited))", re.S | re.I)
# the usual drafting: Alpha Energy Limited ("Resulting Company")
RESULTING_BEFORE_RX = re.compile(
    r"([A-Z][A-Za-z0-9&.\- ]{3,70}?(?:Limited|Ltd\.?))\s*\(\s*[\"'“‘]?(?:the\s+)?"
    r"(?:resulting|transferee)\s+company", re.I)
UNDERTAKING_RX = re.compile(
    r"demerged undertaking[\"'”’\s]*[,:(]?\s*(?:i\.e\.|means|being|namely|shall mean)?\s*(.{10,200}?)[.;\n]",
    re.I | re.S)
PROFORMA_RX = re.compile(r"pro[- ]?forma", re.I)
NEWS_RX = re.compile(r"news verification|sought clarification|news item|rumou?r|denie[sd]|"
                     r"clarification on (news|media)", re.I)
ESOP_RX = re.compile(r"\b(stock options?|esops?|esos|restricted stock|rsus?)\b.{0,160}?"
                     r"\b(exercise price|grant|pric\w+|adjust\w*)\b", re.I | re.S)
INSIDER_RX = re.compile(
    r"promoter\w*.{0,60}?(shall |will |to )?(continue to (hold|own|remain)|retain|"
    r"same (percentage|proportion)|mirror(ed)? shareholding|identical shareholding)|"
    r"shareholding (pattern )?(of|in) the resulting compan.{0,80}?(mirror|same|identical)|"
    r"(managing director|chief executive|ceo|whole[- ]time director).{0,80}?"
    r"(resulting|demerged|new) compan", re.I | re.S)
OVERSUB_RX = re.compile(r"additional (rights )?(equity )?shares|over[- ]?subscri\w+|"
                        r"apply for additional|renounc", re.I)
INSIDER_OVERSUB_RX = re.compile(
    r"promoter\w*.{0,120}?(subscribe|oversubscri|additional|unsubscribed|entitlement)", re.I | re.S)
SMALL_RX = re.compile(r"(\d{1,2}(?:\.\d+)?)\s*%\s*(?:of)?\s*(?:the )?(?:total |consolidated )?"
                      r"(revenue|turnover|sales|income|assets|net worth|ebitda|profit)", re.I)


def _to_date(m) -> str | None:
    try:
        d, mon, y = m.group(1), m.group(2)[:3].title(), m.group(3)
        if mon == "Sep" and m.group(2).lower().startswith("sept"):
            mon = "Sep"
        return dt.date(int(y), _MONTHS[mon], int(d)).isoformat()
    except (KeyError, ValueError):
        return None


def facts_in(text: str, rights: bool = True) -> dict:
    """What a scheme filing states: entitlement ratio, resulting company,
    demerged undertaking, record / appointed dates, pro-forma mention,
    ESOP pricing mention, insider continuity, size hints."""
    t = text or ""
    out: dict = {}
    m = RATIO_RX.search(t)
    if m:
        out["entitlement_ratio"] = f"{m.group(1)} for every {m.group(2)}"
        out["entitlement_quote"] = _snippet(t, m.start(), m.end(), 60)
    m = RESULTING_BEFORE_RX.search(t) or RESULTING_RX.search(t)
    if m:
        name = re.sub(r"\s+", " ", m.group(1)).strip()
        name = re.split(r"\b(?:and|between|with|amongst|among|into)\b", name, flags=re.I)[-1].strip()
        name = re.sub(r"^(of|by|the)\s+", "", name, flags=re.I)
        if len(name) > 6:
            out["resulting_company"] = name
    m = UNDERTAKING_RX.search(t)
    if m:
        u = re.sub(r"\s+", " ", m.group(1)).strip()
        if not re.match(r"(as defined|as on|from the|to the|into the|of the demerged|in the|shall have)", u, re.I) \
                and len(u) > 12:
            out["demerged_undertaking"] = u[:200]
    for key, rx in (("record_date", re.compile(r"record date", re.I)),
                    ("appointed_date", re.compile(r"appointed date", re.I))):
        for hit in rx.finditer(t):
            dm = DATE_WORDS.search(t, hit.end(), hit.end() + 160)
            if dm and _to_date(dm):
                out[key] = _to_date(dm)
                break
    if PROFORMA_RX.search(t):
        out["pro_forma"] = True
    m = ESOP_RX.search(t)
    if m:
        out["esop_pricing"] = _snippet(t, m.start(), m.end(), 80)
    m = INSIDER_RX.search(t)
    if m:
        out["insider_continuity"] = _snippet(t, m.start(), m.end(), 80)
    sizes = [(float(a.replace(",", "")), what.lower(), a)
             for a, what in SMALL_RX.findall(t)[:12]]
    small = [(v, w) for v, w, _ in sizes if v < 25]
    if small:
        out["small_share"] = f"{small[0][0]:g}% of {small[0][1]}"
    if rights and OVERSUB_RX.search(t):
        out["oversubscription_clause"] = True
    m = INSIDER_OVERSUB_RX.search(t) if rights else None
    if m:
        out["insider_oversubscribe"] = _snippet(t, m.start(), m.end(), 80)
    return out


# -------------------------------------------------------- the situations

def load_filings(path: Path = FA.MATCHES) -> list[dict]:
    return FA.read_csv(path)


def load_text(row: dict) -> str:
    tf = row.get("text_file") or ""
    if not tf.startswith("text/"):
        return ""
    p = ANN_DIR / tf
    return p.read_text(errors="replace") if p.exists() else ""


def refine_kind(row: dict, text: str) -> str:
    """A 'Scheme of Arrangement' headline says nothing; its attachment
    does. Re-classify from the text: a scheme whose text demerges is a
    demerger; one that only amalgamates is a merger."""
    kind = row["kind"]
    if not text:
        return kind
    head = text[:60_000].lower()
    demerg = len(re.findall(r"\bde-?merg", head))
    amalg = len(re.findall(r"amalgamat|\bmerger\b", head))
    listing = bool(FA.PATTERNS["subsidiary_listing"].search(head))
    if kind in ("scheme_other", "merger", "demerger"):
        if demerg >= 3 and demerg >= amalg * 0.5:
            return "demerger"
        if kind == "scheme_other" and amalg >= 3:
            return "merger"
    if kind == "scheme_other" and listing:
        return "subsidiary_listing"
    return kind


def family_of(kind: str) -> str:
    return {"demerger": "spin-off", "subsidiary_listing": "partial spin-off / listing",
            "scheme_other": "scheme (nature unclear)", "merger": "merger",
            "slump_sale": "slump sale", "rights_issue": "rights offering",
            "capital_reduction": "capital reduction"}.get(kind, kind)


def build_situations(rows: list[dict], texts: dict[str, str] | None = None,
                     today: dt.date | None = None) -> list[dict]:
    """Group a company's filings into situations (one per kind family),
    walk their stages, and gather every fact and reason the texts state.
    `texts` maps ann_id -> attachment text (tests inject; the CLI reads
    from disk)."""
    today = today or dt.date.today()
    by: dict[tuple[str, str], list[dict]] = {}
    for r in rows:
        text = (texts or {}).get(r["ann_id"]) if texts is not None else load_text(r)
        kind = refine_kind(r, text or "")
        fam = ("spin" if kind in ("demerger", "subsidiary_listing", "scheme_other")
               else kind)
        by.setdefault((r["symbol"], fam), []).append({**r, "kind": kind, "_text": text or ""})
    out = []
    for (sym, fam), fl in by.items():
        fl.sort(key=lambda r: r["date"])
        kinds = [r["kind"] for r in fl]
        kind = ("demerger" if "demerger" in kinds else
                "subsidiary_listing" if "subsidiary_listing" in kinds else kinds[0])
        stage_dates: dict[str, str] = {}
        facts: dict = {}
        reasons: list[dict] = []
        seen_reasons = set()
        rights_rows = []
        news_only = 0
        for r in fl:
            blob = f"{r['category']} {r['headline']} {r['_text'][:120_000]}"
            st = stage_of(f"{r['category']} {r['headline']}")
            if st is None and r["_text"] and STAGES[0][1].search(r["_text"][:3_000]):
                st = "announced"            # a board-approval letter with a bare headline
            if st and (st not in stage_dates or r["date"] < stage_dates[st]):
                stage_dates[st] = r["date"]
            for k, v in facts_in(blob, rights=(r["kind"] == "rights_issue")).items():
                facts.setdefault(k, v)
            if NEWS_RX.search(f"{r['category']} {r['headline']}"):
                news_only += 1
            for rr in reasons_in(r["_text"] or r["headline"]):
                if rr["reason"] not in seen_reasons:
                    seen_reasons.add(rr["reason"])
                    reasons.append(rr)
            if r["kind"] == "rights_issue":
                rights_rows.append(r)
        stage = (max(stage_dates, key=STAGE_ORDER.index) if stage_dates else "announced")
        first, last = fl[0]["date"], fl[-1]["date"]
        days = (today - dt.date.fromisoformat(first)).days
        if news_only == len(fl):
            facts["news_only"] = True        # rumour / clarification / denial only
            stage = "rumoured"
        listed_on = (facts.get("record_date") if stage in ("record_date", "listed")
                     and facts.get("record_date") and facts["record_date"] <= today.isoformat()
                     else None) or stage_dates.get("listed") or stage_dates.get("record_date")
        age_listed = ((today - dt.date.fromisoformat(listed_on)).days
                      if listed_on else None)
        out.append({
            "symbol": sym, "company": fl[0]["company"], "kind": kind,
            "family": family_of(kind), "n_filings": len(fl),
            "first_filing": first, "latest_filing": last, "days_since_first": days,
            "stage": stage, "stage_dates": dict(sorted(stage_dates.items(),
                                                        key=lambda x: STAGE_ORDER.index(x[0]))),
            "listed_on": listed_on, "days_since_listing": age_listed,
            "facts": facts, "reasons": reasons,
            "sources": sorted({r["source"] for r in fl}),
            "headlines": [{"date": r["date"], "category": r["category"],
                           "headline": r["headline"][:220], "kind": r["kind"],
                           "attachment": r["attachment"]} for r in fl],
            "has_text": any(r["_text"] for r in fl),
        })
    out.sort(key=lambda s: (s["kind"] not in SPIN_KINDS, -s["n_filings"], s["symbol"]))
    return out


# ------------------------------------------------------ conference calls

MENTION_RX = re.compile(
    r"\bde-?merg\w*|spin[\s-]?offs?|hiv(e|ing)[\s-]?off|carve[\s-]?out|"
    r"(separate|independent) listing|list(ing)? (of )?(the |our |its )?(subsidiar|arm|business)|"
    r"value[\s-]?unlock\w*|slump sale|scheme of arrangement|"
    r"(ipo|initial public offer\w*) (of|for) (the |our |its )?(subsidiar|arm|business)",
    re.I)


def concall_sections(text: str) -> list[tuple[str, str]]:
    """[(label 'Call: MMM YYYY', section text)] from a consolidated
    transcript PDF's text, in file order."""
    parts = re.split(r"(Call: \w{3} \d{4})", text)
    out = []
    for i in range(1, len(parts) - 1, 2):
        out.append((parts[i], parts[i + 1]))
    return out


def _label_date(label: str) -> dt.date | None:
    m = re.search(r"(\w{3}) (\d{4})", label)
    if not m or m.group(1) not in _MONTHS:
        return None
    return dt.date(int(m.group(2)), _MONTHS[m.group(1)], 1)


FORWARD_RX = re.compile(
    r"\b(plan|planning|propos\w*|evaluat\w*|consider\w*|explor\w*|intend\w*|option|"
    r"will|would|going to|potential|possible|likely|expect\w*|target\w*|update on|"
    r"timeline|in due course|board (has )?approved|filed|announce\w*|next (step|year|quarter)|"
    r"around the corner|unlock\w* value|value unlock\w*)\b", re.I)
BACKWARD_RX = re.compile(
    r"\b(post|after|since|completed|complete|concluded|was|were|had|last year|earlier|"
    r"predecessor|erstwhile|no plan|not planning|no intention|deni\w*|rule[sd]? out)\b", re.I)


def tone(quote: str) -> str:
    """forward (a spin being planned or in motion), backward (one that
    already happened, or a denial), or neutral."""
    f = len(FORWARD_RX.findall(quote or ""))
    b = len(BACKWARD_RX.findall(quote or ""))
    if re.search(r"no plan|not planning|no intention|deni\w*|rule[sd]? out", quote or "", re.I):
        return "backward"
    if f > b:
        return "forward"
    if b > f:
        return "backward"
    return "neutral"


def concall_mentions(text: str, today: dt.date | None = None,
                     months: int = CONCALL_MONTHS, max_per_call: int = 6) -> list[dict]:
    """Spin-off / demerger language in the calls of the last `months`
    months, each with its verbatim snippet."""
    today = today or dt.date.today()
    cutoff = dt.date(today.year, today.month, 1) - dt.timedelta(days=months * 31)
    out = []
    for label, body in concall_sections(text):
        d = _label_date(label)
        if d is None or d < cutoff:
            continue
        n = 0
        for m in MENTION_RX.finditer(body):
            q = _snippet(body, m.start(), m.end(), 160)
            out.append({"call": label.replace("Call: ", ""), "term": m.group(0),
                        "quote": q, "tone": tone(q)})
            n += 1
            if n >= max_per_call:
                break
    return out


def concall_text(symbol: str) -> str:
    """The consolidated transcript PDF's text, or ''."""
    p = CONCALLS / f"{symbol}.pdf"
    if not p.exists():
        return ""
    try:
        import PyPDF2                                    # noqa: PLC0415
        reader = PyPDF2.PdfReader(str(p), strict=False)
        return "\n".join((pg.extract_text() or "") for pg in reader.pages)
    except Exception:                                    # noqa: BLE001
        return ""


# ---------------------------------------------------------- the numbers

def _latest(csv_path: Path, line_item: str) -> tuple[str, float] | None:
    if not csv_path.exists():
        return None
    with open(csv_path) as fh:
        rows = list(csv.reader(fh))
    if not rows:
        return None
    header = rows[0]
    for r in rows[1:]:
        if r and r[0] == line_item:
            for col, val in reversed(list(zip(header[2:], r[2:]))):
                try:
                    return col, float(val)
                except ValueError:
                    continue
    return None


def live_market() -> dict[str, dict]:
    out = {}
    if LIVE.exists():
        for r in FA.read_csv(LIVE):
            out[r["nse_symbol"]] = r
    return out


def industry_map() -> dict[str, str]:
    return {r["nse_symbol"]: r.get("industry", "") for r in FA.read_csv(CONSTITUENTS)}


def financial_picture(symbol: str, live: dict[str, dict] | None = None,
                      industries: dict[str, str] | None = None) -> dict:
    """Leverage, earnings and the comparable P/E from what is on file.
    Every number carries its source and year; missing data is said."""
    live = live if live is not None else live_market()
    industries = industries if industries is not None else industry_map()
    out: dict = {"symbol": symbol, "industry": industries.get(symbol, "")}
    b = _latest(BALANCE / f"{symbol}.csv", "Borrowings")
    if b:
        out["borrowings_cr"], out["borrowings_year"] = b[1], b[0]
    for item, key in (("Net Profit", "net_profit_cr"), ("Sales", "sales_cr"),
                      ("EPS in Rs", "eps")):
        v = _latest(PNL / f"{symbol}.csv", item)
        if v:
            out[key], out[key + "_year"] = v[1], v[0]
    lm = live.get(symbol)
    if lm:
        try:
            out["market_cap_cr"] = float(lm["market_cap_rs_cr"])
            out["price"] = float(lm["current_price_rs"])
            out["stock_pe"] = float(lm["stock_pe"]) if lm.get("stock_pe") else None
            out["market_data_at"] = lm.get("fetched_at", "")
        except (ValueError, KeyError):
            pass
    if out.get("borrowings_cr") is not None and out.get("market_cap_cr"):
        out["debt_to_market_cap"] = round(out["borrowings_cr"] / out["market_cap_cr"], 2)
    if out.get("net_profit_cr") and out.get("market_cap_cr"):
        out["pe_on_latest_profit"] = round(out["market_cap_cr"] / out["net_profit_cr"], 1) \
            if out["net_profit_cr"] > 0 else None
    peers = [float(r["stock_pe"]) for s, r in live.items()
             if s != symbol and industries.get(s) == out["industry"]
             and r.get("stock_pe") not in (None, "", "nan")
             and 0 < float(r["stock_pe"]) < 200]
    if len(peers) >= 3:
        out["industry_median_pe"] = round(statistics.median(peers), 1)
        out["industry_peers"] = len(peers)
    return out


def stub_value(parent_price: float, parent_shares: float,
               holdings: list[tuple[float, float]]) -> dict:
    """The partial-spin-off arithmetic from the notes: what the market
    pays for the parent AFTER subtracting its listed stakes.
    holdings: [(listed price, shares the parent owns)].
    Sears: parent $54, 340m shares; Dean Witter $37 × 136m, Allstate
    $29 × 340m → stakes $15 + $29 = $44 → stub $10 per Sears share."""
    stakes = [(p * n) / parent_shares for p, n in holdings]
    stub = parent_price - sum(stakes)
    return {"stake_values_per_parent_share": [round(s, 2) for s in stakes],
            "stub_per_share": round(stub, 2),
            "stub_share_of_price": round(stub / parent_price, 3) if parent_price else None}


def leverage_doubling(price: float, debt_per_share: float) -> dict:
    """Host Marriott's point: with debt D and equity E per share, a rise
    of x% in asset value moves equity by x% × (D+E)/E. Returns the asset
    move that doubles the stock."""
    if price <= 0:
        return {}
    ev = price + max(debt_per_share, 0.0)
    return {"enterprise_per_share": round(ev, 2),
            "equity_share_of_ev": round(price / ev, 3),
            "asset_rise_to_double_equity_pct": round(100 * price / ev, 1)}


# ---------------------------------------------------------- the checklist

def checklist(sit: dict, fin: dict, mentions: list[dict],
              today: dt.date | None = None) -> list[dict]:
    """The notes' questions, each answered from the evidence on file:
    {item, status: yes|no|partly|unknown, evidence, next}."""
    today = today or dt.date.today()
    f = sit["facts"]
    items = []

    # 1. the reason
    if sit["reasons"]:
        items.append({"item": "Why the spin-off", "status": "yes",
                      "evidence": "; ".join(r["reason"] for r in sit["reasons"]),
                      "quote": sit["reasons"][0]["quote"]})
    else:
        items.append({"item": "Why the spin-off", "status": "unknown",
                      "evidence": "no stated rationale in the filings on file",
                      "next": "read the scheme's rationale section / the board's press release"})

    # 2. institutional selling pressure: size + different business
    small = f.get("small_share")
    diff = "unrelated businesses separated" in {r["reason"] for r in sit["reasons"]}
    if small or diff:
        items.append({"item": "Institutional selling likely (small / different business)",
                      "status": "yes" if small and diff else "partly",
                      "evidence": "; ".join(x for x in (
                          f"the demerged piece is {small}" if small else "",
                          "the businesses are described as distinct" if diff else "") if x)})
    else:
        items.append({"item": "Institutional selling likely (small / different business)",
                      "status": "unknown", "evidence": "size of the demerged piece not stated",
                      "next": "pro-forma statements: revenue / assets of the demerged undertaking vs the parent"})

    # 3. insiders' incentives
    ev = []
    if f.get("insider_continuity"):
        ev.append(f.get("insider_continuity"))
    if f.get("esop_pricing"):
        ev.append("option pricing mentioned: " + f["esop_pricing"])
    items.append({"item": "Insider ownership and incentives aligned",
                  "status": "partly" if ev else "unknown",
                  "evidence": " | ".join(ev) if ev else
                  "no promoter-continuity or option-pricing language found",
                  "next": "the date the management options are priced; promoter holding in the resulting company"})

    # 4. hidden value: pro-forma, leverage, comparables
    lev = fin.get("debt_to_market_cap")
    pf = f.get("pro_forma")
    ev = []
    if pf:
        ev.append("pro-forma statements are referenced in the filings")
    if lev is not None:
        ev.append(f"borrowings {fin['borrowings_cr']:,.0f} cr ({fin['borrowings_year']}) "
                  f"= {lev:.2f}× market cap")
    if fin.get("pe_on_latest_profit") and fin.get("industry_median_pe"):
        ev.append(f"P/E {fin['pe_on_latest_profit']} on {fin['net_profit_cr_year']} profit vs "
                  f"industry median {fin['industry_median_pe']} ({fin['industry_peers']} peers)")
    cheap = (fin.get("pe_on_latest_profit") and fin.get("industry_median_pe")
             and fin["pe_on_latest_profit"] < 0.8 * fin["industry_median_pe"])
    items.append({"item": "A hidden value revealed (pro-forma, leverage, comparables)",
                  "status": "yes" if cheap else "partly" if ev else "unknown",
                  "evidence": "; ".join(ev) if ev else "no pro-forma or market data on file",
                  "next": "pro-forma P&L of each piece × the peer P/E of its own industry"})

    # 5. the parent as the trade
    items.append({"item": "Parent before the spin (clean parent, takeover prelude)",
                  "status": "partly" if sit["stage"] in PRE_STAGES
                  else "no" if sit["stage"] in ("effective", "record_date", "listed") else "unknown",
                  "evidence": f"stage {sit['stage']}" + (
                      " — the spin has not happened; the parent can still be bought whole"
                      if sit["stage"] in PRE_STAGES
                      else " — the pieces trade separately now")})

    # 6. partial spin-off / rights
    if sit["kind"] == "subsidiary_listing":
        items.append({"item": "Partial spin-off: price the stub from the listed piece",
                      "status": "partly", "evidence": "a subsidiary is being listed; once it trades, "
                      "stub = parent price − (stake value ÷ parent shares)",
                      "next": "stub_value(parent price, parent shares, [(sub price, shares held)])"})
    if f.get("oversubscription_clause") or f.get("insider_oversubscribe"):
        items.append({"item": "Rights offering: oversubscription clause / insiders oversubscribing",
                      "status": "yes" if f.get("insider_oversubscribe") else "partly",
                      "evidence": f.get("insider_oversubscribe") or "additional-shares clause present"})

    # 7. timing
    if sit.get("days_since_listing") is not None:
        d = sit["days_since_listing"]
        status, text = ("partly", "first year since listing — the selling-pressure window; "
                        "watch, size the entry") if d < 365 else \
                       ("yes", "second year since listing — where the notes found the largest gains") \
                       if d < 730 else ("no", "more than two years listed — no longer a spin-off situation")
        items.append({"item": "Timing (first year sells, second year gains)", "status": status,
                      "evidence": f"{d} days since listing/record date; {text}"})
    else:
        items.append({"item": "Timing (first year sells, second year gains)", "status": "partly",
                      "evidence": f"not yet listed — {sit['days_since_first']} days since the first filing, "
                                  f"stage {sit['stage']}"})

    # 8. management talking about it on the calls
    if mentions:
        items.append({"item": "Management discussing it on the calls", "status": "yes",
                      "evidence": f"{len(mentions)} mention(s) in the last {CONCALL_MONTHS} months of calls",
                      "quote": mentions[-1]["quote"]})
    return items


def verdict(sit: dict, items: list[dict]) -> dict:
    """One line and a 0–10 score: how much of the notes' pattern is
    present, and where in the cycle the situation sits."""
    score = sum({"yes": 1.0, "partly": 0.5}.get(i["status"], 0.0) for i in items)
    score = round(10 * score / max(len(items), 1), 1)
    k, st = sit["kind"], sit["stage"]
    if k not in SPIN_KINDS:
        label = {"merger": "MERGER — not a spin-off; noted for the record",
                 "slump_sale": "SLUMP SALE — cash deal, no new listing",
                 "rights_issue": "RIGHTS OFFERING — check the oversubscription clause",
                 "capital_reduction": "CAPITAL ACTION — not a spin-off"}.get(k, k.upper())
    elif st == "rumoured":
        label = "RUMOURED — news verification / denial only; no scheme filed"
    elif st in ("announced", "exchange_noc", "meetings", "nclt_sanction"):
        label = "PRE-SPIN — study the parent; the pieces do not trade yet"
    elif st in ("effective", "record_date") and (sit.get("days_since_listing") or 0) < LISTING_LAG_DAYS:
        label = "SPINNING — record date set; the new entity lists soon"
    else:
        d = sit.get("days_since_listing") or 0
        label = ("LISTED <1Y — selling-pressure window; the bargain forms here" if d < 365
                 else "LISTED 1–2Y — the second-year window" if d < 730
                 else "MATURE — past the spin-off window")
    return {"label": label, "score": score}


# ------------------------------------------------------------ the record

def analyse(rows: list[dict], texts: dict[str, str] | None = None,
            today: dt.date | None = None, with_calls: bool = True,
            live: dict | None = None, industries: dict | None = None) -> list[dict]:
    """Every situation, fully judged. `texts` and `live`/`industries` are
    injectable for tests; the CLI reads everything from disk."""
    today = today or dt.date.today()
    live = live if live is not None else live_market()
    industries = industries if industries is not None else industry_map()
    out = []
    call_cache: dict[str, list[dict]] = {}
    for sit in build_situations(rows, texts, today):
        sym = sit["symbol"]
        if with_calls and sym not in call_cache:
            call_cache[sym] = concall_mentions(concall_text(sym), today) \
                if sit["kind"] in SPIN_KINDS else []
        mentions = call_cache.get(sym, [])
        fin = financial_picture(sym, live, industries)
        items = checklist(sit, fin, mentions, today)
        out.append({**sit, "financials": fin, "concall_mentions": mentions,
                    "checklist": items, "verdict": verdict(sit, items)})
    return out
