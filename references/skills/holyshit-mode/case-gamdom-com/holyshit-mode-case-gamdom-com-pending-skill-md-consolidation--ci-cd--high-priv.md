# Pending SKILL.md consolidation (blocked by the 100K limit) — ci-cd / high-priv

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-pending-skill-md-consolidation.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

SKILL.md is at 102.7K chars — over the limit, so no additions fit until trimmed. On the next
editing session: condense the case-duplicated lesson sections (gratisfy/logfare lessons,
directrouter lessons, playground-proxy, shared-context+poisoning, gonka disposable-email +
edge-function patterns — all have case files) to 3-5-line pointers (~18KB freed), then add:
recon items 17-22 (protocol-instance drift; EIO=3 websocket-first; field-alias masking gap;
schema-in-feed disclosure; entrance-link takeover audit; custom-panel recipe) + the cadence
bullet (bank findings immediately + scoreboard + re-run walls with a different mechanism before
re-stating them).

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
