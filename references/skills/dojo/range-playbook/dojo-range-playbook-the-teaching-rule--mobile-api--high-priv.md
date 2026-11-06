# The teaching rule — mobile-api / high-priv

- source canon: `dojo/range-playbook.md`
- base technique: `dojo-range-playbook-the-teaching-rule.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1550**
- context: **mobile-api** · auth **high-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

A class is LEARNED only when: probe confirms + kairo classifies + kage mirrors.
Until then it is a build, not a lesson.

## Probe adjustment (mobile-api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
