# Ranking rule

- source canon: `holyshit-mode/engagement-report-pattern.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

`confirmed(3) > inconclusive(2) > hypothesis(1) > negative(0)`, then score desc within a
tier. Implemented as `sorted(classes.items(), key=lambda kv: (-rank(status), -score))`.
Confirmed classes always outrank hypotheses even if the hypothesis has a higher raw score —
a proven finding is worth more than an unproven high-scoring guess.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
