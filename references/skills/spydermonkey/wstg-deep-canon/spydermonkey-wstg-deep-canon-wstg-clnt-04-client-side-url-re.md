# WSTG-CLNT-04 Client-side URL Redirect

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: fragment/JS-driven redirects attacker-controllable
- probe: the REDIRECT battery + location header differential
- wall: benign evil.example marker only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
