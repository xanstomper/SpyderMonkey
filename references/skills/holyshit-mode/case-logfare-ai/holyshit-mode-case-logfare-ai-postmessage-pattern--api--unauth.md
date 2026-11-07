# postMessage Pattern — api / unauth

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-postmessage-pattern.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **api** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Callback uses: `window.opener.postMessage(data, window.location.origin)`
- This is CORRECT (targets sender origin)
- Not a vulnerability

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
