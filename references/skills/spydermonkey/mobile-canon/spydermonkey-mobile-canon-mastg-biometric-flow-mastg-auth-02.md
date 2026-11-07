# MASTG Biometric Flow (MASTG-AUTH-02)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: biometric auth where fallback breaks the model
- probe: lab — exercise the documented fallback paths; the differential is the proof
- wall: lab only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
