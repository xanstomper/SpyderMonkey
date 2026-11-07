# Attack Surface Mapped (Not Exploited) — graphql / hardened

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-attack-surface-mapped-not-expl.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **graphql** · auth **hardened** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- **IDOR on DSAR:** `/v1/me/data`, `/v1/me/delete` — need valid session
- **SSO confusion:** Race condition on `/v1/sso/approve` + `/v1/sso/token` — need valid session
- **Post-auth injection:** Stored XSS, CSRF — need valid session
- **Rate limit bypass:** `X-Forwarded-For` spoofing — not tested
- **Premium model access:** Tier 1 models require auth — no bypass found

## Probe adjustment (graphql × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
