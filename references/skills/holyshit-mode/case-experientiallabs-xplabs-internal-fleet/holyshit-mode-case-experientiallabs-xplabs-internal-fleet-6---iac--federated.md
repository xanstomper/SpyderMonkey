# 6. Lesson: operator-owned LLM-gateway engagements — where the findings actually live — iac / federated

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-6-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iac** · auth **federated** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

On a well-built reseller gateway, do NOT judge the whole estate by the hardened public edge.
The high-value compromisable class is almost always: **the hidden self-hosted serving fleet
(`experiential_cloud`-style lane) disclosed via the keyless catalog `base_url`**, whose
control-plane/inference-routes share the inference binary but skip the auth middleware. Sweep the
internal hosts for `/openapi.json`, `/invocations`, `/scale_elastic_ep`, `/usage.json`, and
validate auth-asymmetry by contrast (same-route 401 on a sibling host = the finding is real).
Full ledger recorded at `~/.hermes/scripts/holyleadger/experientiallabs-ai.json` (12 confirmed).

## Probe adjustment (iac × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
