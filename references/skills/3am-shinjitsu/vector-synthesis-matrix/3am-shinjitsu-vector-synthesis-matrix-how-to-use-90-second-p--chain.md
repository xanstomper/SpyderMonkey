# How to use (90-second protocol) — chain composition

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-how-to-use-90-second-p.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Note the target's **flaw families** (from era-stack, framework signatures, design
   reading — §9 ladder rungs 1–2) and **trust seams** (observed trust boundaries).
2. Cross them against the matrix rows: matching row → score §14 → run the decisive
   one-liner. Unlisted pairs → apply the remainder rule (§R) to derive the probe.
3. Every run goes to `exploit_intel.synthesis_queue[]`; every negative is ledgered with
   its exact test (anti-loop canon).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
