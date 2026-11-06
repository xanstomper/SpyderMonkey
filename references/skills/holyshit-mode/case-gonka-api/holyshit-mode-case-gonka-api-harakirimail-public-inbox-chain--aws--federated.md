# harakirimail public-inbox chain (mailinator blocked here) — aws / federated

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-harakirimail-public-inbox-chain.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **aws** · auth **federated** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- List: `GET https://harakirimail.com/api/v1/inbox/<name>` (metadata only).
- Full body: `GET https://harakirimail.com/api/v1/email/<_id>` (`bodyhtmltext`).
- Extract `token=([a-f0-9]{40,})` from the confirm link; consume ONCE.
- Confirm: `GET /auth/v1/verify?token=...&type=signup&email=...` → 303 with
  `#access_token` fragment. Take a stable session via password grant afterward.
- Bonus leak: the confirm email's `redirect_to` exposed the Lovable mirror host.

## Probe adjustment (aws × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
