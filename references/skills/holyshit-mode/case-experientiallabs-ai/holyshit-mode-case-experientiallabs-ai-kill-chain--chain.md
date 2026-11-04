# Kill-chain — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-kill-chain.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Recon (keyless catalog + SPF + DNS) → internal-fleet enumeration (`*.xplabs.ai` base_url leak
in `/api/models`) → internal control-plane discovery (`/openapi.json`) → **unauth free-AI
inference (`/invocations`, premium models) + unauth elastic-scaling control-plane
(`/scale_elastic_ep`) = Impact**.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
