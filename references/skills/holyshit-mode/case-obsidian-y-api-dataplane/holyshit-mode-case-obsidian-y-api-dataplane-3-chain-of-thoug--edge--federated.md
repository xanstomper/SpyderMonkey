# 3. Chain-of-thought leak — `muse/muse-glimmer` (score 50) — edge / federated

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-3-chain-of-thoug.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **edge** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`reasoning_content` field on EVERY muse response carries full hidden CoT, even for trivial math
(17*23 → narrates the working). Also leaks speculative-decoding internals:
`timings: {cache_n, draft_n, draft_n_accepted, predicted_ms}` and a concrete
`system_fingerprint: b11382-11fe02151`. No user/system secrets in the CoT here, but it's a real
instruction/privacy leak channel and confirms model internals.

## Probe adjustment (edge × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
