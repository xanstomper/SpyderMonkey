# SSTI detection arithmetic (jinja/smarty/twig)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-INPV** · **CWE-1336** · **ATT&CK T1059**
- generated: 2026-11-06

## The technique

{{7*7}} → 49 is the arithmetic marker; engine fingerprint follows ({{7*'7'}} → 7777777 = jinja2). Decisive test: the arithmetic marker reflected — class confirmed; template execution beyond arithmetic is RCE-class and is REPORTED, not executed (no-gain).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
