#!/usr/bin/env python3
"""
FLEET_PROVISION — SPYDERMONKEY v7.2: real arsenal activation.

The operator-box rule stands: THIS machine never installs arsenal tooling.
Fleet machines (engagement VMs, CI, fresh checkouts) run the emitted script:

    python3 scripts/fleet_provision.py --emit          # → fleet-provision.sh
    bash fleet-provision.sh                            # ON THE FLEET BOX ONLY

Coverage model: 1,605 wrappers ≠ 1,605 packages. NSE wrappers ride with nmap,
msf-* with metasploit-framework, nuclei-* with nuclei — the distinct base
packages are what provisioning installs; the rest activate with their host.
Idempotent: `command -v` guards, nothing reinstalled. stdlib-only.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import arsenal as ar  # noqa: E402  (1,605 wrappers, post-merge)

# tool → install spec. apt = Kali/Debian · pip = python · go/cargo/gem noted.
# Names follow the Kali repos (the fleet baseline).
PKG: dict[str, str] = {
    # recon / dns / osint
    "nmap": "apt:nmap", "masscan": "apt:masscan", "zmap": "apt:zmap",
    "amass": "apt:amass", "subfinder": "apt:subfinder", "sublist3r": "apt:sublist3r",
    "assetfinder": "go:github.com/tomnomnom/assetfinder@latest",
    "findomain": "apt:findomain", "theharvester": "apt:theharvester",
    "dnsrecon": "apt:dnsrecon", "dnsenum": "apt:dnsenum", "dnsmap": "apt:dnsmap",
    "massdns": "apt:massdns", "shuffledns": "go:github.com/projectdiscovery/shuffledns@latest",
    "dnsx": "go:github.com/projectdiscovery/dnsx@latest", "fierce": "apt:fierce",
    "dnsutils": "apt:dnsutils", "whois": "apt:whois", "curl": "apt:curl",
    # web / content / api
    "httpx": "go:github.com/projectdiscovery/httpx@latest",
    "nuclei": "go:github.com/projectdiscovery/nuclei@latest",
    "ffuf": "apt:ffuf", "feroxbuster": "apt:feroxbuster", "gobuster": "apt:gobuster",
    "dirsearch": "pip:dirsearch", "dirb": "apt:dirb", "gau": "go:github.com/lc/gau@latest",
    "hakrawler": "go:github.com/hakluke/hakrawler@latest",
    "katana": "go:github.com/projectdiscovery/katana@latest",
    "sqlmap": "apt:sqlmap", "nikto": "apt:nikto", "whatweb": "apt:whatweb",
    "wafw00f": "pip:wafw00f", "arjun": "pip:arjun", "crlfuzz": "go:github.com/dwisiswant0/crlfuzz@latest",
    "dalfox": "go:github.com/hahwul/dalfox@latest", "kiterunner": "go:github.com/assetnote/kiterunner@latest",
    "wpscan": "apt:wpscan", "joomscan": "apt:joomscan", "droopescan": "pip:droopescan",
    "gmt": "apt:gmt", "subzy": "go:github.com/lukasikic/subzy@latest",
    "takeover": "go:github.com/anshumanpattnaik/takeover@latest",
    # tls / net / services
    "testssl": "apt:testssl.sh", "testssl.sh": "apt:testssl.sh",
    "sslscan": "apt:sslscan", "sslyze": "pip:sslyze", "tlssled": "apt:tlssled",
    "ssh-audit": "pip:ssh-audit", "sslstrip": "apt:sslstrip",
    "naabu": "go:github.com/projectdiscovery/naabu@latest",
    "hping3": "apt:hping3", "nping": "apt:nping", "fping": "apt:fping",
    "nc": "apt:netcat-openbsd", "socat": "apt:socat", "traceroute": "apt:traceroute",
    "mtr": "apt:mtr", "arp-scan": "apt:arp-scan", "netdiscover": "apt:netdiscover",
    "enum4linux": "apt:enum4linux", "smbclient": "apt:smbclient",
    "nbtscan": "apt:nbtscan", "snmp": "apt:snmp", "onesixtyone": "apt:onesixtyone",
    "ridenum": "apt:ridenum", "nbtscan-unix": "apt:nbtscan",
    # exploitation / frameworks
    "metasploit": "apt:metasploit-framework", "msfconsole": "apt:metasploit-framework",
    "searchsploit": "apt:exploitdb", "impacket-smbexec": "apt:python3-impacket",
    "impacket-psexec": "apt:python3-impacket", "impacket-secretsdump": "apt:python3-impacket",
    "impacket-wmiexec": "apt:python3-impacket", "impacket-getST": "apt:python3-impacket",
    "hydra": "apt:hydra", "medusa": "apt:medusa", "patator": "apt:patator",
    "cewl": "apt:cewl", "crackmapexec": "apt:crackmapexec", "enum4linux-ng": "pip:enum4linux-ng",
    # cloud / container
    "cloudsploit": "npm:cloudsploit", "scoutsuite": "pip:scoutsuite",
    "trivy": "apt:trivy", "grype": "apt:grype", "dockerscan": "pip:dockerscan",
    "kube-bench": "go:github.com/aquasecurity/kube-bench@latest",
    # fuzz domain (v7.0)
    "afl-fuzz": "apt:aflplusplus", "afl-showmap": "apt:aflplusplus",
    "afl-cmin": "apt:aflplusplus", "afl-tmin": "apt:aflplusplus",
    "honggfuzz": "apt:honggfuzz", "radamsa": "apt:radamsa", "zzuf": "apt:zzuf",
    "boofuzz": "pip:boofuzz", "jazzer": "manual:# GitHub releases: fuzzing/jazzer",
    # misc
    "wget": "apt:wget", "httrack": "apt:httrack", "snallygaster": "pip:snallygaster",
    "snmpwalk": "apt:snmp", "gospider": "go:github.com/jaelesproject/gospider@latest",
    "nuclei-templates": "go:github.com/projectdiscovery/nuclei@latest",
    "seclists": "apt:seclists", "wordlists": "apt:wordlists",
    "proxychains": "apt:proxychains4", "tor": "apt:tor",
}

# wrapper-prefix → the host package that carries it
HOST_PREFIX = {"nmap-": "apt:nmap", "msf-": "apt:metasploit-framework",
               "nuclei-": "go:github.com/projectdiscovery/nuclei@latest",
               "impacket-": "apt:python3-impacket"}


def _coverage() -> dict:
    """Installed-now census + the activation plan the fleet script represents."""
    tools = list(ar.ARSENAL.keys())
    installed = {t for t in tools if ar.shutil.which(t)}
    rides: dict[str, list[str]] = {}
    for t in tools:
        for pre, pkg in HOST_PREFIX.items():
            if t.startswith(pre) and t != pre[:-1]:
                rides.setdefault(pkg, []).append(t)
    direct = [t for t in tools if t not in installed and t not in
              {r for lst in rides.values() for r in lst}
              and t not in set(ar.ARSENAL) - set(ar.ARSENAL)]
    mapped = [t for t in direct if t in PKG]
    unmapped = [t for t in direct if t not in PKG]
    return {"tools": len(tools), "installed_here": sorted(installed),
            "direct_missing": len(direct), "mapped": mapped,
            "unmapped": unmapped, "ride_along": rides}


def emit(path: str | None = None) -> str:
    cov = _coverage()
    pkgs = sorted({PKG[t] for t in cov["mapped"]})
    lines = ["#!/usr/bin/env bash",
             "# SPYDERMONKEY FLEET PROVISIONING — generated by fleet_provision.py",
             "# RUN THIS ON A FLEET MACHINE ONLY (engagement VM / CI / fresh checkout).",
             "# The operator box NEVER runs this (the operator-box rule).",
             "set -uo pipefail",
             "",
             "have() { command -v \"$1\" >/dev/null 2>&1; }",
             "",
             "# ── apt (Kali/Debian fleet) ──────────────────────────────",
             "APT_PKGS=("]
    apt = sorted(p[4:] for p in pkgs if p.startswith("apt:"))
    lines += [f"  {a}" for a in apt]
    lines += [")",
              "",
              "if command -v apt-get >/dev/null 2>&1; then",
              "  for pkg in \"${APT_PKGS[@]}\"; do",
              "    dpkg -s \"$pkg\" >/dev/null 2>&1 || sudo apt-get install -y \"$pkg\" || true",
              "  done",
              "fi",
              "",
              "# ── pip ─────────────────────────────────────────────────",
              ""]
    pip = sorted(p[4:] for p in pkgs if p.startswith("pip:"))
    for t in pip:
        lines.append(f"python3 -m pip show {t} >/dev/null 2>&1 || python3 -m pip install --user {t}")
    lines += ["", "# ── go ─────────────────────────────────────────────────", ""]
    go = sorted(p[3:] for p in pkgs if p.startswith("go:"))
    for g in go:
        lines.append(f"have $(basename {g.split('@')[0]}) || GOBIN=$(go env GOPATH 2>/dev/null)/bin go install {g} 2>/dev/null || true")
    lines += ["", "# ── manual (documented, not automatable) ───────────────", ""]
    for t in cov["unmapped"][:60]:
        cap = ar.ARSENAL[t][0] if t in ar.ARSENAL else "?"
        lines.append(f"# {t}: {cap}")
    lines += ["", "echo '── fleet activation report ──'",
              "python3 scripts/arsenal.py verify 2>/dev/null | tail -2 || true",
              "python3 scripts/spydermonkey.py arsenal list --json 2>/dev/null | "
              "python3 -c 'import json,sys; d=json.load(sys.stdin); "
              "print(f\"arsenal: {d[\\\"installed\\\"]}/{d[\\\"total\\\"]} wrappers active\")' || true"]
    out = path or str(HERE.parent / "fleet-provision.sh")
    open(out, "w").write("\n".join(lines) + "\n")
    os.chmod(out, 0o755)
    return out


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "--detect"
    cov = _coverage()
    if mode == "--json":
        print(json.dumps({k: (v if k != "ride_along" else
                              {k2: len(v2) for k2, v2 in v.items()})
                          for k, v in cov.items()
                          if k != "installed_here"} |
                         {"installed_here": len(cov["installed_here"])}, indent=2))
        return 0
    if mode == "--emit":
        out = emit(sys.argv[2] if len(sys.argv) > 2 else None)
        print(f"═══ FLEET PROVISIONING SCRIPT → {out} ═══")
        print(f"  mapped auto-install : {len(cov['mapped'])} tools")
        print(f"  ride with hosts     : {sum(len(v) for v in cov['ride_along'].values())} wrappers "
              f"(nmap/msf/nuclei/impacket carry them)")
        print(f"  manual-documented   : {len(cov['unmapped'])} tools")
        print("  RUN ON A FLEET BOX ONLY — the operator box never installs")
        return 0
    # default: detect (read-only)
    print(f"═══ ARSENAL ACTIVATION — {cov['tools']} wrappers ═══")
    print(f"  installed here (operator box): {len(cov['installed_here'])}")
    rides = {k: len(v) for k, v in cov['ride_along'].items()}
    print(f"  ride with host packages      : {sum(rides.values())} {rides}")
    print(f"  direct-missing               : {cov['direct_missing']} "
          f"({len(cov['mapped'])} mapped, {len(cov['unmapped'])} manual)")
    print("  activation = fleet-provision.sh on a fleet box (never here)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
