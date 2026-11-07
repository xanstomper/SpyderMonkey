# Azure IMDS and SAS-token exposure

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

IMDS (169.254.169.254/metadata/instance) and SAS tokens in client code (long-lived, broad-scope). Decisive test: metadata response fields; SAS token parsed for scope/expiry — an unexpired broad token in client JS is the crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
