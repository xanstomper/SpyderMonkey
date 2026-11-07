# Plane 3 — Radio & wireless

- source canon: `kairo/offensive-hardware-batteries.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
