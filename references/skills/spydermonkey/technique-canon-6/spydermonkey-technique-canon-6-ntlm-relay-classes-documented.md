# NTLM relay classes (documented mechanisms)

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

SMB signing absent / channel-binding gaps — the CONFIG posture (signing required?) is the read-only finding; the relay is never executed. Decisive test: SMB negotiation flags — the flag absence is the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
