# MSSQL xp/error channel and stacked-query detection — container / unauth

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-mssql-xp-error-channel-and-st.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

`CONVERT` errors and batched `;WAITFOR DELAY` acceptance differ per driver. Decisive test: error reflection first; stacked-query acceptance only if the driver evidence suggests it (one probe).

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
