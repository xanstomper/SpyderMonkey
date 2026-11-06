# JWT kid path traversal and jku/x5u injection — ci-cd / machine

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-jwt-kid-path-traversal-and-jku-.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **ci-cd** · auth **machine** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`kid` is a file-path or SQL lookup in many libraries; `jku`/`x5u` let the token name its own key source. Decisive test: kid=<harmless traversal string> that flips the error class (signature error → file-not-found), and a jku pointing at YOUR registered domain serving a key — the 200-vs-400 delta is the proof. Never persist a forged trust chain.

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
