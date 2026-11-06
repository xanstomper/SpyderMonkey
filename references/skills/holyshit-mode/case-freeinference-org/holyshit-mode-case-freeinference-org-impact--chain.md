# Impact — chain composition

- source canon: `holyshit-mode/case-freeinference-org.md`
- base technique: `holyshit-mode-case-freeinference-org-impact.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Operational Security**: Full infrastructure topology (exact GPU models, server layout, model versions) enables adversarial capacity planning — attacker can target the cheapest/easiest-to-exhaust node for bill-drain attacks.
- **Traffic Analysis**: 278k req/day = 24 req/s average traffic volume reveals usage patterns, peak hours, and capacity headroom — attacker can time a coordinated drain to coincide with peak load.
- **Cache Intelligence**: 20.5B cache tokens/day = the fleet serves mostly cached completions with ~67% cache hit rate — reveals which queries/models are hot (attacker can craft cache-poisoning or cache-exhaustion attacks).
- **Credential Reuse**: `x-refresh-password` (different secret, also unthrottled) confirms a shared-secret credential model with no MFA and no rate limiting on ANY auth path.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
