# WSTG Error Handling (WSTG-ERRH) — cloud / low-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-wstg-error-handling-wstg-errh.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **cloud** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: stack traces, debug output leaking through errors
- probe: malformed inputs forcing 500s; harvest the trace for class crowns
- wall: read-only

## Probe adjustment (cloud × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
