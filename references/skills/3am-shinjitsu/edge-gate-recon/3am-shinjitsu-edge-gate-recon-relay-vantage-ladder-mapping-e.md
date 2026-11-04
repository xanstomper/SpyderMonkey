# Relay-vantage ladder (mapping eyes when every direct vantage is denied)

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
