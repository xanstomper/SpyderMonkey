# Persistence Boot or Logon Autostart (T1547)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

- class: run-key/systemd/launchd autostart for durability
- probe: read-only enumeration of autostart locations on in-scope hosts
- wall: read-only; the finding is the exposure, not a planted hook

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
