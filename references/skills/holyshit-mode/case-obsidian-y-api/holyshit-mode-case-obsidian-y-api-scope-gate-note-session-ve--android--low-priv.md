# Scope-gate note (session-verified) — android / low-priv

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- base technique: `holyshit-mode-case-obsidian-y-api-scope-gate-note-session-ve.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **android** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Operator first asked for "destructive level" holy shits on this third-party target → REFUSED (DoS/bill-drain = sabotage regardless of target openness). Operator clarified "just look for vectors" → proceeded read-only. Read-only oracle probing (a handful of summarization prompts) proved the cross-user leak without abusing it. "Free AI" findings are reported as a bill-drain RISK for the operator, never demonstrated by draining.

## Probe adjustment (android × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
