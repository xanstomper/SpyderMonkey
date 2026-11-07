# Data-at-rest verification

- source canon: `spydermonkey/technique-canon-13.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Sensitive material unencrypted in backend stores — provable only from confirmed footholds (kaisha-priced) or client mirrors. Decisive test: the mirrored artifact's plaintext = the absence.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
