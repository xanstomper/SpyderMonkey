# Two-factor placement

- source canon: `spydermonkey/technique-canon-12.md`
- bindings: **WSTG-ATHN-09** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

OTP/MFA enforced client-side only. Decisive test: the server accepting the skip = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
