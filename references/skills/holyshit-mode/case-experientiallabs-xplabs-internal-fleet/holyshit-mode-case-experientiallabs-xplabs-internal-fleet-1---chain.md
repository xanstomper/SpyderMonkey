# 1. How to discover the hidden internal fleet (keyless catalog base_url leak) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-1-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`GET https://<platform>/api/models` is a KEYLESS catalog (public row mode). Model rows include a
`providers[]` array; **self-hosted lanes carry a real `base_url`** where cloud lanes carry `null`.
On experientiallabs, the `experiential_cloud` provider rows leaked 8 real internal serving
endpoints:

```
gateway.xplabs.ai/glm/v1  gateway.xplabs.ai/glm3/v1  gateway.xplabs.ai/qwen/v1
wm.xplabs.ai/v1   clef.xplabs.ai/v1   clef.xplabs.ai/flash/v1
```

- These map to specific model slugs: `glm-5.3-flash`→/glm, `deepseek-v4-flash`→wm,
  `qwen3.8-27b`→/qwen, `clef(-flash)`→clef.
- The public gateway's own docs/`openapi.json` NEVER list these — they're reachable only by
  mining the catalog for non-null `base_url` on provider rows.
- **Sweep all `*.xplabs.ai`-style base domains** (`dig +short <sub>.<base>`), and probe each
  host's `/openapi.json`, `/docs`, `/health`, live/ready probes — internal gateways frequently
  leave FastAPI/Caddy auto-docs ON while the public edge disables them.
- Recipe: `grep base_url in catalog → enumerate <base> subdomain family → probe /openapi.json+/docs → read full internal route map`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
