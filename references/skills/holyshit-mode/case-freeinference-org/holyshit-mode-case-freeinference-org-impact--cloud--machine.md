# Impact — cloud / machine

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-impact.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- **Operational Security**: Full infrastructure topology (exact GPU models, server layout, model versions) enables adversarial capacity planning — attacker can target the cheapest/easiest-to-exhaust node for bill-drain attacks.
- **Traffic Analysis**: 278k req/day = 24 req/s average traffic volume reveals usage patterns, peak hours, and capacity headroom — attacker can time a coordinated drain to coincide with peak load.
- **Cache Intelligence**: 20.5B cache tokens/day = the fleet serves mostly cached completions with ~67% cache hit rate — reveals which queries/models are hot (attacker can craft cache-poisoning or cache-exhaustion attacks).
- **Credential Reuse**: `x-refresh-password` (different secret, also unthrottled) confirms a shared-secret credential model with no MFA and no rate limiting on ANY auth path.

## Probe adjustment (cloud × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
