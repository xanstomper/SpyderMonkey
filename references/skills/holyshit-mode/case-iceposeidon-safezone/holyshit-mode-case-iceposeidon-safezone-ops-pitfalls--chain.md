# Ops pitfalls — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-ops-pitfalls.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- holyleadger `add` positional grammar (bit three times this session): `add <class_id> <status> [--target T] [--score N] --technique "..."` — status is a REQUIRED positional right after class_id, never a flag; `add hypothesis --technique ...` without status errors with a confusing "the following arguments are required: status" even though the flag form looks complete.
- Astro re-export shims — see bundle-recovery section above.
- **skill_manage write_file param**: new support files need `file_content=`, NOT `content=` — `content` is only for create/edit of SKILL.md. Error is just `file_content is required`.
- **WS recon scripts must self-terminate**: set `ss.settimeout(dur+slack)` BEFORE the read loop and a hard `time.time()` deadline — an unset or too-generous socket timeout on a quiet stream hangs the sandbox to its 300s kill. Keep per-read timeouts ≤3s when probing client→server messages.
- **Post-hoc verify fixtures must mirror the real wire layout**: first synthetic kind1 fixture omitted the i32 latBase/lngBase fields at payload offsets 12/16 → struct.error. Re-read the reference layout table before hand-packing frames; offset errors masquerade as "decoder bugs".

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
