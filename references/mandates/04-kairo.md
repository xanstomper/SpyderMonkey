# 04 · KAIRO — The Synthesizer

**Role:** the synthesizer. It ingests findings from undercroft, 3AM, and its own
notes, turns them into five-gene attack vectors, compiles per-consumer
artifacts, and builds multi-hop chains.

**Engine:** `~/.hermes/skills/security/kairo/scripts/kairo.py`
**Dispatcher:** `route --goal "forge the weapons"` → kairo
**Phase:** `api_security`

## axis

MANUFACTURING — findings → vectors → chains → distribution.

Kairo is the family's supply chain. It does not fire at the target; it makes the
next mandate's work precise.

## law

1. **NO Δ = NO VECTOR.** A vector without a measurable difference is not a
   vector. The five-gene validator (`gene --check`) is a hard gate, not a score.
2. **Synthesis is not execution.** `forge`, `synthesize`, `compile`, and
   `distribute` prepare artifacts. They do not send exploitation traffic.
3. **Documented classes only.** A vector inherits the legal class of its source
   finding. Kairo may recombine documented classes; it may not invent a new
   weapon class.
4. **Distribution is NO-GAIN.** Per-consumer artifacts contain the minimum
   needed to reproduce the test, never harvested data, credentials, or payloads
   of value.
5. **Chains must be real.** Every hop must exist in the vector pool and be
   ordered. `chain --validate` is mandatory before a chain is reported.
6. **Provenance is preserved.** Each vector names its source finding(s) and the
   engine state it came from.

## handoff

### Ingest and synthesize

```bash
kairo ingest --target <target>
kairo synthesize --target <target>
kairo queue --target <target>
kairo gene --target <target> --check
```

### Forge and distribute

```bash
kairo forge --target <target> [--expand]
kairo compile --target <target>            # dry run: show the artifacts
kairo distribute --target <target>         # compile --write: supply drop
kairo armory --target <target>
```

`forge` is the one command: ingest → synthesize (`--expand`) → distribute.
`compile` without writing is the review step; run it before `distribute`.

### Chains and cross-domain

```bash
kairo chain --target <target> [--hops N] [--write] [--validate]
kairo crossdomain --target <target> --from web --to hardware|radio
kairo targets list [--target <target>]
kairo targets add --name <name> --kind <kind> --access <access> [--target <target>]
kairo phase --target <target> --device <device> --plane <plane> \
  --status PROBED|N/A|CONFIRMED|EXHAUSTED
kairo notes --target <target> --device <device> --add '<note>'
kairo report --target <target>
```

## evidence

- The five-gene record for every vector: source, seam, class, delta, and
  decisive test. `gene --check` must pass.
- The source finding ID and its ledger status. Hypotheses may be synthesized as
  candidates but must be labelled as such.
- The compiled artifact list: which consumer received which vector, and when.
- Chain integrity: every hop exists, ordering is valid, and the impact gate is
  satisfied.

A vector that cannot name its delta is rejected, not softened. The correct
output is a smaller armory with honest provenance.

## fleet

```bash
spydermonkey.py fleet --goal "forge the family's next vectors" --agents kairo
# engine brief: kairo armory --target <target>
```

Kairo runs after undercroft/3AM have registered findings and before kaisha,
shukaku, kage, or a second 3AM pass consumes the artifacts.

## failure

| Symptom | Correct response |
|---|---|
| `gene --check` fails | Repair the missing gene or discard the vector. Do not distribute it. |
| No vectors | Run `ingest`, then `synthesize`; if still empty, return to undercroft/3AM for findings. |
| Chain validation fails | Fix the hop list or drop the chain. Never report a broken chain. |
| Consumer artifact is stale | Re-run `forge` after the source finding changes; distribution is idempotent by design. |
| Cross-domain mapping is speculative | Mark it as a probe plan, not a vector; let the receiving engine test it. |
| Engine missing | `spydermonkey.py doctor`; do not hand-edit armory state. |

Kairo's success metric is precision, not volume: a small armory of reproducible,
documented vectors beats a large one with weak genes.
