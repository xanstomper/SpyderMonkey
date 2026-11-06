# Automated life: the report is the output of `scan` — chain composition

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-automated-life-the-r.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

With `HOLYSHIT_TARGET` exported, `holyshit.py scan <task>`:
1. **dispatches** to the models (`holyshit-inject`)
2. **converges** to CONFIRMED/BLOCKED/HYPOTHESIS (`holyconverge`)
3. **auto-persists** the outcome — confirmed → `holyleadger add confirmed` + `chain` (rc 0);
   blocked/exhausted → `holyleadger add hypothesis` (rc 1/3). No `HOLYSHIT_TARGET` → no-op
   (safety + makes offline harnesses deterministic).

So a confirmed finding is guaranteed to land in state (and appear in the next `report`)
with zero manual `add`. The report is thus always current after any `scan`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
