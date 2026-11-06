# RabbitMQ management and AMQP anonymous — chain composition

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-rabbitmq-management-and-amqp-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

15672 management UI gate class; AMQP anonymous connect posture. Decisive test: management UI 401-vs-404 + AMQP connect reaching auth stage — inventory rows.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
