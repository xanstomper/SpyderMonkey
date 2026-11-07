# MASTG Sensitive Data in Local Storage (MASTG-STORAGE-02)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: shared prefs / sqlite / files holding credentials unencrypted
- probe: read the app sandbox on the lab device; diff the storage before/after a login
- wall: lab device, lab app; the finding is the storage class, not the data

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
