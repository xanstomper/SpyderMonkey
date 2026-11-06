# Negatives (held) — chain composition

- source canon: `holyshit-mode/case-somny-xyz.md`
- base technique: `holyshit-mode-case-somny-xyz-negatives-held.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- CORS: no ACAO reflection; CSP `connect-src 'self'`; cookies Lax.
- Paid-model gate: 403 `model_access` on claude/*; 9-variant bypass matrix (case/space/`:latest`/dot/#/array-type) all 404/400. Same gate on messages/responses/batch.
- PTOK constant → stateless, no shared buffer.
- Stripe checkout honors only server-side plan codes → legit `cs_live` session.
- No admin/internal/webhook surface (uniform 404 JSON). `/api/status` leaks only `{service, inference, billing, billingManagement, signup, google, mode}` — gate map enumerable unauth.
- `verify-email?callbackURL=` origin-locked (evil.com → 403). Userinfo-confusion `https://evil.com@somny.xyz` → 302 but host resolves to somny.xyz (browser-safe, low).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
