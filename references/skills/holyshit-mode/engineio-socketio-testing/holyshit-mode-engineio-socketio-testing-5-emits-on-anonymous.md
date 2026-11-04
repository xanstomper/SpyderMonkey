# 5. Emits on anonymous sockets

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- generated: 2026-11-04

## The technique

- Try socket events (`42/ns,["event",args]`) benign-first, gates LAST: many servers disconnect the namespace (`41`) on ANY unexpected emit, and the disconnect kills the rest of the probe queue.
- Receive-only anonymous sockets are a deliberate design on modern stacks — record as the fence, do not re-probe.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
