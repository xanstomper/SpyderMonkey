# Lockout-mechanism geometry — ci-cd / high-priv

- source canon: `spydermonkey/technique-canon-11.md`
- base technique: `spydermonkey-technique-canon-11-lockout-mechanism-geometry.md`
- bindings: **WSTG-ATHN-08** · **CWE-521** · **ATT&CK T1110**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Wrong-password counters, lock TTL, and reset behavior mapped. Decisive test: 5+1 attempts measuring the geometry = the row (the arithmetic, not a crack).

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
