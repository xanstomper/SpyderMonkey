# Relay-vantage ladder (mapping eyes when every direct vantage is denied) — api / unauth

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-relay-vantage-ladder-mapping-e.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **unauth** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
