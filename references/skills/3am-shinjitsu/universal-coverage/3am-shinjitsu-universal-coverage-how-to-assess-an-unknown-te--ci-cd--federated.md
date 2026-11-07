# How to assess an unknown technology — ci-cd / federated

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-how-to-assess-an-unknown-te.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ci-cd** · auth **federated** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Use this decision tree when the stack is unfamiliar:

1. **Identify the trust boundary.** Who calls it, with what authority, and what does it
   trust by default? (browser→server, service→service, tenant→control plane, device→cloud)
2. **Enumerate identities and secrets.** Humans, services, tokens, certificates, workloads,
   break-glass accounts. Stale and over-privileged identities are the universal failure.
3. **Map inputs to privileged actions.** Any field/header/message/event that changes
   authorization, routing, tenancy, billing, execution, or data access is a candidate.
4. **Check the negative space.** Missing verification, missing expiry, missing audience,
   missing tenant check, missing revocation, missing audit — not just implemented crypto.
5. **Verify read-only.** Prefer configuration review, logs, policy diffs, and one-request
   proofs. Never pivot from a finding into persistence, data extraction, or disruption.
6. **Ledger the exact test.** A negative without its exact procedure is not durable.

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
