# Password-security verification

- source canon: `spydermonkey/technique-canon-13.md`
- bindings: **WSTG-ATHN-08** · **CWE-521** · **ATT&CK T1110**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Server-enforced length/complexity/newness tested by one policy-violating change. Decisive test: acceptance on your account = control absent.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
