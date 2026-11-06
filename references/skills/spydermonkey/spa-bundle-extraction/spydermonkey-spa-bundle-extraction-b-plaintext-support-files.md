# B. Plaintext support files are a free feature map

- source canon: `spydermonkey/spa-bundle-extraction.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
