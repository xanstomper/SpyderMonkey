# D1 — CUSTOM-CODE — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d1-custom-code.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Seam | How to read it | Confirmed-when |
|---|---|---|
| authn bypass | session construction, token verify order, admin flags in payloads | one unprivileged request authenticated as privileged |
| authz | route guards, tenant filters, org-id in body/params | one cross-tenant/cross-role read 200 |
| crypto | own crypto, key reuse, ECB/malleable modes, magic bytes in JWT alg | one forged/decoded proof read |
| injection | raw concat into query/exec/template (runtime-expanded) | one harmless probe reflected/executed (read-only) |
| trust boundary | client-validated totals, server-trusted fields in hidden inputs | one altered field accepted |

Source reads: declared repos, client bundles, JS payloads — always on-estate assets.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
