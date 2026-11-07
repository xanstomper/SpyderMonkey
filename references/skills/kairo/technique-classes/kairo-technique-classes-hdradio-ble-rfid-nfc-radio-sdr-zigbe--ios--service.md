# HDRADIO — ble, rfid, nfc, radio, sdr, zigbee — ios / service

- source canon: `kairo/technique-classes.md`
- base technique: `kairo-technique-classes-hdradio-ble-rfid-nfc-radio-sdr-zigbe.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **ios** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- HDRADIO
- ble, rfid, nfc, radio, sdr, zigbee
- 18/M
- OTHER

## Probe adjustment (ios × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
