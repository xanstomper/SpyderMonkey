# Ghost-route discrimination

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

404s returning `application/json` = real routing layer (not SPA fallback). Only `text/html`
404/200s are ghosts. Check `/openapi.json`, `/docs`, `/api/docs` — but expect them genuinely absent on hardened non-FastAPI targets.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
