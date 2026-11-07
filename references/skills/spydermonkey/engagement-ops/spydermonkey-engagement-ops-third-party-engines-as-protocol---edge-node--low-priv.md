# Third-party engines as protocol documentation — edge-node / low-priv

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-third-party-engines-as-protocol-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **edge-node** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`gh search code "<target socket/API host>"` (authed `gh`) surfaces production-grade
third-party engines built on the target's protocol. They are: (1) an independent
implementation of the wire format you are reversing — treat their transport docs as a
cross-check on namespace names, sign chains, and forced-transport behavior; (2) an EV
corroborator — if their own strategy layer pegs break-even at the fair odds (e.g. 0.7692
for 1.30×) and gates on fair+edge, they have no predictive edge, which independently
confirms your 0/N decisive-negative; (3) a reportable automation signal — a public
prediction engine + in-page observer (Tampermonkey posting round telemetry to a remote
worker) operating against the target is an anti-automation/ToS finding for the target's
report. Always scan the repo for committed credentials (env-driven config = clean, not a
leak), and check their deployed endpoints — a withdrawn worker (404 `Application not
found`) means the operation folded, which is fine: the remaining repo is still protocol
intel. Register with the IN-ESTATE asset (the ledger estate gate refuses out-of-estate
assets, rc=1) and put the third-party repo identity in the title/proof with explicit
"NOT target infra" attribution.

## Probe adjustment (edge-node × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
