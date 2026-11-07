# Global constants — web-app / expired

- source canon: `holyshit-mode/example-target-binary-map-protocol.md`
- base technique: `holyshit-mode-example-target-binary-map-protocol-global-cons.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **web-app** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

`bt=36` header size; `$r=1e7` generic coord grid; `Re=1e5` contestant-fix coord scale; coord validation `X(v,isLat,scale)` = v/scale, abs<=90 lat / 180 lng. Health status enum `Yi = [disabled, paused, inside, outside, unavailable, eliminated]`.

## Probe adjustment (web-app × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
