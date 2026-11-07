# App-files secret scan — iot / unauth

- source canon: `spydermonkey/technique-canon-10.md`
- base technique: `spydermonkey-technique-canon-10-app-files-secret-scan.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **iot** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

App-private storage (files/, databases/, shared_prefs) holding tokens/PII on your own build. Decisive test: your build's data dump showing live secret material outside keychain.

## Probe adjustment (iot × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
