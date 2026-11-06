# MASTG Cleartext Traffic (MASTG-NETWORK-01) — android / unauth

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-cleartext-traffic-mastg-netw.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **android** · auth **unauth** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: http / mixed-content on the mobile client
- probe: mitm on the lab proxy; inventory every cleartext request
- wall: lab proxy; the app under scope only

## Probe adjustment (android × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
