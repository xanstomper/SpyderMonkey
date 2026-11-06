# WSTG Input Validation Testing (WSTG-INPT) — websocket / low-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-wstg-input-validation-testing-wstg.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **websocket** · auth **low-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: injection families — sql, ldap, xss, xxe, ssti, cmd, deserialization
- probe: the 14-marker INJECTION battery + 8-encoding traversal battery
- wall: reflected/evaluated markers only; never destructive payloads

## Probe adjustment (websocket × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
