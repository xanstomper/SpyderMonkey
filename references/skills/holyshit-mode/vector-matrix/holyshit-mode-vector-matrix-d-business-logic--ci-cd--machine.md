# D. BUSINESS LOGIC — ci-cd / machine

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-d-business-logic.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **ci-cd** · auth **machine** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Race conditions: parallel withdraw/redeem/transfer (single-packet attack — N requests, one connection)
- Payment flows: negative/zero/decimal prices, currency confusion, coupon stacking, post-hoc price edits
- Stateless verification: claim gates with no server-to-server callback (playbook §5)
- Subscription/lifetime bypass: downgrade-with-features, trial re-spam via email tricks
- Export/import: CSV injection (=cmd), formula injection in generated files
- Referrer/CSRF: state-changing actions without CSRF tokens (SameSite=None paths)
- Webhooks: unsigned payloads, signature-confusion, replay without timestamp/nonce
- Introspection leaks: GraphQL, Swagger UI live, Spring Boot actuators, .git/.svn deployment

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
