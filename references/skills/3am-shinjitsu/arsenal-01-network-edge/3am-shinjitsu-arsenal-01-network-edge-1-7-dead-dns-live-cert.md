# 1.7 Dead-DNS-live-cert hosts (score 75)

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- DECISIVE: passive-DNS dump (hackertarget hostsearch) ∩ CT-log names ∖ resolving names.
- CONFIRMED WHEN: `crt.sh` shows cert for a name with no A/AAAA on two public resolvers —
  "internal control panel" signature; try `https://<name>` via origin IP + Host header.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
