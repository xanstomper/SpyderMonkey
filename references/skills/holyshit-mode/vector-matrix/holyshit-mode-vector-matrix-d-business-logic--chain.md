# D. BUSINESS LOGIC — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-d-business-logic.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Race conditions: parallel withdraw/redeem/transfer (single-packet attack — N requests, one connection)
- Payment flows: negative/zero/decimal prices, currency confusion, coupon stacking, post-hoc price edits
- Stateless verification: claim gates with no server-to-server callback (playbook §5)
- Subscription/lifetime bypass: downgrade-with-features, trial re-spam via email tricks
- Export/import: CSV injection (=cmd), formula injection in generated files
- Referrer/CSRF: state-changing actions without CSRF tokens (SameSite=None paths)
- Webhooks: unsigned payloads, signature-confusion, replay without timestamp/nonce
- Introspection leaks: GraphQL, Swagger UI live, Spring Boot actuators, .git/.svn deployment

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
