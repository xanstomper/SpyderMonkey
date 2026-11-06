# Origin-lock matrix (cookie-auth endpoints) — grpc / unauth

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-origin-lock-matrix-cook.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **unauth** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

For each POST endpoint, fire: attacker Origin, `Origin: null`, and NO Origin — all should 403.

## Probe adjustment (grpc × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
