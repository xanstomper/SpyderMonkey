# 9.6 Drift oracles — fire FIRST on every re-entry (score 90, mandatory)

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- PTOK drift (LLM targets): 3× identical 1-word requests → `usage.prompt_tokens`: constant =
  stateless/patched; drifting = shared buffer re-emerged (highest-value re-find).
- Bundle-hash diff (§2.8), wayback CDX diff (§2.3), wall-shape re-verify (403 → 500 drift).
- TOP prior compromisables were patched between sessions — re-asserting without a fresh test
  is a stale-finding ERROR.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
