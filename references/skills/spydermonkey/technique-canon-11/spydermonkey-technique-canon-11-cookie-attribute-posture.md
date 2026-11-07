# Cookie-attribute posture

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-SESS-03** · **CWE-1004** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Secure/HttpOnly/SameSite/__Host- absence per cookie. Decisive test: Set-Cookie audit = the matrix.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
