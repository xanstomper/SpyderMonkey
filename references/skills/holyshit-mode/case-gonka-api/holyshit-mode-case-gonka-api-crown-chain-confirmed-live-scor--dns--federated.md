# Crown chain (confirmed live, score 75) — dns / federated

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-crown-chain-confirmed-live-scor.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **dns** · auth **federated** · chain role **final**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`disposable_signup → harakirimail_public_inbox_confirm → mint_sk_key →
20¢_free_credit → /functions/v1/gonka inference`. Operator's gateway routes to
gonka → scaled signups bleed the operator's upstream supply chain.

## Probe adjustment (dns × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
