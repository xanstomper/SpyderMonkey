# 3a. CONFIRMED — Unbounded elastic-scale execution / cost-destruction (score 78) — web-app / unauth

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-3a-confirmed-unbounde.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **web-app** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- `POST /scale_elastic_ep` accepts **any positive integer** for `new_data_parallel_size`.
- **EVIDENCE:** `0` → 400 "must be a positive integer" (DoS-to-zero blocked at validation —
  a mitigation); `1000` → **500 "Scale failed"** — the endpoint actually *attempted* the
  unbounded scale and hit an internal error, proving real execution, not a stub; `1` → 200
  (executes). A moderately-high feasible value matching real engine counts will execute.
- **IMPACT:** Cost-destruction / resource-wastage on the operator's upstream — scale the
  DeepSeek lane's data-parallel engines unboundedly = GPU/serving cost burn.
- **CONFIDENCE:** High.

## Probe adjustment (web-app × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
