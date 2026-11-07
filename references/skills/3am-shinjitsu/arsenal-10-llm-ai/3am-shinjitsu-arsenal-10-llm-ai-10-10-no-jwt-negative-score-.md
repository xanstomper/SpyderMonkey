# 10.10 No-JWT negative (score 50 — stop chasing)

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Uniform `invalid_api_key` for EVERY bearer/JWT/alg-none/Basic/key-prefix variant = NO JWT
  auth path exists. Log it. Pivot to server-side secret paths or closeout.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
