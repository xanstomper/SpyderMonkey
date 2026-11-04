# 3. Chain-of-thought leak — `muse/muse-glimmer` (score 50)

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-04

## The technique

`reasoning_content` field on EVERY muse response carries full hidden CoT, even for trivial math
(17*23 → narrates the working). Also leaks speculative-decoding internals:
`timings: {cache_n, draft_n, draft_n_accepted, predicted_ms}` and a concrete
`system_fingerprint: b11382-11fe02151`. No user/system secrets in the CoT here, but it's a real
instruction/privacy leak channel and confirms model internals.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
