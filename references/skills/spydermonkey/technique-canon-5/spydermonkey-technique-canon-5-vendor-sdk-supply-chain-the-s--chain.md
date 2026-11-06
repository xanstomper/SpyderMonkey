# Vendor SDK supply-chain (the SPY-095 class family) — chain composition

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-vendor-sdk-supply-chain-the-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Production pages importing personal/third-party infra (workers.dev class), SDK env-defaults (`mode||"development"`), auth material in URLs. Decisive test: passive capture of the page's OWN traffic (in-scope), the executing SDK pulled and cold-mapped — the env->host map verbatim is the crown.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
