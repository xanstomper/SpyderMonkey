# Bridging the holyleadger into the spydermonkey control plane — mesh / machine

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-bridging-the-holyleadger-into-th.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mesh** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. `scope add --value` every asset the engagement covers — raw IPs and unregistered domains
   get ledger REFUSED until added; the refusal is the scope authority working, not a bug.
   **Parallel sessions CLOBBER the shared scope.json — it is a single-tenant file.** Another
   agent's `scope init` replaces the whole estate mid-engagement (your adds vanish, the
   engagement label changes, and ledger adds start refusing with "not in the declared
   estate" — that refusal is how you notice the clobber). Fix cooperatively: re-`scope add`
   YOUR estate onto the current file (append, never `--force` — a forced re-init breaks the
   OTHER session's gate), and point the campaign manifest's `engagement` field at whatever
   engagement now holds the estate. Never run `scope init` while any session may hold a live
   estate; `campaign init` inherits the engagement label from scope.json, so a mismatched
   label there is the clobber symptom.
2. `campaign init --target T`.
3. Convert holyleadger rows to `ledger add --title ... --class ... --asset ... --severity
   ... --proof "baseline: ... attack: ... diff: ..."`. No 3-gate shape → the machinery
   downgrades to hypothesis (correct — let it). Dedupe attaches evidence to existing rows;
   don't fight it.
4. `ledger triage` → `chain detect` → `coverage` → `mission --skip-fleet` → `report`.
5. kairo: seed `~/.redteam/campaigns/<t>/undercroft-state.json` groups `code`/`surface`/
   `logic` (entries: seam · where · status · proof · **asset** — missing `asset` crashes
   undercroft's report with KeyError) → `ingest` → `synthesize` → `distribute`. `notes`
   needs a registered device first (`targets add --name X --kind other --access none`).
   `--expand` is a `forge` flag, not `synthesize`.
6. kage `mirror --target T` after new confirmed rows; `export --dir <campaign>/kage-rules`.

## Probe adjustment (mesh × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
