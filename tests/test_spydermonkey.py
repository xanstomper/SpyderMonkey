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
import time
import unittest
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
DISPATCHER = SCRIPTS / "spydermonkey.py"
sys.path.insert(0, str(SCRIPTS))
import scope_authority as sa  # noqa: E402
import spydermonkey as sm  # noqa: E402


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
        self.assertEqual(v["version"], sm.VERSION)
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

    def test_mandate_pack_is_complete_and_compact(self):
        r = self.cli(["mandate", "--pack"])
        self.assertEqual(r.returncode, 0, r.stderr)
        text = r.stdout
        for marker in ("THE WALLS", "DECLARED ESTATES ONLY", "DOCUMENTED-PoC",
                       "NEVER THIRD PARTIES", "THE KERNEL LOOP", "THE EVIDENCE CONTRACT",
                       "THE ROUTE TABLE", "3-gate", "hypothesis conf 0.4",
                       "---8<--- END MANDATE PACK ---8<---"):
            self.assertIn(marker, text, marker)
        self.assertLess(len(text.split()), 2600, "pack must stay under ~3k tokens")
        p = self.cli(["mandate", "--pack", "--file"])
        self.assertEqual(p.returncode, 0)
        self.assertTrue(Path(p.stdout.strip()).exists(), p.stdout)

    def test_inject_context_packet(self):
        r = self.cli(["inject", "--target", "camp1", "--goal",
                      "find jwt ssrf in the api", "--json"])
        self.assertEqual(r.returncode, 0, r.stderr)
        p = json.loads(r.stdout)
        self.assertIn("undercroft", p["route"]["sequence"])
        self.assertTrue(p["walls"].startswith("declared estates only"))
        self.assertGreaterEqual(len(p["knowledge"]), 1)
        t = self.cli(["inject", "--target", "camp1", "--goal", "privesc sudo suid"])
        self.assertEqual(t.returncode, 0, t.stderr)
        self.assertIn("KNOWLEDGE", t.stdout)
        self.assertIn("ROUTE", t.stdout)

    def test_context_router_is_deterministic(self):
        import context_router as crr
        a = crr.query("jwt forge", top=4)
        b = crr.query("jwt forge", top=4)
        self.assertEqual(a, b)
        self.assertTrue(a)
        self.assertTrue(all(h["kind"] in ("canon", "skill", "expanded", "tool",
                                          "sigma", "cve", "capec", "gtfobin")
                            for h in a))
        idx = crr.build_index()
        counts = {}
        for d in idx["docs"]:
            counts[d["k"]] = counts.get(d["k"], 0) + 1
        self.assertGreaterEqual(counts.get("canon", 0), 29,
                                "numbered technique-canon volumes must be indexed")
        self.assertGreaterEqual(counts.get("sigma", 0), 3000,
                                "sigma knowledge lane must be present")
        self.assertGreaterEqual(counts.get("gtfobin", 0), 400,
                                "gtfobin lane must be present")

    def test_ledger_feeds_shared_weight_store(self):
        mem = Path(self.env["SPYDERMONKEY_HOME"]) / "memory" / "spydermonkey-priors.json"
        if mem.exists():
            mem.unlink()
        proof = ("baseline: GET /api/x?org=acme -> 200 acme; "
                 "attack: GET /api/x?org=other -> 200 other; "
                 "diff: tenant echoed from the query")
        self.j(["ledger", "add", "--target", "t1", "--title", "tenant read",
                "--cls", "IDOR", "--asset", "https://example.test/api/x",
                "--proof", proof, "--json"])
        pr = json.loads(mem.read_text())
        self.assertEqual(pr["IDOR"]["hits"], 1)
        self.assertEqual(pr["IDOR"]["runs"], 1)
        self.assertIn("last", pr["IDOR"])  # v7.6.3: decay timestamp stamped
        self.j(["ledger", "add", "--target", "t1", "--title", "weak guess",
                "--cls", "IDOR", "--asset", "https://example.test/api/x",
                "--proof", "same response both ways", "--json"])
        pr = json.loads(mem.read_text())
        self.assertEqual(pr["IDOR"]["runs"], 2)
        self.assertEqual(pr["IDOR"]["hits"], 1)
        self.j(["ledger", "add", "--target", "t1", "--title", "tenant read",
                "--cls", "IDOR", "--asset", "https://example.test/api/x",
                "--proof", proof, "--json"])
        pr = json.loads(mem.read_text())
        self.assertEqual(pr["IDOR"]["hits"], 1)
        self.assertEqual(pr["IDOR"]["runs"], 2)  # duplicates must not re-learn
        self.j(["ledger", "add", "--target", "t1", "--title", "lab probe",
                "--cls", "SSRF", "--asset", "http://127.0.0.1:9999/fetch",
                "--proof", proof, "--json"])
        pr = json.loads(mem.read_text())
        self.assertNotIn("SSRF", pr, "lab rows must stay out of the weight store")

    def test_fleet_writes_squad_briefs(self):
        r = self.cli(["fleet", "--goal", "find api bugs and take them over",
                      "--target", "camp1", "--domain", "example.test",
                      "--dry-run", "--json"])
        self.assertEqual(r.returncode, 0, r.stderr)
        brief_root = Path(self.env["SPYDERMONKEY_HOME"]) / "campaigns" / "camp1" / "fleet"
        briefs = list(brief_root.glob("*.brief.md"))
        self.assertGreaterEqual(len(briefs), 3)
        txt = briefs[0].read_text()
        self.assertIn("WALLS: declared estates only", txt)
        self.assertIn("one-paste pack", txt)
        self.assertIn("## Lane knowledge", txt)

    def test_kairo_validate_range_gate(self):
        kairo = Path.home() / ".hermes" / "skills" / "security" / "kairo" \
            / "scripts" / "kairo.py"
        if not kairo.exists():
            self.skipTest("kairo engine not on disk")
        camp = Path(self.env["HOME"]) / ".redteam" / "campaigns" / "kfly"
        camp.mkdir(parents=True, exist_ok=True)
        (camp / "hardware-state.json").write_text(json.dumps({"vectors": [
            {"id": "V-1", "class": "AUTHBYPASS", "technique": "t", "proof": "p",
             "delta": "d", "source": "s", "target": "https://example.test/api"},
            {"id": "V-2", "class": "MOBILEX", "technique": "t", "proof": "p",
             "delta": "d", "source": "s", "target": "device-x"},
        ]}))
        r = run([str(kairo), "validate", "--target", "kfly"],
                self.env, timeout=120)
        self.assertEqual(r.returncode, 0, r.stderr)
        st = json.loads((camp / "hardware-state.json").read_text())
        by_id = {v["id"]: v for v in st["vectors"]}
        self.assertIs(by_id["V-1"]["validated"], True,
                      "AUTHBYPASS must range-prove via dojo AUTHN")
        self.assertIsNone(by_id["V-2"]["validated"],
                          "still-no-replica classes stay honest, never validated")

    def test_fleet_agent_loop_and_foundation(self):
        """THE FLEET LANE: controller → beacon agent → gated node execution →
        kernel-schema result, end to end on localhost. Plus the foundation."""
        f = self.cli(["foundation", "--file"])
        self.assertEqual(f.returncode, 0)
        fpath = Path(f.stdout.strip())
        self.assertTrue(fpath.exists())
        spec = fpath.read_text()
        for layer in ("L0 PERSONA", "L1 ESTATE", "L2 EVIDENCE", "L3 ENGINES",
                      "L4 KNOWLEDGE", "L5 SYNTHESIS", "L6 FLEET", "L7 MIRROR"):
            self.assertIn(layer, spec)

        import socket as _s
        agent = Path(ROOT / "scripts" / "fleet_agent.py")
        if not agent.exists():
            self.skipTest("fleet_agent not on disk")
        node_home = Path(self.tmp) / "node-home"
        ctrl_dir = Path(self.tmp) / "ctrl"
        node_home.mkdir(); ctrl_dir.mkdir()
        env = {**os.environ, "SPYDERMONKEY_HOME": str(node_home)}
        r = run([str(DISPATCHER), "scope", "init", "--engagement", "fleet-test",
                 "--in-scope", "node.example.test"], env, timeout=60)
        self.assertEqual(r.returncode, 0, r.stderr)

        s = _s.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
        ctrl = subprocess.Popen([sys.executable, str(agent), "controller",
                                 "--port", str(port), "--node-dir", str(ctrl_dir)],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        ag = subprocess.Popen([sys.executable, str(agent), "agent",
                               "--controller", f"http://127.0.0.1:{port}",
                               "--interval", "1", "--home", str(node_home)],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            time.sleep(2.5)
            req = urllib.request.Request(
                f"http://127.0.0.1:{port}/task",
                data=json.dumps({"id": "T-TEST-1", "node": "node-home",
                                 "command": ["version", "--json"]}).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            urllib.request.urlopen(req, timeout=5).read()
            res_path = None
            for _ in range(20):
                cand = ctrl_dir / "node-home" / "T-TEST-1.json"
                if cand.exists():
                    res_path = cand
                    break
                time.sleep(1)
            self.assertIsNotNone(res_path, "result never landed")
            res = json.loads(res_path.read_text())
            self.assertTrue(res["ok"], res.get("output", "")[:300])
            self.assertEqual(json.loads(res["output"])["version"], sm.VERSION)
        finally:
            ctrl.terminate(); ag.terminate()

    def test_taint_boundary_pass(self):
        """THE BOUNDARY PASS (v7.5.1): cli/env-fed sinks downgrade, request-fed
        stays hot — the llama-stack FP class, fixed."""
        import discover_taint as dtt
        fps = {
            "env": ('def fetch(self, base_url, api_key):\n'
                    '    env = {**os.environ, "OPENAI_API_KEY": api_key}\n'
                    '    result = subprocess.run(["codex"], env=env)\n'),
            "cli": ('def install():\n'
                    '    subprocess.run(["sh", script_path] + sys.argv[1:])\n'),
        }
        for key, src in fps.items():
            hits = dtt.analyze(src, f"{key}.py")
            self.assertTrue(hits, key)
            for h in hits:
                self.assertEqual(h["boundary"], key, key)
                self.assertEqual(h["score"], 2, key)
                self.assertEqual(h["sev"], "low", key)
        hot = ('def handler():\n'
               '    host = request.args.get("host")\n'
               '    subprocess.run(["sh", "-c", "ping " + host])\n')
        hits = dtt.analyze(hot, "hot.py")
        self.assertTrue(hits)
        self.assertEqual(hits[0]["boundary"], "request")
        self.assertGreaterEqual(hits[0]["score"], 5)

    def test_hypothesis_cards_cite_cve_instances(self):
        """v7.6.1 — cve-map cards cite REAL catalog instances: the reasoning
        carries CVE→exploit evidence from the committed 66.5k corpus."""
        import hypothesis as hp
        state = {"arsenal": {"runs": [{"findings": ["php"]}]},
                 "context": {"fingerprints": ["php"]}}
        cards = hp.cve_hypotheses(state, "smoke.example.test", limit=10)
        self.assertTrue(cards)
        for c in cards:
            self.assertIn("instances", c)
        cited = [c for c in cards if c.get("instances")]
        self.assertTrue(cited, "php fingerprints must surface catalog CVE cites")
        self.assertIn("CVE-", cited[0]["instances"][0])

    def test_retrieval_kind_balancing(self):
        """v7.6.3 — mix=True: canon/skill/tool/sigma each get seats; the 138k
        expanded corpus can't shout over the curated lanes."""
        import context_router as crr
        hits = crr.query("kerberos", top=8, budget=None, mix=True)
        self.assertTrue(hits)
        kinds_present = {h["kind"] for h in hits}
        # a multi-lane term must surface more than the expanded flood
        self.assertGreaterEqual(len(kinds_present), 2,
                                f"kind-balancing failed: {kinds_present}")
        pure = crr.query("kerberos", top=8, budget=None, mix=False)
        self.assertTrue(pure)  # mix=False still returns ranked hits
        # determinism holds under mix
        self.assertEqual(hits, crr.query("kerberos", top=8, budget=None, mix=True))

    def test_planner_fuzz_lane_and_artifact_verify(self):
        """v7.6.3 — materialized artifacts route the planner into the fuzz
        lane; artifacts verify well-formed."""
        import spydermonkey as smod
        d = Path(self.tmp) / "artcheck"
        d.mkdir()
        (d / "t.yml").write_text("id: x\ninfo:\n  name: y\n")
        (d / "bad.py").write_text("def (:\n")
        self.assertTrue(smod._verify_artifact(d / "t.yml")[0])
        self.assertFalse(smod._verify_artifact(d / "bad.py")[0])
        # planner: walk directives to fixed point; fuzz-lane must fire.
        # IN-PROCESS ISOLATION: smod reads the real env — wrap it or the walk
        # pollutes ~/.redteam (the live-engagement home) and cross-run state
        # makes the test order-dependent.
        old_home = os.environ.get("SPYDERMONKEY_HOME")
        old_scope = os.environ.get("SPYDERMONKEY_SCOPE")
        os.environ["SPYDERMONKEY_HOME"] = str(self.env["SPYDERMONKEY_HOME"])
        os.environ["SPYDERMONKEY_SCOPE"] = str(self.env["SPYDERMONKEY_SCOPE"])
        try:
            camp = Path(self.env["SPYDERMONKEY_HOME"]) / "campaigns" / "fz"
            (camp / "materialized").mkdir(parents=True, exist_ok=True)
            (camp / "materialized" / "x.bin").write_bytes(b"\x00\x01")
            seen = set()
            for _ in range(40):
                dv = smod._planner_directive("fz", url="http://127.0.0.1:9",
                                             domain="example.test")
                if dv is None:
                    break
                if dv["directive_id"] == "fuzz-lane":
                    self.assertIn("fuzz-file", " ".join(dv["argv"]))
                    break
                seen.add(dv["directive_id"])
                st = smod._kernel_state("fz")
                st["steps"].append({"directive_id": dv["directive_id"],
                                    "absorbed": True})
                smod._kernel_save("fz", st)
            else:
                self.fail(f"fuzz-lane never emitted; saw {sorted(seen)}")
            self.assertIn("barbican-posture", seen)  # the walk advanced
        finally:
            if old_home is None:
                os.environ.pop("SPYDERMONKEY_HOME", None)
            else:
                os.environ["SPYDERMONKEY_HOME"] = old_home
            if old_scope is None:
                os.environ.pop("SPYDERMONKEY_SCOPE", None)
            else:
                os.environ["SPYDERMONKEY_SCOPE"] = old_scope

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
        self.assertEqual(data["version"], sm.VERSION)
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
        self.assertIn(sm.VERSION, json.dumps(lines[1]["result"]))

    # ── v7.2 acquisition lane ────────────────────────────────────────────────

    def test_arsenal_install_plan_covers_hw_esp(self):
        d = self.j(["arsenal", "install", "--chain", "hw-esp", "--json"])
        names = {t["tool"] for t in d["tools"]}
        self.assertTrue({"esptool", "mosquitto_sub", "mosquitto_pub"} <= names)
        self.assertEqual(d["machine"], "none (plan only)")
        self.assertIn("to_install", d)

    def test_arsenal_install_plan_covers_hw_audio(self):
        d = self.j(["arsenal", "install", "--chain", "hw-audio", "--json"])
        names = {t["tool"] for t in d["tools"]}
        self.assertTrue({"sox", "ffmpeg", "minimodem", "multimon-ng"} <= names)
        managed = [t for t in d["tools"] if not t["installed"] and t["managed"]]
        self.assertTrue(managed)  # recipes exist, not all guessed

    def test_arsenal_install_recipe_resolution(self):
        import arsenal as ars
        r = ars.resolve_install("esptool")
        self.assertTrue(r["managed"])
        self.assertTrue(r["cmds"])
        r2 = ars.resolve_install("binwalk")
        self.assertTrue(r2["managed"])
        self.assertTrue(r2["cmds"])
        r3 = ars.resolve_install("no-such-tool-zzz")
        # unknown: every family probe class can degrade safely — guess or manual,
        # but never a crash and never an unlabelled command
        self.assertIn(r3["managed"], (True, False))
        for c in r3["cmds"]:
            self.assertIn(c["manager"], ("apt", "pip", "cargo", "go", "npm", "gem",
                                         "dnf", "pacman", "apk", "brew"))

    def test_arsenal_verify_covers_install_map(self):
        r = run([str(SCRIPTS / "arsenal.py"), "verify"], self.env)
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)

    # ── v7.3 catalog materialization ─────────────────────────────────────────

    def test_catalog_runbook_all_kinds(self):
        for kind, ident in (("exploit-db", "edb-16929"),
                            ("nuclei", "CVE-2012-4242"),
                            ("metasploit", "msf-auxiliary-admin-2wire-xslt_password_reset")):
            r = self.cli(["catalog", "runbook", "--kind", kind, "--id", ident])
            self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
            self.assertIn("gate", r.stdout.lower() + r.stderr.lower())
        # a real nuclei CVE from the surge resolves to a real template path
        d = self.j(["catalog", "runbook", "--kind", "nuclei", "--id",
                    "CVE-2012-4242", "--json"])
        self.assertTrue(d["ok"])
        self.assertIn("cves/2012/CVE-2012-4242.yaml", d["path"])
        # the EDB runbook carries the build/run recipe (the how-to-perform)
        e = self.j(["catalog", "runbook", "--kind", "exploit-db", "--id",
                    "edb-16929", "--json"])
        self.assertTrue(any("build" in s for s in e["steps"]))
        self.assertTrue(any("gcc" in s for s in e["steps"]))

    def test_catalog_materialize_dry_run_touches_nothing(self):
        before = set((Path(self.env["SPYDERMONKEY_HOME"])).glob("*")) if \
            Path(self.env["SPYDERMONKEY_HOME"]).exists() else set()
        r = self.cli(["catalog", "materialize", "--kind", "exploit-db",
                      "--id", "edb-16929", "--dry-run", "--json"])
        self.assertEqual(r.returncode, 0, r.stderr)
        d = json.loads(r.stdout)
        self.assertTrue(d["ok"])
        self.assertTrue(any("16929" in e for e in d["events"]))
        after = set((Path(self.env["SPYDERMONKEY_HOME"])).glob("*")) if \
            Path(self.env["SPYDERMONKEY_HOME"]).exists() else set()
        self.assertEqual(before, after)  # no mirror, no artifact — dry-run held

    def test_arsenal_url_lane_resolves_before_go(self):
        import arsenal as ars
        r = ars.resolve_install("nuclei")
        self.assertTrue(r["managed"])
        self.assertTrue(any(c["manager"] == "url" for c in r["cmds"]))

    def test_catalog_show_carries_how(self):
        d = self.j(["catalog", "show", "edb-16929", "--json"])
        self.assertEqual(d["tool"]["src"], "exploit-db")
        self.assertIn("materialize", d["tool"]["how"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
