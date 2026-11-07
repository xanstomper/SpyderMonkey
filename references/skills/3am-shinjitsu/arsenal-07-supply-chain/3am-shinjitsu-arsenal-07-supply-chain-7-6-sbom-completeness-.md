# 7.6 SBOM completeness (score 55)

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Phantom deps (referenced, never shipped), license gaps as attack-surface indicators,
  reproducible-build validation on operator artifacts.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
