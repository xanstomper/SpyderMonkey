# 3.8 Unauth token-mint (score 80) — chain composition

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-8-unauth-token-mint-score-80.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- PATTERN: `POST /auth/token?scope=X` mints RS256 JWTs unauth, signs ANY client scope.
- Map CONSUMERS first (bundle vocabulary: sub/admin/mod/internal/system + websocket identity);
  any-scope mint + proven privileged consumer = chain; inert HTTP plane + server-side room
  enforcement = ~45. Test EVERY implied sub value incl. a second mint on the OAuth-authority
  host (bare `/token` may mint `sub=websocket` with a GLOBAL constant id).
- Uniform 403 in bearer AND query delivery = mint inert on HTTP plane; state both planes.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
