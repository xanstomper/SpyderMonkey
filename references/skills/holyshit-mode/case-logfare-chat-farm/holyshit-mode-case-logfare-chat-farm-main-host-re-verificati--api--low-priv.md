# Main host re-verification — api / low-priv

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-main-host-re-verificati.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **CORS reflection re-verified** (score 72, downgraded from 9.1): `access-control-allow-origin: https://evil.com` + `access-control-allow-credentials: true` on ALL endpoints incl. state-changers (`/v1/auth/regenerate-key`, `/v1/me/delete`). BUT auth moved to cookies with `SameSite=Lax; HttpOnly; Secure` — cross-site POSTs don't carry the session. Misconfig stands, exploitability dropped.
- **New hardening since baseline:** Discord-membership signup gate (register → 403 "Verify that you are in the Logfare Discord server"); forged OAuth state → 400 (state = server-issued HS256 JWT cookie, path-scoped, 10-min); `redirect_uri` on `/v1/auth/discord/start` NOT client-controllable; login rate limiter works (5x401 then 429).
- **SSR pivot:** site dropped its SPA — no bundle to hash. `/openapi.json` (200, 60+ routes, no security schemes) was the free recon map. Always re-run openapi/docs discovery on re-engage; architecture changes invalidate the bundle-hash baseline ritual.
- OAuth/SSO/device-flow surfaces: bogus client_id renders generic page (no enumeration oracle), `POST /oauth/authorize` → 302 to `/login?next=...` (session required), device flow + `/v1/sso/token` uniform 401.

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
