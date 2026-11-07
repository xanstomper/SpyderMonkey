# B. Plaintext support files are a free feature map — mobile-api / service

- source canon: `spydermonkey/spa-bundle-extraction.md`
- base technique: `spydermonkey-spa-bundle-extraction-b-plaintext-support-files.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **service** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

1. **New Relic browser-agent config leaks the sensitive routes.** Fetch the agent
   script the app serves (often `/api/script` on the SPA origin): its
   `obfuscate:[{regex:...}]` array exists to redact sensitive URL segments from
   telemetry, so each regex LITERALLY SPELLS the routes worth redacting — admin
   paths, ID-bearing segments (`/(handhistory|open/hand/scene)/admin/` spelled out
   verbatim). One request, zero obfuscation, and it names surfaces no bundle grep
   found. `NREUM.loader_config/info` accountID/applicationID are recon-grade.
2. **`/assets/i18n/en.json` is plaintext and names every feature** — money lanes,
   share flows, report flows, reward mechanics, admin-fee strings. ~150KB of catalog
   without touching the obfuscator.
3. **Boot endpoints are plaintext while data APIs are enveloped.** An `/api/env`-style
   endpoint (region / env tier / langs / currency) loads unauthenticated — read the
   env tier (`"env":"live"`); an app admitting `development` on a prod host is the
   dev-in-prod class.
4. **Runtime hooks beat static hunting for client crypto.** `evaluateOnNewDocument` a
   hook that wraps `SubtleCrypto.prototype.importKey`/`decrypt` (hex-dump key+data
   args, then call the ORIGINAL from the prototype — replace on the prototype, never
   on the instance, or the original reference is lost) and a filtered `JSON.parse`.
   An empty capture is itself signal: no subtle-crypto calls = the crypto is a pure-JS
   lib inside the bundle closure, and the app never fired the data API (no session).

## Probe adjustment (mobile-api × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
