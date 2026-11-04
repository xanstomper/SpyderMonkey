# L1 — VANTAGE — chain composition

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l1-vantage.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Audit | Synthesis |
|---|---|
| default route (residential iface = CRITICAL) | posture declares vm/vps/vpn/lab as THE sanctioned exit |
| proxy/VPN env + resolver config | engagement shells verify the route before firing |
| target-side logs will show the vantage — assume it's recorded forever | never mix personal browsing with engagement vantage |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
