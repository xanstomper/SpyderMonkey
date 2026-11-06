# Subprotocol/namespace confusion — cloud / machine

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-subprotocol-namespace-confusi.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- context: **cloud** · auth **machine** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`Sec-WebSocket-Protocol` and socket.io namespace gates answering when they should not. Decisive test: the anon namespace CONNECT ack (type-matched to the app) = the exposure class.

## Probe adjustment (cloud × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
