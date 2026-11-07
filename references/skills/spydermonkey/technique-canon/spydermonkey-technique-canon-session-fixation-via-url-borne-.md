# Session fixation via URL-borne tokens

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

A session id accepted from the URL (`?sid=`) and re-issued as a cookie lets an attacker pre-set the victim's session. Decisive test: set sid=attacker-value in the URL, authenticate, and read the session cookie — identical value = fixation prep confirmed. NO-GAIN: never let a third party authenticate through your fixed session.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
