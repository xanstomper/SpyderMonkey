# CAPTCHA-gate anatomy (the Fastly _fs-ch class family) — kubernetes / unauth

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-captcha-gate-anatomy-the-fast.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **kubernetes** · auth **unauth** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

The challenge SVG/logo-strip is NOT the captcha — the form-adjacent JPEG is (engagement-ops). Decisive test: challenge-object inventory on the live edge — the anatomy map is the finding; solving is NOT attempted (the wall).

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
