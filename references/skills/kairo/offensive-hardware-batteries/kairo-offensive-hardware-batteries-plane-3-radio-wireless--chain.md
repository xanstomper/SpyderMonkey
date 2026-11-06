# Plane 3 — Radio & wireless — chain composition

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-3-radio-wireless.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| WiFi WPS | `reaver`/`wash` on OWN AP (lab) — WPS enabled + no lockout | WPS active, no rate-limit |
| WiFi handshake | `airmon-ng` own AP capture → PMKID check (owned infra) | PMKID present = offline attack feasible |
| BLE GATT | `bluetoothctl`/`gatttool` scan + services on OWN device | writable characteristic without auth |
| BLE pairing | legacy pairing (no MITM) on owned peripheral | Just-Works pairing accepted |
| RFID/NFC | `libnfc`/Proxmark read of OWN badge; identify tag type + locks | tag readable / rolling code pattern observed |
| ISM/SDR | HackRF capture of own remote's 433/868MHz frames → decode/replay feasibility | frame structure + fixed code (or rolling with sync) |
| Zigbee/Z-Wave | SDR/Conbee scan of own network keys exchange | network key captured on own coordinator |

RF rule: transmit ONLY against operator-owned hardware in the operator's own lab;
document frequency/power before any tx.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
