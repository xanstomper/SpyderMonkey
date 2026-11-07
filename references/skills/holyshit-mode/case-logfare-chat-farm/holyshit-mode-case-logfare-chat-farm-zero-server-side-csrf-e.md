# Zero server-side CSRF enforcement (score 45, hypothesis for browser-exploit)

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`PUT /api/settings` returns 200 with `Origin: evil.com` AND no Origin. Only SameSite=Lax blocks browser exploitation — one flag from drive-by config hijack. Server does no verification.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
