# Ops pitfalls — grpc / unauth

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-ops-pitfalls.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **grpc** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- holyleadger `add` positional grammar (bit three times this session): `add <class_id> <status> [--target T] [--score N] --technique "..."` — status is a REQUIRED positional right after class_id, never a flag; `add hypothesis --technique ...` without status errors with a confusing "the following arguments are required: status" even though the flag form looks complete.
- Astro re-export shims — see bundle-recovery section above.
- **skill_manage write_file param**: new support files need `file_content=`, NOT `content=` — `content` is only for create/edit of SKILL.md. Error is just `file_content is required`.
- **WS recon scripts must self-terminate**: set `ss.settimeout(dur+slack)` BEFORE the read loop and a hard `time.time()` deadline — an unset or too-generous socket timeout on a quiet stream hangs the sandbox to its 300s kill. Keep per-read timeouts ≤3s when probing client→server messages.
- **Post-hoc verify fixtures must mirror the real wire layout**: first synthetic kind1 fixture omitted the i32 latBase/lngBase fields at payload offsets 12/16 → struct.error. Re-read the reference layout table before hand-packing frames; offset errors masquerade as "decoder bugs".

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
