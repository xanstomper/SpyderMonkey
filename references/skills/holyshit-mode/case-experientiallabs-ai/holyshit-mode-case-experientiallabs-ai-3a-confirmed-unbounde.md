# 3a. CONFIRMED — Unbounded elastic-scale execution / cost-destruction (score 78)

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `POST /scale_elastic_ep` accepts **any positive integer** for `new_data_parallel_size`.
- **EVIDENCE:** `0` → 400 "must be a positive integer" (DoS-to-zero blocked at validation —
  a mitigation); `1000` → **500 "Scale failed"** — the endpoint actually *attempted* the
  unbounded scale and hit an internal error, proving real execution, not a stub; `1` → 200
  (executes). A moderately-high feasible value matching real engine counts will execute.
- **IMPACT:** Cost-destruction / resource-wastage on the operator's upstream — scale the
  DeepSeek lane's data-parallel engines unboundedly = GPU/serving cost burn.
- **CONFIDENCE:** High.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
