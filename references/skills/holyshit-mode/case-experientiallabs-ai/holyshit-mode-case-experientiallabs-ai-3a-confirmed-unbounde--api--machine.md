# 3a. CONFIRMED — Unbounded elastic-scale execution / cost-destruction (score 78) — api / machine

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-3a-confirmed-unbounde.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **api** · auth **machine** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `POST /scale_elastic_ep` accepts **any positive integer** for `new_data_parallel_size`.
- **EVIDENCE:** `0` → 400 "must be a positive integer" (DoS-to-zero blocked at validation —
  a mitigation); `1000` → **500 "Scale failed"** — the endpoint actually *attempted* the
  unbounded scale and hit an internal error, proving real execution, not a stub; `1` → 200
  (executes). A moderately-high feasible value matching real engine counts will execute.
- **IMPACT:** Cost-destruction / resource-wastage on the operator's upstream — scale the
  DeepSeek lane's data-parallel engines unboundedly = GPU/serving cost burn.
- **CONFIDENCE:** High.

## Probe adjustment (api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
