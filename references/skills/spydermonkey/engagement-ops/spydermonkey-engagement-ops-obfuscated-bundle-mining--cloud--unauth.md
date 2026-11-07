# Obfuscated-bundle mining — cloud / unauth

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-obfuscated-bundle-mining.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **cloud** · auth **unauth** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

The decoder-replay recipe for javascript-obfuscator bundles, the New Relic `/api/script`
obfuscate-regex route leak, i18n/env plaintext feature maps, runtime crypto hooks, and the
wildcard-cert DNS wordlist all live in `references/spa-bundle-extraction.md` — load that before
touching any obfuscated or lazy-loaded SPA bundle.

## Probe adjustment (cloud × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
