"""
Tests for the DarvasSkill — the mechanics on synthetic series (including
the method's own worked examples), and validation of the fetched archive
when one is present.

  python3 -m pytest test_skill.py -q        (from DarvasSkill/scripts/)
"""

import csv
import datetime as dt
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import charts as CH        # noqa: E402
import darvas as DV        # noqa: E402
import earnings as EP      # noqa: E402
import fetch_data as FD    # noqa: E402


# ------------------------------------------------------ weekly aggregation

def _day(date, o, h, l, c, v, sym="TEST"):
    return {"symbol": sym, "date": date, "open": o, "high": h,
            "low": l, "close": c, "volume": v}


def test_weeks_aggregate_mon_to_fri():
    daily = [
        _day("2026-08-31", 10, 12, 9, 11, 100),   # Mon
        _day("2026-09-02", 11, 13, 10, 12, 150),  # Wed
        _day("2026-09-04", 12, 15, 11, 14, 200),  # Fri
        _day("2026-09-07", 14, 16, 13, 15, 300),  # next Mon
    ]
    weeks = FD.aggregate_weeks(daily, today=dt.date(2026, 9, 20))
    assert len(weeks) == 2
    w = weeks[0]
    assert w["week_start"] == "2026-08-31"
    assert w["volume"] == 450                      # summed across the week
    assert w["high"] == 15 and w["low"] == 9       # extremes of the week
    assert w["open"] == 10 and w["close"] == 14    # first open, last close
    assert w["complete"] is True


def test_the_running_week_is_flagged_incomplete_until_the_weekend():
    daily = [_day("2026-09-07", 10, 11, 9, 10, 100),
             _day("2026-09-09", 10, 11, 9, 10, 100)]
    # Wednesday of the same ISO week: not complete
    w = FD.aggregate_weeks(daily, today=dt.date(2026, 9, 9))
    assert w[-1]["complete"] is False
    # Saturday: the trading week is over
    w = FD.aggregate_weeks(daily, today=dt.date(2026, 9, 12))
    assert w[-1]["complete"] is True


# --------------------------------------------------------- volume trigger

def _weeks(vols, closes):
    return [{"week_start": f"2026-{6 + i // 4:02d}-{1 + (i % 4) * 7:02d}",
             "open": c, "high": c, "low": c, "close": c, "volume": v}
            for i, (v, c) in enumerate(zip(vols, closes))]


def test_volume_trigger_flags_a_multifold_surge_on_a_price_rise():
    vols = [100_000] * 12 + [400_000]
    closes = [50] * 12 + [54]
    sig = DV.volume_signal(_weeks(vols, closes))
    assert sig["qualifies"] is True
    assert sig["volume_multiple"] == pytest.approx(4.0)
    assert sig["tier"] == "multifold"
    assert sig["price_change_pct"] == pytest.approx(8.0)
    assert sig["last_week_volume"] == 400_000
    assert sig["baseline_avg_volume"] == 100_000


def test_a_surge_on_a_falling_price_never_qualifies():
    """Volume without price appreciation is distribution, not Darvas."""
    vols = [100_000] * 12 + [500_000]
    closes = [50] * 12 + [46]
    sig = DV.volume_signal(_weeks(vols, closes))
    assert sig["qualifies"] is False
    assert sig["volume_multiple"] == pytest.approx(5.0)


def test_a_price_rise_on_normal_volume_never_qualifies():
    vols = [100_000] * 13
    closes = [50] * 12 + [55]
    sig = DV.volume_signal(_weeks(vols, closes))
    assert sig["qualifies"] is False


def test_too_little_history_is_not_judged():
    assert DV.volume_signal(_weeks([100] * 4, [50] * 4)) is None


def test_scan_ranks_qualifiers_by_multiple_in_order():
    weekly = {
        "SLOW": _weeks([100_000] * 13, [50] * 13),
        "GOOD": _weeks([100_000] * 12 + [250_000], [50] * 12 + [53]),
        "BEST": _weeks([100_000] * 12 + [900_000], [50] * 12 + [55]),
    }
    scan = DV.scan_universe(weekly)
    assert [s["symbol"] for s in scan[:2]] == ["BEST", "GOOD"]
    assert scan[0]["volume_multiple"] > scan[1]["volume_multiple"]
    assert scan[-1]["symbol"] == "SLOW" and not scan[-1]["qualifies"]


# -------------------------------------------------------------- box theory

def _bars(seq):
    """[(high, low, close)] -> daily rows with synthetic dates."""
    base = dt.date(2026, 1, 1)
    out = []
    for i, (h, l, c) in enumerate(seq):
        out.append({"date": (base + dt.timedelta(days=i)).isoformat(),
                    "high": float(h), "low": float(l), "close": float(c),
                    "volume": 1000})
    return out


def test_the_50_55_box_from_the_method_description():
    """A stock 'moving in the 50-55 range' seals exactly that box."""
    seq = ([(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)]
           + [(53, 50, 52), (54, 51, 53), (54, 51, 52), (54, 51, 53)])
    st = DV.find_boxes(_bars(seq))
    assert st["state"] == "IN_BOX"
    box = st["current"]
    assert box["top"] == 55 and box["bottom"] == 50
    assert box["range_pct"] == pytest.approx(10.0)


def test_moving_up_to_the_56_62_box_is_an_upward_break_then_a_new_box():
    """The description's own progression: 50-55, then up into 56-62."""
    seq = (
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(58, 54, 57)]                       # close above 55 — breaks up
        + [(62, 57, 60)]                       # new high 62
        + [(61, 57, 59), (60, 56, 58), (61, 57, 60)]   # 62 stands 3 days
        + [(60, 56, 58), (61, 57, 59), (60, 57, 59)]   # 56 stands 3 days
    )
    st = DV.find_boxes(_bars(seq))
    boxes = st["boxes"]
    assert boxes[0]["top"] == 55 and boxes[0]["bottom"] == 50
    assert boxes[0]["outcome"] == "up"
    assert st["current"]["top"] == 62 and st["current"]["bottom"] == 56
    assert st["state"] == "IN_BOX"


def test_dropping_below_the_box_bottom_is_the_red_flag():
    """'…drops below 50, like to 48 — it is a red flag.'"""
    seq = ([(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
           + [(51, 47, 48)])                   # close 48 < bottom 50
    st = DV.find_boxes(_bars(seq))
    assert st["boxes"][0]["outcome"] == "down"
    assert st["state"] == "BREAKDOWN"


def test_each_stock_gets_its_own_box_height():
    tight = DV.find_boxes(_bars(
        [(105, 102, 104)] + [(104, 100, 102), (103, 100, 101),
                             (104, 101, 103)] * 2))
    wide = DV.find_boxes(_bars(
        [(85, 74, 80)] + [(84, 70, 75), (82, 70, 72), (83, 71, 78)] * 2))
    assert tight["current"]["range_pct"] == pytest.approx(5.0)
    assert wide["current"]["range_pct"] == pytest.approx(21.43, abs=0.01)


# -------------------------------------------------------------- stop losses

def test_stop_loss_matches_the_50_55_worked_example():
    assert DV.stop_loss({"top": 55, "bottom": 50}) == pytest.approx(48.5)


def test_stop_loss_matches_the_70_85_worked_example():
    assert DV.stop_loss({"top": 85, "bottom": 70}) == pytest.approx(65.5)


def test_ledger_ratchets_stops_up_never_down(tmp_path):
    path = tmp_path / "_positions.csv"
    DV.update_ledger(path, [{"symbol": "AAA", "action": "BUY",
                             "box_bottom": 50, "box_top": 55,
                             "stop_loss": 48.5, "last_close": 56}],
                     today="2026-09-05")
    # the stock seals a higher box: stop moves UP
    rows = DV.update_ledger(path, [{"symbol": "AAA", "action": "ACCUMULATE",
                                    "box_bottom": 56, "box_top": 62,
                                    "stop_loss": DV.stop_loss(
                                        {"top": 62, "bottom": 56}),
                                    "last_close": 60}],
                            today="2026-09-12")
    assert float(rows[0]["stop_loss"]) == pytest.approx(54.2)
    assert rows[0]["first_flagged"] == "2026-09-05"
    # a LOWER computed stop must never lower the standing one
    rows = DV.update_ledger(path, [{"symbol": "AAA", "action": "WATCH",
                                    "box_bottom": 50, "box_top": 55,
                                    "stop_loss": 48.5, "last_close": 54}],
                            today="2026-09-19")
    assert float(rows[0]["stop_loss"]) == pytest.approx(54.2)


def test_ledger_marks_a_breakdown_as_exit(tmp_path):
    path = tmp_path / "_positions.csv"
    DV.update_ledger(path, [{"symbol": "BBB", "action": "BUY",
                             "box_bottom": 50, "box_top": 55,
                             "stop_loss": 48.5, "last_close": 56}])
    rows = DV.update_ledger(path, [{"symbol": "BBB", "action": "SELL",
                                    "box_bottom": 50, "box_top": 55,
                                    "last_close": 47}])
    assert rows[0]["action"] == "SELL" and rows[0]["stop_loss"] == ""


# ---------------------------------------------------------- recommendations

def test_breakout_is_a_buy_and_breakdown_is_a_sell():
    up = DV.find_boxes(_bars(
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(58, 54, 57)]))
    assert DV.recommend(up, {})["action"] == "BUY"
    down = DV.find_boxes(_bars(
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(51, 47, 48)]))
    r = DV.recommend(down, {})
    assert r["action"] == "SELL" and "red" in r["why"]


def test_holding_the_higher_box_is_accumulate():
    seq = (
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(58, 54, 57)] + [(62, 57, 60)]
        + [(61, 57, 59), (60, 56, 58), (61, 57, 60)]
        + [(60, 56, 58), (61, 57, 59), (60, 57, 59)]
    )
    r = DV.recommend(DV.find_boxes(_bars(seq)), {})
    assert r["action"] == "ACCUMULATE"
    assert r["stop_loss"] == pytest.approx(54.2)   # 56 − 0.3×6


def test_in_box_with_no_prior_break_is_watch_with_a_buy_point():
    st = DV.find_boxes(_bars(
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2))
    r = DV.recommend(st, {})
    assert r["action"] == "WATCH" and r["buy_above"] == 55


# ------------------------------------------------------------ earnings power

def test_earnings_power_reads_the_stored_statements():
    p = EP.earnings_power("PIDILITIND")
    assert p["verdict"] in ("RISING", "FLAT", "FALLING")
    assert p["ebitda"] and p["pat"]
    assert p["pat_margin_pct"], "PAT margin must be derived from Sales"


def test_lenders_fall_back_to_financing_lines():
    p = EP.earnings_power("HDFCBANK")
    assert p["verdict"] != "NO DATA"
    assert p["lender_lines"] is True


def test_new_age_read_is_honest_without_ai():
    v = EP.new_age_verdict("PIDILITIND", allow_ai=False)
    assert v["new_age"] in ("yes", "entering", "no", "not assessed")
    if v["status"] == "ai_unavailable":
        assert v["new_age"] == "not assessed"


# ------------------------------------------------------------------- charts

def test_weekly_chart_carries_the_exact_numbers():
    weeks = _weeks([100_000] * 12 + [400_000], [50] * 12 + [54])
    ch = CH.weekly_chart(weeks)
    assert "4.00 L" in ch and "◀ trigger week" in ch
    assert "+8.0%" in ch


def test_box_picture_shows_edges_stop_and_buy_point():
    st = DV.find_boxes(_bars(
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2))
    rec = DV.recommend(st, {})
    pic = CH.box_picture(st, rec)
    assert "55.00 ─ top" in pic and "50.00 ─ bottom" in pic
    assert "48.50 ─ stop loss" in pic
    assert "buy on a close above" in pic


# ------------------------------------------- the fetched archive, validated

ARCHIVE = FD.OUT_DIR / "_all_weekly_long.csv"


@pytest.mark.skipif(not ARCHIVE.exists(),
                    reason="no fetched archive in this checkout yet")
def test_fetched_archive_is_sane():
    syms = set()
    bad = []
    with open(ARCHIVE) as fh:
        for r in csv.DictReader(fh):
            syms.add(r["symbol"])
            if int(r["volume"]) < 0:
                bad.append((r["symbol"], "negative volume"))
            if not (0 < float(r["low"]) <= float(r["high"])):
                bad.append((r["symbol"], "low/high inverted"))
            if not (float(r["low"]) - 1e-6 <= float(r["close"])
                    <= float(r["high"]) + 1e-6):
                bad.append((r["symbol"], "close outside the week's range"))
    assert not bad, f"{len(bad)} bad rows: {bad[:5]}"
    assert len(syms) >= 700, f"only {len(syms)} symbols in the archive"


@pytest.mark.skipif(not ARCHIVE.exists(),
                    reason="no fetched archive in this checkout yet")
def test_every_scan_row_traces_to_the_archive():
    weekly = DV.load_weekly()
    scan = DV.scan_universe(weekly)
    q = [s for s in scan if s["qualifies"]]
    assert q, "a 742-stock universe with zero volume surges is implausible"
    for s in q[:10]:
        weeks = weekly[s["symbol"]]
        assert weeks[-1]["volume"] == s["last_week_volume"]
        base = [w["volume"] for w in weeks[-(DV.BASELINE_WEEKS + 1):-1]]
        assert round(sum(base) / len(base)) == s["baseline_avg_volume"]
        assert s["volume_multiple"] == pytest.approx(
            s["last_week_volume"] / (sum(base) / len(base)), abs=0.01)


def test_a_recovered_breakdown_is_watched_not_sold():
    """The AWFIS shape from the first live run: box, breakdown, then a
    violent close back ABOVE the old box top on the surge. A stale
    breakdown must not print as SELL at a price above the old box."""
    seq = ([(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
           + [(51, 47, 48), (50, 47, 49), (49, 46, 47)]   # breakdown, drift
           + [(58, 48, 57)])                              # recovery close 57
    st = DV.find_boxes(_bars(seq))
    assert st["state"] == "RECOVERY"
    r = DV.recommend(st, {})
    assert r["action"] == "WATCH"
    assert "recovery" in r["why"]
    assert "stop_loss" not in r, "a stale box must not supply a stop"


def test_a_standing_breakdown_still_sells():
    seq = ([(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
           + [(51, 47, 48), (50, 47, 49)])
    st = DV.find_boxes(_bars(seq))
    assert st["state"] == "BREAKDOWN"
    assert DV.recommend(st, {})["action"] == "SELL"
