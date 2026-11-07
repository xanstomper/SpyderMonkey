# 10.1 Hidden-model map (score 80)

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- DECISIVE: `curl /status?json=1` (find via `fetch("/status?json=1")` in page JS) — diffs
  against public `/v1/models`: extras = hidden tier + upstream vendor names + verbatim error bodies.
- GATE DISCRIMINATOR: private models → `no_access` (403) vs `model_not_found` (404) for
  nonexistent = models exist server-side AND gate is real code.
- BYPASS MATRIX (all-variants-once discipline): case swap, lead/trail space, null byte,
  trailing dot, double-slash, `:latest`, `?query`, array-typed model field
  (`{"model":["x"]}`), `stream:true`, second host. Uniform failure = hardened, ledger it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
