# The two crown compound findings — chain composition

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-the-two-cro.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
