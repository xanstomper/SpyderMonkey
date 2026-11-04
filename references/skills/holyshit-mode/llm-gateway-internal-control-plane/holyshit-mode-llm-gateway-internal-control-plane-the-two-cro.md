# The two crown compound findings

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
