# R5 — Checkout/order state-machine bypass (e-commerce/booking) — web-app / high-priv

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r5-checkout-order-state-machi.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **high-priv** · chain role **final**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. `undercroft stateflow --states "cart,paid,fulfilled,refunded" --guard "fulfilled:paid,refunded:paid" --flow checkout --target <c>`
2. Drive the generated matrix with your own orders: fire later transitions from
   earlier states (N+2 before N+1).
3. CONFIRMED when the flow lands in an undocumented state (e.g. refunded order
   that still fulfills, fulfilled without payment).
4. Reverse: cancel/void your own test orders. `craft` as STATE, `export`.

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
