# Kill-chain that worked

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

1. **`GET /.well-known/api-catalog`** (advertised in the root `Link:` header):
   `{"linkset":[{"anchor":"https://api.<domain>/v1","service-desc":[{"href":".../openapi.json"}]}]}`.
   Also `</docs>` and `</llms.txt>` are advertised in the root HTTP `Link:` header.
   **Always read the `Link:` header first** — it hands you the API-meta endpoints for free.
2. **Keyless catalog reads leak internal `base_url`s.** `GET /api/models` (public, no key)
   returns every model + per-provider rows incl. `base_url`. Any non-null `base_url` that is
   NOT the public host is an **internal serving endpoint**: here
   `gateway.xplabs.ai/glm|glm3|qwen`, `wm.xplabs.ai`, `clef.xplabs.ai`.
3. **DNS-enumerate the leaked host family.** `dig +short <sub>.xplabs.ai` revealed
   `gateway./wm./clef./platform./www.` — all publicly reachable on GCP/Azure/other ranges.
4. **Probe each internal host for `/openapi.json` + `/docs`.** The DeepSeek lane
   (`wm.xplabs.ai`) returned a 242KB full vLLM surface incl. control-plane routes. This is
   the single highest-value recon primitive: **internal hosts often leak openapi.json even
   when the public edge doesn't.**
5. **Find the auth-asymmetry.** On the same internal host, `/v1/chat/completions` was 401
   but `/invocations`, `/scale_elastic_ep`, `/generative_scoring`, `/load`, `/is_scaling_elastic_ep`,
   `/kv_event_sources`, `/detokenize` were **open**. Same-host asymmetry = misconfig = crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
