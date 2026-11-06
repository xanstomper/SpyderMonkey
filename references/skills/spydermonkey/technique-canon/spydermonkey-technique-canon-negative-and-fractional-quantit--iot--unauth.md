# Negative and fractional quantity — iot / unauth

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-negative-and-fractional-quantit.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **iot** · auth **unauth** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Quantity=-1 or 0.5 submitted to a cart/checkout inverts the math server-side. Decisive test: quantity=-1 on the cheapest line, read the recalculated total — negative TOTAL is the crown; rejected = bank the negative.

## Probe adjustment (iot × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
