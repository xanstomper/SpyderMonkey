# 10.2 PTOK drift oracle (score 90 — mandatory on every gateway re-entry)

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- 3× identical minimal requests → `usage.prompt_tokens`: CONSTANT = stateless/patched;
  DRIFTING/GROWING = live cross-user server state (the shared global buffer).
- Drift confirmed → §10.4 poisoning becomes the WRITE primitive on that buffer (own gateway
  only; score 95 when cross-user verbatim recurrence is proven).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
