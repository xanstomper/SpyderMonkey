# Hypotheses KILLED (honest negatives)

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- **Handoff code brute (55→dead):** live flow captured real code = 32-hex, 128-bit, one-time. Dead.
- **profiles RLS UPDATE bypass:** 204 was `content-range: */0`. RLS holds.
- **Realtime WS:** 101 + unauth heartbeat OK, but postgres_changes subscription on public tables errors (Realtime not enabled). No leak. Prior "401 = auth gate" was a curl false-negative.
- **/admin/users 200:** SPA ghost route (text/html).
- **handoff_code_entropy_unknown (55→negative):** resolved by live flow.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
