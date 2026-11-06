# Discovery Account Discovery (T1087) — mobile / federated

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-discovery-account-discovery-t1087.md`
- bindings: **WSTG-ATHN-07** · **CWE-640** · **ATT&CK T1078**
- context: **mobile** · auth **federated** · chain role **pivot**

## Context

- platform: family probes cover the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: valid account enumeration
- probe: response-differential username classes (login vs reset timing/length)
- wall: length/timing DIFFERENTIALS only — no successful logins attempted

## Probe adjustment (mobile × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
