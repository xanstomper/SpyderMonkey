# ASN-block discriminator (block page ≠ solvable challenge) — chain composition

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-asn-block-discriminator.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

A 403 "Attention Required!" that PERSISTS for a real headless chromium while
`cdn-cgi/challenge-platform/...` assets return 200 is an ASN/datacenter block, not
a challenge — the JS runs, the wall stays. No header/TLS/cookie stack clears it; the
plane is reachable only from residential egress, which is a sanctioned-vantage
decision for the operator, never a home-IP technique. Record the class negative
with the discriminator evidence and move on.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
