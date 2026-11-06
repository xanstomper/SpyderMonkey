# Lateral rules (the strictest) — api / federated

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-lateral-rules-the-strictest.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **federated** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. Own declared estates only — the scope authority (`~/.redteam/scope.json`) is
   checked; out-of-scope hosts refuse.
2. One shot per path per engagement window — never repeated without drift.
3. Nothing persists: no keys copied to disk, no schedules, no implants.
4. Every CONFIRMED lateral → shukaku ingest (the family loop closes).

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
