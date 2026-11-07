# New hardening since baseline (negatives) — chain composition

- source canon: `holyshit-mode/case-logfare-ai-retest2.md`
- base technique: `holyshit-mode-case-logfare-ai-retest2-new-hardening-since-ba.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Signup Discord-membership gate**: `POST /v1/auth/register` → 403 "Verify that you are in
  the Logfare Discord server before creating an account." Homepage marketing ("No email, no
  verification, no bullshit") is FALSE — actual gate is Discord membership. `/migrate`
  flow exists for existing accounts.
- **Discord OAuth state binding**: forged state → 400. State cookie = server-issued HS256
  JWT, HttpOnly/Secure/SameSite=Lax/path-scoped/10-min. Textbook.
- **redirect_uri NOT client-controllable**: `/v1/auth/discord/start?redirect_uri=https://evil.com/cb`
  ignored the param, hardcoded `redirect_uri=https://logfare.ai/v1/auth/discord/callback`
  verbatim in the 302 Location (client_id 1553307977572941916, scope=identify).
- **Login rate limiter works now** (baseline said broken): 12-burst → 5×401 then 429s.
- **OAuth/SSO/device no oracle**: bogus client_id on `GET /oauth/authorize` renders generic
  "Connect an app / Enter the code" page (200, no enumeration); `POST /oauth/authorize` 403;
  `POST /v1/integrations/oauth/device_authorization` + `/v1/sso/token` uniform 401.
- `/connections` → 302 `/login?next=%2Fconnections` (proper login redirect).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
