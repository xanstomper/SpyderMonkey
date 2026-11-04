# MODULE 1 — PROCESS & MEMORY TRADECRAFT — chain composition

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-1-process-mem.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
