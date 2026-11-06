# The trail ledger (v1.2 — `trail`) — chain composition

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-trail-ledger-v1-2-trail.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Row format: `provider :: purpose` (+ timestamp). Rules:
1. Engagement traffic touches ONLY sanctioned providers — personal accounts are a
   HIGH flag and the scan prints it in the row.
2. The trail is the engagement's upstream map: if a provider must be named in a
   disclosure later, the trail already knows.
3. `check --target T` surfaces the trail — a pre-flight that can't say which
   providers the engagement touches isn't a pre-flight.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
