# L5 — TIMELINE — ci-cd / federated

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l5-timeline.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- context: **ci-cd** · auth **federated** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Audit | Synthesis |
|---|---|
| engagement pacing patterns (burst = fingerprint) | bursts chunked + paused (same discipline as noise budgets) |
| time-of-day correlation with the operator's routine | schedule around it; the vantage's timezone is the opsec timezone |

## Probe adjustment (ci-cd × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
