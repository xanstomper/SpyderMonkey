# MODULE 1 — PROCESS & MEMORY TRADECRAFT — wasm / hardened

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-1-process-mem.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **wasm** · auth **hardened** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

**Objective**: validate EDR/AV detection of in-memory techniques.

**Techniques**:
- **In-memory payload delivery**: reflective DLL injection, process hollowing, APCLoad
  on operator lab hosts. Validate: does EDR flag memory anomalies (RWX pages, unbacked
  regions) or only file-system IOCs?
- **Syscall direct invocation**: bypass userland hooks via direct syscalls (Hell's Gate
  class) on Windows lab; `syscall` inline on Linux lab. Validate: does ETW catch the
  syscall pattern or only the API call?
- **AMSI/ETW patching**: patch AMSI or ETW in a lab process, execute known-bad payload.
  Validate: does the EDR still catch the payload via kernel callback or behavioral chain?
- **Process herpaderping**: write payload, map, modify on-disk, execute — validate
  hash-mismatch detection.

**Detection surface to report**: EDR memory scanning, ETW-TI (threat intelligence) events,
kernel callbacks, behavioral chains, AMSI integration.

---

## Probe adjustment (wasm × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
