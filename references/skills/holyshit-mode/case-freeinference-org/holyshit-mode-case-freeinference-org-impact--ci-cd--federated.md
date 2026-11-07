# Impact — ci-cd / federated

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-impact.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ci-cd** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Operational Security**: Full infrastructure topology (exact GPU models, server layout, model versions) enables adversarial capacity planning — attacker can target the cheapest/easiest-to-exhaust node for bill-drain attacks.
- **Traffic Analysis**: 278k req/day = 24 req/s average traffic volume reveals usage patterns, peak hours, and capacity headroom — attacker can time a coordinated drain to coincide with peak load.
- **Cache Intelligence**: 20.5B cache tokens/day = the fleet serves mostly cached completions with ~67% cache hit rate — reveals which queries/models are hot (attacker can craft cache-poisoning or cache-exhaustion attacks).
- **Credential Reuse**: `x-refresh-password` (different secret, also unthrottled) confirms a shared-secret credential model with no MFA and no rate limiting on ANY auth path.

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
