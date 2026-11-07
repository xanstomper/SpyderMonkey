# 1. Mine the operator's documented scheme first — browser / guest

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-1-mine-the-operator.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **browser** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Search their blog/help-center for the PF explainer. Extract: seed model (server/client
seed, nonce), commitment pattern (commit-and-reveal, hash chain), consumption order
(forward chain vs reverse chain), and the published anchor ("final hash published before
play"). This defines exactly what the public wire must show for the claim to hold.

## Probe adjustment (browser × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
