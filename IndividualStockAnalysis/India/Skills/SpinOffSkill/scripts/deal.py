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


def entity_terms(names: list[str], company: str = "", text: str = "") -> re.Pattern:
    """SPIN_TERMS plus the names of the separated entities, so 'when does
    Fleur list?' is caught without the word demerger — but only names that
    MEAN the entity: the first two words of its name when the parent's own
    name does not contain them ('Vedanta Power', 'ITC Hotels'; not 'Tata
    Motors' inside Tata Motors Passenger Vehicles), and a single coined
    word ('Digitide', 'Fleur') — never an ordinary word of the business
    ('aluminium', 'power', 'steel', 'hotels'), which the transcripts also
    print in lower case and which would pull in every operating question."""
    parent = " ".join(re.findall(r"[A-Za-z0-9]+", company)).lower()
    skip = set(parent.split()) | set(FN.GENERIC_WORDS)
    skip |= {"india", "indian", "limited", "private", "services", "solutions", "enterprises", "industries", "holdings",
             "global", "international", "technologies", "products", "ventures", "national", "management", "company"}
    terms: list[str] = []
    for n in names:
        ws = re.findall(r"[A-Za-z][A-Za-z0-9']*", _stem(SO.clean_entity(n or "")))
        if len(ws) >= 2:
            pair = f"{ws[0]} {ws[1]}".lower()
            if pair not in parent and len(pair) >= 7 and ws[1].lower() not in ("and", "of", "limited", "private"):
                terms.append(r"\b" + re.escape(ws[0]) + r"\s+" + re.escape(ws[1]) + r"\b")
        for w in ws:
            lw = w.lower()
            if len(w) < 5 or lw in skip:
                continue
            ordinary = len(re.findall(r"(?<![A-Za-z])" + re.escape(lw) + r"(?![A-Za-z])", text or "")) >= 3   # printed in lower case
            if not ordinary:
                terms.append(r"\b" + re.escape(lw) + r"\b")
            break                                  # only the first distinctive word of each name
    terms = list(dict.fromkeys(terms))
    if not terms:
        return SPIN_TERMS_RX
    return re.compile(SPIN_TERMS_RX.pattern + "|" + "|".join(terms), re.I)


def call_exchanges(symbol: str, today: dt.date, months: int = 36, names: list[str] | None = None,
                   company: str = "", links: dict | None = None) -> list[dict]:
    """Every call of the last `months` months (never after `today`), oldest
    first, with its exchanges about the separation:
    [{'call': 'May 2024', 'date': '2024-05-01', 'url': …, 'exchanges': […]}]."""
    text = SO.concall_text(symbol)
    if not text:
        return []
    rx = entity_terms(names or [], company, text)
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

ROLE_SEPARATED = ("resulting", "listed_subsidiary")
LONG_LISTED_DAYS = 1100
_ROLE_KEYS = (("resulting", "resulting"), ("listed_sub", "listed_subsidiary"), ("subsidiary", "listed_subsidiary"),
              ("former_parent", "former_parent"), ("parent", "parent"), ("remaining", "parent"), ("demerged", "parent"),
              ("merged", "merged_in"), ("amalgam", "merged_in"), ("transferor", "merged_in"),
              ("unrelated", "unrelated"), ("other", "other"))
_MERGED_RX = re.compile(r"\b(?:amalgamated (?:into|with)|merged (?:by absorption )?(?:into|with)|transferor compan|"
                        r"dissolved without|stands? dissolved|amalgamating compan)", re.I)
_REMAIN_RX = re.compile(r"^\W*(?:the\s+)?(?:remaining business|demerged company|residual)", re.I)
_NO_LISTING_RX = re.compile(r"^\W*not to be listed", re.I)
_DROPPED_RX = re.compile(r"\b(?:withdrawn|dropped|shelved|not pursued|called off)\b", re.I)


def entity_role(e: dict, is_self: bool) -> str:
    """What an entity IS in the scheme: 'resulting' (a separated business
    whose shares go to the parent's shareholders), 'listed_subsidiary' (a
    partial spin-off by IPO), 'parent' (the company itself / what remains),
    'former_parent', 'merged_in' (amalgamated and dissolved — nothing to
    hold), 'unrelated' or 'other'. The judge's own label when it gave one;
    otherwise read from the entry's words (an older answer, or a name the
    mechanical read added)."""
    if is_self:
        return "parent"
    r = re.sub(r"[^a-z]+", "_", str(e.get("role") or "").lower()).strip("_")
    for k, v in _ROLE_KEYS:
        if r.startswith(k):
            return v
    blob = " ".join(str(e.get(k) or "") for k in ("business", "swap_ratio"))
    if _REMAIN_RX.search(str(e.get("business") or "")):
        return "parent"
    if _NO_LISTING_RX.search(str(e.get("listing") or "")) or _MERGED_RX.search(blob):
        return "merged_in"
    return "resulting"


def is_separated(e: dict) -> bool:
    """An entity a shareholder of the parent ends up holding (or can buy in
    an IPO) — not the parent, not a company merged in, not one dropped."""
    if "role" not in e:
        return not e.get("is_parent")
    return e.get("role") in ROLE_SEPARATED and not e.get("dropped")


def separated(entities: list[dict] | None) -> list[dict]:
    return [e for e in (entities or []) if is_separated(e)]


def enrich_entities(entities: list[dict], parent_symbol: str, today: dt.date) -> list[dict]:
    """Each entity the deal sheet names, cleaned, with its role in the
    scheme, and its NSE symbol and listing date when the exchange's equity
    list has it under its name, a former name, or the symbol the judge
    matched from the exchange's own list (never a date after `today`)."""
    dates, names = SO.equity_list()
    out, seen = [], {}
    for e in entities or []:
        if not isinstance(e, dict):
            continue
        name = SO.clean_entity(str(e.get("name") or ""))
        if not name or re.match(SO.UNNAMED_RX, name):
            continue
        key = SO._norm_name(name)
        sym = names.get(key)
        if not sym:                                   # the symbol the judge matched, when the exchange has it
            cand = str(e.get("nse_symbol") or "").strip().upper()
            sym = cand if cand in dates else None
        if not sym:                                   # a former name the exchange still lists
            for fn in (e.get("former_names") or []) if isinstance(e.get("former_names"), list) else []:
                sym = names.get(SO._norm_name(SO.clean_entity(str(fn))))
                if sym:
                    break
        dup = seen.get(key) or (seen.get("sym:" + sym) if sym else None)
        if dup is not None:                           # the same company named twice: keep the fuller entry
            for k, v in e.items():
                if v and not dup.get(k):
                    dup[k] = str(v).strip() if isinstance(v, (str, int, float)) else v
            continue
        listed = dates.get(sym) if sym else None
        if listed and listed > today.isoformat():
            listed = None
        row = {k: (str(v).strip() if isinstance(v, (str, int, float)) else v) for k, v in e.items()}
        is_self = bool(sym and sym == parent_symbol)
        role = entity_role(e, is_self)
        if role == "listed_subsidiary" and listed and (today - dt.date.fromisoformat(listed)).days > LONG_LISTED_DAYS:
            role = "other"                            # a subsidiary listed years ago (Hindustan Zinc) is not a spin-off now
        row.update({"name": name, "symbol": sym or "", "listed_on": listed or "", "is_parent": is_self,
                    "role": role,
                    "dropped": bool(_DROPPED_RX.search(str(e.get("status") or "")))})
        out.append(row)
        seen[key] = row
        if sym:
            seen["sym:" + sym] = row
    return out


def _stem(name: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"\b(?:Limited|Ltd\.?)\s*$", "", name or "", flags=re.I)).strip()


def equity_rows(path: Path | None = None) -> list[dict]:
    """NSE's equity list as rows (symbol, name, listing_date)."""
    path = path or SO.EQUITY_LIST
    if not path.exists():
        return []
    with open(path) as fh:
        return [r for r in csv.DictReader(fh)
                if r.get("symbol") and re.fullmatch(r"\d{4}-\d{2}-\d{2}", r.get("listing_date") or "")]


def arrivals(company: str, parent_symbol: str, record_date: str, today: dt.date, text: str = "",
             equities: list[dict] | None = None, window: int = 150) -> list[dict]:
    """The exchange's own cross-check on the entity list: companies that
    BEGAN TRADING in the `window` days after a demerger record date and
    either carry the parent's name (Vedanta → Vedanta Aluminium Metal,
    Vedanta Power, Vedanta Iron and Steel, Vedanta Oil and Gas) or are
    named in the company's filings. Candidates only — the judge says from
    the documents which of them the scheme created."""
    try:
        rd = dt.date.fromisoformat(str(record_date)[:10])
    except ValueError:
        return []
    first = (re.sub(r"[^A-Za-z0-9 ]", " ", company or "").split() or [""])[0].lower()
    low = re.sub(r"\s+", " ", text or "").lower()
    out = []
    for e in (equities if equities is not None else equity_rows()):
        if e["symbol"] == parent_symbol or e["listing_date"] > today.isoformat():
            continue
        gap = (dt.date.fromisoformat(e["listing_date"]) - rd).days
        if not 0 <= gap <= window:
            continue
        stem = _stem(e.get("name") or "")
        tok = (re.sub(r"[^A-Za-z0-9 ]", " ", stem).split() or [""])[0].lower()
        by_name = len(first) >= 4 and tok == first
        in_text = len(stem) >= 10 and len(stem.split()) >= 2 and stem.lower() in low
        if by_name or in_text:
            out.append({"symbol": e["symbol"], "name": e.get("name") or e["symbol"], "listed_on": e["listing_date"],
                        "why": "carries the parent's name" if by_name else "named in the filings"})
    return sorted(out, key=lambda x: (x["listed_on"], x["symbol"]))


# ------------------------------------------------------------------- size

def _pct(s) -> float | None:
    m = re.search(r"(\d{1,3}(?:\.\d+)?)\s*%", str(s or ""))
    return float(m.group(1)) if m else None


def _reading(share: float | None) -> str:
    if share is None:
        return "not determinable — the documents on file give no size for the separated piece"
    if share < 10:
        return ("VERY LIKELY — the piece is under a tenth of the whole; index funds and large holders "
                "who receive it without choosing it tend to sell")
    if share < 25:
        return "LIKELY — the piece is small beside the parent; mandates with size limits tend to sell"
    if share < 50:
        return "POSSIBLE — the piece is a sizeable minority of the whole; forced selling on size alone is weaker"
    return "LESS LIKELY on size alone — the piece is the larger part of the business"


def stated_split(statement: str, e: dict) -> float | None:
    """This entity's share in a split the documents print by name — the
    cost-of-acquisition apportionment a company publishes after a demerger
    ('Vedanta Aluminium Metal Limited 7.15% | Talwandi Sabo Power Limited
    12.23%'), under its name or an earlier name."""
    names = [e.get("name", "")] + [x for x in (e.get("former_names") or []) if isinstance(x, str)] \
        if isinstance(e.get("former_names"), list) else [e.get("name", "")]
    for n in names:
        stem = _stem(SO.clean_entity(n))
        if len(stem) < 4:
            continue
        m = re.search(re.escape(stem) + r"\s*(?:Limited|Ltd\.?)?[^%\d]{0,12}(\d{1,2}(?:\.\d+)?)\s*%", statement or "", re.I)
        if m:
            return float(m.group(1))
    return None


def size_view(entities: list[dict], parent_fin: dict, seg_tables: list[dict], parent_symbol: str,
              mcaps: tuple[str, dict[str, float]] | None = None, members: dict | None = None,
              size_statement: str = "") -> dict:
    """Each separated piece against the WHOLE (the parent plus every
    separated entity), three ways, and the reading for forced selling —
    entity by entity, since one company can separate a large piece and a
    small one. The stated percentage is the documents' own (a turnover
    share, or the cost-of-acquisition split); the market-cap share is the
    entity's value over the parent's plus all the separated entities'; the
    segment share is the business's revenue over the parent's sales. The
    reading uses the first of these that exists, in that order."""
    rows = []
    mdate, caps = mcaps or ("", {})
    pcap = caps.get(parent_symbol)
    spun = separated(entities)
    whole = (pcap + sum(caps.get(e.get("symbol") or "", 0) or 0 for e in spun)) if pcap else None
    parent_sales = None
    if parent_fin.get("available"):
        sales = next((r["values"] for r in parent_fin["rows"] if r["metric"].startswith("Sales (")), [])
        parent_sales = dict(zip(parent_fin.get("years", []), sales))
    best = []
    for e in spun:
        stated, basis = _pct(e.get("turnover_pct_of_parent")), "share of turnover"
        if stated is None:
            stated, basis = stated_split(size_statement, e), ("cost-of-acquisition split" if re.search(
                r"cost of acquisition", size_statement or "", re.I) else "split stated in the documents")
        cap = caps.get(e.get("symbol") or "")
        cap_share = round(100 * cap / whole, 1) if cap and whole else None
        seg_share, seg_fy = None, ""
        mine = tables_for(e, spun, seg_tables)
        years = sorted({fy for st in mine for fy in st.get("years", [])}, reverse=True)
        for fy in years:                               # the latest year the parent's sales cover; several segments add up
            ps = _parent_sales_for(parent_sales, fy)
            tot = 0.0
            for st in mine:
                rev = next((r["values"] for r in st["rows"] if r["metric"].startswith("Revenue (")), [])
                v = dict(zip(st.get("years", []), rev)).get(fy)
                if v and st.get("unit_factor"):
                    tot += v * st["unit_factor"]
            if tot and ps:
                seg_share, seg_fy = round(100 * tot / ps, 1), fy
                break
        share = stated if stated is not None else cap_share if cap_share is not None else seg_share
        if share is not None:
            best.append(share)
        rows.append({"entity": e["name"], "symbol": e.get("symbol", ""),
                     "stated_turnover": e.get("turnover", ""), "stated_pct": stated,
                     "stated_basis": basis if stated is not None else "",
                     "segment_pct": seg_share, "segment_fy": seg_fy,
                     "mcap_cr": round(cap) if cap else None, "mcap_pct": cap_share,
                     "index_member": bool(members and e.get("symbol") in members), "share_used": share,
                     "reading": _reading(share).split(" — ")[0]})
    total = sum(best) if best else None
    smallest = min(best) if best else None
    reading = _reading(smallest)
    sized = [r for r in rows if r["share_used"] is not None]
    if len(sized) > 1 and len({r["reading"] for r in sized}) > 1:
        reading = "BY ENTITY — " + "; ".join(f"{r['entity']}: {r['reading'].lower()} ({r['share_used']}% of the whole)" for r in sized)
    return {"rows": rows, "parent_mcap_cr": round(pcap) if pcap else None, "whole_mcap_cr": round(whole) if whole else None,
            "mcap_date": mdate, "total_share": total, "smallest_share": smallest, "reading": reading}


MATCH_SKIP = set(FN.GENERIC_WORDS) | {"enterprises", "industries", "holdings", "global", "international", "technologies",
                                      "ventures", "corporation", "under", "which", "their", "other", "businesses", "including",
                                      "composite", "remaining", "company", "through", "related", "comprising"}


def _same_business(entity: str, segment: str, e: dict, shared: frozenset = frozenset()) -> bool:
    """Does a segment table belong to entity `e`? By the entity the judge
    attached to it — its full name or an earlier name, else the first
    distinctive word of its name that no other entity shares (not
    'Vedanta' for Vedanta's five) — then by a distinctive word of the
    entity's business in the segment's name."""
    ent = SO._norm_name(entity)
    names = [e.get("name", "")] + ([x for x in e.get("former_names") if isinstance(x, str)]
                                   if isinstance(e.get("former_names"), list) else [])
    if any(len(SO._norm_name(n)) >= 5 and SO._norm_name(n) in ent for n in names):
        return True
    for w in re.findall(r"[A-Za-z]{4,}", e.get("name", "")):
        if w.lower() not in MATCH_SKIP and w.lower() not in shared:
            if w.lower() in ent:
                return True
            break                                   # only the first distinctive word of the name
    seg = SO._norm_name(segment)
    return any(w.lower() in seg for w in re.findall(r"[A-Za-z]{6,}", e.get("business", ""))
               if w.lower() not in MATCH_SKIP and w.lower() not in shared)


def tables_for(e: dict, spun: list[dict], seg_tables: list[dict]) -> list[dict]:
    """The separated-business segment tables that belong to entity `e`. A
    table the judge attached by full name to ANOTHER entity is never this
    one's; words several entities share do not identify any of them."""
    words: dict[str, int] = {}
    for x in spun:
        for w in {w.lower() for w in re.findall(r"[A-Za-z]{4,}", x.get("name", ""))}:
            words[w] = words.get(w, 0) + 1
    shared = frozenset(w for w, n in words.items() if n > 1) if len(spun) > 1 else frozenset()
    def named(st, x):
        ent = SO._norm_name(st.get("entity", ""))
        ns = [x.get("name", "")] + ([y for y in x.get("former_names") if isinstance(y, str)]
                                    if isinstance(x.get("former_names"), list) else [])
        return any(len(SO._norm_name(n)) >= 5 and SO._norm_name(n) in ent for n in ns)
    out = []
    for st in seg_tables or []:
        if not st.get("available") or st.get("side") == "remaining":
            continue
        if named(st, e):
            out.append(st)
        elif any(named(st, x) for x in spun if x is not e):
            continue
        elif _same_business(st.get("entity", ""), st.get("segment_name", ""), e, shared):
            out.append(st)
    return out


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
        years = [re.sub(r"\s+", " ", y).strip() for y in rd[0][1:]]
        for r in rd[1:]:
            vals = [float(x) if x not in ("", None) else None for x in r[1:]]
            v, y = _last(vals, years)
            if v is not None:
                out[r[0]] = (v, y)
    b = BS_DIR / f"{symbol}.csv"
    if b.exists():
        years, series = FN._table(b)
        years = [re.sub(r"\s+", " ", str(y)).strip() for y in years]
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
                          ("Operating margin", "Operating margin (%)"), ("PAT margin", "PAT margin (%)"),
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
        if not is_separated(e):
            continue
        sym = e.get("symbol") or ""
        own = FN.parent_financials(sym, min_years=1) if sym else {"available": False}
        if own.get("available"):
            cols.append({"label": f"{e['name']} ({sym})", "basis": "its own reported statements",
                         "metrics": {**fin_metrics(own), **working_capital(sym)}})
            continue
        st = next(iter(tables_for(e, separated(entities), seg_tables)), None)
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
