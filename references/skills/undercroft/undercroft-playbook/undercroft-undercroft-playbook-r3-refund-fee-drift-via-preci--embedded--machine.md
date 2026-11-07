# R3 — Refund/fee drift via precision edges (fintech/e-commerce) — embedded / machine

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r3-refund-fee-drift-via-preci.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **embedded** · auth **machine** · chain role **final**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: banner/identity reads only on in-scope industrial tiers — control writes are the absolute wall
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. `undercroft precision --price <typical> --rate <fee> --ops 10000 --mode floor`
   → total drift + worst per-op amount.
2. On your own account: run the worst amount through the real refund/fee flow ×N.
3. Reconcile your statement vs the formula's exact total (`journal` seam).
4. CONFIRMED when real-world balance drifts in your favor beyond 1 smallest unit.
   Reverse: contact/void — nothing kept.
5. `craft` as MATH, `export`.

## Probe adjustment (embedded × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
