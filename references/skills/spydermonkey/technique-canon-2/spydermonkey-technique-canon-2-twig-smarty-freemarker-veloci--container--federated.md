# Twig/Smarty/Freemarker/Velocity fingerprints — container / federated

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-twig-smarty-freemarker-veloci.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **federated** · chain role **entry**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`{{7*7}}` variants per engine (twig `{{7*7}}` ok, smarty `{php}` legacy, freemarker `<#assign>`, velocity `#set`) — the fingerprint table IS the class map. Decisive test: one marker per engine until one renders.

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
