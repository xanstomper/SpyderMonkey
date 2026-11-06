# Class lesson: user_metadata persistence ≠ authorization — gcp / low-priv

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-class-lesson-user-meta.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gcp** · auth **low-priv** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Admin-claim injection into JWT `user_metadata` (role/is_admin/credits persist verbatim through
phone signup) is a finding only if a BACKEND endpoint trusts the claim. g***REDACTED***.xyz's backend
gates on its own DB (`profiles.email_verified` middleware on all /api/account/*) — dead end
despite full claim persistence. Locate the real gate before scoring JWT-claim escalation.

## Probe adjustment (gcp × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
