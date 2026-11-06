# R5 — Checkout/order state-machine bypass (e-commerce/booking) — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r5-checkout-order-state-machi.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. `undercroft stateflow --states "cart,paid,fulfilled,refunded" --guard "fulfilled:paid,refunded:paid" --flow checkout --target <c>`
2. Drive the generated matrix with your own orders: fire later transitions from
   earlier states (N+2 before N+1).
3. CONFIRMED when the flow lands in an undocumented state (e.g. refunded order
   that still fulfills, fulfilled without payment).
4. Reverse: cancel/void your own test orders. `craft` as STATE, `export`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
