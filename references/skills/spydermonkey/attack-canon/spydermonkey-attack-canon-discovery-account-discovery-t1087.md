# Discovery Account Discovery (T1087)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-ATHN-07** · **CWE-640** · **ATT&CK T1078**
- generated: 2026-11-04

## The technique

- class: valid account enumeration
- probe: response-differential username classes (login vs reset timing/length)
- wall: length/timing DIFFERENTIALS only — no successful logins attempted

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
