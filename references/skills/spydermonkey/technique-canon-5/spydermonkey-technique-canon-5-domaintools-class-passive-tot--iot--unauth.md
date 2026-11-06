# Domaintools-class passive-total and sibling-brand mapping — iot / unauth

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-domaintools-class-passive-tot.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **iot** · auth **unauth** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Registration-tree expansion (registrant org → sibling brands) feeding the shared-backend hypothesis (the error-taxonomy canon-I test confirms). Decisive test: whois org field + the sibling's confirmed shared taxonomy.

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
