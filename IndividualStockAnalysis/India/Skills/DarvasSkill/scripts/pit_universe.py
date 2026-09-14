"""
pit_universe.py — a POINT-IN-TIME universe from NSE's own records.

The survivorship problem cannot be fixed with today's constituent
list: companies that died or delisted since are missing from it, and
Yahoo no longer serves their prices. NSE's daily bhavcopy archives do
not have that flaw — every stock that traded on a given day is in that
day's official file, winners and casualties alike.

    python3 pit_universe.py download --start 2014-03-01 --end 2026-09-13 \
        --dest <raw-store>
    python3 pit_universe.py build --asof 2014-03 --top 750 \
        --start 2014-03-01 --end 2020-03-31 --dest <raw-store> \
        --out <archive-dir>

`download` pulls each trading day's bhavcopy (both NSE formats: the
classic cm<DD><MON><YYYY>bhav.csv.zip until mid-2024 and the UDiFF
BhavCopy_NSE_CM_… after), parses the EQ series, and stores one small
CSV per day — resumable, holidays remembered so they are never
re-asked.

`build` then does two things with zero hindsight:
  * UNIVERSE — every EQ symbol that traded in the as-of month, ranked
    by that month's traded value, top N kept (~750 mirrors the
    NiftyTotalMarket's breadth; the index itself only launched in
    October 2021, so a point-in-time proxy is the only honest option);
  * BARS — daily OHLCV for exactly those symbols over [start, end],
    written as a standard `_all_daily_long.csv` archive the backtest
    runner already understands, plus the constituents file and a
    build log.

Raw bhavcopy prices are unadjusted, so the builder back-adjusts
(price ÷ r, volume × r before the ex-date) when one day's open
implies a standard corporate-action ratio against the prior close
(1.25, 1.5, 2, 2.5, 4, 5, 10 — within 4%) AND the next month's
median close HOLDS the rebased level (a crash recovers or keeps
falling; only a changed share count holds it) AND the volume regime
steps up AND the event day itself trades normally (no crash-rebound).
Every adjustment applied is written to `_adjustments.csv`, none is
silent.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import statistics
import sys
import time
import urllib.request
import zipfile
from collections import defaultdict
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64)"
NEW_FORMAT_FROM = dt.date(2024, 7, 8)
RATIOS = (10.0, 5.0, 4.0, 2.5, 2.0, 1.5, 1.25)
RATIO_TOL = 0.04
SERIES_KEPT = {"EQ"}


def _old_url(d: dt.date) -> str:
    mon = d.strftime("%b").upper()
    return (f"https://nsearchives.nseindia.com/content/historical/EQUITIES/"
            f"{d.year}/{mon}/cm{d.strftime('%d')}{mon}{d.year}bhav.csv.zip")


def _new_url(d: dt.date) -> str:
    return (f"https://nsearchives.nseindia.com/content/cm/"
            f"BhavCopy_NSE_CM_0_0_0_{d.strftime('%Y%m%d')}_F_0000.csv.zip")


def _get(url: str, retries: int = 3) -> bytes | None:
    """A holiday is a REPEATED miss, never a single one — a throttled
    or dropped request must not poison the holiday cache."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:             # genuinely absent
                return None
        except Exception:                 # noqa: BLE001 — retried
            pass
        time.sleep(1.5 * (attempt + 1))
    return None


def _parse(data: bytes, d: dt.date) -> list[dict]:
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        raw = z.read(z.namelist()[0]).decode("utf-8", "replace")
    rows = []
    rd = csv.DictReader(io.StringIO(raw))
    fields = {f.strip(): f for f in (rd.fieldnames or [])}
    old = "SYMBOL" in fields
    for r in rd:
        try:
            if old:
                if r["SERIES"].strip() not in SERIES_KEPT:
                    continue
                rows.append({
                    "symbol": r["SYMBOL"].strip(),
                    "date": d.isoformat(),
                    "open": float(r["OPEN"]), "high": float(r["HIGH"]),
                    "low": float(r["LOW"]), "close": float(r["CLOSE"]),
                    "volume": int(float(r["TOTTRDQTY"])),
                    "value": float(r["TOTTRDVAL"])})
            else:
                if r[fields["SctySrs"]].strip() not in SERIES_KEPT:
                    continue
                rows.append({
                    "symbol": r[fields["TckrSymb"]].strip(),
                    "date": d.isoformat(),
                    "open": float(r[fields["OpnPric"]]),
                    "high": float(r[fields["HghPric"]]),
                    "low": float(r[fields["LwPric"]]),
                    "close": float(r[fields["ClsPric"]]),
                    "volume": int(float(r[fields["TtlTradgVol"]])),
                    "value": float(r[fields["TtlTrfVal"]])})
        except (KeyError, ValueError, TypeError):
            continue
    return rows


def _fetch_day(dest: Path, d: dt.date) -> str:
    day_csv = dest / f"{d.isoformat()}.csv"
    marker = dest / f"{d.isoformat()}.none"
    if day_csv.exists() or marker.exists():
        return "cached"
    urls = ([_new_url(d), _old_url(d)] if d >= NEW_FORMAT_FROM
            else [_old_url(d), _new_url(d)])
    data = _get(urls[0]) or _get(urls[1])
    if data is None:
        marker.write_text("")             # holiday — never re-asked
        return "holiday"
    rows = _parse(data, d)
    tmp = day_csv.with_suffix(".tmp")
    with open(tmp, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "symbol", "date", "open", "high", "low", "close",
            "volume", "value"])
        w.writeheader()
        w.writerows(rows)
    tmp.rename(day_csv)
    return "fetched"


def cmd_download(args) -> None:
    from concurrent.futures import ThreadPoolExecutor
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    d = dt.date.fromisoformat(args.start)
    end = dt.date.fromisoformat(args.end)
    days = []
    while d <= end:
        if d.weekday() < 5:
            days.append(d)
        d += dt.timedelta(days=1)
    counts = {"fetched": 0, "holiday": 0, "cached": 0}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for i, res in enumerate(ex.map(lambda x: _fetch_day(dest, x),
                                       days), 1):
            counts[res] += 1
            if i % 200 == 0:
                print(f"[bhav {i}/{len(days)}] {counts} "
                      f"({time.time() - t0:.0f}s)",
                      file=sys.stderr, flush=True)
    print(f"done: {counts}", file=sys.stderr)


# ------------------------------------------------------------------ build

def _load_days(dest: Path, start: str, end: str) -> list[Path]:
    return sorted(p for p in dest.glob("*.csv")
                  if start <= p.stem <= end)


# ----------------------------------------- ETFs and funds: not stocks

# The skill picks STOCKS — an ETF has no earnings power, no conference
# calls, and a liquid fund is cash wearing a costume. NSE lists ETFs in
# the same EQ series as equities, so they are excluded by name:
# conservative generic tokens plus an explicit roster, with an explicit
# whitelist for real companies whose names merely look fund-like.
FUND_TOKENS = ("ETF", "BEES", "LIQUID", "GILT", "GSEC", "NIFTY",
               "SENSEX", "MOM50", "MOM100", "MON100", "MOM30",
               "LOWVOL", "NV20", "QUAL30", "ALPHL", "EQUAL")
FUND_EXACT = {
    "ICICIB22", "MAFANG", "MASPTOP50", "MAHKTECH", "CPSEETF",
    "GOLD1", "SILVER1", "EGOLD", "ESILVER", "GOLDCASE", "GOLDSHARE",
    "QGOLDHALF", "GOLDADD", "SILVERADD", "AXISGOLD", "AXISILVER",
    "GOLDAXIS", "HDFCGOLD", "HDFCSILVER", "ICICIGOLD", "ICICISILVE",
    "KOTAKGOLD", "KOTAKSILVE", "SBIGOLD", "SBISILVER", "SETFGOLD",
    "BSLGOLDETF", "IDBIGOLD", "TATAGOLD", "TATSILV", "GOLDIETF",
    "SILVERIETF", "GOLDTECH", "UTIGOLDETF", "LIQUIDPLUS", "LIQUID1",
    "LIQUIDCASE", "CASHIETF", "HDFCMFGETF", "ABSLBANETF", "AUTOBEES",
    "BANKNIFTY1", "MID150", "TOP100", "MOGSEC", "LICNFNHGP",
}
NOT_FUNDS = {"SKYGOLD", "GOLDIAM", "DECNGOLD", "SILVERTUC", "MANAKSILV",
             "SILVERLINE", "GOLDENTOBC", "ALPHAGEO", "GOLDKART"}


def is_etf(symbol: str) -> bool:
    """True for ETF/fund instruments that must never enter the buy
    universe. Explicit whitelist beats every pattern."""
    s = symbol.upper()
    if s in NOT_FUNDS:
        return False
    if s in FUND_EXACT:
        return True
    if s.startswith("SETF") or s.startswith("EBBETF") \
            or s.startswith("BBETF") or s.startswith("BBNPP"):
        return True
    return any(tok in s for tok in FUND_TOKENS)


# ------------------------------------------- rolling membership (PIT)

ENTER_RANK = 750             # a stock ENTERS the radar at this rank …
EXIT_RANK = 900              # … and leaves only past this for a full
                             # month — hysteresis, no flapping
IPO_SEASONING_DAYS = 92      # a new listing stays OFF the radar for its
                             # first three months — no IPO-pop chasing;
                             # from month four it competes like any stock

# Official NiftyTotalMarket monthly constituent lists, WHEN THEY EXIST:
# drop a CSV named <YYYY-MM>.csv with an nse_symbol (or symbol) column
# into this folder and that month's membership uses it verbatim (minus
# ETFs) instead of the bhavcopy turnover proxy. The index only launched
# in October 2021 and NSE publishes no public archive of historical
# monthly membership, so this stays a hook: official first, proxy as
# the fallback — never today's list projected into the past.
OFFICIAL_DIR = Path(__file__).resolve().parents[3] \
    / "NiftyTotalMarket" / "constituents_history"


def official_members(month: str) -> set[str] | None:
    p = OFFICIAL_DIR / f"{month}.csv"
    if not p.exists():
        return None
    out = set()
    with open(p) as fh:
        for r in csv.DictReader(fh):
            sym = (r.get("nse_symbol") or r.get("symbol") or "").strip()
            if sym:
                out.add(sym)
    return out or None


def next_month(month: str) -> str:
    y, m = int(month[:4]), int(month[5:7])
    return f"{y + (m == 12)}-{(m % 12) + 1:02d}"


def rolling_membership(month_ranks: dict[str, dict[str, int]],
                       first_month: str, last_month: str,
                       enter: int = ENTER_RANK,
                       exit_: int = EXIT_RANK,
                       eligible: dict[str, str] | None = None
                       ) -> dict[str, dict]:
    """month -> {"members": set, "entered": set, "left": set}.

    A month's membership is decided ENTIRELY from the TRAILING month's
    turnover ranks — nothing later can influence it, so there is no
    lookahead. New names (IPOs, emerging small-caps) enter the first
    month they rank inside `enter`; an incumbent stays until it has
    spent a full month ranked past `exit_` (or stopped trading).
    When an OFFICIAL NiftyTotalMarket list exists for a month
    (official_members), it is used verbatim instead of the proxy.
    ETFs and funds are excluded in every case — stocks only.
    `eligible` (symbol -> first eligible month) is the IPO seasoning
    gate: a new listing cannot enter membership in any earlier month,
    on either path."""
    out: dict[str, dict] = {}
    members: set[str] = set()
    month = first_month
    while month <= last_month:
        def seasoned(s):
            return eligible is None or eligible.get(s, "") <= month

        official = official_members(month)
        if official is not None:
            new_members = {s for s in official
                           if not is_etf(s) and seasoned(s)}
            out[month] = {"members": new_members,
                          "entered": new_members - members,
                          "left": members - new_members,
                          "source": "official"}
            members = new_members
            month = next_month(month)
            continue
        prev = {y: m for y, m in month_ranks.items() if y < month}
        if not prev:
            raise ValueError(f"no trailing ranks before {month}")
        ranks = {s: r for s, r in prev[max(prev)].items()
                 if not is_etf(s) and seasoned(s)}
        fresh = {s for s, r in ranks.items() if r <= enter}
        stay = {s for s in members if ranks.get(s, 10 ** 9) <= exit_}
        new_members = fresh | stay
        out[month] = {"members": new_members,
                      "entered": new_members - members,
                      "left": members - new_members,
                      "source": "proxy"}
        members = new_members
        month = next_month(month)
    return out


def first_seen_dates(dest: Path) -> dict[str, str]:
    """Each symbol's FIRST trading day across the ENTIRE bhavcopy
    store — the listing date as the exchange records it (a symbol
    already trading at the store's first day is simply seasoned)."""
    first: dict[str, str] = {}
    for p in sorted(dest.glob("*.csv")):
        day = p.stem
        for r in csv.DictReader(open(p)):
            s = r["symbol"]
            if s not in first:
                first[s] = day
    return first


def eligible_month(first_day: str,
                   seasoning_days: int = IPO_SEASONING_DAYS) -> str:
    """First month whose 1st falls on/after listing + seasoning."""
    e = (dt.date.fromisoformat(first_day)
         + dt.timedelta(days=seasoning_days))
    m = f"{e.year}-{e.month:02d}"
    return m if e.day == 1 else next_month(m)


def month_turnover_ranks(dest: Path, months: list[str]) -> dict:
    """month -> {symbol: rank} from that month's bhavcopies, rank 1 =
    the month's highest total traded value."""
    out = {}
    for month in months:
        turnover: dict[str, float] = defaultdict(float)
        for p in sorted(dest.glob(f"{month}-*.csv")):
            for r in csv.DictReader(open(p)):
                turnover[r["symbol"]] += float(r["value"])
        ranked = sorted(turnover, key=turnover.get, reverse=True)
        out[month] = {s: i for i, s in enumerate(ranked, 1)}
    return out


def _detect_adjustments(bars: list[dict]) -> list[dict]:
    """Unadjusted history: a split/bonus shows as one overnight cliff.
    Three tests separate it from a crash, each calibrated on real
    events (EICHERMOT 10:1 2020, RELIANCE 1:1 2024, IRCTC 1:5 2021 —
    caught) and real non-events (the Jan-2016 crash gap that
    V-recovered intraday — rejected):

      RATIO        prev close ÷ next open lands on a standard factor;
      PERSISTENCE  the next month's median close STAYS at the rebased
                   level (a crash either recovers or keeps falling —
                   only a changed share count holds the new level);
      VOLUME       the next month's median volume steps up — shares
                   multiplied — with a stricter bar for the small
                   ratios a crash can fake.

    Prices before the ex-date are divided and volumes multiplied."""
    events = []
    vols = [b["volume"] for b in bars]
    for i in range(1, len(bars)):
        prev_c, op = bars[i - 1]["close"], bars[i]["open"]
        if not prev_c or not op:
            continue
        implied = prev_c / op
        ratio = next((r for r in RATIOS
                      if abs(implied - r) / r <= RATIO_TOL), None)
        if ratio is None:
            continue
        if abs(bars[i]["close"] / op - 1) > 0.15:
            continue                      # crash-rebound day, not a split
        before = [v for v in vols[max(0, i - 21):i] if v > 0]
        after_bars = bars[i:i + 21]
        after_v = [b["volume"] for b in after_bars if b["volume"] > 0]
        if len(before) < 5 or len(after_v) < 5:
            continue
        level = (statistics.median(b["close"] for b in after_bars)
                 / prev_c) * ratio        # 1.0 = held the rebased level
        lo, hi = (0.85, 1.18) if ratio < 2 else (0.75, 1.30)
        if not lo <= level <= hi:
            continue
        vr = statistics.median(after_v) / statistics.median(before)
        if vr < (1.5 if ratio < 2 else 1.15):
            continue
        events.append({"index": i, "date": bars[i]["date"],
                       "ratio": ratio, "implied": round(implied, 3),
                       "volume_step": round(vr, 2),
                       "level_hold": round(level, 3)})
    return events


def cmd_build(args) -> None:
    dest = Path(args.dest)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    if args.rolling:
        # ---- monthly point-in-time membership, trailing data only
        months, m = [], args.start[:7]
        while m <= args.end[:7]:
            months.append(m)
            m = next_month(m)
        print(f"ranking {len(months)} months of turnover…",
              file=sys.stderr)
        ranks = month_turnover_ranks(dest, months)
        print("scanning listing dates for the IPO seasoning gate…",
              file=sys.stderr)
        first = first_seen_dates(dest)
        elig = {s: eligible_month(d) for s, d in first.items()}
        memb = rolling_membership(ranks, args.rolling, args.end[:7],
                                  enter=args.top, exit_=args.exit_rank,
                                  eligible=elig)
        keep = set().union(*(v["members"] for v in memb.values()))
        with open(out / "_membership_long.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["month", "symbol"])
            for month in sorted(memb):
                for s in sorted(memb[month]["members"]):
                    w.writerow([month, s])
        entered = sum(len(v["entered"]) for v in list(memb.values())[1:])
        left = sum(len(v["left"]) for v in memb.values())
        first = memb[args.rolling]["members"]
        trail = max(y for y in ranks if y < args.rolling)
        with open(out / "constituents_asof.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["rank", "symbol", "trailing_month"])
            for s in sorted(first, key=lambda x: ranks[trail].get(x, 0)):
                w.writerow([ranks[trail].get(s, ""), s, trail])
        universe = sorted(keep)
        print(f"rolling membership {args.rolling} → {args.end[:7]}: "
              f"{len(first)} at the start, {entered} admitted along the "
              f"way, {left} dropped (exit past rank {args.exit_rank}); "
              f"{len(keep)} symbols ever on the radar", file=sys.stderr)
    else:
        asof_days = sorted(p for p in dest.glob(f"{args.asof}-*.csv"))
        if not asof_days:
            sys.exit(f"no bhavcopies for as-of month {args.asof} in {dest}")
        turnover: dict[str, float] = defaultdict(float)
        for p in asof_days:
            for r in csv.DictReader(open(p)):
                turnover[r["symbol"]] += float(r["value"])
        ranked = sorted(turnover, key=turnover.get, reverse=True)
        universe = ranked[:args.top]
        with open(out / "constituents_asof.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["rank", "symbol", "asof_month_traded_value"])
            for i, s in enumerate(universe, 1):
                w.writerow([i, s, round(turnover[s], 2)])
        print(f"universe: top {len(universe)} of {len(ranked)} EQ "
              f"symbols trading in {args.asof}, by that month's traded "
              f"value", file=sys.stderr)
        keep = set(universe)
    by_sym: dict[str, list[dict]] = defaultdict(list)
    for p in _load_days(dest, args.start, args.end):
        for r in csv.DictReader(open(p)):
            if r["symbol"] in keep:
                by_sym[r["symbol"]].append({
                    "symbol": r["symbol"], "date": r["date"],
                    "open": float(r["open"]), "high": float(r["high"]),
                    "low": float(r["low"]), "close": float(r["close"]),
                    "volume": int(r["volume"])})

    adjustments = []
    for sym, bars in by_sym.items():
        bars.sort(key=lambda b: b["date"])
        for ev in _detect_adjustments(bars):
            for b in bars[:ev["index"]]:
                for k in ("open", "high", "low", "close"):
                    b[k] = round(b[k] / ev["ratio"], 4)
                b["volume"] = int(b["volume"] * ev["ratio"])
            adjustments.append({"symbol": sym, **ev})

    daily_path = out / "_all_daily_long.csv"
    with open(daily_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "symbol", "date", "open", "high", "low", "close", "volume"])
        w.writeheader()
        for sym in sorted(by_sym):
            w.writerows(by_sym[sym])
    if daily_path.stat().st_size > 90_000_000:
        import gzip
        import shutil
        with open(daily_path, "rb") as src, \
                gzip.open(f"{daily_path}.gz", "wb") as dst:
            shutil.copyfileobj(src, dst)
        daily_path.unlink()
        print("daily archive gzipped (over 90MB plain)", file=sys.stderr)
    with open(out / "_adjustments.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "symbol", "index", "date", "ratio", "implied", "volume_step", "level_hold"])
        w.writeheader()
        w.writerows(adjustments)
    (out / "_fetched_at.txt").write_text(
        dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        + "\n")
    with open(out / "_fetch_log.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["symbol", "status", "days", "note"])
        for s in universe:
            n = len(by_sym.get(s, []))
            w.writerow([s, "ok" if n >= 20 else "thin", n,
                        "" if n >= 20 else "under 20 bars in window"])
    print(f"archive: {len(by_sym)} symbols, "
          f"{sum(len(v) for v in by_sym.values())} bars, "
          f"{len(adjustments)} corporate-action adjustments "
          f"(all listed in _adjustments.csv)", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("download")
    d.add_argument("--start", required=True)
    d.add_argument("--end", required=True)
    d.add_argument("--dest", required=True)
    d.add_argument("--sleep", type=float, default=0.25)
    d.add_argument("--workers", type=int, default=6)
    b = sub.add_parser("build")
    b.add_argument("--asof", default=None, help="universe month YYYY-MM "
                   "(fixed-cohort mode)")
    b.add_argument("--rolling", default=None, metavar="YYYY-MM",
                   help="first SCREEN month — monthly PIT membership: "
                   "top N by the trailing month's turnover, exit past "
                   "--exit-rank, no lookahead")
    b.add_argument("--exit-rank", type=int, default=EXIT_RANK)
    b.add_argument("--top", type=int, default=750)
    b.add_argument("--start", required=True)
    b.add_argument("--end", required=True)
    b.add_argument("--dest", required=True)
    b.add_argument("--out", required=True)
    args = ap.parse_args()
    if args.cmd == "download":
        cmd_download(args)
    else:
        cmd_build(args)


if __name__ == "__main__":
    main()
