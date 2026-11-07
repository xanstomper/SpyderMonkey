# Verification — worker / guest

- source canon: `holyshit-mode/engagement-report-pattern.md`
- base technique: `holyshit-mode-engagement-report-pattern-verification.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

`report` is verified (a) in-module with an isolated temp ledger seeded with mixed
confirmed/hypothesis/negative + one chain, asserting: rc 0, all six sections present,
score-desc ordering, accurate counts line, chain steps + impact rendered, `--out` writes
a file; and (b) as a subprocess CLI (`holyleadger.py report --target --out`) writing to an
isolated dir. The CI workflow's ledger smoke step ALSO runs `report` and greps for the
"Confirmed Holy Shits" section + a known class name, so a broken report fails the build.

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
