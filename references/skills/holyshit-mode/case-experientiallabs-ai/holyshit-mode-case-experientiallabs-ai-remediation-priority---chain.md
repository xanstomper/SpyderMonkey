# Remediation (priority order) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-remediation-priority-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **[CRITICAL]** Put the `/invocations` + `/scale_elastic_ep` (and `/generative_scoring`,
   `/tokenize`, `/detokenize`, `/kv_event_sources`, `/is_scaling_elastic_ep`, `/load`)
   control-plane of `wm.xplabs.ai` behind the **same bearer/auth gate as `/v1/chat/completions`**,
   or move them off the public edge to an internal network / admin-only route. Free premium
   inference + unauth GPU scaling = the two crown findings, both on this surface.
2. **[HIGH]** Gate `/usage` + `/usage.json` on `gateway.xplabs.ai` behind auth, or restrict to
   internal network. Internal tenant/account names + spend must not be world-readable.
3. **[MED]** Disable `openapi.json`/`/docs` auto-generation on the public-facing internal
   gateways (`docs_url=None`, `openapi_url=None`) or ACL them.
4. **[LOW]** Hide `clef.xplabs.ai/health` GPU metrics behind auth.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
