# Leak claims: row-level correlation or it isn't a finding — cloud / federated

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-leak-claims-row-level-correlatio.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Counting `"display_username"` fields does NOT prove a masking failure — a feed full of
visible users also contains that field. The decisive test: find rows where the masked
field (`username == "Hidden user"`) appears, then check the SAME row's `display_username`
for a real value. Report `masked occurrences → correlated rows → unique userIds`. Only the
correlated count is the leak; the rest is noise. Same discipline as the 3-gate: a diff
needs the baseline and the attack joined on the same object.

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
