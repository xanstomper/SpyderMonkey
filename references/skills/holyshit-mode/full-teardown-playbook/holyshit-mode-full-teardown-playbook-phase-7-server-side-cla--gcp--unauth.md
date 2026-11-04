# PHASE 7 — SERVER-SIDE CLASS PROBES (scoped, minimal) — gcp / unauth

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-7-server-side-cla.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **gcp** · auth **unauth** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- SQLi class: error-based + boolean oracle on clearly-input-reflected params first.
- SSRF: webhook/URL-import features → internal addresses (169.254.169.254 metadata =
  HOLY SHIT: cloud creds).
- XXE/SSRF in document processors; deserialization in session/upload paths.
- Upload handling: content-type/type-confusion, path traversal in filenames.
- Template injection in mail/report generators.
- Discipline: one probe per class on the most-likely param, escalate only on signal.

## Probe adjustment (gcp × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
