# Automated life: the report is the output of `scan`

- source canon: `holyshit-mode/engagement-report-pattern.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

With `HOLYSHIT_TARGET` exported, `holyshit.py scan <task>`:
1. **dispatches** to the models (`holyshit-inject`)
2. **converges** to CONFIRMED/BLOCKED/HYPOTHESIS (`holyconverge`)
3. **auto-persists** the outcome — confirmed → `holyleadger add confirmed` + `chain` (rc 0);
   blocked/exhausted → `holyleadger add hypothesis` (rc 1/3). No `HOLYSHIT_TARGET` → no-op
   (safety + makes offline harnesses deterministic).

So a confirmed finding is guaranteed to land in state (and appear in the next `report`)
with zero manual `add`. The report is thus always current after any `scan`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
