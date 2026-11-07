# Impact

- source canon: `holyshit-mode/case-freeinference-org.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- **Operational Security**: Full infrastructure topology (exact GPU models, server layout, model versions) enables adversarial capacity planning — attacker can target the cheapest/easiest-to-exhaust node for bill-drain attacks.
- **Traffic Analysis**: 278k req/day = 24 req/s average traffic volume reveals usage patterns, peak hours, and capacity headroom — attacker can time a coordinated drain to coincide with peak load.
- **Cache Intelligence**: 20.5B cache tokens/day = the fleet serves mostly cached completions with ~67% cache hit rate — reveals which queries/models are hot (attacker can craft cache-poisoning or cache-exhaustion attacks).
- **Credential Reuse**: `x-refresh-password` (different secret, also unthrottled) confirms a shared-secret credential model with no MFA and no rate limiting on ANY auth path.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
