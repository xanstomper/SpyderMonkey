# 2. Edge control-plane route discovery + validation-not-auth discriminator — grpc / high-priv

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-2-edge-contro.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **high-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

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

## Probe adjustment (grpc × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
