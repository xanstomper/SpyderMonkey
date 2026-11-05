#!/usr/bin/env python3
"""SPYDERMONKEY stdlib test suite — scope, contracts, CLI, ledger, kernel.

Run:  python3 -m unittest discover -s tests -v

Every CLI test runs in a throwaway HOME with its own scope file and campaign
root. Nothing here touches ~/.redteam or a real estate.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
DISPATCHER = SCRIPTS / "spydermonkey.py"
sys.path.insert(0, str(SCRIPTS))
import scope_authority as sa  # noqa: E402


def run(args, env, timeout=90):
    return subprocess.run([sys.executable] + args, cwd=str(ROOT), env=env,
                          capture_output=True, text=True, timeout=timeout)


class ScopeUnitTests(unittest.TestCase):
    def scope(self, **kw):
        base = {"schema": 2, "engagement": "test",
                "in_scope": ["example.test", "*.api.example.test",
                             "10.0.0.0/24", "203.0.113.7:8443",
                             "https://shop.example.test/v1"],
                "out_of_scope": ["billing.example.test", "10.0.0.5"],
                "rules": {"max_rate_rps": 10, "allow_lab": True},
                "expires": None}
        base.update(kw)
        return base

    def test_exact_and_subdomain(self):
        s = self.scope()
        self.assertTrue(sa.match(s, "https://example.test/x")[0])
        self.assertTrue(sa.match(s, "https://deep.example.test/x")[0])
        self.assertFalse(sa.match(s, "https://notexample.test/x")[0])

    def test_wildcard_is_subdomains_only(self):
        s = self.scope(in_scope=["*.api.example.test"])
        self.assertTrue(sa.match(s, "https://v2.api.example.test/x")[0])
        self.assertFalse(sa.match(s, "https://api.example.test/x")[0])

    def test_cidr_and_port(self):
        s = self.scope()
        self.assertTrue(sa.match(s, "http://10.0.0.9/")[0])
        self.assertFalse(sa.match(s, "http://10.0.1.9/")[0])
        self.assertTrue(sa.match(s, "https://203.0.113.7:8443/")[0])
        self.assertFalse(sa.match(s, "https://203.0.113.7:443/")[0])

    def test_path_constraint(self):
        s = self.scope(in_scope=["https://shop.example.test/v1"])
        self.assertTrue(sa.match(s, "https://shop.example.test/v1/orders")[0])
        self.assertFalse(sa.match(s, "https://shop.example.test/v2/orders")[0])

    def test_deny_beats_allow(self):
        s = self.scope()
        ok, reason = sa.match(s, "https://billing.example.test/x")
        self.assertFalse(ok)
        self.assertIn("denied", reason)
        self.assertFalse(sa.match(s, "http://10.0.0.5/")[0])

    def test_expiry_closes_everything(self):
        s = self.scope(expires="2000-01-01T00:00:00+00:00")
        ok, reason = sa.match(s, "https://example.test/")
        self.assertFalse(ok)
        self.assertIn("expired", reason)

    def test_none_scope_is_default_deny(self):
        self.assertFalse(sa.match(None, "https://example.test/")[0])

    def test_validate_rejects_malformed_entries(self):
        with self.assertRaises(sa.ScopeError):
            sa.validate({"in_scope": ["*.bad"], "rules": {}})
        with self.assertRaises(sa.ScopeError):
            sa.validate({"in_scope": ["host:99999"], "rules": {}})
        sa.validate(self.scope())

    def test_safe_name_blocks_traversal(self):
        self.assertEqual(sa.safe_name("acme-p1"), "acme-p1")
        for bad in ("../etc", "a/b", ".hidden", "", "..", "a\\b"):
            with self.assertRaises(sa.ScopeError):
                sa.safe_name(bad)


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="spydermonkey-test-"))
        self.env = os.environ.copy()
        self.env.update({
            "HOME": str(self.tmp),
            "SPYDERMONKEY_HOME": str(self.tmp / ".redteam"),
            "SPYDERMONKEY_SCOPE": str(self.tmp / "scope.json"),
            "SM_SELFTEST": "1",
        })
        r = self.cli(["scope", "init", "--engagement", "test",
                      "--in-scope", "example.test,10.0.0.0/24",
                      "--out-of-scope", "billing.example.test", "--json"])
        self.assertEqual(r.returncode, 0, r.stderr)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def cli(self, args, timeout=90):
        return run([str(DISPATCHER)] + args, self.env, timeout=timeout)

    def j(self, args, expect=0):
        r = self.cli(args)
        self.assertEqual(r.returncode, expect, f"{args}\n{r.stdout}\n{r.stderr}")
        return json.loads(r.stdout) if r.stdout.strip() else None

    def test_version_and_tree(self):
        v = self.j(["version", "--json"])
        self.assertEqual(v["version"], "5.2.0")
        self.assertEqual(v["schema"], 4)
        t = self.j(["tree", "--json"])
        self.assertEqual(len(t["mandates"]), 10)
        self.assertEqual(t["mandates"][0]["name"], "barbican")

    def test_global_json_after_subcommand(self):
        v = self.j(["version", "--json"])
        self.assertEqual(v["name"], "spydermonkey")
        r = self.j(["route", "--goal", "protect my opsec", "--json"])
        self.assertEqual(r["primary"], "barbican")

    def test_scope_deny_exit_1_and_audit(self):
        r = self.cli(["scope", "check", "--value", "https://evil.test/", "--json"])
        self.assertEqual(r.returncode, 1)
        payload = json.loads(r.stdout)
        self.assertFalse(payload["in_scope"])
        h = self.j(["scope", "history", "--json"])
        self.assertGreaterEqual(len(h["history"]), 1)

    def test_scope_file_is_private(self):
        p = Path(self.env["SPYDERMONKEY_SCOPE"])
        self.assertEqual(oct(p.stat().st_mode & 0o777), "0o600")

    def test_ledger_confirm_dedupe_integrity_export(self):
        proof = ("baseline: GET /api/x?org=acme -> 200 acme; "
                 "attack: GET /api/x?org=other -> 200 other; "
                 "diff: tenant echoed from the query")
        a = self.j(["ledger", "add", "--target", "t1", "--title", "cross-tenant read",
                    "--cls", "IDOR", "--asset", "https://example.test/api/x",
                    "--proof", proof, "--json"])
        self.assertEqual(a["finding"]["status"], "CONFIRMED")
        self.assertFalse(a["duplicate"])
        b = self.j(["ledger", "add", "--target", "t1", "--title", "cross-tenant read",
                    "--cls", "IDOR", "--asset", "https://example.test/api/x",
                    "--proof", "second sample", "--json"])
        self.assertTrue(b["duplicate"])
        self.assertEqual(a["finding"]["id"], b["finding"]["id"])
        v = self.j(["ledger", "verify", "--target", "t1", "--json"])
        self.assertTrue(v["ok"])
        sarif = self.j(["ledger", "export", "--target", "t1", "--format", "sarif",
                        "--output", "-", "--json"])
        self.assertEqual(sarif["version"], "2.1.0")

    def test_ledger_refuses_out_of_scope_asset(self):
        r = self.cli(["ledger", "add", "--target", "t1", "--title", "outside",
                      "--asset", "https://evil.test/x", "--proof",
                      "baseline: a; attack: b; diff: c", "--json"])
        self.assertEqual(r.returncode, 1)

    def test_campaign_lifecycle(self):
        c = self.j(["campaign", "init", "--target", "camp1",
                    "--objective", "test engagement", "--json"])
        self.assertEqual(c["campaign"]["target"], "camp1")
        l = self.j(["campaign", "list", "--json"])
        self.assertTrue(any(x["target"] == "camp1" for x in l["campaigns"]))
        t = self.j(["campaign", "timeline", "--target", "camp1", "--json"])
        self.assertGreaterEqual(t["count"], 1)
        a = self.j(["campaign", "archive", "--target", "camp1", "--json"])
        self.assertGreater(a["bytes"], 0)
        r = self.cli(["campaign", "purge", "--target", "camp1"])
        self.assertEqual(r.returncode, 2)
        p = self.j(["campaign", "purge", "--target", "camp1", "--force", "--json"])
        self.assertTrue(p["purged"])

    def test_contracts_and_bench(self):
        m = self.j(["mandates", "verify", "--json"])
        self.assertTrue(m["ok"])
        self.assertEqual(m["count"], 10)
        b = self.j(["bench", "--json"])
        self.assertEqual(b["passed"], b["total"])
        self.assertGreaterEqual(b["accuracy"], 100.0)

    def test_kernel_next_is_state_driven(self):
        d = self.j(["next", "--target", "camp1", "--domain", "example.test", "--json"])
        self.assertFalse(d["done"])
        self.assertEqual(d["next"]["directive_id"], "barbican-posture")
        self.assertIn("argv", d["next"])
        self.assertTrue(d["next"]["walls"])
        self.assertIn("command", d["next"])

    def test_report_defaults_to_campaign_dir(self):
        self.j(["ledger", "add", "--target", "camp1", "--title", "probe",
                "--cls", "IDOR", "--asset", "https://example.test/x",
                "--proof", "baseline: a; attack: b; diff: c", "--json"])
        out = self.tmp / "report.md"
        r = self.cli(["report", "--target", "camp1", "--format", "markdown",
                      "--output", str(out)])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Executive summary", out.read_text())
        default = self.cli(["report", "--target", "camp1"])
        self.assertEqual(default.returncode, 0, default.stderr)
        self.assertTrue(list((self.tmp / ".redteam" / "campaigns" / "camp1")
                             .glob("*report*")))

    def test_usage_errors_are_2(self):
        self.assertEqual(self.cli(["route"]).returncode, 2)
        self.assertEqual(self.cli(["ledger", "add", "--target", "t1"]).returncode, 2)
        self.assertEqual(self.cli(["campaign", "purge", "--target", "no-such"]).returncode, 2)

    def test_unknown_campaign_name_is_rejected(self):
        r = self.cli(["campaign", "init", "--target", "../escape"])
        self.assertEqual(r.returncode, 2)
        self.assertIn("invalid", r.stderr.lower())

    def test_skilltree_verify_and_count(self):
        c = self.j(["bench", "--json"])  # keep the suite warm; dispatcher still healthy
        self.assertTrue(c)
        r = run([str(SCRIPTS / "skilltree.py"), "--verify", "--json"], self.env)
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertTrue(data["ok"])
        # base + expanded corpus = every file indexed (the context corpus is
        # committed, so expanded_links must hold the 7k+ scale floor)
        self.assertEqual(data["links"] + data["expanded_links"], data["files"])
        self.assertGreaterEqual(data["expanded_links"], 10000)
        self.assertEqual(data["orphans"], 0)

    def test_mcp_surface(self):
        r = run([str(SCRIPTS / "mcp_server.py"), "--test"], self.env)
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(data["version"], "5.2.0")
        self.assertGreaterEqual(len(data["tools"]), 43)
        self.assertIn("skilltree_verify", data["tools"])

    def test_mcp_stdio_tools_list_and_call(self):
        req = "\n".join([
            json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}),
            json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                        "params": {"name": "version", "arguments": {}}}),
        ]) + "\n"
        r = subprocess.run([sys.executable, str(SCRIPTS / "mcp_server.py")],
                           input=req, cwd=str(ROOT), env=self.env,
                           capture_output=True, text=True, timeout=90)
        self.assertEqual(r.returncode, 0, r.stderr)
        lines = [json.loads(l) for l in r.stdout.splitlines() if l.strip()]
        self.assertEqual(len(lines), 2)
        self.assertGreaterEqual(len(lines[0]["result"]["tools"]), 43)
        self.assertIn("5.2.0", json.dumps(lines[1]["result"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
