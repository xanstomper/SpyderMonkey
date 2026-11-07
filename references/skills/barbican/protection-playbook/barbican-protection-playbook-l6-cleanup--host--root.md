# L6 — CLEANUP — host / root

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l6-cleanup.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **host** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

| Audit | Synthesis |
|---|---|
| campaign dirs left full | `wipe --confirm` = campaign + posture removed; canon rows survive BY DESIGN |
| sim/test rows in canon | stripped same-session (family hygiene, formalized) |
| shell history carrying engagement commands | engagement shells: HISTFILE=/dev/null or clean-env shells |

## Probe adjustment (host × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
