# Plane 4 — Protocol & logic

- source canon: `kairo/offensive-hardware-batteries.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Vendor protocol fuzz-lite | grammar probe of a single field on owned device (one malformed packet) | crash/exception observed (documented-PoC) |
| MQTT | connect to OWN broker with empty creds; subscribe `#` | topics stream without auth |
| Modbus/DNP3 | read-only register/coil read on OWN PLC/RTU test rig | values returned without auth |
| Cloud-device trust | MITM device↔app TLS (own cert) on owned device; inspect API calls | device token/key visible in transit |
| Update channel | intercept own device's update check; serve unsigned modified image in LAB | device applies it |
| Dongle/license | USB capture of OWN dongle protocol → replay analysis | auth token replayable |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
