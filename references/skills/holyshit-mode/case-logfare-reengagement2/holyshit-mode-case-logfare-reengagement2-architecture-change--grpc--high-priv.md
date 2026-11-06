# Architecture change since 2026-10-03 baseline — grpc / high-priv

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-architecture-change.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **high-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Main host is now server-rendered (no SPA bundle); auth moved to cookie sessions; signup gained a
**Discord-membership gate** ("Verify that you are in the Logfare Discord server") — the old
no-email signup is gone. `/migrate` flow for existing accounts.

## Probe adjustment (grpc × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
