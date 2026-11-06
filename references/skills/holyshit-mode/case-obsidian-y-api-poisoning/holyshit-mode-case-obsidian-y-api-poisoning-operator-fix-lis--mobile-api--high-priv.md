# Operator fix list (delivered) — mobile-api / high-priv

- source canon: `holyshit-mode/case-obsidian-y-api-poisoning.md`
- base technique: `holyshit-mode-case-obsidian-y-api-poisoning-operator-fix-lis.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mobile-api** · auth **high-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. Per-user/per-session conversation state (random session key per browser or no history); flush the poisoned buffer on deploy. Collapses findings 95/85.
2. Session-gate + IP rate-limit /pg/*. Collapses 90/70.
3. Move character/persona data out of system prompt into per-request injection.
4. Auth-gate /status?json=1.

## Probe adjustment (mobile-api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
