# SvelteKit chunk walk (client-API call-site discovery)

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`index.html` → `entry/start.<hash>.js` → `chunks/<hash>.js` → `nodes/<n>.<hash>.js`. The 358KB **node** chunk (not the tiny entry/app chunks) held ALL fetch call sites — including the correct `/api/conversations/${id}/messages` subresource that guessed paths missed (all wrong guesses 404'd). Don't guess subresource paths; read the framework's lazy-loaded page chunks.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
