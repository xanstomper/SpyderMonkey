# 8.2 Helpdesk trust model (score 60, documentation only) — ci-cd / hardened

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-2-helpdesk-trust-m.md`
- bindings: **WSTG-ATHN-08** · **CWE-521** · **ATT&CK T1110**
- context: **ci-cd** · auth **hardened** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Public-facing support channels, documented identity-verification requirements (or their
  absence), password-reset-over-phone policy in public docs.
- Findings are PROSE ratings: "helpdesk reset requires account number only = MFA bypass
  exposure" — no contact is ever made.

## Probe adjustment (ci-cd × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
