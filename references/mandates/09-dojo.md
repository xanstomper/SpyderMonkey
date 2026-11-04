# 09 · DOJO — The Range

**Role:** the range. Dojo builds vulnerable replicas of every technique class,
strikes them to prove the flaw, and teaches the lesson: flaw → probe → detection.

**Engine:** `~/.hermes/skills/security/dojo/scripts/dojo.py`
**Dispatcher:** `route --goal "train on a replica"` → dojo
**Phase:** `reporting`

## axis

TRAINING — a safe place to prove the family's technique classes before they are
aimed at a declared estate.

Dojo is lab-bound by construction. It is how the family validates its own
tooling, its gates, and its detections without touching a client.

## law

1. **Loopback only.** Replicas bind 127.0.0.1. Dojo never exposes a vulnerable
   service on a public interface, a LAN interface, or a tunnel.
2. **Synthetic data only.** Replicas contain fabricated records. No real client
   data, credentials, or personal information is ever loaded into a lab.
3. **One class per replica.** `build --class <CLASS>` serves the documented flaw
   for that class. Do not turn a replica into a general-purpose target.
4. **Bench proves the flaw.** `bench --class <CLASS>` must report CONFIRMED. A
   replica that cannot be struck is not a training aid.
5. **Teach the defense.** `teach --class <CLASS>` pairs the flaw with its probe
   and its detection. Training without the detection half is incomplete.
6. **Self-terminate.** CI and shared hosts use `--serve-seconds`; no orphan
   listener is left behind.

## handoff

### Catalogue and build

```bash
dojo catalog
dojo build --class <CLASS> [--port <p>] [--serve-seconds <n>]
dojo bench --class <CLASS> [--port <p>]
dojo teach --class <CLASS>
dojo verify
```

### Use the range

```bash
# terminal 1 — a bounded replica
dojo build --class BOUNDARY --port 8801 --serve-seconds 60

# terminal 2 — prove the flaw
dojo bench --class BOUNDARY --port 8801

# pair the lesson with its detection
dojo teach --class BOUNDARY
```

For CI, keep the replica on loopback and let `--serve-seconds` terminate it.

## evidence

- The class catalogue entry and the documented flaw it represents.
- The replica's bind address: 127.0.0.1 and the chosen port.
- `bench` output: CONFIRMED, with the baseline/attack/diff shape.
- `teach` output: the probe and the matching detection lesson.
- `verify`: ALL PASS for the range's own self-check.

Dojo findings are **training evidence**. They validate the family's tooling and
detections; they are never reported as client findings.

## fleet

```bash
spydermonkey.py fleet --goal "train the family on a replica" --agents dojo
# engine brief: dojo catalog
```

Dojo runs before a live engagement (tool validation) and after a new technique
class is added (regression training). It is also the safe target for kage
`refire` when no client lab exists.

## failure

| Symptom | Correct response |
|---|---|
| Port already in use | Choose another port; never kill an unrelated listener. |
| Replica binds a non-loopback address | Stop it immediately and fix the bind. This is a wall violation. |
| `bench` does not confirm | Fix the replica or the probe; do not mark it as trained. |
| Class is unknown | Run `catalog`; do not invent a class name. |
| Orphan listener after a test | Use `--serve-seconds`; clean up only the replica you started. |
| Engine missing | `spydermonkey.py doctor`; do not stand up a random vulnerable app as a substitute. |

The range is successful when a technique can be taught, struck, detected, and
torn down without leaving the loopback boundary.
