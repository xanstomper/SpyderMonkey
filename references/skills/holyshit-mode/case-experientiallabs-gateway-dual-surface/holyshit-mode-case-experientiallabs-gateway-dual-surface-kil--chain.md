# Kill-chain that worked — chain composition

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-kil.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
