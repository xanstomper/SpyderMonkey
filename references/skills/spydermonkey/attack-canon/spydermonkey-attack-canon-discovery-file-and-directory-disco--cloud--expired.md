# Discovery File and Directory Discovery (T1083) — cloud / expired

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-discovery-file-and-directory-disco.md`
- bindings: **WSTG-PATH** · **CWE-22** · **ATT&CK T1005**
- context: **cloud** · auth **expired** · chain role **pivot**

## Route

- probes: `gobuster`, `ffuf`, `dirsearch`, `dirb`, `feroxbuster`, `wfuzz`, `dirhunt`
- chains: `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- class: locating sensitive files
- probe: the traversal battery (8 encodings) — the response body diff is the proof
- wall: read paths only; no deletion/modification probes

## Probe adjustment (cloud × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
