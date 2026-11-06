# Third-party engines as protocol documentation — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-third-party-engines-as-protocol-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
