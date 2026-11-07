# 2. CONTROL-PLANE AUTH ASYMMETRY (the crown pattern) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-2-.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
