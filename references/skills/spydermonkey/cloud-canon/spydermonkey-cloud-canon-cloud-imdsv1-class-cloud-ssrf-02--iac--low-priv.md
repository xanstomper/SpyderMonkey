# Cloud IMDSv1 Class (CLOUD-SSRF-02) — iac / low-priv

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-imdsv1-class-cloud-ssrf-02.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **iac** · auth **low-priv** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: token-less metadata negotiation — the SSRF metadata marker answers
- probe: the SSRF differential against the in-scope app's fetch surface
- wall: proof-of-class only

## Probe adjustment (iac × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
