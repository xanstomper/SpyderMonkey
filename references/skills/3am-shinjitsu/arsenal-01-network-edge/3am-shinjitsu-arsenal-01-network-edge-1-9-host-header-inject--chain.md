# 1.9 Host-header injection (score 65) [ONE request, off-peak] — chain composition

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-9-host-header-inject.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- DECISIVE: `curl -s -H 'Host: evil.com' https://<target>/password-reset -d 'email=x@y.z'`
  → inspect reset link host in any response body / downstream email (operator-supplied box).
- CONFIRMED WHEN: reset URL carries attacker host (reset poisoning / cache poisoning).
- FP: absolute-URL builders that re-derive host server-side.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
