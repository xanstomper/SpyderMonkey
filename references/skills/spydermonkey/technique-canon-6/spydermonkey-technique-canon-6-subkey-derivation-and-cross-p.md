# Subkey derivation and cross-protocol key reuse

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Same key material across protocols/tiers (the mkey+securityKey class) — proven from bundle/config co-occurrence + one probe showing cross-tier acceptance on YOUR test material.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
