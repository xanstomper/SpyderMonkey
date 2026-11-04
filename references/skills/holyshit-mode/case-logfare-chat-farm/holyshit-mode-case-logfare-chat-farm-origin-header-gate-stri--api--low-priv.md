# Origin-header gate = string match, not security — api / low-priv

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-origin-header-gate-stri.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`/api/*` on chat host returns 403 for evil/null/absent Origin. But:
1. `Origin: https://chat.logfare.ai` from curl bypasses entirely.
2. Discriminator: `GET /api/models` → 403 with evil Origin, 200 with allowed Origin — reveals the gate is header-only.
3. `POST /api/chat` with allowed Origin → server MINTS anon `lfc_session` cookie (HttpOnly; Secure; SameSite=Lax; **Max-Age 7776000 = 90 days**) and completes the request.
4. **Existing sessions work with NO Origin header at all** — Origin required only at MINT.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
