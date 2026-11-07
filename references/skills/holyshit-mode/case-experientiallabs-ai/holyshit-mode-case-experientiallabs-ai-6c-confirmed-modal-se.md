# 6c. CONFIRMED — Modal serverless GPU endpoint leak in catalog (score 45)

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Staging catalog exposes a **Modal endpoint**: `hy4-preview` →
  `https://bespoke-ai-agents--explabs-ec-hy4-preview-hy4preview.us-east.modal.direct/v1`.
- Currently **scale-to-zero** (503 `no upstreams available` → no live container). If it wakes with open
  auth it's a free-GPU surface; Modal functions usually have web-auth unless misconfigured.
- **IMPACT:** Internal serving infra URL disclosed in the public keyless catalog; potential free-GPU if
  the function is authless. Recon primarily.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
