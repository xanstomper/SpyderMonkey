# MASTG Deep Links and Intent Redirection (MASTG-PLATFORM-06) — mobile / unauth

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-deep-links-and-intent-redire.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **mobile** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the client is another principal — storage/permission surface, own device only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: hijackable deep links, intent passthrough
- probe: static link inventory; am-probe the lab app with crafted intents
- wall: lab device

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
