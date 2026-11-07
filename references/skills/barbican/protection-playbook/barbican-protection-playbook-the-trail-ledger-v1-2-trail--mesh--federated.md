# The trail ledger (v1.2 — `trail`) — mesh / federated

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-trail-ledger-v1-2-trail.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **mesh** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Row format: `provider :: purpose` (+ timestamp). Rules:
1. Engagement traffic touches ONLY sanctioned providers — personal accounts are a
   HIGH flag and the scan prints it in the row.
2. The trail is the engagement's upstream map: if a provider must be named in a
   disclosure later, the trail already knows.
3. `check --target T` surfaces the trail — a pre-flight that can't say which
   providers the engagement touches isn't a pre-flight.

## Probe adjustment (mesh × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
