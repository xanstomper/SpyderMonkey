# Plane 3 — Radio & wireless — iot-edge / root

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-3-radio-wireless.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **iot-edge** · auth **root** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

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

## Probe adjustment (iot-edge × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
