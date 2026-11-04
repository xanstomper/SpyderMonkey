# Models Discovered — firmware / high-priv

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-models-discovered.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **firmware** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Tier 1 (premium): ling-3.0-flash-vl, sdxl-lightning, flux-2-klein-4b, flux-2-klein-9b, flux-2-dev, logfare/auto, flux-1-schnell, gemma-4-26b
- Tier 2 (free): whisper-large-v3-turbo, gpt-image-2, phoenix-1.0, space-bunny-alpha, flux-2-pro, nano-banana-2, aura-2-en, nova-3, qwen-3.8-27b, lucid-origin, deepseek-v4.1-flash

## Probe adjustment (firmware × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
