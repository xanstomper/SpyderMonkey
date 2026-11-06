# Leak claims: row-level correlation or it isn't a finding — container / unauth

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-leak-claims-row-level-correlatio.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Counting `"display_username"` fields does NOT prove a masking failure — a feed full of
visible users also contains that field. The decisive test: find rows where the masked
field (`username == "Hidden user"`) appears, then check the SAME row's `display_username`
for a real value. Report `masked occurrences → correlated rows → unique userIds`. Only the
correlated count is the leak; the rest is noise. Same discipline as the 3-gate: a diff
needs the baseline and the attack joined on the same object.

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
