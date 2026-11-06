# RTP telemetry sweep discipline

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

Rolling-window liveRtp sweeps every session (fresh money-pump rows), DISTINCT leading words per title (dedupe discipline), mirror the exact POST verb+headers. Decisive test: liveRtp_24h from the public endpoint — the repricing pattern across sweeps is the crown class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
