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

def _weeks(vols, closes, partial_last=False, last_days=5):
    out = [{"week_start": f"2026-{6 + i // 4:02d}-{1 + (i % 4) * 7:02d}",
            "open": c, "high": c, "low": c, "close": c, "volume": v,
            "days": 5, "complete": True}
           for i, (v, c) in enumerate(zip(vols, closes))]
    if partial_last and out:
        out[-1]["complete"] = False
        out[-1]["days"] = last_days
    return out


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

def test_stop_loss_50_55_now_respects_the_5pct_floor():
    """0.3×height would put the stop at 48.5 — only 3% below the bottom.
    The 5% floor pulls it to 47.5, so ordinary noise inside a shallow box
    cannot churn the position."""
    assert DV.stop_loss({"top": 55, "bottom": 50}) == pytest.approx(47.5)


def test_stop_loss_matches_the_70_85_worked_example():
    """A wide box: 0.3×height (4.5) beats the 5% floor (3.5) — unchanged."""
    assert DV.stop_loss({"top": 85, "bottom": 70}) == pytest.approx(65.5)


def test_stop_loss_is_never_closer_than_5pct_below_the_bottom():
    assert DV.stop_loss({"top": 102, "bottom": 100}) == pytest.approx(95.0)


def test_ledger_ratchets_stops_up_never_down(tmp_path):
    path = tmp_path / "_positions.csv"
    DV.update_ledger(path, [{"symbol": "AAA", "action": "BUY",
                             "box_bottom": 50, "box_top": 55,
                             "stop_loss": 47.5, "last_close": 56}],
                     today="2026-09-05")
    # the stock seals a higher box: stop moves UP
    rows = DV.update_ledger(path, [{"symbol": "AAA", "action": "ACCUMULATE",
                                    "box_bottom": 56, "box_top": 62,
                                    "stop_loss": DV.stop_loss(
                                        {"top": 62, "bottom": 56}),
                                    "last_close": 60}],
                            today="2026-09-12")
    assert float(rows[0]["stop_loss"]) == pytest.approx(53.2)
    assert rows[0]["first_flagged"] == "2026-09-05"
    # a LOWER computed stop must never lower the standing one
    rows = DV.update_ledger(path, [{"symbol": "AAA", "action": "WATCH",
                                    "box_bottom": 50, "box_top": 55,
                                    "stop_loss": 47.5, "last_close": 54}],
                            today="2026-09-19")
    assert float(rows[0]["stop_loss"]) == pytest.approx(53.2)


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

def test_breakout_is_a_buy_and_a_confirmed_breakdown_is_a_sell():
    up = DV.find_boxes(_bars(
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(58, 54, 57)]))
    assert DV.recommend(up, {})["action"] == "BUY"
    # close 47 is through the 47.5 stop — the red flag CONFIRMED
    down = DV.find_boxes(_bars(
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(50, 46.5, 47)]))
    r = DV.recommend(down, {})
    assert r["action"] == "SELL" and "red" in r["why"]


def test_breakdown_inside_the_grace_is_watched_not_sold():
    """Close 48.5: below the 50 bottom (a red flag) but ABOVE the 47.5
    stop — the stabilisation grace holds it instead of churning."""
    down = DV.find_boxes(_bars(
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(51, 48, 48.5)]))
    r = DV.recommend(down, {})
    assert r["action"] == "WATCH"
    assert "grace" in r["why"]
    assert r["stop_loss"] == pytest.approx(47.5)


def test_holding_the_higher_box_is_accumulate():
    seq = (
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(58, 54, 57)] + [(62, 57, 60)]
        + [(61, 57, 59), (60, 56, 58), (61, 57, 60)]
        + [(60, 56, 58), (61, 57, 59), (60, 57, 59)]
    )
    r = DV.recommend(DV.find_boxes(_bars(seq)), {})
    assert r["action"] == "ACCUMULATE"
    assert r["stop_loss"] == pytest.approx(53.2)   # 56 − max(0.3×6, 5%×56)


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
    assert "47.50 ─ stop loss" in pic
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
        prior = [w for w in weeks[:-1] if w["complete"]]
        base = [w["volume"] for w in prior[-DV.BASELINE_WEEKS:]]
        assert round(sum(base) / len(base)) == s["baseline_avg_volume"]
        assert s["raw_volume_multiple"] == pytest.approx(
            s["last_week_volume"] / (sum(base) / len(base)), abs=0.01)
        assert len(s["recent_weeks"]) == 4
        assert s["recent_weeks"][-1]["volume"] == s["last_week_volume"]


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


def test_a_standing_breakdown_through_the_stop_still_sells():
    """Closes at 47 — through the 47.5 stop, past the grace: SELL."""
    seq = ([(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
           + [(50, 46.5, 47), (48, 46.5, 47)])
    st = DV.find_boxes(_bars(seq))
    assert st["state"] == "BREAKDOWN"
    assert DV.recommend(st, {})["action"] == "SELL"


# ------------------------------------------- the latest (partial) week

def test_the_running_week_is_the_week_under_test():
    """The gap the first review caught: a surge happening THIS week must
    be tested now, pro-rated to five days — not ignored until next week."""
    # 12 quiet completed weeks, then 2 days of the running week carrying
    # a full normal week's volume: 1.0x raw = 2.5x pro-rated
    vols = [100_000] * 12 + [100_000]
    closes = [50] * 12 + [53]
    sig = DV.volume_signal(_weeks(vols, closes, partial_last=True,
                                  last_days=2))
    assert sig["partial_week"] is True and sig["days_traded"] == 2
    assert sig["raw_volume_multiple"] == pytest.approx(1.0)
    assert sig["volume_multiple"] == pytest.approx(2.5)
    assert sig["qualifies"] is True
    assert sig["week_start"] == _weeks(vols, closes)[-1]["week_start"]


def test_a_quiet_partial_week_does_not_qualify():
    vols = [100_000] * 12 + [30_000]        # 2 days at normal daily pace
    closes = [50] * 12 + [51]
    sig = DV.volume_signal(_weeks(vols, closes, partial_last=True,
                                  last_days=2))
    assert sig["volume_multiple"] == pytest.approx(0.75)
    assert sig["qualifies"] is False


def test_signal_always_carries_the_last_four_weeks():
    vols = [100_000] * 12 + [400_000]
    closes = [50] * 12 + [54]
    sig = DV.volume_signal(_weeks(vols, closes))
    assert len(sig["recent_weeks"]) == 4
    assert [w["volume"] for w in sig["recent_weeks"]] == \
        [100_000, 100_000, 100_000, 400_000]


def test_incomplete_weeks_never_pollute_the_baseline():
    """A partial week in the middle of history (halt/holiday edge) must
    not drag the average down."""
    weeks = _weeks([100_000] * 13, [50] * 13)
    weeks[5]["complete"] = False
    weeks[5]["volume"] = 1                  # would poison a naive mean
    sig = DV.volume_signal(weeks)
    assert sig["baseline_avg_volume"] == 100_000


def test_weekly_chart_labels_a_partial_trigger_week():
    weeks = _weeks([100_000] * 12 + [200_000], [50] * 12 + [54],
                   partial_last=True, last_days=3)
    ch = CH.weekly_chart(weeks)
    assert "partial: 3 days so far" in ch


# ------------------------------------ monthly trend + the combined picture

def _daily_months(vol_by_month):
    """[(month 1-12, per-day volume)] -> daily rows, ~20 bars per month."""
    out = []
    for m, v in vol_by_month:
        for day in range(1, 21):
            out.append({"date": f"2026-{m:02d}-{day:02d}", "high": 11.0,
                        "low": 9.0, "close": 10.0, "volume": v})
    return out


def test_monthly_volumes_flag_the_running_month():
    months = DV.monthly_volumes(_daily_months([(4, 100), (5, 100),
                                               (6, 100), (7, 100)]))
    assert [m["month"] for m in months] == ["2026-04", "2026-05",
                                            "2026-06", "2026-07"]
    assert months[-1]["complete"] is False and all(
        m["complete"] for m in months[:-1])
    assert months[0]["volume"] == 100 * 20


def test_building_volume_is_called_building():
    months = DV.monthly_volumes(_daily_months(
        [(3, 100), (4, 100), (5, 120), (6, 150), (7, 200), (8, 260),
         (9, 300)]))
    t = DV.monthly_trend(months)
    assert t["verdict"] == "BUILDING"
    assert t["rising_months"] >= 3
    assert "building" in t["why"]


def test_flat_months_before_a_surge_are_spike_only():
    months = DV.monthly_volumes(_daily_months(
        [(3, 100), (4, 100), (5, 100), (6, 100), (7, 100), (8, 100),
         (9, 900)]))                     # the surge sits in the RUNNING month
    t = DV.monthly_trend(months)
    assert t["verdict"] == "SPIKE ONLY"


def test_the_running_month_never_drives_the_trend():
    """A monster running month must not print BUILDING on its own."""
    flat = DV.monthly_trend(DV.monthly_volumes(_daily_months(
        [(4, 100), (5, 100), (6, 100), (7, 100), (8, 100), (9, 9000)])))
    assert flat["verdict"] == "SPIKE ONLY"


def test_price_volume_chart_carries_both_panels_and_exact_numbers():
    weeks = _weeks([100_000] * 12 + [400_000],
                   [50] * 10 + [52, 53, 58])
    ch = CH.price_volume_chart(weeks)
    assert "●" in ch and "█" in ch          # price line AND volume bars
    assert "₹58" in ch                      # top price labelled
    assert "₹50" in ch                      # bottom price labelled
    assert "4.00 L" in ch                   # peak volume labelled
    assert "close ₹58.0" in ch              # the exact latest numbers
    price_part, vol_part = ch.split("┼")
    assert "●" in price_part and "●" not in vol_part
    assert "█" in vol_part and "█" not in price_part


def test_price_volume_chart_labels_a_partial_latest_week():
    weeks = _weeks([100_000] * 12 + [200_000], [50] * 13,
                   partial_last=True, last_days=2)
    assert "partial: 2 days so far" in CH.price_volume_chart(weeks)


def test_box_picture_shows_the_full_ladder():
    seq = (
        [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
        + [(58, 54, 57)] + [(62, 57, 60)]
        + [(61, 57, 59), (60, 56, 58), (61, 57, 60)]
        + [(60, 56, 58), (61, 57, 59), (60, 57, 59)]
        + [(64, 61, 63)] + [(68, 63, 66)]
        + [(67, 63, 65), (66, 62, 64), (67, 63, 66)]
        + [(66, 62, 64), (67, 63, 65), (66, 63, 65)]
    )
    st = DV.find_boxes(_bars(seq))
    assert len(st["boxes"]) >= 3
    pic = CH.box_picture(st, DV.recommend(st, {}))
    for b in st["boxes"]:                   # EVERY sealed box on the ladder
        assert f"{b['top']:,.2f}" in pic


# ------------------------------------------------------------ the backtest

import backtest as BT


def test_backtest_window_url_pins_the_period():
    import datetime as _dt
    url = BT.window_url("PIDILITIND", _dt.date(2025, 6, 1),
                        _dt.date(2026, 3, 31))
    assert "period1=" in url and "period2=" in url and "range=" not in url
    assert "PIDILITIND.NS" in url and "interval=1d" in url


def test_backtest_asof_fiscal_year_cuts_correctly():
    import datetime as _dt
    assert BT.asof_fiscal_year(_dt.date(2026, 3, 31)) == "Mar 2026"
    assert BT.asof_fiscal_year(_dt.date(2026, 3, 30)) == "Mar 2025"
    assert BT.asof_fiscal_year(_dt.date(2025, 12, 31)) == "Mar 2025"
    assert BT.asof_fiscal_year(_dt.date(2026, 6, 1)) == "Mar 2026"


def test_backtest_archive_is_separate_from_the_live_one():
    import datetime as _dt
    d = BT.window_dir(_dt.date(2025, 6, 1), _dt.date(2026, 3, 31))
    assert "VolumeAndPricingBacktest" in str(d)
    assert str(FD.OUT_DIR) not in str(d) or "Backtest" in str(FD.OUT_DIR)


def test_backtest_banner_discloses_the_cuts():
    import datetime as _dt
    b = BT.banner(_dt.date(2025, 6, 1), _dt.date(2026, 3, 31), "Mar 2026")
    assert "as of 2026-03-31" in b
    assert "Mar 2026" in b and "EXCLUDED" in b
    assert "would not all have been published" in b   # the optimism, stated


# ------------------------------------------------- the walk-forward rhythm

import walkforward as WF


def _wf_bars(seq, start="2026-01-05"):
    """[(high, low, close)] -> consecutive WEEKDAY bars (Mon-Fri only)."""
    d = dt.date.fromisoformat(start)
    out = []
    for h, l, c in seq:
        while d.weekday() >= 5:
            d += dt.timedelta(days=1)
        out.append({"date": d.isoformat(), "high": float(h),
                    "low": float(l), "close": float(c)})
        d += dt.timedelta(days=1)
    return out


BOX_5055 = [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2


def test_walkforward_ratchets_the_stop_on_a_new_higher_box():
    seq = (BOX_5055
           + [(58, 54, 57)] + [(62, 57, 60)]
           + [(61, 57, 59), (60, 56, 58), (61, 57, 60)]
           + [(60, 56, 58), (61, 57, 59), (60, 57, 59)]
           + [(61, 58, 60)] * 5)
    bars = _wf_bars(seq)
    r = WF.simulate_position(bars, bars[0]["date"], 54.0, 48.5,
                             bars[-1]["date"])
    assert r["events"], "the higher box must ratchet the stop"
    assert r["final_stop"] == pytest.approx(53.2)      # 56 − max(1.8, 2.8)
    assert all(e["to"] > (e["from"] or 0) for e in r["events"])
    assert r["reason"] == "held through the period"


def test_walkforward_stop_hit_exits_at_the_stop_price():
    seq = BOX_5055 + [(52, 47, 47.5)]      # low 47 pierces the 48.5 stop
    bars = _wf_bars(seq)
    r = WF.simulate_position(bars, bars[0]["date"], 54.0, 48.5,
                             bars[-1]["date"])
    assert r["reason"] == "stop hit"
    assert r["exit_px"] == pytest.approx(48.5)         # at the stop, not the low


def test_walkforward_breakdown_inside_the_grace_is_held_not_sold():
    """Closes drift below the 50 bottom but never touch the 47.5 stop:
    the stabilisation grace holds the position — no more instant weekly
    sells the moment a box floor is closed under."""
    seq = BOX_5055 + [(51, 49.4, 49.5), (50.5, 49.4, 49.6),
                      (50.5, 49.4, 49.5), (50.5, 49.4, 49.6),
                      (50.5, 49.4, 49.5)]
    bars = _wf_bars(seq)
    r = WF.simulate_position(bars, bars[0]["date"], 54.0, 47.5,
                             bars[-1]["date"])
    assert r["reason"] == "held through the period"


def test_walkforward_the_stop_still_ends_a_true_slide():
    seq = BOX_5055 + [(51, 49.4, 49.5), (49.5, 47.2, 47.4)]
    bars = _wf_bars(seq)
    r = WF.simulate_position(bars, bars[0]["date"], 54.0, 47.5,
                             bars[-1]["date"])
    assert r["reason"] == "stop hit" and r["exit_px"] == pytest.approx(47.5)


def test_walkforward_watch_enters_on_the_first_close_above_the_top():
    seq = BOX_5055 + [(55.5, 53, 54.8), (56.5, 54, 56.2), (57, 55, 56.5)]
    bars = _wf_bars(seq)
    hit = WF.watch_entry(bars, bars[0]["date"], 55.0, bars[-1]["date"])
    assert hit is not None and hit["px"] == pytest.approx(56.2)
    assert hit["date"] == bars[len(BOX_5055) + 1]["date"]
    assert WF.watch_entry(bars, bars[0]["date"], 99.0,
                          bars[-1]["date"]) is None


def test_walkforward_refuses_a_mismatched_archive_seam(tmp_path):
    import io
    hdr = "symbol,date,open,high,low,close,volume\n"
    (tmp_path / "_all_daily_long.csv").write_text(
        hdr + "AAA,2026-03-20,10,11,9,100.0,5\n")
    live_dir = tmp_path / "live"
    live_dir.mkdir()
    (live_dir / "_all_daily_long.csv").write_text(
        hdr + "AAA,2026-03-20,10,11,9,50.0,5\n")   # a 2:1 adjustment
    old = DV.DATA_DIR
    DV.DATA_DIR = live_dir
    try:
        with pytest.raises(ValueError, match="corporate action"):
            WF.stitched_bars(tmp_path, ["AAA"])
    finally:
        DV.DATA_DIR = old


# ------------------------------------------------------- re-entry rules

def _vol_bars(seq, start="2026-01-05", base_vol=100_000):
    d = dt.date.fromisoformat(start)
    out = []
    for item in seq:
        h, l, c = item[:3]
        v = item[3] if len(item) > 3 else base_vol
        while d.weekday() >= 5:
            d += dt.timedelta(days=1)
        out.append({"symbol": "T", "date": d.isoformat(), "open": float(c),
                    "high": float(h), "low": float(l), "close": float(c),
                    "volume": v})
        d += dt.timedelta(days=1)
    return out


def test_reentry_needs_BOTH_price_break_and_volume():
    """A breakout on quiet volume must NOT re-enter; the same breakout on
    trigger volume must."""
    quiet = (BOX_5055 * 5                       # long quiet history
             + [(58, 54, 57)])                  # breakout, normal volume
    bars = _vol_bars(quiet)
    assert WF.reentry_ready(bars, len(bars) - 1) is None
    loud = (BOX_5055 * 5
            + [(58, 54, 57, 800_000)])          # breakout on 8x daily volume
    bars = _vol_bars(loud)
    ready = WF.reentry_ready(bars, len(bars) - 1)
    assert ready is not None and ready["state"] == "BREAKOUT"
    assert ready["stop"] == pytest.approx(47.5)


def test_simulate_with_reentry_rebuys_after_a_stopout():
    """Stop-out, drift, then a loud breakout: the second leg must open."""
    seq = (BOX_5055 * 5
           + [(52, 47, 47.5)]                       # leg 1 stopped at 48.5
           + [(50, 47.5, 48.5), (50, 48, 49), (51, 48, 50),
              (51, 48.5, 50), (51, 48.5, 50.5)]     # quiet drift, box seals
           + [(56, 51, 55.5, 900_000)]              # loud break above
           + [(57, 54, 56)] * 3)
    bars = _vol_bars(seq)
    legs = WF.simulate_with_reentry(bars, bars[0]["date"], 54.0, 48.5,
                                    bars[-1]["date"])
    assert len(legs) >= 2, "the stop-out must be followed by a re-entry"
    assert legs[0]["reason"] == "stop hit"
    assert legs[1]["entry_px"] == pytest.approx(55.5)


def test_no_reentry_when_volume_never_returns():
    seq = (BOX_5055 * 5
           + [(52, 47, 47.5)]
           + [(56, 51, 55.5)] + [(57, 54, 56)] * 5)   # breaks, quiet volume
    bars = _vol_bars(seq)
    legs = WF.simulate_with_reentry(bars, bars[0]["date"], 54.0, 48.5,
                                    bars[-1]["date"])
    assert len(legs) == 1, "price alone must never re-enter"


# ---------------------------------- the three-gate qualification (v2)

def _flat_days(n, vol, close=50.0, start="2025-01-06"):
    d = dt.date.fromisoformat(start)
    out = []
    for _ in range(n):
        while d.weekday() >= 5:
            d += dt.timedelta(days=1)
        out.append({"symbol": "T", "date": d.isoformat(), "open": close,
                    "high": close + 1, "low": close - 1, "close": close,
                    "volume": vol})
        d += dt.timedelta(days=1)
    return out


def test_month_vs_year_gate_passes_a_genuinely_louder_month():
    daily = _flat_days(231, 100_000) + _flat_days(21, 250_000,
                                                  start="2025-12-01")
    mv = DV.month_vs_year(daily)
    assert mv["qualifies"] is True
    assert mv["month_vs_year_multiple"] == pytest.approx(2.5)
    assert mv["month_avg_daily"] == 250_000
    assert mv["year_avg_daily"] == 100_000


def test_month_vs_year_gate_fails_a_single_moderate_week():
    """One 3x week inside an otherwise normal month lifts the month to
    (16×100k + 5×300k)/21 ≈ 1.48x — under the 1.5x bar. A lone loud week
    in a sleepy name cannot carry the month gate by itself."""
    daily = (_flat_days(231, 100_000)
             + _flat_days(16, 100_000, start="2025-12-01")
             + _flat_days(5, 300_000, start="2025-12-23"))
    mv = DV.month_vs_year(daily)
    assert mv["qualifies"] is False
    assert mv["month_vs_year_multiple"] == pytest.approx(1.48, abs=0.01)


def test_month_vs_year_needs_a_real_baseline():
    assert DV.month_vs_year(_flat_days(60, 100_000)) is None


def test_ladder_gate_wants_three_rising_boxes():
    def box(bottom, top):
        return {"top": top, "bottom": bottom}
    rising = [box(50, 55), box(56, 62), box(63, 70)]
    assert DV.box_uptrend(rising)["qualifies"] is True
    flat = [box(50, 55), box(49, 54), box(50, 56)]
    assert DV.box_uptrend(flat)["qualifies"] is False
    short = [box(50, 55), box(56, 62)]
    up = DV.box_uptrend(short)
    assert up["qualifies"] is False and "too short" in up["why"]


def test_full_qualifiers_requires_all_three_gates():
    # a stock passing the weekly trigger but with flat yearly volume and
    # no ladder must NOT fully qualify
    daily = _flat_days(252, 100_000)
    scan = [{"symbol": "T", "qualifies": True, "volume_multiple": 3.0,
             "price_change_pct": 5.0}]
    out = DV.full_qualifiers(scan, {"T": daily})
    assert len(out) == 1
    assert out[0]["fully_qualifies"] is False


def test_only_a_genuine_in_box_watch_is_a_buy_instruction():
    in_box = _wf_bars(BOX_5055 * 3)
    assert WF.genuine_watch_buy_above(
        in_box, in_box[-1]["date"]) == pytest.approx(55.0)
    broken_out = _wf_bars(BOX_5055 * 3 + [(58, 54, 57)])
    assert WF.genuine_watch_buy_above(
        broken_out, broken_out[-1]["date"]) is None, \
        "a downgraded BREAKOUT's stale box top must never become a trigger"


# --------------------------------------- the rolling rhythm (rolling.py)

import rolling as RL       # noqa: E402


def _roll_bars(sym, closes, start="2026-01-02", vol=100_000):
    """Consecutive weekday bars, close-driven, open = previous close."""
    d = dt.date.fromisoformat(start)
    out, prev = [], closes[0]
    for c in closes:
        while d.weekday() >= 5:
            d += dt.timedelta(days=1)
        out.append({"symbol": sym, "date": d.isoformat(), "open": prev,
                    "high": max(prev, c) + 0.5, "low": min(prev, c) - 0.5,
                    "close": c, "volume": vol})
        prev = c
        d += dt.timedelta(days=1)
    return out


def test_plan_deployment_slices_the_cash_and_refuses_crumbs():
    # three signals, cash for 2.4 slices: two full slices, then the
    # 0.4-slice remainder is refused (below half a slice)
    assert RL.plan_deployment(24.0, 10.0, 3) == [10.0, 10.0]
    # the remainder IS deployed when it clears half a slice
    assert RL.plan_deployment(26.0, 10.0, 3) == [10.0, 10.0, 6.0]
    # no cash, no entries — and never a negative amount
    assert RL.plan_deployment(0.0, 10.0, 2) == []
    assert RL.plan_deployment(4.9, 10.0, 1) == []


def test_screen_day_refuses_thin_history():
    bars = _roll_bars("T", [50.0] * 30)
    day = dt.date.fromisoformat(bars[-1]["date"])
    assert RL.screen_day(bars, day) is None


def _rolling_world():
    """AAA is seeded and slides through its stop; BBB is flat and waits
    for the injected Friday signal. 2026-01-02 is a Friday."""
    aaa = _roll_bars("AAA", [100.0] * 6 + [98.0, 94.0] + [93.0] * 32)
    bbb = _roll_bars("BBB", [50.0] * 40)
    return {"AAA": aaa, "BBB": bbb}


def test_rolling_redeploys_stop_out_cash_into_the_next_fresh_signal():
    bars_by = _rolling_world()
    signal_friday = "2026-01-16"

    def stub(bars_upto, day):
        if bars_upto[-1]["symbol"] == "BBB" \
                and day.isoformat() == signal_friday:
            return {"action": "BUY", "stop": 45.0,
                    "volume_multiple": 2.0, "month_multiple": 2.0}
        return None

    res = RL.run_rolling(bars_by, [{"symbol": "AAA", "stop": 95.0}],
                         "2026-01-02", bars_by["AAA"][-1]["date"],
                         100.0, lambda s, d: True, screen=stub)
    text = "\n".join(f"{d} {s} {w}" for d, s, w in res["blotter"])
    # the seed took the whole slice, the stop freed ₹95 …
    assert "AAA BUY ₹100.00 at ₹100.00" in text
    assert "AAA SELL ₹95.00 at stop ₹95.00" in text
    # … and the freed cash entered BBB at the NEXT trading day's open,
    # never on the signal Friday itself
    bbb_buy = [b for b in res["blotter"] if b[1] == "BBB" and "BUY" in b[2]]
    assert bbb_buy and bbb_buy[0][0] == "2026-01-19"
    assert "at ₹50.00" in bbb_buy[0][2]
    # cash never went negative anywhere along the curve
    assert all(w["cash"] >= 0 for w in res["equity_curve"])
    # the books balance: everything rides in BBB at the end
    assert res["final_equity"] == pytest.approx(95.0)
    assert [b["symbol"] for b in res["book"]] == ["BBB"]


def test_rolling_never_rebuys_a_stopout_without_a_fresh_screen_pass():
    bars_by = _rolling_world()
    res = RL.run_rolling(bars_by, [{"symbol": "AAA", "stop": 95.0}],
                         "2026-01-02", bars_by["AAA"][-1]["date"],
                         100.0, lambda s, d: True, screen=lambda b, d: None)
    buys = [b for b in res["blotter"] if "BUY" in b[2]]
    assert len(buys) == 1, "no screen pass, no re-entry — the cash waits"
    assert res["final_equity"] == pytest.approx(95.0)
    assert res["cash"] == pytest.approx(95.0)


def test_rolling_refuses_fresh_signals_on_falling_earnings():
    bars_by = _rolling_world()

    def stub(bars_upto, day):
        if bars_upto[-1]["symbol"] == "BBB" \
                and day.isoformat() == "2026-01-16":
            return {"action": "BUY", "stop": 45.0,
                    "volume_multiple": 2.0, "month_multiple": 2.0}
        return None

    res = RL.run_rolling(bars_by, [{"symbol": "AAA", "stop": 95.0}],
                         "2026-01-02", bars_by["AAA"][-1]["date"],
                         100.0, lambda s, d: s != "BBB", screen=stub)
    text = "\n".join(f"{d} {s} {w}" for d, s, w in res["blotter"])
    assert "BBB fresh signal REFUSED — falling earnings power" in text
    assert not [b for b in res["blotter"] if b[1] == "BBB" and "BUY" in b[2]]


def test_rolling_seed_book_gets_equal_slices():
    aaa = _roll_bars("AAA", [100.0] * 40)
    bbb = _roll_bars("BBB", [50.0] * 40)
    res = RL.run_rolling({"AAA": aaa, "BBB": bbb},
                         [{"symbol": "AAA", "stop": 90.0},
                          {"symbol": "BBB", "stop": 45.0}],
                         "2026-01-02", aaa[-1]["date"],
                         100.0, lambda s, d: True, screen=lambda b, d: None)
    seeds = [b for b in res["blotter"] if "seed" in b[2]]
    assert len(seeds) == 2
    assert all("₹50.00" in b[2] for b in seeds)
    assert res["final_equity"] == pytest.approx(100.0)


# ------------------------------------------- the six-year run (longrun.py)

import longrun as LR        # noqa: E402


def test_fy_end_dates_parse_by_real_calendar():
    assert LR.fy_end_date("Mar 2020") == dt.date(2020, 3, 31)
    assert LR.fy_end_date("Jun 2020") == dt.date(2020, 6, 30)
    assert LR.fy_end_date("Dec 2019") == dt.date(2019, 12, 31)
    assert LR.fy_end_date("TTM") is None


def test_a_june_fiscal_year_never_leaks_into_a_june_screen():
    # at a screen in June 2020 the cut is "Mar 2020" (2020-03-31):
    # a 'Jun 2020' year ends 2020-06-30 — AFTER the cut — and must be
    # excluded even though naive label sorting would let it through
    cut = LR.fy_end_date("Mar 2020")
    assert LR.fy_end_date("Jun 2020") > cut
    assert LR.fy_end_date("Dec 2019") <= cut
    assert LR.fy_end_date("Mar 2020") <= cut


def test_genesis_mode_starts_all_cash_and_stays_cash_without_signals():
    aaa = _roll_bars("AAA", [100.0] * 40)
    res = RL.run_rolling({"AAA": aaa}, [], "2026-01-02",
                         aaa[-1]["date"], 100.0,
                         lambda s, d: True, screen=lambda b, d: None,
                         slots=10)
    assert res["final_equity"] == pytest.approx(100.0)
    assert res["cash"] == pytest.approx(100.0)
    assert not res["book"] and not res["closed"]
    assert all(w["positions"] == 0 for w in res["equity_curve"])


def test_genesis_mode_deploys_equal_slices_from_the_first_screen():
    aaa = _roll_bars("AAA", [100.0] * 40)
    bbb = _roll_bars("BBB", [50.0] * 40)

    def stub(bars_upto, day):
        if day.isoformat() == "2026-01-09":
            return {"action": "BUY",
                    "stop": bars_upto[-1]["close"] * 0.9,
                    "volume_multiple": 2.0, "month_multiple": 2.0}
        return None

    res = RL.run_rolling({"AAA": aaa, "BBB": bbb}, [], "2026-01-02",
                         aaa[-1]["date"], 100.0,
                         lambda s, d: True, screen=stub, slots=10)
    buys = [b for b in res["blotter"] if "BUY ₹" in b[2]]
    # both signals funded on the next trading day, one tenth each
    assert len(buys) == 2 and all(b[0] == "2026-01-12" for b in buys)
    assert all("BUY ₹10.00" in b[2] for b in buys)
    assert res["cash"] == pytest.approx(80.0)
    assert all(w["cash"] >= 0 for w in res["equity_curve"])


# --------------------------------- real-world frictions (frictions.py)

import frictions as FR      # noqa: E402


def test_angel_one_rates_switch_on_the_brokerage_date():
    f = FR.AngelOneFrictions()
    # before 1 Nov 2024: delivery brokerage was zero
    pre_buy = f.buy_rate("2022-05-02")
    assert pre_buy == pytest.approx(
        0.0010 + 0.0000297 + 0.000001 + 0.00015
        + 0.18 * (0.0000297 + 0.000001))
    # after: 0.1% brokerage plus 18% GST on it joins every order
    post_buy = f.buy_rate("2025-05-02")
    assert post_buy == pytest.approx(pre_buy + 0.0010 * 1.18)
    # sells carry no stamp duty
    assert f.sell_rate("2022-05-02") == pytest.approx(
        pre_buy - 0.00015)


def test_buy_split_conserves_cash_to_the_paisa():
    f = FR.AngelOneFrictions()
    notional, cost = f.buy_split(100.0, "2025-05-02")
    assert notional + cost == pytest.approx(100.0)
    assert cost == pytest.approx(100.0 - 100.0 / (1 + f.buy_rate("2025-05-02")))
    assert f.total_costs == pytest.approx(cost)


def test_set_off_short_loss_absorbs_long_gain_but_never_the_reverse():
    # ST loss 40 eats into LT gain 100 → LT taxable 60, no ST tax
    r = FR.offset_and_tax(-40.0, 100.0, 0.0, 0.0)
    assert r["tax"] == pytest.approx(0.125 * 60.0)
    assert r["cf_st"] == 0.0 and r["cf_lt"] == 0.0
    # LT loss NEVER offsets an ST gain — it only carries forward
    r = FR.offset_and_tax(100.0, -40.0, 0.0, 0.0)
    assert r["tax"] == pytest.approx(0.20 * 100.0)
    assert r["cf_lt"] == pytest.approx(40.0)


def test_carried_losses_absorb_later_years_gains():
    r = FR.offset_and_tax(50.0, 20.0, 30.0, 10.0)
    # b/f ST loss 30 eats ST gain to 20; b/f LT loss 10 eats LT to 10
    assert r["tax"] == pytest.approx(0.20 * 20.0 + 0.125 * 10.0)
    assert r["cf_st"] == 0.0 and r["cf_lt"] == 0.0


def test_holding_over_a_year_is_long_term():
    f = FR.AngelOneFrictions()
    f.on_sale("2020-06-08", "2021-06-08", 100.0, 150.0, 1.0)   # 365 d: ST
    f.on_sale("2020-06-08", "2021-06-09", 100.0, 150.0, 1.0)   # 366 d: LT
    assert f.st_by_fy[FR.fy_label("2021-06-08")] == pytest.approx(50.0)
    assert f.lt_by_fy[FR.fy_label("2021-06-09")] == pytest.approx(50.0)


def test_rolling_with_frictions_charges_orders_and_settles_april_tax():
    # AAA is bought at 100, stopped at 95 in January — a realised loss;
    # BBB is bought at 50 and rides to 80 — unrealised, untaxed.
    aaa = _roll_bars("AAA", [100.0] * 6 + [98.0, 94.0] + [93.0] * 60)
    bbb = _roll_bars("BBB", [50.0] * 8 + [80.0] * 60)
    # extend both series past 1 April so the tax day arrives
    for sym, bars in (("AAA", aaa), ("BBB", bbb)):
        d = dt.date.fromisoformat(bars[-1]["date"])
        while d < dt.date(2026, 4, 10):
            d += dt.timedelta(days=1)
            if d.weekday() < 5:
                c = bars[-1]["close"]
                bars.append({"symbol": sym, "date": d.isoformat(),
                             "open": c, "high": c + 0.5, "low": c - 0.5,
                             "close": c, "volume": 100_000})

    def stub(bars_upto, day):
        if bars_upto[-1]["symbol"] == "BBB" \
                and day.isoformat() == "2026-01-16":
            return {"action": "BUY", "stop": 45.0,
                    "volume_multiple": 2.0, "month_multiple": 2.0}
        return None

    f = FR.AngelOneFrictions()
    res = RL.run_rolling({"AAA": aaa, "BBB": bbb},
                         [{"symbol": "AAA", "stop": 95.0}],
                         "2026-01-02", aaa[-1]["date"], 100.0,
                         lambda s, d: True, screen=stub, slots=None,
                         frictions=f)
    text = "\n".join(f"{d} {s} {w}" for d, s, w in sorted(res["blotter"]))
    # every order carries its charges
    assert "charges ₹" in text
    # the AAA loss is short-term and carries forward — no tax due
    tax_lines = [b for b in res["blotter"] if b[1] == "TAX"]
    assert len(tax_lines) == 1 and "FY2026 settled: ₹0.00 paid" in tax_lines[0][2]
    assert f.cf_st > 0 and f.total_tax == 0.0
    # charges genuinely shrank the position: fewer than 1 share of AAA
    aaa_trade = [c for c in res["closed"] if c["symbol"] == "AAA"][0]
    assert aaa_trade["shares"] < 1.0
    # and the books still balance to the paisa
    assert res["final_equity"] == pytest.approx(
        res["cash"] + sum(b["value"] for b in res["book"]))
    assert all(w["cash"] >= -1e-9 for w in res["equity_curve"])


def test_rolling_with_frictions_taxes_a_short_term_gain_at_20pct():
    # AAA bought at 100 (seed), ratchet-free, stopped at 130 in March
    # via a spike through a raised... simpler: stop set above entry by
    # the seed row, price falls to it after a run-up
    aaa = _roll_bars("AAA", [100.0] * 5 + [140.0] * 30 + [129.0] * 20)
    d = dt.date.fromisoformat(aaa[-1]["date"])
    while d < dt.date(2026, 4, 10):
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            aaa.append({"symbol": "AAA", "date": d.isoformat(),
                        "open": 129.0, "high": 129.5, "low": 128.5,
                        "close": 129.0, "volume": 100_000})
    f = FR.AngelOneFrictions()
    res = RL.run_rolling({"AAA": aaa}, [{"symbol": "AAA", "stop": 130.0}],
                         "2026-01-02", aaa[-1]["date"], 100.0,
                         lambda s, d: True, screen=lambda b, d: None,
                         frictions=f)
    assert len(res["closed"]) == 1
    gain = (130.0 - 100.0) * res["closed"][0]["shares"]
    assert f.total_tax == pytest.approx(0.20 * gain)
    tax_lines = [b for b in res["blotter"] if b[1] == "TAX"]
    assert len(tax_lines) == 1


# --------------------------- pyramiding: NEW capital on every box jump

def _box_bars(seq, sym="AAA", start="2026-01-02"):
    """[(high, low, close)] -> full weekday bars for the rolling engine."""
    d = dt.date.fromisoformat(start)
    out, prev = [], seq[0][2]
    for h, l, c in seq:
        while d.weekday() >= 5:
            d += dt.timedelta(days=1)
        out.append({"symbol": sym, "date": d.isoformat(), "open": prev,
                    "high": float(h), "low": float(l), "close": float(c),
                    "volume": 100_000})
        prev = float(c)
        d += dt.timedelta(days=1)
    return out


CLIMB_3_BOXES = (
    [(55, 52, 54)] + [(54, 51, 52), (53, 50, 51), (54, 51, 53)] * 2
    + [(58, 54, 57), (62, 57, 60)]                       # jump to box 2
    + [(61, 57, 59), (60, 56, 58), (61, 57, 60)]         # seal 56-62
    + [(66, 61, 65), (70, 64, 68)]                       # jump to box 3
    + [(69, 64, 67), (68, 63, 66), (69, 64, 68)]         # seal 63-70
    + [(69, 64, 68)] * 10)                               # hold box 3


def test_every_box_jump_doubles_with_new_external_capital():
    bars = _box_bars(CLIMB_3_BOXES)
    res = RL.run_rolling({"AAA": bars}, [{"symbol": "AAA", "stop": 47.5}],
                         "2026-01-02", bars[-1]["date"], 100.0,
                         lambda s, d: True, screen=lambda b, d: None,
                         slots=3, pyramid=True)
    text = sorted(res["blotter"])
    raises = [b for b in text if "RAISE STOP" in b[2]]
    pyramids = [b for b in text if "PYRAMID BUY" in b[2]]
    assert len(raises) == 2 and len(pyramids) == 2, \
        "EVERY jump doubles now — two jumps, two doublings"
    # each add-on lands after its own raise, at the next day's open
    assert raises[0][0] < pyramids[0][0] <= raises[1][0] < pyramids[1][0]
    # doubling arithmetic: lot 2 equals lot 1; lot 3 equals lots 1+2
    lots = res["book"][0]["lots"]
    assert len(lots) == 3
    assert lots[1]["shares"] == pytest.approx(lots[0]["shares"])
    assert lots[2]["shares"] == pytest.approx(lots[0]["shares"]
                                              + lots[1]["shares"])
    assert res["book"][0]["shares"] == pytest.approx(4 * lots[0]["shares"])
    # each injection equals the position's market value that morning
    assert len(res["injections"]) == 2
    for (d_inj, amt), lot in zip(res["injections"], lots[1:]):
        assert d_inj == lot["date"]
        assert amt == pytest.approx(lot["px"] * lot["shares"])
    assert res["total_injected"] == pytest.approx(
        sum(a for _, a in res["injections"]))


def test_external_pyramids_never_touch_the_portfolio_cash():
    bars = _box_bars(CLIMB_3_BOXES)
    args = ({"AAA": bars}, [{"symbol": "AAA", "stop": 47.5}],
            "2026-01-02", bars[-1]["date"], 100.0)
    kw = dict(screen=lambda b, d: None, slots=3)
    plain = RL.run_rolling(*args, lambda s, d: True, **kw)
    pyr = RL.run_rolling(*args, lambda s, d: True, **kw, pyramid=True)
    # cash is identical week for week — fresh entries can never starve
    assert [w["cash"] for w in pyr["equity_curve"]] \
        == [w["cash"] for w in plain["equity_curve"]]
    # and the engine without doubling still exists, unchanged: no
    # pyramid lines, no injections
    assert not [b for b in plain["blotter"] if "PYRAMID" in b[2]]
    assert plain["injections"] == [] and plain["total_injected"] == 0


def test_pyramid_lots_are_taxed_each_on_its_own_clock():
    # after two doublings the stock slides through the ratcheted stop:
    # lot 1 (54) exits at a gain, lots 2-3 (bought higher) at losses —
    # the frictions engine must see ALL lots, netted short-term
    slide = CLIMB_3_BOXES + [(60, 58, 59), (59.5, 58, 59), (59, 55, 56)]
    bars = _box_bars(slide)
    f = FR.AngelOneFrictions()
    res = RL.run_rolling({"AAA": bars}, [{"symbol": "AAA", "stop": 47.5}],
                         "2026-01-02", bars[-1]["date"], 100.0,
                         lambda s, d: True, screen=lambda b, d: None,
                         slots=3, frictions=f, pyramid=True)
    assert len(res["closed"]) == 1
    c = res["closed"][0]
    assert len(c["lots"]) == 3
    expect = sum((c["exit_px"] - l["px"]) * l["shares"] for l in c["lots"])
    assert sum(f.st_by_fy.values()) == pytest.approx(expect)
    assert not f.lt_by_fy, "every lot was held under a year"
    assert res["final_equity"] == pytest.approx(res["cash"])


def test_xirr_matches_cagr_when_there_are_no_injections():
    flows = [("2020-06-08", -100.0), ("2026-06-08", 400.0)]
    r = LR.xirr(flows)
    assert r == pytest.approx((4.0 ** (1 / 6) - 1) * 100, abs=0.05)


def test_xirr_accounts_for_money_added_along_the_way():
    # ₹100 for two years plus ₹100 added after one year, ending at 231:
    # 100·(1+r)² + 100·(1+r) = 231 → r = 10%
    flows = [("2020-01-01", -100.0), ("2021-01-01", -100.0),
             ("2022-01-01", 231.0)]
    assert LR.xirr(flows) == pytest.approx(10.0, abs=0.05)


def test_inr_formats_in_lakhs_and_crores_when_the_numbers_grow():
    assert RL.inr(788.82) == "₹788.82"
    assert RL.inr(99_999.99) == "₹99,999.99"
    assert RL.inr(123_456) == "₹1.23 lakh"
    assert RL.inr(2.5e7) == "₹2.50 crore"
    assert RL.inr(3.2e12) == "₹3.20 lakh crore"
    assert RL.inr(8.4e21) == "₹840.00 lakh crore crore"
    assert RL.inr(-150_000) == "-₹1.50 lakh"


CLIMB_5_BOXES = (
    CLIMB_3_BOXES[:-10]                                  # boxes 1-3 sealed
    + [(73, 68, 72), (77, 71, 75)]                       # jump to box 4
    + [(76, 71, 74), (75, 70, 73), (76, 71, 75)]         # seal 70-77
    + [(80, 75, 79), (84, 78, 82)]                       # jump to box 5
    + [(83, 78, 81), (82, 77, 80), (83, 78, 82)]         # seal 77-84
    + [(83, 78, 82)] * 10)                               # hold box 5


def test_doubling_is_capped_at_three_per_position():
    bars = _box_bars(CLIMB_5_BOXES)
    res = RL.run_rolling({"AAA": bars}, [{"symbol": "AAA", "stop": 47.5}],
                         "2026-01-02", bars[-1]["date"], 100.0,
                         lambda s, d: True, screen=lambda b, d: None,
                         slots=3, pyramid=True)
    raises = [b for b in res["blotter"] if "RAISE STOP" in b[2]]
    pyramids = [b for b in res["blotter"] if "PYRAMID BUY" in b[2]]
    capped = [b for b in res["blotter"] if "NOT doubled" in b[2]]
    assert len(raises) == 4, "four box jumps up the five-box ladder"
    assert len(pyramids) == 3, "the 4th jump must NOT double — cap is 3"
    assert len(capped) == 1 and "cap is already used" in capped[0][2]
    book = res["book"][0]
    assert len(book["lots"]) == 4                    # entry + 3 doublings
    # 3 doublings = 8× the original share count, and no more
    assert book["shares"] == pytest.approx(8 * book["lots"][0]["shares"])
    assert len(res["injections"]) == 3


# ------------------------- rolling point-in-time membership (the radar)

import pit_universe as PIT  # noqa: E402


def test_membership_enters_at_rank_and_exits_only_past_hysteresis():
    ranks = {
        "2020-01": {"A": 1, "B": 2, "C": 5},
        "2020-02": {"A": 1, "B": 4, "C": 2},   # B slips past enter, stays
        "2020-03": {"A": 1, "B": 9, "C": 2},   # B past exit → leaves
        "2020-04": {"A": 1, "B": 2, "C": 2},   # B earns re-entry
    }
    m = PIT.rolling_membership(ranks, "2020-02", "2020-05",
                               enter=2, exit_=4)
    assert m["2020-02"]["members"] == {"A", "B"}
    # March judged on February: B ranked 4 — past enter(2) but within
    # exit(4), so the incumbent STAYS (hysteresis, no flapping)
    assert m["2020-03"]["members"] == {"A", "B", "C"}
    # April judged on March: B ranked 9 — past exit → out
    assert m["2020-04"]["members"] == {"A", "C"}
    assert m["2020-04"]["left"] == {"B"}
    # May judged on April: B back at rank 2 → re-enters
    assert m["2020-05"]["members"] == {"A", "B", "C"}
    assert m["2020-05"]["entered"] == {"B"}


def test_membership_never_uses_the_month_being_decided():
    # the month's OWN ranks must not matter — only trailing ones do
    ranks = {"2020-01": {"A": 1}, "2020-02": {"Z": 1}}
    m = PIT.rolling_membership(ranks, "2020-02", "2020-02",
                               enter=1, exit_=2)
    assert m["2020-02"]["members"] == {"A"}, \
        "February must be decided by January's ranks, never February's"


def test_a_symbol_that_stops_trading_drops_off_the_radar():
    ranks = {"2020-01": {"A": 1, "B": 1},
             "2020-02": {"A": 1}}              # B vanishes (suspended)
    m = PIT.rolling_membership(ranks, "2020-02", "2020-03",
                               enter=1, exit_=5)
    assert "B" in m["2020-02"]["members"]
    assert m["2020-03"]["members"] == {"A"}


def test_membership_gates_fresh_entries_but_never_held_positions():
    bars = _box_bars(CLIMB_3_BOXES)
    bbb = _roll_bars("BBB", [50.0] * len(bars))
    months = sorted({b["date"][:7] for b in bars})
    # AAA is seeded, then drops OFF the radar after the first month;
    # BBB is never a member at all
    membership = {m: ({"AAA"} if i == 0 else set())
                  for i, m in enumerate(months)}

    def stub(bars_upto, day):
        if bars_upto[-1]["symbol"] == "BBB":
            return {"action": "BUY", "stop": 45.0,
                    "volume_multiple": 2.0, "month_multiple": 2.0}
        return None

    res = RL.run_rolling({"AAA": bars, "BBB": bbb},
                         [{"symbol": "AAA", "stop": 47.5}],
                         "2026-01-02", bars[-1]["date"], 100.0,
                         lambda s, d: True, screen=stub, slots=3,
                         membership=membership)
    # BBB's signal never fires — it was never on the radar
    assert not [b for b in res["blotter"] if b[1] == "BBB"]
    # AAA left the radar but the HELD position kept its full rhythm:
    # ratchets continued and it is still held at the end
    assert [b for b in res["blotter"] if "RAISE STOP" in b[2]]
    assert [b["symbol"] for b in res["book"]] == ["AAA"]

    # same world, BBB a member in month 2 → the signal trades
    membership2 = {m: ({"AAA", "BBB"} if i <= 1 else set())
                   for i, m in enumerate(months)}
    res2 = RL.run_rolling({"AAA": bars, "BBB": bbb},
                          [{"symbol": "AAA", "stop": 47.5}],
                          "2026-01-02", bars[-1]["date"], 100.0,
                          lambda s, d: True, screen=stub, slots=3,
                          membership=membership2)
    assert [b for b in res2["blotter"] if b[1] == "BBB" and "BUY" in b[2]]
