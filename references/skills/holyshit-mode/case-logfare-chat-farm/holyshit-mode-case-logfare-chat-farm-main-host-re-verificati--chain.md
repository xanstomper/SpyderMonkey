# Main host re-verification — chain composition

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-main-host-re-verificati.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **CORS reflection re-verified** (score 72, downgraded from 9.1): `access-control-allow-origin: https://evil.com` + `access-control-allow-credentials: true` on ALL endpoints incl. state-changers (`/v1/auth/regenerate-key`, `/v1/me/delete`). BUT auth moved to cookies with `SameSite=Lax; HttpOnly; Secure` — cross-site POSTs don't carry the session. Misconfig stands, exploitability dropped.
- **New hardening since baseline:** Discord-membership signup gate (register → 403 "Verify that you are in the Logfare Discord server"); forged OAuth state → 400 (state = server-issued HS256 JWT cookie, path-scoped, 10-min); `redirect_uri` on `/v1/auth/discord/start` NOT client-controllable; login rate limiter works (5x401 then 429).
- **SSR pivot:** site dropped its SPA — no bundle to hash. `/openapi.json` (200, 60+ routes, no security schemes) was the free recon map. Always re-run openapi/docs discovery on re-engage; architecture changes invalidate the bundle-hash baseline ritual.
- OAuth/SSO/device-flow surfaces: bogus client_id renders generic page (no enumeration oracle), `POST /oauth/authorize` → 302 to `/login?next=...` (session required), device flow + `/v1/sso/token` uniform 401.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
