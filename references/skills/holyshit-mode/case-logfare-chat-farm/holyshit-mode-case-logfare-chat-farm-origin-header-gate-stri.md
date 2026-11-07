# Origin-header gate = string match, not security

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`/api/*` on chat host returns 403 for evil/null/absent Origin. But:
1. `Origin: https://chat.logfare.ai` from curl bypasses entirely.
2. Discriminator: `GET /api/models` → 403 with evil Origin, 200 with allowed Origin — reveals the gate is header-only.
3. `POST /api/chat` with allowed Origin → server MINTS anon `lfc_session` cookie (HttpOnly; Secure; SameSite=Lax; **Max-Age 7776000 = 90 days**) and completes the request.
4. **Existing sessions work with NO Origin header at all** — Origin required only at MINT.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
