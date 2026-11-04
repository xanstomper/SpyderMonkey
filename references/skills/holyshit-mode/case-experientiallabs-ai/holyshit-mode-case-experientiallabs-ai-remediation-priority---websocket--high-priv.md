# Remediation (priority order) — websocket / high-priv

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-remediation-priority-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **high-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (websocket × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
