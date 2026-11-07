# Deserialization gadget DNS-ping

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The safe proof of a deserialization class is a DNS-only gadget (no command execution). Decisive test: serialized payload whose gadget list ends in a DNS resolution to your domain — the lookup arrival is the finding. Execution gadgets are REPORTED as the class, never fired.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
