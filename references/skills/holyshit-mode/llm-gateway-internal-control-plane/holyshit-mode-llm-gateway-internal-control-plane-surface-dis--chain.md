# Surface-discovery pattern (recon to impact in ~6 moves) — chain composition

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-surface-dis.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Grab `/llms.txt` + `/.well-known/api-catalog` first.** These are linked from the HTTP
   `Link:` headers and often carry the full API contract: base URL, the management-API split
   (`/v1` inference vs `/api` management), key format (`xpl_` + 40 hex), and the fact that
   "one key reaches both surfaces but CANNOT mint keys / reach admin." This map precedes ANY
   targeted probe.
2. **`/api/models` (the management catalog) is often keyless** even when `/v1/models`
   (the OpenAI-compatible list) requires a key — the docs spell this split out. `GET /api/models`
   keyless leaks the **entire catalog**: every model, its provider rows, billing fields, AND the
   **internal `base_url` of each routing lane** (e.g. `wm.x***REDACTED***.ai/v1`, `gateway.x***REDACTED***.ai/qwen/v1`,
   `...us-east.modal.direct/v1`). Grep every provider row's `base_url` — that's the internal fleet.
3. **Enumerate `*.internal-tld` subdomains** (crt.sh + `socket.getaddrinfo` on a wordlist).
   The catalog base_urls reveal the fleet; confirm each host answers from the internet.
4. **Pull `/openapi.json` on every internal host.** The PUBLIC gateway often has none (or a
   relay stub), but internal serving gateways frequently ship the full spec — revealing
   control-plane routes (`/invocations`, `/scale_elastic_ep`, `/is_scaling_elastic_ep`,
   `/generative_scoring`, `/kv_event_sources`, `/load`, `/detokenize`, `/tokenize`) that the
   public surface never exposes.
5. **Probe auth-ASYMMETRY, not just presence.** Fire `/v1/chat/completions` (expect 401) THEN
   the control-plane routes with an empty/minimal body. The discriminator:
   - `401` = auth-gated (like inference).
   - `400` with a "field required" / **field name in the error** = NO AUTH — only body
     validation blocks execution. Supply the field and it executes. `{"new_data_parallel_size" is
     required"}` → send it → `200 "Scaled to N data parallel engines"`.
   - `404`/`000` = not on this host / model-not-on-lane.
6. **Verify the control-plane primitive ONCE with a bounded, non-destructive value**, then stop.
   For free-AI: one minimal `{"prompt":"Say OK","model":"<slug>"}` proves reachability; a
   `stream:true` probe proves OpenAI-SDK drop-in usability. For scaling: use the safe floor (1),
   NOT 0 (DoS) and NOT a huge number (cost burn). The `500 "Scale failed"` on a huge value is
   itself proof the endpoint really attempts the op (not a stub).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
