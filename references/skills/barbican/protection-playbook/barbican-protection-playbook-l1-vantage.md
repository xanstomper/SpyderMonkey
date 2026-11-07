# L1 — VANTAGE

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Audit | Synthesis |
|---|---|
| default route (residential iface = CRITICAL) | posture declares vm/vps/vpn/lab as THE sanctioned exit |
| proxy/VPN env + resolver config | engagement shells verify the route before firing |
| target-side logs will show the vantage — assume it's recorded forever | never mix personal browsing with engagement vantage |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
