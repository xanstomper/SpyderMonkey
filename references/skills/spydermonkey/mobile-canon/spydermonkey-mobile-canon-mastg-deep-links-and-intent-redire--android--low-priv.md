# MASTG Deep Links and Intent Redirection (MASTG-PLATFORM-06) — android / low-priv

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-deep-links-and-intent-redire.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **android** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: hijackable deep links, intent passthrough
- probe: static link inventory; am-probe the lab app with crafted intents
- wall: lab device

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
