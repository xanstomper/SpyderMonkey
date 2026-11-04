# Privilege Escalation Abuse Elevation Control (T1548)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- class: sudo/sudoers misconfiguration abuse
- probe: `sudo -n -l` inventory — what can THIS principal do
- wall: read-only; rung climbing stops at the exposure statement (kaisha)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
