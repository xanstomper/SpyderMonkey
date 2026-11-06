# Feed-fabrication test: block the data channels, then re-render — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-feed-fabrication-test-block-the-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

To decide whether a "live" feed (multipliers, players, rounds) is client-fabricated or
server-sourced: intercept and abort every XHR/fetch/websocket first, re-render the page,
and read the FEED REGION. A feed that still populates with all data channels blocked is
fabricated; a page that shows only "Connecting…/Stay tuned" needs the socket —
server-authoritative. Trap: preset buttons render as multiplier-looking labels (`2×`,
`1.71×` preset chips) in body text — extract the round-history/feed region, never judge
from full-body text. And `?mode=demo`/`?demo=1` legitimately renders simulated players
(robotNNNNN) — an official demo mode is not fabrication; check what the OFFICIAL UI shows
without the demo param.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
