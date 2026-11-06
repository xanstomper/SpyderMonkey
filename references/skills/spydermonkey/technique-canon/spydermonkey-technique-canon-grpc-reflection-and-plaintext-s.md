# gRPC reflection and plaintext services

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

grpcurl list on plaintext = service inventory without auth. Decisive test: reflection output names services the web app never exposes — crown the inventory gap.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
