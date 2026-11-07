# OIDC scope/audience downgrade

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Resource servers trust the AS's audience tag; an attacker-controlled client registration (or a lax AS) can mint tokens for scopes the principal never granted. Decisive test: request scope=X with prompt=none from a fresh session and compare the minted token's scope/aud claims against the consent screen's promises — a delta is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
