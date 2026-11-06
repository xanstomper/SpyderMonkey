# Global constants — dns / machine

- source canon: `holyshit-mode/i***REDACTED***-binary-map-protocol.md`
- base technique: `holyshit-mode-i***REDACTED***-binary-map-protocol-global-constan.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **dns** · auth **machine** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`bt=36` header size; `$r=1e7` generic coord grid; `Re=1e5` contestant-fix coord scale; coord validation `X(v,isLat,scale)` = v/scale, abs<=90 lat / 180 lng. Health status enum `Yi = [disabled, paused, inside, outside, unavailable, eliminated]`.

## Probe adjustment (dns × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
