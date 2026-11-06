# WASM module execution in-page — api / machine

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-wasm-module-execution-in-page.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **api** · auth **machine** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Signing modules as WASM executed in-page for the replication chain — the module's exported functions map is the finding (execution happens in YOUR browser session on the page's own code).

## Probe adjustment (api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
