# The timeline math (v1.2 — `timeline`) — cloud / federated

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-timeline-math-v1-2-timeline.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Bursts chunk at ≤25 requests (the family noise budget's atomic unit).
- Intra-burst gap: `--pause` (default 0.2s — matches undercroft's live pacing).
- Inter-burst pause: 1s (a burst boundary is a breath).
- Wall-clock = Σ(count × pause) + Σ(inter-burst gaps) — printed so the operator
  knows the engagement's tempo BEFORE it runs.
- The window: engagement pacing avoids the operator's routine hours (posture
  holds the window; the vantage's timezone is the opsec timezone).

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
