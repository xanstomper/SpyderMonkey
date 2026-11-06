# Concurrent-session and piggyback policy — firmware / unauth

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-concurrent-session-and-piggyb.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **firmware** · auth **unauth** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

No session revocation on password change / unlimited parallel sessions = replay-window classes. Decisive test: old session alive after rotation on YOUR accounts — the window is the finding.

## Probe adjustment (firmware × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
