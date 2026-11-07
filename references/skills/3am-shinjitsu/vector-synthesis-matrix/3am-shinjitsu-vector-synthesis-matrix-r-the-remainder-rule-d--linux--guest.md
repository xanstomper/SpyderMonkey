# §R — the remainder rule (derive any unlisted pair) — linux / guest

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-r-the-remainder-rule-d.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **linux** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Pair (F, S) not in the table → derive mechanically, 60 seconds:

1. Take F's canonical primitive shape (flaw-family key).
2. Substitute S's boundary as the attacker-controlled input position (seam key).
3. Write the one-liner: `[primitive shape] at [seam's input position]`.
4. Score §14. ≥60 → run; else ledger as rejected-with-reason.

Derivation example: (3 Type-coercion × H Multi-host) → "send the object-where-string
payload to the mirror host's twin endpoint, where the validator is one version older" —
this is exactly how the g***REDACTED*** mirrors got probed.

## Probe adjustment (linux × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
