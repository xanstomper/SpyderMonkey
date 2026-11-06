"""Tests for the /spydermonkey session-hijack mandate (v5.4.0).

The contract is the interface other agents inject (opencode agent, claude
command, hermes skill, cline wrapper). If it drifts — wording, walls,
persistence clause — those integrations silently lie. Pin its shape.
Stdlib unittest — same style as the rest of the suite so CI's
`unittest discover` gates it.
"""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class SessionMandateTests(unittest.TestCase):
    def test_session_mandate_file_shape(self):
        p = ROOT / "references" / "mandate-session.md"
        self.assertTrue(p.exists(), "references/mandate-session.md missing")
        text = p.read_text(encoding="utf-8")
        for token in ("PERSISTENCE CLAUSE", "STOP CONDITIONS", "NO-GAIN",
                      "/spydermonkey off", "baseline → attack", "SPYDERMONKEY — DISPATCHER ONLINE"):
            self.assertIn(token, text, f"session mandate missing: {token}")
        # the walls must remain non-negotiable text in the injectable contract
        self.assertIn("not overridable", text)

    def test_mandate_session_cli_prints_contract(self):
        r = subprocess.run(
            [sys.executable, "scripts/spydermonkey.py", "mandate", "--session"],
            capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("SESSION MANDATE", r.stdout)
        self.assertIn("STOP CONDITIONS", r.stdout)

        r = subprocess.run(
            [sys.executable, "scripts/spydermonkey.py", "mandate", "--session", "--file"],
            capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(r.stdout.strip().endswith("mandate-session.md"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
