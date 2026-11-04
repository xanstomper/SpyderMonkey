# R3 — Refund/fee drift via precision edges (fintech/e-commerce)

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

1. `undercroft precision --price <typical> --rate <fee> --ops 10000 --mode floor`
   → total drift + worst per-op amount.
2. On your own account: run the worst amount through the real refund/fee flow ×N.
3. Reconcile your statement vs the formula's exact total (`journal` seam).
4. CONFIRMED when real-world balance drifts in your favor beyond 1 smallest unit.
   Reverse: contact/void — nothing kept.
5. `craft` as MATH, `export`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
