# Score discipline — edge / unauth

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-score-discipline.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **edge** · auth **unauth** · chain role **pivot**

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Confirmed-when must be stateable in one line BEFORE running — if it isn't, the probe
  is not decisive, re-derive.
- Every row, run or not, ends in the exhaustion ledger with its exact test string.
- A synthesized probe that succeeds gets OP-ESCALATE treatment immediately (hunt the
  consumer) — a confirmed primitive without a consumer hunt is a half-finished chain.

## Probe adjustment (edge × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
