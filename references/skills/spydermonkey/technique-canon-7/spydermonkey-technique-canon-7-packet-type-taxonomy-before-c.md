# Packet-type taxonomy before conclusions

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Connect-ack vs data-gate vs event-layer — misread packets manufactured the SPY-053 refutation. Rule: characterize the ack taxonomy FIRST, then interpret gates. Decisive test: the ack map itself — every gate claim cites its packet type.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
