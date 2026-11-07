# Origin-header gate = string match, not security — api / machine

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-origin-header-gate-stri.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **api** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`/api/*` on chat host returns 403 for evil/null/absent Origin. But:
1. `Origin: https://chat.logfare.ai` from curl bypasses entirely.
2. Discriminator: `GET /api/models` → 403 with evil Origin, 200 with allowed Origin — reveals the gate is header-only.
3. `POST /api/chat` with allowed Origin → server MINTS anon `lfc_session` cookie (HttpOnly; Secure; SameSite=Lax; **Max-Age 7776000 = 90 days**) and completes the request.
4. **Existing sessions work with NO Origin header at all** — Origin required only at MINT.

## Probe adjustment (api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
