# First-party OIDC (separate from GoTrue external OAuth) — chain composition

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-first-party-oid.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Platforms that offer "Login with X" via their own OIDC provider (`/oauth/authorize` + `/api/oauth/token`) are a SEPARATE auth surface from the Supabase GoTrue external OAuth (Discord/Google). On gratisfy.xyz the first-party flow used:

- PKCE S256 with `crypto.getRandomValues(48)` verifier — proper, not bruteable
- `code_challenge_method: S256`, nonce, sessionStorage state binding
- Server rejects garbage codes with uniform `invalid_grant`

Treat first-party OIDC as hardened unless the verifier is `Math.random()`-based or the challenge method is `plain`. Mine the SPA bundle for the PKCE generation function to confirm — `grep -oE 'crypto\.getRandomValues|Math\.random' firstPartyOidc*.js`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
