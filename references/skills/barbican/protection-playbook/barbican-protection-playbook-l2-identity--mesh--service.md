# L2 — IDENTITY — mesh / service

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l2-identity.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mesh** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

| Audit | Synthesis |
|---|---|
| git user.email: personal = CRITICAL; noreply form = acceptable | engagement alias in posture; commits carry alias@users.noreply |
| username in file paths (reports, logs, JSON states) | sanitize rewrites /home/<user> → /home/<alias> |
| shell env markers (AI_AGENT, HERMES_AGENT) | engagement shells: `env -i bash -lc` |
| hostname strings in artifacts | sanitize rewrites to "op-host" |

## Probe adjustment (mesh × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
