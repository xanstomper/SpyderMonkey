# R2 — Plan/seat-limit bypass via client-supplied scope ids (SaaS) — ci-cd / low-priv

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r2-plan-seat-limit-bypass-via.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

1. From the bundle, find the scope id the client sends (`scan` flags `org_id`/
   `tenant_id`/`workspace_id` in client calls).
2. On your own tenant at plan limit, send the upgrade/invite/seat request with a
   forged scope id in the BODY (server should read it from the session).
3. Decisive test: create limit+1 resources; count.
4. CONFIRMED when limit+1 exists. Reverse: delete the extra resources.
5. `craft` as IDOR (scope trust), `export`.

## Probe adjustment (ci-cd × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
