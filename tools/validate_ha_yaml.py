"""Parse Home Assistant YAML and compile all embedded Jinja templates."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any, Iterator

import yaml
from jinja2 import Environment


class HomeAssistantSafeLoader(yaml.SafeLoader):
    """Safe YAML loader that accepts Home Assistant-specific tagged values."""


def _construct_home_assistant_tag(loader: HomeAssistantSafeLoader, node: Any) -> Any:
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    return None


HomeAssistantSafeLoader.add_constructor(None, _construct_home_assistant_tag)


def iter_strings(value: Any, path: str = "root") -> Iterator[tuple[str, str]]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield from iter_strings(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from iter_strings(item, f"{path}[{index}]")
    elif isinstance(value, str):
        yield path, value


def validate(path: Path) -> int:
    environment = Environment(extensions=["jinja2.ext.loopcontrols"])

    if path.suffix.lower() == ".jinja":
        try:
            environment.parse(path.read_text(encoding="utf-8"))
        except Exception as error:
            print(f"{path}: invalid Jinja: {error}", file=sys.stderr)
            return 1
        print(f"OK: {path} (standalone Jinja template compiled)")
        return 0

    try:
        data = yaml.load(
            path.read_text(encoding="utf-8"), Loader=HomeAssistantSafeLoader
        )
    except Exception as error:
        print(f"{path}: invalid YAML: {error}", file=sys.stderr)
        return 1

    template_count = 0
    for yaml_path, value in iter_strings(data):
        if "{{" not in value and "{%" not in value and "{#" not in value:
            continue
        try:
            environment.parse(value)
        except Exception as error:
            print(
                f"{path}: invalid Jinja at {yaml_path}: {error}", file=sys.stderr
            )
            return 1
        template_count += 1

    print(f"OK: {path} (YAML parsed; {template_count} Jinja templates compiled)")
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_ha_yaml.py FILE [FILE ...]", file=sys.stderr)
        return 2
    return max(validate(Path(argument)) for argument in sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
