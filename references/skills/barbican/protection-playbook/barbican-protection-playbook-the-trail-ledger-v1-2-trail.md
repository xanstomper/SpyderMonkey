# The trail ledger (v1.2 — `trail`)

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

Row format: `provider :: purpose` (+ timestamp). Rules:
1. Engagement traffic touches ONLY sanctioned providers — personal accounts are a
   HIGH flag and the scan prints it in the row.
2. The trail is the engagement's upstream map: if a provider must be named in a
   disclosure later, the trail already knows.
3. `check --target T` surfaces the trail — a pre-flight that can't say which
   providers the engagement touches isn't a pre-flight.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
