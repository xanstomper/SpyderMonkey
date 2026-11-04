# Plane 4 — Protocol & logic — chain composition

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-4-protocol-logic.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| Vendor protocol fuzz-lite | grammar probe of a single field on owned device (one malformed packet) | crash/exception observed (documented-PoC) |
| MQTT | connect to OWN broker with empty creds; subscribe `#` | topics stream without auth |
| Modbus/DNP3 | read-only register/coil read on OWN PLC/RTU test rig | values returned without auth |
| Cloud-device trust | MITM device↔app TLS (own cert) on owned device; inspect API calls | device token/key visible in transit |
| Update channel | intercept own device's update check; serve unsigned modified image in LAB | device applies it |
| Dongle/license | USB capture of OWN dongle protocol → replay analysis | auth token replayable |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
