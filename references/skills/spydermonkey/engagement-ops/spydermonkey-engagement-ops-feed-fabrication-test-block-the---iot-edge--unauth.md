# Feed-fabrication test: block the data channels, then re-render — iot-edge / unauth

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-feed-fabrication-test-block-the-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot-edge** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (iot-edge × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
