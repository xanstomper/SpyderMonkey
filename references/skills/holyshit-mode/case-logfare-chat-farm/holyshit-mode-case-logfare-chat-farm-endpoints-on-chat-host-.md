# Endpoints on chat host (all Origin-gated, all real JSON)

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`/api/health {status,version}` · `/api/models` (full tier/visibility/premium intel; leaks hidden default `claude-sonnet-4.5` not in public list) · `/api/chat` · `/api/conversations` (GET list / PATCH / DELETE per-id) · `/api/settings` (GET/PUT) · `/api/consent` (GET: `{tier:"anonymous",can_use_premium:false,logged_in:false}`).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
