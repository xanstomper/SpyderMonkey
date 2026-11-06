# Origin-header gate = string match, not security — mobile-api / federated

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-origin-header-gate-stri.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`/api/*` on chat host returns 403 for evil/null/absent Origin. But:
1. `Origin: https://chat.logfare.ai` from curl bypasses entirely.
2. Discriminator: `GET /api/models` → 403 with evil Origin, 200 with allowed Origin — reveals the gate is header-only.
3. `POST /api/chat` with allowed Origin → server MINTS anon `lfc_session` cookie (HttpOnly; Secure; SameSite=Lax; **Max-Age 7776000 = 90 days**) and completes the request.
4. **Existing sessions work with NO Origin header at all** — Origin required only at MINT.

## Probe adjustment (mobile-api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
