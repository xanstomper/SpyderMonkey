# H. PROTOCOL / WIRELESS (operator hardware)

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- WiFi: PMKID, handshake capture+crack, rogue AP, WPS
- BLE: GATT enumeration, no-pairing writes
- SDR: replay, rolling-code
- RFID/NFC: MIFARE nested, UID clone

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
