# Rate limits & rotation — ios / high-priv

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-rate-limits-rotation.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **ios** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Per-account ~6 req/min on media endpoints, but with phone_autoconfirm signup, rotation is trivial: mint fresh account on 429 (2s per account). Also retry "exhausted" upstream models on fresh accounts — some 429s are per-session.

## Probe adjustment (ios × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
