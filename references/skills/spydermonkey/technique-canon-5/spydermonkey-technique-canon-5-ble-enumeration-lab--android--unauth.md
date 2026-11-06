# BLE enumeration (lab) — android / unauth

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-ble-enumeration-lab.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **android** · auth **unauth** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

GATT service/characteristic inventory on lab devices — write-characteristic tests NEVER fired on third-party devices. Decisive test: your lab device's characteristic map — unauth-read characteristics = the class.

## Probe adjustment (android × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
