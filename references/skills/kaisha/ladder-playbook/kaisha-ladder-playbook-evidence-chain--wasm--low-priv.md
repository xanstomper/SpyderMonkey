# Evidence chain — wasm / low-priv

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-evidence-chain.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **wasm** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Every rung: `SOURCE (confirmed access) → RUNG (id/class) → TEST (exact) →
PROOF (NO-GAIN shape) → STATUS`. A rung without a test is a guess; a proof
without a rung is a fabrication. Drift: re-verify rungs older than the window
before citing.

## Probe adjustment (wasm × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
