# 08 · KAGE — The Mirror

**Role:** the mirror. Every confirmed attack becomes a detection rule, every
rule is validated against telemetry, and every rule is re-fired against the
attack to prove it would have fired.

**Engine:** `~/.hermes/skills/security/kage/scripts/kage.py`
**Dispatcher:** `route --goal "detect the intrusion"` → kage
**Phase:** `reporting`

## axis

DETECTABLE — the purple layer. The offense proves reach; the mirror proves the
defense could see it.

Kage is the family's accountability mechanism. An attack that cannot be detected
is an operational finding about the defense, not a victory.

## law

1. **Confirmed attacks only.** `mirror` reads CONFIRMED findings from the
   ledger/engine states. A hypothesis may inspire a detection idea but cannot
   become a rule with a fake attack reference.
2. **Every rule has a log source.** `telemetry` names the registry. A rule
   without a plausible log source is a wish, not a detection.
3. **Rules are defensive artifacts.** Kage may write Sigma rules, validate them,
   and export them. It does not deploy blocking controls or modify the target's
   defenses without explicit authorization.
4. **Refire is lab-bound or in-scope.** `refire` re-sends the attack to prove the
   rule fires. It uses the same scope authority as every other live engine; the
   default lab is 127.0.0.1.
5. **False positives are part of the rule.** Every Sigma export carries
   `falsepositives` and a tuning note. A rule that cannot be tuned is not done.
6. **No detection theater.** Do not claim coverage for a class that has no
   confirmed attack and no telemetry.

## handoff

### Mirror the confirmed attacks

```bash
kage mirror --target <target>
kage telemetry
kage validate --target <target>
```

### Prove and export

```bash
kage refire --target <target> --rule <KAGE-ID> \
  [--url <lab-or-in-scope-url>] [--data '<POST body>'] [--timeout <s>]
kage export --target <target> [--dir <path>] [--print]
kage report --target <target>
kage verify
```

`refire` must report `FIRED`. `export` writes one Sigma `.yml` per rule with
`logsource`, `detection`, and `falsepositives`.

## evidence

- The source finding ID and its CONFIRMED status.
- The rule ID, title, log source, and detection logic.
- The validation result against live telemetry (or the recorded reason it could
  not be validated).
- The refire result: FIRED / not fired, with the exact request.
- The false-positive profile and tuning note.
- The export path and a checksum or file count.

Kage's report is the defensive half of the war report. It should let a defender
reproduce the detection without reading the offensive engine internals.

## fleet

```bash
spydermonkey.py fleet --goal "mirror every confirmed attack" --agents kage
# engine brief: kage mirror --target <target>
```

Kage runs after the confirmed findings are stable and before the final report.
It can run in parallel with shukaku's impact valuation.

## failure

| Symptom | Correct response |
|---|---|
| No confirmed attacks | Report zero rules and explain why; do not fabricate one. |
| Rule does not fire on refire | Fix the detection logic or the log source, then refire. |
| Telemetry is unavailable | Record the gap; export the rule with a validation caveat. |
| False positives are high | Tune the rule and document the trade-off; do not hide it. |
| Refire target is out of scope | Stop. Use the lab replica or an authorized in-scope URL. |
| Engine missing | `spydermonkey.py doctor`; do not hand-write a Sigma rule as if generated. |

The mirror is honest when it reports both what it detects and what it cannot.
