# Scope interpretation — gaming context (recorded for reuse) — container / unauth

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-scope-interpretation.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Buying a nuke with faucet-farmed Cx Bucks and dropping it via intended checkout→launch = playing the game as designed = IN scope (it's the product).
- Forging/replaying delivery calls, multi-account claim farming, launch racing = griefing a live third-party event = OUT of scope (mandate: destructive end-states on third-party production). State the line once, pivot to the legit path.

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
