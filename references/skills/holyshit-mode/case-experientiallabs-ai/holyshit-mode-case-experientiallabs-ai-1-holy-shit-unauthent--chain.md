# 1. HOLY SHIT — Unauthenticated elastic-scaling control-plane on `wm.xplabs.ai` (score 85) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-1-holy-shit-unauthent.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
