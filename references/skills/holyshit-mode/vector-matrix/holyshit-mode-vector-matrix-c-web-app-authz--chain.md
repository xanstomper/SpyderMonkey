# C. WEB APP — AUTHZ — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-c-web-app-authz.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- IDOR/BOLA: every GET/PUT/DELETE with enumerateable IDs, cross-account only
- BFLA: privileged API actions replayed as low-priv test user
- Mass assignment: is_admin/role/verified/credits/price/owner_id injected on writes
- Hidden endpoints: ghost routes (playbook §3), debug endpoints (/debug, /actuator, /swagger, /api-docs, /.env)
- Client-only gates: frontend-hidden routes still callable (verify server-side 405/401)
- JWT: alg=none, kid injection, weak HMAC secret (hashcat), no audience check, key-confusion RS256→HS256
- Session: fixation via URL params, no rotation on privilege change, non-HttpOnly, missing SameSite
- OAuth: missing/predictable state, redirect_uri bypass (open-redirect chains), token-in-fragment, PKCE downgrade
- Password reset: host-header poisoning, token-in-URL leakage (referrer), predictability, no single-use
- 2FA: response-status trust, brute-forceable codes, bypass via backup-code enumeration, remember-token reuse

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
