# MASTG Sensitive Data in Local Storage (MASTG-STORAGE-02)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-04

## The technique

- class: shared prefs / sqlite / files holding credentials unencrypted
- probe: read the app sandbox on the lab device; diff the storage before/after a login
- wall: lab device, lab app; the finding is the storage class, not the data

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
