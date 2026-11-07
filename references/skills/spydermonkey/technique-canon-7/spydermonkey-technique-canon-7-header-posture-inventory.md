# Header posture inventory

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

CSP/HSTS/SRI/X-Frame/X-Content-Type on every in-scope tier — the posture matrix is a generalizing recon row (one row, not hundreds — report discipline).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
