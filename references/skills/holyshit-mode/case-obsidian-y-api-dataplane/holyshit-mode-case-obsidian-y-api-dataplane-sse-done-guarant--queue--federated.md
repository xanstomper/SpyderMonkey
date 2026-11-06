# SSE `[DONE]` guarantee — queue / federated

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-sse-done-guarant.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **queue** · auth **federated** · chain role **pivot**

## Context

- platform: management/metadata endpoints first; topics and channels are the inventory
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Upstream SSE streams can truncate without `data: [DONE]`. A browser reader loop that waits for
the terminator hangs forever. The proxy's `sse_wrap` must gated-yield `data: [DONE]\n\n` in a
`finally` when the upstream didn't. (For the browser half: a `finalize()` guard that always runs
on stream end / error / catch, so the meta/status line always renders.)

## Probe adjustment (queue × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
