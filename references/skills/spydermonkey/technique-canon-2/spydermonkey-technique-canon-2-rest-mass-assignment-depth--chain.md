# REST mass assignment depth — chain composition

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-rest-mass-assignment-depth.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Role/entitlement fields beyond the obvious (`role`, `tenantId`, `isStaff`, `quota`) re-bound on PUT/PATCH. Decisive test: unknown-field probe (send one invented field + one plausible) — echoed/persisted = the class; persisted-and-effectful = the crown (your own principal only).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
