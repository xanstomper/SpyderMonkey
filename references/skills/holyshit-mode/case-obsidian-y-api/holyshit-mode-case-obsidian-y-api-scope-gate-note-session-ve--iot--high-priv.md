# Scope-gate note (session-verified) — iot / high-priv

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- base technique: `holyshit-mode-case-obsidian-y-api-scope-gate-note-session-ve.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **iot** · auth **high-priv** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Operator first asked for "destructive level" holy shits on this third-party target → REFUSED (DoS/bill-drain = sabotage regardless of target openness). Operator clarified "just look for vectors" → proceeded read-only. Read-only oracle probing (a handful of summarization prompts) proved the cross-user leak without abusing it. "Free AI" findings are reported as a bill-drain RISK for the operator, never demonstrated by draining.

## Probe adjustment (iot × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
