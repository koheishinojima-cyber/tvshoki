#!/usr/bin/env python3
"""Minimal schema tests for tvshoki.grok.observation.v1."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "observation.v1.schema.json"
MD_PATH = ROOT / "observation.v1.md"
VALID_DIR = ROOT / "fixtures" / "valid"
INVALID_DIR = ROOT / "fixtures" / "invalid"


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def schema_from_md(text: str) -> object:
    marker = "## JSON Schema"
    i = text.index(marker)
    rest = text[i:]
    start = rest.index("```json") + len("```json")
    end = rest.index("```", start)
    return json.loads(rest[start:end])


class ObservationV1SchemaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_json(SCHEMA_PATH)
        cls.validator = Draft202012Validator(
            cls.schema, format_checker=FormatChecker()
        )

    def test_embedded_md_schema_matches_schema_json(self) -> None:
        md_schema = schema_from_md(MD_PATH.read_text(encoding="utf-8"))
        self.assertEqual(md_schema, self.schema)

    def test_valid_fixtures_are_accepted(self) -> None:
        paths = sorted(VALID_DIR.glob("*.json"))
        self.assertGreaterEqual(len(paths), 1)
        for path in paths:
            with self.subTest(path.name):
                self.validator.validate(load_json(path))

    def test_invalid_fixtures_are_rejected(self) -> None:
        paths = sorted(INVALID_DIR.glob("*.json"))
        self.assertGreaterEqual(len(paths), 2)
        for path in paths:
            with self.subTest(path.name):
                with self.assertRaises(ValidationError):
                    self.validator.validate(load_json(path))


if __name__ == "__main__":
    unittest.main()
