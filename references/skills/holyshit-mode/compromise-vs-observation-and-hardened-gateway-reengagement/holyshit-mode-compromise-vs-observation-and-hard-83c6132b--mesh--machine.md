# Why this matters — mesh / machine

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- base technique: `holyshit-mode-compromise-vs-observation-and-hardened-gateway.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mesh** · auth **machine** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

A target with 21 "confirmed" ledger entries can still have ZERO compromisable findings.
Prior sessions milked a hardened gateway for read-only observations (served_by model
substitution, CoT leak, system-prompt reconstruction, supply-chain hostnames) and scored
them high. Those are NOT compromises — an attacker gains no control, no data, no
availability damage. When the operator asks for "real compromisable holy shits," re-set the
bar BEFORE probing: the finding must answer **"what does the attacker actually GAIN / DAMAGE?"**

Classify EVERY candidate as:
- **COMPROMISE** — attacker achieves control (RCE, auth bypass, stored XSS in trusted UI),
  data exfil (cross-user content, secrets, sessions), or availability/financial damage to the
  operator's OWN assets (credit/CPU drain).
- **OBSERVATION** — attacker learns info but gains nothing usable (served_by, CoT leak,
  hidden-model map, upstream hostnames, prompt reconstruction). Recon coverage, NOT a finding.
- **RISK (already-defined)** — unauthenticated unlimited free-AI is a COMPROMISE when it
  bleeds the OPERATOR's paid third-party upstream credits (financial + availability DoS of
  operator's own service), even though it's "just" resource abuse. Sometimes the highest
  true compromise.

## Probe adjustment (mesh × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
