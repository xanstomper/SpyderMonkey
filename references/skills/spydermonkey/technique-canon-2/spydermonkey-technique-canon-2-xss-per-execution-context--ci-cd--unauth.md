# XSS per-execution-context — ci-cd / unauth

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-xss-per-execution-context.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **ci-cd** · auth **unauth** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

HTML-body, attribute, JS-string, URL-attribute (`href`/`src` javascript:), and CSS contexts each need THEIR encoding-vocabulary variant. Decisive test: the reflected marker in the correct context form — context-specific execution in YOUR session is the proof; stored/cross-principal framing stays hypothesis without a second principal.

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
