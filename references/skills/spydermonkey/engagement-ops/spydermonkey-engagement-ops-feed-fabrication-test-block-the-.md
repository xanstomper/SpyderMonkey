# Feed-fabrication test: block the data channels, then re-render

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

To decide whether a "live" feed (multipliers, players, rounds) is client-fabricated or
server-sourced: intercept and abort every XHR/fetch/websocket first, re-render the page,
and read the FEED REGION. A feed that still populates with all data channels blocked is
fabricated; a page that shows only "Connecting…/Stay tuned" needs the socket —
server-authoritative. Trap: preset buttons render as multiplier-looking labels (`2×`,
`1.71×` preset chips) in body text — extract the round-history/feed region, never judge
from full-body text. And `?mode=demo`/`?demo=1` legitimately renders simulated players
(robotNNNNN) — an official demo mode is not fabrication; check what the OFFICIAL UI shows
without the demo param.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
