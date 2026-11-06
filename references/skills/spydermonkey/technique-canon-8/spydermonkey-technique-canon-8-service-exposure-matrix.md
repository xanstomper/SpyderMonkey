# Service exposure matrix

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

NodePort/LoadBalancer surfaces mapping internal services externally. Decisive test: svc listing + external reachability of one = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
