# R1 — Webhook replay → duplicate effect (payments/integrations) — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r1-webhook-replay-duplicate-e.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Trigger ONE legitimate event on your own account (e.g. a test payment/callback).
2. Capture the outbound callback the platform sent your endpoint (request log,
   webhook debugger, or your own receiver log): full method+headers+body.
3. `undercroft replay --url <your-endpoint> --method POST --header "X-Sig: <as captured>" --body '<captured>' --times 3 --confirm`
4. Check: one effect or N? (order created once vs N; ledger entry duplicated).
5. CONFIRMED when the platform's own dedup key fails to gate the replay. Reverse:
   refund/delete the duplicates immediately (NO-GAIN).
6. `craft` as STATE; `export` → 3AM.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
