# Shared 36-byte header (all kinds) — web-app / machine

- source canon: `holyshit-mode/iceposeidon-binary-map-protocol.md`
- base technique: `holyshit-mode-iceposeidon-binary-map-protocol-shared-36-byte.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- context: **web-app** · auth **machine** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| off | type | field |
|-----|------|-------|
| 0 | u8 | kind (1..8) |
| 1 | u8 | version = 1 |
| 2 | u16 LE | flags: 1=full, 1|2=clear, 4=sparse |
| 4 | u32 | generation (>0) |
| 8 | u32 | sequence (>0) |
| 12 | f64 | eventRevision |
| 20 | f64 | sampledAt (epoch ms, must be multiple of 100) |
| 28 | u16 | partIndex |
| 30 | u16 | partCount (1..256) |
| 32 | u16 | recordCount |
| 34 | u16 | reserved (must be 0) |

Sparse/clear semantics: sparse = patch upserts (recordCount>0), clear = empty replacement (recordCount=0, len==36).

## Probe adjustment (web-app × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
