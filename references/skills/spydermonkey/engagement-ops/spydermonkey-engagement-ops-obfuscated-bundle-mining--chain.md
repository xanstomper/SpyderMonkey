# Obfuscated-bundle mining — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-obfuscated-bundle-mining.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The decoder-replay recipe for javascript-obfuscator bundles, the New Relic `/api/script`
obfuscate-regex route leak, i18n/env plaintext feature maps, runtime crypto hooks, and the
wildcard-cert DNS wordlist all live in `references/spa-bundle-extraction.md` — load that before
touching any obfuscated or lazy-loaded SPA bundle.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
