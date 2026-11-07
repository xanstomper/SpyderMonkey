# PHASE 8 — CONSOLIDATE & REPORT — azure / service

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-8-consolidate-rep.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **azure** · auth **service** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- **Severity ranking**: HOLY SHIT tier = RCE, auth bypass on admin, full PII access, cloud
  cred theft, takeover chains, stateless payment/claim gates. Then high → med → low.
- **Attack-path chains**: combine findings into kill-chain narratives (recon→impact).
- **Detection gaps** (if purple-team scope): per-finding, propose analytic coverage.
- **Disclosure**: host abuse contact, upstream provider ToS, regulator — for anything
  outside own-infrastructure boundary.
- Deliverable: executive summary, technique-mapped findings, chains, remediations, evidence appendix.

## Probe adjustment (azure × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
