# Class lesson: re-read old negatives narrowly (2026-10-10) — mobile-api / federated

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-class-lesson-re-read-o.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

"SMS OTP dead" (verify path) coexisted with phone SIGNUP autoconfirm returning full sessions.
Negatives are scoped to the exact endpoint probed, not the feature family — enumerate sibling
endpoints (signup vs verify vs recover vs magiclink) before declaring an auth feature dead.
Also: email delivery may be broken server-side (signup confirm + email-change + recover all
silently dropped; verify with a healthy public-inbox API like Mailinator v2 as control).

## Probe adjustment (mobile-api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
