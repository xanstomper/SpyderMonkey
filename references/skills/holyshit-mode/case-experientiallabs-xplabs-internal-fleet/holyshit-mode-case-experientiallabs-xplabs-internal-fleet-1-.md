# 1. How to discover the hidden internal fleet (keyless catalog base_url leak)

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
