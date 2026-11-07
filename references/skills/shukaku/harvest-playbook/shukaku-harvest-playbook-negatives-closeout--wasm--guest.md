# Negatives & closeout — wasm / guest

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-negatives-closeout.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **wasm** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- A finding with no data reach is EXCLUDED with the reason, not padded.
- The SHUKAKU report is the P5 impact layer: register + valuation summary +
  disclosure map + remediation prerequisites (what must happen before the
  organization can call the breach closed).
- Never move data, never copy, never threaten. The register IS the harvest.

## Probe adjustment (wasm × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
