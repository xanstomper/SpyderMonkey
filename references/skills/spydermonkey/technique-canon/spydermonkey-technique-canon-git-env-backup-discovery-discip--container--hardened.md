# .git /.env /backup discovery discipline — container / hardened

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-git-env-backup-discovery-discip.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **container** · auth **hardened** · chain role **entry**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Distinguish SPA-fallback 200 shells from REAL exposure: require content distinct from the canonical nonexistent-path control (size/content-type delta). Decisive test: control path vs candidate path — identical shell = exhausted, different = the finding.

## Probe adjustment (container × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
