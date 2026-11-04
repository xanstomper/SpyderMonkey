# WSTG-CLNT-04 Client-side URL Redirect — dns / unauth

- source canon: `spydermonkey/wstg-deep-canon.md`
- base technique: `spydermonkey-wstg-deep-canon-wstg-clnt-04-client-side-url-re.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **dns** · auth **unauth** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: fragment/JS-driven redirects attacker-controllable
- probe: the REDIRECT battery + location header differential
- wall: benign evil.example marker only

## Probe adjustment (dns × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
