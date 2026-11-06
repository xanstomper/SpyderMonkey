# 4. CONFIRMED — Internal gateways expose full API specs publicly (score 50) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-4-confirmed-internal-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `GET https://wm.xplabs.ai/openapi.json` → 200 (242KB, full vLLM/OpenAI/Anthropic surface +
  control-plane routes: `/scale_elastic_ep`, `/is_scaling_elastic_ep`, `/kv_event_sources`,
  `/generative_scoring`, `/tokenize`, `/load`, `/measure`).
- `GET https://gateway.xplabs.ai/openapi.json` and `/docs` → 200.
- **IMPACT:** Full internal surface map + control-plane discovery primitive. This is what
  made Finding 1 trivially discoverable.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
