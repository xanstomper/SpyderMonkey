# 5.7 Trust-header vocabulary mining (score 70) — chain composition

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-7-trust-header-vocabu.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- GREP chunks for `ssr-client-ip`, `x-client-geo`, `cf-ipcountry`, `country`, `region` header
  builders at call sites — SSR-to-API forwarding leaks the trust vocabulary.
- If the API honors client-supplied geo headers, region blocks (`451 er_sign_up_region_block`-
  class) are one header away. Spoof-test on the LEAST-throttled discriminating endpoint
  (game launch/demo), NEVER on the auth plane (self-DoS law, §3.7).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
