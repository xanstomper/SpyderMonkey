# 1. HOLY SHIT — Unauthenticated elastic-scaling control-plane on `wm.xplabs.ai` (score 85)

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
