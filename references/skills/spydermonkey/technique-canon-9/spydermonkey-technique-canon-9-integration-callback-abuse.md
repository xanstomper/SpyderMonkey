# Integration callback abuse

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Platform callbacks (oauth/intercom-class) accepting forged payloads — signature posture detection. Decisive test: the callback's signature-verification refusal/acceptance behavior on YOUR test payload = the row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
