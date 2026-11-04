# 1. HOLY SHIT — Unauthenticated elastic-scaling control-plane on `wm.xplabs.ai` (score 85) — api / low-priv

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-1-holy-shit-unauthent.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **VERDICT: CONFIRMED — control (unauth infra manipulation / DoS / cost destruction)**
- **EVIDENCE:**
  - `POST https://wm.xplabs.ai/scale_elastic_ep` body `{"new_data_parallel_size": N}`
    → `200 {"message":"Scaled to N data parallel engines"}`
  - **No auth token required.** Compare: inference `/v1/chat/completions` → `401 Unauthorized`.
    The control plane bypasses the auth gate that inference enforces.
  - The only requirement is a body field; the error oracle disclosed the exact field name
    (`new_data_parallel_size is required`) on an empty-body probe.
- **IMPACT:** An attacker resizes the data-parallel engine count of the elastic endpoint.
  `num=0` → **denial of service** of the DeepSeek lane; `num=high` → **GPU/serving-cost
  destruction** against the operator's fleet (and the upstream it routes to). Availability +
  financial damage to operator-owned assets = **COMPROMISE class**, not an observation.
- **CONFIDENCE:** High — live 200 confirmation of actual scaling execution.
- **NEXT DECISIVE TEST:** Destructive-trigger test (scale up/down) is the operator's call —
  I only executed a bounded, minimal `new_data_parallel_size: 1` (safe floor), no burn.
- **BOUNDED-BURN NOTE:** I did NOT trigger a cost-heavy scale; the finding is proven by one
  `1`-engine confirmation. Per mandate discipline, the vulnerability proof is that an
  attacker COULD scale; I measured the primitive, not the damage.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
