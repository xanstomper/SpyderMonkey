# 02 · UNDERCROFT — The Descent

**Role:** the descent into the target's own custom surface — bundles, routes,
JWTs, business logic, boundary objects, and state transitions. It converts an
unknown application into a registered, prioritized seam list.

**Engine:** `~/.hermes/skills/security/undercroft/scripts/undercroft.py`
**Dispatcher:** `route --goal "their custom code"` → undercroft
**Phase:** `active_recon`

## axis

UNKNOWN — the parts of the estate that no public case canon describes.

Undercroft is where the family stops reading about the target and starts
examining the target's own skin. It stays read-only by default and registers
seams for other mandates to prove.

## law

1. **Read-only by default.** `run`, `scan`, `map`, `descend`, `jwt`, `probe`,
   `fuzz`, `stateflow`, `replay`, `precision`, `entropy`, and `corpus` are
   observation and planning tools. They do not exploit, mutate, or exfiltrate.
2. **GET-only live probing unless a documented safe method is explicitly
   required.** `--cookie` is the operator's own session, never a stolen one.
   `--header` is for declared headers, not identity spoofing.
3. **Boundary probes use own IDs.** `--boundary-url` with `{id}` and
   `--probe-ids` exist to test whether the application enforces ownership on
   objects the operator already owns. Swapping in a foreign ID is a separate,
   explicitly authorized test with its own proof.
4. **No brute force.** A 401/403/WAF response is a result. Record it, drift it,
   and move on; do not turn a validation into a credential-stuffing run.
5. **One seam, one registered row.** Every candidate gets a class, an asset,
   and a plan. Untracked "maybe" observations are not findings.
6. **NO-GAIN.** Nothing of value is retained. A bundle or response is inspected
   for structure, not harvested for secrets.

## handoff

### Full read-only engagement

```bash
undercroft run --target <target> --domain <domain> \
  [--url <base-url>] [--bundle <path>] [--cookie 'k=v'] \
  [--header 'K: V'] [--boundary-url '<url-with-{id}>'] \
  [--probe-ids <own-ids>] [--max-routes <n>]
```

### Focused descent

```bash
undercroft scan --path <bundle-or-source> [--target <target>]
undercroft map --domain <domain>            # e-commerce|fintech|saas|…
undercroft descend --target <target> --domain <domain> [--path <bundle>]
undercroft jwt --token <token>
undercroft probe [--class <SEAM_CLASS>]
undercroft fuzz --base <url> [--methods GET,POST]
undercroft stateflow --states '<a,b,c>' [--guard '<state:prereq>'] [--target <target>]
undercroft replay --url <url> [--method <M>] [--times <n>] [--target <target>]
undercroft precision --price <n> --rate <n> [--mode floor|trunc|round]
undercroft entropy [--samples '<tokens>'] [--file <path>]
undercroft corpus --type money|int|string|json|date
```

### Register and prioritize

```bash
undercroft surface --target <target> --add <route> \
  --kind hidden|misused|legacy|admin --status PROBED|CONFIRMED|EXHAUSTED [--proof '<ref>']
undercroft prioritize --target <target>
undercroft drift --target <target> [--days <n>]
undercroft report --target <target>
undercroft export --target <target>
```

`export` feeds kairo/3AM; it is a handoff artifact, not an execution.

## evidence

A seam becomes a ledger finding only with the family proof shape:

```text
baseline: <request> -> <status/body observation>
attack:   <changed request> -> <status/body observation>
diff:     <the measurable difference that proves the class>
```

Keep the raw request/response pair, the timestamp, and the scope decision. A
suspicious route with no differential is a **hypothesis** (0.4), not a
CONFIRMED finding. `drift` exists to re-verify previously confirmed seams before
they are re-asserted.

## fleet

```bash
spydermonkey.py fleet --goal "descend into the custom surface" --agents undercroft
# engine brief: undercroft probe
```

Undercroft's fleet brief is intentionally NO-GAIN: it produces the probe plan,
not live exploitation.

## failure

| Symptom | Correct response |
|---|---|
| No live URL | Run the static path: `scan` / `descend` over the bundle or source. |
| 401 / 403 / WAF | Record the negative with status and timestamp; do not brute force. |
| JWT is opaque | Record it as an observation; do not attempt to crack it. |
| Bundle is minified beyond reading | Use `scan` for seams and `fuzz` for route candidates; document the limitation. |
| A seam cannot be proven read-only | Stop at the hypothesis and hand it to 3am with the exact missing proof. |
| Engine missing | `spydermonkey.py doctor`; do not substitute a generic scanner. |

The descent is successful when the seam list is honest, prioritized, and
reproducible — not when it produces a dramatic finding.
