# Modbus/S7/BACnet exposure classes

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Protocol banners reachable unauth (502/102/47808) — the BANNER is the inventory finding; control writes are the absolute wall (never sent). Decisive test: read-only identity/banners on in-scope industrial tiers.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
