# D3 — PROTOCOL — cloud / machine

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d3-protocol.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **cloud** · auth **machine** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Class (documented) | Crafted input (Δ) | Confirmed-when |
|---|---|---|
| parsing ambiguity | double-encoded/overlapping tokens in declared formats | server consumes two meanings |
| deserialization class | type-confused field in declared schema | unexpected object/error path |
| length/precision | boundary ints, negative/NaN, max-precision floats | divergent handling |
| split/merge race | concurrent chunked submits on the same logical unit | duplicate/desync accepted |
| state machine | out-of-order transitions on declared flows | illegal-but-accepted state |

Δ must state the class + the modification. Never craft for unknown parser internals
beyond observed behavior (black-box adaptation stays within documented classes).

## Probe adjustment (cloud × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
