# D1 — CUSTOM-CODE

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

| Seam | How to read it | Confirmed-when |
|---|---|---|
| authn bypass | session construction, token verify order, admin flags in payloads | one unprivileged request authenticated as privileged |
| authz | route guards, tenant filters, org-id in body/params | one cross-tenant/cross-role read 200 |
| crypto | own crypto, key reuse, ECB/malleable modes, magic bytes in JWT alg | one forged/decoded proof read |
| injection | raw concat into query/exec/template (runtime-expanded) | one harmless probe reflected/executed (read-only) |
| trust boundary | client-validated totals, server-trusted fields in hidden inputs | one altered field accepted |

Source reads: declared repos, client bundles, JS payloads — always on-estate assets.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
