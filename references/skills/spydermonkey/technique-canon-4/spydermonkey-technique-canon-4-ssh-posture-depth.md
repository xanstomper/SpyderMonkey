# SSH posture depth

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Algorithm inventory (ssh-audit lane), auth-methods ordering, MaxAuthTentрад behavior reflected in error cadence. Decisive test: ssh-audit output + banner parse — the posture table is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
