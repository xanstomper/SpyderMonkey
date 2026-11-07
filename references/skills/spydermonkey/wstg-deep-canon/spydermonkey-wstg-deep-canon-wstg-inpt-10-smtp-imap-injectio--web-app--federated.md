# WSTG-INPT-10 SMTP/IMAP Injection — web-app / federated

- source canon: `spydermonkey/wstg-deep-canon.md`
- base technique: `spydermonkey-wstg-deep-canon-wstg-inpt-10-smtp-imap-injectio.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **web-app** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: header injection into mail flows
- probe: CRLF markers in the lab replica's mailer form
- wall: lab replica; no real mail is ever sent

## Probe adjustment (web-app × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
