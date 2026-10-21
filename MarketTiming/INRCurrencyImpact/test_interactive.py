"""End-to-end smoke test for the Chart.js interactive HTMLs.

Opens each *_interactive.html in a headless Chromium via the `file://`
protocol (the same protocol Safari uses for downloaded files), then:

  1. waits for the chart canvas to render,
  2. checks the line-toggle checkboxes match the Chart.js datasets,
  3. clicks each preset (Last 5y / 10y / 15y / 25y / All) and verifies
     the chart's x scale.min / scale.max changed accordingly,
  4. types a custom From/To range and verifies the chart updates,
  5. unchecks a line and verifies the corresponding Chart.js dataset is
     hidden,
  6. fails the test if any console error / page error fired.

Run:  python3 test_interactive.py
Exits non-zero on any failure so it can gate CI.
"""

from __future__ import annotations
import os
import sys
import traceback
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
HTMLS = [
    "inr_vs_usd_interactive.html",
    "nifty_indices_interactive.html",
    "constituent_medians_interactive.html",
    "combined_all_interactive.html",
]


def assert_eq(a, b, msg: str) -> None:
    if a != b:
        raise AssertionError(f"{msg}: expected {b!r}, got {a!r}")


def _check_one(page, html_path: Path) -> None:
    errors: list[str] = []
    page.on("pageerror", lambda exc: errors.append(f"pageerror: {exc}"))
    page.on("console", lambda msg: errors.append(f"console.{msg.type}: "
            f"{msg.text}") if msg.type in ("error",) else None)

    page.goto(html_path.as_uri(), wait_until="load", timeout=15000)

    # Wait for the canvas to actually be drawn (Chart.js paints on mount).
    page.wait_for_function(
        "() => window.Chart && document.querySelector('canvas')"
        " && document.querySelectorAll('#lineToggles input').length > 0",
        timeout=10000,
    )

    n_datasets = page.evaluate(
        "() => Chart.getChart('chart').data.datasets.length")
    n_checkboxes = page.evaluate(
        "() => document.querySelectorAll('#lineToggles input').length")
    assert_eq(n_checkboxes, n_datasets,
              "checkbox count vs Chart.js dataset count")

    full_width = page.evaluate(
        "() => Chart.getChart('chart').data.labels.length")

    # ---- preset buttons ----
    presets = {"5": 5, "10": 10, "15": 15, "25": 25}
    for years_attr, n in presets.items():
        page.click(f"#presetRow button[data-years='{years_attr}']")
        page.wait_for_timeout(120)
        x = page.evaluate(
            "() => { const c = Chart.getChart('chart');"
            "  return [c.options.scales.x.min, c.options.scales.x.max]; }")
        x_min, x_max = x
        # Preset clamps to the available data span when n > full_width
        expected = min(n, full_width)
        assert_eq(x_max - x_min + 1, expected,
                  f"preset Last {n}y window width")
    # 'All' should restore full range
    page.click("#presetRow button[data-years='all']")
    page.wait_for_timeout(120)
    full = page.evaluate(
        "() => { const c = Chart.getChart('chart');"
        "  const xs = c.data.datasets[0].data.length;"
        "  return [c.options.scales.x.min, c.options.scales.x.max,"
        "          c.data.labels.length]; }")
    assert full[1] - full[0] + 1 == full[2], (
        f"All preset full width mismatch: {full}")

    # ---- custom From/To via input boxes ----
    page.fill("#fromYear", "2010")
    page.dispatch_event("#fromYear", "change")
    page.fill("#toYear", "2018")
    page.dispatch_event("#toYear", "change")
    page.wait_for_timeout(120)
    x = page.evaluate(
        "() => { const c = Chart.getChart('chart');"
        "  return [c.options.scales.x.min, c.options.scales.x.max]; }")
    assert_eq(x, [2010, 2018], "custom From/To range applied")

    # ---- line toggle ----
    page.click("#resetBtn")
    page.wait_for_timeout(120)
    page.evaluate("() => document.querySelector("
                  "'#lineToggles input[data-idx=\"0\"]').click()")
    page.wait_for_timeout(120)
    visible = page.evaluate(
        "() => Chart.getChart('chart').isDatasetVisible(0)")
    assert visible is False, "dataset 0 should be hidden after toggle"

    # restore and check it shows up again
    page.evaluate("() => document.querySelector("
                  "'#lineToggles input[data-idx=\"0\"]').click()")
    page.wait_for_timeout(120)
    visible = page.evaluate(
        "() => Chart.getChart('chart').isDatasetVisible(0)")
    assert visible is True, "dataset 0 should be visible after toggle back"

    if errors:
        raise AssertionError("page errors / console.error fired:\n"
                              + "\n".join(errors))


def main() -> int:
    failures: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for name in HTMLS:
            path = HERE / name
            print(f"\n=== Testing {name} ===")
            try:
                _check_one(page, path)
                print(f"   PASSED")
            except Exception:
                print(f"   FAILED")
                traceback.print_exc()
                failures.append(name)
        browser.close()

    if failures:
        print(f"\nFAILURES: {len(failures)} of {len(HTMLS)} ({failures})")
        return 1
    print(f"\nAll {len(HTMLS)} interactive HTMLs passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
