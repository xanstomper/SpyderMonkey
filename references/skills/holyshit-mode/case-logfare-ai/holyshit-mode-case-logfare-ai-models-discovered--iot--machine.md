# Models Discovered — iot / machine

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-models-discovered.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **iot** · auth **machine** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Tier 1 (premium): ling-3.0-flash-vl, sdxl-lightning, flux-2-klein-4b, flux-2-klein-9b, flux-2-dev, logfare/auto, flux-1-schnell, gemma-4-26b
- Tier 2 (free): whisper-large-v3-turbo, gpt-image-2, phoenix-1.0, space-bunny-alpha, flux-2-pro, nano-banana-2, aura-2-en, nova-3, qwen-3.8-27b, lucid-origin, deepseek-v4.1-flash

## Probe adjustment (iot × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
