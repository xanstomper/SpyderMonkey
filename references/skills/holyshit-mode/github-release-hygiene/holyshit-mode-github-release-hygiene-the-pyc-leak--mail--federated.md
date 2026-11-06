# The `.pyc` Leak — mail / federated

- source canon: `holyshit-mode/github-release-hygiene.md`
- base technique: `holyshit-mode-github-release-hygiene-the-pyc-leak.md`
- bindings: **WSTG-CONF-04** · **CWE-538** · **ATT&CK T1552**
- context: **mail** · auth **federated** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`git add -A` silently commits `__pycache__/*.pyc` after any local run. The first release
of holyshit-mode shipped a `.pyc` before `.gitignore` existed; it was caught only because
`git ls-files` was manually checked post-push.

**Rule:** create `.gitignore` with `__pycache__/` + `*.pyc` BEFORE the first `git commit`.
If already committed: `git rm -r --cached scripts/__pycache__` then commit + push.

## Probe adjustment (mail × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
