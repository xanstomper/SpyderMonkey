# Cross-case note (2026-10-20, somny.xyz) — ios / machine

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-cross-case-note-2026-10-20-s.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ios** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Recurring reseller pattern (gratisfy, gonka, somny): **key-create endpoints return masked keys; a `reveal`/`secret` sub-endpoint is the real primitive** (somny: `POST /api/keys` → masked `sk-som...wle0`, `POST /api/keys/{id}/reveal` → full key). IDOR on reveal with foreign UUID → 400 body-validation (auth checked before existence). Also recurring: disposable-domain signup filters miss mail.tm's rotating domains — probe mail.tm `/domains` for newly-active ones first. See `references/case-somny-xyz.md`.

## Probe adjustment (ios × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
