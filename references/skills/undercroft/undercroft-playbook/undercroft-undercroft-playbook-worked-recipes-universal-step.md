# Worked recipes (universal, step-by-step)

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

### R1 — Webhook replay → duplicate effect (payments/integrations)

1. Trigger ONE legitimate event on your own account (e.g. a test payment/callback).
2. Capture the outbound callback the platform sent your endpoint (request log,
   webhook debugger, or your own receiver log): full method+headers+body.
3. `undercroft replay --url <your-endpoint> --method POST --header "X-Sig: <as captured>" --body '<captured>' --times 3 --confirm`
4. Check: one effect or N? (order created once vs N; ledger entry duplicated).
5. CONFIRMED when the platform's own dedup key fails to gate the replay. Reverse:
   refund/delete the duplicates immediately (NO-GAIN).
6. `craft` as STATE; `export` → 3AM.

### R2 — Plan/seat-limit bypass via client-supplied scope ids (SaaS)

1. From the bundle, find the scope id the client sends (`scan` flags `org_id`/
   `tenant_id`/`workspace_id` in client calls).
2. On your own tenant at plan limit, send the upgrade/invite/seat request with a
   forged scope id in the BODY (server should read it from the session).
3. Decisive test: create limit+1 resources; count.
4. CONFIRMED when limit+1 exists. Reverse: delete the extra resources.
5. `craft` as IDOR (scope trust), `export`.

### R3 — Refund/fee drift via precision edges (fintech/e-commerce)

1. `undercroft precision --price <typical> --rate <fee> --ops 10000 --mode floor`
   → total drift + worst per-op amount.
2. On your own account: run the worst amount through the real refund/fee flow ×N.
3. Reconcile your statement vs the formula's exact total (`journal` seam).
4. CONFIRMED when real-world balance drifts in your favor beyond 1 smallest unit.
   Reverse: contact/void — nothing kept.
5. `craft` as MATH, `export`.

### R4 — Trial/TTL boundary crossing (SaaS/booking/anything time-gated)

1. Map the documented boundary: trial end, grace period, token TTL.
2. Fire the gated action at boundary−1s, boundary+1s (clock skew only on
   infrastructure you control).
3. CONFIRMED when expired-but-accepted (or pre-expiry grant) occurs.
4. Reverse: revert the granted state. `craft` as TIME, `export`.

### R5 — Checkout/order state-machine bypass (e-commerce/booking)

1. `undercroft stateflow --states "cart,paid,fulfilled,refunded" --guard "fulfilled:paid,refunded:paid" --flow checkout --target <c>`
2. Drive the generated matrix with your own orders: fire later transitions from
   earlier states (N+2 before N+1).
3. CONFIRMED when the flow lands in an undocumented state (e.g. refunded order
   that still fulfills, fulfilled without payment).
4. Reverse: cancel/void your own test orders. `craft` as STATE, `export`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
