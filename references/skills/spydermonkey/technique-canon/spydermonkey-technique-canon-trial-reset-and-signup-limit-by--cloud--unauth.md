# Trial reset and signup-limit bypass — cloud / unauth

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-trial-reset-and-signup-limit-by.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **cloud** · auth **unauth** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Trial entitlement tied to a client-controllable identity fragment (device id, email alias) is a logic seam. Decisive test: second trial via email+1 alias on your OWN address — entitlement granted = the finding (the abuse class, not the grant).

## Probe adjustment (cloud × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
