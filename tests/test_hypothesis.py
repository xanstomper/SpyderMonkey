#!/usr/bin/env python3
"""SPYDERMONKEY hypothesis-engine tests — pure reasoning, no live fire.

Run:  python3 -m unittest discover -s tests -v

Every test builds synthetic family state in memory (or a throwaway campaign
dir). Nothing touches ~/.redteam, no scope authority is needed, and no
request ever leaves the process.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
import hypothesis as hy  # noqa: E402


def _row(id, cls, asset, status="CONFIRMED", proof=""):
    return {"id": id, "cls": cls, "asset": asset, "status": status,
            "severity": "high", "proof": proof,
            "title": f"{cls} on {asset}"}


def _state(ledger=None, endpoints=None, fingerprints=None):
    return {
        "context": {"endpoints": endpoints or [], "roles": [],
                    "credentials": [], "functions": []},
        "ledger": ledger or [],
        "priors": {},
        "arsenal": {"runs": (["x-powered-by: express"] if fingerprints else [])},
        "chains": [],
    }


class SurfaceTests(unittest.TestCase):
    def test_param_shape_maps_to_classes(self):
        st = _state(endpoints=["http://lab.test/api/orders?org_id=acme"])
        cards = hy.surface_hypotheses(st, "t")
        classes = {c["cls"] for c in cards}
        self.assertIn("IDOR", classes)
        self.assertIn("AUTHZ", classes)

    def test_url_shape_maps_to_fetch_classes(self):
        st = _state(endpoints=["http://lab.test/fetch?url=http://x"])
        cards = hy.surface_hypotheses(st, "t")
        classes = {c["cls"] for c in cards}
        self.assertTrue(classes & {"SSRF", "REDIRECT", "CRLF"})

    def test_confirmed_class_on_asset_is_deduped(self):
        ep = "http://lab.test/api/orders?org_id=acme"
        st = _state(ledger=[_row("SPY-001", "IDOR", ep)], endpoints=[ep])
        cards = hy.surface_hypotheses(st, "t")
        self.assertFalse(any(c["cls"] == "IDOR" and c["asset"] == ep
                             for c in cards))

    def test_confirmed_class_on_other_asset_still_proposed(self):
        ep1 = "http://lab.test/api/orders?org_id=acme"
        ep2 = "http://lab.test/api/users?id=7"
        st = _state(ledger=[_row("SPY-001", "IDOR", ep1)], endpoints=[ep1, ep2])
        cards = hy.surface_hypotheses(st, "t")
        self.assertTrue(any(c["cls"] == "IDOR" and c["asset"] == ep2
                            for c in cards))

    def test_query_form_never_defeats_dedupe(self):
        # the gate stores the request form; the context may carry another —
        # scheme+host+path is the dedupe key
        ep = "http://lab.test/file?path=etc"
        st = _state(ledger=[_row("SPY-001", "TRAVERSAL", ep)], endpoints=[ep])
        cards = hy.surface_hypotheses(st, "t")
        self.assertFalse(any(c["cls"] == "TRAVERSAL" for c in cards))

    def test_every_card_carries_walls_and_citations(self):
        st = _state(endpoints=["http://lab.test/api/orders?org_id=acme"])
        for c in hy.surface_hypotheses(st, "t"):
            self.assertTrue(c["walls"])
            self.assertIn("declared estates only", c["walls"])
            self.assertTrue(c["citations"])
            self.assertTrue(c["why"])
            self.assertIn("probe", c)


class CveMapTests(unittest.TestCase):
    def test_fingerprint_maps_to_documented_family(self):
        st = _state(fingerprints=True)
        cards = hy.cve_hypotheses(st, "t")
        self.assertTrue(any(c["cls"] == "NOSQL" for c in cards))
        self.assertTrue(all("CWE-" in c["title"] for c in cards))

    def test_no_fingerprint_no_cards(self):
        st = _state()
        self.assertEqual(hy.cve_hypotheses(st, "t"), [])


class VariantTests(unittest.TestCase):
    def test_confirmed_finding_opens_variant_families(self):
        proof = ("baseline: http://l/fetch?url=http://example.com → 200; "
                 "attack: http://l/fetch?url=http://127.0.0.1:9/ → 200; diff: ok")
        st = _state(ledger=[_row("SPY-007", "SSRF", "http://l/fetch?url=x",
                                 proof=proof)])
        cards = hy.variant_hypotheses(st, "t")
        self.assertTrue(cards)
        self.assertTrue(all(c["kind"] == "variant" for c in cards))
        self.assertTrue(all(c.get("parent") == "SPY-007" for c in cards))

    def test_fired_payloads_are_not_reproposed(self):
        # the gate stores the URL-ENCODED form — the fired check must match it
        proof = "attack: http://l/file?path=....%2F%2Fetc%2Fpasswd → 200"
        st = _state(ledger=[_row("SPY-019", "TRAVERSAL", "http://l/file?path=x",
                                 proof=proof)])
        cards = hy.variant_hypotheses(st, "t")
        fam = [c for c in cards if "filter evasion" in c["title"]]
        self.assertTrue(fam)
        self.assertNotIn("....//etc/passwd", fam[0]["probe"]["payloads"])

    def test_hypothesis_rows_open_no_variants(self):
        st = _state(ledger=[_row("SPY-001", "SSRF", "http://l/fetch?url=x",
                                 status="HYPOTHESIS")])
        self.assertEqual(hy.variant_hypotheses(st, "t"), [])


class ChainTests(unittest.TestCase):
    def test_confirmed_need_plus_missing_give(self):
        st = _state(ledger=[_row("SPY-001", "REDIRECT", "http://l/r?next=/")])
        cards = hy.chain_hypotheses(st, "t")
        self.assertTrue(any(c["cls"] in ("AUTHN", "JWT") for c in cards))

    def test_everything_confirmed_closes_the_chains(self):
        ledger = [_row("SPY-001", "REDIRECT", "http://l/r"),
                  _row("SPY-002", "AUTHN", "http://l/login"),
                  _row("SPY-003", "JWT", "http://l/token"),
                  _row("SPY-004", "HARVEST", "http://l/.env"),
                  _row("SPY-005", "SSRF", "http://l/fetch"),
                  _row("SPY-006", "CORS", "http://l/api"),
                  _row("SPY-007", "NOSQL", "http://l/login2"),
                  _row("SPY-008", "AUTHZ", "http://l/admin"),
                  _row("SPY-009", "IDOR", "http://l/api/orders")]
        self.assertEqual(hy.chain_hypotheses(_state(ledger=ledger), "t"), [])


class RankAndBriefTests(unittest.TestCase):
    def test_rank_orders_and_bounds_scores(self):
        st = _state(ledger=[_row("SPY-001", "JWT", "http://l/token")])
        cards = hy.surface_hypotheses(
            _state(endpoints=["http://l/search?q=x",
                              "http://l/redirect?next=/home"]), "t")
        ranked = hy.rank(cards, st)
        scores = [c["score"] for c in ranked]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertTrue(all(0.0 <= s <= 1.0 for s in scores))

    def test_learned_prior_shifts_the_rank(self):
        st = _state(endpoints=["http://l/search?q=x"])
        st["priors"] = {"class_priors": {"XSS": 1.0, "INJECTION": 0.0}}
        ranked = hy.rank(hy.surface_hypotheses(st, "t"), st)
        self.assertEqual(ranked[0]["cls"], "XSS")

    def test_brief_carries_loop_and_rules(self):
        st = _state(endpoints=["http://l/search?q=x"])
        out = hy.generate(st, "t")
        brief = out["brief"]
        self.assertGreaterEqual(len(brief["loop"]), 4)
        self.assertGreaterEqual(len(brief["rules"]), 3)
        self.assertIn("CONFIRMED", " ".join(brief["loop"]))


class PriorsTests(unittest.TestCase):
    """The learned-priors wire: train writes, the ranker reads."""

    def test_global_priors_are_loaded_and_smoothed(self):
        import os
        from unittest import mock
        with tempfile.TemporaryDirectory() as td:
            mem = Path(td) / "memory"
            mem.mkdir()
            (mem / "spydermonkey-priors.json").write_text(json.dumps(
                {"JWT": {"hits": 7, "runs": 7},
                 "AUTHN": {"hits": 1, "runs": 7}}))
            with mock.patch.dict(os.environ, {"SPYDERMONKEY_HOME": td}):
                st = hy.load_state(Path(td))
        cp = st["priors"]["class_priors"]
        self.assertAlmostEqual(cp["JWT"], 8 / 9, places=3)   # Laplace
        self.assertAlmostEqual(cp["AUTHN"], 2 / 9, places=3)

    def test_learned_prior_moves_the_ranking(self):
        st = _state(endpoints=["http://l/search?q=x",
                               "http://l/token?token=a"])
        st["priors"] = {"class_priors": {"JWT": 1.0, "XSS": 0.0,
                                         "INJECTION": 0.0}}
        ranked = hy.rank(hy.surface_hypotheses(st, "t"), st)
        self.assertEqual(ranked[0]["cls"], "JWT")

    def test_boundary_alias_feeds_idor(self):
        st = _state(endpoints=["http://l/api/orders?org_id=acme"])
        st["priors"] = {"class_priors": {"BOUNDARY": 1.0}}
        ranked = hy.rank(hy.surface_hypotheses(st, "t"), st)
        idor = next(c for c in ranked if c["cls"] == "IDOR")
        self.assertGreater(idor["score"], 0.3)


class StateTests(unittest.TestCase):
    def test_ledger_assets_backfill_the_surface(self):
        with tempfile.TemporaryDirectory() as td:
            camp = Path(td)
            (camp / "ledger.jsonl").write_text(
                json.dumps(_row("SPY-001", "IDOR", "http://lab.test/api/x?id=1")) + "\n")
            st = hy.load_state(camp)
            self.assertEqual(hy.observed_surface(st),
                             ["http://lab.test/api/x?id=1"])

    def test_corrupt_ledger_lines_are_skipped(self):
        with tempfile.TemporaryDirectory() as td:
            camp = Path(td)
            (camp / "ledger.jsonl").write_text(
                json.dumps(_row("SPY-001", "IDOR", "http://l/x"))
                + "\n{\"partial\": tru")
            st = hy.load_state(camp)
            self.assertEqual(len(st["ledger"]), 1)


class RunPathTests(unittest.TestCase):
    """The pure request-pair builder behind `hypothesis run` (no network)."""

    @classmethod
    def setUpClass(cls):
        import spydermonkey as sm
        cls.sm = sm

    def test_surface_card_pairs(self):
        card = {"kind": "surface", "cls": "SSRF",
                "asset": "http://l/fetch?url=x",
                "probe": {"method": "GET", "url": "http://l/fetch",
                          "param": "url", "baseline": "url=x",
                          "attacks": ["http://127.0.0.1:9/"]}}
        base, attacks = self.sm._hypothesis_request_pair(card, [])
        self.assertEqual(base["url"], "http://l/fetch?url=x")
        self.assertEqual(len(attacks), 1)
        payload, akw = attacks[0]
        self.assertIn("url=http%3A%2F%2F127.0.0.1%3A9%2F", akw["url"])

    def test_variant_card_uses_parent_asset_param(self):
        ledger = [_row("SPY-001", "TRAVERSAL", "http://l/file?path=etc")]
        card = {"kind": "variant", "cls": "TRAVERSAL", "parent": "SPY-001",
                "asset": "http://l/file?path=etc",
                "probe": {"payloads": ["....//etc/passwd"]}}
        base, attacks = self.sm._hypothesis_request_pair(card, ledger)
        self.assertEqual(base["url"], "http://l/file?path=etc")
        self.assertIn("path=....%2F%2Fetc%2Fpasswd", attacks[0][1]["url"])

    def test_chain_card_is_not_executable(self):
        card = {"kind": "chain", "cls": "AUTHN", "asset": "t",
                "probe": {"note": "plan only"}}
        base, attacks = self.sm._hypothesis_request_pair(card, [])
        self.assertIsNone(base)
        self.assertEqual(attacks, [])

    def test_cors_card_builds_header_pair(self):
        card = {"kind": "surface", "cls": "CORS", "asset": "http://l/api",
                "probe": {"url": "http://l/api"}}
        base, attacks = self.sm._hypothesis_request_pair(card, [])
        self.assertEqual(base["headers"]["Origin"],
                         "https://baseline.probe.invalid")
        self.assertEqual(attacks[0][1]["headers"]["Origin"],
                         "https://cors.probe.invalid")

    def test_shape_successor_placeholder_is_skipped(self):
        ledger = [_row("SPY-001", "IDOR", "http://l/o?id=7")]
        card = {"kind": "variant", "cls": "IDOR", "parent": "SPY-001",
                "asset": "http://l/o?id=7",
                "probe": {"payloads": ["__SHAPE_SUCCESSOR__"]}}
        base, attacks = self.sm._hypothesis_request_pair(card, ledger)
        self.assertEqual(attacks, [])

    def test_path_probe_card_uses_control_baseline(self):
        card = {"kind": "surface", "cls": "HARVEST", "asset": "http://l/debug",
                "probe": {"method": "GET", "base": "http://l/",
                          "paths": [".env", "debug"], "control": "__ctl__"}}
        base, attacks = self.sm._hypothesis_request_pair(card, [])
        self.assertEqual(base["url"], "http://l/__ctl__")
        self.assertEqual([a[1]["url"] for a in attacks],
                         ["http://l/.env", "http://l/debug"])

    def test_cve_map_path_card_derives_origin_from_ledger(self):
        ledger = [_row("SPY-001", "IDOR", "https://app.test/api/x?id=1")]
        card = {"kind": "cve-map", "cls": "HARVEST", "asset": "campaign-x",
                "probe": {"paths": ("actuator/env",)}}
        base, attacks = self.sm._hypothesis_request_pair(card, ledger)
        self.assertEqual(base["url"],
                         "https://app.test/__spydermonkey_control__")
        self.assertEqual(attacks[0][1]["url"],
                         "https://app.test/actuator/env")


if __name__ == "__main__":
    unittest.main()


class FlowCardTests(unittest.TestCase):
    """v5.13 — multi-step flow cards: marker substitution + sequence shape."""

    @classmethod
    def setUpClass(cls):
        import spydermonkey as sm
        cls.sm = sm

    CARD = {"kind": "surface", "cls": "AUTHN", "asset": "http://l/app",
            "probe": {"flow": [
                {"method": "GET", "url": "http://l/login"},
                {"method": "POST", "url": "http://l/api/auth/login/",
                 "body": "user=b&pass=p&otb=__PAYLOAD__",
                 "headers": {"X-OTB": "__PAYLOAD__"}},
                {"method": "GET", "url": "http://l/api/orders"}],
                "payloads": ["reused-otb", "malformed"],
                "baseline": "fresh-otb"}}

    def test_flow_baseline_substitutes_marker(self):
        base, _ = self.sm._hypothesis_request_pair(self.CARD, [])
        self.assertIn("flow", base)
        self.assertIn("fresh-otb", base["flow"][1]["body"])
        self.assertNotIn("__PAYLOAD__", base["flow"][1]["body"])
        self.assertEqual(base["flow"][1]["headers"]["X-OTB"], "fresh-otb")

    def test_flow_attacks_each_substitute(self):
        _, attacks = self.sm._hypothesis_request_pair(self.CARD, [])
        self.assertEqual([p for p, _ in attacks], ["reused-otb", "malformed"])
        self.assertIn("reused-otb", attacks[0][1]["flow"][1]["body"])
        self.assertIn("reused-otb", attacks[0][1]["flow"][1]["headers"]["X-OTB"])
        self.assertIn("malformed", attacks[1][1]["flow"][1]["body"])

    def test_flow_chain_card_without_payloads_not_executable(self):
        card = {"kind": "chain", "cls": "AUTHN", "asset": "t",
                "probe": {"flow": [{"url": "http://l/"}]}}
        base, attacks = self.sm._hypothesis_request_pair(card, [])
        self.assertIsNone(base)
        self.assertEqual(attacks, [])


class FlowTokenCarryoverTests(unittest.TestCase):
    """v5.16 — token carryover: save_as/{{name}} substitution across a live flow."""

    @classmethod
    def setUpClass(cls):
        import spydermonkey as sm
        cls.sm = sm
        import threading
        from http.server import BaseHTTPRequestHandler, HTTPServer
        seen = {}

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a): pass
            def _send(self, code, body):
                self.send_response(code)
                self.send_header("Content-Length", len(body))
                self.end_headers()
                self.wfile.write(body.encode())
            def do_GET(self):
                if self.path == "/login":
                    self._send(200, '{"token": "tkn_deadbeef"}')
                elif self.path == "/me":
                    seen["auth"] = self.headers.get("Authorization", "")
                    ok = seen["auth"] == "Bearer tkn_deadbeef"
                    self._send(200 if ok else 401,
                               '{"authenticated": %s}' % str(ok).lower())
                else:
                    self._send(404, "{}")

        cls.srv = HTTPServer(("127.0.0.1", 8893), H)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.seen = seen

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    FLOW = [
        {"method": "GET", "url": "http://127.0.0.1:8893/login",
         "save_as": "token", "save_from": "body",
         "save_pattern": r'"token":\s*"([^"]+)"'},
        {"method": "GET", "url": "http://127.0.0.1:8893/me",
         "headers": {"Authorization": "Bearer {{token}}"}},
    ]

    def test_token_extracted_and_carried(self):
        out = self.sm._flow_http(self.FLOW, timeout=5)
        self.assertEqual(out["status"], 200)
        self.assertEqual(self.seen["auth"], "Bearer tkn_deadbeef")
        self.assertIn('"authenticated": true', out["body"])

    def test_header_source_extraction(self):
        flow = [
            {"method": "GET", "url": "http://127.0.0.1:8893/login",
             "save_as": "tok", "save_from": "body",
             "save_pattern": r'"token":\s*"([^"]+)"'},
            {"method": "GET", "url": "http://127.0.0.1:8893/me?x={{tok}}"},
        ]
        out = self.sm._flow_http(flow, timeout=5)
        self.assertIn("x=tkn_deadbeef", out["url"])
