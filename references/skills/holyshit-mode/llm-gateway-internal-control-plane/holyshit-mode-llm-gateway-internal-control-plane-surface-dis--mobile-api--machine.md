# Surface-discovery pattern (recon to impact in ~6 moves) — mobile-api / machine

- source canon: `holyshit-mode/llm-gateway-internal-control-plane.md`
- base technique: `holyshit-mode-llm-gateway-internal-control-plane-surface-dis.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **machine** · chain role **entry**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. **Grab `/llms.txt` + `/.well-known/api-catalog` first.** These are linked from the HTTP
   `Link:` headers and often carry the full API contract: base URL, the management-API split
   (`/v1` inference vs `/api` management), key format (`xpl_` + 40 hex), and the fact that
   "one key reaches both surfaces but CANNOT mint keys / reach admin." This map precedes ANY
   targeted probe.
2. **`/api/models` (the management catalog) is often keyless** even when `/v1/models`
   (the OpenAI-compatible list) requires a key — the docs spell this split out. `GET /api/models`
   keyless leaks the **entire catalog**: every model, its provider rows, billing fields, AND the
   **internal `base_url` of each routing lane** (e.g. `wm.xplabs.ai/v1`, `gateway.xplabs.ai/qwen/v1`,
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

## Probe adjustment (mobile-api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
