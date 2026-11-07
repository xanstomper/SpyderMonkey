# Webhook SSRF and replay — chain composition

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-webhook-ssrf-and-replay.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

User-registered webhooks pointing at internal ranges (SSRF class) and unsigned webhook payloads (replay/forge class). Decisive test: webhook delivered to YOUR listener (SSRF proof), or a replayed payload accepted twice (replay proof).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
