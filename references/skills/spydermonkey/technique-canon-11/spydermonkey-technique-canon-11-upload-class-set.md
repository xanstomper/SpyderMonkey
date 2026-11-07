# Upload-class set

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-BUSL-09** · **CWE-434** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Extension/content-type/size validation absent — DETECTION via benign markers. Decisive test: upload accepted with mismatched type + the served path = the class (never a working payload).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
