"""Tests for the known-tool catalog (v5.3.0).

The catalog is a lazy-loaded REFERENCE INDEX: it must never execute
anything, never read stdin, and never hit the network. These tests pin the
schema, the floor count (1,000+), and the CLI contract. Stdlib unittest —
same style as the rest of the suite so CI's `unittest discover` gates it.
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class CatalogTests(unittest.TestCase):
    def _catalog(self):
        return json.loads((ROOT / "references" / "tool-catalog.json").read_text(encoding="utf-8"))

    def test_catalog_schema_and_count(self):
        data = self._catalog()
        self.assertGreaterEqual(len(data), 1000, "catalog must hold 1,000+ known tools")
        names = [e.get("name", "").lower() for e in data]
        self.assertTrue(all(names), "every entry needs a name")
        self.assertEqual(len(set(names)), len(names), "tool names must be unique")
        for e in data:
            self.assertTrue(e.get("cat"), e)
            self.assertTrue(e.get("desc"), e)
            self.assertIn(e.get("mode"), ("passive", "active"), e)

    def test_catalog_cli_stats_offline_and_json(self):
        r = subprocess.run(
            [sys.executable, "scripts/spydermonkey.py", "catalog", "stats", "--json"],
            capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        payload = json.loads(r.stdout)
        self.assertGreaterEqual(payload["entries"], 1000)
        self.assertTrue(payload["note"].startswith("metadata only"))

    def test_catalog_cli_search_and_show(self):
        r = subprocess.run(
            [sys.executable, "scripts/spydermonkey.py", "catalog", "search", "nmap",
             "--limit", "5", "--json"],
            capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        hits = json.loads(r.stdout)["tools"]
        self.assertTrue(any(h["name"].lower() == "nmap" for h in hits))

        r = subprocess.run(
            [sys.executable, "scripts/spydermonkey.py", "catalog", "show", "nmap"],
            capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("nmap", r.stdout)

        r = subprocess.run(
            [sys.executable, "scripts/spydermonkey.py", "catalog", "show",
             "definitely-not-a-real-tool-xyz"],
            capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
        )
        self.assertEqual(r.returncode, 1)

    def test_catalog_mcp_tools_registered(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import mcp_server

        names = {t["name"] for t in mcp_server.TOOLS}
        self.assertIn("catalog_search", names)
        self.assertIn("catalog_show", names)
        self.assertGreaterEqual(len(mcp_server.HANDLERS), 52)


if __name__ == "__main__":
    unittest.main(verbosity=2)
