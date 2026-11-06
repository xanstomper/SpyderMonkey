# Request smuggling CL.TE / TE.CL differential — cloud / hardened

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-request-smuggling-cl-te-te-cl-d.md`
- bindings: **WSTG-ADV-02** · **CWE-444** · **ATT&CK T1190**
- context: **cloud** · auth **hardened** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Two conflicting-header probes with a timing/response-length delta — ONE probe pair, never a burst against a shared edge. Decisive test: the differential timeout/smuggled-response signature in the lab replica first (dojo has the replica).

## Probe adjustment (cloud × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
