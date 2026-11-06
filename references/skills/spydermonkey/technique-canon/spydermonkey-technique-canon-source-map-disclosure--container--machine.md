# Source-map disclosure — container / machine

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-source-map-disclosure.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- context: **container** · auth **machine** · chain role **final**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

.map files ship original source to anyone. Decisive test: GET /app.js.map → 200 JSON with sources — the finding; original code with secrets in comments = the crown.

## Probe adjustment (container × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
