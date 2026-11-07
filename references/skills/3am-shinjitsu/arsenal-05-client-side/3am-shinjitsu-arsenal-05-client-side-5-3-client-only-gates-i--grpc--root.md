# 5.3 Client-only gates + ID backdoors (score 80) — grpc / root

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-3-client-only-gates-i.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **grpc** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- GREP every chunk: `user.id === <numeric literal>`, `is_admin`, `switchTab`, `can_*`,
  `window.hide*Gate` — dev backdoors bypassing UI role checks.
- Cross-file consistency law: map EVERY module's check independently — the backdoor may grant
  provider admin in one chunk while giveaway creation stays blocked in another. The
  inconsistency IS the true attack surface.
- EXPLOITABILITY GATE: does the backing API ALSO trust the client flag, or does the endpoint
  independently validate? Client-only bypass without API validation = needs-API-confirmation.

## Probe adjustment (grpc × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
