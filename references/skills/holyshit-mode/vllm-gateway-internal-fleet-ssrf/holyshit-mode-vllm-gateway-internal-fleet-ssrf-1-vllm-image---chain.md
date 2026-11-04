# 1. vLLM `image_url` SSRF + COST-FREE status oracle (the big one) — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-1-vllm-image-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

On vLLM-backed OpenAI-compatible inference endpoints, `POST {api}/invocations` (and some
`/v1/chat/completions`) accept an `image_url` content part that the worker **fetches server-side**
and — crucially — **reports the fetched HTTP status / connect result in the error message**.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
