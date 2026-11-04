"""Repository integrity: Markdown lint, claims-ledger freshness and CLI smoke tests."""

import contextlib
import io
import json
import unittest

import _paths  # noqa: F401
import extract_claims
import lint_markdown
from love_translation import cli


class Repository(unittest.TestCase):
    def test_markdown_is_clean(self):
        self.assertEqual(lint_markdown.lint(), [])

    def test_claims_ledger_is_fresh(self):
        expected = extract_claims.serialise(extract_claims.build())
        current = extract_claims.LEDGER.read_text(encoding="utf-8")
        self.assertEqual(current, expected, "run `make claims` after editing the paper")

    def test_every_claim_is_graded(self):
        grades = {"established", "moderate", "preliminary", "theoretical", "hypothesis", "assumption"}
        rows = [json.loads(line) for line in extract_claims.LEDGER.read_text(encoding="utf-8").splitlines()]
        self.assertGreater(len(rows), 100)
        self.assertTrue(all(r["grade"] in grades for r in rows))
        self.assertEqual(len({r["id"] for r in rows}), len(rows))


class CommandLine(unittest.TestCase):
    def run_cli(self, *argv):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = cli.main(list(argv))
        return code, buffer.getvalue()

    def test_trust_command(self):
        code, out = self.run_cli("trust", "--slope", "4.5", "--midpoint", "0.5")
        self.assertEqual(code, 0)
        self.assertIn("bistable: yes", out)

    def test_cosine_demo_reproduces_the_paper(self):
        _, out = self.run_cli("cosine-demo")
        for value in ("0.959", "0.926", "0.763", "0.770"):
            self.assertIn(value, out)

    def test_claims_query(self):
        _, out = self.run_cli("claims", "--grade", "hypothesis", "--count", "--file", str(extract_claims.LEDGER))
        self.assertGreater(int(out.strip()), 0)


if __name__ == "__main__":
    unittest.main()
