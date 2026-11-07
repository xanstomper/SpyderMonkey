# 4.4 Session fixation / cookie hygiene (score 65) — gateway / root

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-4-session-fixation-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **gateway** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- URL-param session ids (`?sid=`) → set, login, check retention. No rotation on privilege
  change. Read raw `Set-Cookie` on EVERY authed endpoint: HttpOnly/Secure/SameSite/Path scope.
- Cookie-scoped OAuth state yardstick: `HttpOnly; Secure; SameSite=Lax; Path=/v1/auth/discord;
  Max-Age=600` + server-issued HS256 JWT, forged → 400.

## Probe adjustment (gateway × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
