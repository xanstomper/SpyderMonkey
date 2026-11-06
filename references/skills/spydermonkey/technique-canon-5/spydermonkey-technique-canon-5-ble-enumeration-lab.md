# BLE enumeration (lab)

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

GATT service/characteristic inventory on lab devices — write-characteristic tests NEVER fired on third-party devices. Decisive test: your lab device's characteristic map — unauth-read characteristics = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
