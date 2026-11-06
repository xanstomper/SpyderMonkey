# New hardening since baseline (negatives) — mobile-api / high-priv

- source canon: `holyshit-mode/case-logfare-ai-retest2.md`
- base technique: `holyshit-mode-case-logfare-ai-retest2-new-hardening-since-ba.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mobile-api** · auth **high-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

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

## Probe adjustment (mobile-api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
