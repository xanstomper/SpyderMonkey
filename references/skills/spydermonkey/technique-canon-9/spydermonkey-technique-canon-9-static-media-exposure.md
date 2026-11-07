# Static/media exposure

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `gobuster`, `ffuf`, `dirsearch`, `dirb`, `feroxbuster`, `wfuzz`, `dirhunt`
- chains: `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

MEDIA_ROOT serving uploads unauth + directory posture. Decisive test: upload-path fetch class = the inventory.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
