# 00 · BARBICAN — The Shield

**Role:** the first layer and the last action. Barbican protects the operator
before the family touches an estate, and removes the operator's footprint when
the engagement closes.

**Engine:** `~/.hermes/skills/security/barbican/scripts/barbican.py`
**Dispatcher:** `spydermonkey.py` → `route --goal "protect my opsec"` → barbican
**Phase:** `scope_analysis`

## axis

BEFORE — posture, vantage, identity, artifacts, noise budget, wipe.

Barbican owns the questions every other mandate assumes are already answered:

- Where am I firing from, and has that exit been verified?
- What alias and infrastructure identify this engagement?
- How much noise is this engagement allowed to make, and when?
- What operator strings could leak into family artifacts?
- What is removed, reversibly, at close?

## law

1. **No target action before posture.** A non-lab engagement without a recorded
   posture is not ready. The dispatcher's kernel returns `barbican-posture` as
   the first directive for exactly this reason.
2. **Vantage is verified, never assumed.** `vantage check` must show the exit IP
   echo. A claimed VPN is not a verified VPN. `--vantage lab` is valid only for
   loopback replicas (127.0.0.1 / ::1).
3. **Zero documents, zero real identity.** The recorded P0 declaration is the
   whole gate. Barbican uses an engagement alias; it never stores or transmits
   operator identity documents.
4. **Noise is budgeted.** `timeline` is a pacing plan, not decoration. Batch
   within the family noise budget; do not turn a validation into a stress test.
5. **Close is a lifecycle step.** `sanitize` runs before `wipe`; `wipe` is
   explicit (`--confirm`) and reversible-by-design. Nothing of value is kept.
6. **Barbican does not attack.** Its exposure audit examines the operator's own
   estate. It is not a target-recon tool and never becomes one.

## handoff

### Open the engagement

```bash
barbican assess --target <target>
barbican posture --target <target> --vantage vm --alias <alias>
barbican vantage check --target <target>
barbican timeline --target <target> --burst <n> [--pause <seconds>]
barbican trail --target <target>
```

`posture` is the hard gate. `assess` ranks the operator's own exposure first.

### During the engagement

```bash
barbican check
barbican alias --target <target> [--rotate]
barbican leakscan --target <target> [--deep]
barbican sanitize --target <target> [--write]
```

`leakscan` is the operator-string battery over family artifacts. `sanitize`
reports what it would strip; `--write` applies the changes. Neither command
touches the target.

### Close the engagement

```bash
barbican sanitize --target <target> --write
barbican wipe --target <target> --confirm
barbican verify
```

After `wipe`, the campaign closeout should record `wiped` and the report should
name what was removed. Do not call `rm -rf` on family state instead.

## evidence

- `posture` state: alias, vantage class, timestamp.
- `vantage check`: exit IP echo and the gate result.
- `timeline`: the noise budget actually used.
- `leakscan` / `sanitize`: findings count before and after.
- `wipe --confirm`: the reversible cleanup receipt.

Barbican findings are **operator-exposure findings**, not target findings. Keep
them in the campaign closeout and the war report; do not invent a target ledger
row to carry them. If a target finding is discovered during an exposure audit,
it follows the normal gate + ledger path.

## fleet

```bash
spydermonkey.py fleet --goal "establish a verified vantage" --agents barbican
# engine brief: barbican assess --target <target>
```

The fleet treats barbican as the readiness gate. A barbican failure means no
other agent is cleared to fire at a non-lab estate.

## failure

| Symptom | Correct response |
|---|---|
| `vantage check` cannot confirm the exit | Stop. Fix the VM/VPN or declare the target a loopback lab. Never fire anyway. |
| `posture` missing | Run `posture`; the dispatcher kernel will keep returning it. |
| `leakscan` reports operator strings | Block close, rotate the alias, rerun `sanitize`, then `leakscan` until clean. |
| `wipe` refuses without `--confirm` | That is the safety interlock. Review what will be removed, then pass `--confirm`. |
| Engine missing | `spydermonkey.py doctor` and install the family engine; do not emulate barbican by hand. |

A barbican error is a readiness problem, not permission to skip the shield.
