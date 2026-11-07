# Stage 2 — The unauth worker-level proto surface (the crown) — firmware / expired

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- base technique: `holyshit-mode-hardened-gateway-internal-fleet-proto-surface-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **firmware** · auth **expired** · chain role **final**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

On a vLLM + Caddy internal gateway:
- **`/invocations` — keyless inference = free premium AI + payment-gate bypass + bill-drain.**
  `POST /invocations {"prompt":"...","model":"claude-opus-5","stream":true}` → 200 SSE completion, NO
  key, while `/v1/chat/completions` on the same host returns 401. Serves the whole paid catalog
  (`claude-opus-5`, `deepseek-r1`, glm/qwen/internvl) keylessly, **ignoring `requires_payment`** = a
  complete payment-gate bypass (verify by noting the paid surface advertises `requires_payment:true`).
  `stream:true` ⇒ drop-in OpenAI-SDK endpoint → free-AI / unlimited upstream bill-drain.
  Serve-mismatch: one requested model may be answered by another (`glm-5.3-flash-abliterated` for
  deepseek) — the uncensored model bypasses the content gate too.
- **`/scale_elastic_ep` — unauth control-plane write.** `POST {"new_data_parallel_size":N}` → 200
  "Scaled to N data parallel engines", no auth. `0` blocked (400 "positive integer") but **any
  positive int executes** (1000 → real 500 "Scale failed" proves unbounded execution attempt) =
  cost-destruction / GPU-burn. Control plane bypasses the auth gate that inference enforces.
- **`/usage.json` + `/usage` — keyless internal billing/tenant ledger.** Internal `identity` names
  (`platform`, `opflow`, `kion-unlimited`) + per-tenant token/cost (µUSD), world-readable.
- **`/openapi.json` + `/docs`** expose the full control/inference surface (`/generative_scoring`,
  `/tokenize`, `/detokenize`, `/load`, `/is_scaling_elastic_ep`, `/kv_event_sources`). Many answer
  validation-only 400 — **no auth, only a missing body field** (error oracles disclose the field).
- **Caddy `Host`-header ACL bypass on `/metrics`+`/debug/pprof`:** `server: Caddy`; `/metrics` 403 for
  the public hostname, but **200 with `Host: 127.0.0.1`/`localhost`** via `--resolve`. The loopback-only
  ACL is Host/SNI-bound and remotely spoofable.

## Probe adjustment (firmware × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
