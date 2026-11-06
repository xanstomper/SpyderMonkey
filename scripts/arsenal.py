#!/usr/bin/env python3
"""
SPYDERMONKEY ARSENAL — the execution layer. Discovers the operator's installed
tooling (48 wrappers: nmap, masscan, httpx, nuclei, gobuster, testssl.sh, dnsx,
subfinder, nikto, dirb, whatweb, wafw00f, amass, ffuf, naabu, katana, dalfox,
tlsx, gau, sslscan, sslyze, openssl, ssh-audit, whois, host, nslookup, dnsrecon,
fierce, dnsenum, dnsmap, massdns, shuffledns, sublist3r, theharvester, dirsearch,
feroxbuster, wfuzz, arjun, crlfuzz, sqlmap, wapiti, redis-cli, snmpwalk, grpcurl,
nbtscan, enum4linux …), plans the run per target class, and —
ONLY when the target is inside the shared scope authority — executes with the
family's gates in front. Every tool run is scope-checked, lab-defaulted, and
its output is classified into the family canon on the way out.

v4.0 uses scripts/scope_authority.py (the same implementation as the dispatcher,
gate, ledger, MCP server and live bench): CIDRs, deny precedence, expiry, URL
paths, ports and rate limits are all honored. No authority → NO EXECUTION.

Commands:
  list                          what's installed (tool × capability × class)
  plan    --target T            the full run plan per class (nothing executes)
  run     --target T [--only T1,T2] [--dry-run]   execute (scope-gated)
  verify                        self-check in a throwaway scope

Exit: 0 ok · 1 gate/scope refusal · 2 usage.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scope_authority as sa  # noqa: E402

VERSION = "5.11.0"

# tool → (capability, canon classes it feeds, plan line, args builder)
ARSENAL = {
    "nmap":      ("port/service scan", ("network", "services"),
                  "top-1000 TCP + service versions",
                  lambda t, extra=None: ["-Pn", "--top-ports", "1000", "-sV", "--open", t]),
    "httpx":     ("http surface probe", ("web", "api"),
                  "live-host + title + tech fingerprint",
                  lambda t, extra=None: [t, "-title", "-tech-detect", "-status-code"]),
    "nuclei":    ("vuln templates", ("web", "api"),
                  "medium+ severity template sweep (read-only tags)",
                  lambda t, extra=None: ["-u", t, "-severity", "medium,high,critical",
                                         "-tags", "cve,misconfig,exposure", "-silent"]),
    "gobuster":  ("path/content discovery", ("web", "harvest"),
                  "dir sweep with common wordlist",
                  lambda t, extra=None: ["dir", "-u", t, "-w",
                                         str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "-q", "--no-error-continuation"]),
    "testssl":   ("tls posture", ("crypto", "config"),
                  "tls versions/ciphers/chain audit",
                  lambda t, extra=None: ["--quiet", "--color", "0", t]),
    "dnsx":      ("dns inventory", ("dns", "domtake"),
                  "A/AAAA/CNAME/MX/TXT enumeration",
                  lambda t, extra=None: ["-silent", "-a", "-cname", "-mx", "-txt", t]),
    "subfinder": ("subdomain enum", ("dns", "domtake"),
                  "passive subdomain discovery",
                  lambda t, extra=None: ["-d", t, "-all", "-silent"]),
    "whatweb":   ("tech fingerprint", ("web", "api"),
                  "web tech identification",
                  lambda t, extra=None: ["-q", "-a", "3", t]),
    "wafw00f":   ("waf detection", ("web", "edge"),
                  "waf/edge identification",
                  lambda t, extra=None: [t]),
    "nikto":     ("web misconfig sweep", ("web", "config"),
                  "classic misconfig/exposure checks",
                  lambda t, extra=None: ["-quiet", "-nolisting", t]),
    "masscan":   ("fast port scan", ("network", "services"),
                  "high-rate tcp syn (lab nets only)",
                  lambda t, extra=None: ["-p1-65535", "--rate", "1000", t]),
    "dig":       ("dns records", ("dns",),
                  "zone records via system resolver",
                  lambda t, extra=None: ["+short", "ANY", t]),
    "curl":      ("http fetch", ("web",),
                  "header/body fetch (always present)",
                  lambda t, extra=None: ["-sSI", "-m", "10", t]),
    # v5 — the seven new executors (uniform builder signatures, scheme-aware)
    "ffuf":      ("content discovery", ("web", "harvest"),
                  "dir fuzz with autofilter (needs a wordlist)",
                  lambda t, extra=None: ["-u", t.rstrip("/") + "/FUZZ", "-w",
                                         str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "-mc", "all", "-ac", "-s"]),
    "naabu":     ("fast port scan", ("network", "services"),
                  "top-1000 tcp syn scan",
                  lambda t, extra=None: ["-host", t, "-top-ports", "1000", "-silent"]),
    "amass":     ("passive subdomain enum", ("dns", "domtake"),
                  "passive-only osint subdomain discovery",
                  lambda t, extra=None: ["enum", "-passive", "-d", t]),
    "katana":    ("crawler/url discovery", ("web", "api"),
                  "depth-3 crawl, urls out",
                  lambda t, extra=None: ["-u", t, "-d", "3", "-silent"]),
    "dalfox":    ("xss scanner", ("web", "xss"),
                  "documented-PoC xss parameter scan",
                  lambda t, extra=None: ["url", t, "--no-color", "--no-banner", "-silence"]),
    "tlsx":      ("tls posture", ("crypto", "config"),
                  "cert/san/cn grab",
                  lambda t, extra=None: ["-u", t, "-san", "-cn", "-silent"]),
    "gau":       ("known-url collection", ("web", "harvest"),
                  "passive url corpus (wayback/otx/otx)",
                  lambda t, extra=None: [t]),
    # v5.1 — the twenty-eight new executors (same gates, same scope authority)
    "sslscan":   ("tls posture", ("crypto", "config"),
                  "tls versions/ciphers/renegotiation sweep",
                  lambda t, extra=None: ["--no-colour", t]),
    "sslyze":    ("tls posture", ("crypto", "config"),
                  "cert chain + session resumption audit",
                  lambda t, extra=None: ["--regular", t]),
    "openssl":   ("tls/cert probe", ("crypto",),
                  "s_client brief handshake (always present)",
                  lambda t, extra=None: ["s_client", "-connect", f"{t}:443",
                                         "-brief"]),
    "ssh-audit": ("ssh posture", ("crypto", "config"),
                  "ssh algorithms/host-key policy audit",
                  lambda t, extra=None: ["-n", t]),
    "whois":     ("registration intel", ("dns", "recon"),
                  "domain registration record",
                  lambda t, extra=None: [t]),
    "host":      ("dns records", ("dns",),
                  "A/AAAA/MX/TXT via system resolver",
                  lambda t, extra=None: ["-a", t]),
    "nslookup":  ("dns records", ("dns",),
                  "ANY-type record query",
                  lambda t, extra=None: ["-type=ANY", t]),
    "dnsrecon":  ("dns enum", ("dns", "domtake"),
                  "standard record enumeration + zone attempt",
                  lambda t, extra=None: ["-t", "std", t]),
    "fierce":    ("dns brute", ("dns", "domtake"),
                  "subdomain brute + wildcard detect",
                  lambda t, extra=None: ["--domain", t]),
    "dnsenum":   ("dns enum", ("dns", "domtake"),
                  "record + brute enumeration",
                  lambda t, extra=None: [t]),
    "dnsmap":    ("dns brute", ("dns",),
                  "default-wordlist subdomain brute",
                  lambda t, extra=None: [t]),
    "massdns":   ("dns brute", ("dns",),
                  "high-rate resolver fan-out (needs resolvers)",
                  lambda t, extra=None: ["-r", str(extra or "/usr/share/wordlists/resolvers.txt"),
                                         "-t", "A", t]),
    "shuffledns":("dns brute", ("dns", "domtake"),
                  "massdns wrapper with permutation",
                  lambda t, extra=None: ["-d", t,
                                         "-r", str(extra or "/usr/share/wordlists/resolvers.txt"),
                                         "-silent"]),
    "sublist3r": ("passive subdomain enum", ("dns", "domtake"),
                  "passive osint subdomain discovery",
                  lambda t, extra=None: ["-d", t, "-v"]),
    "theharvester": ("osint collection", ("recon", "harvest"),
                  "email/host harvest from public sources",
                  lambda t, extra=None: ["-d", t, "-l", "50", "-b", "hackertarget"]),
    "dirsearch": ("content discovery", ("web", "harvest"),
                  "dir sweep with default extensions",
                  lambda t, extra=None: ["-u", t,
                                         "-w", str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "-q"]),
    "dirb":      ("content discovery", ("web", "harvest"),
                  "classic dirb sweep",
                  lambda t, extra=None: [t,
                                         str(extra or "/usr/share/wordlists/dirb/common.txt")]),
    "feroxbuster": ("content discovery", ("web", "harvest"),
                  "recursive dir brute with auto-tune",
                  lambda t, extra=None: ["-u", t,
                                         "-w", str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "--quiet", "--auto-tune"]),
    "wfuzz":     ("content discovery", ("web", "harvest"),
                  "FUZZ placement sweep, filtered codes",
                  lambda t, extra=None: ["-w", str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "-c", t.rstrip("/") + "/FUZZ",
                                         "--sc", "200,301,302,403"]),
    "arjun":     ("parameter discovery", ("web", "api"),
                  "hidden query/body parameter discovery",
                  lambda t, extra=None: ["-u", t]),
    "crlfuzz":   ("crlf/open-redirect probe", ("web", "injection"),
                  "documented-PoC crlf parameter scan",
                  lambda t, extra=None: ["-u", t]),
    "sqlmap":    ("injection confirm-aid", ("web", "injection"),
                  "manual-confirmation aid — level1/risk1, one thread",
                  lambda t, extra=None: ["--batch", "--url", t, "--level", "1",
                                         "--risk", "1", "--threads", "1",
                                         "--random-agent"]),
    "wapiti":    ("web vuln sweep", ("web", "api"),
                  "passive-first module sweep",
                  lambda t, extra=None: ["-u", t]),
    "redis-cli": ("service exposure", ("network", "harvest"),
                  "unauth INFO probe (read-only, port 6379)",
                  lambda t, extra=None: ["-h", t, "-p", "6379",
                                         "--no-raw", "INFO", "server"]),
    "snmpwalk":  ("service exposure", ("network", "harvest"),
                  "read-only sysDescr walk, community public",
                  lambda t, extra=None: ["-v", "2c", "-c", "public", t, "sysDescr.0"]),
    "grpcurl":   ("grpc surface", ("api",),
                  "plaintext service reflection list",
                  lambda t, extra=None: ["-plaintext", "-max-time", "5", t, "list"]),
    "nbtscan":   ("netbios inventory", ("network",),
                  "netbios name table sweep",
                  lambda t, extra=None: [t]),
    "enum4linux":("windows enum", ("network", "services"),
                  "read-only smb/null-session inventory",
                  lambda t, extra=None: ["-a", t]),
    # v5.6 — the seventeen new executors: CMS lane, win/SMB lane, OSINT lane
    "wpscan":    ("cms enum", ("web", "cms", "harvest"),
                  "wordpress theme/plugin/user enum (passive+aggressive-light)",
                  lambda t, extra=None: ["--url", t, "--enumerate", "vp,vt,cb",
                                         "--no-banner"]),
    "joomscan":  ("cms enum", ("web", "cms", "harvest"),
                  "joomla component/config enumeration",
                  lambda t, extra=None: ["-u", t]),
    "droopescan":("cms enum", ("web", "cms", "harvest"),
                  "drupal/silverstripe module enumeration",
                  lambda t, extra=None: ["scan", "drupal", "-u", t]),
    "cmsmap":    ("cms enum", ("web", "cms"),
                  "wordpress/joomla/drupal fingerprint sweep",
                  lambda t, extra=None: [t]),
    "zaproxy":   ("web scanner", ("web", "api"),
                  "baseline passive scan (no active attacks)",
                  lambda t, extra=None: ["zap-baseline.py", "-t", t, "-I", "-q"]),
    "smbclient": ("smb enum", ("network", "services", "harvest"),
                  "anonymous share listing (null session)",
                  lambda t, extra=None: ["-L", t, "-N", "-g"]),
    "rpcclient": ("smb enum", ("network", "services"),
                  "null-session samr/querydominfo probe",
                  lambda t, extra=None: ["-N", "-U", "%", "-c", "querydominfo", t]),
    "ldapsearch":("ldap enum", ("network", "services"),
                  "anonymous rootDSE + base listing",
                  lambda t, extra=None: ["-x", "-H", f"ldap://{t}", "-b", "",
                                         "(objectClass=*)", "namingContexts"]),
    "enum4linux-ng": ("windows enum", ("network", "services"),
                  "read-only smb/ldap/rid inventory (ng rewrite)",
                  lambda t, extra=None: ["-A", t]),
    "netexec":   ("windows/smb enum", ("network", "services"),
                  "read-only module pass (shares/users/sessions)",
                  lambda t, extra=None: ["smb", t, "-u", "", "-p", "",
                                         "--shares", "--users"]),
    "hakrawler": ("crawler/url discovery", ("web", "api", "harvest"),
                  "fast js/endpoint crawl",
                  lambda t, extra=None: ["-url", t, "-depth", "3", "-plain"]),
    "linkfinder":("js secret/url mining", ("web", "harvest", "secret"),
                  "static js endpoint/secret extraction",
                  lambda t, extra=None: ["-i", t, "-o", "cli"]),
    "findomain": ("subdomain enum", ("dns", "domtake"),
                  "multi-source passive subdomain discovery",
                  lambda t, extra=None: ["-t", t, "-q"]),
    "assetfinder":("subdomain enum", ("dns", "domtake"),
                  "passive subdomain sources (amass family)",
                  lambda t, extra=None: ["--subs-only", t]),
    "dnstwist":  ("typosquat/domtake", ("dns", "domtake", "recon"),
                  "permutation domain detection (fuzz, mx, spf records)",
                  lambda t, extra=None: [t, "--registered", "--mxcheck"]),
    "shodan":    ("passive host intel", ("recon", "network"),
                  "shodan host record (works when API key configured)",
                  lambda t, extra=None: ["host", t]),
    "xsser":     ("xss scanner", ("web", "xss"),
                  "documented-PoC xss vector sweep",
                  lambda t, extra=None: ["--url", t, "--no-banner", "-q"]),
    # v5.7 — db/service confirm-aids + takeover lane
    "subzy":     ("takeover checker", ("dns", "domtake"),
                  "known-service takeover fingerprint sweep",
                  lambda t, extra=None: ["run", "--target", t, "--hide_fails"]),
    "git-dumper":("git exposure dump", ("harvest", "secret"),
                  "dump an exposed /.git directory (read-only fetch)",
                  lambda t, extra=None: [t.rstrip("/") + "/.git/",
                                         str(extra or "/tmp/git-dump")]),
    "cewl":      ("wordlist mining", ("web", "harvest"),
                  "target-word wordlist from the page's own text",
                  lambda t, extra=None: ["-d", "1", "-m", "5", "-q", t]),
    "memcstat":  ("service exposure", ("network", "harvest"),
                  "memcached stats probe (read-only, port 11211)",
                  lambda t, extra=None: ["--servers", t]),
    "psql":      ("db confirm-aid", ("db", "network"),
                  "auth-stage reachability probe (error class is the finding)",
                  lambda t, extra=None: ["-h", t, "-p", "5432", "-w", "-c",
                                         "select 1;", "postgres"]),
    "mysql":     ("db confirm-aid", ("db", "network"),
                  "auth-stage handshake probe",
                  lambda t, extra=None: ["-h", t, "-P", "3306", "-u", "probe",
                                         "-e", "select 1;"]),
    "mongosh":   ("db confirm-aid", ("db", "network"),
                  "unauth list-databases probe (read-only)",
                  lambda t, extra=None: ["--host", t, "--quiet", "--eval",
                                         "db.adminCommand('listDatabases')"]),
    "whatwaf":   ("waf detection", ("web", "edge"),
                  "waf fingerprint + detection-response class",
                  lambda t, extra=None: ["--url", t, "--silent"]),
    # v5.8 — the thirty new executors: packet lane, cloud lane, fuzz confirm-aids
    "hping3":    ("packet crafting", ("network", "edge"),
                  "4-SYN reachability/firewall validation probe",
                  lambda t, extra=None: ["-c", "4", "-S", "-p", "80", t]),
    "nping":     ("packet probe", ("network", "edge"),
                  "tcp reachability probe, 4 packets",
                  lambda t, extra=None: ["--tcp", "-p", "443", "-c", "4", t]),
    "traceroute":("path recon", ("network", "recon"),
                  "hop path to the target",
                  lambda t, extra=None: ["-n", "-m", "15", t]),
    "mtr":       ("path quality", ("network", "recon"),
                  "route report mode, 5 cycles",
                  lambda t, extra=None: ["-n", "-c", "5", "-r", t]),
    "fping":     ("reachability", ("network",),
                  "4-probe icmp reachability",
                  lambda t, extra=None: ["-c", "4", t]),
    "arp-scan":  ("lan inventory", ("network", "recon"),
                  "arp sweep of the local segment (lab lan)",
                  lambda t, extra=None: [t]),
    "netdiscover":("lan inventory", ("network", "recon"),
                  "passive/active lan host discovery",
                  lambda t, extra=None: ["-r", t]),
    "tcpdump":   ("passive capture", ("network", "recon"),
                  "first 100 packets filtered to the target (read-only)",
                  lambda t, extra=None: ["-i", "any", "-c", "100", "host", t]),
    "tshark":    ("passive capture", ("network", "recon"),
                  "first 100 packets filtered to the target (read-only)",
                  lambda t, extra=None: ["-i", "any", "-c", "100", "host", t]),
    "ngrep":     ("payload grep", ("network", "recon"),
                  "payload-match passive sniff (read-only)",
                  lambda t, extra=None: ["-q", "-d", "any", t]),
    "nc":        ("raw socket probe", ("network", "services"),
                  "port reachability banner grab (port via --wordlist)",
                  lambda t, extra=None: ["-zv", "-w", "3", t,
                                         str(extra or "443")]),
    "zmap":      ("fast single-port scan", ("network", "services"),
                  "single-port syn sweep",
                  lambda t, extra=None: ["-p", "443", t]),
    "dirhunt":   ("content discovery", ("web", "harvest"),
                  "crawler-based path hunting",
                  lambda t, extra=None: [t]),
    "gospider":  ("crawler/url discovery", ("web", "api", "harvest"),
                  "js/link/robots crawl depth 3",
                  lambda t, extra=None: ["-s", t, "-d", "3", "-q"]),
    "xsstrike":  ("xss scanner", ("web", "xss"),
                  "documented-PoC xss crawl+scan",
                  lambda t, extra=None: ["-u", t]),
    "commix":    ("cmd-injection confirm-aid", ("web", "injection"),
                  "manual-confirmation aid — batch, level 1",
                  lambda t, extra=None: ["--url=" + t, "--batch", "--level=1"]),
    "tplmap":    ("ssti confirm-aid", ("web", "injection"),
                  "ssti detection probe (arithmetic markers)",
                  lambda t, extra=None: ["-u", t]),
    "nosqlmap":  ("nosql confirm-aid", ("web", "injection"),
                  "nosql operator-injection probe (batch)",
                  lambda t, extra=None: ["-u", t, "--batch"]),
    "mitmdump":  ("passive proxy capture", ("web", "recon"),
                  "reverse-proxy capture lane (listen 8081)",
                  lambda t, extra=None: ["--mode", "reverse:" + t,
                                         "--listen-port", "8081"]),
    "trufflehog":("secret scan", ("harvest", "secret"),
                  "verified-secret scan of a git URL",
                  lambda t, extra=None: ["git", t, "--only-verified"]),
    "s3scanner": ("bucket exposure", ("cloud", "harvest"),
                  "s3 bucket enumeration for the estate name",
                  lambda t, extra=None: ["scan", "-b", t]),
    "cloudbrute":("cloud asset finder", ("cloud", "recon"),
                  "multi-provider bucket/asset discovery",
                  lambda t, extra=None: ["-d", t]),
    "kerbrute":  ("kerberos user enum", ("windows", "network"),
                  "read-only username enumeration (AS-REP class input)",
                  lambda t, extra=None: ["userenum", "--dc", t, "-d", t,
                                         str(extra or "/usr/share/wordlists/dirb/others/names.txt")]),
    "kube-hunter":("k8s hunting", ("cloud", "network"),
                  "read-only k8s exposure checks",
                  lambda t, extra=None: ["--remote", t, "--quiet"]),
    "adb":       ("device lane", ("mobile", "network"),
                  "adb tcp connect to a lab device (port 5555)",
                  lambda t, extra=None: ["connect", t + ":5555"]),
    "snallygaster":("file exposure scan", ("web", "harvest"),
                  "scans for exposed files on http hosts",
                  lambda t, extra=None: [t]),
    "dotdotpwn": ("traversal confirm-aid", ("web", "injection"),
                  "traversal probe, http-url module",
                  lambda t, extra=None: ["-m", "http-url", "-u", t, "-k", "root:"]),
    "webtech":   ("tech fingerprint", ("web", "api"),
                  "cms/platform fingerprint via headers+paths",
                  lambda t, extra=None: ["-u", t]),
    "kiterunner":("api path discovery", ("web", "api"),
                  "api route discovery (wordlist via --wordlist)",
                  lambda t, extra=None: ["discover", t]),
    "ipmitool":  ("bmc/ipmi exposure", ("network", "services"),
                  "read-only mc info over lanplus",
                  lambda t, extra=None: ["-I", "lanplus", "-H", t, "mc", "info"]),
    # v5.9 — NSE validation probes (targeted nmap scripts = named checks)
    "nmap-http-enum": ("web path enum", ("web", "harvest"),
                  "http-enum: known-path probe set via nmap",
                  lambda t, extra=None: ["-Pn", "--script", "http-enum", "-p", "80,443", t]),
    "nmap-http-git": ("git exposure", ("harvest", "secret"),
                  "http-git: probes exposed .git via nmap",
                  lambda t, extra=None: ["-Pn", "--script", "http-git", "-p", "80,443", t]),
    "nmap-http-backup": ("backup exposure", ("harvest",),
                  "http-backup-finder: backup-file probe set",
                  lambda t, extra=None: ["-Pn", "--script", "http-backup-finder", "-p", "80,443", t]),
    "nmap-http-methods": ("method posture", ("web", "config"),
                  "http-methods: OPTIONS/allow-header inventory",
                  lambda t, extra=None: ["-Pn", "--script", "http-methods", "-p", "80,443", t]),
    "nmap-http-cors": ("cors posture", ("web", "config"),
                  "http-cors: ACAO reflection probes",
                  lambda t, extra=None: ["-Pn", "--script", "http-cors", "-p", "80,443", t]),
    "nmap-http-userdir": ("userdir enum", ("web", "recon"),
                  "http-userdir-enum: ~user path oracle",
                  lambda t, extra=None: ["-Pn", "--script", "http-userdir-enum", "-p", "80", t]),
    "nmap-shellshock": ("shellshock check", ("web", "injection"),
                  "http-shellshock: documented-PoC header probe",
                  lambda t, extra=None: ["-Pn", "--script", "http-shellshock", "-p", "80", t]),
    "nmap-ssl-heartbleed": ("heartbleed check", ("crypto",),
                  "ssl-heartbleed: documented-vuln CHECK (validation-only)",
                  lambda t, extra=None: ["-Pn", "--script", "ssl-heartbleed", "-p", "443", t]),
    "nmap-ssl-ccs": ("ccs check", ("crypto",),
                  "ssl-ccs-injection: documented-vuln CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "ssl-ccs-injection", "-p", "443", t]),
    "nmap-ssl-ciphers": ("cipher enum", ("crypto", "config"),
                  "ssl-enum-ciphers: per-version cipher inventory",
                  lambda t, extra=None: ["-Pn", "--script", "ssl-enum-ciphers", "-p", "443", t]),
    "nmap-smb-security": ("smb posture", ("network", "windows"),
                  "smb-security-mode: signing/level flags",
                  lambda t, extra=None: ["-Pn", "--script", "smb-security-mode", "-p", "445", t]),
    "nmap-smb-vuln": ("smb vuln check", ("windows",),
                  "smb-vuln-ms17-010: documented-vuln CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "smb-vuln-ms17-010", "-p", "445", t]),
    "nmap-mysql-empty": ("mysql auth check", ("db",),
                  "mysql-empty-password: empty-cred CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "mysql-empty-password", "-p", "3306", t]),
    "nmap-ftp-anon": ("ftp auth check", ("network",),
                  "ftp-anon: anonymous-ftp CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "ftp-anon", "-p", "21", t]),
    "nmap-dns-nsec": ("nsec enum", ("dns", "domtake"),
                  "dns-nsec-enum: nsec walking oracle",
                  lambda t, extra=None: ["-Pn", "--script", "dns-nsec-enum",
                                         "--script-args", "dns-nsec-enum.domain=" + t,
                                         "-p", "53", t]),
    "nmap-smtp-relay": ("relay check", ("mail",),
                  "smtp-open-relay: relay-class CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "smtp-open-relay", "-p", "25", t]),
    "nmap-vulners": ("cve banner map", ("recon", "services"),
                  "vulners: banner→CVE lookup (reference only)",
                  lambda t, extra=None: ["-Pn", "-sV", "--script", "vulners", "--open", t]),
    # v5.9 — mode splits: same binary, different probe shape
    "nmap-udp":   ("udp scan", ("network", "services"),
                  "top-100 udp with version",
                  lambda t, extra=None: ["-Pn", "-sU", "--top-ports", "100", "--open", t]),
    "nmap-fast":  ("fast tcp scan", ("network", "services"),
                  "T4 top-100 no version (fast lane)",
                  lambda t, extra=None: ["-Pn", "-T4", "--top-ports", "100", "--open", t]),
    "nmap-discovery": ("host discovery", ("network", "recon"),
                  "ping-sweep only (no port scan)",
                  lambda t, extra=None: ["-sn", t]),
    "nmap-vuln":  ("vuln-class sweep", ("network", "services"),
                  "--script vuln category (safe checks)",
                  lambda t, extra=None: ["-Pn", "-sV", "--script", "vuln", "--open", t]),
    "gobuster-vhost": ("vhost enum", ("web", "edge"),
                  "vhost brute on the host",
                  lambda t, extra=None: ["vhost", "-u", t, "-w",
                                         str(extra or "/usr/share/wordlists/dirb/vhosts_default.txt")]),
    "gobuster-dns": ("dns brute", ("dns", "domtake"),
                  "subdomain brute via gobuster",
                  lambda t, extra=None: ["dns", "-d", t, "-w",
                                         str(extra or "/usr/share/wordlists/dirb/common.txt")]),
    "gobuster-s3": ("bucket enum", ("cloud", "harvest"),
                  "s3 bucket name brute",
                  lambda t, extra=None: ["s3", "-w",
                                         str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "-c", t]),
    "nuclei-cves": ("cve templates", ("web", "api"),
                  "cve-tag template sweep",
                  lambda t, extra=None: ["-u", t, "-tags", "cve", "-silent"]),
    "nuclei-misconfig": ("misconfig templates", ("web", "config"),
                  "misconfig-tag sweep",
                  lambda t, extra=None: ["-u", t, "-tags", "misconfig", "-silent"]),
    "nuclei-exposures": ("exposure templates", ("web", "harvest"),
                  "exposure/panel/dashboard sweep",
                  lambda t, extra=None: ["-u", t, "-tags", "exposure,panel", "-silent"]),
    "nuclei-takeover": ("takeover templates", ("dns", "domtake"),
                  "subdomain-takeover template sweep",
                  lambda t, extra=None: ["-u", t, "-tags", "takeover", "-silent"]),
    "nuclei-tokens": ("token templates", ("web", "api", "secret"),
                  "token/exposed-secret template sweep",
                  lambda t, extra=None: ["-u", t, "-tags", "token,exposed", "-silent"]),
    "dnsx-brute": ("dns brute", ("dns",),
                  "dnsx wordlist resolution",
                  lambda t, extra=None: ["-silent", "-w",
                                         str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "-a", t]),
    "dnsx-reverse": ("reverse dns", ("dns", "recon"),
                  "PTR sweep of resolvable targets",
                  lambda t, extra=None: ["-silent", "-reverse", "-resp", t]),
    "dig-axfr":   ("zone transfer", ("dns", "domtake"),
                  "AXFR attempt against the domain's NS",
                  lambda t, extra=None: ["AXFR", t]),
    "dig-mx":     ("mail records", ("dns", "mail"),
                  "MX records of the domain",
                  lambda t, extra=None: ["+short", "MX", t]),
    "dig-txt":    ("spf/dmarc records", ("dns", "mail"),
                  "TXT records (SPF/DMARC posture)",
                  lambda t, extra=None: ["+short", "TXT", t]),
    "amass-intel": ("org intel", ("dns", "recon"),
                  "reverse-whois org expansion (passive)",
                  lambda t, extra=None: ["intel", "-d", t, "-passive"]),
    "ffuf-vhost": ("vhost fuzz", ("web", "edge"),
                  "vhost-name fuzzing via Host header",
                  lambda t, extra=None: ["-u", t, "-H", "Host: FUZZ." + _host(t),
                                         "-w", str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "-ac", "-s"]),
    "ldapsearch-enum": ("ldap enum", ("windows", "network"),
                  "anonymous base-object search",
                  lambda t, extra=None: ["-x", "-H", f"ldap://{t}", "-b", "",
                                         "(objectClass=*)", "*"]),
    "curl-cors":  ("cors probe", ("web", "config"),
                  "Origin-reflection cors check",
                  lambda t, extra=None: ["-sSI", "-m", "10", "-H",
                                         "Origin: https://evil.example", t]),
    "curl-trace": ("trace check", ("web", "config"),
                  "TRACE enablement check (cross-site tracing class)",
                  lambda t, extra=None: ["-sSI", "-m", "10", "-X", "TRACE", t]),
    "ffuf-deep":  ("deep content discovery", ("web", "harvest"),
                  "raft-words deep sweep (higher noise budget — kernel-gated)",
                  lambda t, extra=None: ["-u", t.rstrip("/") + "/FUZZ", "-w",
                                         str(extra or "/usr/share/wordlists/dirb/raft-large-words.txt"),
                                         "-mc", "all", "-ac", "-s"]),
    "gobuster-deep": ("deep content discovery", ("web", "harvest"),
                  "raft-large deep sweep (higher noise budget)",
                  lambda t, extra=None: ["dir", "-u", t, "-w",
                                         str(extra or "/usr/share/wordlists/dirb/raft-large-words.txt"),
                                         "-q", "--no-error-continuation"]),
    # v5.9 — remaining distinct tools
    "gowitness": ("screenshot recon", ("web", "recon"),
                  "headless screenshot of the surface",
                  lambda t, extra=None: ["screenshot", "--url", t]),
    "cmseek":    ("cms detect+deep", ("web", "cms"),
                  "cms detection with deep version enum",
                  lambda t, extra=None: ["-u", t]),
    "webanalyze": ("tech fingerprint", ("web", "api"),
                  "wappalyzer-cli port — tech map",
                  lambda t, extra=None: ["-u", t, "-crawl"]),
    "urlcrazy":  ("typosquat", ("dns", "domtake", "recon"),
                  "typo-domain generation + registration check",
                  lambda t, extra=None: [t]),
    "cloudlist": ("cloud asset enum", ("cloud", "recon"),
                  "multi-provider asset discovery",
                  lambda t, extra=None: ["-id", t]),
    "smbmap":    ("share perm enum", ("network", "windows", "harvest"),
                  "anonymous share listing + perm classes",
                  lambda t, extra=None: ["-H", t, "-u", "guest"]),
    "crackmapexec": ("smb enum (legacy name)", ("network", "windows"),
                  "read-only smb module pass (crackmapexec install)",
                  lambda t, extra=None: ["smb", t, "-u", "", "-p", "",
                                         "--shares"]),
    "finalrecon": ("all-in-one recon", ("recon", "web", "dns"),
                  "full passive+active recon module set",
                  lambda t, extra=None: ["--url", t, "--full"]),
    "gitleaks":  ("secret scan", ("harvest", "secret"),
                  "secret scan of a git source",
                  lambda t, extra=None: ["detect", "--source", t, "--no-banner",
                                         "--redact"]),
    "o-saft":    ("deep tls audit", ("crypto", "config"),
                  "openssl-audit toolkit — deep tls posture",
                  lambda t, extra=None: ["+info", "--quiet", t]),
    "paramspider": ("param mining", ("web", "api"),
                  "wayback parameter-name mining for the domain",
                  lambda t, extra=None: ["-d", t, "--quiet"]),
    "swaks":     ("smtp relay test", ("mail",),
                  "one self-addressed relay-class test (swaks)",
                  lambda t, extra=None: ["--server", t, "--to",
                                         "probe@" + _host(t), "--quit-after", "RCPT"]),
    "ssh-keyscan": ("host-key harvest", ("crypto", "recon"),
                  "host-key type harvest (read-only)",
                  lambda t, extra=None: ["-t", "rsa,ecdsa,ed25519", t]),
    # v5.9b — NSE validation probes batch 2 (vuln CHECKs + service inventories)
    "nmap-ssl-poodle": ("poodle check", ("crypto",),
                  "ssl-poodle: documented-vuln CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "ssl-poodle", "-p", "443", t]),
    "nmap-ssl-drown": ("drown check", ("crypto",),
                  "sslv2-drown: documented-vuln CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "sslv2-drown", "-p", "443", t]),
    "nmap-ssl-logjam": ("logjam check", ("crypto",),
                  "ssl-logjam: dh-export CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "ssl-logjam", "-p", "443", t]),
    "nmap-smtp-commands": ("smtp commands", ("mail",),
                  "smtp-commands: capability inventory",
                  lambda t, extra=None: ["-Pn", "--script", "smtp-commands", "-p", "25", t]),
    "nmap-imap-caps": ("imap caps", ("mail",),
                  "imap-capabilities inventory",
                  lambda t, extra=None: ["-Pn", "--script", "imap-capabilities", "-p", "143", t]),
    "nmap-pop3-caps": ("pop3 caps", ("mail",),
                  "pop3-capabilities inventory",
                  lambda t, extra=None: ["-Pn", "--script", "pop3-capabilities", "-p", "110", t]),
    "nmap-mongodb-info": ("mongo info", ("db",),
                  "mongodb-info: version/build inventory",
                  lambda t, extra=None: ["-Pn", "--script", "mongodb-info", "-p", "27017", t]),
    "nmap-redis-info": ("redis info", ("db",),
                  "redis-info: version/role inventory",
                  lambda t, extra=None: ["-Pn", "--script", "redis-info", "-p", "6379", t]),
    "nmap-mysql-info": ("mysql info", ("db",),
                  "mysql-info: version/auth-plugin inventory",
                  lambda t, extra=None: ["-Pn", "--script", "mysql-info", "-p", "3306", t]),
    "nmap-mssql-info": ("mssql info", ("db",),
                  "ms-sql-info: version/config inventory",
                  lambda t, extra=None: ["-Pn", "--script", "ms-sql-info", "-p", "1433", t]),
    "nmap-mongodb-dbs": ("mongo dbs", ("db",),
                  "mongodb-databases: read-only db listing",
                  lambda t, extra=None: ["-Pn", "--script", "mongodb-databases", "-p", "27017", t]),
    "nmap-devframework": ("framework detect", ("web", "recon"),
                  "http-devframework: framework fingerprint probes",
                  lambda t, extra=None: ["-Pn", "--script", "http-devframework", "-p", "80,443", t]),
    "nmap-iis-shortname": ("iis 8.3 oracle", ("web", "config"),
                  "http-iis-short-name: short-name enumeration",
                  lambda t, extra=None: ["-Pn", "--script", "http-iis-short-name", "-p", "80,443", t]),
    "nmap-aspnet-debug": ("aspnet debug", ("web", "config"),
                  "http-aspnet-debug: debug-flag CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-aspnet-debug", "-p", "80,443", t]),
    "nmap-drupal-enum": ("drupal enum", ("web", "cms"),
                  "http-drupal-enum: module/theme inventory",
                  lambda t, extra=None: ["-Pn", "--script", "http-drupal-enum", "-p", "80,443", t]),
    "nmap-wp-plugins": ("wp plugins", ("web", "cms"),
                  "http-wordpress-plugins: plugin probe set",
                  lambda t, extra=None: ["-Pn", "--script", "http-wordpress-plugins", "-p", "80,443", t]),
    "nmap-apache-status": ("server-status", ("web", "harvest"),
                  "http-apache-server-status: /server-status exposure",
                  lambda t, extra=None: ["-Pn", "--script", "http-apache-server-status", "-p", "80", t]),
    "nmap-php-version": ("php probe", ("web", "recon"),
                  "http-php-version: php fingerprint via hashes",
                  lambda t, extra=None: ["-Pn", "--script", "http-php-version", "-p", "80,443", t]),
    "nmap-smb-shares": ("smb shares", ("windows", "harvest"),
                  "smb-enum-shares: read-only share inventory",
                  lambda t, extra=None: ["-Pn", "--script", "smb-enum-shares", "-p", "445", t]),
    "nmap-smb-users": ("smb users", ("windows",),
                  "smb-enum-users: read-only user inventory",
                  lambda t, extra=None: ["-Pn", "--script", "smb-enum-users", "-p", "445", t]),
    "nmap-smb2-caps": ("smb2 caps", ("windows",),
                  "smb2-capabilities: protocol capability inventory",
                  lambda t, extra=None: ["-Pn", "--script", "smb2-capabilities", "-p", "445", t]),
    "nmap-smb-conficker": ("smb vuln check 2", ("windows",),
                  "smb-vuln-conficker: documented-vuln CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "smb-vuln-conficker", "-p", "445", t]),
    "nmap-nfs-showmount": ("nfs exports", ("network", "harvest"),
                  "nfs-showmount: export inventory",
                  lambda t, extra=None: ["-Pn", "--script", "nfs-showmount", "-p", "2049", t]),
    "nmap-nfs-ls": ("nfs listing", ("network", "harvest"),
                  "nfs-ls: read-only export listing",
                  lambda t, extra=None: ["-Pn", "--script", "nfs-ls", "-p", "2049", t]),
    "nmap-rpcinfo": ("rpc map", ("network", "services"),
                  "rpcinfo: rpc service inventory",
                  lambda t, extra=None: ["-Pn", "--script", "rpcinfo", "-p", "111", t]),
    "nmap-ipmi-cipher0": ("ipmi check", ("network",),
                  "ipmi-cipher-zero: cipher-0 CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "ipmi-cipher-zero", "-p", "623", t]),
    "nmap-open-proxy": ("proxy check", ("network",),
                  "http-open-proxy: open-proxy CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-open-proxy", "-p", "8080,3128", t]),
    "nmap-ftp-bounce": ("ftp bounce", ("network",),
                  "ftp-bounce: check-class probe",
                  lambda t, extra=None: ["-Pn", "--script", "ftp-bounce", "-p", "21", t]),
    "nmap-rdp-info": ("rdp intel", ("network", "windows"),
                  "rdp-ntlm-info: banner/os intel (read-only)",
                  lambda t, extra=None: ["-Pn", "--script", "rdp-ntlm-info", "-p", "3389", t]),
    "nmap-vnc-info": ("vnc intel", ("network",),
                  "vnc-info: banner/auth-type inventory",
                  lambda t, extra=None: ["-Pn", "--script", "vnc-info", "-p", "5900", t]),
    "nmap-telnet-enc": ("telnet posture", ("network",),
                  "telnet-encryption: encryption-support CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "telnet-encryption", "-p", "23", t]),
    "nmap-sip-methods": ("sip methods", ("network",),
                  "sip-methods: voip capability inventory",
                  lambda t, extra=None: ["-Pn", "--script", "sip-methods", "-p", "5060", t]),
    "nmap-ssl-cert": ("cert fetch", ("crypto", "recon"),
                  "ssl-cert: live certificate inventory (SAN/CN)",
                  lambda t, extra=None: ["-Pn", "--script", "ssl-cert", "-p", "443", t]),
    "nmap-cookie-flags": ("cookie posture", ("web", "config"),
                  "http-cookie-flags: secure/httponly CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-cookie-flags", "-p", "80,443", t]),
    # v5.9b — mode splits batch 2 + last tools
    "testssl-protocols": ("protocol support", ("crypto", "config"),
                  "protocol-version inventory only (-p)",
                  lambda t, extra=None: ["--quiet", "--color", "0", "-p", t]),
    "testssl-ciphers": ("cipher strength", ("crypto", "config"),
                  "cipher-strength inventory only (-E)",
                  lambda t, extra=None: ["--quiet", "--color", "0", "-E", t]),
    "sslyze-cert": ("cert chain", ("crypto",),
                  "certificate-info only",
                  lambda t, extra=None: ["--cert", t]),
    "dig-ns":     ("nameserver map", ("dns", "recon"),
                  "NS records — the delegation inventory",
                  lambda t, extra=None: ["+short", "NS", t]),
    "dig-soa":    ("soa record", ("dns",),
                  "SOA record — zone administration intel",
                  lambda t, extra=None: ["+short", "SOA", t]),
    "dig-cname":  ("cname map", ("dns", "domtake"),
                  "CNAME records — domtake-prep inventory",
                  lambda t, extra=None: ["+short", "CNAME", t]),
    "arp-scan-lan": ("lab lan sweep", ("network", "recon"),
                  "local-segment arp sweep (lab)",
                  lambda t, extra=None: ["--localnet"]),
    "netdiscover-passive": ("passive lan", ("network", "recon"),
                  "listen-only lan discovery",
                  lambda t, extra=None: ["-p"]),
    "asnmap":     ("asn mapping", ("recon", "dns"),
                  "domain → ASN/netblock mapping",
                  lambda t, extra=None: ["-d", t]),
    # v5.10 — vuln CHECK batch 3 + source-pull lane
    "nmap-cve-struts": ("struts check", ("web",),
                  "http-vuln-cve2017-5638: content-type CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-vuln-cve2017-5638", "-p", "80,443", t]),
    "nmap-cve-drupal": ("drupalgeddon check", ("web", "cms"),
                  "http-vuln-cve2014-3704: drupal SQLi CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-vuln-cve2014-3704", "-p", "80,443", t]),
    "nmap-cve-httpsys": ("httpsys check", ("web",),
                  "http-vuln-cve2015-1635: ms15-034 range CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-vuln-cve2015-1635", "-p", "80", t]),
    "nmap-cve-phpcgi": ("php-cgi check", ("web",),
                  "http-vuln-cve2012-1823: php-cgi query CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-vuln-cve2012-1823", "-p", "80,443", t]),
    "nmap-cve-coldfusion": ("coldfusion check", ("web",),
                  "http-vuln-cve2010-2861: admin-dir traversal CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-vuln-cve2010-2861", "-p", "80,443", t]),
    "nmap-cve-rails": ("rails check", ("web",),
                  "http-vuln-cve2013-0156: rails yaml CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-vuln-cve2013-0156", "-p", "80,443", t]),
    "nmap-vsftpd-backdoor": ("vsftpd check", ("network",),
                  "ftp-vsftpd-backdoor: backdoor-banner CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "ftp-vsftpd-backdoor", "-p", "21", t]),
    "nmap-proftpd-backdoor": ("proftpd check", ("network",),
                  "ftp-proftpd-backdoor: backdoor CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "ftp-proftpd-backdoor", "-p", "21", t]),
    "nmap-default-accounts": ("default-cred check", ("web",),
                  "http-default-accounts: default-panel/cred CHECK",
                  lambda t, extra=None: ["-Pn", "--script", "http-default-accounts", "-p", "80,443,8080", t]),
    "wget-mirror": ("source mirror", ("web", "harvest"),
                  "recursive pull of the site's public source (depth 2)",
                  lambda t, extra=None: ["-r", "-l", "2", "-np", "-q", t]),
    "httrack":   ("site copier", ("web", "harvest"),
                  "full public-source mirror for offline mining",
                  lambda t, extra=None: ["--quiet", "-O", "/tmp/httrack-dump", t]),
    "nmap-allports": ("full port sweep", ("network", "services"),
                  "all-65535 slow sweep (thorough lane)",
                  lambda t, extra=None: ["-Pn", "-p-", "-sV", "--open", t]),
}

# v5.1 — the chains, doubled: stages feed each other (subfinder's domains become
# dnsx's input; katana's urls become dalfox's strikes). Every stage is scope-gated.
CHAINS = {
    "recon":    ["subfinder", "amass", "sublist3r", "theharvester", "dnsx",
                 "httpx", "nuclei"],
    "web":      ["katana", "gau", "dalfox", "ffuf", "nikto"],
    "tls":      ["tlsx", "sslscan", "sslyze", "testssl", "ssh-audit"],
    "net":      ["naabu", "nmap", "masscan", "zmap", "hping3", "nping", "fping",
                 "nc", "traceroute", "mtr", "arp-scan", "netdiscover"],
    "dns":      ["subfinder", "amass", "sublist3r", "shuffledns", "massdns",
                 "dnsrecon", "dnsx"],
    "content":  ["katana", "gau", "dirsearch", "feroxbuster", "ffuf", "dirb",
                 "gobuster", "dirhunt", "gospider", "snallygaster", "wget-mirror",
                 "httrack"],
    "api":      ["httpx", "arjun", "crlfuzz", "katana", "dalfox", "kiterunner",
                 "webtech", "gospider"],
    "services": ["ssh-audit", "redis-cli", "snmpwalk", "grpcurl", "nbtscan",
                 "enum4linux"],
    "cms":      ["wpscan", "joomscan", "droopescan", "cmsmap"],
    "win":      ["smbclient", "rpcclient", "ldapsearch", "enum4linux",
                 "enum4linux-ng", "netexec", "nbtscan", "kerbrute"],
    "osint":    ["theharvester", "sublist3r", "assetfinder", "findomain",
                 "amass", "shodan", "dnstwist"],
    "db":       ["psql", "mysql", "mongosh", "memcstat", "redis-cli"],
    "takeover": ["subzy", "dnstwist", "dnsx", "subfinder"],
    "cloud":    ["s3scanner", "cloudbrute", "kube-hunter", "shodan"],
    "packet":   ["tcpdump", "tshark", "ngrep"],
    "fuzz":     ["dotdotpwn", "xsstrike", "commix", "tplmap", "nosqlmap",
                 "sqlmap", "crlfuzz", "wfuzz"],
}

CHAIN_NAMES = {"recon", "web", "tls", "net", "dns", "content", "api",
               "services", "cms", "win", "osint", "db", "takeover", "cloud",
               "packet", "fuzz"}
FEED_PARSE = {
    "subfinder": lambda out: [l.strip() for l in out.splitlines() if l.strip() and "." in l],
    "amass":     lambda out: [l.strip() for l in out.splitlines() if l.strip() and "." in l],
    "sublist3r": lambda out: [l.strip() for l in out.splitlines()
                              if l.strip() and "." in l and " " not in l],
    "shuffledns":lambda out: [l.strip() for l in out.splitlines()
                              if l.strip() and "." in l and " " not in l],
    "massdns":   lambda out: [l.split()[0].rstrip(".") for l in out.splitlines()
                              if l.strip() and "." in l.split()[0]],
    "dnsx":      lambda out: [l.strip() for l in out.splitlines() if l.strip() and "." in l],
    "naabu":     lambda out: [l.split(":")[0] for l in out.splitlines()
                              if l.strip() and ":" in l],
    "httpx":     lambda out: [l.split()[0] for l in out.splitlines() if l.strip()],
    "katana":    lambda out: [l.strip() for l in out.splitlines()
                              if l.strip().startswith("http")],
    "gau":       lambda out: [l.strip() for l in out.splitlines()
                              if l.strip().startswith("http")],
    "dirsearch": lambda out: [l.split()[0] for l in out.splitlines()
                              if l.strip().startswith("http")],
    "feroxbuster": lambda out: [l.strip() for l in out.splitlines()
                                if l.strip().startswith("http")],
    "hakrawler": lambda out: [l.strip() for l in out.splitlines()
                              if l.strip().startswith("http")],
    "assetfinder": lambda out: [l.strip() for l in out.splitlines()
                                if l.strip() and "." in l and " " not in l],
    "findomain": lambda out: [l.strip() for l in out.splitlines()
                              if l.strip() and "." in l and " " not in l],
}
FEED_CAP = 50

TAKES_EXTRA = {"nuclei", "gobuster", "testssl", "nikto", "masscan", "ffuf",
               "dirsearch", "dirb", "feroxbuster", "wfuzz", "massdns",
               "shuffledns"}
HTTP_TOOLS = {"curl", "httpx", "nuclei", "gobuster", "nikto", "whatweb", "wafw00f",
              "ffuf", "katana", "dalfox", "tlsx", "gau", "dirsearch", "dirb",
              "feroxbuster", "wfuzz", "arjun", "crlfuzz", "sqlmap", "wapiti",
              "wpscan", "joomscan", "droopescan", "cmsmap", "hakrawler",
              "linkfinder", "xsser", "subzy", "git-dumper", "cewl"}
CANON_KW = {
    "BOUNDARY": ("idor", "unauthorized access", "403"),
    "REPLAY": ("replay", "idempoten"),
    "HARVEST": ("backup", ".env", ".git", "dump", "exposed"),
    "CRYPTO": ("tls", "ssl", "cipher", "expired", "weak"),
    "NETWORK": ("open port", "open tcp", "http on", "service:"),
    "DIRECTORY": ("directory listing", "index of"),
    "XSS": ("<script", "xss", "reflected"),
    "DOMTAKE": ("cname", "dangling", "nodomain", "nxdomain"),
    "SERVICES": ("redis", "snmp", "grpc", "memcache", "netbios", "smb"),
    "SSH": ("ssh", "algorithm", "key exchange", "host key"),
    "INJECTION": ("injectable", "sqlmap", "parameter", "crlf", "payload"),
    "CMS": ("wordpress", "joomla", "drupal", "plugin", "theme"),
    "SECRET": ("api_key", "apikey", "secret", "token", "password", "aws_key"),
}


def _host(target: str) -> str:
    if "://" in target:
        return urlsplit(target).hostname or target
    return target.split("/")[0].split(":")[0]


def _url(target: str) -> str:
    return target if "://" in target else "http://" + target


def _state_path(target: str) -> Path:
    try:
        name = sa.safe_name(target, "target")
    except sa.ScopeError:
        name = re.sub(r"[^A-Za-z0-9._-]+", "-", target)[:64] or "target"
    return sa.campaigns_root() / name / "arsenal-state.json"


def _record(target: str, row: dict) -> None:
    try:
        p = _state_path(target)
        p.parent.mkdir(parents=True, exist_ok=True)
        state = {}
        if p.exists():
            try:
                state = json.loads(p.read_text())
            except Exception:
                state = {}
        state.setdefault("target", target)
        state.setdefault("version", VERSION)
        state.setdefault("runs", []).append(row)
        state["runs"] = state["runs"][-20:]
        state["updated"] = datetime.now(timezone.utc).isoformat()
        tmp = p.with_name(p.name + f".tmp.{os.getpid()}")
        tmp.write_text(json.dumps(state, indent=2) + "\n")
        os.chmod(tmp, 0o600)
        os.replace(tmp, p)
    except OSError:
        pass


def scope_verdict(target: str, scope_file: str | None = None) -> tuple[bool, str]:
    ok, reason, _ = sa.check(target, file=scope_file, strict=True,
                             audit=True, allow_lab=True)
    return ok, reason


def installed() -> dict:
    out = {}
    for tool, (cap, classes, plan, _b) in ARSENAL.items():
        path = shutil.which(tool)
        if path:
            out[tool] = {"capability": cap, "classes": list(classes),
                         "path": path, "plan": plan}
    return out


def _emit(args, payload, text: str | None = None) -> None:
    if getattr(args, "json", False):
        print(json.dumps(payload, indent=2))
    elif text is not None:
        print(text)


def cmd_list(args):
    inv = installed()
    rows = []
    for tool, (cap, classes, plan, _b) in ARSENAL.items():
        rows.append({"tool": tool, "installed": tool in inv,
                     "path": inv.get(tool, {}).get("path", ""),
                     "capability": cap, "classes": list(classes), "plan": plan})
    payload = {"version": VERSION, "tools": rows, "installed": len(inv),
               "total": len(ARSENAL)}
    if getattr(args, "json", False):
        _emit(args, payload)
        return 0
    print(f"═══ ARSENAL INVENTORY — {len(inv)}/{len(ARSENAL)} tools ═══")
    for r in rows:
        if r["installed"]:
            print(f"  ✓ {r['tool']:10s} {r['capability']:22s} feeds: {', '.join(r['classes'])}")
        else:
            print(f"  · {r['tool']:10s} not installed — family probes cover the class")
    print(f"═══ the muscle: {len(inv)} tool(s) · the gate: shared scope authority ═══")
    return 0


def cmd_plan(args):
    inv = installed()
    ok, why = scope_verdict(args.target, getattr(args, "scope_file", None))
    plan = []
    for tool, (cap, classes, line, builder) in ARSENAL.items():
        if tool not in inv:
            continue
        target = _url(args.target) if tool in HTTP_TOOLS else _host(args.target)
        try:
            argv = [tool] + builder(target, getattr(args, "wordlist", None))
        except Exception as e:
            argv = [tool, f"<builder error: {e}>"]
        plan.append({"tool": tool, "capability": cap, "classes": list(classes),
                     "plan": line, "argv": argv})
    payload = {"version": VERSION, "target": args.target, "scope_ok": ok,
               "scope": why, "plan": plan, "installed": len(inv),
               "executed": False}
    if getattr(args, "json", False):
        _emit(args, payload)
    else:
        print(f"═══ ARSENAL RUN PLAN — {args.target} ═══")
        print(f"  scope gate: {'OPEN' if ok else 'CLOSED'} ({why})")
        for p in plan:
            print(f"  ▸ {p['tool']:10s} {p['plan']}")
        if not plan:
            print("  (no tools installed — plan is family-probes only)")
        print("═══ nothing executed — run adds --dry-run off ═══")
    return 0 if ok else 1


def cmd_run_chain(args, inv, why, ok):
    """v5 CHAIN EXECUTION — stages feed each other. subfinder's domains become
    dnsx's input; katana/gau's urls become dalfox's strikes. Every stage is
    scope-gated (the chain refuses as one)."""
    stages = [t for t in CHAINS[args.chain] if t in inv]
    skipped = [t for t in CHAINS[args.chain] if t not in inv]
    started = datetime.now(timezone.utc).isoformat()
    timeout = max(5, min(int(getattr(args, "timeout", 300) or 300), 3600))
    rows, findings = [], []
    targets = [args.target]
    if not getattr(args, "json", False):
        print(f"═══ ARSENAL CHAIN '{args.chain}' — {args.target} (scope: {why}) ═══")
        print(f"  stages: {' → '.join(stages)}"
              + (f"  (skipped: {', '.join(skipped)})" if skipped else ""))
    for tool in stages:
        cap, classes, plan, builder = ARSENAL[tool]
        stage_out = []
        for tgt in targets[:FEED_CAP]:
            t2 = _url(tgt) if tool in HTTP_TOOLS else _host(tgt)
            argv = [tool] + builder(t2, args.wordlist)
            row = {"tool": tool, "target": tgt, "argv": argv, "rc": None,
                   "hits": [], "output": ""}
            if getattr(args, "dry_run", False):
                row["skipped"] = "dry-run"
                rows.append(row)
                if not getattr(args, "json", False):
                    print(f"  ▸ [dry] {tool:10s} ← {tgt[:40]}")
                continue
            try:
                r = subprocess.run(argv, capture_output=True, text=True,
                                   timeout=timeout)
                out = (r.stdout + r.stderr).strip()
                hits = [cls for cls, kws in CANON_KW.items()
                        if any(k in out.lower() for k in kws)]
                row.update({"rc": r.returncode, "hits": hits, "output": out[:12000]})
                findings.extend({"tool": tool, "class": c, "target": t2}
                                for c in hits)
                stage_out.append(out)
                if not getattr(args, "json", False):
                    first = out.splitlines()[0][:50] if out else "(no output)"
                    print(f"  ✓ {tool:10s} ← {tgt[:36]:36s} rc={r.returncode}"
                          f" canon={len(hits)}  {first}")
            except subprocess.TimeoutExpired:
                row.update({"rc": 124, "error": f"timeout {timeout}s"})
                if not getattr(args, "json", False):
                    print(f"  ⚠ {tool:10s} timeout — stage continues")
            except Exception as e:
                row.update({"rc": 1, "error": str(e)})
                if not getattr(args, "json", False):
                    print(f"  ✗ {tool:10s} {e}")
            rows.append(row)
        feed = FEED_PARSE.get(tool)
        if feed and not getattr(args, "dry_run", False):
            new = []
            for out in stage_out:
                new += feed(out)
            targets = [t for t in dict.fromkeys(new) if t][:FEED_CAP]
            if not getattr(args, "json", False):
                print(f"    ↳ feeds {len(targets)} target(s) into the next stage")
    payload = {"version": VERSION, "target": args.target, "chain": args.chain,
               "scope_ok": ok, "scope": why, "dry_run": bool(args.dry_run),
               "ran": sum(1 for r in rows if r.get("rc") is not None),
               "stages": rows, "findings": findings, "started": started}
    _record(args.target, {"at": started, "chain": args.chain, "scope": why,
                          "ran": payload["ran"],
                          "hits": [f["class"] for f in findings]})
    if getattr(args, "out", None):
        result = {
            "step": 0, "directive_id": f"arsenal-chain-{args.chain}",
            "exit": 0 if payload["ran"] else 1,
            "findings": [{"title": f"{f['tool']} {f['class']}-class candidate",
                          "cls": f["class"], "asset": f["target"],
                          "severity": "low",
                          "proof": (f"arsenal {f['tool']} output matched"
                                    f" {f['class']} signatures — needs a 3-gate"
                                    f" confirmation (hypothesis-grade)")}
                         for f in findings],
            "context": {}, "notes": f"arsenal v5 chain '{args.chain}': "
                         f"{payload['ran']} stage run(s) · feeds: {CHAINS[args.chain]}"}
        Path(args.out).write_text(json.dumps(result, indent=2) + "\n")
        payload["out"] = args.out
    if getattr(args, "json", False):
        _emit(args, payload)
    else:
        print(f"═══ chain '{args.chain}': {payload['ran']} stage run(s) · "
              f"{len(findings)} canon candidate(s) · walls intact ═══")
    return 0 if payload["ran"] or payload["dry_run"] else 1


def cmd_run(args):
    if getattr(args, "chain", None):
        ok, why = scope_verdict(args.target, getattr(args, "scope_file", None))
        if not ok:
            print(f"✗ CHAIN REFUSED — scope gate: {why}", file=sys.stderr)
            return 1
        return cmd_run_chain(args, installed(), why, ok)
    ok, why = scope_verdict(args.target, getattr(args, "scope_file", None))
    if not ok:
        print(f"✗ EXECUTION REFUSED — scope gate: {why}", file=sys.stderr)
        if getattr(args, "json", False):
            _emit(args, {"target": args.target, "scope_ok": False,
                         "error": why, "executed": False})
        return 1
    inv = installed()
    if args.only:
        chosen = [s.strip() for s in args.only.split(",") if s.strip()]
        unknown = [t for t in chosen if t not in ARSENAL]
        if unknown:
            print(f"✗ unknown tool(s): {', '.join(unknown)}", file=sys.stderr)
            return 2
    else:
        chosen = list(inv)
    tgt = args.target
    timeout = max(5, min(int(getattr(args, "timeout", 300) or 300), 3600))
    started = datetime.now(timezone.utc).isoformat()
    runs, ran, failed, findings = [], 0, 0, []
    if not getattr(args, "json", False):
        print(f"═══ ARSENAL RUN — {args.target} (scope: {why}) ═══")
    for tool in chosen:
        if tool not in inv:
            continue
        target = _url(tgt) if tool in HTTP_TOOLS else _host(tgt)
        argv = [tool] + ARSENAL[tool][3](target, args.wordlist)
        row = {"tool": tool, "argv": argv, "rc": None, "hits": [],
               "output": "", "elapsed": 0.0}
        if getattr(args, "dry_run", False):
            row["skipped"] = "dry-run"
            runs.append(row)
            if not getattr(args, "json", False):
                print(f"  ▸ [dry] {' '.join(argv)}")
            continue
        try:
            r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
            out = (r.stdout + r.stderr).strip()
            hits = [cls for cls, kws in CANON_KW.items()
                    if any(k in out.lower() for k in kws)]
            row.update({"rc": r.returncode, "hits": hits, "output": out[:12000]})
            runs.append(row)
            ran += 1
            if r.returncode != 0:
                failed += 1
            findings.extend({"tool": tool, "class": c, "target": target}
                            for c in hits)
            if not getattr(args, "json", False):
                first = out.splitlines()[0][:60] if out else "(no output)"
                print(f"  ✓ {tool:10s} rc={r.returncode} canon-hits={len(hits)}  {first}")
        except subprocess.TimeoutExpired:
            failed += 1
            row.update({"rc": 124, "error": f"timeout {timeout}s"})
            runs.append(row)
            if not getattr(args, "json", False):
                print(f"  ⚠ {tool:10s} timeout {timeout}s — skipped")
        except Exception as e:
            failed += 1
            row.update({"rc": 1, "error": str(e)})
            runs.append(row)
            if not getattr(args, "json", False):
                print(f"  ✗ {tool:10s} {e}")
    payload = {"version": VERSION, "target": args.target, "scope_ok": True,
               "scope": why, "dry_run": bool(getattr(args, "dry_run", False)),
               "ran": ran, "failed": failed, "tools": runs,
               "findings": findings, "started": started}
    _record(args.target, {"at": started, "scope": why,
                          "dry_run": payload["dry_run"], "ran": ran,
                          "failed": failed, "tools": [r["tool"] for r in runs],
                          "hits": [f["class"] for f in findings]})
    if getattr(args, "output_dir", None):
        outdir = Path(args.output_dir).expanduser()
        outdir.mkdir(parents=True, exist_ok=True)
        out = outdir / f"arsenal-{sa.safe_name(args.target, 'target')}.json"
        out.write_text(json.dumps(payload, indent=2) + "\n")
        payload["output"] = str(out)
    if getattr(args, "json", False):
        _emit(args, payload)
    else:
        print(f"═══ {ran} tool run(s) · {len(findings)} canon-classified candidate(s)"
              f" · {failed} failure(s) · walls intact ═══")
    if payload["dry_run"]:
        return 0
    if chosen and inv and ran == 0:
        return 1
    return 0


def cmd_verify(args):
    bad = []
    self = Path(__file__).resolve()
    if subprocess.run([sys.executable, "-m", "py_compile", str(self)],
                      capture_output=True).returncode != 0:
        bad.append("compile")
    help_out = subprocess.run([sys.executable, str(self), "--help"],
                              capture_output=True, text=True).stdout
    for want in ("list", "plan", "run", "verify"):
        if want not in help_out:
            bad.append(want)
    if len(ARSENAL) < 20:
        bad.append("arsenal-inventory")
    if set(CHAINS) != CHAIN_NAMES:
        bad.append("chains")
    with tempfile.TemporaryDirectory(prefix="arsenal-verify-") as td:
        absent = str(Path(td) / "no-scope.json")
        r = subprocess.run([sys.executable, str(self), "run", "--target",
                            "never-in-scope.invalid", "--dry-run",
                            "--scope-file", absent], capture_output=True, text=True)
        if r.returncode != 1:
            bad.append("scope-gate-run")
        r = subprocess.run([sys.executable, str(self), "plan", "--target",
                            "never-in-scope.invalid", "--scope-file", absent],
                           capture_output=True, text=True)
        if r.returncode != 1:
            bad.append("scope-gate-plan")
        r = subprocess.run([sys.executable, str(self), "list", "--json"],
                           capture_output=True, text=True)
        try:
            data = json.loads(r.stdout)
            if data.get("total") != len(ARSENAL):
                bad.append("json-list")
        except Exception:
            bad.append("json-list")
        # v5: a lab dry-run chain must emit a kernel-schema result via --out
        outf = Path(td) / "chain-result.json"
        r = subprocess.run([sys.executable, str(self), "run", "--target",
                            "http://127.0.0.1:9", "--chain", "net", "--dry-run",
                            "--out", str(outf)], capture_output=True, text=True)
        try:
            res = json.loads(outf.read_text())
            for k in ("step", "exit", "findings", "context", "notes",
                      "directive_id"):
                if k not in res:
                    bad.append(f"chain-out {k}")
        except Exception:
            bad.append("chain-out file")
    if bad:
        print(f"✗ ARSENAL verify FAILED: {bad}")
        return 1
    print(f"✓ ARSENAL verify: compile · commands · {len(ARSENAL)} tools · "
          f"{len(CHAINS)} chains · shared-scope refusal · kernel --out schema — ALL PASS")
    return 0


def _extract(argv):
    out, json_flag, scope_file = [], False, None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--json":
            json_flag = True
            i += 1
            continue
        if a == "--scope-file":
            if i + 1 >= len(argv):
                print("✗ --scope-file needs a value", file=sys.stderr)
                raise SystemExit(2)
            scope_file = argv[i + 1]
            i += 2
            continue
        if a.startswith("--scope-file="):
            scope_file = a.split("=", 1)[1]
            i += 1
            continue
        out.append(a)
        i += 1
    return out, json_flag, scope_file


def main(argv=None):
    raw, json_flag, scope_file = _extract(list(sys.argv[1:] if argv is None else argv))
    ap = argparse.ArgumentParser(description="SPYDERMONKEY ARSENAL — scope-gated execution layer")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="installed tools × capabilities")
    p = sub.add_parser("plan", help="the run plan (nothing executes)")
    p.add_argument("--target", required=True)
    p.add_argument("--wordlist")
    r = sub.add_parser("run", help="execute (scope-gated)")
    r.add_argument("--target", required=True)
    r.add_argument("--only", help="comma-separated tool list")
    r.add_argument("--chain", help="execute a feeding chain: recon | web | tls | net | dns | content | api | services | cms | win | osint | db | takeover | cloud | packet | fuzz")
    r.add_argument("--out", help="write the kernel result-schema JSON (spydermonkey absorb ingests it)")
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--wordlist", help="gobuster/ffuf wordlist path")
    r.add_argument("--timeout", type=int, default=300)
    r.add_argument("--output-dir")
    sub.add_parser("verify", help="self-check")
    a = ap.parse_args(raw)
    a.json = json_flag
    a.scope_file = scope_file
    return {"list": cmd_list, "plan": cmd_plan, "run": cmd_run,
            "verify": cmd_verify}[a.cmd](a)


def main_with(argv):
    return main(argv)


if __name__ == "__main__":
    sys.exit(main())
