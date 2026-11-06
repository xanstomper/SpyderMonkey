# R2 — Plan/seat-limit bypass via client-supplied scope ids (SaaS) — ci-cd / high-priv

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r2-plan-seat-limit-bypass-via.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. From the bundle, find the scope id the client sends (`scan` flags `org_id`/
   `tenant_id`/`workspace_id` in client calls).
2. On your own tenant at plan limit, send the upgrade/invite/seat request with a
   forged scope id in the BODY (server should read it from the session).
3. Decisive test: create limit+1 resources; count.
4. CONFIRMED when limit+1 exists. Reverse: delete the extra resources.
5. `craft` as IDOR (scope trust), `export`.

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
