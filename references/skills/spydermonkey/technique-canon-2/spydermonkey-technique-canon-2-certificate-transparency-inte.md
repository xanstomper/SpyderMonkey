# Certificate-transparency intel depth

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

crt.sh/certspotter + live-cert SAN mining (the CT-log lane in the ops canon) — wildcard/SAN/sibling-brand exposure is the inventory crown. Decisive test: SAN list from a live handshake naming hosts DNS never published.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
