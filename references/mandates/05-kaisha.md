# 05 · KAISHA — The Ladder

**Role:** the ladder. Once a foothold is confirmed, kaisha maps the depth below
it: the era-stack, privilege-escalation rungs, and lateral trust paths — one
rung at a time, with reversal evidence.

**Engine:** `~/.hermes/skills/security/kaisha/scripts/kaisha.py`
**Dispatcher:** `route --goal "climb deeper"` → kaisha
**Phase:** `infrastructure`

## axis

DEPTH — what an initial foothold would reach if it were real.

Kaisha is post-exploitation **planning** first and execution only under the same
validation-only walls. It answers: what is this host, what documented escalation
classes apply, what adjacent declared hosts trust it, and what must be reversed.

## law

1. **No foothold, no ladder.** Kaisha starts from confirmed access (or an
   explicitly declared lab host). It never manufactures access to justify a
   ladder.
2. **One rung at a time.** Execute the minimum rung that proves reachability,
   then stop and record it. No chaining rungs in a single uncontrolled run.
3. **Reversible by design.** Every executed rung gets a reversal record via
   `revert --rung <id> --evidence <what was and was not changed>`. Persistence
   is never installed.
4. **No destructive end states.** No wiping, no exhausting, no denial of
   service, no encryption, no data destruction. If a rung cannot be reversed,
   it is not a valid rung.
5. **Declared hosts only.** Lateral movement is limited to adjacent hosts the
   operator declared. A trust path to an undeclared third party is documented,
   not traversed.
6. **Credentials are counts, not contents.** A credential proves access; it is
   not copied into reports or retained after the proof.

## handoff

### Build the depth picture

```bash
kaisha ladder --target <target> --host <host> [--access '<confirmed access>']
kaisha cve --banner '<banner>'
kaisha rungs --target <target> [--host <host>]
kaisha lateral --target <target> --from <host> [--to <adjacent-host,...>]
```

### Execute and reverse

```bash
kaisha rungs --target <target> --host <host>
kaisha revert --target <target> --host <host> --rung <RUNG> \
  --evidence '<documented class matched; nothing executed>'
kaisha report --target <target>
kaisha verify
```

`rungs` is the ladder, rung by rung. `revert` is not optional paperwork: it is
the proof that the engagement stayed reversible.

## evidence

- The confirmed foothold (or the declared lab host) that justifies the ladder.
- The host's era-stack and the documented classes that follow from it.
- For each executed rung: the command, the observation, the timestamp, and the
  reversal record.
- For each lateral edge: both hosts are declared and the trust path is named.
- Explicit negatives: rungs that were blocked or not applicable.

Kaisha's output feeds shukaku (what depth would reach), kage (what a detection
would see), and the war report's impact section. A rung without reversal
evidence is an open finding, not a completed step.

## fleet

```bash
spydermonkey.py fleet --goal "map the depth below the foothold" --agents kaisha
# engine brief: kaisha rungs --target <target>
```

Kaisha runs after 3AM/undercroft produce a confirmed foothold and before
shukaku values the impact or kage writes detection for the depth path.

## failure

| Symptom | Correct response |
|---|---|
| No confirmed access | Stop. Return to 3AM/undercroft; do not invent a foothold. |
| Host is undeclared | Document the trust edge as an observation; do not traverse it. |
| Rung is blocked | Record the negative and move to the next documented rung. |
| Reversal evidence missing | Treat the rung as incomplete; do not report depth as achieved. |
| Lateral path reaches a third party | Stop at the boundary; note it for the disclosure map. |
| Engine missing | `spydermonkey.py doctor`; do not simulate rungs manually. |

Depth is proven by reversible, documented reach — not by how far an uncontrolled
session happened to wander.
