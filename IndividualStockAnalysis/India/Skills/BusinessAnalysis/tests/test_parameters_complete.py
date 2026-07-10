"""
The load-bearing test: enforces that EVERY module and parameter from the source
document exists in parameters.yaml, and that the framework is internally valid.
This is the machine guarantee behind "no parameter should be missed".
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import framework as F  # noqa: E402


def test_framework_loads():
    fw = F.load_framework()
    assert fw.version
    assert len(fw.modules) == 7
    assert len(fw.parameters) == 34


def test_framework_valid_and_complete():
    problems = F.validate()
    assert problems == [], "framework validation problems:\n" + "\n".join(problems)


def test_all_expected_modules_present():
    import yaml
    checklist = yaml.safe_load((F.REFERENCE / "checklist.yaml").read_text())
    fw = F.load_framework()
    got = set(fw.module_ids())
    for m in checklist["expected_modules"]:
        assert m in got, f"module {m} missing from parameters.yaml"


def test_all_expected_parameters_present():
    import yaml
    checklist = yaml.safe_load((F.REFERENCE / "checklist.yaml").read_text())
    fw = F.load_framework()
    got = {p.id for p in fw.parameters}
    expected = set()
    for plist in checklist["expected_parameters"].values():
        expected.update(plist)
    missing = expected - got
    assert not missing, f"parameters missing (framework incomplete): {sorted(missing)}"


def test_every_parameter_has_full_contract():
    fw = F.load_framework()
    for p in fw.parameters:
        assert p.nature in F.VALID_NATURES, p.id
        assert p.direction in F.VALID_DIRECTIONS, p.id
        assert p.data_sources, f"{p.id} has no data_sources"
        assert p.signal, f"{p.id} has no signal"
        assert p.description, f"{p.id} has no description"


def test_parameter_ids_unique_and_namespaced():
    fw = F.load_framework()
    ids = [p.id for p in fw.parameters]
    assert len(ids) == len(set(ids)), "duplicate parameter ids"
    for p in fw.parameters:
        assert p.id.startswith(p.module + "."), p.id


def test_data_sources_are_known():
    """Every data_source referenced must be one the skill knows how to fetch."""
    known = {"balance_sheet", "profit_loss", "cash_flow", "working_capital",
             "stock_info", "concalls", "annual_reports", "management_info"}
    fw = F.load_framework()
    for p in fw.parameters:
        for ds in p.data_sources:
            assert ds in known, f"{p.id} references unknown data source '{ds}'"
