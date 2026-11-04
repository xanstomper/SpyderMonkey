# HDRADIO — ble, rfid, nfc, radio, sdr, zigbee — ios / unauth

- source canon: `kairo/technique-classes.md`
- base technique: `kairo-technique-classes-hdradio-ble-rfid-nfc-radio-sdr-zigbe.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **ios** · auth **unauth** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- HDRADIO
- ble, rfid, nfc, radio, sdr, zigbee
- 18/M
- OTHER

## Probe adjustment (ios × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
