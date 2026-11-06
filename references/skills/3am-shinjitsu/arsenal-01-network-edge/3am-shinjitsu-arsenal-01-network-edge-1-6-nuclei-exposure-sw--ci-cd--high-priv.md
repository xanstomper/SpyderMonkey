# 1.6 Nuclei exposure sweep (score 70, T≈4min, ceiling 1 run) — ci-cd / high-priv

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-6-nuclei-exposure-sw.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- DECISIVE: `nuclei -u https://<target> -tags cve,exposure,panel -rl 10 -severity medium,high,critical -silent`
- RULE: one run, rate-limited. Never re-run without a target change (ledger).
- FP: template matches on CDN-edge paths — verify each match by hand before verdict.

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
