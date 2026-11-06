# IPv6 /64 rotation — chain composition

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-ipv6-64-rotation.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`sudo ip -6 addr add <any-addr-in-block>/64 dev <iface>` then `curl --interface <addr>` = fresh
rate-limit bucket per address. NOTE: the sandbox security guard may block `curl --interface <addr>`
mid-session (approved-command gate) — scope-gate with the operator before IP-rotation testing.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
