# MASTG Runtime Detection Evasion (MASTG-RESILIENCE) — worker / expired

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-runtime-detection-evasion-ma.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **worker** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- class: root/jailbreak/frida detection in the app
- probe: LAB — document which detectors fire; the bypass is proof of weakness, not a foothold
- wall: lab only; no distribution of bypass tooling

## Probe adjustment (worker × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
