# 3. Chain-of-thought leak — `muse/muse-glimmer` (score 50) — web-app / machine

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-3-chain-of-thoug.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **web-app** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`reasoning_content` field on EVERY muse response carries full hidden CoT, even for trivial math
(17*23 → narrates the working). Also leaks speculative-decoding internals:
`timings: {cache_n, draft_n, draft_n_accepted, predicted_ms}` and a concrete
`system_fingerprint: b11382-11fe02151`. No user/system secrets in the CoT here, but it's a real
instruction/privacy leak channel and confirms model internals.

## Probe adjustment (web-app × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
