# 5. CONFIRMED — GPU fleet internals leak keyless on `clef.xplabs.ai` (score 35)

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `GET https://clef.xplabs.ai/health` → 200 `{"status":"ok","max_length":65536,"queued":0,
  "gpu_allocated_gib":29.46,"gpu_peak_gib":36.76,...}` — no auth.
- **IMPACT:** Infra/GPU-fleet capacity disclosure.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
