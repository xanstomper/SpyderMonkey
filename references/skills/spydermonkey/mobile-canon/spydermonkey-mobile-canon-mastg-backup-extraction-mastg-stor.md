# MASTG Backup Extraction (MASTG-STORAGE-06)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: adb backup / iOS backup exposing app data
- probe: lab backup of the lab app; inventory the extracted class
- wall: lab only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
