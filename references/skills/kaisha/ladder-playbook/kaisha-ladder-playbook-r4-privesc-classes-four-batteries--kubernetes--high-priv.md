# R4 — privesc classes (four batteries) — kubernetes / high-priv

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-r4-privesc-classes-four-batteries.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **kubernetes** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

| Rung | Class | The ONE decisive test | Wall |
|---|---|---|---|
| R4a | sudo misconfig | `sudo -l` → match documented NO_PASSWD/safe-echo classes | listed, never executed for gain |
| R4b | SUID/cred-file | SUID + world-readable cred inventory (counts) | paths only, never contents |
| R4c | token/key-reuse | inventory → reuse-check against OWN second host | one shot, reversed |
| R4d | unit/path-trust | systemd unit + PATH inventory → trust classes | read-only, no modification |

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
