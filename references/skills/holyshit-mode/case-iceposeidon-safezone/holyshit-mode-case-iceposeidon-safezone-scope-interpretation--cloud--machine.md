# Scope interpretation — gaming context (recorded for reuse) — cloud / machine

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-scope-interpretation.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **cloud** · auth **machine** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Buying a nuke with faucet-farmed Cx Bucks and dropping it via intended checkout→launch = playing the game as designed = IN scope (it's the product).
- Forging/replaying delivery calls, multi-account claim farming, launch racing = griefing a live third-party event = OUT of scope (mandate: destructive end-states on third-party production). State the line once, pivot to the legit path.

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
