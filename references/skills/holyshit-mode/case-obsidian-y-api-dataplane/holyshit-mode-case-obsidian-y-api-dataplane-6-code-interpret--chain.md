# 6. Code-interpreter sandbox triage — `meituan/longcat-2.0` (NEGATIVE, good coverage) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-6-code-interpret.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Model executes Python but hardened jail:
- ALLOWED: `math, random, json, re, datetime, collections, itertools, functools, string, base64,
  hashlib, hmac, struct, codecs`. `print(2+2)`→4, list-comprehension works.
- BLOCKED: `os, sys, subprocess`, networking (`urllib, socket, requests`), fs (`open, pathlib`),
  `globals/locals/dir/__builtins__`, `getattr(__builtins__,...)` trickery, `__subclasses__()`
  class-hierarchy escape. The model itself narrates "blocked for security reasons."
- Each execution isolated — variables do NOT persist across turns (sandbox reset per call).
- Conclusion: "can execute code" ≠ sandbox escape. No host RCE. Escalation to host = would be
  Holy Shit; not found.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
