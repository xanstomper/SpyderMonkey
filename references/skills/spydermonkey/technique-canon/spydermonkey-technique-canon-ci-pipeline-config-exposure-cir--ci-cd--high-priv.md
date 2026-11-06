# CI pipeline config exposure (.circleci/.github workflows) — ci-cd / high-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-ci-pipeline-config-exposure-cir.md`
- bindings: **WSTG-CONF-04** · **CWE-538** · **ATT&CK T1552**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Runner configs with secrets referenced (not values) map the secret inventory. Decisive test: workflow YAML naming secrets + the pull-request trigger surface = the supply-chain finding.

## Probe adjustment (ci-cd × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
