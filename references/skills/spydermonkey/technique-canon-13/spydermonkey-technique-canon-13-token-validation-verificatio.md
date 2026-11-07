# Token-validation verification

- source canon: `spydermonkey/technique-canon-13.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Server-side validation of signature/expiry/audience. Decisive test: forged-but-benign acceptance = the absence.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
