# Hypothesis (needs one real session/key to prove) — api / low-priv

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-hypothesis-needs-one-real-se.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **`chat_auth_mode_split` (score 65)**: chat backend accepts `X-Chat-Auth-Mode: platform_key` and validates a CLIENT-supplied `X-Gratisfy-API-Key` header. Uniform `401 invalid_api_key` across key shapes = no format oracle. If validation bypasses (truncation, format quirk, header confusion with `Authorization`), full chat-API access. conversations/media/realtime/attachments all gated the same way.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
