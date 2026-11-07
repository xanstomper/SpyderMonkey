# MODULE 1 — PROCESS & MEMORY TRADECRAFT

- source canon: `holyshit-mode/detection-evasion-modules.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
