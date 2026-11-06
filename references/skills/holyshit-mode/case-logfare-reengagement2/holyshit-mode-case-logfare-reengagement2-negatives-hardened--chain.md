# Negatives (hardened) — chain composition

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-negatives-hardened.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Discord OAuth: forged state → 400; state cookie HttpOnly/Secure/Lax/path-scoped JWT;
`redirect_uri` on `/v1/auth/discord/start` NOT client-controllable. Login rate limit works
(5×401 → 429). OAuth/device/SSO client probes give no enumeration oracle. `/api/conversations`
and `/api/settings` 200 on anon sessions are per-session state, not leaks.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
