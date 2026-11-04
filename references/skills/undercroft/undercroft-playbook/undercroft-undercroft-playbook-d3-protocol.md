# D3 — PROTOCOL

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
