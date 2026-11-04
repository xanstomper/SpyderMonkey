# L6 — CLEANUP — websocket / high-priv

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l6-cleanup.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **websocket** · auth **high-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

| Audit | Synthesis |
|---|---|
| campaign dirs left full | `wipe --confirm` = campaign + posture removed; canon rows survive BY DESIGN |
| sim/test rows in canon | stripped same-session (family hygiene, formalized) |
| shell history carrying engagement commands | engagement shells: HISTFILE=/dev/null or clean-env shells |

## Probe adjustment (websocket × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
