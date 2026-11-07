# Password-policy weakness — mobile / unauth

- source canon: `spydermonkey/technique-canon-11.md`
- base technique: `spydermonkey-technique-canon-11-password-policy-weakness.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **mobile** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the client is another principal — storage/permission surface, own device only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Length/complexity/rotation rules enforced client-side only. Decisive test: server accepts a policy-violating change on your own account = the finding.

## Probe adjustment (mobile × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
