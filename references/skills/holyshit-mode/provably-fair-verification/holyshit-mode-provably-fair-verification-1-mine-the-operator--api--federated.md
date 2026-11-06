# 1. Mine the operator's documented scheme first — api / federated

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-1-mine-the-operator.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **api** · auth **federated** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Search their blog/help-center for the PF explainer. Extract: seed model (server/client
seed, nonce), commitment pattern (commit-and-reveal, hash chain), consumption order
(forward chain vs reverse chain), and the published anchor ("final hash published before
play"). This defines exactly what the public wire must show for the claim to hold.

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
