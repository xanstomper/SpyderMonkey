# XInclude and SOAP param XXE — gateway / root

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-xinclude-and-soap-param-xxe.md`
- bindings: **WSTG-INPV-07** · **CWE-611** · **ATT&CK T1190**
- context: **gateway** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

Client-side XML parsers (XInclude on a fragment, SOAP body param) carry the same entity class without a full document control. Decisive test: the OOB marker through the fragment param.

## Probe adjustment (gateway × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
