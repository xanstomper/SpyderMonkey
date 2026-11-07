# Plane 4 — Protocol & logic — serverless / service

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-4-protocol-logic.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **serverless** · auth **service** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: function identity + env surface — read-only enumeration, crowns as the control-plane class
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Vendor protocol fuzz-lite | grammar probe of a single field on owned device (one malformed packet) | crash/exception observed (documented-PoC) |
| MQTT | connect to OWN broker with empty creds; subscribe `#` | topics stream without auth |
| Modbus/DNP3 | read-only register/coil read on OWN PLC/RTU test rig | values returned without auth |
| Cloud-device trust | MITM device↔app TLS (own cert) on owned device; inspect API calls | device token/key visible in transit |
| Update channel | intercept own device's update check; serve unsigned modified image in LAB | device applies it |
| Dongle/license | USB capture of OWN dongle protocol → replay analysis | auth token replayable |

## Probe adjustment (serverless × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
