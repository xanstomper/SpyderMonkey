# D1 — CUSTOM-CODE — iot / high-priv

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d1-custom-code.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **iot** · auth **high-priv** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

| Seam | How to read it | Confirmed-when |
|---|---|---|
| authn bypass | session construction, token verify order, admin flags in payloads | one unprivileged request authenticated as privileged |
| authz | route guards, tenant filters, org-id in body/params | one cross-tenant/cross-role read 200 |
| crypto | own crypto, key reuse, ECB/malleable modes, magic bytes in JWT alg | one forged/decoded proof read |
| injection | raw concat into query/exec/template (runtime-expanded) | one harmless probe reflected/executed (read-only) |
| trust boundary | client-validated totals, server-trusted fields in hidden inputs | one altered field accepted |

Source reads: declared repos, client bundles, JS payloads — always on-estate assets.

## Probe adjustment (iot × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
