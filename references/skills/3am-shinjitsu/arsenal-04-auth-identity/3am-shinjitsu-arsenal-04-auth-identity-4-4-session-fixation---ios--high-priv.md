# 4.4 Session fixation / cookie hygiene (score 65) — ios / high-priv

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-4-session-fixation-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- URL-param session ids (`?sid=`) → set, login, check retention. No rotation on privilege
  change. Read raw `Set-Cookie` on EVERY authed endpoint: HttpOnly/Secure/SameSite/Path scope.
- Cookie-scoped OAuth state yardstick: `HttpOnly; Secure; SameSite=Lax; Path=/v1/auth/discord;
  Max-Age=600` + server-issued HS256 JWT, forged → 400.

## Probe adjustment (ios × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
