# CONFIRMED HOLYSHIT #1 — unauth realtime GPS surveillance (score 90)

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- bindings: **WSTG-BUSL-01** · **CWE-1336** · **ATT&CK T1565**
- generated: 2026-11-04

## The technique

Streaming kind-1 fixes at ~300ms + `tracked_devices` JSON = meter-precision live tracking of real people with zero credentials. Verified: Nate tracked-device at **3.8m accuracy + live heading (~146°, walking S)** updating ~1/s; contestant slots 21/27/67 tracked continuously; tracker also correlates staff↔contestant proximity (slot 27 was ~20m from Nate's device). Invisible-status contestants still appear in binary fixes (invisibility hides on map render, not in stream).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
