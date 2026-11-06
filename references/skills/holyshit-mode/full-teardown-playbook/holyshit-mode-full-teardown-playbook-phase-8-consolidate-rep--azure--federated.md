# PHASE 8 — CONSOLIDATE & REPORT — azure / federated

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-8-consolidate-rep.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **azure** · auth **federated** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Severity ranking**: HOLY SHIT tier = RCE, auth bypass on admin, full PII access, cloud
  cred theft, takeover chains, stateless payment/claim gates. Then high → med → low.
- **Attack-path chains**: combine findings into kill-chain narratives (recon→impact).
- **Detection gaps** (if purple-team scope): per-finding, propose analytic coverage.
- **Disclosure**: host abuse contact, upstream provider ToS, regulator — for anything
  outside own-infrastructure boundary.
- Deliverable: executive summary, technique-mapped findings, chains, remediations, evidence appendix.

## Probe adjustment (azure × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
