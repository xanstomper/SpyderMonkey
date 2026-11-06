# L. INDUSTRIAL / IOT-ADJACENT (NOT OT/ICS) — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-l-industrial-iot-adjacent-not-ot.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- MQTT brokers: anonymous auth, topic wildcard abuse, retained-message poisoning
- CoAP devices: unauthenticated resource discovery, firmware extraction via /firmware
- Zigbee/Z-Wave: pairing-mode weaknesses, network-key extraction from operator devices
- Building management: BACnet/IP exposure on IT networks (flag, don't touch OT)
- Fleet management: GPS spoofing validation, OTA update signing on operator vehicles
- Smart-city dashboards: non-safety-critical API exposure, data poisoning validation

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
