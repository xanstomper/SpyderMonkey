# L. INDUSTRIAL / IOT-ADJACENT (NOT OT/ICS)

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- MQTT brokers: anonymous auth, topic wildcard abuse, retained-message poisoning
- CoAP devices: unauthenticated resource discovery, firmware extraction via /firmware
- Zigbee/Z-Wave: pairing-mode weaknesses, network-key extraction from operator devices
- Building management: BACnet/IP exposure on IT networks (flag, don't touch OT)
- Fleet management: GPS spoofing validation, OTA update signing on operator vehicles
- Smart-city dashboards: non-safety-critical API exposure, data poisoning validation

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
