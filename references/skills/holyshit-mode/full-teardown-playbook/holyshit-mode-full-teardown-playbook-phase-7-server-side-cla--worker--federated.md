# PHASE 7 — SERVER-SIDE CLASS PROBES (scoped, minimal) — worker / federated

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-7-server-side-cla.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **worker** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- SQLi class: error-based + boolean oracle on clearly-input-reflected params first.
- SSRF: webhook/URL-import features → internal addresses (169.254.169.254 metadata =
  HOLY SHIT: cloud creds).
- XXE/SSRF in document processors; deserialization in session/upload paths.
- Upload handling: content-type/type-confusion, path traversal in filenames.
- Template injection in mail/report generators.
- Discipline: one probe per class on the most-likely param, escalate only on signal.

## Probe adjustment (worker × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
