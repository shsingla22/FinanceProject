"""
deal.py — the mechanical parts of a company's nine-part write-up.

  call_exchanges      verbatim, uncut management-call statements about the
                      separation: every prepared-remarks turn and every
                      QUESTION-AND-ANSWER exchange that mentions it, call by
                      call, oldest first. Nothing is summarised or trimmed.
  shareholding        promoters / FIIs / DIIs / public, quarter by quarter,
                      from the screener company page (stored under
                      ShareholdingPattern/NiftyTotalMarket/).
  latest_mcaps        market capitalisation of every NSE symbol from the
                      newest bhavcopy bundle on disk.
  enrich_entities     every resulting company / listed subsidiary the deal
                      sheet names, with its NSE symbol and listing date.
  size_view           the separated piece against the parent — stated
                      turnover share, segment revenue share, market-cap share —
                      and what that says about forced selling.
  compare             parent against each separated business: margins,
                      growth, working-capital days, return on capital, debt.
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import spinoff as SO                       # noqa: E402
import financials as FN                    # noqa: E402

INDIA = HERE.parent.parent.parent
SHP_DIR = INDIA / "ShareholdingPattern" / "NiftyTotalMarket"
WC_DIR = INDIA / "WorkingCapital" / "NiftyTotalMarket"
BS_DIR = INDIA / "BalanceSheet" / "NiftyTotalMarket"
BUNDLES = INDIA / "Announcements" / "_bhav_bundles"

# ------------------------------------------------------- call exchanges

SPEAKER_RX = re.compile(r"^[ \t]*((?:Mr\.?|Ms\.?|Mrs\.?|Dr\.?|Shri|Smt\.?)?[ \t]*[A-Z][\w.'’\-]*(?:[ \t]+[A-Z(][\w.'’\-()]*){0,5})[ \t]*:[ \t]+(?=\S)",
                        re.M)
PAGE_FURNITURE_RX = re.compile(r"^\s*Page\s+\d+\s+of\s+\d+\s*$", re.I | re.M)
MODERATOR_RX = re.compile(r"^(moderator|operator|coordinator)\b", re.I)
NOT_SPEAKERS = {"sub", "subject", "ref", "reference", "note", "source", "date", "to", "from", "cin", "tel", "fax", "email",
                "e-mail", "website", "web", "regd", "registered office", "scrip code", "security code", "nse symbol",
                "bse", "nse", "symbol", "isin", "encl", "enclosure", "dear sir", "management", "participants",
                "disclaimer", "contact", "phone", "mob", "mobile", "address", "time", "venue", "agenda"}
SPIN_TERMS_RX = re.compile(
    r"de-?merg\w*|spin[\s-]?offs?|hiv(?:e|ing)[\s-]?off|carve[\s-]?outs?|resulting compan\w*|"
    r"scheme of (?:arrangement|demerger)|composite scheme|separate(?:ly)? list\w*|vertical split|"
    r"(?:ipo|initial public offer\w*|drhp|draft red herring|listing)\b[^.?!]{0,80}\b(?:subsidiar\w*|arm)|"
    r"(?:subsidiar\w*|arm)\b[^.?!]{0,80}\b(?:ipo|initial public offer\w*|drhp|listing)\b|value[\s-]?unlock\w*", re.I)


def split_turns(section: str) -> list[tuple[str, str]]:
    """[(speaker, text)] for one call's transcript text. A speaker label is
    a capitalised name at the start of a line followed by a colon; a label
    counts only when it recurs in the call (or is the moderator), so letter
    furniture ('Sub:', 'NSE Symbol:') does not start a turn. The text of a
    turn is everything up to the next label, lines rejoined with spaces —
    nothing is dropped except 'Page N of M' lines."""
    text = PAGE_FURNITURE_RX.sub("", section or "")
    cands = [(m.start(), m.end(), re.sub(r"\s+", " ", m.group(1)).strip()) for m in SPEAKER_RX.finditer(text)]
    counts: dict[str, int] = {}
    for _, _, name in cands:
        counts[name] = counts.get(name, 0) + 1
    def ok(name: str) -> bool:
        low = name.lower().strip(". ")
        if low in NOT_SPEAKERS or len(name) < 3:
            return False
        if MODERATOR_RX.match(low) or counts[name] >= 2:
            return True
        # a speaker heard once in the call: a person's name (two to four
        # capitalised words) still starts a turn
        words = name.replace(".", " ").split()
        return 2 <= len(words) <= 4 and all(w[0].isupper() and w.replace("'", "").replace("-", "").isalpha() for w in words)
    marks = [(a, b, n) for a, b, n in cands if ok(n)]
    turns = []
    for i, (a, b, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        body = re.sub(r"[ \t]*\n[ \t]*", " ", text[b:end]).strip()
        body = re.sub(r"[ \t]{2,}", " ", body)
        if body:
            turns.append((name, body))
    return turns


QA_OPEN_RX = re.compile(r"(?:first|next|following|last|final)\s+question|question\s+(?:is|comes|will be)\s+from|"
                        r"from the line of|take (?:the|our) (?:first|next) question|begin the question", re.I)
REMARKS_CONTEXT = 3            # complete sentences kept either side of a mention in prepared remarks


def passage(text: str, terms_rx: re.Pattern, context: int = REMARKS_CONTEXT) -> str:
    """The part of a prepared-remarks turn that concerns the separation:
    every sentence that mentions it with `context` complete sentences on
    either side, in order, runs joined by ' […] '. A short turn is returned
    whole. Sentences are never cut."""
    if len(text) <= 1800:
        return text
    sents = re.split(r"(?<=[.?!])\s+(?=[A-Z“\"'(])", text)
    hit = [i for i, s in enumerate(sents) if terms_rx.search(s)]
    if not hit:
        return text
    keep = sorted({j for i in hit for j in range(max(0, i - context), min(len(sents), i + context + 1))})
    runs, cur = [], [keep[0]]
    for j in keep[1:]:
        if j == cur[-1] + 1:
            cur.append(j)
        else:
            runs.append(cur)
            cur = [j]
    runs.append(cur)
    return " […] ".join(" ".join(sents[j] for j in run) for run in runs)


def exchanges_in(section: str, terms_rx: re.Pattern = SPIN_TERMS_RX) -> list[dict]:
    """The exchanges of one call that mention the separation, in order:
      {'kind': 'remarks', 'turns': [(speaker, text)]}   the passage of a
            prepared-remarks turn that concerns it (complete sentences,
            see `passage`); 'full_chars' is the length of the whole turn;
      {'kind': 'qa', 'turns': [...]}   a question and every answer to it,
            in full, up to the questioner's next question.
    The questioner is the first speaker after the moderator opens a
    question; short acknowledgements ('Okay.', 'Thank you.') stay inside
    the exchange they belong to."""
    turns = split_turns(section)
    out: list[dict] = []
    i, n = 0, len(turns)
    in_qa = False
    while i < n:
        name, body = turns[i]
        if MODERATOR_RX.match(name):
            in_qa = in_qa or bool(QA_OPEN_RX.search(body))
            # the block: everything until the next moderator turn
            j = i + 1
            while j < n and not MODERATOR_RX.match(turns[j][0]):
                j += 1
            block = turns[i + 1:j]
            if in_qa and block:
                asker = block[0][0]
                # split the block at each substantive turn by the asker
                starts = [k for k, (nm, tx) in enumerate(block) if nm == asker and (len(tx) > 60 or "?" in tx)]
                starts = starts or [0]
                if starts[0] != 0:
                    starts = [0] + starts
                for si, st in enumerate(starts):
                    en = starts[si + 1] if si + 1 < len(starts) else len(block)
                    sub = block[st:en]
                    if any(terms_rx.search(tx) for _, tx in sub):
                        out.append({"kind": "qa", "turns": sub})
            elif block:
                for nm, tx in block:
                    if terms_rx.search(tx):
                        out.append({"kind": "remarks", "turns": [(nm, passage(tx, terms_rx))], "full_chars": len(tx)})
            i = j
            continue
        if terms_rx.search(body):                 # before any moderator turn: prepared remarks
            out.append({"kind": "remarks", "turns": [(name, passage(body, terms_rx))], "full_chars": len(body)})
        i += 1
    if not turns:                                 # no speaker labels at all: fall back to paragraphs
        for para in re.split(r"\n\s*\n", PAGE_FURNITURE_RX.sub("", section or "")):
            if terms_rx.search(para):
                out.append({"kind": "remarks", "turns": [("(speaker not labelled)", re.sub(r"\s+", " ", para).strip())]})
    return out


def entity_terms(names: list[str], company: str = "") -> re.Pattern:
    """SPIN_TERMS plus the distinctive words of the entities' names (so
    'when does Fleur list?' is caught without the word demerger)."""
    skip = {w.lower() for w in re.findall(r"[A-Za-z]+", company)} | set(FN.GENERIC_WORDS)
    skip |= {"india", "indian", "limited", "private", "services", "solutions", "enterprises", "industries", "holdings",
             "global", "international", "technologies", "products", "ventures", "national", "management", "company"}
    words = []
    for n in names:
        for w in re.findall(r"[A-Za-z][A-Za-z0-9]{4,}", n or ""):
            if w.lower() not in skip and w.lower() not in words:
                words.append(w.lower())
                break                              # the first distinctive word of each name
    if not words:
        return SPIN_TERMS_RX
    return re.compile(SPIN_TERMS_RX.pattern + "|" + "|".join(r"\b" + re.escape(w) + r"\b" for w in words), re.I)


def call_exchanges(symbol: str, today: dt.date, months: int = 36, names: list[str] | None = None,
                   company: str = "", links: dict | None = None) -> list[dict]:
    """Every call of the last `months` months (never after `today`), oldest
    first, with its exchanges about the separation:
    [{'call': 'May 2024', 'date': '2024-05-01', 'url': …, 'exchanges': […]}]."""
    text = SO.concall_text(symbol)
    if not text:
        return []
    rx = entity_terms(names or [], company)
    cutoff = dt.date(today.year, today.month, 1) - dt.timedelta(days=months * 31)
    out = []
    for label, body in SO.concall_sections(text):
        d = SO._label_date(label)
        if d is None or d < cutoff or d > today:
            continue
        ex = exchanges_in(body, rx)
        if ex:
            lab = label.replace("Call: ", "")
            out.append({"call": lab, "date": d.isoformat(), "url": (links or {}).get(lab, ""), "exchanges": ex})
    out.sort(key=lambda c: c["date"])
    return out


# ---------------------------------------------------------- shareholding

def parse_shareholding(html: str) -> dict:
    """{'quarters': [...], 'rows': {'Promoters': [...], 'FIIs': [...], …}}
    from a screener company page, percentages as floats."""
    m = re.search(r'id="quarterly-shp".*?</table>', html or "", re.S)
    if not m:
        return {}
    seg = m.group(0)
    quarters = re.findall(r"<th[^>]*>\s*([A-Za-z]{3} \d{4})\s*</th>", seg)
    rows: dict[str, list] = {}
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", seg, re.S):
        cells = [re.sub(r"<[^>]+>", "", c).replace("&nbsp;", " ").strip()
                 for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
        if len(cells) < 2:
            continue
        name = cells[0].rstrip("+ ").strip()
        if name in ("Promoters", "FIIs", "DIIs", "Government", "Public", "Others"):
            vals = []
            for c in cells[1:]:
                try:
                    vals.append(float(c.rstrip("%").replace(",", "")))
                except ValueError:
                    vals.append(None)
            rows[name] = vals[-len(quarters):] if quarters else vals
    return {"quarters": quarters, "rows": rows} if rows else {}


def shareholding(symbol: str, fetch: bool = False) -> dict:
    """The stored shareholding pattern of a symbol; fetched from screener
    and stored when `fetch` and not on disk. {} when unavailable."""
    path = SHP_DIR / f"{symbol}.csv"
    if not path.exists() and fetch:
        try:
            sys.path.insert(0, str(INDIA / "InvestorPresentations"))
            import fetch_presentations as FP                      # noqa: PLC0415
            for variant in ("consolidated/", ""):
                code, body = FP._get(f"{FP.SCREENER}/company/{symbol}/{variant}", timeout=40, referer=f"{FP.SCREENER}/")
                if code == 200 and body:
                    shp = parse_shareholding(body.decode("utf-8", "replace"))
                    if shp:
                        SHP_DIR.mkdir(parents=True, exist_ok=True)
                        with open(path, "w", newline="") as fh:
                            w = csv.writer(fh)
                            w.writerow(["holder"] + shp["quarters"])
                            for k, v in shp["rows"].items():
                                w.writerow([k] + ["" if x is None else x for x in v])
                        break
        except Exception:                                         # noqa: BLE001
            return {}
    if not path.exists():
        return {}
    with open(path) as fh:
        rd = list(csv.reader(fh))
    if len(rd) < 2:
        return {}
    quarters = rd[0][1:]
    rows = {r[0]: [float(x) if x not in ("", None) else None for x in r[1:]] for r in rd[1:] if r}
    return {"quarters": quarters, "rows": rows, "source": f"ShareholdingPattern/NiftyTotalMarket/{symbol}.csv (screener.in)"}


def latest_holding(shp: dict, holder: str = "Promoters") -> tuple[float | None, str]:
    vals = (shp.get("rows") or {}).get(holder) or []
    qs = shp.get("quarters") or []
    for v, q in zip(reversed(vals), reversed(qs)):
        if v is not None:
            return v, q
    return None, ""


def fetch_entity_statements(symbol: str) -> list[str]:
    """Pull the profit statement, balance sheet and working-capital ratios
    of a LISTED resulting company that is not on file (it is not an index
    member, so the routine fetchers never asked for it), with the same
    fetchers and into the same folders. Returns what was written."""
    wrote = []
    jobs = (("ProfitStatement", "fetch_profit_loss", "fetch_company_detailed", FN.PNL),
            ("BalanceSheet", "fetch_balance_sheets", "fetch_company_detailed", BS_DIR),
            ("WorkingCapital", "fetch_working_capital", "fetch_company", WC_DIR))
    for folder, module, func, out_dir in jobs:
        path = out_dir / f"{symbol}.csv"
        if path.exists():
            continue
        try:
            sys.path.insert(0, str(INDIA / folder))
            mod = __import__(module)
            df = getattr(mod, func)(symbol)[0]
            if df is not None and len(df):
                df.to_csv(path)
                wrote.append(folder)
        except Exception:                                         # noqa: BLE001
            continue
    return wrote


# ------------------------------------------------------------ market caps

_MCAP: tuple[str, dict[str, float]] | None = None


def latest_mcaps(bundles: Path = BUNDLES, as_of: dt.date | None = None) -> tuple[str, dict[str, float]]:
    """(date, {symbol: market cap in ₹ crore}) from the newest PR bundle on
    disk dated on or before `as_of`; ('', {}) when none."""
    global _MCAP
    if _MCAP is not None and as_of is None:
        return _MCAP
    best = None
    for p in bundles.glob("PR*.zip"):
        m = re.fullmatch(r"PR(\d\d)(\d\d)(\d\d)", p.stem)
        if not m:
            continue
        d = dt.date(2000 + int(m.group(3)), int(m.group(2)), int(m.group(1)))
        if (as_of is None or d <= as_of) and (best is None or d > best[0]):
            best = (d, p)
    if not best:
        return "", {}
    caps: dict[str, float] = {}
    try:
        with zipfile.ZipFile(best[1]) as z:
            name = next((n for n in z.namelist() if n.lower().startswith("mcap")), None)
            if name:
                for r in csv.DictReader(io.StringIO(z.read(name).decode("utf-8", "replace"))):
                    r = {(k or "").strip().lower(): (v or "").strip() for k, v in r.items()}
                    sym = r.get("symbol", "")
                    cap = next((v for k, v in r.items() if k.startswith("market cap")), "")
                    try:
                        if sym and r.get("series", "EQ") in ("EQ", "BE", "BZ"):
                            caps[sym] = float(cap) / 1e7
                    except ValueError:
                        continue
    except (zipfile.BadZipFile, OSError):
        return "", {}
    res = (best[0].isoformat(), caps)
    if as_of is None:
        _MCAP = res
    return res


# --------------------------------------------------------------- entities

def enrich_entities(entities: list[dict], parent_symbol: str, today: dt.date) -> list[dict]:
    """Each entity the deal sheet names, cleaned, with its NSE symbol and
    listing date when the exchange's equity list has it (never a date
    after `today`)."""
    dates, names = SO.equity_list()
    out, seen = [], set()
    for e in entities or []:
        if not isinstance(e, dict):
            continue
        name = SO.clean_entity(str(e.get("name") or ""))
        if not name or re.match(SO.UNNAMED_RX, name):
            continue
        key = SO._norm_name(name)
        if key in seen:
            continue
        seen.add(key)
        sym = names.get(key)
        listed = dates.get(sym) if sym else None
        if listed and listed > today.isoformat():
            listed = None
        row = {k: (str(v).strip() if isinstance(v, (str, int, float)) else v) for k, v in e.items()}
        row.update({"name": name, "symbol": sym if (sym and sym != parent_symbol) else (sym or ""),
                    "listed_on": listed or "", "is_parent": bool(sym and sym == parent_symbol)})
        out.append(row)
    return out


# ------------------------------------------------------------------- size

def _pct(s) -> float | None:
    m = re.search(r"(\d{1,3}(?:\.\d+)?)\s*%", str(s or ""))
    return float(m.group(1)) if m else None


def size_view(entities: list[dict], parent_fin: dict, seg_tables: list[dict], parent_symbol: str,
              mcaps: tuple[str, dict[str, float]] | None = None, members: dict | None = None) -> dict:
    """The separated piece(s) against the parent, three ways, and the
    reading for forced selling. Shares are computed here; the stated
    percentage is the documents' own."""
    rows = []
    mdate, caps = mcaps or ("", {})
    pcap = caps.get(parent_symbol)
    parent_sales = None
    if parent_fin.get("available"):
        sales = next((r["values"] for r in parent_fin["rows"] if r["metric"].startswith("Sales (")), [])
        parent_sales = dict(zip(parent_fin.get("years", []), sales))
    best = []
    for e in entities:
        if e.get("is_parent"):
            continue
        stated = _pct(e.get("turnover_pct_of_parent"))
        cap = caps.get(e.get("symbol") or "")
        cap_share = round(100 * cap / (cap + pcap), 1) if cap and pcap else None
        seg_share, seg_fy = None, ""
        for st in seg_tables:
            if not st.get("available") or st.get("side") == "remaining" \
                    or not _same_business(st.get("entity", ""), st.get("segment_name", ""), e):
                continue
            rev = next((r["values"] for r in st["rows"] if r["metric"].startswith("Revenue (")), [])
            for fy, v in reversed(list(zip(st.get("years", []), rev))):
                ps = _parent_sales_for(parent_sales, fy)
                if v and ps and st.get("unit_factor"):
                    seg_share, seg_fy = round(100 * v * st["unit_factor"] / ps, 1), fy
                    break
            if seg_share is not None:
                break
        share = stated if stated is not None else seg_share if seg_share is not None else cap_share
        if share is not None:
            best.append(share)
        rows.append({"entity": e["name"], "symbol": e.get("symbol", ""),
                     "stated_turnover": e.get("turnover", ""), "stated_pct": stated,
                     "segment_pct": seg_share, "segment_fy": seg_fy,
                     "mcap_cr": round(cap) if cap else None, "mcap_pct": cap_share,
                     "index_member": bool(members and e.get("symbol") in members), "share_used": share})
    total = sum(best) if best else None
    smallest = min(best) if best else None
    if smallest is None:
        reading = "not determinable — the documents on file give no size for the separated piece"
    elif smallest < 10:
        reading = ("VERY LIKELY — the piece is under a tenth of the whole; index funds and large holders "
                   "who receive it without choosing it tend to sell")
    elif smallest < 25:
        reading = "LIKELY — the piece is small beside the parent; mandates with size limits tend to sell"
    elif smallest < 50:
        reading = "POSSIBLE — the piece is a sizeable minority of the whole; forced selling on size alone is weaker"
    else:
        reading = "LESS LIKELY on size alone — the piece is the larger part of the business"
    return {"rows": rows, "parent_mcap_cr": round(pcap) if pcap else None, "mcap_date": mdate,
            "total_share": total, "smallest_share": smallest, "reading": reading}


MATCH_SKIP = set(FN.GENERIC_WORDS) | {"enterprises", "industries", "holdings", "global", "international", "technologies",
                                      "ventures", "corporation", "under", "which", "their", "other", "businesses", "including",
                                      "composite", "remaining", "company", "through", "related", "comprising"}


def _same_business(entity: str, segment: str, e: dict) -> bool:
    """Does a segment table belong to entity `e`? First by the entity the
    judge attached to it (a distinctive word of the entity's name), then by
    a distinctive word of the entity's business in the segment's name."""
    ent = SO._norm_name(entity)
    for w in re.findall(r"[A-Za-z]{4,}", e.get("name", "")):
        if w.lower() not in MATCH_SKIP:
            if w.lower() in ent:
                return True
            break                                   # only the first distinctive word of the name
    seg = SO._norm_name(segment)
    return any(w.lower() in seg for w in re.findall(r"[A-Za-z]{6,}", e.get("business", ""))
               if w.lower() not in MATCH_SKIP)


def _parent_sales_for(parent_sales: dict | None, fy: str) -> float | None:
    """Parent sales (₹ cr) for a fiscal-year label like 'FY2025'."""
    if not parent_sales:
        return None
    m = re.search(r"(\d{4})", fy or "")
    if not m:
        return None
    for label, v in parent_sales.items():
        if label.endswith(m.group(1)) and v:
            return v
    return None


UNIT_FACTOR = {"crore": 1.0, "cr": 1.0, "million": 0.1, "mn": 0.1, "lakh": 0.01, "lakhs": 0.01, "billion": 100.0, "bn": 100.0}


def unit_factor(unit: str) -> float | None:
    """₹-crore multiplier for a unit string ('₹ million' → 0.1); None for
    a foreign currency or an unknown unit."""
    u = (unit or "").lower()
    if re.search(r"usd|\$|eur|€|gbp|£|sek", u):
        return None
    hits = [(m.start(), f) for k, f in UNIT_FACTOR.items() for m in [re.search(rf"\b{k}\b", u)] if m]
    return min(hits)[1] if hits else None          # the first unit the string names


# ---------------------------------------------------------------- compare

def _last(series: list, years: list) -> tuple[float | None, str]:
    for v, y in zip(reversed(series or []), reversed(years or [])):
        if v is not None:
            return v, y
    return None, ""


def working_capital(symbol: str) -> dict:
    """Latest debtor / inventory / payable days, cash conversion cycle,
    working-capital days and ROCE from the stored working-capital file,
    and debt / equity from the stored balance sheet."""
    out: dict = {}
    p = WC_DIR / f"{symbol}.csv"
    if p.exists():
        with open(p) as fh:
            rd = list(csv.reader(fh))
        years = rd[0][1:]
        for r in rd[1:]:
            vals = [float(x) if x not in ("", None) else None for x in r[1:]]
            v, y = _last(vals, years)
            if v is not None:
                out[r[0]] = (v, y)
    b = BS_DIR / f"{symbol}.csv"
    if b.exists():
        years, series = FN._table(b)
        eq = [(a or 0) + (c or 0) if a is not None or c is not None else None
              for a, c in zip(series.get("Equity Capital", []), series.get("Reserves", []))]
        debt = series.get("Borrowings", [])
        for i in range(len(years) - 1, -1, -1):
            if i < len(eq) and i < len(debt) and eq[i] and debt[i] is not None:
                out["Debt / equity (x)"] = (round(debt[i] / eq[i], 2), years[i])
                out["Borrowings (₹ cr)"] = (debt[i], years[i])
                break
    return out


def compare(parent_symbol: str, parent_fin: dict, entities: list[dict], seg_tables: list[dict]) -> dict:
    """Parent against each separated business. A listed entity with stored
    statements is compared on its own reported numbers; otherwise the
    segment numbers the judge extracted are used. Every figure is the
    latest available, labelled with its year; nothing is estimated."""
    def fin_metrics(fin: dict) -> dict:
        m = {}
        if not fin.get("available"):
            return m
        yrs = fin["years"]
        for want, key in (("Sales (", "Sales (₹ cr)"), ("Sales growth", "Sales growth (%)"),
                          ("OPM", "Operating margin (%)"), ("PAT margin", "PAT margin (%)"),
                          ("Operating profit growth", "Operating profit growth (%)")):
            row = next((r for r in fin["rows"] if r["metric"].startswith(want)), None)
            if row:
                v, y = _last(row["values"], yrs)
                if v is not None:
                    m[key] = (v, y)
        return m
    cols = [{"label": f"Parent ({parent_symbol})", "basis": "reported, consolidated",
             "metrics": {**fin_metrics(parent_fin), **working_capital(parent_symbol)}}]
    for e in entities:
        if e.get("is_parent"):
            continue
        sym = e.get("symbol") or ""
        own = FN.parent_financials(sym) if sym else {"available": False}
        if own.get("available"):
            cols.append({"label": f"{e['name']} ({sym})", "basis": "its own reported statements",
                         "metrics": {**fin_metrics(own), **working_capital(sym)}})
            continue
        st = next((t for t in seg_tables if t.get("available") and t.get("side") != "remaining"
                   and _same_business(t.get("entity", ""), t.get("segment_name", ""), e)), None)
        if st:
            m = {}
            yrs = st["years"]
            for want, key in (("Revenue (", f"Sales ({st.get('unit', '')})"), ("Revenue growth", "Sales growth (%)"),
                              ("Operating margin", "Operating margin (%)"), ("Operating profit growth", "Operating profit growth (%)"),
                              ("Return on capital employed", "ROCE %"), ("Segment assets / revenue", "Segment assets / revenue (x)")):
                row = next((r for r in st["rows"] if r["metric"].startswith(want)), None)
                if row:
                    v, y = _last(row["values"], yrs)
                    if v is not None:
                        m[key] = (v, y)
            cols.append({"label": e["name"], "basis": f"segment numbers ({st.get('segment_name', '')})", "metrics": m})
        else:
            cols.append({"label": e["name"], "basis": "no numbers on file", "metrics": {}})
    order = ["Sales (₹ cr)", "Sales growth (%)", "Operating margin (%)", "Operating profit growth (%)", "PAT margin (%)",
             "ROCE %", "Debtor Days", "Inventory Days", "Days Payable", "Cash Conversion Cycle", "Working Capital Days",
             "Debt / equity (x)", "Borrowings (₹ cr)", "Segment assets / revenue (x)"]
    keys = [k for k in order if any(k in c["metrics"] for c in cols)]
    keys += [k for c in cols for k in c["metrics"] if k not in keys and k not in order]
    return {"columns": cols, "metrics": keys}
