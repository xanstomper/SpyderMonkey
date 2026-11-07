# The two crown compound findings — iot-edge / high-priv

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-the-two-cro.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot-edge** · auth **high-priv** · chain role **final**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- **Free AI / payment-gate bypass.** A vLLM `/invocations` (or `/generate`, `/completions`)
  control-plane route that serves LLM completions keylessly while `/v1/chat/completions` is 401.
  It accepts ANY catalog slug routed to that lane (`claude-opus-5`, `deepseek-r1`, glm/qwen/...)
  — incl. models that advertise `requires_payment:true` on the paid surface → **payment-gate
  bypass**. `stream:true` → SSE = drop-in for any OpenAI SDK. This is COMPROMISE (upstream
  bill-drain + free premium inference), not an observation. The served_by model can differ from
  the requested one (model substitution), and an **abliterated** model may be served by default.
- **Unauthenticated infra write.** `/scale_elastic_ep`-style control plane lets an attacker
  resize the serving fleet's data-parallel engines: cost-destruction (scale up) or DoS (scale to
  0, if `0` isn't validation-blocked). Even when `0` → 400 "must be positive", unbounded positive
  scaling still executes.

## Probe adjustment (iot-edge × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
