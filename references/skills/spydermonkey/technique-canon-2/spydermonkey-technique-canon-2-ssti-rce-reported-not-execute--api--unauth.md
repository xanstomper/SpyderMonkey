# SSTI → RCE reported-not-executed — api / unauth

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-ssti-rce-reported-not-execute.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **api** · auth **unauth** · chain role **final**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Gadget chains (jinja `__mro__` walks, freemarker `Execute`) are DOCUMENTED as the impact ceiling; the deliverable is the writeup with the marker-level proof — never the executed command. NO-GAIN.

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
