# Error-code vocabulary = the API feature map — graphql / machine

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-error-code-vocabula.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **machine** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Grep all chunks for the platform's error-code prefix (e.g. `er_[a-z0-9_]+`) and sort: every
`er_<feature>_<failure>` names an endpoint family that may not appear in any fetch site
(kick, telegram, sol, kyc/persona, vault+2fa, raffles, seeds, party). 150+ codes = a full
hidden-surface inventory; score only after probing, but USE the map to pick probe targets
(and to spot auth methods the current UI hides, e.g. sol-wallet sign-in codes without a UI
button).

## Probe adjustment (graphql × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
