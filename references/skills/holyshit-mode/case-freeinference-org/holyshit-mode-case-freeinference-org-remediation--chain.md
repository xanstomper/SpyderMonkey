# Remediation — chain composition

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-remediation.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Rate-limit** `/api/export` and `/api/dashboard?refresh=1` — lockout after 5 failed password attempts
2. **Replace shared secret** `madsys` with per-user tokens or session-based auth
3. **Add MFA** for refresh/export operations
4. **Restrict unauthenticated `/api/dashboard`** (returns stale cache anyway — gate it)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
