# HOLY SHIT #1 — Unauthenticated free AI via playground proxy (score 90) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- base technique: `holyshit-mode-case-obsidian-y-api-holy-shit-1-unauthenticate.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`POST /pg/chat` — the playground's internal backend path — requires NO API key and serves real completions. The operator assumed /pg/* was internal; it's internet-reachable.
- Working models at test time: `meituan/longcat-2.0`, `ollama/*` (qwen3.6-35b, gemma4-26b, llama4, qwen3.8), `muse/muse-glimmer`, `laguna/*`, `ling/ling-3.0-flash-fin`. `hyb/*`+`asdisunknown/*` upstream 502 (down at test time, same free access).
- Malformed requests give clean validation errors (`messages must be a non-empty list`) — fine-grained oracle, model existence via `model_not_found` vs 502.
- Same vuln on the Vercel host — always test BOTH hosts when docs leak a second base URL (docs page contained the vercel URL verbatim).
- 15-burst: zero 429s. No rate limiter anywhere.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
