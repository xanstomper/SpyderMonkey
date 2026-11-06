# Rate limits & rotation — firmware / federated

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-rate-limits-rotation.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **firmware** · auth **federated** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Per-account ~6 req/min on media endpoints, but with phone_autoconfirm signup, rotation is trivial: mint fresh account on 429 (2s per account). Also retry "exhausted" upstream models on fresh accounts — some 429s are per-session.

## Probe adjustment (firmware × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
