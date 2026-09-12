"""
fetch_data.py — fresh weekly volume + price data for the whole universe.

Darvas's first trigger is a volume surge, and a surge is only visible in
CURRENT data — so this fetcher runs every time the skill runs (step 1.6
of the method). For every NiftyTotalMarket symbol it pulls the last six
months of DAILY bars from Yahoo Finance (SYMBOL.NS), keeps the daily rows
for box detection, and aggregates them into ISO weeks for the volume
trigger — a "week" is Monday-to-Friday, and only COMPLETED weeks count
(the running week would understate volume and fake a decline).

Everything lands beside the other statement archives, as required:

    IndividualStockAnalysis/India/VolumeAndPricing/NiftyTotalMarket/
        _all_daily_long.csv    symbol, date, open, high, low, close, volume
        _all_weekly_long.csv   symbol, week_start, open, high, low, close,
                               volume, complete
        _fetch_log.csv         per-symbol status of the latest fetch
        _fetched_at.txt        UTC timestamp of the latest fetch

Failures are recorded, never papered over: a symbol Yahoo does not serve
appears in the log with its reason and is simply absent from the scan.
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDIA = HERE.parent.parent.parent
UNIVERSE = "NiftyTotalMarket"
OUT_DIR = INDIA / "VolumeAndPricing" / UNIVERSE
CONSTITUENTS = INDIA / UNIVERSE / "niftytotalmarket_constituents.csv"

RANGE = "6mo"          # 3 months of completed weeks for the trigger,
INTERVAL = "1d"        # with headroom for box detection on daily bars
RETRIES = 3
UA = "Mozilla/5.0 (X11; Linux x86_64)"


def universe_symbols() -> list[str]:
    with open(CONSTITUENTS) as fh:
        return [row["nse_symbol"] for row in csv.DictReader(fh)]


def _yahoo_url(sym: str) -> str:
    return (f"https://query1.finance.yahoo.com/v8/finance/chart/"
            f"{urllib.parse.quote(sym, safe='')}.NS"
            f"?range={RANGE}&interval={INTERVAL}")


def fetch_symbol(sym: str) -> list[dict]:
    """Daily bars for one symbol, oldest first. Raises on failure."""
    last_err = None
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(_yahoo_url(sym),
                                         headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.load(resp)
            result = (data.get("chart", {}).get("result") or [None])[0]
            if not result:
                raise ValueError(str(data.get("chart", {}).get("error"))[:120])
            ts = result.get("timestamp") or []
            q = result["indicators"]["quote"][0]
            rows = []
            for i, t in enumerate(ts):
                c = q["close"][i]
                v = q["volume"][i]
                if c is None or v is None:
                    continue          # holiday/halted rows carry nulls
                rows.append({
                    "symbol": sym,
                    "date": dt.date.fromtimestamp(t).isoformat(),
                    "open": round(q["open"][i], 4) if q["open"][i] else None,
                    "high": round(q["high"][i], 4) if q["high"][i] else None,
                    "low": round(q["low"][i], 4) if q["low"][i] else None,
                    "close": round(c, 4),
                    "volume": int(v),
                })
            if len(rows) < 20:
                raise ValueError(f"only {len(rows)} usable daily bars")
            return rows
        except Exception as e:            # noqa: BLE001 — retried, then logged
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(str(last_err)[:160])


def week_key(date: dt.date) -> tuple[int, int]:
    iso = date.isocalendar()
    return (iso[0], iso[1])


def week_start(date: dt.date) -> dt.date:
    return date - dt.timedelta(days=date.weekday())


def aggregate_weeks(daily: list[dict],
                    today: dt.date | None = None) -> list[dict]:
    """Daily bars (one symbol, oldest first) -> ISO weeks, oldest first.

    A week is `complete` when it is not the running calendar week — or
    when it IS the current week but the weekend has arrived (Saturday
    onward the trading week is over). The trigger only reads complete
    weeks; the running one is stored for transparency, flagged false."""
    today = today or dt.date.today()
    weeks: dict[tuple, dict] = {}
    for row in daily:
        d = dt.date.fromisoformat(row["date"])
        k = week_key(d)
        w = weeks.get(k)
        if w is None:
            weeks[k] = w = {"symbol": row["symbol"],
                            "week_start": week_start(d).isoformat(),
                            "open": row["open"], "high": row["high"],
                            "low": row["low"], "close": row["close"],
                            "volume": 0}
        w["high"] = max(x for x in (w["high"], row["high"]) if x is not None)
        w["low"] = min(x for x in (w["low"], row["low"]) if x is not None)
        w["close"] = row["close"]
        w["volume"] += row["volume"]
    out = [weeks[k] for k in sorted(weeks)]
    cur = week_key(today)
    for k, w in zip(sorted(weeks), out):
        w["complete"] = (k != cur) or today.weekday() >= 5
    return out


def fetch_universe(symbols: list[str] | None = None,
                   sleep: float = 0.12,
                   progress_every: int = 50) -> dict:
    """Fetch everything, write the archive, return a summary dict."""
    symbols = symbols or universe_symbols()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    daily_rows: list[dict] = []
    weekly_rows: list[dict] = []
    log: list[dict] = []
    ok = failed = 0
    t0 = time.time()
    for i, sym in enumerate(symbols, 1):
        try:
            rows = fetch_symbol(sym)
            daily_rows.extend(rows)
            weekly_rows.extend(aggregate_weeks(rows))
            log.append({"symbol": sym, "status": "ok",
                        "days": len(rows), "note": ""})
            ok += 1
        except Exception as e:            # noqa: BLE001
            log.append({"symbol": sym, "status": "failed",
                        "days": 0, "note": str(e)[:150]})
            failed += 1
        if progress_every and i % progress_every == 0:
            print(f"[fetch {i}/{len(symbols)}] ok={ok} failed={failed} "
                  f"({time.time() - t0:.0f}s)", file=sys.stderr)
        time.sleep(sleep)

    _write_csv(OUT_DIR / "_all_daily_long.csv", daily_rows,
               ["symbol", "date", "open", "high", "low", "close", "volume"])
    _write_csv(OUT_DIR / "_all_weekly_long.csv", weekly_rows,
               ["symbol", "week_start", "open", "high", "low", "close",
                "volume", "complete"])
    _write_csv(OUT_DIR / "_fetch_log.csv", log,
               ["symbol", "status", "days", "note"])
    stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    (OUT_DIR / "_fetched_at.txt").write_text(stamp + "\n")
    return {"ok": ok, "failed": failed, "symbols": len(symbols),
            "daily_rows": len(daily_rows), "weekly_rows": len(weekly_rows),
            "seconds": round(time.time() - t0), "fetched_at": stamp}


def _write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields)
    w.writeheader()
    for r in rows:
        w.writerow(r)
    path.write_text(buf.getvalue())


if __name__ == "__main__":
    syms = sys.argv[1:] or None
    print(json.dumps(fetch_universe(syms), indent=2))
