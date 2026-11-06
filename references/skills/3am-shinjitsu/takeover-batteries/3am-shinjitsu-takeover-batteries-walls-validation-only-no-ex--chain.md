# Walls (validation-only, no exceptions) — chain composition

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-walls-validation-only-no-ex.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Persistence is NEVER installed. Proof = the path exists (auth success, capability
  check, one read). A "takeover" that requires installing an implant to prove is not
  a takeover — it's an observation plus a plan; ship the plan.
- No destructive end-states, no data movement, no lateral damage. LOTL one-command
  reads only.
- External dangling-domain registration and third-party tenant app-install are
  third-party actions — operator-owned records/tenants only; everything else ships
  as documented feasibility.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
