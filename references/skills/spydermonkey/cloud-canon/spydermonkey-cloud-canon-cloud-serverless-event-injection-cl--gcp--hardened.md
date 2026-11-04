# Cloud Serverless Event Injection (CLOUD-LAMBDA-01) — gcp / hardened

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-serverless-event-injection-cl.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **gcp** · auth **hardened** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- class: unsanitized event fields reaching the runtime
- probe: the INJECTION battery aimed at the documented event surface (lab functions)
- wall: lab functions only for live proof; prod is inventory-only

## Probe adjustment (gcp × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
