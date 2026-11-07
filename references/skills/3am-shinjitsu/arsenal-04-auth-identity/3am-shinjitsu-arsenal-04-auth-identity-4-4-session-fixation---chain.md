# 4.4 Session fixation / cookie hygiene (score 65) — chain composition

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-4-session-fixation-.md`
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

- URL-param session ids (`?sid=`) → set, login, check retention. No rotation on privilege
  change. Read raw `Set-Cookie` on EVERY authed endpoint: HttpOnly/Secure/SameSite/Path scope.
- Cookie-scoped OAuth state yardstick: `HttpOnly; Secure; SameSite=Lax; Path=/v1/auth/discord;
  Max-Age=600` + server-issued HS256 JWT, forged → 400.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
