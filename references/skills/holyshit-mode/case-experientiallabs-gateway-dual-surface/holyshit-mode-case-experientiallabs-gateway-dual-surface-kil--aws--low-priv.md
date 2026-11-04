# Kill-chain that worked — aws / low-priv

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-kil.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **aws** · auth **low-priv** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (aws × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
