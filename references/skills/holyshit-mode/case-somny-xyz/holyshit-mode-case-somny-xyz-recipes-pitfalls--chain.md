# Recipes / pitfalls — chain composition

- source canon: `holyshit-mode/case-somny-xyz.md`
- base technique: `holyshit-mode-case-somny-xyz-recipes-pitfalls.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Key-masking pattern:** key-create endpoints return masked keys; a `reveal`/`secret` sub-endpoint is the real primitive (same as gratisfy's `platform-keys/{id}/secret`). IDOR on reveal with foreign UUID → 400 body-validation (auth before existence).
- **mail.tm flow:** GET `/domains` (find active domain) → POST `/accounts` → POST `/token` → poll `/messages` (5s) → GET `/messages/{id}` for full body → regex `token=([a-zA-Z0-9._-]+)&callbackURL`. Consume ONCE via GET with no-redirect opener; capture 302 Location.
- **Verification token may be JWT-style (167 chars), not hex** — regex must allow dots: `[a-zA-Z0-9._-]+`.
- **Terminal `&` guard:** shell loops with `&` backgrounding rejected by terminal tool — serialize.
- **delete-user 404:** better-auth endpoint present in client bundle but plugin not enabled server-side — bundle lists endpoints the server doesn't have; always live-probe.
- Hygiene: revoked probe key via `DELETE /api/keys/{id}` (worked).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
