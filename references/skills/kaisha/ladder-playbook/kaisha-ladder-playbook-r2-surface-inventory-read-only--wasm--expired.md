# R2 — surface inventory (read-only) — wasm / expired

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-r2-surface-inventory-read-only.md`
- bindings: **MASTG-RES** · **CWE-798** · **ATT&CK T1552**
- context: **wasm** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- listening services: address:port + process name (own host)
- banners: exact strings → feed `kaisha cve --banner`

## Probe adjustment (wasm × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
