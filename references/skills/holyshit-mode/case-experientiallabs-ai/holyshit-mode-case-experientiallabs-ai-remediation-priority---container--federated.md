# Remediation (priority order) — container / federated

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-remediation-priority-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
