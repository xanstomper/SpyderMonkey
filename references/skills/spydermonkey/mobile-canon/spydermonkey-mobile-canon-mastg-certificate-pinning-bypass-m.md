# MASTG Certificate Pinning Bypass (MASTG-NETWORK-02)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: pinning that can be bypassed at runtime (frida/objection)
- probe: LAB DEVICE — attempt the documented runtime bypass, prove traffic visibility
- wall: lab device + lab cert only; never against a device the scope doesn't own

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
