# Integration callback abuse

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Platform callbacks (oauth/intercom-class) accepting forged payloads — signature posture detection. Decisive test: the callback's signature-verification refusal/acceptance behavior on YOUR test payload = the row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
