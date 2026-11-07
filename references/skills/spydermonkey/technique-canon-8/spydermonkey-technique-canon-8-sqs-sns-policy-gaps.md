# SQS/SNS policy gaps

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Queue/topic policies with wildcard principals or open HTTP notification endpoints. Decisive test: policy doc where readable + one subscribe-probe to YOUR endpoint = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
