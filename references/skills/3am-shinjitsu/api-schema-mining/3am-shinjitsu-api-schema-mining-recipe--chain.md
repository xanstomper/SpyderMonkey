# Recipe — chain composition

- source canon: `3am-shinjitsu/api-schema-mining.md`
- base technique: `3am-shinjitsu-api-schema-mining-recipe.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. `curl https://docs.<domain>/llms.txt` — agent-friendly docs platforms (ReadMe.io and
   similar) publish a markdown index of every page. `<meta name="readme-deploy">` /
   `readme-subdomain` in the HTML shell confirms ReadMe.
2. The index links `https://docs.<domain>/reference/<slug>.md` — fetch each; the body
   carries a complete OpenAPI 3.1 JSON block under `# OpenAPI definition`: servers,
   securitySchemes (auth header scheme + bearer format), paths, operationIds,
   request/response schemas, and EXAMPLE VALUES. Saving every page IS the schema library
   — no fuzzing, no rate limit, no WAF.
3. Also try `/llms-full.txt`, `/sitemap.xml`, `/openapi.json` — but expect `openapi.json`
   to be WAF-gated or proxied to the real API (same bot-gate as `/api/*`;
   see edge-gate-recon.md). llms.txt yields the same schema anyway.
4. Fetch `/changelog/<slug>.md` pages too — they document feature and trust-model changes
   (token storage, automation grants, dispute mechanics) that the reference buries.
5. Error-envelope archaeology: the example 400/500 values in the OpenAPI blocks show the
   framework's real error shape (e.g. Laravel `exception` + `backtrace` JSON envelopes).
   That shape is what the live API returns — confirm with ONE request once credentialed.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
