# 2. CONTROL-PLANE AUTH ASYMMETRY (the crown pattern) — container / machine

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-2-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **machine** · chain role **final**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

The internal host `wm.xplabs.ai` ran the SAME vLLM OpenAI/Anthropic inference stack as the
public edge, but **the control-plane/inference routes were unauthenticated while
`/v1/chat/completions` correctly 401'd**. Test every route for **"validation-only 400"** —
a 400 that names a required body field (not a 401/403) is the signature of an unauthenticated
live endpoint that just needs the right body:

- **`/invocations`** — vLLM's keyless text-completion route. `POST {"prompt":"...","model":"<any catalog slug>"}`
  returns a real `text_completion` with **no API key**. Validates the *entire* payment gate:
  `claude-opus-5`, `deepseek-r1`, etc. all marked `requires_payment:true` on the paid surface,
  yet served keylessly here = **payment-gate bypass / free AI / upstream bill-drain**.
  `stream:true` → SSE, a drop-in OpenAI-compatible endpoint for any SDK.
  ValueError: it accepts ANY catalog slug routed to the shared lane; unknown/other-lane models
  return 000/timeout (not an auth error) — distinguish by timing, not status.
- **`/scale_elastic_ep`** — vLLM elastic-endpoint data-parallel scaling, unauth. Body
  `{"new_data_parallel_size": N}`. Contract map: `0`/`-1`/`'x'` → 400 "must be a positive
  integer" (DoS-to-zero blocked), `1` → 200 "Scaled to N data parallel engines" (executes),
  `1000` → real `500 "Scale failed"` (proves live unbounded execution attempt). Cost-destruction:
  scale engines unboundedly = GPU burn. **Bounded-burn discipline:** confirm the contract with a
  safe floor value (1), never trigger a large scale or DoS-to-zero.
- **`/is_scaling_elastic_ep` -> 200 `{"is_scaling_elastic_ep":false}`** (POST only, GET=405).
- **`/kv_event_sources` -> 200 `{}`**, **`/load` -> 200 `{"server_load":N}`**, **`/version`**,
  **`/detokenize`**, **`/generative_scoring`** (needs `{query, items, label_token_ids}`) — all
  validation-200, no auth.
- **`/metrics` and `/debug/pprof`** return 403 for the public hostname but **200 with
  `Host: 127.0.0.1`/`Host: localhost`** (via `--resolve 127.0.0.1:443:<ip>`). Serve is **Caddy**
  (`server: Caddy`) — a loopback-only ACL that is **Host-header/SNI bound and remotely
  spoofable**. Host-header-based internal-surface ACL bypass.

## Probe adjustment (container × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
