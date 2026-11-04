# Key-plane trust-root split (operator supplied live sk-proxy- key mid-session) — iot / high-priv

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-key-plane-trust-root-split-ope.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot** · auth **high-priv** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Key opens `/v1/*` fully (30-model catalog incl. grok-4.7 family, kimi-k3, muse-spark, nano-banana-pro; Anthropic + Responses APIs both 429 at quota).
- ALL `/api/*` dashboard endpoints 401 on Bearer/X-Api-Key/X-Atessa-Key/X-Proxy-Key/raw-key variants — session-cookie-only. **No plane bleed** (good architecture). Lesson: when the operator hands an API key, first map WHICH plane it opens before planning the authed chain; say explicitly what still needs the session cookie.

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
