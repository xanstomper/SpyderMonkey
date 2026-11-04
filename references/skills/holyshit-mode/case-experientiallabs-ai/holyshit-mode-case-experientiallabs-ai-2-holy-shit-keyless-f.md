# 2. HOLY SHIT — Keyless free-AI inference on `wm.xplabs.ai/invocations` (score 80)

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- **VERDICT: CONFIRMED — free AI + upstream bill-drain (COMPROMISE)**
- **EVIDENCE:**
  - `POST https://wm.xplabs.ai/invocations` body `{"prompt":"...","model":"claude-opus-5"}`
    → **200** with a real completion, **no API key**. Inference gate (`/v1/chat/completions`)
    returns 401, but `/invocations` does not.
  - **BY-PASSES THE `requires_payment` GATE on the entire paid catalog.** On the paid
    surface, `claude-opus-5`, `deepseek-r1`, etc. all advertise `requires_payment:true`
    (paid credits needed). `/invocations` serves them keylessly, ignoring the payment gate
    entirely — a complete payment-gate bypass, not just the free-trial models.
  - Serves the operator's **most expensive models keyless:** `claude-opus-5` (Anthropic
    flagship), `deepseek-r1`, `glm-5.3(-flash)`, `deepseek-v4-flash`, `qwen3.8-27b`,
    `internvl3-38b` (any catalog slug routed to the shared lane).
  - **`stream:true` → returns SSE chunks** — a fully **OpenAI-compatible drop-in inference
    endpoint** usable by any OpenAI SDK.
  - Notable: requests for some models are served by `glm-5.3-flash-abliterated`
    (served_by/model-substitution).
- **IMPACT:** Any attacker gets **free premium inference** and can **drain the operator's
  upstream wallet** (bill-drain) across the paid catalog. The abliterated (uncensored) model
  is served by default on this lane. COMPROMISE class.
- **CONFIDENCE:** High — live 200 completions + SSE stream observed across multiple models.
- **BOUNDED-BURN NOTE:** Proven with minimal calls; NOT scaled to a drain. Operator owns the
  estate and authorized the free-AI hunt.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
