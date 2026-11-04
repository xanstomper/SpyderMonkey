# Remediation (priority order)

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
