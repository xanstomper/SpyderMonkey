# 3a. CONFIRMED — Unbounded elastic-scale execution / cost-destruction (score 78) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-3a-confirmed-unbounde.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `POST /scale_elastic_ep` accepts **any positive integer** for `new_data_parallel_size`.
- **EVIDENCE:** `0` → 400 "must be a positive integer" (DoS-to-zero blocked at validation —
  a mitigation); `1000` → **500 "Scale failed"** — the endpoint actually *attempted* the
  unbounded scale and hit an internal error, proving real execution, not a stub; `1` → 200
  (executes). A moderately-high feasible value matching real engine counts will execute.
- **IMPACT:** Cost-destruction / resource-wastage on the operator's upstream — scale the
  DeepSeek lane's data-parallel engines unboundedly = GPU/serving cost burn.
- **CONFIDENCE:** High.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
