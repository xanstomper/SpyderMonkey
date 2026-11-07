# Discovery File and Directory Discovery (T1083)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-PATH** · **CWE-22** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `gobuster`, `ffuf`, `dirsearch`, `dirb`, `feroxbuster`, `wfuzz`, `dirhunt`
- chains: `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: locating sensitive files
- probe: the traversal battery (8 encodings) — the response body diff is the proof
- wall: read paths only; no deletion/modification probes

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
