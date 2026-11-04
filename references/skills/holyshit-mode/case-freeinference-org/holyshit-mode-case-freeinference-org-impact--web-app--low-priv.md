# Impact — web-app / low-priv

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-impact.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **Operational Security**: Full infrastructure topology (exact GPU models, server layout, model versions) enables adversarial capacity planning — attacker can target the cheapest/easiest-to-exhaust node for bill-drain attacks.
- **Traffic Analysis**: 278k req/day = 24 req/s average traffic volume reveals usage patterns, peak hours, and capacity headroom — attacker can time a coordinated drain to coincide with peak load.
- **Cache Intelligence**: 20.5B cache tokens/day = the fleet serves mostly cached completions with ~67% cache hit rate — reveals which queries/models are hot (attacker can craft cache-poisoning or cache-exhaustion attacks).
- **Credential Reuse**: `x-refresh-password` (different secret, also unthrottled) confirms a shared-secret credential model with no MFA and no rate limiting on ANY auth path.

## Probe adjustment (web-app × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
