# Cross-case note (2026-10-20, somny.xyz) — iot / high-priv

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-cross-case-note-2026-10-20-s.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **iot** · auth **high-priv** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Recurring reseller pattern (gratisfy, gonka, somny): **key-create endpoints return masked keys; a `reveal`/`secret` sub-endpoint is the real primitive** (somny: `POST /api/keys` → masked `sk-som...wle0`, `POST /api/keys/{id}/reveal` → full key). IDOR on reveal with foreign UUID → 400 body-validation (auth checked before existence). Also recurring: disposable-domain signup filters miss mail.tm's rotating domains — probe mail.tm `/domains` for newly-active ones first. See `references/case-somny-xyz.md`.

## Probe adjustment (iot × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
