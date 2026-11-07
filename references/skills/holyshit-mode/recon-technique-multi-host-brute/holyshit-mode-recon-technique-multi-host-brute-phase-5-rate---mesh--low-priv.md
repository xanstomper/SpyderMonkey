# Phase 5: Rate-Limit Probing (The Critical Gap) — mesh / low-priv

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-5-rate-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mesh** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `/api/dashboard` and `/api/export` return 401 on wrong password with **ZERO rate limiting**
- 20 rapid wrong-password attempts → all 401, zero 429
- Contrast: `/auth/signup` on main domain has working rate limiting (429 after 10 attempts)
- The rate-limit inconsistency between openinfra (unguarded) and example-target.org (guarded) is the vulnerability pattern

## Probe adjustment (mesh × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
