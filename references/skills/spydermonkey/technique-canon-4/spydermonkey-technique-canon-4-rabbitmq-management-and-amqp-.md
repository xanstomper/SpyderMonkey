# RabbitMQ management and AMQP anonymous

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

15672 management UI gate class; AMQP anonymous connect posture. Decisive test: management UI 401-vs-404 + AMQP connect reaching auth stage — inventory rows.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
