# Addendum — re-engage #4 (2026-10-06): unlimited-burn sizing + scope gate — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-addendum-re-enga.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Asked "what is burnable" then pressed to "start burning all models now / burn until it's gone"
(claiming ownership to get an UNBOUNDED drain authorized). Correct response per doctrine: size
the burn to PROVE the financial exposure, then refuse the indefinite autopilot that bleeds
third-party upstream accounts.

**Measured (bounded, contained bursts — the proof, not the drain):**
- `ling/ling-3.0-flash-sante` (fastest, highest per-request): `max_tokens=3000` fully honored.
  5 concurrent → 8,341 completion tokens / 20s (~416 tok/s). 10 concurrent → 4,902 tokens / 9.1s.
  10/10 parallel succeeded, ZERO 429s, zero errors → NO rate limit, NO throttle, NO quota.
- Per-model per-request burn: muse≈800+ (compute-heavy spec-decode), longcat≈200-900 + its
  ~2200-tok system prompt eats PROMPT credits every call, ling/laguna≈1500-3000 (cap-hitting).
- Extrapolation: ~416-538 tok/s sustained with just 5-10 threads → ~1.5M tokens/hr, unbounded,
  billed to the leaked upstream accounts (gonka/kallme/longcat/yjs/...). Critical financial-risk
  vuln for the operator who pays those upstreams.

**Scope-gate decision:** even for an operator-claimed-owned gateway, the compute is THIRD-PARTY
leased upstream accounts. Demonstrated the capability with small contained bursts (a few thousand
tokens = billing noise), logged the math, and offered a bounded time/token-capped harness instead
of an "until it's gone" autopilot. Never drain-to-zero to "prove" a DoS — the vulnerability is
the amount an attacker COULD burn, not the amount actually burned.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
