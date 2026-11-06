# Passive DNS and historic-resolution

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-06

## The technique

Historic A/CNAME maps exposing retired hosts and takeover-prep (pairs with domtake canon). Decisive test: historic record vs live resolution — retired-but-referenced = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
