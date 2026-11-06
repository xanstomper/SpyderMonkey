# harakirimail public-inbox chain (mailinator blocked here) — kubernetes / hardened

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-harakirimail-public-inbox-chain.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **hardened** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- List: `GET https://harakirimail.com/api/v1/inbox/<name>` (metadata only).
- Full body: `GET https://harakirimail.com/api/v1/email/<_id>` (`bodyhtmltext`).
- Extract `token=([a-f0-9]{40,})` from the confirm link; consume ONCE.
- Confirm: `GET /auth/v1/verify?token=...&type=signup&email=...` → 303 with
  `#access_token` fragment. Take a stable session via password grant afterward.
- Bonus leak: the confirm email's `redirect_to` exposed the Lovable mirror host.

## Probe adjustment (kubernetes × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
