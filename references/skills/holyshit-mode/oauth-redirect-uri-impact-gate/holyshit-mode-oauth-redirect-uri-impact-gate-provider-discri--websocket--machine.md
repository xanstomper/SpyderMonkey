# Provider discriminator matrix — websocket / machine

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-provider-discri.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **machine** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Provider | Render-time validation | Token-exchange validation | Impact |
|----------|----------------------|--------------------------|--------|
| **Google** | Hard-rejects unregistered URIs at render (`redirect_uri_mismatch` error page) | N/A | **Chain blocked at render** — safe even with GoTrue flaw |
| **Discord** | Renders authorize page 200 regardless (validates at token-exchange, not render) | Rejects unregistered URIs at token-exchange | **Impact gate = Discord app's registered redirect URIs** |

Discord's 200 on the authorize page is NOT proof of acceptance. The only way to know is to complete the flow and see whether Discord delivers the code to your URI or shows "Invalid OAuth".

## Probe adjustment (websocket × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
