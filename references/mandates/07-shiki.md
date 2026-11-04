# 07 · SHIKI — The Command

**Role:** the command. Shiki conducts the whole family as one assault: gate →
find → descend → forge → chain → verdict, with lanes, a fire list, a war board,
resume, and closeout.

**Engine:** `~/.hermes/skills/security/shiki/scripts/shiki.py`
**Dispatcher:** `route --goal "full assault"` → shiki
**Phase:** `reporting`

## axis

TOGETHER — the family as one operation, not ten disconnected tools.

Shiki is the conductor. It does not replace a mandate's engine; it sequences the
mandates, records lane state, and produces the joint verdict.

## law

1. **Gate first.** `assault` starts with the barbican vantage check and the
   scope authority. No scope authority → no assault. No verified vantage on a
   non-lab estate → no assault.
2. **One plan, explicit steps.** `--plan-only` shows the exact sequence before
   anything fires. `--skip` is for documented reasons, not impatience.
3. **Resume, don't restart.** `--resume` continues from lane state. Re-running a
   completed step is a new decision, not a default.
4. **Parallel is bounded.** `--parallel` runs independent lanes; it does not
   multiply traffic at a single target beyond the noise budget.
5. **Closeout is explicit.** `--close` closes the campaign and writes the
   verdict. It does not wipe operator artifacts; that is barbican's `wipe`.
6. **The verdict is evidence-based.** A lane is green only when its deliverable
   exists. A joint report never upgrades a hypothesis to a confirmation.

## handoff

### Plan before fire

```bash
shiki plan --org <target> --estate <estate> --lanes <lane,lane,…>
shiki board --org <target>
shiki warroom --org <target>
shiki assault --target <target> --url <base-url> --domain <domain> --plan-only
```

(`assault --plan-only` is the canonical planner; `plan` and `board` are the
read-only views.)

### Run the assault

```bash
shiki assault --target <target> --domain <domain> \
  [--url <base-url>] [--bundle <path>] [--cookie 'k=v'] \
  [--boundary-url '<url-with-{id}>'] [--probe-ids <own-ids>] \
  [--skip gate,find,descend,forge,chain] [--parallel] [--resume] [--close]
```

### Validate and hand off

```bash
shiki validate --target <target> [--days <n>]
shiki fires --org <target>
shiki handoff --target <target> --to shukaku
shiki handoff --target <target> --to kage
shiki report --target <target>
shiki verify
```

`validate` re-checks every CONFIRMED claim for drift. `fires` is the joint fire
list. `handoff` prints the next mandate's exact command sequence.

## evidence

- Lane state: which step ran, when, against which asset, with which result.
- The joint fire list: every candidate, its owner, and its status.
- The drift validation result for each confirmed claim.
- The final verdict: green/amber/red per lane, and the evidence behind it.
- The closeout record: what was delivered, what was reversed, what remains.

Shiki's report is the engagement's single source of truth. It must agree with
the dispatcher ledger, the phase board, and each engine's own state; a
disagreement is a bug to resolve before the report ships.

## fleet

```bash
spydermonkey.py fleet --goal "run the joint assault" --agents shiki
# engine brief: shiki board --org <target>
```

Shiki is the fleet's conductor. It can run in parallel with barbican's closeout
preparation, but not before the scope gate.

## failure

| Symptom | Correct response |
|---|---|
| Scope authority missing | Run `scope init`; do not bypass the gate. |
| Vantage unverified | Return to barbican; the assault stays blocked. |
| One lane fails | Mark the lane blocked, continue independent lanes, then `--resume`. |
| Report disagrees with an engine | Reconcile state before publishing; do not paper over it. |
| Closeout requested mid-run | Finish or explicitly stop the active lane, then `--close`; never leave an orphan process. |
| Engine missing | `spydermonkey.py doctor`; do not simulate a lane. |

A clean red verdict is a successful engagement; a green verdict built on a
missing deliverable is a failed one.
