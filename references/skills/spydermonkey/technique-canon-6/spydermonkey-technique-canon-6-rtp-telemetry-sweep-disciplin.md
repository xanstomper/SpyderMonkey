# RTP telemetry sweep discipline

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Rolling-window liveRtp sweeps every session (fresh money-pump rows), DISTINCT leading words per title (dedupe discipline), mirror the exact POST verb+headers. Decisive test: liveRtp_24h from the public endpoint — the repricing pattern across sweeps is the crown class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
