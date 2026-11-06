# 2. Edge control-plane route discovery + validation-not-auth discriminator — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-2-edge-contro.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Mine `/openapi.json` on the internal gateway** (it 200s keyless on the lanes that are
  misconfigured); find `/scale_elastic_ep`, `/is_scaling_elastic_ep`, `/generative_scoring`,
  `/kv_event_sources`, `/detokenize`, `/load`, `/invocations`, `/metrics`, `/version`.
- **Auth-asymmetry discriminator:** inference (`/v1/completions`, `/v1/chat/completions`) → 401,
  but the control-plane routes → 200/400/500. A **400 with a field-name error = auth PASSED and
  body-validation only**; supply the named field and the endpoint executes. `/scale_elastic_ep`
  asked `new_data_parallel_size is required` → `{new_data_parallel_size: 1000}` → `500 "Scale failed"`
  (it actually TRIED an unbounded scale → real execution, not a stub).
- **Contract map = the value:** probe with incrementally-satisfied bodies and read the next missing
  field from each 400. This both proves reachability AND maps the invoke contract WITHOUT triggering
  the destructive value. Do not actually trigger DoS-to-zero or a huge scale on operator infra —
  prove with the safe floor (`1`) and honestly note the destructive test is operator's call.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
