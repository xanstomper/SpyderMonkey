# Persistence Boot or Logon Autostart (T1547) — container / machine

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-persistence-boot-or-logon-autostar.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **container** · auth **machine** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- class: run-key/systemd/launchd autostart for durability
- probe: read-only enumeration of autostart locations on in-scope hosts
- wall: read-only; the finding is the exposure, not a planted hook

## Probe adjustment (container × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
