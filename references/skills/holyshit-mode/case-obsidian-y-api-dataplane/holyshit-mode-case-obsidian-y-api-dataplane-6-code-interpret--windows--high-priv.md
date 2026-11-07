# 6. Code-interpreter sandbox triage — `meituan/longcat-2.0` (NEGATIVE, good coverage) — windows / high-priv

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-6-code-interpret.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **windows** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Model executes Python but hardened jail:
- ALLOWED: `math, random, json, re, datetime, collections, itertools, functools, string, base64,
  hashlib, hmac, struct, codecs`. `print(2+2)`→4, list-comprehension works.
- BLOCKED: `os, sys, subprocess`, networking (`urllib, socket, requests`), fs (`open, pathlib`),
  `globals/locals/dir/__builtins__`, `getattr(__builtins__,...)` trickery, `__subclasses__()`
  class-hierarchy escape. The model itself narrates "blocked for security reasons."
- Each execution isolated — variables do NOT persist across turns (sandbox reset per call).
- Conclusion: "can execute code" ≠ sandbox escape. No host RCE. Escalation to host = would be
  Holy Shit; not found.

## Probe adjustment (windows × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
