# NTLM relay classes (documented mechanisms)

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

SMB signing absent / channel-binding gaps — the CONFIG posture (signing required?) is the read-only finding; the relay is never executed. Decisive test: SMB negotiation flags — the flag absence is the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
