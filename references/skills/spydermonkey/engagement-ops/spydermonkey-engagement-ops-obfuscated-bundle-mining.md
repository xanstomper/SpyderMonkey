# Obfuscated-bundle mining

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

The decoder-replay recipe for javascript-obfuscator bundles, the New Relic `/api/script`
obfuscate-regex route leak, i18n/env plaintext feature maps, runtime crypto hooks, and the
wildcard-cert DNS wordlist all live in `references/spa-bundle-extraction.md` — load that before
touching any obfuscated or lazy-loaded SPA bundle.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
