#!/usr/bin/env python3
"""
SPYDERMONKEY SKILLTREE — generate the family's per-technique skill files from
its REAL canon: every mandate's references/ dir that exists on disk (barbican,
holyshit-mode, undercroft, 3am-shinjitsu, kairo, kaisha, shukaku, kage, dojo —
plus the dispatcher's own references) with WSTG/CWE/ATT&CK bindings. One
technique = one lazy-loaded skill file + a searchable index.

Run:  python3 skilltree.py           # emit to references/skills/ + index.md
      python3 skilltree.py --count   # just count what would be generated
      python3 skilltree.py --verify  # prove index ↔ files ↔ bindings are intact
      python3 skilltree.py --count --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
OUT = REFS / "skills"

# methodology bindings: class keyword → (WSTG, CWE, ATT&CK)
BINDINGS = {
    "boundary": ("WSTG-ATHZ-04", "CWE-639", "T1068"),
    "idor": ("WSTG-ATHZ-04", "CWE-639", "T1068"),
    "replay": ("WSTG-BUSL-06", "CWE-294", "T1550"),
    "webhook": ("WSTG-BUSL-06", "CWE-294", "T1550"),
    "idempoten": ("WSTG-BUSL-06", "CWE-294", "T1550"),
    "state": ("WSTG-BUSL-08", "CWE-841", "T1574"),
    "transition": ("WSTG-BUSL-08", "CWE-841", "T1574"),
    "math": ("WSTG-BUSL-01", "CWE-681", "T1565"),
    "rounding": ("WSTG-BUSL-01", "CWE-681", "T1565"),
    "precision": ("WSTG-BUSL-01", "CWE-1336", "T1565"),
    "entitle": ("WSTG-BUSL-05", "CWE-285", "T1068"),
    "coupon": ("WSTG-BUSL-05", "CWE-285", "T1068"),
    "auth": ("WSTG-ATHN", "CWE-287", "T1111"),
    "token": ("WSTG-SESS", "CWE-287", "T1528"),
    "jwt": ("WSTG-SESS-01", "CWE-347", "T1552"),
    "session": ("WSTG-SESS", "CWE-384", "T1550"),
    "otp": ("WSTG-ATHN-09", "CWE-287", "T1111"),
    "firmware": ("MASTG-RES", "CWE-494", "T1601"),
    "uart": ("MASTG-RES", "CWE-494", "T1601"),
    "flash": ("MASTG-RES", "CWE-494", "T1601"),
    "ota": ("MASTG-RES", "CWE-494", "T1601"),
    "ble": ("MASTG-RES", "CWE-288", "T1557"),
    "radio": ("MASTG-RES", "CWE-288", "T1557"),
    "rfid": ("MASTG-RES", "CWE-288", "T1557"),
    "nfc": ("MASTG-RES", "CWE-288", "T1557"),
    "injection": ("WSTG-INPV", "CWE-74", "T1190"),
    "sql": ("WSTG-INPV-05", "CWE-89", "T1190"),
    "xss": ("WSTG-INPV-02", "CWE-79", "T1189"),
    "ssrf": ("WSTG-INPV-10", "CWE-918", "T1190"),
    "xxe": ("WSTG-INPV-07", "CWE-611", "T1190"),
    "redirect": ("WSTG-INPV-06", "CWE-601", "T1190"),
    "backup": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "dump": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "env": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "git": ("WSTG-CONF-04", "CWE-538", "T1552"),
    "secret": ("WSTG-CONF-04", "CWE-798", "T1552"),
    "cors": ("WSTG-CLNT-03", "CWE-942", "T1557"),
    "smuggl": ("WSTG-ADV-02", "CWE-444", "T1190"),
    "graphql": ("WSTG-APIT-10", "CWE-1321", "T1190"),
    "prototype": ("WSTG-CLNT-04", "CWE-1321", "T1189"),
    "websocket": ("WSTG-CLNT-05", "CWE-345", "T1557"),
    "subdomain": ("WSTG-CONF-09", "CWE-350", "T1584"),
    "takeover": ("WSTG-CONF-09", "CWE-350", "T1584"),
    "bucket": ("WSTG-CONF-04", "CWE-732", "T1530"),
    "s3": ("WSTG-CONF-04", "CWE-732", "T1530"),
    "pi": ("WSTG-BUSL", "CWE-200", "T1005"),
    "disclosure": ("WSTG-INFO", "CWE-200", "T1592"),
    "privesc": ("PTES-LE", "CWE-250", "T1068"),
    "sudo": ("PTES-LE", "CWE-250", "T1548"),
    "suid": ("PTES-LE", "CWE-250", "T1548"),
    "lateral": ("PTES-PE", "CWE-287", "T1550"),
    "cred": ("PTES-PE", "CWE-522", "T1555"),
    "harvest": ("WSTG-BUSL", "CWE-200", "T1005"),
    "crown": ("WSTG-BUSL", "CWE-200", "T1005"),
    "leak": ("WSTG-INFO", "CWE-200", "T1592"),
    "sanitize": ("PTES-OPSEC", "CWE-200", "T1070"),
    "vantage": ("PTES-OPSEC", "CWE-200", "T1070"),
    "timeline": ("PTES-OPSEC", "CWE-200", "T1070"),
    "trail": ("PTES-OPSEC", "CWE-200", "T1070"),
    "rate": ("WSTG-ATHN-04", "CWE-307", "T1110"),
    "brute": ("WSTG-ATHN-04", "CWE-307", "T1110"),
    "cookie": ("WSTG-SESS-03", "CWE-1004", "T1550"),
    "toss": ("WSTG-SESS-03", "CWE-1004", "T1550"),
    "cache": ("WSTG-ADV-01", "CWE-444", "T1190"),
    "poison": ("WSTG-ADV-01", "CWE-444", "T1190"),
    "header": ("WSTG-PARA", "CWE-113", "T1190"),
    "host-header": ("WSTG-PARA", "CWE-113", "T1190"),
    "redirect": ("WSTG-INPV-06", "CWE-601", "T1190"),
    "deserial": ("WSTG-INPV", "CWE-502", "T1190"),
    "race": ("WSTG-BUSL-07", "CWE-362", "T1499"),
    "randomness": ("WSTG-BUSL-03", "CWE-330", "T1036"),
    "entropy": ("WSTG-BUSL-03", "CWE-330", "T1036"),
    "logic": ("WSTG-BUSL", "CWE-840", "T1499"),
    "payment": ("WSTG-BUSL-02", "CWE-840", "T1565"),
    "price": ("WSTG-BUSL-02", "CWE-840", "T1565"),
    "password": ("WSTG-ATHN-08", "CWE-521", "T1110"),
    "reset": ("WSTG-ATHN-07", "CWE-640", "T1078"),
    "mfa": ("WSTG-ATHN-09", "CWE-308", "T1111"),
    "upload": ("WSTG-BUSL-09", "CWE-434", "T1190"),
    "traversal": ("WSTG-PATH", "CWE-22", "T1005"),
    "directory": ("WSTG-CONF-03", "CWE-548", "T1083"),
    "sourcemap": ("WSTG-INFO-10", "CWE-540", "T1552"),
    "container": ("PTES-CON", "CWE-250", "T1611"),
    "kubernetes": ("PTES-CON", "CWE-250", "T1610"),
    "kerberos": ("PTES-WIN", "CWE-287", "T1558"),
    "ldap": ("WSTG-INPV", "CWE-90", "T1190"),
    "cmd": ("WSTG-INPV-09", "CWE-78", "T1059"),
    "ssti": ("WSTG-INPV", "CWE-1336", "T1059"),
    "nosql": ("WSTG-INPV-05", "CWE-943", "T1190"),
    "mysql": ("WSTG-INPV-05", "CWE-89", "T1190"),
    "postgres": ("WSTG-INPV-05", "CWE-89", "T1190"),
    "mssql": ("WSTG-INPV-05", "CWE-89", "T1190"),
    "sqlite": ("WSTG-INPV-05", "CWE-89", "T1190"),
    "mongo": ("WSTG-INPV-05", "CWE-943", "T1190"),
    "cassandra": ("WSTG-INPV-05", "CWE-943", "T1190"),
    "viewstate": ("WSTG-INPV", "CWE-502", "T1190"),
    "pickle": ("WSTG-INPV", "CWE-502", "T1190"),
    "h2c": ("WSTG-ADV-02", "CWE-444", "T1190"),
    "http2": ("WSTG-ADV-02", "CWE-444", "T1190"),
    "continuation": ("WSTG-ADV-02", "CWE-444", "T1499"),
    "ja3": ("WSTG-INFO", "CWE-200", "T1592"),
    "imds": ("WSTG-INPV-10", "CWE-918", "T1190"),
    "metadata": ("WSTG-INPV-10", "CWE-918", "T1190"),
    "sas": ("WSTG-CONF-04", "CWE-732", "T1530"),
    "kubelet": ("PTES-CON", "CWE-250", "T1610"),
    "etcd": ("PTES-CON", "CWE-250", "T1610"),
    "service-account": ("PTES-CON", "CWE-250", "T1610"),
    "samr": ("PTES-WIN", "CWE-287", "T1558"),
    "null-session": ("PTES-WIN", "CWE-287", "T1558"),
    "as-rep": ("PTES-WIN", "CWE-287", "T1558"),
    "kerberoast": ("PTES-WIN", "CWE-287", "T1558"),
    "pinning": ("MASTG-RES", "CWE-295", "T1557"),
    "keychain": ("MASTG-RES", "CWE-922", "T1555"),
    "webview": ("MASTG-PLATFORM", "CWE-749", "T1557"),
    "deep-link": ("MASTG-PLATFORM", "CWE-927", "T1546"),
    "allowbackup": ("MASTG-STORAGE", "CWE-530", "T1552"),
    "wordpress": ("WSTG-INFO", "CWE-200", "T1592"),
    "joomla": ("WSTG-INFO", "CWE-200", "T1592"),
    "drupal": ("WSTG-INFO", "CWE-200", "T1592"),
    "cms": ("WSTG-INFO", "CWE-200", "T1592"),
    "smtp": ("WSTG-CFG", "CWE-284", "T1110"),
    "mta-sts": ("WSTG-INFO", "CWE-359", "T1584"),
    "caa": ("WSTG-CONF", "CWE-693", "T1014"),
    "dnssec": ("WSTG-CONF", "CWE-345", "T1584"),
    "subscription": ("WSTG-BUSL-05", "CWE-285", "T1068"),
    "concurrent": ("WSTG-SESS", "CWE-613", "T1550"),
    "voucher": ("WSTG-BUSL-05", "CWE-285", "T1068"),
    "webhook": ("WSTG-BUSL-06", "CWE-294", "T1550"),
    "nginx": ("WSTG-CONF", "CWE-22", "T1190"),
    "apache": ("WSTG-CONF", "CWE-530", "T1552"),
    "iis": ("WSTG-CONF", "CWE-530", "T1552"),
    "tomcat": ("WSTG-CONF", "CWE-530", "T1552"),
    "actuator": ("WSTG-CONF", "CWE-530", "T1552"),
    "spring": ("WSTG-CONF", "CWE-530", "T1552"),
    "django": ("WSTG-CONF", "CWE-215", "T1552"),
    "rails": ("WSTG-INPV", "CWE-1321", "T1190"),
    "laravel": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "express": ("WSTG-INFO-10", "CWE-540", "T1552"),
    "elasticsearch": ("WSTG-CONF", "CWE-732", "T1530"),
    "memcached": ("WSTG-CONF", "CWE-732", "T1530"),
    "rabbitmq": ("WSTG-CONF", "CWE-284", "T1530"),
    "kafka": ("WSTG-CONF", "CWE-284", "T1530"),
    "rdp": ("PTES-RA", "CWE-287", "T1078"),
    "vnc": ("PTES-RA", "CWE-284", "T1021"),
    "vpn": ("PTES-RA", "CWE-287", "T1078"),
    "breach": ("WSTG-INFO", "CWE-200", "T1592"),
    "github": ("WSTG-CONF-04", "CWE-538", "T1552"),
    "asn": ("WSTG-INFO", "CWE-200", "T1592"),
    "wifi": ("MASTG-RES", "CWE-288", "T1557"),
    "sdr": ("MASTG-RES", "CWE-288", "T1557"),
    "spi": ("MASTG-RES", "CWE-494", "T1601"),
    "modbus": ("PTES-ICS", "CWE-284", "T0886"),
    "bacnet": ("PTES-ICS", "CWE-284", "T0886"),
    "dependency": ("WSTG-BUSL", "CWE-1357", "T1195"),
    "sdk": ("WSTG-BUSL", "CWE-1357", "T1195"),
    "sri": ("WSTG-CONF", "CWE-693", "T1014"),
    "iv": ("WSTG-CRYPTO-04", "CWE-329", "T1573"),
    "ecb": ("WSTG-CRYPTO-03", "CWE-327", "T1573"),
    "padding": ("WSTG-CRYPTO-04", "CWE-326", "T1573"),
    "length-extension": ("WSTG-CRYPTO-04", "CWE-327", "T1573"),
    "hardcoded": ("WSTG-CONF-04", "CWE-798", "T1552"),
    "ntlm": ("PTES-WIN", "CWE-287", "T1558"),
    "relay": ("PTES-WIN", "CWE-287", "T1558"),
    "webauthn": ("WSTG-ATHN", "CWE-287", "T1111"),
    "captcha": ("WSTG-BUSL", "CWE-307", "T1110"),
    "antibot": ("WSTG-CONF", "CWE-693", "T1014"),
    "provably": ("WSTG-BUSL-03", "CWE-330", "T1036"),
    "rtp": ("WSTG-BUSL-02", "CWE-681", "T1565"),
    "bet": ("WSTG-BUSL-02", "CWE-840", "T1565"),
    "logcat": ("MASTG-PLATFORM", "CWE-532", "T1552"),
    "clipboard": ("MASTG-STORAGE", "CWE-532", "T1552"),
    "apk": ("MASTG-RES", "CWE-494", "T1601"),
    "assetlinks": ("MASTG-PLATFORM", "CWE-927", "T1546"),
    "strings": ("MASTG-RES", "CWE-798", "T1552"),
    "wasm": ("WSTG-INFO-10", "CWE-540", "T1552"),
    "vhost": ("WSTG-CONF", "CWE-350", "T1584"),
    "origin-cert": ("WSTG-CONF", "CWE-295", "T1584"),
    "526": ("WSTG-CONF", "CWE-295", "T1584"),
    "geoblock": ("WSTG-CONF", "CWE-284", "T1557"),
    "dedupe": ("PTES-OPSEC", "CWE-200", "T1070"),
    "grading": ("PTES-OPSEC", "CWE-200", "T1070"),
    "ceiling": ("PTES-OPSEC", "CWE-200", "T1070"),
    "grpc": ("WSTG-APIT", "CWE-285", "T1190"),
    "mail": ("WSTG-INFO", "CWE-359", "T1584"),
    "spf": ("WSTG-INFO", "CWE-359", "T1584"),
    "dmarc": ("WSTG-INFO", "CWE-359", "T1584"),
    "dkim": ("WSTG-INFO", "CWE-359", "T1584"),
    "saml": ("WSTG-SESS", "CWE-347", "T1550"),
    "sso": ("WSTG-SESS", "CWE-287", "T1550"),
    "oauth": ("WSTG-SESS", "CWE-601", "T1550"),
    "queue": ("WSTG-BUSL", "CWE-840", "T1499"),
    "pipeline": ("PTES-CON", "CWE-250", "T1610"),
    "registry": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "cron": ("PTES-LE", "CWE-250", "T1053"),
    "waf": ("WSTG-CONF", "CWE-693", "T1014"),
    "ratelimit": ("WSTG-ATHN-04", "CWE-307", "T1110"),
    "idempotency": ("WSTG-BUSL-06", "CWE-294", "T1550"),
}


def _bindings(text):
    t = text.lower()
    hits = []
    for kw, (w, c, a) in BINDINGS.items():
        if kw in t:
            hits.append((w, c, a))
    if not hits:
        return ("WSTG-INFO", "CWE-200", "T1592")
    return hits[0]


def _slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60] or "technique"


def _extract_blocks(text, headers):
    """Split a reference doc into (title, body) chunks by ## AND ### headers —
    the deeper the header, the denser the tree."""
    out = []
    cur_title, cur = None, []
    for line in text.splitlines():
        if line.startswith("## ") or line.startswith("### "):
            if cur_title and cur:
                out.append((cur_title, "\n".join(cur).strip()))
            cur_title, cur = line.lstrip("#").strip(), []
        elif cur_title:
            cur.append(line)
    if cur_title and cur:
        out.append((cur_title, "\n".join(cur).strip()))
    return out


def collect_sources():
    """Every (category, title, body) from the family's real canon — every mandate
    references/ dir present on disk (all ten mandates, where installed), plus the
    dispatcher's own references."""
    srcs = []
    dirs = []
    sec = Path.home() / ".hermes/skills/security"
    for name in ("barbican", "holyshit-mode", "undercroft", "3am-shinjitsu",
                 "kairo", "kaisha", "shukaku", "kage", "dojo"):
        d = sec / name / "references"
        if d.exists():
            dirs.append((name, d))
    dirs.append(("spydermonkey", REFS))
    seen_titles = set()
    for cat, d in dirs:
        for p in sorted(d.glob("*.md")):
            try:
                text = p.read_text(errors="replace")
            except Exception:
                continue
            for title, body in _extract_blocks(text, True):
                key = f"{cat}:{title}".lower()
                if key in seen_titles or len(body) < 40:
                    continue
                seen_titles.add(key)
                srcs.append((f"{cat}/{p.stem}", title, body))
    # kairo technique classes (table rows)
    se = None
    for cat, d in dirs:
        if cat == "kairo" and (d / "synthesis-engine.md").exists():
            se = d / "synthesis-engine.md"
    if se:
        for ln in se.read_text(errors="replace").splitlines():
            if ln.startswith("| ") and any(c in ln for c in ("REPLAY", "STATEBYPASS", "MATH",
                                                             "ENTITLEMENT", "AUTHBYPASS",
                                                             "HWFLASH", "HDRADIO")):
                cells = [c.strip() for c in ln.strip("|").split("|")]
                if len(cells) >= 3 and cells[0] not in ("Class", "---", ""):
                    srcs.append(("kairo/technique-classes",
                                 f"{cells[0]} — {cells[1]}",
                                 "\n".join(f"- {c}" for c in cells)))
    return srcs


def _existing_dates():
    """Preserve the original 'generated' date of files that already exist, so
    regeneration refreshes index + colliding slugs without touching 690+ files."""
    dates = {}
    try:
        for p in OUT.rglob("*.md"):
            try:
                m = re.search(r"^- generated: (\d{4}-\d{2}-\d{2})$",
                              p.read_text(errors="replace"), re.M)
                if m:
                    dates[p.resolve()] = m.group(1)
            except Exception:
                continue
    except Exception:
        pass
    return dates


def emit(args):
    import hashlib
    srcs = collect_sources()
    if args.count:
        payload = {
            "count": len(srcs),
            "sources": len({s for s, _, _ in srcs}),
            "bindings": len(BINDINGS),
            "generated": OUT.exists(),
        }
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(f"{len(srcs)} technique skill files would be generated "
                  f"from {payload['sources']} source docs ({len(BINDINGS)} binding keys)")
        return 0
    made = 0
    today = datetime.now(timezone.utc).date().isoformat()
    existing_dates = _existing_dates()
    used_paths = {}
    index = ["# SPYDERMONKEY SKILLTREE — the family's technique library",
             "",
             "_generated from the family's REAL canon — one technique per file,_",
             "_WSTG/CWE/ATT&CK-bound, lazy-loaded. regenerate: skilltree.py_",
             ""]
    for src, title, body in sorted(srcs, key=lambda x: (x[0], x[1].lower())):
        slug = _slug(f"{src}-{title}")
        d = OUT / src
        f = d / f"{slug}.md"
        # _slug truncates at 60 chars — on collision, append a stable hash so a
        # later technique never silently overwrites an earlier one.
        if f.resolve() in used_paths:
            digest = hashlib.sha1(f"{src}\0{title}".encode()).hexdigest()[:8]
            slug = f"{slug[:50]}-{digest}"
            f = d / f"{slug}.md"
        used_paths[f.resolve()] = True
        w, c, a = _bindings(f"{title} {body}")
        d.mkdir(parents=True, exist_ok=True)
        generated = existing_dates.get(f.resolve(), today)
        f.write_text(
            f"# {title}\n\n"
            f"- source canon: `{src}.md`\n- bindings: **{w}** · **{c}** · **ATT&CK {a}**\n"
            f"- generated: {generated}\n\n"
            f"## The technique\n\n{body}\n\n"
            f"## Family use\n\n- decisive-test shape lives in the source canon\n"
            f"- walls: validation-only · NO-GAIN · documented-class adaptation only\n")
        made += 1
        index.append(f"- [{title}](skills/{src}/{slug}.md) — `{src}` · {w} · {c} · {a}")
    (REFS / "skilltree-index.md").write_text("\n".join(index) + "\n")
    if args.json:
        print(json.dumps({"count": made, "sources": len({s for s, _, _ in srcs}),
                          "bindings": len(BINDINGS), "out": str(OUT),
                          "index": str(REFS / "skilltree-index.md")}, indent=2))
    else:
        print(f"▸ skilltree: {made} technique skill files → {OUT}/")
        print(f"▸ index: {REFS / 'skilltree-index.md'} ({len(BINDINGS)} binding keys)")
    return 0


LINK_RE = re.compile(
    r"^- \[(?P<title>.+?)\]\((?P<href>skills/[^)]+)\) — "
    r"`(?P<source>[^`]+)` · (?P<wstg>[^ ·]+) · (?P<cwe>[^ ·]+) · (?P<attack>\S+?)"
    r"(?: · (?P<role>entry|pivot|final))?$",
    re.M)

# ── the corpus expander (scale): technique × platform × auth = the 7k+ library ─

DOMAIN_PLATFORMS = [
    (r"firmware|uart|flash|ota|\bble\b|radio|rfid|nfc|hardware|jtag|keychain|webview|deep.?link|allowbackup|android|ios|mastg",
     ["android", "ios", "firmware", "iot"]),
    (r"container|kubernetes|docker|kube|pod|ci|pipeline|registry|etcd|kubelet|service.?account",
     ["container", "kubernetes", "cloud", "ci-cd"]),
    (r"kerberos|windows|active.?directory|domain controller|samr|null.?session|as-rep|kerberoast|smb|rpcclient",
     ["windows", "host", "cloud"]),
    (r"\baws\b|\bs3\b|bucket|azure|\bgcp\b|cloud|iam|lambda|terraform|iac|imds|metadata|sas|blob|gcs|lambda",
     ["aws", "azure", "gcp", "kubernetes", "iac"]),
    (r"graphql|api|websocket|jwt|session|auth|token|oauth|sso|cookie|grpc|cswsh|h2c|http2|continuation|ja3|deserial|pickle|viewstate|mongo|cassandra",
     ["web-app", "api", "graphql", "websocket", "mobile-api", "grpc"]),
    (r"sudo|suid|privesc|lateral|kernel|linux|\bssh\b|\bhost\b|systemd",
     ["linux", "windows", "container"]),
    (r"dns|subdomain|takeover|domtake|cname|edge|cache|cdn|header|smuggl|mail|spf|dmarc|dkim|smtp|mta-sts|bimi|caa|dnssec",
     ["edge", "dns", "web-app", "mail"]),
    (r"cors|xss|csrf|clickjacking|prototype|dom\b|postmessage|service.?worker|xs.?leak|css",
     ["web-app", "api"]),
    (r"sql|nosql|injection|ldap|\bcmd\b|ssti|deserial|upload|traversal|xxe|mysql|postgres|mssql|sqlite|oracle|nosql|ssrf|gopher|rebind",
     ["web-app", "api", "container"]),
    (r"payment|price|coupon|cart|logic|math|rounding|race|replay|idempoten|webhook|voucher|subscription|referral|cashback|concurrent|entitle",
     ["web-app", "api", "mobile"]),
    (r"backup|dump|\.env|\.git|secret|harvest|sourcemap|disclosure|info|linkfinder|artifact",
     ["web-app", "api", "container"]),
    (r"rate|brute|password|reset|\bmfa\b|\botp\b", ["web-app", "api", "mobile"]),
    (r"wordpress|joomla|drupal|\bcms\b|wp-json|plugin|theme",
     ["web-app", "api"]),
    (r"sanitize|vantage|timeline|trail|opsec|anonym|alias|artifact",
     ["external", "host"]),
    (r"nginx|apache|iis|tomcat|spring|django|rails|laravel|express|next|nuxt|actuator|framework|server",
     ["web-app", "api", "host"]),
    (r"elasticsearch|memcached|clickhouse|couchdb|influxdb|psql|mysql|mongosh|\bdb\b|database",
     ["db", "container", "host"]),
    (r"rabbitmq|kafka|queue|pub.?sub|stream|amqp",
     ["queue", "container", "api"]),
    (r"rdp|vnc|openvpn|wireguard|vpn|bastion|remote.?access|\bnla\b",
     ["host", "windows", "linux"]),
    (r"ble|sdr|nfc|rfid|wifi|wpa|uart|jtag|spi|glitch|hardware|radio",
     ["iot", "wireless", "embedded"]),
    (r"modbus|bacnet|scada|ics|hmi|historian|plc",
     ["embedded", "host"]),
    (r"dependency|supply.?chain|confusion|pipeline|cache.?poison|action",
     ["ci-cd", "container", "web-app"]),
    (r"padding|ecb|\biv\b|crypto|cipher|hmac|prng|entropy|length.?extension|key.?material|signature",
     ["web-app", "api", "host"]),
    (r"logcat|clipboard|keychain|webview|deep.?link|allowbackup|apk|assetlinks|mastg|app.?link|backup.?sync",
     ["android", "ios", "mobile"]),
    (r"bundle|chunk|string.?table|wire.?format|packet.?type|wasm|loader|sdk|decompile",
     ["web-app", "api", "host"]),
    (r"vhost|origin.?cert|526|geoblock|edge|cdn|cache.?key|header.?posture",
     ["edge", "web-app", "lb"]),
    (r"dedupe|grading|ceiling|hypothesis|ledger.?discipline|report",
     ["external", "host"]),
]
DEFAULT_PLATFORMS = ["web-app", "api", "host"]
AUTH_STATES = ("unauth", "low-priv", "high-priv", "federated", "machine")
# the hardened state is REAL, not filler: it only applies to technique families
# where a WAF/filter tier actually changes the probe shape
_HARDENED_RE = re.compile(
    r"injection|xss|ssti|traversal|xxe|sql|ldap|\bcmd\b|deserial|smuggl"
    r"|prototype|brute|password|upload|shell", re.I)
_HARDENED_ADJ = (
    "a filter/WAF tier fronts the target: expect canonicalization and signature "
    "matching on the raw request — the probe vocabulary's encodings (double-encode, "
    "unicode, backslash, case-split) exist exactly for this tier; the differential "
    "must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a "
    "class confirmation. Low-and-slow: one variant per request, never a burst.")
PLATFORM_ADJ = {
    "web-app": "strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value",
    "api": "strike the JSON body + query string; content-type and parameter placement change the probe shape",
    "graphql": "aliases and batched queries bypass field-level checks; type confusion lives in the schema",
    "websocket": "state carries across frames — the replay/state-bypass classes apply frame-to-frame",
    "android": "the check often lives client-side — frida/objection at the runtime, MASTG methodology",
    "ios": "the check often lives client-side — runtime inspection, MASTG/MASVS methodology",
    "firmware": "the check lives in the image — uart/flash/ota paths, no-gain read-only dumps",
    "iot": "radio/serial surface — BLE/NFC/UART classes, lab hardware only",
    "linux": "read-only inventory first (kaisha rungs), then the documented class match",
    "windows": "token/session confusion classes; read-only enumeration, NO-GAIN",
    "container": "namespace/capability surface — read-only inventory, no escape execution",
    "kubernetes": "RBAC/service-account surface — read-only enumeration, crown the exposure",
    "aws": "IAM/identity surface — read-only enumeration (shukaku hunt semantics)",
    "azure": "identity surface — read-only enumeration (shukaku hunt semantics)",
    "gcp": "IAM/service-account surface — read-only enumeration",
    "cloud": "control-plane exposure — read-only, crown the class",
    "edge": "rate/segmentation differences — masscan-class first, then the app layer",
    "dns": "record/cname surface — the domtake chain starts here",
    "mail": "spf/dkim/dmarc record surface — spoofing and spoofability live in the record math",
    "external": "passive-first; the dossier feeds everything downstream",
    "host": "era-stack banner mapping (kaisha cve) before any rung",
    "mobile-api": "the mobile client IS another api principal — same routes, different trust assumptions",
    "cms": "the CMS's own REST/route surface first — enumerate what the platform publishes about itself",
    "grpc": "reflection/list methods first; protobuf definitions are the schema oracle",
    "ci-cd": "pipeline config/runner surface — secrets and lateral movement ride the runners",
    "iac": "template/state files are the infrastructure inventory — read-only crown of the exposure",
    "db": "the engine's own handshake/banner first — auth-stage reachability is the inventory row",
    "queue": "management/metadata endpoints first; topics and channels are the inventory",
    "lb": "routing/header-trust differentials at the edge tier — the treatment matrix is the finding",
    "wireless": "LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall",
    "embedded": "banner/identity reads only on in-scope industrial tiers — control writes are the absolute wall",
    "desktop": "thick-client IPC/update channels — characterize from your own installed build",
}
AUTH_ADJ = {
    "unauth": "no credential material — the classic differential applies as-is; absent auth = the authn-bypass class",
    "low-priv": "hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)",
    "high-priv": "the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)",
    "federated": "identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, "
                 "issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; "
                 "the local session may be fine while the trust boundary is not",
    "machine": "the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the "
               "differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, "
               "unscoped keys, and which audit trail the key leaves; the human account model does not apply",
}
CHAIN_ROLES = {
    "entry": "opens the kill chain (first blood) — pairs with the info/harvest/recon findings",
    "pivot": "combines with a prior finding — chain detect pairs same-origin findings",
    "final": "the impact leg — shukaku prices what this rung reaches",
}


def _platforms_for(text):
    t = text.lower()
    for pat, plats in DOMAIN_PLATFORMS:
        if re.search(pat, t):
            return plats
    return DEFAULT_PLATFORMS


def expand(json_mode=False, min_count=0):
    """THE CORPUS — every technique × applicable platform × auth state. Each
    variant file is REAL: the canon body + context applicability + probe
    adjustment + chain roles. Deterministic content (no run dates in files) so
    regeneration is git-stable."""
    import hashlib
    srcs = collect_sources()
    today = datetime.now(timezone.utc).date().isoformat()
    made = 0
    index = ["# SPYDERMONKEY EXPANDED CORPUS — technique × platform × auth",
             "",
             f"_generated {today} from the family's real canon. Deterministic:_",
             "_regenerate any time, content is stable. lazy-loaded, one at a time._",
             ""]
    used = {}
    for src, title, body in sorted(srcs, key=lambda x: (x[0], x[1].lower())):
        plats = _platforms_for(f"{title} {body}")
        w, c, a = _bindings(f"{title} {body}")
        base_slug = _slug(f"{src}-{title}")
        d = OUT / src
        d.mkdir(parents=True, exist_ok=True)
        roles = ("entry" if any(k in title.lower() for k in
                 ("recon", "enumerate", "fingerprint", "backup", "info", "subdomain"))
                 else "final" if any(k in title.lower() for k in
                 ("takeover", "rce", "crown", "price", "harvest", "dump"))
                 else "pivot")
        # chain-composition companion (one per base technique, REAL pairing)
        c_slug = f"{base_slug}--chain"
        c_f = d / f"{c_slug}.md"
        if c_f.resolve() not in used:
            used[c_f.resolve()] = True
            c_role = ("entry — this OPENS a chain: everything after pairs with it; "
                      "chain detect looks for same-origin findings that follow"
                      if any(k in title.lower() for k in
                             ("recon", "enumerate", "fingerprint", "backup", "info",
                              "subdomain", "harvest", "disclosure"))
                      else "final — this CLOSES a chain: shukaku prices what it "
                           "reaches; chain detect looks for the entries that feed it"
                      if any(k in title.lower() for k in
                             ("takeover", "rce", "crown", "price", "dump", "exfil",
                              "destruction", "denial"))
                      else "pivot — this BRIDGES a chain: an entry finding upstream "
                           "plus this pivot plus a final downstream")
            c_f.write_text(
                f"# {title} — chain composition\n\n"
                f"- source canon: `{src}.md`\n- base technique: `{base_slug}.md`\n"
                f"- chain role: **{c_role}**\n\n"
                f"## Pairing rule\n\n"
                f"chain detect pairs same-origin findings (the `_origin()` key: "
                f"scheme + netloc). This technique composes when a sibling finding "
                f"shares that origin and the pattern's two legs match. Never invent a "
                f"chain: both legs need their own baseline→attack→diff proof first.\n\n"
                f"## Composition\n\n{body}\n\n"
                f"## Walls\n\n- a chain is a SEVERITY judgment over proven findings — "
                f"never new execution\n- every leg keeps its own ledger row and its own "
                f"evidence\n")
            made += 1
            index.append(f"- [{title} — chain composition](skills/{src}/{c_slug}.md)"
                         f" — `{src}` · {w} · {c} · {a} · {roles}")
        for plat in plats:
            states = AUTH_STATES + (("hardened",) if _HARDENED_RE.search(
                f"{title} {body}") else ())
            for auth in states:
                slug = f"{base_slug}--{plat}--{auth}"
                f = d / f"{slug}.md"
                if f.resolve() in used:      # slug truncation collision guard
                    digest = hashlib.sha1(f"{src}\0{title}\0{plat}\0{auth}".encode()).hexdigest()[:8]
                    slug = f"{base_slug[:48]}-{digest}--{plat}--{auth}"
                    f = d / f"{slug}.md"
                used[f.resolve()] = True
                roles = ("entry" if any(k in title.lower() for k in
                         ("recon", "enumerate", "fingerprint", "backup", "info", "subdomain"))
                         else "final" if any(k in title.lower() for k in
                         ("takeover", "rce", "crown", "price", "harvest", "dump"))
                         else "pivot")
                f.write_text(
                    f"# {title} — {plat} / {auth}\n\n"
                    f"- source canon: `{src}.md`\n- base technique: `{base_slug}.md`\n"
                    f"- bindings: **{w}** · **{c}** · **ATT&CK {a}**\n"
                    f"- context: **{plat}** · auth **{auth}** · chain role **{roles}**\n\n"
                    f"## Context\n\n"
                    f"- platform: {PLATFORM_ADJ.get(plat, 'family probes cover the class')}\n"
                    f"- auth state: {AUTH_ADJ.get(auth, _HARDENED_ADJ)}\n\n"
                    f"## The technique\n\n{body}\n\n"
                    f"## Probe adjustment ({plat} × {auth})\n\n"
                    f"1. baseline first: the request/session with NOTHING changed\n"
                    f"2. attack: the documented class probe, adjusted per context above\n"
                    f"3. diff: measurable only — status/length/body — or it is not a finding\n\n"
                    f"## Chain roles\n\n- {CHAIN_ROLES[roles]}\n"
                    f"- pairs-with: see `skilltree-index.md` for the sibling techniques\n\n"
                    f"## Walls\n\n- validation-only · NO-GAIN · documented-class adaptation only\n"
                    f"- in-scope only: the scope authority refuses everything else (rc=1)\n")
                made += 1
                index.append(f"- [{title} — {plat}/{auth}](skills/{src}/{slug}.md)"
                             f" — `{src}` · {w} · {c} · {a} · {roles}")
    (REFS / "skilltree-expanded-index.md").write_text("\n".join(index) + "\n")
    payload = {"expanded": made, "sources": len(srcs),
               "index": str(REFS / "skilltree-expanded-index.md"),
               "total_with_base": made + len(srcs)}
    if json_mode:
        print(json.dumps(payload, indent=2))
    else:
        print(f"▸ corpus expanded: {made} context variant(s) over {len(srcs)} base"
              f" technique(s) → {payload['total_with_base']} total skill files")
        print(f"▸ index: {payload['index']}")
    if min_count and payload["total_with_base"] < min_count:
        print(f"✗ corpus below the scale floor ({payload['total_with_base']} < {min_count})",
              file=sys.stderr)
        return 1
    return 0


def verify(json_mode=False):
    """Check the generated tree is internally consistent: every index link
    resolves, every file carries its provenance + bindings, and no orphan file
    is left behind from an older generation run. When the expanded corpus
    exists, its index links resolve too (sampled content checks)."""
    errors, warnings = [], []
    index_path = REFS / "skilltree-index.md"
    if not index_path.exists():
        errors.append("references/skilltree-index.md missing — run skilltree.py")
        links = []
    else:
        text = index_path.read_text(errors="replace")
        links = [m.groupdict() for m in LINK_RE.finditer(text)]
        if len(links) < 1:
            errors.append("index contains no technique links")
        if "regenerate: skilltree.py" not in text:
            warnings.append("index is missing its regeneration banner")
    linked = {}
    for item in links:
        href = item["href"]
        path = REFS / href
        if href in linked:
            errors.append(f"duplicate index link: {href}")
            continue
        linked[href] = item
        if not path.exists():
            errors.append(f"index link has no file: {href}")
            continue
        body = path.read_text(errors="replace")
        for needle, label in (
                ("- source canon:", "source canon"),
                ("- bindings:", "bindings"),
                ("## The technique", "technique body"),
                ("## Family use", "family use")):
            if needle not in body:
                errors.append(f"{href}: missing {label}")
        if not re.search(r"^- generated: \d{4}-\d{2}-\d{2}$", body, re.M):
            errors.append(f"{href}: missing generated date")
        if item["source"] not in body:
            errors.append(f"{href}: source canon mismatch ({item['source']})")
        for binding in (item["wstg"], item["cwe"], "ATT&CK " + item["attack"]):
            if binding not in body:
                errors.append(f"{href}: binding {binding} not present in file")
    files = sorted(str(p.relative_to(REFS)) for p in OUT.rglob("*.md")) if OUT.exists() else []
    # the expanded corpus: its own index, sampled link + content checks
    exp_index = REFS / "skilltree-expanded-index.md"
    expanded_links = []
    if exp_index.exists():
        etext = exp_index.read_text(errors="replace")
        expanded_links = [m.groupdict() for m in LINK_RE.finditer(etext)]
        if len(expanded_links) < 100:
            errors.append("expanded index exists but holds <100 links — regenerate")
        import random
        rng = random.Random(1337)   # deterministic sampling
        for item in rng.sample(expanded_links, min(20, len(expanded_links))):
            p = REFS / item["href"]
            if not p.exists():
                errors.append(f"expanded link has no file: {item['href']}")
                continue
            body = p.read_text(errors="replace")
            for needle in ("## Context", "## The technique", "## Probe adjustment",
                           "## Chain roles", "## Walls", "- source canon:"):
                if needle not in body:
                    errors.append(f"{item['href']}: missing '{needle}'")
    linked_all = linked | {i["href"]: i for i in expanded_links}
    orphans = [f for f in files if f not in linked_all]
    if orphans:
        warnings.append(f"{len(orphans)} orphan file(s) not in any index "
                        f"(e.g. {orphans[0]})")
    payload = {
        "ok": not errors,
        "index": str(index_path),
        "links": len(links),
        "expanded_links": len(expanded_links),
        "files": len(files),
        "sources": len({i["source"] for i in links}),
        "bindings": len(BINDINGS),
        "orphans": len(orphans),
        "errors": errors[:40],
        "warnings": warnings[:20],
    }
    if json_mode:
        print(json.dumps(payload, indent=2))
    else:
        print("═══ SPYDERMONKEY SKILLTREE VERIFY ═══")
        print(f"  index links: {payload['links']} · expanded: {payload['expanded_links']}"
              f" · files: {payload['files']} "
              f"· sources: {payload['sources']} · orphans: {payload['orphans']}")
        for e in payload["errors"]:
            print(f"  ✗ {e}")
        for w in payload["warnings"]:
            print(f"  ! {w}")
        print(f"═══ {'ALL PASS' if payload['ok'] else 'FAILED'} ═══")
    return 0 if payload["ok"] else 1


def main():
    ap = argparse.ArgumentParser(description="SPYDERMONKEY skilltree generator")
    ap.add_argument("--count", action="store_true")
    ap.add_argument("--expand", action="store_true",
                    help="generate the context corpus: technique × platform × auth")
    ap.add_argument("--min", dest="min_count", type=int, default=0,
                    help="scale floor for --expand (rc=1 below it)")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.verify:
        sys.exit(verify(json_mode=a.json))
    if a.expand:
        sys.exit(expand(json_mode=a.json, min_count=a.min_count))
    sys.exit(emit(a))


if __name__ == "__main__":
    main()
