# 1.11 Request-smuggling differential (score 55) [owned infra only]

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **WSTG-ADV-02** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- ONE CL.TE differential probe max; timing-only. Any ambiguity = stop, document, never iterate.
- Serverless/CDN-fronted (no dual proxy layer) = N/A — say once, pivot.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
