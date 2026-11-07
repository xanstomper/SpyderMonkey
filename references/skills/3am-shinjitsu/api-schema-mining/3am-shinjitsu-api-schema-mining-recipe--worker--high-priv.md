# Recipe — worker / high-priv

- source canon: `3am-shinjitsu/api-schema-mining.md`
- base technique: `3am-shinjitsu-api-schema-mining-recipe.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

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

## Probe adjustment (worker × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
