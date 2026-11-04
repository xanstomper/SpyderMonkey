# 5. Emits on anonymous sockets — mobile / unauth

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-5-emits-on-anonymous.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- context: **mobile** · auth **unauth** · chain role **pivot**

## Context

- platform: family probes cover the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Try socket events (`42/ns,["event",args]`) benign-first, gates LAST: many servers disconnect the namespace (`41`) on ANY unexpected emit, and the disconnect kills the rest of the probe queue.
- Receive-only anonymous sockets are a deliberate design on modern stacks — record as the fence, do not re-probe.

## Probe adjustment (mobile × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
