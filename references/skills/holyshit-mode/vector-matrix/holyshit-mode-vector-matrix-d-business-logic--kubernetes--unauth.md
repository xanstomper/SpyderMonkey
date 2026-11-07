# D. BUSINESS LOGIC — kubernetes / unauth

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-d-business-logic.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **kubernetes** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Race conditions: parallel withdraw/redeem/transfer (single-packet attack — N requests, one connection)
- Payment flows: negative/zero/decimal prices, currency confusion, coupon stacking, post-hoc price edits
- Stateless verification: claim gates with no server-to-server callback (playbook §5)
- Subscription/lifetime bypass: downgrade-with-features, trial re-spam via email tricks
- Export/import: CSV injection (=cmd), formula injection in generated files
- Referrer/CSRF: state-changing actions without CSRF tokens (SameSite=None paths)
- Webhooks: unsigned payloads, signature-confusion, replay without timestamp/nonce
- Introspection leaks: GraphQL, Swagger UI live, Spring Boot actuators, .git/.svn deployment

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
