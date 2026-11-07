# Dedupe-by-leading-word discipline

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Two rows sharing a leading word collide — title every finding with a distinct leading word (the engagement-ops rule). Decisive test: `ledger list` post-registration shows both rows — the survival check.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
