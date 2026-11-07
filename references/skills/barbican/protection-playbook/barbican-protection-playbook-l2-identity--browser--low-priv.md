# L2 — IDENTITY — browser / low-priv

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l2-identity.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **browser** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

| Audit | Synthesis |
|---|---|
| git user.email: personal = CRITICAL; noreply form = acceptable | engagement alias in posture; commits carry alias@users.noreply |
| username in file paths (reports, logs, JSON states) | sanitize rewrites /home/<user> → /home/<alias> |
| shell env markers (AI_AGENT, HERMES_AGENT) | engagement shells: `env -i bash -lc` |
| hostname strings in artifacts | sanitize rewrites to "op-host" |

## Probe adjustment (browser × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
