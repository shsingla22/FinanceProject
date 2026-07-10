"""
framework.py — load and validate the Business Analysis parameter taxonomy.

This is the programmatic entry point an autonomous agent uses to read the
framework. It loads `reference/parameters.yaml`, validates it against
`reference/checklist.yaml`, and exposes typed accessors.

Pure-stdlib except PyYAML. No network, no side effects.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    raise

SKILL_ROOT = Path(__file__).resolve().parent.parent
REFERENCE = SKILL_ROOT / "reference"
PARAMS_FILE = REFERENCE / "parameters.yaml"
CHECKLIST_FILE = REFERENCE / "checklist.yaml"

VALID_NATURES = {"quantitative", "qualitative", "hybrid"}
VALID_DIRECTIONS = {"maximize", "minimize", "stable", "context"}
REQUIRED_FIELDS = {"id", "module", "name", "description", "nature",
                   "data_sources", "signal", "direction"}


@dataclass
class Parameter:
    id: str
    module: str
    name: str
    description: str
    nature: str
    data_sources: list
    signal: str
    direction: str
    examples: list = field(default_factory=list)
    cautions: list = field(default_factory=list)
    extra: str = ""


@dataclass
class Module:
    id: str
    order: int
    name: str
    guidance: str = ""


@dataclass
class Framework:
    version: str
    modules: list  # list[Module]
    parameters: list  # list[Parameter]

    def module_ids(self) -> list[str]:
        return [m.id for m in self.modules]

    def params_for(self, module_id: str) -> list:
        return [p for p in self.parameters if p.module == module_id]

    def by_id(self, pid: str) -> Parameter | None:
        for p in self.parameters:
            if p.id == pid:
                return p
        return None

    def by_nature(self, nature: str) -> list:
        return [p for p in self.parameters if p.nature == nature]


def load_framework(path: Path = PARAMS_FILE) -> Framework:
    data = yaml.safe_load(path.read_text())
    modules = [Module(id=m["id"], order=m["order"], name=m["name"],
                      guidance=m.get("guidance", "")) for m in data["modules"]]
    params = []
    for p in data["parameters"]:
        params.append(Parameter(
            id=p["id"], module=p["module"], name=p["name"],
            description=p["description"], nature=p["nature"],
            data_sources=p["data_sources"], signal=p["signal"],
            direction=p["direction"], examples=p.get("examples", []) or [],
            cautions=p.get("cautions", []) or [], extra=p.get("extra", ""),
        ))
    return Framework(version=data["version"], modules=modules, parameters=params)


def validate(framework: Framework | None = None) -> list[str]:
    """Return a list of problems. Empty list == valid.

    Checks: field contract, enum validity, unique ids, and — crucially —
    exact coverage against the checklist (no parameter missing OR extra).
    """
    if framework is None:
        framework = load_framework()
    problems: list[str] = []

    # 1. Per-parameter field contract
    seen = set()
    for p in framework.parameters:
        for f in REQUIRED_FIELDS:
            if not getattr(p, f, None):
                problems.append(f"{p.id}: missing/empty required field '{f}'")
        if p.nature not in VALID_NATURES:
            problems.append(f"{p.id}: invalid nature '{p.nature}'")
        if p.direction not in VALID_DIRECTIONS:
            problems.append(f"{p.id}: invalid direction '{p.direction}'")
        if not isinstance(p.data_sources, list) or not p.data_sources:
            problems.append(f"{p.id}: data_sources must be a non-empty list")
        if p.id in seen:
            problems.append(f"{p.id}: duplicate parameter id")
        seen.add(p.id)
        if not p.id.startswith(p.module + "."):
            problems.append(f"{p.id}: id must start with its module id '{p.module}.'")

    # 2. Coverage against the checklist (the "no parameter missed" guarantee)
    checklist = yaml.safe_load(CHECKLIST_FILE.read_text())
    exp_modules = set(checklist["expected_modules"].keys())
    got_modules = set(framework.module_ids())
    if exp_modules != got_modules:
        problems.append(f"module mismatch: missing={exp_modules - got_modules} "
                        f"extra={got_modules - exp_modules}")

    exp_params = set()
    for plist in checklist["expected_parameters"].values():
        exp_params.update(plist)
    got_params = {p.id for p in framework.parameters}
    missing = exp_params - got_params
    extra = got_params - exp_params
    if missing:
        problems.append(f"MISSING parameters (framework incomplete): {sorted(missing)}")
    if extra:
        problems.append(f"EXTRA parameters not in checklist: {sorted(extra)}")
    if len(framework.parameters) != checklist["expected_total"]:
        problems.append(f"expected_total={checklist['expected_total']} but got "
                        f"{len(framework.parameters)} parameters")

    return problems


def main() -> int:
    fw = load_framework()
    problems = validate(fw)
    if problems:
        print("FRAMEWORK INVALID:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"Framework OK: version {fw.version}, "
          f"{len(fw.modules)} modules, {len(fw.parameters)} parameters.")
    by_nat = {n: len(fw.by_nature(n)) for n in sorted(VALID_NATURES)}
    print(f"  by nature: {by_nat}")
    for m in sorted(fw.modules, key=lambda x: x.order):
        print(f"  [{m.id}] {m.name}: {len(fw.params_for(m.id))} parameters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
