# Evidence chain — cloud / high-priv

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-evidence-chain.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **cloud** · auth **high-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Every rung: `SOURCE (confirmed access) → RUNG (id/class) → TEST (exact) →
PROOF (NO-GAIN shape) → STATUS`. A rung without a test is a guess; a proof
without a rung is a fabrication. Drift: re-verify rungs older than the window
before citing.

## Probe adjustment (cloud × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
