# 1. Supply-chain orchestration leak — `GET /status?json=1` (score 60-70) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-1-supply-chain-o.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Unauth status JSON dumps the ENTIRE upstream provider fleet:
- 10 aggregator providers: `deepseek, gonka, hyb, kallme, kiosapi, longcat, muse, ollama, stealth, yjs`
- Crypto-billing host: `gonka-api.org` ("balance too low, top up via crypto, no subscription")
- Router host: `router.kiosapi.com/v1/chat/completions` (kiosapi)
- Internal backend name: `hyb` calls its backend **"venesus"** (`venesus chat error 404` in bodies)
- Taiwanese `yjs` distributor, Chinese error with request IDs:
  `分組 auto 下模型 laguna-s-2.1 無可用管道（distributor） (request id: 202610061000176252022908268d9d6nWCOUkyz)`
  → reveals a "distributor" pipeline architecture under yjs.
- `stealth/ox-alpha` upstream returns raw legacy IE6-era HTML (different originating stack).
- `kallme/*` upstream = Anthropic chromium fleet (503s).
- 49 models total in status vs fewer in public `/v1/models` — extras are the hidden/provisioned tier.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
