# Relay-vantage ladder (mapping eyes when every direct vantage is denied) — chain composition

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-relay-vantage-ladder-mapping-e.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Ladder: keyless allorigins `/raw?url=` (HTML passes, API hosts often 52x or the block
  page) → jina reader with `X-Return-Format: html` (raw HTML, keeps script tags) →
  keyless Firecrawl (HTML fine; RAW-JSON endpoints crash the extractor — "all engines
  failed" is an extractor limit, not a 403).
- Relays are GET-only: any POST-dependent decisive test (socket.io connect packets, auth
  flows) must run from a host the box reaches directly (via an exempt path class), not
  through a relay.
- Relays map and observe only — inside a jurisdiction deny they are the mapping channel,
  never a bypass channel; decisive access tests still need a sanctioned vantage.
- Verify every relay result with the body-size discriminator above — a relay "success"
  can be the target's block page relayed back verbatim.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
