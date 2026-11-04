# 1.15 Erlang/RabbitMQ exposure battery (score 85 on infra-heavy estates, all read-only) — graphql / low-priv

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-15-erlang-rabbitmq-e.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **graphql** · auth **low-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- 5672 AMQP: raw socket, send `AMQP\x00\x00\x09\x01`, parse the Connection.Start frame's
  field table for product/version/cluster_name — full broker fingerprint, zero auth.
- 5671 amqps: TLS cert grab (issuer + notBefore) — auto-renewed LE = actively-maintained
  live broker; then the same AMQP Start over TLS.
- 4369 EPMD: send `\x00\x01n` → `name <node> at port <N>` = node-name disclosure + the
  dist-port oracle; dist port closed from your vantage downgrades to info-disclosure.
- 15672 mgmt UI + 25672 Erlang dist: one connect each; OPEN 25672 = RCE-behind-cookie
  class (cookie brute is a credential attempt — RoE-gated, never run it).
- Auth decisive test: ONE guest/guest attempt per broker (pika), confirm read-only with a
  passive default-exchange declare; ACCESS_REFUSED = hardened, ledger it.
- PIP PITFALL: system python is PEP 668 externally-managed and managed venvs ship without
  pip — `python3 -m venv <scratch>/venv && <venv>/bin/pip install pika` before the auth
  test; the raw-socket handshake needs no dependencies.

## Probe adjustment (graphql × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
