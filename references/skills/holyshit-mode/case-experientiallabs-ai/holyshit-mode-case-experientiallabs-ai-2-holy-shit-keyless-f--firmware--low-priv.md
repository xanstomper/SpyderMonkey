# 2. HOLY SHIT — Keyless free-AI inference on `wm.xplabs.ai/invocations` (score 80) — firmware / low-priv

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-2-holy-shit-keyless-f.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **firmware** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
