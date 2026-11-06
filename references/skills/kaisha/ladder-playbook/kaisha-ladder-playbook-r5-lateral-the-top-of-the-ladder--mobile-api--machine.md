# R5 — lateral (the top of the ladder) — mobile-api / machine

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-r5-lateral-the-top-of-the-ladder.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **machine** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Basis: the harvest register's CRED rows + documented reuse classes
  (flaw 10 entropy/forge · seam C auth<->backend-binding)
- The plan: `from → to` on OWN declared hosts only; ONE validation shot each,
  reversed; on CONFIRM the new vantage feeds shukaku (reason → hunt → crown).

## Probe adjustment (mobile-api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
