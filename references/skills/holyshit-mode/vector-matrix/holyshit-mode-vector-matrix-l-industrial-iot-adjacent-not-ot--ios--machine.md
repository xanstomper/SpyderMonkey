# L. INDUSTRIAL / IOT-ADJACENT (NOT OT/ICS) — ios / machine

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-l-industrial-iot-adjacent-not-ot.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ios** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- MQTT brokers: anonymous auth, topic wildcard abuse, retained-message poisoning
- CoAP devices: unauthenticated resource discovery, firmware extraction via /firmware
- Zigbee/Z-Wave: pairing-mode weaknesses, network-key extraction from operator devices
- Building management: BACnet/IP exposure on IT networks (flag, don't touch OT)
- Fleet management: GPS spoofing validation, OTA update signing on operator vehicles
- Smart-city dashboards: non-safety-critical API exposure, data poisoning validation

## Probe adjustment (ios × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
