# CONFIRMED HOLYSHIT #1 — unauth realtime GPS surveillance (score 90) — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-confirmed-holyshit-1.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Streaming kind-1 fixes at ~300ms + `tracked_devices` JSON = meter-precision live tracking of real people with zero credentials. Verified: Nate tracked-device at **3.8m accuracy + live heading (~146°, walking S)** updating ~1/s; contestant slots 21/27/67 tracked continuously; tracker also correlates staff↔contestant proximity (slot 27 was ~20m from Nate's device). Invisible-status contestants still appear in binary fixes (invisibility hides on map render, not in stream).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
