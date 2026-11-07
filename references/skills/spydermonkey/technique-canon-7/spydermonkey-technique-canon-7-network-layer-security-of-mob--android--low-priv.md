# Network-layer security of mobile APIs — android / low-priv

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-network-layer-security-of-mob.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **android** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

APIs accepting TLS-stripped traffic, ignoring cert errors, or trusting user CAs in release builds. Decisive test: your build's traffic through a local CA — accepted = the class (MASTG-NET).

## Probe adjustment (android × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
