# TLS-only enforcement — linux / unauth

- source canon: `spydermonkey/technique-canon-13.md`
- base technique: `spydermonkey-technique-canon-13-tls-only-enforcement.md`
- bindings: **WSTG-INPV-06** · **CWE-601** · **ATT&CK T1190**
- context: **linux** · auth **unauth** · chain role **final**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

http→https redirect + HSTS on every tier. Decisive test: the http variant serving content = the absence.

## Probe adjustment (linux × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
