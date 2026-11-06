# Other confirmations — iot / machine

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- base technique: `holyshit-mode-case-obsidian-y-api-other-confirmations.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **iot** · auth **machine** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `stream:true` works on /pg/chat; upstream model identifiers leak (`glm-4.7-flash:latest`, `fp_ollama`).
- `conversation_id` in response is NOT IDOR-able (server regenerates/ignores supplied values).
- CORS `ACAO: *` but Bearer-auth (no cookies) → config-flaw-only, not exploitable alone.
- Negative: no /pg/* admin surfaces, no PII endpoints, junk keys rejected uniformly.

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
