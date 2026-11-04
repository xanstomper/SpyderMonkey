# 10.3 Playground-proxy auth bypass (score 90) — chain composition

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-3-playground-proxy-auth-b.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- SPA "try it" playgrounds expose INTERNAL proxies skipping the public API-key gate.
- DECISIVE: fetch playground HTML → grep `fetch\(` for proxy paths → sweep `/pg/*`,
  `/api/playground/*`, `/demo/*`, `/internal/*` → 502 `upstream_unavailable` = auth PASSED
  (iterate provider prefixes before concluding); burst-rate the PROXY specifically.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
