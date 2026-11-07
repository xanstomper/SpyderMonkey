# D1 — CUSTOM-CODE — mesh / machine

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d1-custom-code.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **mesh** · auth **machine** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Seam | How to read it | Confirmed-when |
|---|---|---|
| authn bypass | session construction, token verify order, admin flags in payloads | one unprivileged request authenticated as privileged |
| authz | route guards, tenant filters, org-id in body/params | one cross-tenant/cross-role read 200 |
| crypto | own crypto, key reuse, ECB/malleable modes, magic bytes in JWT alg | one forged/decoded proof read |
| injection | raw concat into query/exec/template (runtime-expanded) | one harmless probe reflected/executed (read-only) |
| trust boundary | client-validated totals, server-trusted fields in hidden inputs | one altered field accepted |

Source reads: declared repos, client bundles, JS payloads — always on-estate assets.

## Probe adjustment (mesh × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
