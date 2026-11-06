# Webhook SSRF and replay — chain composition

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-webhook-ssrf-and-replay.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

User-registered webhooks pointing at internal ranges (SSRF class) and unsigned webhook payloads (replay/forge class). Decisive test: webhook delivered to YOUR listener (SSRF proof), or a replayed payload accepted twice (replay proof).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
