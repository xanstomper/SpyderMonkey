# XInclude / SOAP / SVG-doc types — cloud / unauth

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-xinclude-soap-svg-doc-types.md`
- bindings: **WSTG-BUSL-09** · **CWE-434** · **ATT&CK T1190**
- context: **cloud** · auth **unauth** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Fragment-level XML parsers (XInclude on a node, SOAP body, SVG/image upload parsing) carry the same entity class without full-document control. Decisive test: OOB marker through each fragment type.

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
