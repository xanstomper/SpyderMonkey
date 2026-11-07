# Provider discriminator matrix

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Provider | Render-time validation | Token-exchange validation | Impact |
|----------|----------------------|--------------------------|--------|
| **Google** | Hard-rejects unregistered URIs at render (`redirect_uri_mismatch` error page) | N/A | **Chain blocked at render** — safe even with GoTrue flaw |
| **Discord** | Renders authorize page 200 regardless (validates at token-exchange, not render) | Rejects unregistered URIs at token-exchange | **Impact gate = Discord app's registered redirect URIs** |

Discord's 200 on the authorize page is NOT proof of acceptance. The only way to know is to complete the flow and see whether Discord delivers the code to your URI or shows "Invalid OAuth".

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
