# 9.3 Forensics cascade (score 70) — external / machine

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- base technique: `3am-shinjitsu-arsenal-09-breach-osint-9-3-forensics-cascade-.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- context: **external** · auth **machine** · chain role **pivot**

## Context

- platform: passive-first; the dossier feeds everything downstream
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Wire → aggregators → forensic blogs: drain timelines, attacker/consolidation addresses,
  mixer flows, chaser dust.
- "No post-mortem published" + rushed rebuilt stack = HIGHEST-priority live brief: root cause
  possibly unfixed; focus the whole engagement on the rebuilt surface.

## Probe adjustment (external × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
