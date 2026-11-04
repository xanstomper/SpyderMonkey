# 06 · SHUKAKU — The Harvester

**Role:** the harvester. It catalogues what a confirmed finding *could* reach,
prices the impact on a defensible ladder, maps disclosure obligations, and feeds
the result back to the family — without taking anything.

**Engine:** `~/.hermes/skills/security/shukaku/scripts/shukaku.py`
**Dispatcher:** `route --goal "price what they could take"` → shukaku
**Phase:** `data_protection`

## axis

AFTER/GAIN — the impact layer: catalog, price, disclose, feed.

Shukaku answers the operator's real question after a confirmation: *what would
this have been worth, and who must be told?* It answers with counts, classes,
and evidence — never with contents.

## law

1. **NO-GAIN is literal.** Shukaku registers that a class of asset is reachable
   and how many records the proof touched. It never copies, downloads, stores,
   or transmits the contents.
2. **Confirmed findings only.** `ingest` requires a finding ID and a
   reproducible read-only proof reference. A hypothesis may be valued as a
   scenario but cannot become a crown entry.
3. **Crown entries need an evidence chain.** `crown --asset --class --scope
   --source` requires a scope statement (counts, not contents) and a source
   finding. No source, no crown.
4. **Valuation is a range with a basis.** Use `--value` and `--basis
   market-ladder|benchmark|disclosed-demand`; never present a single invented
   number as fact.
5. **Disclosure is an obligation, not an option.** `disclose` maps the trigger
   (PII-US, PII-EU, FIN, HEALTH, CONTRACT, RANSOM) to its timeline and
   prerequisites. The report names the obligation even when the operator dislikes
   it.
6. **Exclusion is explicit.** `exclude --finding <id> --reason <why>` is how a
   finding leaves the harvest path. Silent omission is not allowed.

## handoff

### Ingest and reason

```bash
shukaku ingest --target <target> --finding <id> --proof '<reproducible read-only ref>'
shukaku reason --target <target>
shukaku hunt --target <target> [--live <base-url>] [--cookie 'k=v'] \
  [--max <n>] [--dry-run]
```

`hunt` works hypotheses read-only. `--dry-run` is the default posture for a
plan; live probing is GET-only and scope-gated.

### Crown, exclude, disclose

```bash
shukaku crown --target <target> --asset <asset> --class PII \
  --scope '<counts, never contents>' --source <finding-id> \
  [--value '<range>'] [--basis market-ladder]
shukaku exclude --target <target> --finding <id> --reason '<why>'
shukaku disclose --target <target> --trigger PII-EU
shukaku disclose --target <target> --add '<obligation> · <timeline> · <prerequisite>'
shukaku ladder [--class PII]
```

### Feed the family and report

```bash
shukaku feed --target <target>
shukaku report --target <target>
shukaku verify
```

`feed` sends harvest hypotheses to 3AM, undercroft, and holyshit as *leads*,
not as confirmed data.

## evidence

- The source finding ID, its CONFIRMED status, and the proof reference.
- The crown entry's scope statement: counts and classes, never contents.
- The valuation range and its basis.
- The disclosure trigger, obligation, timeline, and prerequisite.
- The exclusion reason for anything deliberately left out.

Shukaku's report is the engagement's impact narrative. It must be defensible to
a client, a regulator, and a reviewer without exposing a single record.

## fleet

```bash
spydermonkey.py fleet --goal "value the confirmed impact" --agents shukaku
# engine brief: shukaku ladder
```

Shukaku runs after confirmed findings and kaisha depth, and before the final war
report and the closeout.

## failure

| Symptom | Correct response |
|---|---|
| Finding is not CONFIRMED | Keep it as a scenario; do not ingest or crown it. |
| Proof reference is missing | Return to the source engine and produce the read-only proof. |
| Asset scope cannot be counted safely | Use a conservative count and state the method; never sample contents. |
| Disclosure trigger is unclear | Record the uncertainty and consult the playbook; do not omit the obligation. |
| A finding is out of scope | `exclude` with the reason; do not silently drop it. |
| Engine missing | `spydermonkey.py doctor`; do not hand-write crown state. |

The harvest succeeds when the client can understand the impact without the
family ever holding the data.
