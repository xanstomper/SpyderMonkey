# SSTI detection arithmetic (jinja/smarty/twig) — cloud / hardened

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-ssti-detection-arithmetic-jinja.md`
- bindings: **WSTG-INPV** · **CWE-1336** · **ATT&CK T1059**
- context: **cloud** · auth **hardened** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

{{7*7}} → 49 is the arithmetic marker; engine fingerprint follows ({{7*'7'}} → 7777777 = jinja2). Decisive test: the arithmetic marker reflected — class confirmed; template execution beyond arithmetic is RCE-class and is REPORTED, not executed (no-gain).

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
