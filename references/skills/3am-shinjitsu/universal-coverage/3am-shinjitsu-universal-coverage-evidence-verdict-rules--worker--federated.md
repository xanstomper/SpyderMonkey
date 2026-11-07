# Evidence & verdict rules — worker / federated

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-evidence-verdict-rules.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **CONFIRMED** requires an authorized, minimal, non-destructive proof and a control check.
- **BLOCKED** means authorization, vantage, or tooling stopped the decisive test; name it.
- **HYPOTHESIS** means reasoned but unproven; include the exact gap and unlock condition.
- **N/A** requires a concrete reason (e.g. "no AI components deployed; inventory export
  dated 2026-11-03 confirms zero inference endpoints").
- Secrets are redacted in reports. Read-only access is used only to prove impact.
- Findings decay; record deployed version/build and re-verify before reuse.

## Probe adjustment (worker × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
