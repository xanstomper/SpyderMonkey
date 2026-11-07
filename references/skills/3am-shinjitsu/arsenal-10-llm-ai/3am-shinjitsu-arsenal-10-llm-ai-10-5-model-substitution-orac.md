# 10.5 Model-substitution oracle (score 75)

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `served_by`/upstream headers vs requested model = substitution collapse (pay-for-X,
  served-Y). Client-supplied `system` role honored = stack manipulation primitive.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
