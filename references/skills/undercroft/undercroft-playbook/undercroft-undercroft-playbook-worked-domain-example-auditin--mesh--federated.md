# Worked domain example — auditing shipped odds math from client bundles (casino RTP audit) — mesh / federated

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-worked-domain-example-auditin.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **mesh** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. Extract game-config regions from the verifier/game chunks: search for
   `fairValueProduces|roundMultiplier|weights|slug:"` and pull ±12KB context.
2. Reconstruct the fair multiplier per outcome: `fair = 1/P(outcome)` where P comes
   from the shipped `weights` table (weights summing to 100 are percentages).
3. Verify every ladder rung against `rung(f) = edge × fair^floor` — a consistent
   constant across ALL difficulties/floors means the math is sound; a rung
   off-formula, or an inverted derivation for one mode, is the finding.
4. Check rounding direction on every printed value: flooring in the USER's favor
   at scale is a margin finding even when the formula is right.
5. If outcome derivation never ships client-side (server-only math), say so — the
   audit ends EXHAUSTED, not INCONCLUSIVE; the remaining test needs an account +
   browser vantage and is a parked decisive test, not a hole in the sweep.

The same method transfers to ANY shipped-math audit: pricing ladders, fee tables,
scoring formulas, rank/elo curves — reconstruct, verify against formula, check
rounding direction, park what needs a live vantage.

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
