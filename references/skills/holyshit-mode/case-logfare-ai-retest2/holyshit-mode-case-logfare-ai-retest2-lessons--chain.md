# Lessons — chain composition

- source canon: `holyshit-mode/case-logfare-ai-retest2.md`
- base technique: `holyshit-mode-case-logfare-ai-retest2-lessons.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. CORS finding severity is a function of auth model + cookie SameSite, not the reflection
   alone. Read raw Set-Cookie flags before rating; re-derive severity when auth model churns.
2. Targets get rebuilt between sessions (SPA → server-rendered). Diff the openapi route list
   across re-engagements like bundle hashes; don't grep a stale bundle.
3. Marketing copy about signup friction is not evidence — probe the register endpoint.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
