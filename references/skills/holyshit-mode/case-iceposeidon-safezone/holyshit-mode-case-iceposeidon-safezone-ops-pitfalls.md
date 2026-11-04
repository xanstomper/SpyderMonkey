# Ops pitfalls

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- holyleadger `add` positional grammar (bit three times this session): `add <class_id> <status> [--target T] [--score N] --technique "..."` — status is a REQUIRED positional right after class_id, never a flag; `add hypothesis --technique ...` without status errors with a confusing "the following arguments are required: status" even though the flag form looks complete.
- Astro re-export shims — see bundle-recovery section above.
- **skill_manage write_file param**: new support files need `file_content=`, NOT `content=` — `content` is only for create/edit of SKILL.md. Error is just `file_content is required`.
- **WS recon scripts must self-terminate**: set `ss.settimeout(dur+slack)` BEFORE the read loop and a hard `time.time()` deadline — an unset or too-generous socket timeout on a quiet stream hangs the sandbox to its 300s kill. Keep per-read timeouts ≤3s when probing client→server messages.
- **Post-hoc verify fixtures must mirror the real wire layout**: first synthetic kind1 fixture omitted the i32 latBase/lngBase fields at payload offsets 12/16 → struct.error. Re-read the reference layout table before hand-packing frames; offset errors masquerade as "decoder bugs".

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
