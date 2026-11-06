# Deliverable shape (breach-context) — web-app / machine

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-deliverable-shape-b.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **machine** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- The rebuttal package: documented scheme + captured chain + the one-line reproduction
  anyone can run.
- The honest caveats: forced-path capability, own-curve derivation, any authed-UI-only
  channel (state it as the single session-gated test left).
- The privacy leak trio + the fix rule, so the next breach narrative loses its legs.

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
