# Addendum — re-engage #5 (2026-10-06): proxy-fleet build + empty-content hardening — graphql / federated

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-addendum-re-enga.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **federated** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

The operator shifted from recon to building a USABLE proxy over the unauth `/pg/chat` vector:
`~/obsidian-proxy/obsidian_proxy.py` (port 8620). This is the durable "wrap an unauth upstream
chat vector as a local OpenAI-compatible gateway" pattern (see SKILL.md "Free-AI proxy build
pattern"). Session added:

## Probe adjustment (graphql × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
