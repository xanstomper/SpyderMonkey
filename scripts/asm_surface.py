#!/usr/bin/env python3
"""SpyderMonkey ASM lane — autonomous exposure management (lite).

`smk asm --domain D [--target T]` — finds the applications nobody listed:
passive certificate-transparency subdomain discovery (crt.sh, read-only,
public data), then catalogs every host into the campaign's context as
endpoints, ready for scope-gated testing. Loading (context set) is the only
side effect; NO live probes fire here — reachability classification is a
separate, scope-gated step (arsenal/dns lanes).

Honest ceiling: crt.sh is the passive surface only; deeper ASM (port
inventory, tech fingerprinting) lives in the recon lanes and stays
scope-gated. This lane finds the addresses; the family tests the estate.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import scope_authority as sa  # noqa: E402

CRTSH = "https://crt.sh/?q=%25.{domain}&output=json"


def _crtsh(domain: str) -> list[str]:
    url = CRTSH.format(domain=domain)
    req = urllib.request.Request(url, headers={"User-Agent": "smk-asm/8.2"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8", "replace"))
    hosts: set[str] = set()
    for row in data:
        for name in (row.get("name_value", "") or "").splitlines():
            n = name.strip().strip("*.")
            if n.endswith(domain) and "*" not in n:
                hosts.add(n.lower())
    return sorted(hosts)


def main() -> int:
    ap = argparse.ArgumentParser(prog="smk asm")
    ap.add_argument("--domain", required=True)
    ap.add_argument("--target", default="", help="campaign target (default: domain)")
    ap.add_argument("--limit", type=int, default=500)
    ap.add_argument("--no-catalog", action="store_true", help="print only")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.target and not sa.scope_path().exists():
        print(f"✗ no scope authority — asm catalogs into a campaign; "
              f"scope init first: spydermonkey scope init --engagement E "
              f"--in-scope {a.domain}", file=sys.stderr)
        return 1

    try:
        hosts = _crtsh(a.domain)
    except Exception as e:
        print(f"✗ crt.sh fetch failed: {e}", file=sys.stderr)
        return 1
    hosts = hosts[: a.limit]

    if a.json:
        print(json.dumps({"domain": a.domain, "found": len(hosts),
                          "hosts": hosts}, indent=2))
        return 0

    print(f"═══ ASM — {a.domain} · {len(hosts)} host(s) from certificate "
          f"transparency ═══")
    for h in hosts:
        print(f"  {h}")
    if a.no_catalog or not a.target:
        print("  (catalog into a campaign: --target T)")
        return 0

    # catalog: persist each host as a context endpoint (the family's spine)
    camp = sa.campaigns_root() / a.target
    camp.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "SPYDERMONKEY_HOME": str(sa.redteam_home())}
    added = 0
    for h in hosts:
        r = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "spydermonkey.py"),
             "context", "set", "--target", a.target, "--kind", "endpoint",
             "--value", f"https://{h}"],
            capture_output=True, text=True, timeout=60, env=env)
        if r.returncode == 0:
            added += 1
    print(f"  catalogued {added}/{len(hosts)} endpoints → campaign "
          f"'{a.target}' context (scope-gated testing next)")
    return 0


if __name__ == "__main__":
    sys.exit(main())