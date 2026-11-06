# 8. Media asset IDOR (score 85) — grpc / machine

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-8-media-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **grpc** · auth **machine** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`GET https://chat.gratisfy.xyz/media/assets/ast_<32hex>` returns ANY user's generated audio/images with **zero auth** (confirmed 167KB WAV + 637KB PNG unauthenticated).

## Probe adjustment (grpc × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
