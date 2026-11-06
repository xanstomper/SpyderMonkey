# .NET ObjectStateFormatter / ViewState — container / high-priv

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-net-objectstateformatter-view.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **high-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

MAC-enabled vs legacy ViewState — the `__VIEWSTATE` parameter with tamper acceptance is the class. Decisive test: modified viewstate → distinct MAC error vs acceptance (acceptance = crown; never execute the gadget).

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
