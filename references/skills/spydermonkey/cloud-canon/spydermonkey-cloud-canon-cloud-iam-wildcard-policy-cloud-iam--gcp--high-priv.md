# Cloud IAM Wildcard Policy (CLOUD-IAM-01) — gcp / high-priv

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-iam-wildcard-policy-cloud-iam.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **gcp** · auth **high-priv** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- class: `*` actions/resources in identity policies — the over-privileged principal
- probe: read-only policy inventory for every principal the scope declares
- wall: shukaku hunt semantics — inventory + pricing only, nothing assumed

## Probe adjustment (gcp × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
