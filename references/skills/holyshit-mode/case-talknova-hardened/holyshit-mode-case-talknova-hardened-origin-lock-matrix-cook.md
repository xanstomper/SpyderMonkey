# Origin-lock matrix (cookie-auth endpoints)

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

For each POST endpoint, fire: attacker Origin, `Origin: null`, and NO Origin — all should 403.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
