# DNS-cookie and anycast classes

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-SESS-03** · **CWE-1004** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

EDNS-cookie support and anycast divergence affecting enumeration honesty. Decisive test: cookie echo behavior = the measurement note.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
