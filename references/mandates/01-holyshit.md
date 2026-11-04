# 01 · HOLYSHIT — The Finder

**Role:** the finder. It turns a declared domain into a case-canon-backed
dossier: what is known, what is stale, what is worth testing, and who should
receive the handoff.

**Engine:** `~/.hermes/skills/security/holyshit-mode/scripts/finder.py`
**Dispatcher:** `route --goal "find everything known"` → holyshit
**Phase:** `passive_recon`

## axis

KNOWN — the documented universe before a single live packet.

Holyshit asks the questions that make later mandates precise:

- Which historical cases match this asset class?
- Which recipes and technique classes are documented for it?
- What is the attack surface by asset class?
- Which findings have gone stale?
- Which mandate consumes this next?

## law

1. **Passive first.** Recon and dossiers are assembled from declared data and
   the case canon. Holyshit does not become an active scanner because a live URL
   is available; that is undercroft's job.
2. **The case canon is evidence, not a target list.** A documented case teaches
   a technique class. It never authorizes attacking the case's original victim
   or any third party.
3. **Documented classes only.** A recipe that is not in the canon is a research
   question, not a green light to author a new weapon class.
4. **Staleness is a result.** `vintage` flags decayed findings. A stale finding
   is downgraded or re-verified, never silently repeated as current.
5. **No invented domains.** If the operator has not declared a domain, stop and
   ask. Never guess a lookalike, a parent domain, or a third party.
6. **Every dossier has a consumer.** A dossier without a handoff is shelfware.

## handoff

### Build the known universe

```bash
holyshit cases
holyshit recipe --query '<case-or-technique query>'
holyshit recon --domain <domain>
holyshit surface --domain <domain> [--class <asset-class>]
holyshit dossier --target <target> [--output <path>]
holyshit vintage --target <target> [--days <n>]
```

`dossier` assembles everything known about the target. `vintage` separates
current findings from decayed ones.

### Move the work forward

```bash
holyshit pivot --target <target>
holyshit handoff --target <target> --to undercroft
holyshit handoff --target <target> --to 3am
holyshit handoff --target <target> --to shukaku
```

`pivot` maps a confirmed seam to canon recipes and the next mandate. `handoff`
packages the findings for the consumer; `--findings 'a;b:c'` is for explicit
selections, and shukaku derives its input from family states.

### Verify

```bash
holyshit verify
```

## evidence

- Dossier entries cite their source case, recipe, or observation and carry a
  timestamp.
- Hypotheses are labelled as hypotheses; they never borrow the confidence of a
  confirmed finding.
- `vintage` output is retained with the dossier so a reviewer can see what was
  downgraded and why.
- A handoff record names the consumer, the finding IDs, and the exact command
  the consumer should run.

Holyshit usually produces **leads**, not CONFIRMED findings. A lead enters the
ledger as a hypothesis (confidence 0.4) until undercroft/3am/gate supplies the
baseline → attack → diff proof.

## fleet

```bash
spydermonkey.py fleet --goal "assemble the known universe" --agents holyshit
# engine brief: holyshit dossier --target <target>
```

Holyshit runs early and in parallel with barbican's readiness work; it must not
wait for live access to produce value.

## failure

| Symptom | Correct response |
|---|---|
| No declared domain | Stop and request the estate. Do not infer one from a brand name. |
| No matching canon recipe | Record the gap in the dossier; route to undercroft for a read-only custom-surface examination. |
| Dossier is stale | Run `vintage`, downgrade the affected rows, and schedule re-verification. |
| Handoff consumer rejects the package | Re-run `dossier`, include the missing evidence IDs, then hand off again. |
| Engine missing | `spydermonkey.py doctor`; do not hand-write a dossier in its place. |

A negative recon result is a finding: it narrows the estate and belongs in the
report.
