# 4.4 Session fixation / cookie hygiene (score 65)

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- URL-param session ids (`?sid=`) → set, login, check retention. No rotation on privilege
  change. Read raw `Set-Cookie` on EVERY authed endpoint: HttpOnly/Secure/SameSite/Path scope.
- Cookie-scoped OAuth state yardstick: `HttpOnly; Secure; SameSite=Lax; Path=/v1/auth/discord;
  Max-Age=600` + server-issued HS256 JWT, forged → 400.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
