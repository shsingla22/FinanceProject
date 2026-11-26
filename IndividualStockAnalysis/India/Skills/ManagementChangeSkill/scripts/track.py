"""
track.py — the numbers: three years of financials, and the track record of
the people going out and coming in. Everything here is computed from the
stored statements (screener.in, consolidated) — never read from a model.

A track record is the company's results while a person held the seat:
sales, profit, margin and return on capital at the start and the end of
the tenure, and the growth in between. It is the record of the company
under them, not a claim about what one person caused.

For an incoming person the documents' own profile gives the earlier
employers; where an earlier employer is itself a company in the universe
(or the annual reports on file show the person in a seat there), the same
record is computed for that company over those years.
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import re
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
PNL = INDIA / "ProfitStatement" / "NiftyTotalMarket"
BS = INDIA / "BalanceSheet" / "NiftyTotalMarket"
CASH = INDIA / "CashFlow" / "NiftyTotalMarket"
WC = INDIA / "WorkingCapital" / "NiftyTotalMarket"
MGMT_INFO = INDIA / "ManagementInfo" / "NiftyTotalMarket"
BUNDLES = INDIA / "Announcements" / "_bhav_bundles"
YEARS = 3


# ----------------------------------------------------------- statements

def table(path: Path) -> tuple[list[str], dict[str, list[float | None]]]:
    """(year labels, {line item: values}) from a stored statement CSV. The
    P&L, balance sheet and cash flow carry a parent-line-item column; the
    working-capital file does not."""
    if not path.exists():
        return [], {}
    with open(path, newline="") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        return [], {}
    off = 2 if len(rows[0]) > 1 and rows[0][1] == "parent_line_item" else 1
    years = [re.sub(r"\s+", " ", y).strip() for y in rows[0][off:]]
    out = {}
    for r in rows[1:]:
        if not r or not r[0]:
            continue
        vals = []
        for v in r[off:off + len(years)]:
            try:
                vals.append(float(v))
            except ValueError:
                vals.append(None)
        out[r[0]] = vals + [None] * (len(years) - len(vals))
    return years, out


def _fy(label: str) -> int | None:
    """'Mar 2026' → 2026 (the fiscal year it closes); 'Dec 2025' → 2025."""
    m = re.search(r"(\d{4})", label or "")
    return int(m.group(1)) if m else None


def growth(cur, prev):
    if cur is None or prev is None or prev == 0:
        return None
    return round((cur - prev) / abs(prev) * 100, 1)


def ratio(num, den, pct=True):
    if num is None or den in (None, 0):
        return None
    return round(num / den * (100 if pct else 1), 1 if pct else 2)


def cagr(first, last, years: int):
    if first is None or last is None or first <= 0 or last <= 0 or years <= 0:
        return None
    return round(((last / first) ** (1 / years) - 1) * 100, 1)


def series(symbol: str) -> dict:
    """Every year on file for one company, the lines a reader needs, under
    common names whether it is a company (Sales / Operating Profit) or a
    lender (Revenue / Financing Profit): {'years': [...], 'fy': [...],
    'revenue', 'operating_profit', 'pat', 'eps', 'cfo', 'fcf', 'equity',
    'borrowings', 'roce', 'wc_days', 'debtor_days', 'lender': bool}."""
    years, p = table(PNL / f"{symbol}.csv")
    if not years:
        return {"available": False}
    lender = "Sales" not in p and "Revenue" in p
    rev = p.get("Sales") or p.get("Revenue") or [None] * len(years)
    op = p.get("Operating Profit") or p.get("Financing Profit") or [None] * len(years)
    out = {"available": True, "years": years, "fy": [_fy(y) for y in years], "lender": lender,
           "revenue": rev, "operating_profit": op, "pat": p.get("Net Profit") or [None] * len(years),
           "eps": p.get("EPS in Rs") or [None] * len(years)}

    def align(path: Path, items: dict[str, str]) -> None:
        ys, t = table(path)
        pos = {y: i for i, y in enumerate(ys)}
        for name, item in items.items():
            vals = t.get(item) or []
            out[name] = [vals[pos[y]] if y in pos and pos[y] < len(vals) else None for y in years]
    align(CASH / f"{symbol}.csv", {"cfo": "Cash from Operating Activity", "fcf": "Free Cash Flow"})
    align(BS / f"{symbol}.csv", {"equity_capital": "Equity Capital", "reserves": "Reserves", "borrowings": "Borrowings"})
    align(WC / f"{symbol}.csv", {"roce": "ROCE %", "wc_days": "Working Capital Days", "debtor_days": "Debtor Days",
                                 "ccc": "Cash Conversion Cycle"})
    out["equity"] = [(a or 0) + (b or 0) if (a is not None or b is not None) else None
                     for a, b in zip(out["equity_capital"], out["reserves"])]
    return out


def financials(symbol: str, n: int = YEARS) -> dict:
    """The last `n` fiscal years: revenue, operating profit, PAT with growth
    and margins, cash flow, return on capital and equity, debt, working
    capital — one table."""
    s = series(symbol)
    if not s.get("available"):
        return {"available": False}
    idx = [i for i, v in enumerate(s["revenue"]) if v is not None]
    if not idx:
        return {"available": False}
    show = idx[-n:]
    prev = {i: (idx[idx.index(i) - 1] if idx.index(i) > 0 else None) for i in show}
    g = lambda k, i: s[k][i] if i is not None and i < len(s[k]) else None      # noqa: E731
    rev_name = "Revenue" if s["lender"] else "Sales"
    op_name = "Financing profit" if s["lender"] else "Operating profit"
    rows = [
        (f"{rev_name} (₹ cr)", [g("revenue", i) for i in show]),
        (f"{rev_name} growth (%)", [growth(g("revenue", i), g("revenue", prev[i])) for i in show]),
        (f"{op_name} (₹ cr)", [g("operating_profit", i) for i in show]),
        (f"{op_name} margin (%)", [ratio(g("operating_profit", i), g("revenue", i)) for i in show]),
        ("PAT (₹ cr)", [g("pat", i) for i in show]),
        ("PAT growth (%)", [growth(g("pat", i), g("pat", prev[i])) for i in show]),
        ("PAT margin (%)", [ratio(g("pat", i), g("revenue", i)) for i in show]),
        ("EPS (₹)", [g("eps", i) for i in show]),
        ("Cash from operations (₹ cr)", [g("cfo", i) for i in show]),
        ("Free cash flow (₹ cr)", [g("fcf", i) for i in show]),
        ("ROCE (%)", [g("roce", i) for i in show]),
        ("ROE (%)", [ratio(g("pat", i), g("equity", i)) for i in show]),
        ("Borrowings (₹ cr)", [g("borrowings", i) for i in show]),
        ("Debt / equity (x)", [ratio(g("borrowings", i), g("equity", i), pct=False) for i in show]),
        ("Working-capital days", [g("wc_days", i) for i in show]),
    ]
    rows = [{"metric": m, "values": v} for m, v in rows if any(x is not None for x in v)]
    return {"available": True, "years": [s["years"][i] for i in show], "rows": rows, "lender": s["lender"],
            "source": f"ProfitStatement, BalanceSheet, CashFlow and WorkingCapital /NiftyTotalMarket/{symbol}.csv "
                      f"(consolidated, screener.in); growth, margins and ratios computed here"}


# ---------------------------------------------------------- track record

def fy_of(date_or_year: str | int | None) -> int | None:
    """The fiscal year (April–March, named by its closing year) a date falls
    in: '2019-07-01' → 2020, '2019-02' → 2019, '2019' → 2020 (a bare year is
    read as the fiscal year that began in it), 'FY2021' → 2021."""
    s = str(date_or_year or "").strip()
    m = re.search(r"FY\s*'?(\d{2,4})", s, re.I)
    if m:
        y = int(m.group(1))
        return y + 2000 if y < 100 else y
    m = re.search(r"(\d{4})-(\d{1,2})", s)
    if m:
        y, mo = int(m.group(1)), int(m.group(2))
        return y + 1 if mo >= 4 else y
    m = re.search(r"\b(19|20)\d{2}\b", s)
    if m:
        mon = re.search(r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)", s, re.I)
        y = int(m.group(0))
        if mon:
            return y + 1 if "jan feb mar".find(mon.group(1).lower()) == -1 else y
        return y + 1
    return None


def tenure_record(symbol: str, start_fy: int | None, end_fy: int | None) -> dict:
    """The company's results over a tenure: the fiscal year BEFORE the
    person took the seat (the base they inherited) to the last full fiscal
    year they held it. {'available', 'from', 'to', 'years', 'rows':
    [{metric, start, end, change}]} — CAGR for sales and profit, start → end
    for margin, ROCE, ROE, borrowings."""
    s = series(symbol)
    if not s.get("available") or not start_fy:
        return {"available": False, "why": "no statements on file" if not s.get("available") else "tenure start not known"}
    have = {fy: i for i, fy in enumerate(s["fy"]) if fy is not None and s["revenue"][i] is not None}
    if not have:
        return {"available": False, "why": "no statements on file"}
    last = max(have)
    end = min(end_fy or last, last)
    base = start_fy - 1
    clipped = False
    if base < min(have):
        base, clipped = min(have), True
    if end not in have:
        end = max((fy for fy in have if fy <= end), default=None)
    if end is None or base not in have or end <= base:
        return {"available": False, "why": "the tenure is shorter than one full fiscal year on file"}
    a, b, n = have[base], have[end], end - base
    g = lambda k, i: s[k][i] if i < len(s[k]) else None      # noqa: E731
    rev_name = "Revenue" if s["lender"] else "Sales"
    op_name = "Financing profit" if s["lender"] else "Operating profit"
    rows = [
        {"metric": f"{rev_name} (₹ cr)", "start": g("revenue", a), "end": g("revenue", b),
         "change": _cagr_text(g("revenue", a), g("revenue", b), n)},
        {"metric": f"{op_name} (₹ cr)", "start": g("operating_profit", a), "end": g("operating_profit", b),
         "change": _cagr_text(g("operating_profit", a), g("operating_profit", b), n)},
        {"metric": "PAT (₹ cr)", "start": g("pat", a), "end": g("pat", b), "change": _cagr_text(g("pat", a), g("pat", b), n)},
        {"metric": f"{op_name} margin (%)", "start": ratio(g("operating_profit", a), g("revenue", a)),
         "end": ratio(g("operating_profit", b), g("revenue", b)), "change": "points"},
        {"metric": "ROCE (%)", "start": g("roce", a), "end": g("roce", b), "change": "points"},
        {"metric": "ROE (%)", "start": ratio(g("pat", a), g("equity", a)), "end": ratio(g("pat", b), g("equity", b)), "change": "points"},
        {"metric": "Borrowings (₹ cr)", "start": g("borrowings", a), "end": g("borrowings", b), "change": "abs"},
    ]
    for r in rows:
        if r["change"] in ("points", "abs"):
            d = (r["end"] - r["start"]) if r["start"] is not None and r["end"] is not None else None
            r["change"] = "—" if d is None else (f"{d:+.1f} pts" if r["change"] == "points" else f"{d:+,.0f}")
    rows = [r for r in rows if r["start"] is not None or r["end"] is not None]
    return {"available": True, "symbol": symbol, "from": s["years"][a], "to": s["years"][b], "years": n,
            "clipped": clipped, "rows": rows}


def _cagr_text(first, last, n: int) -> str:
    c = cagr(first, last, n)
    if c is not None:
        return f"{c:+.1f}% a year over {n} year{'s' if n != 1 else ''}"
    if first is not None and last is not None:
        if first <= 0 < last:
            return "loss to profit"
        if last <= 0 < first:
            return "profit to loss"
    return "—"


# ------------------------------------------------- people on file

_INFO: list[dict] | None = None


def _norm(name: str) -> str:
    n = re.sub(r"\b(?:Mr|Ms|Mrs|Shri|Smt|Dr|Sri|Prof|CA|CS)\.?\s+", "", name or "", flags=re.I)
    return re.sub(r"\s+", " ", re.sub(r"[^A-Za-z ]", " ", n).lower()).strip()


def same_person(a: str, b: str) -> bool:
    """Two spellings of one person: every word of the shorter name appears
    in the longer (in full, or as an initial), and the surnames agree. A
    single shared word is never enough."""
    x, y = _norm(a).split(), _norm(b).split()
    if len(x) < 2 or len(y) < 2 or x[-1] != y[-1]:
        return False
    short, long_ = (x, y) if len(x) <= len(y) else (y, x)
    for w in short[:-1]:
        if not any(w == v or (len(w) == 1 and v.startswith(w)) or (len(v) == 1 and w.startswith(v)) for v in long_[:-1]):
            return False
    return True


def people_on_file() -> list[dict]:
    """Every (company, seat, person, years) the annual-report read has on
    file (`ManagementInfo/`), with the first and last fiscal year seen."""
    global _INFO
    if _INFO is None:
        _INFO = []
        for p in sorted(MGMT_INFO.glob("*.csv")):
            try:
                with open(p, newline="") as fh:
                    rows = list(csv.DictReader(fh))
            except OSError:
                continue
            for r in rows:
                name = re.sub(r"\s+", " ", (r.get("name") or "")).strip(" -")
                yrs = [int(x) for x in re.findall(r"FY(\d{4})", r.get("years_present") or "")]
                if len(_norm(name).split()) < 2 or not yrs:
                    continue
                _INFO.append({"symbol": p.stem, "role": r.get("role") or "", "name": name,
                              "first_fy": min(yrs), "last_fy": max(yrs), "status": r.get("status") or ""})
    return _INFO


def seats_held(name: str, exclude_symbol: str = "") -> list[dict]:
    """Seats the annual reports on file show this person in — at this or
    any other company of the universe."""
    out, seen = [], set()
    for r in people_on_file():
        if r["symbol"] == exclude_symbol or not same_person(name, r["name"]):
            continue
        key = (r["symbol"], r["role"])
        if key in seen:
            for o in out:
                if (o["symbol"], o["role"]) == key:
                    o["first_fy"], o["last_fy"] = min(o["first_fy"], r["first_fy"]), max(o["last_fy"], r["last_fy"])
            continue
        seen.add(key)
        out.append(dict(r))
    return out


def seat_since(symbol: str, name: str, seat: str) -> int | None:
    """The first fiscal year the annual reports on file show this person in
    this seat at this company (a floor: the reports on file go back about
    five years)."""
    want = {"CFO": ("cfo",), "CEO": ("ceo", "managing director", "chairman"),
            "MD": ("managing director", "ceo", "chairman")}.get(seat, (seat.lower(),))
    hits = [r["first_fy"] for r in people_on_file()
            if r["symbol"] == symbol and same_person(name, r["name"]) and any(w in r["role"].lower() for w in want)]
    return min(hits) if hits else None


# -------------------------------------------------------------- prices

_PX: dict[str, dict[str, float]] = {}


def _bundle(d: dt.date) -> Path:
    return BUNDLES / f"PR{d.day:02d}{d.month:02d}{d.year % 100:02d}.zip"


def closes_on(d: dt.date) -> dict[str, float]:
    """{symbol: close} from the bhavcopy bundle of one trading day ({} when
    there is none)."""
    key = d.isoformat()
    if key in _PX:
        return _PX[key]
    out: dict[str, float] = {}
    p = _bundle(d)
    if p.exists():
        try:
            with zipfile.ZipFile(p) as z:
                name = next((n for n in z.namelist() if n.lower().startswith("pd") and n.lower().endswith(".csv")), None)
                if name:
                    for r in csv.DictReader(io.StringIO(z.read(name).decode("utf-8", "replace"))):
                        sym = (r.get("SYMBOL") or "").strip()
                        if sym and (r.get("SERIES") or "").strip() in ("EQ", "BE", "BZ"):
                            try:
                                out[sym] = float(r["CLOSE_PRICE"])
                            except (ValueError, KeyError, TypeError):
                                pass
                        elif not sym and (r.get("SECURITY") or "").strip() == "Nifty 500":
                            try:
                                out["^NIFTY500"] = float(r["CLOSE_PRICE"])
                            except (ValueError, KeyError, TypeError):
                                pass
        except (zipfile.BadZipFile, OSError, StopIteration):
            pass
    _PX[key] = out
    return out


def close_near(symbol: str, d: dt.date, direction: int, reach: int = 10) -> tuple[str, float] | None:
    """The close on the nearest trading day at or before (direction -1) or
    at or after (+1) `d`, within `reach` days."""
    for k in range(reach + 1):
        day = d + dt.timedelta(days=direction * k)
        px = closes_on(day).get(symbol)
        if px:
            return day.isoformat(), px
    return None


def latest_trading_day(today: dt.date, reach: int = 30) -> dt.date | None:
    for k in range(reach + 1):
        d = today - dt.timedelta(days=k)
        if _bundle(d).exists():
            return d
    return None


def price_since(symbol: str, announced: str, today: dt.date) -> dict:
    """The share price from the last close BEFORE the announcement to the
    latest close on file, beside the Nifty 500 over the same days."""
    try:
        d = dt.date.fromisoformat(announced[:10])
    except ValueError:
        return {"available": False}
    last = latest_trading_day(today)
    if not last or last <= d:
        return {"available": False}
    before = close_near(symbol, d - dt.timedelta(days=1), -1)
    after = close_near(symbol, last, -1)
    if not before or not after:
        return {"available": False}
    out = {"available": True, "before": before, "latest": after, "change_pct": growth(after[1], before[1])}
    ib, ia = close_near("^NIFTY500", dt.date.fromisoformat(before[0]), -1), close_near("^NIFTY500", dt.date.fromisoformat(after[0]), -1)
    if ib and ia:
        out["index_change_pct"] = growth(ia[1], ib[1])
    return out
