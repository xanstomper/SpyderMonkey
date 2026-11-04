# R3 — Refund/fee drift via precision edges (fintech/e-commerce) — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r3-refund-fee-drift-via-preci.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. `undercroft precision --price <typical> --rate <fee> --ops 10000 --mode floor`
   → total drift + worst per-op amount.
2. On your own account: run the worst amount through the real refund/fee flow ×N.
3. Reconcile your statement vs the formula's exact total (`journal` seam).
4. CONFIRMED when real-world balance drifts in your favor beyond 1 smallest unit.
   Reverse: contact/void — nothing kept.
5. `craft` as MATH, `export`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
