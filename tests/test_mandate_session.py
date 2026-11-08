"""Tests for the /spydermonkey session-hijack mandate (v8 — the fusion contract).

The contract is the interface other agents inject (opencode agent, claude
command, hermes skill, cline wrapper). If it drifts — wording, walls,
persistence clause — those integrations silently lie. Pin its shape.
Stdlib unittest — same style as the rest of the suite so CI's
`unittest discover` gates it.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class SessionMandateTests(unittest.TestCase):
    def test_session_mandate_file_shape(self):
        p = ROOT / "references" / "mandate-session.md"
        self.assertTrue(p.exists(), "references/mandate-session.md missing")
        text = p.read_text(encoding="utf-8")
        for token in ("PERSISTENCE CLAUSE", "STOP CONDITIONS", "NO-GAIN",
                      "/spydermonkey off", "baseline → attack", "SPYDERMONKEY — DISPATCHER ONLINE",
                      "THE TAKEOVER", "THE TRAINING LOOP", "THE TEACHING PROTOCOL",
                      "spydermonkey inject", "spydermonkey train",
                      "IN-MANDATE", "AMBIENT LAYER", ".spydermonkey-active",
                      "Contract ID: SM8.3"):
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

    def test_inmandate_reports_takeover_state(self):
        env = dict(os.environ)
        env.pop("SPYDERMONKEY_MANDATE", None)
        r = subprocess.run(
            [sys.executable, "scripts/spydermonkey.py", "inmandate", "--json"],
            capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
            env=env,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("in_mandate", r.stdout)

        env_on = dict(env)
        env_on["SPYDERMONKEY_MANDATE"] = "1"
        r = subprocess.run(
            [sys.executable, "scripts/spydermonkey.py", "inmandate", "--json"],
            capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
            env=env_on,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"in_mandate": true', r.stdout)
        self.assertIn("SM8.3", r.stdout)

    def test_sessionstart_hook_injects_only_in_mandate(self):
        hook = ROOT / "scripts" / "claude_hook_sessionstart.py"
        if not hook.exists():
            self.skipTest("sessionstart hook not present in this tree")
        payload = '{"session": {"cwd": "%s"}}' % ROOT
        r = subprocess.run(
            [sys.executable, str(hook)], input=payload,
            capture_output=True, text=True, cwd=ROOT, timeout=60,
        )
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout.strip(), "", "no marker → no injection")

        env = dict(os.environ)
        env["SPYDERMONKEY_MANDATE"] = "1"
        r = subprocess.run(
            [sys.executable, str(hook)], input=payload,
            capture_output=True, text=True, cwd=ROOT, timeout=60, env=env,
        )
        self.assertEqual(r.returncode, 0)
        self.assertIn("AMBIENT TAKEOVER", r.stdout)

    def test_campaign_init_deploys_ambient_takeover(self):
        home = Path(tempfile.mkdtemp(prefix="sm-camp-"))
        env = dict(os.environ)
        env["SPYDERMONKEY_HOME"] = str(home)
        env.pop("SPYDERMONKEY_MANDATE", None)
        try:
            r = subprocess.run(
                [sys.executable, "scripts/spydermonkey.py", "campaign", "init",
                 "--target", "amb-e2e", "--objective", "ambient"],
                capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL,
                timeout=60, env=env,
            )
            self.assertEqual(r.returncode, 0, r.stderr)
            camp = home / "campaigns" / "amb-e2e"
            self.assertTrue((camp / "AGENTS.md").exists(),
                            "campaign init must deploy the ambient takeover brief")
            self.assertIn("AMBIENT TAKEOVER", (camp / "AGENTS.md").read_text(encoding="utf-8"))
            # idempotent: re-init (--force) must not clobber a hand-edited brief
            (camp / "AGENTS.md").write_text("OPERATOR CUSTOM", encoding="utf-8")
            r = subprocess.run(
                [sys.executable, "scripts/spydermonkey.py", "campaign", "init", "--force",
                 "--target", "amb-e2e", "--objective", "ambient"],
                capture_output=True, text=True, cwd=ROOT, stdin=subprocess.DEVNULL,
                timeout=60, env=env,
            )
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual((camp / "AGENTS.md").read_text(encoding="utf-8"),
                             "OPERATOR CUSTOM", "re-init must not overwrite the brief")
        finally:
            shutil.rmtree(home, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
