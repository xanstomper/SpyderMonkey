# IMDS classes (v1 vs v2) — container / high-priv

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-imds-classes-v1-vs-v2.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **container** · auth **high-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

IMDSv1 (tokenless GET) reachable via SSRF = the class; IMDSv2-required = mitigated negative (bank it). Decisive test: SSRF response carrying instance-id/iam-info, or the 401 token-gate — either is a ledger row.

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
