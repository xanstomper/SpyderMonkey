# API-key extraction from the build

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Embedded API keys/tokens in the binary/resources (the merchant-key class at mobile tier). Decisive test: strings/manifest analysis of your build — the key + its use-site pairing = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
