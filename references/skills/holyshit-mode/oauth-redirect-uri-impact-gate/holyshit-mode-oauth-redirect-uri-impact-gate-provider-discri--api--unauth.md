# Provider discriminator matrix — api / unauth

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-provider-discri.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

| Provider | Render-time validation | Token-exchange validation | Impact |
|----------|----------------------|--------------------------|--------|
| **Google** | Hard-rejects unregistered URIs at render (`redirect_uri_mismatch` error page) | N/A | **Chain blocked at render** — safe even with GoTrue flaw |
| **Discord** | Renders authorize page 200 regardless (validates at token-exchange, not render) | Rejects unregistered URIs at token-exchange | **Impact gate = Discord app's registered redirect URIs** |

Discord's 200 on the authorize page is NOT proof of acceptance. The only way to know is to complete the flow and see whether Discord delivers the code to your URI or shows "Invalid OAuth".

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
